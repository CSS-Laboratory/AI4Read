---
id: pid-control
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 10
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch04-examples, astrom-2021-feedbacksystems/ch09-transfer-p2, astrom-2021-feedbacksystems/ch11-pid, astrom-2021-feedbacksystems/ch12-frequency, astrom-2021-feedbacksystems/ch15-architecture-p2, bertsekas-2026-rlcourse/ch01-exact-p5, bertsekas-2026-rlcourse/ch01-exact-p6]
raw_ids: [PID control]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# pid-control

## Canon spine entry

- **PID control** (control-theory): proportional (react to error), integral (remove lasting offset), derivative (anticipate trend) (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch01-introduction]] (p. 1-20): sum of proportional, integral and derivative terms, Eq. (1.5) [as `PID control`]
- [[astrom-2021-feedbacksystems/ch02-feedback]] (p. 2-29): the chapter treats PI control $u=k_pe+k_i\int e$ (p. 2-14); Exercise 2.7 (p. 2-29) asks for a PID design for a second-order process
- [[astrom-2021-feedbacksystems/ch03-system-p1]] (p. 3-17): the PI case: $u=k_pe+k_i\int e$, discretized in Example 3.6
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-4, p. 4-11, p. 4-18, p. 4-26): mostly the PI form: cruise control (4.4), the op-amp circuit, the AFM controller; the MiniMed 670G uses a PID algorithm
- [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (p. 9-30): Fig. 9.12 shows the Bode plot of an ideal PID [as `PID control`]
- [[astrom-2021-feedbacksystems/ch11-pid]] (p. 11-2): control signal as sum of P (present error), I (past errors), D (predicted error) terms, eq. (11.1) [as `PID control`]
- [[astrom-2021-feedbacksystems/ch12-frequency]] (p. 12-15): PI is a lag compensator, PD with filter a lead compensator
- [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (p. 15-40): the dominant controller in process industry
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (p. 109): three-parameter controller holding a single-input single-output system at a set point [as `PID control`]
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (p. 147): mentioned as applied in adaptive and robust control; Minorsky 1922 [as `PID control`]

## Candidate bridges

- [structural-analogy] Integral term of PID ↔ control-theory: disturbance observer on an augmented state $(x,w)$ with $w_{k+1}=w_k$ — the author calls the integral term the simplest instance of the idea of inferring a constant disturbance, and calls the MPC version "a similar strategy" (pp. 130–131). — from [[bertsekas-2026-rlcourse/ch01-exact-p5]] (control-theory → control-theory)
- [metaphor] "test the simple EKF first as a baseline" ↔ control practice of testing simple (e.g. PID) control before complex designs — from [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (control-theory → unspecified)
