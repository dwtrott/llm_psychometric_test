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
 if g.get('battery_version')!='0.7.0-draft' or g.get('bank')!='profile':raise ValueError('Use v0.7 profile graphs; older instruments and capability controls remain in the legacy viewer.')
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
   coverage.append(dict(facet=facet,title=meta['title'],status=status,n_scenarios=len({r['scenario'] for r in rr}),n_presentations=len({(r['order'],r['transfer']) for r in rr}),n_numeric_trials=sum(bool(r['features']) for r in rr),human_content='not imported / requires review' if facet in HUMAN else 'task-choice features only',scope='supplied plan only; no claim that unselected facets were tested'))
  reports.append(dict(id=p['id'],label=p['label'],split=p['split'],synthetic=p['synthetic'],battery_hash=p['hash'],coverage=coverage,cells=cell_table(p),contrasts={axis:contrast(p,axis) for axis in ['condition','wording','order','transfer']},evidence_status='Behavioral observations only. Human ratings are not imported; psychological stability unestablished.'))
 comparisons=[];skipped=[]
 for a,b in itertools.combinations(profiles,2):
  transfer=a['config']==b['config'] and a['split']!=b['split']
  if transfer and a['split']=='heldout':a,b=b,a
  if a['split']!=b['split'] and not transfer:
   skipped.append(dict(a=a['id'],b=b['id'],reason='Different models and different partitions; not a direct comparison'));continue
  try:comparisons.append(compare(a,b,transfer))
  except ValueError as e:skipped.append(dict(a=a['id'],b=b['id'],reason=str(e)))
 return dict(schema='psychometric-analysis-1',profiles=reports,comparisons=comparisons,skipped=skipped)

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
    if axis=='transfer':explanation+=' These numeric features describe first-stage choices made before the fourth case was shown. This checks balance across transfer variants, not transfer performance. Application of the distinction requires human-coded evidence, which is not imported here.'
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

def profile_map(p,report):
 """Compact full-profile map: regions are design links, never inferred traits."""
 cov={r['facet']:r for r in report['coverage']}
 out=['<svg class="profile-map" viewBox="0 0 1100 630" role="img" aria-label="Full psychological profile map"><title>Full profile: regions connect to the model; color shows evidence availability, not trait strength</title>']
 domains=p['catalog']['domains']
 for i,d in enumerate(domains):
  side=i%2;row=i//2;x=20 if side==0 else 730;y=16+row*102
  valid=sum(cov[m]['status'].get('valid',0) for m in d['modules'])
  numeric=sum(cov[m]['n_numeric_trials'] for m in d['modules'])
  color='#e1f0ec' if numeric else '#fff0d9' if valid else '#edf0f3'
  out.append(f'<path d="M550,305 Q550,{y+40} {x+350 if side==0 else x},{y+40}" fill="none" stroke="#bbcbd6" stroke-width="2"/>')
  out.append(f'<a href="#region-{p["id"]}-{i}"><rect x="{x}" y="{y}" width="350" height="82" rx="12" fill="{color}" stroke="#b0c6c8"/>')
  for j,line in enumerate(textwrap.wrap(d['title'],36)):
   out.append(f'<text x="{x+15}" y="{y+24+j*18}" font-size="15" font-weight="600">{esc(line)}</text>')
  status='Task measurements available' if numeric else 'Responses awaiting interpretation' if valid else 'No valid responses supplied'
  out.append(f'<text x="{x+15}" y="{y+69}" font-size="12" fill="#526979">{status}</text></a>')
 out.append('<circle cx="550" cy="305" r="77" fill="#183f50"/>')
 for j,line in enumerate(textwrap.wrap(p['label'],17)[:3]):out.append(f'<text x="550" y="{290+j*20}" text-anchor="middle" fill="white" font-size="16">{esc(line)}</text>')
 out.append('</svg>')
 return ''.join(out)

def render(profiles,analysis):
 by={p['id']:p for p in profiles}
 css='''body{font:16px/1.55 system-ui;color:#203b4a;background:#f3f6f7;margin:0}main{max-width:1180px;margin:auto;padding:32px}h1,h2,h3{line-height:1.2}h1{font-size:38px;margin:8px 0}h2{font-size:28px}h3{font-size:21px}p{max-width:90ch}a{color:#17618b}nav{display:flex;gap:12px;flex-wrap:wrap;margin:24px 0}nav a{background:#183f50;color:white;padding:10px 18px;border-radius:8px;text-decoration:none}.eyebrow{letter-spacing:.12em;text-transform:uppercase;font-size:12px;font-weight:700;color:#53717c}.muted,small{color:#586f7b}.banner{padding:10px 16px;background:#fff0d3;border-radius:8px;font-size:14px}.panel,section,article{background:white;border:1px solid #dce5e9;border-radius:14px;padding:22px;margin:18px 0}details{margin:12px 0}summary{cursor:pointer;padding:14px;background:#edf3f5;border-radius:8px;font-weight:600}summary:hover{background:#dcebed}summary:focus-visible,a:focus-visible{outline:3px solid #267eb0;outline-offset:3px}details[open]>summary{margin-bottom:16px}.model-picker{display:flex;flex-wrap:wrap;gap:8px}.model-tab{position:absolute;opacity:0;pointer-events:none}.model-label{cursor:pointer;padding:12px 18px;border:1px solid #b6cbd3;border-radius:8px;background:white}.model-tab:checked+.model-label{background:#183f50;color:white}.model-tab:focus-visible+.model-label{outline:3px solid #267eb0;outline-offset:3px}.profile-panel{display:none}.graphs{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}.graphs>div{background:#f8fafb;border:1px solid #e2e9ed;border-radius:12px;padding:12px}.graphs h4{margin:0;text-align:center}.graphs svg{display:block}.region-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px}.region-grid>details{margin:0;align-self:start;border:1px solid #dce5e9;border-radius:10px;padding:10px}.facet{padding:12px 4px;border-top:1px solid #dce5e9}.facet h4{margin:5px 0}.legend{display:flex;gap:18px;flex-wrap:wrap;font-size:14px}.blue{color:#267eb0}.orange{color:#a95b18}.gray{color:#657782}svg{width:100%;height:auto}svg text{font-family:system-ui;fill:currentColor}.profile-map text[fill="white"]{fill:white}.table{overflow:auto}table{border-collapse:collapse;width:100%;font-size:13px}td,th{padding:8px;border:1px solid #dce3e9;text-align:left}th{background:#edf3f8}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f3f6f9;padding:12px;font-size:12px}.technical>summary{padding:20px}html{scroll-behavior:smooth;scroll-padding-top:20px}@media(max-width:650px){main{padding:16px}h1{font-size:29px}.panel,section,article{padding:14px}.profile-map{min-width:760px}.map-scroll{overflow:auto}.graphs{grid-template-columns:1fr}.region-grid{grid-template-columns:1fr}}'''
 for i,p in enumerate(profiles):css+=f'#model-{i}:checked~.profile-{i}{{display:block}}'
 out=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>LLM psychological profiles</title><style>'+css+'</style><main><div class="eyebrow">Psychometric explorer · v0.7</div><h1>Understand a model. Then compare.</h1><p class="muted">Explore the full psychological profile, see where models differ, and inspect the evidence when you need it.</p>']
 if any(p['synthetic'] for p in profiles):out.append('<p class="banner"><b>SYNTHETIC DATA INCLUDED</b> · These examples demonstrate the tool, not real LLM findings.</p>')
 out.append('<nav aria-label="Report sections"><a href="#understand">1 · Understand a model</a><a href="#compare">2 · Compare models</a><a href="#technical">3 · Inspect evidence</a></nav><h2 id="understand">The full psychological profile</h2><p>Select a model. The map covers every region of the battery; choose a region to learn what its questions measure. Color indicates available evidence, not a personality score.</p><div class="profile-selector">')
 for i,p in enumerate(profiles):out.append(f'<input class="model-tab" type="radio" name="profile" id="model-{i}"'+(' checked' if i==0 else '')+f'><label class="model-label" for="model-{i}">{esc(p["label"])} · {esc(p["split"])}</label> ')
 for i,report in enumerate(analysis['profiles']):
  p=by[report['id']];cov={r['facet']:r for r in report['coverage']}
  out.append(f'<div class="profile-panel profile-{i}"><div class="panel"><h3>{esc(p["label"])} · {esc(p["split"])}</h3><div class="map-scroll">'+profile_map(p,report)+'</div><p class="muted">Read this as a map of measured questions, not established traits. Response content that needs human interpretation remains unrated.</p></div><div class="region-grid">')
  for j,d in enumerate(p['catalog']['domains']):
   out.append(f'<details><summary>{esc(d["title"])}</summary><div id="region-{p["id"]}-{j}">')
   for m in d['modules']:
    meta=p['catalog']['modules'][m];c=cov[m]
    out.append('<div class="facet"><h4>'+esc(meta['title'])+'</h4><p>'+esc(meta['scoring'])+'</p><p class="muted">'+str(c['n_scenarios'])+' scenarios · '+str(c['status'].get('valid',0))+' valid responses. '+('Content interpretation still needs human review.' if m in HUMAN else 'Task-choice measurements available; no validated trait score.')+'</p>')
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
 out.append('</div><h2 id="compare">Where do models differ?</h2><p>Compare the same questions under matched conditions. The graphs show concept associations; the region summaries below cover the broader psychological profile.</p>')
 comparisons=[c for c in analysis['comparisons'] if c['mode']=='model_comparison']
 if not comparisons:out.append('<div class="panel">No compatible model pair supplied. Add a second model from the same battery and partition to compare.</div>')
 for i,c in enumerate(comparisons):
  a,b=by[c['a_id']],by[c['b_id']]
  out.append('<details class="panel"'+(' open' if i==0 else '')+'><summary>'+esc(a['label']+' vs '+b['label']+' · '+a['split'])+'</summary><div class="legend"><span class="blue">● Blue: B higher</span><span class="orange">● Orange: A higher</span><span class="gray">● Gray: equal</span></div><p>A = '+esc(a['label'])+' · B = '+esc(b['label'])+'. Differences do not mean better or worse.</p>')
  contexts=sorted({e.get('context') for p in [a,b] for e in p['graph']['edges'] if e['type']=='elicited_associate'})
  for j,context in enumerate(contexts):
   out.append(('<div><h3>' if j==0 else '<details><summary>')+'Concept associations · '+esc(context)+('</h3>' if j==0 else '</summary>')+semantic_svg([a,b],context)+('</div>' if j==0 else '</details>'))
  if not contexts:out.append('<p>No concept-association data supplied. Other profile regions remain available below.</p>')
  out.append('<h3>Compare the full profile by region</h3><p class="muted">Counts identify where task measurements differ. They are not effect sizes or trait scores. Expand a region to see the actual measurements and conditions.</p><div class="region-grid">')
  for d in a['catalog']['domains']:
   rr=[r for r in c['scenario_balanced'] if r['facet'] in d['modules']];changed=sum(not math.isclose(r['delta'],0,abs_tol=1e-12) for r in rr)
   status=f'{changed} of {len(rr)} matched cells differ' if rr else 'No matched numeric measurements'
   out.append('<details><summary>'+esc(d['title'])+'<br><small>'+status+'</small></summary>')
   if any(m in HUMAN for m in d['modules']):out.append('<p>Content requiring human review is not scored here. Equal numeric cells do not establish equal psychological patterns.</p>')
   if rr:out.append(difference_svg(rr)+table(rr,['facet','metric','condition','wording','base','order','transfer','a','b','delta'],36))
   out.append('</details>')
  out.append('</div><p class="muted">'+str(c['n_common_observations'])+' common valid feature observations. Unmatched observations excluded: '+str(c['n_a_only'])+' for A, '+str(c['n_b_only'])+' for B.</p></details>')
 out.append('<details class="technical panel" id="technical"><summary>Detailed analysis &amp; response evidence — presentation effects, held-out comparisons and raw responses</summary><p>Measurements remain separated by scenario, wording, option order and condition. These are descriptive observations, not a validated psychological fingerprint.</p>'+render_detailed(profiles,analysis)+'</details></main></html>')
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
 if not profiles:raise ValueError('Supply at least one v0.7 graph')
 result=analyze(profiles)
 result['provenance']=dict(analyzer_version='1.0.0',analyzer_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),inputs=[dict(profile_id=p['id'],filename=pathlib.Path(p['path']).name,sha256=hashlib.sha256(pathlib.Path(p['path']).read_bytes()).hexdigest(),run=p['run'],split=p['split'],battery_hash=p['hash']) for p in profiles])
 destination=pathlib.Path(out);destination.mkdir(parents=True,exist_ok=True)
 (destination/'analysis.json').write_text(json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False),encoding='utf-8')
 (destination/'report.html').write_text(render(profiles,result),encoding='utf-8')
 for p in result['profiles']:
  save_csv(destination/(p['id']+'-cells.csv'),p['cells'])
  for axis,rows in p['contrasts'].items():save_csv(destination/(p['id']+'-'+axis+'.csv'),rows)
 for i,c in enumerate(result['comparisons']):
  save_csv(destination/f'comparison-{i+1}-cells.csv',c['cells']);save_csv(destination/f'comparison-{i+1}-effects.csv',c['condition_effect_changes'])
 return destination/'report.html'

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('graphs',nargs='+');parser.add_argument('--out',default='results/psychometric-analysis');args=parser.parse_args();print(build(args.graphs,args.out).resolve())
if __name__=='__main__':main()
