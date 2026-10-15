---
id: nielsen-2020-elementary/index
work: nielsen-2020-elementary
type: work-map
units: [nielsen-2020-elementary/main-p1, nielsen-2020-elementary/main-p2]
---

# Nielsen, F. (2020). *An Elementary Introduction to Information Geometry*. Entropy, 22(10), 1100. DOI 10.3390/e22101100.

## In one paragraph
The paper shows how families of probability distributions can be studied with differential geometry. A family becomes a manifold with a metric (local lengths and angles) and two coupled "dual" connections (rules for transporting vectors and defining straight curves). These structures come from a divergence, or from exponential and mixture families. A convex potential and its Legendre conjugate give a dually flat space whose canonical divergence is a Bregman divergence. KL divergence arises this way: reverse KL for exponential families, forward KL for mixture families. The Fisher metric is the unique invariant metric under Markov embeddings, up to scale. The same structure explains natural gradient, mirror descent and Chernoff information. Proofs are mostly omitted.

## The path through the work
- [[nielsen-2020-elementary/main-p1]] — Information geometry treats a family of probability models as a curved space (a manifold) with a metric and two coupled "dual" connections, built from a divergence or from exponential/mixture families.
- [[nielsen-2020-elementary/main-p2]] — A convex potential $F$ and its conjugate $F^*$ make a dually flat space whose canonical divergence is a Bregman divergence. The KL divergence arises this way from exponential families (reverse KL) and mixture families (forward KL). The same structure gives geometric descriptions of natural gradient, mirror descent and (within an exponential family) Chernoff information.

## Big ideas across units
- **Metric and connection are separate structures.** The metric gives lengths and angles, and the connection gives transport, geodesics and curvature. The Levi-Civita connection (Riemannian geometry) is the self-dual special case, and conjugate pairs generalize it. Units: main-p1, main-p2 (which uses the Riemannian metric and connection language).
- **Divergences generate geometry.** A divergence induces a metric and a pair of conjugate connections. Bregman divergences of convex potentials give dually flat spaces. Units: main-p1, main-p2.
- **Legendre duality and dual coordinates.** The coordinates $\theta$ and $\eta=\nabla F(\theta)$ come with dual Pythagorean identities in part 1 and dual Hessian metrics in part 2. Units: main-p1, main-p2.
- **KL divergence as a Bregman divergence.** Exponential families (log-normalizer as $F$) give reverse KL, and mixture families (negative entropy as $F$) give forward KL. Units: main-p1 (exponential/mixture families, dual and flat), main-p2 (KL identification).
- **Statistical invariance.** The Fisher metric is unique under Markov embeddings, and f-divergences are the only invariant separable divergences. Part 2 uses the extended f-divergence to fix the Monte Carlo KL estimator. Units: main-p1, main-p2.
- **Geometry yields algorithms and tools.** Natural gradient equals ordinary gradient in dual coordinates. Mirror descent is natural gradient in the dual space. Chernoff information is a Bregman divergence, and Monte Carlo generators support Bregman clustering of mixtures. Unit: main-p2, built on the dually flat theory of main-p1.
- **Distances versus divergences.** Fisher–Rao distance is the geodesic distance of the Fisher metric. Squared Riemannian distances are divergences, but powers of divergences need not be metrics. Units: main-p1, main-p2.

## How to read it
- **Essential:** main-p1 is the foundation (manifold, metric, connections, conjugacy, Bregman divergence, dual flatness, Fisher metric). It is needed for everything in main-p2.
- **Depends on part 1:** main-p2 assumes the metric tensor, connections and Fisher information from main-p1. Its core is the identification of KL with a Bregman divergence, and its applications follow from that.
- **Can be skipped on a first pass:** the invariance results (Markov embeddings, f-divergence uniqueness) in main-p1, and the Monte Carlo clustering part of the applications in main-p2. Appendix A (f-divergence estimation) and Appendix B (Gaussian formulas) are reference material in main-p2.
- The catalog suggests reading after Cover & Thomas Ch. 2 and 11. The units list prerequisites such as KL divergence, convex functions and expectation/covariance.

## Concepts introduced
Several ids below probably name the same idea, but they are kept as given in the units.
- [[metric-tensor]] — main-p1
- [[affine-connection]] — main-p1
- [[curvature-torsion]] — main-p1
- [[levi-civita-connection]] — main-p1
- [[conjugate-connections]] — main-p1
- [[statistical-manifold]] — main-p1
- [[alpha-connection]] — main-p1
- [[divergence-parameter]] — main-p1
- [[bregman-divergence]] — main-p1
- [[dually-flat-manifold]] — main-p1 (main-p2 uses [[dually-flat-space]])
- [[legendre-fenchel-transform]] — main-p1 (main-p2 uses [[legendre-fenchel-conjugate]])
- [[mixture-family]] — main-p1
- [[information-monotonicity]] — main-p1
- [[markov-embedding]] — main-p1
- [[f-divergence]] — main-p1
- [[relative-entropy-kl-divergence]] — main-p1
- [[fisher-information]] — main-p1
- [[fisher-rao-metric-information-geometry]] — main-p1 (main-p2 uses [[fisher-rao-information-geometry]])
- [[exponential-family]] — main-p1 (main-p2 uses [[exponential-family-gibbs]])
- [[legendre-fenchel-conjugate]] — main-p2
- [[dually-flat-space]] — main-p2
- [[natural-gradient]] — main-p2
- [[mirror-descent]] — main-p2
- [[chernoff-information]] — main-p2
- [[exponential-family-gibbs]] — main-p2
- [[fisher-rao-information-geometry]] — main-p2
- [[differential-entropy]] — main-p2
- [[cross-entropy]] — main-p2
