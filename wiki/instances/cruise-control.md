---
id: cruise-control
type: instance
fields: [control-theory]
n_sources: 9
tiers: [core, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch04-examples, astrom-2021-feedbacksystems/ch06-linear, astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch09-transfer-p2, astrom-2021-feedbacksystems/ch11-pid, astrom-2021-feedbacksystems/ch12-frequency, astrom-2021-feedbacksystems/ch13-robust, bertsekas-2026-rlcourse/ch01-exact-p6]
canon_instance: [cruise-control-pi]
canon_match_rule: alias
generated_by: build_kg.py
---

# cruise-control

## Canon entry

- **Cruise control (PI)** (control-theory): a car holds speed up and down hills; integral action removes the steady-state error that pure proportional control leaves — astrom-2021-feedbacksystems

## Descriptions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch01-introduction]] (pp. 1-14, 1-21): PI speed control robust to road slope and mass; mode logic via state machine
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-3, p. 4-4): first-order nonlinear plant with PI feedback; hill response
- [[astrom-2021-feedbacksystems/ch06-linear]] (pp. 6-29, 6-33): linearization validated on hills; feedback linearization example
- [[astrom-2021-feedbacksystems/ch07-state]] (p. 7-25): integral action rejects hill disturbance
- [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (p. 9-28): PI design cancelling the process pole; slow mode remains
- [[astrom-2021-feedbacksystems/ch11-pid]] (p. 11-9, 11-15, 11-20): PI design by pole placement; windup on a steep hill; setpoint weighting
- [[astrom-2021-feedbacksystems/ch12-frequency]] (p. 12-2): slope changes as load disturbance, shaft-pulse electronics as noise
- [[astrom-2021-feedbacksystems/ch13-robust]] (p. 13-2, 13-11): PI controller robust to mass, gear, speed variations; bound with $M_t=1.17$
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (pp. 153, 158–159): exercise settings
