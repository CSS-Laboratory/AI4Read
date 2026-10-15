---
id: fundamental-problem-of-causal-inference
type: concept
fields: [bayesian, political-science]
fields_strong: [bayesian, political-science]
n_sources: 11
n_works: 7
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch14-introduction, grimmer-2022-textasdata/ch22-principles, grimmer-2022-textasdata/ch24-causal, hernan-2020-whatif/ch01-definition, hernan-2020-whatif/ch02-randomized, hernan-2020-whatif/ch03-observational, holland-1986-statistics/main, murphy-2023-pml2/ch04-graphical-p3, murphy-2023-pml2/ch36-causality-p1, pearl-2016-primer/ch04-counterfactuals, pearl-2018-bookofwhy/ch08-counterfactuals]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# fundamental-problem-of-causal-inference

## Canon spine entry

- **Fundamental problem of causal inference** (bayesian): for any unit we observe at most one potential outcome, so causal inference is a missing-data problem (UG)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch14-introduction]] (p. 359): only one of $y^I$, $y^O$ is observed per district
- [[hernan-2020-whatif/ch01-definition]] (p. 4): only the outcome for the received treatment is observed, so individual effects are not identified
- [[hernan-2020-whatif/ch02-randomized]] (p. 13): only one counterfactual outcome observed per person; the others are "?" in Table 2.1
- [[hernan-2020-whatif/ch03-observational]] (p. margin, p. 31): $Y^a$ is unknown for those with $A\neq a$, so conditional exchangeability cannot be verified
- [[holland-1986-statistics/main]] (p. 947): $Y_t(u)$ and $Y_c(u)$ cannot both be observed on one unit
- [[murphy-2023-pml2/ch04-graphical-p3]] (p. 217): only one potential outcome per unit is seen
- [[murphy-2023-pml2/ch36-causality-p1]] (p. 1193): used implicitly: only one potential outcome per individual is observed, so within-individual dependence is not observable
- [[pearl-2016-primer/ch04-counterfactuals]] (p. 105): in a trial only one of $Y_0,Y_1$ is observed per unit (Table 4.4)
- [[pearl-2018-bookofwhy/ch08-counterfactuals]] (pdf 248–249): Holland's name for one observed potential outcome per unit; Pearl rejects the missing-data framing

### political-science

- [[grimmer-2022-textasdata/ch22-principles]] (p. 374): counterfactual outcomes are never observed, so effects cannot be directly validated [new]
- [[grimmer-2022-textasdata/ch24-causal]] (p. 410): the counterfactual is never observed, so individual effects are not observable (p. 410) (new)
