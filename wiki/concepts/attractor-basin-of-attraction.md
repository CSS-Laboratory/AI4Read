---
id: attractor-basin-of-attraction
type: concept
fields: [complex-systems, bayesian, information-theory, llm]
fields_strong: [complex-systems, bayesian, information-theory, llm]
n_sources: 14
n_works: 7
tiers: [core, reference]
grounding: digests
sources: [bak-1987-soc/main, lorenz-1963-nonperiodic/main, mackay-2003-information/ch42-hopfield, mitchell-2009-guidedtour/ch02-dynamics, mitchell-2009-guidedtour/ch18-evolution, scheffer-2009-earlywarning/main, schelling-1971-segregation/main-p2, strogatz-2024-nonlinear/ch05-linear, strogatz-2024-nonlinear/ch06-phase-p1, strogatz-2024-nonlinear/ch08-bifurcations-p1, strogatz-2024-nonlinear/ch09-lorenz-p1, strogatz-2024-nonlinear/ch09-lorenz-p2, strogatz-2024-nonlinear/ch10-one-p1, strogatz-2024-nonlinear/ch12-strange]
aliases: [attractor-basin, basin-of-attraction]
raw_ids: [attractor / basin of attraction]
canon_spine: [complex-systems]
generated_by: build_kg.py
---

# attractor-basin-of-attraction

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `attractor-basin` — 3 digest(s)
- `basin-of-attraction` — 1 digest(s)

## Canon spine entry

- **attractor / basin of attraction** (complex-systems): the set the dynamics settle onto, and the initial states that lead there (UG)

## Definitions in the sources

### complex-systems

- [[bak-1987-soc/main]] (p. 381): the critical state is an attractor reached from far from equilibrium [as `attractor / basin of attraction`]
- [[lorenz-1963-nonperiodic/main]] (p. 135): the ultimate set approached by trajectories. Here it is a zero-volume subspace holding all central trajectories; Lorenz does not use the word "attractor" (canon link; not stated in this unit) [as `attractor / basin of attraction`; weak: not really used in this unit]
- [[mitchell-2009-guidedtour/ch02-dynamics]] (pdf 50): regular final behaviour (fixed point or oscillation) that initial conditions are "attracted to" (pdf 50). Only the attractor half is covered here. [as `attractor / basin of attraction`]
- [[mitchell-2009-guidedtour/ch18-evolution]] (p. 161): Kauffman's term for the repeating cycle of global states of an RBN; basins not discussed [as `attractor / basin of attraction`]
- [[scheffer-2009-earlywarning/main]] (p. Box 1, p. 54): stable state and the set of states leading to it; the unstable equilibrium is the border [as `attractor / basin of attraction`]
- [[schelling-1971-segregation/main-p2]] (p. 20): initial conditions and relative speeds decide which stable equilibrium is reached [as `attractor / basin of attraction`]
- [[strogatz-2024-nonlinear/ch05-linear]] (p. 130): only touched on (global attraction of the origin in Fig. 5.1.5a–c) [alias `attractor-basin`]
- [[strogatz-2024-nonlinear/ch06-phase-p1]] (p. 159): here basin of an attracting fixed point: the set of initial conditions flowing to it
- [[strogatz-2024-nonlinear/ch08-bifurcations-p1]] (p. 248): the saddle's stable manifold separates the basins of two sinks [alias `attractor-basin`]
- [[strogatz-2024-nonlinear/ch09-lorenz-p1]] (pp. 331–332): closed, invariant, attracts an open set, minimal [as `attractor / basin of attraction`]
- [[strogatz-2024-nonlinear/ch09-lorenz-p2]] (p. 333): an attracting set must also be minimal; an attracting set can contain smaller attractors [as `attractor / basin of attraction`]
- [[strogatz-2024-nonlinear/ch10-one-p1]] (p. 374): $\lambda$ is the same across one basin of attraction [alias `attractor-basin`]
- [[strogatz-2024-nonlinear/ch12-strange]] (pp. 433, 453): set approached by orbits, and its set of initial conditions; basin boundaries can be fractal [as `attractor / basin of attraction`]

### information-theory

- [[mackay-2003-information/ch42-hopfield]] (p. 508): set of initial states flowing to a given attractor [alias `basin-of-attraction`; new; work fields: information-theory, bayesian, llm]

## Candidate bridges

- [structural-analogy] region of stability = region of convergence of Newton's method ↔ dynamical systems: basin of attraction of a fixed point. — from [[bertsekas-2026-rlcourse/ch01-exact-p3]] (control-theory → complex-systems)
- [structural-analogy] stable equilibria from curve intersections ↔ dynamical systems: fixed points and basins of attraction — the same picture of several stable states, with initial conditions choosing. — from [[schelling-1971-segregation/main-p2]] (complex-systems → complex-systems)
