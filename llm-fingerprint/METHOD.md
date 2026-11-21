# Method

## Aim

The aim is a fingerprint: a measurement that identifies which model produces a
set of responses and that stays stable when the same model is deployed in a
different context. The earlier batteries in `llm_psychometric_test` pursue a
different aim. They ask what a response reveals about a psychological
construct, and the v0.11 revision concludes correctly that the question has no
supported answer and withholds every trait estimate. A fingerprint does not
depend on that question. It requires discrimination between models and
stability within a model, and both are measurable.

The method keeps the instruments of psychometrics and changes the population.
Reliability, item discrimination and scale structure are properties of a group
of subjects observed on repeated occasions. Here the subjects are models and
the occasions are deployment contexts. One model observed once supports none
of these statistics, which is the central reason the earlier scoring cannot be
made sound by revising items.

## Observation

Each item has a closed response set. The observation is the model's
probability distribution over that set, read from the logits of the first
generated token. A single greedy answer carries no information about how
strongly the model prefers it, and repeating a greedy run returns the same
answer, so it supplies no estimate of variability either. The distribution
supplies both and costs one forward pass. For an interface that returns text
only, the same distribution is estimated from repeated sampling.

The share of first-token probability that falls on a valid answer letter is
recorded for every probe. It shows whether the model is answering in the
requested format, and it is itself a stable property of a model.

## Presentation design

Response order is a known influence on model answers. The design removes it
from the content measurement and keeps it as a separate measurement.

An item whose options have no natural order is presented once for each cyclic
rotation of its options. Every option then occupies every position exactly
once. Averaging the presentations by option gives the content distribution.
Averaging them by displayed position gives the position distribution, which
is exactly uniform for a model that responds to content alone. Any departure
from uniform is position preference and nothing else.

An item whose options form a scale is presented ascending and descending. The
share of responses on the first half of the displayed scale against the last
half is exactly even for a model that responds to content alone.

## Contexts

Each model is observed under several system prompts. Logit readout has no
sampling noise, so variation across contexts is the within-model variation
that matters for the intended use, which is recognizing a model whose
deployment is not controlled by the examiner. A fingerprint that changes with
a routine system prompt is not usable, and the design measures this directly.

## Distance and information

The distance between two fingerprints is the root mean Jensen-Shannon
divergence over items, in bits.

For each item the analysis computes two quantities. The between-model
information is the mutual information between model identity and one sampled
response. The within-model information is the mutual information between
context and one sampled response, averaged over models. An item is useful to
the degree that the first is large and the second is small. An item on which
all models give the same answer has no between-model information, whatever
construct it is written to probe. Items about harm, deception and disclosure
are likely to fall in this class for aligned models, which is the reason the
new battery does not rely on them.

## Tests

Identification. The fingerprint of each model under one context is compared
with reference fingerprints built from all other contexts. The model is
identified when its own reference is nearest. References never include the
context being tested.

Verification. Distances between same-model pairs and different-model pairs
are compared. The report gives the area under the curve and the share of
same-model pairs accepted at a threshold that admits one percent of
different-model pairs. This is the operating point for checking whether an
endpoint serves the model it claims to serve.

Lineage. Declared relatives, such as fine-tunes and quantized copies, are
expected to be nearer to their base than to any unrelated model. Relatives are
scored at lineage level and are excluded from the different-model set when
the verification threshold is computed.

Unknown models. Closed-set identification assumes the true model is among the
references. Each query is therefore also tested as if its own lineage had
never been enrolled. The acceptance threshold is the 95th percentile of
genuine same-model distances, and the report gives the share of such queries
that would be wrongly accepted as an enrolled model.

Adversarial contexts. An optional set of system prompts is written to move
the responses: claims to be another vendor's model, strong personas, an
instruction to prefer the first option and an instruction to choose at
random. These contexts never contribute to a reference or a scale value. The
report gives identification under each one and the distance the model moves
from its own reference.

Uncertainty. Identification accuracy is given with a 95 percent interval from
resampling the items, which shows how far the result depends on the
particular items in the battery.

Item selection. Items are ranked by information on half of the contexts and
identification is tested on the other half, so that the selection is not
scored on the data that produced it.

Split-half agreement. Random halves of the items each produce a matrix of
distances among models. The correlation of the two matrices states whether
the battery measures one consistent similarity structure.

Control comparison. Two families contain no psychological content. Random
subsets of psychometric items of the same size are compared with them on the
identification margin. If the controls perform as well, the psychometric
content does not explain the fingerprint.

## Scoring models

Each family has a scoring model taken from classical psychometrics or
psychophysics. Every scale value is computed for every model and context, and
its intraclass correlation is reported with models as subjects and contexts
as occasions. A scale value with low intraclass correlation is not a property
of the model and is not interpreted.

Similarity ratings. The expected rating for each pair of concepts is an edge
weight in a concept graph.

Paired comparisons. The probability that one concept is given priority over
another is fitted with the Bradley-Terry model, which places the concepts on
one scale. The share of triads whose majority preferences form a cycle
measures how far the preferences depart from any single ordering.

Response curves. Each sweep asks one binary decision at seven levels of one
quantity. The Spearman-Karber estimate gives the level at which the response
changes without assuming a functional form, and a penalized logistic fit
gives the slope. This is the method of constant stimuli. It replaces the
single yes or no risk item of the earlier battery, which cannot distinguish a
model that is indifferent from one that is far from its threshold.

Alternate forms. Every sweep is asked in two independently worded forms with
the same levels. The correlation across models between the two thresholds is
the alternate-form reliability. A threshold that does not survive rewording is
a property of the wording and is not interpreted as a property of the model.

Self-report. Each dimension has three statements keyed in each direction.
Cronbach's alpha is reported for each dimension with models as subjects.
The difference between the two sets is the content score. The mean over all
statements is acquiescence, because the content cancels under balanced
keying. The self-report dimensions of caution and deference have behavioral
counterparts in the abstain and defer sweeps, so the agreement between what a
model says and what it chooses is observable.

Borderline requests. Sixteen harmless requests on which assistants plausibly
differ are each answered with help, partial help or refusal. The willingness
score per request and overall replaces the harm and deception cards of the
earlier battery, on which aligned models are expected to agree.

Declared identity. The developer and training year that a model states are
recorded as a separate family. They are not treated as behavior, because a
system prompt can change them.

Estimative phrases. The expected probability assigned to each phrase gives a
calibration curve for uncertainty language.

## Knowledge graph

Each model's graph has a fixed set of uniquely labeled nodes and typed edges
with weights between zero and one. Concepts are linked by similarity and by
priority. Cues are linked to associated words. The model node is linked to
its decision thresholds, self-report scores, phrase probabilities and
response style values. Because the node set is shared, two graphs are aligned
by label and a difference between them is a difference in measured weights.
The graph is a presentation of the scale values and adds no information
beyond them. The report gives identification accuracy from scale values alone
so that the loss from this abstraction is visible.

A partial-correlation network among scale values within one model is
available when at least thirty contexts are collected. Contexts take the role
that persons take in a human psychometric network. Below that number the
estimate is not meaningful and the function refuses to run.

## Limits

The battery is new and no real model has answered it. Which families
discriminate, and whether any does so better than the controls, is unknown.

A short format check runs before every collection and reports label mass and
the leading first tokens, because a format failure invalidates a whole run.

First-token readout measures the first token. A model that reasons before it
answers, or that answers in a format without a leading letter, is measured
poorly, and label mass is the indicator.

The adversarial contexts are simple instructions. A system prompt that copies
another model's measured fingerprint item by item is a stronger attack and is
not included.

The scale names describe the questions asked. They are not claims that a
model has a trait in the human sense. The method needs the scales to be
reliable and discriminating, and it does not need them to be valid as
psychology.
