---
id: stone-2022-information/ch03-source
work: stone-2022-information
unit: "3 The Source Coding Theorem"
pages: 45–78
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# The Source Coding Theorem

## L0 — One line
A source with entropy H bits/symbol can be encoded so that, on average, each symbol needs only a little more than H binary digits, and not fewer, because in practice a source of n-digit binary messages produces only about $2^{nH}$ of its $2^n$ possible messages.

## L1 — The gist (≤ 120 words)
How can messages be encoded for a noiseless channel so that each binary digit carries as close to one bit as possible? Shannon's source coding theorem says one can come arbitrarily close to C/H symbols per second, but cannot exceed it, where C is the channel capacity and H the source entropy. Codes can approach this limit by coding blocks of symbols (die throws, English letters) and by giving frequent symbols short codewords (Huffman coding). The theorem also covers dependent sequences such as English, whose entropy is far below log 27 bits per letter. The reason it holds: long messages almost always fall into a small set of roughly equiprobable messages. Kolmogorov complexity is a related idea about compression.

**Prerequisites:** base-2 logarithms; entropy $H=\sum p\log(1/p)$; iid (independent, identically distributed) variables; conditional probability; binomial coefficients $n!/(n_1!\,n_0!)$.

## L2 — Key ideas (5–10 bullets)
- Natural signals are "dilute" because neighbouring values are related and because of how the values are distributed; efficient transmission is best done by making values independent and giving them a distribution suited to the channel (uniform, for a channel with fixed bounds) (p. 45).
- A noiseless channel's capacity equals the number of binary digits it passes per second. It is reached only if each digit carries one bit, which needs equiprobable, independent symbols (pp. 46–50).
- Source coding theorem: one can transmit at nearly C/H symbols/s, but never faster than C/H (p. 49).
- If symbols carry a non-integer number of bits, coding several symbols per codeword improves efficiency, e.g. 0.86 → 0.970 bits per binary digit for a 6-sided die (pp. 52–54).
- Huffman coding gives frequent symbols short codewords. It yields $H\le L<H+1$ and a prefix code, but assumes independent symbols (pp. 57–61).
- For dependent sequences, the block-entropy estimates $G_N$ fall as N grows and settle at the entropy once N reaches the correlation length; English comes out near 1.8 bits/letter (pp. 64–69).
- Why the theorem holds: long messages almost all contain about nP ones, so only about $2^{H}$ of the $2^n$ possible messages occur (the author writes $2^H$, with H the entropy of the whole n-digit message). For large n, Stirling's approximation gives $\log_2 m = nH$ with H per binary digit (pp. 71–76).
- Kolmogorov complexity (shortest program for an object) is a parallel notion of compression, but is non-computable (pp. 76–78).

## L3 — Walkthrough

### 3.1 Introduction (p. 45)
- Natural signals (sounds, images) carry information in a dilute form. Reason 1: nearby values are similar or related, so values partly duplicate each other. Reason 2 concerns the distribution of values: the best distribution depends on the channel's constraints (p. 45).
- Which distribution is best depends on the channel's constraints. For a channel with fixed lower and upper bounds, recoding an iid signal so all values are equally frequent (uniform) makes each binary digit carry one bit (p. 45).
- Efficient transmission therefore needs (1) a transformation to independent values and (2) a distribution optimised for that channel (p. 45).
- The theorem says such recoding is possible but not how to do it. Practical schemes close to Shannon's limits were found afterwards (p. 46). It applies also to structured sequences like English text (p. 46).

### 3.2 Capacity of a discrete noiseless channel (pp. 46–49)
- Capacity C is the maximum number of bits the channel can communicate, in bits/s or bits/symbol. Since one binary digit conveys at most one bit, a channel passing R binary digits per second has $C=R$ bits/s. If digits carry less than one bit each, the information rate is $R<C$ (pp. 46–47).
- Example: a symbol of eight binary digits, each carrying half a bit, sent unencoded ($x_i=s_i$) carries only $C/2$ bits per input. The theorem guarantees an encoding in which each input of C binary digits carries close to C bits on average (p. 47).
- Capacity is defined through the input distribution that maximises information per input (the author notes a uniform p(X) maximises H(X), without proof):
$$C=\max_{p(X)} H(X)\ \text{bits per input}\tag{3.1}$$
$$C=\max_{p(X)} H(X)\ \text{bits/s}\tag{3.2}$$
- The maximum number of symbols per second is
$$C/H(S)\ \text{symbols/s}\tag{3.3}$$
- Shannon's equivalent definition uses the number $N(t)$ of distinct encoded messages communicable in time t:
$$C=\lim_{t\to\infty}\frac{\log N(t)}{t}\ \text{bits/s}\tag{3.4}$$
  The limit is needed because some messages have very long codewords, which are averaged out over long times (p. 48).
- This counts messages that *could* be sent, not those actually sent. Example: choosing one word per second from about 1,000 words gives $\log 1000=9.96$ bits/s. That is reached only if all words are equally frequent and in random (iid) order. Unequal frequencies or predictable words (the "you" in "thank you") give a lower rate (p. 48).
- Check: nine binary digits per second give $2^{9t}$ possible messages in t seconds, so
$$C=\frac{\log 2^{9t}}{t}=9t/t=9\ \text{bits/s}\tag{3.5}$$
  (p. 49).
- **Intuition note:** Capacity measures how many different messages the channel could carry, not how many you actually use. Predictable or unevenly used symbols waste capacity.

### 3.3 Shannon's source coding theorem (pp. 49–50)
- **Shannon & Weaver (1949), quoted:** let a source have entropy H (bits/symbol) and a channel capacity C (bits/s). Then one can encode the source output so as to transmit at average rate $C/H-\epsilon$ symbols/s, with ε arbitrarily small. Transmitting at an average rate greater than $C/H$ symbols/s is not possible (p. 49; the symbol ε is lost in the text layer, so this is read from the author's explanation on p. 50).
- **Author's gloss:** messages from a source generating information at H bits/s can be encoded to be transmitted at a rate arbitrarily close to C, provided $H<C$. The author says this may seem circular to modern eyes familiar with computers, but in Shannon's day it was a revelation (p. 50).
- **Intuition note:** C/H is a speed limit. You can get arbitrarily close to it with a clever code but never beat it.

### 3.4 Calculating information rates (pp. 50–54)
- Full capacity is used only if each transmitted binary digit represents on average one bit (p. 50). Dice are used because they avoid the complications of non-iid variables (p. 50).
- **8-sided die.** The eight symbols are equiprobable and iid, so $H=3$ bits/symbol, and 3 binary digits suffice (Table 3.1: $s_1=1\to 000,\dots,s_8=8\to 111$, i.e. decimal minus one, in binary). With $C=3$ bits/s:
$$R=C/H=\frac{3\ \text{bits/s}}{3\ \text{bits/symbol}}=1\ \text{symbol/s}\tag{3.6–3.8}$$
  which is 3 bits/s, so this is an *efficient code* (p. 51).
- **Coding efficiency** is the entropy divided by the average codeword length L(X). Here
$$\frac{H(S)}{L(X)}=\frac{3}{3}=1\ \text{bit/binary digit}\tag{3.9–3.10}$$
  Efficiency ranges between 0 and 1 (p. 52).
- **6-sided die.** $H=\log 6=2.58$ bits/symbol (3.13–3.14). With $C=1$ bit/s, the best possible rate is
$$R=\frac{1\ \text{bit/s}}{2.58\ \text{bits/symbol}}\approx0.387\ \text{symbols/s}\tag{3.15–3.17}$$
  (p. 52).
- Simple code, 3 digits per symbol (first six rows of Table 3.1): efficiency $2.58/3=0.86$ bits/binary digit (3.18–3.19), so $R\approx0.333$ symbols/s (3.20–3.22). This is an inefficient code (p. 53).
- Better: code three throws at once. There are $6^3=216$ combinations; 8 binary digits give $2^8=256$ labels. That is $8/3\approx2.66$ digits/symbol, with efficiency $2.58/2.66=0.970$ bits/binary digit (3.23–3.24) and $R\approx0.376$ symbols/s (3.25–3.26), closer to 0.387 (pp. 53–54).
- **Key point (author):** if each independently chosen value represents a non-integer number of bits, an efficient encoding can be obtained by combining several symbols in one codeword (p. 54).
- **Intuition note:** Whole binary digits cannot be split, so a single die wastes the fraction 3 − 2.58. Packing several throws into one label spreads that waste over three symbols.

### 3.5 Data compression (pp. 54–57)
- Non-uniform distributions are where the ideas matter most. Take two dice and define the outcome as the sum: alphabet $A_s=\{2,\dots,12\}$, $m=11$ symbols (3.27–3.28). There are 36 equiprobable ordered pairs, so each sum has probability freq/36 (Table 3.2, Fig. 3.2b):
$$H(S)=\sum_{i=1}^{11}p(s_i)\log\frac1{p(s_i)}=3.27\ \text{bits/symbol}\tag{3.29–3.30}$$
- By the theorem one should be able to transmit with an average of no more than 3.27 binary digits/symbol (p. 56).
- A fixed-length code needs 4 digits (3 give only 8 labels, 4 give 16, so 5 codewords go unused): efficiency $3.27/4.00=0.818$ (3.31–3.32) (p. 56).
- Aside: 11 equiprobable outcomes would have entropy $\log 11=3.46$ bits (3.33). A single die with the same entropy as two dice would have
$$m=2^{H(S)}=2^{3.27}=9.65\ \text{equally probable values}\tag{3.34–3.36}$$
  (pp. 56–57).

### 3.6 Huffman coding (pp. 57–60)
- Huffman coding (David Huffman, 1952) gives frequent symbols short codewords and rare symbols long codewords. It is lossless, and for independent symbols the compression is close to the entropy (p. 57).
- **Source coding theorem for symbol codes** (the author cites MacKay): for a discrete variable X there exists a symbol code with expected length
$$H(X)\le L(X)<H(X)+1\tag{3.37}$$
  (p. 57).
- **Procedure.** Find the two least probable symbols and replace them by a composite symbol whose probability is their sum. Repeat until one symbol is left. Label each pair of branches 1 (upper) and 0 (lower). A symbol's code is read by concatenating labels from right to left (p. 58).
- Figure 3.3: five symbols A–E with probabilities 0.87, 0.04, 0.04, 0.03, 0.02 give A = 1, B = 011, C = 010, D = 001, E = 000 (p. 58).
- For the dice (codes in Table 3.2):
$$L(X)=\sum_{i=1}^{11}p(x_i)L(x_i)=3.31\ \text{binary digits/symbol}\tag{3.38–3.39}$$
  Efficiency $3.27/3.31=0.99$ (3.40–3.41). The difference from the entropy is less than one binary digit, so (3.37) holds (pp. 58–59).
- Huffman codes are **prefix codes**: no codeword is the first part of another, so boundaries between consecutive codewords are easy to detect (p. 59).
- **Images.** The 127-bin histogram of grey-level differences (from Chapter 1) would need $7\approx\log127$ digits with naive coding. Huffman gives $L=5.97$ against $H=5.94$, efficiency 0.99 (3.42). But 5.94 is itself an over-estimate, since it ignores that nearby pixels have similar grey-levels, and Huffman coding does not remove such dependencies (pp. 59–60).
- **English letters** (27 symbols including space, Table 3.3): treating letters as independent gives $H\le4.11$ bits/letter. Huffman needs 4.15 digits/letter, efficiency $4.11/4.15=0.990$. Since $2^{4.15}=17.8$, this is like 18 equiprobable letters (p. 60).
- Shannon–Fano coding (Shannon's own method) was largely superseded by Huffman. Both assume independent symbols, so for English the entropy must be below 4.11 (p. 61). Shannon, using people's ability to predict the next letter, estimated about 1.3 bits/letter ($2^{1.3}=2.46$, which the author reads as about three equiprobable letters). A purely statistical upper bound of 1.75 bits/letter has been estimated (p. 61).
- **Intuition note:** Huffman coding exploits unequal frequencies but cannot see structure across symbols. The numbers 4.11 → 1.8 show how much structure English has.

### 3.7 The entropy of English letters (pp. 61–70)
**Informal account (pp. 61–63)**
- A letter's probability depends on its context, so it is a conditional probability. The relative frequency of Table 3.3 is an unconditional probability (the author calls it "relative frequency"). The average information of letters under conditional probabilities is less than or equal to that under relative frequencies, so frequency-only estimates are too large (p. 62).
- As more surrounding letters are used, uncertainty about a hidden letter decreases, until an "uncertainty horizon" beyond which it stops decreasing. There the average uncertainty equals the entropy of English (p. 62; Fig. 3.6).
- **Objection (some mathematicians):** strictly, entropy applies to an ensemble of sequences, not one sequence. The author's response: entropy of English is defined for an ensemble of infinitely many sequences, but in practice it is estimated from finite data (p. 63).

**Blocks (pp. 63–66)**
- Text is cut into consecutive, non-overlapping blocks of N letters (Fig. 3.7); the author says this simplification does not alter the results. $G_N$ is the entropy per letter estimated from N-letter blocks. Pairs are not equiprobable (Fig. 3.8), so $G_2<G_1$, and likewise $G_3<G_2$ (pp. 63–64).
- As N grows, each letter depends less on letters in other blocks, so blocks become increasingly independent (p. 65). Suppose letters more than 10 apart are independent. With $N=10$, a block depends only on the previous and next blocks. For long texts this dependence is a tiny share of the total, so blocks behave like independent super-symbols (p. 65).
- The **correlation length** $N_C$ is the block length beyond which inter-letter dependence falls to zero. Beyond it, $G_N=H$. Shannon's theorems are stated for infinite block lengths but in practice apply to any block length above $N_C$ (p. 66).
- **Key point (author):** as block size grows, the average uncertainty per letter decreases (p. 66).

**Formal account (pp. 66–68)** (70 million characters; $G_1$ uses slightly different frequencies from Table 3.3)
$$G_1=\sum_{i=1}^{27}p(x_i)\log\frac1{p(x_i)}=4.08\ \text{bits/letter}\tag{3.43–3.44}$$
$$G_2=\frac12\sum_{i=1}^{27}\sum_{j=1}^{27}p([x_i,y_j])\log\frac1{p([x_i,y_j])}=\frac12\sum_{k=1}^{729}p(B_k)\log\frac1{p(B_k)}=3.32\ \text{bits/letter}\tag{3.45–3.47}$$
- The factor 1/2 is because each block holds two letters. 729 = 27², e.g. block [ce]. 3.32 is still an over-estimate because dependencies beyond two letters are ignored (p. 67).
$$G_3=\frac13\sum_{i}\sum_{j}\sum_{k}p([x_i,y_j,z_k])\log\frac1{p([x_i,y_j,z_k])}=\frac13\sum_{k=1}^{19{,}683}p(B_k)\log\frac1{p(B_k)}=2.73\ \text{bits/letter}\tag{3.48–3.50}$$
  Common triplets (and, the) dominate the average; rare ones (nud) contribute little. The key to the theorem is that a small proportion of possible sub-sequences are common while most are practically non-existent (p. 67).
$$G_N=\frac1N\sum_{k=1}^{27^N}p(B_k)\log\frac1{p(B_k)}\ \text{bits/letter}\tag{3.51}$$
- Once N reaches $N_C$, $G_{N_C}=H$. In practice the estimate converges to about 1.8 bits/letter (p. 68). If $H=1.8$, the theorem guarantees communication with just over 1.8 binary digits per letter (p. 68).
- **Intuition note:** $G_N$ is "how surprising is one letter if I read it inside a block of N". Larger blocks capture more context, so the surprise per letter goes down until context no longer helps.

**Efficient transmission of English (pp. 68–70)**
- Assume $N_C=10$ (the author says it is almost certainly not greater). The number of 10-letter sub-sequences is
$$m_C=27^{10}\approx206\times10^{12}\tag{3.52–3.53}$$
  which, if all were equiprobable, would need $\log(206\times10^{12})=47.5$ binary digits (3.54) (p. 68).
- Shannon proved (Section 3.8): the most common sub-sequences are a tiny proportion of all, they have collective probability about one, and each has about the same probability (pp. 68–69). With $H=1.8$:
$$m_H=2^{1.8\times10}=262{,}144\tag{3.55–3.56}$$
$$\log_2 2^{1.8\times10}=18\ \text{binary digits}\tag{3.57}$$
  Each of these has probability about 1/262,144. The other >205 million million have collective probability about zero. Since the 262,144 are equiprobable, Huffman coding would add no further saving (p. 69).
- **Scheme:** rank 10-letter sub-sequences by frequency in a large corpus. Give each of the top 262,144 an 18-digit codeword in a shared look-up table (codebook). Cut the message into 10-letter pieces and send the codewords. This uses 18 instead of 47.5 digits per piece, i.e. 1.8 instead of 4.75 per letter. The cost of sending the table is small if it is used often (p. 70).
- Before his letter-by-letter code (Section 1.6), Morse had made a numbered list of common phrases and sent the number. The author says this is conceptually similar (p. 70).
- The same reasoning applies to images (square blocks of grey-levels) and to most natural sequences (music, movies, DNA) (p. 71).

### 3.8 Why the theorem is true (pp. 71–76)
- Core observation: most events that could occur almost certainly do not, and those that do occur with about the same probability. The section is a counting argument, not a rigorous proof (pp. 71, 76).
- Setup: messages of n binary digits, iid, with $P=\Pr(\text{digit}=1)$. Possible messages: $m_{max}=2^n$. Messages actually generated: $m\ll m_{max}$. For large n, almost all messages contain about nP ones (law of large numbers); e.g. $P=1/8$, $n=8000$ gives about 1,000 ones (p. 71).
- The proof needs long messages; the author uses $n=8$ for illustration and pretends the long-message "facts" hold exactly (pp. 72–73).
- Example: $n=8$, $P=0.125$, $nP=1$, so the common messages have one 1 (Table 3.4: $s_1,\dots,s_8$), $m=8$ of them out of $m_{max}=256$. Probability of one specific such message:
$$P_1\times P_2\times\dots\times P_8=0.125\times0.875^7\tag{3.59}$$
$$=0.049\tag{3.60}$$
  Independence makes this the same wherever the 1 sits, so all eight messages are equally probable; the probability of "one 1, any position" is $8\times0.049\approx0.4$ (p. 73).
- Assuming only these eight occur and are equiprobable, $p=1/m=0.125$ (3.64–3.65), not to be confused with 0.049. They need
$$n_w=\log 8=3\ \text{binary digits per codeword}\tag{3.61–3.63}$$
  Entropy:
$$H=E[\log(1/p)]=\log m=3\ \text{bits per message}\tag{3.66–3.68}$$
  So the codeword length equals H, though 256 messages are possible (pp. 73–74). The author says that even when $nP>1$, m is still much less than $2^n$ (p. 74).
- **Why only m messages (pp. 75–76).** The number of messages with $n_1$ ones and $n_0$ zeros is
$$C_{n,n_1}=\frac{n!}{n_1!\,n_0!}\tag{3.69}$$
$$\sum_{n_1=0}^{n}C_{n,n_1}=2^n\tag{3.70}$$
  As n grows, almost all messages contain nP ones, so, for all practical purposes,
$$m=C_{n,nP}\tag{3.71}$$
$$m\ll2^n\tag{3.72}$$
- **Stirling's approximation** (large n): $\ln n!\approx n[(\ln n)-1]$. Starting from $\ln C_{n,n_1}=\ln n!-\ln n_1!-\ln n_0!$ (3.73), with $n_1=nP$:
$$\ln m\approx n[(\ln n)-1]-n_1[(\ln n_1)-1]-n_0[(\ln n_0)-1]\tag{3.74}$$
$$=n\ln n-n_1\ln n_1-n_0\ln n_0-(n-(n_1+n_0))\tag{3.75}$$
  The last bracket is zero because $n=n_0+n_1$ (added step), giving
$$\ln m=(n_0+n_1)\ln n-n_1\ln n_1-n_0\ln n_0\tag{3.76}$$
$$=n_1(\ln n-\ln n_1)+n_0(\ln n-\ln n_0)\tag{3.77}$$
$$=n\Big(\Big[\tfrac{n_1}{n}\ln\tfrac{n}{n_1}\Big]+\Big[\tfrac{n_0}{n}\ln\tfrac{n}{n_0}\Big]\Big)\tag{3.78}$$
$$=n(p_1\ln1/p_1+p_0\ln1/p_0)\tag{3.79}$$
  with $p_1=n_1/n$, $p_0=n_0/n$. This is the entropy of an n-digit message in nats. In bits:
$$\log_2 m=n\sum_{i=0}^{1}p_i\log_2\frac1{p_i}\ \text{bits per message}\tag{3.80}$$
  the entropy of an n-digit binary number (p. 76).
- **Intuition note:** Of all $2^n$ strings, those with the "right" proportion of ones are very few, but they contain nearly all the probability. Naming only those needs about nH binary digits.

### 3.9 Kolmogorov complexity (pp. 76–78)
- The compression reading of the theorem was developed independently by Kolmogorov (1933, as cited). His algorithmic complexity, now Kolmogorov complexity, is the length of the shortest computer program that describes an object (pp. 76–77).
- Example: the first million digits of π come from a program much shorter than a million binary digits, e.g. the Leibniz formula
$$\pi=4\times\Big(1-\tfrac13+\tfrac15-\tfrac17+\tfrac19\dots\Big)\tag{3.81}$$
$$\pi=4\times\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}\tag{3.82}$$
  written as a 'for' loop (p. 77).
- The shortest program for π has a finite but unknown $n_\pi$ binary digits. The author argues it also contains $n_\pi$ bits, because if each digit conveyed less than one bit a shorter program would exist. So the Kolmogorov complexity of π is $n_\pi$ bits. The link to Shannon: the Kolmogorov complexity of a random digit sequence is approximately equal to its entropy (p. 78).
- Kolmogorov complexity is non-computable: only exhaustive search over programs finds it, so one can never be certain no shorter program exists (p. 78).

### 3.10 Summary (p. 78)
Encoding messages efficiently is data compression. Channel capacity is the maximum rate of information transmission. Some codes are inefficient (each binary digit carries well under one bit). Dependent symbols can be encoded as independent blocks, so the theorem applies to natural sequences such as English and images (p. 78).

## Toy example (ours, not from the text)
Source with four symbols A, B, C, D with probabilities 1/2, 1/4, 1/8, 1/8, iid. Channel passes $C=1$ binary digit/s.

- Entropy: $H=\tfrac12\log2+\tfrac14\log4+\tfrac18\log8+\tfrac18\log8=0.5+0.5+0.375+0.375=1.75$ bits/symbol.
- Fixed-length code (A=00, B=01, C=10, D=11): $L=2$, efficiency $1.75/2=0.875$. Rate: 1 digit/s ÷ 2 digits/symbol $=0.5$ symbols/s.
- Huffman (as in Section 3.6): combine the two least probable, C and D, into 1/4. Now the least probable are the original B (1/4) and the composite (1/4); combine into 1/2. Finally combine this with A (1/2). Labelling gives A = 1, B = 01, C = 001, D = 000. (Any 0/1 labelling works; the lengths are what matter.)
- Average length: $L=\tfrac12(1)+\tfrac14(2)+\tfrac18(3)+\tfrac18(3)=0.5+0.5+0.375+0.375=1.75$ binary digits/symbol.
- Efficiency $1.75/1.75=1$. Rate $R=C/H=1/1.75\approx0.571$ symbols/s, which equals the theorem's limit, and is better than the 0.5 of the fixed code. Here every probability is a power of 1/2, so $-\log p_i$ is a whole number and (3.37) holds with $L=H$ exactly. For other probabilities L would lie between H and H + 1.

## Concepts
- [[channel-capacity]] — here, the maximum bits/s a noiseless channel carries, $\max_{p(X)}H(X)$; equals the number of binary digits per second (pp. 46–48)
- [[source-coding-theorem]] — rate $C/H-\epsilon$ symbols/s is achievable; more than $C/H$ is not (p. 49)
- [[entropy-H(X)]] — average information per symbol, $\sum p\log(1/p)$; used as the lower limit for average codeword length (pp. 52, 57–58)
- [[bit]] — unit of information; one binary digit carries at most one bit (p. 46)
- [[self-information-surprisal]] — $h=\log(1/p)$, listed per symbol in Table 3.2 (p. 55)
- [[coding-efficiency]] (new) — $H(S)/L(X)$ in bits per binary digit, between 0 and 1 (p. 52)
- [[redundancy]] — author's usage: predictable symbols or unequal frequencies make the information rate fall below capacity (p. 48)
- [[huffman-arithmetic-coding]] — Huffman coding built by repeatedly merging the two least probable symbols; Huffman codes are prefix codes (pp. 57–59)
- [[prefix-code-kraft]] — here only the prefix property (no codeword begins another) is stated, not the Kraft inequality (p. 59)
- [[entropy-rate]] — here the block estimates $G_N$ that converge to H of English at $N_C$ (pp. 64–68)
- [[correlation-length]] (new) — block length beyond which inter-letter dependence is zero, so $G_N=H$ (p. 66)
- [[typical-set-aep]] — not named by the author; his counting argument says most long messages fall in a set of about $2^H$ roughly equiprobable messages (pp. 71–76)
- [[kolmogorov-complexity]] — length of the shortest program that generates an object; non-computable (pp. 76–78)

## Canonical instances
- [[eight-sided-die-code]] (new) — 3-digit binary code with efficiency 1 (pp. 51–52)
- [[six-sided-die-block-code]] (new) — single-symbol code vs three-throw code; efficiencies 0.86 and 0.970 (pp. 52–54)
- [[two-dice-huffman]] (new) — H = 3.27, fixed 4-digit efficiency 0.818, Huffman L = 3.31 (pp. 55–59)
- [[english-letter-entropy-GN]] (new) — $G_1=4.08$, $G_2=3.32$, $G_3=2.73$, H ≈ 1.8 bits/letter (pp. 66–68)
- [[morse-phrase-codebook]] (new) — numbered phrase list as an early block codebook (p. 70)
- [[eight-digit-message-counting]] (new) — $n=8$, $P=1/8$: 8 of 256 messages, 3 digits (pp. 72–74)
- [[pi-leibniz-program]] (new) — π generated by a short program (pp. 77–78)

## Bridges (candidates)
- [structural-analogy] counting argument ($\log_2 C_{n,nP}\approx nH$) ↔ information-theory: typical set / AEP — both say about $2^{nH}$ sequences carry nearly all probability
- [same-math] block estimates $G_N\to H$ ↔ information-theory: entropy rate of a process with memory — per-letter block entropy converging to the limit
- [structural-analogy] ranking 10-letter blocks and coding the top 262,144 ↔ computational social science: measuring the predictability of language corpora by compressibility
- [structural-analogy] shortest program for an object ↔ information-theory: Minimum Description Length — both equate good description with short description

## Questions this raises
- The codebook scheme for English needs a table of 262,144 entries. Are there methods that adapt to the source without such a table, and how close do they get to H?
- How can the correlation length of a real sequence be estimated, and is 10 letters a reasonable value for English?
- The three English estimates (1.3, 1.75, 1.8 bits/letter) differ. What do the different methods assume?
- Kolmogorov complexity is non-computable, yet it is said to match entropy for random sequences. How can it be used in practice?

## Reading notes
- Offset: printed = pdf − 16 (pdf 61 = printed 45).
- Text layer: the ε in the theorem quotation (p. 49) and in "C/H − ε" is lost; read via the author's explanation on p. 50. A small misprint: "6 × 6 × 6× = 216" has a stray ×. Loose wording: Eq. 3.21 puts 0.86 bits/s in R = C/H (this is the actual information rate, 0.86 bits per binary digit × 1 binary digit/s, not the capacity), and the text calls the capacity "one bit or 0.387 symbols", mixing units (p. 53).
- Three values for the first-order English entropy appear: 4.11 (Table 3.3), 4.12 (Romeo and Juliet, Fig. 3.4) and 4.08 (70-million-character corpus, Eq. 3.44). English entropy is given as about 1.3 (Shannon; Table 3.3 caption), 1.75 (statistical upper bound) and about 1.8 (this chapter's estimate). The dashed H line in Fig. 3.6 sits near 1.75.
- $2^{1.3}=2.46$ is described as "just three" letters; this is the author's rounding.
- In the $n=8$ example, each of the 8 messages has probability 0.049 (3.60) and together about 0.4, yet the text sets $p=1/8$ by assuming only those messages occur. The author flags this as a pretence valid only for large n (p. 73).
- Eq. 3.75 includes a term $-(n-(n_1+n_0))$ that equals zero; I made this explicit as an added step. 3.37 is attributed to MacKay (2003) and Appendix F is referenced (p. 73) but not in this unit.
- The unit has no exercises.
