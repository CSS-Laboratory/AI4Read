---
id: spielman-2025-sagt/ch32-sparsification
work: spielman-2025-sagt
unit: "Chapter 32 — Sparsification by Random Sampling"
pages: 258–263
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
# Sparsification by Random Sampling

## L0 — One line
Sampling each edge with probability proportional to its leverage score, and reweighting it by 1/probability, gives with high probability a sparse graph with O(ε⁻² n log n) edges that ε-approximates the original graph's Laplacian.

## L1 — The gist (≤ 120 words)
Can every graph be approximated by a sparse graph, as expanders approximate complete graphs? The chapter says yes. Keep each edge independently with probability proportional to its leverage score (weight × effective resistance), and give kept edges weight w/p. This keeps the Laplacian unchanged in expectation. After normalising by $L_G^{+/2}$, the sampled Laplacian is a sum of independent PSD (positive semidefinite) matrices, each of norm at most $R$ (exactly $R$ if its edge is kept). A matrix Chernoff bound then shows it is close to the projection Π, so $(1-\epsilon)L_G \preceq L_H \preceq (1+\epsilon)L_G$ with high probability. Graphs that approximate each other have similar effective resistances, eigenvalues, cut values and linear-system solutions.

**Prerequisites:** Loewner order (≼) on symmetric matrices; PSD matrices; pseudoinverse and its square root; graph Laplacian $L=\sum w\,\delta\delta^T$; effective resistance; trace; Chernoff bounds.

## L2 — Key ideas
- ε-approximation is defined by $(1-\epsilon)L_G \preceq L_H \preceq (1+\epsilon)L_G$. It makes resistances, eigenvalues, cut values and linear solves similar (p. 258).
- Keep edge $(a,b)$ with probability $p_{a,b}$ and give it weight $w_{a,b}/p_{a,b}$. Then $\mathbb E L_H=L_G$ (p. 259).
- Matrix Chernoff (Thm 32.3.1) bounds the extreme eigenvalues of a sum of independent PSD matrices with norm ≤ R. Larger norms make the bound weaker (pp. 259–260).
- Multiplying by $L_G^{+/2}$ on both sides reduces the goal to showing $L_G^{+/2}L_HL_G^{+/2}$ is close to its expectation Π, the projection onto range($L_G$) (p. 260).
- Choosing $p_{a,b}=\ell_{a,b}/R$ makes every sampled matrix have norm exactly R. The expected edge count is $(n-1)/R$, because leverage scores sum to $n-1$ (pp. 261–262).
- With $R=\epsilon^2/(3.5\ln n)$, both tails are polynomially small in $n$ and $H$ has at most $4n\ln n/\epsilon^2$ edges with high probability (p. 262).
- Edges with $p\ge1$ are either kept outright or split into several independent pieces (p. 263).
- Open problem: estimate effective resistances quickly without fast Laplacian solvers (p. 263).

## L3 — Walkthrough

All matrices are $n\times n$ (n = number of vertices).

### 32.1–32.2 Overview and definition
- Claim: any graph on $n$ vertices has an ε-approximation with $O(\epsilon^{-2}n\log n)$ edges (p. 258).
- Originally proved in [SS11] via Rudelson's bound. Here it is proved via Tropp's matrix Chernoff bound. The next chapter removes the $\log n$ (p. 258).
- Definition: $H$ is an ε-approximation of $G$ if
$$(1-\epsilon)L_G\preceq L_H\preceq(1+\epsilon)L_G.$$
- Consequences listed: similar effective resistances, eigenvalues, set boundaries ($\chi_S^TL_G\chi_S$) and linear-system solutions (p. 258).
- Construction: pick $p_{a,b}$ per edge, include the edge independently with that probability, and give it weight $w_{a,b}/p_{a,b}$. The goal is at most $4n\ln n/\epsilon^2$ edges and an ε-approximation with high probability (p. 259).
- Why reweight: with $L_G=\sum_{(a,b)\in E}w_{a,b}L_{a,b}$ ($L_{a,b}$ = unit-weight edge Laplacian),
$$\mathbb E L_H=\sum_{(a,b)\in E}p_{a,b}(w_{a,b}/p_{a,b})L_{a,b}=L_G.$$
- Footnote: the $p_{a,b}$ will be proportional to leverage scores (p. 259).

### 32.3 Matrix Chernoff bounds
**Theorem 32.3.1** (Tropp, Cor. 5.2). Let $X_1,\dots,X_m$ be independent random symmetric PSD matrices with $\|X_i\|\le R$ almost surely. Let $X=\sum_iX_i$. Let $\mu_{\min},\mu_{\max}$ be the extreme eigenvalues of $\mathbb E[X]=\sum_i\mathbb E[X_i]$. Then
$$\Pr\Big[\lambda_{\min}\Big(\sum_iX_i\Big)\le(1-\epsilon)\mu_{\min}\Big]\le n\Big(\frac{e^{-\epsilon}}{(1-\epsilon)^{1-\epsilon}}\Big)^{\mu_{\min}/R},\quad 0<\epsilon<1,$$
$$\Pr\Big[\lambda_{\max}\Big(\sum_iX_i\Big)\ge(1+\epsilon)\mu_{\max}\Big]\le n\Big(\frac{e^{\epsilon}}{(1+\epsilon)^{1+\epsilon}}\Big)^{\mu_{\max}/R},\quad 0<\epsilon.$$
The $X_i$ may have different distributions (p. 259). Simpler forms (p. 260):
$$\frac{e^{-\epsilon}}{(1-\epsilon)^{1-\epsilon}}\le e^{-\epsilon^2/2},\qquad \frac{e^{\epsilon}}{(1+\epsilon)^{1+\epsilon}}\le e^{-\epsilon^2/3},\qquad 0<\epsilon<1.$$

*Intuition note:* The text presents this as a matrix analog of the Chernoff bound for real variables (p. 259). The bound carries a factor $n$ in front, where $n$ is the matrix dimension. Smaller norm bound $R$ gives a sharper bound, because bigger norms make it weaker (p. 259).

### 32.4 The key transformation
- For positive definite $A,B$: $A\preceq(1+\epsilon)B\iff B^{-1/2}AB^{-1/2}\preceq(1+\epsilon)I$ (p. 260).
- The same holds for singular PSD matrices with the same nullspace:
$$L_H\preceq(1+\epsilon)L_G\iff L_G^{+/2}L_HL_G^{+/2}\preceq(1+\epsilon)L_G^{+/2}L_GL_G^{+/2},$$
where $L_G^{+/2}$ is the square root of the pseudoinverse (p. 260).
- Let $\Pi=L_G^{+/2}L_GL_G^{+/2}$, the projection onto range($L_G$). The text says $L_G$ is an ε-approximation of $L_H$ iff $L_G^{+/2}L_HL_G^{+/2}$ is an ε-approximation of $\Pi$ (p. 260).
- Expectation commutes with fixed linear maps (p. 260):
$$\mathbb E\,L_G^{+/2}L_HL_G^{+/2}=L_G^{+/2}(\mathbb E L_H)L_G^{+/2}=\Pi.$$
- It suffices to show the random matrix is probably close to Π. One may pretend Π = I, or project onto span(Π) (p. 260).

*Intuition note:* The transformation measures every error relative to $L_G$ itself. After that, the target is "close to the identity on the relevant subspace", so $\mu_{\min}=\mu_{\max}=1$.

### 32.5 The probabilities
- Define $X_{a,b}=(w_{a,b}/p_{a,b})L_G^{+/2}L_{(a,b)}L_G^{+/2}$ with probability $p_{a,b}$, and $0$ otherwise. Then $L_G^{+/2}L_HL_G^{+/2}=\sum_{(a,b)\in E}X_{a,b}$ (pp. 260–261).
- Choose
$$p_{a,b}\overset{\text{def}}{=}\frac1R\,w_{a,b}\big\|L_G^{+/2}L_{(a,b)}L_G^{+/2}\big\|,\quad R<1\text{ to be chosen}.$$
Then $\|X_{a,b}\|=R$ whenever the edge is chosen. Making this uniform optimises one part of Thm 32.3.1 (p. 261).
- Leverage score: $\ell_{a,b}=w_{a,b}(\delta_a-\delta_b)^TL_G^+(\delta_a-\delta_b)=w_{a,b}R_{\rm eff}(a,b)$ (p. 261).
- Norm computation (p. 261). The matrix is rank one, so its norm equals $v^Tv$ for $v=L_G^{+/2}(\delta_a-\delta_b)$ (added step):
$$\|L_G^{+/2}L_{(a,b)}L_G^{+/2}\|=\|(\delta_a-\delta_b)^TL_G^{+/2}L_G^{+/2}(\delta_a-\delta_b)\|=(\delta_a-\delta_b)^TL_G^+(\delta_a-\delta_b)=R_{\rm eff}(a,b).$$
Hence $p_{a,b}=\ell_{a,b}/R$. Effective resistances can be approximated quickly, so sufficient probabilities can be computed quickly (p. 261).
- Leverage scores sum to $n-1$. Reason 1: an edge's leverage score is the probability it lies in a random spanning tree, and each tree has $n-1$ edges (p. 261). Reason 2 (trace proof, p. 262):
$$\sum\ell_{a,b}=\sum w_{a,b}R_{\rm eff}(a,b)=\sum w_{a,b}(\delta_a-\delta_b)^TL_G^+(\delta_a-\delta_b)=\sum w_{a,b}\mathrm{Tr}\big(L_G^+(\delta_a-\delta_b)(\delta_a-\delta_b)^T\big)=\mathrm{Tr}\Big(L_G^+\sum w_{a,b}L_{a,b}\Big)=\mathrm{Tr}(L_G^+L_G)=\mathrm{Tr}(\Pi)=n-1.$$
- So $\sum p_{a,b}=(n-1)/R\le n/R$, the expected number of edges in $H$. A real-variable Chernoff bound makes exceeding a small multiple of this exponentially unlikely (p. 261).

*Intuition note:* The sampling probability of an edge is its leverage score (weight × effective resistance) divided by $R$, so edges with larger leverage score are kept with larger probability. The scores sum to $\mathrm{Tr}(\Pi)=n-1$, which is why the expected number of edges is $(n-1)/R$.

### 32.6 The analysis
- Choose $R=\epsilon^2/(3.5\ln n)$. Then $n/R=3.5\,n\ln n/\epsilon^2$, consistent with the target of at most $4n\ln n/\epsilon^2$ edges (p. 262; see Reading notes).
- $\sum\mathbb E X_{a,b}=\Pi$ (p. 262).
- Assume first that all $p_{a,b}\le1$. Upper tail (p. 262):
$$\Pr\Big[\sum X_{a,b}\succeq(1+\epsilon)\Pi\Big]\le n\exp(-\epsilon^2/3R)=n\exp(-(3.5/3)\ln n)=n^{-1/6}.$$
- Lower tail: work orthogonal to the all-ones vector, so the smallest relevant eigenvalue of Π is 1. The source then writes (p. 262)
$$\Pr\Big[\sum X_{a,b}\preceq(1-\epsilon)\Pi\Big]\le n\exp(-\epsilon^2/2R)=n\exp(-(3.5/2)\ln n)=n^{-3/2}.$$
(The printed value $n^{-3/2}$ is a misprint; see Reading notes.)
- Edges with $p_{a,b}\ge1$ (p. 263): either (i) include them in $H$ and drop them from the analysis, which needs a small adjustment to the Chernoff application; or (ii) split each such $X_{a,b}$ into $k=\lfloor\ell_{a,b}/R\rfloor$ independent copies appearing with probability 1, plus one copy with probability $\ell_{a,b}/R-k$. This keeps the expectation and the expected edge count, provided weights of repeated edges are added. The rest of the proof is unchanged.

### 32.7 Open problem
- Effective resistances can be estimated from a logarithmic number of random linear systems in $L_G$ ([SS11], better in [KLP12]) (p. 263).
- Sparsification does not need always-accurate estimates. It needs a way to identify many low-resistance edges without listing any high-resistance ones. The author believes better algorithms remain to be found (p. 263).
- Current fast algorithms rely on fast Laplacian solvers. A step away from them: [CGP+18, LSY18] decompose graphs into short cycles plus a few edges (p. 263).

## Toy example (ours)
Triangle on 3 vertices, unit weights. Each pair has resistance $1\,\|\,2$, so $R_{\rm eff}=\frac{1\cdot2}{1+2}=\frac23$. Then $\ell=\frac23$ per edge and $\sum\ell=3\cdot\frac23=2=n-1$ ✓.
Take $R=0.8$ (not the chapter's value; used for easy numbers). Then $p=\ell/R=\frac{2/3}{0.8}=\frac56$, kept weight $=1/p=1.2$.
- Expected edges $=3\cdot\frac56=2.5=(n-1)/R=2/0.8$ ✓.
- Expected weight per edge $=\frac56\cdot1.2=1$, so $\mathbb E L_H=L_G$ ✓.
- Norm check: $\|X\|=\ell/p=\frac{2/3}{5/6}=0.8=R$ ✓.
- One outcome: edge $(2,3)$ dropped, the others kept at weight 1.2. For $x=(1,0,0)$: $x^TL_Hx=1.2+1.2=2.4$ against $x^TL_Gx=2$, ratio 1.2. For $x=(0,1,-1)$: $2.4$ against $6$, ratio 0.4. A single sample on 3 vertices is a poor approximation. The Chernoff guarantee needs large $n$.

## Concepts
- [[graph-laplacian]] — $L_G=\sum w_{a,b}L_{a,b}$, sum of weighted elementary edge Laplacians (p. 259)
- [[positive-semidefinite-matrix]] — hypothesis on the summands in Thm 32.3.1 (p. 259)
- [[pseudoinverse]] — $L_G^{+/2}$ is the square root of $L_G^+$ (p. 260)
- [[projection]] — $\Pi=L_G^{+/2}L_GL_G^{+/2}$ projects onto range($L_G$) (p. 260)
- [[norm]] — the matrix norm bound $\|X_i\|\le R$ controls the Chernoff bound (p. 259)
- [[spectral-approximation]] (new) — ε-approximation: $(1-\epsilon)L_G\preceq L_H\preceq(1+\epsilon)L_G$ (p. 258)
- [[graph-sparsification]] (new) — approximating a graph by one with far fewer edges (p. 258)
- [[matrix-chernoff-bound]] (new) — tail bounds for extreme eigenvalues of sums of independent PSD matrices (p. 259)
- [[effective-resistance]] (new) — $R_{\rm eff}(a,b)=(\delta_a-\delta_b)^TL_G^+(\delta_a-\delta_b)$ (p. 261)
- [[leverage-score]] (new) — $\ell_{a,b}=w_{a,b}R_{\rm eff}(a,b)$; sums to $n-1$ (p. 261)
- [[importance-sampling-reweighting]] (new) — keep with probability $p$, weight by $1/p$, to preserve the expectation (p. 259)

## Canonical instances
- [[leverage-score-edge-sampling]] — the sparsification algorithm of this chapter (pp. 259–262)
- [[sum-of-leverage-scores-is-n-minus-1]] — trace proof $\mathrm{Tr}(\Pi)=n-1$ (p. 262)

## Bridges (candidates)
- [structural-analogy] Matrix Chernoff for $\sum X_i$ ↔ probability: Chernoff bounds for real variables; the text calls the matrix bounds analogs of these (p. 259).
- [structural-analogy] Reweighting by $1/p$ ↔ statistics: Horvitz–Thompson/importance weighting; the expectation is preserved.
- [same-math] Normalising by $L_G^{+/2}$ ↔ generalized eigenvalue problems: $A\preceq(1+\epsilon)B$ iff $B^{-1/2}AB^{-1/2}\preceq(1+\epsilon)I$.

## Questions this raises
- How can the $\log n$ factor be removed (promised in the next chapter)?
- How can all effective resistances be estimated quickly without Laplacian solvers (the open problem)?
- Why must a sparsifier keep high-leverage edges, and what happens with uniform sampling?
- Does the splitting trick for $p\ge1$ change the Chernoff constants?

## Reading notes
- Printed page = pdf − 24 (labels already give printed numbers).
- The text layer lost some symbols (ε, ≼, ≽). I read them from the page images.
- Misprint, p. 262: the number of edges is written "$4(\ln n)\epsilon^{-2}$" without the factor $n$. It should be $4n\ln n/\epsilon^2$, as on p. 259 and from $n/R$.
- Misprint, p. 262: $n\exp(-(3.5/2)\ln n)=n^{1-1.75}=n^{-3/4}$, not $n^{-3/2}$ as printed.
- Thm 32.3.1 has $0<\epsilon$ for the upper tail. The simplified $e^{-\epsilon^2/3}$ form is stated only for $0<\epsilon<1$ (p. 260).
- Section 32.4 says "$L_G$ is an ε-approximation of $L_H$" where the sense seems to be $L_H$ approximating $L_G$. With the definition on p. 258, the roles of $G$ and $H$ look swapped in that sentence.
- The unit has no exercises.
