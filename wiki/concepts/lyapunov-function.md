---
id: lyapunov-function
type: concept
fields: [complex-systems, bayesian, information-theory, control-theory, llm]
fields_strong: [complex-systems, bayesian, information-theory, control-theory, llm]
n_sources: 6
n_works: 3
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch05-dynamic, mackay-2003-information/ch20-example, mackay-2003-information/ch42-hopfield, strogatz-2024-nonlinear/ch07-limit-p1, strogatz-2024-nonlinear/ch09-lorenz-p1, strogatz-2024-nonlinear/ch09-lorenz-p2]
aliases: [liapunov-function]
generated_by: build_kg.py
---

# lyapunov-function

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `liapunov-function` — 3 digest(s)

## Definitions in the sources

### complex-systems

- [[strogatz-2024-nonlinear/ch07-limit-p1]] (p. 203): positive definite $V$ with $\dot V<0$ away from $\mathbf x^*$ [alias `liapunov-function`; new]
- [[strogatz-2024-nonlinear/ch09-lorenz-p1]] (p. 323): positive definite function decreasing along trajectories; proves global stability of origin for r < 1 [alias `liapunov-function`; new]
- [[strogatz-2024-nonlinear/ch09-lorenz-p2]] (p. 347): a positive-definite function that decreases along trajectories, proving global stability [alias `liapunov-function`; new]

### information-theory

- [[mackay-2003-information/ch20-example]] (p. 287): a bounded-below function of the state that decreases at every change; guarantees convergence [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch42-hopfield]] (p. 508): function that decreases along the dynamics and is bounded below; implies settling to a fixed point or limit cycle, no chaos [new; work fields: information-theory, bayesian, llm]

### control-theory

- [[astrom-2021-feedbacksystems/ch05-dynamic]] (p. 5-19): energy-like $V$ with $V>0$, $\dot V\le0$ (or $<0$) near equilibrium [new]

## Instances that use it

- [[noise-cancelling-headphones]] — adaptive nonlinear feedback from a Lyapunov function — from [[astrom-2021-feedbacksystems/ch05-dynamic]]

## Candidate bridges

- [structural-analogy] Lyapunov function $V$ ↔ physics: total energy with dissipation — $\dot V\le0$ plays the role of energy loss (p. 5-18). — from [[astrom-2021-feedbacksystems/ch05-dynamic]] (control-theory → other:physics)
- [same-math] $\hat V=x^TPx$ decreasing along trajectories ↔ stability theory: Lyapunov function; the author calls this the "Lyapunov argument" (p. 156, 160). — from [[liberzon-2012-calculus/ch06-linear]] (control-theory → other:stability-theory)
- [structural-analogy] Liapunov function / gradient potential ↔ optimisation: a loss function that decreases along update steps rules out cycling — both use a strictly decreasing quantity to forbid loops. — from [[strogatz-2024-nonlinear/ch07-limit-p1]] (complex-systems → other:optimization)
