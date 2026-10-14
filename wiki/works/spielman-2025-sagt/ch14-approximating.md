---
id: spielman-2025-sagt/ch14-approximating
work: spielman-2025-sagt
unit: "Chapter 14 — Approximating Effective Resistances"
pages: 129–133
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
# Approximating Effective Resistances

## L0 — One line
Effective resistances are squared Euclidean distances, so, with high probability, a random Gaussian projection to $d=8\ln(n^2/\delta)/\epsilon^2$ dimensions preserves all of them up to a factor $1\pm\epsilon$, and the projected vectors can be computed approximately with only Laplacian solves.

## L1 — The gist (≤ 120 words)
The chapter asks how to store or compute all $\binom n2$ effective resistances of a connected weighted graph cheaply. Effective resistance equals a squared distance between the vectors $L^{+/2}\delta_a$. The Johnson–Lindenstrauss Lemma (JL) says a random Gaussian matrix with $d=O(\log n)$ rows keeps all pairwise squared distances within $1\pm\epsilon$, with high probability. Any $M$ with $M^TM=L^+$ works in place of $L^{+/2}$. Using $M=W^{1/2}UL^+$ means we need only $d$ Laplacian solves. The proof uses Gaussian facts, a $\chi^2$ tail bound, and a union bound over pairs.

**Prerequisites:** pseudoinverse and Laplacian $L=U^TWU$; Euclidean norm; Gaussian variables (mean, variance); union bound; matrix shapes.

## L2 — Key ideas
- $\mathrm{R}_{\rm eff}(a,b)=\|L^{+/2}\delta_a-L^{+/2}\delta_b\|^2$, so effective resistances are squared Euclidean distances between the points $L^{+/2}\delta_a$ (p. 129).
- JL (Thm 14.1.1): a $d\times k$ matrix $R$ of i.i.d. $\mathcal N(0,1/d)$ entries, with $d=8\ln(n^2/\delta)/\epsilon^2$, preserves all pairwise squared distances within $1\pm\epsilon$ with probability $\ge1-\delta$ (p. 130).
- Storing the $y_a$ replaces $\binom n2$ numbers by a table of size about $nd$ (the source prints "?nd") (p. 130).
- Any $M$ with $M^TM=L^+$ suffices. With $M=W^{1/2}UL^+$, computing needs $d$ Laplacian solves (p. 131).
- A sum of independent Gaussians is Gaussian with the variances added, so each entry of $Rx$ is $\mathcal N(0,\sigma^2\|x\|^2)$ (pp. 131–132).
- A sum $X$ of $d$ squared independent standard Gaussians (a $\chi^2$ variable) has mean $d$ and is very unlikely to deviate much; for $\epsilon<1$, $\Pr[|X-d|\ge\epsilon d]\le2e^{-\epsilon^2d/8}$ (p. 132).
- The proof: the single-pair failure probability is $\le2\delta/n^2$, and the union bound over $\binom n2$ pairs gives $<\delta$ (p. 133).

## L3 — Walkthrough

### 14.1 Representing effective resistances
Goal: a data structure that quickly estimates $\mathrm{R}_{\rm eff}(a,b)$ for all pairs (p. 129). Using Section 12.1:
$$\mathrm{R}_{\rm eff}(a,b)=(\delta_a-\delta_b)^TL^+(\delta_a-\delta_b)=\|L^{+/2}(\delta_a-\delta_b)\|^2=\|L^{+/2}\delta_a-L^{+/2}\delta_b\|^2=\mathrm{dist}(L^{+/2}\delta_a,L^{+/2}\delta_b)^2 .$$
**Matrix norm.** For positive semidefinite $A$: $\|x\|_A=\sqrt{x^TAx}=\|A^{1/2}x\|$. It is a norm: it is zero at $x=0$, it is symmetric, and for $z=x+y$,
$\|z\|_A=\|A^{1/2}(x+y)\|\le\|A^{1/2}x\|+\|A^{1/2}y\|=\|x\|_A+\|y\|_A$ (p. 129).

**JL lemma.** Every Euclidean metric on $n$ points is well approximated by one in $O(\log n)$ dimensions, whatever the original dimension. Johnson and Lindenstrauss used a random orthogonal projection. The chapter analyzes a Gaussian matrix instead, which is simpler (p. 130). Gaussian facts used: density $p(x)=\frac1{\sqrt{2\pi}}e^{-x^2/2}$ for variance 1, and $\frac1{\sqrt{2\pi}\sigma}e^{-x^2/2\sigma^2}$ for variance $\sigma^2$. $\mathcal N(0,\sigma^2)$ is $\sigma$ times $\mathcal N(0,1)$ (p. 130).

**Theorem 14.1.1.** Let $x_1,\dots,x_n\in\mathbb R^k$ and $\epsilon,\delta>0$. Let $d=8\ln(n^2/\delta)/\epsilon^2$. If $R$ is $d\times k$ with i.i.d. $\mathcal N(0,1/d)$ entries, then with probability $\ge1-\delta$, for all $a\ne b$,
$$(1-\epsilon)\,\mathrm{dist}(x_a,x_b)^2\le\mathrm{dist}(Rx_a,Rx_b)^2\le(1+\epsilon)\,\mathrm{dist}(x_a,x_b)^2 .$$
Application: take $x_a=L^{+/2}\delta_a$, so $k=n$ and $R$ is $d\times n$. Set $y_a=RL^{+/2}\delta_a$. With probability $\ge1-\delta$, $\mathrm{R}_{\rm eff}(a,b)$ is within a $1\pm\epsilon$ factor of $\mathrm{dist}(y_a,y_b)^2$ for all $a,b$. Writing all resistances needs $\binom n2$ numbers; storing $y_1,\dots,y_n$ needs "?nd" (p. 130). The 8 can be replaced by a constant tending to 4 as $\epsilon\to0$ (p. 130).

*Intuition note:* Resistances are squared distances between $n$ points. With high probability, random Gaussian projection keeps all these squared distances within a factor $1\pm\epsilon$ while the dimension falls to order $\log n$. Each node then stores a short vector instead of $n$ resistances.

### 14.2 Computing effective resistances
The naive way solves one Laplacian system per pair. The chapter shows how to approximate all pairs with a logarithmic number of solves (p. 130). Multiplying by $L^{+/2}$ quickly would suffice; Cheng–Cheng–Liu–Peng–Teng show this is possible in nearly-linear time. The chapter instead gives a more elementary route needing only Laplacian solves (p. 131).

Key: any $M$ with $M^TM=L^+$ will suffice. Write $L=U^TWU$, with $U$ the signed edge–vertex adjacency matrix and $W$ the diagonal matrix of edge weights. Then
$$L^+U^TW^{1/2}W^{1/2}UL^+=L^+LL^+=L^+,\qquad\text{so}\qquad \|W^{1/2}UL^+(\delta_a-\delta_b)\|^2=\mathrm{R}_{\rm eff}(a,b).$$
Let $R$ be $d\times m$ with i.i.d. $\mathcal N(0,1/d)$ entries. Compute $RW^{1/2}UL^+=(RW^{1/2}U)L^+$. This takes $d$ multiplications of vectors in $\mathbb R^m$ by $W^{1/2}U$, and $d$ solves in $L$. Set $y_a=(RW^{1/2}U)L^+\delta_a\in\mathbb R^d$. With high probability $\|y_a-y_b\|^2$ approximates $\mathrm{R}_{\rm eff}(a,b)$ (p. 131).

Shapes (added step): $R$: $d\times m$; $W^{1/2}$: $m\times m$; $U$: $m\times n$; $L^+$: $n\times n$; $\delta_a$: $n\times1$. The points $x_a=W^{1/2}UL^+\delta_a$ lie in $\mathbb R^m$, so Theorem 14.1.1 applies with $k=m$. The text states only "with high probability".

*Intuition note:* We never need the square root of $L^+$. Any "square root" in the sense $M^TM=L^+$ gives the same squared distances. The choice $W^{1/2}UL^+$ turns the work into $d$ Laplacian solves.

### 14.3 Properties of Gaussian random variables
**Claim 14.3.1.** If $r_1,\dots,r_n$ are independent Gaussians of variances $\sigma_i^2$, then $\sum r_i$ is Gaussian of variance $\sum\sigma_i^2$. The variance rule is the familiar one; the claim adds that the sum is Gaussian (p. 131). Hence for a fixed vector $x$ and $r$ with i.i.d. $\mathcal N(0,1)$ entries, $x^Tr=\sum x(i)r(i)$ is Gaussian of variance $\|x\|^2$ (p. 131).

If $R$ has i.i.d. $\mathcal N(0,\sigma^2)$ entries, each entry of $Rx$ is $\mathcal N(0,\sigma^2\|x\|^2)$. The entries are independent because they come from different rows of $R$ (p. 132).

The norm of a vector of i.i.d. $\mathcal N(0,1)$ variables is a $\chi$ variable; its square is a $\chi^2$ variable. In dimension $d$ the expectation is $d$, and large deviations are very unlikely (p. 132).

**Lemma 14.3.2** (Lemma 1 of [LM00]). For independent $\mathcal N(0,1)$ variables $r_1,\dots,r_d$, with $X=\sum_ir_i^2$ and all $t>0$:
$$\Pr\big[X\ge d+2\sqrt{dt}+2t\big]\le e^{-t},\qquad \Pr\big[X\le d-2\sqrt{dt}\big]\le e^{-t}.$$

**Corollary 14.3.3.** For $\epsilon<1$: $\Pr[|X-d|\ge\epsilon d]\le2\exp(-\epsilon^2d/8)$.
*Proof.* Set $t=\epsilon^2d/8$. Then
$$2\sqrt{dt}+2t\le2\frac{\epsilon d}{\sqrt8}+\frac{\epsilon^2d}{4}\le2\frac{\epsilon d}{\sqrt8}+\frac{\epsilon d}{4}<\epsilon d .$$
The probability that $X-d>\epsilon d$ or $X-d<-\epsilon d$ is at most the sum of the two lemma probabilities, so at most $2e^{-t}$ (p. 132).

Remark: for small $\epsilon$ the term $2\epsilon d/\sqrt8$ dominates, and the bound $\epsilon d$ approaches $\epsilon d/\sqrt2$. Pushing this through the proof, a dimension a little over $4\ln(n^2/\delta)/\epsilon^2$ suffices instead of $8\ln(n^2/\delta)/\epsilon^2$ (p. 132).

*Intuition note:* A sum of $d$ squared standard Gaussians sits near $d$. The chance of missing by a fraction $\epsilon$ falls exponentially in $\epsilon^2d$. This is why $d$ only needs to grow like $\log n$.

### 14.4 Proof of Theorem 14.1.1
Fix $a,b$ and let $\Delta=\|x_a-x_b\|^2$. $R(x_a-x_b)$ is a $d$-dimensional vector of $\mathcal N(0,\sigma^2)$ entries with $\sigma^2=\Delta/d$. By Corollary 14.3.3 (p. 132):
$$\Pr\big[|\,\mathrm{dist}(Rx_a,Rx_b)^2-\mathrm{dist}(x_a,x_b)^2|>\epsilon\,\mathrm{dist}(x_a,x_b)^2\big]=\Pr\big[|\|R(x_a-x_b)\|^2-\Delta|\ge\epsilon\Delta\big]\le2e^{-\epsilon^2d/8}.$$
(Added step: $\|R(x_a-x_b)\|^2=(\Delta/d)X$ with $X$ a $\chi^2_d$ variable, so the event is $|X-d|\ge\epsilon d$.)

With $d=8\ln(n^2/\delta)/\epsilon^2$: $2e^{-\epsilon^2d/8}=2e^{-\ln(n^2/\delta)}=2\delta/n^2$. There are $\binom n2$ pairs, so the probability that some pair has $\|R(x_a-x_b)\|^2\notin(1\pm\epsilon)\|x_a-x_b\|^2$ is at most $\binom n2\frac{2\delta}{n^2}<\delta$ (p. 133). $\square$

*Intuition note:* Each pair fails with tiny probability, and the factor $n^2$ inside the logarithm pays for the union bound over pairs. That is why $\ln(n^2/\delta)$ appears in $d$.

## Toy example (ours)
Triangle graph, unit weights ($W=I$). $L^+=\tfrac13(I-J/3)$, where $J$ is the all-ones matrix. For adjacent $a=1$, $b=2$: $\delta_1-\delta_2=(1,-1,0)$ has zero sum, so $L^+(\delta_1-\delta_2)=\tfrac13(1,-1,0)$. Then $\mathrm{R}_{\rm eff}(1,2)=\tfrac13\cdot2=\tfrac23$.

Edges are $(1,2),(2,3),(1,3)$, so $U$ has rows $(1,-1,0),(0,1,-1),(1,0,-1)$. Then $z=W^{1/2}UL^+(\delta_1-\delta_2)=\tfrac13(2,-1,1)$, and $\|z\|^2=\tfrac{4+1+1}{9}=\tfrac23$ ✓.

Take $d=2$, $R=\tfrac1{\sqrt2}\begin{pmatrix}1&0&1\\1&-1&0\end{pmatrix}$ (an arbitrary choice, not random). $Rz$ has entries $\tfrac1{\sqrt2}\cdot\tfrac13(2+1)=\tfrac1{\sqrt2}$ and $\tfrac1{\sqrt2}\cdot\tfrac13(2+1)=\tfrac1{\sqrt2}$. So $\|Rz\|^2=\tfrac12+\tfrac12=1$ versus the true $\tfrac23$, a ratio of 1.5. With so few rows the estimate is rough. By Section 14.3 each entry of $Rz$ is $\mathcal N(0,\|z\|^2/d)$, so $\mathbb E\|Rz\|^2=\|z\|^2=\tfrac23$. For $n=3$, $\epsilon=0.5$, $\delta=0.1$, the theorem needs $d=8\ln(90)/0.25\approx144$.

## Concepts
- [[effective-resistance]] (new) — $\mathrm{R}_{\rm eff}(a,b)=(\delta_a-\delta_b)^TL^+(\delta_a-\delta_b)$, a squared Euclidean distance (p. 129)
- [[norm]] — here the matrix norm $\|x\|_A=\sqrt{x^TAx}=\|A^{1/2}x\|$ for PSD $A$ (p. 129)
- [[pseudoinverse]] — $L^+$, whose square root or any factor $M$ with $M^TM=L^+$ gives the distances (pp. 129, 131)
- [[graph Laplacian]] — $L=U^TWU$, with $U$ the signed edge–vertex matrix and $W$ the edge weights (p. 131)
- [[incidence matrix]] — the author's $U$ (signed edge–vertex adjacency matrix), $m\times n$ (p. 131)
- [[johnson-lindenstrauss-lemma]] (new) — random projection to $O(\log n)$ dimensions preserves, with high probability, all pairwise squared distances up to $1\pm\epsilon$ (p. 130)
- [[gaussian-random-matrix]] (new) — matrix of i.i.d. $\mathcal N(0,1/d)$ entries; $Rx$ has independent $\mathcal N(0,\|x\|^2/d)$ entries (p. 132)
- [[chi-squared-concentration]] (new) — for $\epsilon<1$, $\sum r_i^2$ (independent $\mathcal N(0,1)$ terms) stays within $\epsilon d$ of $d$ except with probability $\le2e^{-\epsilon^2d/8}$ (p. 132)
- [[union-bound]] (new) — failure over all $\binom n2$ pairs is at most the sum of the single-pair failures (p. 133)

## Canonical instances
- [[reff-as-squared-distance]] — resistance as distance between $L^{+/2}\delta_a$ and $L^{+/2}\delta_b$ (p. 129)
- [[jl-sketch-of-reff]] — $y_a=(RW^{1/2}U)L^+\delta_a$, $d$ Laplacian solves (p. 131)

## Bridges (candidates)
- [structural-analogy] $y_a$ = short random embedding of nodes ↔ randomized sketching in numerical linear algebra: a random matrix compresses data while preserving geometry.
- [structural-analogy] Reff as distance between $L^{+/2}\delta_a$ vectors ↔ spectral embeddings of graphs: both place nodes as vectors built from the Laplacian.
- [same-math] "Any $M$ with $M^TM=L^+$" ↔ factorizations of a PSD matrix: only the Gram matrix matters, not which factor is used.

## Questions this raises
- What does a Laplacian solve cost, and how does that set the total running time (the text defers to "Chapter ??")?
- Can Gaussian projection be replaced by other random matrices or a deterministic one?
- How tight is $d\approx4\ln(n^2/\delta)/\epsilon^2$ for $\epsilon\to0$?
- For small graphs, is the bound even useful? (In our toy, $d\approx144>n$.)

## Reading notes
- Printed = pdf − 24. Printed page numbers are visible on every page.
- Misprints and gaps seen in the images: "storing $y_1,\dots,y_n$ only requires ?nd" (the size is left as "?"); "Chapter ??" is an unresolved cross-reference; "dimension dimension" (p. 132); "The sum a Gaussian" (p. 131).
- The statement of Theorem 14.1.1 has an unbalanced bracket in "$8(\ln(n^2/\delta)/\epsilon^2$". I read it as $8\ln(n^2/\delta)/\epsilon^2$, as the proof confirms (p. 133).
- The proof's phrase "Each entry of $R(x_a-x_b)$ is a $d$-dimensional vector" is loosely worded. $R(x_a-x_b)$ itself is the $d$-vector.
- The chapter has no exercises. The work's citation calls the source an incomplete draft; the unresolved "Chapter ??" is consistent with that. Theorem 14.1.1 is stated for any $\epsilon>0$, but Corollary 14.3.3, used in its proof, assumes $\epsilon<1$; the text does not comment on this (pp. 130, 132).
