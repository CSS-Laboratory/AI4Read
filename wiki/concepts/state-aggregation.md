---
id: state-aggregation
type: concept
fields: [control-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [sutton-2018-rl/ch09-policy-p1, sutton-2018-rl/ch16-applications]
generated_by: build_kg.py
---

# state-aggregation

## Definitions in the sources

### control-theory

- [[sutton-2018-rl/ch09-policy-p1]] (p. 208): states grouped, one weight per group; a special case of SGD (p. 203) and of linear approximation [new]
- [[sutton-2018-rl/ch16-applications]] (p. 454): group states and share one value per group; used in soaring [new]

## Instances that use it

- [[random-walk-1000-states]] — running example for state aggregation, bootstrapping and feature comparisons — from [[sutton-2018-rl/ch09-policy-p1]]

## Candidate bridges

- [structural-analogy] State aggregation ↔ control-theory: discretizing a continuous state space into cells — both treat nearby states as one. — from [[sutton-2018-rl/ch09-policy-p1]] (control-theory → control-theory)
