---
id: clustering
type: concept
fields: [decision-game-theory, bayesian, complex-systems, information-theory, linear-algebra]
fields_strong: [decision-game-theory, bayesian, complex-systems, information-theory, linear-algebra]
n_sources: 6
n_works: 4
tiers: [core]
grounding: digests
sources: [axelrod-1984-cooperation/ch05-evolution, axelrod-1984-cooperation/ch07-promote, axelrod-1984-cooperation/ch09-robustness, boyd-2018-vmls/ch04-clustering, mackay-2003-information/ch20-example, mitchell-2009-guidedtour/ch15-science]
generated_by: build_kg.py
---

# clustering

## Definitions in the sources

### decision-game-theory

- [[axelrod-1984-cooperation/ch05-evolution]] (p. 98): reciprocators interacting disproportionately with each other, which lets them invade ALL D [new]
- [[axelrod-1984-cooperation/ch07-promote]] (p. 131): a small group interacting enough among itself can invade a population of defectors [new]
- [[axelrod-1984-cooperation/ch09-robustness]] (p. 175): some interactions among nice, discriminating strategies; needed to start cooperation [new]

### complex-systems

- [[mitchell-2009-guidedtour/ch15-science]] (p. 101; Mitchell's informal usage): largely separate tight-knit communities in a network [new]

### information-theory

- [[mackay-2003-information/ch20-example]] (p. 284): grouping N objects into K clusters [new; work fields: information-theory, bayesian]

### linear-algebra

- [[boyd-2018-vmls/ch04-clustering]] (p. 69): partition $N$ vectors into $k$ groups of mutually close vectors [new]

## Instances that use it

- [[imageclef-color-histogram-clustering]] — 30-cluster mixture on 576-dim histograms of 10,000 images; CAVI vs. HMC sampler — from [[blei-2017-variational/main-p1]]
- [[mnist-digit-clustering]] — k-means with $k=20$ on 60000 vectors of length 784; most representatives are recognisable digits — from [[boyd-2018-vmls/ch04-clustering]]
- [[galaxy-acidity-iris-mixtures]] — overfitted Gaussian mixtures for density estimation and clustering — from [[gelman-2013-bda3/ch22-finite]]
- [[hospital-quality-hdp]] — hospitals in states, hierarchical clustering — from [[gelman-2013-bda3/ch23-dirichlet]]
- [[minimal-pairs-clustering]] — the four lexicons tested (Dutch, English, French, German) have more minimal pairs than phonotactic baselines — from [[gibson-2019-efficiency/main]]
- [[affinity-propagation]] — exemplar clustering by max-product LBP — from [[murphy-2023-pml2/ch09-message]]
- [[w-gmm-bregman-kmeans]] — Monte Carlo generator, clustering of Gaussian mixtures — from [[nielsen-2020-elementary/main-p2]]
- [[snow-cholera-map]] — dot-map clustering as evidence of a cause — from [[rogers-2003-diffusion/ch08-diffusion-p2]]
- [[spielman-teng-local-clustering]] — walk-and-sweep algorithm, analysed via Kwok–Lau–Lee — from [[spielman-2025-sagt/ch22-local]]
- [[cockroach-graph]] — ladder graph where unnormalized spectral clustering is $k/2$ times worse in RatioCut — from [[vonluxburg-2007-spectralclustering/main]]

## Candidate bridges

- [structural-analogy] Clustering of TIT FOR TAT ↔ network reciprocity: local interaction helps cooperators. — from [[axelrod-1984-cooperation/ch05-evolution]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Feature-space partitioning (Ex. 3.1.7–3.1.8) ↔ clustering: grouping states by similar features, like clusters in a feature space. — from [[bertsekas-2026-rlcourse/ch03-learning-p1]] (control-theory → linear-algebra)
- [metaphor] Fractal field structure ↔ multilevel or hierarchical clustering: the same dialogical pattern recurs at each level of granularity. — from [[craig-1999-field/main-p2]] (communication-theory → bayesian)
- [structural-analogy] Mixture model with observed $\pi_i$ ↔ supervised classification of documents by group (the book defers it to Ch. 19); unobserved $\pi$ ↔ clustering (Ch. 12). — from [[grimmer-2022-textasdata/ch06-multinomial]] (political-science → unspecified)
- [same-math] Hard clustering with $\Sigma_k=I$, uniform prior ↔ K-means nearest-centroid rule (28.10) — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → unspecified)
- [structural-analogy] LDA vs mixture models ↔ Clustering: mixed vs single-cluster assignment (p. 963). — from [[murphy-2023-pml2/ch28-latent-p2]] (bayesian → linear-algebra)
- [structural-analogy] Voronoi decoding cells ↔ geometry/clustering: nearest-center classification (p. 347) — from [[polyanskiy-2025-information/ch19-error]] (information-theory → other:mathematics)
- [structural-analogy] journal clusters ↔ network community detection (title of the work: maps of random walks reveal community structure) — each field here would be one module found in a journal network; the clustering method is not in these pages. — from [[rosvall-2008-maps/main-p3]] (information-theory → other:network-community-detection-title)
- [structural-analogy] Rounding $y$ to $x$ and sweeping thresholds ↔ spectral clustering: Fiedler-vector sweep cut. — from [[spielman-2025-sagt/ch22-local]] (linear-algebra → linear-algebra)
- [structural-analogy] Tanner neighbour growth ↔ community structure: a large λ₂ means no sparse cuts, the opposite of Fiedler-vector clustering. — from [[spielman-2025-sagt/ch27-properties]] (linear-algebra → complex-systems)
