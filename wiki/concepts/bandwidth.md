---
id: bandwidth
type: concept
fields: [control-theory, information-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch02-feedback, pierce-1980-introduction/ch02-origins]
generated_by: build_kg.py
---

# bandwidth

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch02-feedback]] (p. 2-18): $\omega_c$ bounds the reference frequencies tracked with small error [new]

### information-theory

- [[pierce-1980-introduction/ch02-origins]] (p. 38): the range (band) of frequencies used; speed is proportional to it [new]

## Instances that use it

- [[op-amp-feedback-circuit]] — dynamic op amp gives closed-loop $G$, gain $\approx-R_2/R_1$, bandwidth $\approx aR_1k/R_2$ — from [[astrom-2021-feedbacksystems/ch09-transfer-p1]]
- [[jet-engine-rotating-stall]] — feedback not feasible for lack of actuator bandwidth; alleviated instead by small turbine asymmetries — from [[astrom-2021-feedbacksystems/ch15-architecture-p1]]
- [[gaussian-mac-fdm]] — frequency division touches the capacity boundary only at the point where bandwidths are proportional to powers — from [[cover-2006-elements/ch14-network-p2]]
- [[bandwidth-4mc-example]] — W = 4 Mc/s, P/N = 1,000, C = 40,000,000 bits/s — from [[pierce-1980-introduction/ch09-many]]

## Candidate bridges

- [structural-analogy] $S+T=1$ and the cost of high bandwidth ↔ signal processing: a trade-off between passing signal and passing noise. Both are "pass band versus noise" constraints. — from [[astrom-2021-feedbacksystems/ch12-frequency]] (control-theory → other)
- [structural-analogy] RHP pole needs high bandwidth, RHP zero needs low bandwidth ↔ balancing a stick: the shorter the stick the faster the reaction needed, and delay limits it (the unit compares the X-29 dynamics to an inverted pendulum and treats the cart–pendulum balance system in Ex. 14.7). — from [[astrom-2021-feedbacksystems/ch14-fundamental]] (control-theory → other)
- [same-math] Eq. (20.8) GMM on training points ↔ KDE (20.1) with a Gaussian kernel — same form, bandwidth $\epsilon$. — from [[murphy-2023-pml2/ch20-generative]] (bayesian → unspecified)
- [structural-analogy] Shutter/filter trade-off: short wavetrain versus narrow momentum range ↔ signal processing: time–bandwidth trade-off — both involve sums of waves, but the source gives no formulas. — from [[popper-1959-logic/appvi-untitled]] (analytic-philosophy → other)
