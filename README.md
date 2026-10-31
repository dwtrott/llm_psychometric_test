# LLM psychometric testing and knowledge-graph visualization

A research-informed exploratory battery and an independent offline viewer for comparing LLM response profiles. **Not a validated personality test or a clinical diagnostic instrument.**

## Components

- [`battery/`](battery/README.txt): 436 CSV questions across 28 modules, Python preparation/scoring, configuration templates, research sources, and graph export.
- [`viewer/`](viewer/README.txt): self-contained HTML viewer, Python embedding helper, Colab notebook, and explicitly synthetic demonstrations.
- [`viewer/src/`](viewer/src/): editable JavaScript and HTML/CSS source.
- [`tests/`](tests/): 17 battery checks and 20 viewer checks.

Coverage includes conceptual associations, learning/reasoning, evidence/confidence, risk/time preferences, social understanding, values, self-evaluation, and integrity/alignment under conflict. Deception and Dark Triad-inspired behavioral probes form one component, not the entire profile. No global personality or alignment score is calculated.

## Quick start

Requires Python 3.10+ (standard library only). Open `viewer/demo.html` in a browser to explore two **synthetic profiles**, or open `viewer/viewer.html` and load processor `graph.json` exports. No CDN or server is required.

```sh
cd battery
# Edit config.example.json with the actual model configuration first.
python processor.py prepare --config config.example.json --run-id modelA-session1 --repeats 4 --out ../runs/modelA
# Collect model outputs using your own API adapter, then:
python processor.py process --plan ../runs/modelA/plan.json --responses ../runs/modelA/responses.csv --out ../results/modelA
cd ..
python viewer/viewer.py results/modelA/graph.json --out results/modelA/viewer.html
```

The processor prepares prompts and scores collected responses; it does **not** call a model API. Never send scoring keys, construct labels or the full plan to the tested model. See the battery guide for response formats and counterbalancing.

## Graph comparison

Select two profiles and open **Graph comparison**. A, B and difference panels share node positions, pan/zoom and selection. Gray indicates differences within a descriptive tolerance, teal stronger in A, orange stronger in B. Dashed links indicate one-sided observations; missing links are not zeros. Inspect a concept for the supporting trials.

Comparisons require the same battery hash. Scores are matched by item and condition; generation settings and missingness can confound differences. Semantic regions are exploratory and researcher-defined domains are organizing hypotheses, not validated latent traits.

## Colab

Upload [`viewer/Psychometric_KG_Viewer.ipynb`](viewer/Psychometric_KG_Viewer.ipynb) to Colab and run its cells. It contains the complete viewer and embedding helper; upload processor graph exports when prompted. Colab uploads are handled in your cloud session. The downloaded HTML works offline. Live Colab execution has not been verified.

## Development and validation

```sh
python scripts/build_viewer.py
python tests/test_battery.py
node tests/test_viewer.js
python -m http.server 8767 --bind 127.0.0.1 --directory viewer
```

Then visit http://127.0.0.1:8767/demo.html. Node is needed only for JavaScript tests. The build refreshes HTML, embedded demos and notebook from source. Browser checks confirmed shared positions, synchronized pan/zoom, linked selection, difference colors, tolerance controls and rating-layer switching. A horizontal-overflow issue found during testing was fixed. Demo outputs are synthetic; no real-model validation is claimed.

Research references, scoring rules and evidence limitations are included alongside each component. All imported raw prompts/responses are included when saving a portable viewer; do not commit private runs or credentials.
