---
id: maximization-bias
type: concept
fields: [bayesian, control-theory]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [murphy-2023-pml2/ch35-reinforcement, sutton-2018-rl/ch06-temporal]
generated_by: build_kg.py
---

# maximization-bias

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch35-reinforcement]] (p. 1153): $\mathbb E[\max X_a]\ge\max\mathbb E[X_a]$ makes Q-learning overestimate; double Q-learning fixes it [new]

### control-theory

- [[sutton-2018-rl/ch06-temporal]] (p. 134): positive bias when a max over noisy estimates estimates a max true value [new]

## Instances that use it

- [[maximization-bias-mdp]] — states A and B with $\mathcal N(-0.1,1)$ rewards; Q-learning vs double Q-learning — from [[murphy-2023-pml2/ch35-reinforcement]]
- [[maximization-bias-mdp]] — Q-learning favors *left* wrongly; Double Q-learning does not — from [[sutton-2018-rl/ch06-temporal]]
