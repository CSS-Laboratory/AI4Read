---
id: iterated-ekf
type: concept
fields: [bayesian, control-theory]
fields_strong: [bayesian, control-theory]
n_sources: 2
n_works: 2
tiers: [deep, reference]
grounding: digests
sources: [murphy-2023-pml2/ch08-gaussian-p1, sarkka-2023-bayesianfiltering/ch07-extended]
generated_by: build_kg.py
---

# iterated-ekf

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch08-gaussian-p1]] (pp. 377–378): EKF with repeated re-linearization at the posterior; Gauss–Newton MAP [new; work fields: bayesian, control-theory]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch07-extended]] (p. 121): EKF whose update is repeated, re-linearising at the latest mean [new; work fields: control-theory, bayesian]

## Candidate bridges

- [structural-analogy] Iterated EKF ↔ optimization: Gauss–Newton for MAP, with the prior as a quadratic penalty (p. 378). — from [[murphy-2023-pml2/ch08-gaussian-p1]] (bayesian → other:optimization)
