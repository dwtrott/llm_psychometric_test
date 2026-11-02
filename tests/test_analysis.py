import copy,importlib.util,json,pathlib,tempfile,unittest,re,xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('design_analysis',ROOT/'analyzer/psychometric.py');a=importlib.util.module_from_spec(s);s.loader.exec_module(a)
def profile(name='A',split='development'):
 rows=[]
 for scenario in [1,2]:
  for condition in ['cheap','costly']:
   for wording in ['P1','P2']:
    for order in ['order01','order02']:
     for repeat in [0,1]:
      rows.append(dict(trial=f'{name}:{scenario}:{condition}:{wording}:{order}:{repeat}',facet='TEST',pair=f'M{scenario}',scenario=f'S{scenario+(3 if split=="heldout" else 0)}',condition=condition,wording=wording,base='standard',order=order,transfer='none',cue='',repeat=repeat,status='valid',features={'choice':int(condition=='cheap')+.1*int(wording=='P2')+.2*int(order=='order02')}))
 return dict(id=name+split,label=name,split=split,config={'id':name,'model':name},hash='same',lock='locked' if split=='heldout' else None,rows=rows)
class Analysis(unittest.TestCase):
 def test_axes_remain_separate(self):
  p=profile()
  for axis,expected in [('condition',-1),('wording',.1),('order',.2)]:
   results=a.contrast(p,axis);self.assertTrue(results)
   self.assertTrue(all(abs(r['delta']-expected)<1e-9 for r in results))
 def test_missing_not_zero_and_common_repeats(self):
  p=profile();victim=next(r for r in p['rows'] if r['condition']=='cheap');victim.update(status='missing',features={})
  result=a.contrast(p,'condition');self.assertEqual(min(r['n_repeat_pairs'] for r in result),1)
  self.assertTrue(all(abs(r['delta']+1)<1e-9 for r in result))
 def test_exact_model_comparison_and_equal_scenario_weight(self):
  p,q=profile(),profile('B')
  for r in q['rows']:r['features']['choice']+=.3
  result=a.compare(p,q)
  self.assertTrue(all(abs(r['delta']-.3)<1e-9 and r['n_scenarios']==2 for r in result['scenario_balanced']))
  self.assertTrue(all(abs(r['delta'])<1e-9 for r in result['condition_effect_changes']))
 def test_transfer_joins_pair_not_scenario(self):
  result=a.compare(profile(),profile(split='heldout'),True)
  self.assertTrue(result['cells']);self.assertTrue(all(r['delta']==0 for r in result['cells']))
 def test_incompatible_comparisons_rejected(self):
  p,q=profile(),profile('B');q['hash']='different'
  with self.assertRaises(ValueError):a.compare(p,q)
  with self.assertRaises(ValueError):a.compare(p,profile('B','heldout'),True)
  q=profile(split='heldout');q['lock']=None
  with self.assertRaises(ValueError):a.compare(p,q,True)
 def test_order_not_averaged_away(self):
  p,q=profile(),profile('B')
  for r in q['rows']:r['features']['choice']+=1 if r['order']=='order01' else -1
  results=a.compare(p,q)['scenario_balanced'];self.assertEqual({r['delta'] for r in results},{1,-1})
 def test_no_variance_invented_for_single_repeat(self):
  p=profile();p['rows']=[r for r in p['rows'] if r['repeat']==0]
  self.assertTrue(all(r['sample_sd'] is None for r in a.cell_table(p)))
 def test_four_arm_common_support(self):
  p,q=profile(),profile('B')
  for r in p['rows']:
   if r['condition']=='cheap' and r['repeat']==0:r['features']={};r['status']='missing'
  for r in q['rows']:
   if r['condition']=='costly' and r['repeat']==1:r['features']={};r['status']='missing'
  self.assertFalse(a.compare(p,q)['condition_effect_changes'])
 def test_html_escaping(self):
  self.assertNotIn('<script>',a.table([{'x':'<script>alert(1)</script>'}],['x']))
 def test_csv_formula_escape(self):
  with tempfile.TemporaryDirectory() as d:
   path=pathlib.Path(d)/'test.csv';a.save_csv(path,[dict(name='=1+1',value=-.2)])
   self.assertIn("'=1+1",path.read_text(encoding='utf-8-sig'));self.assertIn(',-0.2',path.read_text(encoding='utf-8-sig'))
 def test_findings_preserve_reversals_and_missingness(self):
  p=profile();p['catalog']={'modules':{'DEC-RISK':{}}}
  for r in p['rows']:
   r['facet']='DEC-RISK'
   r['features']={'risky_choice':int((r['condition']=='cheap')==(r['scenario']=='S1'))}
  report={'cells':a.cell_table(p),'contrasts':{axis:a.contrast(p,axis) for axis in ['condition','wording','order']}}
  f=a.response_findings(p,report)[0]
  self.assertEqual((f['effects'][0]['min'],f['effects'][0]['max']),(-1,1))
  self.assertEqual(f['n_scenarios'],2)
  for r in p['rows']:r.update(status='missing',features={})
  report={'cells':a.cell_table(p),'contrasts':{axis:a.contrast(p,axis) for axis in ['condition','wording','order']}}
  f=a.response_findings(p,report)[0]
  self.assertEqual(f['status'],'unmeasured');self.assertFalse(f['conditions']);self.assertFalse(f['effects'])
 def test_actual_v7_exports_report_and_svg(self):
  spec=importlib.util.spec_from_file_location('synthetic_analysis_fixture',ROOT/'scripts/demo_analysis.py');demo=importlib.util.module_from_spec(spec);spec.loader.exec_module(demo)
  battery=demo.p.load()
  with tempfile.TemporaryDirectory() as directory:
   paths=[]
   for model,split in [('A','development'),('B','development'),('A','heldout')]:
    graph=demo.create_graph(battery,model,split);path=pathlib.Path(directory)/(model+split+'.json');path.write_text(json.dumps(graph),encoding='utf-8');paths.append(path)
   report=a.build(paths,pathlib.Path(directory)/'output');text=report.read_text(encoding='utf-8');data=json.loads(report.with_name('analysis.json').read_text(encoding='utf-8'))
   self.assertEqual(len(data['comparisons']),2);self.assertEqual(len(data['skipped']),1)
   self.assertEqual(len(data['profiles'][0]['coverage']),14)
   self.assertIn('SYNTHETIC DATA INCLUDED',text);self.assertNotIn('<script',text.lower())
   self.assertNotIn('No association edges in common exposures',text)
   self.assertIn('Actual response evidence',text)
   self.assertIn('Transfer-pattern balance checks',text)
   self.assertIn('not transfer performance',text)
   self.assertNotIn('Conceptual transfer-pattern effects',text)
   svgs=re.findall(r'<svg\b.*?</svg>',text,flags=re.S);self.assertGreater(len(svgs),10)
   for svg in svgs:ET.fromstring(svg)
   transfer=next(c for c in data['comparisons'] if c['mode']=='heldout_transfer')
   self.assertTrue(transfer['condition_effect_changes'])
   self.assertTrue(all(abs(r['delta'])<1e-9 for r in transfer['condition_effect_changes']))
   comparison=next(c for c in data['comparisons'] if c['mode']=='model_comparison')
   risk=[r for r in comparison['scenario_balanced'] if r['facet']=='DEC-RISK']
   self.assertEqual({r['delta'] for r in risk},{-1,0,1})
   aa,bb=data['profiles'][:2]
   ar=next(f for f in aa['findings'] if f['facet']=='DEC-RISK')
   br=next(f for f in bb['findings'] if f['facet']=='DEC-RISK')
   self.assertIn('gain 100%',ar['headline']);self.assertIn('loss 0%',ar['headline'])
   self.assertEqual(ar['checks']['order']['changed'],0)
   self.assertEqual(br['checks']['order']['changed'],12)
   self.assertEqual(ar['effects'][0]['min'],-1)
   self.assertEqual(br['effects'][0]['min'],0)
   self.assertEqual(next(f for f in aa['findings'] if f['facet']=='OPEN-CREATE')['status'],'unrated')
   kg=json.loads(report.with_name('knowledge_graph.json').read_text(encoding='utf-8'))
   ids={n['id'] for n in kg['nodes']};self.assertEqual(len(ids),len(kg['nodes']))
   self.assertTrue(all(e['source'] in ids and e['target'] in ids for e in kg['edges']))
   self.assertTrue({'qualified_by','supported_by','observed_under','elicited_in','informs_hypothesis','compares_a'} <= {e['type'] for e in kg['edges']})
   self.assertTrue(all(n['epistemic_status']=='not_validated_as_latent_trait' for n in kg['nodes'] if n['kind']=='candidate_facet'))
   self.assertTrue(any(n['mode']=='heldout_transfer' for n in kg['nodes'] if n['kind']=='matched_comparison'))
   self.assertIn('Psychological behavior differences by region',text)
if __name__=='__main__':unittest.main()
