---
id: spielman-2025-sagt/ch22-local
work: spielman-2025-sagt
unit: "Chapter 22 — Local Graph Clustering"
pages: 181–188
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
# Local Graph Clustering

## L0 — One line
A lazy random walk of $t=1/2\phi$ steps from a well-chosen seed vertex in a low-conductance set $S$ is in $S$ with probability at least $1/2$, and a threshold sweep over $D^{-1}\widetilde W^t\delta_a$ then yields a set of conductance at most $\sqrt{8\ln(8|S|)\,\phi}$ (pp. 181, 188).

## L1 — The gist (≤ 120 words)
Given a seed vertex and a hidden small set $S$ of low conductance, can we find a similar set near the seed (such algorithms can avoid scanning the whole graph, p. 181)? The chapter analyses the Spielman–Teng algorithm using the Kwok–Lau–Lee proof. Run a lazy random walk from the seed. Take $y=D^{-1}p_t$. Return the best threshold set of $y$. The proof has four parts: (1) a good seed exists in $S$; (2) the walk's $D^{-1}$-norm stays large; (3) the Rayleigh quotient is therefore small; (4) rounding small entries to zero lets Cheeger's inequality apply. The proof is for existence of a good seed, and ignores run time and parameter tuning.

**Prerequisites:** conductance $\phi(S)=w(\partial S)/d(S)$; graph Laplacian and normalized Laplacian $N$; random walk matrix and its lazy version $\widetilde W=\tfrac12(I+W)$; Rayleigh quotient; Cheeger's inequality (Thm 21.1.3, used but not restated); Cauchy–Schwarz.

## L2 — Key ideas
- Local clustering aims to find a low-conductance cluster near a seed vertex. As stated, the theorem promises only that some seed in $S$ works; loosening constants would show that most seeds (by degree) work (pp. 181, 184).
- Algorithm: lazy walk $t=1/2\phi$ steps from $\delta_a$, set $y=D^{-1}\widetilde W^t p_0$, return the best-conductance threshold set (pp. 181–182).
- A seed is "good" if $d(a)/d(S)\ge 1/2|S|$ and the walk is in $S$ after $t$ steps with probability $\ge 1/2$. Good seeds exist because a degree-weighted random start in $S$ is outside $S$ at step $t$ with probability at most $t\phi(S)/2$ (pp. 182–184).
- For a good seed, being in $S$ at step $t$ with probability $\ge1/2$ forces $p_t^TD^{-1}p_t\ge 1/4d(S)$ (Cauchy–Schwarz), so this $D^{-1}$-norm stays large (p. 184).
- Lemma 22.4.1 bounds the Rayleigh quotient by $\frac1t\ln(\text{ratio of }D^{-1}\text{-norms})$, via the Power Means Inequality (pp. 185–186).
- Rounding $y$ to $x=\max(0,y-1/16s)$ keeps the set small and, for a good seed with $p_0=\delta_a$, loses at most half of $y^TDy$; this rounding is for the analysis only (pp. 187–188).
- Cheeger's inequality then gives conductance $\le\sqrt{8\ln(8|S|)\phi}$ (p. 188).

## L3 — Walkthrough

### Intro and 22.1 The algorithm (pp. 181–182)
Inputs: target size $s$, conductance bound $\phi$, seed $a$. **Claim:** if $G$ has $S$ with $d(S)\le s\le d(V)/32$ and $\phi(S)\le\phi$, then some $a\in S$ makes the algorithm return $T$ with $d(T)\le16s$ and $\phi(T)\le\sqrt{8\ln(8s)\phi}$ (p. 181). The source says the algorithm is not guaranteed to work for all $a\in S$, but that one can show it works for "most" $a$, measured by weighted degree. It also says most local clustering algorithms can be implemented to run in time depending on $d(S)$ rather than on the graph size (p. 181).

1. $p_0=\delta_a$. 2. $t=1/2\phi$ (assumed an integer). 3. $y=D^{-1}\widetilde W^t p_0$. 4. Return the threshold set $T_\tau=\{b:y(b)>\tau\}$ of least conductance among those with $d(T_\tau)\le 8s$ (pp. 181–182).

The stable distribution is $d/(\mathbf 1^Td)$. Closeness of $p$ to it is measured by the generalized Rayleigh quotient $\frac{p^TD^{-1}LD^{-1}p}{p^TD^{-1}p}$. With $y=D^{-1}p$ it equals $\frac{y^TLy}{y^TDy}$. The walk matrix is lazy: $\widetilde W=\tfrac12(I+W)=\tfrac12(I+MD^{-1})$ (p. 182).

### 22.2 Good choices for $a$ (pp. 182–184)
**Definition.** $a\in S$ is *good for $S$* if $\frac{d(a)}{d(S)}\ge\frac1{2|S|}$ and $\mathbf 1_S^T\widetilde W^t\delta_a\ge 1/2$ (p. 182).

Let $p_S(a)=d(a)/d(S)$ for $a\in S$, else $0$.

**Lemma 22.2.1.** If $d(S)\le d(V)/2$ and $p_t=\widetilde W^tp_S$, then $\mathbf 1_{V-S}^Tp_t\le t\phi(S)/2$ (p. 182).
*Proof.* Step 1: the probability of leaving $S$ is $\sum_{a\in S}p_S(a)\frac12\sum_{b\sim a,\,b\notin S}\frac{w_{a,b}}{d(a)}=\frac12\frac{w(\partial S)}{d(S)}=\frac12\phi(S)$ (p. 183). Induction on $p_i=\widetilde W p_{i-1}$ shows $p_i(a)\le d(a)/d(S)$ for all $a$, tight on $S$. Since $\widetilde W$ and $p_{i-1}$ are nonnegative, $\delta_a^Tp_i\le\delta_a^T\widetilde Wd/d(S)=d(a)/d(S)$ for $a\in S$. So the leaving probability at step $i$ is at most that of step 1, namely $\phi(S)/2$ (p. 183). Summing over $t$ steps gives the lemma (the summation is implicit in the source).

**Lemma 22.2.2.** $S$ contains a good vertex (p. 183).
*Proof.* Write $p_S=\sum_{a\in S}\frac{d(a)}{d(S)}\delta_a$. Lemma 22.2.1 gives $\sum_a\frac{d(a)}{d(S)}\mathbf 1_{V-S}^T\widetilde W^t\delta_a\le t\phi(S)/2$. Let $f_a=1$ if $\mathbf 1_{V-S}^T\widetilde W^t\delta_a>t\phi(S)$, and $b_a=1$ if $d(a)/d(S)<1/2|S|$. By what the source calls essentially Markov's inequality, $\sum_a\frac{d(a)}{d(S)}f_a<\frac12$ (p. 184). Also $\sum_a\frac{d(a)}{d(S)}b_a<\sum_a\frac1{2|S|}b_a\le\frac12$. So some $a$ has $f_a=b_a=0$. For it, $\mathbf 1_S^T\widetilde W^t\delta_a=1-\mathbf 1_{V-S}^T\widetilde W^t\delta_a\ge1-t\phi(S)\ge\frac12$, since $t\phi(S)\le\frac12$ (p. 184).

*Intuition note.* From a degree-weighted random start in $S$, the chance of being outside $S$ at step $t$ is at most $t\phi(S)/2$. Starts with unusually high escape probability carry degree-weight $<1/2$, and so do starts with unusually small degree, so some start is neither. Loosening constants would show that most vertices of $S$ (degree-weighted) are good (p. 184).

### 22.3 Bounding the $D$-norm (p. 184)
**Claim 22.3.1.** For a probability vector $p$: $p^TD^{-1}p\ge(\mathbf 1_S^Tp)^2/d(S)$.
*Proof.* $\mathbf 1_S^Tp=\sum_{a\in S}\sqrt{d(a)}\,\big(p(a)/\sqrt{d(a)}\big)$. Cauchy–Schwarz gives $(\mathbf 1_S^Tp)^2\le\big(\sum_{a\in S}d(a)\big)\big(\sum_{a\in S}p(a)^2/d(a)\big)\le d(S)\,p^TD^{-1}p$.

For good $a$, $\mathbf 1_S^Tp_t\ge\frac12$, so $p_t^TD^{-1}p_t\ge\frac1{4d(S)}$.

*Intuition note.* (Our gloss.) If at least half the mass sits on $S$, then $p^TD^{-1}p\ge 1/4d(S)$, which is large when $d(S)$ is small. This is the bound used next.

### 22.4 Bounding the Rayleigh quotient (pp. 185–186)
**Lemma 22.4.1.** If $p_t=\widetilde W^tp_0$ for a probability vector $p_0$, then
$$\frac{p_t^TD^{-1}LD^{-1}p_t}{p_t^TD^{-1}p_t}\le\frac1t\ln\!\Big(\frac{p_0^TD^{-1}p_0}{p_t^TD^{-1}p_t}\Big).$$

**Theorem 22.4.2 (Power Means).** For $k>h>0$, weights $w_i\ge0$ summing to 1, and $\lambda_i\ge0$: $\big(\sum w_i\lambda_i^k\big)^{1/k}\ge\big(\sum w_i\lambda_i^h\big)^{1/h}$ (p. 185).

*Proof of 22.4.1.* Let $z_t=D^{-1/2}p_t$. Then the numerator is $z_t^TNz_t$ and the denominator is $z_t^Tz_t$. Expand $z_0=\sum_ic_i\psi_i$ in the eigenbasis of $N$, and set $\gamma=1/\sum c_i^2=1/z_0^Tz_0$, so $\sum_i\gamma c_i^2=1$. Then $z_t=(D^{-1/2}\widetilde WD^{1/2})^tz_0$, and $D^{-1/2}\widetilde WD^{1/2}=I-\tfrac12N$ (Chapter 10). Eigenvalues satisfy $\nu_i=2-2\omega_i$ ($\nu_i$ of $N$, $\omega_i$ of this matrix). So $z_t=\sum_ic_i\omega_i^t\psi_i$ and
$$z_t^TNz_t=\sum_ic_i^2\nu_i\omega_i^{2t}\le2\sum_ic_i^2\omega_i^{2t}-2\sum_ic_i^2\omega_i^{2t+1}$$
(p. 186; (added step) substituting $\nu_i=2-2\omega_i$ makes this an equality). Hence
$$\frac{z_t^TNz_t}{z_t^Tz_t}=2-2\frac{\sum_i\gamma c_i^2\omega_i^{2t+1}}{\sum_i\gamma c_i^2\omega_i^{2t}}.$$
Apply Power Means with weights $\gamma c_i^2$, $k=2t+1$, $h=2t$:
$$\Big(\sum\gamma c_i^2\omega_i^{2t+1}\Big)^{\frac1{2t+1}}\ge\Big(\sum\gamma c_i^2\omega_i^{2t}\Big)^{\frac1{2t}}\Rightarrow\sum\gamma c_i^2\omega_i^{2t+1}\ge\Big(\sum\gamma c_i^2\omega_i^{2t}\Big)^{1+\frac1{2t}}\Rightarrow\frac{\sum\gamma c_i^2\omega_i^{2t+1}}{\sum\gamma c_i^2\omega_i^{2t}}\ge\Big(\sum\gamma c_i^2\omega_i^{2t}\Big)^{\frac1{2t}}.$$
Thus the quotient is $\le2-2\big(\tfrac{z_t^Tz_t}{z_0^Tz_0}\big)^{1/2t}$. Let $R=z_t^Tz_t/z_0^Tz_0$. Then $R^{1/2t}=\exp(-\ln(1/R)/2t)\ge1-\ln(1/R)/2t$. So the bound is $\le\ln(1/R)/t=\frac1t\ln\frac{z_0^Tz_0}{z_t^Tz_t}$ (p. 186). ∎

*Skip path:* carry forward Lemma 22.4.1 only.

*Application.* For good $a$, with $p_0=\delta_a$ (so $p_0^TD^{-1}p_0=1/d(a)$, an added step): $\frac{p_t^TD^{-1}p_t}{p_0^TD^{-1}p_0}\ge\frac1{4d(S)p_0^TD^{-1}p_0}\ge\frac{d(a)}{4d(S)}\ge\frac1{8|S|}$. So the quotient is $\le\frac{\ln(8|S|)}t\le2\phi\ln(8|S|)$ (p. 186).

*Intuition note.* (Our gloss.) The lemma says: if the norm $p_t^TD^{-1}p_t$ has not dropped much below $p_0^TD^{-1}p_0$ after $t$ steps, then the Rayleigh quotient is small. For a good seed the norm drops by a factor of at most $8|S|$.

### 22.5 Rounding (pp. 187–188)
Let $y=D^{-1}p_t$. So that the algorithm underlying Cheeger's inequality finds a set that is not too big, the source rounds small entries of $y$ to zero; it says this is not necessary for the algorithm but facilitates the analysis (p. 187). Since $\mathbf 1^Tp_t=1$, $d^Ty=1$, and the Rayleigh quotient equals $y^TLy/y^TDy$ (p. 187). Define
$$x(a)=\max(0,\,y(a)-1/16s).\tag{22.1}$$
If $s\le d(V)/32$, $x$ is positive on degree-weight $<16s\le d(V)/2$: $\sum_{y(a)>1/16s}d(a)<\sum_{p_t(a)>d(a)/16s}16s\,p_t(a)\le16s$. As Cheeger's inequality will produce a set of the form $T_\tau=\{a:y(a)>\tau\}$, the source concludes that this set satisfies $d(T_\tau)\le16s$ (p. 187).

**Lemma 22.5.1.** If $d^Ty=1$ and $x(a)=\max(0,y(a)-\epsilon)$, then $x^TDx\ge y^TDy-2\epsilon$.
*Proof.* The source says "for every number $y$ and $\epsilon$": $\max(0,y-\epsilon)^2\ge y^2-2y\epsilon$ (added remark: this needs $y\ge0$, $\epsilon>0$, which holds here since $y=D^{-1}p_t\ge0$). If $y\le\epsilon$ the source says the right side is $<0$ (true for $0<y\le\epsilon$); if $y>\epsilon$, $(y-\epsilon)^2=y^2-2y\epsilon+\epsilon^2$. Sum with weights $d(a)$: $x^TDx\ge y^TDy-2\epsilon\sum_ad(a)y(a)=y^TDy-2\epsilon$ (p. 187).

For good $a$ with $p_0=\delta_a$: $x^TDx\ge y^TDy-\frac1{8d(S)}\ge\frac12y^TDy$ (p. 188). (Added steps: $2\epsilon=1/8s\le1/8d(S)$ since $d(S)\le s$; and $y^TDy=p_t^TD^{-1}p_t\ge1/4d(S)$ by 22.3.) Shifting and thresholding cannot increase any edge length, so $x^TLx\le y^TLy$. Together
$$\frac{x^TLx}{x^TDx}\le2\frac{y^TLy}{y^TDy}\le4\ln(8|S|)\phi.$$
Since $x$ is balanced with respect to $d$ (the source writes $y$; see Reading notes), Cheeger's inequality gives a set $T$ with conductance at most $\sqrt{8\ln(8|S|)\phi}$ (p. 188).

*Intuition note.* Dropping tiny entries keeps the support small, and costs at most half the norm. So the roughness ratio rises only by a factor of 2.

### 22.6 Notes (p. 188)
Only a placeholder; no content.

## Toy example (ours)
Path $1-2-3-4$, unit weights, $d=(1,2,2,1)$, $d(V)=6$. Seed $a=1$, $p_0=\delta_1$.
- $p_1=\tfrac12p_0+\tfrac12Wp_0$. All mass of vertex 1 moves to 2 under $W$, so $p_1=(\tfrac12,\tfrac12,0,0)$.
- $p_2$: vertex 1 (mass ½) stays ¼, sends ¼ to 2. Vertex 2 (mass ½) stays ¼, sends ⅛ to 1 and ⅛ to 3. So $p_2=(\tfrac38,\tfrac12,\tfrac18,0)$, sum $=1$.
- $y=D^{-1}p_2=(\tfrac38,\tfrac14,\tfrac1{16},0)$. Check $d^Ty=\tfrac38+\tfrac12+\tfrac18=1$.
- Sweep (with $\phi(T)=w(\partial T)/d(T)$, $d(T)\le3$): $\{1\}$: $1/1=1$; $\{1,2\}$: $1/3$; $\{1,2,3\}$ has $d=5>3$, excluded. Best: $\{1,2\}$ with $\tau=0.2$.

## Concepts
- [[local-graph-clustering]] (new) — find a low-conductance set near a seed; the intro says most such algorithms can run in time depending on $d(S)$ rather than the graph size (p. 181)
- [[conductance]] (new) — $\phi(S)=w(\partial S)/d(S)$ (p. 183)
- [[lazy-random-walk]] (new) — $\widetilde W=\tfrac12(I+W)$ (p. 182)
- [[good-seed-vertex]] (new) — $a\in S$ with $d(a)/d(S)\ge1/2|S|$ and walk stays in $S$ w.p. $\ge1/2$ (p. 182)
- [[rayleigh-quotient]] — used here in generalized form $p^TD^{-1}LD^{-1}p/p^TD^{-1}p$ (p. 182)
- [[power-means-inequality]] (new) — $(\sum w_i\lambda_i^k)^{1/k}\ge(\sum w_i\lambda_i^h)^{1/h}$ for $k>h>0$, weights $w_i\ge0$ summing to 1 (p. 185)
- [[cheeger-inequality]] (new) — turns a small Rayleigh quotient of a $d$-balanced vector into a threshold set of low conductance (used, not restated, pp. 187–188)
- [[graph-laplacian]] — $L$, and normalized $N=D^{-1/2}LD^{-1/2}$ (p. 185)

## Canonical instances
- [[spielman-teng-local-clustering]] — walk-and-sweep algorithm, analysed via Kwok–Lau–Lee (pp. 181–188)

## Bridges (candidates)
- [structural-analogy] Rounding $y$ to $x$ and sweeping thresholds ↔ spectral clustering: Fiedler-vector sweep cut.
- [same-math] $\|D^{-1/2}p_t\|^2$ decay under $I-\tfrac12N$ ↔ power iteration: components shrink by $\omega_i^t$.
- [structural-analogy] Escape probability $\le t\phi(S)/2$ ↔ Markov chains: bottleneck ratio slows mixing.

## Questions this raises
- Can the work be bounded by $d(S)$ rather than $|V|$, and how (the source only asserts this, p. 181)?
- How does $\ln(8|S|)$ in the proof relate to $\ln(8s)$ in the claim?
- Can the $\sqrt\phi$ loss be improved? (The intro mentions later improvements, p. 181.)
- Which fraction of $S$ is good after loosening constants (p. 184)?

## Reading notes
- Printed = pdf − 24.
- Step 4 uses $d(T_\tau)\le8s$ (p. 182), while 22.5 derives $d(T_\tau)\le16s$ (p. 187), matching the claim (p. 181).
- The claim (p. 181) uses $\ln(8s)$; the proof ends with $\ln(8|S|)$. The source does not connect them.
- p. 188: "$y$ is balanced" presumably means $x$, which was shown balanced on p. 187.
- 22.4: Power Means needs $\omega_i\ge0$, which is not stated on these pages.
- Intro promises pointers to advances; §22.6 is only a placeholder. $M$ is not defined here.
- p. 185: Lemma 22.4.1 is printed without the transpose in $p_0D^{-1}p_0$ and $p_tD^{-1}p_t$; the digest writes the intended $p^TD^{-1}p$.
- p. 187: the source writes $(y-\epsilon)^2=y^2-2y+\epsilon^2$ (missing $\epsilon$ in the middle term). It also says "for every number $y$", but the inequality needs $y\ge0$, which holds here.
