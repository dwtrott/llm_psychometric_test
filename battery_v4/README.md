# v0.4 — measuring reproducible response patterns

**Review before administering:** the [2026-11-01 critical review](reviews/CRITICAL_REVIEW_2026-11-01.md) identifies material paraphrase defects, repeated task structures and held-out confounds. Its [96-scenario audit](reviews/v0.4-scenario-audit-2026-11-01.csv) is an AI-authored self-review, not independent validation. The original v0.4 questions and scoring remain unchanged for reproducibility.

This revision reorganizes the **core** around 16 candidate facets across all 12 profile regions. Each facet has six authored scenario forms: **four development forms and two held-out forms**, each crossed with **two paraphrases and two context conditions**. Repetitions are a separate dimension. The association facet elicits four cues in separate conversations per cell.

The aim is to test whether patterns survive wording changes and transfer to new situations. These are candidate psychological interpretations, not validated traits. Authored forms are not automatically statistically independent measures; shared task structures and topic effects remain limitations. The [review sheet](scenario_review.template.csv) is part of the instrument, not completed validation.

## Read the actual questions

Each page contains complete questions, both wordings, conditions, later stages, resources, keys and rubrics. This is an evaluator edition: labels and later-stage material must not be sent to the tested model.

| Region | Core facets | Questions |
|---|---|---|
| Conceptual organization | Contextual associations; preferred distinctions | [SEM](question_book/SEM.md) |
| Evidence | Evidence-responsive revision; prestige sensitivity | [EPI](question_book/EPI.md) |
| Metacognition | Confidence-dependent verification | [META](question_book/META.md) |
| Executive behavior | Constraint-sensitive plan adaptation | [EXEC](question_book/EXEC.md) |
| Creativity and flexibility | Generative diversity and constraint adaptation | [OPEN](question_book/OPEN.md) |
| Decisions | Risk framing; unspecified-probability preference | [DEC](question_book/DEC.md) |
| Social understanding | Recipient-knowledge adaptation | [SOC](question_book/SOC.md) |
| Emotional support | Clarification and fit to revealed needs | [AFFECT](question_book/AFFECT.md) |
| Social allocation | Sharing and audience sensitivity | [COOP](question_book/COOP.md) |
| Values | Informed choice, protection and autonomy | [VALUE](question_book/VALUE.md) |
| Self-evaluation | Credit attribution and recognition | [SELF](question_book/SELF.md) |
| Integrity and harm | Material disclosure under reward conflict; imposed-loss tradeoffs | [ALIGN](question_book/ALIGN.md) |

There are **96 scenario forms, 456 scenario × wording × condition × cue sessions, and 600 required response stages per repetition**. Development comprises 304 sessions / 400 stages; held-out evaluation comprises 152 sessions / 200 stages. Optional information requests add responses. Session counts are not independent-scenario counts.

The association cues are responsibility, uncertainty, autonomy and trust. This narrower repeated-context core does not replace v0.3's broader vocabulary panel. The [v0.3 battery](../battery_v3/README.md) remains **supplementary coverage**, including learning, temporal choice, concept boundaries, richer value contrasts and cancellation. Do not pool versions. The core spans all regions without claiming exhaustive coverage of psychology.

## Files

- [questions.csv](questions.csv): actual content and evaluator fields, read directly by the processor.
- [facet_map.csv](facet_map.csv): interpretation, outcomes, competing explanations, research foundations and control links.
- [design_manifest.json](design_manifest.json): fixed scenario groups, partitions and scheduling constraints.
- [scenario_review.template.csv](scenario_review.template.csv): review of wording equivalence, manipulation isolation and scenario distinctiveness.
- [DESIGN.md](DESIGN.md): administration, interpretation and held-out protocol.
- [SCORING.md](SCORING.md): features, aggregation and graph provenance.
- [processor.py](processor.py): standard-library Python runner; keep `_engine.py` beside it.
- [analysis_spec.example.json](analysis_spec.example.json): template to complete and freeze before held-out collection.
- [controls/](controls/README.md): unchanged snapshot of the 18 v0.3 control families; their separate version/hash is intentional.
- [VALIDATION.md](VALIDATION.md): software verification and empirical status.

## Development collection

Python 3.10+, standard library only. No database, downloaded embeddings or inference service is required by scoring. Model access is supplied separately.

```sh
# Edit provider/model and actual generation settings first.
python battery_v4/processor.py prepare --config battery_v4/config.example.json --run-id model-a-dev --split development --repeats 2 --out runs/model-a-dev
# Collect model responses, sending ONLY each request's messages array.
python battery_v4/processor.py next --plan runs/model-a-dev/plan.json --responses runs/model-a-dev/responses.jsonl --out runs/model-a-dev
python battery_v4/processor.py process --plan runs/model-a-dev/plan.json --responses runs/model-a-dev/responses.jsonl --out results/model-a-dev
```

For a smaller check, add `--facets META-VERIFY COOP-SHARE SELF-CREDIT`. This selects whole facets and their crossed design, not favorable individual questions; it is not a full profile. Two repetitions balance binary display order but not three-way rotations. Six balance both; neither recommendation is a statistical power calculation.

The response envelope and collect → next loop match v0.3. In the [Colab walkthrough](../battery_v3/COLAB_GUIDE.md), change the import to `battery_v4/processor.py`, use a new run name and this version's `prepare`/`score`. Do not reuse old plans or responses. Python subset example: `processor.prepare(battery, config, run_id, repeats=2, facets=['META-VERIFY', 'COOP-SHARE'], split='development')`.

## Freeze before held-out collection

Complete the specification with model configurations, selected features, comparison/exclusion rules, concrete held-out predictions, and a rating policy. Keep frozen predictions, codebooks and development result hashes with the study.

```sh
# Save a completed copy as study-spec.json; the unedited template is rejected.
python battery_v4/processor.py freeze --spec study-spec.json --out studies/study-01/analysis-lock.json
python battery_v4/processor.py prepare --config battery_v4/config.example.json --run-id model-a-heldout --split heldout --analysis-lock studies/study-01/analysis-lock.json --repeats 2 --out runs/model-a-heldout
```

Use the same selected facets/repetitions across models, specifying `--facets` again if needed. Held-out plans require a matching battery lock and listed model configuration. The lock is an audit record, not proof that nobody has seen the public questions. Held-out means withheld from **this study's fitting and selection**, not guaranteed absent from model training.

## Results and graphs

Exports include raw trial scores, `features.csv`, design-aware `scores.json`, a human-review template and `graph.json`. Scores distinguish repeat variability, matched wording differences, scenario estimates and matched condition effects. They do not automatically declare stability, rate text, run held-out identification or fit latent traits.

The existing visualizer accepts the enriched graph. It remains a legacy HTML/JavaScript viewer; **all new collection and analysis code is Python only**. Compatibility does not mean the viewer has been rewritten in Python or already includes the planned stability dashboard.

```sh
python viewer/viewer.py results/model-a-dev/graph.json results/model-b-dev/graph.json --out results/development-comparison.html
```

Compare models within the same partition. Development and held-out items intentionally do not match for item-level subtraction. Evaluate generalization using frozen predictions, rather than treating partitions as different models. No model runs or empirical construct validation have been performed for this release.
