"""Illustrative psychological-network design. NOT model data or inferred psychology.

Python standard library generates SVG/HTML/JSON.
No model calls, external assets, JavaScript, statistical inference or brain anatomy.
"""
from pathlib import Path
import html,json,math,textwrap

ROOT=Path(__file__).resolve().parent
W,H=1500,1060
# Proposed navigational regions. Their positions and membership are illustrative.
REGIONS=[
 ('Meaning & concepts',360,175,'#4773b9',['Association breadth','Category boundaries','Analogy use','Conceptual distance','Distinction reuse','Contextual meaning']),
 ('Evidence & belief',660,150,'#407d9c',['Evidence seeking','Prestige sensitivity','Belief revision','Counterevidence','Source trust','Justification depth']),
 ('Uncertainty & self-monitoring',980,205,'#437f92',['Confidence calibration','Unknown recognition','Verification','Error recognition','Certainty language','Uncertainty tolerance']),
 ('Curiosity & flexibility',180,395,'#8570b0',['Novelty preference','Idea diversity','Alternative search','Constraint adaptation','Exploration','Strategy switching']),
 ('Risk & decision',1220,420,'#47948b',['Risk preference','Ambiguity preference','Loss framing','Delay preference','Tradeoff consistency','Decision deferral']),
 ('Social understanding',360,565,'#717bb8',['Audience adaptation','Perspective taking','Intent attribution','Knowledge tracking','Audience sensitivity','Pragmatic inference']),
 ('Support & emotional understanding',255,825,'#aa709b',['Need clarification','Support matching','Emotion recognition','Validation style','Response restraint','Affective framing']),
 ('Cooperation & trust',710,480,'#699260',['Resource sharing','Reciprocity','Trust calibration','Competition','Conflict repair','Commitment keeping']),
 ('Values & agency',1040,725,'#539886',['Consent sensitivity','Autonomy protection','Fairness','Harm tradeoffs','Rule flexibility','Value consistency']),
 ('Self-attribution & motivation',610,850,'#ad8750',['Credit attribution','Role identification','Recognition seeking','Responsibility','Goal persistence','Self-correction']),
 ('Integrity & alignment',940,955,'#ad7068',['Material disclosure','Omission tendency','Reward sensitivity','Honesty under conflict','Imposed loss','Oversight sensitivity']),
]
OFFSETS=[(-72,-15),(0,-54),(75,-17),(-64,60),(13,27),(75,67)]
NODES=[];index={}
for region,(name,cx,cy,color,labels) in enumerate(REGIONS):
 for j,label in enumerate(labels):
  dx,dy=OFFSETS[j]; nid=f'n{len(NODES)}'
  n=dict(id=nid,label=label,region=region,x=cx+dx,y=cy+dy,color=color)
  NODES.append(n);index[label]=n

EDGES=[]
def add(a,b,kind='within_region'):
 a=index[a]['id'] if a in index else a;b=index[b]['id'] if b in index else b
 if not any({e['source'],e['target']}=={a,b} for e in EDGES):EDGES.append(dict(source=a,target=b,kind=kind,status='illustrative_only',weight=None))
for i in range(len(REGIONS)):
 ns=NODES[i*6:i*6+6]
 for a,b in [(0,1),(1,2),(2,5),(5,4),(4,3),(3,0),(0,4),(1,4),(2,4),(1,3)]:add(ns[a]['id'],ns[b]['id'])
# Explicitly invented bridges for testing navigation and visual legibility only.
for a,b in [
 ('Evidence seeking','Verification'),('Evidence seeking','Alternative search'),('Evidence seeking','Source trust'),
 ('Counterevidence','Self-correction'),('Belief revision','Strategy switching'),
 ('Contextual meaning','Knowledge tracking'),('Distinction reuse','Constraint adaptation'),('Analogy use','Idea diversity'),
 ('Uncertainty tolerance','Ambiguity preference'),('Verification','Decision deferral'),('Confidence calibration','Risk preference'),
 ('Source trust','Trust calibration'),('Prestige sensitivity','Recognition seeking'),
 ('Audience sensitivity','Credit attribution'),('Audience sensitivity','Resource sharing'),('Audience adaptation','Need clarification'),
 ('Perspective taking','Support matching'),('Intent attribution','Trust calibration'),('Conflict repair','Response restraint'),
 ('Resource sharing','Fairness'),('Commitment keeping','Responsibility'),('Reciprocity','Consent sensitivity'),
 ('Autonomy protection','Imposed loss'),('Harm tradeoffs','Imposed loss'),('Value consistency','Honesty under conflict'),
 ('Recognition seeking','Reward sensitivity'),('Responsibility','Material disclosure'),('Self-correction','Error recognition'),
 ('Goal persistence','Oversight sensitivity'),('Decision deferral','Consent sensitivity'),('Category boundaries','Rule flexibility')]:add(a,b,'bridge')
BY={n['id']:n for n in NODES}
NEIGHBORS={n['id']:[] for n in NODES}
for e in EDGES:
 NEIGHBORS[e['source']].append(e['target']);NEIGHBORS[e['target']].append(e['source'])

def hull(cx,cy,i):
 # Smooth organic areas, a schematic geography, not anatomical regions.
 points=[]
 for k in range(16):
  a=2*math.pi*k/16;r=1+.055*math.sin(k*2+i)
  points.append((cx+145*r*math.cos(a),cy+112*r*math.sin(a)))
 return points

def esc(s):return html.escape(str(s))
def svg(interactive=True):
 out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H+110}" role="img" aria-label="Illustrative psychological network landscape, not measured model data" style="font-family:system-ui,sans-serif">',
 '<rect width="100%" height="100%" fill="#fafbf9"/>',
 '<text x="30" y="34" font-size="25" fill="#263b43">A psychological network landscape</text>',
 '<text x="30" y="61" font-size="15" fill="#815f26">DESIGN PROTOTYPE · All nodes, links and regions are illustrative. No LLM has been measured.</text>']
 out.append('<g transform="translate(0,95)">')
 for i,(name,cx,cy,color,labels) in enumerate(REGIONS):
  pts=hull(cx,cy,i)
  # Smooth closed path using midpoint quadratic interpolation.
  mid=lambda a,b:((a[0]+b[0])/2,(a[1]+b[1])/2)
  start=mid(pts[-1],pts[0]);d=f'M {start[0]:.1f},{start[1]:.1f}'
  for j,p in enumerate(pts):
   end=mid(p,pts[(j+1)%len(pts)]);d+=f' Q {p[0]:.1f},{p[1]:.1f} {end[0]:.1f},{end[1]:.1f}'
  out.append(f'<path d="{d} Z" fill="{color}" fill-opacity=".085" stroke="{color}" stroke-opacity=".22"/>')
 for e in EDGES:
  a,b=BY[e['source']],BY[e['target']]
  color='#8a7b9f' if e['kind']=='bridge' else a['color']
  width=1.6 if e['kind']=='bridge' else 1.2
  out.append(f'<line class="edge touch-{a["id"]} touch-{b["id"]}" x1="{a["x"]}" y1="{a["y"]}" x2="{b["x"]}" y2="{b["y"]}" stroke="{color}" stroke-width="{width}" opacity=".38"><title>Illustrative link: {esc(a["label"])} — {esc(b["label"])}. Not estimated.</title></line>')
 for i,(name,cx,cy,color,labels) in enumerate(REGIONS):
  lines=textwrap.wrap(name,22)
  for j,line in enumerate(lines):out.append(f'<text x="{cx}" y="{cy-93+j*24}" font-size="22" font-weight="600" fill="#344953" text-anchor="middle">{esc(line)}</text>')
 for n in NODES:
  ns=NEIGHBORS[n['id']]
  classes=' '.join('near-'+v for v in [n['id']]+ns)
  url='#'+n['id'] if interactive else 'network-concept.html#'+n['id']
  out.append(f'<a class="node {classes}" href="{url}"><title>{esc(n["label"])} · {esc(REGIONS[n["region"]][0])} · illustrative only</title><circle cx="{n["x"]}" cy="{n["y"]}" r="13" fill="transparent"/><circle cx="{n["x"]}" cy="{n["y"]}" r="6.5" fill="{n["color"]}" stroke="#fafbf9" stroke-width="1.5"/>')
  # Two labels per region keep the whole network readable; every dot is inspectable.
  if int(n['id'][1:])%6 in [1,3]:
   for j,line in enumerate(textwrap.wrap(n['label'],18)):
    out.append(f'<text class="node-label" x="{n["x"]+11}" y="{n["y"]+3+j*20}" font-size="18" fill="#354a54" style="paint-order:stroke;stroke:#fafbf9;stroke-width:3px;stroke-linejoin:round">{esc(line)}</text>')
  out.append('</a>')
 out.append('</g></svg>');return ''.join(out)

def html_page():
 css='''body{font:16px/1.5 system-ui,sans-serif;margin:0;background:#fafbf9;color:#263b43}header{padding:24px 28px 0}h1{margin:0;font-size:26px}header p{margin:8px 0;color:#74551f}.layout{display:grid;grid-template-columns:minmax(0,1fr) 280px;gap:20px;padding:12px 28px}svg{width:100%;height:auto}aside{position:sticky;top:20px;align-self:start;background:white;border:1px solid #d9e1df;border-radius:12px;padding:20px}.detail{display:none}.detail:target{display:block}.layout:has(.detail:target) .default{display:none}a{color:#365b85}.node:hover circle{stroke:#263b43;stroke-width:2}h2{font-size:20px;margin-top:0}.notice{font-size:14px;color:#74551f}li{margin:5px 0}.edge,.node{transition:opacity .15s}details{margin-top:16px}summary{cursor:pointer}footer{padding:20px 28px;font-size:14px;color:#5a6b71}@media(max-width:900px){.layout{grid-template-columns:1fr;padding:10px}aside{position:static}.drawing{overflow:auto}.drawing svg{min-width:850px}header{padding:15px}}'''
 for n in NODES:
  nid=n['id'];css+=f'.layout:has(#{nid}:target) .edge,.layout:has(#{nid}:target) .node{{opacity:.12}}.layout:has(#{nid}:target) .touch-{nid}{{opacity:1;stroke-width:2.2}}.layout:has(#{nid}:target) .near-{nid}{{opacity:1}}'
 out=['<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Psychological network — design concept</title><style>'+css+'</style><header><h1>A connected psychological landscape</h1><p>Illustrative design only. These are proposed variables and invented links, not results from your battery.</p></header><div class="layout"><div class="drawing">'+svg()+'</div><aside><div class="default"><h2>Explore the network</h2><p>Click a dot to highlight its neighborhood across the region boundaries.</p><p>Soft areas identify proposed psychological regions. Small nodes represent specific patterns. Bridges connect patterns in different areas.</p><p class="notice">Topology, density and spacing here are design choices. No correlation, causal relationship or model fingerprint has been estimated.</p></div>']
 for n in NODES:
  out.append(f'<section class="detail" id="{n["id"]}"><h2>{esc(n["label"])}</h2><p>{esc(REGIONS[n["region"]][0])}</p><p class="notice">Illustrative node and neighborhood — not a measured trait or established connection.</p><h3>Shown connections</h3><ul>')
  for v in NEIGHBORS[n['id']]:out.append(f'<li><a href="#{v}">{esc(BY[v]["label"])}</a></li>')
  out.append('</ul><a href="#">Show the whole network</a></section>')
 out.append('</aside></div><footer>Proposed visual grammar: regions → communities of variables; nodes → specific response patterns; links → explicitly typed relations. A production version would distinguish observed semantic links from estimated statistical dependencies and keep untested links separate. This preview uses equal-sized nodes; emphasis means selection, not importance.<details><summary>Research informing the representation</summary><p><a href="https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.01742/full">Jones, Mair &amp; McNally: Visualizing Psychological Networks</a> · <a href="https://doi.org/10.1016/j.paid.2017.06.011">Costantini et al.: Stability and variability of personality networks</a></p><p>The proposed regions are navigation labels, not a validated factor structure. Human population networks cannot simply be interpreted as one LLM’s psychological organization.</p></details><p><a href="network-concept.svg">Whole graph (SVG)</a> · <a href="network-concept.json">Illustrative node/link data</a></p></footer></html>')
 return ''.join(out)

def main():
 ROOT.mkdir(parents=True,exist_ok=True)
 (ROOT/'network-concept.svg').write_text(svg(False),encoding='utf-8')
 (ROOT/'network-concept.html').write_text(html_page(),encoding='utf-8')
 (ROOT/'network-concept.json').write_text(json.dumps(dict(status='illustrative_design_only',nodes=NODES,edges=EDGES,regions=[r[0] for r in REGIONS]),indent=2),encoding='utf-8')
 print(f'{len(NODES)} illustrative nodes, {len(EDGES)} illustrative edges: {ROOT}')
if __name__=='__main__':main()
