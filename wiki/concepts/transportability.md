---
id: transportability
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 4
n_works: 2
tiers: [core]
grounding: digests
sources: [hernan-2020-whatif/ch03-observational, hernan-2020-whatif/ch04-effect, pearl-2018-bookofwhy/ch07-beyond, pearl-2018-bookofwhy/ch10-big]
generated_by: build_kg.py
---

# transportability

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch03-observational]] (p. 35): whether a causal effect from one population carries to another; affected by how precisely the intervention is specified [new]
- [[hernan-2020-whatif/ch04-effect]] (pp. 52, 54): extrapolating effects to another population; depends on modifiers, treatment definition, interference [new]
- [[pearl-2018-bookofwhy/ch07-beyond]] (pdf 219–220): Judging whether effects from one environment hold in another, using diagrams [new]
- [[pearl-2018-bookofwhy/ch10-big]] (pdf 317–318): translating a study's causal result to a different population, decided by a diagram with $S$ variables [new]

## Instances that use it

- [[parachute-transportability]] — Smith and Pell: no major modifiers found — from [[hernan-2020-whatif/ch04-effect]]
- [[ad-transportability-example]] — five cities versus Arkansas, Figs. 10.1–10.2 — from [[pearl-2018-bookofwhy/ch10-big]]

## Candidate bridges

- [structural-analogy] sequential refinement of $Y^{a_0,a_1,a_2,a_3}$ (Technical Point 3.2) ↔ hierarchical models: unspecified components $A_j^{a_0=1}$ are random quantities whose population distribution drives transportability. — from [[hernan-2020-whatif/ch03-observational]] (bayesian → bayesian)
- [metaphor] "Transportability depends on unmeasured modifiers" ↔ bayesian: prior-sensitivity of out-of-sample prediction. — from [[hernan-2020-whatif/ch04-effect]] (bayesian → bayesian)
- [structural-analogy] Transportability with $S$ nodes ↔ bayesian: hierarchical models, where populations differ in some parameters and share others — both decide what to borrow across groups. — from [[pearl-2018-bookofwhy/ch10-big]] (bayesian → bayesian)
