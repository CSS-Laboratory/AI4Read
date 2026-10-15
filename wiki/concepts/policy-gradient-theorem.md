---
id: policy-gradient-theorem
type: concept
fields: [bayesian, control-theory]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [murphy-2023-pml2/ch35-reinforcement, sutton-2018-rl/ch13-policy]
generated_by: build_kg.py
---

# policy-gradient-theorem

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch35-reinforcement]] (p. 1157): $\nabla J\propto\mathbb E[\nabla\log\pi\cdot Q]$ under discounted visitation [new]

### control-theory

- [[sutton-2018-rl/ch13-policy]] (p. 326): $\nabla J\propto\sum_s\mu(s)\sum_aq_\pi(s,a)\nabla\pi(a|s,\theta)$, with no derivative of the state distribution [new]
