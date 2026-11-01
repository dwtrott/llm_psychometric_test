"""v0.2 draft: prepare complete prompts, score explicit outcomes, export evidence KG.
Python 3.10+ standard library. No model API calls; no automatic psychological diagnosis.
"""
import argparse,collections,csv,hashlib,json,math,pathlib,random,statistics
BASE=pathlib.Path(__file__).resolve().parent
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,allow_nan=False,separators=(',',':')).encode()).hexdigest()
def read(path):return json.loads(pathlib.Path(path).read_text(encoding='utf-8-sig'))
def write(path,obj):pathlib.Path(path).write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8')
def jsonl(path):return [json.loads(s) for s in pathlib.Path(path).read_text(encoding='utf-8-sig').splitlines() if s.strip()]
def load():
    b=read(BASE/'battery.json');items=[]
    with (BASE/'questions.csv').open(encoding='utf-8-sig',newline='') as h:
        for row in csv.DictReader(h):
            i={k[:-5] if k.endswith('_json') else k:json.loads(v) if k.endswith('_json') else v for k,v in row.items()}
            i['correct']=i['correct'] or None
            if not i['question'].strip() or i['kind'] not in ['choice','open','associations']:raise ValueError('Invalid question/kind')
            if i['kind']=='choice' and (len(i['options'])<2 or (i['correct'] and i['correct'] not in i['options'])):raise ValueError('Invalid choices/key')
            items.append(i)
    if len({i['item_id'] for i in items})!=len(items):raise ValueError('Duplicate item ID')
    families={f['id'] for f in b['families']}
    if any(i['family_id'] not in families for i in items):raise ValueError('Unknown family')
    b['items']=items;return b
def prepare(b,config,run_id,repeats=4,seed=1729):
    if not run_id or type(repeats)!=int or repeats<1:raise ValueError('Provide run ID and positive repeats')
    if not config.get('model') or not config.get('provider'):raise ValueError('Record model and provider')
    if any(any(s in k.lower() for s in ['secret','password','api_key','access_token']) for k in config):raise ValueError('Do not record credentials')
    config=dict(config,system_prompt=b['system_prompt']);trials=[]
    for i in b['items']:
        keys=list(i['options']);random.Random(f'{seed}:{i["family_id"]}').shuffle(keys)
        for r in range(repeats):
            rotated=keys[r%len(keys):]+keys[:r%len(keys)] if keys else []
            mapping={chr(65+n):key for n,key in enumerate(rotated)}
            prompt=i['question']+('\n\nOptions:\n'+'\n'.join(f'{letter}. {i["options"][key]}' for letter,key in mapping.items()) if mapping else '')
            prompt+='\n\nReturn JSON fields: '+json.dumps(i['response_schema'],ensure_ascii=False)
            trials.append(dict(trial_id=f'{run_id}:{i["item_id"]}:r{r:03}',item_id=i['item_id'],repeat=r,option_map=mapping,messages=[dict(role='system',content=b['system_prompt']),dict(role='user',content=prompt)]))
    random.Random(seed).shuffle(trials)
    return dict(version=b['version'],battery_hash=digest(b),config_id='config:'+digest(config)[:20],config=config,run_id=run_id,repeats=repeats,seed=seed,trials=trials)
def validate(i,t,answer):
    if not isinstance(answer,dict):raise ValueError('Expected JSON object')
    if answer=={'declined':True}:return 'declined',{},None
    if set(answer)!=set(i['response_schema']):raise ValueError('Incorrect response fields')
    if i['kind']=='choice':
        if not isinstance(answer['choice'],str) or answer['choice'] not in t['option_map']:raise ValueError('Unknown displayed option')
        if not isinstance(answer['evidence'],str) or not 1<=len(answer['evidence'].split())<=80:raise ValueError('Evidence must be 1–80 words')
        chosen=t['option_map'][answer['choice']];metrics={'choice_'+k:float(k==chosen) for k in i['options']}
        if i['correct']:
            confidence=answer['confidence']
            if type(confidence) not in [int,float] or not math.isfinite(confidence) or not 0<=confidence<=100:raise ValueError('Invalid confidence')
            correct=float(chosen==i['correct']);metrics.update(accuracy=correct,confidence=confidence/100,brier=(confidence/100-correct)**2,overconfident_error=float(not correct and confidence>=80))
        return 'valid',metrics,chosen
    if i['kind']=='open':
        if not isinstance(answer['response'],str) or not 1<=len(answer['response'].split())<=300:raise ValueError('Open response must be 1–300 words')
    else:
        bycue=answer['associates']
        if not isinstance(bycue,dict) or set(bycue)!=set(i['response_schema']['associates']):raise ValueError('Need exactly the requested cue keys')
        for cue,words in bycue.items():
            if not isinstance(words,list) or len(words)!=5 or not all(isinstance(w,str) and 0<len(w.strip())<=80 for w in words) or len({' '.join(w.casefold().split()) for w in words})!=5 or cue in {' '.join(w.casefold().split()) for w in words}:raise ValueError('Need five distinct short associates excluding cue')
    return 'valid',{},None
def score(b,plan,records):
    if plan['battery_hash']!=digest(b):raise ValueError('Battery changed; regenerate the plan')
    if plan['config_id']!='config:'+digest(plan['config'])[:20]:raise ValueError('Configuration mismatch')
    bytrial={t['trial_id']:t for t in plan['trials']};items={i['item_id']:i for i in b['items']};rr={}
    for r in records:
        if r.get('trial_id') not in bytrial or r['trial_id'] in rr:raise ValueError('Unknown or duplicate trial ID')
        if r.get('config_id')!=plan['config_id']:raise ValueError('Response configuration mismatch')
        if r.get('status') not in ['ok','api_error']:raise ValueError('Response status must be ok or api_error')
        rr[r['trial_id']]=r
    rows=[];review=[];nodes={};edges=[];assoc=collections.defaultdict(list);den=collections.Counter()
    def node(id,kind,**props):nodes[id]=dict(id=id,kind=kind,**props);return id
    def edge(src,typ,dst,**props):edges.append(dict(id='e:'+str(len(edges)),source=src,type=typ,target=dst,**props))
    def concept(label):return node('concept:'+' '.join(label.casefold().split()),'concept',label=' '.join(label.casefold().split()))
    cid=node(plan['config_id'],'model_configuration',**plan['config']);rid=node('run:'+plan['run_id'],'run',battery_version=b['version'])
    edge(cid,'has_run',rid)
    for t in plan['trials']:
        i=items[t['item_id']];r=rr.get(t['trial_id']);answer=None;metrics={};choice=None;error=None
        status='missing' if r is None else 'api_error' if r['status']=='api_error' else 'invalid'
        if r and r['status']=='ok':
            try:answer=json.loads(r['raw_response']);status,metrics,choice=validate(i,t,answer)
            except (ValueError,KeyError,TypeError) as e:error=str(e)
        row=dict(trial_id=t['trial_id'],item_id=i['item_id'],family_id=i['family_id'],domain=i['domain'],condition=i['condition'],status=status,metrics=metrics,choice=choice,review_status='pending' if status=='valid' and i['kind']=='open' else 'not_required')
        rows.append(row)
        it=node('item:'+i['item_id'],'item',module=i['family_id'],scenario_family=i['family_id'],conditions={'condition':i['condition']},facet=i['facet'])
        tn=node('trial:'+t['trial_id'],'trial',status=status,metrics=metrics,raw_response=r.get('raw_response') if r else None,rendered_messages=t['messages'],option_map=t['option_map'],answer=answer,error=error,response_timestamp=r.get('timestamp') if r else None,response_hash=digest(r) if r else None)
        edge(rid,'contains_trial',tn);edge(tn,'instance_of',it)
        hypothesis=node('hypothesis:'+i['facet'],'construct_hypothesis',label=i['facet'],validation_status='unvalidated')
        edge(it,'designed_to_probe',hypothesis,origin='researcher_design')
        for a in i['anchors']:edge(it,'researcher_assigned_anchor',concept(a),origin='researcher_design')
        if choice is not None:
            op=node('option:'+i['item_id']+':'+choice,'response_option',label=i['options'][choice],semantic_choice=choice);edge(tn,'selected',op,origin='observed_response')
        for metric,value in metrics.items():
            mn=node(tn+':metric:'+metric,'measurement',label=metric,value=value);edge(tn,'has_measurement',mn,origin='scored_response')
        if status=='valid' and i['kind']=='associations':
            for cueword,words in answer['associates'].items():
                cue=concept(cueword);den[(cue,i['condition'])]+=1
                for rank,word in enumerate(words,1):
                    target=concept(word);edge(tn,'elicited_associate',target,cue=cue,context=i['condition'],rank=rank,origin='observed_response');assoc[(cue,target,i['condition'])].append((tn,rank))
        if status=='valid' and i['kind']=='open':
            text=node(tn+':text','open_response',text=answer['response'],review_status='pending');edge(tn,'produced_text',text,origin='observed_response')
            for criterion,anchors in i['rubric'].items():review.append(dict(trial_id=t['trial_id'],criterion=criterion,rubric=anchors,rater_id='',score=None,evidence_quote='',review_status='pending'))
    for (cue,target,context),obs in assoc.items():edge(cue,'evokes',target,context=context,weight=len(obs)/den[(cue,context)],n_valid=den[(cue,context)],n_mentions=len(obs),mean_rank=statistics.mean(r for _,r in obs),evidence=[t for t,_ in obs],origin='estimated')
    cells=collections.defaultdict(list)
    for r in rows:
        for metric,value in r['metrics'].items():cells[(r['family_id'],r['condition'],metric)].append(value)
    estimates=[dict(family_id=f,condition=c,metric=m,mean=statistics.mean(v),n_valid=len(v)) for (f,c,m),v in sorted(cells.items())]
    lookup={(r['family_id'],r['condition'],r['metric']):r for r in estimates};contrasts=[]
    for f in b['families']:
        ca,cb=[v[0] for v in f['variants']]
        for metric in {m for fam,c,m in cells if fam==f['id']}:
            a=lookup.get((f['id'],ca,metric));bb=lookup.get((f['id'],cb,metric))
            if a and bb:contrasts.append(dict(family_id=f['id'],condition_a=ca,condition_b=cb,metric=metric,delta_b_minus_a=bb['mean']-a['mean'],n_a=a['n_valid'],n_b=bb['n_valid']))
    catalog=dict(domains=[dict(title=d['title'],modules=[f['id'] for f in b['families'] if f['domain']==d['id']],description='Original controlled probes; inspect each family and its condition contrast.',limit='Exploratory behavioral evidence; no validated domain total.') for d in b['domains']],modules={f['id']:dict(title=f['title'],scoring=f['probe']+' '+f['contrast'],limit=f['confounds']) for f in b['families']},primary={f['id']:'accuracy' for f in b['families'] if f['correct']},sourcesFor={f['id']:'; '.join(b['sources'][s]['title']+' — '+b['sources'][s]['url'] for s in f['sources']) for f in b['families']})
    graph=dict(schema_version='0.1.0',battery_version=b['version'],battery_hash=plan['battery_hash'],model_configuration=cid,synthetic=bool(plan['config'].get('synthetic')),profile_catalog=catalog,nodes=list(nodes.values()),edges=edges)
    summary=dict(version=b['version'],quality=dict(collections.Counter(r['status'] for r in rows)),estimates=estimates,contrasts=contrasts,review_pending=sum(r['review_status']=='pending' for r in rows),warning='No latent trait scores, human norms, uncertainty intervals or empirical validity claims. Condition deltas are descriptive; repeats are not independent scenarios.')
    return rows,summary,graph,review
def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='command',required=True)
    a=sub.add_parser('prepare');a.add_argument('--config',required=True);a.add_argument('--run-id',required=True);a.add_argument('--repeats',type=int,default=4);a.add_argument('--out',required=True)
    a=sub.add_parser('process');a.add_argument('--plan',required=True);a.add_argument('--responses',required=True);a.add_argument('--out',required=True)
    args=p.parse_args();b=load();out=pathlib.Path(args.out);out.mkdir(parents=True,exist_ok=True)
    if args.command=='prepare':
        plan=prepare(b,read(args.config),args.run_id,args.repeats);write(out/'plan.json',plan)
        (out/'prompts.jsonl').write_text(''.join(json.dumps(dict(trial_id=t['trial_id'],config_id=plan['config_id'],messages=t['messages']),ensure_ascii=False)+'\n' for t in plan['trials']),encoding='utf-8')
        write(out/'response_record.example.json',dict(trial_id=plan['trials'][0]['trial_id'],config_id=plan['config_id'],status='ok',raw_response='REPLACE with unedited JSON response text'))
        print(f'Prepared {len(plan["trials"])} trials. No model calls made.')
    else:
        rows,summary,graph,review=score(b,read(args.plan),jsonl(args.responses));write(out/'scores.json',summary);write(out/'graph.json',graph)
        for name,data in [('trial_scores.jsonl',rows),('human_review.template.jsonl',review)]:
            (out/name).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in data),encoding='utf-8')
        print(json.dumps(summary['quality']))
if __name__=='__main__':main()
