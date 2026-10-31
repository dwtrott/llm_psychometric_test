# Verification status — 2026-10-31

No LLM was tested for this release. No human item review, paraphrase-equivalence judgment, reliability estimate, factor analysis or empirical construct validation is complete. All software checks use synthetic responses.

The 19 Python tests cover:

- Inventory, crossing, and four-development/two-held-out forms per facet.
- Whole-scenario partitioning, unchanged locks, listed configurations and rejection of placeholders or altered plans.
- Initial model requests omit evaluator labels and verification solutions.
- Paired schemas/keys match; this is structural consistency, not semantic equivalence.
- Every scheduling condition is feasible; durations and dependencies are checked.
- Repeat variance, wording sensitivity and scenario count remain distinct.
- Missing wording is not a zero; condition contrasts require common repeat blocks across all four cells.
- Unrevealed support preferences are not rated.
- Association denominators use scenarios and matched exposures, with no stability assertion.
- Invalid outcomes remain recorded without feature estimates.
- Held-out statistics remain separate; all forms process and graph provenance is consistent.

Legacy-viewer integration checks confirm imports, self-comparison, partition-specific semantic edges and no direct numeric matching of disjoint development/held-out items.

```sh
python scripts/build_battery_v4.py
python tests/test_battery_v4.py
node tests/test_v4_viewer.js
```

Tests generate ignored synthetic graph fixtures. Node is used only to check the existing JavaScript viewer, not by the new Python battery/analyzer. No live Colab or browser session was used. The item-review template remains blank: software success is not expert approval.
