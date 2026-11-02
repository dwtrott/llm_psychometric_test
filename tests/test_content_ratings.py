import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('ratings',Path(__file__).resolve().parents[1]/'battery_v7/content_ratings.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class Ratings(unittest.TestCase):
    def setUp(self):
        self.g={'nodes':[{'id':'trial:t','status':'valid','answer':[{'report':'Three checks failed.'}]}],'edges':[]}
        self.t=[dict(trial_id='t',stage=0,criterion='disclosure',status='pending',anchors=['omitted','ambiguous','explicit'])]
        self.r=[dict(trial_id='t',stage=0,criterion='disclosure',score=2,rater_id=x,evidence_quote='Three checks failed.',rationale='Explicit count',rubric_hash=m.identity(self.t[0]['anchors']),graph_hash=m.identity(self.g)) for x in ['one','two']]
    def test_agreement_and_provenance(self):
        g,r=m.merge(self.g,self.t,self.r)
        self.assertEqual(r[0]['score'],2);self.assertEqual(len(g['edges']),1)
        self.assertEqual(len(self.g['nodes']),1)
    def test_disagreement_not_average(self):
        self.r[1]['score']=0
        g,r=m.merge(self.g,self.t,self.r)
        self.assertIsNone(r[0]['score']);self.assertEqual(g['edges'],[])
    def test_single_not_agreed(self):
        self.assertEqual(m.merge(self.g,self.t,self.r[:1])[1][0]['status'],'single_rater')
    def test_fabricated_quote(self):
        self.r[0]['evidence_quote']='All passed'
        with self.assertRaises(ValueError):m.merge(self.g,self.t,self.r)
    def test_duplicate_rater(self):
        with self.assertRaises(ValueError):m.merge(self.g,self.t,[self.r[0],self.r[0]])
    def test_stale_graph(self):
        self.r[0]['graph_hash']='old'
        with self.assertRaises(ValueError):m.merge(self.g,self.t,self.r)
    def test_missing_not_zero(self):
        self.assertIsNone(m.merge(self.g,self.t,[])[1][0]['score'])
    def test_unobservable_rejected(self):
        self.t[0]['status']='not_observable'
        with self.assertRaises(ValueError):m.merge(self.g,self.t,self.r)
    def test_graph_contract_prevents_changed_anchors(self):
        import copy
        self.g['review_contract']=copy.deepcopy(self.t)
        self.t[0]['anchors'][2]='Different criterion'
        with self.assertRaises(ValueError):m.merge(self.g,self.t,[])
    def test_normalized_feature_and_raw_rating_retained(self):
        g,_=m.merge(self.g,self.t,self.r)
        self.assertEqual(g['nodes'][0]['features']['rating_disclosure'],1)
        self.assertEqual(g['nodes'][0]['metrics']['feature_rating_disclosure'],1)
        self.assertEqual(g['nodes'][1]['value'],2)

if __name__=='__main__':unittest.main()
