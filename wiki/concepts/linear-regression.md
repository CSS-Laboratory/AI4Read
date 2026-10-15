---
id: linear-regression
type: concept
fields: [bayesian, linear-algebra]
fields_strong: [bayesian, linear-algebra]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [deisenroth-2020-mml/ch09-linear, mcelreath-2020-rethinking/ch04-linear-p2]
aliases: [linear-regression-model]
generated_by: build_kg.py
---

# linear-regression

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `linear-regression-model` — 1 digest(s)

## Definitions in the sources

### bayesian

- [[mcelreath-2020-rethinking/ch04-linear-p2]] (p. 93): a Gaussian outcome whose mean is a deterministic linear function of a predictor, $\mu_i=\alpha+\beta x_i$ [alias `linear-regression-model`; new]

### linear-algebra

- [[deisenroth-2020-mml/ch09-linear]] (pp. 291, 295): model $y=\phi^\top(x)\theta+\epsilon$, linear in the parameters, Gaussian noise [new]

## Instances that use it

- [[ard-linear-regression]] — CAVI with normal-gamma and Gamma factors — from [[blei-2017-variational/main-p2]]
- [[linear-regression]] — inputs $x\in\mathbb{R}^D$ mapped to real labels $y$ — from [[deisenroth-2020-mml/ch01-introduction]]
- [[gaussian-likelihood-linear-regression]] — Gaussian noise gives least squares (Ex. 8.4–8.5) — from [[deisenroth-2020-mml/ch08-when]]
- [[election-forecasting-regression]] — Hibbs 'bread and peace' linear regression, $n=15$; running example for all criteria — from [[gelman-2013-bda3/ch07-evaluating]]
- [[ptolemy-epicycles]] — a wrong but predictive descriptive model, analogy for linear regression — from [[mcelreath-2020-rethinking/ch04-linear-p1]]
- [[1d-linear-regression]] — the line $y=\phi_0+\phi_1x$ fitted by least squares — from [[prince-2023-udl/ch02-supervised]]
- [[linear-regression-gradient-descent]] — convex loss; after four iterations the parameters are already close to the minimum — from [[prince-2023-udl/ch06-fitting]]
- [[bayesian-linear-regression]] — Exercise 2.4 — from [[sarkka-2023-bayesianfiltering/ch02-bayesian]]
- [[linear-regression-recursive]] — recursive Gaussian regression equals the batch solution — from [[sarkka-2023-bayesianfiltering/ch03-batch]]

## Candidate bridges

- [same-math] straight-line slope ρ·std(y)/std(x) ↔ statistics: simple linear regression coefficient and "regression to the mean" (exercise 13.2). — from [[boyd-2018-vmls/ch13-least]] (linear-algebra → other:statistics)
- [same-math] Normal equation $B^\top B\lambda=B^\top x$ ↔ linear regression (Ch. 9, as stated in the unit): the least-squares fit is a projection of the target onto the column space (p. 88). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other:statistics)
- [same-math] Gaussian conditioning (6.66)–(6.67) ↔ linear-algebra: least squares/projection, where the conditional mean is a linear regression of $x$ on $y$ with the Schur complement as residual covariance — the formulas are the same block-matrix algebra (the text itself does not state this link). — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
- [same-math] t as normal scale mixture ↔ Bayesian linear regression: weighted regression with weights $1/V_i$, so robust regression is IRLS (p. 444–445) — from [[gelman-2013-bda3/ch17-models]] (bayesian → bayesian)
- [metaphor] Linear regression as geocentric model ↔ philosophy of modelling: a descriptive model can predict well while its structure is not the true process. — from [[mcelreath-2020-rethinking/ch04-linear-p1]] (bayesian → analytic-philosophy)
- [same-math] Kalman update (8.56) ↔ bayesian: conjugate Gaussian linear regression posterior — same conditioning formula. — from [[murphy-2023-pml2/ch08-gaussian-p1]] (bayesian → bayesian)
- [same-math] Gaussian prior MAP in linear regression ↔ ridge regression: $\lambda=\sigma^2/\tau^2$ in (15.49–15.50), up to the factor-of-2 noted in Reading notes. — from [[murphy-2023-pml2/ch15-generalized]] (bayesian → linear-algebra)
- [same-math] EKF on a linear model = recursive least squares ↔ Kalman filtering: the text itself says the KF applied to linear regression is recursive least squares (p. 673). — from [[murphy-2023-pml2/ch17-bayesian]] (bayesian → control-theory)
- [same-math] Bayesian linear regression with prior $\mathcal N(0,\Sigma_w)$ ↔ GP with kernel $\phi^{\mathsf T}\Sigma_w\phi$: identical predictive mean and variance (p. 696). — from [[murphy-2023-pml2/ch18-gaussian-p1]] (bayesian → other:gp-with-kernel-phimathsf)
- [same-math] M step of PPCA-EM ↔ multi-output linear regression (author notes this, p. 946), with latent expectations in place of inputs — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → unspecified)
- [same-math] RLS ↔ Bayesian: sequential updating of a Gaussian posterior for linear-regression weights; both are the same conjugate update. — from [[murphy-2023-pml2/ch29-state-p2]] (bayesian → bayesian)
- [same-math] Gaussian conditional expectation is linear in the regressors ↔ Bayesian linear regression: both use the multivariate normal conditional $E[Y|X_1..X_n]=r_0+\sum r_ix_i$. — from [[pearl-2016-primer/ch03-effects]] (bayesian → bayesian)
- [same-math] SL/SLR coefficients $\mathbf A=\mathbf C^{\mathsf T}\mathbf P^{-1}$ ↔ statistics: best linear (least-squares) predictor and its residual covariance — same formulas as linear regression, taken with respect to a Gaussian input. — from [[sarkka-2023-bayesianfiltering/ch09-gaussian]] (control-theory → other:statistics)
