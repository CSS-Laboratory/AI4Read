---
id: k-means
type: instance
fields: [information-theory, llm]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [polyanskiy-2025-information/ch27-rate, prince-2023-udl/ch14-unsupervised]
generated_by: build_kg.py
---

# k-means

## Descriptions in the sources

### information-theory

- [[polyanskiy-2025-information/ch27-rate]] (p. 481): optimal vector quantization of the empirical distribution

### llm

- [[prince-2023-udl/ch14-unsupervised]] (p. 270): maps $\mathbf{x}$ to a cluster index $z$

## Candidate bridges

- [structural-analogy] k-means centroid update (mean minimises sum of squared distances) ↔ least squares: both minimise a sum of squared distances, and the mean is the best single constant fit (exercise 4.1 shows the minimiser). — from [[boyd-2018-vmls/ch04-clustering]] (linear-algebra → other)
- [structural-analogy] GMM-EM ↔ K-means: with covariances ignored, soft assignment becomes hard assignment (stated on p. 368). — from [[deisenroth-2020-mml/ch11-density]] (linear-algebra → other)
- [structural-analogy] k-means as limit of a Gaussian mixture as covariances → 0 ↔ statistics: hard-EM as limit of soft-EM — the chapter states the limiting relation (p. 222). — from [[grimmer-2022-textasdata/ch12-clustering]] (political-science → other)
- [structural-analogy] K-means two-step loop ↔ bayesian: assigning data to hidden causes, then re-fitting parameters, as in mixture-model inference — the book says it returns to this view later (p. 290) — from [[mackay-2003-information/ch20-example]] (information-theory → bayesian)
- [same-math] Soft K-means update (22.21) ↔ Expectation–Maximization for Gaussian mixtures — the same weighted-mean update; these pages never mention EM, and say only that a proof that the algorithm maximizes the likelihood is deferred to section 33.7 (p. 305). — from [[mackay-2003-information/ch22-maximum]] (information-theory → unspecified)
- [structural-analogy] Gibbs sampling for mixtures ↔ soft K-means: alternate sampling labels and updating parameters, as noted in Ex. 29.16 (p. 383). — from [[mackay-2003-information/ch29-monte]] (information-theory → other)
- [same-math] Hard clustering with $\Sigma_k=I$, uniform prior ↔ K-means nearest-centroid rule (28.10) — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → unspecified)
- [same-math] Lloyd's algorithm ↔ machine learning: $k$-means heuristic — the text states the objective is the same (p. 481). — from [[polyanskiy-2025-information/ch27-rate]] (information-theory → other)
