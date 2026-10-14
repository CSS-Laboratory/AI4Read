---
id: spielman-2025-sagt/ch41-expected
work: spielman-2025-sagt
unit: Chapter 41 — Expected Characteristic Polynomials
pages: 326–332
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
# Expected Characteristic Polynomials

## L0 — One line
The average of $\chi_x(A+\Pi B\Pi^T)$ over a uniformly random permutation $\Pi$ is real rooted (all its roots are real), because a uniform random permutation can be built from random swaps and interlacing shows that each random swap preserves real-rootedness.

## L1 — The gist (≤ 120 words)
Goal: show that the expected characteristic polynomial of a sum of randomly permuted symmetric matrices has only real roots. The chapter sits inside a proof that infinite families of bipartite Ramanujan graphs exist. A sum of real-rooted polynomials (all roots real) need not be real rooted, so something special is needed. The tool is interlacing (roots alternate), which is tied to real-rootedness of the combinations $p-tq$ (Obreschkoff). A swap of two coordinates changes $A$ by a rank-two correction $-uu^T+vv^T$. Averaging over such a swap preserves real-rootedness (under a suitable hypothesis). A uniform random permutation can be assembled from random swaps with suitable probabilities, which gives the result.

**Prerequisites:** characteristic polynomial; symmetric matrices and Courant–Fischer; permutation matrices; roots depend continuously on coefficients; rank and trace.

## L2 — Key ideas (5–10 bullets)
- Random $d$-regular-type graphs are built as sums of $d$ random perfect matchings $\Pi_iM\Pi_i^T$. The chapter studies the expected characteristic polynomial of such sums (pp. 326–327).
- Main claim (Thm 41.2.1): $\mathbb E_\Pi\,\chi_x(A+\Pi B\Pi^T)$ is real rooted for symmetric $A,B$. This is not automatic, since real-rooted polynomials can sum to one with no real roots (p. 327).
- Interlacing (roots alternate) is the key tool. Obreschkoff's theorem has two halves: if $p,q$ interlace (positive leading coefficients), then $p-tq$ is real rooted for $t>0$; conversely, if $p-tq$ is real rooted for all real $t$, then $p,q$ interlace (pp. 327–328).
- Rank-one updates $A+tvv^T$ give $\chi_x(A)-tq(x)$ with $q$ of degree $n-1$ (Lemma 41.3.3, p. 329).
- If monic degree-$n$ polynomials satisfy $p_0\to r$ and $p_1\to r$, every convex combination of $p_0,p_1$ is real rooted (Lemma 41.3.4, p. 329).
- A swap acts as $\Gamma A\Gamma = A-uu^T+vv^T$, so, if the weighted sums are real rooted for all symmetric $A,B$, averaging over a swap keeps them real rooted (Lemmas 41.4.1–41.4.2, Cor. 41.4.3, pp. 330–331).
- A uniform random permutation is a product of random swaps with probabilities other than 1/2 (Lemma 41.5.2, p. 332).

## L3 — Walkthrough

### 41.1–41.2 Setting and goal
The chapter belongs to a proof that infinite families of bipartite Ramanujan graphs exist. At present these techniques are not known to prove that non-bipartite ones exist (p. 326). Take $n$ even and let $M$ be a perfect-matching adjacency matrix. A random matching is $\Pi M\Pi^T$ with $\Pi$ a uniform random permutation matrix. A sum of $d$ independent ones is $\sum_{i=1}^d \Pi_iM\Pi_i^T$, and repeated edges add their weights (pp. 326–327). Define $\chi_x(M)\overset{def}{=}\det(xI-M)$. For simplicity the chapter treats two matrices.

**Theorem 41.2.1.** For symmetric $n\times n$ $A,B$ and uniform random $\Pi$, $\mathbb E_\Pi[\chi_x(A+\Pi B\Pi^T)]$ has only real roots (p. 327). It also holds for sums of many matrices (p. 327).

Why this is surprising: $(x-2)^2$ and $(x+2)^2$ are real rooted, but their sum $2x^2+8$ is not (p. 327).

### 41.3 Interlacing
For $p$ of degree $n$ with roots $\lambda_1\ge\dots\ge\lambda_n$ and $q$ of degree $n-1$ with roots $\mu_1\ge\dots\ge\mu_{n-1}$, they *interlace* if $\lambda_1\ge\mu_1\ge\lambda_2\ge\dots\ge\mu_{n-1}\ge\lambda_n$. Examples: a polynomial and its derivative; the characteristic polynomials of a symmetric matrix and of a principal submatrix (p. 327). For equal degrees, roots alternate in one of two ways. Write $q\to p$ if $\lambda_1\ge\mu_1\ge\lambda_2\ge\mu_2\ge\dots\ge\lambda_n\ge\mu_n$ (p. 328).

**Lemma 41.3.1.** Let $p,q$ (degrees $n$, $n-1$) interlace and have positive leading coefficients. For $t>0$, $p_t=p-tq$ is real rooted and $p\to p_t$ (p. 328).
*Sketch (distinct roots):*
- $q>0$ for $x>\mu_1$ and $\lambda_1>\mu_1$, so $p_t(\lambda_1)=-tq(\lambda_1)<0$. As $p_t$ is eventually positive, it has a root above $\lambda_1$.
- For each $i$, $p_t$ has a root between $\lambda_{i+1}$ and $\lambda_i$. Here $p_t(\lambda_i)=-tq(\lambda_i)$, and $q$ has opposite signs at $\lambda_i$ and $\lambda_{i+1}$. This accounts for all roots (p. 328).

**Lemma 41.3.2 (converse).** If $p_t=p-tq$ is real rooted for all $t\in\mathbb R$, then $p,q$ interlace (p. 328).
*Sketch (distinct roots), by contradiction:*
- Suppose two consecutive roots $\lambda_{i+1},\lambda_i$ of $p$ have no root of $q$ between them. Say $p,q>0$ there.
- For small $t_0>0$, $p_{t_0}>0$ somewhere inside, so it has two roots in the interval.
- For large $t$, $p_t<0$ on the whole interval, so it has no roots there.
- The two roots vary continuously with $t$ and cannot cross $\lambda_{i+1}$ or $\lambda_i$. So they must become complex, a contradiction (p. 328).

Together the two lemmas are Obreschkoff's theorem (p. 328).

**Lemma 41.3.3.** For symmetric $A$ and $p_t(x)=\chi_x(A+tvv^T)$, there is $q$ of degree $n-1$ with $p_t=\chi_x(A)-tq(x)$ (p. 329).
*Proof:* Take $v=\delta_1$; this suffices because rotations leave determinants unchanged. Then
$$\det(xI-A-t\delta_1\delta_1^T)=\det(xI-A)-t\det(xI^{(1)}-A^{(1)})=\chi_x(A)-t\chi_x(A^{(1)}),$$
where $A^{(1)}$ deletes row and column 1 (p. 329).

The author notes that $\chi_x(A+tvv^T)$ is real rooted for all $t$, and that for $t>0$ it interlaces $\chi_x(A)$ from above (shown easily by Courant–Fischer). Obreschkoff's lemmas show these two facts imply each other (p. 329).

**Lemma 41.3.4.** Let $p_0,p_1$ be monic of degree $n$ with $p_0\to r$ and $p_1\to r$, $r$ of degree $n$. Then $p_s=sp_1+(1-s)p_0$ is real rooted for $0\le s\le1$ (p. 329).
*Sketch (distinct roots $\mu_1>\dots>\mu_n$ of $r$):* both $p_0,p_1$ are positive at $\mu_i$ for odd $i$ and negative for even $i$. So $p_s$ is too, giving at least $n-1$ real roots. Complex roots come in conjugate pairs, so $p_s$ cannot have exactly one non-real root. With at least $n-1$ real roots, this leaves all $n$ roots real (the source states only the conjugate-pair remark; this last step is implied) (p. 329).

*Intuition note:* Interlacing means "the roots take turns". Two polynomials that each sit just below a common third one can be mixed without creating complex roots. The sign pattern at the roots of $r$ forces enough real roots.

### 41.4 Sums of polynomials
Aim: $\sum_{\Pi\in S_n}\chi_x(A+\Pi B\Pi^T)$ is real rooted. Start with $S=\{I\}$ and enlarge by swaps. This gives weighted sums $\sum_\Pi\sigma(\Pi)\chi_x(A+\Pi B\Pi^T)$ with $\sigma:S_n\to\mathbb R_{\ge0}$. $\Gamma_{i,j}$ is the permutation matrix swapping $i,j$ (p. 330).

**Lemma 41.4.1.** For symmetric $A$ and any $i,j$, there are $u,v$ with $\Gamma_{i,j}A\Gamma_{i,j}=A-uu^T+vv^T$ (p. 330).
*Proof (as written):* take $i=1,j=2$. Show $A-\Gamma A\Gamma$ has rank 2 and trace 0. It has the form with blocks $\begin{bmatrix}\alpha&\beta&y^T\\-\beta&-\alpha&-y^T\\y&-y&0_{n-2}\end{bmatrix}$. If $\alpha\ne\beta$, the sum of the first two rows is $(c,-c,0,\dots,0)$ with $c\neq0$ and every other row is a multiple of it. If $\alpha=\beta$, the first two rows are dependent and all other rows are multiples of $(1,-1,0,\dots,0)$ (p. 330). The step from "rank 2, trace 0" to the $-uu^T+vv^T$ form is not spelled out.

**Lemma 41.4.2.** Suppose $p_x(A,B)=\sum_\sigma\sigma(\Pi)\chi_x(A+\Pi B\Pi^T)$ is real rooted for all symmetric $A,B$. Then for $0<s<1$ and any $u,v$, the polynomial $(1-s)p_x(A,B)+sp_x(A-uu^T+vv^T,B)$ is real rooted (p. 330).
*Proof:* Let $r_t=p_x(A+tvv^T,B)$, real rooted for all $t$. By Lemma 41.3.3, $r_t=r_0-tq$, with $q$ of degree $n-1$ and both $r_0,q$ having positive leading coefficients. By Obreschkoff's converse, $q$ interlaces $r_0=p_x(A,B)$. By Obreschkoff's forward direction, $p_x(A,B)\to p_x(A+vv^T,B)$. The same argument gives $p_x(A-uu^T+vv^T,B)\to p_x(A+vv^T,B)$. Both polynomials interlace $r_1$ from below, so Lemma 41.3.4 applies (p. 331).

**Corollary 41.4.3.** Under the same hypothesis, $\sum_\Pi s\sigma(\Pi)\chi_x(A+\Pi B\Pi^T)+(1-s)\sigma(\Pi)\chi_x(A+\Gamma_{i,j}\Pi B\Pi^T\Gamma_{i,j}^T)$ is real rooted (p. 331).
*Proof:* $\chi_x(A+\Gamma\Pi B\Pi^T\Gamma^T)=\chi_x(\Gamma^TA\Gamma+\Pi B\Pi^T)=\chi_x(\Gamma A\Gamma^T+\Pi B\Pi^T)$. Now apply Lemma 41.4.1 and Lemma 41.4.2 (p. 331). As printed, $s$ multiplies the unswapped term and $1-s$ the swapped one.

*Intuition note:* Conjugating $A$ by a swap changes it by a rank-two correction. That correction is one downward and one upward rank-one step, and interlacing handles such steps. So mixing "swap" and "no swap" keeps real-rootedness, provided the weighted sums were real rooted for all symmetric $A,B$.

### 41.5 Random swaps
A random swap is $I$ with probability $1-s$ and $\Gamma_{i,j}$ with probability $s$. **Corollary 41.5.1:** if $\mathbb E\chi_x(A+\Pi B\Pi^T)$ is real rooted for all symmetric $A,B$, then so is $\mathbb E\chi_x(A+S\Pi B\Pi^TS^T)$ for a random swap $S$ (p. 332).

**Lemma 41.5.2.** For every $n$ there is a finite sequence of random swaps $S_1,\dots,S_k$ such that $S_1S_2\cdots S_k$ is a uniform random permutation (p. 332). Swap probabilities other than 1/2 are needed, since $n!$ is not a power of 2.
*Proof (induction):*
- Build a random permutation of the first $n-1$ elements.
- Compose with a swap of elements 1 and $n$ with probability $1-1/n$. The element that maps to $n$ is then uniformly random.
- Compose with another random permutation of the first $n-1$ elements (p. 332).

The unit ends here. Theorem 41.2.1 follows by applying Corollary 41.5.1 along the swap sequence, starting from $\{I\}$. The text implies this but does not write it out.

## Toy example (ours)
$n=2$. Let $A=\mathrm{diag}(1,0)$, $B=\mathrm{diag}(0,2)$, and $\Gamma$ the swap, so $\Gamma B\Gamma=\mathrm{diag}(2,0)$.
- No swap: $A+B=\mathrm{diag}(1,2)$, so $\chi=(x-1)(x-2)=x^2-3x+2$.
- Swap: $A+\Gamma B\Gamma=\mathrm{diag}(3,0)$, so $\chi=x(x-3)=x^2-3x$.
- Swap with probability $s$: $(1-s)(x^2-3x+2)+s(x^2-3x)=x^2-3x+2(1-s)$. Its discriminant is $9-8(1-s)=1+8s>0$, so it is real rooted for every $s\in[0,1]$.
- For $s=1/2$ (the uniform case for $n=2$, matching $1-1/n$): $x^2-3x+1$, with roots $(3\pm\sqrt5)/2$.

## Concepts
- [[characteristic-polynomial]] — $\chi_x(M)=\det(xI-M)$ (p. 327)
- [[rank-one-matrix-outer-product]] — $tvv^T$; adding it gives $\chi_x(A)-tq(x)$ (p. 329)
- [[interlacing]] (new) — roots of $p$ and $q$ alternate; $q\to p$ if the $i$th root of $p$ is $\ge$ that of $q$ (pp. 327–328)
- [[real-rooted-polynomial]] (new) — all roots real; not closed under sums (p. 327)
- [[obreschkoff-theorem]] (new) — interlacing (positive leading coefficients) gives $p-tq$ real rooted for $t>0$; conversely $p-tq$ real rooted for all real $t$ gives interlacing (p. 328)
- [[expected-characteristic-polynomial]] (new) — $\mathbb E_\Pi\chi_x(A+\Pi B\Pi^T)$ (p. 327)
- [[random-swap]] (new) — identity with probability $1-s$, $\Gamma_{i,j}$ with probability $s$ (p. 331)

## Canonical instances
- [[sum-of-real-rooted-not-real-rooted]] — $(x-2)^2+(x+2)^2=2x^2+8$ (p. 327)
- [[random-matching-sum]] — $\sum_i\Pi_iM\Pi_i^T$ as a random graph (pp. 326–327)

## Bridges (candidates)
- [structural-analogy] Interlacing of $p$ and $p-tq$ ↔ linear-algebra: Cauchy interlacing for a principal submatrix, and rank-one updates via Courant–Fischer — same alternating-root pattern.
- [metaphor] Building a uniform permutation from biased swaps ↔ probability: shuffling by sequences of random transpositions.

## Questions this raises
- Why does real-rootedness of the expected polynomial help show that some graph in the family has small second eigenvalue? (Not answered here.)
- Why do these methods stop at bipartite graphs (p. 326)?
- What changes for sums of many matrices, which the text says also works (p. 327)?
- How does the sequence of swaps in Lemma 41.5.2 look for $n=3$?

## Reading notes
- Printed page = pdf − 24. The chapter opens with "This Chapter Needs Editing".
- Lemma cross-references are broken. "Lemma 44.7.1/44.7.2/44.7.3/44.5.1" appear to mean 41.3.2, 41.3.1, 41.3.4, 41.3.3 (inferred from use). "Corollary 41.5.1" is cited on p. 331 and stated at the top of p. 332; it is the random-swap form of Cor. 41.4.3, so this reference is not broken.
- Proof of 41.3.1 (p. 328): it says "$d-1$" and "$d$ roots" (should be $n$) and says $p_t$ is monic although $p,q$ only have positive leading coefficients. It also writes $p_t(\lambda_i)>0$, $p_t(\lambda_{i+1})<0$ for odd $i$. Since $p_t(\lambda_i)=-tq(\lambda_i)$ and $q(\lambda_i)>0$, the signs should be reversed. The conclusion is unaffected.
- Lemma 41.3.4 is stated for monic $p_0,p_1$. Lemma 41.4.2 presumably needs $\sigma$ to be a probability distribution (total weight 1) for monicness; the text does not say so.
- Lemma 41.3.4 is applied as "interlace $r_1$ from below" with $r_1=p_x(A+vv^T,B)$ (p. 331).
