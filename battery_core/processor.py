"""Run the compact prompt CSV using the existing staged interaction engine.

Python standard library only. No model API dependency. Requests contain all model
stimuli; evaluator scoring rules and keys are not sent to the tested model.
"""
import argparse
import collections
import csv
import importlib.util
import json
import math
from pathlib import Path

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('core_engine',BASE.parent/'battery_v7/_engine.py')
engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
read,write,lines,jsonl,digest=engine.read,engine.write,engine.lines,engine.jsonl,engine.digest

_legacy_stage_prompt=engine.stage_prompt


def stage_prompt(s):
    """Keep historical plans replayable; new plans use plain value instructions."""
    if s.get('response_protocol')!='plain-values-v1':return _legacy_stage_prompt(s)
    parts=[s['prompt'],
        'Return exactly one JSON object, with no Markdown fences or text before or after it. '
        'Its "action" must be "submit", and its "answer" must be an object containing exactly the fields listed below. '
        'Put actual values directly in those fields. Do not include schema definitions or wrap a value in a type, values, text, content, count or max_words object.',
        'Answer fields:']
    for name,f in s['fields'].items():
        typ=f['type']
        if typ=='enum':description='a JSON string chosen from '+', '.join(json.dumps(v) for v in f['values'])
        elif typ=='text':description=f'a JSON string containing your own words, at most {f["max_words"]} words'
        elif typ=='strings':
            description=f'a JSON array of exactly {f["count"]} distinct strings, each one to five words'
            if f.get('exclude'):description+='; do not repeat '+json.dumps(f['exclude'])
        elif typ in ['number','integer']:
            description=('a whole JSON number' if typ=='integer' else 'a JSON number')+f' from {f["min"]} to {f["max"]}'
        else:raise ValueError('Unknown response field type')
        parts.append('- '+json.dumps(name)+': '+description+'.')
    if 'confidence' in s['fields']:parts.append('Confidence means your probability, from 0 to 100, that your submitted answer is correct.')
    if s['resources']:
        menu={k:dict(cost=r['cost']) for k,r in s['resources'].items()}
        parts.append('Before submitting, you may open each resource once by returning only {"action":"request","resource":"NAME"}. Available resources and costs: '+json.dumps(menu)+'.')
    parts.append('To decline, return only {"action":"decline"}.')
    return '\n\n'.join(parts)


engine.stage_prompt=stage_prompt


def load(base=None):
    base=Path(base) if base is not None else BASE
    b=read(base/'battery.json');items={}
    with (base/'prompts.csv').open(encoding='utf-8-sig',newline='') as f:
        for r in csv.DictReader(f):
            mid=r['facet'];sid=r['prompt_id']
            if mid not in b['modules'] or r['category']!=b['modules'][mid]['domain']:
                raise ValueError('Category/facet mismatch')
            t=items.setdefault(sid,dict(item_id=sid,module=mid,scenario=sid,scenario_name=r['title'],
                condition='base',split='development',paraphrase='original',cue=r['cue'],stratum='standard',
                matched_pair=sid,presentation=dict(base_stratum='standard',order_id='original',transfer_pattern='none'),
                features=json.loads(r['features']),control_features=json.loads(r['capability_controls']),stages=[]))
            if t['module']!=mid or int(r['stage'])!=len(t['stages']):raise ValueError('Inconsistent stages')
            for key,col in [('features','features'),('control_features','capability_controls')]:
                if t[key]!=json.loads(r[col]):raise ValueError('Inconsistent scoring definitions')
            s=dict(prompt=r['prompt'],fields=json.loads(r['response_fields']),resources=json.loads(r['resources']),
                   keys=json.loads(r['answer_keys']),rubric=json.loads(r['review_rubric']),effects={},feedback=False)
            if b.get('response_protocol'):s['response_protocol']=b['response_protocol']
            if not s['prompt'].strip():raise ValueError('Missing stimulus')
            t['stages'].append(s)
    b['items']=list(items.values())
    if set(b['modules'])!={t['module'] for t in b['items']}:raise ValueError('Empty facet')
    return b


def prepare(b,config,run_id,repeats=1,facets=None):
    chosen=set(facets or b['modules'])
    if not chosen or not chosen<=b['modules'].keys():raise ValueError('Unknown facet selection')
    subset=dict(b,items=[t for t in b['items'] if t['module'] in chosen])
    p=engine.prepare(subset,config,run_id,repeats)
    p.update(battery_hash=digest(b),facets=sorted(chosen),split='development')
    p.pop('plan_hash');p['plan_hash']=digest(p)
    return p


def validate(b,p):
    engine.validate_plan(b,p)
    expected={t['item_id']:t for t in b['items'] if t['module'] in p['facets']}
    seen=set()
    for t in p['trials']:
        base=expected.get(t['item_id'])
        if not base or any(t.get(k)!=v for k,v in base.items()):raise ValueError('Plan differs from CSV')
        cell=(t['item_id'],t['repeat'])
        if cell in seen:raise ValueError('Duplicate trial')
        seen.add(cell)
    if seen!={(sid,r) for sid in expected for r in range(p['repeats'])}:raise ValueError('Plan scope mismatch')


def measure(rule,state,t):
    sub=state['submissions'][rule['stage']];op=rule['op']
    if op=='requested':return int(rule['resource'] in sub['resources'])
    if op=='key_accuracy':
        keys=t['stages'][rule['stage']]['keys']
        return sum(sub['metrics'][k+'_accuracy'] for k in keys)/len(keys)
    value=sub['answer'][rule['field']];arg=rule.get('arg')
    if op=='scale':return value/arg
    if op=='equals':return int(value==arg)
    if op=='not_equals':return int(value!=arg)
    if op=='error':return abs(value-arg)/100
    if op=='difference':return (value-state['submissions'][rule['other_stage']]['answer'][rule['field']])/arg
    raise ValueError('Unknown feature operation: '+op)


def score(b,p,records):
    validate(b,p)
    rows,summary,g,review=engine.score(b,p,records)
    states=engine.replay(b,p,records);trials={t['trial_id']:t for t in p['trials']}
    nodes={n['id']:n for n in g['nodes']}
    def node(nid,kind,**attrs):
        if nid not in nodes:
            nodes[nid]=dict(id=nid,kind=kind,**attrs);g['nodes'].append(nodes[nid])
        return nid
    def edge(a,rel,z,**attrs):g['edges'].append(dict(id='core:'+str(len(g['edges'])),source=a,type=rel,target=z,**attrs))
    for row in rows:
        t=trials[row['trial_id']];st=states[row['trial_id']];valid=st['status']=='valid'
        features={k:measure(v,st,t) for k,v in t['features'].items()} if valid else {}
        controls={k:measure(v,st,t) for k,v in t['control_features'].items()} if valid else {}
        if any(not math.isfinite(v) for v in features.values()):raise ValueError('Invalid feature')
        row.update(features=features,capability_controls=controls,**{k:t[k] for k in ['split','paraphrase','cue','stratum','matched_pair','presentation']})
        tn=nodes['trial:'+row['trial_id']]
        tn.update(features=features,capability_controls=controls,split=t['split'],presentation=t['presentation'])
        tn['metrics'].update({'feature_'+k:v for k,v in features.items()})
        it=nodes['item:'+t['item_id']]
        it.update(matched_pair=t['matched_pair'],presentation=t['presentation'],conditions=dict(condition=t['condition'],
                  paraphrase=t['paraphrase'],split=t['split'],cue=t['cue'],stratum=t['stratum']))
        for name,value in features.items():
            mn=node(tn['id']+':feature:'+name,'measurement',label=name,value=value,measurement_level='task_feature',stability_status='not_established')
            edge(tn['id'],'has_measurement',mn,origin='prespecified_task_rule')
        for name,value in controls.items():
            mn=node(tn['id']+':control:'+name,'capability_measurement',label=name,value=value)
            edge(tn['id'],'has_capability_control',mn)
        if t['module']=='SEM-LINK' and valid:
            cue=node('concept:'+t['cue'],'concept',label=t['cue'])
            for rank,word in enumerate(st['submissions'][0]['answer']['associates'],1):
                normalized=' '.join(word.casefold().split());target=node('concept:'+normalized,'concept',label=normalized)
                edge(tn['id'],'elicited_associate',target,cue=cue,rank=rank,context='development|base',origin='observed_response')
                edge(cue,'evokes_in_response',target,evidence=[tn['id']],rank=rank,origin='observed_response')
    # The catalog carries metric meanings so the existing analyzer need not guess.
    g['profile_catalog']['modules']={k:dict(v) for k,v in b['modules'].items()}
    g['profile_catalog']['primary']={k:'feature_'+v['primary_metric'] for k,v in b['modules'].items() if v['primary_metric']}
    observations=collections.defaultdict(list);exposures=collections.Counter()
    for row in rows:
        if row['module']=='SEM-LINK' and row['status']=='valid':exposures[row['cue']]+=1
    for e in list(g['edges']):
        if e['type']=='elicited_associate':observations[e['cue'],e['target']].append(e['source'])
    for (cue,target),evidence in observations.items():
        edge(cue,'evokes',target,context='development|base',weight=len(evidence)/exposures[cue.removeprefix('concept:')],
             n_valid=exposures[cue.removeprefix('concept:')],evidence=evidence,origin='observed_association_frequency')
    for d in g['profile_catalog']['domains']:
        d['description']='Text-only compact core: actual response evidence.'
        d['limit']='Two scenarios per non-association facet; stability and generalization are not established.'
    g.update(bank='profile',analysis_split='development',analysis_lock_hash=None,
             measurement_design=dict(kind='compact_prompt_list',wording_effects='not tested',order_effects='not tested',heldout='not supplied'))
    g['review_contract']=review
    summary.update(version=b['version'],warning='Descriptive task features. Capability controls stay separate. Content ratings require review. No stability or latent-trait claim.')
    return rows,summary,g,review


def main():
    ap=argparse.ArgumentParser(description=__doc__);sub=ap.add_subparsers(dest='command',required=True)
    a=sub.add_parser('prepare');a.add_argument('--config',required=True);a.add_argument('--run-id',required=True);a.add_argument('--repeats',type=int,default=1);a.add_argument('--facets',nargs='+');a.add_argument('--out',required=True)
    for command in ['next','process']:
        a=sub.add_parser(command);a.add_argument('--plan',required=True);a.add_argument('--responses');a.add_argument('--out',required=True)
    a=ap.parse_args();b=load();out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    if a.command=='prepare':
        if (out/'plan.json').exists():raise ValueError('Use a new run directory or resume with next')
        p=prepare(b,read(a.config),a.run_id,a.repeats,a.facets);write(out/'plan.json',p)
        lines(out/'requests.jsonl',engine.next_requests(b,p,[]))
    else:
        p=read(a.plan);validate(b,p);records=jsonl(a.responses)
        if a.command=='next':lines(out/'requests.jsonl',engine.next_requests(b,p,records))
        else:
            rows,summary,g,review=score(b,p,records)
            write(out/'graph.json',g);write(out/'scores.json',summary);lines(out/'trial_scores.jsonl',rows);lines(out/'human_review.template.jsonl',review)
    print('Wrote outputs to',out)


if __name__=='__main__':main()
