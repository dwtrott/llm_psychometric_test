# From a battery map to a candidate behavioral fingerprint

The original region map represented the instrument, not what a model's responses revealed. The analyzer now adds observed findings and an evidence KG. This is useful structure for studying a fingerprint; it is not validation of an underlying model psychology.

## What the interface now means

Region nodes contain response-derived behavior summaries. For example, the synthetic A run chooses the risky option in every observed gain-framed cell and never in the loss-framed cells. Synthetic B's risk choices instead vary with option order. This is a distinction between conditional patterns, not a difference in an overall risk personality score.

The full-profile comparison shows A and B's behavior by condition, the range of matched B-minus-A differences, and separate wording/order sensitivity counts. Purple means the direction changes across the supplied contexts. Identical values mean identical observed values for that measure, not equivalent psychological profiles.

Percentages are repeat means within a fixed scenario and presentation. Displayed ranges are minima/maxima across those cells, not confidence intervals. Nothing is pooled across conditions or transformed into a human norm. Condition-effect summaries preserve every matched estimate, including opposite signs and zero effects. Presentation variants and repeated samples are never counted as distinct scenarios. Wording/order counts beside comparisons use each model's available data and are labeled accordingly; the A/B values and deltas use common valid cells only.

## Typed KG structure

### Psychological relationship layer

The visible graph has 11 bounded psychological regions and 14 behavioral-pattern nodes. Its layout is fixed across models and the difference graph. Node content is response-derived; region membership is theory-defined. The following eight edges are research proposals, displayed as dashed lines with H1–H8 labels:

| ID | Candidate connection |
| --- | --- |
| H1 | Information seeking ↔ prestige sensitivity |
| H2 | Social allocation ↔ credit attribution under audience changes |
| H3 | Credit attribution ↔ disclosure under incentives |
| H4 | Choice/consent ↔ own gain versus others' loss |
| H5 | Audience adaptation ↔ support adaptation |
| H6 | Conceptual distinctions ↔ creative adaptation |
| H7 | Risk framing ↔ unspecified probabilities |
| H8 | Concept associations ↔ conceptual distinctions |

These are **not established psychological connections**. Each hypothesis node includes a question, the required joint design, proposal provenance, `status: untested` and `strength: null`. A `hypothesized_relationship` edge connects the two candidate facets, with `directed: false`. The shared proposal layer is deliberately identical across models. No relationship strength, sign, causal direction or model difference is inferred from unrelated scenario numbers, wording variants, or the synthetic fixture.

This layer supplies an explicit structure to test. It does not provide the missing joint observations or validate the constructs. The battery is unchanged. New paired designs, independent content coding and held-out evaluation are still required before replacing dashed proposals with supported associations.

### Observational and provenance layer

`knowledge_graph.json` is a standalone JSON graph with typed nodes, typed edges and input/analyzer provenance. It is also included under `knowledge_graph` in `analysis.json`.

| Node | Relationship | Node |
| --- | --- | --- |
| Psychological region | organizes | Candidate facet |
| Model run/configuration | has_observation | Behavioral finding |
| Behavioral finding | informs_hypothesis | Candidate facet |
| Behavioral finding | summarizes | Measurement cell |
| Measurement cell | observed_under | Design context |
| Measurement cell | supported_by | Original response evidence |
| Response evidence | elicited_in | Scenario |
| Behavioral finding | has_condition_effect | Matched condition effect |
| Behavioral finding | qualified_by | Wording/option-order check |
| Effect or check | supported_by_a / supported_by_b | Responses from each arm |
| Matched comparison | compares_a / compares_b | Findings for the displayed behavior |
| Matched comparison | model_a / model_b | Model runs |
| Matched comparison | within_facet | Candidate facet |
| Unrated finding | awaits_interpretation_of | Original responses |
| Behavioral finding | excluded_from_numeric_summary | Missing, invalid, declined or error response |

Comparisons of additional features remain linked to their facet, model runs and supporting responses, without implying that they measure the displayed headline behavior. Held-out comparisons retain their mode and matched-pair identity. The graph includes negative and null numerical results; it does not export only supporting results.

Candidate facets are theory-defined hypotheses. There are no inferred causal links, latent-factor links, or cross-facet psychological relationships. Word associations remain a separate observed network. Graph layout does not represent conceptual distance or the model's internal representations.

## Displayed behaviors and interpretation gaps

The `BEHAVIORS` registry selects an explicit task feature for each numerical headline: advice-agreement change, verification purchase, risky choice, unspecified-probability choice, clarification, allocation, honoring a stated choice, credit assigned to one's role, incentivized recommendation, and gain/loss transfer. These display choices are not the study's preregistered primary-outcome specification. All original feature-level analyses remain available.

Some decisions are measurable while their psychological meaning is not yet rated. Buying verification does not itself establish calibrated metacognition. A recommendation choice does not establish honesty or deception. Credit allocation does not establish narcissism. Transfer choices do not diagnose psychopathy. Human content review is still needed for those interpretations.

Four facets have no defensible automatic psychological headline here: contextual associations, conceptual distinctions/transfer, creative adaptation, and recipient-aware communication. Their actual responses remain in the graph as evidence awaiting interpretation. Canonical pair selections are retained in the detailed analysis but are not used as an automatic score of conceptual organization. This release does not import or generate human ratings.

## What would establish a fingerprint?

The current export is a candidate behavioral fingerprint with traceable evidence. Validation would require:

1. **Independent content coding:** frozen behavioral codebooks and blinded ratings, with rater agreement, for the text-based facets.
2. **Cross-scenario recurrence:** test whether the same conditional pattern recurs across distinct situations while retaining contradictory cases and presentation effects.
3. **Held-out prediction:** freeze expectations from development scenarios and score their predictions on untouched partners. Having a held-out lock or displaying a development/held-out difference is not itself predictive validation.
4. **Within-model reproducibility versus between-model separation:** multiple independent runs and configurations, testing identification on held-out runs without leaking scenario variants into both sides. The present one-run-per-configuration interface does not perform this validation.
5. **Construct and external validity:** show that hypothesized facets predict relevant behavior beyond these prompts, and test which facets really relate to one another. A statistical cross-facet structure cannot be established from two synthetic profiles.

There is a difference between identifying a model from stable language habits and identifying a psychologically meaningful pattern. Both may distinguish models; only the second supports the project's stronger interpretation.

Research supports treating validation as separate work. [Serapio-García et al.'s psychometric framework](https://www.nature.com/articles/s42256-025-01115-6) explicitly evaluates reliability and validity of LLM personality measurements. [Jung et al. (2026 revision)](https://arxiv.org/abs/2510.11254) report moderate reliability but poor alignment with downstream behavior for the particular human-derived constructs they studied. Neither finding validates this battery; they motivate testing its own measurement claims.

No new questions, model calls, external services, Python dependencies or JavaScript are introduced by this change.
