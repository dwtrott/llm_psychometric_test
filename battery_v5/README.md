# v0.5: matched-context profile battery

This revision addresses the [v0.4 critical review](../battery_v4/reviews/CRITICAL_REVIEW_2026-11-01.md). v0.4 remains unchanged. **This is an exploratory instrument, not a validated psychological fingerprint.**

Read the actual questions in [questions.csv](questions.csv) or the complete evaluator [question book](question_book/). No external questionnaire is required. Each entry includes its full stimulus, response schema, resource costs, mechanical keys and applicable human-review rubric.

## What changed

- Repaired paraphrases that changed durations, precedence, commitment, resource permissions, or emotional cues. Essential facts and response requirements are shared across both wordings.
- Moved Bayesian updating and constrained scheduling into a separately runnable [capability-control bank](controls/README.md). Their accuracy is not a psychological trait score.
- Assigned three development and three held-out contexts to each of 14 candidate facets. S01 pairs with S04, S02 with S05, and S03 with S06. Both wordings and every experimental condition stay within the assigned partition.
- Matched numerical risk probabilities, harm-game payoffs, verification arithmetic and checking costs, and disclosure counts/thresholds/rewards within each pair. Held-out verification questions no longer introduce a new mathematical operation.
- Added correct-advice, incorrect-advice and no-advice strata to recognition sensitivity. Recognition supplies no additional stated expertise or familiarity. The two no-advice recognition cells are identical baseline prompts, not an actual recognition manipulation.
- Added originator-self, implementer-self and neutral-observer strata to credit attribution. The same contribution facts remain fixed across roles. These are assigned roles, not evidence of an enduring model self.
- Distinguished equal claims, greater need and greater contribution in allocation tasks. Their matched held-out partners retain the same claim structure and multiplier.
- Added pair and stratum metadata to scoring and graph export. Role/advice strata are not averaged together. Graph links to design pairs denote researcher-defined matching, not observed psychological similarity.

The profile bank has **14 facets across 11 regions, 84 scenario forms, 504 sessions and 648 stages per repetition across both partitions**. Each partition has 252 sessions. Executive planning is currently represented only as a capability control; this release does not claim complete psychological coverage. Broader v0.3 tasks remain supplementary, not additional validated facets.

## What matching means

[design_manifest.json](design_manifest.json) records each partner, invariant contract and transfer scope. The contract lists family parameters and a zero-based pair index. It is an inspectable design specification, not an empirical equivalence certificate.

For example, both META-VERIFY-S01 and S04 require `23 * 18 - 127 + 46`, followed by the same 1-point or 8-point verification decision. The contexts differ (cups versus archive cards). Their arithmetic and incentive demands are fixed; language familiarity could still affect performance. Initial accuracy and confidence must remain visible when interpreting checking behavior.

For open-ended creativity, social meaning and conceptual association, shared response demands do not guarantee equal difficulty. Context meaning is intentionally varied; topical associations can identify a model without a psychological explanation. Creative constraints may already be satisfied by the first answer: independently code whether a constraint actually binds before interpreting adaptation.

Pairs test **transfer within a task family**. Changing a setting does not create an independent psychological method. Similar performance on both wordings is useful evidence of wording robustness, not proof of a trait. Equal empirical difficulty and stable model differences still require pilot evidence. Substantive prose option order is not counterbalanced in this release; schema order rotation does not remove that limitation.

## Run in Python or Colab

Standard-library Python 3.10+; no new libraries or services required for preparation/scoring. The existing [Colab collection guide](../battery_v3/COLAB_GUIDE.md) explains the staged response loop. Import `battery_v5/processor.py` instead of v0.3, use a new run directory, and send only each request's `messages` to the model. Keep keys, future stages, metadata and held-out questions evaluator-side. Model access is supplied separately.

```sh
python battery_v5/processor.py prepare --config battery_v5/config.example.json --run-id model-a-dev --split development --repeats 2 --out runs/model-a-dev-v5
python battery_v5/processor.py next --plan runs/model-a-dev-v5/plan.json --responses runs/model-a-dev-v5/responses.jsonl --out runs/model-a-dev-v5
python battery_v5/processor.py process --plan runs/model-a-dev-v5/plan.json --responses runs/model-a-dev-v5/responses.jsonl --out results/model-a-dev-v5
```

Edit the configuration before preparing. Collect the requested responses before `next`, repeating that step until finished. `process` exports descriptive scores, evidence graph, trial records, feature CSV and pending human-review records. It never calls a model. For a smaller pilot, add `--facets META-VERIFY COOP-SHARE SELF-CREDIT` to `prepare`. Use the same scope and settings for both models.

Complete a copy of [analysis_spec.example.json](analysis_spec.example.json) with concrete predictions and treatment of missingness, task accuracy, wording sensitivity and human ratings before collecting held-out responses:

```sh
python battery_v5/processor.py freeze --spec study-spec.json --out studies/v5-lock.json
python battery_v5/processor.py prepare --config battery_v5/config.example.json --run-id model-a-held-v5 --split heldout --analysis-lock studies/v5-lock.json --repeats 2 --out runs/model-a-held-v5
```

The lock records this study's analysis choices; public questions are not secret or guaranteed absent from training. Do not mix versions, partitions or control banks in one profile. Compare models within the same partition. Evaluate held-out transfer by joining scenario estimates or condition effects on `matched_pair`, metric, cue and stratum; do not treat partitions as two different models. The processor exports these inputs but does not automatically fit traits or evaluate frozen predictions.

## Scoring and graph interpretation

Continuous task features retain their original meaning: risky choice, information purchase, allocation fraction, attribution fraction, or recommendation under incentive. None is automatically labeled narcissism, deception or misalignment. For credit attribution, compare originator-credit fractions across assigned roles and the neutral baseline. For recognition, compare high versus low recognition within advice validity; `error_change` and `advice_agreement_change` are separate outcomes. No-advice trials have no advice-agreement score.

Human-coded content remains pending until rated under a frozen codebook. Absence of a rating is not a zero. Text quality, honesty, helpfulness and conceptual distinctions cannot be inferred from the selected option alone. Scenario estimates and condition effects require matched wordings/repetitions; report missingness with any common complete subset.

```sh
python viewer/viewer.py results/model-a-dev-v5/graph.json results/model-b-dev-v5/graph.json --out results/v5-comparison.html
```

The existing HTML viewer consumes the evidence graph. This release updates the Python battery and analyzer; the viewer is still the separate legacy tool. Pair membership is a design link, not a discovered psychological relationship. No real-model results or empirical validity claims accompany this revision.
