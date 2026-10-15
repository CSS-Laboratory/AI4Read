---
id: rts-smoother
type: concept
fields: [control-theory, bayesian]
n_sources: 4
tiers: [deep, reference]
grounding: digests
sources: [murphy-2023-pml2/ch08-gaussian-p1, sarkka-2023-bayesianfiltering/ch01-are, sarkka-2023-bayesianfiltering/ch12-bayesian, sarkka-2023-bayesianfiltering/ch20-list]
generated_by: build_kg.py
---

# rts-smoother

## Definitions in the sources

### control-theory

- [[sarkka-2023-bayesianfiltering/ch01-are]] (p. 13): closed-form smoother for linear Gaussian models [new]
- [[sarkka-2023-bayesianfiltering/ch12-bayesian]] (p. 255): closed-form Kalman smoother for linear Gaussian models [new]
- [[sarkka-2023-bayesianfiltering/ch20-list]] (p. 394): named in 12.3, 12.4; no definition here [new]

### bayesian

- [[murphy-2023-pml2/ch08-gaussian-p1]] (p. 370): Kalman smoother using the backwards gain $J_t$ [new]

## Instances that use it

- [[rts-smoother-example]] — sine tracked more accurately by smoothing than by filtering — from [[sarkka-2023-bayesianfiltering/ch03-batch]]
- [[rts-smoother]] — entry 12.2 — from [[sarkka-2023-bayesianfiltering/ch21-list]]

## Candidate bridges

- [same-math] RTS smoother ↔ control-theory: fixed-interval Kalman smoothing of a whole record offline. The book itself calls the RTS smoother the Kalman smoother (p. 255). — from [[sarkka-2023-bayesianfiltering/ch12-bayesian]] (control-theory → control-theory)
- [structural-analogy] Reweighting smoother ↔ RTS smoother: both fold future information into the filter estimate, here as weights instead of Gaussian moments. — from [[sarkka-2023-bayesianfiltering/ch15-particle]] (control-theory → other)
