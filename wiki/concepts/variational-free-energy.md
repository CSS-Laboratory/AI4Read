---
id: variational-free-energy
type: concept
fields: [bayesian, information-theory]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [mackay-2003-information/ch33-variational, murphy-2023-pml2/ch10-variational-p1]
generated_by: build_kg.py
---

# variational-free-energy

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch10-variational-p1]] (p. 440): expected energy minus entropy, the negative ELBO [new]

### information-theory

- [[mackay-2003-information/ch33-variational]] (p. 423): βF̃(θ) = β⟨E⟩_Q − S_Q = D_KL(Q‖P) + βF; objective minimized over Q [new]

## Candidate bridges

- [same-math] variational free energy F̃ = D_KL(Q‖P) + F ↔ bayesian: ELBO, since F̃ = −ln P(D|H) + D_KL(Q‖posterior) is minus the lower bound on log evidence. — from [[mackay-2003-information/ch33-variational]] (information-theory → bayesian)
- [structural-analogy] predictive coding / active inference ↔ bayesian: variational free energy as the objective for perception and action (p. 1181). — from [[murphy-2023-pml2/ch35-reinforcement]] (bayesian → bayesian)
