---
id: maximum-entropy-principle
type: concept
fields: [information-theory]
n_sources: 33
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch02-entropy, cover-2006-elements/ch09-differential, cover-2006-elements/ch10-gaussian, cover-2006-elements/ch11-maximum, cover-2006-elements/ch12-information-p1, cover-2006-elements/ch12-information-p2, cover-2006-elements/ch13-rate, cover-2006-elements/ch16-inequalities, jaynes-1957-information/main, jaynes-2003-probability/ch07-central-p1, jaynes-2003-probability/ch07-central-p2, jaynes-2003-probability/ch09-repetitive-p1, jaynes-2003-probability/ch09-repetitive-p2, jaynes-2003-probability/ch11-discrete, jaynes-2003-probability/ch12-ignorance, jaynes-2003-probability/ch14-simple, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch19-physical, jaynes-2003-probability/ch20-model, jaynes-2003-probability/ch22-introduction, jaynes-2003-probability/front-preface, mackay-2003-information/ch22-maximum, mackay-2003-information/ch23-useful, mackay-2003-information/ch46-deconvolution, polyanskiy-2025-information/ch03-divergence, polyanskiy-2025-information/ch06-extremization, polyanskiy-2025-information/ch29-evaluating, shannon-1948-mathematical/main-p1, shannon-1948-mathematical/main-p2, stone-2022-information/ch05-entropy, stone-2022-information/ch07-channel, stone-2022-information/ch11-information]
raw_ids: [maximum entropy principle]
canon_spine: information-theory
generated_by: build_kg.py
---

# maximum-entropy-principle

## Canon spine entry

- **maximum entropy principle** (information-theory): among distributions consistent with what you know, choose the one with maximum entropy (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 10): mentioned: a model maximising entropy gives the maximum entropy approach to inference [as `maximum entropy principle`]
- [[cover-2006-elements/ch02-entropy]] (p. 27): only the fact that the uniform pmf maximizes $H$ on a finite alphabet (Thm 2.6.4); no constraints in the chapter text (Problem 30, p. 48, adds a mean constraint)
- [[cover-2006-elements/ch09-differential]] (p. 234): normal maximizes $h$ for given covariance
- [[cover-2006-elements/ch10-gaussian]] (pp. 241–242): the normal maximizes entropy for fixed variance; this fixes the optimal input
- [[cover-2006-elements/ch11-maximum]] (p. 266): choose the max-entropy distribution consistent with known constraints; here for moments and autocorrelations
- [[cover-2006-elements/ch12-information-p1]] (p. 295): $P^*$ is max-entropy when $Q$ is uniform
- [[cover-2006-elements/ch12-information-p2]] (p. 301): the theorem is called a strengthening of it; P* has the MaxEnt form
- [[cover-2006-elements/ch13-rate]] (p. 345): normal has maximum entropy for a given second moment
- [[cover-2006-elements/ch16-inequalities]] (p. 488): Gaussian maximises $h$ for fixed covariance
- [[jaynes-1957-information/main]] (p. 623): choose the distribution with maximum entropy subject to the known averages; Jaynes calls it the unbiased choice
- [[jaynes-2003-probability/ch07-central-p1]] (pp. 208, 216–217): given only $\langle e\rangle$ and $\langle e^2\rangle$, the maximum-entropy density is Gaussian; theorem is deferred to Ch. 11
- [[jaynes-2003-probability/ch07-central-p2]] (p. 221): here, the Gaussian has maximum entropy at fixed variance, so information-discarding operations that conserve variance approach it [as `maximum entropy principle`]
- [[jaynes-2003-probability/ch09-repetitive-p1]] (p. 287, footnote 4): multiplicity found by maximising $H$ over the constraint region; derived from probability rules, at least in this case
- [[jaynes-2003-probability/ch09-repetitive-p2]] (p. 292): in §9.9, the Gibbs distribution solves the constrained extremum; unique λ from (9.78)
- [[jaynes-2003-probability/ch11-discrete]] (p. 350): among distributions meeting the stated averages, pick the one maximizing $H$; the "most honest" assignment
- [[jaynes-2003-probability/ch12-ignorance]] (p. 374–376): choose the max-entropy distribution given constraints, here relative to an invariant measure $m(x)$
- [[jaynes-2003-probability/ch14-simple]] (pp. 443, 446): used to assign priors from mean-demand constraints [as `maximum entropy principle`]
- [[jaynes-2003-probability/ch17-principles-p1]] (p. 519): the distributions attaining the Cramér–Rao equality, (17.33), have the maximum-entropy form
- [[jaynes-2003-probability/ch19-physical]] (p. 592, 595): given only the error magnitude (second moments), it yields independent Gaussians; it also resolves underdetermined problems
- [[jaynes-2003-probability/ch20-model]] (pp. 602, 610, 614): cited for the Gaussian prior and for final causes; also the partition-function analogy
- [[jaynes-2003-probability/ch22-introduction]] (pp. 638–641): choose $p(M)$ of maximum entropy given expected frequencies; presented as the most conservative design
- [[jaynes-2003-probability/front-preface]] (pdf 24–25): assign probabilities from a sample space and data constraints, with no model or sampling distribution; nonspeculative
- [[mackay-2003-information/ch22-maximum]] (p. 308): maximize $H$ under average constraints; the solution is exponential-family
- [[mackay-2003-information/ch23-useful]] (p. 318): only named as a field using the entropic distribution
- [[mackay-2003-information/ch46-deconvolution]] (p. 551): used here as an image-prior family, with $S$ from (46.14)
- [[polyanskiy-2025-information/ch03-divergence]] (p. Thm 2.8, p. 28): Gaussian maximizes $h$ under covariance bound or second-moment bound [as `maximum entropy principle`]
- [[polyanskiy-2025-information/ch06-extremization]] (p. 100): Example 5.2 bounds $\max H(X)$ under $\mathbb Ef(X)\le a$
- [[polyanskiy-2025-information/ch29-evaluating]] (p. 510): Gaussian maximizes entropy for given covariance; bounds $h(X^n|W)$
- [[shannon-1948-mathematical/main-p1]] (p. 18): (canon link; the principle is not stated in this unit) in §10, use the maximum-entropy source subject to the statistical conditions one chooses to retain
- [[shannon-1948-mathematical/main-p2]] (pp. 35–37): Gaussian maximises entropy for fixed second moments; exponential for fixed mean on a half line; uniform on a bounded volume
- [[stone-2022-information/ch05-entropy]] (p. 124): choose the distribution with largest entropy under a given constraint; here uniform, exponential or Gaussian
- [[stone-2022-information/ch07-channel]] (pp. 155, 166): fixed variance gives Gaussian; bounded range gives uniform [as `maximum entropy principle`]
- [[stone-2022-information/ch11-information]] (p. 233): a uniform pdf has maximum entropy, so a cdf encoder maximises information per output value

## Candidate bridges

- [structural-analogy] Equality conditions (distinct codewords, i.i.d. outputs with $p^*(y)$) ↔ maximum entropy principle: capacity achieved when outputs are as spread as the constraints allow. — from [[cover-2006-elements/ch08-channel-p2]] (information-theory → other)
- [same-math] Optimal Gaussian input via maximum entropy ↔ information-theory: maximum entropy principle — a normal maximizes entropy for fixed variance. — from [[cover-2006-elements/ch10-gaussian]] (information-theory → information-theory)
- [structural-analogy] Gaussian as maximum entropy under fixed mean and variance ↔ information-theory: the maximum-entropy principle and exponential families (pp. 216–217) — from [[jaynes-2003-probability/ch07-central-p1]] (information-theory → information-theory)
- [structural-analogy] Gaussian as maximum-entropy attractor under variance-conserving operations ↔ information theory: maximum entropy principle and the typical set — repeated information-losing steps approach a maximum-entropy law. — from [[jaynes-2003-probability/ch07-central-p2]] (information-theory → information-theory)
- [structural-analogy] $\mathbf Q$ built from $\mathbf e^{(L)}$ so all long valid strings are equally likely ↔ maximum entropy principle: least-committal distribution under constraints. — from [[mackay-2003-information/ch17-communication]] (information-theory → other)
- [same-math] Gibbs distribution bound on max entropy ↔ maximum entropy principle in statistical physics: both give $p\propto e^{-\lambda f}$. — from [[polyanskiy-2025-information/ch06-extremization]] (information-theory → complex-systems)
- [structural-analogy] I-projection with P uniform ↔ maximum entropy principle: the author notes this link (p. 308). — from [[polyanskiy-2025-information/ch17-information]] (information-theory → other)
