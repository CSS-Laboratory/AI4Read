---
id: circuit
type: concept
fields: [llm]
fields_strong: []
n_sources: 0
n_works: 0
tiers: []
grounding: digests
sources: []
canon_spine: [llm]
generated_by: build_kg.py
---

# circuit

## Canon spine entry

- **circuit** (llm): a subgraph of weights and components that implements an identifiable algorithm (grad)

## Definitions in the sources

(no digest uses this id yet)

## Instances that use it

- [[causalgia]] — a two-state regenerative circuit, one state painful — from [[ashby-1956-cybernetics/ch05-stability]]
- [[mechanical-electrical-ode-isomorphism]] — spring-wheel system, L–R–C circuit and second-order equation behave identically — from [[ashby-1956-cybernetics/ch06-black]]
- [[radio-set-with-three-circuits]] — selecting a machine equals fixing an input — from [[ashby-1956-cybernetics/ch13-regulating]]
- [[active-band-pass-filter]] — op amp circuit with a band-pass frequency response — from [[astrom-2021-feedbacksystems/ch06-linear]]
- [[op-amp-feedback-circuit]] — dynamic op amp gives closed-loop $G$, gain $\approx-R_2/R_1$, bandwidth $\approx aR_1k/R_2$ — from [[astrom-2021-feedbacksystems/ch09-transfer-p1]]
- [[op-amp-pid-circuit]] — PI and PID built from op amps — from [[astrom-2021-feedbacksystems/ch11-pid]]
- [[circuit-fan-out-dup]] — Fig. 6.1 circuit and the dup/sum trick for fan-out — from [[murphy-2023-pml2/ch06-optimization-p1]]
- [[circuit-diagram-interventions]] — one diagram predicts millions of abnormal conditions — from [[pearl-2009-causality/main]]
- [[ashby-homeostat]] — machine that readjusts its circuits by trial and error to regain stability — from [[pierce-1980-introduction/ch11-cybernetics]]
- [[noisy-boolean-circuit-von-neumann]] — δ-noisy gates; Evans–Schulman bound and the $\frac12-\frac1{2\sqrt K}$ threshold — from [[polyanskiy-2025-information/ch36-strong-p1]]
- [[rc-vs-rlc-circuit]] — $n=1$ cannot oscillate; $n=2$ can — from [[strogatz-2024-nonlinear/ch01-overview]]
- [[rc-circuit-charging]] — globally stable linear first-order system — from [[strogatz-2024-nonlinear/ch02-flows]]
- [[forced-rc-circuit]] — Poincaré map is a line of slope below 1, so a unique globally stable cycle — from [[strogatz-2024-nonlinear/ch08-bifurcations-p2]]
- [[cuomo-oppenheim-circuit]] — analog Lorenz circuit used for masked speech — from [[strogatz-2024-nonlinear/ch09-lorenz-p2]]

## Candidate bridges

- [same-math] Mechanical spring–wheel–friction system, RLC circuit and $a\ddot z + b\dot z + cz = w$ (pp. 95–96) ↔ control-theory: systems sharing one second-order transfer function — the same differential equation with matched parameters. — from [[ashby-1956-cybernetics/ch06-black]] (control-theory → control-theory)
- [same-math] PI controller as a controller state $z$ with $\dot z=v_r-v$ (4.4) ↔ op-amp PI circuit (p. 4-11) — both realize a PI law (the op-amp circuit with an inversion sign). — from [[astrom-2021-feedbacksystems/ch04-examples]] (control-theory → unspecified)
- [structural-analogy] Generalised impedance $Z(s)$ with algebraic circuit analysis ↔ resistor networks: same series/parallel rules with $Z$ replacing $R$. — from [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (control-theory → other:resistor-networks)
- [metaphor] Selective attention allocation under overload ↔ computing: priority scheduling versus a circuit breaker (pdf 36) — from [[kahneman-2011-thinking/ch02-attention]] (decision-game-theory → other:computer-science)
- [structural-analogy] functional completeness of ↑ or ↓ ↔ digital logic: a single gate type (NAND or NOR) can build any Boolean function — the text itself does not mention circuits. — from [[magnus-2025-forallx/ch46-functional]] (analytic-philosophy → other:computer-science)
- [metaphor] Forney factor graph ↔ circuit or neural-network diagram: signals flow along edges, modified by nodes. — from [[murphy-2023-pml2/ch04-graphical-p3]] (bayesian → other:circuit-or-neural-network)
- [same-math] Reverse-mode AD on circuits ↔ neural networks: backpropagation — the text states they are the same algorithm (p. 270) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → llm)
- [structural-analogy] Wiener filtering of signal in noise ↔ signal processing: choose a circuit that best estimates a signal from a mixture. — from [[pierce-1980-introduction/ch02-origins]] (information-theory → other:signal-processing)
- [structural-analogy] unraveled residual net as many paths ↔ llm: circuit/path analysis in interpretability — both decompose output into paths through the graph. — from [[prince-2023-udl/ch11-residual]] (llm → llm)
- [structural-analogy] spring chain K, T, B ↔ circuits: voltage drops e and currents y with heat loss eᵀy (p. 68). — from [[strang-2023-introduction/ch02-solving-p2]] (linear-algebra → llm)
