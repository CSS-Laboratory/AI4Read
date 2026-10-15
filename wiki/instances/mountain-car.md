---
id: mountain-car
type: instance
fields: [control-theory]
n_sources: 3
tiers: [core, deep]
grounding: digests
sources: [ng-2000-irl/main, sutton-2018-rl/ch10-policy, sutton-2018-rl/ch12-eligibility]
generated_by: build_kg.py
---

# mountain-car

## Descriptions in the sources

### control-theory

- [[ng-2000-irl/main]] (p. 6): continuous test with two true rewards, with fitted rewards judged by the authors to capture the main structure
- [[sutton-2018-rl/ch10-policy]] (p. 244): continuous control where progress requires first moving away from the goal; linear tile-coded Sarsa [new]
- [[sutton-2018-rl/ch12-eligibility]] (pp. 305–306): Example 12.2 and Fig. 12.11: Sarsa(λ) versus n-step Sarsa and true online Sarsa(λ)

## Candidate bridges

- [metaphor] Mountain Car ("worse before better") ↔ control theory: systems whose response first moves the wrong way. — from [[sutton-2018-rl/ch10-policy]] (control-theory → control-theory)
