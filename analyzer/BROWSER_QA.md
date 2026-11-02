# Local browser verification — 2026-11-01

Tested the generated synthetic report in the in-app browser over a localhost HTTP server, using `results/analysis-demo/report.html`.

| Check | Observed result |
| --- | --- |
| Full profile | All 14 facets remain represented for both development profiles and the held-out profile. |
| Model comparison | DEC-RISK exposes eight matched measurement cells with B-minus-A differences of -1, 0 and +1 as constructed; bars show orange, gray and blue respectively. |
| Option order | Synthetic B's DEC-RISK table shows +1 in all 12 matched contrasts; Synthetic A shows 0, with two repeat pairs per contrast. |
| Wording | Synthetic A's DEC-RISK paraphrase table shows 0 in all 12 contrasts. |
| Concept comparisons | Three panels render A, B and B-minus-A with identical node coordinates. Gray links show equal observed rates, orange A-greater and blue B-greater. The private comparison reports 48 common valid exposures. |
| Link values | Difference tooltips include autonomy→context -1, autonomy→oversight +1 and autonomy→care 0. |
| Transfer-variant labeling | After regeneration and browser reload, the section reads “Transfer-pattern balance checks” and explains that first-stage choices do not score transfer performance. |
| Browser diagnostics | No captured warning or error messages at completion. |
| Regression tests | All 11 analyzer tests pass, including the corrected label and explanation. |

The report uses synthetic data, not measurements of real LLMs. The aligned panels are static SVGs; synchronized pan/zoom is not a feature of this Python report. Live Colab execution and human-coded transfer scoring were not tested. The browser screenshot is retained locally under the ignored results directory as `browser-comparison.jpg`.
