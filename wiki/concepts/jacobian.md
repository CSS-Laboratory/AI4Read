---
id: jacobian
type: concept
fields: [linear-algebra, complex-systems, llm]
fields_strong: [linear-algebra, complex-systems, llm]
n_sources: 4
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [boyd-2018-vmls/ch18-nonlinear, deisenroth-2020-mml/ch05-vector, prince-2023-udl/ch22-mathematics, strogatz-2024-nonlinear/ch06-phase-p1]
aliases: [jacobian-matrix]
generated_by: build_kg.py
---

# jacobian

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `jacobian-matrix` — 2 digest(s)

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch18-nonlinear]] (p. 383): the $m\times n$ matrix $Df(x)$ of partial derivatives of $f$; gradient of $\|f\|^2$ is $2Df^Tf$ [alias `jacobian-matrix`; new]
- [[deisenroth-2020-mml/ch05-vector]] (p. 150): m×n matrix of first partials of $\mathbf f:\mathbb R^n\to\mathbb R^m$, numerator layout [new]

### complex-systems

- [[strogatz-2024-nonlinear/ch06-phase-p1]] (p. 152): matrix of partial derivatives of $(f,g)$ at the fixed point; multivariable analog of $f'(x^*)$ [alias `jacobian-matrix`; new]

### llm

- [[prince-2023-udl/ch22-mathematics]] (p. 448): D_x × D_y matrix of ∂y_j/∂x_i [new]

## Instances that use it

- [[gradient-of-linear-map]] — $\mathbf f=\mathbf A\mathbf x$ has Jacobian $\mathbf A$ — from [[deisenroth-2020-mml/ch05-vector]]
- [[jacobian-area-scaling]] — the parallelogram example with $|\det\mathbf J|=3$ — from [[deisenroth-2020-mml/ch05-vector]]

## Candidate bridges

- [same-math] Linearization and Jacobian eigenvalues ↔ dynamical-systems analysis of any fixed point: same criterion on $\partial F/\partial x$. — from [[astrom-2021-feedbacksystems/ch05-dynamic]] (control-theory → other:mathematics)
- [same-math] Linearization of a nonlinear ODE ↔ multivariable calculus: first-order Taylor expansion with the Jacobian — the matrices (6.35) are partial derivatives. — from [[astrom-2021-feedbacksystems/ch06-linear]] (control-theory → other:mathematics)
- [same-math] chain rule $Df=Dg\,Dh$ ↔ linear-algebra: matrix multiplication as composition — the Jacobian of a composition is the product of Jacobians. — from [[boyd-2018-vmls/app-appendices]] (linear-algebra → linear-algebra)
- [same-math] Chain rule as $Dh=Df\cdot Dg$ ↔ calculus/optimization: gradient of f(Ax+b) is $A^T\nabla f$ — the same Jacobian product. — from [[boyd-2018-vmls/ch10-matrix]] (linear-algebra → other:optimization)
- [same-math] Jacobian of a linear map ↔ linear-algebra: matrix of a linear map. $\mathbf f=\mathbf A\mathbf x$ has Jacobian $\mathbf A$, and the basis-change matrix equals the Jacobian (pp. 151–153). — from [[deisenroth-2020-mml/ch05-vector]] (linear-algebra → linear-algebra)
- [same-math] Jacobian determinant ↔ probability: change-of-variables density factor. The text defers this to Section 6.7 (p. 152). — from [[deisenroth-2020-mml/ch05-vector]] (linear-algebra → other:probability)
- [structural-analogy] Chain rule as product of Jacobians ↔ matrix multiplication as composition: neighbouring dimensions must match (p. 148). — from [[deisenroth-2020-mml/ch05-vector]] (linear-algebra → linear-algebra)
- [same-math] Jacobian determinant in (6.144) ↔ linear-algebra: determinant as signed volume scaling. — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
- [same-math] linearised perturbation $\dot\eta=A_*\eta+B_*\xi$ ↔ control-theory linearization: Jacobian linearisation along a trajectory (p. 72) — from [[liberzon-2012-calculus/ch03-calculus]] (control-theory → control-theory)
- [structural-analogy] MAP basis dependence (22.29) ↔ Bayesian: Jacobian of a density under change of variables — densities transform with $|\partial\theta/\partial u|$, so maxima move. — from [[mackay-2003-information/ch22-maximum]] (information-theory → bayesian)
- [structural-analogy] RJMCMC change of measure ↔ change of variables with Jacobian determinant in probability densities. — from [[murphy-2023-pml2/ch12-markov-p2]] (bayesian → unspecified)
- [same-math] Flow density via change of variables ↔ probability: transformation of random variables — the same formula with the Jacobian determinant. — from [[murphy-2023-pml2/ch23-normalizing]] (bayesian → other:probability)
- [structural-analogy] GAN training ↔ game theory/dynamical systems: Nash equilibria and Jacobian eigenvalues, as in the DiracGAN analysis. — from [[murphy-2023-pml2/ch26-generative]] (bayesian → decision-game-theory)
- [same-math] Jacobian ∂y/∂x = Aᵀ for y = Ax ↔ backpropagation through a linear layer: the same transpose-of-weights rule. — from [[prince-2023-udl/ch22-mathematics]] (llm → other:backpropagation-through-a-linear)
- [structural-analogy] EKF linearisation at the current estimate ↔ control-theory linearisation: Jacobian approximation of a non-linear system near an operating point — here taken at the moving estimate, not a fixed equilibrium. — from [[sarkka-2023-bayesianfiltering/ch07-extended]] (control-theory → control-theory)
- [structural-analogy] SLR as an affine fit averaged over a density ↔ Jacobian linearization: SLR replaces the Taylor expansion at a point (p. 291) by a fit over a density. Not the same math in general. — from [[sarkka-2023-bayesianfiltering/ch14-general]] (control-theory → other:jacobian-linearization)
- [same-math] Jacobian $A_x(m)$ in (A.33) ↔ control-theory: linearization about an equilibrium or trajectory — same Jacobian linearization. — from [[sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]] (control-theory → control-theory)
- [same-math] Chain-rule product of Jacobians ↔ linear-algebra: matrix multiplication as composition — each ∂F_k/∂F_{k−1} is a matrix and the whole is their product. — from [[strang-2023-introduction/ch09-linear]] (linear-algebra → linear-algebra)
- [same-math] $f'(x^*)$ stability test ↔ complex-systems: Jacobian eigenvalue test in higher dimensions — for $n=1$ the Jacobian is the single number $f'(x^*)$. — from [[strogatz-2024-nonlinear/ch02-flows]] (complex-systems → complex-systems)
- [same-math] Jacobian determinant as area/volume scaling ↔ change-of-variables for densities under a map: both use $|\det\mathbf J|$. — from [[strogatz-2024-nonlinear/ch12-strange]] (complex-systems → other:change-of-variables-for)
- [same-math] EKF Jacobians $A_k,W_k,H_k,V_k$ ↔ control-theory linearization: first-order Taylor expansion of $f,h$ about an operating point. — from [[welch-2004-kalmanintro/main]] (control-theory → control-theory)
