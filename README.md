# llmfp: behavioral fingerprints for language models

`llmfp` measures how a language model distributes its responses over a battery
of closed questions, and tests whether those distributions identify the model.
It replaces the trait scoring of the earlier versions of this repository with a
criterion that can be checked: different models respond differently, and the same model
responds the same way when its deployment context changes. The result is also
exported as a typed, weighted knowledge graph per model.

## Status

The statistics are verified on synthetic models with known parameters
(`tests/test_llmfp.py`). The Hugging Face readout is verified mechanically on
small randomly initialized networks (`tests/test_hf_backend.py`): templating,
label tokens, batching and resumable collection. No real model has been run.
Every statement about how real models respond to this battery is a hypothesis
until a panel of real models is collected.

## Install

Python 3.10 or later. The analysis needs only `numpy`. Local model collection
needs `torch` and `transformers`.

```sh
pip install -e .            # analysis only
pip install -e ".[hf]"      # with local model collection
python tests/test_llmfp.py
```

## Use

Collect one observation file per model, then analyze them together.

```sh
python -m llmfp run-hf Qwen/Qwen2.5-7B-Instruct --out obs/qwen2.5-7b.jsonl --name qwen2.5-7b
python -m llmfp run-hf meta-llama/Llama-3.1-8B-Instruct --out obs/llama3.1-8b.jsonl --name llama3.1-8b
python -m llmfp analyze obs/*.jsonl --out report --groups groups.json
```

Open `report/report.html`. Collection is resumable: rerun the same command
after an interruption. One model needs 5,808 single-token forward passes with
the default eight contexts, which is a few minutes on one GPU. Adding
`--context-set all` also collects six adversarial system prompts (10,164 passes).

Every run starts with a short format check that prints the label mass and the
model's leading first tokens. `--check` runs only that check and stops, so a
format problem is found before a full run is spent:

```sh
python -m llmfp run-hf Qwen/Qwen2.5-7B-Instruct --out obs/x.jsonl --check
```

On Windows, `obs/*.jsonl` and a bare folder name such as `obs` both work in
`analyze` and `identify`. The tool expands them itself.

For a served model, any OpenAI-compatible endpoint that returns token
log-probabilities works (vLLM, llama.cpp server, hosted APIs):

```sh
python -m llmfp run-api my-model --base-url http://localhost:8000/v1 --out obs/my-model.jsonl
```

For an endpoint that returns text only, add `--samples 20`. Each probe is then
sampled that many times and the distribution is estimated from the replies, so
the cost rises by the number of samples. Any other text generator can be
wrapped in `llmfp.backends.SamplingBackend` and passed to
`llmfp.collect.collect`.

`python -m llmfp simulate --out sim` followed by `analyze` runs the whole
pipeline on synthetic models and shows the report format.

On Colab, [`notebooks/Run_Colab.ipynb`](https://colab.research.google.com/github/dwtrott/llm_psychometric_test/blob/main/notebooks/Run_Colab.ipynb)
collects several models on one GPU and analyzes them together. The notebook
has not been executed yet.

Two further commands work on collected files:

```sh
python -m llmfp identify obs/unknown.jsonl obs/qwen2.5-7b.jsonl obs/llama3.1-8b.jsonl
python -m llmfp diff report/graphs/qwen2.5-7b.json report/graphs/llama3.1-8b.json --out diff.csv
```

`identify` ranks the enrolled models as candidates for an unlabeled model and
states whether the unlabeled model falls inside each candidate's own range
across contexts. `diff` labels every edge of two model graphs as SHARED,
CHANGED, A_ONLY or B_ONLY.

Options that matter in practice:

- `--no-thinking` for models that open their reply with a reasoning block. The
  readout uses the first generated token, so reasoning must be off. Other chat
  template settings can be passed as JSON with `--template-kwargs`.
- `--prefill "("` or similar when the format check shows low label mass because
  a model habitually answers in a form such as `(A)`. For a tokenizer that
  emits a separate leading space token, `--prefill " "` has the same effect.
- `--groups groups.json` declares known relatives, for example
  `{"qwen2.5-7b-awq": "qwen2.5-7b"}`. Relatives are then scored at lineage
  level and are not counted as different models when the verification
  threshold is set. See `groups.example.json`.
- `--context-set all` adds system prompts written to move the model: claims
  to be another vendor's model, a blunt persona, an extremely cautious
  persona, an instruction to prefer the first option, and an instruction to
  choose at random. These never contribute to a reference. The report states
  whether each model is still identified under them.
- `--contexts contexts.json` replaces the default system prompts. The format
  is a list of `{"id": ..., "system": ...}`.

## The battery

`BATTERY.md` lists every item. `llmfp/battery.py` is the source. There are 352
items in ten families. No item has a correct answer.

| Family | Items | What is asked | Scoring model |
|---|---|---|---|
| similarity | 66 | Similarity of every pair of 12 value concepts on a five-point scale | Expected rating per pair, giving a weighted concept graph |
| priority | 66 | Which of two concepts takes priority when they conflict | Bradley-Terry strengths and the share of circular triads |
| association | 24 | First word that comes to mind for a cue | Cue-to-word probability graph |
| sweep | 112 | Eight binary decisions, each asked at seven levels of one quantity, in two independent wordings | Threshold and slope of the response curve, and agreement between the two wordings |
| likert | 30 | Self-descriptions on five dimensions, three statements keyed each way | Content score, acquiescence, extremity, midpoint use |
| estimative | 12 | Probability meant by phrases such as "very likely" | Expected probability per phrase |
| boundary | 16 | Whether to carry out a borderline but harmless request | Willingness per request and overall |
| identity | 2 | Declared developer and training year | Reported separately from behavior |
| arbitrary | 12 | Pick one of four unrelated things at random | Distribution only (control) |
| style | 12 | Choice between two writing or coding conventions | Distribution only (control) |

The eight sweeps are risk for gains, risk for losses, delay of payment,
acceptance of unequal splits, declining to answer under a penalty, trading one
large cost against many small benefits, exploring an unknown option, and
deferring to a colleague of stated accuracy.

The identity family records what a model says it is. It is kept out of the
psychometric group because a system prompt can change it, and comparing it
with the behavioral families shows whether a model that claims one origin
behaves like another.

The two control families contain no psychological content. The report compares
them with psychometric items in equal numbers. If the control items identify
models as well as the psychometric items, the psychometric content is not what
carries the fingerprint, and the report says so.

## Outputs

`report.html` and `summary.json` give identification accuracy with a
bootstrap interval over items, the false accept rate for models that are not
enrolled, results under adversarial contexts, the verification operating point, a breakdown by family and channel, the
psychometric against control comparison, an item selection curve, split-half
agreement, scale reliability and the model distance matrix.

The report also gives a readable profile per model in the units of the
questions, the agreement between the two wordings of each sweep, Cronbach's
alpha for the self-report dimensions, the identifying information per probe
for each family, and the distance of each declared relative from its base.
`scale_values.csv` holds every scale value for every model.

`item_information.csv` ranks every cell by the bits it carries about model
identity. `scale_reliability.csv` gives the intraclass correlation of every
scale value. `graphs/<model>.json` and `graphs/<model>.edges.csv` hold each
model's knowledge graph, and `graphs/lineage.json` holds the graph among
models.

## Reading a first real run

Read label mass first. It is the share of first-token probability that falls
on a valid answer letter. If it is low for a model, that model is not answering
in the requested format and its content distributions are renormalized noise.

Then read the family table. A family with high between-model bits and low
within-model bits is carrying the fingerprint. A family where both are near
zero is one on which models agree, and the selection step removes it.

Identification accuracy on a small panel of unrelated models is expected to be
high and is not the hard test. The hard tests are whether fine-tunes and
quantized copies stay close to their base, whether a system prompt can move a
model outside its own range, and whether the psychometric families beat the
controls.

## Layout

```
llmfp/battery.py      items, families and their metadata
llmfp/probes.py       presentation orders, contexts, message rendering
llmfp/backends.py     Hugging Face, OpenAI-compatible and sampling backends
llmfp/collect.py      resumable collection
llmfp/fingerprint.py  observations to distributions, by channel
llmfp/analysis.py     information, identification, verification, lineage
llmfp/scales.py       scoring models and scale reliability
llmfp/graph.py        knowledge graph export and comparison
llmfp/report.py       full analysis and HTML report
llmfp/simulate.py     synthetic models for tests
```

`METHOD.md` states the measurement model and its limits.

## Earlier versions

The v0.1 to v0.11 batteries, the analyzer, the viewer and the network atlas are
no longer in this repository. This package supersedes the batteries and their
scoring. The interactive viewer and the network atlas have no replacement here:
`analyze` writes each graph as plain JSON and as a CSV edge list for use in
other tools. Everything removed remains in the git history. The last commit
that contains only the earlier versions is `4c80dc3`:

```sh
git checkout 4c80dc3 -- viewer network_atlas    # restore chosen folders
```
