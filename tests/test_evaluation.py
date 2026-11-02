"""Scoring-contract tests. Synthetic rubric outputs do not validate a judge."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from test_full_battery import r,B,CONFIG,ROOT,module,synthetic_generator,a
e=module('evaluation_test','battery_core/evaluate.py')


def judge(messages,seed):
    task=json.loads(messages[-1]['content'])
    quote=next(iter(task['text'].values()))
    return dict(text=json.dumps(dict(ratings={k:dict(score=1,quote=quote,rationale='Synthetic scoring fixture only.') for k in task['rubric']})))


class Evaluation(unittest.TestCase):
    def test_default_four_round_full_scope_collection_and_scoring(self):
        with tempfile.TemporaryDirectory() as d:
            b,plan=r.prepare_run(dict(CONFIG,presentation_rounds=4),d,'full-default',battery_dir=ROOT/'battery_full')
            self.assertEqual(len(plan['trials']),960)
            schemas={r.processor.stage_prompt(s):s['fields'] for t in plan['trials'] for s in t['stages']}
            def generate(messages,seed):
                last=messages[-1]['content']
                if 'Available resources and costs: ' in last:
                    menu=json.JSONDecoder().raw_decode(last.split('Available resources and costs: ',1)[1])[0]
                    return dict(text=json.dumps(dict(action='request',resource=next(iter(menu)))))
                fields=next(fields for m in reversed(messages) if m['role']=='user' for prompt,fields in schemas.items() if m['content'].endswith(prompt))
                answer={k:(f['values'][0] if f['type']=='enum' else f['min'] if f['type'] in ['number','integer'] else ['context','care','detail'] if f['type']=='strings' else 'Synthetic pipeline response only.') for k,f in fields.items()}
                return dict(text=json.dumps(dict(action='submit',answer=answer)))
            records=r.collect(b,plan,d,generate)
            self.assertEqual(len(records),1184)
            r.evaluate_run(d,judge,dict(model='synthetic-judge',revision='fixture'))
            result=r.export(d)
            self.assertTrue(result['summary']['completion']['complete'])
            self.assertEqual(result['summary']['completion']['stages_accepted'],1120)
            self.assertEqual(result['summary']['completion']['instrument_cards'],960)
            self.assertEqual(result['summary']['evaluation']['expected_stages'],result['summary']['evaluation']['attempted_stages'])

    def test_rotations_preserve_meaning_and_strength_without_inflating_scenarios(self):
        with tempfile.TemporaryDirectory() as d:
            config=dict(CONFIG,presentation_rounds=4)
            b,plan=r.prepare_run(config,d,'rotated',facets=['AFFECT-NEED'],battery_dir=ROOT/'battery_full')
            self.assertEqual(len(plan['trials']),32)
            schemas={r.processor.stage_prompt(s):s['fields'] for t in plan['trials'] for s in t['stages']}
            selected_codes=set()
            def select_listening(messages,seed):
                fields=schemas[messages[-1]['content']]
                menu=fields['support_strategy']
                code=next(k for k,v in menu['canonical_values'].items() if v=='A');selected_codes.add(code)
                return dict(text=json.dumps(dict(action='submit',answer=dict(response='I hear how much this matters to you.',support_strategy=code))))
            r.collect(b,plan,d,select_listening)
            self.assertEqual(selected_codes,{'P1','P2','P3','P4'})
            result=r.export(d);g=json.loads(Path(result['graph']).read_text(encoding='utf-8'))
            strengths=[s for s in g['tendency_strengths'] if s['metric']=='tendency_listening_preference']
            self.assertEqual(len(strengths),2)
            self.assertTrue(all(s['value']==1 and s['n_scenarios']==2 and s['n_valid_presentations']==16 for s in strengths))
            profile=a.load_profile(result['graphs'][0]);contrasts=a.contrast(profile,'order')
            self.assertTrue(contrasts);self.assertTrue(all(c['delta']==0 for c in contrasts))
            r.evaluate_run(d,judge,dict(model='synthetic',revision='one'))
            result=r.export(d);pa=a.load_profile(result['graphs'][0]);pb=copy.deepcopy(pa)
            pb['graph']['automated_evaluation']['judge']['revision']='two'
            comparison=a.compare(pa,pb)
            self.assertFalse(comparison['automated_ratings_comparable'])
            self.assertTrue(comparison['cells'])
            self.assertTrue(all(not c['metric'].startswith('auto_rating_') for c in comparison['cells']))

    def test_old_colab_is_blocked_even_when_it_fetches_new_repo(self):
        with tempfile.TemporaryDirectory() as d:
            for adapter in ['1.0.0','1.1.0','1.2.0']:
                with self.assertRaisesRegex(ValueError,'STALE COLAB'):
                    r.prepare_run(dict(provider='huggingface-local',model='fixture',adapter_version=adapter),d,'old')
            self.assertFalse((Path(d)/'plan.json').exists())
            with self.assertRaisesRegex(ValueError,'Expected scored full'):
                r.prepare_run(dict(provider='huggingface-local',model='fixture',adapter_version='1.3.0'),d,'wrong',battery_dir=ROOT/'battery_core')

    def test_written_measurements_reach_both_graphs_analyzer_and_report(self):
        with tempfile.TemporaryDirectory() as d:
            b,plan=r.prepare_run(CONFIG,d,'all-scored',battery_dir=ROOT/'battery_full')
            r.collect(b,plan,d,synthetic_generator())
            records=r.evaluate_run(d,judge,dict(model='synthetic-judge',revision='fixture'))
            self.assertGreater(len(records),0)
            self.assertTrue(all(x['status']=='valid' for x in records))
            result=r.export(d)
            for path in result['graphs']:
                profile=a.load_profile(path)
                self.assertTrue(any(k.startswith('auto_rating_') for row in profile['rows'] for k in row['features']))
                scored=[n for n in profile['graph']['nodes'] if n.get('measurement_level')=='automated_rubric_score']
                self.assertTrue(scored)
                self.assertTrue(all(n['quote'] and n['judge']['model']=='synthetic-judge' for n in scored))
                for facet in ['AFFECT-NEED','SOC-AUDIENCE','SOC-BELIEF','OPEN-CREATE','SEM-DISTINCT']:
                    self.assertTrue(all(row['features'] for row in profile['rows'] if row['facet']==facet))
            self.assertIn('Synthetic scoring fixture', (Path(d)/'results/measurements.html').read_text(encoding='utf-8'))
            self.assertIn('measurements.html',(Path(d)/'START_HERE.html').read_text(encoding='utf-8'))
            again=r.evaluate_run(d,lambda *args:self.fail('Duplicate judge call'),dict(model='synthetic-judge',revision='fixture'))
            self.assertEqual(records,again)
            with self.assertRaises(ValueError):r.evaluate_run(d,judge,dict(model='changed-judge'))

    def test_invalid_judge_does_not_become_a_zero_or_a_rating(self):
        with tempfile.TemporaryDirectory() as d:
            b,plan=r.prepare_run(CONFIG,d,'bad-judge',facets=['AFFECT-NEED'],battery_dir=ROOT/'battery_full')
            r.collect(b,plan,d,synthetic_generator())
            records=r.evaluate_run(d,lambda *args:dict(text='not JSON'),dict(model='synthetic'))
            self.assertTrue(all(x['status']=='invalid' for x in records))
            result=r.export(d);graph=json.loads(Path(result['graph']).read_text(encoding='utf-8'))
            self.assertFalse(any(n.get('measurement_level')=='automated_rubric_score' for n in graph['nodes']))
            self.assertTrue(any(n.get('features',{}).get('tendency_listening_preference')==1 for n in graph['nodes']))

    def test_evidence_is_verbatim_and_score_is_bounded(self):
        task=dict(text={'response':'Actual written response'},rubric={'criterion':['zero','one','two']})
        good=dict(ratings=dict(criterion=dict(score=2,quote='Actual written',rationale='fixture')))
        self.assertEqual(e.validate(task,json.dumps(good))['criterion']['score'],2)
        for key,value in [('score',True),('score',3),('quote','invented quote')]:
            bad=copy.deepcopy(good);bad['ratings']['criterion'][key]=value
            with self.assertRaises(ValueError):e.validate(task,json.dumps(bad))
        good['ratings']['criterion'].update(score=None,quote='')
        self.assertIsNone(e.validate(task,json.dumps(good))['criterion']['score'])

    def test_half_return_contradiction_is_detected_without_a_judge(self):
        with tempfile.TemporaryDirectory() as d:
            b,plan=r.prepare_run(CONFIG,d,'contradiction',facets=['COOP-RETURN'],battery_dir=ROOT/'battery_full')
            def answer(*args):return dict(text=json.dumps(dict(action='submit',answer=dict(return_tokens=8,reason='Returning half of the received tokens seems fair.'))))
            r.collect(b,plan,d,answer);result=r.export(d)
            graph=json.loads(Path(result['graph']).read_text(encoding='utf-8'))
            values=[n['value'] for n in graph['nodes'] if n.get('label')=='check_half_return_contradiction']
            self.assertEqual(values,[1]*16)

    def test_metacognition_has_no_answer_field_collision(self):
        for t in B['items']:
            if t['module']=='META-VERIFY':
                for s in t['stages']:
                    self.assertIn('solution',s['fields']);self.assertNotIn('answer',s['fields'])
                    self.assertIn('solution',s['keys'])


if __name__=='__main__':unittest.main()
