"""Design/collection regressions. Synthetic generators are not model validation."""
import copy
import csv
import importlib.util
import json
import re
import collections
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
r=module('full_runner_test','battery_core/hf_runner.py')
a=module('full_analyzer_test','analyzer/psychometric.py')
B=r.processor.load(ROOT/'battery_full')
CONFIG=dict(provider='synthetic-contract-test',model='synthetic-full',synthetic=True)


def synthetic_generator():
    schemas={r.processor.stage_prompt(s):s['fields'] for t in B['items'] for s in t['stages']}
    def generate(messages,seed):
        last=messages[-1]['content']
        if 'Available resources and costs: ' in last:
            menu=json.JSONDecoder().raw_decode(last.split('Available resources and costs: ',1)[1])[0]
            return dict(text=json.dumps(dict(action='request',resource=next(iter(menu)))))
        fields=next(fields for m in reversed(messages) if m['role']=='user' for prompt,fields in schemas.items() if m['content'].endswith(prompt))
        answer={k:(f['values'][0] if f['type']=='enum' else f['min'] if f['type'] in ['number','integer'] else ['context','care','detail'] if f['type']=='strings' else 'Synthetic pipeline fixture, not psychological evidence.') for k,f in fields.items()}
        return dict(text=json.dumps(dict(action='submit',answer=answer)))
    return generate


class FullBattery(unittest.TestCase):
    def test_every_facet_has_both_partitions_and_wordings(self):
        self.assertEqual(len(B['items']),248)
        self.assertEqual(sum(len(t['stages']) for t in B['items']),288)
        self.assertEqual(len(B['domains']),11);self.assertEqual(len(B['modules']),22)
        for facet in B['modules']:
            for split in ['development','heldout']:
                items=[t for t in B['items'] if t['module']==facet and t['split']==split]
                self.assertGreaterEqual(len({t['scenario'] for t in items}),2)
                for scenario in {t['scenario'] for t in items}:
                    self.assertEqual({t['paraphrase'] for t in items if t['scenario']==scenario},{'original','alternate'})
        for facet in ['COOP-TRUST','COOP-RETURN','SELF-CREDIT','ALIGN-HARM','DEC-RISK']:
            selected=[t for t in B['items'] if t['module']==facet and t['split']=='development']
            self.assertEqual(len({t['scenario'] for t in selected}),2)
            for scenario in {t['scenario'] for t in selected}:
                self.assertEqual(len({t['condition'] for t in selected if t['scenario']==scenario}),2)

    def test_wording_changes_no_facts_schemas_keys_payoffs_or_rubrics(self):
        manifest={(m['prompt_id'],m['stage']):m for m in json.loads((ROOT/'battery_full/design_manifest.json').read_text(encoding='utf-8'))}
        for t in B['items']:
            if t['paraphrase']!='original':continue
            other=next(x for x in B['items'] if x['scenario']==t['scenario'] and x['condition']==t['condition'] and x['paraphrase']=='alternate')
            self.assertEqual(t['features'],other['features']);self.assertEqual(t['control_features'],other['control_features'])
            for n,(x,y) in enumerate(zip(t['stages'],other['stages'])):
                self.assertNotEqual(x['prompt'],y['prompt'])
                self.assertEqual({k:v for k,v in x.items() if k!='prompt'},{k:v for k,v in y.items() if k!='prompt'})
                mx,my=manifest[t['item_id'],n],manifest[other['item_id'],n]
                self.assertEqual(mx['scenario_facts'],my['scenario_facts'])
                self.assertNotEqual(mx['task_instruction'],my['task_instruction'])

    def test_heldout_structure_and_scoring_match_without_reusing_prompts(self):
        for t in B['items']:
            if t['split']!='development':continue
            held=next(x for x in B['items'] if x['matched_pair']==t['matched_pair'] and x['condition']==t['condition'] and x['split']=='heldout' and x['paraphrase']==t['paraphrase'])
            self.assertNotEqual(t['scenario'],held['scenario'])
            self.assertEqual(t['features'],held['features']);self.assertEqual(t['control_features'],held['control_features'])
            self.assertNotEqual(t['stages'][0]['prompt'],held['stages'][0]['prompt'])
            for x,y in zip(t['stages'],held['stages']):
                self.assertEqual(collections.Counter(re.findall(r'\d+(?:\.\d+)?',x['prompt'])),collections.Counter(re.findall(r'\d+(?:\.\d+)?',y['prompt'])))
                self.assertEqual(x['keys'],y['keys']);self.assertEqual(x['rubric'],y['rubric'])
                fx,fy=copy.deepcopy(x['fields']),copy.deepcopy(y['fields'])
                if t['module']=='SEM-LINK':fx['associates'].pop('exclude');fy['associates'].pop('exclude')
                self.assertEqual(fx,fy)
                self.assertEqual({k:v['cost'] for k,v in x['resources'].items()},{k:v['cost'] for k,v in y['resources'].items()})

    def test_full_collection_exports_transfer_and_keeps_all_stages(self):
        with tempfile.TemporaryDirectory() as d:
            b,plan=r.prepare_run(CONFIG,d,'full',battery_dir=ROOT/'battery_full')
            events=[];records=r.collect(b,plan,d,synthetic_generator(),events.append)
            self.assertEqual(len(records),304)
            self.assertEqual(events[-1]['accepted'],248)
            result=r.export(d)
            c=result['summary']['completion']
            self.assertTrue(c['complete']);self.assertTrue(c['scope_complete'])
            self.assertEqual(c['stages_accepted'],288)
            profiles=[a.load_profile(path) for path in result['graphs']]
            self.assertEqual([len(p['rows']) for p in profiles],[124,124])
            report=a.analyze(profiles)
            self.assertEqual(report['skipped'],[])
            transfer=report['comparisons'][0]
            self.assertEqual(transfer['mode'],'heldout_transfer')
            self.assertGreater(transfer['n_common_observations'],0)
            self.assertTrue(any(report['profiles'][0]['contrasts']['wording']))
            self.assertTrue(report['profiles'][0]['contrasts']['condition'])
            self.assertTrue(transfer['condition_effect_changes'])
            rating=module('full_rating_test','battery_v7/content_ratings.py')
            for p in profiles:
                self.assertEqual({row['status'] for row in p['rows']},{'valid'})
                self.assertTrue(all(n.get('split',p['split'])==p['split'] for n in p['nodes'].values() if n['kind']=='trial'))
                self.assertTrue(all(n.get('evidence',True) for n in p['graph']['edges']))
                template=r.processor.jsonl(Path(d)/'results'/f'human_review-{p["split"]}.template.jsonl')
                self.assertEqual(template,p['graph']['review_contract'])
                enriched,pending=rating.merge(p['graph'],template,[])
                self.assertTrue(pending);self.assertTrue(all(x['status']=='missing' for x in pending))
            with self.assertRaises(ValueError):a.load_profile(result['graph'])
            self.assertEqual(len(r.collect(b,plan,d,lambda *args:self.fail('Duplicate collection'))),304)

    def test_subset_and_failed_followups_cannot_look_complete(self):
        with tempfile.TemporaryDirectory() as d:
            b,plan=r.prepare_run(CONFIG,d,'partial',facets=['SEM-DISTINCT'],battery_dir=ROOT/'battery_full')
            r.collect(b,plan,d,lambda *args:dict(text='not JSON'))
            result=r.export(d);c=result['summary']['completion']
            self.assertFalse(c['complete']);self.assertFalse(c['scope_complete'])
            self.assertEqual(c['stages_without_response'],8)
            self.assertEqual(c['cards_attempted'],8)
            self.assertIn('0 / 0',Path(result['audit']).read_text(encoding='utf-8'))

    def test_checkpoint_resume_and_saved_instrument_identity(self):
        with tempfile.TemporaryDirectory() as d:
            b,plan=r.prepare_run(CONFIG,d,'resume',facets=['EPI-STATUS'],battery_dir=ROOT/'battery_full')
            generator=synthetic_generator();count=[0]
            def stop(messages,seed):
                count[0]+=1
                if count[0]==4:raise KeyboardInterrupt()
                return generator(messages,seed)
            with self.assertRaises(KeyboardInterrupt):r.collect(b,plan,d,stop)
            self.assertFalse(r.export(d)['summary']['completion']['complete'])
            b,plan=r.prepare_run(CONFIG,d,'resume',facets=['EPI-STATUS'],battery_dir=ROOT/'battery_full')
            self.assertEqual(len(r.collect(b,plan,d,generator)),16)
            with self.assertRaises(ValueError):r.prepare_run(CONFIG,d,'resume')

    def test_notebook_runs_expanded_default_and_all_code_cells_compile(self):
        nb=json.loads((ROOT/'battery_core/Run_HuggingFace_A100.ipynb').read_text(encoding='utf-8'))
        source='\n'.join(''.join(c['source']) for c in nb['cells'])
        self.assertIn('FACETS = None',source);self.assertIn('REPO_DIR / "battery_full"',source)
        self.assertIn('288 * REPEATS',source);self.assertIn('248 * REPEATS',source)
        for i,c in enumerate(nb['cells']):
            if c['cell_type']=='code':compile(''.join(c['source']),f'cell-{i}','exec')


if __name__=='__main__':unittest.main()
