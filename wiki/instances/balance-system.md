---
id: balance-system
type: instance
fields: [control-theory]
n_sources: 3
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch03-system-p2, astrom-2021-feedbacksystems/ch14-fundamental]
canon_instance: [inverted-pendulum-on-a-cart]
canon_match_rule: confirmed
generated_by: build_kg.py
---

# balance-system

## Canon entry

- **Inverted pendulum on a cart** (control-theory): an unstable system made stable by fast state feedback; the standard demonstration of controllability, LQR and Kalman filtering — brunton-2017-controlbootcamp

## Descriptions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch03-system-p1]] (pp. 3-12 to 3-14): cart–pendulum with nonlinear (3.9) and linearized models; inverted pendulum (3.10)
- [[astrom-2021-feedbacksystems/ch03-system-p2]] (p. 3-29): scaling from 5 to 2 parameters
- [[astrom-2021-feedbacksystems/ch14-fundamental]] (p. 14-14, 14-28): cart-position output has $p=2.68$, $z=2.09$, hard to control; friction-induced oscillations (Ex. 14.7, 14.14)

## Candidate bridges

- [structural-analogy] RHP pole needs high bandwidth, RHP zero needs low bandwidth ↔ balancing a stick: the shorter the stick the faster the reaction needed, and delay limits it (the unit compares the X-29 dynamics to an inverted pendulum and treats the cart–pendulum balance system in Ex. 14.7). — from [[astrom-2021-feedbacksystems/ch14-fundamental]] (control-theory → other:balancing-a-stick)
