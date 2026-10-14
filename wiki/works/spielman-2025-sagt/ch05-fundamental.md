---
id: spielman-2025-sagt/ch05-fundamental
work: spielman-2025-sagt
unit: "Chapter 5 — Fundamental Graphs"
pages: 44-52
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Fundamental Graphs

## L0 — One line
The Laplacian eigenvalues and eigenvectors of complete graphs, stars, hypercubes, rings and paths can be computed exactly, or bounded, using orthogonality, trace, graph products, test vectors and quotients.

## L1 — The gist (≤ 120 words)
Which Laplacian eigenvalues do the basic graphs have, and how do we find them? Complete graphs have eigenvalues 0 and n. Stars have 0, 1 and n. Products of graphs add eigenvalues, which gives the hypercube and grids. Rings have cosine and sine eigenvectors. Paths come from rings by identifying vertex a with vertex a+n of R_{2n}. For λ₂ (the second-smallest eigenvalue), any guessed vector orthogonal to 1 (a test vector) gives an upper bound. Combined with the isoperimetric bound θ(S) ≥ λ₂(1−s) (θ(S): boundary edges of S divided by |S|; s = |S|/n), these examples show where that bound is sharp (K_n, hypercube) and where it is loose (path).

**Prerequisites:** Laplacian L = D − A and its action (Lx)(a) = Σ(x(a) − x(b)); eigenvectors of symmetric matrices are orthogonal; trace = sum of eigenvalues; Courant–Fischer; cos/sin addition formulas; Kronecker product.

## L2 — Key ideas (5–10 bullets)
- For K_n, L = nI − 11ᵀ, so every vector orthogonal to 1 has eigenvalue n. The bound θ(S) ≥ λ₂(1−s) is then an equality (pp. 44–45).
- In a star, degree-one vertices sharing a neighbour give eigenvectors of eigenvalue 1. The trace fixes the last eigenvalue at n (pp. 45–46).
- For a product G×H, each sum λᵢ + μⱼ is an eigenvalue, with the product vector αᵢ(a)βⱼ(b) as eigenvector (Thm 5.3.2, p. 47).
- The hypercube H_d has eigenvalue 2i with multiplicity C(d,i), and λ₂ = 2. Hence θ ≥ 1, which is tight (pp. 47–48).
- Any v ⊥ 1 upper-bounds λ₂ by its Rayleigh quotient $v^TLv/v^Tv$ (a test vector). This gives λ₂(P_n) ≤ 12/(n(n+1)), and the isoperimetric bound is loose for paths (pp. 48–49).
- The ring R_n has eigenvectors cos(2πka/n) and sin(2πka/n) with eigenvalue 2 − 2cos(2πk/n) (p. 49).
- The path P_n is a quotient of R_{2n} (vertex a is merged with vertex a+n), with eigenvalues 2(1 − cos(πk/n)). This quotient is an equitable partition (pp. 51–52).

## L3 — Walkthrough

**Chapter intro (p. 44).** All graphs here are connected, so 0 has multiplicity 1. The boundary ∂(S) is the set of edges with exactly one endpoint in S. The isoperimetric ratio is $\theta(S)=|\partial(S)|/|S|$. Theorem 20.1.1 (not proved here) gives
$$\theta(S)\ge \lambda_2(1-s). \tag{5.1}$$
(s = |S|/n, defined on p. 45.)

**5.1 Complete graph K_n.**
- *Lemma 5.1.1:* eigenvalue 0 has multiplicity 1 and n has multiplicity n−1 (p. 44).
- Proof: take ψ ≠ 0 with $\sum_a\psi(a)=0$ (5.2). Then $(L\psi)(1)=\sum_{b\ge2}(\psi(1)-\psi(b))=(n-1)\psi(1)-\sum_{b=2}^n\psi(b)=n\psi(1)$ by (5.2). The coordinate was arbitrary, so $L\psi=n\psi$ (p. 45).
- Alternative: $L_{K_n}=nI-\mathbf 1\mathbf 1^T$ (p. 45).
- Isoperimetry: each vertex of S has n−|S| edges leaving S, so $\theta(S)=|S|(n-|S|)/|S|=n-|S|=\lambda_2(1-s)$. Theorem 20.1.1 is sharp for K_n (p. 45).

*Intuition note:* On the space orthogonal to 1, K_n's Laplacian just multiplies by n. Every set of the same size has the same ratio, and (5.1) is met exactly.

**5.2 Star graphs S_n** (edges (1,a), 2 ≤ a ≤ n).
- *Lemma 5.2.1:* if a, b have degree one and the same neighbour, then δ_a − δ_b is an eigenvector of eigenvalue 1. Proof: multiply and check vertex by vertex (p. 45).
- The author states that the C(n−1,2) pairs span only an (n−1)-dimensional space (p. 45); see Reading notes (the proof on p. 46 uses n−2).
- *Lemma 5.2.2:* S_n has eigenvalue 0 (multiplicity 1), 1 (multiplicity n−2) and n (multiplicity 1) (p. 45).
- Proof: the vectors δ_i − δ_{i+1}, 2 ≤ i < n, give n−2 independent eigenvectors of eigenvalue 1. With eigenvalue 0, one eigenvalue remains. tr L = 2n−2, and the n−1 known eigenvalues sum to n−2. So the last one is n (p. 46).
- Its eigenvector is orthogonal to the others, so it is constant on the leaves. Put 1 on each leaf and x at vertex 1. Orthogonality to constants gives (n−1) + x = 0, so x = −(n−1) (p. 46).

**5.3 Products of graphs.**
- *Def 5.3.1:* for weighted G=(V,E,v), H=(W,F,w), G×H has vertex set V×W. Edges are ((a,b),(â,b)) with weight $v_{a,\hat a}$ for (a,â)∈E, and ((a,b),(a,b̂)) with weight $w_{b,\hat b}$ for (b,b̂)∈F (p. 46). The product of paths on m and n vertices is an m-by-n grid (Fig. 5.1).
- *Theorem 5.3.2:* let G, H have eigenpairs (λᵢ, αᵢ), (μⱼ, βⱼ). Then $\gamma_{i,j}(a,b)=\alpha_i(a)\beta_j(b)$ is an eigenvector of L_{G×H} with eigenvalue λᵢ+μⱼ (p. 47).
- Proof, for α, β with eigenvalues λ, μ:
$$(L_{G\times H}\gamma)(a,b)=\sum_{(a,\hat a)\in E}v_{a,\hat a}\bigl(\alpha(a)\beta(b)-\alpha(\hat a)\beta(b)\bigr)+\sum_{(b,\hat b)\in F}w_{b,\hat b}\bigl(\alpha(a)\beta(b)-\alpha(a)\beta(\hat b)\bigr)$$
$$=\sum v_{a,\hat a}\beta(b)(\alpha(a)-\alpha(\hat a))+\sum w_{b,\hat b}\alpha(a)(\beta(b)-\beta(\hat b))=\beta(b)\lambda\alpha(a)+\alpha(a)\mu\beta(b)=(\lambda+\mu)\alpha(a)\beta(b).$$
- Kronecker form: $L_{G\times H}=(L_G\otimes I_W)+(I_V\otimes L_H)$ (p. 47).

*Intuition note:* Moving in the G-direction sees only α. Moving in the H-direction sees only β. The two contributions simply add.

**5.3.1 Hypercube.** H_d has vertex set {0,1}^d, with edges between names differing in one coordinate. It equals H_{d−1}×H₁ (p. 47).
- H₁ has eigenvectors (1,1) and (1,−1) with eigenvalues 0 and 2. If ψ is an eigenvector of H_{d−1} with eigenvalue λ, then (ψ;ψ) and (ψ;−ψ) are eigenvectors of H_d with eigenvalues λ and λ+2 (p. 48).
- So H_d has eigenvalue 2i with multiplicity C(d,i), 0 ≤ i ≤ d. The eigenvectors are $\psi_y(x)=(-1)^{y^Tx}$, y ∈ {0,1}^d (p. 48).
- *Corollary 5.3.3:* with λ₂(H_d)=2 and (5.1), θ_{H_d} ≥ 1. For sets of at most half the vertices, the boundary has at least as many edges as the set has vertices (p. 48). (added step) For s ≤ 1/2, λ₂(1−s) = 2(1−s) ≥ 1.
- It is tight: take the face of vertices whose labels begin with 0 (p. 48).

**5.4 Bounds on λ₂ by test vectors.**
- Courant–Fischer: every v ⊥ 1 gives $\lambda_2\le v^TLv/v^Tv$. Such a v is called a test vector (p. 48).
- For P_n, take $x(a)=(n+1)-2a$, which is ⊥ 1 (p. 49):
$$\lambda_2(P_n)\le\frac{\sum_{1\le a<n}(x(a)-x(a+1))^2}{\sum_a x(a)^2}=\frac{\sum_{1\le a<n}2^2}{\sum_a(n+1-2a)^2}=\frac{4(n-1)}{(n+1)n(n-1)/3}=\frac{12}{n(n+1)}.\tag{5.3}$$
- The author says this is of the right order of magnitude ("we will soon see", p. 49). Then (5.1) is very loose for the path. The set S={1,…,n/2} has θ(S)=2/n, but (5.1) only gives c/n². Cheeger's inequality (Ch. 21) will show the error cannot be worse than quadratic (p. 49).
- Lower bounds need the max-min form $\lambda_2\ge\max_{S:\dim S=n-1}\min_{v\in S}v^TLv/v^Tv$. It is hard to use because S has large dimension (p. 49).

*Intuition note:* Any guess orthogonal to 1 certifies "λ₂ is at most this". Proving "λ₂ is at least this" needs another technique.

**5.5 Ring graph R_n** (vertices 0..n−1, edges (a,a+1) mod n).
- *Theorem 5.5.1:* $x_k(a)=\cos(2\pi ka/n)$ for 0 ≤ k ≤ n/2, and $y_k(a)=\sin(2\pi ka/n)$ for 1 ≤ k < n/2. Both have eigenvalue $2-2\cos(2\pi k/n)$ (p. 49). x₀ is the all-ones vector. For even n, x_{n/2} alternates ±1 (p. 50).
- Geometric proof for k=1: put vertex a at (cos(2πa/n), sin(2πa/n)). The average of a vertex's neighbours points in the same direction as the vertex (p. 50).
- Computation, using the addition formulas:
$$(L x_k)(a)=2x_k(a)-x_k(a+1)-x_k(a-1)=2\cos\tfrac{2\pi ka}{n}-2\cos\tfrac{2\pi ka}{n}\cos\tfrac{2\pi k}{n}=\bigl(2-2\cos\tfrac{2\pi k}{n}\bigr)x_k(a).$$
- y_k is similar. Rotations stay in the span: $\cos(2\pi ka/n+\theta)=(\cos\theta)x_k-(\sin\theta)y_k$ (p. 51).

**5.6 Path graph P_n.** Number R_{2n} as in Fig. 5.3, so that vertex a lies above vertex n+a (p. 51).
- *Theorem 5.6.1:* P_n has eigenvalues $2(1-\cos(\pi k/n))$ with eigenvectors $v_k(a)=\cos(\pi ka/n-\pi k/2n)$, 0 ≤ k < n (p. 51).
- Quotient: identify a and a+n. The author says to check that $(I_n\ I_n)L_{R_{2n}}\binom{I_n}{I_n}=2L_{P_n}$ (p. 51).
- If $L_{R_{2n}}\psi=\lambda\psi$ and ψ(a)=ψ(a+n), set φ(a)=ψ(a) for a ≤ n. Then $\psi=\binom{I}{I}\phi$ and $(I\ I)L\psi=2\lambda\phi$, so φ is an eigenvector of P_n with eigenvalue λ (p. 52).
- Such ψ come from rotating x_k, y_k by θ = −πk/2n, for 1 ≤ k < n: ψ = (cosθ)x_k − (sinθ)y_k. Under the new numbering, ψ(a) = cos(2πka/(2n) − πk/2n) for a ≤ n, and cos(2πk(2n+1−a)/(2n) − πk/2n) for n < a ≤ 2n. The author checks ψ(a+n)=ψ(a) with cos(−x)=cos x (p. 52).
- Eigenvalue: $2-2\cos(2\pi k/2n)=2(1-\cos(\pi k/n))$ for 1 ≤ k < n. These are n−1 distinct eigenvalues, and 0 comes from the constant vector (p. 52).
- This quotient is an *equitable partition* (Godsil's book is cited) (p. 52).

## Toy example (ours)
Take P₂ × P₂ = H₂, a 4-cycle. P₂ has eigenpairs (0, (1,1)) and (2, (1,−1)). By Thm 5.3.2 the eigenvalues are 0+0, 0+2, 2+0, 2+2 = 0, 2, 2, 4. This matches 2i with multiplicity C(2,i): 1, 2, 1.

Check one eigenvector. Order the vertices (0,0), (0,1), (1,0), (1,1). Then γ = (1,−1)⊗(1,−1) = (1,−1,−1,1). Vertex (0,0) has neighbours (0,1) and (1,0), so (Lγ)(0,0) = 2·1 − (−1) − (−1) = 4 = 4·γ(0,0). ✓.

## Concepts
- [[graph Laplacian]] — the matrix whose action is (Lψ)(a) = Σ_{b∼a}(ψ(a) − ψ(b)) (formula (3.4), used on p. 45 and, with weights, p. 47)
- [[eigenvector / eigenvalue]] — computed explicitly for the fundamental graphs (pp. 44–52)
- [[Fiedler vector / algebraic connectivity]] — λ₂, second-smallest Laplacian eigenvalue; bounded here (p. 44, 48–49)
- [[Rayleigh quotient]] — vᵀLv/vᵀv, upper-bounds λ₂ for v ⊥ 1 (Courant–Fischer) (p. 48)
- [[orthogonality]] — used to force eigenvector structure in stars (p. 45–46)
- [[isoperimetric ratio]] (new) — θ(S) = |∂(S)|/|S|; lower-bounded by λ₂(1−s) (p. 44)
- [[graph product]] (new) — G×H; each sum λᵢ+μⱼ is a Laplacian eigenvalue (p. 46–47)
- [[Kronecker product]] (new) — A⊗B block matrix; L_{G×H} = L_G⊗I + I⊗L_H (p. 47)
- [[test vector]] (new) — a guessed v ⊥ 1 used to upper-bound λ₂ (p. 48)
- [[equitable partition]] (new) — quotient used to get P_n from R_{2n} (p. 52)

## Canonical instances
- [[complete graph]] — L = nI − 11ᵀ, which acts as n times the identity on vectors orthogonal to 1; (5.1) is sharp (p. 44–45)
- [[star graph]] — eigenvalues 0, 1 (n−2 times), n (p. 45)
- [[hypercube]] — eigenvalues 2i with multiplicity C(d,i); θ ≥ 1, tight (p. 47–48)
- [[ring graph]] — cosine/sine eigenvectors (p. 49)
- [[path graph]] — λ₂ ≤ 12/(n(n+1)); (5.1) is loose (p. 49, 51)
- [[grid graph]] — product of two paths (p. 46)

## Bridges (candidates)
- [same-math] Eigenvectors of R_n ↔ Fourier analysis on Z_n: cos/sin modes diagonalize the circulant Laplacian — the structure is the same.
- [same-math] Hypercube eigenvectors (−1)^{yᵀx} ↔ Walsh–Hadamard characters of {0,1}^d.
- [structural-analogy] Equitable-partition quotient ↔ lumping a Markov chain by symmetry.
- [structural-analogy] Spectrum of G×H as sums ↔ separation of variables for the Laplacian on a product domain.

## Questions this raises
- If the path's λ₂ is about 1/n², how does Cheeger's inequality (Ch. 21) show the loss in (5.1) is at most quadratic?
- What technique gives lower bounds on λ₂ without a minimum over a large subspace (promised "next section", p. 49)?
- Which eigenvalues of grids follow from P_m × P_n by Thm 5.3.2?
- Which other graphs have eigenvalues from equitable partitions?

## Reading notes
- Printed page = pdf − 24.
- Misprint, p. 50: the last line of the ring computation reads (2 − cos(2πk/n)); the previous line gives 2 − 2cos(2πk/n), which is the correct eigenvalue.
- p. 45: "whenever two whenever two" is a duplicated phrase.
- p. 51, Thm 5.6.1: "excluding 2" looks inconsistent with the formula. Setting k=n in 2(1−cos(πk/n)) gives 4, not 2. This is my observation, not the author's.
- p. 49, (5.3): the line "(clearly, the denominator is at least n³/c…)" is a parenthetical remark beside the line. The exact denominator is (n+1)n(n−1)/3.
- p. 44: s in (5.1) is not defined on p. 44; it is defined on p. 45 (s = |S|/n).
- Theorem 20.1.1, Cheeger's inequality and Courant–Fischer are cited, not proved, in these pages.
- p. 45: the text says the C(n−1,2) pairs of degree-one vertices span a space of dimension n−1, but Lemma 5.2.2 and its proof (p. 46) give only n−2 independent eigenvectors of eigenvalue 1. These vectors lie in the sum-zero subspace of the n−1 leaves, so n−1 appears to be a slip. This is my observation, not the author's.
