---
id: q-learning
type: concept
fields: [control-theory, bayesian, llm]
fields_strong: [control-theory, bayesian, llm]
n_sources: 4
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [murphy-2023-pml2/ch35-reinforcement, prince-2023-udl/ch19-reinforcement, recht-2019-tour/main, sutton-2018-rl/ch06-temporal]
generated_by: build_kg.py
---

# q-learning

## Definitions in the sources

### control-theory

- [[recht-2019-tour/main]] (p. 7): stochastic-approximation update (3.7) of the discounted Q-function [new]
- [[sutton-2018-rl/ch06-temporal]] (p. 131): off-policy TD control with a max target; $Q$ approximates $q_*$ [new]

### bayesian

- [[murphy-2023-pml2/ch35-reinforcement]] (p. 1153): off-policy TD control with greedy next-action target, learning $Q_*$ [new; work fields: bayesian, control-theory]

### llm

- [[prince-2023-udl/ch19-reinforcement]] (p. 385): off-policy TD update using the max next action value [new]

## Instances that use it

- [[maximization-bias-mdp]] — states A and B with $\mathcal N(-0.1,1)$ rewards; Q-learning vs double Q-learning — from [[murphy-2023-pml2/ch35-reinforcement]]
- [[gridworld-q-learning]] — 1d grid, $\gamma=0.9$, values 1, 0.9, 0.81, 0.73 — from [[murphy-2023-pml2/ch35-reinforcement]]
- [[penguin-ice-grid]] — running example for Markov processes, MDPs, values, DP, MC and Q-learning — from [[prince-2023-udl/ch19-reinforcement]]
- [[cliff-walking]] — Sarsa safer online than Q-learning — from [[sutton-2018-rl/ch06-temporal]]
- [[maximization-bias-mdp]] — Q-learning favors *left* wrongly; Double Q-learning does not — from [[sutton-2018-rl/ch06-temporal]]

## Candidate bridges

- [same-math] Q-learning update (3.7) ↔ stochastic approximation: a step-size-weighted average of the old value and a noisy Bellman target. — from [[recht-2019-tour/main]] (control-theory → other:optimization)
- [structural-analogy] Q-learning's max backup ↔ Bellman equation / value iteration — a sampled version of the optimality backup. — from [[sutton-2018-rl/ch06-temporal]] (control-theory → unspecified)
