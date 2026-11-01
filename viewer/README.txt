PSYCHOMETRIC KG VIEWER — exploratory version 0.1

V0.7 DESIGN-AWARE ANALYSIS
For the current battery, start with ../analyzer/README.md and
../analyzer/Psychometric_Analysis.ipynb. The new Python-only analyzer generates
an offline HTML/SVG report with presentation sensitivity, matched-model effects,
held-out transfer and aligned concept differences. This legacy viewer remains
available for interactive pan/zoom exploration and earlier graph formats.

START HERE
Open demo.html in a modern desktop browser for two explicitly SYNTHETIC profiles.
Open viewer.html for an empty viewer, then select processor graph.json exports.
No installation, CDN, server, account or model API is needed for local use.
The demo illustrates functionality; it is not evidence about any actual LLM.

COLAB
Upload Psychometric_KG_Viewer.ipynb to Google Colab and run its cells in order.
It embeds the complete viewer and Python helper. Upload one or more graph.json
exports when prompted. It displays the viewer and downloads a portable HTML.
Colab uploads enter your cloud session; local browser use keeps files local.
Live Colab execution has not been verified. If inline output is too large,
download the generated HTML and open it locally.

PYTHON (3.10+; standard library only)
Keep viewer.py and viewer.html together. From this directory:
  python viewer.py path/to/model-a/graph.json path/to/model-b/graph.json --out comparison.html
With no graph arguments it creates an empty importable viewer.
Do not use viewer.html itself as the output path.

INPUT CONTRACT
Input is graph.json from the separate psychometric battery processor v0.1.0.
Scores, prompts, raw responses, statuses, provenance and semantic edges are
already in this graph. No scores.json is necessary. CSV graph tables alone are
not accepted. One run and model configuration per graph file. Up to 80 MiB,
100,000 nodes and 300,000 edges per profile; practical memory limits may be lower.
The visualizer does not call models or rescore raw answers.

FOUR VIEWS
Full profile: eight broad research-defined domains and 28 modules. Select a
module for all available metrics by condition, scoring interpretation, research
context and supporting trials. Overview scalar values pool tested conditions;
use condition-level comparisons for interpretation. No domain total is created.
Open-ended ideas and elicited distinctions remain available in trial evidence
and require review; they are not assigned automatic psychological scores.

Concept graph: directed associations, conditional similarity and concept-rating
layers. Choose context, filter values, search/select a concept, inspect links
and their supporting trials. Pan by dragging and zoom by scrolling. Comparison
overlay shows shared and one-sided links. Up to 140 nodes and 650 edges are drawn;
the selected-concept table includes relationships outside the drawn subset.
Line width represents the measured value (the larger value in an overlay).
Layout positions are illustrative, not psychological distances.

Exploratory regions: weighted label propagation on the displayed undirected
association projection. Region membership can change with filters and graph
limits. Design-anchor overlap is researcher metadata, not independent evidence
of a trait. Human psychological constructs are interpretive hypotheses.

Compare profiles: requires identical battery hashes, exact item IDs and matching
conditions and metric names. Within each cell, only items with valid observations
in both profiles contribute. Repeats are averaged within scenario families;
families have equal weight. B minus A is descriptive, with counts and evidence.
Different generation settings are flagged. Different model versions, prompts,
sampling, refusal patterns and task coverage can confound interpretation.
Missing/refused/invalid/error trials are never converted into zero scores.
No uncertainty intervals, significance tests, latent traits, global similarity
score, human norms or psychometric measurement-invariance claims are supplied.
Use All scored measures to see secondary measures, including ambiguity choices.

Trial evidence: filter by module, status and text; inspect actual prompt, response
and measurements. This includes elicited distinctions and generated ideas that
are not rendered as automatic trait regions.

SEMANTIC COMPARISONS
Concept IDs retain the processor's case/whitespace normalization; synonyms are
not merged. Association weights are inclusion proportions, not correlations.
One-sided links mean observed only in one export, not a confirmed zero elsewhere.
Similarity comparisons retain the exact offered comparison set and item ID.
Concept ratings use 0–6 scales. Zero-valued offered similarity edges are measured
zeros and can be displayed. Missing edges are never assigned numeric deltas.

BREADTH AND LIMITS
Meaning; learning/reasoning/executive tasks; evidence/confidence; risk/time;
social understanding/support/cooperation; values; self-evaluation; and integrity/
harm/alignment are all represented. Deception and Dark Triad-inspired probes are
one component. Behavioral analogues do not diagnose narcissism, psychopathy or
Machiavellianism, establish emotions, or estimate real-world deception rates.
This is a research-informed exploratory instrument, not a validated full model
of LLM psychology. Sources inherited from the battery are in sources.json.

EXPORTS AND PRIVACY
Export comparison CSV saves the currently filtered measurements. Save portable
viewer embeds every loaded profile, including raw prompts and responses. It
does not preserve current view/filter selections. Share accordingly. Imported
strings are escaped and a Content Security Policy blocks external connections.

FILES
viewer.html                     empty offline application
viewer.py                       optional Python embedding helper
Psychometric_KG_Viewer.ipynb     self-contained Colab notebook
demo.html                       viewer with two synthetic profiles embedded
synthetic-A.graph.json / B       synthetic examples, not model measurements
sources.json                    research context from the battery
verification.txt                verification scope and limitations

DEDICATED GRAPH COMPARISON
Choose Graph comparison in the sidebar after selecting a comparison profile.
The A, B and difference panels use a single joint layout with synchronized
pan/zoom and node selection. Gray solid links have differences within the chosen
tolerance; teal solid links are stronger in A, orange solid links stronger in B.
Difference widths encode absolute B-minus-A changes. One-sided observations are
dashed and fixed-width, with no inferred numeric difference. Side-panel widths
encode original measured strengths. Measured zero edges remain distinct from
unobserved edges. The tolerance is descriptive, not statistical equivalence.
Counts cover the full selected layer/context; drawings are capped at 100 nodes
and 450 links, chosen jointly so both profiles have exactly the same positions.
Select a node to inspect all its relationships and evidence, including links
outside the drawn subset. At narrower widths the difference panel moves below
the paired profiles; small phone screens stack all three.
