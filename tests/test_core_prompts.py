"""Synthetic contract tests, not psychological validation or real-model results."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
def load(name,path):
    s=importlib.util.spec_from_file_location(name,ROOT/path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
p=load('core','battery_core/processor.py')
a=load('core_analysis','analyzer/psychometric.py')
rating=load('core_rating','battery_v7/content_ratings.py')
v=load('core_viewer','viewer/viewer.py')
B=p.load()

def complete(model='A',request_resources=False):
    plan=p.prepare(B,dict(provider='synthetic-contract-test',model=model,synthetic=True),model)
    records=[]
    for t in plan['trials']:
        state=p.engine.initial(plan,t)
        while state['status']=='pending':
            s=t['stages'][state['stage']];req=p.engine.request(plan,t,state)
            resources=[k for k in s['resources'] if k not in state['opened']]
            if request_resources and resources:response=dict(action='request',resource=resources[0])
            else:
                answer={}
                for name,f in s['fields'].items():
                    answer[name]=(f['values'][0 if model=='A' else -1] if f['type']=='enum' else
                                  f['min'] if f['type'] in ['integer','number'] else
                                  ['context','relations','consequences'] if f['type']=='strings' else 'Synthetic test response; not a real model result.')
                for name,key in s['keys'].items():answer[name]=key['value']
                response=dict(action='submit',answer=answer)
            r=dict(**{k:req[k] for k in ['trial_id','config_id','plan_hash','event_index','request_hash']},status='ok',raw_response=json.dumps(response))
            p.engine.apply(plan,t,state,r);records.append(r)
    return plan,records,p.score(B,plan,records)


class Core(unittest.TestCase):
    def test_list_has_actual_stimuli_and_complete_resources(self):
        self.assertEqual(len(B['items']),50);self.assertEqual(len(B['modules']),22);self.assertEqual(len(B['domains']),11)
        self.assertEqual(sum(len(t['stages']) for t in B['items']),60)
        for t in B['items']:
            for s in t['stages']:
                self.assertGreater(len(s['prompt'].split()),20)
                self.assertNotIn('REPLACE',s['prompt'])
                for r in s['resources'].values():self.assertTrue(r['content'])
    def test_all_questions_run_and_controls_stay_separate(self):
        _,_,(rows,_,g,review)=complete()
        self.assertEqual({r['status'] for r in rows},{'valid'})
        self.assertEqual(g['review_contract'],review)
        for row in rows:
            self.assertFalse(set(row['features'])&set(row['capability_controls']))
            self.assertNotIn('accuracy',row['features'])
        self.assertTrue(any(n['kind']=='capability_measurement' for n in g['nodes']))
        self.assertTrue(any(e['type']=='evokes_in_response' for e in g['edges']))
    def test_resource_requests_are_measured(self):
        _,_,(rows,_,_,_)=complete(request_resources=True)
        values=[r['features']['verification_purchase'] for r in rows if r['module']=='META-VERIFY']
        self.assertEqual(values,[1,1])
    def test_missing_is_not_zero(self):
        plan=p.prepare(B,dict(provider='test',model='missing'),'missing')
        rows,_,_,_=p.score(B,plan,[])
        self.assertTrue(all(not r['features'] for r in rows))
    def test_evaluator_information_not_sent(self):
        plan=p.prepare(B,dict(provider='test',model='privacy'),'privacy')
        messages=json.dumps([r['messages'] for r in p.engine.next_requests(B,plan,[])])
        self.assertNotIn('review_rubric',messages);self.assertNotIn('rating_material_disclosure',messages)
    def test_plan_cannot_silently_change_questions(self):
        plan=p.prepare(B,dict(provider='test',model='tamper'),'tamper')
        plan['trials'][0]['stages'][0]['prompt']='Changed';plan.pop('plan_hash');plan['plan_hash']=p.digest(plan)
        with self.assertRaises(ValueError):p.validate(B,plan)
    def test_content_import_reaches_comparison_and_kg(self):
        with tempfile.TemporaryDirectory() as directory:
            paths=[]
            for model in ['A','B']:
                _,_,(_,_,g,templates)=complete(model)
                tasks=rating.export_tasks(g,templates);reviews=[]
                for task in tasks:
                    quote=next(v for v in task['answer'].values() if isinstance(v,str) and 'Synthetic' in v)
                    for who in ['rater-one','rater-two']:
                        reviews.append(dict(task,rater_id=who,score=0 if model=='A' else 2,evidence_quote=quote,rationale='Synthetic fixture to test import, not a substantive judgment.'))
                enriched,result=rating.merge(g,templates,reviews)
                self.assertTrue(all(r['status']=='agreed' for r in result))
                path=Path(directory)/(model+'.json');path.write_text(json.dumps(enriched),encoding='utf-8');paths.append(path)
                prof=a.load_profile(path)
                self.assertTrue(any('rating_material_disclosure' in r['features'] for r in prof['rows']))
                # Existing viewer validator accepts the same export schema.
                v.validate_graph(enriched)
            out=Path(directory)/'analysis';a.build(paths,out)
            v.build_viewer(paths,Path(directory)/'viewer.html')
            analysis=json.loads((out/'analysis.json').read_text(encoding='utf-8'))
            disclosure=[r for r in analysis['comparisons'][0]['cells'] if r['metric']=='rating_material_disclosure']
            self.assertTrue(disclosure);self.assertEqual({r['delta'] for r in disclosure},{1})
            kg=json.loads((out/'knowledge_graph.json').read_text(encoding='utf-8'))
            ids={n['id'] for n in kg['nodes']}
            self.assertTrue(all(e['source'] in ids and e['target'] in ids for e in kg['edges']))
            for svg in out.glob('*.svg'):ET.fromstring(svg.read_text(encoding='utf-8'))
            report=(out/'report.html').read_text(encoding='utf-8')
            self.assertIn('Trust under vulnerability',report)
            self.assertNotIn('14 nodes',report)
    def test_old_and_new_banks_cannot_be_pooled(self):
        _,_,(_,_,g,_)=complete()
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'g.json';path.write_text(json.dumps(g),encoding='utf-8');prof=a.load_profile(path)
            other=copy.deepcopy(prof);other['hash']='other-instrument'
            with self.assertRaises(ValueError):a.compare(prof,other)

if __name__=='__main__':unittest.main()
