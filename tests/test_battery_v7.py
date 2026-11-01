"""Presentation balance and scoring tests; synthetic data, not construct validation."""
import collections,copy,csv,hashlib,importlib.util,itertools,json,pathlib,unittest
from test_battery_v6 import complete
ROOT=pathlib.Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('v7',ROOT/'battery_v7/processor.py');p=importlib.util.module_from_spec(s);s.loader.exec_module(p);B=p.load()
CONFIG=dict(provider='test',model='synthetic',synthetic=True)
SPEC=dict(model_configurations=[CONFIG],primary_features={'DEC-RISK':['risky_choice']},comparison_rules='Match presentation cells.',heldout_prediction_rule='Compare pair-specific condition effects within presentation cells.',exclusions='Keep failures.',rating_codebook_policy='No human-coded outcomes in synthetic fixtures.')
def plan(facets=None,split='development',repeats=1):return p.prepare(B,CONFIG,'v7-fixture',facets=facets,split=split,repeats=repeats,analysis_lock=p.freeze(B,SPEC) if split=='heldout' else None)
class Presentation(unittest.TestCase):
 def test_full_inventory_and_frozen_source(self):
  self.assertEqual(len(B['modules']),14);self.assertEqual(len(B['domains']),11);self.assertEqual(len(B['items']),1224)
  self.assertEqual(sum(len(t['stages']) for t in B['items']),1848)
  revision=json.loads((ROOT/'battery_v7/revision_map.json').read_text())
  self.assertEqual(hashlib.sha256((ROOT/'battery_v6/questions.csv').read_bytes()).hexdigest(),revision['source_questions_sha256'])
 def test_genuinely_distinct_wordings_and_fixed_stage_facts(self):
  groups=collections.defaultdict(list)
  for t in B['items']:groups[t['scenario'],t['condition'],t['cue'],t['stratum']].append(t)
  for forms in groups.values():
   self.assertEqual(len(forms),2);a,z=forms
   self.assertNotEqual(a['stages'][0]['prompt'],z['stages'][0]['prompt'])
   for x,y in zip(a['stages'],z['stages']):
    for key in ['fields','keys','effects','resources','rubric']:self.assertEqual(x[key],y[key])
 def test_all_orders_and_transfer_combinations_crossed(self):
  for sid in {t['scenario'] for t in B['items']}:
   group=[t for t in B['items'] if t['scenario']==sid and t['paraphrase']=='P1']
   for cond in {t['condition'] for t in group}:
    for base in {t['presentation']['base_stratum'] for t in group}:
     cells=[t for t in group if t['condition']==cond and t['presentation']['base_stratum']==base]
     if cells[0]['module']=='SEM-DISTINCT':
      self.assertEqual(len(cells),18)
      self.assertEqual({(tuple(t['presentation']['display_order']),t['presentation']['transfer_pattern']) for t in cells},set(itertools.product(itertools.permutations('LMN'),['LM','LN','MN'])))
     elif cells[0]['presentation']['display_order']:
      orders=[tuple(t['presentation']['display_order']) for t in cells]
      self.assertEqual(set(orders),set(itertools.permutations(orders[0])))
 def test_presentation_is_fixed_across_repeats_and_conditions(self):
  pp=plan(['DEC-RISK','SEM-DISTINCT'],repeats=2)
  by=collections.defaultdict(list)
  for t in pp['trials']:by[t['item_id']].append(t)
  for ts in by.values():self.assertEqual(ts[0]['stages'],ts[1]['stages'])
 def test_prose_and_schema_order_agree(self):
  for t in B['items']:
   mid=t['module'];q=t['stages'][0]['prompt'];order=t['presentation']['display_order'];fields=t['stages'][0]['fields']
   if mid in ['DEC-RISK','DEC-AMBIG','VALUE-AUTONOMY','ALIGN-HARM']:
    markers=[(''+k+':') if mid in ['DEC-AMBIG','VALUE-AUTONOMY'] else k+' ' for k in order]
    self.assertEqual([q.index(k) for k in markers],sorted(q.index(k) for k in markers))
    self.assertEqual(fields['choice']['values'],order)
   if mid=='ALIGN-DISCLOSE':
    self.assertEqual([q.index(k+':') for k in order],sorted(q.index(k+':') for k in order));self.assertEqual(fields['recommendation']['values'],order)
   if mid=='EPI-STATUS':
    self.assertLess(q.index(order[0]+' '),q.index(order[1]+' '));self.assertEqual(fields['choice']['values'],order)
 def test_orders_preserve_keys_costs_and_payoffs(self):
  groups=collections.defaultdict(list)
  for t in B['items']:groups[t['scenario'],t['condition'],t['paraphrase'],t['cue'],t['presentation']['base_stratum']].append(t)
  for ts in groups.values():
   for t in ts[1:]:
    for a,z in zip(ts[0]['stages'],t['stages']):
     for key in ['keys','resources','effects','rubric']:self.assertEqual(a[key],z[key])
 def test_source_incentives_and_response_demands_preserved(self):
  with (ROOT/'battery_v6/questions.csv').open(encoding='utf-8-sig') as f:source_rows=list(csv.DictReader(f))
  index={(r['item_id'],int(r['stage'])):r for r in source_rows}
  for t in B['items']:
   original=t['item_id'].rsplit('.',1)[0]
   for n,stage in enumerate(t['stages']):
    old=index[original,n]
    for key in ['keys','resources','effects','rubric']:self.assertEqual(stage[key],json.loads(old[key+'_json']))
    fields=json.loads(old['fields_json'])
    for name,field in fields.items():
     revised=stage['fields'][name]
     if field['type']=='enum':self.assertEqual(set(field['values']),set(revised['values']))
     else:self.assertEqual(field,revised)
 def test_matched_partners_preserve_presentation(self):
  sc={s['scenario_id']:s for s in B['manifest']['scenarios']}
  index={(t['scenario'],t['condition'],t['paraphrase'],t['cue'],t['stratum']):t for t in B['items']}
  for t in B['items']:
   if t['split']!='development':continue
   z=index[sc[t['scenario']]['partner'],t['condition'],t['paraphrase'],t['cue'],t['stratum']]
   self.assertEqual(t['presentation']['order_id'],z['presentation']['order_id']);self.assertEqual(t['presentation']['transfer_pattern'],z['presentation']['transfer_pattern'])
   if t['module']=='SEM-DISTINCT':self.assertEqual(t['stages'][1],z['stages'][1]);self.assertEqual(t['presentation'],z['presentation'])
 def test_conceptual_answers_are_normalized_to_semantic_identity(self):
  pp=plan(['SEM-DISTINCT'])
  def choose(t,a):
   if 'pair' in a:a['pair']=''.join(sorted(t['presentation']['canonical_to_display'][x] for x in 'LN'))
   return a
  rows,s,g,_=p.score(B,pp,complete(p,pp,choose))
  self.assertTrue(all(r['features']['canonical_pair_LN']==1 for r in rows))
  self.assertEqual({r['presentation']['transfer_pattern'] for r in rows},{'LM','LN','MN'})
  self.assertTrue(all('order' in x['stratum'] and 'transfer' in x['stratum'] for x in s['facet_estimates']))
  self.assertTrue(all('presentation' in n for n in g['nodes'] if n['kind']=='trial'))
 def test_roles_and_advice_not_broken_by_presentation_tags(self):
  pp=plan(['SELF-CREDIT','EPI-STATUS']);rows,_,_,_=p.score(B,pp,complete(p,pp))
  for r in rows:
   base=r['presentation']['base_stratum']
   if base=='neutral_observer':self.assertNotIn('self_credit_fraction',r['features'])
   if base=='no_advice':self.assertNotIn('advice_agreement_change',r['features'])
 def test_full_end_to_end_and_viewer_fixtures(self):
  for split in ['development','heldout']:
   pp=plan(split=split);records=complete(p,pp);rows,s,g,_=p.score(B,pp,records)
   self.assertEqual(s['quality'],{'valid':612});self.assertFalse(p.next_requests(B,pp,records))
   (ROOT/f'tests/v7-{split}-fixture.graph.json').write_text(json.dumps(g),encoding='utf-8')
 def test_heldout_requires_versioned_lock(self):
  with self.assertRaises(ValueError):p.prepare(B,CONFIG,'bad',split='heldout')
if __name__=='__main__':unittest.main()
