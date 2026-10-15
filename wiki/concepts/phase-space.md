---
id: phase-space
type: concept
fields: [bayesian, complex-systems, control-theory]
n_sources: 3
tiers: [core, deep]
grounding: digests
sources: [ashby-1956-cybernetics/ch03-determinate, betancourt-2017-hmc/main-p2, strogatz-2024-nonlinear/ch06-phase-p1]
generated_by: build_kg.py
---

# phase-space

## Definitions in the sources

### bayesian

- [[betancourt-2017-hmc/main-p2]] (p. 23): $2D$-dimensional space of positions and dual momenta, where volume is preserved [new]

### complex-systems

- [[strogatz-2024-nonlinear/ch06-phase-p1]] (p. 146): here the phase plane: points $(x_1,x_2)$ with $\dot{\mathbf x}$ as the velocity vector; trajectories fill it

### control-theory

- [[ashby-1956-cybernetics/ch03-determinate]] (pp. 37–38): the plane or space where states are points and the transformation is drawn as arrows [new]

## Instances that use it

- [[pendulum]] — undamped: librations, rotations, cylindrical phase space; damped: spirals and falling energy — from [[strogatz-2024-nonlinear/ch06-phase-p1]]

## Candidate bridges

- [structural-analogy] Phase space with arrow field ↔ control-theory: phase portrait / vector field of a dynamical system. — from [[ashby-1956-cybernetics/ch03-determinate]] (control-theory → control-theory)
- [structural-analogy] Level-set foliation of phase space ↔ bayesian: marginal energy distribution as a one-dimensional summary of the joint, with trajectories moving within and resampling moving across. — from [[betancourt-2017-hmc/main-p2]] (bayesian → bayesian)
- [same-math] $H=-\sum p_i\log p_i$ ↔ statistical mechanics: entropy over cells of phase space, Boltzmann's $H$ — the author notes the same form (p. 11) — from [[shannon-1948-mathematical/main-p1]] (information-theory → complex-systems)
