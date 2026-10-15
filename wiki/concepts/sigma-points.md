---
id: sigma-points
type: concept
fields: [bayesian, control-theory]
fields_strong: [bayesian, control-theory]
n_sources: 3
n_works: 1
tiers: [deep]
grounding: digests
sources: [sarkka-2023-bayesianfiltering/ch01-symbols, sarkka-2023-bayesianfiltering/ch08-general, sarkka-2023-bayesianfiltering/ch14-general]
aliases: [sigma-point]
generated_by: build_kg.py
---

# sigma-points

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `sigma-point` — 1 digest(s)

## Definitions in the sources

### control-theory

- [[sarkka-2023-bayesianfiltering/ch01-symbols]] (pp. xxvi–xxvii): points such as $\mathcal X^{(i)}$, with weights $W_i$ [alias `sigma-point`; new; work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch08-general]] (p. 137): evaluation points of a numerical integration rule, used to propagate a Gaussian [new; work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch14-general]] (pp. 281–289): Deterministic points and weights approximating Gaussian integrals: GH, cubature, UT, fifth order [new; work fields: control-theory, bayesian]

## Candidate bridges

- [metaphor] Sigma points ↔ a small survey sample chosen deterministically to reproduce known moments of a population. — from [[murphy-2023-pml2/ch08-gaussian-p2]] (bayesian → unspecified)
- [structural-analogy] Sigma-point propagation (UKF) ↔ control-theory: Kalman filter prediction/correction with non-linear dynamics; the Kalman filter is replaced by $\mathbf K=\mathbf C\mathbf S^{-1}$ built from integral-based moments. — from [[sarkka-2023-bayesianfiltering/ch08-general]] (control-theory → control-theory)
