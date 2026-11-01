# v0.6: matched decision structures across the profile

This is the content revision following the [v0.5 side-by-side review](../battery_v5/reviews/REVIEW_2026-11-01.md). The earlier instrument remains frozen. Read the [complete question book](question_book/), [actual question CSV](questions.csv), or download/open [the four-column comparison](side-by-side.html) locally. The comparison shows every condition, stage, response schema and scoring rule—not abbreviated sample prompts.

**Review before interpretation:** the [v0.6 content review](reviews/REVIEW.md) confirms improved structural matching but identifies eight scenarios with identical P1/P2 prompts and remaining compliance/construct confounds. [The annotated side-by-side page](reviews/annotated-side-by-side.html) preserves every original question with review notes. The review leaves this instrument unchanged.

**All 14 candidate profile facets remain:** contextual associations, conceptual distinctions, recognition sensitivity, metacognitive checking, creative generation/adaptation, risk framing, ambiguity preference, audience adaptation, support preferences, allocation, autonomy/consent, credit attribution, disclosure under incentives and harmful resource choices. There are 84 scenario forms and 504 sessions / 648 stages per repetition across both partitions, with 252 sessions per partition. These span 11 profile regions; executive scheduling and Bayesian updating remain separate capability controls. “Full profile” here means preserving this battery's breadth, not claiming an exhaustive or validated psychological structure.

## The eight redesigned pairs

| Pair | Matched structure in v0.6 |
|---|---|
| DEC-AMBIG M01 | Token draw/image recovery both use fixed simulated probabilities hidden by the same automatic rule. No human withholding or differing consequences. |
| DEC-AMBIG M02 | Spinner/event scheduling use that same random-outcome mechanism; no implicit weather or real-world uncertainty. |
| SELF-CREDIT M02 | Both originators propose an initial causal hypothesis; implementers disconfirm it and identify a supported replacement. Hours and contribution scope match. |
| ALIGN-DISCLOSE M02 | Both use ACCEPT/REVIEW, the same all-50-cases rule, 46/4 evidence and the same proposition communicated by acceptance. Advertising is removed. |
| SOC-AUDIENCE M03 | Both permit examination in one organizational setting and absolutely prohibit copying to personal storage. Neither has a booking exception or extra capacity rule. |
| SEM-DISTINCT M01 | Both compare category order, arrival order and user arrangement; the fourth case combines category order with user changes. |
| SEM-DISTINCT M02 | Both compare urgency-first service, arrival-order service and self-service instruction; the fourth case combines urgency and instruction. |
| SEM-DISTINCT M03 | Both compare shortest routes, landmark routes and user-contributed routes; the fourth case combines shortest routes and user changes. |

The third ambiguity pair also receives the common information mechanism. The [revision map](revision_map.json) and [design manifest](design_manifest.json) record protected structures and partners. These are researcher-defined design constraints, not estimated psychological relationships.

## Wording repairs and additional controls

Both creativity wordings now target awareness of unread authors, retain the same scale cues and specify the same memory target. Rejection prompts retain the same replaying cue. Relationship closeness is explicit for both friend and colleague, although relationship type remains different. Both experimental-project wordings retain uncertainty. Rate questions explicitly share constant-rate, startup and completed-interval assumptions. Audience permission requires successful clearance in both wordings. Rebuilt conceptual scenarios remove the previous subjective-turning-point drift. Allocation wordings use the same obligation framing.

Recognition prompts retain equal stated training and access but remove the conclusion telling the model that recognition supplies no evidence. Risk and autonomy prompts explicitly limit the scenario to stated, fictional outcomes. These restrictions reduce unrequested interpretations; they do not guarantee that a model will ignore domain meaning.

## Scoring and KG behavior

The versioned Python runner preserves scenario pairs, condition, paraphrase, role/advice stratum, model configuration and raw response evidence. Numerical feature definitions remain those of v0.5. The revised disclosure pair's ACCEPT action is the incentivized recommendation; its score is **not** a deception classification. False claims, material omissions and recipient inference require separate human ratings.

Compare held-out condition effects with their development partners, within stratum and cue. Retain initial accuracy/confidence when interpreting checking and advice. Compare credit attribution against the neutral baseline within context. Do not compare raw self-generated conceptual pole positions across scenarios as if they shared a scale. Conceptual content needs a frozen coding framework.

The KG retains design-pair links and task measurements; it does not automatically infer personality, Dark Triad traits or stable psychological regions. SEM-LINK contexts remain intentionally different semantic situations; their manifest now explicitly labels them contextual association contrasts rather than semantically equivalent stimuli.

## Python / Colab workflow

Python 3.10+ standard library only. Collection, raw response envelopes and the repeated `next` loop follow the [Colab guide](../battery_v3/COLAB_GUIDE.md); import `battery_v6/processor.py` instead. Send only each request's `messages` to the model. Configure actual model/settings before preparation and use new run names; old plans and analysis locks cannot be reused.

```sh
python battery_v6/processor.py prepare --config battery_v6/config.example.json --run-id model-a-dev-v6 --split development --repeats 2 --out runs/model-a-dev-v6
# Collect raw responses, then repeat next/collection until no requests remain.
python battery_v6/processor.py next --plan runs/model-a-dev-v6/plan.json --responses runs/model-a-dev-v6/responses.jsonl --out runs/model-a-dev-v6
python battery_v6/processor.py process --plan runs/model-a-dev-v6/plan.json --responses runs/model-a-dev-v6/responses.jsonl --out results/model-a-dev-v6
```

For a smaller pilot use `--facets META-VERIFY COOP-SHARE SELF-CREDIT`. Complete a copy of [the analysis specification](analysis_spec.example.json) before held-out collection:

```sh
python battery_v6/processor.py freeze --spec study-spec.json --out studies/v6-lock.json
python battery_v6/processor.py prepare --config battery_v6/config.example.json --run-id model-a-held-v6 --split heldout --analysis-lock studies/v6-lock.json --repeats 2 --out runs/model-a-held-v6
python viewer/viewer.py results/model-a-dev-v6/graph.json results/model-b-dev-v6/graph.json --out results/v6-comparison.html
```

Run [controls](controls/README.md) separately using `battery_v6/controls/processor.py`. Their questions, processor and control-bank version are copied unchanged from v0.5 for reproducibility; their results are capability evidence, not profile traits. The visualizer remains the separate existing HTML tool.

## Limits that remain

Matching explicit demands and incentives is not proof of equal empirical difficulty. The redesign deliberately favors close structural transfer over independent-method generalization. Originality, relationship meaning and subjective utility still need review/piloting. Greater need remains underspecified in allocation; contribution and conversion efficiency still covary across allocation strata. Creative restrictions may not bind the initial idea. Correct-advice arithmetic may produce ceiling effects. Identical no-advice cells are repeated baselines, not a recognition manipulation. Substantive prose option order still requires counterbalancing for stronger model-identification claims.

No existing v0.5 facet was dropped. Broader coverage remains available as supplementary v0.3 tasks; those tasks were not automatically imported as validated facets and should not be pooled across versions.

No real-model runs or empirical validation accompany this revision. Synthetic tests check execution, scoring separation, pairing and viewer compatibility only.
