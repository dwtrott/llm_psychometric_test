# v0.7: distinct wordings and balanced presentations

**Inspect the substance first:** [actual question excerpts from every family](ACTUAL_QUESTIONS.md), with both conditions and all stages, and the [content/scoring audit](CONTENT_AUDIT.md). These are custom exploratory text tasks. Important content scoring remains incomplete, several held-out contexts are close substitutions, and this bank does not establish a full psychological fingerprint.

For the new design-aware results report, use the [Python analyzer and Colab notebook](../analyzer/README.md). It analyzes the existing v0.7 exports without changing these questions or their scoring rules.

All 14 candidate profile facets remain, with 84 scenario forms across 11 regions and capability controls separate. v0.6 is unchanged. The revision addresses its [duplicate-wording and presentation review](../battery_v6/reviews/REVIEW.md), not empirical psychological validation.

Read the full [question CSV](questions.csv), [question book](question_book/), or open [the side-by-side comparison](side-by-side.html) locally. Every presentation is already rendered as an actual question; no hidden prompt-generation step is required to read the battery.

## What changed

- All six allocation scenarios and two author-discovery scenarios now have distinct P1/P2 openings with the same protected facts. These are limited wording variations: keeping the main factual block verbatim does not establish robustness to every possible paraphrase.
- Binary choice descriptions appear in both orders in risk, ambiguity, recognition, disclosure and harmful-resource decisions. Allocation reverses keep/give payoff descriptions. Autonomy's three action descriptions appear in all six orders. The response schema follows the displayed decision order rather than rotating independently.
- Conceptual trials cross all six mappings of semantic alternatives to displayed L/M/N positions with three fourth-case combinations: canonical LM, LN and MN. N is therefore no longer always the displayed user-directed alternative, and the fourth case is no longer always L+N.
- Each presentation is crossed with both wordings and conditions, each applicable role/advice stratum, and the matched development/held-out partner. Presentation balance holds even for one repeat and when selecting whole facets.
- Repeats now replicate each explicit cell. They do not rotate schemas. The CSV and `presentation_manifest.json` fully specify what is shown.
- Scoring records the presentation and decodes conceptual pair answers to their canonical semantic identity. Raw display letters remain in the response evidence.

The conceptual mapping jointly balances semantic identity against display label and position. Labels are displayed in L/M/N order; label and physical position are not independently crossed. Binary labels retain their meanings, so reversing order controls position but does not independently estimate arbitrary-label effects. Autonomy balances the action menu, not the chronological narrative of the recipient's initial choice. Allocation balances payoff descriptions, not every mention of self and other. These boundaries are deliberate and explicit.

## Demands, incentives and transfer patterns

Keys, resource costs, ledger effects, allowed answers, numeric ranges, text limits and rating rubrics are preserved from v0.6. An option moving position does not change its meaning, score or payoff. For example, TRANSFER has the same effect when displayed before KEEP; the correct arithmetic answer does not change when option B is described first.

For conceptual trials, the fourth case now has three alternatives. Each preserves the same request—apply the previously generated distinction on a 0–100 scale and explain a boundary problem—and the same word limit. Development and held-out partners receive the exact same fourth-case text within each transfer pattern. **Different combinations may have different empirical difficulty.** They are kept as separate analysis strata, not assumed interchangeable or averaged as repetitions.

For example, the ordering family uses category-plus-arrival, category-plus-user changes, or arrival-plus-user changes. The service family uses urgency-plus-arrival, urgency-plus-teaching, or arrival-plus-teaching. The route family uses shortest-plus-landmarks, shortest-plus-user changes, or landmarks-plus-user changes. These sample additional relationships within the task family; they do not constitute independent psychological methods.

## Run size and Python workflow

The full factorial design has **1,224 sessions and 1,848 stages per repetition across both partitions**: 612 sessions / 924 stages per partition. These remain 84 scenario forms, not 1,224 independent psychological questions. More repeats increase sample count further; the default two repeats is not a power recommendation.

The standard-library Python workflow is unchanged. Use a new configuration/run directory and new analysis lock for v0.7. The [Colab guide](../battery_v3/COLAB_GUIDE.md) explains recording raw response envelopes and the collect/next loop; substitute `battery_v7/processor.py` when importing. Send only each request's `messages` to the tested model.

```sh
python battery_v7/processor.py prepare --config battery_v7/config.example.json --run-id model-a-dev-v7 --split development --repeats 2 --out runs/model-a-dev-v7
# Collect responses, then repeat next/collection until no requests remain.
python battery_v7/processor.py next --plan runs/model-a-dev-v7/plan.json --responses runs/model-a-dev-v7/responses.jsonl --out runs/model-a-dev-v7
python battery_v7/processor.py process --plan runs/model-a-dev-v7/plan.json --responses runs/model-a-dev-v7/responses.jsonl --out results/model-a-dev-v7
```

For a smaller balanced pilot, add `--facets META-VERIFY COOP-SHARE SELF-CREDIT` to preparation. This keeps every presentation/condition/wording in those facets; do not choose only convenient individual rows. Use identical scope across models.

Complete a copy of [analysis_spec.example.json](analysis_spec.example.json), including whether and how to weight order cells, before held-out collection:

```sh
python battery_v7/processor.py freeze --spec study-spec.json --out studies/v7-lock.json
python battery_v7/processor.py prepare --config battery_v7/config.example.json --run-id model-a-held-v7 --split heldout --analysis-lock studies/v7-lock.json --repeats 2 --out runs/model-a-held-v7
python viewer/viewer.py results/model-a-dev-v7/graph.json results/model-b-dev-v7/graph.json --out results/v7-comparison.html
```

Controls remain the unchanged, separately versioned bank copied from v0.5. Use `battery_v7/controls/processor.py` for them. Never combine control accuracy with profile facets as a global personality score.

## How results preserve presentation

The existing `stratum` column now encodes the base role/advice stratum and presentation, for example `incorrect_advice|order02-transfernone`. The [presentation manifest](presentation_manifest.json) provides structured base stratum, order, transfer pattern and conceptual label mapping for each item. These fields are also attached to trial results and graph evidence. Features CSV retains the full stratum identifier.

Condition effects and paraphrase comparisons are computed **within presentation cells**. The analyzer does not silently average over option orders or transfer patterns. Any marginal estimate should use a prespecified common complete set and equal design-cell weighting, with missingness reported. Presentation effects can be examined by joining corresponding scenario/condition/wording cells; automatic order-effect estimation is not added in this release.

Conceptual `canonical_pair_LM`, `canonical_pair_LN` and `canonical_pair_MN` features identify which original alternatives were grouped, irrespective of displayed labels. They do not place self-generated poles on a common psychological scale. The six label mappings and three transfer patterns are not additional independent scenarios. Human-coded conceptual content remains pending.

The original interpretation limits remain: adherence to explicit rules is not automatically empathy or honesty; assigned-role attribution is not automatically narcissism; hypothetical harm is not automatically real-world misalignment. No model experiments or empirical validation were performed for this release. Tests verify duplicate detection, balance, faithful scoring, preserved demands/incentives and graph compatibility.
