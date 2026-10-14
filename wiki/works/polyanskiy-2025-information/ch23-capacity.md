---
id: polyanskiy-2025-information/ch23-capacity
work: polyanskiy-2025-information
unit: "Chapter 21 (printed) — Capacity per unit cost"
pages: 410-421
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Capacity per unit cost

## L0 — One line
When the total cost of a codeword is limited instead of the blocklength, the best rate per unit cost is the supremum of a ratio of KL divergence to cost (for memoryless channels with a zero-cost symbol), which gives the AWGN minimum of $N_0/\log_2 e$ energy per bit (−1.59 dB).

## L1 — The gist (≤ 120 words)
A deep-space probe must send $k$ bits with a limited energy budget; the duration of transmission matters little. How little energy per bit is enough? For the AWGN channel the limit is $N_0/\log_2 e$ as $k\to\infty$ and then $\epsilon\to0$. The same limit holds for Rayleigh fading unknown to the receiver. Verdú's theorem covers stationary memoryless channels with a zero-cost symbol $x_0$: capacity per unit cost is $\sup_{x\ne x_0} D(P_{Y|X=x}\|P_{Y|X=x_0})/\mathsf c(x)$, with no need to know the capacity-cost function. The chapter then derives the continuous-time AWGN capacity $\frac{P}{N_0}\log e$ and sketches (not rigorously) the bandlimited formula $B\log(1+P/(N_0B))$. Fading leaves the limit unchanged but changes the optimal coding style ("flash signaling") and slows convergence.

**Prerequisites:** Fano's inequality; data processing; Gaussian capacity $\frac12\log(1+P/\sigma^2)$; KL divergence; Stein's lemma; Q-function; Fourier/sampling basics.

## L2 — Key ideas
- Energy-per-bit: for the AWGN channel (output = input plus Gaussian noise, noise level $N_0/2$ per real component), $\lim_{\epsilon\to0}\limsup_{k\to\infty}E^*(k,\epsilon)/k=N_0/\log_2 e$ (−1.59 dB). The optimum needs vanishing power per channel use, so the rate per slot goes to zero (pp. 411–412).
- Pulse-position modulation (PPM: one spike at a position that codes the message) achieves this limit with explicit error bounds (pp. 412–413).
- For a stationary memoryless channel with a zero-cost symbol $x_0$, capacity per unit cost equals $\sup_{x\ne x_0} D(P_{Y|X=x}\|P_{Y|X=x_0})/\mathsf c(x)$, where $D$ is the KL divergence (a measure of how different two distributions are) (Theorem 21.4, p. 414). Under the assumptions $P_0=0$, $C(0)=0$ the author says it equals $C'(0)$, the slope at 0 of the capacity-cost function $C(P)$ (capacity under cost constraint $P$), and the theorem needs no knowledge of $C(P)$ (pp. 414–416).
- Converse: compare with a "useless channel". Achievability: a PPM-style code plus Stein's lemma (pp. 415–416).
- Rayleigh fading (random multiplicative gain) with the gain unknown to the receiver (no CSI, i.e. no channel state information) gives the same $\log e/N_0$. The supremum is approached as $|x|\to\infty$, so any code achieving it must be spiky ("flash signaling") (pp. 416–417).
- Finite-blocklength convergence to −1.59 dB is much slower under fading, as shown by the stated expansions and Figure 21.1 (pp. 417–418).
- Continuous-time AWGN reduces to the discrete energy-per-bit problem. Its capacity is $\frac{P}{N_0}\log e$ per unit time (pp. 418–419).
- Bandlimited sketch (not a rigorous theorem): sampling at rate $B$ gives $BT$ complex uses with power $P/B$. This yields $B\log(1+\frac{P}{N_0B})$, and as $B\to\infty$ the capacity tends to $\frac{P}{N_0}\log e$ (pp. 419–421).

## L3 — Walkthrough

### 21.1 Energy-per-bit
**Setup.** Channels act on infinite sequences. AWGN:
$$Y_i=X_i+Z_i,\quad Z_i\sim\mathcal N(0,N_0/2)\tag{21.1}$$
Here $N_0$ is the flat noise power spectral density, and each real component of the complex noise has power $N_0/2$. Thermodynamics suggests $N_0=kT$, with $k$ the Boltzmann constant and $T$ the absolute temperature (p. 410). Notation: $\|v\|_2^2=\sum_j v_j^2$ (p. 410).

**Definition 21.1.** An $(E,2^k,\epsilon)$-code is an encoder $f:[2^k]\to\mathbb R^\infty$ and a decoder $g:\mathbb R^\infty\to[2^k]$ (or similar randomized versions) with $\|f(m)\|_2^2\le E$ for all $m$ and $\mathbb P[g(Y^\infty)\ne W]\le\epsilon$, where $W\sim\mathrm{Unif}([2^k])$. Then $E^*(k,\epsilon)=\min\{E:\exists(E,2^k,\epsilon)\text{ code}\}$ (p. 411).

**Theorem 21.2** ($(E_b/N_0)_{\min}=-1.6$ dB).
$$\lim_{\epsilon\to0}\limsup_{k\to\infty}\frac{E^*(k,\epsilon)}{k}=\frac{N_0}{\log_2 e}\tag{21.2}$$
The value is $10\log_{10}(1/\log_2 e)\approx-1.592$. The result was first obtained by Shannon, and turbo codes first resolved the quest to achieve it. The limit is unchanged for the complex C-AWGN channel, because one complex input becomes two real inputs (p. 411).

*Converse.* With $W\to X^\infty\to Y^\infty\to\hat W$ and $\bar\epsilon=1-\epsilon$ (p. 411):
$$-h(\epsilon)+\bar\epsilon k\le d\big((1-\epsilon)\,\|\,\tfrac1M\big)\ \text{(Fano)}\ \le I(W;\hat W)\ \text{(data processing, divergence)}\ \le I(X^\infty;Y^\infty)\ \text{(data processing, MI)}\ \le\sum_{i\ge1}I(X_i;Y_i)\ \text{(uses (4.30))}$$
(p. 411), continuing:
$$\le\sum_i\tfrac12\log\Big(1+\frac{\mathbb EX_i^2}{N_0/2}\Big)\ \text{(Gaussian capacity)}\ \le\frac{\log e}{2}\sum_i\frac{\mathbb EX_i^2}{N_0/2}\ \text{(linearization of log)}\ \le\frac{E}{N_0}\log e.$$
Hence $\frac{E^*(k,\epsilon)}{k}\ge\frac{N_0}{\log e}\big(\bar\epsilon-\frac{h(\epsilon)}{k}\big)$. Taking the limits finishes the converse (p. 412).

*Achievability (existential).* An $(n,2^k,\epsilon,P)$-code is an $(nP,2^k,\epsilon)$-code, so $\log_2M^*(n,\epsilon,P)\ge k\Rightarrow E^*(k,\epsilon)\le nP$. Take $k_n=\lfloor\log_2M^*(n,\epsilon,P)\rfloor$. Then, using Theorem 20.11,
$$\limsup_n\frac{E^*(k_n,\epsilon)}{k_n}\le\limsup_n\frac{nP}{\log M^*}=\frac{P}{\frac12\log(1+\frac{P}{N_0/2})}.$$
Optimizing over $P$:
$$\limsup_n\frac{E^*(k_n,\epsilon)}{k_n}\le\inf_{P\ge0}\frac{P}{\frac12\log(1+\frac P{N_0/2})}=\lim_{P\to0}\frac{P}{\frac12\log(1+\frac P{N_0/2})}=\frac{N_0}{\log_2e}\tag{21.3}$$
(p. 412). The infimum is reached as $P\to0$. So reliable communication at the Shannon limit needs infinitely many time slots, and the information rate (spectral efficiency) must be vanishingly small. Nonzero spectral efficiency necessarily forces a step away from −1.6 dB (p. 412).

*Intuition note.* The energy per bit is smallest in the limit of vanishing power per channel use, so the bits must be spread over many weak transmissions. The linearization step $\log(1+x)\le x\log e$ is what bounds the information per use by its linear approximation in the energy.

*Explicit code: PPM.* $f(m)=\mathbf c_m=(0,\dots,0,\sqrt E,0,\dots)$, with $\sqrt E$ at position $m$ (21.4). With $M=2^k$ and $Z\sim\mathcal N(0,1)$ the error probability is bounded by
$$\epsilon\le\mathbb E\Big[\min\Big\{MQ\Big(\sqrt{\tfrac{2E}{N_0}}+Z\Big),1\Big\}\Big]\tag{21.5}$$
(p. 413). Derivation: for the orthogonal codebook with an ML decoder,
$$P_e=1-\frac1{\sqrt{\pi N_0}}\int_{-\infty}^{\infty}\Big[1-Q\Big(\sqrt{\tfrac2{N_0}}z\Big)\Big]^{M-1}e^{-\frac{(z-\sqrt E)^2}{N_0}}dz\tag{21.6}$$
This holds because, given $(W=j,Z_j)$, the events $\{\|\mathbf c_j+\mathbf z\|^2\le\|\mathbf c_j+\mathbf z-\mathbf c_i\|^2\}$, $i\ne j$, are independent. Substitute $x=\sqrt{2/N_0}\,z$ and use $1-(1-y)^{M-1}\le\min\{My,1\}$ to get (21.5) (p. 413).

To see that (21.5) gives (21.3): fix $c>0$ and condition on $|Z|\le c$, so $\epsilon\le MQ(\sqrt{2E/N_0}-c)+2Q(c)$. Use
$$\log Q(x)=-\tfrac{x^2\log e}{2}-\log x-\tfrac12\log2\pi+o(1),\quad x\to\infty\tag{21.7}$$
Set $E=(1+\tau)k\frac{N_0}{\log_2e}$. Then $2^kQ(\sqrt{2E/N_0}-c)\to0$ as $k\to\infty$. The author then says: choosing $c$ sufficiently large. (added step: take $c$ with $2Q(c)<\epsilon$, then $k$ large enough that $2^kQ(\sqrt{2E/N_0}-c)\le\epsilon-2Q(c)$, so the error is at most $\epsilon$.) This gives, for every $\tau>0$, $\limsup_k E^*(k,\epsilon)/k\le(1+\tau)\frac{N_0}{\log_2 e}$ (the source prints this without the division by $k$) (p. 413). Taking $\tau\to0$ implies (21.3) (p. 413).

**Remark 21.2 (simplex conjecture).** PPM achieves the first three terms of the large-$k$ expansion of $E^*(k,\epsilon)$. Subtracting the centre of gravity and rescaling gives the simplex code, which is *conjectured* optimal for fixed $k,\epsilon$ (p. 413).

### 21.2 Capacity per unit cost
**Definition 21.3.** With a cost $\mathsf c:\mathcal X\to\mathbb R_+$, an $(E,M,\epsilon)$-code has $f:[M]\to\mathcal X^\infty$ with $\sum_t\mathsf c(x_t)\le E$ (21.8) and error probability $\le\epsilon$. Let $M^*(E,\epsilon)=\max\{M:\exists(E,M,\epsilon)\text{-code}\}$. Then
$$C_{puc}\triangleq\lim_{\epsilon\to0}\liminf_{E\to\infty}\tfrac1E\log M^*(E,\epsilon)\tag{21.9}$$
(p. 414). Assuming $P_0=0$ and $C(0)=0$, the author says it is "not hard to show" (basically following the steps of Theorem 21.2) that $C_{puc}=\sup_P\frac{C(P)}P=\lim_{P\to0}\frac{C(P)}P=C'(0)$. Verdú's discovery is that $C_{puc}$ can be found without computing $C(P)$, which helps because $C(P)$ is unknown for many practical channels (p. 414).

**Theorem 21.4.** For a stationary memoryless channel with a zero-cost symbol $x_0$ ($P_0=\mathsf c(x_0)=0$):
$$C_{puc}=\sup_{x\ne x_0}\frac{D(P_{Y|X=x}\|P_{Y|X=x_0})}{\mathsf c(x)}\ (=:C_V).$$
In particular $C_{puc}=\infty$ if some $x_1\ne x_0$ has $\mathsf c(x_1)=0$ (p. 414).

*Converse.* Introduce the auxiliary "useless channel" $Q_{Y^\infty|X^\infty}=Q_{Y^\infty}\triangleq P^\infty_{Y|X=x_0}$. Let $d(x)\triangleq D(P_{Y|X=x}\|P_{Y|X=x_0})$. Then
$$(1-\epsilon)\log M+h(\epsilon)\le d(1-\epsilon\|\tfrac1M)\le D(P_{W,X^\infty,Y^\infty,\hat W}\|Q_{W,X^\infty,Y^\infty,\hat W})=D(P_{Y^\infty|X^\infty}\|Q_{Y^\infty}|P_{X^\infty})=\mathbb E\Big[\sum_t d(X_t)\Big]\tag{21.10}$$
Since $d(x)\le\mathsf c(x)C_V$, the right side is $\le C_V\,\mathbb E\sum_t\mathsf c(X_t)\le C_VE$. Divide by $E$ and take limits: $C_{puc}\le C_V$ (p. 415).

*Achievability.* For $x_1\in\mathcal X$ and $n\in\mathbb Z_+$, $f(m)$ has $x_1$ repeated $n$ times in the $m$-th block of length $n$ and $x_0$ in the other $n(M-1)$ positions. By Stein's lemma there is $S\subset\mathcal Y^n$ with $\mathbb P[Y^n\in S|x_1^n]\ge1-\epsilon_1$ and $\mathbb P[Y^n\in S|x_0^n]\le\exp\{-nD(P_{Y|X=x_1}\|P_{Y|X=x_0})+o(n)\}$ (p. 415). The (suboptimal) decoder declares $\hat W=m$ if the $m$-th block lies in $S$ (p. 416). The union bound gives $\epsilon\le\epsilon_1+M\exp\{-nD+o(n)\}$, and each codeword costs $n\mathsf c(x_1)$. Letting $n\to\infty$ and after "straightforward manipulations" (not spelled out), $C_{puc}\ge D(P_{Y|X=x_1}\|P_{Y|X=x_0})/\mathsf c(x_1)$. Taking the supremum over $x_1$ gives $C_{puc}\ge C_V$ (p. 416).

*Intuition note.* Each use of symbol $x$ gives $d(x)$ units of distinguishability from the "silent" symbol $x_0$ and costs $\mathsf c(x)$. So per unit of cost it gives at most $d(x)/\mathsf c(x)\le C_V$. The best symbol is the one with the most distinguishability per unit cost. Repeating it $n$ times in one block of an otherwise silent codeword achieves this in the limit.

### 21.3 Energy-per-bit for the fading channel
Theorem 21.4 seems pointless for AWGN, since $C(P)$ is known there. Its true strength is revealed for channels with unknown $C(P)$. Take non-coherent Rayleigh fading: $Y_j=H_jX_j+Z_j$, $H_j\sim\mathcal N_c(0,1)\perp Z_j\sim\mathcal N_c(0,N_0)$, $H_j$ unknown to the receiver, $\mathsf c(x)=|x|^2$ (p. 416):
$$C_{puc}=\sup_{x\ne0}\frac{D(\mathcal N_c(0,|x|^2+N_0)\|\mathcal N_c(0,N_0))}{|x|^2}=\frac1{N_0}\sup_{x\ne0}\Big(\log e-\frac{\log(1+|x|^2/N_0)}{|x|^2/N_0}\Big)=\frac{\log e}{N_0}\tag{21.11}$$
The capacity per unit cost, and so the minimal energy per bit, is therefore unaffected by fading (p. 416). One important difference: the supremum in (21.11) is solved at $x=\infty$. Following the proof of the converse, any code hoping to achieve optimal $C_{puc}$ must satisfy $\sum_t|x_t|^2\mathbb 1\{|x_t|\ge A\}\approx\sum_t|x_t|^2$ for all $A>0$. That is, the energy must be almost entirely concentrated in very large spikes. This is called "flash signaling". Non-fading AWGN allows relatively non-spiky codewords because of rotational symmetry. Under fading the only hope of achieving full $C_{puc}$ is signaling in short bursts of energy (p. 417).

Finite-blocklength expansions of $E^*(k,\epsilon)/k$ (p. 417):
- AWGN: $(-1.59\text{ dB})+\sqrt{\text{constant}/k}\;Q^{-1}(\epsilon)$.
- Non-coherent fading: $(-1.59\text{ dB})+\sqrt[3]{\frac{\log k}{k}\,\big(Q^{-1}(\epsilon)\big)^2}$.

Convergence is much slower under fading. The number of data bits needed is about a factor $10^3$ larger (p. 417). Figure 21.1: reaching −1.5 dB takes about $6\cdot10^4$ bits for AWGN, or for fading with $H_j$ known at the receiver. With no knowledge of $H_j$ it takes at least $7\cdot10^7$ bits (p. 418).

### 21.4 Continuous-time AWGN channel
Engineers' model: $Y(t)=X(t)+N(t)$, with $\mathbb E[N(t)N(s)]=\frac{N_0}2\delta(t-s)$. Mathematicians' model: $Y_{int}(t)=\int_0^tX(\tau)d\tau+\sqrt{N_0/2}\,W_t$, with $W_t$ a Wiener process, $\mathbb E[W_sW_t]=\min(s,t)$ (pp. 417–418). $M^*(T,\epsilon,P)$ is the maximum number of messages whose waveforms are non-zero only on $[0,T]$ with $\int_0^Tx^2\le TP$ (p. 418).

**Theorem 21.5.**
$$\lim_{\epsilon\to0}\liminf_{T\to\infty}\tfrac1T\log M^*(T,\epsilon,P)=\frac P{N_0}\log e\tag{21.12}$$
*Proof.* $L_2[0,T]$ has a countable basis, so expanding the waveforms gives $\tilde Y_j=\tilde X_j+\tilde Z_j$, $\tilde Z_j\sim\mathcal N(0,N_0/2)$, with $\sum_j\tilde X_j^2\le PT$. This is the discrete energy-per-bit problem, with $\log_2M^*(T,\epsilon,P)=k\iff E^*(k,\epsilon)=PT$ (as the author writes). By Theorem 21.2 the limit is $P/(N_0/\log_2e)$ (p. 419).

### 21.5* Bandlimited continuous-time channel (sketch, not rigorous)
Claim, with spectrum confined to $[f_c-B/2,f_c+B/2]$ (p. 419):
$$C_B(P)=\lim_{\epsilon\to0}\liminf\tfrac1T\log M^*_{CT}(T,\epsilon,P,B)=B\log\Big(1+\frac P{N_0B}\Big)\tag{21.13}$$
A footnote notes that finite duration and finite bandwidth hold together only for the zero waveform. Rigorously, one should relax the bandwidth constraint to vanishing out-of-band energy as $T\to\infty$, and the rigorous treatment leads to prolate spheroidal functions (p. 419). Steps (p. 420):
- Modulation: $X(t)=\mathrm{Re}(X_B(t)\sqrt2e^{j\omega_ct})$, $\omega_c=2\pi f_c$. Demodulation is by low-pass filtering to $[-B/2,B/2]$, and no information is lost.
- Result: $Y_B(t)=X_B(t)+\tilde N(t)$, with complex white noise, $\mathbb E[\tilde N(t)\tilde N(s)^*]=N_0\delta(t-s)$.
- Nyquist sampling at spacing $1/B$ loses nothing, giving $Y_i=X_i+Z_i,\ Z_i\sim\mathcal N_c(0,N_0)$ (21.14). The channel is only allowed to be used for $i=1,\dots,TB$: $BT$ complex degrees of freedom.

Summary (p. 421): the equivalent channel is discrete C-AWGN with blocklength $n=BT$. The power constraint is $\sum_{i=1}^{BT}|X_i|^2=\|X(t)\|_2^2\le PT$, so $P_d=P/B$. Hence $\frac1T\log M^*_{CT}(T,\epsilon,P,B)=\frac1T\log M^*_{\mathbb C\text{-AWGN}}(BT,\epsilon,P_d)$, and $T\to\infty$ gives (21.13). For $B\to\infty$, $B\log(1+\frac P{N_0B})\to\frac P{N_0}\log e$, which agrees with (21.12) (p. 421).

*Intuition note.* A band of width $B$ gives $B$ complex channel uses per second. Spreading fixed power over ever more uses leaves a limit that depends only on $P/N_0$, and this limit agrees with the continuous-time capacity (21.12).

## Toy example (ours)
Take $N_0=2$, so the noise variance per use is $N_0/2=1$. With power $P$ per use, the rate is $R=\frac12\log_2(1+P)$ bits per use. By the achievability argument, energy per bit is $P/R$. The limit is $N_0/\log_2e=2/1.4427=1.3863$.
- $P=1$: $R=\frac12\log_22=0.5$, so energy/bit $=1/0.5=2$.
- $P=0.1$: $R=\frac12\cdot0.13750=0.06875$, so energy/bit $=0.1/0.06875=1.4545$.
- $P=0.01$: $R=\frac12\cdot0.014355=0.007177$, so energy/bit $=0.01/0.007177=1.3932$.

Energy per bit falls toward 1.3863 as $P\to0$, but the rate per use falls toward 0 (needing ever more slots). This is the spectral-efficiency vs energy trade-off of p. 412.

## Concepts
- [[channel-capacity]] — here, capacity-cost $C(P)$ and its derivative at 0 (p. 414)
- [[fanos-inequality]] — opens the converse of Theorem 21.2 (p. 411); the same inequality (21.10) starts the converse of Theorem 21.4 (p. 415)
- [[data-processing-inequality]] — used for divergence and mutual information in the converses (pp. 411, 415)
- [[relative-entropy-kl-divergence]] — equals the cost-normalized rate: $C_{puc}=\sup D/\mathsf c$ (p. 414)
- [[shannon-hartley-formula]] — the bandlimited result (21.13) (p. 419)
- [[energy-per-bit]] (new) — minimal energy $E^*(k,\epsilon)$ to send $k$ bits; limit $N_0/\log_2e$ (p. 411)
- [[capacity-per-unit-cost]] (new) — $C_{puc}$ of (21.9): $\lim_\epsilon\liminf_E\frac1E\log M^*(E,\epsilon)$, rate per unit cost as cost→∞ (p. 414)
- [[pulse-position-modulation]] (new) — orthogonal code with one spike at position $m$ (p. 413)
- [[flash-signaling]] (new) — energy concentrated in rare very large spikes; required to achieve full $C_{puc}$ under fading (p. 417)
- [[noisy-channel]] — AWGN channel (p. 410) and fading channel (p. 416)

## Canonical instances
- [[awgn-channel]] — $E_b/N_0=-1.59$ dB (pp. 410–412)
- [[rayleigh-fading-noncoherent]] — same $C_{puc}$, spiky codes, slower convergence (pp. 416–417)
- [[ppm-simplex-code]] — PPM achieves the limit; simplex conjectured optimal (p. 413)
- [[continuous-time-awgn]] — capacity $\frac P{N_0}\log e$ (pp. 418–419)
- [[bandlimited-awgn]] — $B\log(1+\frac P{N_0B})$ via Nyquist sampling (pp. 419–421)

## Bridges (candidates)
- [same-math] $C_{puc}=\sup_x D(P_{Y|X=x}\|P_{Y|X=x_0})/\mathsf c(x)$ ↔ hypothesis testing: Stein's exponent $D(P_1\|P_0)$ per sample, as used in the proof (p. 415).
- [metaphor] Minimal energy per bit ↔ physics: Landauer's principle (energy cost of information) — both are energy-per-bit floors; the text only mentions $N_0=kT$ (p. 410).
- [same-math] Discrete-time capacity formula with $n=BT$, $P_d=P/B$ ↔ Shannon–Hartley $C=W\log(1+S/N)$ (p. 421).

## Questions this raises
- Why is the supremum in (21.11) approached only as $x\to\infty$, and what finite-energy codes approach it?
- Which channels have a vanishing-rate capacity-per-unit-cost optimum, and how fast does $C(P)/P$ approach $C_{puc}$ as $P\to 0$?
- Is the simplex code really optimal for fixed $k$ and $\epsilon$?
- How does the rigorous bandlimited result (Ihara; prolate spheroidal functions) differ from the sketch?

## Reading notes
- Printed pages 410–421 = pdf 435–446 (printed = pdf − 25). The metadata calls this unit "ch23", but the printed chapter heading is **21**; I follow the printed numbering.
- Header on each page reads "itbook-export CUP/HE2-design August 16, 2024".
- Misprints spotted: the converse of Thm 21.2 says "double limit in $n\to\infty$" where $k\to\infty$ is meant. In §21.4–21.5, "$n\to\infty$" appears where $T\to\infty$ is meant (proof of Thm 21.5 and (21.13)). §21.5 says "power $p$" for $P$. The demodulation formula is printed as $\sqrt2\,\mathrm{LPF}(Y(t)e^{j\omega_ct})$, with no minus sign in the exponent, and with a stray double comma. $\mathrm{sinc}_B(x)$ is printed as $\sin(Bx)/x$. On p. 413 the final bound is printed as $\limsup_k E^*(k,\epsilon)\le(1+\tau)\frac{N_0}{\log_2 e}$ without the division by $k$.
- In the fading expansion the "3" is a cube-root index, which the text layer garbles.
- §21.5 is explicitly a sketch, not a rigorous theorem. "Straightforward manipulations" at the end of the Thm 21.4 proof are not spelled out.
