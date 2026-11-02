# Expanded battery: prompts, scenarios, wordings and transfer

[Open the A100 Colab notebook](https://colab.research.google.com/github/dwtrott/llm_psychometric_test/blob/main/battery_core/Run_HuggingFace_A100.ipynb) · [Actual questions](PROMPTS.md) · [CSV](prompts.csv) · [Side-by-side question file](side-by-side.html)

Choose an A100 runtime and **Run all** with the defaults. The notebook uses this expanded battery, not the compact list. It downloads Qwen2.5-7B-Instruct by default. No paid inference API is used. Use a new run label, `expanded-v09`; an old run cannot be resumed against new questions.

The full run contains **240 conversation cards / 280 question stages**, plus up to **16 optional-resource requests**. Each card begins a fresh conversation. There are 120 development cards and 120 held-out cards, each partition containing both original and alternate task instructions. A repetition repeats these same cards; it is not a new independent scenario. Greedy identical repeats are not a useful estimate of sampling variability.

## What is included

| Category | Facets | Development cards | Held-out cards |
|---|---|---:|---:|
| Meaning and conceptual organization | Associations; organizing distinctions | 20 | 20 |
| Evidence and reasoning | Unsupported authority; belief revision | 8 | 8 |
| Metacognition and uncertainty | Confidence and checking | 4 | 4 |
| Curiosity and creativity | Information seeking; generative flexibility | 8 | 8 |
| Risk, ambiguity and time | Risk; unspecified probabilities; delay | 16 | 16 |
| Social inference and communication | Audience adaptation; perspective separation | 8 | 8 |
| Emotional understanding and support | Support and boundaries | 4 | 4 |
| Cooperation and trust | Allocation; trust; reciprocity | 20 | 20 |
| Values and autonomy | Autonomy and protection | 4 | 4 |
| Self-evaluation and motivation | Recognition; persistence | 12 | 12 |
| Integrity, harm and alignment | Disclosure; influence; imposed loss | 16 | 16 |

Most facets contain two scenario strata in each partition. Risk, trust, reciprocity, recognition and imposed loss contain **two contexts with two contrast arms each**, rather than counting the arms as independent scenarios. Each scenario/arm has two instruction wordings. Associations use eight development cues and eight new held-out cues; different cues are not interchangeable measurements of one latent trait.

These are original research-informed text probes, with paradigm references retained in `battery.json`. They are not a complete or validated human personality inventory. No images, inaccessible questionnaires or external stimuli are needed. No narcissism, psychopathy or Machiavellianism diagnosis is produced.

## What the comparisons mean

- **Scenario observations:** inspect whether behavior recurs across distinct situations. Similar formal tasks across contexts are intentional near-transfer probes; neither context changes nor agreement alone prove psychological independence or generality.
- **Instruction wording:** the scenario facts remain verbatim. Only the question/instruction is paraphrased, with identical response fields, payoffs, resources, constraints and scoring. This tests sensitivity to task wording, not a complete linguistic paraphrase of the situation. Option-order effects are not estimated in this release.
- **Held-out transfer:** each development stratum has a different situation with matched underlying decision structure and incentives. Arithmetic/logical demands remain matched in capability controls. Rubrics, feature definitions, pairing and stimulus hashes are fixed before collection. There is no fitted score model or score tuning on held-out answers. “Held-out” means reserved for this analysis, not unseen during LLM pretraining or secret from a person reading the CSV.
- **Models:** compare identical battery hashes and the same partition, settings and presentation cells. The analyzer preserves scenario and wording distinctions. The graph contains task observations and evidence; relationships labelled researcher design are not learned causal psychological connections.

Accuracy and reference-answer errors remain separate capability measurements. Social-inference correctness and audience-fit ratings are also performance observations; do not interpret them as intrinsic sociability or empathy. Written content remains pending until explicitly reviewed with the supplied rubrics. Counts of format-valid answers do not substitute for these ratings.

## Completion and files

Before collection the notebook lists every facet × partition × wording count. The default scope is all facets. Selecting a subset requires explicitly enabling `ALLOW_PARTIAL`; the audit labels it as a subset.

After downloading, extract the whole ZIP and open **START_HERE.html**. It shows accepted versus planned cards for every facet, partition and wording, all actual prompts and answers, and any missing stages. A rejected response stops that card's dependent follow-ups; all other cards are still attempted. Runtime errors interrupt collection and can be resumed. A full progress bar means processed, not accepted. No response is silently rewritten, retried or fabricated.

- `results/graph-development.json`: development evidence for the analyzer and viewer.
- `results/graph-heldout.json`: held-out evidence, kept separate.
- `results/analysis/report.html`: profiles, wording contrasts and matched transfer comparisons.
- `results/viewer.html`: graph viewer with both partitions.
- `results/graph.json`: combined archival evidence; do not load it into the partition-aware analyzer.
- `results/human_review-development.template.jsonl` and `results/human_review-heldout.template.jsonl`: pending content ratings matched to each partition graph. Use the matching template with `battery_v7/content_ratings.py`. The combined template is for the combined archival graph only. No automatic judge is called.
- `instrument/`: exact battery JSON and CSV used by the run.
- `planned_coverage.json`, `plan.json`, `responses.jsonl`: scope, complete execution plan and unedited response journal.

Compare two models on development questions:

```sh
python analyzer/psychometric.py model-a/results/graph-development.json model-b/results/graph-development.json --out comparison
```

Check within-model transfer:

```sh
python analyzer/psychometric.py run/results/graph-development.json run/results/graph-heldout.json --out transfer
```

The implementation and complete execution path are tested offline with synthetic responses, including interruption/resumption and partition exports. Those tests are not real-model psychological validation or a guarantee that a model will answer every question in valid JSON. A live A100 run of this expanded version still needs to be performed.

## Authoring and preservation

`scripts/build_full_battery.py` contains the actual authored scenario and task-wording definitions. It preserves the compact release and exports `prompts.csv`, readable questions, side-by-side HTML and a manifest separating scenario facts from instructions. The content hash locks the expanded instrument. Edits produce a new battery identity; do not pool runs across different hashes.
