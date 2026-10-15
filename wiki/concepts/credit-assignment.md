---
id: credit-assignment
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [sutton-2018-rl/ch01-introduction, sutton-2018-rl/ch15-neuroscience-p1]
generated_by: build_kg.py
---

# credit-assignment

## Definitions in the sources

### control-theory

- [[sutton-2018-rl/ch01-introduction]] (p. 17): spreading credit for an outcome over the decisions that produced it [new]
- [[sutton-2018-rl/ch15-neuroscience-p1]] (p. 385): here the structural version: sharing credit or blame among the structures that produced a decision [new]

## Instances that use it

- [[chess-policy-network]] — board state → move; extreme credit assignment — from [[prince-2023-udl/ch01-introduction]]

## Candidate bridges

- [structural-analogy] backward-view credit assignment (TD error shouted back to prior states) ↔ control-theory: delay (dead time) — spreading a late signal back over earlier causes compensates for lag between action and effect. — from [[sutton-2018-rl/ch12-eligibility]] (control-theory → control-theory)
- [structural-analogy] team of units with one broadcast reward ↔ game theory: cooperative game with common payoff, where credit assignment replaces communication. — from [[sutton-2018-rl/ch15-neuroscience-p2]] (control-theory → decision-game-theory)
