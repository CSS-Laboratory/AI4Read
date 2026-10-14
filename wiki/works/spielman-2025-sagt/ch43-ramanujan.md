---
id: spielman-2025-sagt/ch43-ramanujan
work: spielman-2025-sagt
unit: "Chapter 43. Ramanujan Graphs of Every Size"
pages: 341-348
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Ramanujan Graphs of Every Size

## L0 — One line
The expected characteristic polynomial of a sum of $d$ random perfect matchings has second-largest root at most $2\sqrt{d-1}$, and an interlacing-family argument shows that some single graph in the family does at least as well.

## L1 — The gist (≤ 120 words)
Can we show that a $d$-regular multigraph on $n$ vertices with second adjacency eigenvalue at most $2\sqrt{d-1}$ exists for every $d<n$? The author sums $d$ random perfect matchings and studies the expected characteristic polynomial instead of the random eigenvalues. Interlacing families show that some graph in the family has a $j$th largest root no larger than that of the expected polynomial. A bound on the "inverse Cauchy transform" of finite free convolutions (stated, proof deferred) then gives the root bound $2\sqrt{d-1}$. The chapter proves existence only. It gives no probability estimate and does not control negative eigenvalues.

**Prerequisites:** characteristic polynomials; real-rooted and interlacing polynomials (Lectures 22–23); adjacency eigenvalues; permutation matrices; derivatives of polynomials.

## L2 — Key ideas (5–10 bullets)
- Goal: for every $d<n$, a $d$-regular multigraph whose second adjacency eigenvalue is at most $2\sqrt{d-1}$. Negative eigenvalues are not controlled (p. 341).
- Method: take the expected characteristic polynomial of $\sum_i \Pi_i M\Pi_i^T$, not moments of random eigenvalues as in Friedman's approach (p. 342).
- If polynomials form an interlacing family (leaves of a rooted tree whose internal labels are nonnegative combinations of their children, and whose sibling groups have a common interlacing, i.e. all interlace one fixed polynomial), some member has $j$th largest root at most that of the root polynomial (Lemma 43.3.2, p. 343).
- The graph polynomials form such a family (Theorem 43.3.3, stated here, p. 343).
- The expected polynomial equals $(x-d)$ times a finite free convolution $\boxplus_{n-1}$ of $d$ copies of $p$, where $\chi_x(M)=(x-1)p(x)$; the convolution is the expected characteristic polynomial of $A+\Pi B\Pi^T$, up to the row-sum factor (p. 344).
- Largest roots alone do not give useful bounds, since $(x-a)^n\boxplus(x-b)^n=(x-(a+b))^n$. The proof uses instead the Cauchy transform $\mathcal G_p=\frac1d p'/p$, the average of $1/(x-\lambda_i)$ over the roots of $p$ (p. 344).
- Theorem 43.4.1, $\mathcal K_{p\boxplus_n q}(w)\le \mathcal K_p(w)+\mathcal K_q(w)-1/w$, with $w$ then optimised, gives $2\sqrt{d-1}$ (pp. 345–346).
- Expected polynomials can behave very differently from typical random matrices (p. 347).

## L3 — Walkthrough

### 43.1 Overview (p. 341)
- The chapter draws on [MSS15d] and [MSS15a]. Those papers prove that for every even $n$ and $d<n$ there is a bipartite Ramanujan graph of degree $d$ on $n$ vertices. Its eigenvalues are $d$, $-d$, and all others have absolute value at most $2\sqrt{d-1}$.
- Today's claim is weaker: for every $d<n$ there is a $d$-regular (multi)graph whose second adjacency eigenvalue is at most $2\sqrt{d-1}$.
- The author says this suffices for many, but not all, applications of expanders. Negative eigenvalues are skipped for simplicity, since the proofs would take more lectures. The author adds that next week a different technique will give a bipartite Ramanujan graph that is not a multigraph.

### 43.2 The approach (pp. 341–342)
- Take the sum of $d$ random perfect matchings. Friedman [Fri08] proves that for all $d$ and $\epsilon>0$ there is $n_0$ such that for $n>n_0$ such a graph probably has all eigenvalues other than $\mu_1$ at most $2\sqrt{d-1}+\epsilon$ in absolute value.
- Here the asymptotics and $\epsilon$ are removed, but only existence is proved. The probability is not estimated. It is "predicted to be a constant" (citation unresolved, p. 342).
- Difference from Friedman: he bounds moments of the eigenvalue distribution. **Author's suspicion:** no true moment bound would imply that a random graph is probably Ramanujan.
- Here: $M$ is the adjacency matrix of a perfect matching, and $\Pi_1,\dots,\Pi_d$ are independent uniform permutation matrices. Consider
$$\mathbb E_{\Pi_1,\dots,\Pi_d}\left[\chi_x\left(\Pi_1 M\Pi_1^T+\cdots+\Pi_d M\Pi_d^T\right)\right].$$
- It is real rooted (Lecture 22) and computable (Lecture 23). The author says the chapter will prove its second-largest root is at most $2\sqrt{d-1}$ (the proof uses Theorem 43.4.1, whose proof is deferred). This implies some choice of $\Pi_i$ gives a graph with second-largest root at most $2\sqrt{d-1}$.

### 43.3 Interlacing families (pp. 342–343)
- $p\to r$ means $p$ and $r$ are monic of the same degree with interlacing roots, those of $r$ being larger.
- If $p_1\to r$ and $p_2\to r$, then $sp_2+(1-s)p_1\to r$ for $0\le s\le 1$. By induction, $\sum_i s_ip_i\to r$ for all $s_i\ge0$, not all zero. Such polynomials have a **common interlacing**.
- By a technique like that of Lemma 22.3.2: $p_1,\dots,p_m$ have a common interlacing if and only if every convex combination is real rooted (p. 342).

**Lemma 43.3.1.** Let $p_i\to r$, let $s_i\ge0$ be not all zero, and let $p_\emptyset=\sum_i s_ip_i$. Then for each $j$ some $p_i$ has $j$th largest root at most that of $p_\emptyset$.
- Proof for the largest root: let $\lambda_1>\lambda_2$ be the top two roots of $r$. Each $p_i$ has exactly one root in $(\lambda_2,\lambda_1)$ and is positive for $x>\lambda_1$.
- The largest root $\mu$ of $p_\emptyset$ lies between $\lambda_1$ and $\lambda_2$, and $\sum_ip_i(\mu)=0$.
- If some $p_i(\mu)=0$, done. Otherwise some $p_i(\mu)>0$. That $p_i$ has one root above $\lambda_2$ and is eventually positive, so its largest root is below $\mu$ (p. 343).

*Intuition note:* The sum is zero at $\mu$, so either some term is zero there (done) or some term must be positive there. A positive term at $\mu$ means that polynomial has already crossed zero, so its top root lies to the left.

**Interlacing family.** A set $p_1,\dots,p_m$ is an interlacing family if a rooted tree $T$ exists with: (a) each leaf labeled by some $p_i$; (b) each internal vertex labeled by a nonzero, nonnegative combination of its children; (c) all siblings have a common interlacing. Then all internal labels are real rooted. The same label may appear at many leaves (p. 343).

**Lemma 43.3.2.** For such a family with root label $p_\emptyset$, for each $j$ some $p_i$ has $j$th largest root at most that of $p_\emptyset$. Proof: at each step apply the lemma the source cites as "Lemma 44.5.2" (apparently Lemma 43.3.1) to move to a child, down to a leaf (p. 343). (The printed text cites "Lemma 44.5.2"; see Reading notes.)

**Theorem 43.3.3** (stated here without proof). The polynomials $p_{\Pi_1,\dots,\Pi_d}(x)=\chi_x(\Pi_1M\Pi_1^T+\cdots+\Pi_dM\Pi_d^T)$ form an interlacing family. The author says the construction of permutations by sequences of random swaps provides it (p. 343).

So it remains to bound the second-largest root of $\mathbb E[p_{\Pi_1,\dots,\Pi_d}]$ by $2\sqrt{d-1}$ (p. 344).

### 43.4 Root bounds for finite free convolutions (pp. 344–345)
- From the last lecture: for symmetric $n\times n$ matrices $A,B$ with uniform row sums $a,b$ and $\chi_x(A)=(x-a)p(x)$, $\chi_x(B)=(x-b)q(x)$,
$$\mathbb E_\Pi[\chi_x(A+\Pi B\Pi^T)]=(x-(a+b))\,p(x)\boxplus_{n-1}q(x).$$
- This extends to many summands. Here $\chi_x(M)=(x-1)^{n/2}(x+1)^{n/2}=(x-1)p(x)$ with $p(x)=(x-1)^{n/2-1}(x+1)^{n/2}$. So
$$p_\emptyset(x)=\mathbb E[p_{\Pi_1,\dots,\Pi_d}(x)]=(x-d)\big(p\boxplus_{n-1}p\boxplus_{n-1}\cdots\boxplus_{n-1}p\big),$$
with $p$ appearing $d$ times.
- A bound in terms of largest roots only is unproductive. For $A=aI$, $B=bI$ we get $A+\Pi B\Pi^T=(a+b)I$, so $(x-a)^n\boxplus(x-b)^n=(x-(a+b))^n$. Largest roots can add, so the distribution of the roots of $p$ must be used.
- **Cauchy transform** of $p(x)=\prod_{i=1}^n(x-\lambda_i)$:
$$\mathcal G_p(x)=\frac1d\sum_i\frac1{x-\lambda_i}=\frac1d\frac{p'(x)}{p(x)}.$$
It is the Cauchy transform of the uniform distribution on the roots. **Inverse Cauchy transform:** $\mathcal K_p(w)=\max\{x:\mathcal G_p(x)=w\}$. For real-rooted $p$ this is the $x$ above all $\lambda_i$ with $\mathcal G_p(x)=w$. It is the largest root for $w=\infty$ and larger for finite $w$ (p. 345).

**Theorem 43.4.1.** For degree $n$ polynomials $p,q$ and $w>0$:
$$\mathcal K_{p\boxplus_nq}(w)\le\mathcal K_p(w)+\mathcal K_q(w)-1/w.$$
- For $w=\infty$ this says the largest root of $p\boxplus_nq$ is at most the sum of the largest roots, which the author calls obvious.
- Why $1/w$: take $q=x^n$, the characteristic polynomial of the zero matrix, so $p\boxplus_nq=p$. Then $\mathcal G_q(x)=\frac1n\frac{nx^{n-1}}{x^n}=1/x$, so $\mathcal K_q(w)=1/w$ and $\mathcal K_q(w)-1/w=0$ (p. 345).
- The proof is deferred to the next lecture, or maybe to the paper [MSS15a].

*Intuition note:* The Cauchy transform is the average of $1/(x-\lambda_i)$ over the roots and serves as a barrier function: it is large when $x$ is just above the roots. The $1/w$ correction is explained by the case $q=x^n$ (a matrix with all roots at 0), which leaves $p$ unchanged.

### 43.5 The calculation (pp. 345–346)
- For $x\ge1$ (as printed):
$$\mathcal G_p(x)=\frac1{n-1}\Big(\frac{n/2-1}{x-1}+\frac{n/2}{x+1}\Big)\le\frac1n\Big(\frac{n/2}{x-1}+\frac{n/2}{x+1}\Big)=\frac{x}{x^2-1}=\mathcal G_{\chi(M)}(x).$$
Hence $\mathcal K_p(w)\le\mathcal K_{\chi(M)}(w)$ for $w\ge0$ (p. 345).
- Theorem 43.4.1 applied $d-1$ times gives
$$\mathcal K_{p\boxplus_{n-1}\cdots\boxplus_{n-1}p}(w)\le d\mathcal K_p(w)-\frac{d-1}{w}\le d\mathcal K_{\chi(M)}(w)-\frac{d-1}{w}.$$
- This bounds the largest root of the convolution, so choose $w$ to minimise it. Since $\mathcal K_{\chi(M)}(w)=x$ iff $w=x/(x^2-1)$, we get $1/w=(x^2-1)/x$, so
$$d\mathcal K_{\chi(M)}(w)-\frac{d-1}{w}\le dx-(d-1)\frac{x^2-1}{x}.$$
- (added step) The derivative in $x$ is $d-(d-1)(1+x^{-2})$. It is zero at $x^2=d-1$. The author states the minimiser is $x=\sqrt{d-1}$. The value is
$$d\sqrt{d-1}-\frac{(d-1)(d-2)}{\sqrt{d-1}}=d\sqrt{d-1}-(d-2)\sqrt{d-1}=2\sqrt{d-1}.$$
(p. 346)

*Intuition note:* (added step) The bound equals $dx-(d-1)\big(x-\tfrac1x\big)=x+\frac{d-1}{x}$. As $x$ grows the first term grows and the second shrinks, and the best compromise $x=\sqrt{d-1}$ gives the value $2\sqrt{d-1}$.

### 43.6 Some explanation of Theorem 43.4.1 (pp. 346–347)
The proof is not given; only its shape.
- $\mathcal G_p(x)=w\iff p(x)-\frac1{wd}p'(x)=0$. So $\mathcal K_p(w)=\mathrm{maxroot}\big((1-\tfrac1{wd}\partial_x)p\big)$. Define $U_\alpha=1-\alpha\partial_x$. The theorem becomes
$$\mathrm{maxroot}(U_\alpha(p\boxplus_nq))\le\mathrm{maxroot}(U_\alpha p)+\mathrm{maxroot}(U_\alpha q)-n\alpha.\tag{43.1}$$
(p. 346; printed with $U_\alpha p$ twice, see Reading notes.)
- Coefficient formula: if $p=\sum_i x^{n-i}(-1)^ia_i$ and $q=\sum_ix^{n-i}(-1)^ib_i$, then
$$p\boxplus_nq=\sum_{k=0}^nx^{n-k}(-1)^k\sum_{i+j=k}\frac{(n-i)!(n-j)!}{n!(n-i-j)!}a_ib_j.\tag{43.2}$$
- Derivative form: $p\boxplus_nq=\frac1{n!}\sum_{i=0}^n(n-i)!\,b_i\,p^{(i)}(x)$. This handles polynomials of different degrees (p. 347).
- **Lemma 43.6.1.** If $\deg p=n$ and $q=x^{n-1}$, then $p\boxplus_nq=\partial_xp$. Here $U_\alpha q=x^{n-1}-\alpha(n-1)x^{n-2}$, so $\mathrm{maxroot}(U_\alpha q)=\alpha(n-1)$, and (43.1) reads $\mathrm{maxroot}(U_\alpha\partial_xp)\le\mathrm{maxroot}(U_\alpha p)-\alpha$.
- The proof has two ingredients: this inequality, and showing the extreme case is $q=(x-b)^n$. For the second, an arbitrary real-rooted $q$ is modified so two roots coincide, giving an induction on degree. It uses **Lemma 43.6.2:** if $\deg p=n$ and $\deg q<n$, then $p\boxplus_nq=\frac1n(\partial_xp)\boxplus_{n-1}q$ (proof said to need 2 pages).

### 43.7 Some thoughts (pp. 347–348)
- Expected polynomials differ from random roots. Let $A$ be symmetric of dimension $3k$ with $k$ eigenvalues each equal to $1$, $0$, $-1$. For random $\Pi$, $A+\Pi A\Pi^T$ almost definitely has roots at $2$ and $-2$; failing is exponentially unlikely in $k$. Yet all roots of the expected characteristic polynomial are strictly bounded away from 2 (p. 347; verifiable via the Cauchy transform).
- In the chapter's case, $A$ has $k$ eigenvalues $1$ and $k$ eigenvalues $-1$. Then $A+\Pi A\Pi^T$ almost definitely has roots at $\pm2$, and the expected polynomial has roots very close to this. For $A+\Pi_1A\Pi_1^T+\Pi_2A\Pi_2^T$ there are almost definitely roots at $\pm3$, but the largest root of the expected polynomial is at most $2\sqrt2<3$ (p. 348).
- Theorem 43.4.1 is inspired by a theorem of Voiculescu in the infinite-dimensional case, where the inequality becomes an equality (p. 348).

## Toy example (ours)
Let $r=(x-2)(x-4)$, $p_1=(x-1)(x-3)=x^2-4x+3$, $p_2=(x-1.5)(x-3.5)=x^2-5x+5.25$.
- Interlacing: $1<2<3<4$ and $1.5<2<3.5<4$, so $p_1\to r$, $p_2\to r$.
- With $s_1=s_2=\tfrac12$: $p_\emptyset=x^2-4.5x+4.125$. Its roots are $(4.5\pm\sqrt{20.25-16.5})/2=(4.5\pm1.9365)/2\approx3.218,\ 1.282$.
- Largest roots: $p_1$ has 3, $p_2$ has 3.5. Since $3\le3.218$, $p_1$ works (Lemma 43.3.1). Second roots: $1\le1.282$, also $p_1$.
- Check the proof: at $\mu\approx3.218$, $p_1(\mu)\approx0.484>0$ and $p_2(\mu)\approx-0.484$, summing to 0. The positive one is $p_1$, whose top root is below $\mu$.

## Concepts
- [[ramanujan-graph]] (new) — $d$-regular graph whose nontrivial eigenvalues are at most $2\sqrt{d-1}$ in absolute value; this chapter proves only the second-eigenvalue bound (p. 341)
- [[characteristic-polynomial]] — $\chi_x(\cdot)$, whose roots are eigenvalues; here averaged over random permutations (p. 342)
- [[adjacency-matrix]] — $M$ for a perfect matching; sums $\sum\Pi_iM\Pi_i^T$ give $d$-regular multigraphs (p. 342)
- [[interlacing-family]] (new) — polynomials labeling the leaves of a rooted tree whose internal vertices are nonzero nonnegative combinations of their children and whose sibling groups have common interlacings (p. 343)
- [[common-interlacing]] (new) — polynomials $p_i$ that all interlace one polynomial $r$ ($p_i\to r$); the author says this is equivalent to every convex combination being real rooted (p. 342)
- [[expected-characteristic-polynomial]] (new) — $\mathbb E\,\chi_x$ over random permutations, studied instead of random roots (p. 342)
- [[finite-free-convolution]] (new) — $p\boxplus_nq$, the expected characteristic polynomial of $A+\Pi B\Pi^T$ up to the row-sum factor (p. 344)
- [[cauchy-transform]] (new) — $\mathcal G_p=\frac1d p'/p$, the barrier function of $p$'s roots; $\mathcal K_p$ is its inverse (p. 344)

## Canonical instances
- [[random-perfect-matching-sum]] — $d$ random perfect matchings give a $d$-regular graph that might be a multigraph (p. 341)
- [[aI-plus-bI-convolution]] — $(x-a)^n\boxplus(x-b)^n=(x-(a+b))^n$, showing largest roots can add (p. 344)
- [[zero-matrix-convolution]] — $q=x^n$ has $\mathcal K_q(w)=1/w$, explaining the $1/w$ term (p. 345)

## Bridges (candidates)
- [structural-analogy] Interlacing-family argument ↔ probabilistic method: the average's property gives an element with a no worse property.
- [structural-analogy] Cauchy-transform barrier ↔ Stieltjes transform of the root distribution (the author calls it the Cauchy transform of the uniform root distribution).
- [structural-analogy] Voiculescu's theorem (infinite dimension, equality) ↔ free probability: the finite inequality mirrors the limiting additive convolution (p. 348).

## Questions this raises
- How is Theorem 43.3.3 proved, i.e. why does the random-swap tree give common interlacings?
- Can negative eigenvalues be controlled, to give Ramanujan graphs rather than only a second-eigenvalue bound?
- What is the actual probability that a random sum of matchings is Ramanujan?
- Why is the expected polynomial more informative than moment bounds here?

## Reading notes
- Printed = pdf − 24. Draft banner: "This Chapter Needs Editing" (p. 341).
- Misprints and loose points seen in the images:
  - Lemma 43.3.2's proof cites "Lemma 44.5.2", a reference that matches no lemma in this unit; Lemma 43.3.1 fits its use.
  - The Cauchy transform definition uses $d$ for the number of roots, but $p$ has degree $n$.
  - (43.1) shows $\mathrm{maxroot}(U_\alpha p)$ twice. The second term should be $U_\alpha q$, as the later use shows.
  - Page 346 prints "$dx-d-1\frac{x^2-1}{x}$", with parentheses missing around $(d-1)$.
- Citations "[?]" (p. 342) and "Lecture ??" (p. 344) are unresolved in the source.
- A sum of perfect matchings needs even $n$; this is our remark, not stated in the unit.
- The proofs of Theorems 43.3.3 and 43.4.1 are not in this unit.
