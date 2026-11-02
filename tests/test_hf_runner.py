"""Offline tests: no model download/GPU, and no claimed LLM measurements."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import types
import unittest
from unittest.mock import patch
from contextlib import nullcontext

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('hf_adapter_test',ROOT/'battery_core/hf_runner.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
CONFIG=dict(provider='synthetic-test',model='fixture',seed=42,synthetic=True)


def fake_generate(messages,seed):
    # Use only the same JSON schema that a model receives, never scoring keys.
    last=messages[-1]['content']
    if 'Available resources and costs: ' in last:
        menu=json.JSONDecoder().raw_decode(last.split('Available resources and costs: ',1)[1])[0]
        return dict(text=json.dumps(dict(action='request',resource=next(iter(menu)))),output_tokens=10)
    prompt=next(m['content'] for m in reversed(messages) if m['role']=='user' and 'Submit JSON: ' in m['content'])
    schema=json.JSONDecoder().raw_decode(prompt.split('Submit JSON: ',1)[1])[0]['answer']
    answer={}
    for k,f in schema.items():
        answer[k]=(f['values'][0] if f['type']=='enum' else f['min'] if f['type'] in ['number','integer'] else
                   ['context','care','detail'] if f['type']=='strings' else 'Synthetic response for pipeline testing.')
    return dict(text=json.dumps(dict(action='submit',answer=answer)),output_tokens=30,hit_token_limit=False)


class HFRunner(unittest.TestCase):
    def test_transformers_adapter_slices_prompt_and_preserves_generated_text(self):
        class Inputs(dict):
            def to(self,device):return self
        class Tokens:
            def __init__(self,values):self.values=values
            def detach(self):return self
            def cpu(self):return self
            def tolist(self):return self.values
        class Output:
            def __getitem__(self,key):return Tokens([1,2,3,4,5,6,9][key[1]])
        class Tokenizer:
            chat_template='template';eos_token_id=9;pad_token_id=None
            def apply_chat_template(self,messages,**kwargs):
                self.messages=messages
                return Inputs(input_ids=types.SimpleNamespace(shape=(1,4)))
            def decode(self,tokens,**kwargs):
                self.tokens=tokens
                return '```json\n{}\n```'
        class Model:
            generation_config=types.SimpleNamespace(eos_token_id=[9])
            config=types.SimpleNamespace(max_position_embeddings=2048)
            device='cuda:0'
            def eval(self):return self
            def generate(self,**kwargs):
                self.kwargs=kwargs;return Output()
        torch=types.SimpleNamespace(manual_seed=lambda seed:None,inference_mode=nullcontext)
        transformers=types.SimpleNamespace(GenerationConfig=lambda **kw:types.SimpleNamespace(**kw))
        with patch.dict('sys.modules',{'torch':torch,'transformers':transformers}):
            model=Model();tokenizer=Tokenizer();gen=r.TransformersGenerator(model,tokenizer,3)
            messages=[dict(role='user',content='Only the public prompt')]
            result=gen(messages,42)
            self.assertEqual(tokenizer.tokens,[5,6,9])
            self.assertEqual(result['text'],'```json\n{}\n```')
            self.assertEqual(result['input_tokens'],4)
            self.assertFalse(result['hit_token_limit'])
            self.assertTrue(result['ended_on_eos'])
            self.assertFalse(model.kwargs['generation_config'].do_sample)
            self.assertEqual(tokenizer.messages,messages)
            model.config.max_position_embeddings=5
            with self.assertRaises(ValueError):gen(messages,42)
    def test_full_battery_with_resources_and_existing_visualizations(self):
        with tempfile.TemporaryDirectory() as d:
            b,p=r.prepare_run(CONFIG,d,'test');events=[]
            records=r.collect(b,p,d,fake_generate,events.append)
            self.assertEqual(len(records),64)
            self.assertEqual(events[-1]['completed'],50)
            result=r.export(d)
            self.assertEqual(result['summary']['quality'],{'valid':50})
            self.assertEqual(result['summary']['collection']['calls'],64)
            for key in ['report','graph','viewer']:self.assertTrue(Path(result[key]).is_file())
            # Re-running a completed run must not generate any additional answers.
            def forbidden(*args):self.fail('Repeated completed request')
            self.assertEqual(len(r.collect(b,p,d,forbidden)),64)
    def test_interruption_resume_preserves_exact_request(self):
        with tempfile.TemporaryDirectory() as d:
            b,p=r.prepare_run(CONFIG,d,'resume');calls=[]
            def interrupt(messages,seed):
                calls.append((copy.deepcopy(messages),seed))
                if len(calls)==3:raise KeyboardInterrupt()
                return fake_generate(messages,seed)
            with self.assertRaises(KeyboardInterrupt):r.collect(b,p,d,interrupt)
            self.assertEqual(len(r.records_at(Path(d)/'responses.jsonl')),2)
            self.assertTrue(Path(r.export(d)['graph']).exists())
            resumed=[]
            def restart(messages,seed):
                if not resumed:resumed.append((copy.deepcopy(messages),seed))
                return fake_generate(messages,seed)
            b,p=r.prepare_run(CONFIG,d,'resume');r.collect(b,p,d,restart)
            self.assertEqual(resumed[0],calls[-1])
    def test_invalid_outputs_preserved_without_repair_or_retry(self):
        with tempfile.TemporaryDirectory() as d:
            b,p=r.prepare_run(CONFIG,d,'invalid',facets=['DEC-RISK'])
            raw='```json\n{"action":"submit","answer":{"choice":"SURE"}}\n```'
            records=r.collect(b,p,d,lambda messages,seed:dict(text=raw))
            self.assertEqual(len(records),2)
            self.assertEqual(records[0]['raw_response'],raw)
            result=r.export(d);self.assertEqual(result['summary']['quality'],{'invalid':2})
    def test_model_exception_leaves_request_pending(self):
        with tempfile.TemporaryDirectory() as d:
            b,p=r.prepare_run(CONFIG,d,'error',facets=['DEC-RISK'])
            def fail(*args):raise RuntimeError('Simulated GPU failure')
            with self.assertRaises(RuntimeError):r.collect(b,p,d,fail)
            self.assertEqual(r.records_at(Path(d)/'responses.jsonl'),[])
            self.assertEqual(len(r.records_at(Path(d)/'generation_errors.jsonl')),1)
            self.assertEqual(len(r.collect(b,p,d,fake_generate)),2)
    def test_changed_settings_rejected_on_resume(self):
        with tempfile.TemporaryDirectory() as d:
            r.prepare_run(CONFIG,d,'same')
            with self.assertRaises(ValueError):r.prepare_run(dict(CONFIG,seed=123),d,'same')
    def test_corrupt_journal_not_silently_discarded(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'responses.jsonl';path.write_text('{"incomplete":',encoding='utf-8')
            with self.assertRaises(ValueError):r.records_at(path)
    def test_notebook_cells_compile_and_have_no_saved_outputs(self):
        nb=json.loads((ROOT/'battery_core/Run_HuggingFace_A100.ipynb').read_text(encoding='utf-8'))
        self.assertEqual(len({c['id'] for c in nb['cells']}),len(nb['cells']))
        for c in nb['cells']:
            if c['cell_type']=='code':
                compile(''.join(c['source']),c['id'],'exec')
                self.assertEqual(c['outputs'],[])
                self.assertIsNone(c['execution_count'])
        text=json.dumps(nb)
        self.assertIn('Qwen/Qwen2.5-7B-Instruct',text)
        self.assertIn('files.download',text)

if __name__=='__main__':unittest.main()
