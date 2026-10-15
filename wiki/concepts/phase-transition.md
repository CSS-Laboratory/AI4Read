---
id: phase-transition
type: concept
fields: [information-theory, llm]
n_sources: 3
tiers: [core, deep]
grounding: digests
sources: [mackay-2003-information/ch31-ising, mackay-2003-information/ch51-appendices, wei-2022-emergent/main]
generated_by: build_kg.py
---

# phase-transition

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch31-ising]] (p. 403): a 'collective phenomenon'; true phase transitions only for infinite $N$, hinted at by relatively bigger fluctuations at intermediate temperature [new]
- [[mackay-2003-information/ch51-appendices]] (pp. 601–602): a critical point where derivatives of $Z$ jump or diverge; needs infinitely many states and long-range correlations [new]

### llm

- [[wei-2022-emergent/main]] (p. 2): a dramatic change in overall behavior not foreseen from smaller-scale systems; here, near-random → well-above-random as scale grows [new]

## Instances that use it

- [[phase-transition-partition-functions]] — relative probability of two phases is $Z_j/Z_k$; indifference where they are equal — from [[jaynes-2003-probability/ch20-model]]
- [[ising-lattice-phase-transition]] — samples clump as coupling rises; $J_c\approx0.44$ for the square lattice — from [[murphy-2023-pml2/ch04-graphical-p2]]

## Candidate bridges

- [structural-analogy] Dynamical selection of a critical point ↔ equilibrium phase transitions: the same scale-free behaviour without tuning a parameter — from [[bak-1987-soc/main]] (complex-systems → other)
- [metaphor] "Tipping" ↔ physics: phase transitions — small changes cause sudden large shifts. — from [[clark-2017-principles/ch08-democratic-p1]] (political-science → other)
- [structural-analogy] Kuhn's critical mass of anomalies ↔ phase transition (melting): sudden change after gradual build-up (p. 82; the author uses the comparison himself) — from [[godfreysmith-2003-theory/ch05-kuhn]] (analytic-philosophy → other)
- [structural-analogy] Renormalization in Feigenbaum's theory ↔ statistical physics: the same technique is used for phase transitions and critical phenomena (pdf 59). — from [[mitchell-2009-guidedtour/ch02-dynamics]] (complex-systems → complex-systems)
- [structural-analogy] Optional $\ell_1$ penalty $\lambda\|R\|_1$ with a sparsity-driven phase transition ↔ statistics: sparsity-promoting regularization; the penalty is used here to pick a simple solution from a set of equally consistent ones. — from [[ng-2000-irl/main]] (control-theory → other)
- [metaphor] Tree reconstruction threshold $b\eta=1$ ↔ statistical physics: Ising model on Bethe lattice and its phase transition. — from [[polyanskiy-2025-information/ch36-strong-p1]] (information-theory → complex-systems)
- [structural-analogy] Coupled-unit spatial systems ↔ ferromagnets: the paper says phase transitions may occur much as in ferromagnetic materials (p. 56); it gives no matching equations. — from [[scheffer-2009-earlywarning/main]] (complex-systems → other)
- [structural-analogy] Feigenbaum universality ↔ complex-systems: universality near critical points — the text itself links chaos to phase transitions. — from [[strogatz-2024-nonlinear/ch01-overview]] (complex-systems → complex-systems)
- [structural-analogy] Pitchfork as continuous (second-order) and subcritical as discontinuous (first-order) phase transition ↔ criticality / phase transition — the text states this relation (pp. 61–62). — from [[strogatz-2024-nonlinear/ch03-bifurcations-p1]] (complex-systems → unspecified)
- [structural-analogy] imperfection $h$ breaking up/down symmetry ↔ physics: external field $h$ on the Ising magnet (Exercise 3.6.7, p. 89), where the phase transition is softened — from [[strogatz-2024-nonlinear/ch03-bifurcations-p2]] (complex-systems → other)
- [structural-analogy] Renormalization at period-doubling ↔ statistical physics: the author says α, δ are analogous to universal exponents at second-order phase transitions (p. 381). Both rely on repeated rescaling and loss of microscopic detail. — from [[strogatz-2024-nonlinear/ch10-one-p2]] (complex-systems → complex-systems)
- [structural-analogy] Free energy F and annealing in β ↔ statistical physics: partition function, phase transitions (pp. 13, 15) — from [[tishby-2000-bottleneck/main]] (information-theory → complex-systems)
- [metaphor] Emergence in the paper's sense ↔ physics: Anderson's "more is different" and phase transitions — the paper takes the framing, but its definition is only about scaling-curve shape (p. 2). — from [[wei-2022-emergent/main]] (llm → other)
