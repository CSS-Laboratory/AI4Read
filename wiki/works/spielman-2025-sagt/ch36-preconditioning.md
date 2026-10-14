---
id: spielman-2025-sagt/ch36-preconditioning
work: spielman-2025-sagt
unit: "Chapter 36 — Preconditioning Laplacians"
pages: 287–294
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Preconditioning Laplacians

## L0 — One line
Preconditioning a graph Laplacian $L_G$ by the Laplacian of a low-stretch spanning tree bounds the largest eigenvalue of $L_T^{-1}L_G$ by the total stretch, which makes preconditioned conjugate gradient fast.

## L1 — The gist (≤ 120 words)
How can we solve $L_Gx=b$ quickly? Use a preconditioner $B$ (a matrix that is easy to solve in) that approximates the matrix $A$ (here $L_G$) in the sense $\alpha B\preceq A\preceq\beta B$. The cost of an iterative method then depends on $\beta/\alpha$. Trees are solvable in linear time. For a tree $T$, $\mathrm{Tr}(L_T^{-1}L_G)$ equals the sum of the edge stretches (an edge's weight times the summed inverse weights along its tree path), and a spanning tree with small total stretch exists. This gives iteration bounds of $O(m^{1/2}\log n)$ (Boman–Hendrickson) and then about $m^{1/3}$ (Spielman–Woo). The chapter ends with faster nearly-linear-time solvers and open questions.

**Prerequisites:** Loewner order ($A\preceq B$ means $B-A$ is PSD); Rayleigh quotient; matrix square root; trace as sum of eigenvalues; Laplacian as $\sum w_{uv}(\chi_u-\chi_v)(\chi_u-\chi_v)^T$; effective resistance; Chebyshev iteration and conjugate gradient as polynomial methods.

## L2 — Key ideas
- Quality of a preconditioner is $\kappa(A,B)=\beta/\alpha$, the ratio of the extreme eigenvalues of $B^{-1}A$ (common nullspace excluded) (p. 287).
- If $(1-\epsilon)B\preceq A\preceq(1+\epsilon)B$, each solve in $B$ shrinks the $A$-norm error (the norm $\|x\|_A=\sqrt{x^TAx}$) by a factor $\epsilon$ (iterative refinement); this fails in the Euclidean norm (p. 288–289).
- Polynomial methods give $\epsilon$-approximate solutions whenever a polynomial $q_t$ with $q_t(0)=1$ has $|q_t(\lambda_i)|\le\epsilon$ on the eigenvalues $\lambda_i$ of $B^{-1}A$. The preconditioned conjugate gradient method (PCG) finds the best solution of this polynomial form without knowing $\alpha,\beta$ (p. 289–290).
- A subgraph $H\subseteq G$ gives $L_H\preceq L_G$, so only the largest eigenvalue of $L_H^{-1}L_G$ matters. Trees can be solved exactly in linear time (p. 290).
- $\mathrm{Tr}(L_T^{-1}L_G)$ = total stretch of $G$'s edges in $T$ (the stretch of an edge is its weight times the sum of $1/$weight along its tree path), which is $O(m\log n\log\log n)$ for a good tree (p. 291–292).
- Few large eigenvalues (trace bound) plus Lemma 36.6.1 improve the iteration count to $O(m^{1/3}\log n\ln 1/\epsilon)$ (p. 292–293).
- Later solvers use subgraph preconditioning with recursion, sparsification, or randomized Gaussian elimination (p. 293).

## L3 — Walkthrough

**36.0 Definitions (p. 287).** A *preconditioner* for PSD $A$ is a PSD matrix $B$ such that solving in $B$ is easy and the condition number of $B^{-1}A$ is small. Define $\kappa(A,B)\overset{def}{=}\beta/\alpha$, where $\alpha$ is the largest and $\beta$ the smallest number with $\alpha B\preceq A\preceq\beta B$.

*Lemma 36.0.1.* $\alpha,\beta$ are the smallest and largest eigenvalues of $B^{-1}A$, excluding zero eigenvalues from a common nullspace. The common nullspace must be excluded, e.g. when $A,B$ are Laplacians of connected graphs. If the two matrices have different nullspaces, then $\alpha=0$ or $\beta=\infty$, so $\kappa$ is infinite (p. 287).

*Proof (for $\beta$, both matrices nonsingular):*
$$\lambda_{\max}(B^{-1}A)=\lambda_{\max}(B^{-1/2}AB^{-1/2})=\max_x\frac{x^TB^{-1/2}AB^{-1/2}x}{x^Tx}=\max_y\frac{y^TAy}{y^TBy},\quad y=B^{-1/2}x,$$
which equals $\beta$ (p. 287). The eigenvalues of $B^{-1}A$ equal those of $B^{-1/2}AB^{-1/2}$ and $A^{1/2}B^{-1}A^{1/2}$ (p. 287).

*Intuition note:* $\alpha,\beta$ are the smallest and largest values of $y^TAy/y^TBy$. So $\kappa$ measures how differently $A$ and $B$ stretch vectors.

**36.1 Approximate solutions (p. 288).** $\|x\|_A=\sqrt{x^TAx}=\|A^{1/2}x\|$. $\tilde x$ is an $\epsilon$-approximate solution of $Ax=b$ if $\|\tilde x-x\|_A\le\epsilon\|x\|_A$.

**36.2 Iterative refinement (p. 288–289).** Suppose $(1-\epsilon)B\preceq A\preceq(1+\epsilon)B$. Then all eigenvalues of $A^{1/2}B^{-1}A^{1/2}-I$ have absolute value at most $\epsilon$ (p. 288). Then
$$\|B^{-1}b-x\|_A=\|A^{1/2}B^{-1}b-A^{1/2}x\|=\|A^{1/2}B^{-1}Ax-A^{1/2}x\|=\|A^{1/2}B^{-1}A^{1/2}(A^{1/2}x)-A^{1/2}x\|\le\|A^{1/2}B^{-1}A^{1/2}-I\|\,\|A^{1/2}x\|\le\epsilon\|A^{1/2}x\|=\epsilon\|x\|_A.$$
This depends on the $A$-norm and fails under the Euclidean norm (p. 288). To improve: set $x_1=B^{-1}b$, $r_1=b-Ax_1=A(x-x_1)$. One solve in $B$ gives $x_2$ with $\|(x-x_1)-x_2\|_A\le\epsilon\|x-x_1\|_A\le\epsilon^2\|x\|_A$. Continuing, $k$ solves in $B$ give an $\epsilon^k$ approximation (p. 289).

*Intuition note:* Each solve in $B$ reduces the remaining $A$-norm error to at most a fraction $\epsilon$ of what it was (an upper bound, not an equality). Repeating on the residual multiplies the error factors.

**36.3 Matrix-norm analysis of iterative methods (p. 289).** A method gives $\epsilon$-approximate solutions after $t$ iterations if some degree-$t$ polynomial $q$ has $q(0)=1$ and $|q(\lambda_i)|\le\epsilon$ at all eigenvalues of $A$. Write $q(x)=1-xp(x)$ and set $\tilde x=p(A)b$. Then $\|\tilde x-x\|_A=\|p(A)Ax-x\|_A$. Since $I,A,p(A),A^{1/2}$ commute, this equals $\|p(A)AA^{1/2}x-A^{1/2}x\|\le\|p(A)A-I\|\,\|A^{1/2}x\|\le\epsilon\|x\|_A$.

**36.4 Preconditioned methods (p. 289–290).** Chebyshev iteration and PCG extend iterative refinement and usually work with condition numbers much larger than 2. Each iteration solves in $B$, multiplies a vector by $A$, and does a constant number of other vector operations, so solves in $B$ must be cheap (p. 289). Let $\lambda_i$ be eigenvalues of $B^{-1}A$. If $q_t(x)=1-xp_t(x)$ has $|q_t(\lambda_i)|\le\epsilon$ for all $i$, then $x_t\overset{def}{=}p_t(B^{-1}A)B^{-1}b$ is $\epsilon$-approximate:
$$\|x-x_t\|_A=\|A^{1/2}x-A^{1/2}x_t\|=\|A^{1/2}x-A^{1/2}p_t(B^{-1}A)B^{-1}b\|=\|A^{1/2}x-A^{1/2}p_t(B^{-1}A)B^{-1}Ax\|=\|A^{1/2}x-A^{1/2}p_t(B^{-1}A)B^{-1}A^{1/2}(A^{1/2}x)\|\le\|I-A^{1/2}p_t(B^{-1}A)B^{-1}A^{1/2}\|\,\|A^{1/2}x\|.$$
Also $I-A^{1/2}p_t(B^{-1}A)B^{-1}A^{1/2}=I-p_t(A^{1/2}B^{-1}A^{1/2})A^{1/2}B^{-1}A^{1/2}=q_t(A^{1/2}B^{-1}A^{1/2})$. So $\|x-x_t\|_A\le\|q_t(A^{1/2}B^{-1}A^{1/2})\|\,\|A^{1/2}x\|\le\epsilon\|x\|_A$ (p. 290).

PCG, after $t$ steps, produces the $x_t$ minimizing $\|x_t-x\|_A$ among all vectors of this polynomial form of degree at most $t$. So it is at least as good as Preconditioned Chebyshev and does not need to know $\alpha,\beta$ (p. 290).

**36.5 Preconditioning by trees (p. 290–292).** Vaidya's idea: precondition $L_G$ by $L_H$ for a subgraph $H$. Then $L_H\preceq L_G$, so all eigenvalues of $L_H^{-1}L_G$ are at least 1; we need only a bound on the largest (p. 290). Tree Laplacians can be solved exactly in linear time, by an LU factorization with linearly many nonzeros or by a dynamic program up from the leaves to a root and back down (p. 290).

With $L_G=\sum_{(u,v)\in E}w_{u,v}(\chi_u-\chi_v)(\chi_u-\chi_v)^T$ and $T$ a spanning tree, linearity and cyclicity of the trace give
$$\mathrm{Tr}(L_T^{-1}L_G)=\sum_{(u,v)\in E}w_{u,v}(\chi_u-\chi_v)^TL_T^{-1}(\chi_u-\chi_v)\quad(p.~291).$$
Each term is the effective resistance in $T$ between $u,v$. In a tree this is a series path of resistors, i.e. the distance in $T$ with edge length $=1/$weight:
$$(\chi_u-\chi_v)^TL_T^{-1}(\chi_u-\chi_v)=\sum_{i=1}^k\frac1{w_i}\tag{36.1}$$
where $w_1,\dots,w_k$ are the weights on the tree path from $u$ to $v$ (p. 291). Alon–Karp–Peleg–West defined this as the *stretch* of an unweighted edge; for a weighted edge the stretch is $w_{u,v}\sum_{i=1}^k 1/w_i$ (p. 291).

*Theorem 36.5.1 (Abraham–Neiman).* Every weighted graph $G$ has a spanning tree $T$ whose total stretch over all edges of $G$ is at most $O(m\log n\log\log n)$, computable in time $O(m\log n\log\log n)$ (p. 291).

So $\mathrm{Tr}(L_T^{-1}L_G)\le O(m\log n\log\log n)$, hence $\lambda_{\max}(L_T^{-1}L_G)$ is at most this. PCG needs at most $O(m^{1/2}\log n)$ iterations, each with one multiplication by $L_G$ and one solve in $L_T$. The running time is $O(m^{3/2}\log n\log1/\epsilon)$, much lower than Gaussian elimination's $O(n^3)$ when $m$ is small (p. 292). This is due to Boman and Hendrickson (p. 292).

*Intuition note:* The trace is a sum of eigenvalues, each at least 1. The largest eigenvalue is therefore at most the trace, i.e. at most the total stretch. A combinatorial property of the tree controls a spectral quantity.

**36.6 Improving the bound (p. 292–293).** Because the trace is the sum of the eigenvalues, $L_T^{-1}L_G$ has at most $\mathrm{Tr}(L_T^{-1}L_G)/\beta$ eigenvalues larger than $\beta$, for every $\beta>0$ (p. 292).

*Lemma 36.6.1.* Let $\lambda_1,\dots,\lambda_n>0$ be at least $\alpha$, with at most $k$ of them above $\beta$. For every $t\ge k$ there is a polynomial $p$ of degree $t$ with $p(0)=1$ and
$$|p(\lambda_i)|\le2\Big(1+\tfrac{2}{\sqrt{\beta/\alpha}}\Big)^{-(t-k)}\ \text{for all }\lambda_i.$$
*Proof.* Take $r$, the earlier Chebyshev-based polynomial of degree $t-k$ with $|r(X)|\le2(1+2/\sqrt{\beta/\alpha})^{-(t-k)}$ on $[\alpha,\beta]$. Set $p(X)=r(X)\prod_{i:\lambda_i>\beta}(1-X/\lambda_i)$. It vanishes at each $\lambda_i>\beta$. For $X\in[\alpha,\beta]$, $|p(X)|\le|r(X)|$ because $X<\lambda_i$ in every factor (p. 292).

*Intuition note:* Each large eigenvalue is removed at the price of one extra iteration. Only the remaining, smaller range controls the Chebyshev-type rate.

Apply this to PCG with $\beta=\mathrm{Tr}(L_T^{-1}L_G)^{2/3}$ and $k=\mathrm{Tr}(L_T^{-1}L_G)^{1/3}$ (and $\alpha=1$, *(added step)*: all eigenvalues are at least 1, p. 290). PCG gives $\epsilon$-approximate solutions in $O(\mathrm{Tr}(L_T^{-1}L_G)^{1/3}\ln(1/\epsilon))=O(m^{1/3}\log n\ln1/\epsilon)$ iterations (p. 293). This is due to Spielman and Woo (p. 293).

**36.7 Further improvements (p. 293).** Three families give nearly-linear-time Laplacian solvers:
- *Subgraph preconditioners:* add edges back to low-stretch trees, eliminate degree-1 and 2 vertices by Gaussian elimination, then recurse. The first such algorithm ran in $O(m\log^cn\log1/\epsilon)$ [ST14]. Koutis–Miller–Peng made it practical and simpler. The asymptotically fastest, $O(m\log^{1/2}m\,\log^c\log n\log1/\epsilon)$, also works this way [CKM+14].
- *Sparsification* ([PS14, KLP+16]): does not use low-stretch trees.
- *Random sampling to accelerate Gaussian elimination* (Kyng–Sachdeva): $O(m\log^2n\log1/\epsilon)$. It is not asymptotically best but is the best in practice because it is so simple (Laplacians.jl).

Algebraic Multigrid and Combinatorial Multigrid are often fast in practice but have no theoretical analysis (p. 293).

**36.8 Questions (p. 293–294).** The author conjectures that spanning trees of even lower stretch can be constructed, and asks whether every graph has a spanning tree of average stretch "2 log2 n" (exponent or base unclear in the text layer). The author sees no reason this should fail, and also believes it should be achievable by a practical algorithm. The author knows no analysis of the AKPW-based heuristic better than a stretch bound garbled in the text layer. The Abraham–Neiman trees seem too complicated to be practical. Eigenvalues of $L_H^{-1}L_G$ are *generalized eigenvalues*; the link to stretch is the first combinatorial interpretation the author knows, and he asks for others (p. 294).

## Toy example (ours)
$G$ = triangle on vertices 1,2,3, all weights 1. $T$ = path 1–2–3 (edges 12, 23).
- Stretches: tree edges have stretch $1\cdot1=1$ each; edge (1,3) has path weights $1,1$, so stretch $1\cdot(1+1)=2$. Total $=1+1+2=4$.
- $L_T=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix}$, $L_G=3I-J$ ($J$ = all-ones matrix). On the space orthogonal to $\mathbf 1$, $L_T$ has eigenvectors $(1,0,-1)$ with eigenvalue 1 and $(1,-2,1)$ with eigenvalue 3 (checked by multiplication). $L_G$ acts as 3 there.
- So the nonzero eigenvalues of $L_T^{+}L_G$ ($L_T^+$ = pseudoinverse) are $3/1=3$ and $3/3=1$. Sum $=4=$ total stretch, as the chapter's trace identity says. Here $\alpha=1,\beta=3$, $\kappa=3$, and $\lambda_{\max}=3\le\mathrm{Tr}=4$.

## Concepts
- [[condition-number]] — here the relative condition $\kappa(A,B)=\beta/\alpha$, with $\alpha B\preceq A\preceq\beta B$ (p. 287)
- [[positive-semidefinite-matrix]] — $A,B$ must be PSD; $\preceq$ is the order "difference is PSD" (p. 287)
- [[rayleigh-quotient]] — $\max_y y^TAy/y^TBy$ gives $\beta$ (p. 287)
- [[krylov-subspace-methods]] — Chebyshev iteration and PCG as polynomial methods (p. 289–290)
- [[graph-laplacian]] — $L_G=\sum w_{uv}(\chi_u-\chi_v)(\chi_u-\chi_v)^T$ (p. 291)
- [[preconditioner]] (new) — easy-to-solve PSD $B$ with small $\kappa(A,B)$ (p. 287)
- [[a-norm-approximate-solution]] (new) — $\|\tilde x-x\|_A\le\epsilon\|x\|_A$ (p. 288)
- [[iterative-refinement]] (new) — repeatedly solve in $B$ on the residual; error shrinks by $\epsilon$ per solve (p. 289)
- [[stretch]] (new) — $w_{uv}\sum_i 1/w_i$ over the tree path; the edge's effective resistance in $T$ times its weight (p. 291)
- [[low-stretch-spanning-tree]] (new) — spanning tree with small total stretch (p. 291)
- [[generalized-eigenvalue]] (new) — eigenvalue of $L_H^{-1}L_G$ (p. 294)

## Canonical instances
- [[tree-preconditioner-vaidya]] — a subgraph/tree Laplacian as preconditioner (p. 290)
- [[boman-hendrickson-bound]] — $O(m^{3/2}\log n\log1/\epsilon)$ solver (p. 292)
- [[spielman-woo-bound]] — $O(m^{1/3}\log n\ln1/\epsilon)$ iterations via Lemma 36.6.1 (p. 293)

## Bridges (candidates)
- [same-math] Stretch of an edge ↔ electrical networks: effective resistance in a series path of resistors (p. 291).
- [structural-analogy] Ignoring the $k$ largest eigenvalues at the cost of $k$ iterations ↔ deflation in Krylov methods.
- [structural-analogy] Preconditioning by a spanning tree ↔ approximating a graph by a sparser, simpler graph (sparsification).

## Questions this raises
- Does every graph have a spanning tree of average stretch about $2\log^2 n$ (or $2\log_2 n$; see Reading notes), and can it be found practically?
- Why does the $A$-norm make the one-step bound work while the Euclidean norm does not?
- What other combinatorial meanings do generalized eigenvalues $\lambda(L_H^{-1}L_G)$ have?
- How does the recursion work when edges are added back to a tree and degree-1 and 2 vertices are eliminated?

## Reading notes
- Printed = pdf − 24. Page images were given only for printed pp. 287–292. For pp. 293–294 only the text layer was available, so the garbled stretch bound on p. 293 (written "$O(m2\log n)$" with a root sign) and the conjecture "2 log2 n" are not verified.
- The text writes PCG's search space as "$p_t(b)$"; read literally this does not match the form $p_t(B^{-1}A)B^{-1}b$ used earlier. It is probably shorthand.
- The $O(m^{1/2}\log n)$ iteration count on p. 292 has no $\log(1/\epsilon)$ factor, although the time bound does.
- The text layer prints $\preceq$ as "4" and $\epsilon$ as a blank; the page images show the proper symbols.
- Theorem 36.5.1 is attributed to [AN12]; the text does not spell out the names (Abraham–Neiman appears on p. 294).
- The proof of Lemma 36.0.1 includes the typo "settting".
