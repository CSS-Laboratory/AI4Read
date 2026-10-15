---
id: likelihood-principle
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 9
n_works: 4
tiers: [core]
grounding: digests
sources: [gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch06-model, jaynes-2003-probability/ch08-sufficiency, jaynes-2003-probability/ch16-orthodox, mackay-2003-information/ch02-probability, mackay-2003-information/ch03-more, mackay-2003-information/ch37-bayesian, mcgrayne-2011-theory/ch07-tool, mcgrayne-2011-theory/ch10-46]
generated_by: build_kg.py
---

# likelihood-principle

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch01-probability]] (pp. 7–8): given the model, data affect the posterior only through the likelihood; reasonable only within the chosen model family [new]
- [[gelman-2013-bda3/ch06-model]] (p. 152): inference depends on data only via likelihood; checking nevertheless depends on the sampling rule [new]
- [[jaynes-2003-probability/ch08-sufficiency]] (p. 250): within a specified model, $L(\theta)$ carries all the information about $\theta$ in $D$; for Jaynes, a trivial consequence of the product rule [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch16-orthodox]] (p. 505): named as violated by orthodox methods; shown in Ch. 17 [new; work fields: bayesian, information-theory]
- [[mcgrayne-2011-theory/ch07-tool]] (p. 104): as stated here, all information in the data sits in the likelihood; scientists could stop an experiment when satisfied [new]
- [[mcgrayne-2011-theory/ch10-46]] (p. 132): only the observed data matter [new]

### information-theory

- [[mackay-2003-information/ch02-probability]] (p. 32): inferences depend on the data only through $P(d_1\mid\boldsymbol\theta)$ [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch03-more]] (p. 61): only the likelihoods of the observed data matter for inference; mentioned, referring to section 2.3 [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch37-bayesian]] (p. 464): as MacKay uses it, the stopping rule is not relevant to what the data tell us about the parameter [new; work fields: information-theory, bayesian]

## Instances that use it

- [[two-urn-likelihood-principle]] — Examples 2.10 and 2.11 — from [[mackay-2003-information/ch02-probability]]

## Candidate bridges

- [structural-analogy] A stopping rule or data-dependent model building has no Bayesian consequence ↔ Bayesian workflow: likelihood principle versus data-adaptive modelling and the need for predictive checks. — from [[efron-1986-bayesian/main]] (bayesian → bayesian)
- [structural-analogy] Jeffreys on "imaginary repetitions" ↔ the likelihood principle (canon link; not stated in this unit) — inference from observed data only — from [[mcgrayne-2011-theory/ch03-many]] (bayesian → unspecified)
