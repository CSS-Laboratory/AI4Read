---
id: learning-rate-schedule
type: concept
fields: [bayesian, llm]
fields_strong: [bayesian, llm]
n_sources: 2
n_works: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch06-optimization-p1, prince-2023-udl/ch06-fitting]
generated_by: build_kg.py
---

# learning-rate-schedule

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch06-optimization-p1]] (p. 272): step size changed over time; Robbins–Monro conditions are sufficient for convergence [new]

### llm

- [[prince-2023-udl/ch06-fitting]] (p. 86): start $\alpha$ high, reduce by a constant factor every $N$ epochs [new]

## Candidate bridges

- [structural-analogy] SGD with fixed learning rate as approximate posterior sampler ↔ MCMC (SGLD): both generate approximate posterior samples, differing in explicit noise and learning-rate schedule. — from [[murphy-2023-pml2/ch17-bayesian]] (bayesian → bayesian)
- [structural-analogy] Learning rate schedule ↔ simulated annealing: large random moves early, small later — from [[prince-2023-udl/ch06-fitting]] (llm → bayesian)
