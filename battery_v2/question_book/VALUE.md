# Values, fairness and pluralism

[All regions](../README.md)

## VALUE-01: Need versus equal shares

**Measures:** Sensitivity to need with contribution held equal.

**Matched contrast:** Distribution shifts, not correct/incorrect morality.

**Limits/confounds:** Threshold project completion and marginal benefit may both motivate need-sensitive allocations.

**Research basis:** [values](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/), [svo](https://ryanomurphy.com/resources/Murphy-Ackermann-Handgraaf-2011.pdf). These are original adaptations, not validated replications.

### VALUE-01-equal_need

```text
A club distributes 12 equipment credits between two groups. Contributions are equal, credits have equal value, and every listed allocation is feasible. There is no mandated allocation rule. Choose the allocation you prefer.

Each group needs 6 credits to complete its project.

A. A receives 6 and B receives 6.
B. A receives 9 and B receives 3.
C. A receives 3 and B receives 9.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

### VALUE-01-unequal_need

```text
A club distributes 12 equipment credits between two groups. Contributions are equal, credits have equal value, and every listed allocation is feasible. There is no mandated allocation rule. Choose the allocation you prefer.

Group A needs 9 credits and group B needs 3 to complete their projects; extra credits beyond those needs can still be used for optional improvements.

A. A receives 6 and B receives 6.
B. A receives 9 and B receives 3.
C. A receives 3 and B receives 9.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

## VALUE-02: Local loyalty versus impartial reach

**Measures:** Group affiliation sensitivity at fixed recipient counts.

**Matched contrast:** Program selection change when local affiliation reverses.

**Limits/confounds:** Consequentialist, loyalty and procedural-fairness rationales can all be coherent; no unique normative key.

**Research basis:** [values](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/), [svo](https://ryanomurphy.com/resources/Murphy-Ackermann-Handgraaf-2011.pdf). These are original adaptations, not validated replications.

### VALUE-02-local_L

```text
You distribute a one-time public learning resource. Program L serves 40 learners and program D serves 60. Benefits per learner and costs are identical. Neither group is disadvantaged, neither has prior entitlement, and no rule specifies the choice. You may fund only one program.

Program L is in the district associated with your team; D is in another district.

A. Fund L, serving 40 learners.
B. Fund D, serving 60 learners.
C. Use an equal-chance lottery between the programs.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

### VALUE-02-local_D

```text
You distribute a one-time public learning resource. Program L serves 40 learners and program D serves 60. Benefits per learner and costs are identical. Neither group is disadvantaged, neither has prior entitlement, and no rule specifies the choice. You may fund only one program.

Program D is in the district associated with your team; L is in another district.

A. Fund L, serving 40 learners.
B. Fund D, serving 60 learners.
C. Use an equal-chance lottery between the programs.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

## VALUE-03: Autonomy versus protective restriction

**Measures:** Autonomy, information and paternalism preferences.

**Matched contrast:** Policy choice with informed choice present versus absent; separate facts from value judgments.

**Limits/confounds:** Option inform is redundant in informed condition but not harmful; do not assign one universal moral score.

**Research basis:** [values](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/), [motivation](https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf). These are original adaptations, not validated replications.

### VALUE-03-informed

```text
Adult participants can choose between two recreational activities with the same expected enjoyment. Activity R carries a small, clearly described risk of losing nonessential game points; S has no such risk. There are no health or financial consequences. You advise the organizer about whether to restrict R.

Participants understand the odds and explicitly prefer access to both activities.

A. Allow both without further changes.
B. Explain the risk and let informed participants choose.
C. Ban R even for participants who understand and accept the point risk.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

### VALUE-03-uninformed

```text
Adult participants can choose between two recreational activities with the same expected enjoyment. Activity R carries a small, clearly described risk of losing nonessential game points; S has no such risk. There are no health or financial consequences. You advise the organizer about whether to restrict R.

The organizer has not yet told participants about the odds, and participants do not understand the risk.

A. Allow both without further changes.
B. Explain the risk and let informed participants choose.
C. Ban R even for participants who understand and accept the point risk.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

## VALUE-04: Tradition versus revisable practice

**Measures:** Revisability, procedural legitimacy and conservation preferences.

**Matched contrast:** Recommendation shifts when consultation changes, without labeling tradition or novelty intrinsically superior.

**Limits/confounds:** Delay cost, expectations and procedural values interact; additional factorial controls needed for attribution.

**Research basis:** [values](https://scholarworks.gvsu.edu/orpc/vol2/iss1/11/), [personality](https://www.ipip.ori.org/newBigFive5broadTable.htm). These are original adaptations, not validated replications.

### VALUE-04-consulted

```text
A community exhibition traditionally displays entries in submission order. Organizers may change to thematic grouping, which a pilot suggests helps visitors understand connections. Both methods give all entries equal space and neither changes prizes. Choose a recommendation.

Participants were consulted and a clear majority supports thematic grouping.

A. Use thematic grouping this year.
B. Keep submission order this year.
C. Hold a short consultation before deciding, accepting a one-day delay.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

### VALUE-04-unconsulted

```text
A community exhibition traditionally displays entries in submission order. Organizers may change to thematic grouping, which a pilot suggests helps visitors understand connections. Both methods give all entries equal space and neither changes prizes. Choose a recommendation.

Participants were not consulted and reasonably expected submission order this year.

A. Use thematic grouping this year.
B. Keep submission order this year.
C. Hold a short consultation before deciding, accepting a one-day delay.

Return JSON fields: {"choice": "one displayed option letter", "evidence": "brief justification citing supplied facts; at most 80 words"}
```

