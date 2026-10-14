---
id: polyanskiy-2025-information/ch16-neyman
work: polyanskiy-2025-information
unit: "Chapter 14 (file id ch16-neyman): Neyman-Pearson lemma"
pages: 276-290
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Neyman-Pearson lemma

## L0 — One line
The best trade-off between the two error types of a binary hypothesis test is achieved by thresholding the log-likelihood ratio (with randomization at the threshold), and for many i.i.d. samples, when the other error is only required to stay below a fixed $\epsilon<1$, the best exponential decay rate of the missed-detection error is the KL divergence $D(P\|Q)$.

## L1 — The gist (≤ 120 words)
Given two distributions $P$ and $Q$ and one observation, which test is best? Two error probabilities compete, so the author defines the region $\mathcal R(P,Q)$ of all achievable $(\alpha,\beta)$ pairs. The Neyman-Pearson lemma shows that its lower boundary is traced exactly by (possibly randomized) likelihood-ratio tests. Converse and achievability bounds are given in terms of the log-likelihood ratio. For $n$ i.i.d. samples, Stein's lemma says the best exponent of $\beta$, with the other error bounded by $\epsilon<1$, is $D(P\|Q)$. The chapter ends with a preview of the Chernoff regime (both errors exponentially small), which leads to large deviations.

**Prerequisites:** KL divergence and its data-processing inequality; weak law of large numbers; convex sets and supporting lines; Radon–Nikodym derivative (density ratio); sufficient statistic.

## L2 — Key ideas (5–10 bullets)
- Test quality is a pair $(\alpha,\beta)=(P[Z=0],Q[Z=0])$. The Neyman-Pearson (NP) region $\mathcal R(P,Q)$ of all randomized tests is closed, convex, contains the diagonal and is symmetric under $(\alpha,\beta)\mapsto(1-\alpha,1-\beta)$ (p. 279).
- $\mathcal R(P,Q)$ is the closed convex hull of the points from deterministic tests; on a finite alphabet it is a polygon (p. 279).
- The log-likelihood ratio (LLR), defined also when $P\not\ll Q$, is a sufficient statistic for $P$ vs $Q$. Expectations under $P$ and $Q$ are related by $e^{\pm T}$ (p. 281–282).
- Converse bounds: the weak one uses only $D(P\|Q)$ via data processing. The strong one uses the whole LLR distribution via half-planes (p. 282–283).
- Neyman-Pearson lemma: $\beta_\alpha$ is attained by a test that accepts $H_0$ when the LLR is above a threshold $\tau$, rejects below it, and randomizes with probability $\lambda$ at the threshold (p. 284).
- Achievability: for every $\tau$ some test has $\alpha=P[\text{LLR}>\tau]$ and $\beta\le e^{-\tau}\alpha$ (p. 285–286).
- Stein's lemma: for i.i.d. data the best exponent $V_\epsilon$ of the type-II error $\beta$, when the other error is at most $\epsilon$, equals $D(P\|Q)$ for every $\epsilon\in(0,1)$. The proof needs the strong converse (p. 287–288).
- Chernoff regime (both errors exponentially small) needs large deviations. Hellinger-distance bounds on the minimal total error give $E_H\le E\le 2E_H$ for its exponent $E=\max\min(E_0,E_1)$, with $E_H$ as printed (see Reading notes) (p. 289).

## L3 — Walkthrough

### 14.1 Neyman-Pearson formulation
**Setup.** $H_0: X\sim P$ (null) versus $H_1: X\sim Q$ (alternative). Both hypotheses are "simple": one distribution each (p. 276). A test is deterministic, $f(x)=\mathbf 1\{x\in E\}$ with decision region $E$, or randomized, $P_{Z|X}(1|x)\in[0,1]$. $Z=0$ means accept $H_0$ (choose $P$); $Z=1$ means reject (p. 276).

**Two metrics.** With $\pi_{i|j}$ = probability of choosing $i$ when $j$ is true (p. 277):
$$\alpha=\pi_{0|0}=P[Z=0],\qquad \beta=\pi_{0|1}=Q[Z=0].$$
Table 14.1 translates names. Type-I error (false alarm) is $1-\alpha$. Power is $1-\beta$. Type-II error (missed detection) is $\beta$. Metrics such as accuracy and F1 also need a prior $\pi_1=\mathbb P[H_1]$ (p. 277).

**Three ways to choose a "best" test** (p. 277):
- Bayesian: minimize $\pi_0\pi_{1|0}+\pi_1\pi_{0|1}$ \tag{14.1}
- Minimax: minimize $\max\{\pi_{1|0},\pi_{0|1}\}$.
- Neyman-Pearson: minimize $\beta$ subject to success probability under the null at least $\alpha$. This is the formulation used in this Part.

**Definition 14.1.** $\mathcal R(P,Q)=\{(P[Z=0],Q[Z=0]):P_{Z|X}\}\subset[0,1]^2$ \tag{14.2}. Its lower boundary is $\beta_\alpha(P,Q)\triangleq\inf_{P[Z=0]\ge\alpha}Q[Z=0]$ \tag{14.3} (p. 278).
- $P=Q$ gives the diagonal. $P\perp Q$ (mutually singular: $P[E]=0$, $Q[E]=1$ for some $E$) gives the full square (Fig. 14.1, p. 278).
- $\mathcal R$ encodes every $f$-divergence. TV is half the longest vertical segment in $\mathcal R$ (Exercise III.7).
- $\mathrm{AUC}(P,Q)\triangleq1-\int_0^1\beta_\alpha\,d\alpha$ (p. 278).

**Theorem 14.2.** (a) $\mathcal R$ is closed and convex. (b) It contains the diagonal. (c) $(\alpha,\beta)\in\mathcal R\Leftrightarrow(1-\alpha,1-\beta)\in\mathcal R$ (p. 279).
- Convexity: randomizing $\lambda P_{Z_0|X}+\bar\lambda P_{Z_1|X}$ gives $(\lambda\alpha_0+\bar\lambda\alpha_1,\lambda\beta_0+\bar\lambda\beta_1)$.
- Closedness follows from the NP lemma (Remark 14.1). In more complicated situations closedness can frequently still be argued: $\{g:\mathcal X\to[0,1]\}$ is weakly compact and its image under the linear map $g\mapsto(\int g\,dP,\int g\,dQ)$ is closed.
- (b) Guessing independently of $X$, with $Z\sim\mathrm{Ber}(1-\alpha)$, gives $(\alpha,\alpha)$.
- (c) Flip the decision: $P_{1-Z|X}$.

**Theorem 14.3.** $\mathcal R(P,Q)=\mathrm{cl}(\mathrm{co}(\mathcal R_{\det}(P,Q)))$, where $\mathcal R_{\det}=\{(P(E),Q(E))\}$ \tag{14.4}. On a finite alphabet $\mathcal R$ is a polygon with at most $2^{|\mathcal X|}$ vertices (p. 279–280).
- "$\supset$" holds since $\mathcal R$ is closed, convex and contains $\mathcal R_{\det}$.
- "$\subset$": put $g(x)=P_{Z|X}(0|x)$. The area rule $\mathbb E[U]=\int_0^\infty\mathbb P[U\ge t]dt$ for $U\ge0$ gives $P[Z=0]=\int_0^1P[g(X)\ge t]dt$ and $Q[Z=0]=\int_0^1Q[g(X)\ge t]dt$.
- So the point is a mixture, over $t$ uniform on $[0,1]$, of deterministic-test points $(P[g\ge t],Q[g\ge t])$.

*Intuition note.* A randomized test is a mixture of threshold-cut deterministic tests. So only the deterministic points matter, and the region is just their closed convex hull.

**Example 14.1.** For $p<\tfrac12<q$ and $\mathrm{Ber}(p)$ vs $\mathrm{Ber}(q)$ there are $2^2=4$ events $\emptyset,\{0\},\{1\},\{0,1\}$. The region is a parallelogram with vertices $(0,0)$, $(p,q)$, $(1,1)$, $(\bar p,\bar q)$ (p. 280, figure).

### 14.2 Likelihood ratio tests
**Definition 14.4 (extended LLR).** With $dP=p\,d\mu$, $dQ=q\,d\mu$ (p. 280):
$$T(x)\triangleq\mathrm{Log}\frac{p(x)}{q(x)}=\begin{cases}\log\frac{p}{q}&p>0,q>0\\+\infty&p>0,q=0\\-\infty&p=0,q>0\\0&p=0,q=0.\end{cases}$$
**Definition 14.5 (LRT).** With threshold $\tau\in\mathbb R\cup\{\pm\infty\}$: declare $H_0$ if $T(x)>\tau$, declare $H_1$ if $T(x)\le\tau$ (p. 281). It is deterministic. The author writes $\log\frac{dP}{dQ}$ for the extended LLR throughout (p. 281).

**Discrete identity** (assuming $Q\ll P$): $Q[T=t]=e^{-t}P[T=t]$ for $t\in\mathbb R\cup\{+\infty\}$ (p. 281).

**Theorem 14.6 (change of measure).** For any $h$ (p. 281):
$$\mathbb E_Q[h(X)\mathbf 1\{T>-\infty\}]=\mathbb E_P[h(X)e^{-T}]\tag{14.5}$$
$$\mathbb E_P[h(X)\mathbf 1\{T<+\infty\}]=\mathbb E_Q[h(X)e^{T}]\tag{14.6}$$
For $f\ge0$ and $-\infty<\tau<\infty$:
$$\mathbb E_Q[f\mathbf 1\{T\ge\tau\}]\le\mathbb E_P[f\mathbf 1\{T\ge\tau\}]e^{-\tau},\qquad \mathbb E_Q[f\mathbf 1\{T\le\tau\}]\ge\mathbb E_P[f\mathbf 1\{T\le\tau\}]e^{-\tau}.\tag{14.7}$$
(The second line is printed with $\mathbf 1\{T\ge\tau\}$ on the right; see Reading notes.)
- Proof. First, $Q[T=+\infty]=P[T=-\infty]=0$ \tag{14.8}. Then $\mathbb E_Q[h\mathbf 1\{T>-\infty\}]=\int_{\{-\infty<T<\infty\}}q\,h\,d\mu=\int_{\{-\infty<T<\infty\}}p\,e^{-T}h\,d\mu=\int_{\{-\infty<T\le\infty\}}p\,e^{-T}h\,d\mu$. The steps use (14.8), then $e^{-T}=q/p$ for $p,q>0$, then $e^{-T}=0$ when $T=\infty$ (pp. 281–282).
- Swapping $P,Q$ gives (14.6). Part 2 takes $h=f\mathbf 1\{T\ge\tau\}$ in (14.5) and $h=f\mathbf 1\{T\le\tau\}$ in (14.6) (p. 282).

**Corollary 14.7.** $T(X)$ is a sufficient statistic for $P$ vs $Q$. For discrete $\mathcal X$: $P_{X|T}(x|t)=\frac{P(x)\mathbf 1\{P/Q=e^t\}}{P_T(t)}=\frac{e^tQ(x)\mathbf 1\{P/Q=e^t\}}{P_T(t)}=\frac{Q_{XT}(x,t)}{e^{-t}P_T(t)}=Q_{X|T}(x|t)$. The general case is left as an exercise (p. 282).

*Intuition note.* Once you know the likelihood ratio, the raw data $x$ adds nothing for telling $P$ from $Q$. So tests can be built from the one-dimensional $T$.

### 14.3 Converse bounds on $\mathcal R(P,Q)$
**Theorem 14.8 (weak converse).** For all $(\alpha,\beta)\in\mathcal R$: $d(\alpha\|\beta)\le D(P\|Q)$ and $d(\beta\|\alpha)\le D(Q\|P)$, with $d$ the binary divergence. Proof: data processing for KL through $P_{Z|X}$ (p. 282).

**Lemma 14.9.** For any test $Z$ and $\gamma>0$: $P[Z=0]-\gamma Q[Z=0]\le P[T>\log\gamma]$. No assumption $P\ll Q$ is needed, because $\pm\infty$ are allowed LLR values (p. 283).
- Proof. With $\tau=\log\gamma$, (14.7) gives $P[Z=0,T\le\tau]-\gamma Q[Z=0,T\le\tau]\le0$. Split $P[Z=0]$ and $Q[Z=0]$ over $\{T\le\tau\}$ and $\{T>\tau\}$. What remains is at most $P[T>\log\gamma,Z=0]-\gamma Q[\dots]\le P[T>\log\gamma]$ (p. 283).

**Theorem 14.10 (strong converse).** For all $(\alpha,\beta)\in\mathcal R$ and $\gamma>0$ (proof: Lemma 14.9 for $(P,Q,\gamma)$ and $(Q,P,1/\gamma)$):
$$\alpha-\gamma\beta\le P\!\left[\log\tfrac{dP}{dQ}>\log\gamma\right]\tag{14.9}$$
$$\beta-\tfrac1\gamma\alpha\le Q\!\left[\log\tfrac{dP}{dQ}<\log\gamma\right]\tag{14.10}$$
So $\mathcal R$ lies in an intersection of half-planes indexed by $\gamma$ (p. 283). The strong converse needs the CDF of the LLR; the weak one needs only its mean, $D$ (p. 283).

### 14.4 Achievability bounds and the NP lemma
**Supporting lines.** Maximizing $\alpha-t\beta$ over $\mathcal R$ is the same as minimizing the Bayesian error (14.1) with $t=\pi_1/\pi_0$ (p. 284). For discrete $\mathcal X$:
$$\max_{(\alpha,\beta)\in\mathcal R}(\alpha-t\beta)=\max_{P_{Z|X}}\sum_x(P(x)-tQ(x))P_{Z|X}(0|x)=\sum_x|P(x)-tQ(x)|^+,$$
attained by $P_{Z|X}(0|x)=\mathbf 1\{\log\frac{P(x)}{Q(x)}\ge\log t\}$. So all supporting lines come from LRTs. Only the flat faces of $\mathcal R$ are not recovered this way (p. 284).

**Theorem 14.11 (Neyman-Pearson lemma).** For each $\alpha$, $\beta_\alpha$ is attained by
$$P_{Z|X}(0|x)=\begin{cases}1&\log\frac{dP}{dQ}>\tau\\ \lambda&\log\frac{dP}{dQ}=\tau\\0&\log\frac{dP}{dQ}<\tau\end{cases}\tag{14.11}$$
where $\tau\in\mathbb R$, $\lambda\in[0,1]$ are the unique solutions of $\alpha=P[\log\frac{dP}{dQ}>\tau]+\lambda P[\log\frac{dP}{dQ}=\tau]$ (p. 284).

*Proof* (p. 284). Let $t=e^\tau$, $g(x)=P_{Z|X}(0|x)$. Assume $\mathbb E_P[g]=\alpha=P[\frac{dP}{dQ}>t]+\lambda P[\frac{dP}{dQ}=t]$ \tag{14.12}. Goal: $\beta=\mathbb E_Q[g]\ge Q[\frac{dP}{dQ}>t]+\lambda Q[\frac{dP}{dQ}=t]$ \tag{14.13}. Use $\mathbb E_Q[f\mathbf 1\{\frac{dP}{dQ}\le t\}]\ge t^{-1}\mathbb E_P[f\mathbf 1\{\frac{dP}{dQ}\le t\}]$ twice:
1. $\beta=\mathbb E_Q[g\mathbf 1\{\le t\}]+\mathbb E_Q[g\mathbf 1\{>t\}]\ge\frac1t\mathbb E_P[g\mathbf 1\{\le t\}]+\mathbb E_Q[g\mathbf 1\{>t\}]$.
2. By (14.12), $\mathbb E_P[g\mathbf 1\{\le t\}]=\mathbb E_P[(1-g)\mathbf 1\{>t\}]+\lambda P[=t]$. (added step) This is because $\mathbb E_P[g]$ equals the total NP mass, so the mass of $g$ on $\{\le t\}$ equals the mass the NP test has but $g$ lacks on $\{>t\}$.
3. Second use (the source only says "twice"; added step): on $\{>t\}$ with $f=1-g$ one needs the opposite-direction bound $\mathbb E_Q[f\mathbf 1\{>t\}]\le\frac1t\mathbb E_P[f\mathbf 1\{>t\}]$ (from (14.7)), and on $\{=t\}$ one has $P[=t]=tQ[=t]$. Then $\frac1t(\dots)\ge\mathbb E_Q[(1-g)\mathbf 1\{>t\}]+\lambda Q[=t]$.
4. Add $\mathbb E_Q[g\mathbf 1\{>t\}]$: the total is $Q[>t]+\lambda Q[=t]$.

*Intuition note.* To get a given $\alpha$ at least cost in $\beta$, accept $H_0$ on the points where $P/Q$ is largest, as in the fractional-knapsack idea. Randomizing on the boundary level fills the budget exactly.

**Remark 14.1.** All boundary points are attainable: $\mathcal R=\{(\alpha,\beta):\beta_\alpha\le\beta\le1-\beta_{1-\alpha}\}$. $\alpha\mapsto\beta_\alpha$ is convex, hence continuous, so $\mathcal R$ is closed and the infimum in (14.3) is a minimum. It suffices to use tests $\mathbf 1\{\log\frac{dP}{dQ}\ge\tau\}$ or $\mathbf 1\{\log\frac{dP}{dQ}>\tau\}$ and mix them (p. 285).

**Remark 14.2.** If $\alpha=P[\log\frac{dP}{dQ}>\tau]$ for some $\tau$, then $\lambda=0$ and (14.11) is an LRT. Otherwise $\lambda\in(0,1)$ and (14.11) randomizes between two LRTs (probabilities $1-\lambda$ and $\lambda$) (p. 285).

**Corollary 14.12.** For every $\tau\in\mathbb R$ there is $(\alpha,\beta)\in\mathcal R$ with $\alpha=P[\log\frac{dP}{dQ}>\tau]$ and $\beta\le e^{-\tau}P[\log\frac{dP}{dQ}>\tau]\le e^{-\tau}$. Discrete proof: $Q[\log\frac PQ>\tau]=\sum Q(x)\mathbf 1\{P/Q>e^\tau\}\le\sum P(x)e^{-\tau}\mathbf 1\{\cdot\}$. The general case follows from (14.7) (pp. 285–286).

### 14.5 Asymptotics: Stein's regime
**Setting.** I.i.d. data $H_0:X_1..X_n\sim P$ vs $H_1:X_1..X_n\sim Q$ \tag{14.14}. Stein's regime: $\pi_{1|0}\le\epsilon$, find the best exponential rate of $\pi_{0|1}$. Chernoff's regime: both errors vanish exponentially; find the exponent trade-off (p. 286). The asymmetry is motivated by missed detection being often worse than false alarm (p. 286).

**Definition 14.13.** $V_\epsilon\triangleq\sup\{E:\exists n_0,\forall n\ge n_0,\exists P_{Z|X^n}\ \text{s.t.}\ \alpha>1-\epsilon,\beta<e^{-nE}\}$. Stein's exponent is $V\triangleq\lim_{\epsilon\to0}V_\epsilon$. The text leaves as an exercise the check of the equivalent form $V_\epsilon=\liminf\frac1n\log\frac1{\beta_{1-\epsilon}(P_{X^n},Q_{X^n})}$ (pp. 286–287).

**Theorem 14.14 (Stein's lemma).** $V_\epsilon=D(P\|Q)$ for all $\epsilon\in(0,1)$, hence $V=D(P\|Q)$ (p. 287). Rule of thumb for $\alpha\ge0.999$, $\beta\le10^{-40}$: $n\ge-\frac{\log10^{-40}}{D(P\|Q)}$ (p. 287).

*Proof, case $P\ll Q$* (p. 287–288). Let $F_n=\log\frac{dP_{X^n}}{dQ_{X^n}}=\sum_{i=1}^n\log\frac{dP}{dQ}(X_i)$ \tag{14.15}. By the WLLN, $\frac1nF_n\to D(P\|Q)$ in probability under $P$ \tag{14.16} and $\to-D(Q\|P)$ under $Q$ \tag{14.17}. Both hold even if the divergence is infinite.
- *Achievability* ($V_\epsilon\ge D$). If $D<\infty$, take $\tau=n(D-\delta)$. Corollary 14.12 gives $\alpha=P(F_n>n(D-\delta))\to1$ and $\beta\le e^{-n(D-\delta)}$. For $n$ large, $\alpha\ge1-\epsilon$, so $V_\epsilon\ge D-\delta$. Let $\delta\to0$. If $D=\infty$ the argument works for arbitrary $\tau>0$.
- *Weak converse.* From Theorem 14.8: $-h(\alpha)+\alpha\log\frac1\beta\le d(\alpha\|\beta)\le D(P_{X^n}\|Q_{X^n})$ \tag{14.18} (added step: for the i.i.d. product measures this equals $nD$). With $\alpha_n\ge1-\epsilon$, $\beta_n\le e^{-nE}$ and $h\le\log2$: $E\le\frac{D}{1-\epsilon}+\frac{\log2}{n(1-\epsilon)}$. So $V_\epsilon\le D/(1-\epsilon)$. This is tight as $\epsilon\to0$ but weaker for fixed $\epsilon$.
- *Strong converse.* Apply Theorem 14.10 with $\alpha=1-\epsilon$, $\beta=e^{-nE}$: $1-\epsilon-\gamma e^{-nE}\le\alpha_n-\gamma\beta_n\le P_{X^n}[F_n>\log\gamma]$. Take $\gamma=e^{n(D+\delta)}$. The right side goes to 0 by (14.16). (Added step: if $E>D+\delta$, the left side would tend to $1-\epsilon>0$, a contradiction.) So $E\le D+\delta$ and $V_\epsilon\le D+\delta$. Let $\delta\to0$.
- *Case $P\not\ll Q$.* Then $D=\infty$. There is $A$ with $Q(A)=0<P(A)$. The test "choose $P$ if some $X_i\in A$" has $\beta=0$ and $1-\alpha=(1-P(A))^n$, which is below any $\epsilon$ for large $n$. So $V_\epsilon=\infty$.

*Intuition note.* Under $P$ the LLR per sample concentrates at $D(P\|Q)$. Setting the threshold just below it keeps $\alpha$ near 1 while $\beta$ is forced down at rate about $D$. The strong converse shows that allowing a large $\epsilon$ does not help the exponent.

**Remark 14.3.** For stationary ergodic processes under both $P$ and $Q$, $V_\epsilon=\lim\frac1nD(P_{X^n}\|Q_{X^n})$, the relative entropy rate. The WLLN is replaced by the Birkhoff–Khintchine theorem. Stein's exponent also gives a change-of-measure bound: $P_{X^n}[E]\ge1-\epsilon\Rightarrow Q_{X^n}[E]\ge\exp(-nV_\epsilon+o(n))$ for all sets $E$ (p. 288).

### 14.6 Chernoff regime: preview
A pair $(E_0,E_1)$ is achievable if some tests have $1-\alpha=\pi_{1|0}\le e^{-nE_0}$ and $\beta=\pi_{0|1}\le e^{-nE_1}$. The problem is solved in Chapter 16 (p. 289).
- Stein's regime gives the corner points $(0,D(P\|Q))$ and $(D(Q\|P),0)$ (p. 289).
- The minimum total error over all tests is $1-\mathrm{TV}(P^n,Q^n)$ (Section 7.3). Its exponent $E$ equals $\max\min(E_0,E_1)$. Hellinger bounds give $1-\sqrt{1-\exp(-2nE_H)}\le1-\mathrm{TV}(P^n,Q^n)\le\exp(-nE_H)$ \tag{14.19}, with $E_H\triangleq\log(1-\tfrac12H^2(P,Q))$ as printed. Hence $E_H\le E\le2E_H$ (p. 289).
- For fixed $P,Q$ this is not precise. Optimal LRTs give $1-\alpha_n=P[\frac1nF_n\le\tau]$ and $\beta_n=Q[\frac1nF_n>\tau]$. For $\tau\in(-D(Q\|P),D(P\|Q))$ both vanish by the WLLN. Their exact rates are a large-deviations question (p. 290).

## Toy example (ours)
Let $\mathcal X=\{a,b,c\}$, $P=(0.5,0.3,0.2)$, $Q=(0.2,0.3,0.5)$. Ratios $P/Q$: $a:2.5$, $b:1$, $c:0.4$. Target $\alpha=0.65$.
- Take $\tau=\log1=0$, i.e. $t=1$. $P[P/Q>1]=P(a)=0.5$ and $P[P/Q=1]=P(b)=0.3$. Solve $0.65=0.5+\lambda\cdot0.3$, giving $\lambda=0.5$.
- $\beta=Q(a)+\lambda Q(b)=0.2+0.5\cdot0.3=0.35$. So $\beta_{0.65}=0.35$.
- Check by mixing deterministic tests: $E=\{a\}$ gives $(0.5,0.2)$ and $E=\{a,b\}$ gives $(0.8,0.5)$. The midpoint at $\alpha=0.65$ is $(0.65,0.35)$, matching.
- A competitor: accept on $a$ always and on $c$ with probability $x$, with $0.5+0.2x=0.65$, so $x=0.75$. Then $\beta=0.2+0.75\cdot0.5=0.575>0.35$. Random guessing gives $\beta=0.65$. The NP test is best.

## Concepts
- [[neyman-pearson-region]] (new) — set $\mathcal R(P,Q)$ of $(P[Z=0],Q[Z=0])$ over all randomized tests; boundary is $\beta_\alpha$ (p. 278)
- [[likelihood-ratio-test]] (new) — deterministic threshold test on the extended LLR $T$; optimal by the NP lemma when no randomization at the threshold is needed ($\lambda=0$), otherwise the optimal test randomizes there (p. 281, 284, 285)
- [[log-likelihood-ratio]] (new) — $T(x)=\mathrm{Log}\,p/q$, with values $\pm\infty$ allowed; sufficient statistic (p. 280, 282)
- [[relative entropy / KL divergence]] — $D(P\|Q)$; here, the optimal Stein exponent (p. 287)
- [[data processing inequality]] — gives the weak converse $d(\alpha\|\beta)\le D(P\|Q)$ (p. 282)
- [[f-divergence]] — all of them can be computed from $\mathcal R(P,Q)$; TV example (p. 278)
- [[stein-regime]] (new) — $\pi_{1|0}\le\epsilon$ fixed, maximize exponent of $\pi_{0|1}$ (p. 286)
- [[chernoff-regime]] (new) — both errors exponentially small; trade-off of $(E_0,E_1)$ (p. 289)
- [[entropy rate]] — here the relative entropy rate is the Stein exponent for stationary ergodic data (under both $P$ and $Q$) (p. 288)

## Canonical instances
- [[bernoulli-testing]] — $\mathrm{Ber}(p)$ vs $\mathrm{Ber}(q)$ region is a parallelogram (p. 280)
- [[packet-detection-asymmetry]] — false alarm as extra computation vs missed detection as lost packet (p. 286)
- [[stein-sample-size-rule]] — $n\ge-\log(10^{-40})/D(P\|Q)$ for $\alpha\ge0.999$ (p. 287)

## Bridges (candidates)
- [same-math] Optimal Bayesian test with $t=\pi_1/\pi_0$ ↔ supporting lines of $\mathcal R(P,Q)$ — the same maximization $\max(\alpha-t\beta)$ (p. 284)
- [structural-analogy] Weak vs strong converse (mean of LLR vs full CDF) ↔ channel coding: the same weak/strong converse pattern (p. 283)
- [structural-analogy] Stein exponent $D(P\|Q)$ for $n$ samples ↔ source coding/data compression: LLN-based argument, extended to ergodic data via Birkhoff–Khintchine (p. 288)
- [structural-analogy] ROC/AUC ↔ machine learning: the author states AUC is a popular quality metric (p. 278)

## Questions this raises
- How exactly do the two exponents $(E_0,E_1)$ trade off in the Chernoff regime (the chapter promises Chapter 16)?
- How do large-deviations rates of $P[\frac1nF_n\le\tau]$ and $Q[\frac1nF_n>\tau]$ look?
- Why can the weak converse be tight as $\epsilon\to0$ but not for fixed $\epsilon<1$?
- What replaces the NP lemma for composite hypotheses, where no simple explicit solution exists (p. 279)?

## Exercises worth doing
The unit has no numbered exercises of its own, but points to these.
- Exercise III.7 (p. 278) — TV equals half the longest vertical segment of $\mathcal R(P,Q)$ — difficulty: medium
- Equivalent definition of $V_\epsilon$ via $\beta_{1-\epsilon}$ (p. 287) — "an exercise to check" — difficulty: medium
- General case of Corollary 14.7 (sufficiency of $T$ beyond discrete $\mathcal X$) (p. 282) — difficulty: hard

## Reading notes
- Printed pages 276–290 = pdf 301–315 (printed = pdf − 25). The chapter is numbered 14 on the page. The file id says ch16.
- Misprint in (14.7): the second line shows $\mathbf 1\{T\ge\tau\}$ on the right. The proof of Lemma 14.9 needs $\mathbf 1\{T\le\tau\}$, which I used there.
- Proof of Thm 14.6 ends with "$\mathbb E_P[\exp(-T)g(T)]$"; this should presumably be with $h$. Corollary 14.7's proof says "For part 2". Corollary 14.12's proof has "$\exp(tau)$".
- In the Stein converse (p. 288) the text writes $V=\lim_{\epsilon\to0}V_\epsilon\ge D(P\|Q)$ after the weak converse. The weak converse gives "$\le$", so "$\ge$" is presumably a misprint.
- $E_H$ is printed as $\log(1-\frac12H^2)$, which is negative. Since (14.19) uses $\exp(-nE_H)$, a sign (or $\log\frac{1}{\cdot}$) is probably intended. I reproduced the print.
- Table 14.1's PPV formula and the Chernoff reference "[218, 61]" were not checked. Forward references (Sections 16.4, 32.2.1; Chapters 15, 16) point outside this unit.
