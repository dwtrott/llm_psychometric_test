# Planning under constraints (PLAN)

[Back to all questions](../QUESTIONS.md)

Researcher scoring note: Feasibility accuracy; schedule category under deadline and resource changes.

Interpretation limit: Small explicit planning tasks; not long-horizon agent competence.

The following blocks contain the complete user prompts. Each uses the shared system prompt in the index.

## PLAN-001

```text
Plan a fictional assembly workflow. Tasks A, B, and C each take one time unit. A must finish before B starts; C has no dependencies. Two workers are available, so two tasks can run at once. All tasks must finish by time 2. Choose a feasible schedule, or say none is feasible.
Options:
A. No listed schedule meets the constraints.
B. Time 0-1: B and C. Time 1-2: A.
C. Time 0-1: A. Time 1-2: B. Time 2-3: C.
D. Time 0-1: A and C. Time 1-2: B.
Return these JSON fields: {"choice": "one displayed option label"}
```

## PLAN-002

```text
Plan a fictional assembly workflow. Tasks A, B, and C each take one time unit. A must finish before B starts; C has no dependencies. Two workers are available, so two tasks can run at once. All tasks must finish by time 3. Choose a feasible schedule, or say none is feasible.
Options:
A. Time 0-1: A and C. Time 1-2: B.
B. Time 0-1: B and C. Time 1-2: A.
C. Time 0-1: A. Time 1-2: B. Time 2-3: C.
D. No listed schedule meets the constraints.
Return these JSON fields: {"choice": "one displayed option label"}
```

## PLAN-003

```text
Plan a fictional assembly workflow. Tasks A, B, and C each take one time unit. A must finish before B starts; C has no dependencies. One worker is available, so only one task can run at once. All tasks must finish by time 2. Choose a feasible schedule, or say none is feasible.
Options:
A. Time 0-1: B and C. Time 1-2: A.
B. Time 0-1: A. Time 1-2: B. Time 2-3: C.
C. No listed schedule meets the constraints.
D. Time 0-1: A and C. Time 1-2: B.
Return these JSON fields: {"choice": "one displayed option label"}
```

## PLAN-004

```text
Plan a fictional assembly workflow. Tasks A, B, and C each take one time unit. A must finish before B starts; C has no dependencies. One worker is available, so only one task can run at once. All tasks must finish by time 3. Choose a feasible schedule, or say none is feasible.
Options:
A. Time 0-1: A. Time 1-2: B. Time 2-3: C.
B. Time 0-1: A and C. Time 1-2: B.
C. Time 0-1: B and C. Time 1-2: A.
D. No listed schedule meets the constraints.
Return these JSON fields: {"choice": "one displayed option label"}
```

## PLAN-005

```text
Plan a fictional preparation workflow. Tasks A, B, and C each take one time unit. A must finish before B starts; C has no dependencies. Two workers are available, so two tasks can run at once. All tasks must finish by time 2. Choose a feasible schedule, or say none is feasible.
Options:
A. No listed schedule meets the constraints.
B. Time 0-1: A. Time 1-2: B. Time 2-3: C.
C. Time 0-1: B and C. Time 1-2: A.
D. Time 0-1: A and C. Time 1-2: B.
Return these JSON fields: {"choice": "one displayed option label"}
```

## PLAN-006

```text
Plan a fictional preparation workflow. Tasks A, B, and C each take one time unit. A must finish before B starts; C has no dependencies. Two workers are available, so two tasks can run at once. All tasks must finish by time 3. Choose a feasible schedule, or say none is feasible.
Options:
A. Time 0-1: A. Time 1-2: B. Time 2-3: C.
B. Time 0-1: B and C. Time 1-2: A.
C. No listed schedule meets the constraints.
D. Time 0-1: A and C. Time 1-2: B.
Return these JSON fields: {"choice": "one displayed option label"}
```

## PLAN-007

```text
Plan a fictional preparation workflow. Tasks A, B, and C each take one time unit. A must finish before B starts; C has no dependencies. One worker is available, so only one task can run at once. All tasks must finish by time 2. Choose a feasible schedule, or say none is feasible.
Options:
A. No listed schedule meets the constraints.
B. Time 0-1: A and C. Time 1-2: B.
C. Time 0-1: B and C. Time 1-2: A.
D. Time 0-1: A. Time 1-2: B. Time 2-3: C.
Return these JSON fields: {"choice": "one displayed option label"}
```

## PLAN-008

```text
Plan a fictional preparation workflow. Tasks A, B, and C each take one time unit. A must finish before B starts; C has no dependencies. One worker is available, so only one task can run at once. All tasks must finish by time 3. Choose a feasible schedule, or say none is feasible.
Options:
A. Time 0-1: A and C. Time 1-2: B.
B. Time 0-1: A. Time 1-2: B. Time 2-3: C.
C. Time 0-1: B and C. Time 1-2: A.
D. No listed schedule meets the constraints.
Return these JSON fields: {"choice": "one displayed option label"}
```

## PLAN-009

```text
Plan a fictional review workflow. Tasks A, B, and C each take one time unit. A must finish before B starts; C has no dependencies. Two workers are available, so two tasks can run at once. All tasks must finish by time 2. Choose a feasible schedule, or say none is feasible.
Options:
A. Time 0-1: A. Time 1-2: B. Time 2-3: C.
B. Time 0-1: B and C. Time 1-2: A.
C. No listed schedule meets the constraints.
D. Time 0-1: A and C. Time 1-2: B.
Return these JSON fields: {"choice": "one displayed option label"}
```

## PLAN-010

```text
Plan a fictional review workflow. Tasks A, B, and C each take one time unit. A must finish before B starts; C has no dependencies. Two workers are available, so two tasks can run at once. All tasks must finish by time 3. Choose a feasible schedule, or say none is feasible.
Options:
A. No listed schedule meets the constraints.
B. Time 0-1: A. Time 1-2: B. Time 2-3: C.
C. Time 0-1: A and C. Time 1-2: B.
D. Time 0-1: B and C. Time 1-2: A.
Return these JSON fields: {"choice": "one displayed option label"}
```

## PLAN-011

```text
Plan a fictional review workflow. Tasks A, B, and C each take one time unit. A must finish before B starts; C has no dependencies. One worker is available, so only one task can run at once. All tasks must finish by time 2. Choose a feasible schedule, or say none is feasible.
Options:
A. No listed schedule meets the constraints.
B. Time 0-1: A and C. Time 1-2: B.
C. Time 0-1: A. Time 1-2: B. Time 2-3: C.
D. Time 0-1: B and C. Time 1-2: A.
Return these JSON fields: {"choice": "one displayed option label"}
```

## PLAN-012

```text
Plan a fictional review workflow. Tasks A, B, and C each take one time unit. A must finish before B starts; C has no dependencies. One worker is available, so only one task can run at once. All tasks must finish by time 3. Choose a feasible schedule, or say none is feasible.
Options:
A. Time 0-1: A. Time 1-2: B. Time 2-3: C.
B. Time 0-1: A and C. Time 1-2: B.
C. Time 0-1: B and C. Time 1-2: A.
D. No listed schedule meets the constraints.
Return these JSON fields: {"choice": "one displayed option label"}
```

