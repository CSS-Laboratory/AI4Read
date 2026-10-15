---
id: bifurcation
type: concept
fields: [complex-systems, control-theory]
fields_strong: [complex-systems, control-theory]
n_sources: 18
n_works: 7
tiers: [core, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch05-dynamic, castellano-2009-socialdynamics/main-p3, granovetter-1978-threshold/main, lorenz-1963-nonperiodic/main, mitchell-2009-guidedtour/ch02-dynamics, scheffer-2009-earlywarning/main, strogatz-2024-nonlinear/ch01-overview, strogatz-2024-nonlinear/ch02-flows, strogatz-2024-nonlinear/ch03-bifurcations-p1, strogatz-2024-nonlinear/ch03-bifurcations-p2, strogatz-2024-nonlinear/ch06-phase-p2, strogatz-2024-nonlinear/ch08-bifurcations-p1, strogatz-2024-nonlinear/ch08-bifurcations-p2, strogatz-2024-nonlinear/ch08-bifurcations-p3, strogatz-2024-nonlinear/ch09-lorenz-p1, strogatz-2024-nonlinear/ch09-lorenz-p2, strogatz-2024-nonlinear/ch10-one-p1, strogatz-2024-nonlinear/ch10-one-p2]
canon_spine: [complex-systems]
generated_by: build_kg.py
---

# bifurcation

## Canon spine entry

- **bifurcation** (complex-systems): a qualitative change in dynamics as a parameter crosses a threshold (UG)

## Definitions in the sources

### complex-systems

- [[castellano-2009-socialdynamics/main-p3]] (p. 41): change of dynamics at $\rho_c$; subcritical for $\eta<2$, critical for $\eta\ge2$
- [[granovetter-1978-threshold/main]] (p. 1427): author notes a discontinuous jump of $r_e$ at $\sigma_c\approx12.2$. He does not use the term [weak: not really used in this unit]
- [[lorenz-1963-nonperiodic/main]] (pp. 135–136): onset of convection at $r=1$ and the instability of steady convection at (34), without the word "bifurcation"
- [[mitchell-2009-guidedtour/ch02-dynamics]] (pdf 56): an abrupt period doubling as the control parameter changes
- [[scheffer-2009-earlywarning/main]] (p. 53): our gloss: qualitative change of dynamics at a parameter value; fundamental shifts at bifurcations are called critical transitions
- [[strogatz-2024-nonlinear/ch01-overview]] (pp. 10–11): named as a new phenomenon appearing at $n=1$; not defined here [weak: not really used in this unit]
- [[strogatz-2024-nonlinear/ch02-flows]] (p. 26): only mentioned: the degenerate cases $f'(x^*)=0$ "arise naturally" there
- [[strogatz-2024-nonlinear/ch03-bifurcations-p1]] (p. 45): qualitative change of the flow as a parameter varies; bifurcation point = parameter value where it occurs
- [[strogatz-2024-nonlinear/ch03-bifurcations-p2]] (p. 71): qualitative change in the fixed points as a parameter varies; here the saddle-node bifurcations along $h=\pm h_c(r)$
- [[strogatz-2024-nonlinear/ch06-phase-p2]] (p. 196): index theory is said to constrain which fixed points can coalesce in bifurcations (p. 174). On these pages it is explored only in Exercise 6.8.12
- [[strogatz-2024-nonlinear/ch08-bifurcations-p1]] (p. 244): change of topological structure of the phase portrait as a parameter varies
- [[strogatz-2024-nonlinear/ch08-bifurcations-p2]] (p. 264): qualitative change of dynamics at a parameter value; here, the creation or destruction of cycles
- [[strogatz-2024-nonlinear/ch08-bifurcations-p3]] (p. 287): qualitative change in dynamics as a parameter varies; exercises cover saddle-node, transcritical, pitchfork, Hopf, homoclinic, infinite-period
- [[strogatz-2024-nonlinear/ch09-lorenz-p1]] (pp. 322–324): pitchfork at r = 1, subcritical Hopf at r = r_H
- [[strogatz-2024-nonlinear/ch09-lorenz-p2]] (p. 338): here pitchfork at r=1, subcritical Hopf at $r_H$=24.74, homoclinic at r≈13.926
- [[strogatz-2024-nonlinear/ch10-one-p1]] (pp. 365, 369): transcritical (r=1), flip (r=3), tangent (window birth) for maps
- [[strogatz-2024-nonlinear/ch10-one-p2]] (p. 384): period-doubling (flip) bifurcations of cycles; for flows they need three or more dimensions

### control-theory

- [[astrom-2021-feedbacksystems/ch05-dynamic]] (p. 5-30): qualitative change in behavior at a parameter value [new]

## Instances that use it

- [[predator-prey]] — stability diagram, bifurcation, limit cycle — from [[astrom-2021-feedbacksystems/ch05-dynamic]]
- [[ising-mean-field]] — T_c^mft = 4 vs true 2.27; pitchfork and saddle-node bifurcations — from [[mackay-2003-information/ch33-variational]]
- [[harvested-population-model]] — $dX/dt = X(1-X/K) - cX^2/(X^2+1)$ is the model of Fig. 1 (p. 54), where higher harvest rate c gives lower resilience, larger s.d. and higher correlation; Fig. 2 (p. 55) uses a harvested-population model driven slowly across a bifurcation (ref. 77) — from [[scheffer-2009-earlywarning/main]]
- [[laser-threshold]] — transcritical bifurcation in photon number at $N_0=k/G$ — from [[strogatz-2024-nonlinear/ch03-bifurcations-p1]]
- [[bead-on-tilted-wire]] — mechanical example of imperfect bifurcation and catastrophe — from [[strogatz-2024-nonlinear/ch03-bifurcations-p2]]
- [[driven-pendulum-josephson-junction]] — bistability, homoclinic and infinite-period bifurcations, hysteretic I–V curve — from [[strogatz-2024-nonlinear/ch08-bifurcations-p2]]
- [[binocular-rivalry-model]] — pitchfork or Hopf bifurcation of the symmetric state, with rhythmic alternation — from [[strogatz-2024-nonlinear/ch08-bifurcations-p3]]
- [[brusselator]] — chemical oscillators with Hopf bifurcations — from [[strogatz-2024-nonlinear/ch08-bifurcations-p3]]
- [[schnackenberg-model]] — chemical oscillators with Hopf bifurcations — from [[strogatz-2024-nonlinear/ch08-bifurcations-p3]]
- [[odell-predator-prey]] — Hopf bifurcation at $a_c=\tfrac12$ — from [[strogatz-2024-nonlinear/ch08-bifurcations-p3]]
- [[period-3-window]] — tangent bifurcation at $1+\sqrt8$, intermittency, 6-cycle — from [[strogatz-2024-nonlinear/ch10-one-p1]]

## Candidate bridges

- [structural-analogy] Bonabeau/$\sigma$-model coexisting stable states above a critical density ↔ saddle-node bifurcation and hysteresis — dependence on initial conditions resembles hysteresis in tipping points. — from [[castellano-2009-socialdynamics/main-p3]] (complex-systems → unspecified)
- [structural-analogy] jump at $\sigma_c$ ↔ saddle-node (fold) bifurcation — two intersections merging into a tangent point and vanishing. — from [[granovetter-1978-threshold/main]] (complex-systems → unspecified)
- [structural-analogy] Punctuated equilibria ↔ tipping points or bifurcations: long stability, then rapid shift. — from [[mitchell-2009-guidedtour/ch05-evolution]] (complex-systems → complex-systems)
- [structural-analogy] Hopf bifurcation ↔ complex-systems: onset of self-sustained oscillation as a control parameter passes a threshold — from [[strogatz-2024-nonlinear/ch08-bifurcations-p1]] (complex-systems → complex-systems)
- [same-math] tangent bifurcation of $f^3$ ↔ saddle-node bifurcation of flows: author states they are the same bifurcation under another name (p. 371). — from [[strogatz-2024-nonlinear/ch10-one-p1]] (complex-systems → complex-systems)
