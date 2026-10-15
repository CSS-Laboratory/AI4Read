---
id: chernoff-information
type: concept
fields: [information-theory]
n_sources: 3
tiers: [core, deep, reference]
grounding: digests
sources: [cover-2006-elements/ch12-information-p2, nielsen-2020-elementary/main-p2, polyanskiy-2025-information/ch18-hypothesis]
generated_by: build_kg.py
---

# chernoff-information

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch12-information-p2]] (pp. 312–314): C(P₁,P₂)=D(P_λ*‖P₁)=D(P_λ*‖P₂)=−min_λ log Σ P₁^λP₂^{1−λ}; the best Bayesian exponent [new]
- [[nielsen-2020-elementary/main-p2]] (p. 37): $-\log\min_\alpha\int p_1^\alpha p_2^{1-\alpha}$; obtained by optimizing the exponent $\alpha$ in MAP testing (optimum $\alpha^*$); a Bregman divergence within an exponential family [new]
- [[polyanskiy-2025-information/ch18-hypothesis]] (p. 315): C(P,Q) = −inf_λ log ∫P^{1−λ}Q^λ; exponent of Bayesian error, prior-independent [new]

## Candidate bridges

- [structural-analogy] Chernoff information ↔ Bayesian decision theory: priors are "washed out" at large n as data dominate. — from [[cover-2006-elements/ch12-information-p2]] (information-theory → bayesian)
- [same-math] Chernoff information ↔ hypothesis testing/large deviations: the best error exponent of the MAP rule (p. 37). — from [[nielsen-2020-elementary/main-p2]] (information-theory → other)
