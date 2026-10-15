---
id: conditional-probability
type: concept
fields: [information-theory, bayesian, decision-game-theory, llm]
fields_strong: [information-theory, bayesian, decision-game-theory, llm]
n_sources: 6
n_works: 5
tiers: [core, reference]
grounding: digests
sources: [osborne-2004-introduction/ch17-mathematics, pearl-2016-primer/ch01-preliminaries, pierce-1980-introduction/app-mathematical, pierce-1980-introduction/ch03-mathematical, prince-2023-udl/ch23-probability, stone-2022-information/appf-rules]
generated_by: build_kg.py
---

# conditional-probability

## Definitions in the sources

### information-theory

- [[pierce-1980-introduction/app-mathematical]] (p. 281): p_x(y), the probability of y given x, in Shannon's notation [new]
- [[pierce-1980-introduction/ch03-mathematical]] (p. 51): probability of one symbol given the previous one, $p_T(H)=.37$ [new]
- [[stone-2022-information/appf-rules]] (p. 261): $p(x|y)=p(x,y)/p(y)$ [new]

### bayesian

- [[pearl-2016-primer/ch01-preliminaries]] (p. 8): $P(A|B)$ = probability of $A$ after filtering the data to cases where $B$ holds [new]

### decision-game-theory

- [[osborne-2004-introduction/ch17-mathematics]] (p. 453): $\Pr(E\mid F)=\Pr(E\text{ and }F)/\Pr(F)$ [new]

### llm

- [[prince-2023-udl/ch23-probability]] (p. 450): slice of the joint divided by the slice's area [new]

## Instances that use it

- [[bertrand-box-paradox]] — the pancake problem; answer 2/3 by conditional probability — from [[mcelreath-2020-rethinking/ch14-missing]]

## Candidate bridges

- [metaphor] DOWNING's updating of conditional probabilities ↔ Bayesian learning about types: the chapter describes only an updated estimate. — from [[axelrod-1984-cooperation/ch02-success]] (decision-game-theory → bayesian)
- [same-math] Prop. 3.4.1 ↔ statistics: the conditional expectation of an indicator is the conditional probability, and it minimizes mean squared error. — from [[bertsekas-2026-rlcourse/ch03-learning-p3]] (control-theory → other:statistics)
- [structural-analogy] conditional probability tables $P(Y\mid X)$ (columns sum to 1) ↔ Markov (stochastic) matrix — nonnegative columns summing to 1. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → unspecified)
- [same-math] Survival as product of conditional survivals ↔ probability: chain rule of conditional probability — the hazard product is that rule applied to $D_1,D_2,\dots$ — from [[hernan-2020-whatif/ch17-causal]] (bayesian → other:probability)
- [structural-analogy] Submarine: product of conditional probabilities telescopes to log 1/P(location) (4.14) ↔ Bayesian: sequential updating, where the order of evidence does not change the final posterior. — from [[mackay-2003-information/ch04-source]] (information-theory → bayesian)
- [structural-analogy] sampling a path with probabilities from backward messages ↔ bayesian: sampling from a posterior using conditional probabilities. — from [[mackay-2003-information/ch16-message]] (information-theory → bayesian)
- [same-math] Law of total probability (1.9) ↔ marginal likelihood: averaging a conditional probability over a distribution of the conditioning variable. — from [[pearl-2016-primer/ch01-preliminaries]] (bayesian → bayesian)
- [same-math] Back-door formula (Eq. 7.2) ↔ standardization over covariate strata in potential-outcomes adjustment: a weighted average of stratum-specific conditional probabilities by the covariate distribution. — from [[pearl-2018-bookofwhy/ch07-beyond]] (bayesian → other:standardization-over-covariate-strata)
- [same-math] $p(x_1,x_2)=p_a(x_1x_2)/p_a(x_2)$ ↔ standard probability: conditional probability as a ratio — the same formula, with Df2 as definition. — from [[popper-1959-logic/appii-untitled]] (analytic-philosophy → other:probability)
- [structural-analogy] conditional probability as a primitive for zero-probability conditions ↔ measure theory: relativized systems such as Rényi's, which Popper mentions in n. 12 (p. 352). — from [[popper-1959-logic/appiv-untitled-2]] (analytic-philosophy → other:mathematics)
- [same-math] $p(a,b)=p(ab)/p(b)$ for $p(b)\ne0$ (97) ↔ standard conditional probability — the same ratio formula. — from [[popper-1959-logic/appv-untitled-2]] (analytic-philosophy → unspecified)
- [same-math] Popper's $p(a,b)=\lim \sum a_nb_n/\sum b_n$ ↔ probability: conditional probability as a limiting relative frequency. — from [[popper-1959-logic/appvi-untitled-2]] (analytic-philosophy → other:probability)
