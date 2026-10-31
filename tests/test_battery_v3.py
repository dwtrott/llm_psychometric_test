"""Behavioral-contract checks, never psychometric validation. Synthetic responses only."""
import importlib.util,json,pathlib,unittest,copy,collections
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('v3',ROOT/'battery_v3/processor.py');v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
B=v.load()
def plan(module=None,condition=None):
    b=copy.deepcopy(B)
    if module:b['items']=[i for i in b['items'] if i['module']==module and (condition is None or i['condition']==condition)]
    return b,v.prepare(b,dict(provider='test',model='synthetic',synthetic=True),'test',1)
def rec(request,answer,status='ok'):
    return dict(**{k:request[k] for k in ['trial_id','config_id','plan_hash','event_index','request_hash']},status=status,raw_response=json.dumps(answer))
def submit(b,p,records,answer):
    r=v.next_requests(b,p,records)[0];records.append(rec(r,dict(action='submit',answer=answer)))
def fixture_answer(s):
    result={}
    for k,f in s['fields'].items():
        typ=f['type'];result[k]=f['values'][0] if typ=='enum' else 'Synthetic format-check text.' if typ=='text' else ['sample one','sample two','sample three','sample four','sample five'] if typ=='strings' else f['min']
    for k,key in s['keys'].items():result[k]=key['value']
    return result
def complete(b,p):
    records=[]
    # Replaying all sessions on every action would obscure the test and be slow; use the same pure transition directly.
    for t in p['trials']:
        state=v.initial(p,t)
        while state['status']=='pending':
            req=v.request(p,t,state);s=t['stages'][state['stage']];r=rec(req,dict(action='submit',answer=fixture_answer(s)))
            v.apply(p,t,state,r);records.append(r)
    return records
class Battery(unittest.TestCase):
    def test_inventory(self):
        self.assertEqual(len(B['modules']),39);self.assertEqual(len(B['items']),194)
        self.assertEqual(len({m['domain'] for m in B['modules'].values()}),12)
        controls=json.loads((ROOT/'battery_v3/controls/battery.json').read_text())
        self.assertEqual(len(controls['items']),36);self.assertEqual(len(controls['families']),18)
    def test_no_key_or_future_stage_leak(self):
        b,p=plan('META-CHECK');r=v.next_requests(b,p,[])[0];s=r['messages'][-1]['content']
        self.assertNotIn('verified answer',s);self.assertNotIn('keys',s);self.assertNotIn('independent verified solution',s)
        self.assertEqual(len(r['messages']),2)
    def test_check_is_observed_and_charged(self):
        b,p=plan('META-CHECK');p['trials']=p['trials'][:1];p['plan_hash']=v.digest({k:x for k,x in p.items() if k!='plan_hash'});rr=[]
        submit(b,p,rr,dict(answer=0,confidence=90));r=v.next_requests(b,p,rr)[0];rr.append(rec(r,dict(action='request',resource='solution')))
        req=v.next_requests(b,p,rr)[0];self.assertIn('verified answer',req['messages'][-1]['content'])
        key=p['trials'][0]['stages'][1]['keys']['answer']['value'];submit(b,p,rr,dict(answer=key,confidence=100))
        rows,_,_,_=v.score(b,p,rr);m=rows[0]['metrics']
        self.assertEqual(m['s1_answer_accuracy'],0);self.assertEqual(m['s2_answer_accuracy'],1);self.assertEqual(m['s2_requests'],1);self.assertAlmostEqual(m['s1_brier'],.81)
        self.assertEqual(m['resource_cost'],p['trials'][0]['stages'][1]['resources']['solution']['cost'])
    def test_repeated_request_invalid(self):
        b,p=plan('EXEC-AUDIT');rr=[];r=v.next_requests(b,p,rr)[0];rr.append(rec(r,dict(action='request',resource='A')))
        r=next(x for x in v.next_requests(b,p,rr) if x['trial_id']==r['trial_id']);rr.append(rec(r,dict(action='request',resource='A')))
        self.assertEqual(v.replay(b,p,rr)[r['trial_id']]['status'],'invalid')
    def test_stale_response_rejected(self):
        b,p=plan('META-CHECK');r=v.next_requests(b,p,[])[0];a=rec(r,dict(action='submit',answer=dict(answer=0,confidence=20)))
        with self.assertRaises(ValueError):v.replay(b,p,[a,a])
    def test_plan_tampering(self):
        b,p=plan();p['trials'][0]['stages'][0]['prompt']='changed'
        with self.assertRaises(ValueError):v.next_requests(b,p,[])
    def test_limits_and_nonfinite(self):
        for answer in [dict(message='word '*71),dict(message='')]:
            with self.assertRaises(ValueError):v.valid_answer({'message':dict(type='text',max_words=70)},answer)
        for n in [True,float('nan'),float('inf'),101]:
            with self.assertRaises(ValueError):v.valid_answer({'x':dict(type='number',min=0,max=100)},dict(x=n))
    def test_decline_and_error_preserved(self):
        b,p=plan('DEC-AMBIG');requests=v.next_requests(b,p,[])
        rr=[rec(requests[0],dict(action='decline')),rec(requests[1],None,'api_error')]
        rows,summary,_,_=v.score(b,p,rr);self.assertEqual(summary['quality'],{'declined':1,'api_error':1,'pending':1});self.assertFalse(summary['estimates'])
    def test_ledger(self):
        b,p=plan('COOP-ALLOC','public_cost2');rr=[];submit(b,p,rr,dict(give=7));m=v.score(b,p,rr)[0][0]['metrics']
        self.assertEqual(m['s1_ledger_allocated'],14);self.assertEqual(m['s1_ledger_remaining'],5)
    def test_cancellation_report_mismatch(self):
        b,p=plan('ALIGN-STOP','audit20_penalty0');rr=[]
        for a in [dict(choice='start'),dict(choice='complete'),dict(status='cancelled',report='The job was cancelled.')]:submit(b,p,rr,a)
        self.assertEqual(v.score(b,p,rr)[0][0]['metrics']['status_mismatch'],1)
    def test_learning_feedback_and_hidden_switch(self):
        b,p=plan('EXEC-LEARN','color_first');rr=[];submit(b,p,rr,dict(choice='left'));r=v.next_requests(b,p,rr)[0]
        self.assertIn('choice_accuracy',r['messages'][-1]['content']);self.assertNotIn('switch',r['messages'][-1]['content'])
    def test_invalid_partial_not_aggregated(self):
        b,p=plan('EXEC-PLAN','blocked2');rr=[];submit(b,p,rr,dict(A=1,B=2,C=3));submit(b,p,rr,dict(A=9,B=2,C=3))
        rows,summary,_,_=v.score(b,p,rr);self.assertEqual(rows[0]['status'],'invalid');self.assertEqual(rows[0]['metrics']['stages_completed'],1);self.assertFalse(summary['estimates'])
    def test_all_paths_and_graph(self):
        b,p=plan();rr=complete(b,p);rows,summary,g,review=v.score(b,p,rr)
        self.assertEqual(summary['quality'],{'valid':194});self.assertEqual(len(rr),278);self.assertTrue(review)
        ids={n['id'] for n in g['nodes']};self.assertEqual(len(ids),len(g['nodes']));self.assertTrue(all(e['source'] in ids and e['target'] in ids for e in g['edges']))
        self.assertTrue(all(e['weight']==1 for e in g['edges'] if e['type']=='evokes'))
        v.write(ROOT/'tests/v3-format-fixture.graph.json',g)
    def test_association_duplicates(self):
        f={'associates':dict(type='strings',count=5,exclude='trust')}
        with self.assertRaises(ValueError):v.valid_answer(f,{'associates':['a','A','b','c','d']})
    def test_order_counterbalance(self):
        b,p=plan('DEC-AMBIG');p=v.prepare(b,p['config'],'order',2);groups=collections.defaultdict(list)
        for t in p['trials']:groups[t['item_id']].append(t['stages'][0]['fields']['choice']['values'])
        self.assertTrue(all(vs[0]==list(reversed(vs[1])) for vs in groups.values()))
    def test_controls_remain_separate_and_runnable(self):
        spec=importlib.util.spec_from_file_location('control',ROOT/'battery_v3/controls/processor.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
        b=c.load();p=c.prepare(b,dict(provider='test',model='test'),'controls',1)
        self.assertEqual(len(p['trials']),36);rows,summary,g,review=c.score(b,p,[])
        self.assertEqual(summary['quality'],{'missing':36});self.assertEqual(len(g['profile_catalog']['domains']),1)
        self.assertIn('controls',g['battery_version'])
    def test_same_final_distribution_across_reference(self):
        forms=[t for t in B['items'] if t['module']=='DEC-SPREAD']
        self.assertEqual(len(forms),4)
        for t in forms:
            self.assertIn('A ends with 20 for sure',t['stages'][0]['prompt'])
            self.assertIn('18 or 22' if 'spread2_' in t['condition'] else '12 or 28',t['stages'][0]['prompt'])
    def test_planning_repair(self):
        b,p=plan('EXEC-PLAN','blocked2');rr=[];submit(b,p,rr,dict(A=1,B=2,C=3));submit(b,p,rr,dict(A=1,B=4,C=3))
        m=v.score(b,p,rr)[0][0]['metrics'];self.assertEqual(m['s2_feasible'],1);self.assertEqual(m['tasks_rescheduled'],1);self.assertEqual(m['initially_used_blocked_slot'],1)
    def test_search_information_matches_posterior(self):
        b,p=plan('EPI-SEARCH','H1');rr=[]
        for key in ['T1','T2']:
            r=v.next_requests(b,p,rr)[0];rr.append(rec(r,dict(action='request',resource=key)))
        submit(b,p,rr,dict(probability_H1=1600/17));m=v.score(b,p,rr)[0][0]['metrics']
        self.assertAlmostEqual(m['posterior_absolute_error'],0);self.assertEqual(m['resource_cost'],2)
if __name__=='__main__':
    unittest.main()
