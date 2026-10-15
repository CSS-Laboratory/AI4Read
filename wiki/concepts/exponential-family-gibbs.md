---
id: exponential-family-gibbs
type: concept
fields: [information-theory]
n_sources: 6
tiers: [reference, core, deep]
grounding: digests
sources: [cover-2006-elements/ch11-maximum, cover-2006-elements/ch12-information-p1, jaynes-2003-probability/ch09-repetitive-p2, jaynes-2003-probability/ch11-discrete, jaynes-2003-probability/ch12-ignorance, nielsen-2020-elementary/main-p2]
generated_by: build_kg.py
---

# exponential-family-gibbs

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch11-maximum]] (p. 267): the max-entropy solution has the form $e^{\lambda_0+\sum\lambda_ir_i}$
- [[cover-2006-elements/ch12-information-p1]] (p. 294): the tilted form (12.110) of $P^*$ under expectation constraints
- [[jaynes-2003-probability/ch09-repetitive-p2]] (p. 292): "Gibbs canonical ensemble"; the function Z (from (9.75), not shown here) and $\overline G=-\partial\log Z/\partial\lambda$
- [[jaynes-2003-probability/ch11-discrete]] (p. 356): maximum-entropy solution under expectation constraints is $p_i=\exp(-\lambda_0-\sum\lambda_jf_j(x_i))$
- [[jaynes-2003-probability/ch12-ignorance]] (p. 376): the solution form (12.11) with partition function $Z$
- [[nielsen-2020-elementary/main-p2]] (p. 29): $p_\theta=\exp(\theta^\top t-F(\theta))$, log-normalizer $F$ as Bregman generator

## Candidate bridges

- [same-math] Max-entropy solution under expectation constraints ↔ information-theory: exponential family / Gibbs distribution — the same form $p\propto\exp(\sum\lambda_if_i)$. — from [[jaynes-1957-information/main]] (information-theory → information-theory)
- [same-math] Partition function $Z(\lambda)$ and $u_j\propto e^{-\lambda g_j}$ ↔ statistical mechanics / exponential families: Gibbs distribution with normaliser $Z$. — from [[jaynes-2003-probability/ch09-repetitive-p1]] (information-theory → complex-systems)
- [same-math] Stage-2 maximum-entropy priors (14.56)–(14.59) ↔ information-theory: exponential-family/Gibbs distribution from mean constraints — same partition-function mathematics. — from [[jaynes-2003-probability/ch14-simple]] (information-theory → information-theory)
- [structural-analogy] Gaussian as the maximum-entropy law under moment constraints ↔ information-theory: exponential family / Gibbs distribution (p. 592) — from [[jaynes-2003-probability/ch19-physical]] (information-theory → information-theory)
- [same-math] Boltzmann distribution $e^{-\beta E}/Z$ ↔ information-theory: exponential family / Gibbs distribution — $\beta$ and $E$ play the roles of natural parameter and sufficient statistic. — from [[mackay-2003-information/ch51-appendices]] (information-theory → information-theory)
- [same-math] Fisher information of an exponential family $=\nabla^2F=\mathrm{Cov}[t]$ ↔ information-theory: exponential family / Gibbs distribution — $F$ is the log-normalizer — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
- [same-math] Gaussian maximises entropy at fixed variance (Lagrange: $-1-\log p+\lambda x^2+\mu=0$) ↔ information-theory canon "exponential family / Gibbs distribution": same exponential form arises from expectation constraints. — from [[shannon-1948-mathematical/main-p2]] (information-theory → information-theory)
- [same-math] Max-entropy under fixed variance gives Gaussian ↔ exponential-family / Gibbs form of MaxEnt solutions (canon link; not stated in this unit). — from [[stone-2022-information/ch05-entropy]] (information-theory → unspecified)
