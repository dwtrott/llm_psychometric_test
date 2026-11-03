# v0.11: conditional measurement and validity checks

[Measurement specification](MEASUREMENT.md) · [Actual questions](PROMPTS.md) · [CSV](prompts.csv) · [Scoring keys](SCORING.md) · [Question comparison](side-by-side.html)

**The previous tendency-strength interpretation is withdrawn.** An option frequency is not a psychological trait strength. The current system retains observed choices and conditional contrasts but withholds latent-trait estimates. Interpretation requires evidence beyond prompt execution, scoring, or a good-looking graph.

## What changed

- The measurement specification covers all 11 regions and 22 facets. It states each proposed construct, observable, competing explanations and inference requirements. `measurement_spec.json` traces every question and option to its observation rules and contract.
- Canonical choices are checked across matched scenario, wording and repeat cells. Semantic reversals are reported. Selecting one displayed code as its meaning changes is exposed explicitly. These are descriptive diagnostics, not causal or significance tests.
- Method-confounded and presentation-sensitive measures are withheld from profile findings and numeric comparisons. Raw answers and descriptive rates remain inspectable. A stable code is not turned into a midpoint trait score.
- Support probes now cross requested listening versus practical help within two contexts in each partition. Their conditional reply rates are not pooled into empathy or listening strength. Request compliance remains a competing explanation.
- Social-uncertainty probes no longer tell the model to give multiple explanations. They ask for concrete actions with a stated cost for obtaining information. The observation is conditional information seeking, not a general open-mindedness trait.
- Strategy self-labels and explicitly instructed communication tasks remain method/performance probes. They cannot establish spontaneous psychological preferences. Fictional points describe scenarios, not calibrated human-like incentives.

## Run in Colab

[Open the current A100 notebook](https://colab.research.google.com/github/dwtrott/llm_psychometric_test/blob/main/battery_core/Run_HuggingFace_A100.ipynb) in a fresh runtime. Keep `FACETS=None` and use `measurement-v011`. The source must be battery `0.11.0-measurement` and adapter `1.4.0`; older cells stop instead of silently running an old battery.

There are **248 base cards / 288 stages**: 124 development and 124 held-out cards, each including two task wordings. Four response-menu rounds produce **992 conversations / 1,152 question stages**, plus up to 64 resource calls and a separate rubric-scoring pass for valid written stages. Repeated wordings and rounds are not independent scenarios. Four rounds balance two- and four-option response menus; use 12 to balance three-option menus too. Scenario narrative order remains fixed.

Each card starts a fresh conversation. Follow-ups retain only that card's history. Invalid responses stop dependent stages and remain visible. Runtime interruptions can resume. No missing answer is fabricated, repaired or silently scored as zero.

The default local subject and judge are Qwen2.5-7B-Instruct. The judge stays fixed when the subject model changes; same-model scoring is flagged when applicable. Automated rubric judgments carry excerpts and provenance, but matching excerpts do not establish correct judgments. Invalid or unsupported judgments stay unscored. The human-review workflow remains separate.

## Read the results

Open `START_HERE.html`, then `results/measurements.html` for actual answers, decoded options, descriptive rates, validity diagnoses, quotations and scoring rationales. The profile report suppresses unsupported psychological interpretations.

- `results/graph-development.json` and `results/graph-heldout.json`: separate partition evidence for the analyzer and viewer.
- `results/analysis/report.html`: conditional findings and admissible matched comparisons.
- `results/graph.json`: combined archival evidence, not the analyzer's partition input.
- `evaluation.jsonl` and `evaluation_config.json`: raw provisional judge outputs and identity.
- `results/human_review-development.template.jsonl` and its held-out counterpart: templates bound to the matching graphs for human review.
- `instrument/`, `plan.json`, `responses.jsonl`: the exact instrument, execution plan and original answers.

Graph nodes labelled `conditional_response_summary` contain observed means, contracts and validity diagnostics. Their `value` field is null because a trait strength is not identified; descriptive data are in `observed_choice_mean`. The legacy `tendency_strengths` array is retained for file compatibility only. `measurement_validity` records the reasons for withholding an interpretation. Automatic rubric nodes remain labelled `automated_rubric_score`, distinct from human ratings and deterministic checks.

The analyzer excludes blocked feature/condition cells from comparisons. It also excludes automated rubric scores when judge configurations differ. Raw evidence is retained for auditing. Cross-facet psychological relationships remain research hypotheses, not inferred causal connections.

```sh
python analyzer/psychometric.py model-a/results/graph-development.json model-b/results/graph-development.json --out comparison
```

To inspect within-model transfer, supply the development and held-out graphs from that run instead. A transfer result on these tasks is not proof of general psychological validity or absence of training contamination.

## Scientific status

This revision corrects misleading interpretations and specific confounds; it does not make the battery a validated personality instrument. Construct validity, independent content review, broader scenario sampling and external predictive evidence remain necessary. Synthetic tests verify the implementation and known counterexamples, not psychology. A synthetic constant-code regression verifies that a midpoint selection frequency is not promoted to a trait estimate. This check does not calibrate item parameters.
