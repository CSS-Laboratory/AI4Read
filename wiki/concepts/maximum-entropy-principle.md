---
id: maximum-entropy-principle
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 34
n_works: 8
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch02-entropy, cover-2006-elements/ch09-differential, cover-2006-elements/ch10-gaussian, cover-2006-elements/ch11-maximum, cover-2006-elements/ch12-information-p1, cover-2006-elements/ch12-information-p2, cover-2006-elements/ch13-rate, cover-2006-elements/ch16-inequalities, jaynes-1957-information/main, jaynes-2003-probability/ch07-central-p1, jaynes-2003-probability/ch07-central-p2, jaynes-2003-probability/ch09-repetitive-p1, jaynes-2003-probability/ch09-repetitive-p2, jaynes-2003-probability/ch11-discrete, jaynes-2003-probability/ch12-ignorance, jaynes-2003-probability/ch14-simple, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch19-physical, jaynes-2003-probability/ch20-model, jaynes-2003-probability/ch22-introduction, jaynes-2003-probability/front-preface, mackay-2003-information/ch22-maximum, mackay-2003-information/ch23-useful, mackay-2003-information/ch46-deconvolution, murphy-2023-pml2/ch02-probability-p2, polyanskiy-2025-information/ch03-divergence, polyanskiy-2025-information/ch06-extremization, polyanskiy-2025-information/ch29-evaluating, shannon-1948-mathematical/main-p1, shannon-1948-mathematical/main-p2, stone-2022-information/ch05-entropy, stone-2022-information/ch07-channel, stone-2022-information/ch11-information]
aliases: [maximum-entropy]
raw_ids: [maximum entropy principle]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# maximum-entropy-principle

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `maximum-entropy` — 1 digest(s)

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
- [[mackay-2003-information/ch22-maximum]] (p. 308): maximize $H$ under average constraints; the solution is exponential-family [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch23-useful]] (p. 318): only named as a field using the entropic distribution [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch46-deconvolution]] (p. 551): used here as an image-prior family, with $S$ from (46.14) [work fields: information-theory, bayesian]
- [[polyanskiy-2025-information/ch03-divergence]] (p. Thm 2.8, p. 28): Gaussian maximizes $h$ under covariance bound or second-moment bound [as `maximum entropy principle`]
- [[polyanskiy-2025-information/ch06-extremization]] (p. 100): Example 5.2 bounds $\max H(X)$ under $\mathbb Ef(X)\le a$
- [[polyanskiy-2025-information/ch29-evaluating]] (p. 510): Gaussian maximizes entropy for given covariance; bounds $h(X^n|W)$
- [[shannon-1948-mathematical/main-p1]] (p. 18): (canon link; the principle is not stated in this unit) in §10, use the maximum-entropy source subject to the statistical conditions one chooses to retain [weak: not really used in this unit]
- [[shannon-1948-mathematical/main-p2]] (pp. 35–37): Gaussian maximises entropy for fixed second moments; exponential for fixed mean on a half line; uniform on a bounded volume
- [[stone-2022-information/ch05-entropy]] (p. 124): choose the distribution with largest entropy under a given constraint; here uniform, exponential or Gaussian
- [[stone-2022-information/ch07-channel]] (pp. 155, 166): fixed variance gives Gaussian; bounded range gives uniform [as `maximum entropy principle`]
- [[stone-2022-information/ch11-information]] (p. 233): a uniform pdf has maximum entropy, so a cdf encoder maximises information per output value

### bayesian

- [[jaynes-2003-probability/ch07-central-p1]] (pp. 208, 216–217): given only $\langle e\rangle$ and $\langle e^2\rangle$, the maximum-entropy density is Gaussian; theorem is deferred to Ch. 11 [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch07-central-p2]] (p. 221): here, the Gaussian has maximum entropy at fixed variance, so information-discarding operations that conserve variance approach it [as `maximum entropy principle`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch09-repetitive-p1]] (p. 287, footnote 4): multiplicity found by maximising $H$ over the constraint region; derived from probability rules, at least in this case [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch09-repetitive-p2]] (p. 292): in §9.9, the Gibbs distribution solves the constrained extremum; unique λ from (9.78) [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch11-discrete]] (p. 350): among distributions meeting the stated averages, pick the one maximizing $H$; the "most honest" assignment [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch12-ignorance]] (p. 374–376): choose the max-entropy distribution given constraints, here relative to an invariant measure $m(x)$ [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch14-simple]] (pp. 443, 446): used to assign priors from mean-demand constraints [as `maximum entropy principle`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch17-principles-p1]] (p. 519): the distributions attaining the Cramér–Rao equality, (17.33), have the maximum-entropy form [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch19-physical]] (p. 592, 595): given only the error magnitude (second moments), it yields independent Gaussians; it also resolves underdetermined problems [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch20-model]] (pp. 602, 610, 614): cited for the Gaussian prior and for final causes; also the partition-function analogy [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch22-introduction]] (pp. 638–641): choose $p(M)$ of maximum entropy given expected frequencies; presented as the most conservative design [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/front-preface]] (pdf 24–25): assign probabilities from a sample space and data constraints, with no model or sampling distribution; nonspeculative [work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch02-probability-p2]] (p. 43): closest distribution to prior $q$ in KL under feature-expectation constraints; with a uniform prior this is maximizing entropy [alias `maximum-entropy`]

## Candidate bridges

- [structural-analogy] Equality conditions (distinct codewords, i.i.d. outputs with $p^*(y)$) ↔ maximum entropy principle: capacity achieved when outputs are as spread as the constraints allow. — from [[cover-2006-elements/ch08-channel-p2]] (information-theory → information-theory)
- [same-math] Optimal Gaussian input via maximum entropy ↔ information-theory: maximum entropy principle — a normal maximizes entropy for fixed variance. — from [[cover-2006-elements/ch10-gaussian]] (information-theory → information-theory)
- [same-math] Sanov's $P^*\propto Q\,e^{\sum\lambda_ig_i}$ ↔ maximum entropy / exponential families: the same tilted form as MaxEnt solutions under expectation constraints. — from [[cover-2006-elements/ch12-information-p1]] (information-theory → information-theory)
- [structural-analogy] Gaussian has only two cumulants ↔ information-theory: maximum-entropy / exponential-family distributions with mean and variance constraints. — from [[jaynes-2003-probability/appc-convolutions]] (bayesian → information-theory)
- [structural-analogy] Desideratum (IIIc), equivalent knowledge gives equal plausibilities ↔ bayesian: principle of indifference/maximum entropy — from [[jaynes-2003-probability/ch01-plausible]] (bayesian → bayesian)
- [structural-analogy] Principle of indifference (uniform $1/n$) ↔ maximum entropy: the uniform distribution is the most uncommitted one when only normalization is known (canon link; not stated in this unit). — from [[jaynes-2003-probability/ch02-quantitative]] (bayesian → information-theory)
- [structural-analogy] Gaussian as maximum entropy under fixed mean and variance ↔ information-theory: the maximum-entropy principle and exponential families (pp. 216–217) — from [[jaynes-2003-probability/ch07-central-p1]] (bayesian → information-theory)
- [structural-analogy] Gaussian as maximum-entropy attractor under variance-conserving operations ↔ information theory: maximum entropy principle and the typical set — repeated information-losing steps approach a maximum-entropy law. — from [[jaynes-2003-probability/ch07-central-p2]] (bayesian → information-theory)
- [structural-analogy] Fundamental domain of a symmetry group fixing the prior ↔ bayesian: Principle of indifference / maximum entropy — symmetry as the formal basis for uninformative priors. — from [[jaynes-2003-probability/ch10-physics]] (bayesian → bayesian)
- [same-math] Stage-2 maximum-entropy priors (14.56)–(14.59) ↔ information-theory: exponential-family/Gibbs distribution from mean constraints — same partition-function mathematics. — from [[jaynes-2003-probability/ch14-simple]] (bayesian → information-theory)
- [structural-analogy] "Jeffreys prior is uninformative for a scale parameter" ↔ information-theory: the group-invariance / maximum-entropy prior constructions Jaynes mentions (pp. 484–485). — from [[jaynes-2003-probability/ch15-paradoxes]] (bayesian → information-theory)
- [structural-analogy] Underdetermined solution $x^*=\tilde A(A\tilde A)^{-1}y$ chosen by minimum length or maximum entropy ↔ information-theory: choosing among data-consistent models by an entropy criterion (p. 594–595) — from [[jaynes-2003-probability/ch19-physical]] (bayesian → information-theory)
- [structural-analogy] Gaussian as the maximum-entropy law under moment constraints ↔ information-theory: exponential family / Gibbs distribution (p. 592) — from [[jaynes-2003-probability/ch19-physical]] (bayesian → information-theory)
- [same-math] Digram maximum entropy via $Q^{N}$ and $q_{\max}$ ↔ statistical mechanics: transfer-matrix-style calculation with periodic boundary conditions — the author notes that physicists use the term 'periodic boundary conditions' for this device (p. 642). — from [[jaynes-2003-probability/ch22-introduction]] (bayesian → complex-systems)
- [structural-analogy] Maximum capacity for given time ↔ minimum time for given $W$ ↔ maximum entropy for given energy / minimum energy for given entropy — dual forms of one variational problem (p. 632). — from [[jaynes-2003-probability/ch22-introduction]] (bayesian → unspecified)
- [structural-analogy] Maximum-entropy assignment ↔ statistical mechanics: the Preface says all presently known statistical mechanics is included in the maximum-entropy approach (pdf 25). — from [[jaynes-2003-probability/front-preface]] (bayesian → complex-systems)
- [structural-analogy] $\mathbf Q$ built from $\mathbf e^{(L)}$ so all long valid strings are equally likely ↔ maximum entropy principle: least-committal distribution under constraints. — from [[mackay-2003-information/ch17-communication]] (information-theory → information-theory)
- [same-math] Boltzmann-machine learning gradient (data minus model moments) ↔ information-theory: maximum-entropy / exponential-family fitting, where parameters are tuned until model expectations match data expectations — same moment-matching condition. — from [[mackay-2003-information/ch43-boltzmann]] (information-theory → information-theory)
- [metaphor] Prior over functions ↔ choosing the least-committal distribution under smoothness constraints (maximum entropy). — from [[mackay-2003-information/ch45-gaussian]] (information-theory → unspecified)
- [structural-analogy] Gaussian as the least-committal shape given mean and variance ↔ Bayesian inference: maximum entropy (developed later in the book). — from [[mcelreath-2020-rethinking/ch04-linear-p1]] (bayesian → bayesian)
- [same-math] Maximum entropy with a non-flat prior $q$ ↔ Bayesian updating: minimizing KL from the prior under constraints (author states the data-as-constraints version, p. 272). — from [[mcelreath-2020-rethinking/ch09-big]] (bayesian → bayesian)
- [metaphor] "Phantom assumptions" of non-maximum-entropy distributions ↔ hidden confounders: unstated structure that shapes conclusions. — from [[mcelreath-2020-rethinking/ch09-big]] (bayesian → other:hidden-confounders)
- [same-math] Maxent model with $\exp(\boldsymbol\theta^\top\boldsymbol\phi)$ ↔ principle of indifference / maximum entropy: least-committal distribution matching feature expectations (p. 174–175). — from [[murphy-2023-pml2/ch04-graphical-p2]] (bayesian → bayesian)
- [metaphor] Random pattern: maximum entropy yet perceptually uniform ↔ typical set: the details are information-rich but irrelevant to the observer. — from [[pierce-1980-introduction/ch13-information]] (information-theory → information-theory)
- [same-math] Gibbs distribution bound on max entropy ↔ maximum entropy principle in statistical physics: both give $p\propto e^{-\lambda f}$. — from [[polyanskiy-2025-information/ch06-extremization]] (information-theory → information-theory)
- [structural-analogy] Averaging over rotations to prove Gaussian extremality ↔ statistics: symmetry/invariance arguments for minimax or maximum-entropy solutions. — from [[polyanskiy-2025-information/ch07-tensorization]] (information-theory → other:statistics)
- [structural-analogy] I-projection with P uniform ↔ maximum entropy principle: the author notes this link (p. 308). — from [[polyanskiy-2025-information/ch17-information]] (information-theory → information-theory)
