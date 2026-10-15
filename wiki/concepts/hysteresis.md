---
id: hysteresis
type: concept
fields: [complex-systems, control-theory, economics-finance]
fields_strong: [complex-systems, control-theory, economics-finance]
n_sources: 10
n_works: 4
tiers: [core, deep]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch02-feedback, castellano-2009-socialdynamics/main-p2, stiglitz-2002-paradigm/main-p3, strogatz-2024-nonlinear/ch03-bifurcations-p1, strogatz-2024-nonlinear/ch03-bifurcations-p2, strogatz-2024-nonlinear/ch04-flows, strogatz-2024-nonlinear/ch08-bifurcations-p1, strogatz-2024-nonlinear/ch08-bifurcations-p2, strogatz-2024-nonlinear/ch08-bifurcations-p3, strogatz-2024-nonlinear/ch09-lorenz-p2]
canon_spine: [complex-systems]
generated_by: build_kg.py
---

# hysteresis

## Canon spine entry

- **hysteresis** (complex-systems): the path back differs from the path forward, so reversing the cause need not reverse the effect (UG)

## Definitions in the sources

### complex-systems

- [[castellano-2009-socialdynamics/main-p2]] (p. 24): RFIM hysteresis behind the universal $dO/dF$ curve
- [[strogatz-2024-nonlinear/ch03-bifurcations-p1]] (p. 61): lack of reversibility when a parameter is varied, from coexisting stable states
- [[strogatz-2024-nonlinear/ch03-bifurcations-p2]] (p. 78): after an outbreak, restoring old parameter values does not restore the refuge state
- [[strogatz-2024-nonlinear/ch04-flows]] (p. 114): Josephson I–V curve when $\beta$ is not negligible: different paths up and down
- [[strogatz-2024-nonlinear/ch08-bifurcations-p1]] (p. 255): in the subcritical Hopf, large oscillations persist after μ returns to 0
- [[strogatz-2024-nonlinear/ch08-bifurcations-p2]] (p. 268): the path back differs from the path forward; here from coexisting stable fixed point and limit cycle
- [[strogatz-2024-nonlinear/ch08-bifurcations-p3]] (p. 298): jump up and jump down at different values of $a$ when sweeping the detuning
- [[strogatz-2024-nonlinear/ch09-lorenz-p2]] (p. 340): possible between a fixed point and a strange attractor for 24.06<r<24.74

### control-theory

- [[astrom-2021-feedbacksystems/ch02-feedback]] (pp. 2-4, 2-26): several stable outputs for the same input, with switching at $\pm r_{max}$ [new]

### economics-finance

- [[stiglitz-2002-paradigm/main-p3]] (p. 519; p. 521): effects that persist after their cause is removed; e.g. bankrupt firms did not recover when rates fell [new]

## Instances that use it

- [[schmitt-trigger-memory]] — positive feedback with saturation gives hysteresis — from [[astrom-2021-feedbacksystems/ch02-feedback]]
- [[relay-with-hysteresis]] — describing-function prediction of limit cycle amplitude and frequency — from [[astrom-2021-feedbacksystems/ch10-frequency]]
- [[east-asia-crisis-1997]] — IMF high interest rates in leveraged economies; hysteresis; Malaysia vs Thailand comparison — from [[stiglitz-2002-paradigm/main-p3]]
- [[josephson-junction]] — overdamped I–V curve and hysteresis with inertia — from [[strogatz-2024-nonlinear/ch04-flows]]
- [[forced-duffing-oscillator]] — averaging, cusp catastrophe, hysteresis — from [[strogatz-2024-nonlinear/ch08-bifurcations-p3]]

## Candidate bridges

- [structural-analogy] Hysteresis from positive feedback with saturation ↔ bistable switches with two stable states — the same equilibrium-and-slope picture (stable where $G'>0$). — from [[astrom-2021-feedbacksystems/ch02-feedback]] (control-theory → unspecified)
- [structural-analogy] Bonabeau/$\sigma$-model coexisting stable states above a critical density ↔ saddle-node bifurcation and hysteresis — dependence on initial conditions resembles hysteresis in tipping points. — from [[castellano-2009-socialdynamics/main-p3]] (complex-systems → unspecified)
- [structural-analogy] Flickering and bimodality ↔ hysteresis and bistability: noise-induced switching inside the bistable region. — from [[scheffer-2009-earlywarning/main]] (complex-systems → complex-systems)
- [structural-analogy] Hysteresis after forced bankruptcy (net worth destroyed, not restored when rates fall) ↔ economics-finance: debt deflation / balance-sheet recession — both involve balance-sheet damage with lasting demand effects. — from [[stiglitz-2002-paradigm/main-p3]] (economics-finance → economics-finance)
- [structural-analogy] double-well potential, two stable equilibria ↔ tipping points/hysteresis: two coexisting stable states (the text does not make this link). — from [[strogatz-2024-nonlinear/ch02-flows]] (complex-systems → complex-systems)
- [structural-analogy] Subcritical pitchfork jumps and hysteresis ↔ complex systems: tipping points with hysteresis — coexisting stable states mean reversing the cause does not reverse the effect. — from [[strogatz-2024-nonlinear/ch03-bifurcations-p1]] (complex-systems → complex-systems)
- [structural-analogy] cusp catastrophe and bistable region ↔ complex-systems: tipping points with hysteresis — a sudden jump plus a different path back — from [[strogatz-2024-nonlinear/ch03-bifurcations-p2]] (complex-systems → complex-systems)
- [structural-analogy] Subcritical Hopf jump and hysteresis ↔ complex-systems: tipping points with irreversible switching — from [[strogatz-2024-nonlinear/ch08-bifurcations-p1]] (complex-systems → complex-systems)
- [structural-analogy] saddle-node jump and slow return in the I–V curve ↔ complex-systems: tipping point with hysteresis — different forward and backward thresholds from bistability. — from [[strogatz-2024-nonlinear/ch08-bifurcations-p2]] (complex-systems → complex-systems)
- [structural-analogy] Coexisting fixed point and strange attractor ↔ tipping points and hysteresis: a big enough perturbation switches the final state — from [[strogatz-2024-nonlinear/ch09-lorenz-p2]] (complex-systems → complex-systems)
