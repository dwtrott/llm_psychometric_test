"""Design/runner tests with synthetic responses; not psychometric validation."""
import collections,copy,importlib.util,itertools,json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('v4',ROOT/'battery_v4/processor.py');p=importlib.util.module_from_spec(s);s.loader.exec_module(p)
B=p.load();CONFIG=dict(provider='test',model='synthetic',synthetic=True)
SPEC=dict(model_configurations=[CONFIG],primary_features={'DEC-RISK':['risky_choice']},comparison_rules='Match scenario and condition; retain failures.',heldout_prediction_rule='Freeze development mean before evaluation; report absolute error on held-out scenarios.',exclusions='No response-content exclusions; retain invalidity.',rating_codebook_policy='No human ratings in these synthetic tests.')
def plan(facets=None,repeats=1,split='development'):
    return p.prepare(B,CONFIG,'fixture',repeats,1729,split,facets,p.freeze(B,SPEC) if split=='heldout' else None)
def answer(stage):
    out={}
    for k,f in stage['fields'].items():
        out[k]=f['values'][0] if f['type']=='enum' else 'Synthetic response for format verification.' if f['type']=='text' else ['sample one','sample two','sample three','sample four','sample five'] if f['type']=='strings' else f['min']
    for k,key in stage['keys'].items():out[k]=key['value']
    return out
def complete(plan,edit=None):
    records=[]
    for trial in plan['trials']:
        state=p.engine.initial(plan,trial)
        while state['status']=='pending':
            req=p.engine.request(plan,trial,state);st=trial['stages'][state['stage']];a=answer(st)
            if edit:a=edit(trial,state['stage'],a)
            record=dict(**{k:req[k] for k in ['trial_id','config_id','plan_hash','event_index','request_hash']},status='ok',raw_response=json.dumps(dict(action='submit',answer=a)))
            p.engine.apply(plan,trial,state,record);records.append(record)
    return records
class Battery(unittest.TestCase):
    def test_inventory_and_crossing(self):
        self.assertEqual(len(B['modules']),16);self.assertEqual(len(B['manifest']['scenarios']),96);self.assertEqual(len(B['items']),456)
        self.assertEqual(sum(len(t['stages']) for t in B['items']),600)
        self.assertEqual(len({m['domain'] for m in B['modules'].values()}),12)
        for mid in B['modules']:
            sc=[s for s in B['manifest']['scenarios'] if s['facet_id']==mid]
            self.assertEqual(collections.Counter(s['split'] for s in sc),{'development':4,'heldout':2})
    def test_split_by_scenario_not_prompt(self):
        dev=plan();hold=plan(split='heldout')
        self.assertFalse({t['scenario'] for t in dev['trials']}&{t['scenario'] for t in hold['trials']})
        self.assertEqual(dev['battery_hash'],hold['battery_hash']);self.assertEqual(len(dev['trials']),304);self.assertEqual(len(hold['trials']),152)
    def test_heldout_lock_required(self):
        with self.assertRaises(ValueError):p.prepare(B,CONFIG,'bad',split='heldout')
        lock=p.freeze(B,SPEC);lock['specification']['exclusions']='changed'
        with self.assertRaises(ValueError):p.prepare(B,CONFIG,'bad',split='heldout',analysis_lock=lock)
    def test_template_cannot_be_frozen(self):
        spec=copy.deepcopy(SPEC);spec['heldout_prediction_rule']='REPLACE'
        with self.assertRaises(ValueError):p.freeze(B,spec)
    def test_wrong_model_outside_lock(self):
        with self.assertRaises(ValueError):p.prepare(B,dict(CONFIG,model='another'),'bad',split='heldout',analysis_lock=p.freeze(B,SPEC))
    def test_no_evaluator_metadata_in_messages(self):
        pp=plan(['META-VERIFY']);requests=p.next_requests(B,pp,[])
        for req in requests:
            model_text=json.dumps(req['messages'])
            self.assertNotIn('META-VERIFY',model_text);self.assertNotIn('development',model_text);self.assertNotIn('verified answer',model_text)
    def test_preserved_option_keys_across_forms(self):
        for sid in {t['scenario'] for t in B['items']}:
            group=[t for t in B['items'] if t['scenario']==sid]
            for condition in {t['condition'] for t in group}:
                forms=[t for t in group if t['condition']==condition]
                # Multiple association cues are separate elicitation units within the same scenario.
                for cue in {t['cue'] for t in forms}:
                    a,z=[t for t in forms if t['cue']==cue]
                    self.assertEqual([s['keys'] for s in a['stages']],[s['keys'] for s in z['stages']])
                    self.assertEqual([s['fields'] for s in a['stages']],[s['fields'] for s in z['stages']])
    def test_all_scheduling_conditions_are_feasible(self):
        for sc in B['manifest']['scenarios']:
            if sc['facet_id']!='EXEC-ADAPT':continue
            e=sc['evaluation'];possibles=[dict(zip('ABC',values)) for values in itertools.product(range(1,e['slots']+1),repeat=3)]
            self.assertTrue(any(p.feasible(a,e) for a in possibles))
            for blocked in e['blocked'].values():self.assertTrue(any(p.feasible(a,e,blocked) for a in possibles))
    def test_scheduling_duration_and_dependencies(self):
        e=next(s['evaluation'] for s in B['manifest']['scenarios'] if s['scenario_id']=='EXEC-ADAPT-S01')
        self.assertTrue(p.feasible(dict(A=1,B=2,C=4),e));self.assertFalse(p.feasible(dict(A=1,B=2,C=3),e));self.assertFalse(p.feasible(dict(A=1,B=2,C=4),e,3))
    def test_within_item_variability_is_not_scenario_count(self):
        pp=plan(['SELF-CREDIT'],2)
        rr=complete(pp,lambda t,n,a:dict(a,self_credit=20 if t['repeat']==0 else 80))
        rows,summary,g,review=p.score(B,pp,rr)
        self.assertTrue(all(x['n_scenarios']==4 for x in summary['facet_estimates']))
        self.assertTrue(all(abs(x['sample_variance']-.18)<1e-9 for x in summary['item_variability']))
        self.assertTrue(all(x['p2_minus_p1']==0 for x in summary['paraphrase_differences']))
    def test_paraphrase_sensitivity_visible(self):
        pp=plan(['SELF-CREDIT']);rr=complete(pp,lambda t,n,a:dict(a,self_credit=20 if t['paraphrase']=='P1' else 80))
        _,summary,_,_=p.score(B,pp,rr)
        self.assertTrue(all(abs(x['p2_minus_p1']-.6)<1e-9 for x in summary['paraphrase_differences']))
        self.assertTrue(all(x['sample_variance'] is None for x in summary['item_variability']))
    def test_missing_form_does_not_become_zero(self):
        pp=plan(['SELF-CREDIT']);rr=complete(pp)
        ids={t['trial_id'] for t in pp['trials'] if t['paraphrase']=='P2'};rr=[r for r in rr if r['trial_id'] not in ids]
        _,summary,_,_=p.score(B,pp,rr);self.assertFalse(summary['scenario_estimates']);self.assertFalse(summary['condition_effects'])
    def test_context_contrast_matches_all_four_cells(self):
        pp=plan(['SELF-CREDIT'],2);rr=complete(pp)
        # Disjoint repeats for public/private would otherwise produce an unpaired contrast.
        keep={t['trial_id'] for t in pp['trials'] if t['repeat']==int(t['condition']=='public')}
        rr=[r for r in rr if r['trial_id'] in keep]
        _,summary,_,_=p.score(B,pp,rr);self.assertTrue(summary['scenario_estimates']);self.assertFalse(summary['condition_effects'])
    def test_unknown_support_need_is_not_rated(self):
        pp=plan(['AFFECT-NEED']);_,_,_,review=p.score(B,pp,complete(pp))
        rows=[r for r in review if r['criterion']=='revealed_need_fit']
        self.assertTrue(all(r['status']=='not_observable' for r in rows if r['condition']=='ambiguous'))
    def test_association_denominators_use_scenarios(self):
        pp=plan(['SEM-LINK'],2);_,_,g,_=p.score(B,pp,complete(pp))
        ee=[e for e in g['edges'] if e['type']=='evokes'];self.assertTrue(ee)
        self.assertTrue(all(e['n_scenarios']==4 and e['n_valid']==16 and e['weight']==1 for e in ee))
        self.assertTrue(all(e['context'].startswith('development|') and e['stability_status']=='not_established' for e in ee))
    def test_invalid_results_retained_not_scored(self):
        pp=plan(['SELF-CREDIT']);rr=complete(pp,lambda t,n,a:dict(a,self_credit=1000))
        rows,summary,_,_=p.score(B,pp,rr);self.assertEqual(summary['quality'],{'invalid':16});self.assertFalse(summary['facet_estimates'])
    def test_heldout_statistics_do_not_pool_development(self):
        pp=plan(['SELF-CREDIT'],split='heldout');_,summary,g,_=p.score(B,pp,complete(pp))
        self.assertEqual(summary['split'],'heldout');self.assertTrue(all(x['n_scenarios']==2 for x in summary['facet_estimates']));self.assertIsNotNone(g['analysis_lock_hash'])
    def test_all_forms_process_and_graph_has_provenance(self):
        for partition in ['development','heldout']:
            pp=plan(split=partition);rows,summary,g,review=p.score(B,pp,complete(pp))
            self.assertEqual(summary['quality'],{'valid':len(pp['trials'])});self.assertTrue(review)
            ids={n['id'] for n in g['nodes']};self.assertEqual(len(ids),len(g['nodes']));self.assertTrue(all(e['source'] in ids and e['target'] in ids for e in g['edges']))
            self.assertTrue(all('paraphrase' in n and 'split' in n for n in g['nodes'] if n['kind']=='item'))
            p.write(ROOT/f'tests/v4-{partition}-fixture.graph.json',g)
    def test_tampered_plan_rejected(self):
        pp=plan();pp['trials'][0]['split']='heldout'
        with self.assertRaises(ValueError):p.next_requests(B,pp,[])
if __name__=='__main__':unittest.main()
