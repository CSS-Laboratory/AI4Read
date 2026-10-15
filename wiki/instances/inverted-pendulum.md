---
id: inverted-pendulum
type: instance
fields: [control-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch05-dynamic, astrom-2021-feedbacksystems/ch10-frequency]
generated_by: build_kg.py
---

# inverted-pendulum

## Descriptions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch05-dynamic]] (pp. 5-6, 5-14, 5-27): open-loop unstable upright equilibrium; stabilized by a Lyapunov-based law plus Krasovski–Lasalle
- [[astrom-2021-feedbacksystems/ch10-frequency]] (p. 10-13): PD control stable only for $k>0.5$ ($Z=N+P=0$)

## Candidate bridges

- [structural-analogy] RHP pole needs high bandwidth, RHP zero needs low bandwidth ↔ balancing a stick: the shorter the stick the faster the reaction needed, and delay limits it (the unit compares the X-29 dynamics to an inverted pendulum and treats the cart–pendulum balance system in Ex. 14.7). — from [[astrom-2021-feedbacksystems/ch14-fundamental]] (control-theory → other)
