---
id: pearl-2016-primer/index
work: pearl-2016-primer
type: work-map
units: [pearl-2016-primer/ch01-preliminaries, pearl-2016-primer/ch02-graphical, pearl-2016-primer/ch03-effects, pearl-2016-primer/ch04-counterfactuals]
---

# Pearl, J., Glymour, M., & Jewell, N. P. (2016). *Causal Inference in Statistics: A Primer*. Chichester: Wiley.

## In one paragraph
Data alone cannot answer causal questions. The same numbers can need opposite readings depending on the causal story behind them, as Simpson's paradox shows. The book therefore builds a formal language for causal assumptions, structural causal models and their graphs. It shows how a graph predicts which variables are independent (d-separation), so the model can be tested against data. It then separates intervening, $do(x)$, from conditioning. With a valid graph, the effect of an intervention can often be computed from observational data, using the adjustment formula, the back-door and front-door criteria, and weighting. Finally, counterfactuals extend the framework to individuals and self-selected groups. They cover treatment on the treated, probabilities of necessity and sufficiency, and direct and indirect effects. The result is working fluency with DAGs.

## The path through the work
- [[pearl-2016-primer/ch01-preliminaries]] — The same numbers can demand opposite readings depending on the causal story that generated them, so statistics needs a formal language for causal assumptions: structural causal models and their graphs.
- [[pearl-2016-primer/ch02-graphical]] — The shape of a causal graph alone tells us which variables are independent, given which others (via chains, forks, colliders and d-separation), so data can test the graph (assuming the error terms are independent).
- [[pearl-2016-primer/ch03-effects]] — If a causal graph is valid, the effect of setting a variable, $P(y\mid do(x))$, can often be computed from purely observational data by removing the arrows into that variable and adjusting for the right covariates.
- [[pearl-2016-primer/ch04-counterfactuals]] — A counterfactual $Y_x(u)$ is the value $Y$ takes in unit $u$'s world after the equation for $X$ is replaced by $X=x$. This lets one compute and, under conditions, estimate individual-level and self-selected-group causal quantities (treatment on the treated, necessity, mediation) that the do-operator cannot express.

## Big ideas across units
- **Data alone cannot settle causal questions.** Simpson's paradox is introduced in Ch. 1, linked to graph structure in Ch. 2, and resolved with the adjustment formula once a graph is given in Ch. 3. Units: ch01, ch02, ch03.
- **A causal model is a set of structural equations with a graph.** The SCM and its acyclic graph appear in Ch. 1. They are used to read off independencies in Ch. 2. They are surgically modified in Ch. 3 and Ch. 4. Units: ch01, ch02, ch03, ch04.
- **Graph shape determines independence.** Chains, forks and colliders, and d-separation, give testable implications and equivalence classes (Ch. 2). The same rules guide covariate choice in Ch. 3 and Ch. 4. Conditioning on a collider can create bias. Units: ch01 (Monty Hall, conditioning as filtering), ch02, ch03, ch04.
- **Intervening is not conditioning.** $do(X=x)$ deletes the arrows into $X$ (graph surgery), while conditioning only selects a subpopulation. The same surgery defines counterfactuals in Ch. 4. Units: ch03, ch04.
- **Identifying causal effects from observational data.** The adjustment formula, truncated product, back-door and front-door criteria, and inverse probability weighting all do this. Back-door sets also give the Ch. 4 result that $Y_x$ is independent of $X$ given $Z$. Units: ch03, ch04.
- **Direct and indirect effects (mediation).** Conditioning on a mediator can open a collider path. The controlled direct effect (CDE) is defined by intervention in Ch. 3. Natural direct and indirect effects use nested counterfactuals in Ch. 4. Units: ch03, ch04.
- **Linear models as a special case.** Regression and partial regression coefficients are reviewed in Ch. 1. Path coefficients, regression on back-door sets and instruments are used in Ch. 3. Ch. 4 turns population slopes into individual-level counterfactuals. Units: ch01, ch03, ch04.
- **Models are testable, and causal quantities go beyond averages.** Failed d-separation tests refute a model (Ch. 2). Counterfactuals add individual-level and legal-style quantities (PN, PS, PNS) that need extra conditions such as monotonicity (Ch. 4). Units: ch02, ch04.

## How to read it
- **Essential:** all four units form one chain. Ch. 1's SCM and DAG material, Ch. 2's d-separation and Ch. 3's do-operator, adjustment and back-door criterion are needed for everything after them.
- **Dependencies:** Ch. 2 needs the DAG and SCM basics from Ch. 1. Ch. 3 needs d-separation and colliders (Ch. 2), conditional probability, the law of total probability, and linear regression. Ch. 4 needs the do-operator, surgery, back-door criterion and adjustment formula (Ch. 3), plus d-separation and simple linear models.
- **Can be skimmed on a first pass:** in Ch. 1, the probability and regression review, if you already know it. The Simpson's paradox discussion and the SCM section should not be skipped. In Ch. 3, the later topics (conditional policies and weighting, linear-system identification) build on the core of surgery, adjustment, back-door and front-door. In Ch. 4, the probabilities of causation and mediation sections come after the core definition and three-step computation.
- **Access:** the author posts Ch. 1–2 in full online.

## Concepts introduced
Ch. 2 uses `structural-causal-model-scm` where Ch. 1, 3 and 4 use `structural-causal-model`. The digests treat them as the same notion, so both ids are listed.

**Chapter 1**
- [[simpsons-paradox]] — ch01
- [[confounding-vs-selection-bias]] — ch01
- [[causation-definition-listening]] — ch01
- [[conditional-probability]] — ch01
- [[independence-conditional-independence]] — ch01
- [[law-of-total-probability]] — ch01
- [[bayes-theorem]] — ch01
- [[prior-distribution]] — ch01
- [[subjective-probability]] — ch01
- [[expected-value-best-guess]] — ch01
- [[variance-covariance-correlation]] — ch01
- [[linear-regression-slope]] — ch01
- [[partial-regression-coefficient]] — ch01
- [[orthogonality-principle]] — ch01
- [[causal-dag]] — ch01
- [[structural-causal-model]] — ch01
- [[exogenous-endogenous-variables]] — ch01
- [[product-decomposition]] — ch01
- [[curse-of-dimensionality]] — ch01

**Chapter 2**
- [[d-separation]] — ch02
- [[fork-chain-collider]] — ch02
- [[structural-causal-model-scm]] — ch02
- [[conditional-independence]] — ch02
- [[intransitive-case]] — ch02
- [[v-structure]] — ch02
- [[equivalence-class]] — ch02
- [[testable-implications]] — ch02

**Chapter 3**
- [[do-operator]] — ch03
- [[graph-surgery]] — ch03
- [[adjustment-formula]] — ch03
- [[average-causal-effect]] — ch03
- [[truncated-product-formula]] — ch03
- [[back-door-front-door-criterion]] — ch03
- [[propensity-score]] — ch03
- [[inverse-probability-weighting]] — ch03
- [[z-specific-effect]] — ch03
- [[controlled-direct-effect]] — ch03
- [[path-coefficient]] — ch03
- [[instrumental-variable]] — ch03

**Chapter 4**
- [[counterfactual]] — ch04
- [[potential-outcomes]] — ch04
- [[fundamental-problem-of-causal-inference]] — ch04
- [[surgical-modification-law]] — ch04
- [[consistency-rule]] — ch04
- [[abduction-action-prediction]] — ch04
- [[cross-world-probability]] — ch04
- [[conditional-ignorability]] — ch04
- [[effect-of-treatment-on-the-treated]] — ch04
- [[additive-intervention]] — ch04
- [[probability-of-necessity]] — ch04
- [[probability-of-sufficiency]] — ch04
- [[probability-of-necessity-and-sufficiency]] — ch04
- [[monotonicity]] — ch04
- [[excess-risk-ratio-confounding-factor]] — ch04
- [[natural-direct-effect]] — ch04
- [[natural-indirect-effect]] — ch04
- [[mediation-formula]] — ch04
