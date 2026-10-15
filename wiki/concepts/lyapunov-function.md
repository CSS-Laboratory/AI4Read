---
id: lyapunov-function
type: concept
fields: [information-theory, control-theory]
n_sources: 3
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch05-dynamic, mackay-2003-information/ch20-example, mackay-2003-information/ch42-hopfield]
generated_by: build_kg.py
---

# lyapunov-function

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch20-example]] (p. 287): a bounded-below function of the state that decreases at every change; guarantees convergence [new]
- [[mackay-2003-information/ch42-hopfield]] (p. 508): function that decreases along the dynamics and is bounded below; implies settling to a fixed point or limit cycle, no chaos [new]

### control-theory

- [[astrom-2021-feedbacksystems/ch05-dynamic]] (p. 5-19): energy-like $V$ with $V>0$, $\dot V\le0$ (or $<0$) near equilibrium [new]

## Instances that use it

- [[noise-cancelling-headphones]] — adaptive nonlinear feedback from a Lyapunov function — from [[astrom-2021-feedbacksystems/ch05-dynamic]]

## Candidate bridges

- [structural-analogy] Lyapunov function $V$ ↔ physics: total energy with dissipation — $\dot V\le0$ plays the role of energy loss (p. 5-18). — from [[astrom-2021-feedbacksystems/ch05-dynamic]] (control-theory → other)
- [same-math] $\hat V=x^TPx$ decreasing along trajectories ↔ stability theory: Lyapunov function; the author calls this the "Lyapunov argument" (p. 156, 160). — from [[liberzon-2012-calculus/ch06-linear]] (control-theory → other)
