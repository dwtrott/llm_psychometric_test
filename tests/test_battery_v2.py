import sys,json,pathlib,unittest,copy,tempfile,importlib.util
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('v2',ROOT/'battery_v2/processor.py');p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
B=p.load();CONFIG={'provider':'synthetic','model':'v2-format-fixture','synthetic':True,'temperature':0}
P=p.prepare(B,CONFIG,'v2-tests',repeats=6);ITEMS={i['item_id']:i for i in B['items']}
def response(i,t):
    if i['kind']=='choice':
        semantic=i['correct'] or next(iter(i['options']));a={'choice':next(k for k,v in t['option_map'].items() if v==semantic),'evidence':'Synthetic format fixture, not a model measurement.'}
        if i['correct']:a['confidence']=80
        return a
    if i['kind']=='open':return {'response':'Synthetic format fixture. Not a substantive response and not a psychological measurement.'}
    return {'associates':{cue:['synthetic one','synthetic two','synthetic three','synthetic four','synthetic five'] for cue in i['response_schema']['associates']}}
R=[dict(trial_id=t['trial_id'],config_id=P['config_id'],status='ok',raw_response=json.dumps(response(ITEMS[t['item_id']],t))) for t in P['trials']]
ROWS,SUMMARY,GRAPH,REVIEW=p.score(B,P,R)
class Checks(unittest.TestCase):
    def test_coverage(self):
        self.assertEqual(len(B['items']),96);self.assertEqual(len(B['families']),48);self.assertEqual(len(B['domains']),12)
        self.assertTrue(all(sum(i['family_id']==f['id'] for i in B['items'])==2 for f in B['families']))
    def test_sources_and_content(self):
        self.assertTrue(all(len(i['question'])>150 and all(s in B['sources'] for s in i['source_ids']) for i in B['items']))
        self.assertTrue(all((ROOT/'battery_v2/question_book'/f'{d["id"]}.md').exists() for d in B['domains']))
    def test_all_valid_and_not_empirical(self):
        self.assertEqual(SUMMARY['quality'],{'valid':576});self.assertTrue(GRAPH['synthetic'])
    def test_counterbalance(self):
        for i in B['items']:
            for op in i['options']:
                letters=[next(k for k,v in t['option_map'].items() if v==op) for t in P['trials'] if t['item_id']==i['item_id']]
                self.assertEqual(sorted(letters),['A','A','B','B','C','C'])
    def test_prompt_key_separation(self):
        self.assertTrue(all('rubric' not in t['messages'][1]['content'] and 'Researcher key' not in t['messages'][1]['content'] for t in P['trials']))
    def test_preference_has_no_accuracy(self):
        self.assertTrue(all('accuracy' not in r['metrics'] for r in ROWS if not ITEMS[r['item_id']]['correct']))
    def test_calibration(self):
        self.assertTrue(all(abs(r['metrics']['brier']-.04)<1e-9 for r in ROWS if 'brier' in r['metrics']))
    def test_pending_review_not_zero(self):
        self.assertTrue(REVIEW);self.assertTrue(all(r['score'] is None for r in REVIEW));self.assertTrue(all(not r['metrics'] and r['review_status']=='pending' for r in ROWS if ITEMS[r['item_id']]['kind']=='open'))
    def test_association_denominator(self):
        es=[e for e in GRAPH['edges'] if e['type']=='evokes'];self.assertEqual(len(es),80);self.assertTrue(all(e['n_valid']==6 and e['weight']==1 for e in es))
    def test_graph_integrity(self):
        ids={n['id'] for n in GRAPH['nodes']};self.assertTrue(all(e['source'] in ids and e['target'] in ids for e in GRAPH['edges']));self.assertEqual(len(GRAPH['profile_catalog']['domains']),12)
    def test_status_separation(self):
        r=copy.deepcopy(R);r.pop();r[0]['raw_response']='bad';r[1]['raw_response']='{"declined":true}';r[2]['status']='api_error'
        q=p.score(B,P,r)[1]['quality'];self.assertTrue(all(q[k]==1 for k in ['missing','invalid','declined','api_error']))
    def test_mismatched_battery(self):
        b=copy.deepcopy(B);b['items'][0]['question']+=' changed'
        with self.assertRaises(ValueError):p.score(b,P,R)
    def test_duplicates_and_unknown(self):
        with self.assertRaises(ValueError):p.score(B,P,R+[R[0]])
        r=copy.deepcopy(R[:1]);r[0]['trial_id']='unknown'
        with self.assertRaises(ValueError):p.score(B,P,r)
    def test_nonfinite_confidence(self):
        t=next(t for t in P['trials'] if ITEMS[t['item_id']]['correct']);i=ITEMS[t['item_id']];a=response(i,t);a['confidence']=float('nan')
        with self.assertRaises(ValueError):p.validate(i,t,a)
    def test_exploration_key_and_expected_value(self):
        items=[i for i in B['items'] if i['family_id']=='OPEN-01'];self.assertEqual([i['correct'] for i in items],['A','B']);self.assertEqual(.5*0+.5*10+9*(.5*6+.5*10),77)
    def test_equal_mean_lotteries(self):self.assertEqual(.5*20,.95*20+.05*(-180))
    def test_no_semantic_edge_from_hypothesis(self):self.assertTrue(all(e['origin']=='researcher_design' for e in GRAPH['edges'] if e['type']=='designed_to_probe'))
if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Checks);result=unittest.TextTestRunner(verbosity=2).run(suite)
    if '--export-fixture' in sys.argv:
        dest=ROOT/'tests/v2-format-fixture.graph.json';p.write(dest,GRAPH)
    sys.exit(not result.wasSuccessful())
