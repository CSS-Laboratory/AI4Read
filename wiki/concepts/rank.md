---
id: rank
type: concept
fields: [linear-algebra]
n_sources: 18
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch03-linear-p2, axler-2024-ladr/ch03-linear-p3, axler-2024-ladr/ch07-operators-p3, deerwester-1990-lsa/main, deisenroth-2020-mml/ch02-linear-p2, deisenroth-2020-mml/ch04-matrix-p1, deisenroth-2020-mml/ch04-matrix-p2, deisenroth-2020-mml/ch09-linear, eckart-1936-lowrank/main, spielman-2025-sagt/ch02-eigenvalues, spielman-2025-sagt/ch23-spectral, strang-2023-introduction/app1-ranks, strang-2023-introduction/ch01-vectors, strang-2023-introduction/ch02-solving-p1, strang-2023-introduction/ch03-four-p1, strang-2023-introduction/ch03-four-p2, strang-2023-introduction/ch03-four-p3, strang-2023-introduction/ch04-orthogonality-p2]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# rank

## Canon spine entry

- **rank** (linear-algebra): the dimension of the column space; how many independent directions survive (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch03-linear-p2]] (pp. 77–79, 90): column rank of a matrix (equal to row rank); also dim range T for T with matrix M(T)
- [[axler-2024-ladr/ch03-linear-p3]] (p. 114): column rank equals row rank, reproved by duality
- [[axler-2024-ladr/ch07-operators-p3]] (p. 272): number of positive singular values (7.68(b))
- [[deerwester-1990-lsa/main]] (pdf 13): $m$, the rank of $X$; the truncated model has rank $k\le m$
- [[deisenroth-2020-mml/ch02-linear-p2]] (p. 47): number of independent columns, equal to the number of independent rows; $\mathrm{rk}(A)=\mathrm{rk}(A^\top)$
- [[deisenroth-2020-mml/ch04-matrix-p1]] (pp. 103, 105): full rank $n$ is equivalent to invertibility; $\operatorname{rk}(A-\lambda I)<n$ characterises eigenvalues
- [[deisenroth-2020-mml/ch04-matrix-p2]] (pp. 126, 130): number of nonzero singular values in the construction; $\mathrm{rk}(\widehat A(k))=k$
- [[deisenroth-2020-mml/ch09-linear]] (p. 297): $\Phi^\top\Phi$ is invertible iff $\mathrm{rk}(\Phi)=K$
- [[eckart-1936-lowrank/main]] (p. 215): number of nonzero diagonal entries in the canonic form
- [[spielman-2025-sagt/ch02-eigenvalues]] (p. 26): here, the dimension of the span of $M$; drops by 1 under deflation
- [[spielman-2025-sagt/ch23-spectral]] (p. 191): $\widehat A$ has rank 2, which makes its spectrum explicit
- [[strang-2023-introduction/app1-ranks]] (p. 400): number of independent columns (= independent rows); cannot increase under multiplication
- [[strang-2023-introduction/ch01-vectors]] (pp. 22, 32): r, the number of independent columns of A (also of rows; informal proof)
- [[strang-2023-introduction/ch02-solving-p1]] (pp. 40, 43): here: full rank means n nonzero pivots in a square matrix; rank 1 example for 2 by 2 singular
- [[strang-2023-introduction/ch03-four-p1]] (pp. 88, 93): r, the number of independent columns; rank A = rank Aᵀ
- [[strang-2023-introduction/ch03-four-p2]] (p. 120): dimension of $C(A)$
- [[strang-2023-introduction/ch03-four-p3]] (pp. 129, 132): number of pivots = number of independent columns = number of independent rows
- [[strang-2023-introduction/ch04-orthogonality-p2]] (p. 193): $r$ is the common dimension of row and column space, and equals the number of columns of $C$

## Instances that use it

- [[rank-order-voting-example]] — 3 voters, 4 candidates, weights 4,3,2,1; deleting $y$ turns $x$'s win into a tie — from [[arrow-1951-socialchoice/ch03-iii]]
- [[harrington-rule]] — best not-nice rule, rank 8 — from [[axelrod-1984-cooperation/appa-tournament]]
- [[leyland-rule]] — rank 49 actually, but first in the hypothetical tournament with REVISED STATE TRANSITION times five — from [[axelrod-1984-cooperation/appa-tournament]]
- [[example-3-53-column-row-rank]] — a 2×4 matrix with both ranks 2 — from [[axler-2024-ladr/ch03-linear-p2]]
- [[rank-one-adjoint-example]] — 7.3, $T^*w=\langle w,x\rangle u$ — from [[axler-2024-ladr/ch07-operators-p1]]
- [[pagerank]] — a page's rank as the eigenvector of the click-probability matrix, eigenvalue 1 — from [[deisenroth-2020-mml/ch04-matrix-p1]]
- [[movie-ratings-svd]] — $u_i$ as stereotypical movies, $v_j$ as stereotypical viewers; rank-2 approximation is close to the ratings — from [[deisenroth-2020-mml/ch04-matrix-p2]]
- [[stonehenge-image-compression]] — rank-5 uses about 0.6% of the numbers — from [[deisenroth-2020-mml/ch04-matrix-p2]]
- [[ivy-league-spring-training]] — a cartel limits wasteful competition in a rank-based game — from [[dixit-2008-art-strategy/ch09-cooperation]]
- [[factor-theory-score-matrix]] — an $n\times N$ matrix of $n$ tests by $N$ individuals, approximated by lower rank — from [[eckart-1936-lowrank/main]]
- [[wilcoxon-as-transformed-normal]] — ranks → quantiles, then normal-theory mean difference — from [[gelman-2013-bda3/ch04-asymptotics]]
- [[tischgesellschaften-germany]] — equality among unequal ranks, partly in secret — from [[habermas-1989-publicsphere/ch02-social]]
- [[bales-who-to-whom]] — speaking rank, popularity and direction of flow — from [[katz-1955-personalinfluence/ch06-interpersonal]]
- [[zipf-law]] — word frequency vs rank is a Pareto/power law with $a=1$ — from [[murphy-2023-pml2/ch02-probability-p1]]
- [[gaussian-mean-2d-vi]] — full vs diagonal vs low-rank Gaussian q for a 2D Gaussian mean; diagonal is over-confident — from [[murphy-2023-pml2/ch10-variational-p1]]
- [[planar-flow]] — $M=1$ low-rank residual flow; $\det=1+w^\top v\sigma'(\cdot)$ — from [[murphy-2023-pml2/ch23-normalizing]]
- [[prisoners-dilemma]] — a unique equilibrium (Fink, Fink) that both players rank below (Quiet, Quiet); may model joint project, duopoly, arms race, common grazing — from [[osborne-2004-introduction/ch02-nash-p1]]
- [[zipf-ulysses-newspaper]] — rank-frequency curves; about 170 words make half of the Joyce passage — from [[pierce-1980-introduction/ch12-information]]
- [[zipf-rank-frequency-plot]] — English, Hebrew and Russian word frequencies, tails with slope close to −1 on log–log axes — from [[polyanskiy-2025-information/ch12-variable]]
- [[zipf-word-entropy]] — 11.82 bits/word = 2.62 bits/letter from word ranks up to 8,727 — from [[shannon-1951-prediction/main]]
- [[risk-ranking-table-1]] — four groups rank 30 hazards differently — from [[slovic-1987-perception/main]]
- [[rank-one-ab-vs-ba]] — A = (1,1,1)ᵀ, B = [1 2 −3]: AB rank 1, BA = 0 — from [[strang-2023-introduction/app1-ranks]]
- [[matrix-a5]] — column 4 = column 1 − column 2 + column 3; rank 3 — from [[strang-2023-introduction/ch01-vectors]]
- [[rank-2-3x4-example-2]] — R₀ with zero row, A = CR, F = $\begin{bmatrix}7&8\\0&9\end{bmatrix}$ — from [[strang-2023-introduction/ch03-four-p1]]
- [[rank-two-cr-example]] — A = CR with 3 by 3 rank-2 matrix — from [[strang-2023-introduction/ch03-four-p3]]
- [[all-ones-rank-one-shift]] — 5I − ones(4): eigenvalues 1, 5, 5, 5, det 125 — from [[strang-2023-introduction/ch06-eigenvalues-p2]]
- [[hilbert-matrix]] — $H(i,j)=(i+j-1)^{-1}$; steep dropoff, low effective rank — from [[strang-2023-introduction/ch07-singular]]
- [[flag-matrices]] — stripe flags rank 1; Greece rank 3, Tonga rank 4 — from [[strang-2023-introduction/ch07-singular]]

## Candidate bridges

- [same-math] Fundamental theorem of linear maps ↔ linear-algebra spine: rank–nullity $\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T$ — same statement, stated without matrices. — from [[axler-2024-ladr/ch03-linear-p1]] (linear-algebra → linear-algebra)
- [same-math] 3.78 dim range T = column rank ↔ linear-algebra spine: rank as dimension of column space — from [[axler-2024-ladr/ch03-linear-p2]] (linear-algebra → linear-algebra)
- [same-math] 7.92 ↔ Eckart–Young theorem (spectral-norm version) — same statement: truncated SVD is the best rank-$k$ approximation, error $s_{k+1}$. — from [[axler-2024-ladr/ch07-operators-p3]] (linear-algebra → unspecified)
- [same-math] $v\otimes w\leftrightarrow(v_jw_k)$ ↔ rank-one matrix / outer product $vw^{\rm t}$. — from [[axler-2024-ladr/ch09-multilinear-p2]] (linear-algebra → unspecified)
- [structural-analogy] gain/loss ratio rule ↔ control-theory: an index policy that ranks actions by a single number computed per option — the text proves it for this two-mine process and only states it for the extensions (Theorems 3–4). — from [[bellman-1957-dp/ch02-ii]] (control-theory → control-theory)
- [structural-analogy] Early stop of Gram–Schmidt ↔ rank: it finds the first vector that adds no new direction (canon link; rank is not stated in this unit). — from [[boyd-2018-vmls/ch05-linear]] (linear-algebra → other)
- [same-math] Least norm solution $C^T(CC^T)^{-1}d$ ↔ linear-algebra: pseudo-inverse of a wide full-row-rank matrix — the chapter states they are the same matrix. — from [[boyd-2018-vmls/ch16-constrained]] (linear-algebra → linear-algebra)
- [metaphor] Carey's "positional goods" for jobs ↔ economics: scarce goods valued by rank — Carey borrows Hirsch's term. — from [[carey-1989-cultural/ch04-overcoming]] (communication-theory → economics-finance)
- [metaphor] Michels's iron law of oligarchy ↔ principal–agent problem: leaders pursue goals distinct from those of the rank and file — from [[clark-2017-principles/ch14-social-p2]] (political-science → other)
- [structural-analogy] pivot columns in REF ↔ linear-algebra: rank — the unit uses pivots to test independence; the rank link is only forward-referenced here (p. 35). — from [[deisenroth-2020-mml/ch02-linear-p1]] (linear-algebra → linear-algebra)
- [same-math] Rank–nullity ↔ the earlier solution-set count: $Ax=0$ has an $(n-\mathrm{rk}A)$-dimensional solution space — the same statement for $\Phi:x\mapsto Ax$. — from [[deisenroth-2020-mml/ch02-linear-p2]] (linear-algebra → other)
- [structural-analogy] Rank-$k$ SVD of a user×item rating matrix ↔ social science: a few latent "types" of respondents and items summarising survey or rating data. — from [[deisenroth-2020-mml/ch04-matrix-p2]] (linear-algebra → other)
- [same-math] Truncated SVD as best rank-$k$ approximation ↔ data compression and noise filtering: the same factor-and-truncate procedure. — from [[deisenroth-2020-mml/ch04-matrix-p2]] (linear-algebra → other)
- [same-math] Eckart–Young best rank-$r$ approximation ↔ principal component analysis: truncated canonic form of the data matrix, keep largest components — same decomposition and truncation. — from [[eckart-1936-lowrank/main]] (linear-algebra → other)
- [same-math] LSA's truncated SVD ↔ text as data: low-rank factorization of the document-feature matrix — the chapter says LSA learns embeddings with a truncated SVD, a low-rank matrix factorization. — from [[grimmer-2022-textasdata/ch08-distributed]] (political-science → other)
- [structural-analogy] $\pi(p)$ overweighting small $p$ and compressing mid-range $p$ ↔ decision-game-theory: probability weighting in cumulative/rank-dependent models — a nonlinear map from stated to effective probability. — from [[kahneman-1979-prospect/main]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Persistence of rank across years ↔ test–retest reliability in measurement: both ask whether differences between units repeat. — from [[kahneman-2011-thinking/ch20-illusion]] (decision-game-theory → other)
- [same-math] Optimal decoding as solving t = Gs over GF(2), and "random K×K matrix has full rank" (Ex. 50.11) ↔ linear algebra over GF(2) — both are solving linear equations mod 2. — from [[mackay-2003-information/ch50-digital]] (information-theory → unspecified)
- [structural-analogy] Effective complexity (low at order and randomness) ↔ statistical complexity: both rank "in between" highest, but they are defined differently. — from [[mitchell-2009-guidedtour/ch07-defining]] (complex-systems → other)
- [structural-analogy] Conformal rank argument ↔ permutation tests (uniform rank of an exchangeable point) — from [[murphy-2023-pml2/ch14-predictive]] (bayesian → unspecified)
- [metaphor] RLHF ranking model and CLIP critic ↔ likelihood × weighting in Bayes' theorem: both use an external score to steer or rank model output. — from [[murphy-2023-pml2/ch22-autoregressive]] (bayesian → bayesian)
- [structural-analogy] Ordinal payoffs (any increasing transformation) ↔ order-invariant statistics, e.g. rank-based methods — only order matters. — from [[osborne-2004-introduction/ch01-introduction]] (decision-game-theory → unspecified)
- [structural-analogy] reduced text of guess ranks, mostly 1's ↔ source coding: a good model turns data into a skewed symbol stream that can be compressed. — from [[shannon-1951-prediction/main]] (information-theory → other)
- [structural-analogy] Courant-Fischer max-min over subspaces ↔ Eckart–Young / best low-rank approximation: both rank directions by singular or eigen values. — from [[spielman-2025-sagt/ch02-eigenvalues]] (linear-algebra → other)
- [same-math] Interlacing under $+pJ$ ↔ rank-one updates of a symmetric matrix: same eigenvalue-ordering statement (Exercise 1). — from [[spielman-2025-sagt/ch08-eigenvalues]] (linear-algebra → linear-algebra)
- [same-math] Counting dimension of $\{y:My=0\}$ ≥ unknowns − constraints ↔ rank–nullity (over $\mathbb F_2$ here). — from [[spielman-2025-sagt/ch29-expander]] (linear-algebra → unspecified)
- [same-math] Sherman–Morrison rank-one update ↔ linear-algebra: the inverse of a matrix after a rank-one change. — from [[spielman-2025-sagt/ch33-linear]] (linear-algebra → linear-algebra)
- [structural-analogy] Interlacing of $p$ and $p-tq$ ↔ linear-algebra: Cauchy interlacing for a principal submatrix, and rank-one updates via Courant–Fischer — same alternating-root pattern. — from [[spielman-2025-sagt/ch41-expected]] (linear-algebra → linear-algebra)
- [same-math] Lemma 44.5.1 rank-one update $\chi_x(A+tvv^T)=\chi_x(A)-tq$ ↔ linear algebra: determinant linearity in one entry plus rotation invariance. — from [[spielman-2025-sagt/ch44-bipartite]] (linear-algebra → linear-algebra)
- [structural-analogy] Interlacing of roots under rank-one perturbation ↔ Cauchy interlacing / Courant–Fischer (cited in the proof, p. 352). — from [[spielman-2025-sagt/ch44-bipartite]] (linear-algebra → unspecified)
- [structural-analogy] CP tensor decomposition ↔ data science: low-rank matrix factorization, extended to three indices without orthogonality. — from [[strang-2023-introduction/app1-ranks]] (linear-algebra → other)
- [structural-analogy] AB = Σ aₖbₖ* (sum of rank-one matrices) ↔ low-rank approximation/SVD: a matrix as a sum of rank-one pieces. — from [[strang-2023-introduction/ch01-vectors]] (linear-algebra → other)
- [structural-analogy] A = LU as a sum of rank-one matrices ℓ_k u_k ↔ low-rank structure: building a matrix from outer products (p. 60) — from [[strang-2023-introduction/ch02-solving-p1]] (linear-algebra → other)
- [structural-analogy] A = CR (independent columns plus mixing matrix) ↔ data science: low-rank factorization of a matrix. — from [[strang-2023-introduction/ch03-four-p3]] (linear-algebra → other)
- [same-math] V = Σ p_ij UUᵀ is a sum of rank-one positive semidefinite matrices ↔ linear algebra: PSD matrices as sums of outer products (p. 396) — from [[strang-2023-introduction/ch10-learning]] (linear-algebra → linear-algebra)
