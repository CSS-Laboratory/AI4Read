---
id: maximum-likelihood-estimation
type: concept
fields: [bayesian, information-theory, linear-algebra, complex-systems, llm, control-theory]
fields_strong: [bayesian, information-theory, linear-algebra, complex-systems, llm, control-theory]
n_sources: 12
n_works: 8
tiers: [core, deep, reference]
grounding: digests
sources: [clauset-2009-powerlaw/main-p1, clauset-2009-powerlaw/main-p2, deisenroth-2020-mml/ch08-when, deisenroth-2020-mml/ch09-linear, deisenroth-2020-mml/ch11-density, efron-1986-bayesian/main, jaynes-2003-probability/ch06-elementary-p1, mackay-2003-information/ch22-maximum, mackay-2003-information/ch43-boltzmann, polyanskiy-2025-information/ch32-classical, prince-2023-udl/ch05-loss, sarkka-2023-bayesianfiltering/ch02-bayesian]
aliases: [maximum-likelihood, maximum-likelihood-estimate, maximum-likelihood-estimator]
generated_by: build_kg.py
---

# maximum-likelihood-estimation

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `maximum-likelihood` — 4 digest(s)
- `maximum-likelihood-estimate` — 1 digest(s)
- `maximum-likelihood-estimator` — 2 digest(s)

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch22-maximum]] (p. 300): choose parameters $\boldsymbol\theta$ maximizing $P(\text{Data}\mid\boldsymbol\theta,\mathcal H)$ [alias `maximum-likelihood`; new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch43-boltzmann]] (p. 523): choosing $\mathbf W$ to maximize the likelihood, dropping the prior $P(\mathbf W)$ [new; work fields: information-theory, bayesian, llm]
- [[polyanskiy-2025-information/ch32-classical]] (p. 581): maximizer of total log-likelihood; asymptotically efficient under conditions [alias `maximum-likelihood-estimator`; new]

### linear-algebra

- [[deisenroth-2020-mml/ch08-when]] (pp. 265–267): minimize the negative log-likelihood (8.17) over θ [new]
- [[deisenroth-2020-mml/ch09-linear]] (p. 293): choose $\theta$ maximizing $p(\mathcal Y\mid\mathcal X,\theta)$; here it equals least squares [new]
- [[deisenroth-2020-mml/ch11-density]] (p. 351): choose $\boldsymbol\theta$ to maximize $\log p(\mathcal X\mid\boldsymbol\theta)$. For GMMs there is no closed form [new]

### bayesian

- [[efron-1986-bayesian/main]] (p. 1): the automatic Fisherian tool, the original jackknife in Tukey's sense of a widely applicable and dependable tool [alias `maximum-likelihood`; new]
- [[jaynes-2003-probability/ch06-elementary-p1]] (pp. 175–176): here, the likelihood maximizer $c/\phi$; ignores prior information [alias `maximum-likelihood-estimate`; new; work fields: bayesian, information-theory]

### complex-systems

- [[clauset-2009-powerlaw/main-p1]] (p. 5): choose parameters maximising the data's likelihood; here MLEs (3.1)–(3.7) for $\alpha$ [new]
- [[clauset-2009-powerlaw/main-p2]] (pp. 32–33): α̂ maximizing the log-likelihood. For the continuous power law it is (B.4), equivalent to the Hill estimator [alias `maximum-likelihood-estimator`; new]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch02-bayesian]] (p. 18): maximise $L(\theta)=\prod p(y_k\mid\theta)$ [alias `maximum-likelihood`; new; work fields: control-theory, bayesian]

### llm

- [[prince-2023-udl/ch05-loss]] (p. 58): choose parameters that maximize the product of probabilities of the training outputs; assumes same form and independence [alias `maximum-likelihood`; new]

## Candidate bridges

- [structural-analogy] posterior under misspecification concentrating where d(θ) is smallest ↔ maximum-likelihood/quasi-likelihood under a wrong model (White, p. 11, fn. 8): both target the best-fitting member of a wrong family — from [[gelman-2013-philosophy/main]] (bayesian → other:maximum-likelihood-quasi-likelihood)
- [structural-analogy] REINFORCE with $\partial\log\pi$ weighted by return ↔ llm: maximum-likelihood next-token training, but weighted by reward and using sampled sequences (the text compares policy-gradient smoothness to maximum likelihood in classification, p. 389). — from [[prince-2023-udl/ch19-reinforcement]] (llm → llm)
- [same-math] stacked-data maximum likelihood via nonlinear regression (Eq. 7.8) ↔ statistics: Bernoulli log-likelihood estimation — the same likelihood function. — from [[zaller-1992-massopinion/ch07-basic]] (political-science → other:statistics)
