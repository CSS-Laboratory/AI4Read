---
id: propensity-score
type: concept
fields: [bayesian]
n_sources: 11
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch08-modeling, hernan-2020-whatif/ch07-confounding, hernan-2020-whatif/ch12-ip, hernan-2020-whatif/ch14-g, hernan-2020-whatif/ch15-outcome, hernan-2020-whatif/ch18-variable, hernan-2020-whatif/ch22-target, murphy-2023-pml2/ch36-causality-p1, murphy-2023-pml2/ch36-causality-p2, pearl-2016-primer/ch03-effects, pearl-2018-bookofwhy/ch00-introduction]
canon_spine: bayesian
generated_by: build_kg.py
---

# propensity-score

## Canon spine entry

- **Propensity score** (bayesian): the probability of treatment given covariates; balancing on it removes measured confounding (grad)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch08-modeling]] (p. 204): $\Pr(I_i=1|X)=\pi_i$ in a strongly ignorable design; not sufficient for posterior predictive replications
- [[hernan-2020-whatif/ch07-confounding]] (p. 103): $\Pr[A=1|L]$, mentioned as a variation of stratification and matching
- [[hernan-2020-whatif/ch12-ip]] (p. 165): $\Pr[A=1|L]$, the denominator of the weight for binary treatment
- [[hernan-2020-whatif/ch14-g]] (p. 194; the term itself is not used on these pages): the model for $\Pr[A=1\mid L]$ is the Chapter 12 IP-weight denominator model plus $H(\psi^\dagger)$
- [[hernan-2020-whatif/ch15-outcome]] (p. 201): $\pi(L)=\Pr[A=1\mid L]$, estimated from data in observational studies
- [[hernan-2020-whatif/ch18-variable]] (p. 246, 251): $\pi(X)=E[A|X]$, a nuisance function for IP weighting and AIPW; the text also calls it the propensity score.
- [[hernan-2020-whatif/ch22-target]] (p. 322): $\Pr[A=1\mid U]$ used to define the random strategy $g$ in Fine Point 22.8
- [[murphy-2023-pml2/ch36-causality-p1]] (p. 1199): $g(x)=P(A=1\mid X=x)$
- [[murphy-2023-pml2/ch36-causality-p2]] (p. 1224): $g(x)=P(A=1|x)$; $\tilde g(x,u)$ adds the confounder
- [[pearl-2016-primer/ch03-effects]] (pp. 59, 72): $P(X=x|PA=z)$ or $P(X=x|Z=z)$; the denominator in (3.7) and the IPW weight
- [[pearl-2018-bookofwhy/ch00-introduction]] (pdf 21): listed among tools for managing sampling uncertainty

## Candidate bridges

- [same-math] Strongly ignorable assignment, $p(I|x,y,\phi)=p(I|x)$ ↔ causal inference: propensity-score theory — the chapter defines propensity scores from this condition. — from [[gelman-2013-bda3/ch08-modeling]] (bayesian → bayesian)
- [structural-analogy] TIRM's treatment projection ↔ causal inference: propensity score — a low-dimensional score for treatment likelihood used for matching — from [[grimmer-2022-textasdata/ch27-text]] (political-science → bayesian)
