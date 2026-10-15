---
id: graph-surgery
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 3
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [murphy-2023-pml2/ch36-causality-p1, pearl-2016-primer/ch03-effects, pearl-2018-bookofwhy/ch01-ladder]
generated_by: build_kg.py
---

# graph-surgery

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch36-causality-p1]] (p. 1190): deleting the edges into the intervened variable and conditioning on its value [new]
- [[pearl-2016-primer/ch03-effects]] (p. 54): simulate an intervention by deleting all arrows into the manipulated variable [new]
- [[pearl-2018-bookofwhy/ch01-ladder]] (pdf 47): to model setting a variable, delete its incoming arrows and fix its value [new]

## Candidate bridges

- [structural-analogy] SCM/graph surgery ↔ bayesian: conditioning on an observed value vs overwriting a node — $P(Y\mid \mathrm{do}(A))$ differs from $P(Y\mid A)$ because the parents of $A$ are cut. — from [[murphy-2023-pml2/ch36-causality-p1]] (bayesian → bayesian)
- [structural-analogy] Equation deletion for do(Y=y) ↔ causal inference: the graph-surgery (truncated factorization) view of intervention — both cut the arrows into the manipulated variable. — from [[pearl-2009-causality/main]] (bayesian → bayesian)
- [same-math] $P(Y \mid do(X))$ via graph surgery ↔ do-operator (canon): the chapter pairs the do-notation for interventions with graph surgery as the way to answer them, without a formal statement of the link. — from [[pearl-2018-bookofwhy/ch01-ladder]] (bayesian → bayesian)
- [structural-analogy] Randomization erases arrows into X ↔ do-operator: the graph surgery in Model 3 mimics the intervention in Model 2 (pdf 141). — from [[pearl-2018-bookofwhy/ch04-confounding]] (bayesian → bayesian)
