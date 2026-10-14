---
id: polyanskiy-2025-information/ch36-strong-p1
work: polyanskiy-2025-information
unit: "Chapter 33 (unit id ch36) — Strong data processing inequality, part 1/2 (§§33.1–33.7, up to the start of the proof of Prop. 33.17)"
pages: 626–647
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Strong data processing inequality (part 1/2)

## L0 — One line
Along a known noisy channel, mutual information and f-divergences can often be shown to shrink by a factor η < 1 that depends only on the channel (one coefficient η_f for each f). This gives impossibility bounds for noisy computation and inference on trees, and the exact rate for communication-limited correlation estimation.

## L1 — The gist (≤ 120 words)
The ordinary data-processing inequality only says information cannot grow along a Markov chain. If the chain passes through a known channel $P_{Y|X}$, one can often say more: information shrinks by a factor η that depends only on the channel. This unit defines these contraction coefficients, computes them for total variation, KL, χ² and the binary symmetric channel (BSC), and links them to percolation on graphs. Applications are noisy Boolean circuits, reconstruction of a root on a tree, and distributed correlation estimation. Input-dependent coefficients behave better under products than input-independent ones. The unit ends by comparing channels with "less noisy" orders.

**Prerequisites:** mutual information and KL divergence; f-divergences, χ², total variation, Hellinger; Markov chains and chain rule; singular values; BSC and erasure channel; Fisher information (for §33.6).

## L2 — Key ideas
- **Contraction coefficient.** $\eta_f(P_{Y|X})$ is the largest ratio $D_f(P_Y\|Q_Y)/D_f(P_X\|Q_X)$ over input pairs. It equals the worst ratio $I_f(U;Y)/I_f(U;X)$ over chains $U\to X\to Y$, so it gives $I_f(U;Y)\le \eta_f I_f(U;X)$ (pp. 629–631).
- **Formulas for η.** $\eta_{TV}$ is the largest TV distance between two rows of the channel. $\eta_{KL}=\eta_{H^2}=\eta_{\chi^2}$, which is the squared maximal correlation. $\eta_{KL}$ is of the same order as the squared-Hellinger diameter of the channel. $\eta_{KL}(\mathrm{BSC}_\delta)=(1-2\delta)^2$ (pp. 630–633).
- **Directed information percolation.** For channels glued on a DAG, $\eta_{KL}$ of the channel from a source vertex to a set $S$ is at most the probability that an open path from the source to $S$ exists, with each vertex open with probability equal to its own $\eta_{KL}$ (p. 635).
- **Noisy circuits.** The percolation theorem gives the Evans–Schulman bound $I(X_i;Y)\le (K(1-2\delta)^2)^{d_i}\log 2$. It implies that reliable computation with $K$-input $\delta$-noisy gates needs $\delta<\tfrac12-\tfrac1{2\sqrt K}$ (pp. 627–628, 636).
- **Input-dependent coefficients.** With the input law fixed, $\eta_{KL}$ and $\eta_{\chi^2}$ tensorize. The input-independent $\eta_{KL}$ of an $n$-fold product generally tends to 1 (p. 638). $\eta_{\chi^2}$ is symmetric and equals the second singular value squared of a matrix (pp. 636–640).
- **Trees.** If $\pi$ is reversible for $P_{X'|X}$ and $b\,\eta_{KL}(\pi,P_{X'|X})<1$, the root of a $b$-ary broadcast tree cannot be reconstructed from deep leaves. This gives BSC and $k$-coloring thresholds (pp. 643–644).
- **Distributed estimation.** As $B\to\infty$, with $B$ bits sent, the optimal squared error for correlation is $\frac{1+o(1)}{2\ln 2}\cdot\frac1B$ (p. 645).
- **Channel orders.** $\eta_{KL}(P_{Y|X})\le 1-\tau$ iff $P_{Y|X}$ is less noisy than the erasure channel $\mathrm{EC}_\tau$ (p. 647).

## L3 — Walkthrough

### Chapter intro (p. 626)
For any Markov chain $U\to X\to Y\to V$ (33.1), the DPI gives $I(U;Y)\le I(U;X)$ and $I(X;V)\le I(Y;V)$ (p. 626). If the chain factors through a known noisy channel $P_{Y|X}$, one can often prove SDPIs $I(U;Y)\le\eta I(U;X)$ and $I(X;V)\le\eta^{(p)}I(Y;V)$. The coefficients are $<1$ and depend only on the channel, not on $P_{U,X}$ or $P_{Y,V}$ (p. 626). The text says η is always, up to a constant factor, the Hellinger-squared diameter of the channel (p. 626). $\eta^{(p)}$ is not developed in this part.

Two aims: general properties of the coefficients, and sharp lower bounds for statistical estimation. The text notes that SDPIs are an active research area (p. 626).

### 33.1 Computing a Boolean function with noisy gates (pp. 626–629)
- A Boolean function is $f:\{0,1\}^n\to\{0,1\}$. It is built from OR, AND and NOT gates (Shannon, 1938). Von Neumann's $\delta$-noisy gate adds independent mod-2 noise $Z\sim\mathrm{Ber}(\delta)$ to the gate output (Fig. 33.1, pp. 626–627).
- A noisy circuit $C$ computes $f$ if, for some $\epsilon_0=\epsilon_0(\delta)$ that does not depend on $f$, $\mathbb P[C(x)\neq f(x)]\le \tfrac12-\epsilon_0$ (33.2) (p. 627). Built the classical way, deep circuits accumulate errors, so $\epsilon_0\to0$ (p. 627).
- **Theorem 33.1 (von Neumann).** There is $\delta^*>0$ such that for all $\delta<\delta^*$, every Boolean $f$ can be computed with $\delta$-noisy 3-majority gates. His estimate $\delta^*\approx0.087$ was later improved by Pippenger. The largest valid $\delta^*$ is still open (p. 627).
- **Theorem 33.2 (Evans–Schulman).** In an $n$-input circuit with gates of at most $K$ inputs and noise of error probability at most $\delta$,
$$I(X_i;Y)\le \big(K(1-2\delta)^2\big)^{d_i}\log 2,$$
where $d_i$ is the minimum number of gates between $X_i$ and $Y$ (pp. 627–628). The proof comes in §33.3.
- **Consequence.** Take $f=\mathrm{XOR}(X_1,\dots,X_n)$. It depends on every input, and a circuit ignoring an input cannot satisfy (33.2). With $K$-input gates, at height $d$ at most $K^d$ inputs are reached, so some $X_i$ has $d_i\ge \log n/\log K$. As $n\to\infty$, $I(X_i;Y)\to0$ unless $\delta\le\delta^*_{ES}=\frac12-\frac1{2\sqrt K}$. This is incompatible with (33.2), so $\delta^*_{ES}$ is the tightest known upper bound on the tolerable noise (p. 628). Illustration (Fig. 33.2, 9 inputs, gates with at most 3 inputs $G_4,G_5,G_6$): $d_3=2$ and $d_5=3$ (p. 628).
- **Formulas** (trees, no undirected loops). For odd $K$, reliable computation is possible if $\delta<\delta_f^*$ and impossible if $\delta>\delta_f^*$, where
$$\delta_f^*=\frac12-\frac{2^{K-1}}{K\binom{K-1}{(K-1)/2}}\qquad[157].$$
Since formulas are circuits, $\delta_f^*<\delta_{ES}^*$. For $K\gg1$, $\delta_f^*\approx\frac12-\frac{\sqrt{\pi/2}}{2\sqrt K}$ while $\delta^*_{ES}\approx\frac12-\frac1{2\sqrt K}$. So Theorem 33.2 has at least the right rate of convergence to $1/2$ (p. 629).

*Intuition note.* Each noisy gate loses information about each input, and a path through $d$ gates loses it $d$ times. The theorem multiplies the per-gate loss factor along every route to the output and sums over routes.

### 33.2 Strong data processing inequality (pp. 629–633)
**Definition 33.3.** For a kernel $P_{Y|X}$,
$$\eta_f(P_{Y|X})=\sup\frac{D_f(P_Y\|Q_Y)}{D_f(P_X\|Q_X)},\tag{33.3}$$
with $P_Y=P_{Y|X}\circ P_X$, $Q_Y=P_{Y|X}\circ Q_X$, over pairs with $0<D_f(P_X\|Q_X)<\infty$. The DPI says $D_f(P_X\|Q_X)\ge D_f(P_Y\|Q_Y)$. The coefficient measures the multiplicative decrease (p. 629).

**Theorem 33.4.** $\eta_{TV}=\sup_{x\ne x'}\mathrm{TV}(P_{Y|X=x},P_{Y|X=x'})$. In general $\eta_f$ is hard to compute, and TV is an exception (p. 630).
- ($\ge$) Take $P_X=\delta_{x_0}$, $Q_X=\delta_{x_0'}$ (p. 630).
- ($\le$) Let $\tilde\eta$ be the right-hand side; discrete alphabets. For every $E\subseteq\mathcal Y$: $P_{Y|X=x_0}(E)-P_{Y|X=x_0'}(E)\le\tilde\eta\,\mathbb 1\{x_0\ne x_0'\}$ (33.4). Take any coupling $\pi$ of $(X_0,X_0')$ with marginals $P_X,Q_X$. Averaging and taking sup over $E$ gives $\sup_E P_Y(E)-Q_Y(E)\le\tilde\eta\,\pi[X_0\ne X_0']$. The left side is $\mathrm{TV}(P_Y,Q_Y)$ (Thm 7.7(a)). The infimum over couplings of the right side is $\tilde\eta\,\mathrm{TV}(P_X,Q_X)$ (Thm 7.7(b)) (p. 630).

**Example 33.1.** $\eta_{TV}(\mathrm{BSC}_\delta)=\mathrm{TV}(\mathrm{Ber}(\delta),\mathrm{Ber}(1-\delta))=\tfrac12(|\delta-(1-\delta)|+|1-\delta-\delta|)=|1-2\delta|$ (p. 630).

**Theorem 33.5.** $\eta_f(P_{Y|X})=\sup_{P_{UX}:\,U\to X\to Y}\frac{I_f(U;Y)}{I_f(U;X)}$. Hence for any chain $U\to X\to Y$,
$$I_f(U;Y)\le\eta_f(P_{Y|X})\,I_f(U;X).\tag{33.5}$$
Proof. (i) For each $u_0$, $D_f(P_{Y|U=u_0}\|P_Y)\le\eta_f D_f(P_{X|U=u_0}\|P_X)$. Average over $P_U$. (ii) Fix $\tilde P_X,\tilde Q_X$ and let $U\sim\mathrm{Ber}(\lambda)$ with $P_{X|U=1}=\tilde P_X$, $P_{X|U=0}=\tilde Q_X$. As $\lambda\to0$, $I_f(U;X)=\lambda D_f(\tilde P_X\|\tilde Q_X)+o(\lambda)$ and $I_f(U;Y)=\lambda D_f(\tilde P_Y\|\tilde Q_Y)+o(\lambda)$. The ratio tends to $D_f(\tilde P_Y\|\tilde Q_Y)/D_f(\tilde P_X\|\tilde Q_X)$, which can be made arbitrarily close to $\eta_f$ (technical subtleties in [345]) (p. 631).

**Theorem 33.6** (for a fixed $P_{Y|X}$; proofs sketched, full ones in [345]) (p. 631):
- (a) For any $f$: $\eta_f\le\eta_{TV}$.
- (b) $\eta_{KL}=\eta_{H^2}=\eta_{\chi^2}$. More generally $\eta_f=\eta_{\chi^2}$ for operator-convex, twice continuously differentiable $f$.
- (c) $\eta_{\chi^2}=\sup_{P_X,f,g}\rho^2(f(X),g(Y))$, the squared maximal correlation, where $\rho(A,B)=\mathrm{Cov}(A,B)/\sqrt{\mathrm{Var}A\,\mathrm{Var}B}$.
- (d) For a binary-input channel with $P_0=P_{Y|X=0}$, $P_1=P_{Y|X=1}$: $\eta_{KL}=\mathrm{LC}_{\max}(P_0,P_1)=\sup_{0<\beta<1}\mathrm{LC}_\beta(P_0\|P_1)$. Here $\mathrm{LC}_\beta(P\|Q)=D_f(P\|Q)$ with $f(x)=\bar\beta\beta\frac{(1-x)^2}{\bar\beta x+\beta}$ is the Le Cam divergence of order $\beta$ (formula as read from the page).
- (e) $\tfrac12H^2(P_0,P_1)\le\eta_{KL}\le H^2(P_0,P_1)-\tfrac{H^4(P_0,P_1)}4$ (33.6).
- (f) If the binary-input channel is also input-symmetric (BMS), then $\eta_{KL}(P_{Y|X})=I_{\chi^2}(X;Y)$ for $X\sim\mathrm{Ber}(1/2)$.
- (g) The supremum in (33.3) can be restricted to pairs with a common binary support, so $\eta_f$ is that of the least contractive binary subchannel. Hence $\tfrac12\mathrm{diam}_{H^2}\le\eta_{KL}=\mathrm{diam}_{LC_{\max}}\le\mathrm{diam}_{H^2}-\tfrac{\mathrm{diam}_{H^2}}{4}$ (as printed; compare (e), where one would expect $\mathrm{diam}_{H^2}^2/4$), and $\eta_{KL}\asymp\mathrm{diam}_{H^2}$ (p. 632). Here $\mathrm{diam}_{H^2}=\sup_{x,x'}H^2(P_{Y|X=x},P_{Y|X=x'})$.

Proof ideas (p. 632):
- (a) Show it for $E_\gamma$ divergences, $f(x)=|x-\gamma|_+-|1-\gamma|_+$, which are piecewise linear. Then approximate any convex $f$ by $\sum_{j\le N}a_j|x-c_j|_++a_0x+c_0$.
- (b) $\eta_{KL}\ge\eta_{\chi^2}$ by local perturbations, since KL behaves locally like χ² (Prop. 2.21). For $\le$, use $D(P\|Q)=\int_0^\infty\chi^2(P\|Q_t)\,dt$ with $Q_t=\frac{tP+Q}{1+t}$. Then $D(P_Y\|Q_Y)=\int_0^\infty\chi^2(P_Y\|Q_{Y,t})dt\le\eta_{\chi^2}\int_0^\infty\chi^2(P_X\|Q_{X,t})dt=\eta_{\chi^2}D(P_X\|Q_X)$.
- (c) Fix $Q_X$. With $g=dP_X/dQ_X$, the map $Tg(y)=dP_Y/dQ_Y=\mathbb E_{Q_{X|Y}}[g(X)|Y=y]$ is linear. $\eta_{\chi^2}$ is the squared top singular value of $T:L_2(Q_X)\to L_2(Q_Y)$ on $\{h:\mathbb E_{Q_X}h=0\}$. The adjoint $T^*h(x)=\mathbb E_{P_{Y|X}}[h(Y)|X=x]$ has the same spectral norm, and that norm is the maximal correlation.
- (d) Follows from the definition of $\eta_{\chi^2}$ and some algebra. (e) Bounds $\mathrm{LC}_{\max}$ by $H^2$ via Cauchy–Schwarz ([345, App. B]).
- (f) Every BMS channel is a mixture of BSCs: $Y=(Y_\Delta,\Delta)$ with $\Delta\in[0,1/2]$ independent of $X$ and $Y_\delta=\mathrm{BSC}_\delta(X)$. Then $I(U;Y)=I(U;Y|\Delta)\le\mathbb E_{\delta\sim P_\Delta}[(1-2\delta)^2I(U;X|\Delta=\delta)]=\mathbb E[(1-2\Delta)^2]\,I(U;X)$, using $I(U;X|\Delta=\delta)=I(U;X)$ and Example 33.2 (pp. 632–633).

**Example 33.2 ($\eta_{KL}(\mathrm{BSC}_\delta)$).** $\mathrm{diam}_{H^2}=2-4\sqrt{\delta(1-\delta)}$, so (33.6) gives $\eta_{KL}\le(1-2\delta)^2$. (Added step: with $a=2\sqrt{\delta(1-\delta)}$, $H^2-H^4/4=2-2a-(1-a)^2=1-a^2=(1-2\delta)^2$.) For the lower bound take $U=\mathrm{Ber}(1/2)$ and $P_{X|U}=\mathrm{Ber}(\alpha)$:
$$\eta_{KL}\ge\frac{I(U;Y)}{I(U;X)}=\frac{\log2-h(\alpha+(1-2\alpha)\delta)}{\log2-h(\alpha)}\to(1-2\delta)^2\quad(\alpha\to\tfrac12).$$
So $\eta_{KL}(\mathrm{BSC}_\delta)=\eta_{H^2}=\eta_{\chi^2}=(1-2\delta)^2$ (p. 633).

**Proposition 33.7.** For $P_\lambda=\lambda P_1+(1-\lambda)P_0$,
$$D(P_\lambda\|P_{1/2})+D(P_{1-\lambda}\|P_{1/2})\le(1-2\lambda)^2\{D(P_0\|P_{1/2})+D(P_1\|P_{1/2})\},$$
and the same holds for χ² and other $D_f$ satisfying Thm 33.6(b). Proof: let $X\sim\mathrm{Ber}(1/2)$, $Y=\mathrm{BSC}_\lambda(X)$, and $U\sim P_0$ if $X=0$, $U\sim P_1$ if $X=1$. Then $I_f(U;Y)$ is the average of $D_f$ terms for $P_\lambda$ and $P_{1-\lambda}$ against $P_{1/2}$, and (added step) $I_f(U;X)=\tfrac12D_f(P_0\|P_{1/2})+\tfrac12D_f(P_1\|P_{1/2})$ (the page prints $P_\lambda$ twice; see Reading notes). Apply SDPI (33.5) (p. 633).

**Remark 33.1.** With $d_{JS}=\sqrt{JS}$ and $d_{LC}=\sqrt{LC}$: $d(P_\lambda,P_{1-\lambda})\le|1-2\lambda|\,d(P_0,P_1)$ for both. A metric induced by a norm on signed measures (such as TV) must have equality. The inequality is natural because $\eta_{KL}(\mathrm{BSC}_\lambda)=(1-2\lambda)^2$ (p. 633).

*Intuition note.* Mixing two inputs through a noisy channel makes them harder to tell apart. Nothing in $\eta$ depends on which two inputs, so one number per channel bounds the loss. For a BSC, the worst-case KL contraction factor is $(1-2\delta)^2$, while the TV factor is only $|1-2\delta|$.

### 33.3 Directed information percolation (pp. 633–637)
Setting: a DAG $G=(V,E)$ with a random variable $X_v$ per vertex, where each $X_v$ is produced from its parents by a channel. Only Shannon mutual information is used, $f=x\log x$ (p. 634).

**Example 33.3.** Graph $X_0\to B$, $X_0\to A$, $B\to A$, $B\to W$, $A\to W$, so $P_{X_0,A,B,W}=P_{X_0}P_{B|X_0}P_{A|B,X_0}P_{W|A,B}$. Let $\eta=\eta_{KL}(P_{W|A,B})$ and prepend $U\sim\mathrm{Bern}(\lambda)$ with $U\to X_0$. The claim is
$$I(U;B,W)\le\bar\eta\,I(U;B)+\eta\,I(U;A,B).\tag{33.7}$$
By the chain rule $I(U;B,W)\ge I(U;B)$. So if $\eta\to0$, then $I(U;B,W)\approx I(U;B)$, and symmetrically $I(U;A,W)\approx I(U;A)$: seeing $W$ adds little (p. 634).
Proof. Conditioned on $B=b$ the chain $U\to X_0\to A\to W$ holds, because given $A,B$, $X_0$ is independent of $W$. SDPI gives $I(U;W|B=b)\le\eta I(U;A|B=b)$. Average over $b$ and add $I(U;B)$: $I(U;W,B)\le\eta I(U;A|B)+I(U;B)=\eta I(U;A,B)+\bar\eta I(U;B)$ (p. 634). By Thm 33.5,
$$\eta_{KL}(P_{W,B|X_0})\le\eta\,\eta_{KL}(P_{A,B|X_0})+(1-\eta)\,\eta_{KL}(P_{B|X_0}).\tag{33.8}$$

**Example 33.4 (percolation).** Same graph, vertices are cities and edges roads. The road into $W$ is open with probability $\eta$. Then
$$\mathbb P[X\to B\text{ or }W]=\eta\,\mathbb P[X\to A\text{ or }B]+\bar\eta\,\mathbb P[X\to B],\tag{33.9}$$
which has the same shape as (33.8) (p. 635).

**Model.** All edges open; vertex $v$ open with probability $p(v)=\eta_{KL}(P_{X_v|X_{\mathrm{Pa}(v)}})$. $\mathrm{perc}[T\to S]=\mathbb P[\exists\text{ open path }T\to S]$. The channels (or at least bounds on their $\eta_{KL}$) are assumed to be given (p. 635).

**Theorem 33.8.** Let $0$ be a source node (in-degree 0) and $S\subset V$ with $0\notin S$. Gluing the channels gives $P_{X_S|X_0}$, and
$$\eta_{KL}(P_{X_S|X_0})\le\mathrm{perc}(0\to S).\tag{33.10}$$
Proof by induction on $|V|$ (clear for $|V|=1$). Let $v$ have out-degree 0. If $v\notin S$, delete it. Otherwise set $S_A=\mathrm{Pa}(v)\setminus S$, $S_B=S\setminus\{v\}$, $A=X_{S_A}$, $B=X_{S_B}$, $W=X_v$ (WLOG $0\notin A$, using a copy $0'$ of the source). With $U\to X_0$ prepended, this is the graph of (33.7). From (33.8):
$$\eta(S)\le\eta_v\,\eta(S_A\cup S_B)+(1-\eta_v)\,\eta(S_B).\tag{33.11}$$
The induction hypothesis bounds the two terms by the percolation probabilities on $G\setminus\{v\}$. By the computation (33.9), the right side is $\mathrm{perc}(0\to S)$ (pp. 635–636).

**Proof of Theorem 33.2.** A noisy circuit is a DAG, and each $\eta_v\le(1-2\delta)^2$, so every vertex is open with probability $(1-2\delta)^2$ (p. 636). SDPI gives $I(X_i;Y)\le\eta_{KL}(P_{Y|X_i})H(X_i)$. By Thm 33.8, $\eta_{KL}(P_{Y|X_i})\le\mathrm{perc}(X_i\to Y)\le\sum_{\pi:X_i\to Y}(1-2\delta)^{2\ell(\pi)}$ (33.12), since a path of length $\ell(\pi)$ is open with probability at most $(1-2\delta)^{2\ell(\pi)}$. Build paths backward from $Y$ as vertices of a $K$-ary tree. The labelled set is prefix-free and all depths are $\ge d_i$. Then $\sum_{u\in V}c^{\mathrm{depth}(u)}\le(Kc)^{d_i}$ provided $Kc\le1$, attained by all vertices at depth $d_i$. So when $K(1-2\delta)^2\le1$, the sum is at most $(K(1-2\delta)^2)^{d_i}$. With $H(X_i)\le\log2$, $I(X_i;Y)\le K^{d_i}(1-2\delta)^{2d_i}\log2$ (p. 636).

**Corollary 33.9.** For the $n$-letter memoryless extension, $\eta_{KL}(P_{Y|X}^{\otimes n})\le1-(1-\eta_{KL}(P_{Y|X}))^n\le n\,\eta_{KL}(P_{Y|X})$. Proof: the graph is $n$ parallel edges, and the percolation probability of reaching some $Y_i$ is $1-(1-\eta)^n$. The first inequality is sharp for binary or $q$-ary erasure channels ([345, Thm 17]) (pp. 636–637).

**Example 33.5.** Gates are 2-input and $\delta$-noisy, with inputs taken from nearest neighbours to the left (a lattice figure); gates may be routers or constants. Theorem 33.2 says computation is impossible in arbitrary topology if $(1-2\delta)^2<\frac12$. Theorem 33.8 improves this to $(1-2\delta)^2<p_c$, the oriented site percolation threshold of the graph. For this graph $p_c\approx0.705$ (Stavskaya automata) (p. 637).

*Intuition note.* The theorem bounds the information from the source to a set of nodes by the probability that some "channel path" survives. Treating each channel as a switch that is open with probability η turns an information question into a connectivity question.

### 33.4 Input-dependent SDPI; mixing of Markov chains (pp. 637–641)
**Definition 33.10.** For a fixed $P_X$:
$$\eta_f(P_X,P_{Y|X})\triangleq\sup_{Q_X}\frac{D_f(Q_Y\|P_Y)}{D_f(Q_X\|P_X)},\quad 0<D_f(Q_X\|P_X)<\infty\ \ (p.\ 637).$$
- Obviously $\eta_f(P_X,P_{Y|X})\le\eta_f(P_{Y|X})$, often strictly (p. 638).
- Unlike the input-independent case, $\eta_f=\eta_{\chi^2}$ fails. Only $\eta_{\chi^2}(P_X,P_{Y|X})\le\eta_f(P_X,P_{Y|X})$ is known, for twice continuously differentiable $f$ with $f''(1)>0$ (33.13) [345, Thm 2].
- Jointly Gaussian pairs have $\eta_{\chi^2}=\eta_{KL}$. In general only $\eta_{\chi^2}<\eta_{KL}$ is known, with a counterexample in [19]. The choice of $f$ therefore matters (p. 638).
- Mutual information form [352]: $\eta_{KL}(P_X,P_{Y|X})=\sup_{P_{U|X}}\frac{I(U;Y)}{I(U;X)}$. It is the slope at 0: $\eta_{KL}(P_X,P_{Y|X})=\frac{d}{dt}F_I(t;P_{X,Y})\big|_{t=0^+}$ (33.14), because $F_I$ is concave (Ex. III.32) so $\sup_t F_I(t)/t=F_I'(0)$ (p. 638).

**Proposition 33.11 (tensorization).** $\eta_{KL}(P_X^{\otimes n},P_{Y|X}^{\otimes n})=\eta_{KL}(P_X,P_{Y|X})$. So for i.i.d. $(X_i,Y_i)\sim P_{X,Y}$ and any $P_{U|X^n}$, $I(U;Y^n)\le\eta_{KL}(P_X,P_{Y|X})I(U;X^n)$ (p. 638). By induction take $n=2$ (Fig. 33.5), $\eta=\eta_{KL}(P_X,P_{Y|X})$:
$$I(U;Y_1,Y_2)=I(U;Y_1)+I(U;Y_2|Y_1)\le\eta[I(U;X_1)+I(U;X_2|Y_1)]\tag{33.15}$$
$$=\eta[I(U;X_1)+I(U;X_2|X_1)+I(U;X_1|Y_1)-I(U;X_1|Y_1,X_2)]\tag{33.16}$$
$$\le\eta[I(U;X_1)+I(U;X_2|Y_1)]\tag{33.17}$$
$$=\eta I(U;X_1,X_2).$$
Reasons given: (33.15) because $U\to X_2\to Y_2$ is still a Markov chain given $Y_1$; (33.16) because $U\to X_1\to Y_1$ is a Markov chain; (33.17) because $X_2\to U\to X_1$ is a Markov chain even given $Y_1$ (p. 639). As printed, (33.17) repeats the bracket of (33.15); see Reading notes. In contrast, $\eta_{TV}(P_X^{\otimes n},P_{Y|X}^{\otimes n})\to1$ exponentially fast (from (7.21)), and by Cor. 33.9 the input-independent $\eta_{KL}$ also tends to 1 for typical channels (pp. 638–639). $\eta_{\chi^2}$ tensorizes (Thm 33.12).

**Example 33.6 (erasure channel).** $\mathrm{EC}_\tau$: $Y=X$ w.p. $1-\tau$, $Y=\,?$ w.p. $\tau$. For $U\to X\to Y$ let $B=\mathbb 1\{Y=?\}$. Then $I(U;Y)=I(U;Y,B)=I(U;B)+I(U;Y|B)=(1-\tau)I(U;X)$, since $B\perp U$ and $I(U;Y|B=1)=0$, $I(U;Y|B=0)=I(U;X)$. Hence $\eta_{KL}(P_X,\mathrm{EC}_\tau)=1-\tau$, and by tensorization the same for $P_X^{\otimes n}$ (p. 639). For a non-product input law $\mu$, studying $\eta_{KL}(\mu,\mathrm{EC}_\tau^{\otimes n})$ is essentially as hard as the mixing of Glauber dynamics for $\mu$ (Ex. VI.26). For uniform input one may have $\eta_{KL}(P_Y,P_{X|Y})>\eta_{KL}(P_X,P_{Y|X})=1-\tau$ (at least for $\tau>0.74$, Example 33.14, not in this part). So $\eta_{KL}$ is not symmetric, unlike $\eta_{\chi^2}$ (p. 639).

**Theorem 33.12 (properties of $\eta_{\chi^2}(P_X,P_{Y|X})$; finite $\mathcal X,\mathcal Y$)** (p. 640):
- (a) Let $M_{x,y}=\frac{P_{X,Y}(x,y)}{\sqrt{P_X(x)P_Y(y)}}$ ($|\mathcal X|\times|\mathcal Y|$), with singular values $1=\sigma_1\ge\sigma_2\ge\dots\ge0$. Then $\eta_{\chi^2}(P_X,P_{Y|X})=\sigma_2^2(M)$.
- (b) Symmetry: $\eta_{\chi^2}(P_X,P_{Y|X})=\eta_{\chi^2}(P_Y,P_{X|Y})$.
- (c) $\eta_{\chi^2}(P_X,P_{Y|X})=\sup_{g_1,g_2}\rho^2(g_1(X),g_2(Y))$.
- (d) $\eta_{\chi^2}(P_X^{\otimes n},P_{Y|X}^{\otimes n})=\eta_{\chi^2}(P_X,P_{Y|X})$.

Proof (p. 640). Spectral part first. Let $\mathbb E_{X|Y}g(y)=\sum_xP_{X|Y}(x|y)g(x)$. For $g=Q_X/P_X$ we have $Q_Y/P_Y=\mathbb E_{X|Y}g$, so $\eta_{\chi^2}=\sup_g\frac{\mathrm{Var}_{P_Y}[\mathbb E_{X|Y}g]}{\mathrm{Var}_{P_X}[g]}$ over $g\ge0$ with $\mathbb E_{P_X}g=1$. This equals $\sup_h\frac{\mathbb E_{P_Y}[\mathbb E_{X|Y}^2h]}{\mathbb E_{P_X}[h^2]}$ over $\mathbb E_{P_X}h=0$ (take $g=1+\epsilon h$ for small $\epsilon$, and $h=g-1$). With $\phi_x=\sqrt{P_X(x)}h(x)$ this is $\sup_{\phi\perp\psi}\frac{\phi^TM^TM\phi}{\phi^T\phi}$, $\psi_x=\sqrt{P_X(x)}$. The top singular vector of $M$ is $\psi$, so the restriction $\phi\perp\psi$ gives $\sigma_2^2$. Symmetry: $M\to M^T$ when swapping $X,Y$. (c): $\sup_{g_2}\frac{\mathbb E[g_1(X)g_2(Y)]}{\sqrt{\mathrm{Var}[g_2(Y)]}}$ is attained at $g_2=\mathbb E_{X|Y}g_1$. (d): singular values of the Kronecker power $M^{\otimes n}$ are products of $n$-tuples of singular values of $M$.

**Example 33.7 (joint Gaussian, correlation $\rho$).** $\eta_{\chi^2}=\eta_{KL}=\rho^2$. The maximal correlation is $|\rho|$ (eigenvalues of the Mehler kernel), so Thm 33.12(c) gives $\eta_{\chi^2}=\rho^2$. By (33.13) it suffices to show $\eta_{KL}\le\rho^2$. WLOG $Y=X+Z$, $X\sim\mathcal N(0,1)$, $Z\sim\mathcal N(0,\sigma^2)$, so $\rho^2=\frac1{1+\sigma^2}$. For $\tilde X$ with finite second moment and differential entropy, $\tilde Y=\tilde X+Z$, Lieb's EPI (3.36) with $U_1=\tilde X$, $U_2=Z/\sigma$, $\cos^2\alpha=\frac1{1+\sigma^2}$ gives
$$h(\tilde Y)\ge\frac1{1+\sigma^2}h(\tilde X)+\frac{\sigma^2}{2(1+\sigma^2)}\log(2\pi e)+\frac12\log(1+\sigma^2),$$
which implies $D(P_{\tilde Y}\|P_Y)\le\frac1{1+\sigma^2}D(P_{\tilde X}\|P_X)$ (p. 641).

**Example 33.8 (mixing of Markov chains).** Let $K=P_{Y|X}$ be a time-homogeneous chain kernel with stationary law $\pi$. For any initial law $q$, SDPI gives $D_f(qP^n\|\pi)\le\eta_f(\pi,K)^nD_f(q\|\pi)$, an exponential decrease if $\eta_f(\pi,K)<1$. For most interesting chains the TV version is useless, while χ² and KL work (spectral gap and modified log-Sobolev methods). For reversible chains, $\chi^2(P_{X_n}\|\pi)\le\gamma_*^{2n}\chi^2(P_{X_0}\|\pi)$ (33.18), where $\gamma_*$ is the absolute spectral gap [124, Prop. 3]. The method for bounding $\eta_{KL}$ called spectral independence is the "most efficient modern" one (Ex. VI.26) (p. 641).

*Intuition note.* Fixing the input law never makes $\eta$ larger (and often makes it smaller), and for KL it stays the same when many independent copies are used. Without fixing it, many copies generally make the worst-case $\eta$ drift toward 1. For χ², the coefficient is a singular value problem.

### 33.5 Application: broadcasting and coloring on trees (pp. 641–644)
**Model.** An infinite $b$-ary tree with $X_\rho\sim\pi$ at the root and each child $X_c$ generated from its parent by the same kernel $P_{X'|X}$. Assume reversibility: $P_{X'|X}(a|b)\pi(b)=P_{X'|X}(b|a)\pi(a)$ (33.19), so $\pi$ is also stationary for the reversed kernel (p. 642). Origins: statistical physics (Ising on Bethe lattices), phylogenetic reconstruction, random constraint satisfaction, sparse-graph coding, and a stochastic block model equivalence (p. 642). Without (33.19) one only needs $\pi$ stationary for $P_{X'|X}$, and (33.21) becomes $\eta_{KL}(\pi,P_{X|X'})\,b<1$. Under (33.19) the law is a Gibbs distribution
$$P_{X_{\mathrm{all}}}=\tfrac1Z\exp\Big(\sum_{(p,c)\in E}f(X_p,X_c)+\sum_{v}g(X_v)\Big),\tag{33.20}$$
with $f$ symmetric. For $\mathcal X=\{0,1\}$ this is the Ising model on a tree. Not every measure of form (33.20) is a broadcasting process (p. 642).

The inference task: reconstruct $X_\rho$ from $X_{L_d}$, the vertices at depth $d$.

**Theorem 33.13.** Let $\pi$ be reversible for $P_{X'|X}$ with
$$\eta_{KL}(\pi,P_{X'|X})\,b<1.\tag{33.21}$$
Then $I(X_\rho;X_{L_d})\to0$ (the page prints "$d\to0$"; the proof gives $d\to\infty$) (p. 643).
Proof. For $v\in L_1$ let $L_{d,v}$ be the depth-$d$ descendants of $v$. Then $I(X_\rho;X_{L_d})\le\sum_{v\in L_1}I(X_\rho;X_{L_{d,v}})$. In the chain $X_{L_{d,v}}\to X_v\to X_\rho$, $P_{X_\rho|X_v}=P_{X'|X}$ and $P_{X_v}=\pi$, so $I(X_{L_{d,v}};X_\rho)\le\eta_{KL}(\pi,P_{X'|X})I(X_{L_{d,v}};X_v)$. Since $P_{X_v}=\pi$ and all edges share the kernel, $I(X_{L_{d,v}};X_v)=I(X_{L_{d-1}};X_\rho)$. So $I(X_\rho;X_{L_d})\le\eta b\,I(X_\rho;X_{L_{d-1}})$ and hence $I(X_\rho;X_{L_d})\le(\eta b)^dH(X_\rho)$, which tends to 0 exponentially if $\eta b<1$ (p. 643). A weaker version (non-reconstruction when $\eta_{KL}(P_{X'|X})b\le1$) follows from percolation. The $k$-coloring example shows the strengthening is essential (p. 643).

**Example 33.9 (BSC tree).** $\mathcal X=\{0,1\}$, $P_{X'|X}=\mathrm{BSC}_\delta$, $\pi=\mathrm{Unif}$ (reversible). If $b(1-2\delta)^2<1$, no algorithm recovers the root as depth $\to\infty$ (originally [63]) (p. 643).

**Example 33.10 ($k$-coloring).** $X_{\mathrm{all}}$ is a uniform valid $k$-coloring of the $b$-ary tree; reconstruct the root colour from the leaves at depth $d$. It is broadcasting with $\pi=\mathrm{Unif}[k]$ and $P_{X'|X}(a|b)=\frac1{k-1}$ if $a\ne b$, 0 if $a=b$ (p. 644).
- By Ex. VI.24, $\eta_{KL}(\mathrm{Unif},P_{X'|X})=\frac1{k\log k(1+o(1))}$ for large $k$. By Thm 33.13, if $b<k\log k(1+o(1))$ reliable reconstruction is impossible ([393], [50]).
- If $b>k\log k(1+o(1))$, with probability close to 1 the children of a node show all colours except the node's own, so the node's colour is the missing one. When $b>(1+\epsilon)k\log k$, seeing a $(1-\epsilon)$-fraction of children suffices. Working bottom-up succeeds with high probability; with positive probability the root posterior is a point mass ("freezing").
- Leaf-majority reconstruction beats chance $1/k$ iff $d>(k-1)^2$ (Kesten–Stigum [244]). The text writes $d$ here, presumably the branching number $b$. This threshold is suboptimal but robust to erasing all but an $\epsilon$-fraction of leaves.
- The χ² version: the transition matrix is symmetric with eigenvalues $\{1,-\frac1{k-1}\}$, so $\eta_{\chi^2}(\mathrm{Unif},P_{X'|X})=\frac1{(k-1)^2}\ll\eta_{KL}$. If Thm 33.13 held with $I_{\chi^2}$, non-reconstruction would follow for $d<(k-1)^2$, contradicting the majority result. The reason it fails is that $I_{\chi^2}$ is not subadditive (7.47), but it is locally subadditive when $I_{\chi^2}(X;A)\ll1$ [202, Lemma 26]. So the argument works when leaves are seen through a very noisy channel, and the robust reconstruction threshold for colouring is exactly $d=(k-1)^2$ (p. 644).

### 33.6 Application: distributed correlation estimation (pp. 644–646)
Alice sees $\{X_i\}\overset{\text{i.i.d.}}\sim B(1/2)$, Bob sees $\{Y_i\}\overset{\text{i.i.d.}}\sim B(1/2)$, pairs $(X_i,Y_i)$ i.i.d. with $\mathbb E[X_iY_i]=\rho\in[-1,1]$. Bob sends $W$ with $H(W)=B$ bits, and Alice outputs $\hat\rho(X^\infty,W)$. The risk is $R^*(B)=\inf_{W,\hat\rho}\sup_\rho\mathbb E[(\rho-\hat\rho)^2]$. The problem is communication-limited, not sample-limited (p. 645). Trivial scheme: send $W=(Y_1,\dots,Y_B)$ and use $\hat\rho=\frac1B\sum_{i\le B}X_iY_i$ (the page writes $\frac1n$), giving $R^*(B)\le\frac1B$ (p. 645).

**Theorem 33.14 ([207]).** As $B\to\infty$, $R^*=\frac{1+o(1)}{2\ln2}\cdot\frac1B$ (p. 645).

*Lower bound.* Fix $P_{W|Y^\infty}$. This defines a family $\{Q_\rho\}$, the law of $(X^\infty,W)$. By the van Trees inequality (Thm 29.2, needs smoothness of $J_F$), $R^*(B)\ge\frac{1+o(1)}{\min_\rho J_F(\rho)}\ge\frac{1+o(1)}{J_F(0)}$. Local approximation: $D(Q_\rho\|Q_0)=\frac{\rho^2\log e}{2}J_F(0)+o(\rho^2)$. Under $\rho=0$, $X^\infty$ and $W$ are independent, so
$$D(Q_\rho\|Q_0)=D(P^\rho_{X^\infty,W}\|P^\rho_{X^\infty}\times P^\rho_W)=I(W;X^\infty)\le\rho^2I(W;Y^\infty)\le\rho^2B\log2.$$
The text does not name the step $\le\rho^2I(W;Y^\infty)$; the section opening points to tensorization. Hence $J_F(0)\le(2\ln2)B+o(1)$ (added step: from $\frac{\rho^2\log e}2J_F(0)\le\rho^2B\log2$), which gives the lower bound (p. 645).

*Upper bound.* Blocks of $m\to\infty$ bits, $\tilde X_i=\frac1{\sqrt m}\sum_{j=(i-1)m}^{im-1}X_j$ (likewise $\tilde Y_i$), give $\rho$-correlated standard Gaussians. Fix a large $N$ and let $W=\arg\max_{1\le j\le N}Y_j$ (motivation: Ex. V.16). Standard concentration gives $\mathbb E[Y_W]=\sqrt{2\ln N}(1+o(1))$ (Lemma 27.10) and $\mathrm{Var}[Y_W]=O(1/\ln N)$. Alice estimates $\hat\rho=X_W/\mathbb E[Y_W]$, which is unbiased with $\mathrm{Var}_\rho[\hat\rho]=\frac{1-\rho^2+o(1)}{2\ln N}$. Setting $N=2^B$ finishes (p. 646).

*Intuition note.* Sending only the index of Bob's largest value uses $B$ bits better than sending $B$ raw bits (error constant $\frac1{2\ln2}$ instead of $1$). In the lower bound, the information between Alice's data and the message $W$ is at most $\rho^2$ times the information $W$ has about Bob's data (an SDPI-type step), and the argmax scheme matches the resulting rate asymptotically.

### 33.7 Channel comparison: degradation, less noisy, more capable (pp. 646–647)
**Definition 33.15.** For channels $P_{Y|X}$, $P_{Z|X}$ (p. 646):
- $P_{Y|X}\le_{\deg}P_{Z|X}$ if $P_{Y|X}=P_{Y|Z}\circ P_{Z|X}$ for some $P_{Y|Z}$.
- $P_{Y|X}\le_{\ln}P_{Z|X}$ ($P_{Z|X}$ is *less noisy*) if $I(U;Y)\le I(U;Z)$ for every $P_{U,X}$ with the chain $U\to X\to(Y,Z)$.
- $P_{Y|X}\le_{mc}P_{Z|X}$ ($P_{Z|X}$ is *more capable*) if $I(X;Y)\le I(X;Z)$ for every $P_X$.

Remarks (proofs in [345]) (p. 647): $\le_{\deg}\Rightarrow\le_{\ln}\Rightarrow\le_{mc}$, with counterexamples for the reverses in [111, Prob. 15.11]. The less-noisy order is equivalent to $D(Q_Y\|P_Y)\le D(Q_Z\|P_Z)$ for all $P_X,Q_X$. Among BMS channels with a given $I_{\chi^2}(X;Y)=\eta$ ($X\sim\mathrm{Ber}(1/2)$), BSC and BEC are the minimal and maximal elements for $\le_{\ln}$ (Ex. VI.21).

**Proposition 33.16.** $\eta_{KL}(P_{Y|X})\le1-\tau$ iff $P_{Y|X}\le_{\ln}\mathrm{EC}_\tau$. Proof: for $\mathrm{EC}_\tau$, $I(U;Z)=(1-\tau)I(U;X)$. By the mutual-information characterization, $I(U;Y)\le(1-\tau)I(U;X)$. Combine (p. 647). So $\eta_{KL}$ is the worst erasure channel that still dominates the channel.

**Proposition 33.17 (tensorization).** If $P_{Y_i|X_i}\le_{\ln}P_{Z_i|X_i}$ for all $i\in[n]$, then $\bigotimes_iP_{Y_i|X_i}\le_{\ln}\bigotimes_iP_{Z_i|X_i}$. The same holds for $\le_{mc}$. The proof is by induction, reducing to $n=2$ with the chain of Fig. at p. 647 ($U\to X_1,X_2$, then $X_i\to Y_i,Z_i$). It continues beyond this part, which stops after setting up this chain (p. 647).

## Toy example (ours)
*Part A — the SDPI with an erasure channel, exact numbers.* Let $U\sim\mathrm{Bern}(1/2)$ and $X=U$, so $I(U;X)=H(U)=1$ bit. Send $X$ through $\mathrm{EC}_{1/4}$ ($\tau=1/4$). With probability $1/4$ we see "?" and know nothing, so $H(U|Y)=1$. With probability $3/4$ we see $X$, so $H(U|Y)=0$. Then $H(U|Y)=\tfrac14\cdot1+\tfrac34\cdot0=0.25$ and $I(U;Y)=1-0.25=0.75=(1-\tau)\,I(U;X)$. This matches Example 33.6: $\eta_{KL}=0.75$, with equality.

*Part B — a tree.* Take a binary tree ($b=2$) with $\mathrm{BSC}_{0.2}$ edges and uniform root. Then $\eta_{KL}=(1-2\cdot0.2)^2=0.36$ and $b\eta=0.72<1$, so Thm 33.13 applies. The bound is $I(X_\rho;X_{L_d})\le0.72^d\cdot H(X_\rho)$ with $H(X_\rho)=1$ bit. For $d=3$: $0.72^2=0.5184$, $0.5184\times0.72=0.373$ bits. For $d=10$: $0.72^4=0.2687$, $0.72^8=0.0722$, $0.72^{10}=0.0722\times0.5184=0.0374$ bits. For $\delta=0.1$, $b\eta=2\times0.64=1.28>1$, and the theorem says nothing.

## Concepts
- [[strong-data-processing-inequality]] (new) — an inequality $I(U;Y)\le\eta I(U;X)$ with $\eta<1$ depending only on the channel (p. 626)
- [[contraction-coefficient]] (new) — $\eta_f(P_{Y|X})$, the sup of $D_f(P_Y\|Q_Y)/D_f(P_X\|Q_X)$ over input pairs (p. 629)
- [[input-dependent-contraction-coefficient]] (new) — same sup with the input law $P_X$ fixed; it tensorizes for KL and χ² (pp. 637–640)
- [[maximal-correlation]] (new) — sup of squared correlation $\rho^2(f(X),g(Y))$; equals $\eta_{\chi^2}$ (p. 631)
- [[directed-information-percolation]] (new) — bounding $\eta_{KL}$ of a DAG by an open-path probability with vertex probability $\eta_v$ (p. 635)
- [[broadcasting-on-trees]] (new) — reconstructing the root of a tree from depth-$d$ values; non-reconstruction if $\pi$ is reversible and $b\,\eta_{KL}<1$ (pp. 641–643)
- [[less-noisy-order]] (new) — $P_{Z|X}$ at least as informative as $P_{Y|X}$ for every $U\to X$ (p. 646)
- [[data-processing-inequality]] — $I(U;Y)\le I(U;X)$ along Markov chains; the SDPI strengthens it (p. 626)
- [[f-divergence]] — the family $D_f$ in which η is defined (p. 629)
- [[relative-entropy-kl-divergence]] — $\eta_{KL}$ is the main coefficient (p. 631)
- [[mutual-information]] — $I(U;Y)$ in all SDPI statements (p. 626)
- [[fisher-information]] — $J_F(0)$ in the correlation lower bound (p. 645)
- [[exponential-family-gibbs-distribution]] — the tree law (33.20) (p. 642)
- [[noisy-channel]] — the known channel $P_{Y|X}$ through which the chain factors (p. 626)

## Canonical instances
- [[noisy-boolean-circuit-von-neumann]] — δ-noisy gates; Evans–Schulman bound and the $\frac12-\frac1{2\sqrt K}$ threshold (pp. 626–628)
- [[bsc-contraction]] — $\eta_{KL}(\mathrm{BSC}_\delta)=(1-2\delta)^2$ and $\eta_{TV}=|1-2\delta|$ (pp. 630, 633)
- [[erasure-channel-sdpi]] — $\eta_{KL}(P_X,\mathrm{EC}_\tau)=1-\tau$, exact (p. 639)
- [[gaussian-sdpi]] — $\eta_{\chi^2}=\eta_{KL}=\rho^2$ for jointly Gaussian pairs (pp. 640–641)
- [[markov-chain-mixing-sdpi]] — $D_f(qP^n\|\pi)\le\eta_f(\pi,K)^nD_f(q\|\pi)$ (p. 641)
- [[bsc-tree-broadcast]] — non-reconstruction when $b(1-2\delta)^2<1$ (p. 643)
- [[k-coloring-tree-reconstruction]] — thresholds $k\log k$ and $(k-1)^2$ (p. 644)
- [[distributed-correlation-estimation]] — minimax error $\frac{1+o(1)}{2\ln2\,B}$ (p. 645)

## Bridges (candidates)
- [same-math] SDPI contraction $\eta_{\chi^2}$ ↔ linear algebra: second singular value squared of $M_{xy}=P_{XY}/\sqrt{P_XP_Y}$ — Thm 33.12(a) states it directly.
- [structural-analogy] Directed information percolation ↔ probability: open-path percolation on a DAG — the recursion (33.8) has the same shape as (33.9).
- [structural-analogy] Mixing bound $D_f(qP^n\|\pi)\le\eta^nD_f(q\|\pi)$ ↔ Markov chain theory: spectral gap contraction of χ² — (33.18) with $\gamma_*^2$.
- [structural-analogy] $\eta_{KL}$ as "worst dominated erasure channel" ↔ channel coding: comparison of channels by erasure channels (Prop. 33.16).
- [metaphor] Tree reconstruction threshold $b\eta=1$ ↔ statistical physics: Ising model on Bethe lattice and its phase transition.

## Questions this raises
- How tight is $\eta_{KL}\asymp\mathrm{diam}_{H^2}$ for channels with large alphabets, and what makes $\eta_{KL}$ hard to compute in general?
- For which $f$ does $\eta_f(P_X,P_{Y|X})$ tensorize, and why does $\eta_{\chi^2}<\eta_{KL}$ occur?
- The Evans–Schulman bound is only matched in rate by the formula threshold: can the circuit threshold be pushed closer to $\delta_f^*$?
- How does the less-noisy order (and its tensorization, Prop. 33.17) yield further comparison results beyond what this part states?

## Reading notes
- **Part boundary.** This part starts at the start of printed Chapter 33 (p. 626) and ends on p. 647, in the middle of the proof of Prop. 33.17, after the set-up chain. The unit id says "ch36", but the printed chapter number is 33. Printed = pdf − 25.
- **No exercises are listed in these pages.** The text only refers to exercises (e.g. III.32, VI.19–VI.26, V.16, VI.20), so there is no "Exercises worth doing" section.
- **Apparent misprints, as the page shows them:**
  - Thm 33.13 reads "as $d\to0$" while the proof gives $d\to\infty$.
  - In the proof of Prop. 33.7, the text writes $P_\lambda$ in both terms of $I_f(U;Y)$. The statement needs $P_{1-\lambda}$ in the second.
  - In (33.17) the bracket repeats (33.15). The final line equals $\eta[I(U;X_1)+I(U;X_2|X_1)]$ rather than the $I(U;X_2|Y_1)$ form.
  - In the proof of Thm 33.8 the induction bound is written $\eta(S_A\cup S_B)\le\mathrm{perc}(0\to S_A)$. It presumably means $S_A\cup S_B$.
  - In Thm 33.6(g) the last term of the upper bound is printed as $\mathrm{diam}_{H^2}/4$ (no square). By (e) one would expect $\mathrm{diam}_{H^2}^2/4$ (added inference).
  - In §33.6 the trivial estimator is written $\frac1n\sum_{i\le B}$, where $\frac1B$ is meant.
  - In Example 33.10, "$d>(k-1)^2$" uses $d$ where the branching number appears intended.
- Text-layer garbling affected Thm 33.2's exponent and some symbols. All equations were checked against the page images. In 33.6(d) the Le Cam $f$ is transcribed as printed; the placement of the bar on β in the denominator is hard to confirm in the image.
- The justification "$\eta_v\le(1-2\delta)^2$ for $\delta$-noisy gates" in the proof of Thm 33.2 is stated without derivation. It matches Example 33.2 for the BSC.
