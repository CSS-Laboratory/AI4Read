---
id: polyanskiy-2025-information/ch14-entropy
work: polyanskiy-2025-information
unit: "Chapter 12 (unit id ch14-entropy): Entropy of ergodic processes"
pages: 230–243
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Entropy of ergodic processes

## L0 — One line
For a stationary ergodic source with memory, the per-symbol log-likelihood converges to the entropy rate, so the iid compression and AEP results carry over, and entropy rates also underlie the Kolmogorov–Sinai entropy, which measures how chaotic a deterministic map is.

## L1 — The gist (≤ 120 words)
The question is whether the iid compression theory (entropy as the compression limit, typical sets) survives for sources with memory. The answer is yes for stationary ergodic processes. The Shannon–McMillan–Breiman theorem says $\frac1n\log\frac{1}{P_{S^n}(S^n)}\to\mathcal H$. This gives the compression limit and the AEP. The proof approximates the process by $m$-th order Markov chains and uses the Birkhoff–Khintchine ergodic theorem (time averages converge to expectations). The chapter ends with Kolmogorov–Sinai entropy. Sinai's generator theorem helps compute it when a generator with finite entropy rate is available. For the doubling map it equals $\log 2$, which shows how deterministic dynamics can look random under finite-precision measurement.

**Prerequisites:** entropy, conditional entropy, KL divergence; entropy rate of stationary processes; σ-algebras and a.s./$L^1$/in-probability convergence; Hilbert-space basics.

## L2 — Key ideas
- A stationary process is a measure-preserving shift $\tau$ applied to a starting variable. Ergodic means every shift-invariant event has probability 0 or 1 (pp. 230, 232).
- Stationary does not imply ergodic: $S_k=S_0$ is stationary but not ergodic unless $S_0$ is constant. Ergodic does not imply stationary: $S_k=k^2$ (p. 232).
- Shannon–McMillan–Breiman: for stationary ergodic discrete $\mathbb S$, $\frac1n\log\frac1{P_{S^n}(S^n)}\to\mathcal H$ in probability, a.s. and in $L^1$ (p. 233).
- Consequences: the optimal compression length per symbol tends to $\mathcal H$, the fixed-length error probability tends to 0 or 1 according to $R\gtrless\mathcal H$, and the AEP holds (pp. 233–234).
- The $L^1$ proof uses Markov approximation. For fixed $m$ it gives $\limsup_n\mathbb E|\cdot|\le 2(\mathcal H_m-\mathcal H)$, and then $m\to\infty$ (pp. 235–236).
- Birkhoff–Khintchine (time average = ensemble average) rests on the maximal ergodic lemma, with Garsia's short proof (pp. 237–239).
- Kolmogorov–Sinai entropy is the supremum of entropy rates over finite measurements. If a generator has finite entropy rate, the two coincide (pp. 239–241).
- The doubling map has $\mathcal H(\tau)=\log 2$ and the irrational rotation has entropy zero. Isomorphic p.p.t.s have equal KS entropy (Kolmogorov's 1958 observation), which lets one show that the Ber(1/2) and Ber(1/3) shifts are not isomorphic (pp. 242–243).

## L3 — Walkthrough

### 12.1 Bits of ergodic theory (pp. 230–233)
**Definitions.** A transformation $\tau:\Omega\to\Omega$ is *measure preserving* (p.p.t.) if $P(E)=P(\tau^{-1}E)$ for all $E\in\mathcal F$. A set is *$\tau$-invariant* if $E=\tau^{-1}E$. The invariant sets form a σ-algebra $\mathcal F_{inv}$ (an exercise) (p. 230). A process is *stationary* if some p.p.t. $\tau$ gives $S_j=S_{j-1}\circ\tau=S_0\circ\tau^j$ (p. 230). It is described by $(\Omega,\mathcal F,P,\tau,S_0)$ (p. 231).

**Remark 12.1** (p. 231).
- Equivalently, the joint law is shift invariant. Take $\Omega=\mathcal S^\infty$ and the left shift $\tau(s_0,s_1,\dots)=(s_1,s_2,\dots)$ (12.1).
- Shift-invariant events: $\{\exists n: x_i=0\ \forall i\ge n\}$ and $\{\limsup x_i<1\}$. Not invariant: $\{x_0=x_1=\dots=0\}$.
- The tail σ-algebra is $\mathcal F_{tail}=\bigcap_{n\ge1}\sigma\{S_n,S_{n+1},\dots\}$. Invariant events lie in it. The inclusion is strict: $\{\exists n: x_i=0\ \forall \text{ odd } i\ge n\}$ is tail but not shift-invariant.

**Proposition 12.3 (Poincaré recurrence).** For measurable $A$ with $P[A]>0$:
$$P\Big[\bigcup_{k\ge1}\tau^{-k}A\,\Big|\,A\Big]=P[\tau^k(\omega)\in A \text{ infinitely often}\mid A]=1.$$
*Proof* (p. 231). Let $B=\bigcup_{k\ge1}\tau^{-k}A$. It suffices to show $P[A\cap B]=P[A]$, i.e. $P[A\cup B]=P[B]$ (12.2). Now $\tau^{-1}A\cup\tau^{-1}B=B$, so $P[\tau^{-1}(A\cup B)]=P[B]$. By measure preservation the left side equals $P[A\cup B]$.

Application (pp. 231–232): for a conservative mechanical system, $\tau$ preserves Lebesgue measure (Liouville). Two mixed gases would then eventually return to the separated state. The author resolves the "paradox": it takes unphysically long.

**Definition 12.4 (ergodicity).** $\tau$ is ergodic if $P[E]\in\{0,1\}$ for all $E\in\mathcal F_{inv}$. A process is ergodic if every shift-invariant event has $P[S_1^\infty\in E]\in\{0,1\}$ (p. 232).

Examples (p. 232):
- $S_k=k^2$: ergodic, not stationary.
- $S_k=S_0$: stationary, not ergodic unless $S_0$ is constant. The event $\{(s,s,\dots)\}$ is invariant with probability $P[S_0=s]\in(0,1)$.
- iid: stationary and ergodic (Kolmogorov 0-1 law).
- If $\{S_i\}$ is ergodic, so is $X_i=f(S_i,S_{i+1},\dots)$. This is a *B-process* if $S_i$ is iid.
- Key example: $S_i\overset{iid}\sim\mathrm{Ber}(1/2)$ and $X_k=\sum_{n\ge0}2^{-n-1}S_{k+n}=2X_{k-1}\bmod 1$. Each $X_k$ is uniform on $[0,1]$. Given $X_0$, the future is deterministic, yet time averages converge to expectations. Full determinism needs infinite-precision knowledge of $X_0$. Any discretization has positive entropy rate (see 12.5).
- *Mixing*: $P[A\cap\tau^{-n}B]\to P[A]P[B]$. *Weakly mixing*: $\sum_{k=1}^n\frac1n|P[A\cap\tau^{-n}B]-P[A]P[B]|\to0$. Strong mixing ⇒ weak mixing ⇒ ergodic (Exercise II.12).
- A finite irreducible Markov chain with recurrent states is ergodic (indeed strongly mixing) for any initial law. Toy case: $P(0|1)=P(1|0)=1$, $P(S_0=0)=0.5$. It has two paths, $(0101\dots)$ and $(1010\dots)$, each with probability $\tfrac12$. It is ergodic in the sense of Def. 12.4 but not in the Markov-chain-literature sense (irreducible, aperiodic, recurrent). The author calls this clash of terminology a frequent source of confusion.

Stationary zero-mean Gaussian process with $c(n)=\mathbb E[S_0S_n^*]$ (p. 233):
$$\lim_n\tfrac1{n+1}\sum_{t=0}^nc(t)=0\iff\text{ergodic}\iff\text{weakly mixing};\qquad \lim_n c(n)=0\iff\text{mixing}.$$
The spectral measure $\mu$ on $[-\pi,\pi]$ satisfies $c(n)=\frac1{2\pi}\int e^{inx}\mu(dx)$. The process is ergodic iff $\mu$ has no atoms, and a B-process iff $\mu$ has a density.

*Intuition note:* ergodic means shift-invariant events are deterministic, and (Birkhoff–Khintchine, p. 234) time averages along one trajectory converge to expectations. An ergodic process can have infinite memory in general, but the memory is weak; for Gaussian processes this means the correlation dies in the Cesàro-mean sense (p. 233).

### 12.2 Shannon–McMillan, entropy rate and AEP (pp. 233–234)
**Theorem 12.5 (Shannon–McMillan–Breiman).** For stationary ergodic discrete $\mathbb S$ with entropy rate $\mathcal H$:
$$\frac1n\log\frac1{P_{S^n}(S^n)}\xrightarrow{\ \mathbb P\ }\mathcal H,\quad\text{also a.s. and in }L^1.\tag{12.3}$$

**Corollary 12.6.** With $f^*_n$ the optimal variable-length compressor and $\epsilon^*(S^n,nR)$ the optimal fixed-length error probability:
$$\tfrac1n\ell(f_n^*(S^n))\xrightarrow{\mathbb P}\mathcal H,\qquad \lim_n\epsilon^*(S^n,nR)=\begin{cases}0&R>\mathcal H\\1&R<\mathcal H\end{cases}\tag{12.4}$$
*Proof.* By Cor. 10.5 the asymptotic laws of $\frac1n\ell(f_n^*)$ and $\frac1n\log\frac1{P_{S^n}}$ coincide. By Thm 12.5 (convergence in probability suffices) the latter tends to the constant $\mathcal H$ (p. 233).

**Corollary 12.7 (AEP).** For $\delta>0$ let $T_n^\delta=\{s^n:|\frac1n\log\frac1{P_{S^n}(s^n)}-\mathcal H|\le\delta\}$. Then (1) $P[S^n\in T_n^\delta]\to1$; (2) $e^{n(\mathcal H-\delta)}(1+o(1))\le|T_n^\delta|\le e^{(\mathcal H+\delta)n}(1+o(1))$ (p. 234). (Cor. 12.6 states $\mathcal H$ in bits, while Cor. 12.7 writes $\exp$ as printed; read $\exp$ with the matching log base.)

History as stated (p. 234): Markov chains in probability, ref. [378]; $L^1$ extension, McMillan; a.s., Breiman. For Markov chains, a trajectory is a transformation of iid choices of transitions, so it should concentrate similarly.

*Intuition note:* it is the law of large numbers applied to log-probabilities. With probability tending to 1, a long sequence lies in the typical set, where its probability is about $e^{-n\mathcal H}$ (up to the log base). Hence compression below $\mathcal H$ fails and compression above it works (Cor. 12.6).

### 12.3 Proof of Shannon–McMillan–Breiman (pp. 234–236)
Only $L^1$ convergence is proved (it implies convergence in probability). Almost-sure convergence is not proved (p. 234).

**Theorem 12.8 (Birkhoff–Khintchine).** For stationary ergodic $\{S_i\}$ and $\mathbb E|f(S_1,\dots)|<\infty$: $\lim_n\frac1n\sum_{k=1}^nf(S_k,\dots)=\mathbb E f(S_1,\dots)$ a.s. and in $L^1$. If $f=f(S_1,\dots,S_m)$ the sum is $\frac1n\sum_k f(S_k,\dots,S_{k+m-1})$ (p. 234). Proof in 12.4.

Example 12.1 (p. 235): for $f=f(S_1)$ and iid this is the strong law of large numbers. For constant trajectories $S_i=S_1$ the process is non-ergodic and the conclusion fails unless $S_1$ is a.s. constant.

**Definition 12.9.** $\{S_i\}$ is an $m$th-order Markov chain if $P_{S_{t+1}|S_1^t}=P_{S_{t+1}|S_{t-m+1}^t}$ for $t\ge m$. It is time homogeneous if this equals $P_{S_{m+1}|S_1^m}$ (p. 235).

**Remark 12.2** (p. 235). For a time-homogeneous $m$th-order chain, (12.3) follows directly. The chain rule gives $\frac1n\log\frac1{P_{S^n}(S^n)}=\frac1n\sum_{t=1}^n\log\frac1{P_{S_t|S^{t-1}}(S_t|S^{t-1})}$; the first $m$ terms are split off and the Markov property is used for the rest:
$$\frac1n\log\frac1{P_{S^n}(S^n)}=\underbrace{\frac1n\log\frac1{P_{S^m}(S^m)}}_{\to0}+\underbrace{\frac1n\sum_{t=m+1}^n\log\frac1{P_{S_{m+1}|S_1^m}(S_t|S_{t-m}^{t-1})}}_{\to H(S_{m+1}|S_1^m)\text{ by Birkhoff–Khintchine}}\tag{12.5}$$
using $f(s_1,s_2,\dots)=\log\frac{1}{P_{S_{m+1}|S_1^m}(s_{m+1}|s_1^m)}$.

**Proof of Thm 12.5 in $L^1$** (Shannon's Markov approximation, pp. 235–236). Fix $m$. Define
$$Q^{(m)}(S_1^\infty)=P_{S_1^m}(S_1^m)\prod_{t=m+1}^\infty P_{S_{m+1}|S_1^m}(S_t|S_{t-m}^{t-1}),$$
an $m$th-order time-homogeneous Markov chain. Let $\mathcal H_m=H(S_{m+1}|S_1^m)$. By the triangle inequality, $\mathbb E|\frac1n\log\frac1{P_{S^n}}-\mathcal H|\le A+B+C$, where
- $A=\mathbb E\big|\frac1n\log\frac1{P_{S^n}}-\frac1n\log\frac1{Q^{(m)}_{S^n}}\big|$,
- $B=\mathbb E\big|\frac1n\log\frac1{Q^{(m)}_{S^n}}-\mathcal H_m\big|$,
- $C=|\mathcal H_m-\mathcal H|$.

Term by term:
- $C\to0$ as $m\to\infty$, by Thm 5.4 ($H(S_{m+1}|S_1^m)\downarrow\mathcal H$ for stationary processes).
- $B\to0$ as $n\to\infty$ for fixed $m$, by Remark 12.2.
- For $A$, Lemma 12.10 gives $\mathbb E[A]\le\frac1nD(P_{S^n}\|Q^{(m)}_{S^n})+\frac{2\log e}{en}$, where by stationarity
$$\tfrac1nD(P_{S^n}\|Q^{(m)}_{S^n})=\tfrac1n\big(-H(S^n)+H(S^m)+(n-m)\mathcal H_m\big)\to\mathcal H_m-\mathcal H.$$

Hence $\limsup_n\mathbb E|\cdot|\le2(\mathcal H_m-\mathcal H)$ for every $m$; let $m\to\infty$.

**Lemma 12.10.** $\mathbb E_P\big|\log\frac{dP}{dQ}\big|\le D(P\|Q)+\frac{2\log e}{e}$. *Proof:* $|x\log x|-x\log x\le\frac{2\log e}e$ for $x>0$. The left side is 0 for $x\ge1$, and for $x<1$ it is at most $2\sup_{0\le x\le1}x\log\frac1x=\frac{2\log e}e$.

*Intuition note:* a finite-memory model $Q^{(m)}$ is close enough to the true process that its log-loss and the true one differ by about $\mathcal H_m-\mathcal H$. That gap shrinks as the memory length $m$ grows.

### 12.4* Proof of Birkhoff–Khintchine (pp. 237–239)
**Setup** (p. 237). Any $\tilde f\in L^1$ splits as $\tilde f=f+h$ with $f$ bounded and $\|h\|_1\le\epsilon$. Bounded implies $f\in L^2$, a Hilbert space with $(f,g)=\mathbb E[f\bar g]$. Define $T f=f\circ\tau$. Then $\|Tf\|_2=\|f\|_2$, so $T$ is unitary. Define $A_n f=\frac1n\sum_{k=1}^nf\circ\tau^k$. Heuristically $A_n=\frac1n\sum T^k=\frac1n(I-T^n)(I-T)^{-1}$, so only the part of $f$ in $\ker(I-T)$ should survive.

Decompose $f=f_1+f_2$ with $f_1\in\ker(I-T)$, $f_2\in\ker(I-T)^\perp$. Facts used (p. 237):
- $g\in\ker(I-T)$ must be constant, by ergodicity. If $g=Tg$ were non-constant, some $\{g\in(a,b)\}$ would be invariant with non-trivial measure.
- $\ker(I-T)=\ker(I-T^*)$, because $T$ is unitary. From $g=Tg$: $\|g\|^2=(Tg,g)=(g,T^*g)$, and equality in Cauchy–Schwarz forces $T^*g=g$.
- $\ker(I-T)^\perp=[\mathrm{Im}(I-T)]$ ($L^2$ closure).
- $g\in\ker(I-T)^\perp\iff\mathbb E g=0$.

So $f_1=m$ is constant and $A_nf_1=f_1=\mathbb E[f]$. Approximate $f_2=f_0+h_1$ with $f_0=g-g\circ\tau$, $g\in L^2$, $\|h_1\|_1\le\|h_1\|_2<\epsilon$. Then $A_nf_0=\frac1n(g-g\circ\tau^n)\to0$ a.s. and in $L^1$. The a.s. part holds because $\mathbb E\sum_n(\frac{g\circ\tau^n}n)^2=\mathbb E[g^2]\sum\frac1{n^2}<\infty$ and Borel–Cantelli.

What remains is
$$P\big[\limsup_nA_n(h+h_1)\ge\delta\big]\le 2\epsilon/\delta.\tag{12.6}$$
Then letting $\epsilon\to0$ gives $P[\limsup A_n(f)\ge\mathbb E[f]+\delta]=0$, and the opposite direction is analogous (p. 238). (Added step: the source only says (12.6) uses Thm 12.11. Since $\|h+h_1\|_1\le2\epsilon$, Thm 12.11 gives $P[\sup_nA_n(h+h_1)>a]\le2\epsilon/a$ for every $a>0$. Applying it with $a$ slightly below $\delta$ and letting $a\uparrow\delta$ gives the bound $2\epsilon/\delta$ for $\{\limsup\ge\delta\}$, up to the index convention $k=0..n-1$ vs $k=1..n$.)

**Theorem 12.11 (Maximal ergodic lemma).** For $f\in L^1(P)$ and p.p.t. $\tau$, with $A_nf=\frac1n\sum_{k=0}^{n-1}f\circ\tau^k$:
$$P\big[\sup_{n\ge1}A_nf>a\big]\le\frac{\mathbb E[f\mathbf 1\{\sup_nA_nf>a\}]}a\le\frac{\|f\|_1}a.$$
It is a "weak $L^1$" estimate and is equivalent to Lemma 12.12 (p. 238).

**Lemma 12.12.** For a stationary $\{Z_n\}$ with $\mathbb E|Z_1|<\infty$: $P[\sup_{n\ge1}\frac{Z_1+\dots+Z_n}n>a]\le\frac{\mathbb E|Z_1|}a$ for all $a>0$.

*Proof (Garsia)* (pp. 238–239). Let $S_n=\sum_{k\le n}Z_k$, $L_n=\max\{0,Z_1,\dots,Z_1+\dots+Z_n\}$, $M_n=\max\{0,Z_2,\dots,Z_2+\dots+Z_n\}$, $Z^*=\sup_nS_n/n$. It suffices to show
$$\mathbb E[Z_1\mathbf 1\{Z^*>0\}]\ge0.\tag{12.7}$$
Applied to $\tilde Z_1=Z_1-a$ (so $\tilde Z^*=Z^*-a$) it gives $\mathbb E[Z_1\mathbf 1\{Z^*>a\}]\ge aP[Z^*>a]$, and the lemma follows by bounding the left side by $\mathbb E|Z_1|$. Now $Z_1+M_n=\max\{S_1,\dots,S_n\}$, and $Z_1+M_n=L_n$ on $\{L_n>0\}$. So $Z_1\mathbf 1\{L_n>0\}=L_n-M_n\mathbf 1\{L_n>0\}$ (no indicator needed on $L_n$, since $L_n=0$ off $\{L_n>0\}$). Then
$$\mathbb E[Z_1\mathbf 1\{L_n>0\}]=\mathbb E[L_n]-\mathbb E[M_n\mathbf 1\{L_n>0\}]\ge\mathbb E[L_n]-\mathbb E[M_n]=\mathbb E[L_n]-\mathbb E[L_{n-1}]\ge0,\tag{12.8}$$
using $M_n\ge0$, $M_n\overset d=L_{n-1}$, and $L_n\ge L_{n-1}$. Let $n\to\infty$ with $\{L_n>0\}\nearrow\{Z^*>0\}$ to get (12.7).

*Intuition note:* the maximal lemma bounds how often running averages can be large. That control gives (12.6): the error part $h+h_1$ has a small probability of a large limsup, while the invariant part gives the constant $\mathbb E f$.

### 12.5* Sinai's generator theorem (pp. 239–243)
Motivation (p. 239): atoms move deterministically, yet large systems behave probabilistically. Any description at time $t$ uses finitely many bits, so from a finite-bit viewpoint $\tau$ appears to act stochastically.

**Definition 12.13.** $\mathcal H(\tau)\triangleq\sup_{X_0}\lim_{n\to\infty}\frac1nH(X_0,X_0\circ\tau,\dots,X_0\circ\tau^{n-1})$, the supremum over finitely-valued $F$-measurable $X_0$. Equivalently, it is the maximal entropy rate of the processes $X_k=X_0\circ\tau^k$ (p. 240).

Terms (p. 240): $\mathcal G\subset\mathcal F$ is *$P$-dense* ($\mathcal G=\mathcal F$ mod $P$) if every $E\in\mathcal F$ has $E'\in\mathcal G$ with $P[E\Delta E']=0$. $Y$ with countable alphabet is a *generator* if $\sigma\{Y,Y\circ\tau,\dots\}=\mathcal F$ mod $P$. (Generating partitions are defined analogously.)

**Theorem 12.14 (Sinai).** If $Y$ is a generator and the entropy rate $H(\mathbb Y)$ of $\mathbb Y=\{Y\circ\tau^k\}$ is finite, then $\mathcal H(\tau)=H(\mathbb Y)$ (p. 240).

*Proof, part 1: $\mathcal H(\tau)\ge H(\mathbb Y)$* (pp. 240–241). For finite alphabet this is the definition. Otherwise take $Y\in\mathbb Z_+$ and $\tilde Y_m=\min(Y,m)$. Lower semicontinuity of mutual information (4.28) gives $\lim_mI(Y;\tilde Y_m)\ge H(Y)$, so $H(Y|\tilde Y)\le\epsilon$ for large $m$. Then
$$H(Y_0^n)=H(\tilde Y_0^n)+H(Y_0^n|\tilde Y_0^n)=H(\tilde Y_0^n)+\sum_{i=0}^nH(Y_i|\tilde Y_0^n,Y_0^{i-1})\le H(\tilde Y_0^n)+\sum_{i=0}^nH(Y_i|\tilde Y_i)=H(\tilde Y_0^n)+nH(Y|\tilde Y)\le H(\tilde Y_0^n)+n\epsilon.$$
So the finite-alphabet process $\tilde{\mathbb Y}$ has entropy rate arbitrarily close to $H(\mathbb Y)$.

*Part 2: every adapted stationary $\mathbb X$ has $H(\mathbb X)\le H(\mathbb Y)$* (p. 241). Take finite $\mathcal X$ and $X_k=X\circ\tau^k$. By the generating property, $X$ is a function of $Y_0^\infty$ (mod 0). Continuity of mutual information in σ-algebras (4.30) gives $H(X_0)=I(X_0;Y_0^\infty)=\lim_nI(X_0;Y_0^n)$, i.e. $H(X_0|Y_0^n)\to0$. Fix $\epsilon$ and choose $m$ with $H(X_0|Y_0^m)\le\epsilon$. Then
$$H(X_0^n)\le H(X_0^n,Y_0^n)=H(Y_0^n)+H(X_0^n|Y_0^n)\le H(Y_0^n)+\sum_{i=0}^nH(X_i|Y_i^n)=H(Y_0^n)+\sum_{i=0}^nH(X_0|Y_0^{n-i})\le H(Y_0^n)+m\log|\mathcal X|+(n-m)\epsilon,$$
by stationarity of $(X_k,Y_k)$ and $H(X_0|Y_0^{n-i})<\epsilon$ for $i\le n-m$. Dividing by $n$ gives $H(\mathbb X)\le H(\mathbb Y)+\epsilon$.

*Alternative proof of part 2* (pp. 241–242). If $X_0=f(Y_0^\infty)$, there are $m(\epsilon)$ and $f_\epsilon:\mathcal Y^{m+1}\to\mathcal X$ with $P[f(Y_0^\infty)\ne f_\epsilon(Y_0^m)]\le\epsilon$. Define $\tilde X_j=f_\epsilon(Y_j^{m+j})$. Then $H(\tilde X_0^n)\le H(Y_0^{n+m})$, so $H(\tilde{\mathbb X})\le H(\mathbb Y)$. Also $P[\tilde X_j\ne X_j]\le\epsilon$, so by Cor. 6.7 $|H(\mathbb X)-H(\tilde{\mathbb X})|\le\epsilon\log|\mathcal X|+h(\epsilon)$. Hence $H(\mathbb X)\le H(\mathbb Y)+\epsilon\log|\mathcal X|+h(\epsilon)$.

**Examples** (p. 242).
- Doubling map on $[0,1]$ with Lebesgue measure: $\tau(\omega)=2\omega\bmod1$. $Y=\mathbf 1\{\omega<1/2\}$ is a generator and $\mathbb Y$ is iid Ber(1/2), so $\mathcal H(\tau)=\log2$. However fine the discrete measurements, the process has entropy rate $\log 2$ bits per measurement. The author says this reconciles the Newtonian (dynamical) and Gibbsian (statistical) views. A ternary measurement $Y'=\mathbf 1\{\omega>1/3\}+\mathbf 1\{\omega>2/3\}$ still gives the same entropy rate.
- Rotation $\tau(\omega)=\omega+\gamma$ on the circle (ergodic when $\gamma/2\pi$ is irrational, "known"). $Y=\mathbf 1\{|\omega|<2\pi\epsilon\}$ is a generator for arbitrarily small $\epsilon$, so $\mathcal H(\tau)\le H(\mathbb X)\le H(Y_0)=h(\epsilon)\to0$: a zero-entropy p.p.t. (as printed).

**Remark 12.3** (p. 243). Two p.p.t.s are isomorphic if there are a.e.-defined maps $f_i$ intertwining the $\tau$'s, mutually inverse a.e., and carrying measures to measures. KS entropies of isomorphic p.p.t.s are equal (Kolmogorov, 1958). So the shifts of iid Ber(1/2) and iid Ber(1/3) are not isomorphic. The spectrum of $U_\tau\phi=\phi\circ\tau$ (12.9–12.10) cannot distinguish them, because for any non-constant iid process it is the whole unit circle (footnote 2).

*Intuition note:* KS entropy is the largest entropy rate that finite measurements of the system can show. For the doubling map, the measurement $\mathbf 1\{\omega<1/2\}$ reveals one fresh bit of the initial point per step, giving rate $\log 2$; the author says the ternary measurement gives the same rate. This is why a deterministic map seen through finite measurements looks random.

## Toy example (ours)
Binary stationary Markov chain: $P(\text{stay})=0.9$, $P(\text{flip})=0.1$, initial law uniform. (It is irreducible, so ergodic.) Entropy rate: $\mathcal H=h(0.1)=0.1\log_2 10+0.9\log_2\frac1{0.9}=0.1(3.3219)+0.9(0.1520)=0.3322+0.1368=0.469$ bits.

Take $n=10$ and a sequence with 8 stays and 1 flip among its 9 transitions. By (12.5), $\log_2\frac1P=1+8(0.1520)+3.3219=1+1.2160+3.3219=5.538$ bits. Per symbol this is $0.554$, close to $0.469$. The gap is mainly the first-symbol term $\frac1n\cdot1=0.1$. As $n$ grows, the fraction of flips tends to $0.1$ (Birkhoff–Khintchine), so the average tends to $0.469$. The typical set then has about $2^{0.469n}$ sequences, not $2^n$.

## Concepts
- [[entropy-rate]] — $\mathcal H(\mathbb S)$, per-symbol entropy of a stationary process; limit of $H(S_{m+1}|S_1^m)$ from above (pp. 233, 236)
- [[typical-set-aep]] — $T_n^\delta$ holds almost all probability and has about $e^{n\mathcal H}$ elements (p. 234)
- [[source-coding-theorem]] — for ergodic sources, length per symbol $\to\mathcal H$; fixed-length error $\to0/1$ (p. 233)
- [[relative-entropy-kl]] — used to bound term $A$ in the proof (p. 236)
- [[mutual-information]] — semicontinuity and σ-algebra continuity used in Sinai's proof (pp. 240–241)
- [[measure-preserving-transformation]] (new) — $\tau$ with $P(\tau^{-1}E)=P(E)$ (p. 230)
- [[stationary-process]] (new) — $S_j=S_0\circ\tau^j$ for a p.p.t. $\tau$ (p. 230)
- [[ergodic-process]] (new) — all shift-invariant events have probability 0 or 1; differs from the Markov-chain use of "ergodic" (p. 232)
- [[mixing]] (new) — strong/weak mixing, both stronger than ergodicity (p. 232)
- [[shannon-mcmillan-breiman]] (new) — a.s./$L^1$ convergence of $\frac1n\log\frac1{P(S^n)}$ to $\mathcal H$ (p. 233)
- [[birkhoff-ergodic-theorem]] (new) — time averages converge to expectations for ergodic processes (p. 234)
- [[markov-approximation]] (new) — approximating a process by an $m$th-order chain $Q^{(m)}$ (p. 235)
- [[kolmogorov-sinai-entropy]] (new) — sup over finite measurements of the entropy rate of $X_0\circ\tau^k$ (p. 239)
- [[generator-sinai]] (new) — $Y$ whose shifts generate $\mathcal F$ mod $P$; with finite entropy rate it gives $\mathcal H(\tau)$ (pp. 240)

## Canonical instances
- [[doubling-map]] — $\tau(\omega)=2\omega\bmod1$ equals the shift on iid Ber(1/2); $\mathcal H(\tau)=\log2$ (pp. 232, 242)
- [[irrational-rotation]] — ergodic with zero KS entropy (p. 242)
- [[constant-process]] — $S_k=S_0$: stationary, not ergodic (p. 232)
- [[alternating-markov-chain]] — $0101\dots$ vs $1010\dots$: ergodic in the process sense (p. 232)
- [[gaussian-process-ergodicity]] — Cesàro decay of $c(n)$ gives ergodicity (p. 233)

## Bridges (candidates)
- [structural-analogy] Birkhoff time average = ensemble average ↔ statistics: law of large numbers; iid case is the SLLN (p. 235).
- [structural-analogy] $m$th-order Markov approximation $Q^{(m)}$, cost $\mathcal H_m-\mathcal H$ ↔ language modelling: finite-context models and cross-entropy.
- [metaphor] KS entropy and finite measurements ↔ statistical mechanics: coarse-grained description makes deterministic dynamics look stochastic.

## Questions this raises
- Almost-sure SMB convergence is not proved here. What extra tools does Breiman's argument need?
- How fast does $\frac1n\log\frac1{P_{S^n}}$ converge, i.e. what do second-order (fluctuation) results look like for ergodic processes?
- Is the entropy rate the only isomorphism invariant that separates Bernoulli shifts?
- For a general p.p.t., when does a generator with finite entropy rate exist?

## Exercises worth doing
- Exercise (p. 230) — show $\mathcal F_{inv}$ is a σ-algebra — difficulty: easy.
- Ex. II.12 (p. 232) — strong mixing ⇒ weak mixing ⇒ ergodic — difficulty: medium.

## Reading notes
- Printed page = pdf page − 25. The unit's id says "ch14", but the printed chapter number is 12, and section numbers are 12.x.
- Text-layer equations were garbled in places. All math above was checked against the images.
- Weak mixing (p. 232): the displayed formula has $\tau^{-n}B$ inside a sum over $k$, as printed. $\tau^{-k}$ was probably meant.
- In Sinai's proof, p. 241: the sum has $n+1$ terms but is written $nH(Y|\tilde Y)$ as printed. On p. 242, "Dividing by $m$" probably means by $n$.
- Theorem 12.8 sums over $k=1..n$ and Thm 12.11 over $k=0..n-1$, as printed.
- Sections 12.4* and 12.5* carry an asterisk in their headings (the pages do not say why). Footnote 1 (p. 234) gives biographical remarks on McMillan and Breiman; footnote 2 (p. 243) gives the spectrum argument.
