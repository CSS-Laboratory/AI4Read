---
id: limit-cycle
type: concept
fields: [complex-systems, control-theory]
fields_strong: [complex-systems, control-theory]
n_sources: 10
n_works: 2
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch04-examples, astrom-2021-feedbacksystems/ch05-dynamic, strogatz-2024-nonlinear/ch01-overview, strogatz-2024-nonlinear/ch07-limit-p1, strogatz-2024-nonlinear/ch07-limit-p2, strogatz-2024-nonlinear/ch08-bifurcations-p1, strogatz-2024-nonlinear/ch08-bifurcations-p2, strogatz-2024-nonlinear/ch08-bifurcations-p3, strogatz-2024-nonlinear/ch09-lorenz-p2, strogatz-2024-nonlinear/ch12-strange]
raw_ids: [limit cycle]
canon_spine: [complex-systems]
generated_by: build_kg.py
---

# limit-cycle

## Canon spine entry

- **limit cycle** (complex-systems): an isolated periodic orbit, as in self-sustained oscillation (UG)

## Definitions in the sources

### complex-systems

- [[strogatz-2024-nonlinear/ch01-overview]] (p. 10): listed among $n=2$ nonlinear phenomena in Figure 1.3.1; not defined here [as `limit cycle`; weak: not really used in this unit]
- [[strogatz-2024-nonlinear/ch07-limit-p1]] (p. 198): isolated closed trajectory; stable if neighbours approach it [as `limit cycle`]
- [[strogatz-2024-nonlinear/ch07-limit-p2]] (pp. 217, 225): here, a closed trajectory that nearby spiralling trajectories approach: van der Pol's stable cycle of radius $2+O(\varepsilon)$ [as `limit cycle`]
- [[strogatz-2024-nonlinear/ch08-bifurcations-p1]] (pp. 252, 256): isolated closed orbit; the cycle is born at a Hopf bifurcation
- [[strogatz-2024-nonlinear/ch08-bifurcations-p2]] (p. 270): isolated closed orbit; here existence proved with a Poincaré map
- [[strogatz-2024-nonlinear/ch08-bifurcations-p3]] (pp. 292–296): a periodic orbit whose existence and bifurcations are probed in the chemical, ecological and neural models
- [[strogatz-2024-nonlinear/ch09-lorenz-p2]] (p. 337): closed orbit; all cycles of the Lorenz map are unstable if $|f'|>1$ everywhere [as `limit cycle`]
- [[strogatz-2024-nonlinear/ch12-strange]] (pp. 446, 450): periodic attractors in the double-well simulations; reconstructed in the sin example [as `limit cycle`]

### control-theory

- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-28): the oscillation in the predator–prey simulation (caption of Fig. 4.20) [new]
- [[astrom-2021-feedbacksystems/ch05-dynamic]] (p. 5-7): nonconstant periodic solution that nearby trajectories approach (stable) or leave (unstable) [new]

## Instances that use it

- [[predator-prey]] — stability diagram, bifurcation, limit cycle — from [[astrom-2021-feedbacksystems/ch05-dynamic]]
- [[relay-with-hysteresis]] — describing-function prediction of limit cycle amplitude and frequency — from [[astrom-2021-feedbacksystems/ch10-frequency]]
- [[van-der-pol-oscillator]] — nonlinear damping gives a unique stable limit cycle; for $\mu=1.5$ it is not a circle, and for $\mu\gg1$ it is a relaxation oscillation with $T\approx\mu(3-2\ln2)$ — from [[strogatz-2024-nonlinear/ch07-limit-p1]]
- [[simple-polar-limit-cycle]] — $\dot r=r(1-r^2),\ \dot\theta=1$ — from [[strogatz-2024-nonlinear/ch07-limit-p1]]
- [[van-der-pol-oscillator]] — weakly nonlinear case: near-circular stable limit cycle, radius $2+O(\varepsilon)$, transient (56) — from [[strogatz-2024-nonlinear/ch07-limit-p2]]
- [[damped-pendulum-degenerate-hopf]] — μ = 0 gives a band of closed orbits, not limit cycles — from [[strogatz-2024-nonlinear/ch08-bifurcations-p1]]

## Candidate bridges

- [structural-analogy] Predator–prey oscillation ↔ the damped-oscillation modes of spring–mass systems — both give oscillating time responses, but the predator–prey system is nonlinear and the chapter calls its oscillation a limit cycle. — from [[astrom-2021-feedbacksystems/ch04-examples]] (control-theory → unspecified)
- [structural-analogy] Predator–prey cycle (a stable limit cycle when the equilibrium is unstable) ↔ cyclical dynamics in economics or epidemics. — from [[astrom-2021-feedbacksystems/ch05-dynamic]] (control-theory → unspecified)
- [structural-analogy] policy chattering in approximate PI ↔ control theory: limit cycles in a loop with nonlinearity (p. 387) — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → control-theory)
- [metaphor] Amplitude equation with a stable nonzero fixed point ↔ complex-systems: attractor — the limit cycle appears as a fixed point of $r$. — from [[strogatz-2024-nonlinear/ch07-limit-p2]] (complex-systems → complex-systems)
