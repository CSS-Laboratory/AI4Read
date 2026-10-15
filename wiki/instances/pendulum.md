---
id: pendulum
type: instance
fields: [complex-systems]
n_sources: 3
tiers: [core]
grounding: digests
sources: [strogatz-2024-nonlinear/ch01-overview, strogatz-2024-nonlinear/ch06-phase-p1, strogatz-2024-nonlinear/ch07-limit-p2]
generated_by: build_kg.py
---

# pendulum

## Descriptions in the sources

### complex-systems

- [[strogatz-2024-nonlinear/ch01-overview]] (pp. 6–7): nonlinear, $n=2$; small-angle fudge vs geometric treatment
- [[strogatz-2024-nonlinear/ch06-phase-p1]] (pp. 169–173): undamped: librations, rotations, cylindrical phase space; damped: spirals and falling energy [new]
- [[strogatz-2024-nonlinear/ch07-limit-p2]] (p. 229): named as the example of a softening spring

## Candidate bridges

- [structural-analogy] Adding angular velocity to make the pendulum single-valued ↔ control-theory: state must include all variables needed to predict the future (state concept). — from [[ashby-1956-cybernetics/ch03-determinate]] (control-theory → control-theory)
- [structural-analogy] RHP pole needs high bandwidth, RHP zero needs low bandwidth ↔ balancing a stick: the shorter the stick the faster the reaction needed, and delay limits it (the unit compares the X-29 dynamics to an inverted pendulum and treats the cart–pendulum balance system in Ex. 14.7). — from [[astrom-2021-feedbacksystems/ch14-fundamental]] (control-theory → other)
- [same-math] Nonuniform oscillator ↔ overdamped pendulum with constant torque — the same equation after nondimensionalizing. — from [[strogatz-2024-nonlinear/ch04-flows]] (complex-systems → unspecified)
