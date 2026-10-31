# Software verification and empirical status

2026-10-31. No tested LLM was run for this revision. All responses used in software checks were explicitly synthetic.

Verified:

- 39 families cover all 12 regions; 194 sessions contain 278 required stages per repetition.
- 18 control families / 36 prompts load and process separately, with a distinct version and one control-only region.
- Initial requests omit later stimuli and verification solutions.
- Verification requests reveal the solution and charge the correct cost; initial/final accuracy and Brier score remain separate.
- Duplicate requests, stale records and modified plans are rejected or marked invalid as specified.
- Per-field word limits, numeric bounds, finite values and concept uniqueness are enforced.
- Refusal, API error and pending states remain separate; partial invalid sessions do not enter summary estimates.
- Allocation multipliers produce the expected ledger values.
- A completion followed by a cancellation status code produces a status mismatch.
- Rule-learning feedback is delivered after action without announcing the rule change.
- Generated schedule repair is checked against dependency, collision and unavailable-slot constraints.
- Diagnostic evidence purchases produce the specified posterior reference and costs.
- Reference-frame lottery forms preserve their final outcome distributions.
- Binary display order rotates across repeats.
- Every profile session completes under a synthetic format fixture; graph IDs and endpoints are consistent.
- The existing viewer accepts the v0.3 catalog and graph, returns zero differences on self-comparison, and retains separate association contexts.
- All 20 existing viewer regression checks pass.

Commands:

```sh
python tests/test_battery_v3.py
node tests/test_v3_viewer.js
node tests/test_viewer.js
```

The first command runs 19 unit/integration tests and writes an ignored synthetic graph fixture for the second command. No browser interaction, live Colab execution, human rating, reliability estimation, factor analysis, or empirical construct-validation experiment was performed in this revision. The deterministic fixtures exercise software contracts; they are not psychological results or example model profiles.
