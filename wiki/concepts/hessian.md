---
id: hessian
type: concept
fields: [linear-algebra, llm]
fields_strong: [linear-algebra, llm]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch05-vector, prince-2023-udl/ch06-fitting]
generated_by: build_kg.py
---

# hessian

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch05-vector]] (p. 165): symmetric matrix of second partials; local curvature [new]

### llm

- [[prince-2023-udl/ch06-fitting]] (p. 92): matrix of second derivatives; positive eigenvalues everywhere implies convexity [new]

## Instances that use it

- [[mm-logistic-regression]] — fixed Hessian bound $-\tfrac14\mathbf X^\top\mathbf X$ yields a cheaper-than-IRLS update — from [[murphy-2023-pml2/ch06-optimization-p2]]

## Candidate bridges

- [same-math] Hessian symmetry and $\boldsymbol\delta^\top\mathbf H\boldsymbol\delta$ ↔ quadratic forms and symmetric matrices (canon link; not stated in this unit). — from [[deisenroth-2020-mml/ch05-vector]] (linear-algebra → unspecified)
- [same-math] Quadratic approximation ↔ Gaussian (Laplace-type) approximation of a density at its mode using the second derivative of the log density (the chapter gives only the mode-plus-Hessian procedure). — from [[mcelreath-2020-rethinking/ch02-small]] (bayesian → unspecified)
- [same-math] Fisher information as Hessian of $D$ ↔ statistics: curvature of log-likelihood — the chapter gives $J_F=-\mathbb E[\mathrm{Hess}\ln p_\theta]$ (p. 39). — from [[polyanskiy-2025-information/ch03-divergence]] (information-theory → other:statistics)
- [structural-analogy] Hessian-eigenvalue classification of zero-gradient points ↔ dynamical systems: stability of fixed points — from [[prince-2023-udl/ch06-fitting]] (llm → complex-systems)
- [same-math] Positive definite second-derivative matrix ↔ optimization: Hessian positive definite means a local minimum and convexity. — from [[strang-2023-introduction/ch06-eigenvalues-p2]] (linear-algebra → other:optimization)
