---
id: mackay-2003-information/ch05-symbol
work: mackay-2003-information
unit: "5 Symbol Codes"
pages: 90-108
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Symbol Codes

## L0 — One line
A lossless code that gives each symbol its own binary codeword must obey a length budget (the Kraft inequality), so its expected length cannot be below the entropy $H(X)$. A prefix code with expected length below $H(X)+1$ exists, and Huffman's algorithm finds an optimal one.

## L1 — The gist (≤ 120 words)
Chapter 4 showed that compression to about $H$ bits per symbol is possible with huge blocks. It gave no practical method. This chapter asks how well a lossless code can do when it encodes one symbol at a time with variable-length codewords. The codeword lengths of a uniquely decodeable code must satisfy $\sum_i 2^{-l_i}\le 1$. Hence the expected length is at least $H(X)$, with equality only if $l_i=\log_2(1/p_i)$. A prefix code with expected length below $H(X)+1$ exists. Huffman's algorithm builds an optimal symbol code. Its drawback is the possible "extra bit" per symbol, which matters when $H$ is small. Arithmetic coding, in the next chapter, removes it.

**Prerequisites:** logarithms and powers of 2; entropy $H(X)=\sum p\log_2(1/p)$ and Shannon information content; relative entropy and Gibbs' inequality; binary trees; geometric growth beats polynomial growth.

## L2 — Key ideas
- A symbol code maps each source symbol to a binary codeword. A prefix code (no codeword is a prefix of another) can be decoded left to right without lookahead, and it is uniquely decodeable (different source strings never share an encoding) (pp. 92–93).
- Codeword lengths work like a budget: a codeword of length $l$ costs $2^{-l}$ and the total available is 1. Every uniquely decodeable code satisfies $\sum_i 2^{-l_i}\le 1$ (Kraft inequality) (pp. 94–95).
- Conversely, any lengths satisfying Kraft are realized by a prefix code. So restricting attention to prefix codes loses nothing in expected length (p. 95).
- The expected length of a uniquely decodeable code is at least $H(X)$. Equality needs $l_i=\log_2(1/p_i)$ and $z=1$, where $z=\sum_i2^{-l_i}$ (p. 97).
- Choosing $l_i=\lceil\log_2(1/p_i)\rceil$ gives a prefix code with $H\le L<H+1$ (Theorem 5.1) (p. 98).
- Codelengths define implicit probabilities $q_i=2^{-l_i}/z$. Using the wrong lengths costs exactly $D_{\mathrm{KL}}(p\|q)$ extra bits per symbol for a complete code (one whose Kraft sum is exactly 1) (p. 98).
- Huffman's algorithm repeatedly merges the two least probable symbols. It is optimal among symbol codes; top-down bisection into near-equiprobable halves is not always optimal (pp. 99–100, 105–106).
- Huffman codes do not handle changing probabilities elegantly, and their overhead above $H$ is between 0 and 1 bit per symbol. That is serious when entropy is about one bit per symbol or less (p. 101).

## L3 — Walkthrough

### About Chapter 5 and the chapter introduction (pp. 90–91)
Chapter 4 proved that $N$ i.i.d. variables can be encoded into about $N(H(X)+\epsilon)$ bits with vanishing error probability. Encoding into $N(H(X)-\epsilon)$ bits makes the error probability virtually 1. That block scheme was lossy and impractical (p. 90).

Chapters 5 and 6 study practical schemes. The water-filled rubber glove is the author's picture: if some codewords get shorter, others must get longer when the scheme is not lossy (p. 90).

Interval notation: $x\in[1,2)$ means $x\ge1$ and $x<2$ (p. 90).

Chapter 5 studies variable-length *symbol codes*, which encode one symbol at a time (p. 91).
- They are lossless, so they decode without error. But they may sometimes produce an encoded string longer than the source string (p. 91).
- Compression is achieved on average: probable outcomes get short codewords, improbable ones get long codewords (p. 91).
- Three issues: what losslessness implies for lengths; how to make decoding easy; what the optimal codelengths and best compression are (p. 91).
- Announced result: there exists a code with $L(C,X)\in[H(X),H(X)+1)$. The average length equals $H(X)$ only if each codelength equals the Shannon information content (p. 91).

Notation: $\mathcal A^N$ is the set of length-$N$ strings over $\mathcal A$, and $\mathcal A^+$ is the set of all finite-length strings. Example 5.1: $\{0,1\}^3=\{000,\dots,111\}$. Example 5.2: $\{0,1\}^+=\{0,1,00,01,\dots\}$ (p. 91).

### 5.1 Symbol codes (pp. 92–94)
**Definitions.**
- A binary symbol code $C$ for ensemble $X$ maps $\mathcal A_X=\{a_1,\dots,a_I\}$ to $\{0,1\}^+$. $c(x)$ is the codeword, $l(x)$ its length, $l_i=l(a_i)$ (p. 92).
- The extended code $C^+$ concatenates codewords without punctuation (p. 92):
$$c^+(x_1x_2\ldots x_N)=c(x_1)c(x_2)\ldots c(x_N).\tag{5.1}$$

**Example 5.3.** $\mathcal A_X=\{a,b,c,d\}$, $\mathcal P_X=\{1/2,1/4,1/8,1/8\}$ (5.2). Code $C_0$ uses $a{=}1000$, $b{=}0100$, $c{=}0010$, $d{=}0001$. Then $c^+(\texttt{acdbac})=100000100001010010000010$ (5.3) (p. 92).

Three requirements for a useful code (p. 92):
1. Unique decoding.
2. Easy decoding.
3. As much compression as possible.

**Unique decodeability.** $C$ is uniquely decodeable if no two distinct strings have the same encoding (p. 92):
$$\forall\,\mathbf x,\mathbf y\in\mathcal A_X^+,\ \mathbf x\ne\mathbf y\Rightarrow c^+(\mathbf x)\ne c^+(\mathbf y).\tag{5.4}$$
$C_0$ is an example (p. 92).

**Easy decoding.** A code is easiest to decode if the end of a codeword is identifiable as soon as it arrives. That means no codeword is a prefix of another. A word $c$ is a prefix of $d$ if $ct=d$ for some tail string $t$ (p. 92).
- A *prefix code* has no codeword that is a prefix of another. It is also called instantaneous or self-punctuating, because decoding runs left to right without lookahead. A prefix code is uniquely decodeable (p. 92).
- Prefix codes correspond to binary trees. Complete prefix codes correspond to trees with no unused branches (pp. 92–93).
- The author says it will be shown later that nothing is lost by restricting to prefix codes (p. 92).

**Examples 5.4–5.7** (p. 93):
- $C_1=\{0,101\}$ is a prefix code. It is incomplete.
- $C_2=\{1,101\}$ is not a prefix code, since 1 is a prefix of 101.
- $C_3=\{0,10,110,111\}$ and $C_4=\{00,01,10,11\}$ are prefix codes.
- Example 5.9: any weighing strategy for the 24-state odd-ball problem can be viewed as a ternary prefix code.

**Compression.** The expected length is
$$L(C,X)=\sum_{x\in\mathcal A_X}P(x)\,l(x)=\sum_{i=1}^I p_il_i.\tag{5.5, 5.6}$$

Examples with $\mathcal P_X=\{1/2,1/4,1/8,1/8\}$ (p. 93):

| Code | Codewords $(a,b,c,d)$ | $L$ | Comment |
|---|---|---|---|
| $C_3$ | $0,10,110,111$ | 1.75 bits | $=H(X)=1.75$ bits; $l_i=\log_2(1/p_i)$. $c^+(\texttt{acdbac})=0110111100110$ |
| $C_4$ | $00,01,10,11$ | 2 bits | fixed length |
| $C_5$ | $0,1,00,11$ | 1.25 bits | below $H(X)$, but not uniquely decodeable: $\texttt{acdbac}\to000111000$, which also decodes as $\texttt{cabdca}$ |
| $C_6$ | $0,01,011,111$ | 1.75 bits | not a prefix code, since $c(a)=0$ is a prefix of $c(b)$ and $c(c)$. $c^+(\texttt{acdbac})=0011111010011$ |

**Is $C_6$ uniquely decodeable?** Yes, though it is hard to decode. After receiving "00", $\mathbf x$ could start $aa$, $ab$ or $ac$. After "001111" the second symbol is still ambiguous ($abd\ldots$ or $acd\ldots$). A unique decoding crystallizes when the next 0 arrives (p. 94).
- Its codewords are the reverses of $C_3$'s.
- Any $C_6$ string is a $C_3$ string read backwards, so the unique decodeability of $C_3$ proves it for $C_6$ (p. 94).

### 5.2 What limit is imposed by unique decodeability? (pp. 94–97)
**Question.** Given positive integers $\{l_i\}$, is there a uniquely decodeable code with these lengths? Probabilities are ignored for now (p. 94).

**Budget idea.**
- Shortening a codeword of $\{00,01,10,11\}$ (e.g. $00\to0$) retains unique decodeability only if other codewords are lengthened (p. 94).
- With only length-3 codewords one can have $2^3=8$ codewords. With a codeword "0" and the rest of length 3, a prefix code allows only four: $\{100,101,110,111\}$. The author "intuitively" thinks other codes cannot do better (p. 94).
- So a codeword of length $l$ costs $2^{-l}$, from a total budget of 1 (length 3 costs 1/8, length 1 costs 1/2) (p. 94). Going over budget means the code is certainly not uniquely decodeable. If the sum is $\le1$, then the code *may* be uniquely decodeable (p. 94).

**Kraft inequality.** For any uniquely decodeable binary code, with $I=|\mathcal A_X|$ (p. 95),
$$\sum_{i=1}^I 2^{-l_i}\le 1.\tag{5.9}$$
- A uniquely decodeable code satisfying this with equality is called *complete* (p. 95).
- *Kraft inequality and prefix codes:* given lengths satisfying the inequality, there exists a uniquely decodeable prefix code with those lengths (p. 95).
- Historical note: Kraft proved that if the inequality holds, a prefix code exists. McMillan (1956) proved the converse: unique decodeability implies the inequality (p. 95).
- Consequence: for any source there is an optimal symbol code that is a prefix code (p. 95).

**Proof of the inequality** (p. 95). Let $S=\sum_i2^{-l_i}$. Then
$$S^N=\Big[\sum_i2^{-l_i}\Big]^N=\sum_{i_1=1}^I\sum_{i_2=1}^I\cdots\sum_{i_N=1}^I2^{-(l_{i_1}+l_{i_2}+\cdots+l_{i_N})}.\tag{5.10}$$
- The exponent is the encoded length of the string $\mathbf x=a_{i_1}\cdots a_{i_N}$. There is one term per string of length $N$.
- Let $A_l$ be the number of strings $\mathbf x$ with encoded length $l$, and $l_{\min}=\min_il_i$, $l_{\max}=\max_il_i$. Then
$$S^N=\sum_{l=Nl_{\min}}^{Nl_{\max}}2^{-l}A_l.\tag{5.11}$$
- If $C$ is uniquely decodeable, the strings with encoded length $l$ have distinct encodings among the $2^l$ bit strings of length $l$, so $A_l\le2^l$. Then
$$S^N=\sum_{l=Nl_{\min}}^{Nl_{\max}}2^{-l}A_l\le\sum_{l=Nl_{\min}}^{Nl_{\max}}1\le Nl_{\max}.\tag{5.12}$$
- So $S^N\le l_{\max}N$ for every $N$. If $S>1$, $S^N$ would grow exponentially and eventually exceed the polynomial $l_{\max}N$. Hence $S\le1$. $\square$

*Intuition note.* Each codeword uses up a share $2^{-l}$ of a fixed supply, so a short codeword is expensive. If the shares add to more than 1, then for long enough source strings (as in the proof) some encoded length would need more strings than there are bit strings of that length, so two source strings would have to share an encoding.

**Exercise 5.14** asks for the converse (prefix code exists if Kraft holds). The "codeword supermarket" (figure 5.1) helps: each box's area is its cost $2^{-l}$ and the budget is 1 (p. 97).
- In figure 5.2, the prefix codes $C_0,C_3,C_4$ have no selected codewords to the right of any selected codeword, because prefix codes correspond to trees (p. 97).
- Probabilities now come back in. Shortening some codewords lengthens others by Kraft, so assigning lengths is not obvious (p. 97).

### 5.3 What's the most compression that we can hope for? (p. 97)
**Lower bound.** The expected length $L(C,X)=\sum_ip_il_i$ (5.13) of a uniquely decodeable code is bounded below by $H(X)$.

*Proof.* Define implicit probabilities $q_i\equiv2^{-l_i}/z$ with $z=\sum_{i'}2^{-l_{i'}}$, so $l_i=\log1/q_i-\log z$. Use Gibbs' inequality, $\sum_ip_i\log1/q_i\ge\sum_ip_i\log1/p_i$ (equality if $q_i=p_i$), and Kraft, $z\le1$ (so $-\log z\ge0$):
$$L(C,X)=\sum_ip_il_i=\sum_ip_i\log1/q_i-\log z\tag{5.14}$$
$$\ge\sum_ip_i\log1/p_i-\log z\tag{5.15}$$
$$\ge H(X).\tag{5.16}$$
Equality $L=H$ is achieved only if $z=1$ and $l_i=\log(1/p_i)$. $\square$

**Optimal source codelengths.** The expected length is minimized and equals $H(X)$ only if
$$l_i=\log_2(1/p_i).\tag{5.17}$$
**Implicit probabilities.** Conversely, any lengths $\{l_i\}$ define a distribution
$$q_i\equiv2^{-l_i}/z,\tag{5.18}$$
for which those lengths would be optimal. For a complete code $z=1$ and $q_i=2^{-l_i}$ (p. 97).

*Intuition note.* Any set of lengths defines implicit probabilities $q_i=2^{-l_i}/z$. The expected length reaches $H(X)$ only when these implicit probabilities match the true probabilities, so $l_i=\log_2(1/p_i)$ (p. 97).

### 5.4 How much can we compress? (p. 98)
**Theorem 5.1 (source coding theorem for symbol codes).** For an ensemble $X$ there exists a prefix code $C$ with
$$H(X)\le L(C,X)<H(X)+1.\tag{5.19}$$

*Proof.* Set $l_i=\lceil\log_2(1/p_i)\rceil$ (5.20), where $\lceil l^*\rceil$ is the smallest integer $\ge l^*$. The author notes that he is not asserting that the optimal code necessarily uses these lengths; he chooses them because they prove the theorem.
- Kraft check:
$$\sum_i2^{-l_i}=\sum_i2^{-\lceil\log_2(1/p_i)\rceil}\le\sum_i2^{-\log_2(1/p_i)}=\sum_ip_i=1.\tag{5.21}$$
- So a prefix code with these lengths exists. Its expected length is
$$L(C,X)=\sum_ip_i\lceil\log(1/p_i)\rceil<\sum_ip_i(\log(1/p_i)+1)=H(X)+1.\tag{5.22}$$
The lower bound is from section 5.3. $\square$

*Intuition note.* Rounding each ideal length up to a whole number of bits wastes less than one bit per symbol. Rounding up also keeps the Kraft sum at most 1, so the rounded lengths still form a valid prefix code.

**The cost of using the wrong codelengths.** If the true probabilities are $\{p_i\}$ and we use a complete code with lengths $l_i$, then $q_i=2^{-l_i}$. Continuing from (5.14) with $z=1$ (the author's step),
$$L(C,X)=H(X)+\sum_ip_i\log p_i/q_i,\tag{5.23}$$
so the length exceeds the entropy by the relative entropy $D_{\mathrm{KL}}(\mathbf p\|\mathbf q)$ (p. 98).

Figure 5.3 gives English letter probabilities (27 symbols, including the space "–" at 0.1928) as an ensemble in need of a code (p. 98).

### 5.5 Optimal source coding with symbol codes: Huffman coding (pp. 98–100)
**How not to do it.** Roughly splitting $\mathcal A_X$ in two and bisecting the subsets, to build a binary tree from the root, has "the right spirit" but is not necessarily optimal. It achieves $L(C,X)\le H(X)+2$ (p. 98).

**Algorithm 5.4 (Huffman).** Build the tree from its leaves, constructing the code backwards (p. 99).
1. Take the two least probable symbols. They get the longest codewords, of equal length, differing only in the last digit.
2. Combine them into a single symbol and repeat.

After $|\mathcal A_X|-1$ steps all symbols have strings. If there is a tie when choosing the two least probable, the choice may be made in any manner; the expected length will not depend on it (p. 99).

**Example 5.15.** $\mathcal P=\{0.25,0.25,0.2,0.15,0.15\}$ for $a,\dots,e$ (p. 99).
- Merge $d,e$ into 0.3. Then merge $b,c$ into 0.45. Then merge $a$ with $de$ into 0.55. Finally merge 0.55 and 0.45.
- Codewords: $C=\{00,10,11,010,011\}$, lengths $2,2,2,3,3$.
- Ideal lengths $\log_2 1/p_i$: $2.0,2.0,2.3,2.7,2.7$. Huffman lengths are sometimes longer, sometimes shorter.
- $L=2.30$ bits; $H=2.2855$ bits.

**Example 5.17.** Huffman code for the English ensemble of figure 2.1 (figure 5.6, p. 100): $L=4.15$ bits, $H=4.11$ bits. Assigned and ideal lengths differ, e.g. $j$ has ideal 10.7 and length 10; $q$ has ideal 10.3 and length 9 (pp. 99–100).

*Intuition note.* The two least probable symbols get the longest codewords, of equal length, differing only in the last digit. So they are merged first, and the tree is built from its leaves (p. 99).

**Top-down is suboptimal.** Balanced trees explained entropy in the weighing problems of earlier chapters. But optimal codes cannot always be built by greedy top-down splitting into near-equiprobable subsets (p. 100).

**Example 5.18.** $\mathcal P=\{0.01,0.24,0.05,0.20,0.47,0.01,0.02\}$ for $a,\dots,g$ (5.24). Greedy: $\{a,b,c,d\}$ and $\{e,f,g\}$ both have probability 1/2, then $\{a,b\}$ and $\{c,d\}$ have 1/4 each (p. 100).
- Greedy code expected length: 2.53.
- Huffman code expected length: 1.97 (lengths $a{:}6,b{:}2,c{:}4,d{:}3,e{:}1,f{:}6,g{:}5$).

Exercise 5.16 asks for a proof that no symbol code beats Huffman; the solution is in 5.9 (p. 99).

### 5.6 Disadvantages of the Huffman code (pp. 100–101)
Huffman is optimal among symbol codes, but "ensemble" and "symbol code" both need attention (p. 100).

**Changing ensemble.** For text, symbol frequencies vary with context: $u$ is much more probable after $q$ than after $e$. Knowledge of the frequencies also changes as we learn the source (p. 101).
- Huffman codes do not handle this elegantly.
- One approach recomputes the code whenever probabilities change.
- Another computes a fixed distribution in advance and must also transmit the code. This is cumbersome, restrictive and suboptimal, since the code description and the document are partially redundant, so it wastes bits (p. 101).

**The extra bit.** Huffman satisfies $H\le L<H+1$, an overhead of between 0 and 1 bit per symbol. If $H$ is large, this is a small fractional increase. But when entropy is about one bit per symbol or lower, the overhead may dominate the file length (p. 101).
- Example: in the context "strings_of_ch", the next nine symbols "aracters_" might each have probability 0.99. A traditional Huffman code would be obliged to use at least one bit per character, so nine bits, where only 0.13 bits in total are conveyed (p. 101).
- The entropy of English, given a good model, is about one bit per character (Shannon, 1948), so Huffman is likely highly inefficient there (p. 101).

**Block patch.** Applying Huffman to blocks ($X^N$, Chapter 4) makes overhead at most $1/N$ bit per symbol. The costs are (a) losing the elegant instantaneous decodeability of simple Huffman coding, and (b) computing probabilities of all relevant strings and building the tree. This means computing codes for a huge number of strings, most of which never occur (p. 101).

**Beyond symbol codes.** Huffman codes are optimal symbol codes, but for practical purposes "we don't want a symbol code". Arithmetic coding dispenses with the integer-bits-per-symbol restriction and is the topic of the next chapter (p. 101).

### 5.7 Summary (p. 102)
- Kraft: uniquely decodeable implies $\sum_i2^{-l_i}\le1$ (5.25). Lengths satisfying it are realized by a prefix code.
- Optimal lengths are $l_i=\log_2(1/p_i)$ (5.26), and any lengths define $q_i=2^{-l_i}/z$ (5.27).
- $D_{\mathrm{KL}}(\mathbf p\|\mathbf q)$ is the number of bits per symbol wasted by using a code with implicit probabilities $\mathbf q$ when the true distribution is $\mathbf p$.
- Theorem 5.1 (5.28), and Huffman combines the two least probable symbols at each iteration.

### 5.8 Exercises (pp. 102–104)
The exercises are listed at the end. Content that bears on the chapter's ideas (pp. 103–104):
- Exercise 5.28 considers $I$ equiprobable symbols, $I$ not a power of 2. With $l^+\equiv\lceil\log_2I\rceil$ (5.30), the fraction of symbols with length $l^+$ is $f^+=2-2^{l^+}/I$ (5.31). The optimal expected length is $L=l^+-1+f^+$ (5.32). The excess $\Delta L\equiv L-H(X)$ is bounded: $\Delta L\le1-\frac{\ln(\ln2)}{\ln2}-\frac1{\ln2}=0.086$ (5.33).
- Exercise 5.30 (the poisoned glass) asks the reader to find the exact number of glasses (between 100 and 200). The reader should explain why the professor ("test one glass first") was wrong. The reader should also find the optimal procedure, the expected waste of the professor's strategy, and the link to symbol coding. No solution is printed.
- *Mixture codes.* A "metacode" picks, per symbol, whichever of several symbol codes gives the shortest codeword. The choice must be signalled, e.g. by a leading bit. The result is suboptimal because it is incomplete (fails Kraft equality) (p. 104). See Exercise 5.33 below.

### 5.9 Solutions (pp. 104–108)
**Exercise 5.8 (p. 104).** $C_2=\{1,101\}$ *is* uniquely decodeable even though it is not a prefix code. Only the codeword 101 contains a 0, so no two different strings give the same encoding.

**Exercise 5.14 (pp. 104–105): prefix code exists if Kraft holds.**
- Buy codewords in the supermarket one at a time, from shortest (biggest) to longest, starting at one side and advancing a distance $2^{-l}$ per purchase.
- Lengths are non-decreasing and intervals shrink, so an adjacent codeword can always be bought. No budget is wasted.
- After the $I$th codeword we have advanced $\sum_{i=1}^I2^{-l_i}$. If this is $\le1$, we never run out of budget.

**Exercise 5.16 (pp. 105–106): Huffman is optimal.** The key step is that the two least probable symbols may be given equal lengths. Proof by contradiction:
- Suppose $a,b$ (smallest probabilities) do not have equal lengths in any optimal code. Take an optimal rival code, wlog a complete prefix code (any uniquely decodeable lengths can be realized by a prefix code), with $l_a<l_b$.
- The codeword of $b$ must have an adjacent codeword of equal or greater length (a complete prefix code never has a solo codeword of maximum length). So some symbol $c$ has $p_c>p_a$ and rival length $l_c\ge l_b$.
- Exchange the codewords of $a$ and $c$ (figure 5.9). The change in expected length is $(p_a-p_c)(l_c-l_a)$. This is negative since $p_a-p_c<0$ and $l_c-l_a>0$ *(added step)*.
- So the rival was not optimal, which is a contradiction.

**Exercise 5.21 (p. 106): final results.**
- $\mathcal P_X=\{0.9,0.1\}$: $X^2$ code $\{00,01,10,11\}\to\{1,01,000,001\}$, $L=1.29$, $H(X^2)=0.938$. $X^3$: $L=1.598$, $H=1.4069$. $X^4$: $L=1.9702$, $H=1.876$.
- $\mathcal P_X=\{0.6,0.4\}$: $X^2$ lengths $\{2,2,2,2\}$, $L=2$, $H=1.94$. $X^4$ (table 5.10): $L=3.92$, $H=3.88$. Some strings with identical probabilities receive different codelengths.

**Exercise 5.22 (p. 106).** $\{1/6,1/6,1/3,1/3\}$ has two optimal length sets: $\{00,01,10,11\}$ or $\{000,001,01,1\}$ (at the second Huffman step any of three pairings can be chosen); both have $L=2$. Other examples: $\{1/5,1/5,1/5,2/5\}$ and $\{1/3,1/3,1/3,0\}$.

**Exercise 5.26–5.27 (p. 106).** With $p_{\max}$ the largest probability, the difference $L-H$ can be no bigger than $\max(p_{\max},0.086)$ (Gallager, 1978). For eleven equiprobable symbols the optimal code exceeds the entropy by 0.086 bits.

**Exercise 5.31 (pp. 106–107): probability that a random bit of the $C_3$-encoded stream is 1.** Three answers are given.
- *Erroneous:* $\sum_ip_if_i=\tfrac12\cdot0+\tfrac14\cdot\tfrac12+\tfrac18\cdot\tfrac23+\tfrac18\cdot1=1/3$ (5.34–5.35). This falls for the bus-stop fallacy: picking a random bit favours symbols with longer codewords ($c,d$ over $a$). The probabilities must be scaled by $l_i$ and renormalized.
- *Correct, same style:* the expected number of 1s per symbol is $\sum_ip_if_il_i$ (5.36) and the expected bits per symbol is $\sum_ip_il_i$ (5.37). Then
$$P(\text{bit is }1)=\frac{\sum_ip_if_il_i}{\sum_ip_il_i}=\frac{\tfrac12\cdot0+\tfrac14\cdot1+\tfrac18\cdot2+\tfrac18\cdot3}{7/4}=\frac{7/8}{7/4}=\tfrac12.\tag{5.38}$$
For a general symbol code and ensemble, (5.38) is the correct answer.
- *Information-theoretic:* $\mathbf c$ is the output of an optimal compressor, so we cannot expect to compress it any further. If $P(\text{bit is }1)\ne1/2$, a block code could compress it more. So the probability must be 1/2, and any $l$-bit sequence in the stream has probability $2^{-l}$. Equivalently, the information per bit would be at most $H_2(P(1))<1$, contradicting that the information per bit must be $H(X)/L(C,X)=1$.

**Exercise 5.32 (pp. 107–108): radix-$q$ Huffman.**
- Combining $q$ symbols into 1 reduces the count by $q-1$. Starting from $A$ symbols, one ends with a complete $q$-ary tree only if $A\bmod(q-1)=1$.
- Otherwise the tree has missing leaves (e.g. a ternary tree for eight symbols has one missing leaf). Optimal codes put the missing leaves in the longest branch.
- This is done by adding zero-probability symbols so that the total number of leaves is $r(q-1)+1$ for some integer $r$. Then combine the $q$ least probable symbols repeatedly.

**Exercise 5.33 (p. 108): the greedy metacode is incomplete.** Suppose $K$ candidate codes with lengths $l_k(x)$ and a header of $\log K$ bits. The metacode lengths are
$$l'(x)=\log_2K+\min_kl_k(x).\tag{5.39}$$
The Kraft sum is
$$S=\sum_x2^{-l'(x)}=\frac1K\sum_x2^{-\min_kl_k(x)}.\tag{5.40}$$
- Split $\mathcal A_X$ into disjoint subsets $\mathcal A_k$ of the symbols sent via code $k$:
$$S=\frac1K\sum_k\sum_{x\in\mathcal A_k}2^{-l_k(x)}.\tag{5.41}$$
- If code $k$ satisfies Kraft equality over all of $\mathcal A_X$, then
$$\sum_{x\in\mathcal A_k}2^{-l_k(x)}\le1,\tag{5.42}$$
with equality only if all symbols lie in $\mathcal A_k$ (only one code used).
- So $S\le\frac1K\sum_{k=1}^K1=1$ (5.43), with equality only if (5.42) is an equality for all $k$. That is impossible with disjoint subsets, so $S<1$.
- Tree view for two codes: after the first bit selects code A, the continuation can only be a codeword of a symbol that is shorter under A than under B. Some strings are invalid continuations, so the code is incomplete and suboptimal.
- The author points to "bits back coding" (section 28.3; Frey, 1998) for further discussion. These pages do not explain it.

## Toy example (ours, not from the text)
Source $\mathcal P=\{a{:}0.4,\ b{:}0.3,\ c{:}0.2,\ d{:}0.1\}$.

**Huffman.**
1. Merge $c,d$: 0.3.
2. The list is $\{0.4,\,b{=}0.3,\,cd{=}0.3\}$. Merge $b$ and $cd$: 0.6.
3. Merge $a$ (0.4) and 0.6.

The lengths are $a{:}1,\ b{:}2,\ c{:}3,\ d{:}3$, e.g. $\{0,10,110,111\}$.
- $L=0.4(1)+0.3(2)+0.2(3)+0.1(3)=0.4+0.6+0.6+0.3=1.9$ bits.

**Entropy.**
- $H=0.4(1.3219)+0.3(1.7370)+0.2(2.3219)+0.1(3.3219)=0.5288+0.5211+0.4644+0.3322=1.8465$ bits.
- So $L-H=0.0535$, within $[0,1)$ as Theorem 5.1 says.

**Relative entropy check.** Lengths $1,2,3,3$ give $q=\{1/2,1/4,1/8,1/8\}$, with Kraft sum $1/2+1/4+1/8+1/8=1$ (complete).
- $D_{\mathrm{KL}}(p\|q)=0.4\log_2\frac{0.4}{0.5}+0.3\log_2\frac{0.3}{0.25}+0.2\log_2\frac{0.2}{0.125}+0.1\log_2\frac{0.1}{0.125}$.
- The terms are $0.4(-0.3219)=-0.1288$, $0.3(0.2630)=0.0789$, $0.2(0.6781)=0.1356$, $0.1(-0.3219)=-0.0322$.
- The sum is $0.0535$, which equals $L-H$ as in (5.23).

**Theorem 5.1's lengths.** $\lceil\log_2(1/p_i)\rceil=2,2,3,4$ (from $1.32,1.74,2.32,3.32$). The Kraft sum is $1/4+1/4+1/8+1/16=0.6875\le1$, so a prefix code exists. Its $L=0.8+0.6+0.6+0.4=2.4<H+1=2.8465$. This is valid but worse than Huffman's 1.9.

**Kraft violation.** Lengths $\{1,1,2\}$ give $0.5+0.5+0.25=1.25>1$, so no uniquely decodeable code has these lengths.

## Concepts
- [[symbol-code]] (new) — a mapping from each source symbol to a binary codeword; extended code concatenates codewords without punctuation (p. 92)
- [[uniquely-decodeable-code]] (new) — distinct source strings always have distinct encodings under $C^+$ (p. 92)
- [[prefix-code-and-kraft-inequality]] — prefix code: no codeword is a prefix of another. Uniquely decodeable codes satisfy $\sum2^{-l_i}\le1$, and any lengths satisfying it are realized by a prefix code (pp. 92, 95)
- [[complete-code]] (new) — a uniquely decodeable code satisfying Kraft with equality; a tree with no unused branches (pp. 93, 95)
- [[expected-code-length]] (new) — $L(C,X)=\sum p_il_i$; the quantity compression tries to minimize (p. 93)
- [[implicit-probabilities]] (new) — $q_i=2^{-l_i}/z$: the distribution for which given codelengths are optimal (p. 97)
- [[source-coding-theorem]] — here, for symbol codes: a prefix code with $H(X)\le L<H(X)+1$ exists (p. 98)
- [[entropy-h-x]] — lower bound on expected length of any uniquely decodeable code (p. 97)
- [[self-information-surprisal]] — Shannon information content $\log_2(1/p_i)$ equals the optimal codelength (p. 97)
- [[relative-entropy-kl-divergence]] — the excess of expected length over $H$ when a complete code with implicit $\mathbf q$ is used for true $\mathbf p$ (p. 98)
- [[huffman-arithmetic-coding]] — Huffman: optimal symbol code by merging the two least probable symbols; arithmetic coding is announced as the fix for its defects (pp. 99, 101)
- [[gibbs-inequality]] (new) — $\sum p_i\log1/q_i\ge\sum p_i\log1/p_i$, used in the lower-bound proof (p. 97)
- [[mixture-code]] (new) — metacode choosing the shortest of several codes plus a header; incomplete, hence suboptimal (p. 104)

## Canonical instances
- [[code-c0-c6-examples]] — $C_0$–$C_6$ on $\{1/2,1/4,1/8,1/8\}$: prefix vs non-prefix, $C_5$ not uniquely decodeable, $C_6$ uniquely decodeable but not a prefix code (pp. 92–94)
- [[huffman-example-5-15]] — five-symbol Huffman code with $L=2.30$, $H=2.2855$ (p. 99)
- [[huffman-english-letters]] — English monogram Huffman code: $L=4.15$, $H=4.11$ (p. 100)
- [[greedy-vs-huffman-example-5-18]] — top-down split gives 2.53 vs Huffman 1.97 (p. 100)
- [[strings-of-ch-extra-bit]] — nine highly predictable characters cost at least nine bits in Huffman, versus 0.13 bits of information (p. 101)
- [[random-bit-of-c3-stream]] — P(bit is 1) = 1/2; the bus-stop fallacy (pp. 106–107)

## Bridges (candidates)
- [same-math] Expected length with wrong lengths $=H(p)+D_{\mathrm{KL}}(p\|q)$ ↔ information-theory/bayesian: cross-entropy as log-loss of model $q$ on data from $p$ — same decomposition, with $-\log_2q_i$ as the codelength.
- [structural-analogy] Implicit probabilities $q_i=2^{-l_i}/z$ ↔ Bayesian: any code is an implicit probabilistic model, as a posterior or predictive distribution defines a code via $-\log p$.
- [structural-analogy] Mixture code with $\log K$-bit header and incompleteness ↔ Bayesian: model averaging over $K$ models with a uniform prior. The source only points to bits-back coding (p. 108), so the link is ours.
- [metaphor] Kraft "budget" of codeword costs ↔ economics: a fixed resource spent across items, where cheap items for some mean costly ones for others.

## Questions this raises
- How can arithmetic coding give fractional bits per symbol and handle a changing probability model, given that Huffman cannot?
- Block Huffman on $X^N$ gets overhead of at most $1/N$ bit per symbol. How does the codebook size grow, and when is that impractical (Exercise 5.29)?
- The solution to 5.26 cites a bound of $\max(p_{\max},0.086)$ for the Huffman excess. When is the excess close to this bound?
- Which interpretation of "the code defines a probability model" lets us use compression as a tool for inference or model comparison?

## Exercises worth doing
- Ex. 5.19 (p. 102) — decide unique decodeability of a binary code by hand; builds intuition beyond prefix codes — difficulty: medium
- Ex. 5.20 (p. 102) — the same for a ternary code — difficulty: medium
- Ex. 5.21 (p. 102) — Huffman codes for $X^2,X^3,X^4$ with skewed sources; shows how block length reduces the gap to entropy — difficulty: hard
- Ex. 5.25 (p. 103) — when all $p_i$ are integer powers of 2, a code with $L=H$ exists — difficulty: medium
- Ex. 5.28 (p. 103) — optimal code for $I$ equiprobable symbols; source of the 0.086 bound — difficulty: medium
- Ex. 5.30 (p. 103) — the poisoned glass puzzle linking optimal testing to symbol coding — difficulty: medium

## Reading notes
- Printed page = pdf page − 12 (pdf 102 = p. 90, …, pdf 120 = p. 108). All references use printed pages.
- Pages carry the Cambridge University Press 2003 on-screen-viewing header. The text layer garbles many math symbols (ceilings, ≠, equations such as 5.10–5.12 and 5.31), figure 5.2 and the Example 5.15 diagram, so I checked equations against the page images. I also checked figures 5.3 and 5.6 and tables 5.5, 5.7 and 5.10 against the images.
- The solution to Exercise 5.26 is given only as a bound from Gallager (1978) with no proof in these pages. Exercise 5.30 has no printed solution.
- Equation (5.31) $f^+=2-2^{l^+}/I$ and (5.33) were read from the image. $1-\frac{\ln\ln2}{\ln2}-\frac1{\ln2}\approx0.086$.
- Exercises are listed with the book's difficulty ratings and solution markers. I included printed solution content in L3 for 5.8, 5.14, 5.16, 5.21, 5.22, 5.26–5.27, 5.31–5.33 and omitted worked solutions for the exercises listed above.
