---
id: k-means
type: concept
fields: [political-science, information-theory, linear-algebra]
n_sources: 4
tiers: [core, deep]
grounding: digests
sources: [deisenroth-2020-mml/ch11-density, grimmer-2013-textasdata/main, grimmer-2022-textasdata/ch12-clustering, mackay-2003-information/ch20-example]
generated_by: build_kg.py
---

# k-means

## Definitions in the sources

### political-science

- [[grimmer-2013-textasdata/main]] (p. 16): clustering that minimises within-cluster squared Euclidean distance; local optima [new]
- [[grimmer-2022-textasdata/ch12-clustering]] (pp. 205–207): alternate nearest-center assignment and mean update to minimize summed squared Euclidean distance [new]

### information-theory

- [[mackay-2003-information/ch20-example]] (p. 286): alternate nearest-mean assignment and mean update; a hard-assignment clustering algorithm [new]

### linear-algebra

- [[deisenroth-2020-mml/ch11-density]] (p. 368): hard-assignment relative of GMM-EM [new]

## Instances that use it

- [[mnist-digit-clustering]] — k-means with $k=20$ on 60000 vectors of length 784; most representatives are recognisable digits — from [[boyd-2018-vmls/ch04-clustering]]
- [[k-means-local-optimum-example]] — Tables 12.1 vs. 12.3: same method, different starts, different clusters — from [[grimmer-2022-textasdata/ch12-clustering]]
- [[little-n-large-clusters]] — in the Fig. 20.5 example, K-means assigns points of the broad cluster to the narrow one; the clusters differ in weight and breadth — from [[mackay-2003-information/ch20-example]]
- [[elongated-clusters-sliced]] — K-means cuts two elongated clusters in half — from [[mackay-2003-information/ch20-example]]
- [[soft-k-means-as-em]] — delta-function Q_θ; "kaboom" problem — from [[mackay-2003-information/ch33-variational]]
- [[k-means]] — optimal vector quantization of the empirical distribution — from [[polyanskiy-2025-information/ch27-rate]]
- [[k-means]] — maps $\mathbf{x}$ to a cluster index $z$ — from [[prince-2023-udl/ch14-unsupervised]]

## Candidate bridges

- [structural-analogy] k-means centroid update (mean minimises sum of squared distances) ↔ least squares: both minimise a sum of squared distances, and the mean is the best single constant fit (exercise 4.1 shows the minimiser). — from [[boyd-2018-vmls/ch04-clustering]] (linear-algebra → other)
- [structural-analogy] GMM-EM ↔ K-means: with covariances ignored, soft assignment becomes hard assignment (stated on p. 368). — from [[deisenroth-2020-mml/ch11-density]] (linear-algebra → other)
- [structural-analogy] k-means as limit of a Gaussian mixture as covariances → 0 ↔ statistics: hard-EM as limit of soft-EM — the chapter states the limiting relation (p. 222). — from [[grimmer-2022-textasdata/ch12-clustering]] (political-science → other)
- [structural-analogy] K-means two-step loop ↔ bayesian: assigning data to hidden causes, then re-fitting parameters, as in mixture-model inference — the book says it returns to this view later (p. 290) — from [[mackay-2003-information/ch20-example]] (information-theory → bayesian)
- [same-math] Soft K-means update (22.21) ↔ Expectation–Maximization for Gaussian mixtures — the same weighted-mean update; these pages never mention EM, and say only that a proof that the algorithm maximizes the likelihood is deferred to section 33.7 (p. 305). — from [[mackay-2003-information/ch22-maximum]] (information-theory → unspecified)
- [structural-analogy] Gibbs sampling for mixtures ↔ soft K-means: alternate sampling labels and updating parameters, as noted in Ex. 29.16 (p. 383). — from [[mackay-2003-information/ch29-monte]] (information-theory → other)
- [same-math] Hard clustering with $\Sigma_k=I$, uniform prior ↔ K-means nearest-centroid rule (28.10) — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → unspecified)
- [same-math] Lloyd's algorithm ↔ machine learning: $k$-means heuristic — the text states the objective is the same (p. 481). — from [[polyanskiy-2025-information/ch27-rate]] (information-theory → other)
