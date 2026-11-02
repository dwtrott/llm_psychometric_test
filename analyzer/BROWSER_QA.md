# Local browser verification — 2026-11-01

## Response findings and typed KG revision

- A's risk region reports gain-framed risky choices at 100% and loss-framed choices at 0%, with a -100 percentage-point matched condition effect across three scenarios.
- The finding's evidence chain opens fixed-design measurements and the actual prompt/assistant answer. Inspected response `DEC-RISK-S01.P1.gain.standard.order01-transfernone:r000` submits `RISK`.
- Model comparisons now display full-region behavior values and matched difference ranges, with wording/order checks alongside them. Concept-association graphs remain separately expandable.
- Automated checks cover opposite effects across scenarios, missingness without zero imputation, A/B's different order sensitivity, explicit unrated facets, unique KG node IDs, valid edge endpoints, candidate-facet status and held-out comparison provenance.
- All 12 analyzer tests pass. The fixture is synthetic; this verifies software, not psychological validity.

## Profile-first layout revision

Verified the redesigned report in a fresh localhost browser tab:

- Switching to Synthetic B hides the other profile panels and displays B's map.
- Clicking the risk region in A's map opens the corresponding region explanation automatically, including observed-choice disclosures and separate wording/order summaries.
- The comparison navigation opens a section with all three aligned concept graphs visible immediately.
- The detailed analysis and raw-evidence container is collapsed by default.
- Screenshots of the revised profile and comparison views are retained in the ignored local results directory. Computation and export formats are unchanged.

## Underlying analysis checks

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
