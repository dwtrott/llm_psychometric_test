# Observation versus intervention (CAUSE)

[Back to all questions](../QUESTIONS.md)

Researcher scoring note: Absolute probability error /100; contrast observation and intervention.

Interpretation limit: Task correctness is not a general causal trait.

The following blocks contain the complete user prompts. Each uses the shared system prompt in the index.

## CAUSE-001

```text
In a fictional deterministic system, switch causes lamp, which causes sensor. Each variable is either on or off. With no interventions, lamp copies switch and sensor copies lamp; switch is on in half the cases. You observe sensor is on. What is the probability that switch is on?
Return these JSON fields: {"probability": "number 0..100"}
```

## CAUSE-002

```text
In a fictional deterministic system, switch causes lamp, which causes sensor. Each variable is either on or off. With no interventions, lamp copies switch and sensor copies lamp; switch is on in half the cases. An external intervention forces sensor on without changing switch or lamp. What is the probability that switch is on?
Return these JSON fields: {"probability": "number 0..100"}
```

## CAUSE-003

```text
In a fictional deterministic system, valve causes flow, which causes meter. Each variable is either on or off. With no interventions, flow copies valve and meter copies flow; valve is on in half the cases. You observe meter is on. What is the probability that valve is on?
Return these JSON fields: {"probability": "number 0..100"}
```

## CAUSE-004

```text
In a fictional deterministic system, valve causes flow, which causes meter. Each variable is either on or off. With no interventions, flow copies valve and meter copies flow; valve is on in half the cases. An external intervention forces meter on without changing valve or flow. What is the probability that valve is on?
Return these JSON fields: {"probability": "number 0..100"}
```

## CAUSE-005

```text
In a fictional deterministic system, button causes motor, which causes display. Each variable is either on or off. With no interventions, motor copies button and display copies motor; button is on in half the cases. You observe display is on. What is the probability that button is on?
Return these JSON fields: {"probability": "number 0..100"}
```

## CAUSE-006

```text
In a fictional deterministic system, button causes motor, which causes display. Each variable is either on or off. With no interventions, motor copies button and display copies motor; button is on in half the cases. An external intervention forces display on without changing button or motor. What is the probability that button is on?
Return these JSON fields: {"probability": "number 0..100"}
```

