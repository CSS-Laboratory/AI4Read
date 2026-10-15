---
id: cumulant
type: concept
fields: [bayesian, control-theory, information-theory]
fields_strong: [bayesian, control-theory, information-theory]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [jaynes-2003-probability/appc-convolutions, sutton-2018-rl/ch17-frontiers]
generated_by: build_kg.py
---

# cumulant

## Definitions in the sources

### bayesian

- [[jaynes-2003-probability/appc-convolutions]] (pp. 678–679): moment corrected by lower moments so it is additive under convolution; equivalently $C_n=i^{-n}\,d^n\log\mathcal F/d\alpha^n$ at 0 [new; work fields: bayesian, information-theory]

### control-theory

- [[sutton-2018-rl/ch17-frontiers]] (p. 459): the signal $C_t$ accumulated in a GVF in place of reward [new]

## Instances that use it

- [[gaussian-cumulants]] — only $C_1=\mu$ and $C_2=\sigma^2$ are nontrivial; all higher $C_n$ vanish — from [[jaynes-2003-probability/appc-convolutions]]
- [[fourth-central-moment-vs-cumulant]] — $\overline{(x-\bar x)^4}=C_4+3C_2^2$ — from [[jaynes-2003-probability/appc-convolutions]]

## Candidate bridges

- [same-math] additivity of cumulants under convolution ↔ bayesian/probability: if the density of a sum of independent variables is the convolution of their densities, cumulants add. The text itself keeps the algebra probability-free. — from [[jaynes-2003-probability/appc-convolutions]] (bayesian → bayesian)
- [structural-analogy] Gaussian has only two cumulants ↔ information-theory: maximum-entropy / exponential-family distributions with mean and variance constraints. — from [[jaynes-2003-probability/appc-convolutions]] (bayesian → information-theory)
- [same-math] $\log Z$ derivatives give means and covariances (11.60, 11.73) ↔ exponential-family theory: log-partition function as cumulant generating function — the same identities — from [[jaynes-2003-probability/ch11-discrete]] (bayesian → other:exponential-family-theory)
