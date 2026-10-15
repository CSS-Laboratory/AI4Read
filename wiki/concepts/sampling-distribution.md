---
id: sampling-distribution
type: concept
fields: [information-theory, bayesian]
n_sources: 5
tiers: [reference, core]
grounding: digests
sources: [jaynes-2003-probability/ch03-elementary, jaynes-2003-probability/ch16-orthodox, mackay-2003-information/ch37-bayesian, mcelreath-2020-rethinking/ch01-golem, murphy-2023-pml2/ch03-statistics-p1]
generated_by: build_kg.py
---

# sampling-distribution

## Definitions in the sources

### information-theory

- [[jaynes-2003-probability/ch03-elementary]] (p. 84): $P(\text{data}|\text{hypothesis})$; Jaynes uses the term whether the link is logical or causal [new]
- [[jaynes-2003-probability/ch16-orthodox]] (p. 493): $p(f|\theta)$, a limiting frequency over repeated draws [new]
- [[mackay-2003-information/ch37-bayesian]] (p. 459): the distribution of a statistic over repetitions of the experiment, assuming the null [new]

### bayesian

- [[mcelreath-2020-rethinking/ch01-golem]] (p. 11): distribution of a measurement under imagined repeated sampling [new]
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 73): distribution of an estimator across datasets from the true model [new]

## Instances that use it

- [[taxicab-problem]] — estimating the number of cabs from number 27; rectangular sampling distribution — from [[jaynes-2003-probability/ch06-elementary-p2]]
- [[cauchy-sampling-distribution]] — arises if $e=\alpha\tan\theta$; gives nonlinear estimators — from [[jaynes-2003-probability/ch07-central-p1]]

## Candidate bridges

- [structural-analogy] Posterior of $(\bar y-\mu)/(s/\sqrt n)$ is $t_{n-1}$ ↔ frequentist inference: the same $t$ appears as a sampling distribution, so intervals coincide numerically, though the interpretation differs. — from [[gelman-2013-bda3/ch03-introduction]] (bayesian → other)
- [same-math] Posterior $\mathrm N(\hat\theta,I^{-1})$ in (4.3) ↔ frequentist sampling distribution of the MLE in (4.4): the same standardised normal, read with $\theta$ random or $\hat\theta$ random. — from [[gelman-2013-bda3/ch04-asymptotics]] (bayesian → other)
- [structural-analogy] Sampling distribution vs. inverse problem ↔ bayesian: likelihood vs. posterior — $P(D|H)$ as a function of $D$ versus $P(H|D)$ needing a prior. — from [[jaynes-2003-probability/ch03-elementary]] (information-theory → bayesian)
- [structural-analogy] Marginalization (B₁ vs B₂) ↔ Bayesian: sufficiency and ancillary statistics — a statistic whose sampling distribution is free of the nuisance parameter is the structure DSZ exploit. — from [[jaynes-2003-probability/ch15-paradoxes]] (information-theory → bayesian)
