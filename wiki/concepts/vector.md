---
id: vector
type: concept
fields: [linear-algebra]
n_sources: 7
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch01-vector, boyd-2018-vmls/ch01-vectors, brin-1998-anatomy/main, deisenroth-2020-mml/ch01-introduction, deisenroth-2020-mml/ch02-linear-p1, mikolov-2013-regularities/main, strang-2023-introduction/ch01-vectors]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# vector

## Canon spine entry

- **vector** (linear-algebra): an arrow or a list of numbers; anything you can add and scale (HS)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch01-vector]] (p. 8, 12): an element of a vector space; in $\mathbf{R}^2$ also seen as an arrow from the origin
- [[boyd-2018-vmls/ch01-vectors]] (p. 3): ordered finite list of numbers; an $n$-vector has size $n$
- [[brin-1998-anatomy/main]] (pdf 6, 12): type-weights and count-weights are vectors indexed by hit type; documents and queries in the vector space model are word-occurrence vectors
- [[deisenroth-2020-mml/ch01-introduction]] (p. 12): here, data as vectors; three views: array, arrow, object obeying addition and scaling
- [[deisenroth-2020-mml/ch02-linear-p1]] (p. 17): any object that can be added and scaled with a result of the same kind; the book mostly uses elements of Rⁿ
- [[mikolov-2013-regularities/main]] (p. 747): a word is a real-valued vector, the column of $\mathbf U$ for that word
- [[strang-2023-introduction/ch01-vectors]] (p. 2): a list of numbers (arrow from the origin) that can be added and scaled

## Instances that use it

- [[two-coin-vector]] — the transformations $N$ and $M$ on four vector states — from [[ashby-1956-cybernetics/ch03-determinate]]
- [[traffic-lights-entropy-and-redundancy]] — entropy 1.63 bits (pp. 174–175); redundancy in two different sets of vectors — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[thermostat-compound-target]] — vector E with two conditions — from [[ashby-1956-cybernetics/ch11-requisite]]
- [[coin-spun-six-times]] — basic variety 2, vector variety 64 — from [[ashby-1956-cybernetics/ch13-regulating]]
- [[tensor-of-two-column-vectors]] — $v\otimes w\leftrightarrow(v_jw_k)$ — from [[axler-2024-ladr/ch09-multilinear-p2]]
- [[gradient-of-squared-norm-of-vector-function]] — $\nabla h(z)=2Df(z)^Tf(z)$ — from [[boyd-2018-vmls/app-appendices]]
- [[rgb-color-vector]] — a 3-vector as a color — from [[boyd-2018-vmls/ch01-vectors]]
- [[word-count-vector]] — document as counts or histogram over a dictionary; sentiment via $w^Tx$ — from [[boyd-2018-vmls/ch01-vectors]]
- [[portfolio-vector]] — holdings per asset, trade vector, value $p^Ts$, return $r^Tw$ — from [[boyd-2018-vmls/ch01-vectors]]
- [[image-as-vector]] — $M\times N$ pixels as a length-$MN$ vector — from [[boyd-2018-vmls/ch01-vectors]]
- [[market-clearing]] — sum of agents' vectors equals zero — from [[boyd-2018-vmls/ch01-vectors]]
- [[mnist-digit-clustering]] — k-means with $k=20$ on 60000 vectors of length 784; most representatives are recognisable digits — from [[boyd-2018-vmls/ch04-clustering]]
- [[kmeans-worked-iteration-fig-4-2]] — one assignment-plus-update iteration on 30 2-vectors — from [[boyd-2018-vmls/ch04-clustering]]
- [[standard-unit-vectors]] — $e_1,\dots,e_n$ are independent, orthonormal and a basis — from [[boyd-2018-vmls/ch05-linear]]
- [[orthonormal-basis-example-5-3]] — a 3-vector orthonormal basis used to expand $(1,2,3)$ — from [[boyd-2018-vmls/ch05-linear]]
- [[gram-schmidt-4-vector-example]] — three 4-vectors orthonormalized, with no early stop — from [[boyd-2018-vmls/ch05-linear]]
- [[bill-clinton-query]] — failure of the vector space model on the web, and Google's results via anchor text and proximity — from [[brin-1998-anatomy/main]]
- [[nairobi-kigali-example]] — geographic example of linearly dependent vectors in the plane — from [[deisenroth-2020-mml/ch02-linear-p1]]
- [[example-coordinates-in-two-bases]] — Example 2.20: the vector with standard coordinates $[2,3]^\top$ has coordinates $\tfrac12[-1,5]^\top$ in basis $([1,-1]^\top,[1,1]^\top)$ — from [[deisenroth-2020-mml/ch02-linear-p2]]
- [[king-man-woman-queen]] — vector offset solves analogies, though not explicitly trained for it — from [[grimmer-2022-textasdata/ch08-distributed]]
- [[embedding-bias]] — gender and ethnic stereotypes in pretrained vectors — from [[grimmer-2022-textasdata/ch08-distributed]]
- [[country-capital-pca]] — Fig. 2: a 2-D PCA of 1000-d vectors illustrates the model organizing country–capital relationships implicitly; the authors say no supervised information about what a capital city means was given — from [[mikolov-2013-compositionality/main]]
- [[king-queen-analogy]] — vector(King) − vector(Man) + vector(Woman) nearest to Queen, reported from [20] — from [[mikolov-2013-efficient/main]]
- [[binary-pca-prototypes]] — 150 bit vectors from 3 prototypes cluster in a 2D latent space — from [[murphy-2023-pml2/ch28-latent-p1]]
- [[k-means]] — optimal vector quantization of the empirical distribution — from [[polyanskiy-2025-information/ch27-rate]]
- [[sparse-vector-denoising]] — rate $\frac kn\log\frac{ed}k$ — from [[polyanskiy-2025-information/ch33-mutual]]
- [[latent-smile-direction]] — resynthesis by vector arithmetic in latent space — from [[prince-2023-udl/ch17-variational]]
- [[bias-in-state-vector]] — drifting velocity-sensor bias — from [[sarkka-2023-bayesianfiltering/ch05-modeling]]
- [[bentley-parallelogram-of-forces]] — groups as force vectors acting on the policy status quo — from [[shepsle-2010-analyzing/ch09-collective-p1]]
- [[complete-graph]] — L = nI − 11ᵀ, which acts as n times the identity on vectors orthogonal to 1; (5.1) is sharp — from [[spielman-2025-sagt/ch05-fundamental]]
- [[hypercube]] — Cayley graph on (Z/2)^d with unit-vector generators — from [[spielman-2025-sagt/ch07-cayley]]
- [[shifted-indicator-test-vector]] — $\mathbf 1_S$ minus a constant, used to bound an eigenvalue — from [[spielman-2025-sagt/ch20-graph]]
- [[polytope-skeleton-laplacian]] — the matrix built from face vectors and cross products on a polytope — from [[spielman-2025-sagt/ch26-planar]]
- [[kadison-singer-problem]] — essentially equivalent to dropping scale factors for equal-norm vectors — from [[spielman-2025-sagt/ch33-linear]]
- [[bioreactor]] — vector-valued states and actions — from [[sutton-2018-rl/ch03-finite]]
- [[pick-and-place-robot]] — vector-valued states and actions — from [[sutton-2018-rl/ch03-finite]]
- [[pomdp-belief-state]] — the belief vector as a Markov state — from [[sutton-2018-rl/ch17-frontiers]]

## Candidate bridges

- [structural-analogy] Phase space with arrow field ↔ control-theory: phase portrait / vector field of a dynamical system. — from [[ashby-1956-cybernetics/ch03-determinate]] (control-theory → control-theory)
- [same-math] Population update $D'=MD$ with a column-stochastic $M$ ↔ control-theory: discrete-time linear state-space model $x_{k+1}=Ax_k$. The equilibrium is a fixed vector of $M$, and the "dying oscillations" are mode behaviour. — from [[ashby-1956-cybernetics/ch09-incessant]] (control-theory → control-theory)
- [structural-analogy] Modes and eigenvectors ↔ principal components / spectral decomposition in data analysis: a state vector decomposed along eigen-directions that evolve independently. — from [[astrom-2021-feedbacksystems/ch06-linear]] (control-theory → linear-algebra)
- [same-math] Function space $\mathbf{F}^S$ ↔ data as vectors in applied settings: a dataset indexed by a finite set $S$ is literally an element of $\mathbf{F}^S$, as $\mathbf{F}^n$ is $\mathbf{F}^{\{1..n\}}$ (p. 14). — from [[axler-2024-ladr/ch01-vector]] (linear-algebra → other)
- [metaphor] linear independence ("no vector is redundant") ↔ statistics/data: redundant, collinear features — an informal way to think about dependent lists. — from [[axler-2024-ladr/ch02-finite]] (linear-algebra → other)
- [structural-analogy] reducing a spanning list to a basis (2.30) ↔ numerical methods: a greedy, left-to-right procedure that keeps only vectors outside the span of earlier ones — compare with Gram–Schmidt in the canon. — from [[axler-2024-ladr/ch02-finite]] (linear-algebra → other)
- [same-math] 3.25 map $\mathbf F^n\to\mathbf F^m$ ↔ matrix–vector product $Ax$ — the coefficient array $A_{j,k}$ is the matrix (matrix introduced later in the chapter). — from [[axler-2024-ladr/ch03-linear-p1]] (linear-algebra → unspecified)
- [same-math] 3.50 "Ab is a combination of columns of A" ↔ linear-algebra spine: matrix–vector product as column space reachability — from [[axler-2024-ladr/ch03-linear-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] 3.70 (dimension classifies vector spaces) ↔ other fields: classification of structures up to isomorphism by one invariant; the author notes this is hard for groups or topological spaces (p. 86) — from [[axler-2024-ladr/ch03-linear-p2]] (linear-algebra → other)
- [same-math] ℳ(T′)=ℳ(T)ᵗ ↔ linear-algebra: transpose matrix Aᵗ acting on row vectors. The dual map is the coordinate-free transpose. — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → linear-algebra)
- [structural-analogy] Dual basis as coordinate functionals ↔ statistics/data: a regression coefficient or weight vector as a linear readout of a feature vector. — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → other)
- [structural-analogy] Vector-state multi-activity recursion ↔ state-space models: resources as state vector, allocations as inputs. — from [[bellman-1957-dp/ch01-i-p2]] (control-theory → other)
- [structural-analogy] Type Three problem with $p$ a probability vector over states ↔ belief-state formulation of decisions under partial observation: "observe the true state" resets the belief to a vertex. — from [[bellman-1957-dp/ch04-iv]] (control-theory → other)
- [structural-analogy] $e_i^Ta=a_i$ and $b=\sum b_ie_i$ ↔ basis and coordinates: unit vectors play the role of a coordinate system. — from [[boyd-2018-vmls/ch01-vectors]] (linear-algebra → other)
- [structural-analogy] sparsity pattern of a vector ↔ network science: the set of neighbors of a node in an adjacency row. — from [[boyd-2018-vmls/ch01-vectors]] (linear-algebra → complex-systems)
- [same-math] $a^Ta=\sum a_i^2$ ↔ norm: squared Euclidean length of a vector (the norm is not defined in this unit). — from [[boyd-2018-vmls/ch01-vectors]] (linear-algebra → other)
- [structural-analogy] word-count vectors and $a^Tb$ for 0/1 occurrence vectors ↔ text analysis/set similarity: overlap counts between documents or subsets. — from [[boyd-2018-vmls/ch01-vectors]] (linear-algebra → other)
- [same-math] Regression prediction $\hat y=\tilde x^T\tilde\beta$ with a constant feature ↔ machine learning: linear model with bias absorbed into the weight vector. — from [[boyd-2018-vmls/ch02-linear]] (linear-algebra → other)
- [structural-analogy] Determining $f$ from $f(e_i)$ ↔ matrix as transformation: columns of $A$ are the images of the basis vectors (the scalar case is a single row). — from [[boyd-2018-vmls/ch02-linear]] (linear-algebra → linear-algebra)
- [same-math] Correlation coefficient ρ = cos∠(ã, b̃) ↔ cosine similarity of centred data vectors — the same formula, applied to mean-removed vectors. — from [[boyd-2018-vmls/ch03-norm]] (linear-algebra → unspecified)
- [structural-analogy] ‖x+y‖² = ‖x‖² + 2‖x‖‖y‖cosθ + ‖y‖² ↔ std(a+b)² = std(a)² + 2ρ std(a)std(b) + std(b)²: the second is the first applied to de-meaned vectors, divided by n. — from [[boyd-2018-vmls/ch03-norm]] (linear-algebra → other)
- [structural-analogy] word-histogram vectors and distance ↔ cosine similarity / embeddings: documents as vectors compared by geometry, though this chapter uses Euclidean distance, not cosine. — from [[boyd-2018-vmls/ch04-clustering]] (linear-algebra → other)
- [metaphor] representatives as archetypes ↔ principal component analysis: both summarise data by a few prototype vectors, but via different constructions. — from [[boyd-2018-vmls/ch04-clustering]] (linear-algebra → other)
- [structural-analogy] Unique coefficients in a basis ↔ linear-algebra: injectivity of a map $\beta\mapsto\sum\beta_ia_i$ — independence means this map never sends two coefficient lists to the same vector. — from [[boyd-2018-vmls/ch05-linear]] (linear-algebra → linear-algebra)
- [structural-analogy] Early stop of Gram–Schmidt ↔ rank: it finds the first vector that adds no new direction (canon link; rank is not stated in this unit). — from [[boyd-2018-vmls/ch05-linear]] (linear-algebra → other)
- [structural-analogy] Document scoring $s=Aw$ ↔ regression/text mining: a linear score on a count vector, computed row by row as inner products. — from [[boyd-2018-vmls/ch06-matrices]] (linear-algebra → other)
- [same-math] Convolution of coefficient vectors ↔ polynomial multiplication (shown on p. 137). — from [[boyd-2018-vmls/ch07-matrix]] (linear-algebra → unspecified)
- [same-math] linear function determined by $f(e_k)$ ↔ linear-algebra: matrix as transformation (columns are images of basis vectors) — same statement. — from [[boyd-2018-vmls/ch08-linear]] (linear-algebra → linear-algebra)
- [structural-analogy] K-Markov model ↔ vector auto-regression in econometrics (named on p. 164). — from [[boyd-2018-vmls/ch09-linear]] (linear-algebra → unspecified)
- [same-math] Matrix least squares for the $K$ coefficient vectors ↔ linear-algebra: least squares with a matrix right-hand side (the text points to p. 233) — same $X$, many right-hand sides. — from [[boyd-2018-vmls/ch14-least]] (linear-algebra → linear-algebra)
- [same-math] $D_q=X_q'TS^{-1}$ ↔ linear-algebra: coordinates of the projection of a vector onto the span of the columns of $T$ (since $T'T=I$, $T'X_q$ gives the coordinates, then rescaled by $S^{-1}$). — from [[deerwester-1990-lsa/main]] (linear-algebra → linear-algebra)
- [structural-analogy] "Similar vectors get similar predictions" ↔ linear algebra: inner-product similarity such as cosine similarity (p. 14). The unit does not name the operation. — from [[deisenroth-2020-mml/ch01-introduction]] (linear-algebra → linear-algebra)
- [metaphor] Different inner products ↔ different "rulers" for the same space: the same vectors get different lengths and angles (p. 75, 77). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other)
- [same-math] PageRank vector $Ax^*=x^*$ via repeated multiplication $x,Ax,A^2x,\dots$ ↔ power iteration / Markov steady state — same eigenvector equation, with the iteration as described on p. 114. — from [[deisenroth-2020-mml/ch04-matrix-p1]] (linear-algebra → unspecified)
- [same-math] correlation $=\cos\theta$ (6.61) ↔ linear-algebra: cosine similarity — the inner product of normalised (centred) vectors. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → linear-algebra)
- [structural-analogy] closure of convexity under nonnegative sums ↔ linear-algebra: closure of vector spaces (the author draws this parallel, p. 238). — from [[deisenroth-2020-mml/ch07-continuous]] (linear-algebra → linear-algebra)
- [structural-analogy] Responsibilities $r_n$ as a normalized probability vector (margin note: Boltzmann/Gibbs) ↔ softmax: normalizing positive scores into a distribution. — from [[deisenroth-2020-mml/ch11-density]] (linear-algebra → other)
- [structural-analogy] Convex-hull weights ($\alpha_n\ge0$, $\sum\alpha_n=1$) ↔ Markov (stochastic) matrix columns — both are probability-like weight vectors. — from [[deisenroth-2020-mml/ch12-classification]] (linear-algebra → unspecified)
- [same-math] Linear-model interference $\sum_{i\ne j}|W_i\cdot W_j|^2$ ↔ compressed sensing: coherence $\max_{i\ne j}|W_i\cdot W_j|$ — the $L^2$ and $L^\infty$ norms of the same off-diagonal vector. — from [[elhage-2022-superposition/main-p1]] (llm → other)
- [same-math] Feature dimensionality $D_i$ ↔ numerical linear algebra: leverage score, roughly equal when the vectors are in isotropic position (Zhang's argument). — from [[elhage-2022-superposition/main-p2]] (llm → linear-algebra)
- [structural-analogy] $\mathrm{softmax}(xK^\top)V$ (Eq. 2) ↔ attention: weighted average of value vectors with query–key weights. Here keys and values are fixed parameters and no scaling is shown. — from [[geva-2021-ffn/main]] (llm → other)
- [same-math] cosine similarity ↔ geometry: cosine of the angle between vectors; for unit vectors, squared Euclidean distance $=2(1-\cos)$ (p. 133). — from [[grimmer-2022-textasdata/ch07-vector]] (political-science → other)
- [structural-analogy] vector-space distances ↔ probability models: both compare documents. Cosine is related to the von Mises–Fisher distribution (p. 138). — from [[grimmer-2022-textasdata/ch07-vector]] (political-science → other)
- [structural-analogy] pointwise multiplier $\lambda^*(x)$ ↔ control theory: costate/adjoint vector (stated on p. 45) — from [[liberzon-2012-calculus/ch02-calculus]] (control-theory → control-theory)
- [structural-analogy] adjoint vector $p^*$ ↔ Lagrange multipliers: both enforce a dynamic constraint inside the cost, and the text says $p$ is "reminiscent of" $\lambda$ but not identical (pp. 73, 75) — from [[liberzon-2012-calculus/ch03-calculus]] (control-theory → other)
- [same-math] Hamiltonian vector field flow (7.8) ↔ classical mechanics (Sec. 2.4): Hamilton's canonical equations — same equations, now read as a symplectic flow. — from [[liberzon-2012-calculus/ch07-advanced]] (control-theory → other)
- [structural-analogy] vector quantization ↔ information-theory: lossy compression with distortion (rate–distortion) — the chapter gives distortion (20.1) but no rate analysis — from [[mackay-2003-information/ch20-example]] (information-theory → information-theory)
- [metaphor] encoder of a vector quantizer ↔ decoding of an error-correcting code (noted in passing, p. 285) — from [[mackay-2003-information/ch20-example]] (information-theory → unspecified)
- [same-math] Invariant distribution of an MCMC chain (eigenvalue 1 of T) ↔ linear algebra: Perron–Frobenius-style stationary vector of a column-stochastic matrix — the text states the eigenvector fact (p. 372). — from [[mackay-2003-information/ch29-monte]] (information-theory → linear-algebra)
- [structural-analogy] Vector of intercepts `a[actor]` ↔ hierarchical models: the same indexing structure that multilevel models will use (p. 299) — from [[mcelreath-2020-rethinking/ch10-counting]] (bayesian → other)
- … 32 more bridge lines mention this id (see wiki/kg/bridges.jsonl)
