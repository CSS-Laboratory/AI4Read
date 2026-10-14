---
id: spielman-2025-sagt/ch10-random
work: spielman-2025-sagt
unit: "Chapter 10 — Random Walks on Graphs"
pages: 92-101
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# Random Walks on Graphs

## L0 — One line
The lazy random walk on a connected graph converges to the degree-proportional distribution π, and the second eigenvalue ω₂ of the walk matrix (equivalently ν₂ of the normalized Laplacian) controls how fast.

## L1 — The gist (≤ 120 words)
How fast does a random walk on a graph forget where it started? The walk matrix is not symmetric, but it is similar to the symmetric normalized adjacency matrix. This gives real eigenvalues and an orthonormal eigenbasis after rescaling. Expanding the walk in that basis shows that the lazy walk converges to π(a) = d(a)/Σd. Starting at a, the pointwise error at b after t steps is at most √(d(b)/d(a))·ω₂ᵗ. In terms of the normalized Laplacian, an upper bound on the time to mix is about (log n)/ν₂ steps for near-constant degrees. Examples (path, tree, dumbbell, bolas) show how bottlenecks make ν₂ small and mixing slow.

**Prerequisites:** eigenvalues/eigenvectors of symmetric matrices; similarity transforms; Laplacian L = D − M; Rayleigh quotient and Courant–Fischer; Perron–Frobenius; Cauchy–Schwarz.

## L2 — Key ideas (5–10 bullets)
- The walk matrix is W = MD⁻¹ and evolves distributions by p_{t+1} = Wp_t. The lazy version W̃ = I/2 + W/2 is used partly because it avoids non-convergence on bipartite graphs (pp. 93–94).
- W is similar to the symmetric A = D^{-1/2}MD^{-1/2}, so W has n real eigenvalues. Its eigenvectors are D^{1/2}ψᵢ, which are generally not orthogonal (pp. 93–94).
- The stable distribution is π = d/(1ᵀd). Expanding D^{-1/2}p₀ in A's eigenbasis shows p_t → π (pp. 94–95).
- Pointwise error: |p_t(b) − π(b)| ≤ √(d(b)/d(a)) ω₂ᵗ when starting at a. A small ω₂ means fast convergence (pp. 95–96).
- With ν₂ = 2 − 2ω₂, a sufficient condition for the walk to have "mixed" (|p_t(b) − π(b)| ≤ π(b)/2) is t ≥ 2 ln(2d(V)/√(d(b)d(a)))/ν₂, where d(V) = Σ_a d(a) (my gloss). This is about 2 ln n/ν₂ for near-constant degrees (pp. 97–98).
- Lemma 10.5.1 sandwiches νᵢ between λᵢ/d_max and λᵢ/d_min, so Laplacian bounds transfer to ν₂ (p. 98).
- Examples: path ~n² steps; binary tree ~n; dumbbell ~n²; bolas ~n³ (pp. 99–100).
- Lazy walks are discrete diffusion. The fine-step limit is exp(t(W − I)). Repeatedly applying W̃ is the power method (p. 101).

## L3 — Walkthrough

### 10.1 Random walks (pp. 92–93)
G = (V,E,w) is a weighted undirected graph. The walk moves to a neighbour with probability proportional to edge weight. p_t ∈ ℝ^V is the distribution at time t, a probability vector (entries ≥ 0, sum 1). Usually p₀ = δ_a, "the walk starts at a" (p. 92). With weighted degree d(b) = Σ_a w(a,b):
$$p_{t+1}(a)=\sum_{b:(a,b)\in E}\frac{w(a,b)}{d(b)}\,p_t(b)\tag{10.1}$$
In matrix form, W = MD⁻¹ (M is the weighted adjacency matrix, not defined on these pages; D is the diagonal degree matrix), and p_{t+1} = Wp_t = W^{t+1}p₀. Check on a unit vector: MD⁻¹δ_b = M(δ_b/d(b)) = Σ_{a∼b}(w_{a,b}/d(b))δ_a (p. 93).

Lazy walk: stay put with probability 1/2.
$$p_{t+1}(a)=\tfrac12 p_t(a)+\tfrac12\sum_{b:(a,b)\in E}\frac{w(a,b)}{d(b)}p_t(b)\tag{10.2}$$
So p_{t+1} = W̃p_t, with W̃ = ½I + ½W = ½I + ½MD⁻¹. The author usually works with lazy walks (p. 93).

### 10.2 Spectra of walk matrices (pp. 93–94)
Define the normalized adjacency matrix A = D^{-1/2}WD^{1/2} = D^{-1/2}MD^{-1/2}. It is symmetric (p. 93).

**Claim 10.2.1.** ψ is an eigenvector of A with eigenvalue ω iff D^{1/2}ψ is an eigenvector of W with eigenvalue ω.
*Proof.* D^{1/2}A = WD^{1/2}, so ωψ = Aψ iff ω(D^{1/2}ψ) = D^{1/2}Aψ = W(D^{1/2}ψ) (p. 93).

W̃ has the same eigenvectors as W (p. 94). The degree vector d satisfies MD⁻¹d = M1 = d, so d is a Perron vector of W with eigenvalue 1. Hence ψ₁ = d^{1/2}/‖d^{1/2}‖ is the unit Perron vector of A with eigenvalue 1, where d^{1/2}(a) = d(a)^{1/2}. By Perron–Frobenius (Thm 4.5.1) all eigenvalues of A lie in [−1,1]. As in Prop. 4.5.3, G is bipartite iff −1 is an eigenvalue of A (p. 94). Since W̃ = W/2 + I/2, its eigenvalues lie in [0,1]. Write the eigenvalues of W̃ (and of I/2 + A/2) as 1 = ω₁ ≥ ω₂ ≥ … ≥ ωₙ ≥ 0 (p. 94).

*Intuition note:* Rescaling by D^{1/2} turns a non-symmetric walk matrix into a symmetric one. So the walk gets real eigenvalues and a clean orthonormal basis, but the eigenvectors of W itself are generally not orthogonal.

### 10.3 The stable distribution (pp. 94–95)
On a connected graph, the lazy walk converges to one distribution from any start. Without laziness a bipartite graph alternates sides, so the limit depends on the parity of t (p. 94). Footnote: any nonzero probability of staying put at any vertex of a connected graph already makes the chain aperiodic and convergent (p. 94). The stable distribution is π = d/(1ᵀd), a right-eigenvector of eigenvalue 1 (pp. 94–95).

Let ψ₁,…,ψₙ be orthonormal eigenvectors of A, ordered to match ω₁,…,ωₙ of W̃. Caution: the eigenvalues of A are then 2ωᵢ − 1. Write D^{-1/2}p₀ = Σᵢcᵢψᵢ, cᵢ = ψᵢᵀD^{-1/2}p₀. Then
$$c_1=\frac{(d^{1/2})^T}{\|d^{1/2}\|}D^{-1/2}p_0=\frac{\mathbf 1^Tp_0}{\|d^{1/2}\|}=\frac1{\|d^{1/2}\|}$$
since p₀ is a probability vector (p. 95). One of the author's reasons for not expanding in eigenvectors of W̃ is that they are not orthogonal, so the coefficients have no nice expression (p. 95). Then:
$$\begin{aligned}p_t=\widetilde W^tp_0&=D^{1/2}\big(D^{-1/2}\widetilde WD^{1/2}\big)^tD^{-1/2}p_0\\&=D^{1/2}(I/2+A/2)^t\sum_ic_i\psi_i=D^{1/2}\sum_i\omega_i^tc_i\psi_i\\&=D^{1/2}c_1\psi_1+D^{1/2}\sum_{i\ge2}\omega_i^tc_i\psi_i=\pi+D^{1/2}\sum_{i\ge2}\omega_i^tc_i\psi_i\end{aligned}$$
because $D^{1/2}c_1\psi_1=d/\|d^{1/2}\|^2=d/\sum_ad(a)=\pi$. As 0 ≤ ωᵢ < 1 for i ≥ 2, the last term goes to zero (p. 95).

*Intuition note:* Each eigen-direction except the top one shrinks by a factor ωᵢ per step. After many steps only the top one, π, is left. The author calls this a main use of spectral theory: understanding repeated application of an operator (p. 95).

### 10.4 The rate of convergence (pp. 95–96)
**Theorem 10.4.1.** For all a, b, t, if p₀ = δ_a, then
$$|p_t(b)-\pi(b)|\le\sqrt{\frac{d(b)}{d(a)}}\;\omega_2^t.$$
*Proof (key steps).* p_t(b) = δ_bᵀp_t = π(b) + δ_bᵀD^{1/2}Σ_{i≥2}ωᵢᵗcᵢψᵢ. Use cᵢ = ψᵢᵀD^{-1/2}δ_a = ψᵢᵀδ_a/√d(a) and δ_bᵀD^{1/2} = √d(b) δ_bᵀ. The error term becomes √(d(b)/d(a)) δ_bᵀΣ_{i≥2}ωᵢᵗψᵢψᵢᵀδ_a. Then
$$\Big|\sum_{i\ge2}\omega_i^t(\delta_b^T\psi_i)(\psi_i^T\delta_a)\Big|\le\omega_2^t\sum_{i\ge1}|\delta_b^T\psi_i||\psi_i^T\delta_a|\le\omega_2^t\sqrt{\sum_{i\ge1}(\delta_b^T\psi_i)^2}\sqrt{\sum_{i\ge1}(\delta_a^T\psi_i)^2}=\omega_2^t\|\delta_b\|\|\delta_a\|=\omega_2^t .$$
The steps are: triangle inequality, ωᵢ ≤ ω₂ for i ≥ 2, adding the i = 1 term, Cauchy–Schwarz, orthonormal basis (p. 96).

*Intuition note:* The error bound shrinks geometrically at rate ω₂ per step, so ω₂ close to 1 (ν₂ small) gives only a slow guarantee. In the examples, graphs with a bottleneck such as the dumbbell have small ν₂ and mix slowly (p. 99).

### 10.5 Relation to the normalized Laplacian (pp. 97–98)
N = D^{-1/2}LD^{-1/2} = I − D^{-1/2}MD^{-1/2} = I − A, with eigenvalues 0 ≤ ν₁ ≤ … ≤ νₙ and the same eigenvectors as A. Relations: νᵢ = 2 − 2ωᵢ, ωᵢ = 1 − νᵢ/2, W̃ = I − ½D^{1/2}ND^{-1/2} (p. 97). The eigenvalue-0 eigenvector is d^{1/2}, since D^{-1/2}LD^{-1/2}d^{1/2} = D^{-1/2}L1 = 0. The ν₂ eigenvector is the arg min of xᵀNx/xᵀx over x ⊥ d^{1/2}. With y = D^{-1/2}x (so xᵀd^{1/2} = yᵀd):
$$\nu_2=\min_{y\perp d}\frac{y^TLy}{y^TDy}$$
N is positive semidefinite with the same rank as L. Its eigenvalues have mean 1, a degree-independent scale. The text says one can prove νₙ ≤ 2, with equality iff the graph is bipartite (p. 97). The theorem becomes |p_t(b) − π(b)| ≤ √(d(b)/d(a))(1 − ν₂/2)ᵗ (p. 97).

*Mixing time.* "Mixed" means |p_t(b) − π(b)| ≤ π(b)/2 for all b. Here π(b) = d(b)/d(V), where d(V) = Σ_a d(a) (my gloss). Using 1 − x ≤ exp(−x), the bound requires
$$\sqrt{\tfrac{d(b)}{d(a)}}(1-\nu_2/2)^t\le \tfrac{d(b)}{2d(V)}\iff(1-\nu_2/2)^t\le\tfrac{\sqrt{d(b)d(a)}}{2d(V)}.$$
This is implied by exp(−tν₂/2) ≤ √(d(b)d(a))/2d(V), i.e.
$$t\ge 2\ln\!\big(2d(V)/\sqrt{d(b)d(a)}\big)/\nu_2 .$$
For roughly constant degrees this is about 2 ln n/ν₂. For some graphs the ln n does not appear. Multiplying all edge weights by a constant does not change any of these expressions (p. 98).

**Lemma 10.5.1.** With L's eigenvalues λ₁ ≤ … ≤ λₙ, for all i: λᵢ/d_min ≥ νᵢ ≥ λᵢ/d_max.
*Proof.* By Courant–Fischer, νᵢ = min_{dim S=i} max_{x∈S} xᵀNx/xᵀx. The change y = D^{-1/2}x is non-singular, so this equals min_{dim T=i} max_{y∈T} yᵀLy/yᵀDy. Since yᵀDy ≤ d_max yᵀy, this is ≥ (1/d_max)·min max yᵀLy/yᵀy = λᵢ/d_max. The other bound is "similar" (p. 98).

*Intuition note:* Each νᵢ lies between λᵢ/d_max and λᵢ/d_min. So known bounds on λ₂ give bounds on ν₂ up to degree factors.

### 10.6 Examples (pp. 98–100)
- **Path** (n vertices): degrees 1 or 2, so ν₂ ≈ λ₂ ≈ c/n². Starting mid-path and ignoring the steps on which the walk stays put, the position after t steps is a sum of t values ±1, with standard deviation √t. √t must be comparable to n/4, so t ≥ O(n²) (p. 99).
- **Complete binary tree:** ν₂ is within a constant of λ₂, approximately c/n. The walk is twice as likely to step towards a leaf as towards the root. From a leaf it needs about n steps to hit the root, and then mixes rapidly (p. 99).
- **Dumbbell Dₙ** (two complete graphs on n vertices, one bridge edge; degrees n−1 or n). Crossing has chance about (1/n)(1/n) = 1/n² per step, so about n² steps are needed (p. 99). Isoperimetric ratio θ ~ 1/n. A test vector (1 on one clique, −1 on the other) gives λ₂ ≤ 4/n, so ν₂ ≤ 4/(d_min n) (p. 99).
 **Lemma 10.6.1.** If unweighted G has diameter ≤ r, then λ₂(G) ≥ 2/(r(n−1)).
 *Proof.* For each pair a,b take a path P_{a,b} of length ≤ r. Then G_{a,b} ≼ r·P_{a,b} ≼ r·G. Summing, K_n = Σ_{a<b}G_{a,b} ≼ C(n,2)·r·G. Hence n ≤ r·C(n,2)·λ₂(G) (p. 100). (Added step: λ₂(Kₙ) = n; solving gives the lemma.) For Dₙ (diameter 3), the text concludes λ₂ ≥ 2/(3(n−1)) and ν₂(Dₙ) ≥ 2/(3(n−1)²) (p. 100).
- **Bolas Bₙ** (two n-cliques joined by a path of length n). Its ν₂ is almost as small as possible, so walks mix almost as slowly as possible. From the first path vertex, the chance of reaching the far end before returning is only about 1/n, so about n³ steps are needed. Test vector: n/2 on one clique, −n/2 on the other, rising by 1 along the path. It is orthogonal to d by symmetry. The numerator is n; the denominator is a constant times n⁴. So ν₂ ≤ c/n³. Lemmas 10.5.1 and 10.6.1 give ν₂ ≥ c/n³ for every connected unweighted graph (p. 100).

### 10.7 Diffusion (p. 101)
Half the substance stays at each vertex and half spreads to neighbours. Then the substance evolves by (10.2), so lazy-walk probability mass obeys this diffusion equation. With finer steps (stay with probability 1 − ε, each step taking time ε):
$$((1-\epsilon)I+\epsilon W)^{t/\epsilon}\to\exp(t(W-I)).$$
The author calls such continuous walks in many ways more natural.

### 10.8 Final notes (p. 101)
Repeatedly multiplying by W̃ is the power method, a common way to approximate eigenvectors. The proof of 10.4.1 has two slacks. (1) Bounding all ωᵢ by ω₂ ignores "eigenvalue decay" and costs about a log n factor. In the examples the time to approximate convergence is typically of order 1/ν₂, not (log n)/ν₂; the author attributes this to eigenvalue decay. (2) The absolute value of a sum was bounded by the sum of absolute values.

## Toy example (ours)
Path a–b–c, unweighted, lazy walk. d = (1,2,1), Σd = 4, so π = (1/4, 1/2, 1/4).
Columns of W̃ = ½I + ½MD⁻¹ are a: (1/2,1/2,0); b: (1/4,1/2,1/4); c: (0,1/2,1/2).
Start p₀ = δ_a = (1,0,0).
- p₁ = column a = (1/2, 1/2, 0).
- p₂ = ½·col a + ½·col b = (1/4+1/8, 1/4+1/4, 0+1/8) = (3/8, 1/2, 1/8).

A has entries A_ab = A_bc = 1/√2, so its eigenvalues are 1, 0, −1. Then ωᵢ = (1+eig)/2 = 1, 1/2, 0, so ω₂ = 1/2.
Errors: p₁−π = (1/4, 0, −1/4); p₂−π = (1/8, 0, −1/8). From t = 1 to t = 2 the error halves, matching ω₂ = 1/2.
Theorem 10.4.1 check at t = 2, a = start, b = c: |1/8 − 1/4| = 1/8 ≤ √(1/1)·(1/2)² = 1/4 ✓.

## Concepts
- [[lazy-random-walk]] (new) — walk that stays put with probability 1/2; matrix W̃ = I/2 + W/2 (p. 93)
- [[walk-matrix]] (new) — W = MD⁻¹; maps distribution p_t to p_{t+1}; not symmetric (p. 93)
- [[normalized-adjacency-matrix]] (new) — A = D^{-1/2}MD^{-1/2}, symmetric, similar to W (p. 93)
- [[normalized-laplacian]] (new) — N = I − A; νᵢ = 2 − 2ωᵢ (p. 97)
- [[stable-distribution]] (new) — π = d/(1ᵀd), the limit of the lazy walk on a connected graph (p. 94)
- [[mixing-time]] (new) — here: t with |p_t(b) − π(b)| ≤ π(b)/2 for all b; upper bound ≈ 2 ln n/ν₂ for near-constant degrees (pp. 97–98)
- [[adjacency-matrix]] — M, the (weighted) adjacency matrix (p. 93)
- [[perron-frobenius-theorem]] — gives eigenvalues of A in [−1,1] (p. 94)
- [[graph-laplacian]] — L; ν₂ and λ₂ related by Lemma 10.5.1 (p. 98)
- [[rayleigh-quotient]] — ν₂ = min_{y⊥d} yᵀLy/yᵀDy (p. 97)
- [[power-iteration]] — repeated multiplication by W̃ (p. 101)
- [[diffusion-matrix-exponential]] (new) — continuous-time limit exp(t(W − I)) (p. 101)

## Canonical instances
- [[path-graph]] — mixing ~n² steps (p. 99)
- [[complete-binary-tree]] — mixing ~n steps (p. 99)
- [[dumbbell-graph]] — mixing ~n² steps, one bridge (p. 99)
- [[bolas-graph]] — mixing ~n³ steps, nearly the slowest possible (p. 100)

## Bridges (candidates)
- [same-math] Convergence of lazy walk ↔ numerical linear algebra: power method — same repeated multiplication by W̃, as the text states (p. 101)
- [structural-analogy] ν₂ via Rayleigh quotient ↔ Fiedler value / algebraic connectivity — a similar minimum over y ⊥ d, but with D-weighting, so not identical to λ₂
- [structural-analogy] Lazy walk as diffusion ↔ heat flow on a graph — update has the form of (10.2); exp(t(W−I)) is the continuous limit
- [structural-analogy] Bottlenecks (dumbbell, bolas) ↔ community structure — a small cut means small ν₂ and slow mixing

## Questions this raises
- When ω₂ < 1 is the only slow rate, how large is the gap between mixing time and 1/ν₂ in graphs without eigenvalue decay?
- Can the 1/n² crossing chance for the dumbbell be turned into a rigorous proof of the lower bound on mixing time?
- How does the pointwise bound compare with other measures of convergence (the text says there are many)?
- Does non-laziness (a small stay-put probability) change the constants in the bound?

## Reading notes
- Printed = pdf − 24. No exercises in this unit.
- Lemma 10.5.1 statement prints "ν₁ ≤ ν₂ ≤ … ≤ ν₂"; the last should be νₙ. Its proof writes ν₂ at the start of the displayed chain where νᵢ is meant (p. 98).
- p. 97: "The eigenvectors of ν₂ is given by" is a typo for "eigenvector".
- p. 99: the text writes ν₂(Dₙ) ≤ 4/(d_min n) "≈ 8/n²". With d_min = n−1 this is about 4/n². The printed 8/n² is still a valid upper bound, but the "≈" looks inconsistent.
- p. 100, dumbbell lower bound: Lemma 10.6.1 is applied with n vertices, but Dₙ has 2n vertices. The text also cites "degree at least n−1", whereas the lemma's lower bound uses d_max. This affects constants only.
- The notation ≼, G_{a,b} and d(V) is not defined on these pages. I glossed ≼ as the matrix order used to compare Laplacians, G_{a,b} as the graph with a single edge on a,b, and d(V) as Σ_a d(a).
- The text gives the bolas test-vector denominator and the tree hitting time only in outline ("one can show"); I did not fill the gaps.
