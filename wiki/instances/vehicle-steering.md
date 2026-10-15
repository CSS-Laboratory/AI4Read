---
id: vehicle-steering
type: instance
fields: [control-theory]
n_sources: 8
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch03-system-p2, astrom-2021-feedbacksystems/ch06-linear, astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch08-output, astrom-2021-feedbacksystems/ch09-transfer-p1, astrom-2021-feedbacksystems/ch10-frequency, astrom-2021-feedbacksystems/ch12-frequency, astrom-2021-feedbacksystems/ch14-fundamental]
generated_by: build_kg.py
---

# vehicle-steering

## Descriptions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch03-system-p2]] (p. 3-30): bicycle model, Dubins car
- [[astrom-2021-feedbacksystems/ch06-linear]] (p. 6-32): linearized lateral dynamics with single parameter $\gamma=a/b$
- [[astrom-2021-feedbacksystems/ch07-state]] (p. 7-11): $k_1=\omega_c^2$, $k_2=2\zeta_c\omega_c-\gamma\omega_c^2$
- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-10, 8-14, 8-25, 8-28): observer (Ex. 8.3), output feedback (Ex. 8.4), lane-change trajectory (Ex. 8.8), velocity-scheduled steering (Ex. 8.10)
- [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (p. 9-21, 9-22): observer-based controller as transfer functions; $G_{yr}$ independent of $l_1,l_2$
- [[astrom-2021-feedbacksystems/ch10-frequency]] (p. 10-20 to 10-22): reverse driving gives a non-minimum-phase zero and inverse response
- [[astrom-2021-feedbacksystems/ch12-frequency]] (p. 12-19): feedforward lane change with $F_r=F_m/P$
- [[astrom-2021-feedbacksystems/ch14-fundamental]] (p. 14-4, 14-22): output placement removes a RHP zero (Ex. 14.1); slow-zero cancellation fixes a fragile design (Ex. 14.12)
