"""Synthetic implementation checks, not evidence of construct validity."""
import collections,hashlib,importlib.util,json,pathlib,re,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load_module(path,name):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
p=load_module(ROOT/'battery_v5/processor.py','v5');B=p.load()
c=load_module(ROOT/'battery_v5/controls/processor.py','controls');C=c.load()
CONFIG=dict(provider='test',model='synthetic',synthetic=True)
SPEC=dict(model_configurations=[CONFIG],primary_features={'DEC-RISK':['risky_choice']},comparison_rules='Match pairs and strata.',heldout_prediction_rule='Compare each frozen development condition effect with its held-out partner.',exclusions='Retain all failures.',rating_codebook_policy='No human ratings in synthetic tests.')
def complete(module,plan,edit=None):
    records=[]
    for t in plan['trials']:
        state=module.engine.initial(plan,t)
        while state['status']=='pending':
            req=module.engine.request(plan,t,state);stage=t['stages'][state['stage']];answer={}
            for k,f in stage['fields'].items():
                answer[k]=f['values'][0] if f['type']=='enum' else 'Synthetic response for verification.' if f['type']=='text' else ['one','two','three','four','five'] if f['type']=='strings' else f['min']
            for k,key in stage['keys'].items():answer[k]=key['value']
            if edit:answer=edit(t,answer)
            r=dict(**{k:req[k] for k in ['trial_id','config_id','plan_hash','event_index','request_hash']},status='ok',raw_response=json.dumps(dict(action='submit',answer=answer)))
            module.engine.apply(plan,t,state,r);records.append(r)
    return records
class Revision(unittest.TestCase):
    def test_frozen_v4(self):
        self.assertEqual(hashlib.sha256((ROOT/'battery_v4/questions.csv').read_bytes()).hexdigest(),'2df0bf6186020d06eb699453c505ee71f8484d3486f807af8f8f9964063da248')
    def test_inventory_and_controls(self):
        self.assertEqual(len(B['modules']),14);self.assertEqual(len(B['domains']),11)
        self.assertEqual(set(C['modules']),{'EXEC-ADAPT','EPI-REVISION'})
        self.assertFalse(set(C['modules'])&set(B['modules']))
        self.assertEqual(len(B['items']),504)
        for mid in B['modules']:
            self.assertEqual(collections.Counter(s['split'] for s in B['manifest']['scenarios'] if s['facet_id']==mid),{'development':3,'heldout':3})
    def test_paraphrase_machine_facts_identical(self):
        for bank in [B,C]:
            groups=collections.defaultdict(list)
            for t in bank['items']:groups[(t['scenario'],t['condition'],t['cue'],t['stratum'])].append(t)
            for pair in groups.values():
                for a,z in zip(pair[0]['stages'],pair[1]['stages']):
                    for key in ['keys','fields','resources','effects','rubric']:self.assertEqual(a[key],z[key])
    def test_matched_payoffs_and_operations(self):
        sc={s['scenario_id']:s for s in B['manifest']['scenarios']}
        for t in B['items']:
            if t['split']!='heldout':continue
            d=next(i for i in B['items'] if i['scenario']==sc[t['scenario']]['partner'] and all(i[k]==t[k] for k in ['condition','paraphrase','cue','stratum']))
            for a,z in zip(t['stages'],d['stages']):
                if t['module']!='ALIGN-DISCLOSE':self.assertEqual(a['effects'],z['effects'])
            if t['module']=='META-VERIFY':
                self.assertEqual(t['stages'][0]['keys'],d['stages'][0]['keys']);self.assertEqual(t['stages'][1],d['stages'][1])
            if t['module']=='OPEN-CREATE':self.assertEqual(t['stages'][1],d['stages'][1])
            if t['module'] in ['DEC-RISK','ALIGN-HARM','ALIGN-DISCLOSE']:
                self.assertEqual(re.findall(r'\d+',t['stages'][0]['prompt']),re.findall(r'\d+',d['stages'][0]['prompt']))
    def test_controls_duration_fix(self):
        for t in C['items']:
            if t['scenario'] in ['EXEC-ADAPT-S02','EXEC-ADAPT-S04'] and t['paraphrase']=='P1':self.assertIn('Each task takes one slot.',t['stages'][0]['prompt'])
    def test_roles_stay_separate(self):
        plan=p.prepare(B,CONFIG,'roles',repeats=2,facets=['SELF-CREDIT'])
        records=complete(p,plan,lambda t,a:dict(a,originator_credit={'originator_self':80,'implementer_self':20,'neutral_observer':50}[t['stratum']]))
        rows,summary,graph,_=p.score(B,plan,records)
        estimates=[x for x in summary['facet_estimates'] if x['metric']=='originator_credit_fraction']
        self.assertEqual({x['stratum']:x['mean'] for x in estimates},{'originator_self':.8,'implementer_self':.2,'neutral_observer':.5})
        self.assertTrue(all(x['n_scenarios']==3 for x in estimates))
        self.assertTrue(all(r['matched_pair'] for r in rows))
        self.assertTrue(all('self_credit_fraction' not in r['features'] for r in rows if r['stratum']=='neutral_observer'))
    def test_no_advice_is_not_agreement(self):
        plan=p.prepare(B,CONFIG,'advice',repeats=1,facets=['EPI-STATUS']);rows,_,_,_=p.score(B,plan,complete(p,plan))
        self.assertTrue(all('advice_agreement_change' not in r['features'] for r in rows if r['stratum']=='no_advice'))
        self.assertTrue(all(r['features']['error_change']==0 for r in rows))
    def test_all_banks_end_to_end(self):
        for module,bank,split in [(p,B,'development'),(p,B,'heldout'),(c,C,'development')]:
            plan=module.prepare(bank,CONFIG,'smoke',repeats=1,split=split,analysis_lock=p.freeze(B,SPEC) if split=='heldout' else None)
            rows,summary,graph,_=module.score(bank,plan,complete(module,plan))
            self.assertTrue(all(r['status']=='valid' for r in rows),summary['quality'])
            self.assertEqual(graph['bank'],bank['bank']);self.assertFalse(module.next_requests(bank,plan,complete(module,plan)))
            if bank['bank']=='profile':(ROOT/f'tests/v5-{split}-fixture.graph.json').write_text(json.dumps(graph),encoding='utf-8')
    def test_lock_required_and_missing_is_not_zero(self):
        with self.assertRaises(ValueError):p.prepare(B,CONFIG,'bad',split='heldout')
        plan=p.prepare(B,CONFIG,'missing',repeats=1,facets=['SELF-CREDIT'])
        _,s,_,_=p.score(B,plan,[]);self.assertFalse(s['scenario_estimates']);self.assertFalse(s['condition_effects'])
if __name__=='__main__':unittest.main()
