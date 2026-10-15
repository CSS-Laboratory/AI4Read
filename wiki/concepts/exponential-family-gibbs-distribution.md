---
id: exponential-family-gibbs-distribution
type: concept
fields: [information-theory]
n_sources: 10
tiers: [reference, core, deep]
grounding: digests
sources: [jaynes-1957-information/main, jaynes-2003-probability/ch14-simple, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch22-introduction, mackay-2003-information/ch31-ising, mackay-2003-information/ch43-boltzmann, polyanskiy-2025-information/ch05-variational, polyanskiy-2025-information/ch06-extremization, polyanskiy-2025-information/ch36-strong-p1, tishby-2000-bottleneck/main]
raw_ids: [exponential family / Gibbs distribution]
canon_spine: information-theory
generated_by: build_kg.py
---

# exponential-family-gibbs-distribution

## Canon spine entry

- **exponential family / Gibbs distribution** (information-theory): the form of every MaxEnt solution under expectation constraints: p ∝ exp(Σ λ_i f_i) (grad)

## Definitions in the sources

### information-theory

- [[jaynes-1957-information/main]] (p. 623): max-entropy solution $p_i=\exp\{-[\lambda_0+\sum\lambda_kf_k(x_i)]\}$
- [[jaynes-2003-probability/ch14-simple]] (pp. 443–447): the geometric/exponential priors (14.59) and the Bose–Einstein form (14.77) [as `exponential family / Gibbs distribution`]
- [[jaynes-2003-probability/ch17-principles-p1]] (p. 519): form (17.33), $m(x)e^{-l\beta(x)}/Z$
- [[jaynes-2003-probability/ch22-introduction]] (p. 639): the form (22.30), with partition function $Z$ giving the multipliers
- [[mackay-2003-information/ch31-ising]] (p. 400): Boltzmann law $P\propto\exp[-\beta E]$ over spin states (31.2)
- [[mackay-2003-information/ch43-boltzmann]] (p. 522): $P\propto\exp(\tfrac12\mathbf x^{\rm T}\mathbf W\mathbf x)$ as an energy-based distribution
- [[polyanskiy-2025-information/ch05-variational]] (p. 74): the tilted measure $Q^f\propto e^fQ$ is of this exponential-tilting form (canon link; the unit does not call it that)
- [[polyanskiy-2025-information/ch06-extremization]] (p. 100): $Q_X(n)=Z(\lambda)^{-1}e^{-\lambda f(n)}$; solves max-entropy bounds
- [[polyanskiy-2025-information/ch36-strong-p1]] (p. 642): the tree law (33.20)
- [[tishby-2000-bottleneck/main]] (p. 6): form $p(\tilde x|x)\propto p(\tilde x)e^{-\beta d}$ of the optimal encoder

## Candidate bridges

- [same-math] Max-entropy solution under expectation constraints ↔ information-theory: exponential family / Gibbs distribution — the same form $p\propto\exp(\sum\lambda_if_i)$. — from [[jaynes-1957-information/main]] (information-theory → information-theory)
- [same-math] Partition function $Z(\lambda)$ and $u_j\propto e^{-\lambda g_j}$ ↔ statistical mechanics / exponential families: Gibbs distribution with normaliser $Z$. — from [[jaynes-2003-probability/ch09-repetitive-p1]] (information-theory → complex-systems)
- [same-math] Stage-2 maximum-entropy priors (14.56)–(14.59) ↔ information-theory: exponential-family/Gibbs distribution from mean constraints — same partition-function mathematics. — from [[jaynes-2003-probability/ch14-simple]] (information-theory → information-theory)
- [structural-analogy] Gaussian as the maximum-entropy law under moment constraints ↔ information-theory: exponential family / Gibbs distribution (p. 592) — from [[jaynes-2003-probability/ch19-physical]] (information-theory → information-theory)
- [same-math] Boltzmann distribution $e^{-\beta E}/Z$ ↔ information-theory: exponential family / Gibbs distribution — $\beta$ and $E$ play the roles of natural parameter and sufficient statistic. — from [[mackay-2003-information/ch51-appendices]] (information-theory → information-theory)
- [same-math] Fisher information of an exponential family $=\nabla^2F=\mathrm{Cov}[t]$ ↔ information-theory: exponential family / Gibbs distribution — $F$ is the log-normalizer — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
- [same-math] Gaussian maximises entropy at fixed variance (Lagrange: $-1-\log p+\lambda x^2+\mu=0$) ↔ information-theory canon "exponential family / Gibbs distribution": same exponential form arises from expectation constraints. — from [[shannon-1948-mathematical/main-p2]] (information-theory → information-theory)
