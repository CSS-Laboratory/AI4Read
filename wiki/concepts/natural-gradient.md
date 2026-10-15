---
id: natural-gradient
type: concept
fields: [information-theory, bayesian, control-theory]
n_sources: 4
tiers: [core, deep, reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch03-learning-p4, blei-2017-variational/main-p1, mackay-2003-information/ch34-independent, nielsen-2020-elementary/main-p2]
generated_by: build_kg.py
---

# natural-gradient

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch34-independent]] (p. 443): the quantity $W_{ij}+x'_jz_i$ of the covariant ICA rule [new]
- [[nielsen-2020-elementary/main-p2]] (pp. 34–35): $g^{-1}\nabla L$; coordinate-invariant steepest-descent direction; equals ordinary gradient in dual coordinates when dually flat [new]

### bayesian

- [[blei-2017-variational/main-p1]] (p. 20): gradient premultiplied by the inverse Fisher information, $a''(\lambda)^{-1}$; for the ELBO it gives $g(\lambda)=\mathbb E[\hat\alpha]-\lambda$ [new]

### control-theory

- [[bertsekas-2026-rlcourse/ch03-learning-p4]] (p. 420): gradient scaled by the inverse Fisher information matrix (3.62)–(3.63) [new]

## Candidate bridges

- [structural-analogy] KL $\approx\frac12\delta^\top F\delta$ ↔ squared Mahalanobis distance with the Fisher matrix as metric (an approximation), the basis of natural gradient (§5.1.9). — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → unspecified)
- [structural-analogy] Natural parameters vs moment parameters ↔ exponential-family duality: ordinary gradient in $\mu$ equals natural gradient in $\lambda$ (p. 284) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → other)
- [same-math] Natural gradient with Fisher metric ↔ machine learning: the natural-gradient update $\theta-\alpha g^{-1}\nabla L$ used in NES — the same formula, with $g$ the (empirical) FIM (pp. 34, 36). — from [[nielsen-2020-elementary/main-p2]] (information-theory → other)
