---
id: laplace-approximation
type: concept
fields: [bayesian, information-theory, llm, control-theory]
fields_strong: [bayesian, information-theory, llm, control-theory]
n_sources: 8
n_works: 4
tiers: [core, reference, deep]
grounding: digests
sources: [gelman-2013-bda3/ch13-modal, gelman-2013-bda3/ch21-gaussian, mackay-2003-information/ch28-model, mackay-2003-information/ch41-learning, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch15-generalized, murphy-2023-pml2/ch17-bayesian, sarkka-2023-bayesianfiltering/ch16-parameter]
generated_by: build_kg.py
---

# laplace-approximation

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch13-modal]] (p. 318): approximate $\int h\,p$ by $h(\theta_0)p(\theta_0|y)(2\pi)^{d/2}|-u''|^{-1/2}$ [new]
- [[gelman-2013-bda3/ch21-gaussian]] (p. 510): normal approximation at the latent posterior mode; also approximates the log marginal likelihood (21.3) [new]
- [[murphy-2023-pml2/ch07-inference]] (p. 352): Gaussian $\mathcal N(\hat\theta,\mathbf H^{-1})$ at the mode [new]
- [[murphy-2023-pml2/ch15-generalized]] (p. 614): Gaussian at the MAP with inverse-Hessian covariance [new]
- [[murphy-2023-pml2/ch17-bayesian]] (pp. 652–653): Gaussian at the MAP with GGN curvature, Eq. (17.16) [new; work fields: bayesian, llm]

### information-theory

- [[mackay-2003-information/ch28-model]] (p. 341): replace a density by a Gaussian at its peak; $Z\simeq P^*(\mathbf{x}_0)\sqrt{(2\pi)^K/\det\mathbf{A}}$ [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch41-learning]] (p. 501): Gaussian fit at $\mathbf w_{\rm MP}$ with covariance $\mathbf A^{-1}$ [new; work fields: information-theory, bayesian, llm]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch16-parameter]] (p. 323): Gaussian around the MAP, covariance = inverse Hessian of the energy [new; work fields: control-theory, bayesian]

## Instances that use it

- [[separable-2d-logistic-laplace]] — Laplace approximation, MC vs probit predictive — from [[murphy-2023-pml2/ch15-generalized]]
- [[finland-heart-attack-disease-mapping]] — Poisson GP, $y_n\sim\mathrm{Poi}(e_nr_n)$, $\log r\sim$ GP, Laplace approximation — from [[murphy-2023-pml2/ch18-gaussian-p2]]

## Candidate bridges

- [same-math] Laplace approximation ↔ physics: saddle-point approximation — the source names them as the same method (p. 341) — from [[mackay-2003-information/ch28-model]] (information-theory → other:physics)
- [same-math] INLA's Laplace step (Gaussian approximation about the mode) ↔ Laplace approximation to the posterior in Bayesian models (p. 179). — from [[murphy-2023-pml2/ch04-graphical-p2]] (bayesian → unspecified)
- [same-math] Laplace approximation ↔ second-order Taylor expansion of a log-density at its maximum — the Gaussian is exactly the quadratic expansion. — from [[murphy-2023-pml2/ch07-inference]] (bayesian → unspecified)
