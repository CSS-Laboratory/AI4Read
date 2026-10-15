---
id: pagerank
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 2
tiers: [core, deep]
grounding: digests
sources: [brin-1998-anatomy/main, bryan-2006-eigenvector/main]
generated_by: build_kg.py
---

# pagerank

## Definitions in the sources

### linear-algebra

- [[brin-1998-anatomy/main]] (pdf 4): a page's score: base amount plus damped sum of in-linkers' scores divided by their out-degrees [new]
- [[bryan-2006-eigenvector/main]] (p. 2, 10): importance score vector $q$ from the link structure; the positive, sum-one fixed point of $M$ [new]

## Instances that use it

- [[pagerank-formula]] — recursive link-weight definition with $d=0.85$ — from [[brin-1998-anatomy/main]]
- [[random-surfer-model]] — behavioural justification of PageRank — from [[brin-1998-anatomy/main]]
- [[cellular-phone-query]] — PageRank returns a result an advertiser would not want — from [[brin-1998-anatomy/main]]
- [[pagerank]] — a page's rank as the eigenvector of the click-probability matrix, eigenvalue 1 — from [[deisenroth-2020-mml/ch04-matrix-p1]]
- [[google-pagerank-power-iteration]] — the original PageRank algorithm uses power iteration on hyperlinks — from [[deisenroth-2020-mml/ch10-dimensionality]]
- [[web-in-degree-pagerank]] — Web in-degrees $\propto 1/k^2$; PageRank relies on this — from [[mitchell-2009-guidedtour/ch15-science]]
- [[google-matrix]] — PageRank matrix with all positive entries — from [[strang-2023-introduction/app1-ranks]]

## Candidate bridges

- [structural-analogy] β as probability of passing a message on ↔ damping in PageRank-style iteration — both attenuate longer paths geometrically. — from [[bonacich-1987-power/main]] (linear-algebra → unspecified)
- [structural-analogy] random surfer with restarts ↔ linear-algebra: Markov chain, steady-state eigenvector — the paper ties PageRank to a principal eigenvector but gives no derivation. — from [[brin-1998-anatomy/main]] (linear-algebra → linear-algebra)
- [structural-analogy] PageRank ↔ network science: eigenvector centrality — importance depends on importance of in-neighbours; the paper adds a constant term and a division by out-degree. — from [[brin-1998-anatomy/main]] (linear-algebra → complex-systems)
- [structural-analogy] PageRank scores ↔ network science: eigenvector centrality — a node's importance depends on the importance of its neighbours — from [[bryan-2006-eigenvector/main]] (linear-algebra → complex-systems)
- [same-math] PageRank vector $Ax^*=x^*$ via repeated multiplication $x,Ax,A^2x,\dots$ ↔ power iteration / Markov steady state — same eigenvector equation, with the iteration as described on p. 114. — from [[deisenroth-2020-mml/ch04-matrix-p1]] (linear-algebra → unspecified)
- [same-math] Power iteration for the top eigenvector ↔ network analysis: PageRank / eigenvector centrality — the same iteration on a different matrix. — from [[deisenroth-2020-mml/ch10-dimensionality]] (linear-algebra → complex-systems)
- [same-math] Random surfer with teleportation ↔ web search: PageRank steady-state distribution. — from [[rosvall-2008-maps/main-p1]] (information-theory → other:computer-science)
- [same-math] Perron's theorem for positive A ↔ network science: eigenvector centrality and PageRank use the dominant positive eigenvector of a nonnegative matrix. — from [[strang-2023-introduction/app1-ranks]] (linear-algebra → complex-systems)
- [structural-analogy] $P=D^{-1}W$ and stationary $\pi$ ↔ PageRank / Markov steady state: a similar random-walk transition matrix and stationary distribution. — from [[vonluxburg-2007-spectralclustering/main]] (linear-algebra → other:pagerank-markov-steady-state)
