---
id: l2-regularization
type: concept
fields: [llm, bayesian, information-theory, linear-algebra]
fields_strong: [llm, bayesian, information-theory, linear-algebra]
n_sources: 3
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [boyd-2018-vmls/ch15-multi, mackay-2003-information/ch44-supervised, prince-2023-udl/ch09-regularization]
aliases: [ridge-regression, tikhonov-regularization, weight-decay]
generated_by: build_kg.py
---

# l2-regularization

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `ridge-regression` — 1 digest(s)
- `tikhonov-regularization` — 1 digest(s)
- `weight-decay` — 1 digest(s)

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch44-supervised]] (p. 529): regularizer $\alpha E_W$ favouring small weights; interpreted as a negative log prior, Gaussian when $E_W$ is quadratic [alias `weight-decay`; new; work fields: information-theory, bayesian, llm]

### linear-algebra

- [[boyd-2018-vmls/ch15-multi]] (p. 317): minimize $\|Ax-y\|^2+\lambda\|x\|^2$; solution $(A^TA+\lambda I)^{-1}A^Ty$ [alias `tikhonov-regularization`, `ridge-regression`; new]
  - also: Tikhonov regularization in data fitting, penalizing $\beta$ but not the offset

### llm

- [[prince-2023-udl/ch09-regularization]] (p. 140): penalty $\lambda\sum_j\phi_j^2$ ("weight decay" in the main text); smooths the function [new]

## Candidate bridges

- [same-math] Exchangeable normal prior on regression coefficients ↔ ridge regression (stated on p. 401) — same quadratic penalty on coefficients. — from [[gelman-2013-bda3/ch15-hierarchical]] (bayesian → unspecified)
- [same-math] Posterior mean (WᵀW + λI)⁻¹(Wᵀy + λμ̂₀) ↔ ridge regression with a nonzero penalty centre: same estimating equation. — from [[gelman-2013-bda3/ch20-basis]] (bayesian → other:statistics)
- [structural-analogy] Weight decay $\alpha E_W$ ↔ Bayesian: a prior penalizing large parameters — the penalty adds to the objective as a log-prior would; this unit does not make the link. — from [[mackay-2003-information/ch39-single]] (information-theory → bayesian)
- [same-math] Weight decay ↔ bayesian: Gaussian prior with variance $1/\alpha$; the penalty is minus the log prior. — from [[mackay-2003-information/ch41-learning]] (information-theory → bayesian)
- [same-math] weight decay $\alpha E_W$ ↔ bayesian: Gaussian prior with variance $1/\alpha$ — the penalty is the negative log prior (p. 529). — from [[mackay-2003-information/ch44-supervised]] (information-theory → bayesian)
- [same-math] $\mathbf f_{\rm MP}$ with Gaussian prior ↔ ridge regression: $\mathbf R^{\rm T}\mathbf R+\lambda\mathbf C$ regularizes least squares. — from [[mackay-2003-information/ch46-deconvolution]] (information-theory → linear-algebra)
- [structural-analogy] Regularizing Gaussian prior / ridge regression ↔ frequentist statistics: penalized least squares with penalty $\lambda$ — the author says both views exist (p. 188). — from [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (bayesian → other:statistics)
- [structural-analogy] Posterior mean as convex combination of prior mean and MLE ↔ ridge regression: $\tau^2$ vs $\sigma^2$ plays the role of the $\ell_2$ penalty (p. 101) — same shrinkage mechanism in a different guise. — from [[murphy-2023-pml2/ch03-statistics-p2]] (bayesian → linear-algebra)
- [same-math] Gaussian prior MAP in linear regression ↔ ridge regression: $\lambda=\sigma^2/\tau^2$ in (15.49–15.50), up to the factor-of-2 noted in Reading notes. — from [[murphy-2023-pml2/ch15-generalized]] (bayesian → linear-algebra)
- [same-math] GP posterior mean (18.55) ↔ kernel ridge regression: equal when loss is squared and $\lambda=\sigma_y^2$ (p. 700). — from [[murphy-2023-pml2/ch18-gaussian-p1]] (bayesian → other:statistics)
