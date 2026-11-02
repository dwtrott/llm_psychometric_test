# Design-aware analysis and visualization for v0.7

The battery is frozen. This software uses its existing dimensions to analyze actual response evidence. It does not propose another questionnaire revision.

`psychometric.py` is a single-file, **Python standard-library-only** analyzer and report generator. Its HTML report uses inline SVG and browser-native expandable sections: no JavaScript, CDN, server, API key or additional plotting library. The report is portable and works offline. The existing interactive graph viewer remains available separately for pan/zoom exploration and older formats.

## Inputs and outputs

Input: one or more `graph.json` exports produced by `battery_v7/processor.py process`. You do not need raw response files alongside those graphs: prompts, responses, task features and presentation metadata are embedded in the export. Supply only one run per exact model configuration and partition. Old battery graphs and capability-control banks are intentionally rejected rather than silently pooled with profile evidence.

```sh
python analyzer/psychometric.py results/model-a-dev/graph.json results/model-b-dev/graph.json --out results/analysis
```

Open `results/analysis/report.html`. The same directory contains complete `analysis.json`, per-profile cell and sensitivity CSVs, and matched-comparison cell/effect CSVs. HTML tables display bounded previews for large designs; the JSON/CSV outputs retain every computed row.

To examine held-out transfer, include the same model configuration's held-out graph:

```sh
python analyzer/psychometric.py results/model-a-dev/graph.json results/model-b-dev/graph.json results/model-a-held/graph.json --out results/analysis
```

## Response-derived findings and evidence KG

The opening map now shows observed behavior in each region, not just coverage. Condition-specific choice/response ranges and presentation effects remain separate. The first comparison view shows those behaviors across all regions; concept-association graphs are a separate expandable view. Interpretation gaps remain explicit.

The report exports `knowledge_graph.json`: typed model-run, region, candidate-facet, finding, measurement, context, scenario, response, presentation-check and comparison nodes, joined by explicit evidence relationships. Expand a region's evidence chain to inspect original responses. This is a candidate behavioral fingerprint, not a validated psychological fingerprint. See [the evidence model and validation boundaries](EVIDENCE_MODEL.md).

The analysis schema is now `psychometric-analysis-2` (additive findings/KG fields); the independent KG schema is `psychometric-evidence-kg-1`. Existing cell and comparison calculations and CSV formats are unchanged. Keep the complete output directory together when opening the report so its KG download link resolves; in Colab, download and extract the results ZIP.

## Detailed report components

The opening view presents **one model at a time** in a full-profile map. Select a model, then click a region to open its response-derived findings, observed choices and wording/order checks. All 11 regions and 14 facets remain available. The map shows measured behavior and interpretation gaps, not inferred trait strength.

**Compare models** jumps directly to regional behavior comparisons with visible A/B values and matched differences. Expand the concept graphs for a separate view of associations. Detailed measurement tables, held-out comparisons and raw responses are grouped in a collapsed **Detailed analysis & response evidence** section. Model switching and disclosures use native HTML/CSS; no JavaScript or new Python dependencies are required.

1. **Full profile and coverage graph.** All 14 catalog facets stay visible, including those with missing or unrated evidence. Research-defined region-to-facet links show the measurement design. Colors show evidence coverage, not trait strength. Counts distinguish scenarios from presentation variants and trials. Unselected facets show no supplied observations; they are not assigned zero scores.
2. **Behavioral measurements.** Means and repeat standard deviations remain conditional on scenario, condition, wording, base role/advice stratum, option order, conceptual transfer pattern and cue. Standard deviation is undefined with one valid repeat. Human-coded content is explicitly marked as not imported; it is not automatically rated from choice features.
3. **Design sensitivity.** Separate matched contrasts for condition, P1/P2 wording and option/label-position order, plus first-stage balance checks across conceptual transfer variants. Other factors stay fixed. Transfer-variant numeric contrasts describe choices made before the fourth case is shown; they do not measure application of the distinction to that case.
4. **Between-model differences.** Comparisons require the same battery hash and partition, and use shared valid feature/cell/repeat indices. Configuration differences are visible. Scenario means receive equal weight within each fixed design cell. There is no cross-condition, cross-role or cross-presentation pooling. Bars show B minus A; blue/orange mean greater/lower, not good/bad.
5. **Held-out transfer.** Identical configurations are joined by matched-pair ID instead of scenario ID. The held-out graph must have a lock identity. The report shows both feature-level changes and changes in within-scenario condition effects. It does not claim that a lock proves secrecy, or automatically score the study's frozen prediction rule.
6. **Aligned concept graphs.** A, B and a difference graph share positions. Association rates are recomputed from common valid exposures, with scenario weighting within cue. Gray difference links have equal observed rates; blue/orange indicate differences. At most 26 nodes/50 candidate links are drawn, with the truncation disclosed. Missing links mean no mentions in those observed exposures, not absence of conceptual knowledge. Layout distance is illustrative.
7. **Evidence inspection.** Expand a facet and trial to inspect its actual messages, status and derived task features. CSV/JSON evidence IDs identify the corresponding records. Model text is escaped; it is never executed as HTML or script.

## Statistical boundaries

These are descriptive summaries, not reliability certification, significance tests, latent factors or a global similarity score. Low observed wording/order effects do not establish a stable psychological trait. Repeat indices align the supplied design only; they do not imply coupled random draws across models. Missing, refused, invalid and error responses are excluded from numerical contrasts and retained in coverage counts. A comparison uses a common valid subset, which can still be selective; excluded observations are counted.

Condition-effect changes use repeat indices present in all four arms, avoiding differences based on unrelated missingness subsets. Evidence references and per-scenario results remain available. No automatic ratings, human norms, Dark Triad diagnoses or independence assumptions for presentation variants are introduced.

Coverage reflects the supplied graph/plan, not a reconstruction of the entire possible battery. This release does not import completed human-review forms, compute confidence intervals or automatically choose robust facets. Keeping those gaps visible is preferable to turning unrated content into inferred traits.

## Colab

Open [Psychometric_Analysis.ipynb](Psychometric_Analysis.ipynb) in Colab. It downloads the Python analyzer from this repository, lets you upload v0.7 graph exports, creates the report and downloads a ZIP of the results. Uploading places those files in your Colab session. No model calls are made. The analysis itself uses only the standard library; the notebook uses Colab's built-in upload/download and display helpers. Live Colab execution has not been verified here.

You can also copy `psychometric.py` alone into a notebook environment and call:

```python
import psychometric
report = psychometric.build(["model-a-graph.json", "model-b-graph.json"], "analysis-output")
```

## Synthetic demonstration and tests

```sh
python scripts/demo_analysis.py
python -m unittest discover -s tests -p test_analysis.py
```

The demo creates two synthetic configurations and one synthetic held-out run, processes their actual staged response envelopes through v0.7, and builds `results/analysis-demo/report.html`. Its constructed differences illustrate order effects, role attribution, allocation and concept-link differences. They are not results about any real model. Generated response data/reports stay under ignored `results/`; they are not published as research findings.

Browser testing over localhost verified model-comparison tables and bar colors, separate wording/order contrasts, shared concept-node positions, gray/orange/blue difference links, and expandable report sections. The conceptual transfer-variant table is explicitly labeled as a first-stage balance check: it does not score application of the distinction to the fourth case. Human-coded transfer performance remains unimported. The demo uses synthetic data; live Colab execution remains unverified.
