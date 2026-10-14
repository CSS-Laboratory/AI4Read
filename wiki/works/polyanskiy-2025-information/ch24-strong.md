---
id: polyanskiy-2025-information/ch24-strong
work: polyanskiy-2025-information
unit: "Chapter 22 (listed as ch24 in the unit metadata) — Strong converse. Channel dispersion. Error exponents. Finite blocklength."
pages: 422-441
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
# Strong converse, channel dispersion, error exponents, finite blocklength

## L0 — One line
Besides capacity $C$, the best achievable $\log M^*(n,\epsilon)$ obeys the strong converse $nC+o(n)$ (finite alphabets), a refined expansion $nC-\sqrt{nV}\,Q^{-1}(\epsilon)+O(\log n)$ for several channels and $\epsilon<\tfrac12$, and can be bounded sharply at finite $n$; hypothesis testing drives the strong converse and the converse bounds.

## L1 — The gist (≤ 120 words)
Capacity says reliable communication is possible below $C$. This chapter asks what happens above $C$, how fast errors vanish, and what $\log M^*(n,\epsilon)$ is at finite $n$. Answers: the error probability tends to 1 above capacity (strong converse for finite alphabets, proved by testing $P_{XY}$ against $P_XQ_Y$). Error exponents are known only partly, and the low-rate exponent is a famous open problem. For several channels the channel dispersion $V$ gives $\log M^*\approx nC-\sqrt{nV}Q^{-1}(\epsilon)$ (for $\epsilon<\tfrac12$; $V$ = variance of the information density). In the BEC and BSC examples this normal approximation is very accurate. It is used to compare real codes by "normalized rate".

**Prerequisites:** capacity and information density; Neyman–Pearson $\beta_\alpha$ and Stein's lemma; Chebyshev and CLT/Berry–Esseen; Gallager's random-coding bound; $Q$-function.

## L2 — Key ideas
- Strong converse: for finite input or output alphabets, $\log M^*(n,\epsilon)=nC+o(n)$ for every $0<\epsilon<1$, so above capacity the error tends to 1 (p. 422–423).
- Proof method: a code gives a test between the true channel and a useless channel $Q_Y^{\otimes n}$. This yields $\beta_{1-\epsilon}\le 1/M$, and the choice of $Q_Y$ removes the unknown code (p. 424–426).
- Finiteness matters: one constructed stationary memoryless channel with countably infinite inputs and capacity $C$ has $C_\epsilon\ge 2C$ for $\epsilon>e^{-1/2}$ (p. 427–428).
- Meta-converse: any auxiliary channel $Q_{Y|X}$ lifts a converse for $Q$ to the true channel via $\beta$. The minimax version equals the LP-relaxation bound (p. 428–430).
- Error exponents (DMC): random coding and sphere-packing match for $R_{cr}<R<C$, and $E(R)$ is known for $R>C$. For low rates it is unknown (p. 431–433).
- Dispersion: $\log M^*(n,\epsilon)=nC-\sqrt{nV}Q^{-1}(\epsilon)+O(\log n)$ with $V=\mathrm{Var}[i(X^*;Y^*)|X^*]$, for fixed $0<\epsilon<\tfrac12$ and for DMC, cost-constrained DMC, AWGN and parallel AWGN (p. 435).
- Normal approximation matches rigorous bounds closely in the BEC and BSC examples (BEC: 213–217 vs 215.5 bits) (p. 439). Normalized rate compares codes of different lengths (p. 439–440).

## L3 — Walkthrough

### Introduction (p. 422)
Notation: $M^*(n,\epsilon)=\max\{M:\exists(n,M,\epsilon)\text{-code}\}$, and $\epsilon^*(n,M)$ is its inverse. Shannon's results say $\lim_{\epsilon\to0}\liminf_n \frac1n\log M^*=C$. Equivalently $\limsup_n\epsilon^*(n,e^{nR})$ is $0$ for $R<C$ and $>0$ for $R>C$. The chapter refines this: strong converse (">0" becomes 1), error exponents, dispersion, and finite-blocklength computable bounds.

### 22.1 Strong converse (p. 422–427)
**Theorem 22.1.** For a stationary memoryless channel with $|\mathcal A|<\infty$ or $|\mathcal B|<\infty$, $C_\epsilon=C$ for $0<\epsilon<1$. Equivalently $\log M^*(n,\epsilon)=nC+o(n)$ (p. 422). Earlier: $C\le C_\epsilon\le \frac{C}{1-\epsilon}$ (Thm 19.7); now equality holds (p. 423). Hence
$$\epsilon^*(n,e^{nR})\to\begin{cases}0&R<C\\1&R>C\end{cases}\tag{22.1}$$
Arimoto's result gives the exponential speed of convergence to 1 (p. 423).

*Waterfall plots.* Engineers fix a code and vary SNR (or $\delta$). Below a critical SNR the error is near 1, above it near 0, unless an error floor appears. This is a single code, whereas (22.1) concerns the best code for each $(n,R)$ (p. 423).

*Proof.* Take an $(n,M,\epsilon)$ code, $W\sim\mathrm{Unif}[M]$, $W\to X^n\to Y^n\to\hat W$, joint law $\mathbb P$. Replace the channel by the useless one $Q_{Y^n|X^n}=(Q_Y)^{\otimes n}$, giving $\mathbb Q$ (p. 423).
1. Under $\mathbb Q$, $X^n\perp Y^n$, so $\mathbb Q[\hat W=W]=1/M$. Under $\mathbb P$, $\mathbb P[\hat W=W]\ge1-\epsilon$. The indicator $1\{\hat W=W\}$ is a test, and Neyman–Pearson optimality gives
$$\beta_{1-\epsilon}(P_{W,X^n,Y^n,\hat W},Q_{W,X^n,Y^n,\hat W})\le\tfrac1M\tag{22.2}$$
2. The likelihood ratio is
$$\frac{P_{WX^nY^n\hat W}}{Q_{WX^nY^n\hat W}}=\frac{P_WP_{X^n|W}P_{Y^n|X^n}P_{\hat W|Y^n}}{P_WP_{X^n|W}(Q_Y)^{\otimes n}P_{\hat W|Y^n}}=\frac{P_{X^nY^n}}{P_{X^n}(Q_Y)^{\otimes n}},$$
so
$$\beta_{1-\epsilon}(P_{X^nY^n},P_{X^n}(Q_Y)^{\otimes n})\le\tfrac1M\tag{22.3}$$
The unknown $P_{X^n}$ is handled by a judicious $Q_Y$ (p. 424).

*Special case BSC$_\delta$.* Take $Q_Y=\mathrm{Ber}(1/2)$, the capacity-achieving output distribution (unique by Cor. 5.5). The log-likelihood ratio is $\log\frac{P_{Z^n}(y^n-x^n)}{2^{-n}}$, so $P_{X^n}$ drops out (p. 424–425):
$$\beta_\alpha(P_{X^nY^n},P_{X^n}(Q_Y)^{\otimes n})=\beta_\alpha(\mathrm{Ber}(\delta)^{\otimes n},\mathrm{Ber}(\tfrac12)^{\otimes n})=\exp\{-nD(\mathrm{Ber}(\delta)\|\mathrm{Ber}(\tfrac12))+o(n)\}\tag{22.4}$$
by Stein's lemma (Thm 14.14). With (22.3): $\log M\le nD(\mathrm{Ber}(\delta)\|\mathrm{Ber}(\frac12))+o(n)=nC+o(n)$ (p. 425).

*General channel.* Let $P_Y^*$ be the unique capacity-achieving output distribution. For every $x\in\mathcal A$,
$$D(P_{Y|X=x}\|P_Y^*)\le C.\tag{22.5}$$
- **Case 1, $|\mathcal B|<\infty$.** Take $Q_Y=P_Y^*$, assuming $\min_yP^*_Y(y)>0$ without loss of generality. By (19.31) the conditional variance of $\log\frac{P_{Y|X}}{Q_Y}$ given $X=x_0$ is at most some $K<\infty$. With $S_n=\sum_{i=1}^n\log\frac{P_{Y|X}(Y_i|X_i)}{P_Y^*(Y_i)}$ (a scalar):
$$\mathbb E[S_n|X^n]\le nC,\quad \mathrm{Var}[S_n|X^n]\le Kn\tag{22.6}$$
and by Chebyshev, conditional on $X^n$,
$$\mathbb P[S_n>nC+\lambda\sqrt{Kn}]\le\mathbb P[S_n>\mathbb E[S_n|X^n]+\lambda\sqrt{Kn}]\le\tfrac1{\lambda^2}\tag{22.7}$$
- **Case 2, $|\mathcal A|<\infty$.** The encoder can be deterministic without loss of generality. A codeword's composition (type) is its empirical distribution $\hat P_c(x)=\frac1n\sum_j1\{c_j=x\}$. By counting, there is an $(n,M',\epsilon)$ subcode with all codewords of one composition $P_0$ and $M'>\frac{M}{(n+1)^{|\mathcal A|-1}}$. Then $\log M=\log M'+O(\log n)$ (p. 426). Set $Q_Y=P_{Y|X}\circ P_0$ and assume $P_0(x)>0$ for all $x$. Since $I(X;Y)\le\log|\mathcal A|<\infty$, $P_{Y|X=x}\ll Q_Y$, and $i(x;y)=\log\frac{dP_{Y|X=x}}{dQ_Y}(y)$. By (19.28), $\mathrm{Var}[i(X;Y)|X]\le\mathrm{Var}[i(X;Y)]\le K$. The text states $\mathbb E[i(X;Y)|X]=D(P_{Y|X}\|Q_Y|P_0)=I(X;Y)\le C$ for $X\sim P_0$. With $S_n=\sum_ii(X_i;Y_i)$, (22.6) and (22.7) follow again.

*Finish.* The lower bound on $\beta$ (14.9) gives, for any $\gamma$,
$$\gamma\,\beta_{1-\epsilon}(P_{X^nY^n},P_{X^n}(Q_Y)^{\otimes n})\ge1-\epsilon-\mathbb P[S_n>\log\gamma].$$
Choose $\log\gamma=nC+\lambda\sqrt{Kn}$ with $\lambda^2=\frac{2}{1-\epsilon}$. By (22.7) the right side is at least $\frac{1-\epsilon}{2}$. Hence $\log\beta_{1-\epsilon}\ge-nC+O(\sqrt n)$. With (22.3): $\log M\le nC+O(\sqrt n)$ (p. 426).

*Lessons.* The method is the weak-converse method, but the hypothesis-testing problem is analysed explicitly instead of using data processing. A bound on the variance of the information density matters. The AWGN channel is excluded by the theorem's assumptions, yet its strong converse holds (Ex. IV.33). The method is also called "sphere-packing" (Ex. IV.32) (p. 426–427).

> **Intuition note.** A code's success looks like a test that says "yes" with probability at least $1-\epsilon$ for the real channel, but succeeds with chance only $1/M$ for a channel that ignores inputs. Tests cannot separate such distributions unless $M\lesssim e^{nC}$. Concentration of $S_n$ makes this hold for every $\epsilon<1$.

### 22.2 A channel without strong converse (p. 427–428)
The proof above used only that a sum of independent variables concentrates around its mean, so one may ask whether the strong converse holds for all stationary memoryless channels (Thm 22.1 covers only finite input or output alphabets). The section gives a counterexample, so it need not hold in general (p. 427). Counterexample (p. 427):
- $\mathcal B=[0,1]$, $\mathcal A=\{(j,m):j,m\in\mathbb Z_+,0\le j\le m\}$.
- Density $p_{Y|X}(y|(j,m))=a_m$ if $\frac jm\le y\le\frac{j+1}m$, and $b_m$ otherwise, with
$$\tfrac1ma_m+(1-\tfrac1m)b_m=1\tag{22.8}$$
$$\tfrac1ma_m\log a_m+(1-\tfrac1m)b_m\log b_m=C\tag{22.9}$$
- For large $m$: $a_m=\frac{mC}{\log m}(1+O(\frac1{\log m}))$ (22.10) and $b_m=1-\frac C{\log m}+O(\frac1{\log^2m})$ (22.11).
- $P_Y^*=\mathrm{Unif}(0,1)$ and $\sup_{P_X}I(X;Y)=C$, so by Thm 19.9 the capacity is $C$. But the $\epsilon$-capacity can exceed $C$.

Fix $n$ and let $P_X$ weight equally the atoms $(j,m)$ with $m=\exp\{2nC\}$. The single-letter information density is $\log a_m$ w.p. $\frac{a_m}m$ (value $2nC+O(\log n)$) and $\log b_m$ otherwise (value $O(\frac1n)$) (p. 428). Using $\frac{a_m}{m}=(1+o(1))\frac1{2n}$ and the Poisson limit theorem,
$$\tfrac1n i(X^n;Y^n)\xrightarrow{d}2C\cdot\mathrm{Poisson}(1/2).$$
By Thm 18.5, for $\epsilon>e^{-1/2}$ there are $(n,M,\epsilon)$-codes with $\log M\ge2nC(1+o(1))$. So $C_\epsilon\ge2C$ for all $\epsilon>e^{-1/2}$ (p. 428).

> **Intuition note.** The information density here is not concentrated: it is rarely huge and usually near zero. The mean is still $C$, but a few lucky outcomes carry much more, so a larger error is "paid" for a higher rate.

### 22.3 Meta-converse (p. 428–430)
Fix a kernel $P_{Y|X}$ (often the $n$-letter channel) and an $(M,\epsilon)$ code. Choose an auxiliary channel $Q_{Y|X}$. The map $(X,Y)\mapsto Z=1\{W\ne\hat W\}$ gives $P_{XY}[Z=0]=1-\epsilon$ and $Q_{XY}[Z=0]=1-\epsilon'$ (the error under $Q$). So
$$\beta_{1-\epsilon}(P_{XY},Q_{XY})\le1-\epsilon'.$$
The idea is to choose a convenient $Q$, bound $1-\epsilon'$ (a converse for $Q$), and lift it to $P$ through $\beta$. The choice of $Q$ is "a matter of art" (p. 429).
- Constant composition (Case 2 above) corresponds to $Q_{Y^n|X^n=c}=(P_{Y|X}\circ\hat P_c)^{\otimes n}$. There are at most $(n+1)^{|\mathcal A|-1}$ output distributions, so $1-\epsilon'\le\frac{(n+1)^{|\mathcal A|-1}}{M}$. For $|\mathcal A|=\infty$ this is unavailable, but the meta-converse still applies (p. 429).
- Trivial channel $Q_{Y|X}=Q_Y$: $1-\epsilon'=\frac1M$, so
$$\tfrac1M\ge\beta_{1-\epsilon}(P_{XY},P_XQ_Y)\tag{22.12}$$
After optimization, $\frac1{M^*(\epsilon)}\ge\inf_{P_X}\sup_{Q_Y}\beta_{1-\epsilon}(P_{XY},P_XQ_Y)$: the *minimax meta-converse*. It has a saddle point and is convex–concave [341] (p. 429).

*Link to LP bound.* Think of a bound on $1-\epsilon$ for given $M$. A code gives a test $P_{Z|XY}$ with $P_{XY}[Z=0]\ge1-\epsilon$ and $P_XQ_Y[Z=0]\le\frac1M$ for all $Q_Y$ (p. 429). So $1-\epsilon\le\tilde\alpha(M;P_X)$, the sup over tests of $\sum P_{XY}P_{Z|XY}(0|x,y)$ under that constraint (finite alphabets). The constraint reduces to $\sum_xP_X(x)P_{Z|XY}(0|x,y)\le\frac1M$ for all $y$. Substitute $\pi_x=MP_X(x)\in[0,1]$ and $r_{x,y}=MP_{Z|XY}(0|x,y)P_X(x)$ (p. 430):
$$\tilde\alpha(M;P_X)=\tfrac1M\sup\Big\{\sum_{x,y}P_{Y|X}(y|x)r_{x,y}:0\le r_{x,y}\le\pi_x,\ \sum_xr_{x,y}\le1\Big\}=\tfrac1MS_{LP}(\pi)$$
with $S_{LP}$ from (18.21). Optimizing over $\sum_x\pi_x\le M$: $1-\epsilon\le S^*_{LP}(M)/M$. By (18.23), a greedy code has $1-\epsilon\ge(1-\frac1e)S^*_{LP}(M)/M$. So at fixed $\epsilon$ the minimax meta-converse should be very sharp, provided the best $Q_Y$ is chosen (easy to guess for symmetric channels) (p. 430).

> **Intuition note.** Every converse can be read as "pretend the channel is easier, count the best success there, then convert back with the cost $\beta$ of the change". The trivial channel makes the "easy" success $1/M$.

### 22.4* Error exponents (p. 430–434)
Large deviations (Thm 15.9) in the proof of Thm 19.9 give $\epsilon^*(n,e^{nR})\le e^{-n\tilde E(R)}$ for $R<C$. Asking for the best $\tilde E(R)$ is, in the author's words, "perhaps the most famous open question in all of channel coding" (p. 431).

**Reliability function.** $E(R)=\lim_n-\frac1n\log\epsilon^*(n,e^{nR})$ for $R<C$, and $\lim_n-\frac1n\log(1-\epsilon^*(n,e^{nR}))$ for $R>C$. It is undefined if the limit does not exist. There is no general proof of existence. Existence can be shown only by proving an achievability bound $E_{lower}$ and a converse bound $E_{upper}$ that coincide. Writing $E_{lower}\le E\le E_{upper}$ for a non-matching pair is an abuse of notation, since $E$ is not known to exist unless the bounds match (p. 431).

**DMC.** Gallager's function (the exponent in the Gallager bound (18.15)):
$$E_0(\rho,P_X)=-\log\sum_{y\in\mathcal B}\Big(\sum_{x\in\mathcal A}P_X(x)P_{Y|X}(y|x)^{\frac1{1+\rho}}\Big)^{1+\rho},$$
$E_0(\rho)=\max_{P_X}E_0(\rho,P_X)$ for $\rho\ge0$, and $\min_{P_X}$ for $\rho\le0$. It tensorizes: the $n$-letter version with $P_X^{\otimes n}$ equals $nE_0(\rho,P_X)$, and the optimizers tensorize too (p. 431).

*Lower bound on $E$.* Gallager's random-coding bound (Thm 18.9) with $P_X^{\otimes n}$:
$$\epsilon^*(n,e^{nR})\le\exp\{n(\rho R-E_0(\rho,P_X))\}\quad\forall P_X,\ \rho\in[0,1]\tag{22.13}$$
Optimizing gives $E(R)\ge E_r(R)\triangleq\sup_{\rho\in[0,1]}E_0(\rho)-\rho R$, which is convex, decreasing and strictly positive on $0\le R<C$ (p. 432). The page prints this as "$E(R)\le E_r(R)$" (see Reading notes). The optimal $\rho\to0$ as $R\to C$ and reaches 1 at the critical rate $R_{cr}$. For $R<R_{cr}$, $E_r(R)=E_0(1)-R$ is linear (p. 432).

*Upper bound.* Taking $Q_Y$ iid in (22.12) gives the sphere-packing bound [381]:
$$E(R)\le E_{sp}(R)=\sup_{\rho\ge0}E_0(\rho)-\rho R\tag{22.14}$$
For $R_{cr}<R<C$: $E_{sp}=E=E_r$. For $R<R_{cr}$: $E_{sp}>E_r$ and $E(R)$ is unknown (p. 432).

*Classical improvements.*
- Expurgation gives $E(R)\ge E_{ex}(R)$, with $E_{ex}>E_r$ for $R<R_x\le R_{cr}$ (second critical rate; Ex. IV.31).
- Minimum-distance bounds (via Hellinger distance and (16.3)); the strongest, "MRRW + mindist", uses [299]. The text says this linear-programming bound has had no improvement in 60 years.
- A straight-line bound interpolates between a min-distance bound and $E_{sp}$.
- These tightly bound $E(R)$ at only one extra point, $E(0+)=E_{ex}(0)$. This is unchanged since 1967. As far as the author knows, the common belief is that $E_{ex}$ is the true $E(R)$ for all rates (p. 433).

*BSC (Fig. 22.1, BSC(0.02)).* The figure marks $R_x=0.24$, $R_{crit}=0.46$, $C=0.86$ (p. 434). For both the Shannon ensemble and random linear codes, $E_r$ is the exact exponent of the average error [178]. At low rates the average is dominated by a few bad codes ($R<\frac12R_x$ for Shannon, $R<R_x$ for linear). A typical linear code has exponent exactly $E_{ex}$ [34]. A famous conjecture says the best minimum Hamming distance is given by the Gilbert–Varshamov bound (Thm 27.5). If true, it would imply $E(R)=E_{ex}(R)$ for $R<R_x$ (p. 433).

*Recent progress.* Litsyn's approach (many pairs of codewords at a given distance, then de Caen's inequality) led to the Barg–MacGregor bound, which matches $E_r$ for $R_{cr}-\epsilon<R<R_{cr}$, extending known $E(R)$ for the first time since [381]. This reinforces the belief that typical linear codes have optimal exponent for $0\le R\le C$ (p. 433).

*$R>C$.* Here $E(R)=\sup_{\rho\in(-1,0)}E_0(\rho)-\rho R$. Achievability is due to Dueck, the converse to Arimoto. Arimoto's converse follows from the weak converse by using Rényi divergence of order $\alpha=\frac1{1+\rho}$ instead of KL. This suggests the general conjecture that replacing Shannon measures with Rényi ones upgrades weak converses to strong converses (p. 433–434).

> **Intuition note.** Exponents tell how fast $\epsilon^*$ dies. Above $R_{cr}$ the best random code is provably optimal. At low rates a few bad codewords spoil random coding on average, but typical codes do better, and nobody knows the true answer.

### 22.5 Channel dispersion (p. 434–438)
Historically, codes with rates far below $C$ made $E(R)$ the main question. Near capacity, the question becomes $\log M^*(n,\epsilon)$ at fixed $\epsilon$ and large $n$; its next-order terms were found to be surprisingly sharp [334]. Since smaller $\epsilon$ intuitively should slow convergence to capacity, the author suggests that the $o(n)$ term in the strong converse hides some interesting dependence on $\epsilon$ (p. 435).

**Theorem 22.2.** For (1) DMC, (2) DMC with cost constraint, (3) AWGN, (4) parallel AWGN, let $(X^*,Y^*)$ be the input–output under the capacity-achieving input and $i(x;y)$ the single-letter information density. For fixed $0<\epsilon<\frac12$, as $n\to\infty$,
$$\log M^*(n,\epsilon)=nC-\sqrt{nV}\,Q^{-1}(\epsilon)+O(\log n)\tag{22.15}$$
where $Q^{-1}$ inverts the complementary normal CDF, $C=I(X^*;Y^*)=\mathbb E[i(X^*;Y^*)]$, and $V=\mathrm{Var}[i(X^*;Y^*)|X^*]$ (the dispersion). With several capacity-achieving inputs, $P_{X^*}$ is the one minimizing this variance (p. 435, footnote 3).

*Proof sketch (p. 435–436).*
- Achievability without cost constraints: Thm 19.11 already gives $nC-\sqrt{nV}Q^{-1}(\epsilon)+o(\sqrt n)$ via the CLT. Berry–Esseen improves $o(\sqrt n)$ to $O(\log n)$. With cost constraints (e.g. AWGN) the uniform-on-sphere input is non-product, so the information density is not a sum of iid terms; the $\kappa$-$\beta$ bound [334, Thm 25] is used instead.
- Converse: apply (22.12) with a suitable $Q_Y$, usually the $n$-th power of the capacity-achieving output distribution. For the BSC, (22.4) gives
$$\log M^*(n,\epsilon)\le-\log\beta_\alpha(\mathrm{Ber}(\delta)^{\otimes n},\mathrm{Ber}(\tfrac12)^{\otimes n}).\tag{22.16}$$
By Ex. III.10,
$$-\log\beta_{1-\epsilon}(\cdot)=nd(\delta\|\tfrac12)+\sqrt{nv}\,Q^{-1}(\epsilon)+o(\sqrt n),$$
with $v=\mathrm{Var}_{Z\sim\mathrm{Ber}(\delta)}\big[Z\log\frac{\delta}{1/2}+(1-Z)\log\frac{1-\delta}{1/2}\big]=\mathrm{Var}[Z\log\frac\delta{1-\delta}]=\delta(1-\delta)\log^2\frac\delta{1-\delta}$. This is the BSC dispersion $V$, so $\log M^*\le nC-\sqrt{nV}Q^{-1}(\epsilon)+o(\sqrt n)$. Berry–Esseen again gives $O(\log n)$.

**Remark 22.1 (zero dispersion).** $V=0$ is possible, e.g. additive noise $Y=X+Z$ over an abelian group with $Z$ uniform on a subset (Ex. IV.7). Some "exotic" zero-dispersion channels have, for $\epsilon>\frac12$, $\log M^*=nC+\Theta_\epsilon(n^{1/3})$. This is why the theorem restricts $\epsilon<\frac12$ (p. 436).

**Remark 22.2.** If $\mathrm{Var}[i(X^*;Y^*)]=\infty$ the theorem need not hold; other stable laws may appear. Without cost constraints $\mathrm{Var}[i|X^*]=\mathrm{Var}[i]$, since $\mathbb E[i|X^*=x]=C$ for $P_{X^*}$-a.e. $x$ (Cor. 5.7) (p. 436).

**Dispersion formulas** ($P$ = SNR) (p. 436–437):
- BEC$_\delta$: $V=\delta\bar\delta\log^22$.
- BSC$_\delta$: $V=\delta\bar\delta\log^2\frac{\bar\delta}\delta$.
- AWGN (real): $V=\frac{P(P+2)}{2(P+1)^2}\log^2e$. Complex: $V=\frac{P(P+2)}{(P+1)^2}\log^2e$.
- BI-AWGN: $V=\mathrm{Var}[\log(1+e^{-2P+2\sqrt PZ})]$, $Z\sim\mathcal N(0,1)$, and $C(P)=\log2-\mathbb E[\log(1+e^{-2P+2\sqrt PZ})]$.
- Parallel AWGN: $V=\frac{\log^2e}{2}\sum_{j=1}^L\big|1-(\sigma_j^2/T)^2\big|^+$, where $T$ is the water-filling threshold, $\sum_j|T-\sigma_j^2|^+=P$. It equals $\sum_jV_{AWGN}(P_j/\sigma_j^2)$ with $P_j=|T-\sigma_j^2|^+$. (added step: with $P_j/\sigma_j^2=T/\sigma_j^2-1$, $V_{AWGN}=\frac{\log^2e}2(1-(\sigma_j^2/T)^2)$, consistent.)

**Other channels (p. 437–438).**
- Memory channels: limited success [335]. Compound DMC: remainder $O(n^{1/4})$ [342].
- Coherent fading: dispersion is known only if one also restricts codewords to limited peak values. The Gaussian erasure channel $Y_i=H_i(X_i+Z_i)$, $H_i\sim\mathrm{Ber}(1/2)$, is unknown.
- Quasi-static MIMO channels: zero dispersion, $\log M^*=nC_\epsilon+O(\log n)$ with outage capacity $C_\epsilon$, so $C_\epsilon$ predicts performance well. Caution: with $H$ known at the transmitter, water-filling (Thm 20.14), which maximizes $C_\epsilon$, is rather sub-optimal at finite $n$.

> **Intuition note.** The first correction to $nC$ is a Gaussian fluctuation of the information density over $n$ uses, whose spread is $\sqrt{nV}$. A smaller $\epsilon$ means going further into the tail ($Q^{-1}(\epsilon)$ larger), so you give up more rate.

### 22.6 Finite-blocklength bounds and normal approximation (p. 439)
Exhaustive computation of $M^*(n,\epsilon)$ is doubly exponential, but known bounds often sandwich it. The *normal approximation* drops the unknown term: $\log M^*(n,\epsilon)\approx nC-\sqrt{nV}Q^{-1}(\epsilon)$. For BSC, AWGN and BI-AWGN, $+\frac12\log n$ is added (the $\log n$ term is $O(1)$ for the BEC, $\frac12\log n$ for these others).
- **BEC example.** $C=1-\delta$, $V=\delta(1-\delta)$ (bits, bits²). Ex. IV.4 gives $213\le\log_2M^*(500,10^{-3})\le217$ for BEC$_{1/2}$; the normal approximation gives $n\bar\delta-\sqrt{n\delta\bar\delta}Q^{-1}(10^{-3})\approx215.5$ bits. Tightness holds across a wide range of $n,\epsilon,\delta$.
- **BSC example** ($\delta=0.11$, $\epsilon=10^{-3}$; Figs. 22.2–22.3). The RCU bound is the tightest achievability bound, impressively close to converse (22.16). The normal approximation is very precise, in contrast with the loose error-exponent estimate (the "Gallager" curve).

### 22.7 Normalized rate (p. 439–441)
Two codes ($k_1\to n_1$, $k_2\to n_2$) are hard to compare via waterfall plots, since the code needing smaller SNR may have a much lower rate. For a $k\to n$ code, find the SNR $P$ where it reaches error $\epsilon$:
$$R_{norm}(\epsilon)=\frac{k}{\log_2M^*(n,\epsilon,P)}\approx\frac{k}{nC(P)-\sqrt{nV(P)}\,Q^{-1}(\epsilon)}$$
using the normal approximation since $\log M^*$ cannot be computed exactly (p. 440). Fig. 22.4 (AWGN and BI-AWGN, $P_e=10^{-4}$) is used to see how coding ideas over the decades drove normalized rate upward toward 1. At "data stream" blocklengths ($n\sim10^4$) LDPC and non-binary LDPC codes reach 95% of the limit. At "control plane" blocklengths ($n\lesssim10^3$) polar and LDPC codes perform similarly, at 90% (p. 440).

## Toy example (ours, not from the text)
BEC with $\delta=0.5$, bits. Then $C=1-\delta=0.5$ and $V=\delta(1-\delta)=0.25$. Take $\epsilon\approx0.1587$, so $Q^{-1}(\epsilon)\approx1$.
- $n=100$: $nC=50$, $\sqrt{nV}=\sqrt{25}=5$. $\log_2M^*\approx50-5(1)=45$ bits, rate $0.45$.
- $n=400$: $nC=200$, $\sqrt{nV}=\sqrt{100}=10$. $\log_2M^*\approx190$, rate $0.475$.
- The rate gap to $C$ shrinks like $\sqrt{V}Q^{-1}(\epsilon)/\sqrt n$: $0.05$ to $0.025$.
- A $40\to100$ code reaching $\epsilon\approx0.159$ has $R_{norm}\approx40/45\approx0.889$.

## Concepts
- [[strong-converse]] (new) — above capacity the error probability tends to 1; $C_\epsilon=C$ for $0<\epsilon<1$ under finite $|\mathcal A|$ or $|\mathcal B|$ (p. 422–423)
- [[channel-capacity]] — the supremum of rates with vanishing error; here $C=\max I(X;Y)$ with $P_Y^*$ unique (p. 425)
- [[noisy-channel-coding-theorem]] — below $C$, $\epsilon^*\to0$; the chapter refines it (p. 422)
- [[fanos-inequality]] — gives the weak converse (Thm 17.3); the proof here instead analyzes hypothesis testing explicitly (p. 423, 426)
- [[relative-entropy-kl-divergence]] — $D(\mathrm{Ber}(\delta)\|\mathrm{Ber}(1/2))=C$ for the BSC; Stein's exponent (p. 425)
- [[data-processing-inequality]] — used in the weak converse; contrasted with the hypothesis-testing approach (p. 426)
- [[meta-converse]] (new) — converse for a chosen auxiliary channel, lifted to the true channel by $\beta_{1-\epsilon}$ (p. 428–429)
- [[reliability-function]] (new) — $E(R)=\lim-\frac1n\log\epsilon^*$ (or of $1-\epsilon^*$ for $R>C$), if the limit exists (p. 431)
- [[gallager-e0-function]] (new) — $E_0(\rho,P_X)$, a tensorizing function giving random-coding and sphere-packing exponents (p. 431)
- [[sphere-packing-bound]] (new) — upper bound $E_{sp}(R)=\sup_{\rho\ge0}E_0(\rho)-\rho R$ (p. 432)
- [[channel-dispersion]] (new) — $V=\mathrm{Var}[i(X^*;Y^*)|X^*]$, the second-order coefficient in $\log M^*$ (p. 435)
- [[normal-approximation]] (new) — $\log M^*\approx nC-\sqrt{nV}Q^{-1}(\epsilon)$ (+ $\frac12\log n$ for some channels) (p. 439)
- [[normalized-rate]] (new) — $k/(nC-\sqrt{nV}Q^{-1}(\epsilon))$, comparing codes of different $n$ (p. 440)
- [[mutual-information]] — $I(X;Y)\le C$ bounds the mean of the information density (p. 426)

## Canonical instances
- [[bsc]] — special case of the strong converse; dispersion $\delta\bar\delta\log^2(\bar\delta/\delta)$; Figs. 22.1–22.3 (p. 424–425, 436)
- [[bec]] — $V=\delta\bar\delta\log^22$; $213\le\log_2M^*(500,10^{-3})\le217$ vs 215.5 (p. 436, 439)
- [[awgn-channel]] — strong converse holds (Ex. IV.33); dispersion $\frac{P(P+2)}{2(P+1)^2}\log^2e$ (p. 427, 437)
- [[countable-input-counterexample-channel]] (new) — capacity $C$ but $C_\epsilon\ge2C$ for $\epsilon>e^{-1/2}$ (p. 427–428)
- [[waterfall-plot]] (new) — fixed-code error vs SNR with a threshold (p. 423)

## Bridges (candidates)
- [same-math] Strong converse proof via $\beta_{1-\epsilon}$ ↔ hypothesis testing: Stein's lemma and Neyman–Pearson — the same $\beta$ exponent gives the code-size bound.
- [structural-analogy] Dispersion expansion $nC-\sqrt{nV}Q^{-1}(\epsilon)$ ↔ CLT/Berry–Esseen statistics: second-order terms in sums of iid variables.
- [structural-analogy] Rényi divergence upgrading weak to strong converse ↔ large-deviation/Rényi methods: the exponent for $R>C$ uses order $1/(1+\rho)$.
- [structural-analogy] Normalized rate ↔ efficiency measures in empirical comparisons: scaling performance by a theoretical limit at the same $(n,\epsilon)$.

## Questions this raises
- Is $E_{ex}(R)$ the true reliability function for all $R<R_{cr}$? What would a Gilbert–Varshamov-type proof give?
- Which additional channels (fading, Gaussian erasure, memory) admit dispersion expansions, and how can their converses be proved?
- Can the conjecture "Rényi measures turn weak converses into strong converses" be proved in general?
- Why are exotic zero-dispersion channels different for $\epsilon>\frac12$, with $n^{1/3}$ behaviour?

## Exercises worth doing
The unit prints no exercises; it points to these (statements as described in the text only):
- Ex. IV.32 (p. 425, 427) — alternative sphere-packing proof of the BSC strong converse — difficulty: medium
- Ex. IV.33 (p. 425, 427) — strong converse for AWGN — difficulty: hard
- Ex. IV.31 (p. 432) — expurgated exponent $E_{ex}$ — difficulty: hard
- Ex. III.10 (p. 436) — second-order expansion of $\beta$ used in the BSC dispersion converse — difficulty: medium
- Ex. IV.4 (p. 439) — BEC bounds $213\le\log_2M^*(500,10^{-3})\le217$ — difficulty: medium

## Reading notes
- The unit is metadata-labelled "ch24", but the printed chapter number is 22. Printed page = pdf − 25 (pdf 447 = printed 422).
- Page 432 prints "$E(R)\le E_r(R)\triangleq\sup_{\rho\in[0,1]}E_0(\rho)-\rho R$". Since (22.13) upper-bounds $\epsilon^*$, the direction that follows is $E(R)\ge E_r(R)$, and $E_r$ is the random-coding (achievability) bound, with the page next turning to the "upper bounds". I wrote ≥ in L3.
- Page 431 repeats "unless the two bounds match" in one sentence (printed duplication).
- (22.14) is shown without a stated restriction on rates; I copied it as printed.
- On p. 426 the claim $\mathbb E[i(X;Y)|X]=I(X;Y)$ is given as printed with "$X\sim P_0$"; the details are not expanded in the text.
- The step from the $\mathrm{Poisson}(1/2)$ limit to the threshold $e^{-1/2}$ is not expanded in the text; I left it as stated. Figures 22.1–22.4 were read from the images; only labelled values ($R_x=0.24$, $R_{crit}=0.46$, $C=0.86$) are used.
