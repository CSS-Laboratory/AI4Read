---
id: betancourt-2017-hmc/index
work: betancourt-2017-hmc
type: work-map
units: [betancourt-2017-hmc/main-p1, betancourt-2017-hmc/main-p2, betancourt-2017-hmc/main-p3]
---

# Betancourt, M. (2017). *A Conceptual Introduction to Hamiltonian Monte Carlo*. arXiv:1701.02434 (v2, 2018).

## In one paragraph
In high dimensions, expectations are dominated by a thin "typical set" that lies away from the mode. Samplers such as Random Walk Metropolis either have proposals rejected or move too slowly there. The gradient of the density alone points toward the mode, so it cannot guide a sampler along the typical set. Hamiltonian Monte Carlo adds auxiliary momentum, which turns the gradient into trajectories that follow the typical set. Its performance depends on three choices: the kinetic energy, the integration time, and the numerical integrator. The paper also shows how HMC fails. Divergences and low E-BFMI are measurable signals of high curvature and heavy tails. Together with split $\hat R$, they make failures interpretable. An appendix shows that the sampler is exact when trajectories are chosen reversibly.

## The path through the work
- [[betancourt-2017-hmc/main-p1]] — In high dimensions, expectations are dominated by a thin "typical set" away from the mode, so a sampler must glide coherently through that set, and the gradient of the density alone cannot guide it there.
- [[betancourt-2017-hmc/main-p2]] — Adding momentum as a dual variable makes the target's gradient generate trajectories along the typical set. How well these trajectories explore then depends on three choices: the kinetic energy, the integration time and the numerical integrator.
- [[betancourt-2017-hmc/main-p3]] — Hamiltonian Monte Carlo can be tuned using the geometry of its integrator, many of its failures show up as measurable diagnostics (divergences: unstable numerical trajectories; low E-BFMI: energy transitions much narrower than the overall energy spread), and a valid sampler needs trajectories chosen reversibly and states drawn with weights proportional to $e^{-H}$.

## Big ideas across units
- **Probability mass lives in the typical set, not at the mode.** Density is highest at the mode, but the volume there is tiny. The typical set narrows as dimension grows. Units: main-p1, main-p2, main-p3.
- **Naive samplers and the bare gradient are not enough.** Random Walk Metropolis scales poorly. The gradient points to the mode and is never aligned with the typical set. Units: main-p1, main-p2.
- **Momentum turns the gradient into motion along the typical set.** The canonical distribution and Hamiltonian $H=K+V$ give trajectories on energy level sets. A transition is a random lift, a deterministic trajectory, and a projection. Units: main-p1 (the physics analogy), main-p2.
- **Exploration quality comes from tuning geometry.** The kinetic energy (mass matrix) should make level sets uniform and match the energy transition distribution to the marginal energy distribution. The integration time should be chosen dynamically, for example with the No-U-Turn criterion. Units: main-p2, main-p3 (generalized No-U-Turn).
- **Symplectic integrators and Metropolis–Hastings correction keep the sampler honest.** They avoid drift. A momentum flip makes the proposal reversible, so the correction is possible. The modified (shadow) Hamiltonian links step size to acceptance. Units: main-p2, main-p3.
- **Failures become diagnostics.** Divergences flag high curvature, low E-BFMI flags heavy tails, and split $\hat R$ flags stuck chains. These are necessary but not sufficient for validity. Units: main-p1, main-p2, main-p3.
- **Geometric ergodicity is the robustness question.** It asks when estimators are well behaved and unbiased. Heavy tails and high curvature obstruct it. Units: main-p1, main-p3.
- **Correct, efficient implementation rests on reversibility.** Choosing trajectories reversibly and drawing states with weights $\propto e^{-H}$ preserves the target. Progressive and doubling schemes make this cheap. Units: main-p2, main-p3.

## How to read it
- Read main-p1 first. It builds the typical set, MCMC and the failure of Random Walk Metropolis. Everything later depends on it.
- main-p2 is the core of the method: momentum, the Hamiltonian, tuning, integrators and the correction. It depends on main-p1.
- main-p3 depends on main-p2 (its prerequisites are the Hamiltonian, level sets and symplectic integrators). Its diagnostics sections (divergences, E-BFMI) are essential for practical use.
- On a first pass, the appendix material in main-p3 can be skipped. This covers the proof of invariance, progressive sampling, and the generalized No-U-Turn rule. It matters for implementation details rather than for the conceptual story.

## Concepts introduced
- [[typical-set]] — main-p1
- [[markov-chain-monte-carlo]] — main-p1
- [[metropolis-hastings]] — main-p1
- [[convergence-diagnostics]] — main-p1
- [[monte-carlo-integration]] — main-p1
- [[concentration-of-measure]] — main-p1
- [[effective-sample-size]] — main-p1
- [[warm-up]] — main-p1
- [[geometric-ergodicity]] — main-p1
- [[random-walk-metropolis]] — main-p1
- [[hamiltonian-monte-carlo]] — main-p2
- [[phase-space]] — main-p2
- [[canonical-distribution]] — main-p2
- [[hamiltonian-function]] — main-p2
- [[kinetic-energy-mass-matrix]] — main-p2
- [[microcanonical-decomposition]] — main-p2
- [[dynamic-ergodicity]] — main-p2
- [[no-u-turn-criterion]] — main-p2
- [[symplectic-integrator]] — main-p2
- [[momentum-flip-reversibility]] — main-p2
- [[shadow-hamiltonian]] — main-p3
- [[e-bfmi]] — main-p3
- [[progressive-sampling]] — main-p3
- [[trajectory-reversibility-condition]] — main-p3
