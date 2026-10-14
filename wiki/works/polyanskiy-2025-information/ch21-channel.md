---
id: polyanskiy-2025-information/ch21-channel
work: polyanskiy-2025-information
unit: "Chapter 19 — Channel capacity (the unit id says ch21; the printed chapter number is 19)"
pages: 370-393
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Channel capacity

## L0 — One line
For a stationary memoryless channel, the largest reliably achievable rate (Shannon capacity) equals the maximum single-letter mutual information $\sup_{P_X} I(X;Y)$, and, for a stationary memoryless source and channel, compressing and then channel coding separately loses nothing at leading order (separation theorem).

## L1 — The gist (≤ 120 words)
How many bits per channel use can be sent with vanishing error over a noisy channel used many times? The chapter defines a channel as a sequence of kernels and defines operational capacity $C$. It proves $C\le C^{(I)}$ by the weak converse and $C\ge\sup_{P_X}I(X;Y)$ by random coding with the law of large numbers. For stationary memoryless channels these coincide, because the information capacity tensorizes (it splits into one-letter problems). It also gives capacities of the BSC, BEC and Z-channel, symmetry classes, information stability, bit-error-rate converses, and the separation theorem: vanishing error is possible for a source if $RH<C$ and not if $RH>C$ ($R$ = source symbols per channel use, $H$ = entropy). This justifies "bits as universal currency".

**Prerequisites:** mutual information and information density; Fano's inequality and the data processing inequality; the weak converse and Shannon's random-coding bound (Chs. 17–18); law of large numbers, CLT, Chebyshev.

## L2 — Key ideas
- A "channel" is a sequence of Markov kernels indexed by blocklength $n$; restrictions such as memoryless, stationary, additive-noise and discrete describe the cases of interest (p. 371–372).
- Capacity is defined operationally as a large-$n$ limit of $\frac1n\log M^*(n,\epsilon)$. The average-error and maximal-error capacities $C$ agree, by expurgation (deleting the worst codewords); the same holds for $C_\epsilon$ where $C_\epsilon=C_{\epsilon-}$ (p. 373–375).
- Theorem 19.9: for stationary memoryless channels $C=C^{(I)}=\sup_{P_X}I(X;Y)$. The converse uses the weak converse; achievability uses random coding plus the law of large numbers (LLN); single-letterization (tensorization) reduces the $n$-letter optimization to $n=1$ (p. 375–377).
- A refinement with the central limit theorem (CLT) gives, for a capacity-achieving input with finite variance $V$ of the information density, $\log M^*\ge nC-\sqrt{nV}Q^{-1}(\epsilon)+o(\sqrt n)$, so under these conditions the gap to capacity is $O(1/\sqrt n)$ (p. 378–379).
- Capacities of three binary channels: binary symmetric (BSC) $\log2-h(\delta)$, binary erasure (BEC) $1-\delta$ bits, Z-channel $h(p^*(1-\delta))-p^*h(\delta)$. Group-noise channels give $\log|G|-H(Z)$ (p. 379–381).
- Several symmetry classes of channels (input/output-symmetric, group-noise, Dobrushin, Gallager, weakly input-symmetric), defined by permutation or group structure, are related by implications, and explicit counterexamples show that some converse implications fail (p. 383–385).
- Information stability ($\frac1n i(X^n;Y^n)\to C^{(I)}$ in probability) is enough for $C=C^{(I)}$. For memoryless channels it holds under conditions (19.25)–(19.26) on the mean and variance of the information density (automatically for finite alphabets). For jointly Gaussian pairs the variance is bounded, which the author says justifies information stability of Gaussian channels (details later) (p. 386–389).
- For memoryless channels, demanding only a vanishing bit error rate (average fraction of wrong message bits) does not raise capacity (p. 389–391).
- Separation theorem: for a stationary memoryless finite-alphabet source and a stationary memoryless channel, vanishing error is possible if $R<C/H$ and not if $R>C/H$ (p. 392–393).

## L3 — Walkthrough

### 19.1 Channels and channel capacity (p. 370–375)
**Definition 19.1.** For an input alphabet $\mathcal A$ and output alphabet $\mathcal B$, a *channel* is a sequence of Markov kernels $P_{Y^n|X^n}:\mathcal A^n\to\mathcal B^n$, $n=1,2,\dots$. The input length $n$ is the *blocklength* (p. 371). Informally one often calls a single kernel "the channel". The index $t$ in $X_t$ usually means time. It can also mean space, as in storage, where noise may depend on past and future symbols (p. 371).

Restrictions (p. 371–372):
- *Non-anticipatory:* the first $k$ outputs depend only on the first $k$ inputs, with kernel $P_{Y^k|X^k}$. Outputs depend causally on inputs.
- *Discrete:* $\mathcal A,\mathcal B$ finite.
- *Additive-noise:* $\mathcal A=\mathcal B$ an abelian group and $Y^n=X^n+Z^n$ with $Z^n\perp X^n$, so $P_{Y^n|X^n}(y^n|x^n)=P_{Z^n}(y^n-x^n)$.
- *Memoryless:* $P_{Y^n|X^n}=\prod_{k=1}^n P_{Y_k|X_k}$ (19.1).
- *Stationary memoryless:* the factors do not depend on $k$: $P_{Y^n|X^n}=(P_{Y|X})^{\otimes n}$ (19.2). In the discrete case $P_{Y^n|X^n}(y^n|x^n)=\prod_k P_{Y|X}(y_k|x_k)$ (19.3). Each coordinate is corrupted independently with the same noise statistics.
- *DMC* (discrete memoryless stationary channel): discrete and stationary memoryless. It is given by a row-stochastic $|\mathcal A|\times|\mathcal B|$ matrix or by a weighted bipartite graph. Table 19.1 lists BSC$_\delta$, BEC$_\delta$ and the Z-channel (p. 372).
- The AWGN channel ($\mathcal A=\mathcal B=\mathbb R$, $Y^n=X^n+Z^n$, $Z^n\sim\mathcal N(0,\sigma^2I_n)$) is non-discrete, stationary memoryless and additive-noise (p. 372).

**Definition 19.2.** An $(n,M,\epsilon)$-code is an $(M,\epsilon)$-code for $P_{Y^n|X^n}$: an encoder $f:[M]\to\mathcal A^n$ and a decoder $g:\mathcal B^n\to[M]\cup\{e\}$. An $(n,M,\epsilon)_{\max}$-code is the same with maximal error probability. The non-asymptotic limits are
$$M^*(n,\epsilon)=\max\{M:\exists(n,M,\epsilon)\text{-code}\},\qquad \epsilon^*(n,M)=\inf\{\epsilon:\exists(n,M,\epsilon)\text{-code}\}\tag{19.4–19.5}$$
and $M^*_{\max},\epsilon^*_{\max}$ analogously (p. 373). The *rate* is $R=\frac{\log_2M}{n}$, in bits per channel use (p. 373).

**Definition 19.3.** $C_\epsilon\triangleq\liminf_{n\to\infty}\frac1n\log M^*(n,\epsilon)$ (the $\epsilon$-capacity) and $C=\lim_{\epsilon\to0^+}C_\epsilon$ (Shannon capacity) (p. 373). Operationally, for any $R<C$ there are $(n,\exp(nR),\epsilon_n)$-codes with $\epsilon_n\to0$ (p. 373). Capacity is a large-$n$ limit, not a supremum over $n$, because the goal is sending large amounts of data (p. 374).

**Zero-error capacity** $C_0\triangleq\liminf_n\frac1n\log M^*(n,0)$ (19.6) is a separate subfield and is often a hard combinatorial problem. For the BSC and BEC, $\log M^*(n,0)=0$ for all $n$, so $C_0=0$. Some channels have $C_0>0$ (p. 374). Generally $C_\epsilon$ may jump at $\epsilon=0$ and increase in $\epsilon$. Typically $C_\epsilon$ is constant on $0<\epsilon<1$ and equals $C$; then the *strong converse* holds (p. 374).

**Theorem 19.4.** For all $\tau\in(0,1)$: $\tau M^*(n,\epsilon(1-\tau))\le M^*_{\max}(n,\epsilon)\le M^*(n,\epsilon)$.
*Proof.* The second inequality holds because maximal error $\le\epsilon$ implies average error $\le\epsilon$. For the first, take an $(n,M,\epsilon(1-\tau))$-code and let $\lambda_j=\mathbb P[\hat W\ne j|W=j]$. Then $M(1-\tau)\epsilon\ge\sum_j\lambda_j\ge\epsilon\,|\{j:\lambda_j>\epsilon\}|$ (Markov's inequality). So at most $(1-\tau)M$ codewords have $\lambda_j>\epsilon$. Removing them (*expurgation*) leaves an $(n,\tau M,\epsilon)_{\max}$-code. Take $M=M^*(n,\epsilon(1-\tau))$ (p. 374–375).

**Corollary 19.5.** $C_\epsilon^{(\max)}=C_\epsilon$ for all $\epsilon>0$ with $C_\epsilon=C_{\epsilon-}$. In particular $C^{(\max)}=C$. *Proof:* from Theorem 19.4, $C_\epsilon\ge C^{(\max)}_\epsilon\ge\liminf\frac1n\log\tau M^*(n,\epsilon(1-\tau))\ge C_{\epsilon(1-\tau)}$. Let $\tau\to0$ (p. 375).

*Intuition note.* Throwing away the worst codewords costs only a constant factor $\tau$ in code size, which vanishes after $\frac1n\log$. So average and maximal error give the same capacity $C$ (and the same $C_\epsilon$ where $C_\epsilon=C_{\epsilon-}$).

### 19.2 Shannon's noisy channel coding theorem (p. 375–379)
**Definition 19.6.** Information capacity: $C^{(I)}=\liminf_{n}\frac1n\sup_{P_{X^n}}I(X^n;Y^n)$. It has no direct operational meaning from first principles (p. 375).

**Theorem 19.7 (converse).** For any channel and $\epsilon\in[0,1)$: $C_\epsilon\le\frac{C^{(I)}}{1-\epsilon}$, and $C\le C^{(I)}$.
*Proof.* The weak converse (Thm 17.3) gives $\log M^*(n,\epsilon)\le\frac{\sup_{P_{X^n}}I(X^n;Y^n)+h(\epsilon)}{1-\epsilon}$. Divide by $n$ and take $\liminf$ (p. 375–376).

**Theorem 19.8 (achievability).** For a stationary memoryless channel, $C_\epsilon\ge\sup_{P_X}I(X;Y)$ for any $\epsilon\in(0,1]$.
*Proof.* Fix $P_X$ and let $P_{X^n}=P_X^{\otimes n}$. Shannon's bound (Thm 18.5) gives, for any $n,M,\tau>0$, an $(n,M,\epsilon_n)$-code with
$$\epsilon_n\le\mathbb P[i(X^n;Y^n)\le\log M+\tau]+\exp(-\tau).$$
Under $P_{X^n,Y^n}=P_{X,Y}^{\otimes n}$ the information density is $i(X^n;Y^n)=\sum_{k=1}^n\log\frac{dP_{X,Y}}{dP_XP_Y}(X_k,Y_k)=\sum_k i(X_k;Y_k)$. This is a sum of iid terms with mean $I(X;Y)$. By the weak LLN, $\mathbb P[i(X^n;Y^n)<n(I(X;Y)-\delta)]\to0$. Set $\log M=n(I(X;Y)-2\delta)$ and $\tau=\delta n$:
$$\epsilon_n\le\mathbb P\Big[\sum_{k=1}^n i(X_k;Y_k)\le nI(X;Y)-\delta n\Big]+\exp(-\delta n)\to0.\tag{19.7}$$
So for all $n$ with $\epsilon_n\le\epsilon$, $\log M^*(n,\epsilon)\ge n(I(X;Y)-2\delta)$, hence $C_\epsilon\ge I(X;Y)-2\delta$. This holds for all $P_X$ and $\delta$ (p. 376).

**Theorem 19.9 (Shannon's channel coding theorem).** For a stationary memoryless channel,
$$C=C^{(I)}=\sup_{P_X}I(X;Y).\tag{19.8}$$
The first equality follows from Theorems 19.7 and 19.8 once the second is shown. The second follows from Proposition 19.10. The author notes that the surprise was $C>0$: reliable communication at positive rate is possible, by coding jointly over many bits, unlike pre-1948 letter-by-letter methods such as Morse code (p. 377).

**Proposition 19.10 (tensorization).** (i) For memoryless channels, $\sup_{P_{X^n}}I(X^n;Y^n)=\sum_{i=1}^n\sup_{P_{X_i}}I(X_i;Y_i)$. (ii) For stationary memoryless channels, $C^{(I)}=\sup_{P_X}I(X;Y)$.
*Proof.* By Thm 6.1, for product kernels $I(X^n;Y^n)\le\sum_kI(X_k;Y_k)$, with equality when the $X_i$ are independent. So only the $n=1$ problem must be solved ("single-letterization") (p. 377).

*Intuition note.* Independent inputs use each channel use separately and lose nothing, so $n$ uses give exactly $n$ times the one-use maximum. Joint coding over many uses is still what makes this rate reliably reachable.

**Price of reaching capacity (p. 378).**
1. *Complexity.* Forney showed linear-time encoders and decoders with exponentially small error probability. If polynomially small error such as $O(n^{-100})$ is acceptable: below capacity, optimal codes have exponentially decaying error. Split the block into pieces of length $c\log n$, each with error $n^{-101}$. By the union bound the whole block errs with probability at most $n^{-100}$. Encoding and exhaustive-search decoding are polynomial time.
2. *Speed.* Shannon's theorem gives gap $C-\frac1n\log M^*(n,\epsilon)=o(1)$. Theorem 19.11 gives $O(1/\sqrt n)$ under conditions.

**Theorem 19.11.** Take a stationary memoryless channel with a capacity-achieving input $P_X^*$, so $C=\max_{P_X}I(X;Y)=I(X_*;Y_*)$. Assume $V=\mathrm{Var}[i(X_*;Y_*)]<\infty$. Then
$$\log M^*(n,\epsilon)\ge nC-\sqrt{nV}\,Q^{-1}(\epsilon)+o(\sqrt n),$$
where $Q$ is the complementary Gaussian CDF.
*Proof.* The goal is $\liminf\frac{\log M^*(n,\epsilon)-nC}{\sqrt{nV}}\ge-Q^{-1}(\epsilon)=\Phi^{-1}(\epsilon)$. Feinstein's bound: there is an $(n,M,\epsilon)_{\max}$-code with $M\ge\beta(\epsilon-\mathbb P[i(X^n;Y^n)\le\log\beta])$. Take $\log\beta=nC+\sqrt{nV}t$. By the CLT the probability tends to $\Phi(t)$, giving, for every $t$ with $\Phi(t)<\epsilon$,
$$\frac{\log M-nC}{\sqrt{nV}}\ge t+\frac{\log(\epsilon-\Phi(t))}{\sqrt{nV}}.$$
Take $\liminf$: it is $\ge t$. Then let $t\nearrow\Phi^{-1}(\epsilon)$ (p. 378–379).

**Remark 19.1.** Examining (19.7), the error for $R<C$ vanishes exponentially (large-deviations event). The optimal exponent is generally open. For fixed $\epsilon$, the optimal coefficient of $\sqrt n$ is called the *channel dispersion* (Sections 22.5–22.6, not in this unit); the author says the bound is often tight (p. 379).

*Intuition note.* For a capacity-achieving input, the LLN says the information density concentrates near $nC$, which gives rates below $C$. The CLT shows its fluctuations are of size $\sqrt{nV}$, so at fixed error $\epsilon$ the achievability bound backs off from $nC$ by about that much.

### 19.3 Examples of capacity computation (p. 379–381)
- **BSC$_\delta$:** $Y=X+Z \bmod 2$, $Z\sim\mathrm{Ber}(\delta)\perp X$. $I(X;X+Z)=H(X+Z)-H(Z)\le\log2-h(\delta)$, with equality iff $X\sim\mathrm{Ber}(1/2)$. So $C=\log2-h(\delta)$ (p. 379).
- **Additive-noise channel over a finite abelian group $G$:** $C=\log|G|-H(Z)$, achieved by $X\sim\mathrm{Unif}(G)$. The same holds for group-noise over a non-abelian group, $x\mapsto x\circ Z$ (p. 380).
- **BEC$_\delta$:** with $X\in\{\pm1\}$, $Y\in\{\pm1,0\}$, $Y=XZ$, $Z\sim\mathrm{Ber}(\delta)\perp X$. Clearly $C\le1-\delta$, since about a $\delta$-fraction of positions is lost. Formally $\mathbb P[X=1|Y=0]=\mathbb P[X=1]$, so an erasure carries no information about $X$ and $H(X|Y=e)=H(X)$. (added step) Then $H(X|Y)=\delta H(X|Y=e)=\delta H(X)$ and $I(X;Y)=(1-\delta)H(X)\le(1-\delta)\log2$, with equality iff $X\sim\mathrm{Ber}(1/2)$. So $C=1-\delta$ bits (p. 380).
- **Z-channel:** $Y=XZ$, $X\in\{0,1\}\perp Z\sim\mathrm{Ber}(1-\delta)$, so $\mathbb P[Z=0]=\delta$. With $X\sim\mathrm{Ber}(p)$: $I(X;Y)=h(p(1-\delta))-p\,h(\delta)$. The optimizer is
$$p^*(\delta)=\frac1{1-\delta}\cdot\frac1{1+\exp\{h(\delta)/(1-\delta)\}},$$
decreasing monotonically from $\tfrac12$ at $\delta=0$ to $\tfrac1e$ as $\delta\to1$. The author remarks that there is infamously no "explanation" of this limit. The capacity is $C=h(p^*(1-\delta))-p^*h(\delta)$ (p. 380–381). Figure 19.1 plots the three capacities (p. 380).

### 19.4* Symmetric channels (p. 381–385)
**Definition 19.12.** A pair of measurable maps $f=(f_i,f_o)$ is a *symmetry* of $P_{Y|X}$ if $P_{Y|X}(f_o^{-1}(E)|f_i(x))=P_{Y|X}(E|x)$ for all measurable $E$ and all $x$. Symmetries compose by $(g_i,g_o)\circ(f_i,f_o)\triangleq(g_i\circ f_i,\,f_o\circ g_o)$ (19.9). A *symmetry group* $G$ is a collection of invertible symmetries closed under this operation. It acts on $\mathcal X\times\mathcal Y$ by $g\cdot(x,y)=(g_i(x),g_o^{-1}(y))$ (19.10), written $(gx,gy)$ (p. 381).

**Definition 19.13.** $G$ is *regular* if it has a left-invariant Haar probability measure $\nu$ for which the action $G\times\mathcal X\times\mathcal Y\to\mathcal X\times\mathcal Y$ is measurable. This is trivial for finite $\mathcal X,\mathcal Y$ (p. 381).

Actions on distributions: $(gP_X)[E]=P_X[g^{-1}E]$ (19.11), and likewise for $Q_Y$ (19.12). The averaged distribution $\bar P_X[E]=\int_GP_X[g^{-1}E]\nu(dg)$ (19.13) is $G$-invariant, $g\bar P_X=\bar P_X$, by left-invariance of $\nu$. Similarly $\bar Q_Y$ (19.14). The key property (19.15): if $X\sim P_X$ and $Y$ is produced by $P_{Y|X}$, then $(gX,gY)$ has marginal $gP_X$ and the same kernel $P_{Y|X}$. For finite alphabets this reads $P_{Y|X}(gy|gx)=P_{Y|X}(y|x)$ (19.16), or equivalently $gP_{Y|X=x}=P_{Y|X=gx}$ (19.17) (p. 382).

The author states that "it is not hard to show" that, for a regular symmetry group, the capacity-achieving output distribution must be $G$-invariant and the capacity-achieving input can be chosen $G$-invariant. So the saddle-point equation $\inf_{P_X}\sup_{Q_Y}D(P_{Y|X}\|Q_Y|P_X)=\sup_{Q_Y}\inf_{P_X}D(P_{Y|X}\|Q_Y|P_X)$ can be solved among $G$-invariant distributions. If $G$ acts transitively on $\mathcal X$ (or $\mathcal Y$), the optimal input (output) can be taken uniform (p. 382–383). The proof is not given here.

**Symmetry notions (p. 383).**
- *Input-/output-symmetric:* a regular $G$ acts transitively on $\mathcal X$ / $\mathcal Y$. A binary-input input-symmetric channel is called BMS.
- *Weakly input-symmetric:* there are $x_0$ and channels $T_x:\mathcal B\to\mathcal B$ with $T_x\circ P_{Y|X=x_0}=P_{Y|X=x}$ and $T_x\circ P_Y^*=P_Y^*$. Randomized $T_x$ is essential, and not all channels are weakly input-symmetric (cited).
- *Group-noise:* $Y=X\circ Z$ with $\mathcal X=\mathcal Y$ a group and $Z\perp X$.
- *Dobrushin-symmetric:* every row of $P_{Y|X}$ is a permutation of the first row and every column is a permutation of the first column.
- *Gallager-symmetric:* $\mathcal Y$ splits into sub-alphabets on each of which the channel is Dobrushin.
- *Square:* $|\mathcal X|=|\mathcal Y|$.

**Relations (p. 383–385).**
- Input- and output-symmetric together $\Rightarrow$ Dobrushin (19.18).
- Group-noise $\Rightarrow$ square, input/output-symmetric (19.19), $\Rightarrow$ Dobrushin, Gallager (19.20).
- Gallager and output-symmetric $\Rightarrow$ Dobrushin.
- Dobrushin and square does **not** imply group-noise. A Latin square that is not a Cayley table, (19.21), scaled by $1/15$, is a counterexample:
$$\begin{pmatrix}1&2&3&4&5\\2&5&4&1&3\\3&1&2&5&4\\4&3&5&2&1\\5&4&1&3&2\end{pmatrix}.$$
- That channel is not input-symmetric. If $g4=1$ on $\mathcal X$, (19.16) with $x=4$ forces $1\mapsto4,2\mapsto3,3\mapsto5,4\mapsto2,5\mapsto1$ on $\mathcal Y$. Then $gP_{Y|X=1}=(5\ 4\ 2\ 1\ 3)/15$, which matches no row, so (19.17) fails at $x=1$. Similarly it is not output-symmetric: if $g2=1$ on $\mathcal Y$, then on $\mathcal X$ it acts $1\mapsto2,2\mapsto5,3\mapsto1,4\mapsto3,5\mapsto4$, and $P_{Y|X}(g1|x)$ is not a column.
- Input-symmetric does not imply Dobrushin (BEC; a square example is (19.22), $\frac1{10}\begin{pmatrix}1&2&3&4\\1&3&2&4\\4&2&3&1\\4&3&2&1\end{pmatrix}$). The same channel shows Gallager and square does not imply Dobrushin.
- Input-symmetric $\Rightarrow$ Gallager $\Rightarrow$ weakly input-symmetric (19.23). The first step: split $\mathcal Y$ into orbits of $G$; each sub-channel is input- and output-symmetric, so (19.18) applies. The second step is called evident.
- Weakly input-symmetric does not imply Gallager. Take $W$ in (19.24), with rows $(1,4,1,1)/7$, $(4,1,0,4)/7$, $(0,0,4,2)/7$, $(2,2,2,0)/7$. Since $\det W\ne0$, the optimal input is unique. $H(Y|X=x)$ does not depend on $x$, and $P_X=[1/4,1/4,3/8,1/8]$ gives uniform $P_Y^*$, so it is the unique optimum. Any permutation fixes the uniform $P_Y^*$, so the channel is weakly input-symmetric. No row is a permutation of another, so it is not Gallager.

Figure 19.2 shows the inclusions (p. 385).

### 19.5* Information stability (p. 386–389)
**Definition 19.14.** A channel is *information stable* if there are input distributions $P_{X^n}$ with $\frac1ni(X^n;Y^n)\xrightarrow{\mathbb P}C^{(I)}$. Stationary memoryless channels are information stable with $P_{X^n}=(P_X^*)^n$ (p. 386).

**Theorem 19.15.** For an information-stable channel, $C=C^{(I)}$. *Proof sketch (author):* the upper bound is the general converse (Thm 17.3); the lower bound follows Thm 19.8 with information stability in place of the WLLN (p. 386).

**Theorem 19.16.** A memoryless channel is information stable if there exist $\{X_k^*\}$ with
$$\frac1n\sum_{k=1}^nI(X_k^*;Y_k^*)\to C^{(I)}\tag{19.25}$$
$$\sum_{n=1}^\infty\frac1{n^2}\mathrm{Var}[i(X_n^*;Y_n^*)]<\infty.\tag{19.26}$$
In particular this holds if $|\mathcal A|<\infty$ or $|\mathcal B|<\infty$ (19.27).
*Proof.* First part: Chebyshev gives $\mathbb P\big[|\frac1n\sum_k i(X_k^*;Y_k^*)-I(X_k^*;Y_k^*)|>\delta\big]\le\frac{\frac1{n^2}\sum_k\mathrm{Var}[i(X_k^*;Y_k^*)]}{\delta^2}\to0$. The convergence follows from Kronecker's lemma with $b_n=n^2$, $x_n=\mathrm{Var}[i(X_n^*;Y_n^*)]/n^2$. Together with (19.25), $\frac1ni\to C^{(I)}$ in probability.
Second part: by memorylessness $C^{(I)}=\liminf\frac1n\sum_k\sup_{P_{X_k}}I(X_k;Y_k)$. Choose $P_{X_k^*}$ with $I(X_k^*;Y_k^*)\ge\sup I(X_k;Y_k)-2^{-k}$ (each sup is $\le\log\min\{|\mathcal A|,|\mathcal B|\}<\infty$). Then $\sum_kI(X_k^*;Y_k^*)\ge\sum_k\sup I(X_k;Y_k)-1$, giving (19.25). For (19.26) one needs
$$\mathrm{Var}[i(X;Y)]\le2\log^2\min(|\mathcal A|,|\mathcal B|)\tag{19.28}$$
for any $P_{X,Y}$. Assume $|\mathcal B|<\infty$. Expanding the square,
$$\mathbb E[i^2]=\int dP_X\sum_yP_{Y|X}\big[\log^2P_{Y|X}+\log^2P_Y-2\log P_{Y|X}\log P_Y\big]\le\int dP_X\sum_yP_{Y|X}\big[\log^2P_{Y|X}+\log^2P_Y\big]\tag{19.29}$$
because $2\log P_{Y|X}\log P_Y\ge0$. Each of the two resulting sums is at most $g(|\mathcal B|)$, where $g(n)\triangleq\sup_{a_j\ge0,\sum a_j=1}\sum_ja_j\log^2a_j$ (19.31). So $\mathbb E[i^2]\le2g(|\mathcal B|)$ (19.30). The solution of (19.31) is interior since $x\log^2x$ has unbounded derivative at 0, and for $n>e$ it is $a_j=1/n$. For $n=2$, $g(2)=0.5629\log^22<\log^22$. In any case $2g(|\mathcal B|)\le2\log^2|\mathcal B|$. The case $|\mathcal A|<\infty$ is symmetric (p. 386–388).

**Lemma 19.17 (Kronecker).** If $0<b_n\nearrow\infty$ and $x_n\ge0$ with $\sum x_n<\infty$, then $\frac1{b_n}\sum_{j\le n}b_jx_j\to0$. *Proof:* split at $m$: $\sum_{k\le n}b_kx_k\le b_m\sum_{k\le m}x_k+\sum_{k=m+1}^nb_kx_k$. Divide by $b_n$ and use $b_k/b_n\le1$ for $k\le n$: the bound is $\frac{b_m}{b_n}\sum_{k\ge1}x_k+\sum_{k>m}x_k$. Let $n\to\infty$, then make the tail small by choosing $m$ large (p. 388).

**Gaussian channels.** For jointly Gaussian $(X,Y)$, $\mathrm{Var}[i(X;Y)]=\rho^2(X,Y)\log^2e\le\log^2e$ (19.32), where $\rho=\mathrm{cov}[X,Y]/\sqrt{\mathrm{Var}X\,\mathrm{Var}Y}$. Write $Y=\tilde X+Z$, $\tilde X=aX\perp Z$. Then $i(\tilde x;y)=\frac{\log e}2\big[\frac{\tilde x^2+2\tilde xz}{\sigma_Y^2}-\frac{\sigma^2}{\sigma_Y^2\sigma_Z^2}z^2\big]$ with $z=y-\tilde x$ (the printed $\sigma^2$ in the numerator is as in the source; presumably $\sigma_{\tilde X}^2$). Use $\mathrm{Var}[\cdot]=\mathrm{Var}[\mathbb E[\cdot|\tilde X]]+\mathbb E\,\mathrm{Var}[\cdot|\tilde X]$ (the source writes $\mathrm{Var}[\cdot|\tilde X]$ for the second term). Then $\mathbb E[i|\tilde X]=\frac{\log e}2\frac{\tilde X^2-\sigma_{\tilde X}^2/\sigma_Z^2}{\sigma_Y^2}$ (as printed), $\mathrm{Var}[\mathbb E[i|\tilde X]]=\frac{2\log^2e}{4\sigma_Y^4}\sigma_{\tilde X}^4$, and $\mathrm{Var}[i|\tilde X]=\frac{2\log^2e}{4\sigma_Y^4}[4\sigma_{\tilde X}^2\sigma_Z^2+2\sigma_{\tilde X}^4]$. Summing gives (19.32). This will justify information stability of Gaussian channels, with or without memory (Sections 20.5*, 20.6*) (p. 388–389).

### 19.6 Capacity under bit error rate (p. 389–391)
For $M=2^k$, identify $W=S^k\in\{0,1\}^k$. The *bit error rate* is $P_b\triangleq\frac1k\sum_{j=1}^k\mathbb P[S_j\ne\hat S_j]=\frac1k\mathbb E[d_H(S^k,\hat S^k)]$ (19.33), the average fraction of wrong bits in a decoded block (p. 389).

**Theorem 19.18.** For $M=2^k$: $P_b\le P_e\le kP_b$. *Proof:* $\frac1k\sum_i\mathbb 1\{S_i\ne\hat S_i\}\le\mathbb 1\{S^k\ne\hat S^k\}\le\sum_i\mathbb 1\{S_i\ne\hat S_i\}$ (the second by the union bound). Take expectations (p. 389).

**Theorem 19.19 (Assouad's lemma).** $P_b\ge\min\{\mathbb P[\hat W=c'|W=c]:d_H(c,c')=1\}$. *Proof:* $\sum_i\mathbb 1\{S_i\ne\hat S_i\}\ge\sum_i\mathbb 1\{S^k=\hat S^k+e_i\}$. Divide by $k$ and take expectations (p. 390).

**Theorem 19.20.** For $A,B\in\{0,1\}^k$ with arbitrary marginals and any $r\ge1$,
$$P_b=\tfrac1k\mathbb E[d_H(A,B)]\ge\binom{k-1}{r-1}P_{r,\min},\quad P_{r,\min}\triangleq\min\{\mathbb P[B=c'|A=c]:d_H(c,c')=r\}.\tag{19.34–19.35}$$
*Proof:* $\mathbb P[d_H(A,B)=r|A=a]=\sum_{b:d_H(a,b)=r}P_{B|A}(b|a)\ge\binom kr P_{r,\min}$, and $d_H(x,y)\ge r\mathbb 1\{d_H(x,y)=r\}$. (added step) Taking expectations gives $\mathbb E\,d_H\ge r\binom krP_{r,\min}$; dividing by $k$ and using $\frac rk\binom kr=\binom{k-1}{r-1}$ gives (19.34) (p. 390). The author notes that Assouad's lemma is used for minimax lower bounds in statistics (Section 31.2, not in this unit).

**Theorem 19.21 (converse under BER).** Any $M$-code with $M=2^k$ and bit error rate $P_b$ satisfies $\log M\le\frac{\sup_{P_X}I(X;Y)}{\log2-h(P_b)}$.
*Proof.* Take $S^k\overset{iid}\sim\mathrm{Ber}(1/2)$, with $S^k\to X\to Y\to\hat S^k$. Using Thm 6.1 for iid $S_i$,
$$\sup_{P_X}I(X;Y)\ge I(X;Y)\ge\sum_iI(S_i;\hat S_i)\ge k\cdot\tfrac1k\sum_id\big(\mathbb P[S_i=\hat S_i]\,\|\,\tfrac12\big)\ge k\,d\Big(\tfrac1k\sum_i\mathbb P[S_i=\hat S_i]\,\Big\|\,\tfrac12\Big)=k\,d(1-P_b\|\tfrac12)=k(\log2-h(P_b)).$$
The second line used Fano's inequality for binary variables (or data processing for divergence); the third used convexity of divergence (p. 391).
Combined with Prop. 19.10, any sequence of codes with $P_b\to0$ over a memoryless channel must have $R<C$. So relaxing $P_e$ to $P_b$ gives no higher rate. The author says this converse is asymptotically achievable for stationary memoryless channels, and that it follows from Theorem 26.5 (not in this unit) (p. 391).

### 19.7 Joint source-channel coding (p. 391–393)
A JSCC code has an encoder $f:\mathcal A^k\to\mathcal X^n$ and a decoder $g:\mathcal Y^n\to\mathcal A^k$, with $S^k\to X^n\to Y^n\to\hat S^k$. The goal is to maximize $R=k/n$ (source symbols per channel use) with small $\epsilon^*_{\rm JSCC}(k,n)=\inf_{f,g}\mathbb P[S^k\ne\hat S^k]$. If $S^k$ is uniform on $\{0,1\}^k$, this is channel coding with $M=2^k$ and $\epsilon^*_{\rm JSCC}(k,n)=\epsilon^*(n,2^k)$ (p. 391–392).

**Theorem 19.22 (Shannon separation theorem).** Let the source be stationary memoryless on a finite alphabet with entropy $H$, and the channel stationary memoryless with finite capacity $C$. Then $\epsilon^*_{\rm JSCC}(nR,n)\to0$ if $R<C/H$, and $\not\to0$ if $R>C/H$, as $n\to\infty$. Interpretation: each source symbol has $H$ bits, each channel use conveys $C$ bits, so transmitting $k$ symbols reliably over $n$ uses needs $kH\le nC$ (p. 392).
*Achievability.* Use the architecture $S^k\to W\to X^n\to Y^n\to\hat W\to\hat S^k$: an optimal compressor $(f_1,g_1)$ and an optimal channel code $(f_2,g_2)$ for maximal error. Let $W$ take at most $M_k$ values. By Cor. 11.3: if $\frac1k\log M_k>H+\delta$ then $\mathbb P[\hat S^k\ne S^k(W)]\le\epsilon$ for $k\ge k_0$. By Thm 19.9: if $\frac1n\log M_k<C-\delta$ then $\mathbb P[\hat W\ne m|W=m]\le\epsilon$ for all $m$ and $k\ge k_0$. Hence $\mathbb P[S^k\ne\hat S^k(\hat W)]\le\mathbb P[S^k\ne\hat S^k,W=\hat W]+\mathbb P[W\ne\hat W]\le\mathbb P[S^k\ne\hat S^k(W)]+\mathbb P[W\ne\hat W]\le2\epsilon$. If $R(H+\delta)<C-\delta$ then $\epsilon^*\to0$ (p. 392–393).
*Converse.* The chain $S^k\to X^n\to Y^n\to\hat S^k$ and data processing give $I(S^k;\hat S^k)\le I(X^n;Y^n)\le nC$. Fano's inequality gives $I(S^k;\hat S^k)=H(S^k)-H(S^k|\hat S^k)\ge kH-\epsilon_n\log|\mathcal A|^k-\log2$. Hence
$$nC\ge kH-\epsilon_n\log|\mathcal A|^k-\log2.\tag{19.36}$$
Divide by $n$, with $R=k/n$, and let $n\to\infty$: $\liminf\epsilon_n\ge\frac{RH-C}{R\log|\mathcal A|}$, which is positive if $R>C/H$ (p. 393).
A remark: instead of Fano, apply data processing for divergence to $(S^k,\hat S^k)\mapsto\mathbb 1\{S^k=\hat S^k\}$ with $Q_{S^k\hat S^k}=U_{S^k}P_{\hat S^k}$. This gives $D(P_{S^k\hat S^k}\|Q)\ge d(1-\epsilon_n\|\mathcal A|^{-k})$, which also yields (19.36); other $f$-divergences could be used (p. 393).

**Theorem 19.23.** For an ergodic finite-alphabet source with entropy rate $H$ and an information-stable channel with capacity $C$, the printed statement is $\lim_n\epsilon^*_{\rm JSCC}(nR,n)=0$ for $R>H/C$ and $>0$ for $R<H/C$. The proof is left as an exercise (see Reading notes) (p. 393).

*Intuition note.* Compress the source to nearly incompressible bits, then protect those bits with a channel code. In the leading-order asymptotics nothing is lost compared with any joint scheme. The feasibility condition is just "bits needed $\le$ bits the channel can carry".

## Toy example (ours)
Take the BEC with $\delta=0.2$ and input $X\sim\mathrm{Ber}(p)$. On p. 380 the chapter bounds $I(X;Y)\le(1-\delta)H(X)$; with our added step above, $I(X;Y)=(1-\delta)H(X)$.
- $p=1/2$: $H(X)=1$ bit, so $I=0.8\times1=0.8$ bit.
- $p=1/4$: $h(1/4)=0.25\cdot2+0.75\log_2(4/3)=0.5+0.75(0.4150)=0.8113$, so $I=0.8\times0.8113=0.649$ bit.

The maximum is at $p=1/2$, so $C=1-\delta=0.8$ bit per use. By Theorem 19.9 (an asymptotic statement), for large $n$ about $nC$ bits can be sent reliably; for $n=100$ that heuristically means about $80$ bits.

Separation: a source with $H=0.5$ bit/symbol has $C/H=0.8/0.5=1.6$ symbols per channel use. Heuristically, for $n=100$ uses, $k<160$ symbols fit, since $kH<80=nC$. Sending $k=200$ symbols needs $kH=100>80$, which violates the necessary condition $kH\lesssim nC$ from (19.36).

## Concepts
- [[noisy channel]] — here a *sequence* of Markov kernels $P_{Y^n|X^n}$ indexed by blocklength, not a single kernel (p. 371)
- [[channel capacity]] — $C=\lim_{\epsilon\to0}\liminf_n\frac1n\log M^*(n,\epsilon)$, an operational quantity (p. 373)
- [[noisy-channel coding theorem]] — $C=C^{(I)}=\sup_{P_X}I(X;Y)$ for stationary memoryless channels (p. 377)
- [[mutual information I(X;Y)]] — the quantity maximized to get capacity; its information density is a sum of iid terms in the proof (p. 376)
- [[source–channel separation]] — vanishing error is possible if $R<C/H$ and not if $R>C/H$ (the boundary $R=C/H$ is left open); achieved by compress-then-code (p. 392)
- [[Fano's inequality]] — used for the BER converse and the separation converse (p. 391, 393)
- [[data processing inequality]] — used for $I(S^k;\hat S^k)\le I(X^n;Y^n)$ (p. 393)
- [[information stability]] (new) — $\frac1ni(X^n;Y^n)\to C^{(I)}$ in probability for some inputs; implies $C=C^{(I)}$ (p. 386)
- [[single-letterization (tensorization)]] (new) — $\sup I(X^n;Y^n)$ reduces to $n$ copies of the one-letter problem for memoryless channels (p. 377)
- [[expurgation]] (new) — deleting bad codewords to turn an average-error code into a maximal-error code (p. 375)
- [[zero-error capacity]] (new) — $C_0=\liminf\frac1n\log M^*(n,0)$ (p. 374)
- [[strong converse]] (new) — $C_\epsilon$ constant for $0<\epsilon<1$ (p. 374)
- [[bit error rate]] (new) — $P_b$, average fraction of wrong bits, $P_b\le P_e\le kP_b$ (p. 389)
- [[channel symmetry classes]] (new) — input/output-, Dobrushin-, Gallager-, weakly input-symmetric, group-noise (p. 383)
- [[channel dispersion]] (new) — the optimal $\sqrt n$-order coefficient; only named here, with Thm 19.11 as one bound (p. 379)

## Canonical instances
- [[BSC]] — capacity $\log2-h(\delta)$ (p. 379)
- [[BEC]] — capacity $1-\delta$ bits, with a clean erasure argument (p. 380)
- [[Z-channel]] — optimal input $p^*(\delta)\to1/e$ as $\delta\to1$ (p. 380)
- [[group-noise channel]] — capacity $\log|G|-H(Z)$ with uniform input (p. 380)
- [[AWGN channel]] — non-discrete, stationary memoryless, additive-noise example (p. 372)
- [[Latin-square channel]] — Dobrushin and square but not group-noise or input/output-symmetric (p. 384)

## Bridges (candidates)
- [structural-analogy] Single-letterization of capacity ↔ Fisher information additivity for iid samples — both reduce an $n$-sample optimum or quantity to $n$ copies of a one-sample one.
- [same-math] Assouad's lemma (Thm 19.19) ↔ statistics: minimax lower bounds — the author states this link (p. 390).
- [structural-analogy] Capacity under a limit on information flow ↔ rational inattention (canon concept) — agents are limited by a channel capacity (canon link; not stated in this unit).
- [metaphor] "Bits as universal currency" (separation theorem) ↔ economics: common unit of exchange — the compressor and channel code interface only through bits (p. 392).

## Questions this raises
- Is the optimal error exponent for $R<C$ known in general, and how does it relate to the dispersion term (p. 379)?
- For which natural channels with memory does information stability fail, and what is $C$ then (p. 386)?
- Is $\frac{RH-C}{R\log|\mathcal A|}$ in the separation converse tight, or does the strong converse make it $1$ (p. 393)?
- How large can $C_0$ be for channels where it is positive (p. 374)?

## Exercises worth doing
The unit prints no exercises. It leaves one proof as an exercise: Theorem 19.23 (p. 393) — adapting the separation proof with Cor. 12.6 and Thm 19.15 — difficulty: medium.

## Reading notes
- Printed pages 370–393 correspond to PDF pages 395–418 (printed = pdf − 25). The chapter title on p. 370 is "19 Channel capacity", although the unit id says ch21.
- Table 19.1 text layer (p. 372): "the binary symmetric channel (BEC)". It should be the binary *erasure* channel; the image shows the same wording as the text layer.
- p. 380, BEC: the image shows $H(X|Y)=H(X|Y=e)$. A factor $\delta$ appears to be missing; I used $H(X|Y)=\delta H(X)$ (marked as an added step).
- Z-channel: Table 19.1 has input 0 flipping to 1 with probability $\delta$. The text on p. 380 has $\mathbb P[Z=0]=\delta$ with $Y=XZ$, so input 1 flips to 0. Both are the same channel up to relabeling.
- Theorem 19.22 achievability ends with "we conclude the weak converse for any $R>C/H$" (p. 393). By context this is the achievability for $R<C/H$.
- Theorem 19.23 as printed (p. 393) says $=0$ for $R>H/C$ and $>0$ for $R<H/C$. This does not match the convention of Theorem 19.22 ($R=k/n$, boundary $C/H$) and is probably a misprint or a different convention for $R$. I report it as printed.
- Gaussian computation (p. 388): in the $i(\tilde x;y)$ formula the image shows $\sigma^2$ in the numerator of the last term. I flagged the likely intended $\sigma_{\tilde X}^2$.
- "Section Section 26.3" is a duplicated word in the source (p. 392). Sections 19.4* and 19.5* carry an asterisk in their headings.
