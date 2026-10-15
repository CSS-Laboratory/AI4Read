---
id: pearl-2018-bookofwhy/index
work: pearl-2018-bookofwhy
type: work-map
units: [pearl-2018-bookofwhy/ch00-introduction, pearl-2018-bookofwhy/ch01-ladder, pearl-2018-bookofwhy/ch02-buccaneers, pearl-2018-bookofwhy/ch03-evidence, pearl-2018-bookofwhy/ch04-confounding, pearl-2018-bookofwhy/ch05-smoke, pearl-2018-bookofwhy/ch06-paradoxes, pearl-2018-bookofwhy/ch07-beyond, pearl-2018-bookofwhy/ch08-counterfactuals, pearl-2018-bookofwhy/ch09-mediation-p1, pearl-2018-bookofwhy/ch09-mediation-p2, pearl-2018-bookofwhy/ch10-big]
---

# Pearl, J., & Mackenzie, D. (2018). *The Book of Why: The New Science of Cause and Effect*. New York: Basic Books.

## In one paragraph
Pearl argues that statistics long lacked a language for causes, and that a "Causal Revolution" now supplies one: causal diagrams to state what we know, and the do-operator to state what we want to know. The organizing image is the Ladder of Causation: seeing (association), doing (intervention) and imagining (counterfactuals). Data alone cannot get above the first rung without a causal model. The book tells the history behind this view (Galton, Pearson, Wright, the smoking debate). It then shows how diagrams settle confounding, paradoxes, unmeasured confounders, individual-level "what if" questions and the "how" of mediation. It ends with implications for Big Data and AI. The book is opinionated, especially about statistics' history. Its main message is that you are smarter than your data.

## The path through the work
- [[pearl-2018-bookofwhy/ch00-introduction]] — Statistics long lacked a language for causes; the "Causal Revolution" supplies one (diagrams plus the do-operator), and with it causal questions can be answered by combining a causal model with data, because data alone are "profoundly dumb" about causes.
- [[pearl-2018-bookofwhy/ch01-ladder]] — Pearl's Ladder of Causation has three rungs (seeing, doing, imagining), each answering questions the lower rungs cannot, and passive data alone, without a causal model, cannot lift a reasoner above the first rung.
- [[pearl-2018-bookofwhy/ch02-buccaneers]] — Galton went looking for a causal law of heredity and found correlation, which has no causal direction. Pearson then worked to remove causation from statistics, and Sewall Wright's path diagrams were the first direct challenge to that culture.
- [[pearl-2018-bookofwhy/ch03-evidence]] — Bayes's rule lets us turn easy "forward" probabilities (effect given cause) into the "inverse" probabilities we need (cause given effect), and Bayesian networks, built from chains, forks and colliders, extend this to many variables and form the probabilistic base of causal diagrams.
- [[pearl-2018-bookofwhy/ch04-confounding]] — Pearl argues that confounding is a causal idea, defined as P(Y | X) ≠ P(Y | do(X)), so the back-door criterion on a causal diagram, not a statistical test or a randomized trial, tells you what to adjust for.
- [[pearl-2018-bookofwhy/ch05-smoke]] — Lacking a formal theory of causation, scientists reached "smoking causes cancer" using many kinds of evidence and informal criteria, and a causal diagram later explained a leftover puzzle, the birth-weight paradox, as collider bias.
- [[pearl-2018-bookofwhy/ch06-paradoxes]] — Pearl argues that many famous paradoxes come from a tension between causal intuition and the logic of proportions in data, and that a causal diagram of how the data were generated settles them.
- [[pearl-2018-bookofwhy/ch07-beyond]] — When a confounder cannot be measured, causal effects can sometimes still be computed from observational data, using the front-door formula, instrumental variables, or the general do-calculus.
- [[pearl-2018-bookofwhy/ch08-counterfactuals]] — Given a structural causal model, a counterfactual about a particular individual or event can be computed in three steps (abduction, action, prediction), which lets us ask about blame, necessity and sufficiency in law and climate science.
- [[pearl-2018-bookofwhy/ch09-mediation-p1]] — To ask *how* a cause works, we must separate direct from indirect effects, which means holding a mediator constant (or setting it counterfactually) rather than just conditioning on it, and indirect effects need rung-three counterfactuals.
- [[pearl-2018-bookofwhy/ch09-mediation-p2]] — In nonlinear models "direct" and "indirect" effects can be defined as counterfactual quantities (natural direct and indirect effects), and the Mediation Formula lets us estimate them from data under explicit graph assumptions.
- [[pearl-2018-bookofwhy/ch10-big]] — Pearl argues that Big Data and AI cannot answer "Why?" without causal models, and that machines given causal models, counterfactual reasoning and a model of themselves could acquire agency and morality.

## Big ideas across units
- **Data alone stay on the bottom rung.** Without a causal model, data cannot answer intervention or counterfactual questions. This idea frames the book and returns in the history and in AI. Units: [[pearl-2018-bookofwhy/ch00-introduction]], [[pearl-2018-bookofwhy/ch01-ladder]], [[pearl-2018-bookofwhy/ch02-buccaneers]], [[pearl-2018-bookofwhy/ch08-counterfactuals]], [[pearl-2018-bookofwhy/ch10-big]].
- **Seeing is not doing.** P(Y | X) differs from P(Y | do(X)). The do-operator makes the difference explicit, defines confounding, and underlies the adjustment and identification tools. Units: [[pearl-2018-bookofwhy/ch00-introduction]], [[pearl-2018-bookofwhy/ch01-ladder]], [[pearl-2018-bookofwhy/ch04-confounding]], [[pearl-2018-bookofwhy/ch07-beyond]], [[pearl-2018-bookofwhy/ch09-mediation-p1]].
- **Diagrams carry the causal assumptions.** The path runs from Wright's path diagrams to Bayesian networks, whose chain, fork and collider junctions leave fingerprints in data, to causal diagrams. Their structure says what the data cannot. Units: [[pearl-2018-bookofwhy/ch01-ladder]], [[pearl-2018-bookofwhy/ch02-buccaneers]], [[pearl-2018-bookofwhy/ch03-evidence]], [[pearl-2018-bookofwhy/ch04-confounding]], [[pearl-2018-bookofwhy/ch06-paradoxes]].
- **Causal assumptions are explicit and partly subjective, but inference is then objective.** Causal conclusions need causal hypotheses. Once these are stated in a diagram, they can be debated and sometimes tested. Units: [[pearl-2018-bookofwhy/ch02-buccaneers]], [[pearl-2018-bookofwhy/ch04-confounding]], [[pearl-2018-bookofwhy/ch07-beyond]], [[pearl-2018-bookofwhy/ch08-counterfactuals]].
- **Collider bias explains many puzzles.** Conditioning on a common effect creates a dependence with no cause. This accounts for M-bias, the birth-weight paradox, and the Monty Hall and Berkson paradoxes. It is also an early warning (Burks) about conditioning on effects. Units: [[pearl-2018-bookofwhy/ch03-evidence]], [[pearl-2018-bookofwhy/ch04-confounding]], [[pearl-2018-bookofwhy/ch05-smoke]], [[pearl-2018-bookofwhy/ch06-paradoxes]], [[pearl-2018-bookofwhy/ch09-mediation-p1]].
- **What to adjust for depends on the causal story, and controlling for everything is wrong.** The back-door criterion gives a rule. Simpson's and Lord's paradoxes are resolved by it (confounder: stratify; mediator: pool). When back-door adjustment is impossible, front-door, instrumental variables and the do-calculus extend what can be identified. Units: [[pearl-2018-bookofwhy/ch04-confounding]], [[pearl-2018-bookofwhy/ch06-paradoxes]], [[pearl-2018-bookofwhy/ch07-beyond]], [[pearl-2018-bookofwhy/ch10-big]].
- **Counterfactuals are computed from a structural causal model.** Abduction, action and prediction give individual-level answers: necessity and sufficiency, blame and credit, and natural direct and indirect effects. Units: [[pearl-2018-bookofwhy/ch00-introduction]], [[pearl-2018-bookofwhy/ch01-ladder]], [[pearl-2018-bookofwhy/ch08-counterfactuals]], [[pearl-2018-bookofwhy/ch09-mediation-p1]], [[pearl-2018-bookofwhy/ch09-mediation-p2]], [[pearl-2018-bookofwhy/ch10-big]].
- **Mechanisms need more than conditioning.** Asking "how" requires separating direct from indirect effects. Conditioning on a mediator is not holding it constant, and the product-of-coefficients rule fails outside linear models. Units: [[pearl-2018-bookofwhy/ch04-confounding]], [[pearl-2018-bookofwhy/ch06-paradoxes]], [[pearl-2018-bookofwhy/ch09-mediation-p1]], [[pearl-2018-bookofwhy/ch09-mediation-p2]].

## How to read it
- **Essential first:** [[pearl-2018-bookofwhy/ch00-introduction]] and [[pearl-2018-bookofwhy/ch01-ladder]] set the framework. Then [[pearl-2018-bookofwhy/ch03-evidence]] (chains, forks, colliders) and [[pearl-2018-bookofwhy/ch04-confounding]] (back-door criterion) give the core working tools.
- **Dependencies (from the stated prerequisites):**
  - Ch. 2 assumes the Ladder from Ch. 1.
  - Ch. 4 assumes diagrams and colliders (Ch. 3) and the do-operator idea (Chs. 1, 3).
  - Ch. 6 assumes confounder, collider, mediator and back-door path.
  - Ch. 7 assumes the back-door criterion and the do-operator.
  - Ch. 8 assumes the do-operator, back-door paths and d-separation.
  - Ch. 9 (both parts) assumes the do-operator and the Ladder. Part 2 continues part 1.
  - Ch. 10 assumes Bayesian networks (Ch. 3), the do-calculus (Ch. 7) and counterfactuals (Ch. 8).
- **Can be skimmed on a first pass:** the historical chapters [[pearl-2018-bookofwhy/ch02-buccaneers]] and [[pearl-2018-bookofwhy/ch05-smoke]] add context and intuition more than tools. The exception is the birth-weight collider story in Ch. 5. The technical parts of [[pearl-2018-bookofwhy/ch07-beyond]] (the do-calculus rules, completeness) can also wait. [[pearl-2018-bookofwhy/ch10-big]] is a reflective closing on AI and can be read independently once the Ladder is clear.
- **Caution:** the catalog entry describes the book as opinionated about statistics' history. Read it alongside Holland and Imbens & Rubin as a counterweight.

## Concepts introduced
- [[do-operator]] — [[pearl-2018-bookofwhy/ch00-introduction]]
- [[causal-dag]] — ch00-introduction
- [[ladder-of-causation]] — ch00-introduction
- [[confounding-vs-selection-bias]] — ch00-introduction
- [[propensity-score]] — ch00-introduction
- [[simpsons-paradox]] — ch00-introduction (the variant id `simpson-s-paradox` in ch09-mediation-p2 refers to the same concept)
- [[frequentist-vs-bayesian]] — ch00-introduction
- [[causal-inference-engine]] — ch00-introduction
- [[estimand]] — ch00-introduction
- [[counterfactual]] — ch00-introduction
- [[testable-implications]] — ch00-introduction
- [[randomized-controlled-trial]] — ch00-introduction
- [[mediation]] — ch00-introduction
- [[graph-surgery]] — ch01-ladder
- [[mini-turing-test]] — ch01-ladder
- [[probability-raising]] — ch01-ladder
- [[bayesian-network]] — ch01-ladder
- [[regression-to-the-mean]] — ch02-buccaneers
- [[correlation-coefficient]] — ch02-buccaneers
- [[spurious-correlation]] — ch02-buccaneers
- [[path-coefficient]] — ch02-buccaneers
- [[path-analysis]] — ch02-buccaneers
- [[positivism]] — ch02-buccaneers
- [[prior-distribution]] — ch02-buccaneers
- [[bayes-theorem]] — ch03-evidence
- [[likelihood]] — ch03-evidence
- [[posterior-distribution]] — ch03-evidence
- [[base-rate-neglect]] — ch03-evidence
- [[inverse-probability]] — ch03-evidence
- [[likelihood-ratio]] — ch03-evidence
- [[belief-propagation]] — ch03-evidence
- [[conditional-probability-table]] — ch03-evidence
- [[conditional-independence]] — ch03-evidence
- [[fork-chain-collider]] — ch03-evidence
- [[collider-bias]] — ch03-evidence
- [[d-separation]] — ch03-evidence
- [[confounding]] — ch04-confounding
- [[deconfounder]] — ch04-confounding
- [[back-door-front-door-criterion]] — ch04-confounding
- [[potential-outcomes]] — ch04-confounding
- [[exchangeability]] — ch04-confounding
- [[mediator]] — ch04-confounding
- [[m-bias]] — ch04-confounding
- [[noncollapsibility-test]] — ch04-confounding
- [[overcontrolling]] — ch04-confounding
- [[case-control-study]] — ch05-smoke
- [[dose-response-effect]] — ch05-smoke
- [[cornfield-inequality]] — ch05-smoke
- [[sensitivity-analysis]] — ch05-smoke
- [[hills-criteria]] — ch05-smoke
- [[explaining-away]] — ch05-smoke
- [[simpsons-reversal]] — ch06-paradoxes
- [[data-generating-process]] — ch06-paradoxes
- [[sure-thing-principle]] — ch06-paradoxes
- [[common-cause-principle]] — ch06-paradoxes
- [[lords-paradox]] — ch06-paradoxes
- [[do-calculus]] — ch07-beyond
- [[instrumental-variable]] — ch07-beyond
- [[mendelian-randomization]] — ch07-beyond
- [[monotonicity-noncompliance]] — ch07-beyond
- [[partial-regression-coefficient]] — ch07-beyond
- [[curse-of-dimensionality]] — ch07-beyond
- [[completeness-do-calculus]] — ch07-beyond
- [[transportability]] — ch07-beyond
- [[local-average-treatment-effect]] — ch07-beyond
- [[fundamental-problem-of-causal-inference]] — ch08-counterfactuals
- [[structural-causal-model]] — ch08-counterfactuals
- [[abduction-action-prediction]] — ch08-counterfactuals
- [[assignment-mechanism-ignorability]] — ch08-counterfactuals
- [[sutva]] — ch08-counterfactuals
- [[probability-of-necessity]] — ch08-counterfactuals
- [[probability-of-sufficiency]] — ch08-counterfactuals
- [[fraction-of-attributable-risk]] — ch08-counterfactuals
- [[mediation-direct-indirect-effect]] — ch08-counterfactuals
- [[direct-indirect-effect]] — ch09-mediation-p1
- [[mediation-fallacy]] — ch09-mediation-p1
- [[controlled-direct-effect]] — ch09-mediation-p1
- [[natural-direct-effect]] — ch09-mediation-p1
- [[natural-indirect-effect]] — ch09-mediation-p1
- [[mediation-formula]] — ch09-mediation-p1
- [[bias-vs-discrimination]] — ch09-mediation-p1
- [[interaction-moderation]] — ch09-mediation-p2
- [[sum-of-products-rule]] — ch09-mediation-p2
- [[baron-kenny-method]] — ch09-mediation-p2
- [[external-validity]] — ch10-big
- [[selection-variable-S]] — ch10-big
- [[effect-of-treatment-on-the-treated]] — ch10-big
- [[strong-ai-agency]] — ch10-big
- [[compatibilism]] — ch10-big
- [[rule-based-systems]] — ch10-big
