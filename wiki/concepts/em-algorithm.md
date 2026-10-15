---
id: em-algorithm
type: concept
fields: [bayesian, information-theory, control-theory, linear-algebra]
fields_strong: [bayesian, information-theory, control-theory, linear-algebra]
n_sources: 10
n_works: 8
tiers: [core, reference, deep]
grounding: digests
sources: [blei-2017-variational/main-p1, deisenroth-2020-mml/ch11-density, gelman-2013-bda3/ch13-modal, gelman-2013-bda3/ch18-models, mackay-2003-information/ch33-variational, mcgrayne-2011-theory/ch16-eureka, murphy-2023-pml2/ch04-graphical-p1, murphy-2023-pml2/ch06-optimization-p2, polyanskiy-2025-information/ch06-extremization, sarkka-2023-bayesianfiltering/ch16-parameter]
aliases: [expectation-maximization]
generated_by: build_kg.py
---

# em-algorithm

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `expectation-maximization` — 2 digest(s)

## Definitions in the sources

### bayesian

- [[blei-2017-variational/main-p1]] (p. 7): maximum-likelihood method for latent-variable models; assumes the posterior expectation is computable, unlike VI [new]
- [[gelman-2013-bda3/ch13-modal]] (pp. 320–321): alternate E-step (expected log joint) and M-step; $p(\phi|y)$ increases each iteration [new]
- [[gelman-2013-bda3/ch18-models]] (p. 452): E-step imputes expected sufficient statistics or counts, M-step updates the parameters; finds posterior modes [new]
- [[mcgrayne-2011-theory/ch16-eureka]] (p. 221): iterative method that turns a small data sample into estimates likely true for a whole population [new]
- [[murphy-2023-pml2/ch04-graphical-p1]] (pp. 160–161): for hidden variables: E step gives expected counts, M step normalizes them [alias `expectation-maximization`; new]
- [[murphy-2023-pml2/ch06-optimization-p2]] (p. 289): alternate E step (posterior over hidden variables) and M step (maximize expected complete-data log likelihood); a case of MM [new]

### information-theory

- [[mackay-2003-information/ch33-variational]] (pp. 432–433): E-step = assignment (Q_k), M-step = update (Q_θ; a delta function for exactly soft K-means); Neal–Hinton view as a variational optimization [new; work fields: information-theory, bayesian]
- [[polyanskiy-2025-information/ch06-extremization]] (p. 105): E-step sets $P_{Y|X}=Q^{(\theta)}_{Y|X}$; M-step maximizes over $\theta$ [alias `expectation-maximization`; new]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch16-parameter]] (p. 327): alternate E-step (smoother, $\mathcal Q$) and M-step (maximize $\mathcal Q$) [new; work fields: control-theory, bayesian]

### linear-algebra

- [[deisenroth-2020-mml/ch11-density]] (pp. 360–361, 367): alternate E-step (responsibilities) and M-step (parameter updates); raises log-likelihood, may reach a local optimum [new]

## Candidate bridges

- [structural-analogy] Variational EM ↔ bayesian: EM algorithm — both alternate local and global updates, with a variational E-step — from [[blei-2017-variational/main-p1]] (bayesian → bayesian)
- [structural-analogy] Blahut–Arimoto alternating minimization ↔ statistics: EM algorithm — the text says the Csiszár–Tusnády alternating-minimization procedure specializes to many situations, including EM (p. 367). — from [[cover-2006-elements/ch13-rate]] (information-theory → other:statistics)
- [same-math] Soft K-means update (22.21) ↔ Expectation–Maximization for Gaussian mixtures — the same weighted-mean update; these pages never mention EM, and say only that a proof that the algorithm maximizes the likelihood is deferred to section 33.7 (p. 305). — from [[mackay-2003-information/ch22-maximum]] (information-theory → unspecified)
- [structural-analogy] BA / IB alternating iteration ↔ EM algorithm — the paper compares the non-uniqueness and convexity structure with EM (p. 14) — from [[tishby-2000-bottleneck/main]] (information-theory → unspecified)
