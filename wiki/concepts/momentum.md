---
id: momentum
type: concept
fields: [control-theory, linear-algebra, llm]
n_sources: 3
tiers: [core, deep, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch07-continuous, liberzon-2012-calculus/ch02-calculus, prince-2023-udl/ch06-fitting]
generated_by: build_kg.py
---

# momentum

## Definitions in the sources

### control-theory

- [[liberzon-2012-calculus/ch02-calculus]] (pp. 34, 36): $p=L_{y'}$; conserved when $L$ has no $y$ [new]

### linear-algebra

- [[deisenroth-2020-mml/ch07-continuous]] (p. 231): gradient update with memory, $\alpha\Delta x_i$ added, dampening oscillations [new]

### llm

- [[prince-2023-udl/ch06-fitting]] (p. 86): step uses a weighted sum of past gradients, with weights shrinking back in time [new]

## Instances that use it

- [[pendulum-feedback-dispute]] — whether position–momentum link counts as feedback — from [[ashby-1956-cybernetics/ch04-machine]]
- [[satellite-orbit-analogy]] — momentum balances gravity to give orbits, motivating the construction — from [[betancourt-2017-hmc/main-p2]]
- [[nuclear-polarization-effect]] — spin polarization predicted from rotation via an angular-momentum bath — from [[jaynes-1957-information/main]]
- [[filter-and-counter-experiment]] — filter selecting momentum, then counter timing arrivals — from [[popper-1959-logic/appvi-untitled]]
- [[heisenberg-microscope]] — Popper argues position and momentum measurements are not symmetric in disturbance — from [[popper-1959-logic/appxi-untitled]]
- [[slit-selection-experiment]] — slit selection by position followed by momentum measurement, showing the need for non-predictive measurements — from [[popper-1959-logic/ch09-observations]]
- [[heisenberg-uncertainty]] — QP − PQ = I forbids exact position and momentum — from [[strang-2023-introduction/ch06-eigenvalues-p1]]

## Candidate bridges

- [metaphor] Satellite orbit ↔ gradient flow around a mode: momentum prevents falling in. — from [[betancourt-2017-hmc/main-p2]] (bayesian → other)
- [structural-analogy] momentum as moving average ↔ time-series: exponential smoothing of past updates. — from [[deisenroth-2020-mml/ch07-continuous]] (linear-algebra → other)
- [metaphor] Using a system's momentum the way a judo expert uses an opponent's ↔ control design that exploits slow dynamics. — from [[meadows-2008-thinking/ch01-basics]] (control-theory → unspecified)
- [structural-analogy] Shutter/filter trade-off: short wavetrain versus narrow momentum range ↔ signal processing: time–bandwidth trade-off — both involve sums of waves, but the source gives no formulas. — from [[popper-1959-logic/appvi-untitled]] (analytic-philosophy → other)
- [same-math] Momentum and Adam's $\mathbf m,\mathbf v$ ↔ statistics: exponentially weighted moving averages — the recursions have the same form — from [[prince-2023-udl/ch06-fitting]] (llm → other)
- [structural-analogy] AB = BA ↔ quantum mechanics: non-commuting position and momentum matrices (p. 224). — from [[strang-2023-introduction/ch06-eigenvalues-p1]] (linear-algebra → other)
