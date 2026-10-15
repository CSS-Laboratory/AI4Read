---
id: bayes-factor
type: concept
fields: [bayesian, linear-algebra]
fields_strong: [bayesian, linear-algebra]
n_sources: 5
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch08-when, gelman-2013-bda3/ch07-evaluating, mcgrayne-2011-theory/ch04-bayes, mcgrayne-2011-theory/ch08-jerome, murphy-2023-pml2/ch03-statistics-p3]
generated_by: build_kg.py
---

# bayes-factor

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch07-evaluating]] (p. 183): ratio of marginal densities of the data under two models (7.16); needs proper marginals [new]
- [[mcgrayne-2011-theory/ch04-bayes]] (p. 69): the factor by which evidence multiplies odds; Good used Bayes factors and their logarithms sequentially [new]
- [[mcgrayne-2011-theory/ch08-jerome]] (p. 116): probability of data under one hypothesis divided by that under another [new]
- [[murphy-2023-pml2/ch03-statistics-p3]] (p. 132): ratio of marginal likelihoods; Jeffreys scale [new]

### linear-algebra

- [[deisenroth-2020-mml/ch08-when]] (p. 287): ratio of evidences p(D | M₁)/p(D | M₂) (8.46) [new]

## Instances that use it

- [[eight-schools]] — no pooling vs complete pooling vs hierarchical compared by AIC/DIC/WAIC/CV (Table 7.1); Bayes factor failure — from [[gelman-2013-bda3/ch07-evaluating]]
- [[genetics-bayes-factor]] — Section 1.4 example with posterior odds 4 — from [[gelman-2013-bda3/ch07-evaluating]]
- [[coin-fair-bayes-factor]] — $M_0$ vs $M_1$, $N=5$, marginal likelihood vs heads — from [[murphy-2023-pml2/ch03-statistics-p3]]

## Candidate bridges

- [structural-analogy] Bayes factor sensitivity to prior variance $A^2$ ↔ Bayesian hypothesis testing (Lindley-type behaviour with diffuse priors) — a model's evidence depends on how much prior mass is wasted on unlikely data. — from [[gelman-2013-bda3/ch07-evaluating]] (bayesian → unspecified)
- [same-math] Weight of evidence $\log\frac{P(D|\mathcal H_1)}{P(D|\mathcal H_2)}$ ↔ bayesian: log Bayes factor / posterior log odds minus prior log odds — the same likelihood ratio, expressed in decibans. — from [[mackay-2003-information/ch18-crosswords]] (information-theory → bayesian)
- [structural-analogy] Bayes factor ↔ marginal-likelihood model comparison — both compare how well hypotheses predict data. — from [[mcgrayne-2011-theory/ch08-jerome]] (bayesian → unspecified)
- [structural-analogy] Expected weight of evidence ↔ Bayes factor / log posterior odds (§5.1.3.3). — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → unspecified)
