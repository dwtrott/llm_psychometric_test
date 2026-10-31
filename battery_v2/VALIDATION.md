# Verification record

Content/implementation review: 2026-10-31.

- 48 scenario families, 96 instantiated prompts, 12 regions, 16 research references.
- Each family has two complete versions with a named contrast and explicit confounds.
- Objective tasks have per-condition keys; preference tasks have no accuracy score.
- Open tasks have criterion-specific 0–2 reviewer anchors; scores remain missing until review.
- Six repetitions per item counterbalance every three-option menu and yield 576 trials.
- Seventeen offline v0.2 tests pass, covering coverage, source IDs, prompt/key separation, option balance, calibration arithmetic, preference handling, missing/invalid/refusal/API-error separation, association denominators, graph integrity, duplicate IDs, battery changes and invalid confidence.
- The existing viewer's 20 tests pass. Additional v0.2 integration checks verify the 12-region/48-family catalog, graph loading, self-comparison, associations and rejection of a malformed catalog.
- Explicit checks verify equal lottery expectations in DEC-04 and the exploration value and key reversal in OPEN-01.

These tests verify implementation properties, not psychological validity. Synthetic format fixtures deliberately use generic text for open responses; acceptance means format validity, not a high-quality answer. No real LLM responses, independent item-review ratings, calibration estimates, reliability coefficients, effect sizes or human norms have been collected. The v0.2 catalog change was checked programmatically; the earlier browser interaction checks applied to v0.1 demonstration data. Live Colab execution remains unverified.
