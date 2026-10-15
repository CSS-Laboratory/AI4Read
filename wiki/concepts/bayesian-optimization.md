---
id: bayesian-optimization
type: concept
fields: [bayesian, control-theory]
fields_strong: [bayesian, control-theory]
n_sources: 2
n_works: 2
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch02-approximation-p6, murphy-2023-pml2/ch06-optimization-p2]
generated_by: build_kg.py
---

# bayesian-optimization

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch06-optimization-p2]] (pp. 297–298): SMBO for expensive black-box $f$: surrogate $p(f|\mathcal D_n)$ plus acquisition function [new]

### control-theory

- [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (p. 299, 301–302): surrogate optimization with a posterior over function values $\theta$, updated after each noisy observation [new]

## Instances that use it

- [[alphazero-networks]] — specialized board-structured network (p. 372); Bayesian optimization used to tune its deep network (p. 377); deep networks an important factor in its success — from [[bertsekas-2026-rlcourse/ch03-learning-p2]]
