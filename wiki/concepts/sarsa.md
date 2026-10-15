---
id: sarsa
type: concept
fields: [bayesian, control-theory]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [murphy-2023-pml2/ch35-reinforcement, sutton-2018-rl/ch06-temporal]
generated_by: build_kg.py
---

# sarsa

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch35-reinforcement]] (p. 1153): on-policy TD control using the sampled next action [new]

### control-theory

- [[sutton-2018-rl/ch06-temporal]] (p. 129): on-policy TD control using $(S,A,R,S',A')$ [new]

## Instances that use it

- [[windy-gridworld]] — Sarsa where MC is awkward — from [[sutton-2018-rl/ch06-temporal]]
- [[cliff-walking]] — Sarsa safer online than Q-learning — from [[sutton-2018-rl/ch06-temporal]]
- [[gridworld-nstep-sarsa]] — one-step vs 10-step Sarsa strengthening of action values after one path — from [[sutton-2018-rl/ch07-n]]
- [[mountain-car]] — continuous control where progress requires first moving away from the goal; linear tile-coded Sarsa — from [[sutton-2018-rl/ch10-policy]]
- [[access-control-queuing]] — tabular differential Sarsa; $\bar R\approx2.31$ — from [[sutton-2018-rl/ch10-policy]]
- [[mountain-car]] — Example 12.2 and Fig. 12.11: Sarsa(λ) versus n-step Sarsa and true online Sarsa(λ) — from [[sutton-2018-rl/ch12-eligibility]]

## Candidate bridges

- [structural-analogy] SARSA update (3.27) ↔ temporal-difference learning: parameter moves along a gradient times the Q prediction error — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → other)
