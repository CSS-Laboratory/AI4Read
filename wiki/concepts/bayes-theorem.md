---
id: bayes-theorem
type: concept
curated: 2026-10-15
fields: [bayesian, information-theory, decision-game-theory, llm, analytic-philosophy, linear-algebra]
level: HS
grounding: digests
aliases: [bayes-rule]
sources: [bayes-1763-essay/main, gelman-2013-bda3/ch01-probability, mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/ch03-sampling, pearl-2016-primer/ch01-preliminaries, jaynes-2003-probability/ch04-elementary, jaynes-2003-probability/ch14-simple, jaynes-2003-probability/appa-other, murphy-2023-pml2/ch02-probability-p1, murphy-2023-pml2/ch07-inference, tenenbaum-2011-grow/main, mcgrayne-2011-theory/ch04-bayes, mackay-2003-information/ch01-introduction, mackay-2003-information/ch02-probability, mackay-2003-information/ch28-model, stone-2022-information/appf-rules, dixit-2008-art-strategy/ch08-interpreting, kahneman-2011-thinking/ch14-tom, kahneman-2011-thinking/appa-judgment, osborne-2004-introduction/ch17-mathematics, prince-2023-udl/ch23-probability, deisenroth-2020-mml/ch06-probability-p1, godfreysmith-2003-theory/ch14-bayesianism, popper-1959-logic/appii-following, gelman-2013-bda3/ch09-decision, grimmer-2013-textasdata/main, welch-2004-kalmanintro/main, pearl-2018-bookofwhy/ch06-paradoxes]
links: [prior-distribution, posterior-distribution, likelihood, marginal-likelihood, base-rate-neglect, bayesian-confirmation, naive-bayes-classifier, kalman-filter]
generated_version: wiki/kg/hub-sources/bayes-theorem.md
---

# Bayes' theorem

**Gist.** Bayes' theorem turns "how likely is the evidence if the hypothesis is true" into "how likely is the hypothesis now that I have the evidence": posterior = likelihood × prior / evidence.

59 digests in six fields use it (full list in the generated version). The id `bayes-rule` (used by the game-theory, decision and LLM texts) is merged here.

## How each field uses it

### Bayesian theory & modeling (home field)
- “here shown as Prop. 5/Prop. 9: probability of the first event given the second equals probability of both divided by probability of the second” — [[bayes-1763-essay/main]] (pp. 15–16, 22)
- “$p(\theta|y)=p(\theta)p(y|\theta)/p(y)$; the unnormalised form is $\propto p(\theta)p(y|\theta)$” — [[gelman-2013-bda3/ch01-probability]] (p. 7)
- “posterior = likelihood × prior / average likelihood, derived by equating two factorisations of the joint probability” — [[mcelreath-2020-rethinking/ch02-small]] (p. 37)
- “(4.3) as the product rule rearranged; "prior" and "posterior" are logical, not temporal” — [[jaynes-2003-probability/ch04-elementary]] (pp. 87–89)
- “posterior = prior × likelihood / $p(\mathcal D)$; $p(\mathcal D)$ is the bottleneck” — [[murphy-2023-pml2/ch07-inference]] (p. 345)
- “Eq. (1): posterior proportional to prior × likelihood, normalized over hypothesis space $H$” (Bayesian models of cognition) — [[tenenbaum-2011-grow/main]] (p. 1280)

### Information theory
- “used for optimal decoding, with posterior ∝ likelihood × prior” — [[mackay-2003-information/ch01-introduction]] (p. 6)
- “used for posterior over parameters (28.4) and over models (28.6)” — [[mackay-2003-information/ch28-model]] (pp. 347–348)
- “posterior = likelihood × prior / marginal likelihood” — [[stone-2022-information/appf-rules]] (p. 262)

### Decision & game theory
- “updating the probability of a type after seeing an action: joint chance divided by the chance of the action” — [[dixit-2008-art-strategy/ch08-interpreting]] (p. 246)
- “combines prior belief with diagnosticity of evidence; here, base rate plus evidence strength” — [[kahneman-2011-thinking/ch14-tom]] (pdf 151)
- “formulas (453.2) and (454.2) for updating a prior given evidence” — [[osborne-2004-introduction/ch17-mathematics]] (pp. 453–454)

### Large language models / ML textbooks
- “posterior = likelihood × prior / evidence” — [[prince-2023-udl/ch23-probability]] (p. 452)

### Linear algebra (ML mathematics)
- “posterior = likelihood × prior / evidence, a consequence of the product rule” — [[deisenroth-2020-mml/ch06-probability-p1]] (p. 185)

### Analytic philosophy
- “$P(h|e)=P(e|h)P(h)/P(e)$, a consequence of axiom 4” — [[godfreysmith-2003-theory/ch14-bayesianism]] (pp. 203, 207)

## Bridges between fields

- **same-math** (decision theory → Bayesian): “Base-rate neglect ↔ Bayes' rule: posterior odds = prior odds × likelihood ratio; the 5.44 factor is the ratio of the prior odds in the two conditions, $(7/3)\div(3/7)=(.7/.3)^2$.” — [[kahneman-2011-thinking/appa-judgment]]. Justification: the experiment's numbers are checked with the odds form of the theorem.
- **same-math** (analytic philosophy → Bayesian): “fourth form of Bayes $(4_s)$ ↔ Bayesian confirmation: posterior from priors and likelihoods — same formula, but here read as frequencies in a finite class, not degrees of belief.” — [[popper-1959-logic/appii-following]]. Justification: one formula, two interpretations of probability.
- **same-math** (political science → ML): “Naïve Bayes classification ↔ statistics/ML: Bayes' rule with conditional independence of features given the class — the equation is the standard one.” — [[grimmer-2013-textasdata/main]]. Justification: the text classifier is the theorem plus an independence assumption.
- **structural-analogy** (Bayesian → decision theory): “Discrete Bayes update after a test (p. 245) ↔ base-rate neglect: the prior (0.9) and the test's error rates combine by Bayes' theorem.” — [[gelman-2013-bda3/ch09-decision]]. Justification: same diagnostic-test shape that people get wrong.
- **structural-analogy** (control theory → Bayesian): “Predict–correct cycle ↔ Bayesian updating: the paper links the filter's justification to conditioning on past measurements (Bayes' rule) (p. 4).” — [[welch-2004-kalmanintro/main]]. Justification: the Kalman filter's correct step is an update on new data.
- **structural-analogy** (Bayesian → ML): “word-by-word odds updating ↔ machine learning: naive Bayes text classifier — evidence from many features combined into one score; the text does not state independence.” — [[mcgrayne-2011-theory/ch12-who]]. Justification: the Federalist-papers study updates odds feature by feature.

## Where definitions disagree

- **What is it a consequence of?** Most digests derive it from the product rule or the definition of conditional probability (e.g. “rule (2.15) obtained from the definition of conditional probability, for events with positive probability” — [[murphy-2023-pml2/ch02-probability-p1]] (p. 8)). Jaynes derives it from logic: “for Jaynes, a consequence of Boolean associativity and commutativity, used without restriction” — [[jaynes-2003-probability/appa-other]] (p. 654). Godfrey-Smith states it as a consequence of an axiom (quote above).
- **Is "prior" earlier in time?** Jaynes: “"prior" and "posterior" are logical, not temporal” — [[jaynes-2003-probability/ch04-elementary]]. The historical and applied digests describe updating as data arrive (e.g. McGrayne: “rule for turning evidence into updated odds, used here as hunch-weighing; Turing talked about bans, not Bayes” — [[mcgrayne-2011-theory/ch04-bayes]] (pp. 67–69)).
- **Degrees of belief vs. frequencies.** Popper uses the same formula for frequencies in a finite class (bridge above), not for degrees of belief.
- **Evidence for a hypothesis that survived a test.** Pearl's digest uses the theorem to explain why “belief rises for a hypothesis that survived a test that threatened it” — [[pearl-2018-bookofwhy/ch06-paradoxes]] (pdf 182); see also [[bayesian-confirmation]].

## Digests

Bayesian: [[bayes-1763-essay/main]], [[gelman-2013-bda3/ch01-probability]], [[gelman-2013-bda3/ch09-decision]], [[mcelreath-2020-rethinking/ch02-small]], [[mcelreath-2020-rethinking/ch03-sampling]], [[pearl-2016-primer/ch01-preliminaries]], [[pearl-2018-bookofwhy/ch06-paradoxes]], [[jaynes-2003-probability/ch04-elementary]], [[jaynes-2003-probability/ch14-simple]], [[jaynes-2003-probability/appa-other]], [[murphy-2023-pml2/ch02-probability-p1]], [[murphy-2023-pml2/ch07-inference]], [[tenenbaum-2011-grow/main]], [[mcgrayne-2011-theory/ch04-bayes]], [[mcgrayne-2011-theory/ch12-who]] ·
Information theory: [[mackay-2003-information/ch01-introduction]], [[mackay-2003-information/ch02-probability]], [[mackay-2003-information/ch28-model]], [[stone-2022-information/appf-rules]] ·
Decision & game theory: [[dixit-2008-art-strategy/ch08-interpreting]], [[kahneman-2011-thinking/ch14-tom]], [[kahneman-2011-thinking/appa-judgment]], [[osborne-2004-introduction/ch17-mathematics]] ·
LLMs / ML: [[prince-2023-udl/ch23-probability]] · Linear algebra: [[deisenroth-2020-mml/ch06-probability-p1]] ·
Analytic philosophy: [[godfreysmith-2003-theory/ch14-bayesianism]], [[popper-1959-logic/appii-following]] ·
Political science: [[grimmer-2013-textasdata/main]] · Control theory: [[welch-2004-kalmanintro/main]]
