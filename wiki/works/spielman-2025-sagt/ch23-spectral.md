---
id: spielman-2025-sagt/ch23-spectral
work: spielman-2025-sagt
unit: "Chapter 23 — Spectral Partitioning in a Stochastic Block Model"
pages: 189-195
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
audited: 2026-10-15
audit_fixes: 7
---
# Spectral Partitioning in a Stochastic Block Model

## L0 — One line
In a planted-bisection random graph, the second eigenvector of the adjacency matrix is probably close to the second eigenvector of the expected matrix, so (under conditions on p and q) its signs are expected to recover the hidden partition with at most $288p(1-p)/(p-q)^2$ errors: a constant number for fixed p and q, a constant fraction for p = 1/2, q = p − 17/√n.

## L1 — The gist (≤ 120 words)
Question: can a graph's hidden two-block structure be found from the second eigenvector of its adjacency matrix? Setup: vertices are split into equal sets X and Y. Edges appear with probability p inside a set and q < p across. Answer: the random matrix M is the expected matrix A plus a small random matrix R. Bounds on ‖R‖, Weyl's inequality and the Davis–Kahan theorem keep the second eigenvector of M close to that of A. Given extra conditions, we expect at most 288p(1−p)/(p−q)² misclassified vertices. This is a constant number for fixed p and q. For q = p − 17/√n (p = 1/2) it allows a constant fraction. The chapter also proves a weak Davis–Kahan.

**Prerequisites:** eigenvalues/eigenvectors of symmetric matrices; spectral norm (largest stretch $\max_{\|x\|=1}\|Rx\|$; for symmetric $R$, the largest $|$eigenvalue$|$); rank; Weyl's inequality (via Courant–Fischer, which writes each eigenvalue as a max–min of $x^TAx/x^Tx$); basic random-graph models.

## L2 — Key ideas (5–10 bullets)
- Planted bisection: edge probability p within X and within Y, q across, p > q; the algorithm sees only the graph (pp. 189–190).
- Expected matrix, shifted by pI, has rank 2. Its second eigenvector is ±1/√n on X and Y, with eigenvalue (n/2)(p−q) (p. 191).
- The noise R = M − E[M] has small norm with high probability: ‖R‖ ≤ 3√(pn) when p ≥ c₀ln⁴n/n (p. 192).
- Weyl's inequality moves eigenvalues by at most ‖R‖. Davis–Kahan bounds the (sine of the) angle of an eigenvector by about 2‖R‖ over the gap to the other eigenvalues (pp. 192–193).
- At a misclassified vertex ψ₂ and φ₂ differ by at least 1/√n, so k errors force ‖ψ₂−φ₂‖ ≥ √(k/n). With the angle bound, and assuming q > p/3 and ‖R‖ ≤ 3√(p(1−p)n), this gives k ≤ 288p(1−p)/(p−q)² (pp. 193–194).
- Weak Davis–Kahan proof: expand ψᵢ in A's eigenbasis, then bound ‖Aψᵢ‖ below by δ sinθᵢ and above by 2‖R‖ (pp. 194–195).
- Warning: real data rarely resembles these models, and there is no reason to expect algorithms tuned to them to work in practice; nevertheless, some do (p. 190).

## L3 — Walkthrough

**Intro (pp. 189–190).** Graph bisection: split the vertices into two equal sets while minimizing edges between them. Planted model: choose equal sets X, Y, then probabilities p > q. Edge (a,b) has probability p if both ends are in X or both in Y, and q otherwise (p. 189). Expected crossing edges: q|X||Y|. For p = 1/2 and q = p − 17/√n the partition can be approximately recovered from the second eigenvector (p. 189). If p is too close to q, the X/Y partition will not be the smallest; for example, if q = p − ε/√n for small ε, the problem is information-theoretically unsolvable (no method can recover the partition from the graph, whatever its computing power) (p. 189). The analysis simplifies McSherry's. Idea: treat the generated matrix as a perturbation of the expected one (pp. 189–190). Warning: few real data sets look like these models, and there is no reason to believe that algorithms optimized for them will be useful in practice. Nevertheless, some of them are (p. 190).

**23.1 The perturbation approach (pp. 190–192).** Take X = {1..n/2}, Y = {n/2+1..n} (the algorithm is not told). Expected matrix:
$$A=\begin{bmatrix} pJ_{n/2} & qJ_{n/2}\\ qJ_{n/2} & pJ_{n/2}\end{bmatrix}-pI_n,$$
with $J$ the all-ones matrix (p. 190). Adjacency matrix $M(a,b)=1$ with probability $A(a,b)$, else 0, with $M(a,b)=M(b,a)$, $M(a,a)=0$. Hence $\mathbb E[M]=A$ (p. 190).

Algorithm: compute $\psi_2$, the eigenvector of the second-largest eigenvalue of $M$. Set $S=\{a:\psi_2(a)<0\}$ and guess that $S$ is one side (p. 190).

Shift: $\widehat M = M+pI$, $\widehat A=A+pI$. Eigenvectors are unchanged. $\widehat A$ has rank 2. Define
$$R=\widehat M-\widehat A=M-\mathbb E[M].$$
(p. 191)

Eigenpairs of $\widehat A$ (p. 191):
$$\widehat A\mathbf 1=\tfrac n2(p+q)\mathbf 1,\quad \alpha_1=\tfrac n2(p+q);$$
$$\phi_2(a)=\begin{cases}1/\sqrt n & a\in X\\ -1/\sqrt n & a\in Y\end{cases},\quad \widehat A\phi_2=\tfrac n2(p-q)\phi_2,\quad \alpha_2=\tfrac n2(p-q).$$
All other eigenvalues are 0. Entries of $R$: for $(a,b)$ in the same part, $1-p$ with probability $p$ and $-p$ with probability $1-p$. For different parts, $1-q$ with probability $q$ and $-q$ with probability $1-q$ (p. 191).

*Intuition note:* In the ideal graph, the sign pattern of one eigenvector is exactly the partition. The random graph is this ideal matrix plus mean-zero noise, so we need the noise to be small compared with the gap $p-q$ (p. 191).

Norm of $R$: the Chapter 8 bounds apply to entries from $\{1-q_{a,b},-q_{a,b}\}$ with $q_{a,b}<p\le 1/2$ and mean 0, because (8.2) still applies (p. 192). Sharper, via Vu:

**Theorem 23.1.1.** There are constants $c_1,c_2$ such that with probability approaching 1,
$$\|R\|\le 2\sqrt{p(1-p)n}+c_1\big(p(1-p)n\big)^{1/4}\ln n,\quad\text{provided } p\ge c_2\tfrac{\ln^4 n}{n}.$$

**Corollary 23.1.2.** There is $c_0$ such that with probability approaching 1, $\|R\|\le 3\sqrt{pn}$, provided $p\ge c_0\ln^4 n/n$ (p. 192). Alon–Krivelevich–Vu: the chance that $\|R\|$ exceeds this value by more than $t$ is exponentially small in $t$ (p. 192).

**23.2 Perturbation theory for eigenvectors (pp. 192–193).** Let $\mu_1\ge\dots\ge\mu_n$ be the eigenvalues of $\widehat M$ and $\alpha_1>\alpha_2>0=\alpha_3=\dots$ those of $\widehat A$. Weyl's inequality (provable via Courant–Fischer):
$$|\mu_i-\alpha_i|\le\|R\|.\tag{23.1}$$
Davis–Kahan says $\psi_2$ is close to $\phi_2$ in angle if $\|R\|$ is well below the distance from $\alpha_2$ to the other eigenvalues of $\widehat A$. An eigenvector does not move much if its eigenvalue is isolated (p. 192).

Why the gap matters (pp. 192–193): $\mathrm{diag}(1+\epsilon,1)$ and $\mathrm{diag}(1,1+\epsilon)$ are close, but their leading eigenvectors $(1,0)^T$ and $(0,1)^T$ are 90° apart. The matrix $\begin{bmatrix}1&\epsilon\\ \epsilon&1\end{bmatrix}$ has eigenvectors $(1,1)^T,(1,-1)^T$, 45° from both. The problem: an eigenvalue of multiplicity above 1 (repeated, so several independent eigenvectors share it) has no unique eigenvector (p. 193).

**Theorem 23.2.1.** $A,B$ symmetric, $R=A-B$. $A$ has eigenvalues $\alpha_i$ and eigenvectors $\phi_i$; $B$ has $\beta_i$ and $\psi_i$. $\theta_i$ is the angle between $\pm\psi_i$ and $\pm\phi_i$. Then
$$\sin2\theta_i\le\frac{2\|R\|}{\min_{j\ne i}|\alpha_i-\alpha_j|}.$$
The angle is at most $\pi/2$, since this bounds the angle between eigenspaces (the set of all eigenvectors of one eigenvalue, plus 0), not between particular eigenvectors. The chapter proves a slightly weaker version, with $\theta$ in place of $2\theta$ (p. 193).

**23.3 Partitioning (pp. 193–194).** When $\|R\|$ is small, Weyl gives that $\mu_2$ has multiplicity one. Let $\phi_2$ be the unit eigenvector nearest in angle to $\psi_2$. Assign $a$ to $X$ if $\psi_2(a)>0$ (p. 193). Let $\delta=\psi_2-\phi_2$ and let $\theta$ be the angle between them. A misclassified vertex has $|\delta(a)|\ge 1/\sqrt n$. So if $k$ vertices are misclassified, $\|\delta\|\ge\sqrt{k/n}$. For unit vectors, $\|\delta\|\le\sqrt2\sin\theta$ (the $\sqrt2$ disappears for small $\theta$) (p. 193).

Assume $q>p/3$. Then $\min_{j\ne2}|\alpha_2-\alpha_j|=\alpha_2-\alpha_3=\alpha_2=\tfrac n2(p-q)$ (p. 194). *(added step: $\alpha_1-\alpha_2=nq$, and $nq\ge\frac n2(p-q)\iff q\ge p/3$.)* Assuming $\|R\|\le3\sqrt{p(1-p)n}$:
$$\sin\theta\le\frac{2\|R\|}{\frac n2(p-q)}\le\frac{2\cdot3\sqrt{p(1-p)n}}{\frac n2(p-q)}=\frac{12\sqrt{p(1-p)}}{\sqrt n\,(p-q)}.$$
Therefore
$$\sqrt{k/n}\le\frac{\sqrt2\cdot12\sqrt{p(1-p)}}{\sqrt n\,(p-q)}\ \Rightarrow\ k\le\frac{288\,p(1-p)}{(p-q)^2}.$$
For constant $p,q$ and growing $n$ the author expects at most a constant number of errors (p. 194). For $p=1/2$, $q=p-17/\sqrt n$ the author writes the bound as $n/4$, so a constant fraction of vertices may be misclassified (p. 194). Once most vertices are right, they can be used to classify the rest better; many advances concern this step (p. 194).

*Intuition note:* Each wrong sign makes the two eigenvectors differ by at least $1/\sqrt n$ at that vertex, so $k$ wrong signs force an error of at least $\sqrt{k/n}$. A small angle error therefore allows only a few wrong signs. A larger gap $p-q$ means a smaller angle and fewer errors.

**23.4 Proof of (weak) Davis–Kahan (pp. 194–195).** Replace $A,B$ by $A-\alpha_iI$, $B-\alpha_iI$, so $\alpha_i=0$. This changes neither eigenvectors nor gaps. If $\alpha_i$ has multiplicity above 1 the theorem is vacuous, so assume multiplicity 1. Weyl gives $|\beta_i|\le\|R\|$. Expand $\psi_i=\sum_jc_j\phi_j$, $c_j=\phi_j^T\psi_i$, and set $\delta=\min_{j\ne i}|\alpha_j|$ (p. 194). Then
$$\|A\psi_i\|^2=\sum_jc_j^2\alpha_j^2=\sum_{j\ne i}c_j^2\alpha_j^2\ge\delta^2\sum_{j\ne i}c_j^2=\delta^2(1-c_i^2)=\delta^2\sin^2\theta_i.$$
On the other side,
$$\|A\psi_i\|=\|(B+R)\psi_i\|\le\|B\psi_i\|+\|R\psi_i\|=\beta_i+\|R\psi_i\|\le2\|R\|.$$
Hence $\sin\theta_i\le 2\|R\|/\delta$ (p. 195).

*Intuition note:* $A$ stretches any part of $\psi_i$ outside $\phi_i$ by at least the gap $\delta$. But $\psi_i$ is nearly killed by $A$, up to a push of size $2\|R\|$. So the outside part must be small.

**23.5 Further Reading (p. 195).** For bounding norms and eigenvalues of random matrices, the author recommends [Ver10] and [Tro12] (p. 195).

## Toy example (ours)
$n=4$, $X=\{1,2\}$, $Y=\{3,4\}$, $p=0.6$, $q=0.2$. $\widehat A$ has $0.6$ in the diagonal 2×2 blocks and $0.2$ elsewhere. $\alpha_1=\frac42(0.8)=1.6$, $\alpha_2=\frac42(0.4)=0.8$, and the rest are 0. Check: $\phi_2=(\tfrac12,\tfrac12,-\tfrac12,-\tfrac12)$. Row 1 of $\widehat A\phi_2$ is $0.3+0.3-0.1-0.1=0.4=0.8\cdot\tfrac12$ ✓.

Suppose noise gives $\psi_2=(\tfrac12,\tfrac12,\tfrac12,-\tfrac12)$, a unit vector. Then $\delta=(0,0,1,0)$ and $\|\delta\|=1$. Vertex 3 is wrong, so $k=1$. Check: $|\delta(3)|=1\ge1/\sqrt4=0.5$, and $\|\delta\|=1\ge\sqrt{1/4}=0.5$. Also $\cos\theta=\phi_2^T\psi_2=\tfrac14+\tfrac14-\tfrac14+\tfrac14=\tfrac12$, so $\theta=60^\circ$, $\sin\theta\approx0.866$, and $\sqrt2\sin\theta\approx1.22\ge1$ ✓.

Limits of this toy: it shows only the step from wrong signs to $\|\delta\|$. It sits exactly at $q=p/3$ ($0.2=0.6/3$), the edge of the chapter's assumption $q>p/3$ (here $\alpha_1-\alpha_2=\alpha_2=0.8$, a tie). The $k$ bound would be $288\cdot0.24/0.16=432\gg n=4$, so it says nothing here.

## Concepts
- [[stochastic-block-model]] (new) — random graph whose edge probability depends on the blocks of the endpoints; here p within, q across (p. 189)
- [[matrix-perturbation]] (new) — treating a random matrix as expected matrix plus small-norm noise R and tracking eigenvectors (p. 190)
- [[weyl-inequality]] (new) — $|\mu_i-\alpha_i|\le\|R\|$ for eigenvalues of symmetric matrices (p. 192)
- [[davis-kahan-theorem]] (new) — sine of the eigenvector angle ($\sin 2\theta$ in the full theorem) bounded by $2\|R\|$ over the eigenvalue gap (p. 193)
- [[eigenvector-eigenvalue]] — second eigenvector of the adjacency matrix used as a partition indicator (p. 190)
- [[rank]] — $\widehat A$ has rank 2, which makes its spectrum explicit (p. 191)
- [[adjacency-matrix]] — here $M$, random, with entries 1 on edges (p. 190)
- [[norm]] — spectral norm $\|R\|$ (largest $|$eigenvalue$|$ of symmetric $R$) measures noise size (p. 191)

## Canonical instances
- [[planted-bisection]] (new) — the equal-sized X/Y model with probabilities p > q (p. 189)
- [[eigenvector-instability-2x2]] (new) — near-identical diagonal matrices with eigenvectors 90° apart show why a gap is needed (pp. 192–193)

## Bridges (candidates)
- [structural-analogy] signal-plus-noise recovery by the second eigenvector ↔ linear-algebra: Fiedler vector splitting a graph into communities — both read a partition from signs of an eigenvector.
- [same-math] Davis–Kahan angle bound ↔ linear-algebra: perturbation of invariant subspaces under symmetric noise — the theorem is the same statement.

## Questions this raises
- Why is the ‖R‖ bound needed with probability approaching 1, and how does Vu's theorem sharpen Chapter 8's bound?
- How do the later "refine from the correct vertices" methods improve on the constant-fraction error?
- What happens when p and q are near the unsolvable threshold q = p − ε/√n?

## Reading notes
- Printed = pdf − 24. All pages were readable in the images.
- p. 189: "p = 1/2 and q = p − 17/√n" and "q = p − ε/√n" (the text layer drops the ϵ; it is visible in the image). Typos: "In this chapter, show", "When then choose", "extends to over values", "the problem in information-theoretically unsolvable" ("in" for "is").
- Sign convention: p. 190 uses $\psi_2(a)<0$ for $S$, p. 193 uses $\psi_2(a)>0$ for $X$. The sign of an eigenvector is arbitrary (Theorem 23.2.1 uses $\pm\psi_i$, $\pm\phi_i$).
- p. 193: "let φ₂ be the unit eigenvector of µ₂" appears to mean the eigenvector of $\alpha_2$ of $\widehat A$ (my reading).
- Corollary 23.1.2 gives $3\sqrt{pn}$ (p. 192), but §23.3 assumes $\|R\|\le3\sqrt{p(1-p)n}$ (p. 194). The second is smaller; it follows from Theorem 23.1.1 only if $c_1(p(1-p)n)^{1/4}\ln n\le\sqrt{p(1-p)n}$ (my reading).
- p. 194: with $p=1/2$, $q=p-17/\sqrt n$, $288p(1-p)/(p-q)^2=72n/289\approx0.249n$, which is slightly below the printed "$=n/4$".
- Proof (p. 194): "ψᵢ is a unit vector in the nullspace of B" holds only if $\beta_i=0$. Later $\|B\psi_i\|=\beta_i$ should read $|\beta_i|$.
- p. 195: "because we assumed cᵢ = 0" should read $\alpha_i=0$.
- p. 193: "Let Let".
