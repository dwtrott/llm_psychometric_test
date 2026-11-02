# Scored v0.10 battery: prompts, scenarios, wordings and transfer

[Open the A100 Colab notebook](https://colab.research.google.com/github/dwtrott/llm_psychometric_test/blob/main/battery_core/Run_HuggingFace_A100.ipynb) · [Actual questions](PROMPTS.md) · [CSV](prompts.csv) · [Side-by-side question file](side-by-side.html)

Choose an A100 runtime and **Run all** with the defaults. The notebook uses this expanded battery, not the compact list. It downloads Qwen2.5-7B-Instruct by default. No paid inference API is used. Use a new run label, `scored-v010`; an old run cannot be resumed against new questions.

The base instrument contains **240 cards / 280 stages**. The default four presentation rounds run **960 conversations / 1,120 question stages**, plus up to **64 optional-resource requests**. The same scenario is repeated under different response-menu codes and positions; these are not independent scenarios. Each card begins a fresh conversation. There are 120 development cards and 120 held-out cards, each partition containing both original and alternate task instructions. A repetition repeats these same cards; it is not a new independent scenario. Greedy identical repeats are not a useful estimate of sampling variability.

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
- **Instruction wording:** the scenario facts remain verbatim. Only the question/instruction is paraphrased, with identical response fields, payoffs, resources, constraints and scoring. This tests sensitivity to task wording, not a complete linguistic paraphrase of the situation. Response menus rotate across presentation rounds, independently of wording. Four rounds fully balance two- and four-option menus; three-option menus require a multiple of three. Use 12 rounds to balance all menu sizes. Scenario narratives remain fixed, so the measured effect is response-menu presentation, not every possible order of facts.
- **Held-out transfer:** each development stratum has a different situation with matched underlying decision structure and incentives. Arithmetic/logical demands remain matched in capability controls. Rubrics, feature definitions, pairing and stimulus hashes are fixed before collection. There is no fitted score model or score tuning on held-out answers. “Held-out” means reserved for this analysis, not unseen during LLM pretraining or secret from a person reading the CSV.
- **Models:** compare identical battery hashes and the same partition, settings and presentation cells. The analyzer preserves scenario and wording distinctions. The graph contains task observations and evidence; relationships labelled researcher design are not learned causal psychological connections.

Accuracy and reference-answer errors remain separate capability measurements. Social-inference correctness and audience-fit ratings are also performance observations; do not interpret them as intrinsic sociability or empathy. Written content is now scored by a separate local-model rubric pass. Each accepted score carries an exact response quotation, a rationale, rubric anchors and judge provenance. These are provisional automated judgments, not human ratings or proof of a trait. Format-valid judgment JSON and a matching quotation do not establish that the judgment itself is correct. Missing or invalid judgments remain unscored.

## Completion and files

Before collection the notebook lists every facet × partition × wording count. The default scope is all facets. Selecting a subset requires explicitly enabling `ALLOW_PARTIAL`; the audit labels it as a subset.

After downloading, extract the whole ZIP and open **START_HERE.html**. It shows accepted versus planned cards for every facet, partition and wording, all actual prompts and answers, and any missing stages. A rejected response stops that card's dependent follow-ups; all other cards are still attempted. Runtime errors interrupt collection and can be resumed. A full progress bar means processed, not accepted. No response is silently rewritten, retried or fabricated.

- `results/graph-development.json`: development evidence for the analyzer and viewer.
- `results/graph-heldout.json`: held-out evidence, kept separate.
- `results/analysis/report.html`: profiles, wording contrasts and matched transfer comparisons.
- `results/viewer.html`: graph viewer with both partitions.
- `results/graph.json`: combined archival evidence; do not load it into the partition-aware analyzer.
- `results/human_review-development.template.jsonl` and `results/human_review-heldout.template.jsonl`: pending content ratings matched to each partition graph. Use the matching template with `battery_v7/content_ratings.py`. The combined template is for the combined archival graph only. Automated scores are kept separate from these human-review templates.
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

## What is automatically scored in v0.10

- **Explicit choices and quantities:** every non-association card has a numeric decision or fixed response option. New menus cover conceptual organizing basis, proposed mechanism, communication strategy, interpretation strategy and support strategy. Per-option frequencies are retained, not collapsed into a good/bad personality total. Selecting a strategy does not prove that the written response implements it.
- **Written content:** existing task-specific rubrics (support fit, mechanism diversity, feasibility, adaptation, audience fit, perspective separation, contribution accuracy, disclosure and others) plus factual and decision consistency. Scores are 0–2, normalized to 0–1 only for graph comparison. The original anchors and score provenance remain attached. Insufficient evidence is null, never zero.
- **Consistency checks:** a narrow deterministic check flags an explicit opening assertion of returning half of 12 when the submitted return differs from 6. Other factual and explanation/decision conflicts are assessed by the rubric scorer, not falsely advertised as deterministic fact checking. Accuracy and confidence controls stay separate from preference scores.

The default judge is Qwen2.5-7B-Instruct, held fixed when the subject model changes. If it is also the subject, its loaded weights are reused in fresh conversations. Otherwise subject weights are freed before loading the judge; no paid API is used. This is convenient but has self-evaluation and shared-model biases. The runner's `evaluate_run` API accepts a separate generator and records its configuration if a different local judge is used. Do not mix judge configurations within an evaluation journal. Human review remains available for validation; machine ratings never impersonate two agreeing human raters.

`evaluation.jsonl` preserves raw judgments and is resumable. `evaluation_config.json` records the judge and protocol. In the KG, automated nodes carry `measurement_level=automated_rubric_score`; exact-rule checks use `deterministic_consistency_check`. Their trial-level features feed the existing analyzer's wording, scenario, transfer and between-model comparisons. Comparisons involving automated ratings should use the same judge configuration. The run's `results/measurements.html` shows selections, actual written answers, rubric scores, excerpts and rationales together.

The source snapshot and notebook now enforce adapter 1.3.0 and battery 0.10.0. A stale notebook that fetches new repository code will stop with a clear error instead of silently running the compact bank. Reopen the GitHub notebook in a fresh runtime; do not just rerun old cells. Keep `FACETS=None`, and use the new run label. The full-scope checks run before model loading and again before collection.

No real A100 execution or empirical judge-accuracy validation is claimed by the repository's synthetic tests. Response and scoring failures are visible in the outputs and must be inspected before interpreting a profile.

## Choice keys and strength estimates

Read [the explicit scoring key](SCORING.md). Each option has a canonical meaning and fixed dimension weights. New dimensions include agency focus, relational focus, information/incentive/procedure redesign preference, clarification seeking, early interpretive commitment, listening, immediate advice, agreement and supportive challenge. Existing risk, allocation, trust, reciprocity, autonomy, disclosure and harm rules remain explicit in the same key. These are candidate behavioral tendencies, not established clinical or Big Five loadings.

The runner rotates response codes and menus across `PRESENTATION_ROUNDS` and updates the scoring key with the same mapping. The KG keeps both the submitted code and its decoded meaning. Thus P1 does not consistently mean listening or risk-taking. Task wording and presentation round are separate factors. `REPEATS` remains a distinct repeat factor.

`graph.json` and each partition graph contain `tendency_strengths` and typed `behavioral_tendency` nodes linked to the actual scored trials. The readable measurements report shows their scenario-balanced estimates and valid/planned counts. No extra confidence is claimed from repeated forms of the same scenario. Conditions and development/held-out partitions remain separate; the analyzer reports presentation effects instead of hiding them in a single personality number.

For comparisons, keep judge model/revision, decoding and rubric protocol fixed. The analyzer excludes automated rubric measures when judge configurations differ, while retaining fixed-rule behavioral comparisons. The default notebook therefore keeps `JUDGE_MODEL_ID` fixed even when you change `MODEL_ID`.
