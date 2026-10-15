---
id: m-bias
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 4
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [hernan-2020-whatif/ch07-confounding, hernan-2020-whatif/ch08-selection, murphy-2023-pml2/ch36-causality-p1, pearl-2018-bookofwhy/ch04-confounding]
generated_by: build_kg.py
---

# m-bias

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch07-confounding]] (p. 97): bias from adjusting for a collider $L$ in $A\leftarrow U_2\to L\leftarrow U_1\to Y$ [new]
- [[hernan-2020-whatif/ch08-selection]] (p. 111): selection bias structures of Figures 8.5–8.6, as named in the margin [new]
- [[murphy-2023-pml2/ch36-causality-p1]] (p. 1205): adjusting for a collider between two unobserved causes of $A$ and $Y$ creates bias [new]
- [[pearl-2018-bookofwhy/ch04-confounding]] (pdf 151–152): adjusting for a collider (the middle of the M) opens a spurious path; the collider becomes a confounder only when controlled [new]

## Instances that use it

- [[pap-smear-m-bias]] — physical activity, cervical cancer, Pap smear $L$, pre-cancer lesion $U_1$, health-conscious personality $U_2$ — from [[hernan-2020-whatif/ch07-confounding]]
- [[m-bias-fig-18-6]] — a pre-treatment collider $L$; adjusting for it introduces bias. — from [[hernan-2020-whatif/ch18-variable]]
- [[m-bias-graph]] — Figure 36.4: adjusting for a collider creates bias — from [[murphy-2023-pml2/ch36-causality-p1]]
- [[seat-belt-m-bias]] — seat-belt use as a collider in Pearl's example model of smoking and lung disease — from [[pearl-2018-bookofwhy/ch04-confounding]]

## Candidate bridges

- [structural-analogy] Collider conditioning opens a path (M-bias) ↔ Bayesian networks: "explaining away", where conditioning on a common effect makes independent causes dependent — the same path logic. — from [[hernan-2020-whatif/ch07-confounding]] (bayesian → bayesian)
- [structural-analogy] Collider conditioning (m-bias) ↔ bayesian: "explaining away" in Bayesian networks. — from [[murphy-2023-pml2/ch36-causality-p1]] (bayesian → bayesian)
