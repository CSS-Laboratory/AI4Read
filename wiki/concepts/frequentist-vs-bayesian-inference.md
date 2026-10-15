---
id: frequentist-vs-bayesian-inference
type: concept
fields: [bayesian, information-theory]
n_sources: 25
tiers: [reference, core, deep]
grounding: digests
sources: [efron-1986-bayesian/main, gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch04-asymptotics, gelman-2013-philosophy/main, hernan-2020-whatif/ch10-random, hernan-2020-whatif/ch11-model, jaynes-2003-probability/ch02-quantitative, jaynes-2003-probability/ch05-queer, jaynes-2003-probability/ch07-central-p1, jaynes-2003-probability/ch09-repetitive-p2, jaynes-2003-probability/ch13-decision, jaynes-2003-probability/ch16-orthodox, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch17-principles-p2, jaynes-2003-probability/ch18-p, jaynes-2003-probability/front-preface, mackay-2003-information/ch35-random, mcelreath-2020-rethinking/ch03-sampling, mcgrayne-2011-theory/ch06-arthur, mcgrayne-2011-theory/ch10-46, mcgrayne-2011-theory/ch17-rosetta, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch03-statistics-p3, murphy-2023-pml2/ch14-predictive, murphy-2023-pml2/ch34-decision]
canon_spine: bayesian
generated_by: build_kg.py
---

# frequentist-vs-bayesian-inference

## Canon spine entry

- **Frequentist vs Bayesian inference** (bayesian): probability as long-run frequency of procedures vs probability as degree of belief about unknowns (UG)

## Definitions in the sources

### bayesian

- [[efron-1986-bayesian/main]] (p. 3): the contrast the whole paper is about; per Efron, the parting of the ways is $\theta$ averages (expectations with the state of nature $\theta$ fixed): central for frequentists, irrelevant to Bayesians
- [[gelman-2013-bda3/ch01-probability]] (pp. 3, 6): Bayesian conclusions condition on observed $y$; the frequentist textbook approach evaluates procedures over possible $y$ given true $\theta$
- [[gelman-2013-bda3/ch04-asymptotics]] (p. 91–97): large-sample correspondence of (4.3) and (4.4); methods compared in 4.5
- [[gelman-2013-philosophy/main]] (pp. 2, 21): the authors say Bayesian methods are no more inductive than other modes of inference, and see much in common between best Bayesian practice and Mayo's frequentist error-statistical approach
- [[hernan-2020-whatif/ch10-random]] (p. 139): here: a frequentist interval's level is a long-run coverage frequency; a Bayesian credible interval would mean degree of belief
- [[hernan-2020-whatif/ch11-model]] (p. 159): probability as frequency vs degree of belief
- [[mcelreath-2020-rethinking/ch03-sampling]] (p. 58): in strict non-Bayesian inference, a confidence interval is read via repeated studies, not as a probability about the parameter
- [[mcgrayne-2011-theory/ch06-arthur]] (pp. 87–88, 92): as described here: Bailey's professors taught using only directly relevant observations, and Blackwell said probability applies to long sequences of repeatable events. The dispute is over priors and one-off events
- [[mcgrayne-2011-theory/ch10-46]] (pp. 129, 132–133): the feud over priors, p-values and fiducial probability
- [[mcgrayne-2011-theory/ch17-rosetta]] (pp. 233–234): here a cooling rivalry. researchers adopt whichever approach fits their needs; most modern Bayesians accept frequentism as still effective for most statistical problems
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 80): data random, θ fixed vs data fixed, θ random
- [[murphy-2023-pml2/ch03-statistics-p3]] (p. 130): $p_B$ conditions on data, $p_C$ uses the null's sampling distribution
- [[murphy-2023-pml2/ch14-predictive]] (p. 586): conformal coverage is frequentist, average-case, not per-instance
- [[murphy-2023-pml2/ch34-decision]] (pp. 1106–1107): here: expectation over data with $h$ fixed vs over $h$ with data fixed

### information-theory

- [[jaynes-2003-probability/ch02-quantitative]] (p. 44): only implicit: the Bernoulli/Laplace ratio is derived from information about equally possible cases (pp. 42–43), and probability assignments are said to describe a state of knowledge, not anything measurable in a physical experiment (p. 44); frequencies are not discussed in this unit
- [[jaynes-2003-probability/ch05-queer]] (pp. 122, 135, 137): here: chi-squared and ad hoc tests criticised for ignoring alternatives
- [[jaynes-2003-probability/ch07-central-p1]] (pp. 210–212): contrast: long-run frequencies of estimators and imagined data sets versus inference from the one data set at hand
- [[jaynes-2003-probability/ch09-repetitive-p2]] (p. 293): Jaynes' stance: probability as logic; frequency links arise as theorems
- [[jaynes-2003-probability/ch13-decision]] (p. 418): the opposed views of what probability is; decision rules can apparently be derived from either
- [[jaynes-2003-probability/ch16-orthodox]] (pp. 493, 498): orthodoxy: probability only as frequency of random variables; Jaynes: probability represents information
- [[jaynes-2003-probability/ch17-principles-p1]] (p. 509): here: orthodox sampling-theory methods compared with Bayes on actual results and on information use
- [[jaynes-2003-probability/ch17-principles-p2]] (p. 533): here "orthodox" means sampling theory, judging estimators by their sampling distribution
- [[jaynes-2003-probability/ch18-p]] (p. 578, p. 585): A_p ≡ A_f equivalence; confidence intervals replaced by communicating the A_p density
- [[jaynes-2003-probability/front-preface]] (pdf 23–24): Jaynes: frequentist methods are a restricted special case; Bayesian methods correct those defects in well-developed problems; both are contained in his rules, which are broader than either
- [[mackay-2003-information/ch35-random]] (pp. 446, 449): the author contrasts Bayesian likelihood-based inference with sampling-theory estimators
