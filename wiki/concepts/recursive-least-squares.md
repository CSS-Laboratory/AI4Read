---
id: recursive-least-squares
type: concept
fields: [control-theory, bayesian]
fields_strong: [control-theory, bayesian]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch15-architecture-p2, murphy-2023-pml2/ch29-state-p2]
generated_by: build_kg.py
---

# recursive-least-squares

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch29-state-p2]] (p. 1008): online Bayesian linear regression as Kalman filtering with weights as state [new; work fields: bayesian, control-theory]

### control-theory

- [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (p. 15-31): recursive estimate, special case of the Kalman filter [new]

## Instances that use it

- [[recursive-least-squares]] — Kalman filter with latent state = regression weights — from [[murphy-2023-pml2/ch08-gaussian-p1]]

## Candidate bridges

- [same-math] Recursive least squares (15.19) ↔ Kalman filter: the author states RLS is a special case of the Kalman filter (§8.2). — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (control-theory → control-theory)
- [same-math] EKF on a linear model = recursive least squares ↔ Kalman filtering: the text itself says the KF applied to linear regression is recursive least squares (p. 673). — from [[murphy-2023-pml2/ch17-bayesian]] (bayesian → control-theory)
- [structural-analogy] LSTD / Sherman–Morrison update ↔ control theory: recursive least squares and covariance-style updates — both maintain a matrix inverse recursively as data arrive. — from [[sutton-2018-rl/ch09-policy-p2]] (control-theory → control-theory)
