---
id: do-operator
type: concept
fields: [bayesian]
n_sources: 16
tiers: [core, reference, deep]
grounding: digests
sources: [murphy-2023-pml2/ch04-graphical-p3, murphy-2023-pml2/ch36-causality-p1, murphy-2023-pml2/ch36-causality-p2, pearl-2009-causality/main, pearl-2016-primer/ch03-effects, pearl-2016-primer/ch04-counterfactuals, pearl-2018-bookofwhy/ch00-introduction, pearl-2018-bookofwhy/ch01-ladder, pearl-2018-bookofwhy/ch03-evidence, pearl-2018-bookofwhy/ch04-confounding, pearl-2018-bookofwhy/ch06-paradoxes, pearl-2018-bookofwhy/ch07-beyond, pearl-2018-bookofwhy/ch08-counterfactuals, pearl-2018-bookofwhy/ch09-mediation-p1, pearl-2018-bookofwhy/ch09-mediation-p2, pearl-2018-bookofwhy/ch10-big]
raw_ids: [Do-operator]
canon_spine: bayesian
generated_by: build_kg.py
---

# do-operator

## Canon spine entry

- **do-operator** (bayesian): P(Y | do(X=x)), the distribution under intervention, as opposed to passive observation P(Y | X=x) (UG)

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch04-graphical-p3]] (p. 215): clamp a variable and cut incoming edges; differs from conditioning
- [[murphy-2023-pml2/ch36-causality-p1]] (p. 1190): $P(\cdot\mid \mathrm{do}(A=a))$: distribution in the graph with edges into $A$ deleted, conditioned on $A=a$
- [[murphy-2023-pml2/ch36-causality-p2]] (p. 1217): here also the variant $\mathbb E^{A=1}$ that uses $P(\text{parents}|A=1)$
- [[pearl-2009-causality/main]] (pp. 421–422): $P(\cdot \mid do(\cdot))$: probability after forcing a variable, as opposed to conditioning on having seen it
- [[pearl-2016-primer/ch03-effects]] (p. 55): $P(y|do(x))$: distribution of $Y$ when $X$ is fixed by intervention, not observed
- [[pearl-2016-primer/ch04-counterfactuals]] (p. 93): $do(X=x)$ replaces the equation for $X$; defined on distributions, so population-level only
- [[pearl-2018-bookofwhy/ch00-introduction]] (pdf 14–15): $P(L\mid do(D))$: distribution under forced intervention, unlike seeing $P(L\mid D)$
- [[pearl-2018-bookofwhy/ch01-ladder]] (pdf 37): $P(Y \mid do(X))$: probability when $X$ is set by intervention, not just observed
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 126–127): only informally: "wiggling" and "holding constant", as opposed to conditioning
- [[pearl-2018-bookofwhy/ch04-confounding]] (pdf 140–141): erases arrows into a variable and sets it; the query P(Y | do(X))
- [[pearl-2018-bookofwhy/ch06-paradoxes]] (pdf 191): the corrected sure-thing principle needs a causal calculus using it
- [[pearl-2018-bookofwhy/ch07-beyond]] (pdf 213–216): $P(Y\mid do(X))$: distribution under intervention, as opposed to seeing; defined here by deleting arrows into X
- [[pearl-2018-bookofwhy/ch08-counterfactuals]] (pdf 245, 253): used to delete arrows into the variable set counterfactually
- [[pearl-2018-bookofwhy/ch09-mediation-p1]] (pdf 289): used to define CDE [as `Do-operator`]
- [[pearl-2018-bookofwhy/ch09-mediation-p2]] (pdf 294, 300): intervention operator; defines the total effect and the controlled direct effect
- [[pearl-2018-bookofwhy/ch10-big]] (pdf 320): do-calculus rules used to test whether a target is transportable

## Candidate bridges

- [structural-analogy] Choosing the best of decisions with $p(x\mid d)$ ↔ do-operator: both treat the action as fixed rather than random. — from [[gelman-2013-bda3/ch09-decision]] (bayesian → other)
- [structural-analogy] Logical vs. causal dependence (3.40) ↔ bayesian: association vs. intervention in the ladder of causation / do-operator — conditioning on information is not the same as physical intervention. — from [[jaynes-2003-probability/ch03-elementary]] (information-theory → bayesian)
- [metaphor] counterfactual plot (changing one predictor in the model) ↔ do-operator: both set a variable by hand, but the text makes no claim that the plot is an intervention estimate. — from [[mcelreath-2020-rethinking/ch05-multivariate-p1]] (bayesian → other)
- [same-math] $P(Y \mid do(X))$ via graph surgery ↔ do-operator (canon): the chapter pairs the do-notation for interventions with graph surgery as the way to answer them, without a formal statement of the link. — from [[pearl-2018-bookofwhy/ch01-ladder]] (bayesian → other)
- [structural-analogy] Randomization erases arrows into X ↔ do-operator: the graph surgery in Model 3 mimics the intervention in Model 2 (pdf 141). — from [[pearl-2018-bookofwhy/ch04-confounding]] (bayesian → other)
