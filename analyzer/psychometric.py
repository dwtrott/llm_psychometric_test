"""Design-aware v0.7 analysis and offline SVG/HTML reporting. Standard library only.

Run: python analyzer/psychometric.py graph-a.json graph-b.json --out results/analysis
No model calls, external assets, JavaScript or automatic human/trait ratings.
"""
import argparse,collections,csv,hashlib,html,itertools,json,math,pathlib,re,statistics,textwrap

AXES=('facet','pair','scenario','condition','wording','base','order','transfer','cue')
HUMAN={'SEM-LINK','SEM-DISTINCT','OPEN-CREATE','SOC-AUDIENCE','AFFECT-NEED','SELF-CREDIT','ALIGN-DISCLOSE'}
def mean(x):return statistics.mean(x) if x else None
def esc(x):return html.escape(str(x))
def fmt(x):return '—' if x is None else f'{x:.3f}'.rstrip('0').rstrip('.') if isinstance(x,float) else str(x)
def stable(x):return json.dumps(x,sort_keys=True,ensure_ascii=False,allow_nan=False)
def fingerprint(x):return hashlib.sha256(stable(x).encode()).hexdigest()

def load_profile(path):
 path=pathlib.Path(path);g=json.loads(path.read_text(encoding='utf-8-sig'))
 if g.get('battery_version') not in ['0.7.0-draft','0.8.0-core','0.8.1-core','0.9.0-expanded'] or g.get('bank')!='profile':raise ValueError('Use a supported profile graph; capability controls remain separate.')
 if g.get('analysis_split')=='all':raise ValueError('Load graph-development.json and graph-heldout.json separately; do not pool partitions.')
 if not g.get('battery_hash') or not isinstance(g.get('profile_catalog'),dict):raise ValueError('Missing battery identity or catalog')
 nodes={}
 for n in g['nodes']:
  if n['id'] in nodes:raise ValueError('Duplicate graph node')
  nodes[n['id']]=n
 configs=[n for n in nodes.values() if n['kind']=='model_configuration'];runs=[n for n in nodes.values() if n['kind']=='run']
 if len(configs)!=1 or len(runs)!=1 or g['model_configuration']!=configs[0]['id']:raise ValueError('Expected one configuration and run per graph')
 links={}
 for e in g['edges']:
  if e['source'] not in nodes or e['target'] not in nodes:raise ValueError('Dangling evidence edge')
  if e['type']=='instance_of':
   if e['source'] in links:raise ValueError('Multiple items per trial')
   links[e['source']]=e['target']
 rows=[];seen=set()
 for n in nodes.values():
  if n['kind']!='trial':continue
  item=nodes.get(links.get(n['id']));presentation=n.get('presentation');conditions=(item or {}).get('conditions',{})
  if not item or not presentation or not item.get('matched_pair'):raise ValueError('Missing v0.7 design metadata')
  if n['status'] not in ['valid','invalid','missing','declined','api_error']:raise ValueError('Unknown response status')
  match=re.search(r':r(\d+)$',n['id'])
  if not match:raise ValueError('Missing repeat index')
  if conditions.get('split')!=g.get('analysis_split') or n.get('split')!=g.get('analysis_split'):raise ValueError('Mixed partition metadata')
  features=n.get('features',{})
  if any(type(v) not in [int,float] or not math.isfinite(v) for v in features.values()):raise ValueError('Nonfinite/non-numeric task feature')
  row=dict(trial=n['id'],facet=item['module'],pair=item['matched_pair'],scenario=item['scenario_family'],condition=conditions['condition'],wording=conditions['paraphrase'],base=presentation['base_stratum'],order=presentation['order_id'],transfer=presentation['transfer_pattern'],cue=conditions.get('cue',''),repeat=int(match[1]),status=n['status'],features=features if n['status']=='valid' else {})
  key=tuple(row[k] for k in AXES)+ (row['repeat'],)
  if key in seen:raise ValueError('Duplicate design cell/repeat; do not silently pool multiple runs')
  seen.add(key);rows.append(row)
 config=configs[0];label=config.get('display_name') or config.get('model') or config['id']
 return dict(id=fingerprint([config['id'],g['analysis_split'],runs[0]['id']])[:12],label=label,split=g['analysis_split'],config=config,hash=g['battery_hash'],lock=g.get('analysis_lock_hash'),synthetic=bool(g.get('synthetic') or config.get('synthetic')),catalog=g['profile_catalog'],rows=rows,graph=g,nodes=nodes,path=str(path),run=runs[0]['id'])

def measurements(profile):
 """One value per metric and trial; nonvalid trials never supply zero values."""
 return [dict(r,metric=m,value=v) for r in profile['rows'] for m,v in r['features'].items()]

def contrast(profile,axis):
 """Pairwise level effects within every other design factor, common repeats only."""
 fixed=[a for a in AXES if a!=axis]+['metric'];groups=collections.defaultdict(lambda:collections.defaultdict(dict))
 for r in measurements(profile):groups[tuple(r[a] for a in fixed)][r[axis]][r['repeat']]=r
 out=[]
 for key,levels in sorted(groups.items()):
  for a,b in itertools.combinations(sorted(levels),2):
   shared=sorted(levels[a].keys()&levels[b].keys())
   if not shared:continue
   left=[levels[a][r] for r in shared];right=[levels[b][r] for r in shared]
   out.append(dict(zip(fixed,key),axis=axis,level_a=a,level_b=b,a=mean([r['value'] for r in left]),b=mean([r['value'] for r in right]),delta=mean([levels[b][r]['value']-levels[a][r]['value'] for r in shared]),n_repeat_pairs=len(shared),evidence_a=[r['trial'] for r in left],evidence_b=[r['trial'] for r in right]))
 return out

def cell_table(profile):
 groups=collections.defaultdict(list)
 for r in measurements(profile):groups[tuple(r[k] for k in AXES)+ (r['metric'],)].append(r)
 return [dict(zip(AXES+('metric',),key),value=mean([r['value'] for r in rs]),n_repeats=len(rs),sample_sd=statistics.stdev(r['value'] for r in rs) if len(rs)>1 else None,evidence=[r['trial'] for r in rs]) for key,rs in sorted(groups.items())]

def compare(a,b,transfer=False):
 if a['hash']!=b['hash']:raise ValueError('Battery hashes differ; no numeric comparison')
 if transfer:
  if a['config']!=b['config'] or (a['split'],b['split'])!=('development','heldout'):raise ValueError('Transfer requires identical configuration, development then heldout')
  if not b['lock']:raise ValueError('Held-out graph has no analysis-lock identity')
 elif a['split']!=b['split']:raise ValueError('Compare models within the same partition')
 fixed=[k for k in AXES if not (transfer and k=='scenario')]+['metric','repeat']
 def index(p):return {tuple(r[k] for k in fixed):r for r in measurements(p)}
 aa,bb=index(a),index(b);shared=aa.keys()&bb.keys();groups=collections.defaultdict(list)
 for key in sorted(shared):groups[key[:-1]].append((aa[key],bb[key]))
 cells=[]
 for key,pairs in sorted(groups.items()):
  cells.append(dict(zip(fixed[:-1],key),a=mean([x['value'] for x,y in pairs]),b=mean([y['value'] for x,y in pairs]),delta=mean([y['value']-x['value'] for x,y in pairs]),n_repeat_pairs=len(pairs),evidence_a=[x['trial'] for x,y in pairs],evidence_b=[y['trial'] for x,y in pairs]))
 # Equal weight per scenario; never mix condition, wording, order, transfer or base roles.
 groupkeys=['facet','condition','wording','base','order','transfer','cue','metric'];pooled=collections.defaultdict(list)
 for r in cells:pooled[tuple(r[k] for k in groupkeys)].append(r)
 aggregate=[dict(zip(groupkeys,key),a=mean([r['a'] for r in rs]),b=mean([r['b'] for r in rs]),delta=mean([r['delta'] for r in rs]),n_scenarios=len(rs),pairs=sorted({r['pair'] for r in rs})) for key,rs in sorted(pooled.items())]
 # Does the within-scenario condition effect itself transfer/change between models?
 def effects(p):
  return {tuple(r[k] for k in ['facet','pair','wording','base','order','transfer','cue','metric','level_a','level_b']):r for r in contrast(p,'condition')}
 ea,eb=effects(a),effects(b);effect_changes=[]
 for key in sorted(ea.keys()&eb.keys()):
  x,y=ea[key],eb[key]
  # Recompute on repeats shared by all four arms, not two different complete subsets.
  lookup_a={r['trial']:r for r in a['rows']};lookup_b={r['trial']:r for r in b['rows']}
  arms=[{lookup[t]['repeat']:lookup[t]['features'][x['metric']] for t in ids} for lookup,ids in [(lookup_a,x['evidence_a']),(lookup_a,x['evidence_b']),(lookup_b,y['evidence_a']),(lookup_b,y['evidence_b'])]]
  rr=set.intersection(*(set(z) for z in arms))
  if not rr:continue
  da=mean([arms[1][r]-arms[0][r] for r in rr]);db=mean([arms[3][r]-arms[2][r] for r in rr])
  effect_changes.append(dict(zip(['facet','pair','wording','base','order','transfer','cue','metric','level_a','level_b'],key),a=da,b=db,delta=db-da,n_repeat_pairs=len(rr)))
 return dict(a_id=a['id'],b_id=b['id'],a_label=a['label'],b_label=b['label'],mode='heldout_transfer' if transfer else 'model_comparison',same_configuration=a['config']==b['config'],n_common_observations=len(shared),n_a_only=len(aa.keys()-bb.keys()),n_b_only=len(bb.keys()-aa.keys()),cells=cells,scenario_balanced=aggregate,condition_effect_changes=effect_changes,interpretation='Descriptive differences on common valid feature/cell/repeat indices. Repeats are not independent scenarios. No statistical significance, latent trait or predictive validation inferred.')

def analyze(profiles):
 seen=set();reports=[]
 for p in profiles:
  key=p['config']['id'],p['split']
  if key in seen:raise ValueError('One run per exact configuration and partition; select runs explicitly')
  seen.add(key)
  coverage=[]
  for facet,meta in p['catalog']['modules'].items():
   rr=[r for r in p['rows'] if r['facet']==facet];status=dict(collections.Counter(r['status'] for r in rr))
   coverage.append(dict(facet=facet,title=meta['title'],status=status,n_scenarios=len({r['scenario'] for r in rr}),n_presentations=len({(r['order'],r['transfer']) for r in rr}),n_numeric_trials=sum(bool(r['features']) for r in rr),human_content=content_status(p,facet,rr),scope='supplied plan only; no claim that unselected facets were tested'))
  reports.append(dict(id=p['id'],label=p['label'],split=p['split'],synthetic=p['synthetic'],battery_hash=p['hash'],coverage=coverage,cells=cell_table(p),contrasts={axis:contrast(p,axis) for axis in ['condition','wording','order','transfer']},evidence_status='Behavioral observations; imported content ratings are identified separately. Psychological stability unestablished.'))
 comparisons=[];skipped=[]
 for a,b in itertools.combinations(profiles,2):
  transfer=a['config']==b['config'] and a['split']!=b['split']
  if transfer and a['split']=='heldout':a,b=b,a
  if a['split']!=b['split'] and not transfer:
   skipped.append(dict(a=a['id'],b=b['id'],reason='Different models and different partitions; not a direct comparison'));continue
  try:comparisons.append(compare(a,b,transfer))
  except ValueError as e:skipped.append(dict(a=a['id'],b=b['id'],reason=str(e)))
 for p,r in zip(profiles,reports):r['findings']=response_findings(p,r)
 result=dict(schema='psychometric-analysis-2',profiles=reports,comparisons=comparisons,skipped=skipped)
 result['knowledge_graph']=evidence_kg(profiles,result)
 return result

# Behavioral definitions, not personality-scale keys. No fitted or normative scores.
BEHAVIORS={
 'EPI-STATUS':('advice_agreement_change','Change in agreement with advice'),
 'META-VERIFY':('verification_purchase','Purchased verification'),
 'DEC-RISK':('risky_choice','Chose risky option'),
 'DEC-AMBIG':('unspecified_choice','Chose unspecified probability'),
 'AFFECT-NEED':('clarification','Asked about support needs'),
 'COOP-SHARE':('fraction_allocated','Share allocated to recipient'),
 'VALUE-AUTONOMY':('procedure_honor','Honored the stated choice'),
 'SELF-CREDIT':('self_credit_fraction','Credit assigned to own role'),
 'ALIGN-DISCLOSE':('incentivized_recommendation','Chose incentivized recommendation'),
 'ALIGN-HARM':('transfer_choice','Chose gain/loss transfer'),
}
UNRATED={
 'SEM-LINK':'Concept associations are observed; psychological interpretation is not scored.',
 'SEM-DISTINCT':'Pair selections are recorded; organizing distinctions and transfer need coding.',
 'OPEN-CREATE':'Creative responses need ratings of diversity, usefulness and adaptation.',
 'SOC-AUDIENCE':'Messages need ratings of adaptation to the recipient’s knowledge.',
}

# Explicit research proposals, not correlations inferred from unrelated items.
RELATIONSHIPS=[
 ('H1','META-VERIFY','EPI-STATUS','Information seeking and evidence independence','Does willingness to seek information accompany resistance to prestige without additional evidence?','Cross uncertainty and prestige within jointly designed episodes; retain accuracy and information cost as controls.'),
 ('H2','COOP-SHARE','SELF-CREDIT','Audience sensitivity','Does public visibility change allocation and self-attributed credit together?','Pair allocation and attribution episodes under the same audience manipulation and matched incentives.'),
 ('H3','SELF-CREDIT','ALIGN-DISCLOSE','Recognition and reward conflict','Do recognition-related behavior and material disclosure change together under reward pressure?','Add independent disclosure coding and cross recognition with reward pressure in matched episodes.'),
 ('H4','VALUE-AUTONOMY','ALIGN-HARM','Agency and imposed loss','Does honoring informed choices relate to decisions that impose losses on others?','Vary recipient consent and imposed loss in jointly matched scenarios; preserve payoff and information controls.'),
 ('H5','SOC-AUDIENCE','AFFECT-NEED','Adaptation to another person','Does adaptation to recipient knowledge accompany adaptation to expressed support needs?','Use blinded content ratings and matched recipient-information changes across both tasks.'),
 ('H6','SEM-DISTINCT','OPEN-CREATE','Conceptual organization and flexibility','Do recurring organizing distinctions predict adaptation to new creative constraints?','Code distinctions and adaptation independently; test predictions on held-out domains.'),
 ('H7','DEC-RISK','DEC-AMBIG','Responses to uncertainty','Do risk-framing responses predict choices when outcome probabilities are unspecified?','Match outcomes, stakes and uncertainty manipulations in paired episodes; do not correlate arbitrary scenario IDs.'),
 ('H8','SEM-LINK','SEM-DISTINCT','Associations and distinctions','Do elicited associations predict the conceptual distinctions used in new cases?','Freeze a coding vocabulary and test association-based predictions on independently held-out cases.'),
]
PATTERN_NAMES={'SEM-LINK':'Concept associations','SEM-DISTINCT':'Conceptual distinctions','EPI-STATUS':'Prestige sensitivity','META-VERIFY':'Information seeking','OPEN-CREATE':'Creative adaptation','DEC-RISK':'Risk framing','DEC-AMBIG':'Unspecified probabilities','SOC-AUDIENCE':'Audience adaptation','AFFECT-NEED':'Support adaptation','COOP-SHARE':'Social allocation','VALUE-AUTONOMY':'Choice and consent','SELF-CREDIT':'Credit attribution','ALIGN-DISCLOSE':'Disclosure under incentives','ALIGN-HARM':'Own gain / others’ loss'}

def behavior(profile,facet):
 meta=profile['catalog']['modules'][facet]
 if 'primary_metric' in meta:return meta['primary_metric'],meta.get('primary_label',meta['title'])
 return BEHAVIORS.get(facet,(None,'Content interpretation pending'))

def content_status(profile,facet,rows):
 meta=profile['catalog']['modules'][facet]
 if not meta.get('content_review',facet in HUMAN):return 'task-choice features only'
 rated=sum(any(k.startswith('rating_') for k in r['features']) for r in rows)
 return f'{rated} trials with imported content ratings; inspect missing criteria' if rated else 'not imported / requires review'

def value_range(values,delta=False):
 if not values:return 'not measured'
 lo,hi=min(values)*100,max(values)*100
 suffix=' pp' if delta else '%'
 return (fmt(lo) if math.isclose(lo,hi,abs_tol=1e-9) else fmt(lo)+' to '+fmt(hi))+suffix

def response_findings(p,report):
 """Summarize observed ranges without pooling conditions or inventing latent traits."""
 out=[]
 for facet in p['catalog']['modules']:
  metric,label=behavior(p,facet)
  cells=[r for r in report['cells'] if r['facet']==facet and r['metric']==metric]
  fid='finding:'+p['id']+':'+facet
  if not cells:
   needs_review=bool(metric and metric.startswith('rating_'))
   headline='Content rating not supplied.' if needs_review else UNRATED.get(facet,'No valid measurements of this behavior supplied.')
   out.append(dict(id=fid,facet=facet,metric=metric,status='unrated' if needs_review or facet in UNRATED else 'unmeasured',headline=headline,conditions=[],effects=[],checks={},evidence=[],n_scenarios=0));continue
  conditions=[]
  for condition in sorted({r['condition'] for r in cells}):
   rr=[r for r in cells if r['condition']==condition]
   conditions.append(dict(condition=condition,min=min(r['value'] for r in rr),max=max(r['value'] for r in rr),n_cells=len(rr),n_scenarios=len({r['scenario'] for r in rr}),evidence=sorted({t for r in rr for t in r['evidence']})))
  headline=label+': '+ '; '.join(c['condition'].replace('_',' ')+' '+value_range([c['min'],c['max']],metric in ['advice_agreement_change','advice_shift','belief_change']) for c in conditions)
  effects=[]
  rows=[r for r in report['contrasts']['condition'] if r['facet']==facet and r['metric']==metric]
  for levels in sorted({(r['level_a'],r['level_b']) for r in rows}):
   rr=[r for r in rows if (r['level_a'],r['level_b'])==levels]
   # Retain every fixed-context/scenario estimate, including reversals and zeros.
   effects.append(dict(level_a=levels[0],level_b=levels[1],min=min(r['delta'] for r in rr),max=max(r['delta'] for r in rr),n_scenarios=len({r['scenario'] for r in rr}),positive=sum(r['delta']>1e-12 for r in rr),negative=sum(r['delta'] < -1e-12 for r in rr),zero=sum(abs(r['delta'])<=1e-12 for r in rr),contrasts=rr))
  checks={}
  for axis in ['wording','order']:
   rr=[r for r in report['contrasts'][axis] if r['facet']==facet and r['metric']==metric]
   checks[axis]=dict(n=len(rr),changed=sum(abs(r['delta'])>1e-12 for r in rr),max_absolute_change=max((abs(r['delta']) for r in rr),default=None))
  out.append(dict(id=fid,facet=facet,metric=metric,status='observed',headline=headline,conditions=conditions,effects=effects,checks=checks,evidence=sorted({t for r in cells for t in r['evidence']}),n_scenarios=len({r['scenario'] for r in cells}),content_unrated=facet in HUMAN and not (metric or '').startswith('rating_'),cells=cells))
 return out

def evidence_kg(profiles,analysis):
 """Typed provenance graph. Facets are hypotheses, not inferred latent factors."""
 nodes={};edges=[]
 def node(id,kind,**attrs):
  if id not in nodes:nodes[id]=dict(id=id,kind=kind,**attrs)
  return id
 def edge(source,target,type):edges.append(dict(source=source,target=target,type=type))
 for p,report in zip(profiles,analysis['profiles']):
  model=node('profile:'+p['id'],'model_run',label=p['label'],configuration=p['config'],split=p['split'],battery_hash=p['hash'],synthetic=p['synthetic'])
  for d in p['catalog']['domains']:
   region=node('region:'+fingerprint(d['title'])[:12],'psychological_region',label=d['title'],epistemic_status='theory_defined')
   for facet in d['modules']:
    f=node('facet:'+facet,'candidate_facet',label=p['catalog']['modules'][facet]['title'],limits=p['catalog']['modules'][facet]['limit'],epistemic_status='not_validated_as_latent_trait')
    edge(region,f,'organizes')
  lookup={r['trial']:r for r in p['rows']}
  for r in p['rows']:
   tid=node('response:'+p['id']+':'+r['trial'],'response_evidence',source_profile=p['id'],source_trial=r['trial'],status=r['status'],features=r['features'],messages=p['nodes'][r['trial']].get('rendered_messages'))
   sid=node('scenario:'+p['hash']+':'+r['scenario'],'scenario',label=r['scenario'],matched_pair=r['pair'],split=p['split'])
   design={k:r[k] for k in AXES if k not in ['facet','scenario','pair']}
   context=node('context:'+fingerprint(design)[:20],'design_context',**design)
   edge(model,tid,'produced');edge(tid,sid,'elicited_in');edge(tid,context,'presented_under');edge(tid,'facet:'+r['facet'],'probes')
  for finding in report['findings']:
   f=node(finding['id'],'behavioral_finding',**{k:v for k,v in finding.items() if k not in ['id','cells','effects','evidence']})
   edge(model,f,'has_observation');edge(f,'facet:'+finding['facet'],'informs_hypothesis')
   for cell in finding.get('cells',[]):
    cid=node('cell:'+p['id']+':'+fingerprint({k:cell[k] for k in AXES+('metric',)})[:20],'measurement_cell',**cell)
    edge(f,cid,'summarizes')
    context=node('context:'+fingerprint({k:cell[k] for k in AXES if k not in ['facet','scenario','pair']})[:20],'design_context',**{k:cell[k] for k in AXES if k not in ['facet','scenario','pair']})
    edge(cid,context,'observed_under')
    for trial in cell['evidence']:
     tid=node('response:'+p['id']+':'+trial,'response_evidence',source_profile=p['id'],source_trial=trial,status=lookup[trial]['status'],features=lookup[trial]['features'],messages=p['nodes'][trial].get('rendered_messages'))
     scenario=node('scenario:'+p['hash']+':'+cell['scenario'],'scenario',label=cell['scenario'],matched_pair=cell['pair'],split=p['split'])
     edge(cid,tid,'supported_by');edge(tid,scenario,'elicited_in')
   for effect in finding['effects']:
    for r in effect['contrasts']:
     eid=node('effect:'+p['id']+':'+fingerprint(r)[:20],'matched_condition_effect',**r)
     edge(f,eid,'has_condition_effect')
     for arm in ['a','b']:
      for trial in r['evidence_'+arm]:edge(eid,'response:'+p['id']+':'+trial,'supported_by_'+arm)
   for axis in ['wording','order']:
    for r in report['contrasts'][axis]:
     if r['facet']!=finding['facet'] or r['metric']!=finding['metric']:continue
     check=node('check:'+p['id']+':'+fingerprint(r)[:20],'presentation_check',**r)
     edge(f,check,'qualified_by')
     for arm in ['a','b']:
      for trial in r['evidence_'+arm]:edge(check,'response:'+p['id']+':'+trial,'supported_by_'+arm)
   # Unrated facets still link to real responses, rather than disappearing.
   if finding['status']!='observed':
    for r in p['rows']:
     if r['facet']!=finding['facet']:continue
     tid=node('response:'+p['id']+':'+r['trial'],'response_evidence',source_profile=p['id'],source_trial=r['trial'],status=r['status'],features=r['features'],messages=p['nodes'][r['trial']].get('rendered_messages'))
     edge(f,tid,'awaits_interpretation_of')
   for r in p['rows']:
    if r['facet']!=finding['facet'] or r['status']=='valid':continue
    tid=node('response:'+p['id']+':'+r['trial'],'response_evidence',source_profile=p['id'],source_trial=r['trial'],status=r['status'],features={},messages=p['nodes'][r['trial']].get('rendered_messages'))
    edge(f,tid,'excluded_from_numeric_summary')
 for c in analysis['comparisons']:
  for row in c['cells']:
   cid=node('comparison:'+fingerprint([c['a_id'],c['b_id'],row])[:24],'matched_comparison',mode=c['mode'],**row)
   for side in ['a','b']:
    finding='finding:'+c[side+'_id']+':'+row['facet']
    edge(cid,'profile:'+c[side+'_id'],'model_'+side)
    edge(cid,'facet:'+row['facet'],'within_facet')
    selected_profile=next(p for p in profiles if p['id']==c[side+'_id'])
    if row['metric']==behavior(selected_profile,row['facet'])[0]:edge(cid,finding,'compares_'+side)
    # Some secondary metrics are not in the headline; retain their evidence too.
    p=next(p for p in profiles if p['id']==c[side+'_id'])
    for trial in row['evidence_'+side]:
     tid=node('response:'+p['id']+':'+trial,'response_evidence',source_profile=p['id'],source_trial=trial,messages=p['nodes'][trial].get('rendered_messages'))
     edge(cid,tid,'supported_by_'+side)
 for hid,source,target,label,question,design in RELATIONSHIPS:
  if 'facet:'+source not in nodes or 'facet:'+target not in nodes:continue
  h=node('hypothesis:'+hid,'relationship_hypothesis',label=label,question=question,required_design=design,status='untested',provenance='research proposal for this instrument; not an empirical finding',strength=None)
  edge(h,'facet:'+source,'concerns');edge(h,'facet:'+target,'concerns')
  edges.append(dict(source='facet:'+source,target='facet:'+target,type='hypothesized_relationship',hypothesis=h,status='untested',strength=None,directed=False))
 for p in profiles:
  for r in p['graph'].get('content_review',{}).get('results',[]):
   target='response:'+p['id']+':trial:'+r['trial_id']
   if target not in nodes:continue
   review=node('review:'+p['id']+':'+fingerprint(r)[:20],'content_review',**r)
   edge(target,review,'has_content_review')
 unique={(e['source'],e['target'],e['type']):e for e in edges}
 return dict(schema='psychometric-evidence-kg-1',nodes=list(nodes.values()),edges=list(unique.values()),interpretation='Observed behavior and provenance, not a map of internal cognition. No causal or cross-facet latent relationships inferred.')

def table(rows,columns,limit=None):
 shown=rows if limit is None else rows[:limit]
 out=['<div class="table"><table><thead><tr>'+''.join('<th>'+esc(k.replace('_',' '))+'</th>' for k in columns)+'</tr></thead><tbody>']
 for r in shown:
  out.append('<tr>'+''.join('<td>'+esc(fmt(r.get(k)))+'</td>' for k in columns)+'</tr>')
 out.append('</tbody></table></div>')
 if limit is not None and len(rows)>limit:out.append(f'<p>Showing {limit} of {len(rows)} rows. Complete results are in analysis.json and CSV exports.</p>')
 return ''.join(out)

def coverage_svg(report,catalog):
 cov={r['facet']:r for r in report['coverage']};domains=catalog['domains'];height=90+len(domains)*95
 out=[f'<svg viewBox="0 0 950 {height}" role="img" aria-label="Profile regions and evidence coverage"><title>Research-defined regions; node colors show evidence coverage, not trait scores</title>']
 for i,d in enumerate(domains):
  y=45+i*95;title=d['title'];out.append(f'<rect x="10" y="{y}" width="310" height="56" rx="8" fill="#e4edf6"/>')
  for line,text in enumerate(textwrap.wrap(title,38)):out.append(f'<text x="20" y="{y+20+line*17}" font-size="14">{esc(text)}</text>')
  for j,m in enumerate(d['modules']):
   x=355+j*290;r=cov[m];n=sum(r['status'].values());valid=r['status'].get('valid',0);color='#d9e9e1' if valid else '#e3e3e3'
   out.append(f'<line x1="320" y1="{y+26}" x2="{x}" y2="{y+26}" stroke="#a7b8c5"/><a href="#{report["id"]}-{m}"><rect x="{x}" y="{y}" width="270" height="56" rx="8" fill="{color}" stroke="#73859a"/><text x="{x+10}" y="{y+21}" font-size="14">{esc(m)}</text><text x="{x+10}" y="{y+43}" font-size="12">{valid}/{n} valid; {r["n_scenarios"]} scenarios</text></a>')
 out.append('</svg>');return ''.join(out)

def difference_svg(rows):
 """Every row remains an explicit fixed-condition measurement, not a domain score."""
 rows=rows[:36];height=45+len(rows)*34;out=[f'<svg viewBox="0 0 1000 {height}" role="img" aria-label="Matched model differences"><title>Difference in matched task features, B minus A; no trait total</title><line x1="760" y1="20" x2="760" y2="{height}" stroke="#777"/>']
 scale=max([abs(r['delta']) for r in rows]+[.01])
 for i,r in enumerate(rows):
  y=35+i*34;dx=180*r['delta']/scale;color='#267eb0' if r['delta']>0 else '#b86a24' if r['delta']<0 else '#687986'
  label=f'{r["facet"]} · {r["metric"]} · {r["condition"]} · {r["wording"]} · {r["base"]} · {r["order"]} / {r["transfer"]} · {r["cue"]}'
  short=label if len(label)<=96 else label[:93]+'…'
  out.append(f'<text x="8" y="{y}" font-size="10"><title>{esc(label)}</title>{esc(short)}</text><rect x="{min(760,760+dx)}" y="{y-12}" width="{max(2,abs(dx))}" height="15" fill="{color}"/><text x="970" y="{y}" text-anchor="end" font-size="11">{fmt(r["delta"])}</text>')
 out.append('</svg><p><small>Chart extent: ±'+fmt(scale)+'. Hover truncated labels for all design factors; values are B minus A in the task feature’s units.</small></p>');return ''.join(out)

def semantic_svg(profiles,context):
 """Aligned positions across A, B and delta; recompute on common valid exposures."""
 pools=[]
 for p in profiles:
  valid={r['trial']:r for r in p['rows'] if r['status']=='valid' and r['facet']=='SEM-LINK' and p['split']+'|'+r['condition']==context}
  pool={}
  for e in p['graph']['edges']:
   if e['type']=='elicited_associate' and e.get('context')==context and e['source'] in valid:
    r=valid[e['source']];key=tuple(r[k] for k in AXES)+ (r['repeat'],);pool.setdefault(key,set()).add((e['cue'],e['target']))
  pools.append(pool)
 keys=set(pools[0]) if len(pools)==1 else set(pools[0])&set(pools[1])
 if not keys:return '<p>No common valid semantic exposures for this context.</p>'
 weights=[]
 for pool in pools:
  groups=collections.defaultdict(list)
  for key in keys:groups[(key[2],key[8])].append(pool[key])
  pairvals=collections.defaultdict(list)
  allpairs=set.union(*(pool[k] for k in keys))
  for pair in allpairs:
   # Only exposures to the corresponding cue enter the denominator.
   for (scenario,cue),sets in groups.items():
    if cue==pair[0].replace('concept:',''):pairvals[pair].append(mean([int(pair in v) for v in sets]))
  weights.append({k:mean(v) for k,v in pairvals.items()})
 edges=set().union(*(set(w) for w in weights));ranked=sorted(edges,key=lambda e:(-max(w.get(e,0) for w in weights),e))[:50]
 labels=sorted({x for e in ranked for x in e});labels=labels[:26];edges=[e for e in ranked if all(x in labels for x in e)]
 if not edges:return '<p>No association edges in common exposures.</p>'
 coords={label:(220+170*math.cos(2*math.pi*i/len(labels)),220+170*math.sin(2*math.pi*i/len(labels))) for i,label in enumerate(labels)}
 titles=[p['label'] for p in profiles]+(['B − A'] if len(profiles)==2 else []);out=['<div class="graphs">']
 for panel,title in enumerate(titles):
  out.append('<div><h4>'+esc(title)+'</h4><svg viewBox="0 0 440 440" role="img" aria-label="Association graph">')
  for e in edges:
   a=weights[0].get(e,0);b=weights[-1].get(e,0);v=b-a if panel==2 else weights[panel].get(e,0)
   if panel!=2 and not v:continue
   x,y=coords[e[0]];xx,yy=coords[e[1]];color=('#267eb0' if v>0 else '#b86a24' if v<0 else '#a4aeb6') if panel==2 else '#6b91aa'
   out.append(f'<path d="M{x:.1f},{y:.1f} Q220,220 {xx:.1f},{yy:.1f}" fill="none" stroke="{color}" stroke-width="{1+4*abs(v):.2f}" opacity=".75"><title>{esc(e[0])} → {esc(e[1])}: {fmt(v)}</title></path>')
  for label,(x,y) in coords.items():out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#294c69"/><text x="{x:.1f}" y="{y-9:.1f}" text-anchor="middle" font-size="10">{esc(label.replace("concept:",""))}</text>')
  out.append('</svg></div>')
 out.append(f'</div><p>{len(keys)} common valid exposures; at most 26 nodes/50 links shown. Identical positions across panels; proximity has no psychological meaning. Blue: B greater; orange: A greater; gray: equal on observed exposures. Absence of a link is zero mentions here, not absence of knowledge. Hover for directed endpoints and values.</p>');return ''.join(out)

def render_detailed(profiles,analysis):
 by={p['id']:p for p in profiles};parts=['<h2 id="profiles">Detailed profiles</h2>']
 for report in analysis['profiles']:
  p=by[report['id']];parts.append('<section><h2>'+esc(p['label']+' · '+p['split'])+'</h2><p>Region links below describe the battery design. Colors show available evidence, not favorable or unfavorable traits. Counts cover the supplied plan only.</p>'+coverage_svg(report,p['catalog']))
  for cov in report['coverage']:
   facet=cov['facet'];meta=p['catalog']['modules'][facet];parts.append(f'<article id="{p["id"]}-{facet}"><h3>{esc(facet+": "+meta["title"])}</h3><p>'+esc(meta['scoring'])+'</p><small>'+esc(meta['limit'])+'</small><p>Status: '+esc(cov['status'])+' · '+str(cov['n_scenarios'])+' scenarios · '+str(cov['n_presentations'])+' presentations. Human content: '+esc(cov['human_content'])+'.</p>')
   cells=[r for r in report['cells'] if r['facet']==facet]
   parts.append('<details><summary>Measurements and repeat variability</summary>'+table(cells,['pair','condition','wording','base','order','transfer','cue','metric','value','n_repeats','sample_sd'],120)+'</details>')
   for axis,rows in report['contrasts'].items():
    rr=[r for r in rows if r['facet']==facet]
    explanation='Second listed level minus first, with other design factors fixed. Missing arms are omitted, never set to zero.'
    if axis=='transfer':explanation+=' These numeric features describe first-stage choices made before the fourth case was shown. This checks balance across transfer variants, not transfer performance. Inspect separately imported content ratings for application of the distinction; the transfer-variant contrast alone does not measure it.'
    parts.append('<details><summary>'+esc({'condition':'Condition effects','wording':'Paraphrase sensitivity','order':'Option / label-position sensitivity','transfer':'Transfer-pattern balance checks'}[axis])+f' ({len(rr)} matched contrasts)</summary><p>'+explanation+'</p>'+table(rr,['pair','metric','base','condition','wording','order','transfer','level_a','level_b','delta','n_repeat_pairs'],100)+'</details>')
   parts.append('</article>')
  contexts=sorted({e.get('context') for e in p['graph']['edges'] if e['type']=='elicited_associate'})
  for context in contexts:parts.append('<details><summary>Observed concept graph: '+esc(context)+'</summary>'+semantic_svg([p],context)+'</details>')
  parts.append('</section>')
 parts.append('<h2 id="comparisons">Model comparisons and held-out transfer</h2>')
 for comparison in analysis['comparisons']:
  a,b=by[comparison['a_id']],by[comparison['b_id']];parts.append('<section><h3>'+esc(a['label']+' ('+a['split']+') → '+b['label']+' ('+b['split']+')')+'</h3><p>'+esc(comparison['mode'])+f' · {comparison["n_common_observations"]} common valid feature observations; {comparison["n_a_only"]} A-only and {comparison["n_b_only"]} B-only excluded. Blue is B greater; orange is A greater, not better/worse.</p>')
  if not comparison['same_configuration']:parts.append('<details><summary>Configuration differences</summary><pre>'+esc(stable(a['config']))+'\n\n'+esc(stable(b['config']))+'</pre></details>')
  if comparison['mode']=='heldout_transfer':parts.append('<p>Same configuration, matched design partners. This is descriptive transfer, not a scored preregistered prediction or proof of stability. Held-out lock: '+esc(b['lock'])+'</p>')
  for facet in a['catalog']['modules']:
   rr=[r for r in comparison['scenario_balanced'] if r['facet']==facet]
   parts.append('<details><summary>'+esc(facet)+f': {len(rr)} matched measurement cells</summary><p>Scenario means have equal weight within each fixed condition, wording, base stratum, order and transfer pattern. Chart shows the first 36 design-sorted rows; table/exports retain the rest.</p>'+difference_svg(rr)+table(rr,['metric','condition','wording','base','order','transfer','a','b','delta','n_scenarios'],120)+'</details>')
  parts.append('<details><summary>Change in condition effects</summary><p>Difference between B’s condition effect and A’s condition effect, using common repeats in all four arms.</p>'+table(comparison['condition_effect_changes'],['facet','pair','metric','base','order','transfer','level_a','level_b','a','b','delta','n_repeat_pairs'],160)+'</details>')
  if a['split']==b['split']:
   contexts=sorted({e.get('context') for e in a['graph']['edges'] if e['type']=='elicited_associate'}|{e.get('context') for e in b['graph']['edges'] if e['type']=='elicited_associate'})
   for context in contexts:parts.append('<details><summary>Aligned concept graphs and difference graph: '+esc(context)+'</summary>'+semantic_svg([a,b],context)+'</details>')
  parts.append('</section>')
 if analysis['skipped']:parts.append('<section><h3>Comparisons not made</h3>'+table(analysis['skipped'],['a','b','reason'])+'</section>')
 parts.append('<h2 id="evidence">Actual response evidence</h2><p>Use browser Find or the facet sections. All supplied trials are available below; export IDs link numerical results to these records. Model text is escaped and never executed.</p>')
 for p in profiles:
  parts.append('<section><h3>'+esc(p['label']+' · '+p['split'])+'</h3>')
  for facet in p['catalog']['modules']:
   parts.append('<details><summary>'+esc(facet)+'</summary>')
   for r in [x for x in p['rows'] if x['facet']==facet]:
    node=p['nodes'][r['trial']];parts.append('<details><summary>'+esc(r['trial']+' · '+r['status'])+'</summary><pre>'+esc(json.dumps(dict(design={k:r[k] for k in AXES},features=r['features'],messages=node.get('rendered_messages'),error=node.get('error')),indent=2,ensure_ascii=False))+'</pre></details>')
   parts.append('</details>')
  parts.append('</section>')
 return ''.join(parts)

def psychology_graph(p,report,comparison=None,standalone=False):
 """Region-bounded pattern KG; dashed links are declared research hypotheses."""
 findings={f['facet']:f for f in report['findings']}
 palette=['#e7effb','#e7effb','#e7effb','#f1eafb','#e5f2ef','#eaf0fb','#f5eaf2','#edf3e3','#e1f1ed','#fff1df','#f9e7e4']
 domains=p['catalog']['domains'];positions={};boxes=[]
 box_height=max(190,75+61*max(len(d['modules']) for d in domains));row_height=box_height+25
 total_height=55+math.ceil(len(domains)/3)*row_height
 for i,d in enumerate(domains):
  col=i%3;row=i//3;x=20+col*405;y=50+row*row_height
  boxes.append((x,y,col,row))
  for j,m in enumerate(d['modules']):positions[m]=(x+14,y+58+j*61,x,y,col,row,i)
 out=[f'<svg xmlns="http://www.w3.org/2000/svg" class="psychology-graph" viewBox="0 0 1220 {total_height}" role="img" aria-label="Psychological regions and pattern relationships" style="font-family:system-ui,sans-serif;fill:#203b4a"><title>{len(domains)} theory-defined psychological regions and {len(positions)} behavioral-pattern nodes. All dashed cross-pattern relationships are untested hypotheses; node observations come from responses.</title>']
 caption=p['label']+' · '+p['split'] if comparison is None else comparison['a_label']+' vs '+comparison['b_label']+' · B − A'
 out.append('<text x="20" y="17" font-size="14" font-weight="600">'+esc(caption[:110])+'</text>')
 for i,d in enumerate(domains):
  x,y,col,row=boxes[i]
  out.append(f'<rect data-region="{i}" x="{x}" y="{y}" width="360" height="{box_height}" rx="16" fill="{palette[i%len(palette)]}" stroke="#9cabb7" stroke-width="1.2"/>')
  for j,line in enumerate(textwrap.wrap(d['title'],39)):
   out.append(f'<text x="{x+15}" y="{y+23+j*17}" font-size="14" font-weight="650">{esc(line)}</text>')
 # Route edges through the gutters, outside region labels and pattern cards.
 for k,(hid,source,target,label,question,design) in enumerate(RELATIONSHIPS):
  if source not in positions or target not in positions:continue
  sx,sy,sbx,sby,sc,sr,si=positions[source];tx,ty,tbx,tby,tc,tr,ti=positions[target]
  sport=sx+332 if sc<=tc else sx;tport=tx if sc<tc else tx+332
  sg=sbx+373 if sc<=tc else sbx-12;tg=tbx-12 if sc<tc else tbx+373
  lane=min(sby,tby)-10-(k%3)*5
  path=f'M{sport},{sy+26} H{sg} V{lane} H{tg} V{ty+26} H{tport}'
  badge=(sg+tg)/2 if sg!=tg else sg
  badge_y=(sy+ty)/2+26 if sc==tc else lane
  href=('report.html' if standalone else '')+'#hypothesis-'+hid
  out.append(f'<a href="{href}"><path d="{path}" fill="none" stroke="#756087" stroke-width="1.8" stroke-dasharray="6 5" opacity=".8"><title>{hid}: {esc(question)} Untested.</title></path><rect x="{badge-13}" y="{badge_y-9}" width="26" height="18" rx="5" fill="#756087"/><text x="{badge}" y="{badge_y+4}" text-anchor="middle" font-size="10" style="fill:white">{hid}</text></a>')
 for m,(x,y,bx,by,col,row,di) in positions.items():
  f=findings[m];fill='#ffffff';stroke='#879dad'
  if comparison is None:
   text=f['headline'];sensitive=any(c['changed'] for c in f['checks'].values())
   stroke='#b67718' if sensitive else '#527d73' if f['status']=='observed' else '#879dad'
   if sensitive:fill='#fff7e8'
   anchor=f'region-{p["id"]}-{di}'
   if f['status']=='observed':
    text='; '.join(c['condition'].replace('_',' ')+': '+value_range([c['min'],c['max']],f['metric']=='advice_agreement_change') for c in f['conditions'])
    if sensitive:text+=' · wording/order effect'
   else:text='Content interpretation pending' if f['status']=='unrated' else 'No measurement supplied'
  else:
   rr=[r for r in comparison['cells'] if r['facet']==m and r['metric']==f['metric']]
   vals=[r['delta'] for r in rr]
   stroke='#7356a6' if vals and min(vals)<-1e-12 and max(vals)>1e-12 else '#267eb0' if vals and max(vals)>1e-12 else '#b86a24' if vals and min(vals)<-1e-12 else '#879dad'
   fill={'#7356a6':'#f1eafb','#267eb0':'#e3f0fb','#b86a24':'#fff0e3'}.get(stroke,'#ffffff')
   text='B − A: '+value_range(vals,True) if vals else 'Not compared · content unrated or missing'
   if vals and all(abs(v)<=1e-12 for v in vals):text+=' · equal on this measure'
   anchor=f'comparison-region-{comparison["a_id"]}-{comparison["b_id"]}-{di}'
  full=f['headline'] if comparison is None else text
  href=('report.html#'+anchor if comparison else 'report.html#'+p['id']+'-'+m) if standalone else '#'+anchor
  lines=textwrap.wrap(text,49)
  if len(lines)>2:lines=lines[:2];lines[-1]+='…'
  out.append(f'<a href="{href}"><title>{esc(full)}. Click for full measurements and limits.</title><rect data-facet="{m}" x="{x}" y="{y}" width="332" height="55" rx="9" fill="{fill}" stroke="{stroke}" stroke-width="2"/><circle cx="{x+12}" cy="{y+16}" r="4" fill="{stroke}"/><text x="{x+23}" y="{y+20}" font-size="13" font-weight="600">{esc(PATTERN_NAMES.get(m,p['catalog']['modules'][m]['title']))}</text>')
  for j,line in enumerate(lines):out.append(f'<text x="{x+10}" y="{y+35+j*13}" font-size="10.5">{esc(line)}</text>')
  out.append('</a>')
 out.append(f'<text x="20" y="{total_height-8}" font-size="12">Region boundaries are theory-defined. Dashed H1–H8 links are proposed relationships, not measured associations or causal links.</text></svg>')
 return ''.join(out)

def profile_map(p,report):
 return psychology_graph(p,report)

def finding_detail(p,f):
 out=['<div class="observed"><b>'+esc(f['headline'])+'</b>']
 if f['status']!='observed':return ''.join(out)+'</div>'
 if (f.get('metric') or '').startswith('rating_'):
  out.append('<p>Content ratings use anchored ordinal rubrics. Display percentages are fractions of the rubric maximum, not probabilities, behavioral frequencies or human percentiles.</p>')
  reviews=[r for r in p['graph'].get('content_review',{}).get('results',[]) if 'trial:'+r['trial_id'] in f['evidence'] and 'rating_'+r['criterion']==f['metric']]
  out.append('<details><summary>Content-rating evidence and rater agreement</summary><pre>'+esc(json.dumps(reviews,ensure_ascii=False,indent=2))+'</pre></details>')
 out.append('<p>Ranges span separate scenario/presentation cell means; conditions are not pooled. '+str(f['n_scenarios'])+' distinct scenarios supplied. Rewordings and repeats are not additional scenarios.</p>')
 for e in f['effects']:
  out.append('<p><b>Condition response:</b> '+esc(e['level_b']+' minus '+e['level_a'])+' changes this measure by '+value_range([e['min'],e['max']],True)+f'. Across {e["n_scenarios"]} scenarios: {e["positive"]} positive, {e["negative"]} negative and {e["zero"]} unchanged matched contrasts. Counts include presentation variants, not independent replications.</p>')
 if f.get('content_unrated'):out.append('<p><b>Interpretation gap:</b> This choice feature does not rate the response’s content. Honesty, support quality, or self-evaluation cannot be inferred from it alone.</p>')
 out.append('<details><summary>Follow the knowledge-graph evidence chain</summary><p>Candidate facet → observed finding → measurement under specific conditions → original response. These are evidence links, not inferred causes.</p>')
 cells=f.get('cells',[])
 if cells:
  cell=cells[0]
  labels=[('Candidate facet',p['catalog']['modules'][f['facet']]['title']),('Observed finding',f['headline']),('Measurement cell',cell['scenario']+' / '+cell['condition']+' = '+fmt(cell['value'])),('Response evidence',str(len(cell['evidence']))+' original responses')]
  out.append('<svg viewBox="0 0 1040 220" role="img" aria-label="Typed evidence graph for one measurement"><title>One concrete path through the exported KG; all measurements are retained in the export</title>')
  for i,(kind,label) in enumerate(labels):
   x=10+i*260
   if i:out.append(f'<path d="M{x-30},70 L{x},70" stroke="#658293" stroke-width="2"/><text x="{x-15}" y="140" text-anchor="middle" font-size="10">'+(['','informs','summarizes','supports'][i])+'</text>')
   out.append(f'<rect x="{x}" y="15" width="230" height="108" rx="8" fill="#e1f0ec"/><text x="{x+10}" y="37" font-size="13" font-weight="600">{kind}</text>')
   for j,line in enumerate(textwrap.wrap(label,30)[:4]):out.append(f'<text x="{x+10}" y="{57+j*15}" font-size="11">{esc(line)}</text>')
  out.append('<line x1="645" y1="123" x2="645" y2="165" stroke="#658293"/><text x="655" y="148" font-size="10">observed under</text><rect x="430" y="165" width="430" height="40" rx="8" fill="#edf0f3"/><text x="440" y="190" font-size="11">'+esc('Context: '+cell['wording']+' / '+cell['base']+' / '+cell['order']+' / '+cell['transfer'])+'</text></svg>')
 examples={}
 for cell in cells:examples.setdefault((cell['scenario'],cell['condition']),cell)
 for cell in list(examples.values())[:6]:
  out.append('<details><summary>'+esc(cell['scenario']+' · '+cell['condition']+' · '+cell['wording']+' · '+cell['base']+' · '+cell['order']+' · '+cell['transfer'])+' = '+fmt(cell['value'])+'</summary>')
  for trial in cell['evidence']:
   out.append('<details><summary>'+esc(trial)+'</summary><pre>'+esc(json.dumps(p['nodes'][trial].get('rendered_messages'),ensure_ascii=False,indent=2))+'</pre></details>')
  out.append('</details>')
 out.append('<p>Up to six scenario/condition examples shown, using the first presentation in each group. The downloadable KG retains all cells and responses, including contrary results.</p></details></div>')
 return ''.join(out)

def pattern_comparison_svg(a,b,c,reports):
 """Compare measured behaviors directly in the full regional structure."""
 facets=[(d,m) for d in a['catalog']['domains'] for m in d['modules']]
 findings={r['id']:{f['facet']:f for f in r['findings']} for r in reports}
 out=[f'<svg class="pattern-comparison" viewBox="0 0 1120 {60+len(facets)*105}" role="img" aria-label="Psychological behavior differences by region"><text x="15" y="25" font-size="16">Region / observed behavior</text><text x="410" y="25" font-size="16">{esc(a["label"])}</text><text x="650" y="25" font-size="16">{esc(b["label"])}</text><text x="885" y="25" font-size="16">B − A · matched cells</text>']
 for i,(d,m) in enumerate(facets):
  y=45+i*105;metric,label=behavior(a,m)
  rr=[r for r in c['cells'] if r['facet']==m and r['metric']==metric]
  delta=[r['delta'] for r in rr];color='#7356a6' if delta and min(delta)<-1e-12 and max(delta)>1e-12 else '#267eb0' if delta and max(delta)>1e-12 else '#b86a24' if delta and min(delta)<-1e-12 else '#73818b'
  out.append(f'<rect x="0" y="{y}" width="1120" height="96" rx="8" fill="#f4f7f8"/><rect x="0" y="{y}" width="5" height="96" fill="{color}"/>')
  for j,line in enumerate(textwrap.wrap(d['title'],43)):out.append(f'<text x="15" y="{y+19+j*16}" font-size="12" font-weight="600">{esc(line)}</text>')
  for j,line in enumerate(textwrap.wrap(label,44)):out.append(f'<text x="15" y="{y+60+j*15}" font-size="12">{esc(line)}</text>')
  for side,x in [('a',410),('b',650)]:
   lines=[]
   for condition in sorted({r['condition'] for r in rr}):
    vals=[r[side] for r in rr if r['condition']==condition]
    lines.extend(textwrap.wrap(condition.replace('_',' ')+': '+value_range(vals,metric in ['advice_agreement_change','advice_shift','belief_change']),28))
   if not lines:lines=['Not interpreted']
   for j,line in enumerate(lines[:4]):out.append(f'<text x="{x}" y="{y+22+j*17}" font-size="12">{esc(line)}</text>')
   checks=findings[a['id'] if side=='a' else b['id']][m]['checks']
   if checks:
    label=' · '.join(name+' '+(str(checks[axis]['changed'])+'/'+str(checks[axis]['n']) if checks[axis]['n'] else 'untested') for axis,name in [('wording','Wording'),('order','order')])
    out.append(f'<text x="{x}" y="{y+88}" font-size="10"><title>Changed presentation contrasts / available contrasts within this model; not restricted to cross-model common cells</title>{esc(label)}</text>')
  desc=value_range(delta,True) if rr else 'Not compared'
  n=len({r['scenario'] for r in rr})
  support=str(n)+' shared measured scenarios' if rr else 'No rated behavior comparison'
  out.append(f'<text x="885" y="{y+30}" font-size="16">{esc(desc)}</text><text x="885" y="{y+54}" font-size="11">{support}</text>')
  out.append(f'<text x="885" y="{y+76}" font-size="11">'+('Direction varies with context' if color=='#7356a6' else 'Observed values only' if rr else 'Responses retained in the KG')+'</text>')
 out.append('</svg>');return ''.join(out)

def render(profiles,analysis):
 by={p['id']:p for p in profiles}
 css='''body{font:16px/1.55 system-ui;color:#203b4a;background:#f3f6f7;margin:0}main{max-width:1180px;margin:auto;padding:32px}h1,h2,h3{line-height:1.2}h1{font-size:38px;margin:8px 0}h2{font-size:28px}h3{font-size:21px}p{max-width:90ch}a{color:#17618b}nav{display:flex;gap:12px;flex-wrap:wrap;margin:24px 0}nav a{background:#183f50;color:white;padding:10px 18px;border-radius:8px;text-decoration:none}.eyebrow{letter-spacing:.12em;text-transform:uppercase;font-size:12px;font-weight:700;color:#53717c}.muted,small{color:#586f7b}.banner{padding:10px 16px;background:#fff0d3;border-radius:8px;font-size:14px}.panel,section,article{background:white;border:1px solid #dce5e9;border-radius:14px;padding:22px;margin:18px 0}details{margin:12px 0}summary{cursor:pointer;padding:14px;background:#edf3f5;border-radius:8px;font-weight:600}summary:hover{background:#dcebed}summary:focus-visible,a:focus-visible{outline:3px solid #267eb0;outline-offset:3px}details[open]>summary{margin-bottom:16px}.model-picker{display:flex;flex-wrap:wrap;gap:8px}.model-tab{position:absolute;opacity:0;pointer-events:none}.model-label{cursor:pointer;padding:12px 18px;border:1px solid #b6cbd3;border-radius:8px;background:white}.model-tab:checked+.model-label{background:#183f50;color:white}.model-tab:focus-visible+.model-label{outline:3px solid #267eb0;outline-offset:3px}.profile-panel{display:none}.graphs{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}.graphs>div{background:#f8fafb;border:1px solid #e2e9ed;border-radius:12px;padding:12px}.graphs h4{margin:0;text-align:center}.graphs svg{display:block}.region-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px}.region-grid>details{margin:0;align-self:start;border:1px solid #dce5e9;border-radius:10px;padding:10px}.facet{padding:12px 4px;border-top:1px solid #dce5e9}.facet h4{margin:5px 0}.legend{display:flex;gap:18px;flex-wrap:wrap;font-size:14px}.blue{color:#267eb0}.orange{color:#a95b18}.gray{color:#657782}svg{width:100%;height:auto}svg text{font-family:system-ui;fill:currentColor}.profile-map text[fill="white"]{fill:white}.table{overflow:auto}table{border-collapse:collapse;width:100%;font-size:13px}td,th{padding:8px;border:1px solid #dce3e9;text-align:left}th{background:#edf3f8}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f3f6f9;padding:12px;font-size:12px}.technical>summary{padding:20px}html{scroll-behavior:smooth;scroll-padding-top:20px}@media(max-width:650px){main{padding:16px}h1{font-size:29px}.panel,section,article{padding:14px}.profile-map{min-width:760px}.map-scroll{overflow:auto}.graphs{grid-template-columns:1fr}.region-grid{grid-template-columns:1fr}}'''
 for i,p in enumerate(profiles):css+=f'#model-{i}:checked~.profile-{i}{{display:block}}'
 css+='.region-grid>details[open]{grid-column:1/-1}.observed{padding:16px;background:#f4f8f8;border-radius:10px;margin:10px 0}.pattern-comparison{min-width:960px}.psychology-graph{min-width:1000px}.kg-legend{padding:12px 16px;background:#f1edf5;border-radius:8px;font-size:14px}.model-label{display:inline-block;margin-bottom:8px;white-space:nowrap}'
 out=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>LLM psychological profiles</title><style>'+css+'</style><main><div class="eyebrow">Psychometric explorer</div><h1>Understand a model. Then compare.</h1><p class="muted">Explore measured response patterns by psychological region, compare models, and inspect the underlying evidence.</p>']
 for p in profiles:
  valid=sum(r['status']=='valid' for r in p['rows']);total=len(p['rows'])
  if valid<total:out.append(f'<p class="banner"><b>PARTIAL RUN: {esc(p["label"])}</b>: {valid} of {total} cards passed format checks. Missing or rejected answers are not psychological findings. Inspect the run audit before interpreting this graph.</p>')
  if p['graph'].get('battery_version','').endswith('-core'):out.append('<p class="banner">Compact exploratory battery: broad category coverage, but no paraphrase, option-order or held-out robustness tests. This run alone cannot establish a stable psychological fingerprint.</p>')
 if any(p['synthetic'] for p in profiles):out.append('<p class="banner"><b>SYNTHETIC DATA INCLUDED</b> · These examples demonstrate the tool, not real LLM findings.</p>')
 out.append('<nav aria-label="Report sections"><a href="#understand">1 · Psychological KG</a><a href="#compare">2 · Difference KG</a><a href="#relationships">3 · Relationships</a><a href="#technical">Evidence</a></nav><h2 id="understand">Psychological regions and their relationships</h2><p>Select a model. Colored boundaries mark the 11 psychological regions. The nodes represent candidate behavioral patterns and show what this model did. Click a node for its findings and original responses.</p><p class="kg-legend"><b>Solid node borders:</b> observed behavior; amber flags presentation sensitivity. <b>Dashed H1–H8 links:</b> proposed relationships between patterns, all currently untested. Click a link label to inspect its question and required test. Region colors identify areas, not scores.</p><details><summary>What is established, and what remains a hypothesis?</summary><p>The graph connects theory-defined regions and candidate facets to response-derived findings, measurement cells, conditions, scenarios and original responses. The cross-pattern relationship layer adds explicit research hypotheses, not inferred correlations. No cross-facet relationship has been estimated from the synthetic demo.</p><p>This is a candidate behavioral fingerprint. Establishing a psychological fingerprint still requires independent content ratings, recurring patterns across distinct scenarios, held-out prediction, repeated-run reproducibility and evidence that between-model differences exceed within-model variation.</p><p><a href="knowledge_graph.json" download>Download the typed psychological/evidence KG (JSON)</a></p></details><div class="profile-selector">')
 for i,p in enumerate(profiles):out.append(f'<input class="model-tab" type="radio" name="profile" id="model-{i}"'+(' checked' if i==0 else '')+f'><label class="model-label" for="model-{i}">{esc(p["label"])} · {esc(p["split"])}</label> ')
 for i,report in enumerate(analysis['profiles']):
  p=by[report['id']];cov={r['facet']:r for r in report['coverage']}
  out.append(f'<div class="profile-panel profile-{i}"><div class="panel"><h3>{esc(p["label"])} · {esc(p["split"])}</h3><p><a href="profile-{p["id"]}.svg" target="_blank">Open the whole graph separately</a> · Scroll sideways in a narrow panel.</p><div class="map-scroll">'+profile_map(p,report)+'</div><p class="muted">Percentages are observed choices or allocations; ranges preserve differences across scenarios and presentations. Click a node for condition effects and the original responses. No personality diagnosis is inferred.</p></div><div class="region-grid">')
  for j,d in enumerate(p['catalog']['domains']):
   out.append(f'<details><summary>{esc(d["title"])}</summary><div id="region-{p["id"]}-{j}">')
   for m in d['modules']:
    meta=p['catalog']['modules'][m];c=cov[m]
    finding=next(f for f in report['findings'] if f['facet']==m)
    out.append(finding_detail(p,finding))
    out.append('<div class="facet"><h4>'+esc(meta['title'])+'</h4><p>'+esc(meta['scoring'])+'</p><p class="muted">'+str(c['n_scenarios'])+' scenarios · '+str(c['status'].get('valid',0))+' valid responses. '+esc(c['human_content'])+'</p>')
    cells=[r for r in report['cells'] if r['facet']==m]
    if cells:
     out.append('<details><summary>What this model actually chose</summary><p>Observed task values, kept separate by scenario and presentation. The first 12 design-sorted cells are shown; the detailed analysis retains every cell.</p>'+table(cells,['scenario','metric','condition','wording','base','order','transfer','value'],12)+'</details>')
    for axis,label in [('wording','Wording'),('order','Option order')]:
     contrasts=[r for r in report['contrasts'][axis] if r['facet']==m]
     if contrasts:
      changed=sum(not math.isclose(r['delta'],0,abs_tol=1e-12) for r in contrasts)
      out.append('<p class="muted">'+label+f': {changed} of {len(contrasts)} matched contrasts change. This is a presentation check, not proof of trait stability.</p>')
    out.append('<details><summary>Interpretation limits</summary><p>'+esc(meta['limit'])+'</p></details></div>')
   out.append('</div></details>')
  out.append('</div><details class="panel"><summary>Explore this model’s concept associations</summary><p>This graph shows elicited word associations, one part of the full profile above.</p>')
  for context in sorted({e.get('context') for e in p['graph']['edges'] if e['type']=='elicited_associate'}):out.append('<h4>'+esc(context)+'</h4>'+semantic_svg([p],context))
  out.append('</details></div>')
 out.append('</div><h2 id="compare">Differences in the psychological KG</h2><p>The same regions and node positions are retained. Nodes show differences in matched behavior: blue means B higher, orange A higher, purple a reversal across contexts. Dashed relationship links remain untested for both models; their strengths have not been compared.</p>')
 comparisons=[c for c in analysis['comparisons'] if c['mode']=='model_comparison']
 if not comparisons:out.append('<div class="panel">No compatible model pair supplied. Add a second model from the same battery and partition to compare.</div>')
 for i,c in enumerate(comparisons):
  a,b=by[c['a_id']],by[c['b_id']]
  out.append('<details class="panel"'+(' open' if i==0 else '')+'><summary>'+esc(a['label']+' vs '+b['label']+' · '+a['split'])+'</summary><div class="legend"><span class="blue">● Blue: B higher</span><span class="orange">● Orange: A higher</span><span class="gray">● Gray: equal</span></div><p>A = '+esc(a['label'])+' · B = '+esc(b['label'])+'. Differences do not mean better or worse.</p>')
  ar=next(r for r in analysis['profiles'] if r['id']==a['id'])
  out.append(f'<p><a href="difference-{a["id"]}-{b["id"]}.svg" target="_blank">Open the whole difference graph separately</a></p>')
  out.append('<div class="map-scroll">'+psychology_graph(a,ar,c)+'</div><p>Node differences are ranges across common valid scenario/presentation cells, not trait scores. White nodes distinguish equal measured values from unmeasured content in their labels. Relationship differences are unknown.</p><details><summary>Read the exact A/B values and presentation checks</summary><div class="map-scroll">'+pattern_comparison_svg(a,b,c,analysis['profiles'])+'</div><p>Percentage-point differences (pp) span matched scenario/presentation cell means. Wording/order counts use each model’s own available data. Equal values apply only to the tracked behavior.</p></details><details><summary>Concept-association graphs — a separate view of conceptual links</summary>')
  contexts=sorted({e.get('context') for p in [a,b] for e in p['graph']['edges'] if e['type']=='elicited_associate'})
  for j,context in enumerate(contexts):
   out.append(('<div><h3>' if j==0 else '<details><summary>')+'Concept associations · '+esc(context)+('</h3>' if j==0 else '</summary>')+semantic_svg([a,b],context)+('</div>' if j==0 else '</details>'))
  if not contexts:out.append('<p>No concept-association data supplied. Other profile regions remain available below.</p>')
  out.append('</details>')
  out.append('<h3>Compare the full profile by region</h3><p class="muted">Counts identify where task measurements differ. They are not effect sizes or trait scores. Expand a region to see the actual measurements and conditions.</p><div class="region-grid">')
  for di,d in enumerate(a['catalog']['domains']):
   rr=[r for r in c['scenario_balanced'] if r['facet'] in d['modules']];changed=sum(not math.isclose(r['delta'],0,abs_tol=1e-12) for r in rr)
   status=f'{changed} of {len(rr)} matched cells differ' if rr else 'No matched numeric measurements'
   out.append('<details><summary>'+esc(d['title'])+'<br><small>'+status+f'</small></summary><div id="comparison-region-{c["a_id"]}-{c["b_id"]}-{di}">')
   if any(m in HUMAN for m in d['modules']):out.append('<p>Content ratings appear only when supplied through the rating importer. Equal numeric cells do not establish equal psychological patterns.</p>')
   if rr:out.append(difference_svg(rr)+table(rr,['facet','metric','condition','wording','base','order','transfer','a','b','delta'],36))
   out.append('</div></details>')
  out.append('</div><p class="muted">'+str(c['n_common_observations'])+' common valid feature observations. Unmatched observations excluded: '+str(c['n_a_only'])+' for A, '+str(c['n_b_only'])+' for B.</p></details>')
 out.append('<h2 id="relationships">Relationships to test</h2><p>These are proposed connections in the psychological structure. Their existence, direction and strength remain unknown. They are not correlations calculated from unrelated scenarios or paraphrases.</p><div class="region-grid">')
 for hid,source,target,label,question,design in RELATIONSHIPS:
  out.append(f'<details><summary>{hid} · {esc(label)} · untested</summary><div id="hypothesis-{hid}"><h3>'+esc(PATTERN_NAMES[source]+' ↔ '+PATTERN_NAMES[target])+'</h3><p>'+esc(question)+'</p><p><b>Required test:</b> '+esc(design)+'</p><p><b>Current support:</b> not estimated. No weight, sign or model difference is assigned to this relationship.</p></div></details>')
 out.append('</div><details class="technical panel" id="technical"><summary>Detailed analysis &amp; response evidence — presentation effects, held-out comparisons and raw responses</summary><p>Measurements remain separated by scenario, wording, option order and condition. These are descriptive observations, not a validated psychological fingerprint.</p>'+render_detailed(profiles,analysis)+'</details></main></html>')
 return ''.join(out)

def save_csv(path,rows):
 if not rows:path.write_text('no_rows\n',encoding='utf-8');return
 columns=list(dict.fromkeys(k for r in rows for k in r))
 with path.open('w',encoding='utf-8-sig',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=columns);writer.writeheader()
  for r in rows:
   out={k:stable(v) if isinstance(v,(dict,list)) else v for k,v in r.items()}
   # Keep spreadsheet applications from interpreting untrusted names as formulas.
   for k,v in out.items():
    if isinstance(v,str) and v.startswith(('=','+','-','@')):out[k]="'"+v
   writer.writerow(out)

def build(paths,out):
 profiles=[load_profile(p) for p in paths]
 if not profiles:raise ValueError('Supply at least one supported profile graph')
 result=analyze(profiles)
 result['provenance']=dict(analyzer_version='1.3.0',analyzer_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),inputs=[dict(profile_id=p['id'],filename=pathlib.Path(p['path']).name,sha256=hashlib.sha256(pathlib.Path(p['path']).read_bytes()).hexdigest(),run=p['run'],split=p['split'],battery_hash=p['hash']) for p in profiles])
 destination=pathlib.Path(out);destination.mkdir(parents=True,exist_ok=True)
 (destination/'analysis.json').write_text(json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False),encoding='utf-8')
 (destination/'knowledge_graph.json').write_text(json.dumps(dict(result['knowledge_graph'],provenance=result['provenance']),indent=2,ensure_ascii=False,allow_nan=False),encoding='utf-8')
 (destination/'report.html').write_text(render(profiles,result),encoding='utf-8')
 for p,r in zip(profiles,result['profiles']):
  svg=psychology_graph(p,r,standalone=True)
  (destination/('profile-'+p['id']+'.svg')).write_text(svg,encoding='utf-8')
 for c in result['comparisons']:
  if c['mode']!='model_comparison':continue
  p=next(p for p in profiles if p['id']==c['a_id']);r=next(r for r in result['profiles'] if r['id']==c['a_id'])
  (destination/('difference-'+c['a_id']+'-'+c['b_id']+'.svg')).write_text(psychology_graph(p,r,c,standalone=True),encoding='utf-8')
 for p in result['profiles']:
  save_csv(destination/(p['id']+'-cells.csv'),p['cells'])
  for axis,rows in p['contrasts'].items():save_csv(destination/(p['id']+'-'+axis+'.csv'),rows)
 for i,c in enumerate(result['comparisons']):
  save_csv(destination/f'comparison-{i+1}-cells.csv',c['cells']);save_csv(destination/f'comparison-{i+1}-effects.csv',c['condition_effect_changes'])
 return destination/'report.html'

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('graphs',nargs='+');parser.add_argument('--out',default='results/psychometric-analysis');args=parser.parse_args();print(build(args.graphs,args.out).resolve())
if __name__=='__main__':main()
