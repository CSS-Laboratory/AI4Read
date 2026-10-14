---
id: spielman-2025-sagt/ch44-bipartite
work: spielman-2025-sagt
unit: "Chapter 44 — Bipartite Ramanujan Graphs"
pages: 349-356
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Bipartite Ramanujan Graphs

## L0 — One line
Every d-regular graph has a signed adjacency matrix whose smallest eigenvalue is at least −2√(d−1); this follows because the expected characteristic polynomial over random signings (the matching polynomial, whose zeros are at most 2√(d−1) in absolute value) is the root of a tree of interlacing polynomials, so some signing does at least as well.

## L1 — The gist (≤ 120 words)
The chapter asks whether bipartite Ramanujan graphs (d-regular graphs whose eigenvalues other than ±d have absolute value at most 2√(d−1)) exist for every degree d. The answer is yes, via 2-lifts (a graph doubled using a ±1 signing of its adjacency matrix). Averaging the characteristic polynomials ($\det(xI-M)$) of all signed adjacency matrices gives the matching polynomial, whose zeros are at most 2√(d−1) in absolute value. The polynomials with partly fixed signs form an interlacing family (polynomials whose zeros interleave), so one can walk down a binary tree without increasing the largest zero. This ends at one concrete signing. The method controls only the largest or smallest eigenvalue, so it does not give non-bipartite Ramanujan graphs.

**Prerequisites:** characteristic polynomial and determinant; symmetric matrices and eigenvalues; Courant–Fischer; rank-one updates; adjacency matrix of a graph; continuity of roots.

## L2 — Key ideas (5–10 bullets)
- A signed adjacency matrix S defines a 2-lift G^S whose eigenvalues are those of A together with those of S. A signing with $\|S\|\le2\sqrt{d-1}$ would therefore turn a Ramanujan graph into one on twice as many vertices (the Bilu–Linial plan, p. 350).
- Theorem 44.2.1: every d-regular G has a signing S with λ_min(S) ≥ −2√(d−1). For bipartite graphs, symmetry about 0 turns this into the full Ramanujan bound (p. 351).
- The expected characteristic polynomial over random signings is the matching polynomial. Its zeros are real with absolute value at most 2√(d−1) (p. 351).
- The smallest zero of an average of polynomials does not in general relate to the smallest zeros of the terms. Common interlacing makes it work (pp. 351–353).
- Lemma 44.5.2: if two polynomials have a common interlacing, one of them has largest zero at most that of their sum (p. 353).
- The polynomials with the first k signs fixed form a binary tree. Siblings have a common interlacing, so descending the tree never increases the largest zero (pp. 353–354).
- Real rootedness and interlacing come from rank-one updates (Lemma 44.5.1) and Obreschkoff's lemmas (pp. 352, 355–356).
- Interlacing controls only one extreme eigenvalue. This is why this chapter's techniques cannot prove existence of non-bipartite Ramanujan graphs, which the author calls the major open problem left by this work (p. 356).

## L3 — Walkthrough

### 44.1 Overview
- The first explicit Ramanujan families (Margulis; Lubotzky–Phillips–Sarnak) have degree p+1 for primes p. Other explicit constructions give degree q+1 for prime powers q. Over this lecture and the next, the author proves existence of bipartite Ramanujan graphs of every degree; today's proof does not give an explicit construction (p. 349).
- There is good reason to think that random d-regular graphs are Ramanujan [MNS08]. Friedman showed they are almost Ramanujan: a 2√(d−1)+ε approximation of the complete graph for large n, with high probability, for every ε>0 (p. 349).
- The chapter uses interlacing families to prove (half) a conjecture of Bilu and Linial. The theorem comes from [MSS15b]; today's proof is informed by the techniques of [HPS15] (p. 349).
- **Definition.** A d-regular graph is *bipartite Ramanujan* if all adjacency eigenvalues other than d and −d have absolute value at most 2√(d−1) (p. 349). The eigenvalue d comes from d-regularity and −d from bipartiteness (p. 349).
- Claim 44.1.1: a symmetric matrix $\begin{pmatrix}0&A\\A^T&0\end{pmatrix}$ has eigenvalues symmetric about the origin. The author leaves the proof to the reader (p. 350).
- Double covers of Ramanujan graphs are bipartite Ramanujan. No way is known to go from bipartite to ordinary Ramanujan graphs (p. 350).
- Notation: $\chi_x(M)\stackrel{def}{=}\det(xI-M)$ (p. 350).

### 44.2 2-Lifts
- A *signed adjacency matrix* S is symmetric with the same nonzero pattern as A, and every nonzero entry is ±1 (p. 350).
- G^S has two vertices $u_1,u_2$ per vertex u. For an edge (u,v) with S(u,v)=−1 it has edges $(u_1,v_2),(v_1,u_2)$. With S(u,v)=1 it has $(u_1,v_1),(u_2,v_2)$. Then $G^{-A}$ is the double cover and $G^{A}$ is two disjoint copies of G (p. 350).
- Problem Set 2 (Problem 3) asks to prove that the spectrum of G^S is the union of the spectra of A and S (p. 350).
- **Bilu–Linial conjecture:** every d-regular G has a signing with $\|S\|\le 2\sqrt{d-1}$. Starting from $K_{d+1}$, repeated lifting would then give infinite Ramanujan families (p. 350).
- **Theorem 44.2.1.** Every d-regular G has a signing S whose minimum eigenvalue is at least $-2\sqrt{d-1}$ (p. 351).
- For bipartite G, the lift is bipartite and its spectrum is symmetric. So $\mu_n\ge-2\sqrt{d-1}$ gives $|\mu_i|\le 2\sqrt{d-1}$ for $1<i<n$ (p. 351).

*Intuition note.* Only one side of the spectrum needs controlling. In a bipartite graph the other side comes free from symmetry.

### 44.3 Random 2-Lifts
- Consider $\mathbb{E}_S[\chi_x(S)]$ (44.1) for a uniformly random signing. Godsil–Gutman: it equals the matching polynomial of G (p. 351).
- **Theorem 44.3.1** (Heilmann–Lieb). For maximum degree at most d, the zeros of the matching polynomial are real with absolute value at most $2\sqrt{d-1}$ (p. 351).
- The difficulty: the smallest zero of an average of polynomials need not relate to the smallest zeros of the terms. The chapter shows it does here (p. 351).

### 44.4 Laplacianized Polynomials
- It suffices to find S with $\lambda_{\max}(dI-S)\le d+2\sqrt{d-1}$ (p. 351). (Added step: eigenvalues of $dI-S$ are $d-\mu_i$, so this is the same as $\mu_n\ge-2\sqrt{d-1}$.)
- Order the m edges and encode S by $\sigma\in\{\pm1\}^m$. Let $p_\sigma(x)=\chi_x(dI-S)$ (p. 351).
- For the i-th edge (a,b): $v_{i,\sigma_i}=\delta_a-\sigma_i\delta_b$ (p. 351). Then $\sum_{i=1}^m v_{i,\sigma_i}v_{i,\sigma_i}^T=dI-S$, so $p_\sigma(x)=\chi_x\big(\sum_i v_{i,\sigma_i}v_{i,\sigma_i}^T\big)$ (p. 352). (Added step: the author does not show this sum. Expanding $vv^T$ for each edge gives the degree matrix minus S, and the degree matrix is $dI$ because G is d-regular.)

### 44.5 Interlacing Families of Polynomials
- Goal: from real-rooted $p_1,\dots,p_m$ with real-rooted sum, find some $p_i$ with $\lambda_{\max}(p_i)\le\lambda_{\max}$(sum). This is false in general (p. 352).
- **Definitions.** For $p=\prod_{i=1}^n(x-\lambda_i)$ and $q=\prod_{i=1}^{n-1}(x-\mu_i)$, q *interlaces* p if $\lambda_n\le\mu_{n-1}\le\lambda_{n-1}\le\cdots\le\lambda_2\le\mu_1\le\lambda_1$. For r of degree n with roots $\mu_i$, write $r\to p$ if $\mu_n\le\lambda_n\le\mu_{n-1}\le\cdots\le\mu_1\le\lambda_1$. Positive multiples are allowed (p. 352).
- **Lemma 44.5.1.** Let A be symmetric and $p_t(x)=\chi_x(A+tvv^T)$. For t>0, $p_0\to p_t$ (by Courant–Fischer). There is a monic degree n−1 polynomial q with $p_t=\chi_x(A)-tq(x)$ for all t (p. 352).
  - *Proof for $v=\delta_1$.* The determinant is linear in each entry, so $\det(xI-A-t\delta_1\delta_1^T)=\det(xI-A)-t\det(xI^{(1)}-A^{(1)})=\chi_x(A)-t\chi_x(A^{(1)})$. Here $A^{(1)}$ deletes row and column 1, and $q=\chi_x(A^{(1)})$ (pp. 352–353).
  - *General v.* Take a rotation Q with $Qv=\delta_1$. Characteristic polynomials are unchanged by $M\mapsto QMQ^T$, so $\chi_x(A+tvv^T)=\chi_x(QAQ^T+t\delta_1\delta_1^T)=\chi_x(QAQ^T)-tq=\chi_x(A)-tq$ (p. 353).
- **Lemma 44.5.2.** If $r\to p_1$ and $r\to p_2$, then $r\to p_1+p_2$ and some i has $\lambda_{\max}(p_i)\le\lambda_{\max}(p_1+p_2)$ (p. 353).
  - *Proof.* Let $\mu_1$ be the largest zero of r. Each $p_i$ is eventually positive and has exactly one zero at least $\mu_1$, so it is nonpositive at $\mu_1$. The same holds for the sum, so its largest zero λ satisfies $\lambda\ge\mu_1$. If some $p_i(\lambda)=0$ we are done. Otherwise some $p_i(\lambda)>0$. Since $p_i$ has one zero above $\mu_1$ and is eventually positive, its largest zero is below λ (p. 353).
  - It extends to any number of polynomials with a *common interlacing* (p. 353).
- The $p_\sigma$ have no common interlacing, but form an *interlacing family* (special case only). For $\sigma\in\{\pm1\}^k$, $k<m$, define $p_\sigma=\mathbb{E}_\rho[p_{\sigma,\rho}]$ over the remaining signs, so $p_\emptyset=\mathbb{E}_\sigma[p_\sigma]$. These sit in a complete binary tree: root ∅, leaves of length m, children $(\sigma,1),(\sigma,-1)$ called siblings (p. 353). The text writes n for m in places.
- **Lemma 44.5.3.** Some leaf σ has $\lambda_{\max}(p_\sigma)\le\lambda_{\max}(p_\emptyset)$ (p. 354).
  - *Proof.* By Corollary 44.6.2 and Lemma 44.5.2, every non-leaf has a child whose largest zero is at most the node's. Descend from the root along such children (p. 354).
- With Theorem 44.3.1, $\lambda_{\max}(p_\emptyset)\le d+2\sqrt{d-1}$, so Theorem 44.2.1 follows (p. 354).

*Intuition note.* In general nothing relates the largest zero of an average to those of its terms, but with a common interlacing some term has largest zero no larger than the average's. At each tree split the better child is at least as good as the parent. Repeating this down the tree fixes all signs.

### 44.6 Common Interlacings
- Base case: for $\sigma\in\{\pm1\}^{m-1}$ let $A=\sum_{i<m}v_{i,\sigma_i}v_{i,\sigma_i}^T$. The children are $\chi_x(A+v_{m,s}v_{m,s}^T)$. Lemma 44.5.1 gives $\chi_x(A)\to$ each, and Lemma 44.5.2 gives an s with $\lambda_{\max}(p_{\sigma,s})\le\lambda_{\max}(p_\sigma)$ (p. 354).
- **Lemma 44.6.1.** For symmetric A and vectors $w_{i,s}$ ($1\le i\le k$, $s\in\{0,1\}$), the polynomial $\sum_{\rho\in\{0,1\}^k}\chi_x\big(A+\sum_{i=1}^k w_{i,\rho_i}w_{i,\rho_i}^T\big)$ is real rooted. For each s, $\sum_{\rho\in\{0,1\}^{k}}\chi_x\big(A+\sum_{i=1}^{k-1}w_{i,\rho_i}w_{i,\rho_i}^T\big)\to\sum_{\rho\in\{0,1\}^k}\chi_x\big(A+\sum_{i=1}^{k-1}w_{i,\rho_i}w_{i,\rho_i}^T+w_{k,s}w_{k,s}^T\big)$ (p. 354).
- **Corollary 44.6.2.** The sibling polynomials $p_{\sigma,s}$, $s=\pm1$, are real rooted with a common interlacing (p. 354).

### 44.7 Real Rootedness (Obreschkoff)
- **Lemma 44.7.1.** If $p$ (degree n) and $q$ (degree n−1) are such that $p_t=p-tq$ is real rooted for all real t, then q interlaces p (p. 355).
  - *Sketch (distinct roots).* Roots depend continuously on t. Suppose two consecutive roots $\lambda_{i+1},\lambda_i$ of p have no root of q between them, and p, q are positive there. For small t>0, $p_t$ is negative at both endpoints but positive somewhere inside, so it has two roots in the interval. For large t it is negative on the whole interval, with no roots. The two roots cannot cross the endpoints, so they must become complex, a contradiction (p. 355).
- **Lemma 44.7.2.** If p, q interlace and have positive leading coefficients, then for t>0, $p-tq$ is real rooted and $p\to p-tq$ (p. 355).
  - *Sketch.* $p_t(\lambda_1)<0$, so $p_t$ has a root above $\lambda_1$. Sign changes at the $\lambda_i$ give a root in each $(\lambda_{i+1},\lambda_i)$. That accounts for all roots (p. 355). The text writes d for the degree and says "monic" here.
- **Lemma 44.7.3.** If $p_0,p_1$ are monic of degree n with $r\to p_0$ and $r\to p_1$, then $r\to\frac12p_0+\frac12p_1$, and the average is real rooted (pp. 355–356).
  - *Sketch (distinct roots).* Both are negative at odd-indexed roots $\mu_i$ of r and positive at even ones, so the average is too. This gives at least n−1 real roots between $\mu_n$ and $\mu_1$. The average is monic, so it has one more root above $\mu_1$ (p. 356).
- **Proof of Lemma 44.6.1** (induction on k). Take any u and real t. Let $p_t=\sum_\rho\chi_x(A+\sum_{i<k}w_{i,\rho_i}w_{i,\rho_i}^T+tuu^T)$. By Lemma 44.5.1, $p_t=p_0-tq$ with q of degree n−1 and positive leading coefficient. Absorbing $tuu^T$ into A, induction shows $p_t$ is real rooted for all t. Lemma 44.7.1 gives that q interlaces $p_0$. Lemma 44.7.2 gives $p_0\to p_t$ for t>0. (Added step: taking $u=w_{k,s}$ and $t=1$ gives the arrow statement for each s.) Lemma 44.7.3 then gives the arrow to the full sum and its real rootedness (p. 356).

### 44.8 Conclusion
Existence of regular non-bipartite Ramanujan graphs is the major open problem left. Interlacing reasons only about the largest or the smallest eigenvalue, not both (p. 356).

## Toy example (ours)
Take $r(x)=(x-1)(x+1)$, $p_1=x(x-2)=x^2-2x$, $p_2=(x-4)(x+1)=x^2-3x-4$.
- Interlacing: $p_1$ has roots 2, 0 and $-1\le0\le1\le2$. $p_2$ has roots 4, −1 and $-1\le-1\le1\le4$. So $r\to p_1$ and $r\to p_2$.
- Average: $\tfrac12(p_1+p_2)=x^2-2.5x-2$, with roots $(2.5\pm\sqrt{14.25})/2$. The largest is about 3.14.
- Check at the roots of r: the average is $1-2.5-2=-3.5\le0$ at $x=1$ and $1+2.5-2=1.5\ge0$ at $x=-1$. This is the sign pattern in Lemma 44.7.3.
- Lemma 44.5.2: $\lambda_{\max}(p_1)=2\le3.14$, so $i=1$ works. $\lambda_{\max}(p_2)=4>3.14$, so not every child works. This is why the walk picks the good child at each step.

## Concepts
- [[characteristic polynomial]] — $\chi_x(M)=\det(xI-M)$; the chapter works with it instead of eigenvalues directly (p. 350)
- [[adjacency matrix]] — A of G; its spectrum is related to that of S through the 2-lift (p. 350)
- [[ramanujan-graph]] (new) — a graph whose adjacency spectrum approximates that of the complete graph (the text does not formally define this ordinary version); the bipartite version requires all eigenvalues other than ±d to have absolute value at most 2√(d−1) (p. 349)
- [[signed-adjacency-matrix]] (new) — symmetric ±1 matrix with the nonzero pattern of A (p. 350)
- [[two-lift]] (new) — graph $G^S$; spectrum is that of A together with that of S (p. 350)
- [[matching-polynomial]] (new) — equals $\mathbb{E}_S\chi_x(S)$ (Godsil–Gutman); zeros bounded by Heilmann–Lieb (p. 351)
- [[interlacing-polynomials]] (new) — q interlaces p, and $r\to p$; the key tool (p. 352)
- [[interlacing-family]] (new) — polynomials indexed by a binary tree whose siblings have common interlacings (special case used here; the text gives no general definition) (p. 353)
- [[common-interlacing]] (new) — one r with $r\to p_i$ for all i (p. 353)
- [[real-rooted-polynomial]] (new) — all zeros real (p. 352)

## Canonical instances
- [[complete-graph-start-of-lifting]] — $K_{d+1}$ as the starting Ramanujan graph for repeated lifting (p. 350)
- [[double-cover]] — $G^{-A}$; $G^{A}$ is two copies of G (p. 350)

## Bridges (candidates)
- [structural-analogy] Descending the interlacing tree ↔ derandomization: the method of conditional expectations; fix one random bit at a time without worsening the quantity.
- [same-math] Lemma 44.5.1 rank-one update $\chi_x(A+tvv^T)=\chi_x(A)-tq$ ↔ linear algebra: determinant linearity in one entry plus rotation invariance.
- [structural-analogy] Interlacing of roots under rank-one perturbation ↔ Cauchy interlacing / Courant–Fischer (cited in the proof, p. 352).

## Questions this raises
- Why is the expected characteristic polynomial equal to the matching polynomial, and why are its zeros bounded by 2√(d−1)?
- Why does interlacing control only one extreme eigenvalue, and what would be needed to control both?
- How does the general definition of an interlacing family differ from the special case used here?

## Exercises worth doing
- Claim 44.1.1 (p. 350) — prove the spectrum of $\begin{pmatrix}0&A\\A^T&0\end{pmatrix}$ is symmetric about 0 — easy
- Problem 3, Problem Set 2 (p. 350) — spectrum of $G^S$ is spec(A) ∪ spec(S) — medium

## Reading notes
- Printed = pdf − 24. Pages 349–356 were read, with images checked for pp. 350–356.
- Misprints in the source: p. 353 says "ρ∈{±1}^{n−k}" and "length less than n" where m is meant; Cor. 44.6.2 says "k<n" (m intended); Lemma 44.7.2's sketch says d and "monic" where n and positive leading coefficient are meant; Lemma 44.6.1 uses {0,1} but its proof uses {±1}.
- Several proofs are labelled sketches and assume distinct roots.
