---
id: structural-causal-model
type: concept
fields: [bayesian]
n_sources: 10
tiers: [core, reference, deep]
grounding: digests
sources: [hernan-2020-whatif/ch06-graphical, murphy-2023-pml2/ch04-graphical-p3, murphy-2023-pml2/ch29-state-p3, murphy-2023-pml2/ch30-graph, murphy-2023-pml2/ch36-causality-p1, pearl-2009-causality/main, pearl-2016-primer/ch01-preliminaries, pearl-2016-primer/ch03-effects, pearl-2016-primer/ch04-counterfactuals, pearl-2018-bookofwhy/ch08-counterfactuals]
generated_by: build_kg.py
---

# structural-causal-model

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch06-graphical]] (pp. 77–78): here the NPSEM/FCISTG/FFRCISTG family: parents plus error give one-step-ahead counterfactuals
- [[murphy-2023-pml2/ch04-graphical-p3]] (p. 212): $(U,V,F)$: deterministic mechanisms plus exogenous noise
- [[murphy-2023-pml2/ch29-state-p3]] (p. 1031): STS read as an SCM
- [[murphy-2023-pml2/ch30-graph]] (p. 1045): directed graphical model with deterministic relations except for stochastic exogenous roots
- [[murphy-2023-pml2/ch36-causality-p1]] (p. 1187): ordered assignments: each variable = function of its causes + independent exogenous noise; supports interventions by replacing assignments
- [[pearl-2009-causality/main]] (pp. 420–421): equations plus a diagram, with an in/out split, independent mechanisms and surgery
- [[pearl-2016-primer/ch01-preliminaries]] (p. 26): exogenous $U$, endogenous $V$, functions $f$ assigning each $V$ from other variables
- [[pearl-2016-primer/ch03-effects]] (pp. 54, 81): the graph and equations behind surgery and linear path analysis
- [[pearl-2016-primer/ch04-counterfactuals]] (p. 92): equations, one per variable, with exogenous $U$; here also the source of counterfactual values
- [[pearl-2018-bookofwhy/ch08-counterfactuals]] (pdf 252, 258): each variable is a function of its parents plus an exogenous $U$; no conditional probability tables

## Candidate bridges

- [metaphor] "Listening" ↔ structural causal models: each variable determined by its parents plus external noise. — from [[pearl-2018-bookofwhy/ch03-evidence]] (bayesian → bayesian)
