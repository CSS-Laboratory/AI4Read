---
id: cover-2006-elements/ch05-data-p1
work: cover-2006-elements
unit: "5 Data Compression (part 1/2): sections 5.1–5.8 (to the middle of the Huffman optimality proof)"
pages: 78–100
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Data Compression (part 1): Kraft inequality, entropy bound, Huffman codes

## L0 — One line
The expected length of any prefix (or uniquely decodable) code is at least the entropy $H_D(X)$, the best code is less than 1 symbol above it, and Huffman's algorithm finds that best code.

## L1 — The gist (≤ 120 words)
How short can the average description of a random variable be? The unit defines non-singular, uniquely decodable and prefix codes. It proves the Kraft inequality: prefix-code lengths satisfy $\sum D^{-l_i}\le 1$, and any lengths that satisfy it can be realised. Hence $L\ge H_D(X)$, with equality iff the distribution is D-adic (every probability is a power of $1/D$). Lengths $\lceil\log_D 1/p_i\rceil$ give $H\le L^*<H+1$. Coding blocks brings the cost per symbol close to the entropy (rate). Coding for a wrong distribution $q$ costs $D(p\|q)$ extra. Uniquely decodable codes obey Kraft too (McMillan). Huffman's algorithm builds optimal codes; its optimality proof begins and is cut off here.

**Prerequisites:** logarithms and expectation; entropy and relative entropy ($D(p\|q)\ge0$); Lagrange multipliers; binary trees; entropy rate of a stationary process.

## L2 — Key ideas
- A source code maps each value to a string over a D-ary alphabet. The classes nest: all ⊃ non-singular ⊃ uniquely decodable ⊃ instantaneous (prefix). Prefix codes can be decoded symbol by symbol without looking ahead (pp. 79–82).
- Kraft inequality: prefix codeword lengths must satisfy $\sum D^{-l_i}\le1$. Conversely, any lengths satisfying it come from some prefix code. It also holds for countably infinite codes (pp. 82–84).
- Main bound: any instantaneous D-ary code has $L\ge H_D(X)$, with equality iff $p_i=D^{-l_i}$ (D-adic distribution). Calculus suggests $l_i^*=-\log_D p_i$ (pp. 85–86).
- Rounding up, $l_i=\lceil\log_D 1/p_i\rceil$, gives a code with $H_D\le L<H_D+1$, so the optimal $L^*$ satisfies the same bounds. Coding blocks of $n$ i.i.d. symbols gives $H\le L_n<H+1/n$. For a general process the per-symbol bounds use $H(X_1,\dots,X_n)/n$, and $L_n^*\to$ entropy rate if the process is stationary (pp. 87–89).
- A Shannon code built for the wrong distribution $q$ has expected length between $H(p)+D(p\|q)$ and $H(p)+D(p\|q)+1$. So $D(p\|q)$ is the coding penalty for wrong information (pp. 89–90).
- McMillan: uniquely decodable codes also satisfy Kraft, so they allow no new sets of codeword lengths beyond prefix codes (pp. 90–92).
- Huffman's algorithm merges the two least likely symbols repeatedly. It works for D-ary alphabets, with dummy zero-probability symbols if needed. It is equivalent to the optimal 20-questions strategy (pp. 92–95).
- Huffman and Shannon codes differ per symbol. Either can be shorter for a given symbol, but Huffman is shorter on average, and optimal length sets are not unique (pp. 96–97).
- Optimality proof, first half: an optimal code exists with the two least likely symbols as sibling longest codewords. Merging them changes $L$ by the fixed amount $p_{m-1}+p_m$, which reduces the problem to $m-1$ symbols (pp. 97–100).

## L3 — Walkthrough

### Chapter introduction (p. 78)
The chapter puts content into the definition of entropy by finding the limit of data compression. Frequent outcomes get short descriptions, rare ones longer descriptions; the text's example is Morse code (p. 78). The plan: define instantaneous codes; prove Kraft; show $L\ge H$; show Shannon's construction approaches $H$ for repeated descriptions; give Huffman's procedure (p. 78). The introduction also announces competitive optimality and random-number generation; these are not in these pages.

### 5.1 Examples of codes (pp. 79–82)
**Definitions.**
- A *source code* $C$ for $X$ maps the range $\mathcal X$ to $\mathcal D^*$, the finite strings over a D-ary alphabet. $C(x)$ is the codeword and $l(x)$ its length (p. 79).
- Expected length: $L(C)=\sum_{x\in\mathcal X}p(x)\,l(x)$ \tag{5.1} (p. 79).
- Without loss of generality the alphabet is $\{0,1,\dots,D-1\}$ (p. 79).

**Example 5.1.1.** $p=(1/2,1/4,1/8,1/8)$ with codewords $0,10,110,111$. Here $H(X)=1.75$ bits and $L(C)=1.75$ bits. The bit string 0110111100110 decodes as 134213 (p. 79).

**Example 5.1.2.** $p=(1/3,1/3,1/3)$ with codewords $0,10,11$. The code is uniquely decodable, with $H=\log 3=1.58$ bits and average length "1.66" bits, so $EL>H$ (p. 79).

**Example 5.1.3 (Morse).** It uses four symbols: dot, dash, letter space, word space. Short sequences stand for frequent letters (E is one dot; Q is dash, dash, dot, dash). It is not optimal for four symbols, because many codewords go unused. The count of allowed sequences was solved by Shannon in 1948 (p. 80).

**Increasingly strict classes (pp. 80–81).**
- *Non-singular*: $x_i\ne x_j\Rightarrow C(x_i)\ne C(x_j)$ \tag{5.4}. This suffices for describing one value.
- *Extension* $C^*$: maps $x_1\cdots x_n$ to the concatenation $C(x_1)\cdots C(x_n)$. Example 5.1.4: if $C(x_1)=00$ and $C(x_2)=11$, then $C(x_1x_2)=0011$.
- *Uniquely decodable*: the extension is non-singular. One may have to read the entire string to decode even the first symbol.
- *Prefix (instantaneous) code*: no codeword is a prefix of another. The end of each codeword is recognised at once, so the code is "self-punctuating". Example: in Example 5.1.1, 01011111010 parses as 0, 10, 111, 110, 10.

**Table 5.1** (p. 82; Figure 5.1 shows the nesting, p. 81):

| X | Singular | Non-singular, not UD | UD, not instantaneous | Instantaneous |
|---|---|---|---|---|
| 1 | 0 | 0 | 10 | 0 |
| 2 | 0 | 010 | 00 | 10 |
| 3 | 0 | 01 | 11 | 110 |
| 4 | 0 | 10 | 110 | 111 |

- In the non-singular code, 010 can be read as 2, or 14, or 31, so it is not uniquely decodable (p. 81).
- The UD-but-not-instantaneous code is decoded from the start. Bits 00 or 10 are decoded at once. If the first two bits are 11 and the next bit is 1, the symbol is 3. If instead a run of 0s follows the 11, an odd run length means the codeword is 110 (symbol 4) and an even length means 11 (symbol 3) (pp. 81–82).
- The Sardinas–Patterson test for unique decodability is mentioned, with details in Problem 24 (p. 82).

### 5.2 Kraft inequality (pp. 82–84)
**Theorem 5.2.1 (Kraft).** For any prefix code over an alphabet of size $D$, the lengths $l_1,\dots,l_m$ satisfy
$$\sum_i D^{-l_i}\le 1.\tag{5.6}$$
Conversely, if lengths satisfy this, a prefix code with these lengths exists (p. 82).

*Proof (p. 83).*
1. Use a D-ary tree. Each codeword is a node, reached by the path of its symbols from the root (Figure 5.2).
2. The prefix condition means no codeword is an ancestor of another. Each codeword removes its descendants from use.
3. Let $l_{\max}$ be the longest length. A codeword of length $l_i$ has $D^{l_{\max}-l_i}$ descendants at level $l_{\max}$. These descendant sets are disjoint, and there are at most $D^{l_{\max}}$ nodes at that level. So
$$\sum_i D^{l_{\max}-l_i}\le D^{l_{\max}}\tag{5.7}$$
and dividing by $D^{l_{\max}}$ gives $\sum_i D^{-l_i}\le1$ \tag{5.8}.
4. Converse: label the first node (lexicographically) of depth $l_1$ as codeword 1 and remove its descendants. Label the first remaining node of depth $l_2$ as codeword 2, and so on.

*Intuition note.* Each codeword of length $l$ uses up a share $D^{-l}$ of the "code space". Short words are expensive, and the total space is 1. This is why the numbers $D^{-l_i}$ behave like probabilities.

**Theorem 5.2.2 (Extended Kraft).** For a countably infinite prefix code, $\sum_{i=1}^\infty D^{-l_i}\le1$ \tag{5.9}. Conversely, lengths satisfying it admit a prefix code (p. 84).

*Proof (p. 84).* The codeword $y_1\cdots y_{l_i}$ gives the real number
$$0.y_1y_2\cdots y_{l_i}=\sum_{j=1}^{l_i}y_jD^{-j}\tag{5.10}$$
and the interval
$$\Big(0.y_1\cdots y_{l_i},\;0.y_1\cdots y_{l_i}+\tfrac1{D^{l_i}}\Big)\tag{5.11}$$
of reals whose D-ary expansion starts with the codeword. The prefix condition makes these subintervals of $[0,1]$ disjoint, so their lengths sum to at most 1 \tag{5.12}. The converse assigns intervals in order from the low end of the unit interval (after reordering the indices).

Section 5.5 will show that uniquely decodable codes also satisfy Kraft (p. 84).

### 5.3 Optimal codes (pp. 84–86)
Kraft is necessary and sufficient for the existence of a prefix code with given lengths. So the optimal prefix code solves: minimize $L=\sum p_il_i$ \tag{5.13} over integers with $\sum D^{-l_i}\le1$ \tag{5.14} (p. 85).

**Calculus heuristic (p. 85).** Ignore integrality and take equality in the constraint:
$$J=\sum p_il_i+\lambda\Big(\sum D^{-l_i}\Big)\tag{5.15}$$
$$\frac{\partial J}{\partial l_i}=p_i-\lambda D^{-l_i}\log_eD\tag{5.16}$$
Setting this to 0 gives $D^{-l_i}=\dfrac{p_i}{\lambda\log_eD}$ \tag{5.17}. Substituting in the constraint gives $\lambda=1/\log_eD$, hence $p_i=D^{-l_i}$ \tag{5.18}, with optimal lengths
$$l_i^*=-\log_Dp_i\tag{5.19}$$
and expected length $L^*=\sum p_il_i^*=-\sum p_i\log_Dp_i=H_D(X)$ \tag{5.20}. Since lengths must be integers, this is not always attainable. The authors verify optimality directly instead of proving by calculus that it is a global minimum (p. 86).

**Theorem 5.3.1.** The expected length of any instantaneous D-ary code satisfies $L\ge H_D(X)$ \tag{5.21}, with equality iff $D^{-l_i}=p_i$ (p. 86).

*Proof (p. 86).*
$$L-H_D(X)=\sum p_il_i-\sum p_i\log_D\tfrac1{p_i}=-\sum p_i\log_DD^{-l_i}+\sum p_i\log_Dp_i\tag{5.22–5.23}$$
Let $r_i=D^{-l_i}/\sum_jD^{-l_j}$ and $c=\sum D^{-l_i}$. Then
$$L-H=\sum p_i\log_D\frac{p_i}{r_i}-\log_Dc\tag{5.24}$$
$$=D(\mathbf p\|\mathbf r)+\log_D\frac1c\tag{5.25}$$
$$\ge0\tag{5.26}$$
by non-negativity of relative entropy and $c\le1$ (Kraft). Equality holds iff $p_i=D^{-l_i}$ for all $i$, i.e. iff every $-\log_Dp_i$ is an integer.

*Intuition note.* Entropy is a floor that no prefix code can beat. The extra cost has two sources: the mismatch $D(\mathbf p\|\mathbf r)$ between the true distribution and the one implied by the lengths, and the unused code space $\log_D(1/c)$.

**Definition.** A distribution is *D-adic* if each probability equals $D^{-n}$ for some integer $n$. So equality in 5.3.1 holds iff the distribution of $X$ is D-adic (p. 86).

The proof suggests a procedure: find the D-adic distribution closest to $p$ in relative entropy and use its lengths. But this search is not obvious (p. 87). Shannon–Fano coding (5.4) is a good suboptimal procedure, and Huffman coding (5.6) finds the optimal code (p. 87).

### 5.4 Bounds on the optimal codelength (pp. 87–90)
**Shannon code.** Choose
$$l_i=\Big\lceil\log_D\tfrac1{p_i}\Big\rceil\tag{5.29}$$
($\lceil x\rceil$ is the smallest integer $\ge x$). These satisfy Kraft because $\sum D^{-\lceil\log\frac1{p_i}\rceil}\le\sum D^{-\log\frac1{p_i}}=\sum p_i=1$ \tag{5.30}. Also $\log_D\frac1{p_i}\le l_i<\log_D\frac1{p_i}+1$ \tag{5.31}. Multiplying by $p_i$ and summing gives $H_D(X)\le L<H_D(X)+1$ \tag{5.32} (p. 87).

**Theorem 5.4.1.** For optimal lengths $l_i^*$ and $L^*=\sum p_il_i^*$,
$$H_D(X)\le L^*<H_D(X)+1.\tag{5.33}$$
*Proof (p. 88).* The Shannon lengths satisfy Kraft and (5.34). The optimal $L^*$ is at most $L$ of the Shannon code, and $L^*\ge H_D$ by Theorem 5.3.1.

**Block coding (p. 88).** The overhead of up to 1 bit comes from rounding. Spread it over $n$ i.i.d. symbols, treated as one supersymbol from $\mathcal X^n$. Define
$$L_n=\frac1n\sum p(x_1,\dots,x_n)\,l(x_1,\dots,x_n)=\frac1nEl(X_1,\dots,X_n)\tag{5.35}$$
$$H(X_1,\dots,X_n)\le El(X_1,\dots,X_n)<H(X_1,\dots,X_n)+1\tag{5.36}$$
Since the $X_i$ are i.i.d., $H(X_1,\dots,X_n)=nH(X)$. Dividing by $n$:
$$H(X)\le L_n<H(X)+\frac1n\tag{5.37}$$
So large blocks achieve expected length per symbol arbitrarily close to the entropy (p. 88).

**Non-i.i.d. case (p. 89).** The same argument gives (5.38), and dividing by $n$ gives (5.39):
$$\frac{H(X_1,\dots,X_n)}n\le L_n<\frac{H(X_1,\dots,X_n)}n+\frac1n.$$
If the process is stationary, $H(X_1,\dots,X_n)/n\to H(\mathcal X)$, the entropy rate.

**Theorem 5.4.2.** The minimum expected codeword length per symbol satisfies
$$\frac{H(X_1,\dots,X_n)}n\le L_n^*<\frac{H(X_1,\dots,X_n)}n+\frac1n\tag{5.40}$$
and, if $X_1,\dots,X_n$ is a stationary process, $L_n^*\to H(\mathcal X)$ \tag{5.41} (p. 89). This is another justification of entropy rate: the expected bits per symbol needed to describe the process.

*Intuition note.* Rounding up wastes less than one bit per codeword. Spreading that waste over $n$ symbols divides it by $n$, so long blocks make the waste negligible.

**Wrong distribution (p. 89).** Design the Shannon code $l(x)=\lceil\log\frac1{q(x)}\rceil$ for $q$, while the true pmf is $p$.

**Theorem 5.4.3.**
$$H(p)+D(p\|q)\le E_pl(X)<H(p)+D(p\|q)+1\tag{5.42}$$
*Proof of the upper bound (p. 90).*
$$E\,l(X)=\sum_xp(x)\Big\lceil\log\tfrac1{q(x)}\Big\rceil\tag{5.43}$$
$$<\sum_xp(x)\Big(\log\tfrac1{q(x)}+1\Big)\tag{5.44}$$
$$=\sum_xp(x)\log\frac{p(x)}{q(x)}\frac1{p(x)}+1\tag{5.45}$$
$$=\sum_xp(x)\log\frac{p(x)}{q(x)}+\sum_xp(x)\log\frac1{p(x)}+1\tag{5.46}$$
$$=D(p\|q)+H(p)+1\tag{5.47}$$
The lower bound "can be derived similarly". So $D(p\|q)$ is the penalty in average description length for using the wrong distribution (p. 90).

### 5.5 Kraft inequality for uniquely decodable codes (pp. 90–92)
UD codes are a larger class than prefix codes. One might expect shorter lengths, but this section shows otherwise (p. 90).

**Theorem 5.5.1 (McMillan; Karush's proof).** The lengths of any uniquely decodable code satisfy $\sum D^{-l_i}\le1$ \tag{5.48}. Conversely, lengths satisfying it admit a uniquely decodable code (p. 90).

*Proof (pp. 90–92).*
1. Take the $k$th extension $C^k$. By unique decodability it is non-singular, so the number of code sequences of length $n$ is at most $D^n$.
2. The extension's length is $l(x_1,\dots,x_k)=\sum_{i=1}^kl(x_i)$ \tag{5.49}. To show $\sum_xD^{-l(x)}\le1$ \tag{5.50}, take the $k$th power:
$$\Big(\sum_xD^{-l(x)}\Big)^k=\sum_{x_1}\sum_{x_2}\cdots\sum_{x_k}D^{-l(x_1)}D^{-l(x_2)}\cdots D^{-l(x_k)}=\sum_{x^k\in\mathcal X^k}D^{-l(x^k)}\tag{5.51–5.53}$$
3. Group by length. With $l_{\max}$ the maximum codeword length and $a(m)$ the number of source sequences $x^k$ whose codeword has length $m$:
$$\sum_{x^k}D^{-l(x^k)}=\sum_{m=1}^{kl_{\max}}a(m)D^{-m}\tag{5.54}$$
4. By unique decodability, at most one source sequence maps to each code $m$-sequence, so $a(m)\le D^m$. Hence
$$\Big(\sum_xD^{-l(x)}\Big)^k=\sum_{m=1}^{kl_{\max}}a(m)D^{-m}\le\sum_{m=1}^{kl_{\max}}D^mD^{-m}=kl_{\max}\tag{5.55–5.57}$$
so $\sum_jD^{-l_j}\le(kl_{\max})^{1/k}$ \tag{5.58}.
5. This holds for all $k$. Since $(kl_{\max})^{1/k}\to1$, the Kraft inequality follows \tag{5.59}.
6. Converse: build the prefix code of Section 5.2; it is uniquely decodable.

**Corollary (infinite alphabet).** The proof breaks at (5.58), since $l_{\max}$ is infinite. The fix: every finite subset of a UD code is UD, so satisfies Kraft; take the limit: $\sum_{i=1}^\infty D^{-l_i}=\lim_{N\to\infty}\sum_{i=1}^ND^{-l_i}\le1$ \tag{5.60}. The converse uses the instantaneous code of the previous section (p. 92).

*Intuition note.* The set of achievable length lists is the same for UD codes and prefix codes. So the bounds on optimal length stay true over all UD codes, and prefix codes lose nothing (p. 92).

### 5.6 Huffman codes (pp. 92–94)
Huffman's simple algorithm gives an optimal prefix code; the proof is promised for Section 5.8 (pp. 92–94).

**Example 5.6.1** (binary). $X\in\{1,\dots,5\}$ with probabilities $0.25,0.25,0.2,0.15,0.15$. The two longest codewords must have equal length, since otherwise a bit could be deleted from the longer one. One can arrange that they differ only in the last bit. So combine symbols 4 and 5 into one symbol of probability 0.30, and continue merging the two least likely symbols. Codewords: $1\to01$, $2\to10$, $3\to11$, $4\to000$, $5\to001$. The average length is 2.3 bits (p. 93).

**Example 5.6.2** (ternary). Combine the three least likely symbols. Codewords: $1\to1$, $2\to2$, $3\to00$, $4\to01$, $5\to02$. The average length is 1.5 ternary digits (p. 93).

**Example 5.6.3** ($D\ge3$, dummy symbols). Each merge reduces the number of symbols by $D-1$. So the total number of symbols should be $1+k(D-1)$, with $k$ the number of levels. Add dummy symbols of probability 0 to reach this form. The printed ternary example has codewords $1,2,01,02,000,001,002$ and average length 1.7 ternary digits (p. 94).

### 5.7 Some comments on Huffman codes (pp. 94–97)
1. **Source coding = 20 questions (pp. 94–95).** A sequence of yes/no questions that identifies an object gives each object a distinct 0/1 answer string, i.e. a binary code. Its average length is the average number of questions. Conversely, a code gives questions: "Is the first bit of the codeword 1?" So the optimal questions follow the Huffman code. In Example 5.6.1 the first question is "Is $X$ equal to 2 or 3?" and the next "Is $X$ equal to 3?". The second question can also be asked without waiting, as "Is $X$ equal to 1 or 3?". The expected number of questions satisfies
$$H(X)\le EQ<H(X)+1.\tag{5.61}$$
2. **Weighted codewords (p. 95).** Huffman's algorithm works for any numbers $p_i\ge0$, whatever $\sum p_i$. It then minimizes $\sum w_il_i$. Example 5.7.1 (table garbled in the source text) states a minimum weighted sum of 36.
3. **"Slice" questions (pp. 95–96).** Huffman codes ask arbitrary questions "Is $X\in A$?". Suppose symbols are ordered $p_1\ge\dots\ge p_m$ and only questions "Is $X>a$?" are allowed. The Huffman code may not be a slice code. Take its lengths ($l_1\le\dots\le l_m$ by Lemma 5.8.1), assign symbols to first available nodes at those levels, and the result is an optimal slice code (an *alphabetic code*). Example 5.7.2: lengths $\{2,2,2,3,3\}$ give $1\to00,\ 2\to01,\ 3\to10,\ 4\to110,\ 5\to111$.
4. **Huffman vs Shannon codes (pp. 96–97).**
   - For probabilities 0.9999 and 0.0001, Shannon lengths are 1 and 14 bits; the optimal length is 1 bit for both.
   - Example 5.7.3 is a four-symbol distribution that the text layer prints illegibly. We read it as $(1/3,1/3,1/4,1/12)$, which fits the printed lengths. Huffman gives lengths $(2,2,2,2)$ or $(1,2,3,3)$, with the same expected length. In the second code the third symbol has length 3, above its Shannon length $\lceil\log\frac1{p_3}\rceil$. So Shannon can beat Huffman on a single symbol, and optimal length sets are not unique.
   - Huffman is shorter on average. Both lie in $[H,H+1)$, so they differ by less than one bit in expected length.
5. **Fano codes (p. 97).** Order probabilities decreasingly. Choose $k$ minimizing $\left|\sum_{i=1}^kp_i-\sum_{i=k+1}^mp_i\right|$. Give the upper set first bit 0 and the lower set 1, and repeat recursively. This is not optimal in general but achieves $L(C)\le H(X)+2$ (reference [37] is cited).

### 5.8 Optimality of Huffman codes (pp. 97–100; the unit ends mid-proof)
The proof is by induction for the binary case. Many optimal codes exist (inverting all bits, or swapping two codewords of equal length, gives another). Assume $p_1\ge p_2\ge\dots\ge p_m$ (p. 97).

**Lemma 5.8.1.** For any distribution there exists an optimal instantaneous code with:
1. $p_j>p_k\Rightarrow l_j\le l_k$;
2. the two longest codewords have the same length;
3. the two longest codewords differ only in the last bit and belong to the two least likely symbols (p. 97).

*Proof (pp. 97–99; Figure 5.3 shows swap, trim, rearrange).*
- *Property 1 (swap).* Let $C_m'$ be an optimal code $C_m$ with codewords $j$ and $k$ interchanged. Then
$$L(C_m')-L(C_m)=\sum p_il_i'-\sum p_il_i\tag{5.62}$$
$$=p_jl_k+p_kl_j-p_jl_j-p_kl_k\tag{5.63}$$
$$=(p_j-p_k)(l_k-l_j)\tag{5.64}$$
If $p_j>p_k$ and $C_m$ is optimal, this is $\ge0$, so $l_k\ge l_j$ (p. 98).
- *Property 2 (trim).* If the two longest codewords differed in length, deleting the last bit of the longer one keeps the prefix property and lowers $L$. By property 1 the longest codewords belong to the least probable symbols (pp. 98–99).
- *Property 3.* A longest codeword without a sibling could lose its last bit, lowering the average length. That contradicts optimality, so every longest codeword in an optimal code has a sibling. Exchanging longest codewords puts the two least likely symbols on sibling nodes without changing $\sum p_il_i$ (p. 99).
- Summary: an optimal code exists with $l_1\le l_2\le\dots\le l_{m-1}=l_m$ and $C(x_{m-1}),C(x_m)$ differing only in the last bit (p. 99).

**Merged code (pp. 99–100).** For a code $C_m$ with these properties, define $C_{m-1}$ on $m-1$ symbols. Take the common prefix of the two longest codewords and give it to a symbol of probability $p_{m-1}+p_m$. All other codewords are unchanged: $w_{m-1}=w'_{m-1}0$, $w_m=w'_{m-1}1$, and $l_{m-1}=l_m=l'_{m-1}+1$ \tag{5.65}. Then
$$L(C_m)=\sum_{i=1}^mp_il_i\tag{5.66}$$
$$=\sum_{i=1}^{m-2}p_il_i'+p_{m-1}(l_{m-1}'+1)+p_m(l_{m-1}'+1)\tag{5.67}$$
$$=\sum_{i=1}^{m-1}p_il_i'+p_{m-1}+p_m\tag{5.68}$$
$$=L(C_{m-1})+p_{m-1}+p_m\tag{5.69}$$
The two lengths differ by an amount independent of $C_{m-1}$, so minimizing $L(C_m)$ is equivalent to minimizing $L(C_{m-1})$. The problem is reduced to $m-1$ symbols with masses $(p_1,\dots,p_{m-2},p_{m-1}+p_m)$ (Figure 5.4). Repeating (reordering, applying the lemma, merging) reduces it to two symbols, where the solution is 0 and 1. The text then begins "Since we have maintained optimality at…" and the page ends. The conclusion is not in these pages (p. 100).

*Intuition note.* In an optimal tree the two rarest symbols can be assumed to be siblings at the bottom. Merging them into one symbol costs a fixed extra $p_{m-1}+p_m$, whatever the rest of the tree looks like. So solving the smaller problem optimally solves the bigger one.

## Toy example (ours, not from the text)
Take $p=(0.4,0.3,0.2,0.1)$, binary ($D=2$).
- Entropy: $0.4(1.3219)+0.3(1.7370)+0.2(2.3219)+0.1(3.3219)=0.5288+0.5211+0.4644+0.3322=1.846$ bits.
- Shannon lengths $\lceil\log_2(1/p_i)\rceil$: $\lceil1.32\rceil=2$, $\lceil1.74\rceil=2$, $\lceil2.32\rceil=3$, $\lceil3.32\rceil=4$. Kraft sum $=1/4+1/4+1/8+1/16=0.6875\le1$. $L=0.8+0.6+0.6+0.4=2.4$. Check (5.32): $1.846\le2.4<2.846$.
- Huffman: merge $0.2+0.1=0.3$. Then merge $0.3$ with $0.3$, giving $0.6$, and finally $0.4+0.6=1$. Lengths $(1,2,3,3)$; Kraft sum $=1/2+1/4+1/8+1/8=1$. $L=0.4+0.6+0.6+0.3=1.9$, within $[1.846,\,2.846)$. Symbol 4 gets 3 bits instead of Shannon's 4.
- Wrong distribution $q=(1/4,1/4,1/4,1/4)$: Shannon lengths are all 2, so $E_pl=2$. $D(p\|q)=\log_24-H(p)=2-1.846=0.154$. So $H(p)+D(p\|q)=2$, and (5.42) reads $2\le2<3$.

## Concepts
- [[prefix-code-kraft-inequality]] — prefix codes (no codeword is a prefix of another) exist for lengths $l_i$ iff $\sum D^{-l_i}\le1$ (pp. 81–83)
- [[source-code]] (new) — mapping from $\mathcal X$ to finite D-ary strings, with expected length $L(C)=\sum p(x)l(x)$ (p. 79)
- [[uniquely-decodable-code]] (new) — code whose extension is non-singular; same Kraft constraint as prefix codes (McMillan) (pp. 80, 90)
- [[d-adic-distribution]] (new) — all probabilities are powers $D^{-n}$; exactly the case where $L=H_D$ is achievable (p. 86)
- [[entropy]] — the lower bound $H_D(X)$ on expected length of instantaneous codes (p. 86)
- [[source-coding-theorem]] — here: $H\le L^*<H+1$, and $L_n\to H$ by block coding (pp. 87–89)
- [[entropy-rate]] — limit of $H(X_1,\dots,X_n)/n$ for a stationary process; the achievable bits per symbol (p. 89)
- [[relative-entropy-kl-divergence]] — $D(p\|q)$, the extra expected length when coding $p$ with a code for $q$ (pp. 89–90)
- [[huffman-arithmetic-coding]] — Huffman: repeatedly merge the two least probable symbols; optimal prefix code (pp. 92–94)
- [[shannon-code]] (new) — lengths $\lceil\log_D 1/p_i\rceil$; within one symbol of $H$, but can be much worse for single symbols (pp. 87, 96)
- [[twenty-questions-equivalence]] (new) — a questioning strategy equals a binary code; $H\le EQ<H+1$ (pp. 94–95)

## Canonical instances
- [[morse-code]] — short codewords for frequent letters in practice (p. 80)
- [[example-5-1-1-dyadic-code]] — $p=(1/2,1/4,1/8,1/8)$, $L=H=1.75$ bits (p. 79)
- [[example-5-6-1-huffman-five-symbols]] — Huffman code, $L=2.3$ bits (p. 93)
- [[shannon-vs-huffman-0.9999]] — Shannon code gives 14 bits to a symbol of probability 0.0001 (p. 96)

## Bridges (candidates)
- [structural-analogy] Kraft sum $\sum D^{-l_i}\le1$ ↔ probability theory: the numbers $D^{-l_i}$ behave like a (sub-)probability mass function.
- [structural-analogy] Theorem 5.4.3 penalty $D(p\|q)$ ↔ machine learning: log-loss of a model $q$ on data from $p$ (cross-entropy minus entropy; the ceiling aside).
- [structural-analogy] 20 questions / Huffman code ↔ decision trees: each yes/no split is one bit of a binary code.
- [metaphor] Merging the two least likely symbols ↔ greedy algorithms: the optimality proof gives an exchange-and-reduce argument.

## Questions this raises
- How does the induction in 5.8 finish, and what do the competitive-optimality and random-number-generation results announced on p. 78 add?
- Block coding makes $L_n\to H$, but what is the cost in code-table size and delay?
- If $q$ is only estimated from data, how large is the expected extra length $D(p\|q)$?
- Which cost functions beyond the weighted sum $\sum w_il_i$ of 5.7 can the Huffman merging idea handle?

## Reading notes
- **Part boundaries.** This part starts at printed p. 78 (chapter opening) and ends on p. 100, in the middle of the proof of Huffman optimality (Section 5.8). The final theorem statement for Huffman optimality is not here. The introduction also announces competitive optimality and random-number generation; they do not appear in these pages. The chapter's end-of-chapter problems (e.g. Problem 24) are not in these pages, so no exercises section is given.
- **Edition.** The pages are the 1991 first edition (copyright line on the chapter's opening page "Copyright 1991 John Wiley & Sons, Inc."), not the 2006 edition named in the metadata.
- **Page numbers.** Printed page = pdf − 22 for the labelled pages here (pdf 100 → printed 78).
- **OCR problems.** The text layer renders "5.x" example numbers as "6.x" in places and garbles many equations. Equations on pdf 101, 103–113, 120–122 were checked against page images. Pdf 100, 102 and 114–119 had no page images: Examples 5.1.3–5.1.4 (pdf 102), the Corollary on p. 92 (pdf 114), Examples 5.6.1–5.7.3, Fano codes and the start of Section 5.8 (pdf 119) rely on the text layer only. The probability tables for Examples 5.6.3 and 5.7.1 are not recoverable. The distribution of Example 5.7.3 is our reading from the lengths.
- **Possible misprints.**
  - Example 5.1.2 gives average length 1.66 bits; the arithmetic is $5/3\approx1.67$ (truncated).
  - In the converse of Theorem 5.2.2 the page image shows the reordering "$l_1\ge l_2\ge\dots$"; for an infinite code increasing order seems intended. This is our observation.
  - The displayed equation in the definition of the extension of a code (p. 80, presumably numbered (5.5)) is missing from the text layer, and pdf 102 had no page image.
