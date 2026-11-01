"""Generate explicitly synthetic v0.7 demonstrations, never call an LLM."""
import importlib.util,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
p=module('battery_demo',ROOT/'battery_v7/processor.py');analysis=module('analysis_demo',ROOT/'analyzer/psychometric.py')
def response(t,stage,model):
 a={}
 for key,f in stage['fields'].items():
  a[key]=f['values'][0] if f['type']=='enum' else 'Synthetic demonstration text. No real model response or psychological finding.' if f['type']=='text' else ['fairness','care','evidence','choice','context' if model=='A' else 'oversight'] if f['type']=='strings' else f['min']
 for key,k in stage['keys'].items():a[key]=k['value']
 if 'confidence' in a:a['confidence']=75 if model=='A' else 90
 if t['module']=='DEC-RISK':a['choice']='RISK' if (t['condition']=='gain' if model=='A' else t['presentation']['order_id']=='order02') else 'SURE'
 if t['module']=='COOP-SHARE':a['give']=(6 if model=='A' else 3)+(2 if t['condition']=='public' else 0)
 if t['module']=='SELF-CREDIT':a['originator_credit']={'originator_self':80 if model=='A' else 60,'implementer_self':20 if model=='A' else 40,'neutral_observer':50}[t['presentation']['base_stratum']]
 return a
def create_graph(b,model,split):
 config=dict(provider='synthetic-demo',model='Synthetic '+model,synthetic=True,temperature=0)
 specification=dict(model_configurations=[config],primary_features={'DEC-RISK':['risky_choice']},comparison_rules='Synthetic demonstration only; all conditions and presentations.',heldout_prediction_rule='Synthetic zero transfer change is generated, not empirically validated.',exclusions='Keep all synthetic records.',rating_codebook_policy='No human ratings; generated text is a placeholder.')
 plan=p.prepare(b,config,'demo-'+model+'-'+split,repeats=2,split=split,analysis_lock=p.freeze(b,specification) if split=='heldout' else None);records=[]
 for t in plan['trials']:
  state=p.engine.initial(plan,t)
  while state['status']=='pending':
   req=p.engine.request(plan,t,state);answer=response(t,t['stages'][state['stage']],model)
   record=dict(**{k:req[k] for k in ['trial_id','config_id','plan_hash','event_index','request_hash']},status='ok',raw_response=json.dumps(dict(action='submit',answer=answer)))
   p.engine.apply(plan,t,state,record);records.append(record)
 return p.score(b,plan,records)[2]
if __name__=='__main__':
 out=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'results/analysis-demo';out.mkdir(parents=True,exist_ok=True);b=p.load();paths=[]
 for model,split in [('A','development'),('B','development'),('A','heldout')]:
  path=out/f'synthetic-{model}-{split}.json';path.write_text(json.dumps(create_graph(b,model,split)),encoding='utf-8');paths.append(path)
 print(analysis.build(paths,out).resolve())
