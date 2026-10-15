---
id: state-space-phase-space
type: concept
fields: [complex-systems, bayesian, control-theory]
fields_strong: [complex-systems, bayesian, control-theory]
n_sources: 11
n_works: 4
tiers: [core, deep, reference]
grounding: digests
sources: [ashby-1956-cybernetics/ch03-determinate, betancourt-2017-hmc/main-p2, lorenz-1963-nonperiodic/main, strogatz-2024-nonlinear/ch01-overview, strogatz-2024-nonlinear/ch02-flows, strogatz-2024-nonlinear/ch03-bifurcations-p1, strogatz-2024-nonlinear/ch05-linear, strogatz-2024-nonlinear/ch06-phase-p1, strogatz-2024-nonlinear/ch06-phase-p2, strogatz-2024-nonlinear/ch07-limit-p1, strogatz-2024-nonlinear/ch09-lorenz-p1]
aliases: [phase-space]
raw_ids: [state space / phase space]
canon_spine: [complex-systems]
generated_by: build_kg.py
---

# state-space-phase-space

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `phase-space` — 3 digest(s)

## Canon spine entry

- **state space / phase space** (complex-systems): the space of all possible system states, where dynamics are trajectories (UG)

## Definitions in the sources

### complex-systems

- [[lorenz-1963-nonperiodic/main]] (p. 131): $M$-dimensional space whose points are states and whose curves are trajectories [as `state space / phase space`]
- [[strogatz-2024-nonlinear/ch01-overview]] (pp. 7–8): space with coordinates $x_1,\dots,x_n$; each point is a state, each trajectory a solution; $n$ is its dimension [as `state space / phase space`]
- [[strogatz-2024-nonlinear/ch02-flows]] (p. 19): here the real line, with the "phase fluid" flowing on it [as `state space / phase space`]
- [[strogatz-2024-nonlinear/ch03-bifurcations-p1]] (p. 68): here the phase plane $(\phi,\Omega)$ for second-order systems
- [[strogatz-2024-nonlinear/ch05-linear]] (pp. 126–127): here the phase plane, with state $(x,v)$ or $(x,y)$ and solutions drawn as trajectories
- [[strogatz-2024-nonlinear/ch06-phase-p1]] (p. 146): here the phase plane: points $(x_1,x_2)$ with $\dot{\mathbf x}$ as the velocity vector; trajectories fill it [alias `phase-space`]
- [[strogatz-2024-nonlinear/ch06-phase-p2]] (p. 175): the phase plane, where index curves are drawn as probes, not necessarily trajectories [as `state space / phase space`]
- [[strogatz-2024-nonlinear/ch07-limit-p1]] (p. 205–206): the plane, with trajectories, nullclines and trapping regions [as `state space / phase space`]
- [[strogatz-2024-nonlinear/ch09-lorenz-p1]] (p. 309, p. 320): space in which trajectories and volume evolution are studied [as `state space / phase space`]

### bayesian

- [[betancourt-2017-hmc/main-p2]] (p. 23): $2D$-dimensional space of positions and dual momenta, where volume is preserved [alias `phase-space`; new]

### control-theory

- [[ashby-1956-cybernetics/ch03-determinate]] (pp. 37–38): the plane or space where states are points and the transformation is drawn as arrows [alias `phase-space`; new]

## Candidate bridges

- [structural-analogy] Phase space with arrow field ↔ control-theory: phase portrait / vector field of a dynamical system. — from [[ashby-1956-cybernetics/ch03-determinate]] (control-theory → control-theory)
- [structural-analogy] Level-set foliation of phase space ↔ bayesian: marginal energy distribution as a one-dimensional summary of the joint, with trajectories moving within and resampling moving across. — from [[betancourt-2017-hmc/main-p2]] (bayesian → bayesian)
- [same-math] $H=-\sum p_i\log p_i$ ↔ statistical mechanics: entropy over cells of phase space, Boltzmann's $H$ — the author notes the same form (p. 11) — from [[shannon-1948-mathematical/main-p1]] (information-theory → complex-systems)
