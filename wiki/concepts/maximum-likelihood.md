---
id: maximum-likelihood
type: concept
fields: [bayesian, control-theory, information-theory, llm]
n_sources: 4
tiers: [core, deep, reference]
grounding: digests
sources: [efron-1986-bayesian/main, mackay-2003-information/ch22-maximum, prince-2023-udl/ch05-loss, sarkka-2023-bayesianfiltering/ch02-bayesian]
generated_by: build_kg.py
---

# maximum-likelihood

## Definitions in the sources

### bayesian

- [[efron-1986-bayesian/main]] (p. 1): the automatic Fisherian tool, the original jackknife in Tukey's sense of a widely applicable and dependable tool [new]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch02-bayesian]] (p. 18): maximise $L(\theta)=\prod p(y_k\mid\theta)$ [new]

### information-theory

- [[mackay-2003-information/ch22-maximum]] (p. 300): choose parameters $\boldsymbol\theta$ maximizing $P(\text{Data}\mid\boldsymbol\theta,\mathcal H)$ [new]

### llm

- [[prince-2023-udl/ch05-loss]] (p. 58): choose parameters that maximize the product of probabilities of the training outputs; assumes same form and independence [new]

## Candidate bridges

- [structural-analogy] posterior under misspecification concentrating where d(θ) is smallest ↔ maximum-likelihood/quasi-likelihood under a wrong model (White, p. 11, fn. 8): both target the best-fitting member of a wrong family — from [[gelman-2013-philosophy/main]] (bayesian → other)
- [structural-analogy] REINFORCE with $\partial\log\pi$ weighted by return ↔ llm: maximum-likelihood next-token training, but weighted by reward and using sampled sequences (the text compares policy-gradient smoothness to maximum likelihood in classification, p. 389). — from [[prince-2023-udl/ch19-reinforcement]] (llm → llm)
- [same-math] stacked-data maximum likelihood via nonlinear regression (Eq. 7.8) ↔ statistics: Bernoulli log-likelihood estimation — the same likelihood function. — from [[zaller-1992-massopinion/ch07-basic]] (political-science → other)
