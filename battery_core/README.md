# Start with the prompts

**[Read the actual prompts, grouped by category](PROMPTS.md)** · **[Download the CSV](prompts.csv)**

**[Run the battery on a Hugging Face model in Colab](https://colab.research.google.com/github/dwtrott/llm_psychometric_test/blob/main/battery_core/Run_HuggingFace_A100.ipynb)**

Select an A100 runtime, then **Run all**. Open **START_HERE.html** in the downloaded ZIP first: it lists completion, category/facet coverage, every question and the exact responses. Processed cards are not necessarily accepted cards. The notebook downloads `Qwen/Qwen2.5-7B-Instruct` by default, runs all prompts/follow-ups locally on the GPU, saves each unedited response, and downloads a ZIP with the graph, scores, analyzer report and viewer. Change `MODEL_ID` to use another compatible model; `Qwen/Qwen2.5-1.5B-Instruct` is a smaller option. No API key is needed for these defaults. Model execution adds Transformers/Accelerate/PyTorch dependencies; the battery and analyzer remain standard-library Python.

An interrupted collection resumes by rerunning its cell. Optional Drive storage preserves results beyond runtime deletion. For a full-runtime resume, pin `SOURCE_REVISION` and `MODEL_REVISION` to the saved commits and keep the configuration unchanged. Invalid model responses are retained, not silently repaired or retried. This notebook's syntax and checkpoint/export pipeline have been tested locally with synthetic generators; a live Colab/A100 model run has not been verified here. [Notebook source](Run_HuggingFace_A100.ipynb).

The compact core has **50 prompt cards across 11 categories and 22 facets**. Ten cards have a follow-up, so the CSV contains 60 stage rows. Eight cards elicit associations to different cue words. The other 42 cards supply two scenarios per facet. These are actual text-only questions; no images or external stimuli are needed.

| Category | Included facets |
|---|---|
| Meaning and conceptual organization | Associations; organizing distinctions and their application |
| Evidence and reasoning | Unsupported authority; belief revision |
| Metacognition and uncertainty | Confidence and purchasing verification |
| Curiosity, creativity and flexibility | Optional information seeking; generating and adapting solutions |
| Risk, ambiguity and time | Risk choices; unknown probabilities and beliefs; delayed benefits |
| Social inference and communication | Audience adaptation; separating evidence from inferred mental states |
| Emotional understanding and support | Listening to stated needs; support without endorsing unsupported beliefs |
| Cooperation and trust | Allocation; vulnerability to another's choices; reciprocity |
| Values and autonomy | Informed individual choice; collective participation and exclusion |
| Self-evaluation and motivation | Recognition and contribution; persistence versus switching |
| Integrity, harm and alignment | Disclosure; selective/false influence; imposed losses |

The disclosure, influence, credit and harm questions probe behaviors relevant to Dark Triad discussions. They do not assign narcissism, Machiavellianism or psychopathy scores. The list is a research-informed exploratory instrument, not a validated full psychological fingerprint. It deliberately exposes the questions and limits instead of multiplying presentation variants. Two scenarios do not establish stable traits; some pairs are controlled contrasts, not independent methods. There are no claimed held-out tests or paraphrase/order robustness estimates in this release.

## Use with the existing harness

The CSV is versioned separately from v0.7 because its question content changed. Keep the repository folders together: this runner reuses the existing standard-library staged engine. Model credentials belong in your API adapter, not the config or graph.

1. Copy `config.example.json` to your run configuration and enter the actual model/provider/settings.
2. Prepare requests:

```sh
python battery_core/processor.py prepare --config model-a.json --run-id model-a-core --out runs/model-a-core
```

3. Send each request's **`messages` only** to the model, in a fresh conversation per card. Save the unedited response in a JSONL envelope carrying `trial_id`, `config_id`, `plan_hash`, `event_index`, `request_hash`, `status: "ok"`, and `raw_response` (the model's raw text). These identity fields come from the request. Use `status: "api_error"` for a failed API call. The prompts request JSON actions; they are not free-form completions. Do not send the CSV, evaluator keys, review rubrics or plan to the model.
4. Continue follow-up stages and optional resources, then process:

```sh
python battery_core/processor.py next --plan runs/model-a-core/plan.json --responses runs/model-a-core/responses.jsonl --out runs/model-a-core
# Collect the new requests; repeat next until requests.jsonl is empty.
python battery_core/processor.py process --plan runs/model-a-core/plan.json --responses runs/model-a-core/responses.jsonl --out results/model-a-core
```

The runner makes no API calls itself. The [existing collection guide](../battery_v3/COLAB_GUIDE.md) explains the response-envelope loop; use `battery_core/processor.py` for this list. `--repeats 2` repeats exactly the same cards and is not an independent-scenario count. `--facets COOP-TRUST DEC-TIME` selects a smaller subset; compare identical subsets across models.

5. Open results with the **existing** analyzer or viewer:

```sh
python analyzer/psychometric.py results/model-a-core/graph.json results/model-b-core/graph.json --out results/core-comparison
python viewer/viewer.py results/model-a-core/graph.json results/model-b-core/graph.json --out results/core-viewer.html
```

Open `results/core-comparison/report.html` for region summaries, model differences and evidence, or `results/core-viewer.html` for the interactive graph viewer. The same `graph.json` works in both. The analyzer uses the supplied catalog of categories and metric definitions. It rejects numeric comparisons across different instrument hashes. **The separate `network_atlas` remains an illustrative prototype and does not import these graphs.**

## What is actually scored

Choices, allocations, belief changes, resource requests and association edges are extracted automatically. Keyed correctness and reference errors are exported as separate capability controls, not added to a personality score. The main analyzer excludes those control fields from the profile-feature comparisons; they remain inspectable in the raw graph and trial output.

Written distinctions, explanations and messages remain available as response evidence. The CSV supplies explicit three-level rubric anchors for content that needs judgment: agency salience, application consistency, mechanism diversity, feasibility/adaptation, audience fit, perspective separation, support fit, contribution accuracy, material disclosure and factual accuracy. These are operational ratings, not human norms or hidden-intent judgments. The agency code is one specified organizing dimension; other distinctions remain in the raw response rather than being silently mapped to that code.

To include content ratings in the analyzer and KG:

```sh
python battery_v7/content_ratings.py --graph results/model-a-core/graph.json --templates results/model-a-core/human_review.template.jsonl --out results/model-a-core/review
# Two independent raters complete separate copies of rating_tasks.jsonl.
# Combine their completed records into completed-ratings.jsonl.
python battery_v7/content_ratings.py --graph results/model-a-core/graph.json --templates results/model-a-core/human_review.template.jsonl --ratings completed-ratings.jsonl --out results/model-a-core/rated
python analyzer/psychometric.py results/model-a-core/rated/rated_graph.json --out results/core-rated-analysis
```

Each rating needs a named rater, exact response quotation, rationale and unchanged graph/rubric hashes. At least two raters must agree; disagreements and missing ratings remain unscored. Rater independence and blinding require study procedures; different names alone do not prove independence. The supplied tasks retain the transcript and trial identity. See [rating-import details](../battery_v7/CONTENT_RATINGS.md).

Agreed content scores appear as separate `rating_*` features and evidence-linked graph nodes. The original 0–2 ratings and quotations are retained. Charts normalize these scores to 0–1: displayed percentages mean **fraction of rubric maximum**, not response probability, human percentile or trait strength. Missing ratings never become zeros. The analyzer's cross-pattern links remain explicitly untested hypotheses; importing these responses does not infer a latent psychological network.

## Colab and verification

The Python runner, content importer and analyzer use only the standard library. Clone/download this repository in Colab, keep its folders together and run the same commands with `!python`. The existing [analysis notebook](../analyzer/Psychometric_Analysis.ipynb) also accepts these graph exports after fetching the updated analyzer. No image or external asset download is needed to answer the prompts. Live Colab execution has not been checked here.

Automated checks exercise all 50 cards, follow-up/resource requests, response validation, separate controls, missingness, rating agreement and provenance, two-model comparison, KG integrity, SVG generation, and the existing viewer export. Fixtures are explicitly synthetic. They test the software contract, not psychological validity, real-model behavior or rater agreement in practice.

The authoring source is [build_core_prompts.py](../scripts/build_core_prompts.py); the rendered CSV and question list are committed for direct reading. Regeneration changes instrument identity if wording or rules change. Sources and adaptation status are listed at the end of the [prompt list](PROMPTS.md).

## Response protocol correction (0.8.1-core)

The first Qwen 7B run exposed ambiguous formatting instructions: the old template placed field definitions where answer values belonged. The new protocol lists required value types in plain language. Question content is unchanged, but the protocol and battery hash change; use a new run label (`format-v1`) and do not pool it with old runs. The notebook fetches the selected source revision each time setup runs. The updated formatting has offline regression coverage; successful completion on a live model still needs verification.

The audit reports missing and rejected stages rather than silently repairing them. Format acceptance is not correctness, content review, or proof of a stable psychological pattern. To audit an older downloaded ZIP with its original battery data (without executing its archived code):

```sh
python battery_core/run_audit.py path/to/results.zip --out results/run-audit
```
