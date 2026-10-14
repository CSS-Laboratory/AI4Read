---
id: spielman-2025-sagt/ch33-linear
work: spielman-2025-sagt
unit: "Chapter 33 — Linear Sized Sparsifiers"
pages: 264–271
fields: [linear-algebra]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Linear Sized Sparsifiers

## L0 — One line
Choosing vectors one at a time while two "barrier" potentials stay at most 1 shows that O(n) reweighted edges can approximate a whole graph's Laplacian.

## L1 — The gist (≤ 120 words)
Can a graph with n vertices be approximated, in the Laplacian eigenvalue sense, by a graph with only about a constant times n edges? The chapter treats edges as vectors whose outer products sum to the identity on the span of the Laplacian. It builds the sparsifier greedily, adding one vector (with a scale factor) per step. Two barrier functions track how close the eigenvalues are to the moving bounds $l$ and $u$. Sherman–Morrison and a trace argument show that, while both barriers are at most 1, a suitable vector exists at every step. The simplified proof gives $6n$ vectors with eigenvalues in $[n, 13n]$. A tighter analysis gives $\lceil n/\epsilon^2\rceil$ vectors (Theorem 33.3.1).

**Prerequisites:** outer products; Loewner order $\preceq$; trace and its cyclic property; Laplacian pseudoinverse; convexity and derivatives; Sherman–Morrison.

## L2 — Key ideas (5–10 bullets)
- Each weighted edge becomes a vector $v_{(a,b)}$. These vectors sum (as outer products) to the projection $\Pi$, so sparsifying means picking few vectors and scales whose sum stays near $\Pi$ (pp. 264–265).
- Theorem 33.3.1 says that for vectors in isotropic position ($\sum_i v_iv_i^T=I$) and every $\epsilon>0$ there are scales with $|S|\le\lceil n/\epsilon^2\rceil$ and eigenvalues in $[(1-\epsilon)^2,(1+\epsilon)^2]$ (p. 265).
- Isotropy gives the trace identity $\sum_i v_i^TMv_i=\operatorname{Tr}(M)$, which is the key averaging tool (p. 265).
- Barrier functions $\Phi^u,\Phi_l$ are the traces $\operatorname{Tr}((uI-A)^{-1})$ and $\operatorname{Tr}((A-lI)^{-1})$. $\Phi^u$ blows up as $u$ approaches the largest eigenvalue and $\Phi_l$ as $l$ approaches the smallest, so keeping them small keeps the eigenvalues away from the bounds $u$ and $l$ (pp. 266–267).
- Sherman–Morrison turns the effect of adding $c\,vv^T$ on a barrier into a condition on a quadratic form of $v$ (pp. 266–269).
- Summing over all $v_i$ gives the upper and lower budgets $1/\delta_U+\Phi^u$ and $1/\delta_L-\dots$. With $\delta_U=2,\delta_L=1/3$ as long as both barriers are at most 1 they are $\le 3/2$ and $\ge 3/2$, so a good vector exists (pp. 269–271).
- After $6n$ steps the eigenvalues lie in $[n,13n]$ (p. 271).

## L3 — Walkthrough

**33.1 Overview (p. 264).** The chapter proves a slight simplification of the main result of [BSS12, BSS14]. The stated consequence (the sharper bound that, per p. 271, comes from tightening the analysis): every $n$-vertex graph has an $\epsilon$-approximation with about $4\epsilon^{-2}n$ edges. Its average degree is $d_{ave}=8\epsilon^{-2}$, so $\epsilon\approx 2\sqrt2/\sqrt d$. The author calls this about twice what a Ramanujan graph gives. It still works for average degree a little above 1.

**33.2 Edges as vectors (pp. 264–265).** Set $v_{(a,b)}=\sqrt{w_{a,b}}\,L_G^{+/2}(\delta_a-\delta_b)$. Then
$$L_G^{+/2}\Big(\sum_{(a,b)\in E}w_{a,b}L_{(a,b)}\Big)L_G^{+/2}=\sum_{(a,b)\in E}v_{(a,b)}v_{(a,b)}^T=\Pi,$$
where $\Pi=\tfrac1nL_{K_n}$ projects orthogonally to the constant vectors (p. 265). Sparsification means finding $S\subseteq E$ and $c:S\to\mathbb R$ with
$$(1-\epsilon)\Pi\preceq\sum_{(a,b)\in S}c_{a,b}v_{(a,b)}v_{(a,b)}^T\preceq(1+\epsilon)\Pi.$$
On the span of the Laplacian this reads $(1-\epsilon)I_{n-1}\preceq\cdots\preceq(1+\epsilon)I_{n-1}$. In words, all eigenvalues of the middle matrix lie in $[1-\epsilon,1+\epsilon]$.

*Intuition note.* The original graph becomes "the identity" after normalising by $L_G^{+/2}$. A sparsifier is a few reweighted pieces that still look like the identity.

**33.3 Main theorem (pp. 265–266).**
**Theorem 33.3.1.** If $\sum_i v_iv_i^T=I$ (*isotropic position*), then for every $\epsilon>0$ there are $S$ and $c_i$ with $(1-\epsilon)^2I\preceq\sum_{i\in S}c_iv_iv_i^T\preceq(1+\epsilon)^2I$ and $|S|\le\lceil n/\epsilon^2\rceil$ (p. 265).

**Lemma 33.3.2.** For vectors in isotropic position and any matrix $M$, $\sum_iv_i^TMv_i=\operatorname{Tr}(M)$. Proof: $v^TMv=\operatorname{Tr}(vv^TM)$, so $\sum_i\operatorname{Tr}(v_iv_i^TM)=\operatorname{Tr}\big((\sum_iv_iv_i^T)M\big)=\operatorname{Tr}(IM)$ (p. 265).

What is proved here is weaker: $6n$ vectors with eigenvalues between $n$ and $13n$. Dividing scales by $\sqrt{13}\,n$ gives the range $[1/\sqrt{13},\sqrt{13}]$. The author says the argument can be tightened to prove Theorem 33.3.1 (p. 266).

The algorithm adds one vector at a time. A vector may be added repeatedly, and its scale then increases. The invariant is that the eigenvalues of the scaled sum lie in $[l,u]$. Start: $S=\emptyset$, $l_0=-n$, $u_0=n$. Each addition raises $l$ by $\delta_L=1/3$ and $u$ by $\delta_U=2$. After $6n$ additions, $l=n$ and $u=13n$ (p. 266).

**33.4 Rank-1 updates (p. 266).**
**Theorem 33.4.1 (Sherman–Morrison).** For nonsingular symmetric $A$, a vector $v$ and real $c$,
$$(A-cvv^T)^{-1}=A^{-1}+c\frac{A^{-1}vv^TA^{-1}}{1-cv^TA^{-1}v}.$$
Proof by multiplying out, writing $x=cv^TA^{-1}v$:
$$(A-cvv^T)\Big(A^{-1}+c\tfrac{A^{-1}vv^TA^{-1}}{1-x}\Big)=I-cvv^TA^{-1}+c\tfrac{vv^TA^{-1}}{1-x}-c^2\tfrac{vv^TA^{-1}vv^TA^{-1}}{1-x}=I-cvv^TA^{-1}\Big(1-\tfrac1{1-x}+\tfrac{x}{1-x}\Big)=I.$$
The bracket is zero (added step: $(1-x)-1+x=0$).

**33.5 Barrier functions (p. 267).** For symmetric $A$ with eigenvalues $\lambda_1\le\dots\le\lambda_n$ and $u>\lambda_n$:
$$\Phi^u(A)=\sum_i\frac1{u-\lambda_i}=\operatorname{Tr}\big((uI-A)^{-1}\big).$$
It is positive, tends to infinity as $u\to\lambda_n$, decreases in $u$, and is convex for $u>\lambda_n$. Hence $\Phi^{u+\delta}(A)<\Phi^u(A)$ for $\delta>0$ (33.1), and $\lambda_n\le u-1/\Phi^u(A)$ (33.2).
For $l<\lambda_1$: $\Phi_l(A)=\sum_i\frac1{\lambda_i-l}=\operatorname{Tr}((A-lI)^{-1})$. It is positive, blows up as $l\to\lambda_1$, and decreases as $l$ decreases. Also $l+1/\Phi_l(A)\le\lambda_1$ (33.3).

**Claim 33.5.1.** If $l$ is a lower bound on $A$ and $\delta<1/\Phi_l(A)$, then $\Phi_{l+\delta}(A)\le\dfrac1{1/\Phi_l(A)-\delta}$. This is an equality in one dimension. Proof: the claim is equivalent to $\Phi_{l+\delta}-\Phi_l\le\delta\Phi_{l+\delta}\Phi_l$. Since all $\lambda_i-l-\delta>0$,
$$\Phi_{l+\delta}-\Phi_l=\sum_i\frac{\delta}{(\lambda_i-l-\delta)(\lambda_i-l)}\le\delta\Big(\sum_i\frac1{\lambda_i-l-\delta}\Big)\Big(\sum_i\frac1{\lambda_i-l}\Big).$$
Initially, with $A=0$: $\Phi_{-n}(0)=1=\Phi^n(0)$ (p. 268).

*Intuition note.* The barrier is large if any eigenvalue is close to a wall, so keeping it $\le1$ keeps every eigenvalue away from the walls.

**33.6 Barrier updates (pp. 268–269).** Apply Sherman–Morrison to $uI-A$ and take the trace (cyclic property):
$$\Phi^u(A+cvv^T)=\Phi^u(A)+c\frac{v^T(uI-A)^{-2}v}{1-cv^T(uI-A)^{-1}v}.$$
This increases $\Phi^u$. To compensate, raise $u$ to $\hat u=u+\delta_U$:
$$\Phi^{u+\delta_U}(A+cvv^T)=\Phi^u(A)-\big(\Phi^u(A)-\Phi^{u+\delta_U}(A)\big)+\frac{v^T(\hat uI-A)^{-2}v}{1/c-v^T(\hat uI-A)^{-1}v}.$$
This is $\le\Phi^u(A)$ if $\Phi^u-\Phi^{u+\delta_U}\ge\dfrac{v^T(\hat uI-A)^{-2}v}{1/c-v^T(\hat uI-A)^{-1}v}$. That is equivalent to $\frac1c\ge\frac{v^T(\hat uI-A)^{-2}v}{\Phi^u-\Phi^{u+\delta_U}}+v^T(\hat uI-A)^{-1}v$. Define
$$U_A=\frac{(\hat uI-A)^{-2}}{\Phi^u(A)-\Phi^{u+\delta_U}(A)}+(\hat uI-A)^{-1}.$$
**Lemma 33.6.1.** If $1/c\ge v^TU_Av$, then $\Phi^{u+\delta_U}(A+cvv^T)\le\Phi^u(A)$. The author calls it a "miracle" that the condition only involves $v$ through a quadratic form (p. 269).

**Lemma 33.6.2.** With $\hat l=l+\delta_L$ and
$$L_A=\frac{(A-\hat lI)^{-2}}{\Phi_{l+\delta_L}(A)-\Phi_l(A)}-(A-\hat lI)^{-1},$$
if $1/c\le v^TL_Av$ then $\Phi_{l+\delta_L}(A+cvv^T)\le\Phi_l(A)$. Here raising $l$ increases the barrier and adding a vector decreases it. So this gives a lower bound on $c$ (p. 269). The page states the lemma without a proof ("analog").

**33.7 The inductive argument (pp. 269–271).** We need some $v_i$ with $v_i^TU_Av_i\le v_i^TL_Av_i$. Then choose $c$ with $v_i^TU_Av_i\le1/c\le v_i^TL_Av_i$ (p. 269).

**Lemma 33.7.1.** $\sum_iv_i^TU_Av_i\le\frac1{\delta_U}+\Phi^u(A)$. Proof: by Lemma 33.3.2 the sum is $\operatorname{Tr}(U_A)$. Split into two parts (p. 270).
- Second part: $\operatorname{Tr}((\hat uI-A)^{-1})=\Phi^{u+\delta}(A)\le\Phi^u(A)$.
- First part: $\partial_u\Phi^u(A)=-\operatorname{Tr}((uI-A)^{-2})$. By convexity, $\Phi^u-\Phi^{u+\delta_U}\ge\delta_U\operatorname{Tr}((\hat uI-A)^{-2})$.
- (added step) So the first part is $\le1/\delta_U$, and adding the second part gives $\operatorname{Tr}(U_A)\le 1/\delta_U+\Phi^u(A)$.

**Lemma 33.7.2.** $\sum_iv_i^TL_Av_i\ge\frac1{\delta_L}-\frac1{1/\Phi_l(A)-\delta_L}$. Proof: by convexity in $l$, $\Phi_{l+\delta_L}-\Phi_l\le\delta_L\operatorname{Tr}((A-(l+\delta_L)I)^{-2})$. By Claim 33.5.1, $\operatorname{Tr}((A-(l+\delta_L)I)^{-1})\le\frac1{1/\Phi_l(A)-\delta_L}$ (p. 270).

So a suitable $v_i$ exists if $\frac1{\delta_U}+\Phi^u(A)\le\frac1{\delta_L}-\frac1{1/\Phi_l(A)-\delta_L}$ (p. 271). *Check:* with both barriers $\le1$, $\frac1{\delta_U}+\Phi^u\le\frac12+1=\frac32$. Also $\frac1{\delta_L}-\frac1{1/\Phi_l-\delta_L}\ge3-\frac1{1-1/3}=\frac32$. Both barriers start at 1, so by induction they stay $\le1$ (p. 271). After $6n$ steps, $l=-n+6n/3=n$ and $u=n+2\cdot6n=13n$.

*Intuition note.* Summed over the vectors, the cost of the upper wall is at most $3/2$ and the room on the lower side is at least $3/2$. So at least one vector fits both walls.

Tightening: Lemma 33.7.2 can be improved to $\sum_iv_i^TL_Av_i\ge\frac1{\delta_L}-\frac1{1/\Phi_l(A)}$. The author refers to the paper for details (p. 271).

**33.8 Progress and open problems (p. 271).**
- The result extends to sums of positive semidefinite matrices [dCSHS11].
- Sparsifiers almost this good can be computed in close to linear time [AZLO15, LS15].
- Author: given the last lecture, it seems natural to conjecture that scale factors of edges should be proportional to their weights times effective resistances.
- Author: one might conjecture that scale factors are unnecessary if all $v_i$ have the same norm. This is true but not obvious, and is essentially equivalent to the Kadison–Singer problem [MSS14, MSS15c].

## Toy example (ours)
Take $n=2$, $v_1=e_1$, $v_2=e_2$ (isotropic), $A=0$, $l=-2$, $u=2$, $\delta_U=2$, $\delta_L=1/3$.
- $\Phi^2(0)=2\cdot\frac12=1$. With $\hat u=4$: $\Phi^4(0)=2\cdot\frac14=\frac12$, difference $\frac12$. $U_A=\frac{I/16}{1/2}+\frac I4=\frac38I$, so $v_1^TU_Av_1=\frac38$.
- $\hat l=-\frac53$: $A-\hat lI=\frac53I$, $\Phi_{\hat l}(0)=2\cdot\frac35=\frac65$, difference $\frac65-1=\frac15$. $L_A=\frac{9/25}{1/5}I-\frac35I=\frac65I$, so $v_1^TL_Av_1=\frac65$.
- Any $1/c\in[\frac38,\frac65]$ works. Take $c=1$, so $A'=e_1e_1^T$ with eigenvalues $1,0$.
- Check: $\Phi^4(A')=\frac13+\frac14=\frac7{12}\le1$ and $\Phi_{-5/3}(A')=\frac38+\frac35=\frac{39}{40}\le1$.
- Sums: $\operatorname{Tr}U_A=\frac34\le\frac32$ and $\operatorname{Tr}L_A=\frac{12}5\ge\frac32$.

## Concepts
- [[rank-one-matrix-outer-product]] — edges are encoded as $v v^T$; sparsifier = weighted sum of few of them (p. 264)
- [[graph-laplacian]] — $L_G=\sum w_{a,b}L_{(a,b)}$, whose normalised form is $\Pi$ (p. 264)
- [[pseudoinverse]] — $L_G^{+/2}$ is used to normalise the Laplacian (p. 264)
- [[projection]] — $\Pi=\frac1nL_{K_n}$ is the projection orthogonal to constants (p. 265)
- [[loewner-order]] (new) — $A\preceq B$ means $B-A$ is positive semidefinite; used to state approximation (the source uses $\preceq$ without defining it; p. 265)
- [[isotropic-position]] (new) — vectors with $\sum v_iv_i^T=I$ (p. 265)
- [[spectral-sparsifier]] (new) — sparse reweighted subset whose outer-product sum is within $1\pm\epsilon$ of $\Pi$ (p. 265)
- [[barrier-function]] (new) — $\Phi^u,\Phi_l$: the traces $\operatorname{Tr}((uI-A)^{-1})$ and $\operatorname{Tr}((A-lI)^{-1})$, measuring how close the eigenvalues are to the bounds (p. 267)
- [[sherman-morrison-formula]] (new) — inverse of a rank-one update (p. 266)

## Canonical instances
- [[ramanujan-graph]] (new) — benchmark: the bound is about twice what Ramanujan graphs give (p. 264)
- [[kadison-singer-problem]] (new) — essentially equivalent to dropping scale factors for equal-norm vectors (p. 271)

## Bridges (candidates)
- [structural-analogy] barrier-function potential ↔ interior-point methods: a log/resolvent potential that blows up at the boundary keeps iterates inside a region.
- [same-math] Sherman–Morrison rank-one update ↔ linear-algebra: the inverse of a matrix after a rank-one change.
- [structural-analogy] choosing $v_i$ by trace averaging ↔ probabilistic method: if the average satisfies the inequality, some element does.

## Questions this raises
- How does the tighter analysis turn $\delta_U,\delta_L$ into the $\lceil n/\epsilon^2\rceil$ bound and the $(1\pm\epsilon)^2$ range? The text only points to the paper.
- How does $n/\epsilon^2$ in Theorem 33.3.1 relate to $4\epsilon^{-2}n$ in the overview?
- Which graph quantities, such as effective resistances, determine good scale factors? (p. 271)

## Reading notes
- Printed page = pdf − 24.
- Misprints visible in the images:
  - The Sherman–Morrison proof shows $cv^TAv$ where $cv^TA^{-1}v$ is meant (p. 266).
  - $U_A$ is defined with $\delta_u$ instead of $\delta_U$ (p. 268).
  - The proof of 33.7.1 writes $\Phi^{u+\delta}$ and $\delta_u$ (p. 270).
  - p. 271 drops the subscript $L$ in $\delta$ and the $^T$ in $v_iU_Av_i$.
  - p. 266 has "produces" for "products" and p. 269 has "exits" for "exists".
- The printed proof of Lemma 33.7.1 ends after the convexity bound on the first part (p. 270). The step to $\le1/\delta_U$ and the final combination are not written there and are marked (added step). The proof of Lemma 33.7.2 also ends before its conclusion, and Lemma 33.6.2 is stated without proof.
- The date (April 2, 2025) comes from the unit metadata, not from these pages.
