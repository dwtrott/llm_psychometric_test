"""Checkpointed local generation for the Colab notebook.

Collection and export use the standard library. Hugging Face / torch imports are
lazy and confined to TransformersGenerator. No prompt rewriting or JSON repair.
"""
import collections
import csv
import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import time

ROOT=Path(__file__).resolve().parents[1]


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj


processor=module('hf_battery_processor',ROOT/'battery_core/processor.py')


def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()


def atomic_json(path,value):
    path=Path(path);temporary=path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8')
    temporary.replace(path)


def append_record(path,record):
    # Only one collector may write a run directory at a time.
    with Path(path).open('a',encoding='utf-8',newline='\n') as stream:
        stream.write(json.dumps(record,ensure_ascii=False,allow_nan=False)+'\n')
        stream.flush();os.fsync(stream.fileno())


def records_at(path):
    path=Path(path)
    if not path.exists():return []
    records=[]
    for line_no,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if not line.strip():continue
        try:records.append(json.loads(line))
        except ValueError as exc:
            raise ValueError(f'Incomplete/corrupt response journal at line {line_no}. Preserve the file and inspect it; records are never silently discarded.') from exc
    return records


def prepare_run(config,run_dir,run_id,repeats=1,facets=None,battery_dir=None):
    if config.get('provider')=='huggingface-local' and (config.get('adapter_version')!='1.4.0' or battery_dir is None):
        raise ValueError('STALE COLAB NOTEBOOK: reopen the notebook from GitHub in a fresh runtime. The scored full battery requires adapter 1.4.0 and an explicit battery_full directory. No compact run was started.')
    out=Path(run_dir);out.mkdir(parents=True,exist_ok=True)
    source=Path(battery_dir) if battery_dir is not None else ROOT/'battery_core'
    b=processor.load(source)
    if config.get('provider')=='huggingface-local' and b['version']!='0.11.0-measurement':
        raise ValueError('Expected scored full battery v0.11.0. Refresh the notebook and source checkout.')
    proposed=processor.prepare(b,config,run_id,repeats,facets)
    path=out/'plan.json'
    if path.exists():
        plan=processor.read(path);processor.validate(b,plan)
        if plan!=proposed:
            raise ValueError('This run directory belongs to a different model revision, settings, battery or scope. Keep it and choose a new RUN_LABEL.')
        processor.engine.replay(b,plan,records_at(out/'responses.jsonl'))
    else:
        if (out/'responses.jsonl').exists():raise ValueError('Response journal exists without its plan; do not overwrite this run.')
        plan=proposed;atomic_json(path,plan)
        atomic_json(out/'config.json',plan['config'])
    instrument=out/'instrument';instrument.mkdir(exist_ok=True)
    for name in ['battery.json','prompts.csv']:
        target=instrument/name;data=(source/name).read_bytes()
        if target.exists() and target.read_bytes()!=data:raise ValueError('Saved instrument differs; use a new run label')
        if not target.exists():target.write_bytes(data)
    return b,plan


def collect(b,plan,run_dir,generate,progress=None):
    """generate(messages, seed) returns {text, ...timing/token metadata}.

    Only the model-facing history is passed to the generator, never answer keys,
    rubrics or evaluator IDs. A generation exception stops collection and leaves
    that request pending for resume. Invalid completed outputs are NOT retried.
    """
    processor.validate(b,plan);out=Path(run_dir)
    records=records_at(out/'responses.jsonl')
    states=processor.engine.replay(b,plan,records)
    for trial in plan['trials']:
        state=states[trial['trial_id']]
        while state['status']=='pending':
            req=processor.engine.request(plan,trial,state)
            seed=int(hashlib.sha256((str(plan['config'].get('seed',42))+req['request_hash']).encode()).hexdigest()[:8],16)
            started=time.perf_counter()
            try:
                generated=generate(req['messages'],seed)
                if not isinstance(generated,dict) or not isinstance(generated.get('text'),str):
                    raise TypeError('Generator must return a text string')
            except Exception as exc:
                append_record(out/'generation_errors.jsonl',dict(trial_id=trial['trial_id'],event_index=req['event_index'],
                    request_hash=req['request_hash'],timestamp=now(),error_type=type(exc).__name__,message=str(exc)))
                raise
            record={k:req[k] for k in ['trial_id','config_id','plan_hash','event_index','request_hash']}
            record.update(status='ok',raw_response=generated['text'],timestamp=now(),
                          generation={k:v for k,v in generated.items() if k!='text'},wall_seconds=time.perf_counter()-started)
            # Validate on a replayable copy before committing the journal record.
            new_state=json.loads(json.dumps(state))
            processor.engine.apply(plan,trial,new_state,record)
            append_record(out/'responses.jsonl',record)
            records.append(record);state=new_state;states[trial['trial_id']]=state
            if progress:
                progress(dict(calls=len(records),processed=sum(s['status']!='pending' for s in states.values()),
                              completed=sum(s['status']=='valid' for s in states.values()),
                              accepted=sum(s['status']=='valid' for s in states.values()),
                              total=len(states),item_id=trial['item_id'],status=state['status'],
                              quality=dict(collections.Counter(s['status'] for s in states.values()))))
    return records


def export(run_dir):
    """Export even a partial run. The notebook can call this after an interruption."""
    out=Path(run_dir);b=processor.load(out/'instrument' if (out/'instrument').exists() else None);plan=processor.read(out/'plan.json')
    records=records_at(out/'responses.jsonl')
    rows,summary,graph,review=processor.score(b,plan,records)
    evaluator=module('hf_evaluator',ROOT/'battery_core/evaluate.py')
    states=processor.engine.replay(b,plan,records)
    graph=evaluator.enrich(graph,b,plan,states,out)
    evaluated_nodes={n['id']:n for n in graph['nodes']}
    for row in rows:row['features']=evaluated_nodes['trial:'+row['trial_id']]['features']
    summary['evaluation']=graph['automated_evaluation']
    result=out/'results';result.mkdir(exist_ok=True)
    evaluator.report(graph,result/'measurements.html')
    processor.lines(result/'trial_scores.jsonl',rows)
    processor.lines(result/'human_review.template.jsonl',review)
    states=processor.engine.replay(b,plan,records)
    with (result/'response_status.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['trial_id','item_id','facet','status','error','stages_completed']);writer.writeheader()
        for t in plan['trials']:
            s=states[t['trial_id']]
            writer.writerow(dict(trial_id=t['trial_id'],item_id=t['item_id'],facet=t['module'],status=s['status'],
                                 error=s.get('error',''),stages_completed=len(s['submissions'])))
    summary['collection']=dict(calls=len(records),generated_tokens=sum(r.get('generation',{}).get('output_tokens',0) for r in records),
        generation_seconds=sum(r.get('wall_seconds',0) for r in records),
        token_limit_hits=sum(bool(r.get('generation',{}).get('hit_token_limit')) for r in records))
    auditor=module('hf_audit',ROOT/'battery_core/run_audit.py')
    audit=auditor.audit(b,plan,records)
    audit_path=auditor.write_report(audit,result)
    graph['run_completion']=audit['summary']
    atomic_json(result/'graph.json',graph)
    summary['completion']=audit['summary']
    summary['run_status']='complete' if audit['summary']['complete'] else 'incomplete'
    start=audit_path.read_text(encoding='utf-8').replace('<h1>',
        '<p><b>Psychological trait strengths are not established.</b> Inspect validity diagnostics before using any response rate as a psychological finding.</p><p><a href="results/measurements.html"><b>Read the actual scores and supporting quotations</b></a> · '
        '<a href="results/analysis/report.html">Open analysis (check coverage below first)</a> · '
        '<a href="results/viewer.html">Open graph viewer</a></p><h1>',1)
    (out/'START_HERE.html').write_text(start,encoding='utf-8')
    atomic_json(result/'scores.json',summary)
    analysis=module('hf_analysis',ROOT/'analyzer/psychometric.py')
    viewer=module('hf_viewer',ROOT/'viewer/viewer.py')
    graphs=[result/'graph.json']
    if plan['split']=='all':
        graphs=[]
        for split in ['development','heldout']:
            _,_,partition,partition_review=processor.score(b,plan,records,split=split)
            partition=evaluator.enrich(partition,b,plan,states,out)
            path=result/f'graph-{split}.json';atomic_json(path,partition);graphs.append(path)
            processor.lines(result/f'human_review-{split}.template.jsonl',partition_review)
    report=analysis.build(graphs,result/'analysis')
    viewer.build_viewer(graphs,result/'viewer.html')
    return dict(summary=summary,audit=str(audit_path),start=str(out/'START_HERE.html'),report=str(report),graph=str(result/'graph.json'),graphs=[str(p) for p in graphs],viewer=str(result/'viewer.html'))


def evaluate_run(run_dir,generate,judge,progress=None):
    out=Path(run_dir);b=processor.load(out/'instrument');plan=processor.read(out/'plan.json')
    processor.validate(b,plan)
    states=processor.engine.replay(b,plan,records_at(out/'responses.jsonl'))
    evaluator=module('hf_evaluator_collection',ROOT/'battery_core/evaluate.py')
    return evaluator.collect(b,plan,states,out,generate,judge,progress)


class TransformersGenerator:
    """One conversation at a time, with an explicit greedy generation config."""
    def __init__(self,model,tokenizer,max_new_tokens=512):
        import torch
        from transformers import GenerationConfig
        if not tokenizer.chat_template:raise ValueError('Select an instruction/chat model with a chat template.')
        self.model=model;self.tokenizer=tokenizer;self.torch=torch
        self.max_new_tokens=max_new_tokens
        eos=model.generation_config.eos_token_id
        if eos is None:eos=tokenizer.eos_token_id
        if eos is None:raise ValueError('Model has no end-of-sequence token definition.')
        pad=tokenizer.pad_token_id
        if pad is None:pad=eos[0] if isinstance(eos,list) else eos
        self.generation=GenerationConfig(do_sample=False,num_beams=1,max_new_tokens=max_new_tokens,
                                        use_cache=True,eos_token_id=eos,pad_token_id=pad)
        self.model.eval()

    def __call__(self,messages,seed):
        self.torch.manual_seed(seed)
        inputs=self.tokenizer.apply_chat_template(messages,tokenize=True,add_generation_prompt=True,
                                                  return_dict=True,return_tensors='pt')
        length=inputs['input_ids'].shape[-1]
        context=getattr(self.model.config,'max_position_embeddings',None)
        if context and length+self.max_new_tokens>context:
            raise ValueError('Prompt plus output budget exceeds the model context; no silent truncation is allowed.')
        inputs=inputs.to(self.model.device)
        with self.torch.inference_mode():
            generated=self.model.generate(**inputs,generation_config=self.generation)
        tokens=generated[0,length:].detach().cpu().tolist()
        eos=self.generation.eos_token_id
        stop=set(eos if isinstance(eos,list) else [eos])
        ended=bool(tokens and tokens[-1] in stop)
        # Decoding removes model control tokens only; prose/fences/JSON stay intact.
        raw=self.tokenizer.decode(tokens,skip_special_tokens=True,clean_up_tokenization_spaces=False)
        return dict(text=raw,input_tokens=length,output_tokens=len(tokens),generated_token_ids=tokens,
                    ended_on_eos=ended,hit_token_limit=len(tokens)>=self.max_new_tokens and not ended)
