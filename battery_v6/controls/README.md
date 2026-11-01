# Separate capability controls

This bank contains EPI-REVISION (Bayesian updating) and EXEC-ADAPT (bounded scheduling and repair), formerly in the v0.4 profile. Twelve scenario forms yield 48 sessions and 96 stages per repetition. All forms are labeled development: there is no psychological held-out claim for this bank.

Read [questions.csv](questions.csv) or [the question book](question_book/CONTROL.md). Run the local processor with the same collection loop described in the [v0.5 guide](../README.md):

```sh
python battery_v5/controls/processor.py prepare --config battery_v5/controls/config.example.json --run-id model-a-controls-v5 --repeats 2 --out runs/model-a-controls-v5
```

Use this bank's processor for `next` and `process` too. Keep control results separate from profile graphs and interpret them as task performance. Accuracy can reveal a competing capability explanation; it is not itself psychological stability or a personality trait. The older supplementary control bank is retained unchanged in [legacy](legacy/) with its own interface.
