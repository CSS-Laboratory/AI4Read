---
id: density-ratio-estimation
type: concept
fields: [bayesian, llm]
fields_strong: [bayesian, llm]
n_sources: 2
n_works: 1
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch02-probability-p3, murphy-2023-pml2/ch26-generative]
generated_by: build_kg.py
---

# density-ratio-estimation

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch02-probability-p3]] (p. 61): estimate $P/Q$ from a classifier's odds [new]
- [[murphy-2023-pml2/ch26-generative]] (p. 896): get $p^*/q_\theta=D/(1-D)$ from a real-vs-fake classifier [new; work fields: bayesian, llm]

## Candidate bridges

- [structural-analogy] NCE ↔ logistic regression / classifier-based density-ratio estimation: the classifier is linked to the density ratio via Bayes' rule (p. 861). — from [[murphy-2023-pml2/ch24-energy]] (bayesian → other:statistics)
