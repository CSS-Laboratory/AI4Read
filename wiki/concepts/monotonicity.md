---
id: monotonicity
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 3
n_works: 2
tiers: [core]
grounding: digests
sources: [hernan-2020-whatif/ch05-interaction, hernan-2020-whatif/ch16-instrumental, pearl-2016-primer/ch04-counterfactuals]
generated_by: build_kg.py
---

# monotonicity

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch05-interaction]] (p. 66): no treatment prevents any individual's outcome (new)
- [[hernan-2020-whatif/ch16-instrumental]] (pp. 217–218): no defiers, $A^{z=1}\ge A^{z=0}$ for all individuals [new]
- [[pearl-2016-primer/ch04-counterfactuals]] (p. 113, p. 117): $Y_1(u)\ge Y_0(u)$ for all $u$; identifies PN and PNS (new)

## Instances that use it

- [[toeplitz-determinant-monotonicity]] — stationary-process entropy rate analogue for $|K_k|^{1/k}$ — from [[cover-2006-elements/ch16-inequalities]]
- [[metropolis-21-state-chain]] — toy chain on $\{0,\dots,20\}$ used for coalescence, CFTP and monotonicity — from [[mackay-2003-information/ch32-exact]]
- [[coarse-graining-simplex]] — merging bins illustrates monotonicity, Fig. 9 — from [[nielsen-2020-elementary/main-p1]]

## Candidate bridges

- [structural-analogy] Condition 2 (positive association) ↔ electoral competition: more support for a party should not lower its result (monotonicity). — from [[arrow-1951-socialchoice/ch03-iii]] (political-science → political-science)
- [structural-analogy] Less-is-more in single evaluation ↔ utility function: a value that fails to rise when a good is added violates monotonicity. — from [[kahneman-2011-thinking/ch15-linda]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Information monotonicity under coarse-graining ↔ information-theory: data processing inequality — both say processing cannot raise divergence, but the source treats only bin merging — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
- [same-math] Monotonicity of probability: if $h_1\Rightarrow h_2$ then $P(h_1\mid e)\le P(h_2\mid e)$ (note *3, p. 269) ↔ probability calculus: stronger statements are never more probable. — from [[popper-1959-logic/ch10-corroboration]] (analytic-philosophy → other:probability)
- [metaphor] Rayleigh monotonicity ↔ stiffer springs give a stiffer whole — an intuition for "more edge weight, more conductance". — from [[spielman-2025-sagt/ch12-effective]] (linear-algebra → unspecified)
- [structural-analogy] Rayleigh monotonicity ↔ variational principles: restricting or weakening a minimisation problem moves its minimum in a fixed direction. — from [[spielman-2025-sagt/ch17-monotonicity]] (linear-algebra → other:variational-principles)
- [structural-analogy] Stretch bounds $\mathrm{Reff}$ ↔ electrical networks: adding resistors in parallel only lowers resistance (Rayleigh monotonicity). — from [[spielman-2025-sagt/ch37-augmented]] (linear-algebra → other:physics)
