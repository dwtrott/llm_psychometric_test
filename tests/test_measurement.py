"""Counterexamples must block interpretation, not become midpoint traits."""
import json
from pathlib import Path
import tempfile
import unittest
from test_full_battery import r,ROOT,CONFIG,a,B


class Measurement(unittest.TestCase):
    def test_constant_code_is_not_moderate_risk(self):
        with tempfile.TemporaryDirectory() as d:
            b,p=r.prepare_run(dict(CONFIG,presentation_rounds=4),d,'position',facets=['DEC-RISK'],battery_dir=ROOT/'battery_full')
            r.collect(b,p,d,lambda *args:dict(text='{"action":"submit","answer":{"choice":"P2"}}'))
            result=r.export(d);g=json.loads(Path(result['graph']).read_text(encoding='utf-8'))
            for s in g['tendency_strengths']:
                self.assertEqual(s['observed_choice_mean'],.5)
                self.assertIsNone(s['value'])
                self.assertEqual(s['validity']['status'],'presentation_sensitive')
                self.assertEqual(s['validity']['invariant_code_changing_meaning_cells'],4)
            profile=a.load_profile(result['graphs'][0]);analysis=a.analyze([profile])
            finding=next(f for f in analysis['profiles'][0]['findings'] if f['facet']=='DEC-RISK')
            self.assertIn('withheld',finding['headline'])
            self.assertEqual(a.compare(profile,profile)['cells'],[])
            self.assertNotIn('DEC-RISK',g['profile_catalog']['primary'])

    def test_support_context_crosses_need_instead_of_pooling_unlike_requests(self):
        for split in ['development','heldout']:
            ts=[t for t in B['items'] if t['module']=='AFFECT-NEED' and t['split']==split]
            self.assertEqual(len({t['scenario'] for t in ts}),2)
            for scenario in {t['scenario'] for t in ts}:
                arms=[t for t in ts if t['scenario']==scenario]
                self.assertEqual({t['condition'] for t in arms},{'requested_listening','requested_practical_help'})
                self.assertTrue(all('need_fit' in t['stages'][0]['rubric'] for t in arms))

    def test_social_uncertainty_does_not_command_scored_alternative_generation(self):
        for t in B['items']:
            if t['module']!='SOC-BELIEF':continue
            prompt=t['stages'][0]['prompt'].lower()
            self.assertNotIn('give two',prompt);self.assertNotIn('two plausible',prompt)
            options=t['stages'][0]['fields']['interpretation_strategy']['options']
            self.assertTrue(options['B'].startswith(('Ask Mira','Send:')))


if __name__=='__main__':unittest.main()
