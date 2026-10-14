---
id: polyanskiy-2025-information/ch12-variable
work: polyanskiy-2025-information
unit: "Variable-length compression (printed as Chapter 10)"
pages: 197-211
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
# Variable-length compression

## L0 — One line
The shortest possible average description of a discrete random variable X is essentially its entropy H(X): for the best unrestricted code f* the mean length lies between H(X) − log₂[e(H(X)+1)] and H(X), and for prefix or uniquely decodable codes (attained by Huffman) it lies between H(X) and H(X)+1.

## L1 — The gist (≤ 120 words)
How short can a lossless bit-string description of a discrete random variable be? The chapter shows that the optimal single-shot code f* just ranks symbols by probability and hands out the shortest strings in order. Its mean length lies between H(X) − log₂[e(H(X)+1)] and H(X). Its length distribution tracks that of log 1/P_X(X), which gives a law of large numbers and a Gaussian approximation for i.i.d. blocks. Prefix and uniquely decodable codes are governed by the Kraft inequality. Their best mean length lies in [H, H+1], and Huffman's algorithm attains it. The chapter also gives Mandelbrot's entropy-based argument for Zipf's power law.

**Prerequisites:** entropy and conditional entropy, chain rule, KL divergence; weak law of large numbers and CLT; convergence in distribution; binary trees; basic convex optimization (Lagrange multipliers).

## L2 — Key ideas
- Optimal single-shot lossless compression sorts the PMF in decreasing order and assigns ∅, 0, 1, 00, 01, … in that order, so $l(f^*(i))=\lfloor\log_2 i\rfloor$. Its length is stochastically smallest (for every k, $\mathbb P[l\le k]$ is at least as large as for any other lossless code), so it is best for the mean, the median and the maximum at once (p. 198–199).
- Source coding bound (Thm 10.3): $H(X)-\log_2[e(H(X)+1)]\le \mathbb E[l(f^*(X))]\le H(X)$. This is the first coding theorem of the book (p. 199).
- The distribution of $l(f^*(X))$ is sandwiched around that of $\log_2 1/P_X(X)$. For i.i.d. blocks this gives $\frac1n l(f^*(S^n))\to H(S)$ in probability and a Gaussian approximation with variance $nV(S)$, where the varentropy is $V(S)=\mathrm{Var}[\log_2 1/P_S(S)]$ (p. 200–202).
- Mandelbrot's argument: power-law distributions maximize entropy for a given mean optimal code length. Maximizing information per unit code length, plus a minimal-entropy requirement, then selects a power law. The author says this does not explain power laws in other domains, where he finds other models such as preferential attachment more plausible (p. 204–206).
- Kraft–McMillan: a uniquely decodable code (its concatenated extension is injective) satisfies the Kraft inequality $\sum 2^{-l_a}\le1$. Any lengths satisfying it are realized by a prefix code (no codeword is a prefix of another), so nothing is lost by restricting to prefix codes (p. 208).
- Best prefix or uniquely decodable code: $H(X)\le L^*(X)\le H(X)+1$ bit. The Huffman algorithm solves this integer program optimally (p. 209–210).
- Huffman's drawbacks are that it needs the source distribution and that block coding costs $|\mathcal A|^n$ complexity. Arithmetic coding and Lempel–Ziv are the announced remedies (p. 210–211).

## L3 — Walkthrough

### Opening (p. 197)
The question is how to describe a discrete random variable X by a variable-length bit string, as short as possible. Likely symbols should get short strings. Shannon's discovery was that compressing groups of symbols together can save a lot, even for i.i.d. symbols. The results here connect an operational problem (code length) with an information measure (entropy), which is why compression is called *source coding* (p. 197).

### 10.1 Variable-length lossless compression
**Setting.** A *single-shot lossless compressor* is a map $f:\mathcal X\to\{0,1\}^*=\cup_{k\ge0}\{0,1\}^k$ (strings of any length, including the empty string ∅). Each $f(x)$ is a *codeword*, and the set of codewords is the *codebook*. Lossless means that some decompressor $g$ has $\mathbb P[X=g(f(X))]=1$, i.e. $f$ is injective on the support of $P_X$ (p. 197–198). Since $\{0,1\}^*$ is countable, this works only for discrete X. We relabel $\mathcal X=\mathbb N$ with $P_X(1)\ge P_X(2)\ge\cdots$. The length function $l$ counts bits: $l(\emptyset)=0$, $l(01001)=5$ (p. 198).

**Definition 10.1 (stochastic dominance).** $X\overset{st.}{\le}Y$ if $\mathbb P[Y\le t]\le\mathbb P[X\le t]$ for all $t$. Then means, medians and suprema are ordered the same way (p. 198).

**Theorem 10.2 (optimal $f^*$).** Define $f^*(1)=\emptyset$, $f^*(2)=0$, $f^*(3)=1$, $f^*(4)=00$, … for the sorted PMF. Then (p. 198–199):
1. $l(f^*(i))=\lfloor\log_2 i\rfloor$.
2. For any lossless $f$, $l(f^*(X))\overset{st.}{\le}l(f(X))$. That is, $\mathbb P[l(f(X))\le k]\le\mathbb P[l(f^*(X))\le k]$ for every $k$, and hence $\mathbb E[l(f^*(X))]\le\mathbb E[l(f(X))]$.

*Proof.* $|A_k|=|\{x:l(f(x))\le k\}|\le\sum_{i=0}^k2^i=2^{k+1}-1=|A_k^*|$, because $f$ is injective. $A_k^*$ holds the $2^{k+1}-1$ most likely symbols, so
$$\mathbb P[l(f(X))\le k]=\sum_{x\in A_k}P_X(x)\le\sum_{x\in A^*_k}P_X(x)=\mathbb P[l(f^*(X))\le k].\tag{10.1}$$

*Intuition note.* Only $2^{k+1}-1$ strings have length ≤ k. The best you can do is give them to the most probable symbols, and this is optimal for every k simultaneously.

**Theorem 10.3.** $H(X)\ \text{bits}-\log_2[e(H(X)+1)]\le\mathbb E[l(f^*(X))]\le H(X)$ bits (p. 199).

*Proof (p. 199–200).* Let $L=l(f^*(X))$.
- Upper bound: sorting gives $P_X(m)\le1/m$, so $L(m)\le\log_2m\le\log_2\frac1{P_X(m)}$. Taking expectations, $\mathbb E[L]\le H(X)$.
- Lower bound: $H(X)=H(X,L)=H(X|L)+H(L)\le\mathbb E[L]+H(L)$ (a). Here $L$ is a function of $X$, and given $L=k$, X takes at most $2^k$ values, so $H(X|L=k)\le k$ bits. Then
$$\le\mathbb E[L]+h\!\left(\tfrac1{1+\mathbb E[L]}\right)(1+\mathbb E[L])\quad\text{(b, Exercise I.4)}$$
$$=\mathbb E[L]+\log_2(1+\mathbb E[L])+\mathbb E[L]\log_2\!\Big(1+\tfrac1{\mathbb E[L]}\Big)\tag{10.2}$$
$$\le\mathbb E[L]+\log_2(1+\mathbb E[L])+\log_2e\quad\text{(c: }x\log(1+1/x)\le\log e)$$
$$\le\mathbb E[L]+\log_2(e(1+H(X)))\quad\text{(d)}.$$
Step (d) uses the bound just shown. The page prints it as "H(X) ≤ E[L]", but the direction needed is $\mathbb E[L]\le H(X)$ (see Reading notes).

*Intuition note.* Mean length is at most H and cannot fall below H by more than a logarithmic term. The length of f* never exceeds $\log_2 1/P$ for any symbol, and on average it cannot be much smaller.

**Blocks.** For a memoryless source $S_j\overset{i.i.d.}\sim P_S$, take $X=S^n$: $nH(S)\ge\mathbb E[l(f^*(S^n))]\ge nH(S)-\log_2n+O(1)$ (p. 200). The exact behaviour is quoted from [408]: $nH(S)+O(1)$ if $P_S$ is uniform, and $nH(S)-\frac12\log_2n+O(1)$ otherwise. If $\log_2\frac1{P_S}$ has a non-lattice distribution,
$$\mathbb E[l(f^*(S^n))]=nH(S)-\tfrac12\log_2(8\pi eV(S)n)+o(1),\tag{10.3}$$
with the *varentropy* $V(S)\triangleq\mathrm{Var}\big[\log_2\frac1{P_S(S)}\big]$ (10.4) (p. 200).

**Theorem 10.4 (code length distribution).** For all $\tau>0$, $k\ge0$ (p. 200):
$$\mathbb P\Big[\log_2\tfrac1{P_X(X)}\le k\Big]\le\mathbb P[l(f^*(X))\le k]\le\mathbb P\Big[\log_2\tfrac1{P_X(X)}\le k+\tau\Big]+2^{-\tau+1}.$$
*Proof.* Lower bound (achievability): $L\le\log_2\frac1{P_X(X)}$ almost surely, as in Thm 10.3. Upper bound (converse): split on whether $\log_2\frac1{P_X}\le k+\tau$. On the other event, $P_X(x)\le2^{-k-\tau}$ and $l(f^*(x))\le k$ hold at once. At most $2^{k+1}-1$ symbols have $l(f^*(x))\le k$, so that event has probability at most $(2^{k+1}-1)2^{-k-\tau}$, which is $\le2^{-\tau+1}$ (added step) (p. 200–201).

**Remark 10.2.** Positive results ("length is smaller than …") are called *achievability*. Negative results ("cannot be smaller than …") are called *converse* (p. 201).

**Corollary 10.5.** For a random process $(S_1,S_2,\dots)$ and real random variables $U,V$ (p. 201):
$$\tfrac1n\log_2\tfrac1{P_{S^n}(S^n)}\xrightarrow{d}U\iff\tfrac1nl(f^*(S^n))\xrightarrow{d}U\tag{10.5}$$
$$\tfrac1{\sqrt n}\Big(\log_2\tfrac1{P_{S^n}(S^n)}-H(S^n)\Big)\xrightarrow{d}V\iff\tfrac1{\sqrt n}\big(l(f^*(S^n))-H(S^n)\big)\xrightarrow{d}V\tag{10.6}$$
*Proof.* Convergence in distribution means CDFs converge at continuity points. For (10.5), apply Thm 10.4 with $k=un$, $\tau=\sqrt n$, which gives a sandwich with $u+1/\sqrt n$ and error $2^{-\sqrt n+1}$. For (10.6), use $k=H(S^n)+\sqrt n\,u$ and $\tau=n^{1/4}$, which gives $u+n^{-1/4}$ and error $2^{-n^{1/4}+1}$ (10.7) (p. 201).

**Memoryless case (p. 202).** Here $\log\frac1{P_{S^n}(S^n)}=\sum_i\log\frac1{P_S(S_i)}$ is an i.i.d. sum.
1. By the WLLN, the limit U in (10.5) is the constant $H(S)$, so $\frac1nl(f^*(S^n))\xrightarrow{\mathbb P}H(S)$. This is a version of Shannon's source coding theorem.
2. By the CLT, if $V(S)<\infty$, $\frac1{\sqrt{nV(S)}}(l(f^*(S^n))-nH(S))\xrightarrow{d}\mathcal N(0,1)$. In shorthand, $l(f^*(S^n))\approx nH(S)+\sqrt{nV(S)}\,\mathcal N(0,1)$. This gives the speed of convergence and the finite-n distribution.

**Example 10.1 (ternary source).** $P_S=[0.445,0.445,0.11]$ (p. 202).

| n | Lower bound | $\mathbb E[l(f^*(S^n))]$ | $H(S^n)$ (upper) | asymptotics (10.3) |
|---|---|---|---|---|
| 20 | 21.5 | 24.3 | 27.8 | 23.3 + o(1) |
| 100 | 130.4 | 134.4 | 139.0 | 133.3 + o(1) |
| 500 | 684.1 | 689.2 | 695.0 | 688.1 + o(1) |

The expected length is close to the midpoint between the bounds. For the distribution of the length, the plain Gaussian approximation is $nH(S)+\sqrt{nV(S)}Z$ (10.8). The mean-adjusted one is $nH(S)-\frac12\log_2(8\pi eV(S)n)+\sqrt{nV(S)}Z$ (10.9). Figure 10.2 compares them with the true CDF and PMF for n = 200 (p. 203).

### 10.2 Mandelbrot's argument for Zipf's law
**Zipf's law.** Sort word frequencies $p_1\ge p_2\ge\cdots$. Then $p_r\asymp r^{-\alpha}$, with $\alpha\approx1$ across several languages (Fig. 10.3). Many other tables are said to be power laws too (city sizes, earthquakes, incomes, …) (p. 203).

**Extremality.** Define $\mathcal H(\Lambda)=\sup_{f,P_X}\{H(X):\mathbb E[l(f(X))]\le\Lambda\}$. Thm 10.3 (via (10.2)) gives
$$\Lambda\log2\le\mathcal H(\Lambda)\le\Lambda\log2+(1+\Lambda)\log(1+\Lambda)-\Lambda\log\Lambda.$$
The author states that the upper bound is tight and is attained at power laws (p. 204). Derivation (p. 205):
- It suffices to take sorted PMFs (class $\mathcal P^\downarrow$), with $l(f(j))=\lfloor\log_2j\rfloor$ by Thm 10.2. So $\mathcal H(\Lambda)=\sup_{P\in\mathcal P^\downarrow}\{H(P):\sum_jp_j\lfloor\log_2j\rfloor\le\Lambda\}$ (p. 204).
- Using logs base 2 and Example 5.2 (not part of this unit), $\mathcal H(\Lambda)\le\inf_{\lambda>0}\lambda\Lambda+\log_2Z(\lambda)$ (10.10). Here $Z(\lambda)=\sum_{n\ge1}2^{-\lambda\lfloor\log_2n\rfloor}=\sum_{m\ge0}2^{(1-\lambda)m}=\frac1{1-2^{1-\lambda}}$ for $\lambda>1$, and $Z=\infty$ otherwise.
- The infimum is a minimum at $\lambda^*>1$ with $\Lambda=-\frac d{d\lambda}\log_2Z(\lambda)|_{\lambda^*}$.
- Define $P_\lambda(n)=\frac1{Z(\lambda)}2^{-\lambda\lfloor\log_2n\rfloor}$. Then $\mathbb E_{P_\lambda}[\lfloor\log_2X\rfloor]=-\frac d{d\lambda}\log_2Z=\frac{2^{1-\lambda}}{1-2^{1-\lambda}}$ and $H(P_\lambda)=\log_2Z(\lambda)+\lambda\,\mathbb E_{P_\lambda}[\lfloor\log_2X\rfloor]$.
- So (10.10) is tight, attained by $P_{\lambda^*}$, with $\lambda^*=\log_2\frac{2+2\Lambda}\Lambda$. This yields $\mathcal H(\Lambda)=\Lambda\log2+(\Lambda+1)\log(\Lambda+1)-\Lambda\log\Lambda$. The extremal law $P_{\lambda^*}(n)\asymp n^{-\lambda^*}$ is a power law with $\lambda^*\to1$ as $\Lambda\to\infty$.

*Intuition note.* Among all distributions with a given mean optimal code length, the one with the most entropy is a power law. This is a property of the optimization, not yet an explanation of why real data look this way.

**Mandelbrot's argument (as reported by the author, p. 205–206).** Assume a countable set of concepts, roughly in one-to-one correspondence with words. In the simplest case, each concept x is stored in the brain as a bit pattern of length $l(f(x))$ ([291] considers more general ones). The number of concept sequences with composition P grows exponentially with exponent $H(P)$ (Prop. 1.5). So the long-run information rate is $\frac{H(P)}{\mathbb E_P[l(f(X))]}$. Mandelbrot concludes that language and brain representation co-evolve to maximize this ratio. Note $\sup_{P,f}\frac{H(P)}{\mathbb E_P[l(f(X))]}=\sup_\Lambda\frac{\mathcal H(\Lambda)}\Lambda$. The author notes this is infinite, because $\mathcal H$ is concave and the supremum is at $\Lambda=0^+$ (the author says it is "not hard to show"). He adds that Mandelbrot appears not to have observed this. The fix is to postulate, for an unknown physiological reason, a minimal entropy $H(P)\ge h_0$. Then $\sup_{P,f:H(P)\ge h_0}\frac{H(P)}{\mathbb E_P[l(f(X))]}=\frac{h_0}{\mathcal H^{-1}(h_0)}$, achieved at a power law. The implied conclusion is that word frequencies evolve until a power law is attained. The author says this does not explain power laws in other domains, where preferential attachment models are more plausible. Also, $P_\lambda$ takes values $2^{-\lambda m-\log_2Z(\lambda)}$ with multiplicity $2^m$, which gives a staircase on frequency–rank plots. Non-binary representations with unequal signal lengths could alleviate this (p. 206).

### 10.3 Uniquely decodable codes, prefix codes and Huffman codes
This section studies codes with good algorithmic properties: low-complexity decoding and short delay on a bit stream (p. 206). $\mathcal A^+=\cup_{n\ge1}\mathcal A^n$ is the set of non-empty strings, and $\mathcal A$ is countable.
- **Def. 10.6.** The *extension* of $f$ is $f(a_1,\dots,a_n)=(f(a_1),\dots,f(a_n))$, the codewords concatenated.
- **Def. 10.7.** $f$ is *uniquely decodable* if its extension is injective.
- **Def. 10.8.** $f$ is a *prefix code* if no codeword is a prefix of another (p. 206).

**Example 10.2** (p. 207), with $\mathcal A=\{a,b,c\}$ except for the third code:
- $f(a)=0,f(b)=1,f(c)=10$: not uniquely decodable, since $f(ba)=f(c)=10$.
- $f(a)=0,f(b)=10,f(c)=11$: uniquely decodable and prefix.
- $f(a)=0,f(b)=01,f(c)=011,f(d)=0111$ (alphabet $\{a,b,c,d\}$): uniquely decodable but not prefix, because a 0 marks the start of the next codeword.

**Remark 10.3 (p. 207).** Prefix codes ⊂ uniquely decodable ⊂ all lossless codes. Huffman codes are prefix codes. Suffix-free codes are also uniquely decodable (decode in reverse). A uniquely decodable code has no empty codeword. Prefix codes decode instantaneously, while other uniquely decodable codes may need look-ahead. Prefix codes correspond one-to-one to binary trees with codewords at leaves, and to strategies of yes/no questions.

**Theorem 10.9 (Kraft–McMillan, p. 208).**
1. If $f$ is uniquely decodable with $l_a=l(f(a))$, then $\sum_{a\in\mathcal A}2^{-l_a}\le1$ (10.11).
2. Conversely, any lengths satisfying (10.11) are the lengths of some prefix code, which can be computed efficiently.

*Proof of 1, prefix case.* Generate independent Ber(½) bits and stop when a codeword has been written. The events "codeword a written" are mutually exclusive because of the prefix condition. So the stopping probability $\sum_a2^{-l_a}$ cannot exceed 1.

*Proof of 1, uniquely decodable case.* First take $\mathcal A$ finite, with $L=\max l_a$. Let $G_f(z)=\sum_az^{l_a}=\sum_{l=0}^LA_l(f)z^l$, where $A_l(f)$ is the number of codewords of length $l$. For the extension $f^k$, $G_{f^k}(z)=\sum_{a_1}\cdots\sum_{a_k}z^{l_{a_1}+\dots+l_{a_k}}=[G_f(z)]^k=\sum_{l=0}^{kL}A_l(f^k)z^l$. Unique decodability makes $f^k$ lossless, so $A_l(f^k)\le2^l$. Hence $G_f(1/2)^k=G_{f^k}(1/2)\le kL$ for all $k$. Therefore $\sum_a2^{-l_a}=G_f(1/2)\le\lim_{k}(kL)^{1/k}=1$. For infinite $\mathcal A$, apply this to every finite subset.

*Proof of 2.* Order $l_1\le l_2\le\cdots$ and set $a_i=\sum_{k<i}2^{-l_k}$, with $a_1=0$ and $a_i<1$ by Kraft. Let $f(i)$ be the first $l_i$ bits of the binary expansion of $a_i$. Suppose $f(i)$ were a prefix of $f(j)$ with $j>i$. Then $a_j-a_i\le2^{-l_i}$, since they agree on the first $l_i$ bits. But $a_j-a_i=2^{-l_i}+2^{-l_{i+1}}+\dots>2^{-l_i}$, a contradiction.

**Remark 10.4.** For compression efficiency we may ignore uniquely decodable codes that are not prefix codes. **Remark 10.5.** A conjecture of Ahlswede et al. says that Kraft sum ≤ 3/4 suffices for a fix-free code (prefix-free and suffix-free). Existence has so far been shown only for sum ≤ 5/8 (p. 208).

*Intuition note.* Each codeword of length $l$ "uses up" $2^{-l}$ of a total budget of 1. A prefix code can be built whenever the budget is not exceeded, and unique decodability cannot beat that budget.

**The optimization problem.** The best average length among prefix or uniquely decodable codes is
$$L^*(X)\triangleq\min\sum_aP_X(a)l_a\quad\text{s.t.}\ \sum_a2^{-l_a}\le1,\ l_a\in\mathbb N\tag{10.12}$$
This is an integer program, in general hard, but solvable in near-linear time by the Huffman algorithm (p. 209).

**Theorem 10.10.** $H(X)\le L^*(X)\le H(X)+1$ bit (10.13) (p. 209).
- Right inequality: take Shannon code lengths $l_a=\lceil\log_2\frac1{P_X(a)}\rceil$. Then $\sum2^{-l_a}\le\sum P_X(a)=1$, so by Thm 10.9 a prefix code exists, with $\mathbb El(f(X))\le H(X)+1$.
- Left inequality, first proof (the page misprints "Light"): relax the integer constraint to get the convex program (10.14), which lower-bounds $L^*$. Lagrange multipliers (left as an exercise) give minimum $H(X)$ at $l_a=\log_2\frac1{P_X(a)}$.
- Second proof: for lengths satisfying Kraft, let $Q(a)=\frac{2^{-l_a}}{\sum_a2^{-l_a}}$. Then $\mathbb El(f(X))-H(X)=D(P\|Q)-\log\sum_a2^{-l_a}\ge0$. The inequality holds because $D\ge0$ and the Kraft sum is ≤ 1.

**Huffman code (p. 210).** Build the binary tree bottom-up. (1) Choose the two least probable symbols. (2) Replace them by one symbol with the summed probability, as the parent node of the two. It stops after $|\mathcal A|-1$ steps. Assign 0/1 to branches. Complexity is $O(|\mathcal A|)$ for a sorted PMF and $O(|\mathcal A|\log|\mathcal A|)$ otherwise.

**Example 10.3.** $P_X=\{0.25,0.25,0.2,0.15,0.15\}$ for $a,\dots,e$. In the tree, $d,e$ sit under a node of probability 0.3, which is joined with $a$ in a node of 0.55; $b,c$ form a node of 0.45; the root joins the 0.55 and 0.45 nodes. Codebook: $a=00$, $b=10$, $c=11$, $d=010$, $e=011$ (p. 210).

**Theorem 10.11.** Huffman achieves the minimum in (10.12) among all prefix or uniquely decodable codes. The proof is only cited ([106, Sec. 5.8]) (p. 210).

**Remark 10.6 (drawbacks, p. 210–211).**
1. Huffman needs the source distribution. Universal compression is deferred to Chapter 13.
2. Coding symbol by symbol can achieve average length $\sum_iH(S_i)+n$ bits. Huffman on the whole block gives $H(S_1,\dots,S_n)+O(1)$, which exploits memory and is smaller than $\sum_iH(S_i)$ (usually much smaller). The cost is complexity $|\mathcal A|^n$, exponential in n.

The announced remedies: arithmetic coding (complexity linear in blocklength, length $H(S_1^n)$, Section 13.1) and Lempel–Ziv (low complexity, universal, provably optimal for all ergodic sources, Section 13.8).

**Chapter summary (p. 211):**
$$H(X)-\log_2[e(H(X)+1)]\le\mathbb E[l(f^*(X))]\le H(X)\le\mathbb E[l(f_{\text{Huffman}}(X))]\le H(X)+1.$$

## Toy example (ours)
Let $P=(0.6,0.3,0.1)$ on symbols 1, 2, 3.
- Entropy: $H=0.6(0.737)+0.3(1.737)+0.1(3.322)=0.442+0.521+0.332\approx1.296$ bits.
- $f^*$: codewords ∅, 0, 1, so lengths $0,1,1$ and $\mathbb E=0.6\cdot0+0.3+0.1=0.4$. Lower bound: $H-\log_2[e(H+1)]=1.296-\log_2(2.718\times2.296)=1.296-\log_2 6.24\approx1.296-2.642=-1.35$. So $-1.35\le0.4\le1.296$ holds.
- $f^*$ is not uniquely decodable. Its Kraft sum is $2^0+2^{-1}+2^{-1}=2>1$, so Thm 10.9 rules it out. This is why $f^*$ can beat $H$ in mean.
- Huffman: merge 0.3 and 0.1 into 0.4, then merge 0.6 and 0.4. Lengths are $1,2,2$, so $\mathbb E=0.6+0.6+0.2=1.4$, and $1.296\le1.4\le2.296$.
- Shannon code: $\lceil\log_2\frac1p\rceil=1,2,4$. Kraft sum $0.5+0.25+0.0625=0.8125\le1$. $\mathbb E=0.6+0.6+0.4=1.6\le H+1$, and it is worse than Huffman, as Thm 10.11 requires.

## Concepts
- [[entropy H(X)]] — average of $\log_2 1/P_X(X)$; the benchmark for mean code length (p. 199)
- [[source coding theorem]] — here Thm 10.3 for single-shot $f^*$, and the WLLN version $\frac1nl(f^*(S^n))\to H(S)$ in probability (p. 199, 202)
- [[prefix code & Kraft inequality]] — prefix codes exist for lengths with $\sum2^{-l_a}\le1$, and uniquely decodable codes obey it (p. 208)
- [[Huffman / arithmetic coding]] — Huffman is optimal among prefix/UD codes with $L^*\in[H,H+1]$; arithmetic coding and Lempel–Ziv are deferred (p. 210–211)
- [[entropy rate]] — the limit of the optimal compression rate of an i.i.d. process, equal to $H(S)$ here (p. 202)
- [[relative entropy / KL divergence]] — used to show $\mathbb El-H=D(P\|Q)-\log\sum2^{-l_a}\ge0$ (p. 209)
- [[universal coding]] — Huffman needs the distribution; whether a universal compressor exists, and at what price, is raised as a question to be addressed in Chapter 13 (p. 210)
- [[stochastic dominance]] (new) — $X\overset{st.}\le Y$ if $\mathbb P[Y\le t]\le\mathbb P[X\le t]$ for all t (p. 198)
- [[single-shot lossless compressor]] (new) — injective map $f:\mathcal X\to\{0,1\}^*$ with no extra constraint (p. 197–198)
- [[varentropy]] (new) — $V(S)=\mathrm{Var}[\log_2 1/P_S(S)]$; sets the Gaussian spread of code length (p. 200)
- [[uniquely decodable code]] (new) — a code whose symbol-by-symbol extension is injective (p. 206)
- [[Shannon code]] (new) — lengths $\lceil\log_2 1/P_X(a)\rceil$ (p. 209)
- [[Zipf's law]] (new) — rank–frequency $p_r\asymp r^{-\alpha}$, with $\alpha\approx1$ for words (p. 203)
- [[Mandelbrot's argument]] (new) — maximizing information per unit code length under the extra requirement $H(P)\ge h_0$ is achieved at a power law; proposed for word frequencies (p. 205–206)

## Canonical instances
- [[ternary-source-example]] — $P_S=[0.445,0.445,0.11]$: expected optimal length vs bounds and Gaussian approximations (p. 202–203)
- [[huffman-example-five-symbols]] — Example 10.3 with codebook 00, 10, 11, 010, 011 (p. 210)
- [[non-prefix-uniquely-decodable-code]] — Example 10.2: 0, 01, 011, 0111 (p. 207)
- [[zipf-rank-frequency-plot]] — English, Hebrew and Russian word frequencies, tails with slope close to −1 on log–log axes (p. 204)

## Bridges (candidates)
- [structural-analogy] Kraft inequality "budget" ↔ probability: lengths $l_a$ ↔ $Q(a)\propto2^{-l_a}$ — lengths and probabilities are interchangeable (p. 209)
- [same-math] Optimal code length of $S^n$ ≈ $nH+\sqrt{nV}\,Z$ ↔ statistics: CLT for sums of log-likelihoods — it follows from the CLT applied to $\sum\log\frac1{P_S(S_i)}$ via Cor. 10.5 (p. 201–202)
- [same-math] $\mathcal H(\Lambda)\le\inf_\lambda\lambda\Lambda+\log_2Z(\lambda)$ ↔ statistical physics/MaxEnt: partition function and Gibbs (exponential-family) form $P_\lambda\propto2^{-\lambda\,\text{cost}}$ (p. 205)
- [metaphor] Mandelbrot's brain/language co-evolution ↔ efficient-communication linguistics: words tuned to maximize information per unit cost (p. 205)

## Questions this raises
- If $f^*$ beats $H(X)$ in mean, what is the price? (It is not uniquely decodable, as the toy example shows.)
- How does the $\frac12\log_2 n$ and varentropy correction in (10.3) change for prefix codes on blocks?
- Can a code that does not know $P_X$ (universal compression) approach $H$, and at what cost?
- Which models other than Mandelbrot's (e.g. preferential attachment) explain power laws outside language?

## Exercises worth doing
The chapter mentions these exercises in passing; their statements are not printed in these pages.
- Exercise II.1 (p. 199) — compute $\mathbb E[l(f^*(X))]$ exactly as an infinite series — difficulty: medium
- Exercise I.4 (p. 200) — the entropy bound used in step (b) of Thm 10.3 — difficulty: medium
- Lagrange multiplier solution of (10.14) (p. 209, marked "Exercise!") — shows that the relaxed minimum equals $H(X)$ — difficulty: easy

## Reading notes
- The unit is labelled ch12 in the metadata, but the printed chapter number is **10** (running titles, theorem numbers 10.x). Printed page = pdf − 25.
- Misprint, p. 200: in step (d) of the Thm 10.3 proof the text says "the previously shown upper bound H(X) ≤ E[L]". The shown bound is $\mathbb E[L]\le H(X)$, and the argument needs that direction.
- Misprint, p. 209: "Light inequality" should read "Left inequality".
- The text layer of p. 200 garbles the second case of the exact asymptotics. The image shows $nH(S)-\frac12\log_2n+O(1)$.
- Table on p. 202: the column header "Lower bound (10.3)" is as printed. The text does not say which result produces the lower-bound numbers.
- Proofs of Thm 10.11, Prop. 1.5, Example 5.2 and Exercise I.4 are not in this unit. The claim that the upper bound in $\mathcal H(\Lambda)$ is tight is derived on p. 205. Concavity of $\mathcal H$ is asserted without proof.
- Citation numbers ([408], [291], etc.) refer to the book's bibliography, which is not in these pages.
