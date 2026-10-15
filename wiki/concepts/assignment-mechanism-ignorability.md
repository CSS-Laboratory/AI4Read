---
id: assignment-mechanism-ignorability
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 19
n_works: 5
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch08-modeling, gelman-2013-bda3/ch14-introduction, hernan-2020-whatif/ch02-randomized, hernan-2020-whatif/ch04-effect, hernan-2020-whatif/ch06-graphical, hernan-2020-whatif/ch07-confounding, hernan-2020-whatif/ch10-random, hernan-2020-whatif/ch12-ip, hernan-2020-whatif/ch13-standardization, hernan-2020-whatif/ch14-g, hernan-2020-whatif/ch15-outcome, hernan-2020-whatif/ch16-instrumental, hernan-2020-whatif/ch17-causal, hernan-2020-whatif/ch18-variable, hernan-2020-whatif/ch19-time, hernan-2020-whatif/ch22-target, holland-1986-statistics/main, murphy-2023-pml2/ch36-causality-p1, pearl-2018-bookofwhy/ch08-counterfactuals]
raw_ids: [Assignment mechanism / ignorability]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# assignment-mechanism-ignorability

## Canon spine entry

- **Assignment mechanism / ignorability** (bayesian): the process deciding who gets treated; if it is independent of potential outcomes given covariates, effects are identifiable (grad)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch08-modeling]] (pp. 202–203): design is ignorable when $p(\theta|x,y_{\rm obs})=p(\theta|x,y_{\rm obs},I)$; sufficient: missing at random plus distinct parameters
- [[gelman-2013-bda3/ch14-introduction]] (p. 360): treatment assignment independent of unobserved outcomes given controls; assumed tentatively for incumbency
- [[hernan-2020-whatif/ch02-randomized]] (p. 14, p. 18): the author's version is exchangeability, $Y^a\perp\!\!\!\perp A$, or conditional exchangeability given $L$; closest canon entry
- [[hernan-2020-whatif/ch04-effect]] (pp. 52, 55): conditional exchangeability $Y^a\perp\!\!\!\perp A|L$ used to give causal meaning to stratum-specific and matched comparisons; partial exchangeability suffices for effects in the treated or untreated
- [[hernan-2020-whatif/ch06-graphical]] (p. 76): willingness to treat Fig. 6.1 as the diagram of an observational study is the graphic translation of conditional exchangeability given $L$
- [[hernan-2020-whatif/ch07-confounding]] (p. 93): here: marginal and conditional exchangeability $Y^a\perp\!\!\!\perp A\,(|L)$
- [[hernan-2020-whatif/ch10-random]] (pp. 140–141): randomization yields exchangeability in the super-population, but only approximate exchangeability in a sample
- [[hernan-2020-whatif/ch12-ip]] (p. 165): here conditional exchangeability $Y^a\perp\!\!\!\perp A|L$ is what lets association in the pseudo-population be causal
- [[hernan-2020-whatif/ch13-standardization]] (p. 175): here called conditional exchangeability given $L$ [as `Assignment mechanism / ignorability`]
- [[hernan-2020-whatif/ch14-g]] (p. 188): here written as $\Pr[A=1\mid Y^{a=0},L]=\Pr[A=1\mid L]$, which is the form used by g-estimation
- [[hernan-2020-whatif/ch15-outcome]] (p. 202): here, conditional exchangeability and positivity given $L$ or $\pi(L)$
- [[hernan-2020-whatif/ch16-instrumental]] (p. 223): IV replaces conditional exchangeability by other assumptions
- [[hernan-2020-whatif/ch17-causal]] (p. 235): here exchangeability given $L$, positivity, consistency
- [[hernan-2020-whatif/ch18-variable]] (p. 241): here "conditional exchangeability", which $L$ must achieve.
- [[hernan-2020-whatif/ch19-time]] (p. 259): the sequential version replaces ordinary conditional exchangeability
- [[hernan-2020-whatif/ch22-target]] (p. 308): here, conditional exchangeability given measured covariates, needed for per-protocol effects
- [[holland-1986-statistics/main]] (p. 948–949): $S$ decides exposure. Independence of $S$ from $Y_t,Y_c$ gives $T=T_{PF}$. Conditional versions are mentioned as "strong ignorability"
- [[murphy-2023-pml2/ch36-causality-p1]] (pp. 1194, 1196): here via "all common causes observed" and RCT random assignment; the term "ignorability" is not used in this unit [weak: not really used in this unit]
- [[pearl-2018-bookofwhy/ch08-counterfactuals]] (pdf 255–256): $Y_x$ independent of received $X$ given $Z$; Pearl says it is in essence exchangeability

## Candidate bridges

- [structural-analogy] Exam-treatment simulation with assignment depending on $x$ ↔ causal inference: assignment mechanism / ignorability — adjusting for the covariate that drives assignment can fail if the outcome model's functional form is wrong (pp. 20–22). — from [[gelman-2020-workflow/main-p1]] (bayesian → bayesian)
- [structural-analogy] Host's rule for opening doors (forced vs. random vs. earthquake) ↔ bayesian: assignment mechanism / ignorability; how an observation arose determines what it means. — from [[mackay-2003-information/ch03-more]] (information-theory → bayesian)
