---
id: matrix-exponential
type: concept
fields: [control-theory, linear-algebra]
fields_strong: [control-theory, linear-algebra]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch06-linear, strang-2023-introduction/ch06-eigenvalues-p3]
generated_by: build_kg.py
---

# matrix-exponential

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch06-linear]] (pp. 6-6, 6-7): $e^{X}=\sum X^k/k!$; $x(t)=e^{At}x(0)$ solves $\dot x=Ax$ [new]

### linear-algebra

- [[strang-2023-introduction/ch06-eigenvalues-p3]] (p. 276): $e^{At}=\sum(At)^n/n!$; solves du/dt = Au [new]

## Instances that use it

- [[rotation-matrix-exponential]] — $e^{At}$ for A = [0 1; −1 0] is a rotation by t — from [[strang-2023-introduction/ch06-eigenvalues-p3]]

## Candidate bridges

- [same-math] $\mathbf A=\exp(\mathbf F\Delta t)$ in Thm 4.3 ↔ control-theory: state transition of a linear time-invariant system between sampling instants — same matrix exponential. — from [[sarkka-2023-bayesianfiltering/ch04-discretization]] (control-theory → control-theory)
- [same-math] Lemma A.9 variation-of-constants solution ↔ control-theory: solution of $\dot x=Ax+Bu$ via the matrix exponential, with noise integral added — same formula with $b$ as input. — from [[sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]] (control-theory → control-theory)
