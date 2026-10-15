---
id: jeffreys-prior
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 6
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch02-single, jaynes-2003-probability/ch06-elementary-p2, jaynes-2003-probability/ch12-ignorance, jaynes-2003-probability/ch13-decision, murphy-2023-pml2/ch03-statistics-p2, polyanskiy-2025-information/ch15-universal]
generated_by: build_kg.py
---

# jeffreys-prior

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch02-single]] (pp. 52–53): $p(\theta)\propto J(\theta)^{1/2}$, invariant to reparameterization [new]
- [[jaynes-2003-probability/ch06-elementary-p2]] (pp. 181–182): $p(s)\propto1/s$, uniform in $\log s$; expresses complete ignorance of a scale parameter, per Jaynes [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch12-ignorance]] (p. 380, 395): $d\sigma/\sigma$, justified here by $\sigma$ being a scale parameter under group (12.18) [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch13-decision]] (p. 423): prior ∝ 1/α for positive α; reinterpreted as part of a percentage-accuracy loss [new; work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 103): $\propto\sqrt{\det\mathbf F}$; invariant to reparameterization [new]

### information-theory

- [[polyanskiy-2025-information/ch15-universal]] (pp. 252–253): prior $\propto\sqrt{\det J_F}$; asymptotically maximin for smooth families and reparametrization-invariant [new]

## Instances that use it

- [[alice-bob-odds-parameterization]] — Jeffreys prior invariance for the binomial (rate vs odds) — from [[murphy-2023-pml2/ch03-statistics-p2]]

## Candidate bridges

- [same-math] Fisher information $J(\theta)$ in Jeffreys' prior ↔ frequentist asymptotics: the same quantity as in (2.20). — from [[gelman-2013-bda3/ch02-single]] (bayesian → other:frequentist-asymptotics)
- [structural-analogy] "Jeffreys prior is uninformative for a scale parameter" ↔ information-theory: the group-invariance / maximum-entropy prior constructions Jaynes mentions (pp. 484–485). — from [[jaynes-2003-probability/ch15-paradoxes]] (bayesian → information-theory)
