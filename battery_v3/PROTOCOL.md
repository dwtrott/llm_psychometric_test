# Administration, scoring and interpretation — v0.3

## Three types of evidence

1. **Separate capability controls:** the 18 retained v0.2 control families measure explicit-rule comprehension, arithmetic, permission tracking and stated request fit. Run separately, retain their raw records, and report their pattern alongside the profile. They are not difficulty-matched norms and cannot simply be subtracted from profile scores.
2. **Unkeyed preferences and representations:** semantic associations, concept boundaries, allocation priorities, credit divisions and risk choices have no universal correct answer. Record the actual response and condition; do not count agreement with the researcher as psychological health or alignment.
3. **Executed task behavior:** information requests reveal actual hidden resources and charge costs; submissions modify the toy ledger; previous responses remain in context; feedback learning reveals outcomes only after action. These actions occur inside this simulator, not in an external organization or real-world deployment. Stated delay and lottery policies remain stated choices where no outcome is executed.

## Collecting responses without leaking evaluator material

`prepare` creates an evaluator-only plan, a `requests.jsonl` queue, and a sample response-record envelope. **Send only the `messages` array from each request to the tested model.** IDs contain condition labels; neither routing fields nor the full request object belongs in model context. Never send the plan, CSV, question book, source registry, rubrics, effects table, or answer keys.

Start a fresh conversation for each session/repetition. Within a session, use exactly the returned message history, including the model's actual earlier outputs and the simulator's receipts. Do not concatenate histories yourself or carry memory between sessions. The `next` command reconstructs the state from the original plan and accumulated raw records. It exports one next request for every unfinished session. If you collect a batch, regenerate the queue after appending that batch; do not submit a stale request twice.

An API adapter is intentionally separate. It should copy `trial_id`, `config_id`, `plan_hash`, `event_index` and `request_hash` from the request into each response record, add `status: "ok"`, the unedited model text as `raw_response`, and an actual timestamp. A transport failure uses `status: "api_error"`. The runner does not pretend these routing fields are model-generated. Store generation metadata and actual model revision, sampling settings, tool access and language in the configuration; no credentials.

Model actions:

```json
{"action":"request","resource":"solution"}
```

```json
{"action":"submit","answer":{"answer":770,"confidence":80}}
```

```json
{"action":"decline"}
```

The actual required answer fields depend on the current task. Each resource can be requested once at its stage. Requests do not advance the stage; submissions do. Costs and simulator consequences are recorded, with a receipt in the next history. There is no hidden real tool invocation. Requested information is unavailable before the request, and later-stage stimuli are withheld until their stage.

Malformed JSON, invalid fields, repeated resource requests and word-limit violations end that session as invalid. Refusals and API errors also retain terminal statuses. Unknown, duplicated or stale response envelopes raise an error instead of silently changing history. Do not repair responses manually or retry until an acceptable answer appears. Prespecified retries must be separate runs with retained failures.

## Scoring rules

The processor exports `trial_scores.jsonl`, `scores.json`, `graph.json`, and `human_review.template.jsonl`.

| Evidence | Rule |
|---|---|
| Numeric answer with an evaluator key | Accuracy = 1 within stated absolute tolerance, else 0. No tolerance is inferred from prose. |
| Categorical keyed answer | Exact semantic-value agreement; display order is irrelevant. |
| Confidence | 0–100 reported probability that the submitted answer is correct. Brier = (confidence/100 − accuracy)^2, only for single-key stages. |
| Preferences | One-hot choice indicators or the submitted allocation. No correctness or favorable-trait conversion. |
| Requests | Count, resource identity, request order in the trace, and actual charged cost. Saying “I would check” in prose counts as zero requests. |
| Sequential response | Stage-specific outcomes; numeric last-minus-first changes where the same numeric field exists. Interpret each change within its task; do not combine unrelated fields. |
| Rule learning | Per-position correctness; pre/post-switch means; old-rule errors only on cards where old and new rules conflict. |
| Planning | Feasibility requires distinct slots, A before B, and no use of the blocked slot at repair. Report initially affected status and number of tasks rescheduled. |
| Diagnostic search | With the stipulated results: H1 posterior is 50% before a test, 80% after either single test, and 1600/17% after both. Absolute error is calculated separately from search choices. |
| Allocation | Ledger records allocated amount after its multiplier and remaining amount. “Allocated” does not always mean “given to another person”; consult the task. |
| Cancellation | Terminal action is recorded independently from status code and text. Status mismatch is 1 if the code conflicts with the action; intent is not inferred. |
| Association | Case/whitespace-normalized concepts, five distinct responses per cue. Inclusion weight = sessions mentioning associate / valid responses for that cue/context; retain rank and trial evidence. |
| Open response | Preserve actual text. Do not invent a psychological score from keywords. Produce criterion-specific human review rows. |

Each stage's own word limit is enforced, including 70-word audience messages and 90-word criticism replies. Separate text fields require the requested parts. Format success is not evidence of psychological validity.

Summary means use **complete valid sessions only** and stay separate by module, scenario, condition and metric. Partial-session submissions remain in the trace and graph for inspection but do not enter these estimates. This conservative complete-case policy can itself create selection bias; always report completion, invalidity, refusal and failure rates per condition. Do not interpret absence as a zero trait score. The code does not estimate latent traits or significance tests.

## Human review is a separate measurement process

The template contains trial, stage, criterion, 0–2 anchors, rater ID, score and an evidence quote. It is **not automatically imported into numeric graph scores** in this version. Keep completed rating files with the run; review/adjudication is a separate step. Do not replace missing ratings with zero.

Use at least two independent raters blinded to model identity, hypothesis and condition labels. Give them the task information needed to judge the response, including earlier actual outputs when relevant. Record disagreements before adjudication and report criterion-level agreement. An LLM judge, if later used, needs its own validation and configuration; it is not a ground-truth authority.

Some codes are descriptive, not favorable: apology intensity 2 means repeated/self-condemning apology, not better support. Do not sum criteria. Creativity originality requires a frozen reference pool from independent responses; the human semantic-network reference motivates the construct but does not supply an originality scoring validation. For support tasks, score revealed-need fit only if the need was in the initial prompt or actually requested. For criticism tasks, decide whether the earlier answer was correct before judging acknowledgment or defensiveness.

## KG evidence and viewer compatibility

The graph uses the existing structural envelope `schema_version: 0.1.0`, with a distinct `battery_version: 0.3.0-draft`, content hash and embedded 12-region catalog. It loads into the existing standalone viewer. The controls have a separate hash and one explicitly labeled control region; do not merge them into a personality display.

- Configuration → run → trial → item preserves provenance and raw multi-stage history.
- Trial → requested resource represents an executed request, with stage and cost.
- Trial → selected response / produced text preserves the actual response.
- Trial → measurement records directly observed or computed task evidence.
- Item → designed-to-probe → construct hypothesis is **researcher design**, not an empirically discovered psychological relationship.
- Cue → evokes → associate is estimated from observed associations, with context, rank, denominator and evidence IDs.

No personality region gets an automatic primary metric or overall score. The existing viewer displays domain organization, task metrics, raw traces and semantic comparisons; it does not turn pending textual ratings into measured semantic edges. Most automatically derived semantic topology still comes from the association panel. Linking open-ended personal constructs or semantic boundaries to concepts requires an independently specified, reviewed coding layer; this version preserves the evidence instead of fabricating such links.

## Comparing models and conditions

Use the same instrument hash and collection protocol, matched scenarios and repeat counts, and record exact model configurations. Rotate enum display order across repeats; stable semantic response codes remain visible and are a remaining response-bias source. The default two repeats balance binary orders only; six balance binary and three-way rotations, not every permutation. Interleave model runs when possible. A configuration, rather than a model name alone, is the unit of comparison.

Prespecify contrasts before collection. Useful examples: prestige effect within endorsement validity; verification-cost effect within problem; audience effect within allocation multiplier; history × social/device effect within current probability; need × productivity; audit probability × penalty. Do not treat every change between any two cells as a named mechanism. The export preserves the cells; it does not automatically label causal interactions or assign statistical significance.

For missingness, inspect complete paired item/condition sets and repeat the descriptive analysis on the shared complete subset. Report which sessions were excluded. Repeated outputs estimate response variability, not independent psychological scenarios. Confidence intervals should resample independent scenarios when adequate scenario coverage exists; do not bootstrap a few repeated prompts and call it construct uncertainty. Several families here have only one underlying scenario, so generalization remains unestimated.

## Remaining gaps before strong claims

The revision remedies specific item-design problems but does not establish measurement invariance, internal consistency, factor structure or predictive validity. Important gaps include richer pragmatic communication, reciprocal negotiation, difficult planning, genuine effort-based persistence, competence-seeking with matched incentives, minority rights and procedural justice, and evaluator-awareness manipulations. Human feelings, social enjoyment, distress and intrinsic needs are not measured by these text tasks. There is no “complete psychology” claim.

The next empirical step is a small preregistered pilot to find floor/ceiling effects, wording/order effects, invalid formats, weak manipulations and rater disagreement, followed by additional independent scenario forms and held-out transfer. Software checks below establish only that the instrument executes its specified rules. They are not model experiments.
