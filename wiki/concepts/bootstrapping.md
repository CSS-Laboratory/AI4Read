---
id: bootstrapping
type: concept
fields: [control-theory, llm]
n_sources: 6
tiers: [core, reference]
grounding: digests
sources: [prince-2023-udl/ch19-reinforcement, sutton-2018-rl/ch04-dynamic, sutton-2018-rl/ch05-monte, sutton-2018-rl/ch06-temporal, sutton-2018-rl/ch07-n, sutton-2018-rl/ch12-eligibility]
generated_by: build_kg.py
---

# bootstrapping

## Definitions in the sources

### control-theory

- [[sutton-2018-rl/ch04-dynamic]] (p. 89): updating estimates from other estimates [new]
- [[sutton-2018-rl/ch05-monte]] (p. 95): updating an estimate from other estimates; MC does not do this [new]
- [[sutton-2018-rl/ch06-temporal]] (p. 120, p. 124): updating an estimate partly from another estimate, a "guess from a guess" [new]
- [[sutton-2018-rl/ch07-n]] (p. 141): updating an estimate from another estimate; here over n steps instead of one [new]
- [[sutton-2018-rl/ch12-eligibility]] (pp. 308, 317): using current value estimates in the target; λ sets the degree [new]

### llm

- [[prince-2023-udl/ch19-reinforcement]] (p. 383): updating a value from other current value estimates [new]

## Instances that use it

- [[random-walk-1000-states]] — running example for state aggregation, bootstrapping and feature comparisons — from [[sutton-2018-rl/ch09-policy-p1]]
