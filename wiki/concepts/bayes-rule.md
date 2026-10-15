---
id: bayes-rule
type: concept
fields: [decision-game-theory, information-theory, llm]
n_sources: 5
tiers: [core, reference]
grounding: digests
sources: [dixit-2008-art-strategy/ch08-interpreting, kahneman-2011-thinking/ch14-tom, osborne-2004-introduction/ch17-mathematics, prince-2023-udl/ch23-probability, stone-2022-information/appf-rules]
generated_by: build_kg.py
---

# bayes-rule

## Definitions in the sources

### decision-game-theory

- [[dixit-2008-art-strategy/ch08-interpreting]] (p. 246): updating the probability of a type after seeing an action: joint chance divided by the chance of the action [new]
- [[kahneman-2011-thinking/ch14-tom]] (pdf 151): combines prior belief with diagnosticity of evidence; here, base rate plus evidence strength [new]
- [[osborne-2004-introduction/ch17-mathematics]] (pp. 453–454): formulas (453.2) and (454.2) for updating a prior given evidence [new]

### information-theory

- [[stone-2022-information/appf-rules]] (p. 262): posterior = likelihood × prior / marginal likelihood [new]

### llm

- [[prince-2023-udl/ch23-probability]] (p. 452): posterior = likelihood × prior / evidence [new]

## Instances that use it

- [[cornfield-1951-risk-bridge]] — Bayes' rule from case-control data to risk — from [[mcgrayne-2011-theory/ch08-jerome]]
- [[casino-craps-roulette-11]] — Bayes' rule, $P(\text{craps}|\text{“11”})=0.679$ — from [[pearl-2016-primer/ch01-preliminaries]]

## Candidate bridges

- [same-math] Bayes' Rule in the poker example ↔ probability/statistics: posterior = joint probability ÷ marginal — the same formula applied to a bid. — from [[dixit-2008-art-strategy/ch08-interpreting]] (decision-game-theory → other)
- [same-math] Naïve Bayes classification ↔ statistics/ML: Bayes' rule with conditional independence of features given the class — the equation is the standard one. — from [[grimmer-2013-textasdata/main]] (political-science → other)
- [same-math] Base-rate neglect ↔ Bayes' rule: posterior odds = prior odds × likelihood ratio; the 5.44 factor is the ratio of the prior odds in the two conditions, $(7/3)\div(3/7)=(.7/.3)^2$. — from [[kahneman-2011-thinking/appa-judgment]] (decision-game-theory → bayesian)
- [same-math] Base rate plus witness reliability ↔ probability: Bayes' rule with prior 0.15 and likelihood ratio 4:1 gives 0.12/0.29. — from [[kahneman-2011-thinking/ch16-causes]] (decision-game-theory → other)
- [same-math] Posterior belief after hearing "better" ↔ statistics: Bayes' rule over speaker types (fn. 19–20). — from [[lupia-1998-dilemma/ch03-people]] (political-science → other)
- [same-math] Kalman filter as derived from Bayes' rule (Aoki 1967) ↔ bayesian: sequential updating — the author says it can be derived directly from Bayes' rule (p. 205). — from [[mcgrayne-2011-theory/ch15-navy]] (bayesian → bayesian)
- [same-math] DRE trick via Bayes' rule ↔ Bayes' theorem — posterior odds times prior odds correction gives the likelihood ratio. — from [[murphy-2023-pml2/ch02-probability-p3]] (bayesian → unspecified)
- [structural-analogy] Bayesian posterior as the KL-minimizing constrained update ↔ Bayes' theorem: the text says Bayes' rule alone is a trivial chain-rule identity, while the KL view gives a principle for updating (§5.1.7). — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → bayesian)
- [metaphor] Logit adjustment ↔ Bayes' rule with changed priors: dividing by $\pi_y$ removes the label prior. — from [[murphy-2023-pml2/ch15-generalized]] (bayesian → bayesian)
- [structural-analogy] NCE ↔ logistic regression / classifier-based density-ratio estimation: the classifier is linked to the density ratio via Bayes' rule (p. 861). — from [[murphy-2023-pml2/ch24-energy]] (bayesian → other)
- [structural-analogy] Scaled likelihood trick ↔ Bayes' rule: $p(y\mid z)\propto p(z\mid y)/p(z)$ (29.17). — from [[murphy-2023-pml2/ch29-state-p1]] (bayesian → bayesian)
- [same-math] Bayes' rule with states and signals ↔ Bayesian game / Bayesian Nash equilibrium: beliefs about types updated on a signal. — from [[osborne-2004-introduction/ch17-mathematics]] (decision-game-theory → bayesian)
- [same-math] Bayes' rule with prior ↔ Bayesian inference: posterior ∝ likelihood × prior — same formula (1.8), with the hypothesis as $A$ and the evidence as $B$. — from [[pearl-2016-primer/ch01-preliminaries]] (bayesian → bayesian)
- [metaphor] Bayes' rule posterior ↔ language models: Bayesian reading of conditioning on a prompt (canon link; not stated here). — from [[prince-2023-udl/ch23-probability]] (llm → llm)
- [same-math] Exercise 1.3 (package choice) ↔ Bayes' rule on a discrete hypothesis — a posterior update after evidence. — from [[sarkka-2023-bayesianfiltering/ch01-are]] (control-theory → unspecified)
- [structural-analogy] Bayes' rule (prior → posterior) ↔ statistics: updating beliefs after data. — from [[stone-2022-information/appf-rules]] (information-theory → other)
- [structural-analogy] Predict–correct cycle ↔ Bayesian updating: the paper links the filter's justification to conditioning on past measurements (Bayes' rule) (p. 4). — from [[welch-2004-kalmanintro/main]] (control-theory → bayesian)
