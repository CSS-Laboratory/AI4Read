---
id: polyanskiy-2025-information/ch10-random
work: polyanskiy-2025-information
unit: "Chapter 9 (printed numbering; unit id ch10-random): Random number generators, followed by Exercises for Part I"
pages: 166–192
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
# Random number generators (von Neumann, Elias, Peres, Bernoulli factory)

## L0 — One line
From i.i.d. Ber(p) coins with unknown p one can extract exactly fair coin flips at a rate that approaches, but never exceeds, the binary entropy $h(p)$.

## L1 — The gist (≤ 120 words)
How many exactly fair bits can be squeezed from biased coin flips when the bias $p$ is unknown? Von Neumann's pair trick works but has rate only $p\bar p$. The converse, from the data processing inequality, caps every extractor (a map from coin strings to fair bits) at $h(p)$. Two constructions approach this cap with $p$ unknown: Elias's (conditioned on the number of ones, the string is uniform over all strings with that many ones) and Peres's (recycle the discarded bits recursively). The Peres proof relies on exchangeability, and its rate recursion has $h$ as a fixed point. The last section asks which functions $f(p)$ can be simulated from Ber($p$) coins (Bernoulli factory). Pages 174–192 are exercises for Part I.

**Prerequisites:** binary entropy $h$, chain rule and data processing inequality for entropy, law of large numbers, binomial coefficients and Stirling's formula, conditional independence.

## L2 — Key ideas
- Von Neumann's scheme (10→0, 01→1, else skip) gives exactly fair bits for every $p$, since 01 and 10 both have probability $p\bar p$. Its rate is only $p\bar p$, i.e. 25% for fair input (pp. 166–167).
- An extractor must be prefix-consistent (if $x$ is a prefix of $y$, then $\Psi(x)$ is a prefix of $\Psi(y)$) and, for i.i.d. Ber($p$) input and every $p$, output uniform bits conditionally on the output length. Its rate is $\limsup E[\ell(\Psi(X^n))]/n$ (pp. 166–167).
- Converse: every extractor, even one that knows $p$, has rate at most $h(p)$. The proof uses $H(X^n)\ge H(\Psi(X^n))\ge E[L]$, where $L$ is the output length (p. 167).
- Elias: given the Hamming weight (number of ones), $X^n$ is uniform on a type class (all strings with that weight) whatever $p$ is. A uniform variable on $[M]$ converts to fair bits with $E[\text{length}]\in[\log_2 M-4,\log_2 M]$. The rate tends to $h(p)$ (pp. 168–169).
- Peres: iterate von Neumann on the discarded information (the XOR sequence $u$ and the equal-pair sequence $v$). Exchangeability (the distribution does not change when positions are permuted) is preserved, so each stage is a valid extractor (pp. 169–171).
- The Peres rate obeys the recursion $r_t=Tr_{t-1}$, where $T$ is an explicit monotone operator (9.1). $h$ is a fixed point of $T$, shown by a chain-rule identity. The author states, without proof, that $r_t$ converges monotonically from below to the fixed point of $T$, which is $h$ (p. 171).
- Bernoulli factory: the Keane–O'Brien condition limits which $f(p)$ can be simulated at all. Any rational $f$ with $0<f<1$ on $(0,1)$ can be simulated with finite memory, while $\sqrt p$ cannot be simulated by a finite-state machine or block simulation but can be by a pushdown automaton (an FSM with a stack). The optimal rate is unknown (p. 172).

## L3 — Walkthrough

### Chapter introduction (p. 166)
- Toy problem: from i.i.d. Ber($p$) bits with unknown $p$, produce independent Ber(1/2) bits, as many as possible (p. 166).
- Von Neumann (1951): cut the stream into pairs. Output 0 for 10 and 1 for 01. Otherwise output nothing. Both 01 and 10 have probability $p\bar p$ ($\bar p=1-p$), so the output is fair for every $p$ (p. 166).
- Efficiency: $2n$ bits in give on average $2p\bar p n$ bits out, so the rate is $p\bar p$ (p. 166).
- Choices in the problem: universal (source unknown) vs non-universal; exactly vs approximately fair, measured by an f-divergence. This chapter treats only universal, exact generation. In contrast, the author says optimal data compressors in Part II output almost purely random bits, but they are non-universal and approximate (p. 166).
- $\log=\log_2$ throughout (p. 166).

### 9.1 Setup (pp. 166–167)
$\{0,1\}^*=\cup_{k\ge0}\{0,1\}^k$ is the set of finite binary strings, $\emptyset$ is the empty string, and $\ell(x)$ is the length of $x$ (p. 166).

**Definition 9.1 (randomness extractor).** $\Psi:\{0,1\}^*\to\{0,1\}^*$ is an extractor if (p. 166–167):
1. $\Psi(x)$ is a prefix of $\Psi(y)$ whenever $x$ is a prefix of $y$.
2. For any $n$ and any $p\in(0,1)$, if $X^n\overset{\text{i.i.d.}}{\sim}\mathrm{Ber}(p)$, then $\Psi(X^n)\sim\mathrm{Ber}(1/2)^k$ conditioned on $\ell(\Psi(X^n))=k$, for each $k\ge1$.

Rate:
$$r_\Psi(p)=\limsup_{n\to\infty}\frac{E[\ell(\Psi(X^n))]}{n},\quad X^n\overset{\text{i.i.d.}}{\sim}\mathrm{Ber}(p).$$
$\Psi$ consumes $n$ coins of bias $p$ and outputs on average $n\,r_\Psi(p)$ fair coins (p. 167).

Von Neumann's scheme is a valid extractor $\Psi_{vN}$, with $\Psi_{vN}(x^{2n+1})=\Psi_{vN}(x^{2n})$. Its rate is $r_{vN}(p)=p\bar p$. Even for fair input it returns only 25% (p. 167).

### 9.2 Converse (p. 167)
**Theorem 9.2.** No extractor has rate above $h(p)=p\log_2\frac1p+\bar p\log_2\frac1{\bar p}$, even if it may depend on $p$ (the text prints "$\ge$", see Reading notes) (p. 167).

*Proof.* Let $L=\ell(\Psi(X^n))$. Then
$$nh(p)=H(X^n)\ge H(\Psi(X^n))=H(\Psi(X^n)|L)+H(L)\ge H(\Psi(X^n)|L)=E[L]\ \text{bits}.$$
The first inequality is the data processing inequality for the deterministic map $\Psi$. The last equality holds because $\Psi(X^n)$ is uniform on $\{0,1\}^k$ given $L=k$ (p. 167).

*Intuition note.* Each Ber($p$) coin carries $h(p)$ bits of uncertainty, and a deterministic function cannot create uncertainty. So the number of fair bits out, on average, cannot exceed the entropy in. Von Neumann's rate $p\bar p$ stays below $h(p)$ (Fig. 9.1, p. 168).

The author says two extractors, by Elias and Peres, attain $h(p)$. More precisely, each is a sequence of extractors whose rates approach the bound (p. 167).

### 9.3 Elias' construction from data compression (pp. 167–169)
Two observations (pp. 167–168):
1. For i.i.d. $X^n$ the probability of a string depends only on its type (number of ones). So conditioned on the number of ones being $qn$, $X^n$ is uniform on the type class $T_q$. This holds for every actual $p$ (p. 168).
2. A uniform variable on a finite set can be turned into a variable-length string of fair flips. Examples: $U$ uniform on $\{1,2,3\}$ maps $1\mapsto\emptyset,2\mapsto0,3\mapsto1$. $U$ uniform on $\{1,\dots,11\}$ maps $1\mapsto\emptyset,2\mapsto0,3\mapsto1$ and the remaining eight numbers to 3-bit strings (p. 168).

**Lemma 9.3.** For $U$ uniform on $[M]$ there is $f:[M]\to\{0,1\}^*$ such that, conditioned on $\ell(f(U))=k$, $f(U)$ is uniform on $\{0,1\}^k$, and
$$\log_2M-4\le E[\ell(f(U))]\le\log_2M\ \text{bits}.$$

*Proof (p. 168).*
- Construction: write $M=\sum_{i=0}^n m_i2^i$ in binary. Taking the nonzero digits, $M=2^{i_0}+\dots+2^{i_t}$ with distinct powers, giving a partition $[M]=\cup_{j=0}^tM_j$ with $|M_j|=2^{i_j}$. Map the elements of $M_j$ bijectively to $\{0,1\}^{i_j}$. Uniform conditioned on a subset stays uniform.
- Upper bound: $\log_2M=H(U)\ge H(f(U))\ge H(f(U)|\ell(f(U)))=E[\ell(f(U))]$.
- Lower bound:
$$E[\ell(f(U))]=\frac1M\sum_{i=0}^nm_i2^i\cdot i=n-\frac1M\sum_{i=0}^nm_i2^i(n-i)\ge n-\frac{2^n}M\sum_{i=0}^n2^{i-n}(n-i)\ge n-\frac{2^{n+1}}M\ge n-4,$$
using $n\le\log_2M+1$ in the last step. (Added steps: $\sum m_i2^i=M$ in the first equality; $m_i\le1$ in the first inequality; $\sum_{j\ge0}j2^{-j}=2$ in the second. The conclusion $n-4\ge\log_2M-4$ needs $n=\lfloor\log_2M\rfloor+1\ge\log_2M$.)

*Intuition note.* Split the $M$ equally likely outcomes into blocks whose sizes are powers of two. A block of size $2^i$ gives exactly $i$ fair bits. Only a few outcomes lose more than a couple of bits, so on average at most 4 bits are lost.

**Elias' extractor (p. 169).** Fix $n$.
- $w_H(x^n)$ is the Hamming weight (number of ones). $T_k=\{x^n:w_H(x^n)=k\}$ is the Hamming sphere of radius $k$.
- For each $0\le k\le n$ apply $f$ of Lemma 9.3 to $T_k$. This defines $\Psi_E:\{0,1\}^n\to\{0,1\}^*$.
- Extend to $\{0,1\}^*$ by working block by block and discarding the last incomplete block. The rate is $\frac1nE[\ell(\Psi_E(X^n))]$.
- By Lemma 9.3, with $|T_k|=\binom nk$:
$$E\log\binom{n}{w_H(X^n)}-4\le E[\ell(\Psi_E(X^n))]\le E\log\binom{n}{w_H(X^n)}.$$
- By Stirling (Exercise I.1), $\log\binom n{w_H(X^n)}=nh(w_H(X^n)/n)+O(\log n)$.
- By the law of large numbers $w_H(X^n)/n\to p$. Since $h$ is continuous and bounded, the author concludes $\frac1nE[\ell(\Psi_E(X^n))]=h(p)+O(\log n/n)$. So the rate approaches the optimum $h(p)$ as $n\to\infty$ (p. 169).

*Intuition note.* The weight $k$ is a summary that carries all the dependence on $p$. Given $k$, every arrangement of the ones is equally likely, so no knowledge of $p$ is needed. The only loss is the few bits spent on the weight, which is of order $\log n$.

### 9.4 Peres' iterated von Neumann scheme (pp. 169–171)
Idea: recycle what von Neumann discards, namely (a) bits from equal pairs and (b) the locations of the distinct pairs (p. 169).

**Notation (p. 169).** Given $x^{2n}$, let $k=\ell(\Psi_{vN}(x^{2n}))$ be the number of distinct pairs.
- $m_1<\dots<m_k$ are the pair indices with $x_{2m_j}\ne x_{2m_j-1}$.
- $i_1<\dots<i_{n-k}$ are the pair indices with $x_{2i_j}=x_{2i_j-1}$.
- $y_j=x_{2m_j}$ and $v_j=x_{2i_j}$. The vector $u^n$ marks distinct pairs: $u_j$ is the XOR of the two bits of pair $j$ (the text prints $x_{2j}\oplus x_{2j+1}$, see Reading notes).
- $y^k$ is von Neumann's output. $v^{n-k}$ and $u^n$ are discarded, although $u^n$ encodes the locations and "contains a lot of information" (p. 169).

**Peres' extractor (p. 169).** Recursively: $\Psi_1=\Psi_{vN}$, i.e. $\Psi_1(x^{2n+1})=\Psi_1(x^{2n})=y^k$, and
$$\Psi_t(x^{2n})=\Psi_t(x^{2n+1})=\big(\Psi_1(x^{2n}),\Psi_{t-1}(u^n),\Psi_{t-1}(v^{n-k})\big).$$

**Author's example (p. 170).** Input $x=100111010011$ ($2n=12$). The first level splits it as $y=011$, $u=110100$, $v=101$. Applying the same split to $u$ gives $y=1$, $u'=010$, $v'=10$, and the second row also ends with a $(0)$ (the output bit from $v$). The next row shows $(1)(0)$, with the underlined bits being the output bits taken at each level. (I checked the first-level split against the pairs 10, 01, 11, 01, 00, 11.)

To verify validity and compute the rate, the author notes that the bits entering the recursion are no longer i.i.d. The right notion is exchangeability.

**Exchangeability (p. 170).** $X^n$ is exchangeable if $P_{X_1,\dots,X_n}=P_{X_{\pi(1)},\dots,X_{\pi(n)}}$ for every permutation $\pi$ of $[n]$. For binary $X_i$ this holds iff $P_{X^n}(x^n)=f(w_H(x^n))$ for some $f$. Examples: i.i.d. Ber($p$), and uniform on a Hamming sphere $T_k$ (p. 170).

**Worked i.i.d. case (p. 170).** For $X^{2n}$ i.i.d. Ber($p$): $L\sim\mathrm{Binom}(n,2p\bar p)$, and conditioned on $L=k$, $V^{n-k}$ is i.i.d. Ber($p^2/(p^2+\bar p^2)$). With $m=w_H(v)$ the author computes
$$P[Y^k=y,U^n=u,V^{n-k}=v|L=k]=2^{-k}\binom nk^{-1}\Big(\tfrac{p^2}{p^2+\bar p^2}\Big)^m\Big(\tfrac{\bar p^2}{p^2+\bar p^2}\Big)^{n-k-m},$$
which equals $P[Y^k=y|L=k]\,P[U^n=u|L=k]\,P[V^{n-k}=v|L=k]$ (p. 170).

**Lemma 9.4 ($\Psi_t$ preserves exchangeability).** Let $X^{2n}$ be exchangeable and $L=\Psi_1(X^{2n})$. Conditioned on $L=k$, $Y^k$, $U^n$, $V^{n-k}$ are independent, each exchangeable. Moreover $Y^k\overset{\text{i.i.d.}}{\sim}\mathrm{Ber}(1/2)$ and $U^n$ is uniform on $T_k$ (p. 170).

*Proof sketch (p. 170).* It suffices to show that for $y,y'\in\{0,1\}^k$, $u,u'\in T_k$ and $v,v'$ with $w_H(v)=w_H(v')$, the conditional probabilities of $(y,u,v)$ and $(y',u',v')$ agree. The string $X^{2n}$ and the triple $(Y^k,U^n,V^{n-k})$ are in one-to-one correspondence: read the $k$ distinct pairs from $y$, place them where $u$ has ones, and fill the equal pairs from $v$. Examples: $(y,u,v)=(01,1100,01)\Rightarrow x=10010011$, and $(11,1010,10)\Rightarrow 01110100$. The two triples correspond to inputs of equal Hamming weight $k+2w_H(v)$, hence equal probability by exchangeability.

**Lemma 9.5 ($\Psi_t$ is an extractor).** For exchangeable $X^{2n}$, $\Psi_t(X^{2n})\sim\mathrm{Ber}(1/2)^{m}$ conditioned on $\ell(\Psi_t(X^{2n}))=m$ (p. 171).

*Proof (p. 171).* Equivalent: $P[\Psi_t(X^{2n})=s^m]=2^{-m}P[\ell(\Psi_t(X^{2n}))=m]$ for all $s^m$. Induct on $t$. The base $t=1$ is Lemma 9.4 (the $Y$ part). Assume $\Psi_{t-1}$ is an extractor, and write the output length as $L=L_1+L_2+L_3$ with $L_2\perp L_3\mid L_1$ by Lemma 9.4. Then
$$P[\Psi_t=s^m]=\sum_{k=0}^m\sum_{r=0}^{m-k}P[L_1=k]\,2^{-k}\,2^{-r}P[L_2=r|L_1=k]\,2^{-(m-k-r)}P[L_3=m-k-r|L_1=k]=2^{-m}P[L=m].$$
Lemma 9.4 gives the factor $2^{-k}$ and the conditional independence. Lemma 9.4 also makes $U^n$ and $V^{n-k}$ exchangeable, so the induction hypothesis gives $2^{-r}$ and $2^{-(m-k-r)}$.

**Rate for i.i.d. input (p. 171).** Let $X^{2n}$ be i.i.d. Ber($p$).
- By the strong law, $\frac1{2n}\ell(\Psi_1(X^{2n}))=\frac{L_n}{2n}\to p\bar p$ a.s., so $r_1(p)=p\bar p$ (the text writes $pq$).
- Assume $\frac1{2n}\ell(\Psi_{t-1}(X^{2n}))\to r_{t-1}(p)$ a.s. Then
$$\frac1{2n}\ell(\Psi_t(X^{2n}))=\frac{L_n}{2n}+\frac1{2n}\ell(\Psi_{t-1}(U^n))+\frac1{2n}\ell(\Psi_{t-1}(V^{n-L_n})).$$
- Here $U^n\overset{\text{i.i.d.}}{\sim}\mathrm{Ber}(2p\bar p)$, $V^{n-L_n}|L_n\overset{\text{i.i.d.}}{\sim}\mathrm{Ber}(p^2/(p^2+\bar p^2))$ and $L_n\to\infty$ a.s. The induction hypothesis then gives the recursion
$$r_t(p)=p\bar p+\frac12r_{t-1}(2p\bar p)+\frac{p^2+\bar p^2}2\,r_{t-1}\Big(\frac{p^2}{p^2+\bar p^2}\Big)\triangleq(Tr_{t-1})(p).\tag{9.1}$$
- $T$ maps continuous functions on $[0,1]$ to such functions and is monotone ($f\le g$ pointwise implies $Tf\le Tg$). The author states it "can be shown" that $r_t$ converges monotonically from below to the fixed point of $T$, which is exactly $h$.
- Instead of verifying $Th=h$ directly, the author gives this proof. For $X_1,X_2\overset{\text{i.i.d.}}{\sim}\mathrm{Ber}(p)$:
$$2h(p)=H(X_1,X_2)=H(X_1\oplus X_2,X_1)=H(X_1\oplus X_2)+H(X_1|X_1\oplus X_2)=h(2p\bar p)+2p\bar p\,h(\tfrac12)+(p^2+\bar p^2)\,h\Big(\frac{p^2}{p^2+\bar p^2}\Big).$$
- Figure 9.2 shows $r_t$ approaching $h$ for $t=1,4,10$ (p. 172).

*Intuition note.* Given the XOR, the pair order is a fair coin when the pair is distinct, and a biased coin with bias $p^2/(p^2+\bar p^2)$ otherwise. The entropy identity says these leftovers carry exactly the entropy that von Neumann missed. Iterating collects more of it each round.

### 9.5 Bernoulli factory (pp. 172–173)
**Question.** Given Ber($p$) bits with unknown $p$, for which $f:[0,1]\to[0,1]$ can one simulate i.i.d. Ber($f(p)$)? The chapter so far is $f\equiv\frac12$. A famous case is $f(p)=2p\wedge1$ (p. 172).

**Keane–O'Brien (as reported, p. 172).** Every simulable $f$ is a constant or "polynomially bounded away from 0 or 1": for all $0<p<1$, $\min\{f(p),1-f(p)\}\ge\min\{p,1-p\}^n$ for some $n\in\mathbb N$. In particular, doubling the bias is impossible.

**Devices (p. 172, citing [308]).** The rates $r_t$ from (9.1) are rational functions, since $r_1$ is quadratic. For any rational $f$ with $0<f<1$ on $(0,1)$, one can generate independent Ber($f(p)$) from Ber($p$) with finite memory in either of two ways:
1. *Finite-state machine (FSM):* initial state, intermediate states, and final states that output 0 or 1 and reset.
2. *Block simulation:* take disjoint $A_0,A_1\subset\{0,1\}^k$. For each $k$-bit segment output 0 if it falls in $A_0$, 1 if in $A_1$, else discard it. The block size is at most the degree of the denominator polynomial of $f$.

**Table 9.1 (p. 173).** Block-simulation realizations (FSM diagrams are also drawn there):

| Goal | Block simulation |
|---|---|
| $f(p)=1/2$ | $A_0=\{10\}$, $A_1=\{01\}$ |
| $f(p)=2pq$ | $A_0=\{00,11\}$, $A_1=\{01,10\}$ |
| $f(p)=p^3/(p^3+\bar p^3)$ | $A_0=\{000\}$, $A_1=\{111\}$ |

- The text asks as an exercise how to generate $f(p)=1/3$ (p. 172).
- Only rational $f$ can be simulated by FSM or block simulation. For $f(p)=\sqrt p$, which satisfies the Keane–O'Brien characterization, these devices fail, but a pushdown automaton (an FSM with a stack, i.e. infinite memory) can do it (p. 172).
- The optimal Bernoulli factory with the best rate is unknown. A converse is the entropy bound $h(p)/h(f(p))$, which can be trivial (bigger than one) (p. 172).

### Exercises for Part I (pp. 174–192)
These 66 problems close Part I and mostly concern earlier chapters. The author's problem statements, grouped by topic, are:
- **Types and entropy counting (I.1–I.3, p. 174–175):** I.1 asks to show $\frac{e^{nh(p)}}{\sqrt{8k(n-k)/n}}\le\binom nk\le\frac{e^{nh(p)}}{\sqrt{2\pi k(n-k)/n}}$ for $k\in[1,n-1]$ with $p=k/n$, hence $\log|T_p|=nh(p)+O(\log n)$. It also asks for $\log Q^n[T_p]=-nd(p\|q)+O(\log n)$ and general-alphabet versions. This is the Stirling fact used in §9.3. I.2 refines it, and I.3 treats Markov types.
- **Maximum entropy and finiteness (I.4–I.7):** e.g. I.4 asks to prove $H(X)\le E[X]\,h(1/E[X])$ for $\mathbb N$-valued $X$ with finite mean, with the geometric law the unique maximizer. I.7 concerns max entropy under a Hamming-weight constraint (p. 175–176).
- **Gaussians and channels (I.8–I.14):** Gaussian divergence, water-filling, MIMO capacity, conditional capacity, Poisson/exponential mutual information, erasure, information bottleneck (pp. 176–177).
- **Hewitt–Savage and random walks (I.15):** an information-theoretic proof (p. 177).
- **Uniform law on an $\ell_p$-ball (I.16, p. 177):** compute $I(X;Y)$ for $(X,Y)$ uniform on the unit $\ell_p$-ball for $p=1/2,1,\infty$, and find the limit as $p\to0$.
- **Sufficiency, divergence tools, continuity of entropy (I.17–I.25):** I.20 asks to show $|H(P)-H(Q)|\le h(TV(P,Q))+TV(P,Q)\log(|\mathcal X|-1)$ (p. 178). I.23 expresses capacity through covering numbers, $C=\inf_{\epsilon\ge0}(\epsilon^2+\log N(\epsilon))$ (p. 178). I.25 gives other proofs of Fano's inequality (p. 179).
- **Markov chains, graphical models, entropy rates (I.26–I.34, pp. 179–181).**
- **Divergences, f-divergences, Rényi, chain rules (I.35–I.45, pp. 181–184).**
- **Fisher information (I.46–I.47, pp. 184–185).**
- **Mixtures, sampling and de Finetti (I.48–I.52, pp. 185–187).** I.48–I.49: Ingster–Suslina formula and community detection. I.50–I.52: sampling without replacement and an effective de Finetti theorem.
- **Applications (I.53–I.66, pp. 187–192):** wringing lemma, generalization gap, subgaussian bounds, mixtures, combinatorial bounds, Mrs. Gerber's lemma, log-Sobolev inequality, stochastic localization.

## Toy example (ours)
**Peres rate at $p=\tfrac12$.** Here $p\bar p=\tfrac14$, $2p\bar p=\tfrac12$, $p^2+\bar p^2=\tfrac12$, and $p^2/(p^2+\bar p^2)=\tfrac12$. So (9.1) at $p=\tfrac12$ reads
$$r_t(\tfrac12)=\tfrac14+\tfrac12r_{t-1}(\tfrac12)+\tfrac14r_{t-1}(\tfrac12)=\tfrac14+\tfrac34r_{t-1}(\tfrac12).$$
- $r_1=\tfrac14$.
- $r_2=\tfrac14+\tfrac34\cdot\tfrac14=\tfrac14+\tfrac3{16}=\tfrac7{16}$.
- $r_3=\tfrac14+\tfrac34\cdot\tfrac7{16}=\tfrac14+\tfrac{21}{64}=\tfrac{37}{64}$.
- In general $1-r_t=(\tfrac34)^t$ (check: $1-\tfrac14=\tfrac34$; $1-\tfrac7{16}=\tfrac9{16}$; $1-\tfrac{37}{64}=\tfrac{27}{64}$). So $r_t\to1=h(\tfrac12)$.
- Fixed-point check: $r=\tfrac14+\tfrac34r$ gives $r=1$. The entropy identity at $p=\tfrac12$ reads $2=h(\tfrac12)+\tfrac12\cdot1+\tfrac12h(\tfrac12)=1+\tfrac12+\tfrac12$, consistent with $h(\tfrac12)=1$.

**Lemma 9.3 with $M=3$.** $3=2+1$, so $M_0$ has one element (output $\emptyset$) and $M_1$ has two (outputs 0 and 1). Expected length $=\frac13\cdot0+\frac23\cdot1=\frac23$. The bounds are $\log_23-4\approx-2.4\le\frac23\le\log_23\approx1.58$. ✓.

## Concepts
- [[randomness-extractor]] (new) — a map from biased coin strings to bits that are fair conditionally on output length, with prefix consistency (p. 166).
- [[extractor-rate]] (new) — $\limsup E[\ell(\Psi(X^n))]/n$, fair bits out per coin in (p. 167).
- [[entropy]] — here the binary entropy $h(p)$ is the upper limit of any extractor's rate (p. 167).
- [[data-processing-inequality]] — used for the converse, since extractors are deterministic functions (p. 167).
- [[chain-rule]] — used to show $h$ is a fixed point of $T$ (p. 171).
- [[type-class]] (new) — strings with a fixed number of ones; given the weight, an i.i.d. string is uniform on it (p. 168).
- [[exchangeability]] (new) — distribution invariant under permutations; for binary strings, depends only on Hamming weight (p. 170).
- [[universal-coding]] — extractors that work without knowing $p$ are universal. (Canon link; the unit uses the word "universal" only for the source being unknown, p. 166.)
- [[bernoulli-factory]] (new) — simulating Ber($f(p)$) from Ber($p$) with $p$ unknown (p. 172).

## Canonical instances
- [[von-neumann-extractor]] — pair trick, rate $p\bar p$, universal and exact (p. 166).
- [[elias-extractor]] — blockwise uniform-on-Hamming-sphere extraction, rate tends to $h(p)$ (p. 169).
- [[peres-iterated-extractor]] — recursive recycling of $u$ and $v$, rate tends to $h(p)$ from below, as the author states without proof (pp. 169–171).
- [[keane-obrien-condition]] — necessary form of simulable $f$ (p. 172).
- [[table-9-1-factories]] — $1/2$, $2pq$, $p^3/(p^3+\bar p^3)$ via block simulation and FSM (p. 173).

## Bridges (candidates)
- [structural-analogy] Elias' extractor ↔ source coding: uniform-on-a-set to bits mirrors enumerative coding of a type class, although the author says the variable-length encoders are studied in Chapter 10.
- [same-math] Peres' fixed-point identity $2h=h(2p\bar p)+\dots$ ↔ chain rule of entropy: the identity is derived by applying the chain rule (p. 171).
- [structural-analogy] Exchangeability here ↔ de Finetti (Ex. I.52, p. 186): exchangeable laws are approximated by mixtures of i.i.d. laws.
- [metaphor] Converse $E[L]\le nh(p)$ ↔ conservation of randomness: entropy cannot be created by deterministic processing.

## Questions this raises
- Can the rate of an extractor be made to reach exactly $h(p)$ at finite block length, and how fast does $r_t\to h$ as $t$ grows?
- What is the best rate for simulating $\mathrm{Ber}(f(p))$ for a given rational $f$ (the author says unknown)?
- What changes if outputs are only approximately fair (measured in total variation or KL) rather than exactly fair?
- Why does exchangeability suffice for the induction, and are there other classes closed under the von Neumann split?

## Exercises worth doing
- Ex. (Bernoulli factory, p. 172) — build an FSM or block simulation for $f(p)=1/3$ — difficulty: medium
- Ex. I.1 (p. 174) — type-class size bounds and $\log Q^n[T_p]=-nd(p\|q)+O(\log n)$; the Stirling fact behind Elias' rate — difficulty: medium
- Ex. I.4 (p. 175) — maximum entropy for $\mathbb N$-valued $X$, with the geometric law as the unique maximizer — difficulty: medium
- Ex. I.20 (p. 178) — quantitative continuity of entropy via Fano and total variation — difficulty: hard
- Ex. I.50 (p. 186) — sampling without replacement vs with replacement, with the $\sqrt n$ threshold — difficulty: medium
- Ex. I.15 (p. 177) — Hewitt–Savage 0-1 law via mutual information — difficulty: hard

## Reading notes
- Printed page = pdf − 25 (pdf 191 = printed 166). Chapter heading prints "9"; the unit id says ch10. The chapter ends at printed p. 173; pp. 174–192 are "Exercises for Part I". Pages carry a "itbook-export … August 16, 2024" proof header.
- Theorem 9.2 is printed with "$r_\Psi(p)\ge h(p)$". The surrounding text and proof show the intended direction is "$\le$". The proof also writes "$L=\Psi(X^n)$", where $L=\ell(\Psi(X^n))$ is meant.
- Lemma 9.3 proof: it defines $M=\sum_{i=0}^nm_i2^i$ with $m_n=1$ but also $n=\lfloor\log_2M\rfloor+1$. These two are off by one (the top index would be $\lfloor\log_2M\rfloor$). The proof's last displayed line ends at $n-4$ and uses $n\le\log_2M+1$; the passage from $n-4$ to $\log_2M-4$ is not written out and needs the second definition.
- §9.4: $u_j$ is printed as $x_{2j}\oplus x_{2j+1}$. The author's example (the XOR of each pair) matches $x_{2j-1}\oplus x_{2j}$. In the displayed i.i.d. computation the image prints $\bar p^{\,n-k-2m}$ in the numerator. Dividing by the printed denominator, the next line is consistent only with $\bar p^{\,2n-k-2m}$.
- §9.4: $r_1(p)=pq$ is printed; $q=\bar p$ is meant. Table 9.1 also uses $q$ for $\bar p$.
- In Elias' extractor the stated $O(\log n/n)$ error is the author's statement; the text derives it only from Stirling, LLN and continuity of $h$.
- Peres: the text states without proof that $r_t$ converges monotonically to the fixed point of $T$. Only "$h$ is a fixed point" is proved.
- The FSM diagrams in Table 9.1 were not transcribed in detail.
