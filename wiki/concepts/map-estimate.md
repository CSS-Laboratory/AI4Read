---
id: map-estimate
type: concept
fields: [bayesian, information-theory, llm, control-theory, linear-algebra]
fields_strong: [bayesian, information-theory, llm, control-theory, linear-algebra]
n_sources: 9
n_works: 5
tiers: [core, reference, deep]
grounding: digests
sources: [deisenroth-2020-mml/ch09-linear, mackay-2003-information/ch22-maximum, mackay-2003-information/ch41-learning, mackay-2003-information/ch44-supervised, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch14-predictive, prince-2023-udl/ch09-regularization, sarkka-2023-bayesianfiltering/ch07-extended]
aliases: [map-estimation, maximum-a-posteriori]
generated_by: build_kg.py
---

# map-estimate

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `map-estimation` — 2 digest(s)
- `maximum-a-posteriori` — 2 digest(s)

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 65): posterior mode; equals the MLE under a uniform prior [new]
- [[murphy-2023-pml2/ch07-inference]] (p. 349): posterior mode, treated as a delta distribution [new]
- [[murphy-2023-pml2/ch14-predictive]] (p. 576): ERM with log loss and $C=-\log\pi_0$; maximizes $\log p(\mathcal D|\theta)+\log\pi_0$ [alias `maximum-a-posteriori`; new]

### information-theory

- [[mackay-2003-information/ch22-maximum]] (p. 306): maximizing the posterior density; it often shares ML's problems, and its answer usually changes with the parametrization [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch41-learning]] (p. 493): $\mathbf w_{\rm MP}$, the (locally) most probable weights found by minimizing $M$ [new; work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch44-supervised]] (p. 529): $\mathbf w_{\rm MP}$, the (locally) most probable parameter vector found by minimizing $M$ [alias `maximum-a-posteriori`; new; work fields: information-theory, bayesian, llm]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch07-extended]] (p. 121): state maximising the posterior; here the minimiser of $L$ [new; work fields: control-theory, bayesian]

### linear-algebra

- [[deisenroth-2020-mml/ch09-linear]] (pp. 300–301): maximize the posterior $p(\theta\mid\mathcal X,\mathcal Y)$; a compromise between prior and likelihood [alias `map-estimation`; new]

### llm

- [[prince-2023-udl/ch09-regularization]] (p. 140): maximizing prior × likelihood; the penalty is $-\log Pr(\phi)$ [alias `map-estimation`; new]

## Candidate bridges

- [same-math] Optimal block decoder argmax P(s|y) ↔ bayesian: MAP estimation with the codeword as the hypothesis and the channel as the likelihood. — from [[mackay-2003-information/ch09-communication]] (information-theory → bayesian)
- [metaphor] ensemble learning: a point estimate is a delta-function Q ↔ MAP estimation: the spike is the crudest member of the family. — from [[mackay-2003-information/ch33-variational]] (information-theory → bayesian)
- [structural-analogy] Min–sum (Viterbi) most-probable path ↔ bayesian: MAP estimate versus full posterior — path cost is a negative log-likelihood under the binary symmetric channel. — from [[mackay-2003-information/ch48-convolutional]] (information-theory → bayesian)
- [same-math] `lm` with flat priors ↔ Bayesian inference: under flat priors and a Gaussian likelihood the OLS estimates equal the MAP estimates (p. 159). — from [[mcelreath-2020-rethinking/ch05-multivariate-p2]] (bayesian → bayesian)
