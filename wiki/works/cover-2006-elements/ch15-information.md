---
id: cover-2006-elements/ch15-information
work: cover-2006-elements
unit: "15 Information Theory and the Stock Market"
pages: 459–481
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Information Theory and the Stock Market

## L0 — One line
Maximizing the expected log of daily wealth (the doubling rate) gives a portfolio that is optimal for long-run growth, one-day expected ratio and competitive play, and its mathematics mirrors entropy, the AEP and mutual information.

## L1 — The gist (≤ 120 words)
Reinvested wealth is a product of daily factors, so its long-run growth is governed by the expected logarithm, not the mean. The chapter defines the doubling rate and the log-optimal portfolio. It characterizes that portfolio by Kuhn–Tucker conditions and proves that, with probability 1, no causal rival (one using only past data) grows faster to first order in the exponent. Wrong beliefs cost at most $D(f\|g)$ in doubling rate. Side information adds at most $I(X;Y)$. For stationary markets $W$ obeys a chain rule like $H$, and an AEP holds. In one period, with fair randomization, any rival matches or beats the log-optimal portfolio with probability at most 1/2. The Shannon–McMillan–Breiman theorem is proved by a sandwich argument.

**Prerequisites:** expectation, Jensen's inequality, Markov inequality, strong law of large numbers; concavity; KL divergence, mutual information, entropy rate, AEP (i.i.d. case), Borel–Cantelli lemma.

## L2 — Key ideas (5–10 bullets)
- Wealth compounds as a product, so the doubling rate $W(\mathbf b,F)=E\log \mathbf b^t\mathbf X$ replaces mean–variance as the objective; for i.i.d. markets $\frac1n\log S_n^*\to W^*$ almost surely, where $S_n^*$ is the wealth under the log-optimal portfolio $\mathbf b^*$ (pp. 460–461).
- $W$ is concave in $\mathbf b$ and linear in $F$; $W^*$ is convex in $F$. Hence log-optimal portfolios (maximizers of $W$) form a convex set and the Kuhn–Tucker conditions (standard optimality conditions for constrained maximization) $E(X_i/\mathbf b^{*t}\mathbf X)\le 1$ (equality where $b_i^*>0$) are necessary and sufficient (pp. 461–463).
- $E\log(S/S^*)\le 0$ for all portfolios is equivalent to $E(S/S^*)\le 1$ for all portfolios, where $S^*$ is the wealth under the log-optimal portfolio. The expected wealth fractions stay at $\mathbf b^*$ from day to day (pp. 464–465).
- In an i.i.d. market, for almost every market sequence, $\limsup \frac1n\log (S_n/S_n^*)\le 0$ against any causal strategy (one using only past market data), so no rival grows faster to first order in the exponent (p. 466; stationary case p. 470).
- Using the log-optimal portfolio of $g$ when the truth is $f$ loses at most $D(f\|g)$. Side information $Y$ raises the doubling rate by at most $I(X;Y)$ (pp. 467–468).
- For stationary markets, $W^*$ obeys a chain rule like that of $H$ ("conditioning reduces $H$ but increases $W$"). $W^*_\infty$ is the limit of conditional doubling rates. An AEP (asymptotic equipartition property) holds for stationary ergodic markets, i.e. processes for which a law of large numbers holds (pp. 469–471).
- One-period competitive optimality: with fair randomization ($U^*\sim[0,2]$, $V\ge0$, $EV=1$), $\Pr(VS\ge U^*S^*)\le 1/2$ (p. 472).
- Horse race as special case: $W^*=\log m-H(X)$ with uniform fair odds (p. 473).
- The Shannon–McMillan–Breiman theorem is proved by sandwiching $-\frac1n\log p(X_0^{n-1})$ between $H^\infty$ and $H^k$, using the ergodic theorem (pp. 474–479).

## L3 — Walkthrough

### 15.1 The stock market: some definitions (pp. 459–462)
- A market is a vector $\mathbf X=(X_1,\dots,X_m)$, $X_i\ge0$, of *price relatives* (end-of-day price ÷ start-of-day price), with $\mathbf X\sim F(\mathbf x)$. $X_i=1.03$ means stock $i$ rose 3% (p. 459).
- A *portfolio* $\mathbf b$ has $b_i\ge0$, $\sum b_i=1$. The *wealth relative* is $S=\mathbf b^t\mathbf X$ (p. 459).
- **Standard theory:** mean–variance (Sharpe–Markowitz). Maximize $E S$ for given variance. The boundary of achievable (mean, variance) pairs is the *efficient frontier*; a risk-free asset adds a tangent line to it (Fig. 15.1). The Capital Assets Pricing Model rests on this idea (pp. 459–460).
- **Author's point:** the mean describes sums of i.i.d. terms. Reinvesting daily makes wealth a product, whose behaviour is set by the expected logarithm (p. 460).

**Definition (doubling rate).**
$$W(\mathbf b,F)=\int\log \mathbf b^t\mathbf x\,dF(\mathbf x)=E(\log \mathbf b^t\mathbf X)\tag{15.1}$$
**Optimal doubling rate:** $W^*(F)=\max_{\mathbf b}W(\mathbf b,F)$ (15.2), over all portfolios. A maximizer $\mathbf b^*$ is *log-optimal* (p. 461).

**Theorem 15.1.1.** Let $\mathbf X_i$ be i.i.d. $\sim F$ and $S_n^*=\prod_{i=1}^n\mathbf b^{*t}\mathbf X_i$ (15.3), the wealth of the constant rebalanced portfolio $\mathbf b^*$. Then $\frac1n\log S_n^*\to W^*$ with probability 1 (15.4).
*Proof:* $\frac1n\log S_n^*=\frac1n\sum_i\log\mathbf b^{*t}\mathbf X_i\to W^*$ a.s. by the strong law of large numbers (15.5–15.6). Hence $S_n^*\doteq2^{nW^*}$, i.e. equal to first order in the exponent (p. 461, p. 466).

*Intuition note:* Each day multiplies wealth by a random factor. The average of the log-factors converges, so wealth grows like $2^{nW^*}$. The author's point is that the behaviour of the product of daily factors is set by the expected logarithm, not the expected value (p. 460).

**Lemma 15.1.1.** $W(\mathbf b,F)$ is concave in $\mathbf b$ and linear in $F$; $W^*(F)$ is convex in $F$.
*Proof:* Linearity in $F$ holds because the integral (15.7) is linear in $F$. Concavity of the logarithm gives
$$\log(\lambda\mathbf b_1+(1-\lambda)\mathbf b_2)^t\mathbf X\ge\lambda\log\mathbf b_1^t\mathbf X+(1-\lambda)\log\mathbf b_2^t\mathbf X\tag{15.8}$$
and taking expectations gives concavity in $\mathbf b$. For convexity of $W^*$, let $\mathbf b^*(\cdot)$ denote the log-optimal portfolio for a given distribution. By linearity,
$$W^*(\lambda F_1+(1-\lambda)F_2)=W(\mathbf b^*(\lambda F_1+(1-\lambda)F_2),\lambda F_1+(1-\lambda)F_2)\tag{15.9}$$
$$=\lambda W(\mathbf b^*(\cdot),F_1)+(1-\lambda)W(\mathbf b^*(\cdot),F_2)\le\lambda W(\mathbf b^*(F_1),F_1)+(1-\lambda)W(\mathbf b^*(F_2),F_2),\tag{15.10}$$
since $\mathbf b^*(F_i)$ maximizes $W(\cdot,F_i)$ (p. 462).

**Lemma 15.1.2.** The set of log-optimal portfolios is convex. *Proof:* a convex combination of two maximizers has doubling rate at least that of each (Lemma 15.1.1), so it also attains the maximum (p. 462).

### 15.2 Kuhn–Tucker characterization of the log-optimal portfolio (pp. 462–465)
Maximizing a concave function over a convex set (the simplex); the maximum may lie on the boundary. The author derives the conditions from first principles.

**Theorem 15.2.1.** $\mathbf b^*$ is log-optimal iff
$$E\!\left(\frac{X_i}{\mathbf b^{*t}\mathbf X}\right)\begin{cases}=1&\text{if }b_i^*>0\\ \le1&\text{if }b_i^*=0\end{cases}\tag{15.11, 15.17}$$
*Proof:* By concavity, $\mathbf b^*$ is optimal iff the directional derivative towards every portfolio $\mathbf b$ is $\le0$. With $\mathbf b_\lambda=(1-\lambda)\mathbf b^*+\lambda\mathbf b$,
$$\left.\tfrac{d}{d\lambda}W(\mathbf b_\lambda)\right|_{\lambda=0+}\le0\tag{15.12}$$
The one-sided derivative is
$$\lim_{\lambda\downarrow0}\tfrac1\lambda E\log\frac{(1-\lambda)\mathbf b^{*t}\mathbf X+\lambda\mathbf b^t\mathbf X}{\mathbf b^{*t}\mathbf X}\tag{15.13}$$
$$=E\Big(\lim_{\lambda\downarrow0}\tfrac1\lambda\log\big(1+\lambda(\tfrac{\mathbf b^t\mathbf X}{\mathbf b^{*t}\mathbf X}-1)\big)\Big)\tag{15.14}$$
$$=E\Big(\frac{\mathbf b^t\mathbf X}{\mathbf b^{*t}\mathbf X}\Big)-1\tag{15.15}$$
The limit and expectation may be interchanged by dominated convergence. So the condition is $E(\mathbf b^t\mathbf X/\mathbf b^{*t}\mathbf X)-1\le0$ for all $\mathbf b$ (15.16). If the segment from $\mathbf b$ to $\mathbf b^*$ extends beyond $\mathbf b^*$ in the simplex, the two-sided derivative vanishes and (15.16) holds with equality. Otherwise it is only an inequality. Since the expression is linear in $\mathbf b$, it suffices to check the extreme points (the $j$th vertex). The segment from the $j$th vertex can be extended beyond $\mathbf b^*$ iff $b_j^*>0$. This gives (15.17) (pp. 463).

*Intuition note:* At the optimum, each stock held in positive amount has expected ratio $E(X_i/\mathbf b^{*t}\mathbf X)$ exactly 1 (the "marginal value" reading is ours). A stock not held cannot have expected ratio above 1.

**Theorem 15.2.2.** With $S^*=\mathbf b^{*t}\mathbf X$ and $S=\mathbf b^t\mathbf X$ for any $\mathbf b$: $E\,S/S^*\le1$ (15.18). Conversely, if $E(S/S^*)\le1$ for all $\mathbf b$, then $E\log S/S^*\le0$ for all $\mathbf b$. Symmetric form: $E\ln\frac S{S^*}\le0\ \forall S\iff E\frac S{S^*}\le1\ \forall S$ (15.19).
*Proof:* (15.11) gives $E(X_i/\mathbf b^{*t}\mathbf X)\le1$ for all $i$ (15.20). Multiply by $b_i$ and sum: $\sum b_iE(X_i/\mathbf b^{*t}\mathbf X)\le\sum b_i=1$ (15.21), i.e. $E\frac{\mathbf b^t\mathbf X}{\mathbf b^{*t}\mathbf X}=E\frac S{S^*}\le1$ (15.22). The converse follows from Jensen: $E\log\frac S{S^*}\le\log E\frac S{S^*}\le\log1=0$ (15.23) (p. 464).

The author concludes that log-optimality is equivalent to expected-ratio optimality. The log-optimal portfolio therefore also "maximizes" the one-day wealth relative, not only asymptotic growth (p. 464).

**Constant expected proportions.** Starting from $\mathbf b^*$, the expected fraction in stock $i$ at day's end is
$$E\frac{b_i^*X_i}{\mathbf b^{*t}\mathbf X}=b_i^*E\frac{X_i}{\mathbf b^{*t}\mathbf X}=b_i^*\cdot1=b_i^*\tag{15.24}$$
(using equality in (15.11), which is applied for $b_i^*>0$; for $b_i^*=0$ the fraction is 0) (p. 465).

### 15.3 Asymptotic optimality (pp. 465–467)
Setting: i.i.d. market; investor uses $\mathbf b_i$ on day $i$, $S_n=\prod\mathbf b_i^t\mathbf X_i$ (15.25); $W^*=\max_{\mathbf b}E\log\mathbf b^t\mathbf X$ (15.26). Only *causal* strategies are allowed: $\mathbf b_i$ depends on the past and not on future market values (p. 465).

**Lemma 15.3.1.** $E\log S_n^*=nW^*\ge E\log S_n$ for any causal strategy (15.27).
*Proof:* $\max E\log S_n=\max E\sum\log\mathbf b_i^t\mathbf X_i$ (15.28); the maximum splits term by term, each over $\mathbf b_i(\mathbf X_1,\dots,\mathbf X_{i-1})$ (15.29). Each term is maximized by the constant $\mathbf b^*$ (15.30), giving $\sum E\log\mathbf b^{*t}\mathbf X_i=nW^*$ (15.31) (p. 466).

**Theorem 15.3.1 (asymptotic optimality).** For any causal $S_n$,
$$\limsup_{n\to\infty}\tfrac1n\log\frac{S_n}{S_n^*}\le0\ \text{ with probability 1}\tag{15.32}$$
*Proof:* From Kuhn–Tucker, $E\,S_n/S_n^*\le1$ (15.33). Markov: $\Pr(S_n>t_nS_n^*)<1/t_n$ (15.34), i.e. $\Pr(\frac1n\log\frac{S_n}{S_n^*}>\frac1n\log t_n)\le1/t_n$ (15.35). Take $t_n=n^2$: $\sum_n\Pr(\frac1n\log\frac{S_n}{S_n^*}>\frac{2\log n}n)\le\sum1/n^2=\pi^2/6$ (15.36). By Borel–Cantelli, the event $\{\cdot>2\log n/n\}$ happens infinitely often with probability 0 (15.37). So almost surely there is $N$ with $\frac1n\log\frac{S_n}{S_n^*}<\frac{2\log n}n$ for $n>N$, hence (15.38) (pp. 466–467).

*Intuition note:* No rival can grow faster in the exponent, except on a set of market histories of probability zero.

### 15.4 Side information and the doubling rate (pp. 467–468)
Chapter 6 showed that side information $Y$ raises the horse-race doubling rate by $I(X;Y)$ for uniform odds. Here $I(X;Y)$ is a possibly unachievable *upper bound* (p. 467).

**Theorem 15.4.1.** Let $\mathbf b_f^*$, $\mathbf b_g^*$ be log-optimal for densities $f$, $g$; $F$ is the true law ($f$). Then
$$\Delta W=W(\mathbf b_f^*,F)-W(\mathbf b_g^*,F)\le D(f\|g)\tag{15.39}$$
*Proof:*
$$\Delta W=\int f\log\mathbf b_f^{*t}\mathbf x-\int f\log\mathbf b_g^{*t}\mathbf x=\int f\log\frac{\mathbf b_f^{*t}\mathbf x}{\mathbf b_g^{*t}\mathbf x}\tag{15.40–15.41}$$
$$=\int f\log\frac{\mathbf b_f^{*t}\mathbf x}{\mathbf b_g^{*t}\mathbf x}\frac{g}{f}+D(f\|g)\tag{15.42–15.43}$$
$$\overset{(a)}\le\log\int f\frac{\mathbf b_f^{*t}\mathbf x}{\mathbf b_g^{*t}\mathbf x}\frac gf+D(f\|g)=\log\int g\frac{\mathbf b_f^{*t}\mathbf x}{\mathbf b_g^{*t}\mathbf x}+D(f\|g)\tag{15.44–15.45}$$
$$\overset{(b)}\le\log1+D(f\|g)=D(f\|g)\tag{15.46–15.47}$$
(a) is Jensen. (b) is Kuhn–Tucker for $g$: $\mathbf b_g^*$ is log-optimal for $g$, so the $g$-expectation of the ratio is $\le1$ (p. 468).

**Theorem 15.4.2.** $\Delta W\le I(X;Y)$ (15.48).
*Proof:* Given $Y=y$, the investor uses the log-optimal portfolio for $f(\mathbf x|Y=y)$. By 15.4.1, $\Delta W_{Y=y}\le D(f(\mathbf x|y)\|f(\mathbf x))$ (15.49). Averaging over $Y$:
$$\Delta W\le\int_y f(y)\int_{\mathbf x}f(\mathbf x|y)\log\frac{f(\mathbf x|y)}{f(\mathbf x)}=\iint f(\mathbf x,y)\log\frac{f(\mathbf x,y)}{f(\mathbf x)f(y)}=I(\mathbf X;Y)\tag{15.50–15.53}$$

*Intuition note:* Acting on a wrong model costs, in growth rate, at most the KL divergence between truth and model. Information about the market cannot be worth more growth than the mutual information it carries.

### 15.5 Investment in stationary markets (pp. 469–471)
Let $\mathbf X_1,\mathbf X_2,\dots$ be a vector process; $\mathbf b_i$ may depend on $\mathbf X_1,\dots,\mathbf X_{i-1}$. $S_n=\prod\mathbf b_i^t(\mathbf X_1,\dots,\mathbf X_{i-1})\mathbf X_i$ (15.54). The maximization splits per day (15.55), and the maximum is $\sum\log\mathbf b_i^{*t}\mathbf X_i$ (15.56), where $\mathbf b_i^*$ is log-optimal for the conditional law of $\mathbf X_i$ given the past. The conditional maximum is
$$\max_{\mathbf b}E[\log\mathbf b^t\mathbf X_i\mid(\mathbf X_1,\dots,\mathbf X_{i-1})=(\mathbf x_1,\dots,\mathbf x_{i-1})]=W^*(\mathbf X_i|\mathbf x_1,\dots,\mathbf x_{i-1})\tag{15.57}$$
and averaging over the past gives the conditional optimal doubling rate $W^*(\mathbf X_i|\mathbf X_1,\dots,\mathbf X_{i-1})$ (15.58). With $W^*(\mathbf X_1,\dots,\mathbf X_n)=\max E\log S_n$ (15.59):
$$W^*(\mathbf X_1,\dots,\mathbf X_n)=\sum_{i=1}^nW^*(\mathbf X_i|\mathbf X_1,\dots,\mathbf X_{i-1})\tag{15.60}$$
This is formally the chain rule for $H$; $W$ is in some ways the dual of $H$: conditioning reduces $H$ but increases $W$ (p. 470).

**Definition.** $W^*_\infty=\lim_n W^*(\mathbf X_1,\dots,\mathbf X_n)/n$ if the limit exists, undefined otherwise (15.61).

**Theorem 15.5.1.** For a stationary market the doubling rate exists and $W_\infty^*=\lim_nW^*(\mathbf X_n|\mathbf X_1,\dots,\mathbf X_{n-1})$ (15.62).
*Proof:* By stationarity the conditional terms are non-decreasing in $n$, so they have a limit (possibly $\infty$). Since $\frac{W^*(\mathbf X_1,\dots,\mathbf X_n)}n=\frac1n\sum_iW^*(\mathbf X_i|\mathbf X_1,\dots,\mathbf X_{i-1})$ (15.63), the Cesàro-mean theorem gives the same limit (15.64) (p. 470).

**Theorem 15.5.2.** For a stationary market and any causal strategy, $\limsup\frac1n\log(S_n/S_n^*)\le0$ (15.65). The proof uses $E\,S_n/S_n^*\le1$ (15.66), from repeated conditional Kuhn–Tucker conditions; the rest is as in the i.i.d. case (pp. 470–471).

**Theorem 15.5.3 (AEP for the stock market).** For a stationary ergodic process, $\frac1n\log S_n^*\to W^*$ with probability 1 (15.68). The proof (a modification of the sandwich argument of §15.7) is omitted (p. 471).

### 15.6 Competitive optimality (pp. 471–474)
From Kuhn–Tucker, $E\,S_n/S_n^*\le1$ (15.69), so by Markov $\Pr(S_n>tS_n^*)\le1/t$ (15.70). The author notes this is like the competitive optimality of Shannon codes (Chapter 5) (p. 471).

**Counterexample.** Two stocks:
$$(X_1,X_2)=\begin{cases}(1,1+\epsilon)&\text{prob. }1-\epsilon\\(1,0)&\text{prob. }\epsilon\end{cases}\tag{15.71}$$
$\mathbf b=(1,0)$ satisfies Kuhn–Tucker, so it is log-optimal. Yet an investor fully in stock 2 earns more with probability $1-\epsilon$. So one cannot prove the log-optimal investor wins with high probability, nor with probability at least one half. The fix is a fair randomization of initial wealth (p. 472).

**Theorem 15.6.1.** Let $S^*$ be one-period wealth under $\mathbf b^*$, $S$ under any other portfolio. Let $U^*$ be uniform on $[0,2]$, and $V\ge0$ with $EV=1$, both independent of $\mathbf X$ and each other. Then
$$\Pr(VS\ge U^*S^*)\le\tfrac12\tag{15.72}$$
*Proof:* $\Pr(VS\ge U^*S^*)=\Pr(W\ge U^*)$ with $W=VS/S^*\ge0$ (15.73–15.74). By independence and Kuhn–Tucker, $EW=E(V)E(S/S^*)\le1$ (15.75). With $F$ the distribution function of $W$:
$$\Pr(W\ge U^*)=\int_0^2\Pr(W>w)\tfrac12dw=\int_0^2\frac{1-F(w)}2dw\le\int_0^\infty\frac{1-F(w)}2dw=\tfrac12EW\le\tfrac12\tag{15.76–15.81}$$
using $EW=\int_0^\infty(1-F(w))dw$ for positive $W$ (15.82), proved by integrating by parts. Hence (15.83) (pp. 472–473).

*Remark (author):* $U,V$ are fair randomizations of initial wealth, achievable by a fair bet. If the only goal is to be ahead of an opponent at day's end and fair randomization is allowed, the investor should swap wealth for uniform $[0,2]$ wealth and then use $\mathbf b^*$. This is the "game theoretic solution" (p. 473).

*Intuition note:* The log-optimal portfolio can lose by a hair most of the time, as in (15.71). Randomizing initial wealth removes that edge: a rival's gain can be at most "fair" in expectation, so it wins at most half the time.

**Horse race as special case.** There are $m$ stocks, one per horse; $\mathbf X$ is non-zero only in the winner's component, with value $o_i$ (the odds). The log-optimal portfolio is proportional betting, $b_i^*=p_i$. For uniform fair odds
$$W^*=\log m-H(X)\tag{15.84}$$
For correlated races, the optimum is conditional proportional betting and
$$W^*=\log m-H(\mathcal X),\quad H(\mathcal X)=\lim\tfrac1nH(X_1,\dots,X_n)\text{ if it exists}\tag{15.85}$$
Theorem 15.5.3 then gives $S_n^*\doteq2^{nW^*}$ (15.86) (pp. 473–474).

### 15.7 The Shannon–McMillan–Breiman theorem (pp. 474–479)
The AEP for ergodic processes. The author says this section is technically heavier than the rest of the book and uses a "sandwich" argument to avoid some details (p. 474).

**Ergodic setup.** Probability space $(\Omega,\mathcal B,P)$ with a time-shift transformation $T$. $T$ is *stationary* if $\mu(TA)=\mu(A)$ for all $A\in\mathcal B$, and *ergodic* if every $A$ with $TA=A$ a.e. has $\mu(A)\in\{0,1\}$. Then $X_n(\omega)=X(T^n\omega)$ is stationary ergodic. **Birkhoff's ergodic theorem** (finite expected value):
$$\tfrac1n\sum_{i=1}^nX_i(\omega)\to EX=\int X\,dP\ \text{ w.p. 1}\tag{15.87}$$
This is a law of large numbers for ergodic processes (p. 474).

**Plan.** One wants $-\frac1n\log p(X_0,\dots,X_{n-1})=-\frac1n\sum_{i=0}^{n-1}\log p(X_i|X_0^{i-1})\to\lim E[-\log p(X_n|X_0^{n-1})]$ (15.88). But the sequence $p(X_i|X_0^{i-1})$ is not ergodic. The related quantities $p(X_i|X_{i-k}^{i-1})$ and $p(X_i|X_{-\infty}^{i-1})$ are ergodic, with expectations identified as entropy rates, and the target is sandwiched between them (pp. 474–475).

**Definitions.**
$$H^k=E\{-\log p(X_k|X_{k-1},\dots,X_0)\}=E\{-\log p(X_0|X_{-1},\dots,X_{-k})\}\tag{15.89–15.90}$$
(equal by stationarity). $H=\lim H^k=\lim\frac1n\sum_{k=0}^{n-1}H^k$ (15.91–15.92); $H^k\searrow H$ because conditioning does not increase entropy. Also $H^\infty=E\{-\log p(X_0|X_{-1},X_{-2},\dots)\}$ (15.93). Showing $H^\infty=H$ requires exchanging expectation and limit (p. 475).

*Motivating idea (author):* a gambler who knows the last $k$ outcomes has growth rate $1-H^k$ and one who knows the infinite past has $1-H^\infty$. A gambler with a growing past lies between, and the sandwich closes because $H^k\searrow H=H^\infty$ (p. 475).

**Theorem 15.7.1 (AEP / SMB).** For a finite-valued stationary ergodic process with entropy rate $H$,
$$-\tfrac1n\log p(X_0,\dots,X_{n-1})\to H\ \text{ with probability 1}\tag{15.94}$$
*Proof:* Define the $k$th-order Markov approximation for $n\ge k$:
$$p^k(X_0^{n-1})=p(X_0^{k-1})\prod_{i=k}^{n-1}p(X_i|X_{i-k}^{i-1})\tag{15.95}$$
By Lemma 15.7.3, $\limsup\frac1n\log\frac{p^k(X_0^{n-1})}{p(X_0^{n-1})}\le0$ (15.96). With Lemma 15.7.1 this becomes
$$\limsup\tfrac1n\log\tfrac1{p(X_0^{n-1})}\le\lim\tfrac1n\log\tfrac1{p^k(X_0^{n-1})}=H^k\tag{15.97}$$
Likewise $\limsup\frac1n\log\frac{p(X_0^{n-1})}{p(X_0^{n-1}|X_{-\infty}^{-1})}\le0$ (15.98) gives
$$\liminf\tfrac1n\log\tfrac1{p(X_0^{n-1})}\ge\lim\tfrac1n\log\tfrac1{p(X_0^{n-1}|X_{-\infty}^{-1})}=H^\infty\tag{15.99}$$
Together: $H^\infty\le\liminf-\frac1n\log p(X_0^{n-1})\le\limsup-\frac1n\log p(X_0^{n-1})\le H^k$ for all $k$ (15.100). By Lemma 15.7.2, $H^k\to H^\infty=H$, so the limit is $H$ (15.101) (p. 476).

**Lemma 15.7.1 (Markov approximations).** For stationary ergodic $\{X_n\}$: $-\frac1n\log p^k(X_0^{n-1})\to H^k$ w.p. 1 (15.102) and $-\frac1n\log p(X_0^{n-1}|X_{-\infty}^{-1})\to H^\infty$ w.p. 1 (15.103).
*Proof:* Functions of ergodic processes are ergodic, so $p(X_n|X_{n-k}^{n-1})$ and $\log p(X_n|X_{n-1},X_{n-2},\dots)$ are ergodic. Then $-\frac1n\log p^k(X_0^{n-1})=-\frac1n\log p(X_0^{k-1})-\frac1n\sum_{i=k}^{n-1}\log p(X_i|X_{i-k}^{i-1})\to0+H^k$ (15.104–15.105) by the ergodic theorem. Similarly the second sum, over $\log p(X_i|X_{i-k}^{i-1},X_{-1},X_{-2},\dots)$, tends to $H^\infty$ (15.106–15.107) (p. 477).

**Lemma 15.7.2 (no gap).** $H^k\searrow H^\infty$ and $H=H^\infty$.
*Proof:* $H^k\searrow H$ is known, so it remains to show $H^k\searrow H^\infty$. Lévy's martingale convergence theorem gives $p(x_0|X_{-k}^{-1})\to p(x_0|X_{-\infty}^{-1})$ w.p. 1 for every $x_0\in\mathcal X$ (15.108). Since $\mathcal X$ is finite and $p\log p$ is bounded and continuous on $[0,1]$, bounded convergence lets us interchange limit and expectation:
$$\lim H^k=\lim E\Big\{-\sum_{x_0}p(x_0|X_{-k}^{-1})\log p(x_0|X_{-k}^{-1})\Big\}=E\Big\{-\sum_{x_0}p(x_0|X_{-\infty}^{-1})\log p(x_0|X_{-\infty}^{-1})\Big\}=H^\infty\tag{15.109–15.111}$$
(p. 477).

**Lemma 15.7.3 (sandwich).** $\limsup\frac1n\log\frac{p^k(X_0^{n-1})}{p(X_0^{n-1})}\le0$ (15.112) and $\limsup\frac1n\log\frac{p(X_0^{n-1})}{p(X_0^{n-1}|X_{-\infty}^{-1})}\le0$ (15.113).
*Proof:* Let $A$ be the support of $p(X_0^{n-1})$. Then $E\frac{p^k(X_0^{n-1})}{p(X_0^{n-1})}=\sum_{x\in A}p^k(x_0^{n-1})=p^k(A)\le1$ (15.114–15.117). Let $B(X_{-\infty}^{-1})$ be the support of $p(\cdot|X_{-\infty}^{-1})$. Conditioning on the past,
$$E\frac{p(X_0^{n-1})}{p(X_0^{n-1}|X_{-\infty}^{-1})}=E\Big[\sum_{x^n\in B}p(x^n)\Big]\le1\tag{15.118–15.121}$$
Markov gives $\Pr\{p^k/p\ge t_n\}\le1/t_n$ (15.122), i.e. $\Pr\{\frac1n\log\frac{p^k}p\ge\frac1n\log t_n\}\le1/t_n$ (15.123). With $t_n=n^2$ and $\sum1/n^2<\infty$, Borel–Cantelli says the event (15.124) occurs only finitely often a.s., so (15.125) follows. The same argument applied to (15.121) gives (15.126) (pp. 478–479).

*Intuition note:* For almost every sequence, a true probability is eventually not exponentially smaller than the probability given by the $k$th-order Markov model or by the infinite-past conditional model (Lemma 15.7.3). So a rival Markov model bounds $-\frac1n\log p$ from above, and the infinite-past model bounds it from below. Both bounds meet at $H$.

### Chapter summary, problems, notes (pp. 479–481)
The summary restates (15.127–15.139): doubling rate, log-optimality conditions, $E\,S_n/S_n^*\le1$, AEP growth rate, asymptotic optimality, $\Delta W\le D(f\|g)$, $\Delta W\le I(X;Y)$, chain rule, $W^*_\infty$, competitive optimality, AEP for $H(\mathcal X)$ (pp. 479–480). The summary states "Growth rate (AEP)" with $W^*(\mathcal X)$ (p. 479).
*Historical notes (p. 481):* the text recommends Sharpe's book as an introduction to the mean–variance approach; says log-optimal portfolios were introduced by Kelly and Latané and generalized by Breiman; points to Samuelson for a criticism of log-optimal investment and to Cover [66] for an adaptive portfolio counterpart to universal data compression; credits the proof of competitive optimality to Bell and Cover, the stock-market AEP and asymptotic optimality to Algoet and Cover, and the ergodic AEP in full generality to Barron and Orey; the sandwich proof is based on Algoet and Cover.

## Toy example (ours, not from the text)
Market: two assets, cash $X_1=1$ always. The "stock" $X_2=3$ with probability ½ ("A") and $X_2=0$ with probability ½ ("B"). Let $\beta=b_2$ be the fraction in the stock. Wealth relative: $1+2\beta$ (A), $1-\beta$ (B). So
$$W(\beta)=\tfrac12\log_2(1+2\beta)+\tfrac12\log_2(1-\beta).$$
- Set the derivative to 0: $\frac{1}{1+2\beta}-\frac{1}{2(1-\beta)}=0\Rightarrow2(1-\beta)=1+2\beta\Rightarrow\beta^*=\tfrac14$. (Here $\tfrac12\cdot\frac{2}{1+2\beta}=\frac1{1+2\beta}$ and $\tfrac12\cdot\frac1{1-\beta}$.)
- Check (15.11): at $\beta=\tfrac14$, $\mathbf b^{*t}\mathbf X=1.5$ (A) or $0.75$ (B). $E(X_1/S^*)=\tfrac12\cdot\frac1{1.5}+\tfrac12\cdot\frac1{0.75}=0.3333+0.6667=1$ ✓. $E(X_2/S^*)=\tfrac12\cdot\frac3{1.5}+\tfrac12\cdot0=1$ ✓. Both stocks are held, so both equal 1.
- $W^*=\tfrac12\log_21.5+\tfrac12\log_20.75=\tfrac12(0.58496)+\tfrac12(-0.41504)=0.08496$ bits/day. So $S_n^*\approx2^{0.085n}$.
- Theorem 15.2.2 check: all-stock gives $E(S/S^*)=\tfrac12\cdot\frac3{1.5}+0=1\le1$ ✓.
- Mean vs log: all-stock has $E S=1.5$ per day, but $S_n=0$ unless A occurs every day, which has probability $2^{-n}$. Its doubling rate is $-\infty$.
- Side information (Thm 15.4.2): if $Y$ reveals the outcome, bet all on the stock after A (wealth 3) and all cash after B (wealth 1). $W=\tfrac12\log_23=0.7925$, so $\Delta W=0.7925-0.0850=0.7075\le I(X;Y)=H(X)=1$ bit ✓.

## Concepts
- [[doubling-rate]] (new; Kelly criterion / doubling rate) — $W(\mathbf b,F)=E\log\mathbf b^t\mathbf X$, the almost-sure exponential growth rate of reinvested wealth (p. 461)
- [[log-optimal-portfolio]] (new) — the portfolio $\mathbf b^*$ maximizing $W$, characterized by Kuhn–Tucker conditions (p. 461, 463)
- [[kuhn-tucker-log-optimality]] (new) — $E(X_i/\mathbf b^{*t}\mathbf X)=1$ if $b_i^*>0$, $\le1$ if $b_i^*=0$; necessary and sufficient (p. 463)
- [[mean-variance-theory]] (new) — Sharpe–Markowitz: maximize mean for a given variance; efficient frontier (p. 460)
- [[causal-portfolio-strategy]] (new) — $\mathbf b_i$ depends only on past market values (p. 465)
- [[competitive-optimality]] (new) — one-period result $\Pr(VS\ge U^*S^*)\le\frac12$ with fair randomization (p. 472)
- [[ergodic-process]] (new) — stationary process where every invariant set has probability 0 or 1; the LLN holds (p. 474)
- [[typical-set-aep]] — here the Shannon–McMillan–Breiman theorem: $-\frac1n\log p(X_0^{n-1})\to H$ a.s. for stationary ergodic finite-valued sources (p. 475)
- [[entropy-rate]] — $H=\lim H^k$, also $\lim\frac1nH(X_1,\dots,X_n)$ (p. 475)
- [[chain-rule]] — $W^*(\mathbf X_1,\dots,\mathbf X_n)=\sum W^*(\mathbf X_i|\text{past})$ (p. 469)
- [[relative-entropy-kl-divergence]] — upper bound on doubling-rate loss from wrong beliefs (p. 467)
- [[mutual-information]] — upper bound on doubling-rate gain from side information (p. 468)

## Canonical instances
- [[horse-race-as-stock-market]] — $b_i^*=p_i$, $W^*=\log m-H(X)$ for uniform fair odds (p. 473)
- [[two-stock-counterexample]] — market (15.71) shows the log-optimal investor can lose most of the time by a small amount (p. 472)
- [[cash-vs-hot-stock]] — Problem 1 market $(1,a)$ / $(1,1/a)$ (p. 480)

## Bridges (candidates)
- [structural-analogy] $W^*$ chain rule and "conditioning increases $W$" ↔ information theory: chain rule for $H$ and "conditioning reduces $H$" — formally parallel, with $W$ called the dual of $H$ (p. 470).
- [structural-analogy] Doubling-rate loss $\le D(f\|g)$ ↔ cross-entropy/KL in model fitting: Thm 15.4.1 bounds the growth-rate cost of acting on model $g$ by a KL divergence (p. 467).
- [structural-analogy] Competitive optimality of $\mathbf b^*$ ↔ competitive optimality of Shannon codes (Chapter 5): the source calls the two results similar (p. 471); here the proof uses $E[S/S^*]\le1$ plus Markov.
- [structural-analogy] Cesàro-mean proof of $W^*_\infty$ ↔ entropy rate of stationary processes: parallel limit structure, since the chain rule for $W$ is formally that of $H$ (p. 470).
- [metaphor] Log-optimal investing ↔ rational inattention / bet-hedging: unequal gains compounded multiplicatively favour geometric over arithmetic average.

## Questions this raises
- The text covers only a market where $\mathbf X$ is observed in full; what changes with transaction costs or limited rebalancing?
- Is the $\frac12$ in Theorem 15.6.1 attainable, and what happens when the rival may also use randomization differently from $(U^*,V)$?
- Can the bound $\Delta W\le I(X;Y)$ be tight for stocks as it is for horse races with uniform odds? When does it fail?
- Why must the SMB proof go through $H^\infty$ and not directly through $p(X_i|X_0^{i-1})$, which is not ergodic?

## Exercises worth doing
- Ex. 1 (p. 480) — compute the log-optimal portfolio, $W^*$ and the behaviour of $S_n$ for every $\mathbf b$ in a cash-versus-hot-stock market — difficulty: easy
- Ex. 2 (p. 481) — find the doubling rate with side information $Y$ and verify $\Delta W\le I(X;Y)$ — difficulty: medium
- Ex. 3 (p. 481) — conditions under which $\mathbf b^*=(0,1)$ when $X_1=2$ with probability 1, and why $W^*\ge1$ — difficulty: medium

## Reading notes
- The PDF is the 1991 first edition (running head of the chapter's first page, p. 459: "Copyright 1991 John Wiley & Sons, Inc.", Print ISBN 0-471-06259-6), not the 2006 second edition. Chapter content and numbering may differ from the 2nd ed.
- Page offset: printed = pdf − 22.
- The text layer is garbled in many equations. I checked them against the page images.
- Theorem 15.5.3 and the chapter summary print $W^*$ (not $W^*_\infty$) as the limit.
- Proof of Theorem 15.7.1: (15.101) prints $p(X_0^n)$ where the theorem statement uses $p(X_0^{n-1})$; this looks like a notational slip.
- The chapter-summary heading on p. 479 is an OCR glitch ("SUMMARY OF C-R 16") in the text layer; the image reads "Summary of Chapter 15".
- Proofs of Theorem 15.5.3 and the details of Lévy/Birkhoff are omitted or cited by the author.
