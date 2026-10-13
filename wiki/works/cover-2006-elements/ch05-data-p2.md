---
id: cover-2006-elements/ch05-data-p2
work: cover-2006-elements
unit: "5 Data Compression (part 2/2): end of 5.8, 5.9–5.12, chapter summary, problems, historical notes"
pages: 101–124
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Shannon–Fano–Elias and arithmetic coding, competitive optimality, and random-variable generation

## L0 — One line
Codeword lengths near $\log 1/p(x)$ cost within a small constant of the entropy $H(X)$, whether we compress a source (Shannon–Fano–Elias, arithmetic coding) or run the problem backwards and generate a random variable from fair coin flips.

## L1 — The gist (≤ 120 words)
How can we build good codes without a code tree, and how good are they? The unit first closes the proof that Huffman codes are optimal. Shannon–Fano–Elias coding then uses the cumulative distribution function to give codewords of length $\lceil\log 1/p\rceil+1$, which is within 2 bits of entropy. Applied to long blocks, this idea becomes arithmetic coding, which works sequentially. Shannon code lengths $\lceil\log 1/p\rceil$ are also "competitively optimal": no other code beats them by many bits with notable probability. Finally, the dual problem is generating a random variable from fair coins. It needs on average between $H(X)$ and $H(X)+2$ flips. Entropy is the cost in both directions.

**Prerequisites:** entropy and $\log_2$; Kraft inequality; prefix codes and code trees; expectation; binary expansions of real numbers; $H(Y,X)=H(X)+H(Y|X)$; geometric-type sums such as $\sum k2^{-k}$.

## L2 — Key ideas
- Huffman coding is optimal among all codes: $L(C^*)\le L(C')$. The proof is for binary alphabets and the author says it extends to $D$-ary ones. The greedy local merging gives a global optimum (p. 101).
- Shannon–Fano–Elias (SFE) coding takes the midpoint $\bar F(x)$ of each step of the cumulative distribution function (CDF, $F(x)=\sum_{a\le x}p(a)$) and keeps its first $\lceil\log 1/p(x)\rceil+1$ bits. The resulting code is prefix-free (no codeword is the beginning of another), and $L<H(X)+2$ (pp. 102–103).
- Arithmetic coding extends SFE to long blocks and can be extended to longer block lengths without redoing all the calculations. It computes $p(x^n)$ and $F(x^n)$ sequentially. It depends on a model whose $p(x^n)$ is easy to compute. The model need not equal the true distribution, but the procedure is efficient only if the model is close to the empirical distribution of the source (pp. 104–107).
- Shannon code lengths satisfy $\Pr(l(X)\ge l'(X)+c)\le 2^{-(c-1)}$ for any other code $l'$ (p. 107).
- For dyadic $p$ (every $\log 1/p(x)$ is an integer), the Shannon code wins at least as often as it loses against any other uniquely decodable code, with equality iff $l'=l$. It is robust to the payoff function (pp. 108–110).
- Generating $X$ from fair bits is described by a complete binary tree. The expected number of flips $ET$ equals the expected depth, and $ET\ge H(X)$ (pp. 111–113).
- For dyadic $p$ the optimum is $ET=H(X)$ (the Huffman tree). For general $p$, splitting each $p_i$ into dyadic atoms gives $H(X)\le ET<H(X)+2$ (pp. 113–116).
- The chapter summary collects the main bounds (Kraft/McMillan, Shannon, Huffman, wrong-code, stochastic processes, competitive, generation) (p. 117).

## L3 — Walkthrough

### 5.8 (end): Optimality of Huffman codes
The proof (begun in the previous part) shows that at every stage of the reduction the code built for $m$ symbols is optimal (p. 101).

**Theorem 5.8.1.** Huffman coding is optimal: if $C^*$ is the Huffman code and $C'$ is any other code, then $L(C^*)\le L(C')$ (p. 101).

The author proved it for a binary alphabet; he says the proof can be extended to a $D$-ary alphabet. Huffman coding is "greedy": it merges the two least likely symbols at each stage. The proof shows that this local optimality ensures global optimality (p. 101).

### 5.9 Shannon–Fano–Elias coding
Section 5.4 showed that lengths $l(x)=\lceil\log\frac1{p(x)}\rceil$ satisfy the Kraft inequality. This section gives a constructive procedure that uses the cumulative distribution function (CDF) (p. 101).

**Setup.** Take $\mathcal X=\{1,\dots,m\}$ and $p(x)>0$ for all $x$. The CDF is
$$F(x)=\sum_{a\le x}p(a)\tag{5.70}$$
The modified CDF is
$$\bar F(x)=\sum_{a<x}p(a)+\tfrac12p(x)\tag{5.71}$$
$\bar F(x)$ is the midpoint of the step of $F$ belonging to $x$ (Fig. 5.5). All probabilities are positive, so $\bar F(a)\ne\bar F(b)$ for $a\ne b$. Hence $\bar F(x)$ determines $x$ (p. 102).

**Rounding.** $\bar F(x)$ is generally a real number needing infinitely many bits. Let $\lfloor\bar F(x)\rfloor_{l(x)}$ be $\bar F(x)$ truncated to its first $l(x)$ bits. By the definition of rounding,
$$\bar F(x)-\lfloor\bar F(x)\rfloor_{l(x)}<\frac1{2^{l(x)}}\tag{5.72}$$
If $l(x)=\lceil\log\frac1{p(x)}\rceil+1$, then
$$\frac1{2^{l(x)}}<\frac{p(x)}2=\bar F(x)-F(x-1)\tag{5.73}$$
So the truncated value lies within the step of $x$, and $l(x)$ bits suffice to identify $x$ (p. 102).

**Prefix-freeness.** Read a codeword $z_1\dots z_l$ as the interval $[0.z_1\dots z_l,\ 0.z_1\dots z_l+2^{-l}]$. The code is prefix-free iff these intervals are disjoint (p. 102). The interval of a codeword has length $2^{-l(x)}$, which by (5.73) is less than half the step height. The author says its lower end lies in the lower half of the step. So the interval lies entirely within the step of its symbol. Different symbols have disjoint steps, so the intervals are disjoint and the code is prefix-free (p. 102). The procedure does not need the symbols ordered by probability. Problem 25 gives a variant that uses ordered probabilities (pp. 102–103).

**Expected length.**
$$L=\sum_xp(x)l(x)=\sum_xp(x)\Big(\Big\lceil\log\frac1{p(x)}\Big\rceil+1\Big)<H(X)+2\tag{5.74}$$
So the average length is within two bits of the entropy (p. 103).

> **Intuition note.** The CDF cuts the interval $[0,1]$ into steps whose heights are the probabilities. A step of height $p$ can be pinned down by a binary fraction with about $\log 1/p$ bits. One extra bit keeps each pinned interval inside its own step, so no codeword is a prefix of another.

**Example 5.9.1 (dyadic).** (p. 103)

| $x$ | $p(x)$ | $F(x)$ | $\bar F(x)$ | $\bar F$ in binary | $l(x)$ | codeword |
|---|---|---|---|---|---|---|
| 1 | 0.25 | 0.25 | 0.125 | 0.001 | 3 | 001 |
| 2 | 0.5 | 0.75 | 0.5 | 0.10 | 2 | 10 |
| 3 | 0.125 | 0.875 | 0.8125 | 0.1101 | 4 | 1101 |
| 4 | 0.125 | 1.0 | 0.9375 | 0.1111 | 4 | 1111 |

The average length is 2.75 bits and the entropy is 1.75 bits. The Huffman code reaches the entropy bound here. The last bit of the last two codewords could be dropped, but removing the last bit from all codewords destroys prefix-freeness (p. 103).

**Example 5.9.2 (non-dyadic).** Here $\bar F(x)$ may have an infinite binary expansion. A bar marks a repeating block, e.g. $0.01010101\ldots=0.\overline{01}$ (p. 103).

| $x$ | $p(x)$ | $F(x)$ | $\bar F(x)$ | $\bar F$ in binary | $l(x)$ | codeword |
|---|---|---|---|---|---|---|
| 1 | 0.25 | 0.25 | 0.125 | 0.001 | 3 | 001 |
| 2 | 0.25 | 0.5 | 0.375 | 0.011 | 3 | 011 |
| 3 | 0.2 | 0.7 | 0.6 | 0.10011… | 4 | 1001 |
| 4 | 0.15 | 0.85 | 0.775 | 0.1100011… | 4 | 1100 |
| 5 | 0.15 | 1.0 | 0.925 | 0.1110110… | 4 | 1110 |

The author says this code is 1.2 bits longer on average than the Huffman code of Example 5.6.1. (added step: from the table, the SFE average is $0.75+0.75+0.8+0.6+0.6=3.5$.) The next section extends SFE to arithmetic coding (p. 103).

### 5.10 Arithmetic coding
**Motivation.** Lengths $\log\frac1p$ are nearly optimal, within 1 bit of entropy. For small alphabets, though, efficiency needs long blocks. A binary source coded symbol by symbol needs 1 bit per symbol whatever its entropy. With long blocks the expected length per symbol can approach the entropy rate (p. 104). Huffman coding is a bottom-up procedure. It needs the probabilities of all sequences of one block length and the full code tree, and we are then stuck with that block length. Arithmetic coding, a direct extension of SFE, avoids this (p. 104).

**Idea.** Compute $p(x^n)$ and $F(x^n)$ efficiently for the source sequence $x^n$. A number in $(F(x^n)-p(x^n),F(x^n)]$ identifies $x^n$. Different sequences get different codewords. This alone does not guarantee a prefix-free set. A prefix-free set results from using $\bar F(x^n)$ rounded to $\lceil\log\frac1{p(x^n)}\rceil+1$ bits as in 5.9. The algorithm tracks both $F$ and $p$, so $\bar F$ is easy to compute at any stage (p. 104).

**Simplified setting.** The block length $n$ is known to encoder and decoder, and the alphabet is binary. There is a simple procedure for $p(x_1,\dots,x_n)$. Strings are in lexicographic order: $x>y$ if $x_i=1,\ y_i=0$ at the first $i$ where they differ. Equivalently $\sum_ix_i2^{-i}>\sum_iy_i2^{-i}$, i.e. $0.x>0.y$. Strings are the leaves of a depth-$n$ tree (Fig. 5.6), and $x>y$ means $x$ is to the right of $y$ (pp. 104–105).

**Computing $F$.** The author suspects that the probabilities of all leaves to the left of $x^n$ are needed to find $F(x^n)$; their sum is the sum over the subtrees to the left of $x^n$. Let $T_{x_1\dots x_{k-1}0}$ be the subtree of strings beginning $x_1\dots x_{k-1}0$:
$$p(T_{x_1x_2\ldots x_{k-1}0})=\sum_{y_{k+1}\ldots y_n}p(x_1x_2\cdots x_{k-1}0y_{k+1}\cdots y_n)\tag{5.75}$$
$$=p(x_1x_2\cdots x_{k-1}0)\tag{5.76}$$
Hence
$$F(x^n)=\sum_{y^n\le x^n}p(y^n)\tag{5.77}$$
$$=\sum_{T:\,T\text{ is to the left of }x^n}p(T)\tag{5.78}$$
$$=\sum_{k:\,x_k=1}p(x_1x_2\cdots x_{k-1}0)\tag{5.79}$$
So $F(x^n)$ is computed quickly from $p$ (p. 106). (See Reading notes on (5.77).)

**Example 5.10.1.** For $X_1,\dots,X_n$ Bernoulli($\theta$) in Fig. 5.6 (p. 106):
$$F(01110)=p(T_1)+p(T_2)+p(T_3)=p(00)+p(010)+p(0110)\tag{5.80}$$
$$=(1-\theta)^2+\theta(1-\theta)^2+\theta^2(1-\theta)^2\tag{5.81}$$
These terms can be computed recursively, e.g. $\theta^3(1-\theta)^3=(\theta^2(1-\theta)^2)\theta(1-\theta)$ (p. 106).

**Encoding and decoding.** To encode the next bit, compute $p(x^ix_{i+1})$ and update $F(x^ix_{i+1})$. So encoding is sequential. To decode, use the same procedure to compute the CDF and compare it with the value of the codeword, using the tree of Fig. 5.6 as a decision tree. At the top node, check whether the received $F(x^n)$ exceeds $p(0)$. If so, the subtree starting with 0 is to the left of $x^n$, hence $x_1=1$. Continue down the tree (p. 106).

**Models.** The procedure needs a model where $p(x^n)$ is easy to compute. Two examples:
$$p(x^n)=\prod_{i=1}^np(x_i)\ \text{(i.i.d.)}\tag{5.82}$$
$$p(x^n)=p(x_1)\prod_{i=2}^np(x_i|x_{i-1})\ \text{(Markov)}\tag{5.83}$$
In both, $p(x^nx_{n+1})$ follows easily from $p(x^n)$ (p. 106). The probabilities used need not equal the true distribution. This matters, for example, in image compression, where a "true" distribution is hard to describe. The procedure is efficient only if the model is close to the empirical distribution of the source (Theorem 5.4.3). Adaptive models, which change dynamically, work well for large classes of sources. Adaptive arithmetic coding is a simple example of a **universal code**, one designed for an arbitrary source distribution. Lempel–Ziv (Section 12.10) is another. The author skips implementation issues (accuracy, buffer sizes) and refers to Langdon [170] (p. 107).

> **Intuition note.** Arithmetic coding keeps narrowing an interval inside $[0,1]$ as each symbol arrives, and the interval's width is the sequence probability. The model's $p(x^n)$ drives the code lengths: the procedure is efficient only if the model is close to the empirical distribution of the source (p. 107).

### 5.11 Competitive optimality of the Shannon code
Huffman coding minimises expected length. But it is not better than every other code on every sequence: some codes give short words to infrequent symbols (p. 107). **Game:** two players design instantaneous codes for the same distribution. A symbol is drawn. Player A's payoff is $+1$ if A's codeword is shorter than B's, $-1$ if longer, and 0 for ties. Huffman lengths have no explicit expression, so the author analyses the Shannon code $l(x)=\lceil\log\frac1{p(x)}\rceil$ (p. 107).

**Theorem 5.11.1.** Let $l(x)$ be the Shannon code lengths and $l'(x)$ the lengths of any other code. Then
$$\Pr\big(l(X)\ge l'(X)+c\big)\le\frac1{2^{c-1}}\tag{5.84}$$
For example, the probability that $l'(X)$ is 5 or more bits shorter than $l(X)$ is at most $2^{-4}$ (c = 5) (p. 107).

*Proof.* (p. 108)
$$\Pr(l(X)\ge l'(X)+c)=\Pr\Big(\Big\lceil\log\tfrac1{p(X)}\Big\rceil\ge l'(X)+c\Big)\tag{5.85}$$
$$\le\Pr\Big(\log\tfrac1{p(X)}\ge l'(X)+c-1\Big)\tag{5.86}$$
$$=\Pr\big(p(X)\le2^{-l'(X)-c+1}\big)\tag{5.87}$$
$$=\sum_{x:\,p(x)\le2^{-l'(x)-c+1}}p(x)\tag{5.88}$$
$$\le\sum_{x:\,p(x)\le2^{-l'(x)-c+1}}2^{-l'(x)-(c-1)}\tag{5.89}$$
$$\le\sum_x2^{-l'(x)}2^{-(c-1)}\tag{5.90}$$
$$\le2^{-(c-1)}\tag{5.91}$$
The last step uses $\sum2^{-l'(x)}\le1$ (Kraft). $\square$

> **Intuition note.** For $l(X)\ge l'(X)+c$ to happen at a symbol, $l'$ must give it a codeword at least $c-1$ bits shorter than $\log 1/p(x)$ (by (5.87)). Kraft's inequality limits how many such symbols there can be. So the probability of that happening shrinks exponentially in $c$.

**Strengthening.** The "$+1$" in (5.84) makes the result non-symmetric. In a game one wants $l(x)<l'(x)$ more often than $l(x)>l'(x)$, and $\Pr\ge\frac12$ of $l\le l'+1$ does not ensure this. A pmf is **dyadic** if $\log\frac1{p(x)}$ is an integer for all $x$ (p. 108).

**Theorem 5.11.2.** For a dyadic pmf $p$, let $l(x)=\log\frac1{p(x)}$ be the Shannon code lengths and $l'(x)$ the lengths of any other uniquely decodable binary code. Then
$$\Pr(l(X)<l'(X))\ge\Pr(l(X)>l'(X))\tag{5.92}$$
with equality iff $l'(x)=l(x)$ for all $x$. So $l(x)=\log\frac1{p(x)}$ is *uniquely competitively optimal* (p. 108).

*Proof.* Define
$$\operatorname{sgn}(t)=\begin{cases}1&t>0\\0&t=0\\-1&t<0\end{cases}\tag{5.93}$$
Figure 5.7 shows
$$\operatorname{sgn}(t)\le2^t-1\quad\text{for }t=0,\pm1,\pm2,\dots\tag{5.94}$$
This is not true for all real $t$, but it is true at integers (p. 109). Then (pp. 109–110):
$$\Pr(l'(X)<l(X))-\Pr(l'(X)>l(X))=\sum_{x:\,l'(x)<l(x)}p(x)-\sum_{x:\,l'(x)>l(x)}p(x)\tag{5.95}$$
$$=\sum_xp(x)\operatorname{sgn}(l(x)-l'(x))\tag{5.96}$$
$$=E\operatorname{sgn}(l(X)-l'(X))\tag{5.97}$$
$$\overset{(a)}{\le}\sum_xp(x)\big(2^{l(x)-l'(x)}-1\big)\tag{5.98}$$
$$=\sum_x2^{-l(x)}\big(2^{l(x)-l'(x)}-1\big)\tag{5.99}$$
$$=\sum_x2^{-l'(x)}-\sum_x2^{-l(x)}\tag{5.100}$$
$$=\sum_x2^{-l'(x)}-1\tag{5.101}$$
$$\overset{(b)}{\le}1-1\tag{5.102}$$
$$=0\tag{5.103}$$
(a) uses (5.94). (b) uses the Kraft inequality for $l'$. Equality needs equality in both. In (a) equality holds only if $t=l-l'$ is 0 or 1. Equality in (b) means $l'$ satisfies Kraft with equality. The author says combining these gives $l'(x)=l(x)$ for all $x$. $\square$

**Corollary (non-dyadic $p$).** With $l(x)=\lceil\log\frac1{p(x)}\rceil$ and $l'$ any other code,
$$E\operatorname{sgn}\big(l(X)-l'(X)-1\big)\le0\tag{5.104}$$
The proof runs along the same lines (p. 110).

**Conclusion.** Shannon coding is optimal under a variety of criteria and is robust to the payoff function. For dyadic $p$: $E(l-l')\le0$, $E\operatorname{sgn}(l-l')\le0$, and by (5.94) $Ef(l-l')\le0$ for any $f$ with $f(t)\le2^t-1$ at integers $t$ (p. 110).

> **Intuition note.** "Expected length is smallest" is one way to compare codes, and "wins more often" is another. For dyadic distributions the Shannon lengths win on both. The proof works because $2^{-l}$ acts like a probability, so the Kraft inequality caps how much any rival code can gain.

### 5.12 Generation of discrete distributions from fair coins
Section 5.12 is a detour to the dual question. The author says it can be argued (Problem 26) that the encoded sequence is essentially incompressible, with an entropy rate close to 1 bit per symbol, so its bits are essentially fair coin flips. Now: how many fair flips are needed to generate $X\sim\mathbf p$? (p. 110)

**Example 5.12.1.** Target: $a$ w.p. $\frac12$, $b$ w.p. $\frac14$, $c$ w.p. $\frac14$. Rule: first bit 0 gives $a$; bits 10 give $b$; bits 11 give $c$. The average number of bits is $\frac12\cdot1+\frac14\cdot2+\frac14\cdot2=1.5$, which is also the entropy (pp. 110–111).

**General formulation.** Flips $Z_1,Z_2,\dots$ are fair; generate $X\in\{1,\dots,m\}$ with pmf $\mathbf p=(p_1,\dots,p_m)$. $T$ is the number of flips used. The algorithm is a binary tree whose leaves are labelled with outputs. Required properties (p. 111):
1. The tree is complete (every node is a leaf or has two descendants). It may be infinite.
2. A leaf at depth $k$ has probability $2^{-k}$. Many leaves may carry the same symbol, and their total probability must equal the desired probability.
3. $ET$ equals the expected depth of the tree.

Other algorithms give the same distribution, e.g. $00\to a,\ 01\to b,\ 10\to c,\ 11\to a$, but use 2 bits per sample, not 1.5 (p. 111).

**Lemma 5.12.1.** For a complete tree with a distribution on leaves $y\in\mathcal Y$ in which a leaf at depth $k$ has probability $2^{-k}$, the expected depth equals the entropy of this distribution (p. 112).

*Proof.* With $k(y)$ the depth of leaf $y$:
$$ET=\sum_{y\in\mathcal Y}k(y)2^{-k(y)}\tag{5.106}$$
$$H(Y)=-\sum_{y\in\mathcal Y}\frac1{2^{k(y)}}\log\frac1{2^{k(y)}}\tag{5.107}$$
$$=\sum_{y\in\mathcal Y}k(y)2^{-k(y)}\tag{5.108}$$
$$H(Y)=ET\tag{5.109}\ \square$$

**Theorem 5.12.1.** For any algorithm generating $X$, the expected number of fair bits satisfies
$$ET\ge H(X)\tag{5.110}$$
(The text says "greater than"; the formula has $\ge$.) (p. 112)

*Proof.* Represent the algorithm by a binary tree, with leaves labelled by distinct symbols $y\in\mathcal Y=\{1,2,\dots\}$ (infinite if the tree is). Let $Y$ be the leaf reached, so $\Pr(Y=y)=2^{-k}$ for a leaf at depth $k$. By Lemma 5.12.1,
$$ET=H(Y)\tag{5.111}$$
$X$ is a function of $Y$ (one or more leaves map to one output symbol), so by Problem 5 of Chapter 2
$$H(X)\le H(Y)\tag{5.112}$$
Thus
$$H(X)\le ET\tag{5.113}\ \square$$
(pp. 112–113)

**Theorem 5.12.2 (dyadic case).** If $X$ has a dyadic distribution, the optimal algorithm needs exactly
$$ET=H(X)\tag{5.114}$$
(p. 113).

*Proof.* The lower bound is Theorem 5.12.1. For the construction, use the Huffman code tree of $X$. For dyadic $p$ the Huffman code equals the Shannon code and meets the entropy bound. The leaf for $x$ has depth $\log\frac1{p(x)}$, hence probability $2^{-\log(1/p(x))}=p(x)$. The expected depth equals the entropy since the distribution is dyadic:
$$ET=H(X)\tag{5.115}\ \square$$

**Non-dyadic case.** The Huffman tree would generate a dyadic distribution on the leaves, not the target. Every leaf probability is $2^{-k}$. So each $p_i$ must be split into atoms of this form, then allotted to leaves. To keep the tree shallow, use the largest possible atoms: take the largest $2^{-k}$ below $p_i$, then the largest that fits the remainder, and so on. This is the same as taking the binary expansion (p. 113):
$$p_i=\sum_{j\ge1}p_i^{(j)},\quad p_i^{(j)}=2^{-j}\text{ or }0\tag{5.116}$$
The atoms are $\{p_i^{(j)}:i=1,\dots,m,\ j\ge1\}$ and their total is $\sum_ip_i=1$. An atom $2^{-j}$ goes to a leaf at depth $j$. The depths satisfy the Kraft inequality, so by Theorem 5.2.1 such a tree exists (p. 114).

**Example 5.12.2.** $X=a$ w.p. $\frac23$, $b$ w.p. $\frac13$ (5.117). Binary expansions: $\frac23=0.101010\ldots_2$ (5.118), $\frac13=0.010101\ldots_2$ (5.119). Atoms: $\frac23\to(\frac12,\frac18,\frac1{32},\ldots)$ (5.120), $\frac13\to(\frac14,\frac1{16},\frac1{64},\ldots)$ (5.121). Fig. 5.9 shows the tree: $a$ at depth 1, $b$ at depth 2, $a$ at depth 3, $b$ at depth 4, and so on, infinitely (p. 114). The author says he has argued the procedure is optimal (minimum expected depth) but gives no formal proof (pp. 114–115).

**Theorem 5.12.3.** The expected number of fair bits needed by the optimal algorithm lies between
$$H(X)\le ET<H(X)+2\tag{5.122}$$
(p. 115).

*Proof.* The lower bound is Theorem 5.12.1. For the upper bound, split each $p_i\to(p_i^{(1)},p_i^{(2)},\dots)$ (5.123). The atoms form a dyadic distribution of a variable $Y$, so the tree gives
$$ET=H(Y)\tag{5.124}$$
Since $X$ is a function of $Y$,
$$H(Y)=H(Y,X)=H(X)+H(Y|X)\tag{5.125}$$
and the aim is to show $H(Y|X)<2$ by an algebraic proof (p. 115). Expand, using that each atom is 0 or $2^{-k}$:
$$H(Y)=-\sum_{i=1}^m\sum_{j\ge1}p_i^{(j)}\log p_i^{(j)}\tag{5.126}$$
$$=\sum_{i=1}^m\ \sum_{j:\,p_i^{(j)}>0}j2^{-j}\tag{5.127}$$
Call the term for $i$
$$T_i=\sum_{j:\,p_i^{(j)}>0}j2^{-j}\tag{5.128}$$
Pick $n$ with $2^{-(n-1)}>p_i\ge2^{-n}$, i.e.
$$n-1<-\log p_i\le n\tag{5.129}$$
Then $p_i^{(j)}>0$ only if $j\ge n$, so
$$T_i=\sum_{j:\,j\ge n,\ p_i^{(j)}>0}j2^{-j}\tag{5.130}$$
$$p_i=\sum_{j:\,j\ge n,\ p_i^{(j)}>0}2^{-j}\tag{5.131}$$
Claim $T_i<-p_i\log p_i+2p_i$. Consider the difference (pp. 115–116):
$$T_i+p_i\log p_i-2p_i\overset{(a)}{<}T_i-p_i(n-1)-2p_i\tag{5.132}$$
$$=T_i-(n-1+2)p_i\tag{5.133}$$
$$=\sum_{j\ge n,\ p_i^{(j)}>0}j2^{-j}-(n+1)\sum_{j\ge n,\ p_i^{(j)}>0}2^{-j}\tag{5.134}$$
$$=\sum_{j\ge n,\ p_i^{(j)}>0}(j-n-1)2^{-j}\tag{5.135}$$
$$=-2^{-n}+0+\sum_{j\ge n+2,\ p_i^{(j)}>0}(j-n-1)2^{-j}\tag{5.136}$$
$$\overset{(b)}{=}-2^{-n}+\sum_{k\ge1,\ p_i^{(k+n+1)}>0}k2^{-(k+n+1)}\tag{5.137}$$
$$\overset{(c)}{\le}-2^{-n}+\sum_{k\ge1}k2^{-(k+n+1)}\tag{5.138}$$
$$=-2^{-n}+2^{-(n+1)}2\tag{5.139}$$
$$=0\tag{5.140}$$
Here (a) follows from (5.129), (b) is a change of variables, and (c) enlarges the range of summation. (The step to (5.139) uses $\sum_{k\ge1}k2^{-k}=2$, an added step.) The two leading terms of (5.136) come from $j=n$ (coefficient $-1$) and $j=n+1$ (coefficient 0). Hence
$$T_i<-p_i\log p_i+2p_i\tag{5.141}$$
Since $ET=\sum_iT_i$,
$$ET<-\sum_ip_i\log p_i+2\sum_ip_i=H(X)+2\tag{5.142}\ \square$$

*Skip path:* carry forward $T_i<-p_i\log p_i+2p_i$ and the conclusion $H(X)\le ET<H(X)+2$.

> **Intuition note.** A fair bit carries one bit of randomness, so you cannot create entropy $H(X)$ from fewer than $H(X)$ bits on average. When $p$ is dyadic, the atoms are the probabilities themselves and the cost is exactly $H(X)$. Otherwise the procedure's cost is the entropy of the atoms, which Theorem 5.12.3 bounds by $H(X)+2$.

### Summary of Chapter 5 (p. 117)
The author lists:
- Kraft: instantaneous codes $\Leftrightarrow\sum D^{-l_i}\le1$. McMillan: uniquely decodable codes $\Leftrightarrow\sum D^{-l_i}\le1$.
- $L=\sum p_il_i\ge H_D(X)$ (5.143).
- Shannon code $l_i=\lceil\log_D\frac1{p_i}\rceil$, $L<H_D(X)+1$ (5.144–5.145).
- Huffman code $L^*=\min_{\sum D^{-l_i}\le1}\sum p_il_i$ with $H_D(X)\le L^*<H_D(X)+1$ (5.146–5.147).
- Wrong code, with $X\sim p(x)$ and $l(x)=\lceil\log\frac1{q(x)}\rceil$: $H(p)+D(p\|q)\le L<H(p)+D(p\|q)+1$ (5.148).
- Stochastic processes: $\frac{H(X_1,\dots,X_n)}n\le L_n<\frac{H(X_1,\dots,X_n)}n+\frac1n$ (5.149). Stationary processes: $L_n\to H(\mathcal X)$ (5.150).
- Competitive optimality $\Pr(l(X)\ge l'(X)+c)\le\frac1{2^{c-1}}$ (5.151).
- Generation of random variables $H(X)\le ET<H(X)+2$ (5.152).

### Problems for Chapter 5 (pp. 118–124)
There are 26 problems. They cover: relations between instantaneous and uniquely decodable codes (1–3, 18, 20, 24); Huffman codes, binary and ternary (4–7, 11–14, 17, 21–23); Markov-source coding (8); tightness of the $H+1$ bound (9); codes achieving the entropy bound (10); Twenty Questions and Hi-Lo games (7, 13, 16); continuity of optimal length (19); Shannon's code construction (25); and dyadic Huffman output as fair coin flips (26).

### Historical notes (p. 124)
Shannon's original paper contains the source coding theorem and simple code examples. Shannon described the procedure of Problem 25, which he attributed to Fano. The Kraft inequality for uniquely decodable codes was first proved by McMillan, and the proof given in the book is due to Karush. Huffman coding was exhibited and proved optimal by Huffman. Arithmetic coding has its roots in a Shannon–Fano code developed by Elias (unpublished), which Jelinek analysed. The prefix-free construction in the text is due to Gilbert and Moore. Arithmetic coding itself was developed by Rissanen and Pasco. Section 5.12 follows Knuth and Yao. Universal algorithms (Lempel–Ziv) are deferred to Chapter 12.

## Toy example (ours, not from the text)
**SFE code for $p=(0.4,\,0.4,\,0.2)$ on $x=1,2,3$.**
- $F=(0.4,\ 0.8,\ 1.0)$, so $\bar F=(0.2,\ 0.6,\ 0.9)$.
- Lengths $\lceil\log_2\frac1p\rceil+1$: $\log_2 2.5=1.32\to2$, plus 1 gives 3, 3; $\log_2 5=2.32\to3$, plus 1 gives 4.
- Binary truncations:
  - $0.2=0.00110011\ldots$; the first 3 bits give 001, i.e. 0.125. The interval is $[0.125,0.25]$, inside the step $(0,0.4]$.
  - $0.6=0.10011001\ldots$; the first 3 bits give 100, i.e. 0.5. The interval is $[0.5,0.625]$, inside $(0.4,0.8]$.
  - $0.9=0.111001\ldots$ (0.5+0.25+0.125 = 0.875, remainder 0.025); the first 4 bits give 1110, i.e. 0.875. The interval is $[0.875,0.9375]$, inside $(0.8,1.0]$.
- Codewords 001, 100, 1110. The three intervals are disjoint, so the code is prefix-free.
- $L=0.4\cdot3+0.4\cdot3+0.2\cdot4=1.2+1.2+0.8=3.2$. $H=0.8\cdot1.3219+0.2\cdot2.3219\approx1.522$. $L=3.2<H+2\approx3.52$. ✓

**Fair-coin generation of $(\frac34,\frac14)$.** $\frac34=0.11_2$ gives atoms $\frac12,\frac14$; $\frac14$ is one atom. Leaves: $a$ at depth 1 (probability $\frac12$), $a$ at depth 2 (probability $\frac14$), $b$ at depth 2 (probability $\frac14$). $ET=\frac12\cdot1+\frac14\cdot2+\frac14\cdot2=1.5$. $H(X)=0.75\log_2\frac43+0.25\cdot2\approx0.311+0.5=0.811$. So $H(X)\le1.5<H(X)+2\approx2.81$. ✓

## Concepts
- [[shannon-fano-elias-coding]] (new) — code by truncating the CDF midpoint $\bar F(x)$ to $\lceil\log\frac1{p(x)}\rceil+1$ bits; prefix-free; $L<H+2$ (p. 102)
- [[cumulative-distribution-function]] (new) — $F(x)=\sum_{a\le x}p(a)$; the modified $\bar F$ is the step midpoint (p. 101–102)
- [[huffman-arithmetic-coding]] — Huffman: greedy optimal code (Theorem 5.8.1); arithmetic: sequential block coding via $p(x^n)$, $F(x^n)$ (pp. 101, 104–106)
- [[prefix-code-kraft-inequality]] — prefix-freeness read as disjoint intervals; $\sum2^{-l}\le1$ used in all proofs (pp. 102, 108, 117)
- [[dyadic-distribution]] (new) — pmf with $\log\frac1{p(x)}$ an integer for all $x$ (p. 108)
- [[competitive-optimality]] (new) — a code beats another more often than it loses; Shannon code is uniquely so for dyadic $p$ (pp. 107–110)
- [[universal-coding]] — code designed for an arbitrary source distribution, e.g. adaptive arithmetic coding (p. 107)
- [[random-variable-generation-from-fair-coins]] (new) — generating $X\sim p$ by a complete binary tree of fair flips; $H(X)\le ET<H(X)+2$ (pp. 110–115)
- [[entropy]] — lower bound for compression and for coin-flip generation (pp. 103, 112)
- [[chain-rule]] — $H(Y,X)=H(X)+H(Y|X)$ used in Theorem 5.12.3 (p. 115)
- [[relative-entropy-kl-divergence]] — cost of a wrong code, $H(p)+D(p\|q)$, only in the summary (p. 117)
- [[entropy-rate]] — block coding's per-symbol length tends to it; summary (pp. 104, 117)

## Canonical instances
- [[sfe-dyadic-example]] — dyadic SFE code: 2.75 bits vs entropy 1.75 (p. 103)
- [[sfe-nondyadic-example]] — 5-symbol SFE code, 1.2 bits longer than Huffman (p. 103)
- [[arithmetic-bernoulli-F01110]] — $F(01110)$ by subtrees for Bernoulli($\theta$) (p. 106)
- [[fair-coin-abc-tree]] — $(\frac12,\frac14,\frac14)$ generated in 1.5 flips (p. 111)
- [[fair-coin-two-thirds-tree]] — $(\frac23,\frac13)$ via infinite tree with dyadic atoms (p. 114)
- [[twenty-questions]] — appears only in Problems 7 and 13 (pp. 118–120)

## Bridges (candidates)
- [structural-analogy] SFE/arithmetic coding: interval of width $p(x^n)$ inside $[0,1]$ ↔ sequential Bayesian prediction in statistics: model's $p(x^{i+1}|x^i)$ updates one sequence probability — both turn a predictive model into a code length.
- [same-math] Lemma 5.12.1 (expected depth $=H(Y)$ for leaf probabilities $2^{-k}$) ↔ information-theory canon, prefix codes: dyadic Shannon code reaches $L=H$ — the same identity read in two directions.
- [structural-analogy] Competitive optimality ($\Pr$ of winning over another code) ↔ game theory: two-person zero-sum game with payoff $\operatorname{sgn}(l-l')$ — the author states it literally as a zero-sum game, but his results bound probabilities rather than solve for equilibria.
- [structural-analogy] Generating $X$ from fair bits (tree of flips) ↔ simulation in computational social science: drawing categorical samples from a pseudo-random bit stream; $H(X)$ lower-bounds the random bits used.

## Questions this raises
- If an arithmetic coder uses a model $q$ that is not the true $p$, how does the extra length relate to $D(p\|q)$ from the summary's "wrong code" bound?
- Does applying (5.74) to blocks $X^n$ give a per-symbol bound of the form $(H(X^n)+2)/n$, and is the SFE/arithmetic cost then arbitrarily close to the entropy rate as $n$ grows?
- The author argues but does not prove that the dyadic-atom tree is optimal for non-dyadic $p$. What would a formal proof look like?
- Does Shannon-code competitive optimality extend to Huffman codes, whose lengths have no explicit formula?

## Exercises worth doing
- Ex. 9 (p. 119) — build a distribution whose optimal expected length approaches $H(X)+1$, showing the Huffman bound is tight — difficulty: medium
- Ex. 12 (p. 120) — Huffman code with lengths that exceed the Shannon length for some symbols; optimal length sets need not be unique — difficulty: easy
- Ex. 21 (pp. 121–122) — optimal code for $m$ equiprobable outcomes; redundancy as a function of $m$ — difficulty: medium
- Ex. 23 (p. 122) — "merges" volume equals a Huffman problem, bounded by $WH(\tilde{\mathbf W})\le V\le WH(\tilde{\mathbf W})+W$ — difficulty: medium
- Ex. 24 (pp. 122–123) — Sardinas–Patterson test for unique decodability — difficulty: hard
- Ex. 26 (pp. 123–124) — Huffman coding of a dyadic source produces fair coin flips, linking to Section 5.12 — difficulty: medium

## Reading notes
- **Part boundaries.** This unit starts on printed p. 101 (on PDF page 123), in the closing lines of the proof of Theorem 5.8.1. It covers 5.9–5.12, the chapter summary, problems, and historical notes, ending on printed p. 124 (on PDF page 146). Offset: printed = pdf − 22.
- **Edition.** The source is the 1991 first edition (as noted in the unit metadata), not the 2006 second edition. Numbering and content may differ from the second edition.
- **OCR.** The text layer garbles numbers: "6.8.1", "6.9.1", "6.12.1", "6.12.2", "(6.151)", "(6.152)", "Theorem 5.123", page numbers printed as "301", "203", "207", "130", "313", "339", and "Z(x)" for $l(x)$. The images show 5.x numbering and the correct page numbers, and I followed the images. Several equations are garbled in the text layer; I read them from the images. In (5.131) the summation condition is read as $j\ge n$ (consistent with (5.130)).
- **Possible inconsistency, (5.77).** As printed, (5.77) sums over $y^n\le x^n$ (which includes $x^n$ itself). Lines (5.78)–(5.79) and Example 5.10.1 sum only subtrees strictly to the left of $x^n$, which excludes $p(x^n)$. I reported both as printed.
- **Wording.** Theorem 5.12.1 is worded "greater than" but stated as $\ge$ in (5.110); I used $\ge$. The equation number (5.153) does not appear in this unit (the numbering goes from (5.152) to (5.154)).
- **Solutions.** No solutions to the problems are printed in these pages.
