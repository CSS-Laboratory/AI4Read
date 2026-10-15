---
id: rejection-sampling
type: concept
fields: [bayesian, control-theory, information-theory]
n_sources: 4
tiers: [core, deep, reference]
grounding: digests
sources: [gelman-2013-bda3/ch10-introduction, mackay-2003-information/ch29-monte, murphy-2023-pml2/ch11-monte, sarkka-2023-bayesianfiltering/ch15-particle]
generated_by: build_kg.py
---

# rejection-sampling

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch10-introduction]] (p. 264): accept a draw from $g$ with probability $p/(Mg)$, where $p/g\le M$; self-monitoring (p. 264) (new)
- [[murphy-2023-pml2/ch11-monte]] (p. 487–488): accept proposals under an envelope $Cq\ge\tilde p$; the acceptance rate is $1/C$ for a normalized target [new]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch15-particle]] (p. 313): draw from $p$ using proposals $q$ with $p\le Mq$ [new]

### information-theory

- [[mackay-2003-information/ch29-monte]] (p. 364–365): accept (x, u) under P* within the envelope cQ*; gives independent samples, acceptance rate 1/c for normalized densities [new]

## Instances that use it

- [[gamma-rejection-sampling]] — $\mathrm{Ga}(\alpha,\lambda)$ with $\mathrm{Ga}(k,\lambda-1)$ proposal — from [[murphy-2023-pml2/ch11-monte]]

## Candidate bridges

- [structural-analogy] ABC rejection sampling ↔ prior predictive simulation — both simulate data from prior draws, but ABC keeps draws close to observed data. — from [[gelman-2013-bda3/ch13-modal]] (bayesian → unspecified)
- [same-math] Rejection sampling with bound $C(\mathbf{x}_k)$ ↔ general Monte Carlo: Algorithm 15.5 applied to a discrete index distribution. — from [[sarkka-2023-bayesianfiltering/ch15-particle]] (control-theory → other)
