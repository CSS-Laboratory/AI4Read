---
id: extended-kalman-filter
type: concept
fields: [control-theory, bayesian]
fields_strong: [control-theory, bayesian]
n_sources: 6
n_works: 4
tiers: [core, deep, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch08-output, murphy-2023-pml2/ch08-gaussian-p1, murphy-2023-pml2/ch08-gaussian-p2, sarkka-2023-bayesianfiltering/ch07-extended, sarkka-2023-bayesianfiltering/ch17-epilogue, welch-2004-kalmanintro/main]
raw_ids: [extended Kalman filter]
generated_by: build_kg.py
---

# extended-kalman-filter

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-30): nonlinear prediction plus linearized gain $L(\hat x)$ (p. 8-30) (new) [as `extended Kalman filter`]
- [[sarkka-2023-bayesianfiltering/ch07-extended]] (p. 113): Kalman filter with $\mathbf f,\mathbf h$ in the means and Jacobians in the covariances; assumes Gaussian filtering densities [new; work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (p. 349): Gaussian-approximation filter; first method to try; has an iterated version and smoother (ERTSS) [new; work fields: control-theory, bayesian]
- [[welch-2004-kalmanintro/main]] (pp. 7–8): Kalman filter linearized about the current estimate; ad hoc, only approximates the optimality of Bayes' rule [new]

### bayesian

- [[murphy-2023-pml2/ch08-gaussian-p1]] (p. 375): Kalman filter on a first-order Taylor linearization [new; work fields: bayesian, control-theory]
- [[murphy-2023-pml2/ch08-gaussian-p2]] (p. 379, 385): Kalman filtering with the model linearized at the mean; equals GGF with linearized moments [new; work fields: bayesian, control-theory]

## Instances that use it

- [[extended-kalman-filter]] — entries 7.4, 7.5 — from [[sarkka-2023-bayesianfiltering/ch21-list]]

## Candidate bridges

- [structural-analogy] Lyapunov ODE (4.53) for $\mathbf P(t)$ ↔ control-theory: covariance propagation in the continuous-discrete extended Kalman filter (the text notes the same approximation is used there, p. 59). — from [[sarkka-2023-bayesianfiltering/ch04-discretization]] (control-theory → control-theory)
