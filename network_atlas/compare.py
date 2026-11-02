"""A/B interaction prototype. All differences are invented, not model findings."""
import json,xml.etree.ElementTree as ET
import build as b

S='http://www.w3.org/2000/svg'
ET.register_namespace('',S)
def key(a,c):return tuple(sorted((a,c)))
def names(a,c):return key(b.index[a]['id'],b.index[c]['id'])
A={key(e['source'],e['target']):e for e in b.EDGES}
REMOVE=[('Evidence seeking','Verification'),('Audience sensitivity','Resource sharing'),('Responsibility','Material disclosure'),('Autonomy protection','Imposed loss'),('Distinction reuse','Constraint adaptation'),('Confidence calibration','Risk preference')]
ADD=[('Evidence seeking','Uncertainty tolerance'),('Audience sensitivity','Oversight sensitivity'),('Recognition seeking','Material disclosure'),('Rule flexibility','Imposed loss'),('Analogy use','Constraint adaptation'),('Confidence calibration','Decision deferral')]
B=dict(A)
for pair in REMOVE:del B[names(*pair)]
for pair in ADD:
 a,c=names(*pair);assert (a,c) not in A
 B[(a,c)]=dict(source=a,target=c,kind='bridge',status='illustrative_only',weight=None)
UNION=A|B
SHARED=A.keys()&B.keys();ONLY_A=A.keys()-B.keys();ONLY_B=B.keys()-A.keys()
CHANGED={n for e in ONLY_A|ONLY_B for n in e}

def neighbors(edges,n):return sorted(c if a==n else a for a,c in edges if n in [a,c])
def render(view,standalone=False):
 root=ET.fromstring(b.svg())
 texts=root.findall(f'{{{S}}}text')
 texts[0].text={'a':'Illustrative graph A','b':'Illustrative graph B','difference':'Difference landscape · illustrative A vs B'}[view]
 root.set('aria-label',texts[0].text+'; fixed node positions; no empirical model data')
 extra=ET.SubElement(root,f'{{{S}}}text',{'x':'30','y':'86','font-size':'16','fill':'#465c67'})
 extra.text=f'Gray: {len(SHARED)} shared links · Orange dashed: {len(ONLY_A)} A-only · Blue solid: {len(ONLY_B)} B-only · Rings: changed neighborhoods' if view=='difference' else 'Same 66 variables and positions in both examples. Click a node to explore its connections.'
 group=root.find(f'{{{S}}}g')
 for e in list(group):
  if 'edge' in e.attrib.get('class','').split():group.remove(e)
 edges={'a':A,'b':B,'difference':UNION}[view]
 for i,(k,e) in enumerate(sorted(edges.items())):
  a,c=(b.BY[n] for n in k)
  status='shared' if k in SHARED else 'only-a' if k in ONLY_A else 'only-b'
  color=('#adb7be' if status=='shared' else '#bb6a25' if status=='only-a' else '#287db7') if view=='difference' else '#8a7b9f' if e['kind']=='bridge' else a['color']
  attributes={'class':f'edge e-{status} touch-{a["id"]} touch-{c["id"]}', 'data-source':a['id'],'data-target':c['id'],'x1':str(a['x']),'y1':str(a['y']),'x2':str(c['x']),'y2':str(c['y']),'stroke':color,'stroke-width':'3.2' if view=='difference' and status!='shared' else '1.4','opacity':'.9' if view=='difference' and status!='shared' else '.32'}
  if view=='difference' and status=='only-a':attributes['stroke-dasharray']='8 5'
  line=ET.Element(f'{{{S}}}line',attributes)
  ET.SubElement(line,f'{{{S}}}title').text=f'{a["label"]} — {c["label"]}: {status}; illustrative, not measured'
  group.insert(len(b.REGIONS)+i,line)
 for node in group.findall(f'{{{S}}}a'):
  nid=node.attrib['href'][1:]
  adjacent=neighbors(edges,nid)
  node.set('class','node '+('changed ' if nid in CHANGED else 'unchanged ')+' '.join('near-'+v for v in [nid]+adjacent))
  if standalone:node.set('href','network-comparison.html#'+nid)
  if view=='difference' and nid in CHANGED:
   n=b.BY[nid]
   ring=ET.Element(f'{{{S}}}circle',{'cx':str(n['x']),'cy':str(n['y']),'r':'11','fill':'none','stroke':'#5e5677','stroke-width':'2','class':'change-ring'})
   node.insert(1,ring)
 return ET.tostring(root,encoding='unicode')

def links(ns):
 return '<ul>'+''.join(f'<li><a href="#{n}">{b.esc(b.BY[n]["label"])}</a></li>' for n in ns)+'</ul>' if ns else '<p>None in this example.</p>'

def page():
 css='''body{font:16px/1.5 system-ui,sans-serif;background:#fafbf9;color:#263b43;margin:0}header{padding:22px 26px 0}h1{font-size:26px;margin:0}header p{color:#75551e;margin:8px 0}.controls{display:flex;gap:8px;flex-wrap:wrap;padding:12px 26px;align-items:center}.controls input[type=radio]{position:absolute;opacity:0}.tab{display:inline-block;padding:9px 16px;border:1px solid #bdcbd0;border-radius:8px;background:white;cursor:pointer}.controls input:checked+.tab{background:#23434e;color:white}.controls input:focus-visible+.tab{outline:3px solid #4a80a0}.view,.facts{display:none}.app:has(#view-a:checked) .view-a,.app:has(#view-a:checked) .facts-a,.app:has(#view-b:checked) .view-b,.app:has(#view-b:checked) .facts-b,.app:has(#view-difference:checked) .view-difference,.app:has(#view-difference:checked) .facts-difference{display:block}.layout{display:grid;grid-template-columns:minmax(0,1fr) 290px;gap:20px;padding:12px 26px}svg{width:100%;height:auto}aside{position:sticky;top:20px;align-self:start;background:white;border:1px solid #d9e1df;border-radius:12px;padding:18px}.detail{display:none}.detail:target{display:block}.layout:has(.detail:target) .default{display:none}a{color:#365b85}h2{font-size:20px;margin-top:0}h3{font-size:16px;margin-bottom:6px}li{margin:5px 0}.notice{color:#75551e;font-size:14px}.node:hover circle{stroke-width:2.5}.legend{font-size:14px}.orange{color:#a45b20}.blue{color:#246eaa}.shared-control{margin-left:10px}.app:not(:has(#view-difference:checked)) .shared-control{display:none}.app:has(#show-shared:not(:checked)) .view-difference .e-shared{display:none}.app:has(#show-shared:not(:checked)) .view-difference .unchanged{opacity:.18}footer{padding:20px 26px;font-size:14px;color:#52656f}summary{cursor:pointer}@media(max-width:900px){.layout{grid-template-columns:1fr;padding:10px}aside{position:static}.drawing{overflow:auto}.drawing svg{min-width:850px}.controls{padding:10px}}'''
 for n in b.NODES:
  nid=n['id'];css+=f'.layout:has(#{nid}:target) .edge,.layout:has(#{nid}:target) .node{{opacity:.1}}.layout:has(#{nid}:target) .touch-{nid}{{opacity:1;stroke-width:3.2}}.layout:has(#{nid}:target) .near-{nid}{{opacity:1}}'
 out=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Psychological landscapes — single and difference views</title><style>'+css+'</style><div class="app"><header><h1>One map. Two profiles. Their differences.</h1><p>Illustrative design: invented graphs A and B, not results about actual LLMs.</p></header><div class="controls">']
 for v,title in [('a','Graph A'),('b','Graph B'),('difference','Difference graph')]:
  out.append(f'<input type="radio" name="view" id="view-{v}"'+(' checked' if v=='difference' else '')+f'><label class="tab" for="view-{v}">{title}</label>')
 out.append('<label class="shared-control"><input type="checkbox" id="show-shared" checked> Show shared connections</label></div><div class="layout"><div class="drawing">')
 for v in ['a','b','difference']:out.append(f'<div class="view view-{v}">'+render(v)+'</div>')
 out.append('<p class="legend">Region colors keep their meaning across views. Position is fixed; it is not a brain location or a measured psychological distance.</p></div><aside><div class="default"><h2>Compare the structure</h2><p>Switch between A and B to inspect each full graph. The difference graph overlays their shared and distinct connections.</p><p class="legend">Gray — shared<br><span class="orange">Orange dashed — A only</span><br><span class="blue">Blue solid — B only</span><br>Ring around a node — its connections differ</p><p>Click a node to compare its neighborhood. Uncheck “Show shared connections” to focus on changes.</p><p class="notice">All examples have the same 66 variables. We changed six links in each direction solely to demonstrate comparison.</p></div>')
 for n in b.NODES:
  nid=n['id'];na=set(neighbors(A,nid));nb=set(neighbors(B,nid))
  out.append(f'<section class="detail" id="{nid}"><h2>{b.esc(n["label"])}</h2><p>{b.esc(b.REGIONS[n["region"]][0])}</p><div class="facts facts-a"><h3>Connections in graph A</h3>'+links(sorted(na))+'</div><div class="facts facts-b"><h3>Connections in graph B</h3>'+links(sorted(nb))+'</div><div class="facts facts-difference"><h3>Shared</h3>'+links(sorted(na&nb))+'<h3 class="orange">A only</h3>'+links(sorted(na-nb))+'<h3 class="blue">B only</h3>'+links(sorted(nb-na))+'</div><p class="notice">Illustrative relationships, not estimated associations.</p><a href="#">Show whole graph</a></section>')
 out.append('</aside></div><footer><details><summary>How comparisons of real models must differ from this mockup</summary><p>This prototype compares unweighted edge presence only. A real comparison must match variable definitions, relation types, context, coding rules and adequate evidence coverage. An unmeasured or uncertain edge is not a measured zero. Strength differences would need comparable estimates and uncertainty; numerical equality would not establish psychological equivalence.</p><p>The same reference layout would be reused across models. Within-model reliability, context sensitivity and held-out predictive validation must be reported separately from the visualization.</p></details><p><a href="comparison-a.svg">Graph A alone</a> · <a href="comparison-b.svg">Graph B alone</a> · <a href="comparison-difference.svg">Whole difference graph</a> · <a href="network-comparison.json">Illustrative comparison data</a></p></footer></div></html>')
 return ''.join(out)

def main():
 assert len(SHARED)==134 and len(ONLY_A)==len(ONLY_B)==6
 assert all(n in b.BY for k in UNION for n in k)
 for v in ['a','b','difference']:
  text=render(v,True);ET.fromstring(text)
  (b.ROOT/f'comparison-{v}.svg').write_text(text,encoding='utf-8')
 (b.ROOT/'network-comparison.html').write_text(page(),encoding='utf-8')
 (b.ROOT/'network-comparison.json').write_text(json.dumps(dict(status='illustrative_design_only',nodes=b.NODES,graph_a=list(A.values()),graph_b=list(B.values()),shared=sorted(SHARED),only_a=sorted(ONLY_A),only_b=sorted(ONLY_B),changed_neighborhoods=sorted(CHANGED)),indent=2),encoding='utf-8')
 print(f'{len(b.NODES)} common nodes; {len(SHARED)} shared, {len(ONLY_A)} A-only, {len(ONLY_B)} B-only links. All illustrative.')
if __name__=='__main__':main()
