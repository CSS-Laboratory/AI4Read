---
id: responsibility
type: concept
fields: [information-theory, bayesian, linear-algebra]
n_sources: 4
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch11-density, mackay-2003-information/ch20-example, mackay-2003-information/ch22-maximum, murphy-2023-pml2/ch28-latent-p1]
generated_by: build_kg.py
---

# responsibility

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch20-example]] (pp. 286, 289): degree $r_k^{(n)}$ to which cluster k owns point n; 0/1 in hard, in [0,1] in soft K-means [new]
- [[mackay-2003-information/ch22-maximum]] (pp. 303–304): $r_k^{(n)}$ or $p_{k|n}$: posterior probability that point $n$ belongs to cluster $k$ [new]

### bayesian

- [[murphy-2023-pml2/ch28-latent-p1]] (p. 931): posterior $p(z_n=k|x_n,\theta)$ of cluster $k$ for point $n$, via Bayes' rule [new]

### linear-algebra

- [[deisenroth-2020-mml/ch11-density]] (pp. 352, 367): $r_{nk}=\pi_k\mathcal N(\boldsymbol x_n\mid\cdot)/\sum_j\pi_j\mathcal N(\boldsymbol x_n\mid\cdot)$; soft assignment, later the posterior $p(z_{nk}=1\mid\boldsymbol x_n)$ [new]

## Instances that use it

- [[robin-cook-resignation-2003]] — collective cabinet responsibility in action — from [[clark-2017-principles/ch12-parliamentary-p1]]
- [[gmm-running-example-1d]] — 7 points, $K=3$; responsibility table, one update cycle (−28.3→−14.4), final fit after 5 EM iterations — from [[deisenroth-2020-mml/ch11-density]]
- [[gmm-2d-clusters-example]] — Figure 11.1 data fitted with $K=3$; EM takes 62 iterations; ambiguous points with responsibility near 0.5 — from [[deisenroth-2020-mml/ch11-density]]

## Candidate bridges

- [structural-analogy] Blame shifting in federalism ↔ retrospective voting: voting by outcomes works only if responsibility is identifiable (p. 691). — from [[clark-2017-principles/ch15-institutional-p2]] (political-science → political-science)
- [structural-analogy] clarity of responsibility as a necessary condition for accountability ↔ principal–agent problem: voters cannot sanction agents they cannot identify. — from [[clark-2017-principles/ch16-consequences-p1]] (political-science → other)
- [structural-analogy] Weighted covariance update (11.30) ↔ PCA/covariance matrix: the same average of outer products of centered data, but with responsibility weights. — from [[deisenroth-2020-mml/ch11-density]] (linear-algebra → linear-algebra)
- [structural-analogy] Responsibilities $r_n$ as a normalized probability vector (margin note: Boltzmann/Gibbs) ↔ softmax: normalizing positive scores into a distribution. — from [[deisenroth-2020-mml/ch11-density]] (linear-algebra → other)
- [same-math] soft-min responsibilities (20.7) ↔ softmax / Gibbs distribution $p\propto\exp(-\beta\,\text{energy})$ — same exponential-normalized form — from [[mackay-2003-information/ch20-example]] (information-theory → unspecified)
- [same-math] Responsibilities $r_{nk}$ (28.8) ↔ Bayesian inference: posterior over a discrete hypothesis from prior × likelihood, normalised — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → bayesian)
- [structural-analogy] Baum-Welch E/M steps ↔ EM for mixture models: soft responsibilities and normalised expected counts, with $\gamma$ and $\xi$ computed by forwards-backwards. — from [[murphy-2023-pml2/ch29-state-p1]] (bayesian → other)
