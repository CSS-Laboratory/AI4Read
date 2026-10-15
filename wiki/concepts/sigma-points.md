---
id: sigma-points
type: concept
fields: [control-theory]
n_sources: 2
tiers: [deep]
grounding: digests
sources: [sarkka-2023-bayesianfiltering/ch08-general, sarkka-2023-bayesianfiltering/ch14-general]
generated_by: build_kg.py
---

# sigma-points

## Definitions in the sources

### control-theory

- [[sarkka-2023-bayesianfiltering/ch08-general]] (p. 137): evaluation points of a numerical integration rule, used to propagate a Gaussian [new]
- [[sarkka-2023-bayesianfiltering/ch14-general]] (pp. 281–289): Deterministic points and weights approximating Gaussian integrals: GH, cubature, UT, fifth order [new]

## Candidate bridges

- [metaphor] Sigma points ↔ a small survey sample chosen deterministically to reproduce known moments of a population. — from [[murphy-2023-pml2/ch08-gaussian-p2]] (bayesian → unspecified)
- [structural-analogy] Sigma-point propagation (UKF) ↔ control-theory: Kalman filter prediction/correction with non-linear dynamics; the Kalman filter is replaced by $\mathbf K=\mathbf C\mathbf S^{-1}$ built from integral-based moments. — from [[sarkka-2023-bayesianfiltering/ch08-general]] (control-theory → control-theory)
