---
id: cover-2006-elements/ch08-channel-p2
work: cover-2006-elements
unit: "8 Channel Capacity (part 2/2: end of the proof of the coding theorem, §8.8–8.13, summary, problems, historical notes)"
pages: 203-223
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Channel Capacity, part 2: converse, Hamming codes, feedback, source–channel theorem

## L0 — One line
Capacity $C=\max_{p(x)}I(X;Y)$ is a sharp rate threshold: above it the error probability stays bounded away from 0 (even with feedback), and a source can be sent reliably if its entropy rate is below $C$ and not if it is above $C$.

## L1 — The gist (≤ 120 words)
This part finishes the noisy-channel coding theorem by proving its converse. It first treats zero-error codes, then uses Fano's inequality to handle small error probabilities. Looking at when equality holds in the same chain of inequalities suggests what a capacity-achieving code must look like. The unit then gives Hamming codes as a first structured code, proves that feedback does not raise the capacity of a discrete memoryless channel, and proves the joint source–channel coding theorem. That theorem says that, for a single-user channel, compression and channel coding can be designed separately without loss. Why it matters: it ties the two basic theorems together. The author also notes that known structured codes do not yet reach capacity.

**Prerequisites:** entropy, mutual information, chain rule, data processing inequality, Markov chains, AEP and typical sets, definition of channel capacity and of $(2^{nR},n)$ codes, binary linear algebra (mod 2).

## L2 — Key ideas
- Random-coding proofs show good codes exist but give no practical construction; structured codes known so far do not reach capacity (p. 203).
- Converse for zero-error codes: $nR=H(W)\le I(X^n;Y^n)\le\sum I(X_i;Y_i)\le nC$, so $R\le C$ (pp. 203–204).
- Fano's inequality plus Lemma 8.9.2 ($I(X^n;Y^n)\le nC$ for a DMC) gives $P_e^{(n)}\ge 1-C/R-1/(nR)$. So error is bounded away from 0 when $R>C$ (pp. 205–207).
- Equality analysis: a capacity-achieving code needs distinct codewords and outputs that look i.i.d. with $p^*(y)$ (p. 208).
- Hamming codes use a parity-check matrix $H$; the product $H\mathbf r$ locates a single error. They correct one error; like all codes known so far, they do not meet the capacity bound (pp. 209–212).
- Feedback capacity equals capacity for a discrete memoryless channel: $C_{FB}=C$ (pp. 213–214).
- Source–channel theorem: reliable transmission is possible if $H(\mathcal V)<C$ (for a source satisfying the AEP) and impossible if $H(\mathcal V)>C$ (for a stationary source). So source and channel coding can be designed separately (pp. 215–218).
- The separation can look wasteful for particular sources (English over an erasure channel), and the author notes the decomposition breaks down for some multiuser channels (p. 215).

## L3 — Walkthrough

### 8.7 (end) — Remarks on the coding-theorem proof (p. 203)
The page opens in the middle of a sentence: among the set of codes of length $n$ with small probability of error, the best code can be found by exhaustive search. The author remarks that the Kolmogorov complexity of the best code is therefore a small constant. So telling sender and receiver which code was chosen needs no channel: they just agree to use the best $(2^{nR},n)$ code (p. 203).
The theorem shows good codes with exponentially small error exist for long blocks. It does not construct them. A random code is likely good, but without structure decoding by table lookup needs an exponentially large table. Researchers have built many structured codes, but their asymptotic rates are not yet near capacity (p. 203).

### 8.8 Zero-error codes (pp. 203–204)
Goal: show $P_e^{(n)}=0\Rightarrow R\le C$. Assume a $(2^{nR},n)$ code with $g(Y^n)=W$ with probability 1, so $H(W|Y^n)=0$. Take $W$ uniform on $\{1,\dots,2^{nR}\}$, so $H(W)=nR$ (p. 203).

$$nR=H(W)=H(W|Y^n)+I(W;Y^n)\tag{8.82}$$
$$=I(W;Y^n)\tag{8.83}$$
$$\overset{(a)}{\le} I(X^n;Y^n)\tag{8.84}$$
$$\overset{(b)}{\le}\sum_{i=1}^n I(X_i;Y_i)\tag{8.85}$$
$$\overset{(c)}{\le} nC\tag{8.86}$$

(a) is the data processing inequality ($W\to X^n(W)\to Y^n$ is a Markov chain). (b) uses the discrete memoryless assumption and is proved in Lemma 8.9.2. (c) is the definition of capacity. Hence $R\le C$ for any zero-error code, for all $n$ (8.87) (p. 204).

*Intuition note:* With no errors, the output must pin down the message, so the output must carry all $nR$ bits. A channel used $n$ times can pass at most $nC$ bits.

### 8.9 Fano's inequality and the converse (pp. 204–207)
**Setup.** $W$ uniform on $\{1,\dots,2^{nR}\}$; $\hat W=g(Y^n)$; $P_e^{(n)}=\Pr(\hat W\ne W)$ (8.88). Define $E=1$ if $\hat W\neq W$, else $E=0$ (8.89) (p. 204).
Expand $H(E,W|Y^n)$ two ways with the chain rule:
$$H(E,W|Y^n)=H(W|Y^n)+H(E|W,Y^n)\tag{8.90}$$
$$=H(E|Y^n)+H(W|E,Y^n).\tag{8.91}$$
$E$ is a function of $W$ and $g(Y^n)$, so $H(E|W,Y^n)=0$. Also $H(E)\le1$ since $E$ is binary (p. 204). Then
$$H(W|E,Y^n)=P(E=0)H(W|Y^n,E=0)+P(E=1)H(W|Y^n,E=1)\tag{8.92}$$
$$\le(1-P_e^{(n)})0+P_e^{(n)}\log(|\mathcal W|-1)\tag{8.93}$$
$$\le P_e^{(n)}nR.\tag{8.94}$$
Given $E=0$, $W=g(Y^n)$. When $E=1$ the conditional entropy is at most the log of the number of outcomes (p. 205). Combining:
$$H(W|Y^n)\le1+P_e^{(n)}nR.\tag{8.95}$$
For a fixed code $X^n(W)$ is a function of $W$, so $H(X^n(W)|Y^n)\le H(W|Y^n)$ (8.96).

**Lemma 8.9.1 (Fano).** For a DMC with codebook $\mathcal C$ and uniform messages, with $P_e^{(n)}=\Pr(W\ne g(Y^n))$: $H(X^n|Y^n)\le1+P_e^{(n)}nR$ (8.97) (p. 205).

**Lemma 8.9.2.** If $Y^n$ is the result of passing $X^n$ through a DMC, then $I(X^n;Y^n)\le nC$ for all $p(x^n)$ (8.98). *Proof* (pp. 205–206):
$$I(X^n;Y^n)=H(Y^n)-H(Y^n|X^n)\tag{8.99}$$
$$=H(Y^n)-\sum_{i=1}^nH(Y_i|Y_1,\dots,Y_{i-1},X^n)\tag{8.100}$$
$$=H(Y^n)-\sum_{i=1}^nH(Y_i|X_i)\tag{8.101}$$
because in a DMC, $Y_i$ depends only on $X_i$ and is conditionally independent of everything else.
$$\le\sum_{i=1}^nH(Y_i)-\sum_{i=1}^nH(Y_i|X_i)\tag{8.103}$$
$$=\sum_{i=1}^nI(X_i;Y_i)\tag{8.104}$$
$$\le nC.\tag{8.105}$$
(8.103) uses that the entropy of a collection of variables is at most the sum of the individual entropies. (8.105) is the definition of capacity. So using the channel many times does not raise capacity per transmission (p. 206).

**Converse to Theorem 8.7.1.** Claim: any sequence of $(2^{nR},n)$ codes with $\lambda^{(n)}\to0$ must have $R\le C$. If the maximal error tends to 0, so does the average error $P_e^{(n)}$ (defined in (8.31)). With $W$ uniform, $P_e^{(n)}=\Pr(\hat W\ne W)$ (p. 206).
$$nR=H(W)=H(W|Y^n)+I(W;Y^n)\tag{8.106}$$
$$\le H(W|Y^n)+I(X^n(W);Y^n)\tag{8.107}$$
$$\le1+P_e^{(n)}nR+I(X^n(W);Y^n)\tag{8.108}$$
$$\le1+P_e^{(n)}nR+nC\tag{8.109}$$
by Lemmas 8.9.1 and 8.9.2. Dividing by $n$:
$$R\le P_e^{(n)}R+\frac1n+C.\tag{8.110}$$
As $n\to\infty$ the first two terms tend to 0, so $R\le C$ (8.111). Rewriting (8.110):
$$P_e^{(n)}\ge1-\frac CR-\frac1{nR}.\tag{8.112}$$
So if $R>C$, the error is bounded away from 0 for large $n$. It is also bounded away from 0 for all $n$, because if $P_e^{(n)}=0$ for small $n$, concatenating such codes gives zero-error codes for large $n$ (p. 207). Hence arbitrarily low error is impossible above capacity (Figure 8.10).

This is the *weak converse*. A *strong converse* exists (stated, not proved here): above capacity the error goes exponentially to 1. So $P_e^{(n)}\to0$ exponentially below $C$ and $P_e^{(n)}\to1$ exponentially above $C$ (p. 207).

*Intuition note:* Fano says that if the output leaves much uncertainty about the message, errors must be frequent. The channel can supply at most $nC$ bits, so a code asking for $nR>nC$ bits leaves unavoidable uncertainty.

### 8.10 Equality in the converse (pp. 207–209)
Repeat the zero-error chain with $P_e=0$ to see what equality requires:
$$nR=H(W)\overset{(a)}{=}H(X^n(W))=H(X^n|Y^n)+I(X^n;Y^n)\tag{8.113–8.115}$$
$$=I(X^n;Y^n)=H(Y^n)-H(Y^n|X^n)=H(Y^n)-\sum_iH(Y_i|X_i)\tag{8.116–8.118}$$
$$\overset{(b)}{\le}\sum H(Y_i)-\sum H(Y_i|X_i)=\sum I(X_i;Y_i)\overset{(c)}{\le}nC.\tag{8.119–8.121}$$
$H(X^n|Y^n)=0$ because $P_e=0$; (8.118) uses that the channel is a DMC (p. 208).
Equality holds in (a) only if all codewords are distinct, in (b) only if the $Y_i$ are independent, and in (c) only if $X_i$ has the capacity-achieving distribution $p^*(x)$. So an efficient code that achieves capacity has distinct codewords and $Y_i$'s that look i.i.d. with
$$p^*(y)=\sum_xp^*(x)p(y|x).\tag{8.122}$$
The distribution meant is the empirical distribution induced by a uniform distribution over codewords:
$$p(x_i,y_i)=\frac1{2^{nR}}\sum_{w=1}^{2^{nR}}I(X_i(w)=x_i)\,p(y_i|x_i).\tag{8.123}$$
Examples (pp. 208–209):
1. *Noisy typewriter.* 26 letters; each is printed correctly or changed to the next letter, each with probability $\tfrac12$. Using every alternate letter gives 13 codewords of block length 1 and achieves capacity $\log13$. Choosing codewords i.i.d. uniform on $\{1,3,\dots,25\}$ gives outputs i.i.d. uniform on $\{1,\dots,26\}$, as expected.
2. *Binary symmetric channel.* Every output sequence has positive probability given any input, so even two codewords cannot be told apart with zero error. The zero-error capacity of the BSC is zero. Still, efficient codes induce an output that looks i.i.d. Bernoulli$(\tfrac12)$. Near capacity, decoding sets cover almost all output sequences. Above capacity they begin to overlap and the error cannot be made arbitrarily small.

### 8.11 Hamming codes (pp. 209–212)
**Background.** Shannon's theorem promises block codes; useful codes must also be simple to encode and decode. The author describes only Hamming's scheme (p. 209).
- *Repetition code:* send 11111 for 1 and 00000 for 0, rate $\tfrac15$. Over a BSC the optimal decoder is majority vote. Longer repetition gives arbitrarily low error but the rate goes to 0 (p. 209). (The page says an error occurs "if and only if more than 3" bits change; see Reading notes.)
- *Parity-check code:* from $n-1$ information bits, choose the $n$-th so the block has an even number of 1's. It detects an odd number of errors, misses an even number, and does not say how to correct (p. 210).

**Hamming (7,4) code.** Work modulo 2. Put all non-zero binary length-3 vectors as columns (p. 210):
$$H=\begin{bmatrix}0&0&0&1&1&1&1\\0&1&1&0&0&1&1\\1&0&1&0&1&0&1\end{bmatrix}\tag{8.124}$$
The codewords are the vectors in the null space of $H$. $H$ has rank 3, so the null space has dimension 4: $2^4=16$ codewords (Table 8.1 lists them). The set is linear: the sum of two codewords is a codeword. It is a 4-dimensional subspace of a 7-dimensional space (p. 210).
- *Minimum weight* = smallest number of 1's in a non-zero codeword; here 3. It is at least 3 because all columns of $H$ are different, so no two columns add to 000. It is exactly 3 because the sum of any two columns is a column of $H$ (p. 210).
- *Minimum distance* = smallest number of places in which two codewords differ. By linearity, differences are codewords, so any two codewords differ in at least 3 places. For a linear code, minimum distance equals minimum weight (p. 211).
- A codeword corrupted in one place differs from any other codeword in at least 2 places, so it is closer to the sent one (p. 211).

**Decoding.** $H$ is the *parity check matrix*: $H\mathbf c=\mathbf 0$ for every codeword. If position $i$ is corrupted, $\mathbf r=\mathbf c+\mathbf e_i$ ($\mathbf e_i$ has a 1 only in position $i$), and
$$H\mathbf r=H(\mathbf c+\mathbf e_i)=H\mathbf c+H\mathbf e_i=H\mathbf e_i,\tag{8.125}$$
the $i$-th column of $H$. This identifies the corrupted position; flipping that bit gives a codeword. The code corrects up to one error (p. 211).

**Encoding.** The first 4 bits of the codewords cycle through all $2^4$ patterns, so they can carry the message and the other 3 bits are parity bits. A linear code with first $k$ bits as message and last $n-k$ as parity bits is *systematic*. A code is labelled $(n,k,d)$; this one is $(7,4,3)$. With $l$ rows in $H$: $n=2^l-1$, $k=2^l-l-1$, minimum distance 3. All these are Hamming codes and correct one error (p. 211).

**Beyond Hamming (p. 212).** Reed and Solomon (early 1950s) found multiple-error-correcting codes for non-binary channels. Bose–Chaudhuri and Hocquenghem (late 1950s) used Galois field theory to build $t$-error-correcting BCH codes for any $t$. Compact disc players use two interleaved Reed–Solomon codes, $(32,28,5)$ and $(28,24,5)$, correcting bursts of up to 4000 errors (as printed). All of these are block codes. *Convolutional codes* let each output block depend on past inputs too (details omitted).
**Gap to capacity.** For a BSC with crossover $p$, meeting Shannon's bound needs a code correcting about $np$ errors with $n(1-H(p))$ information bits. No known code does this. The repetition code corrects up to $n/2$ errors but its rate tends to 0. Until 1972 all known codes correcting $n\alpha$ errors had asymptotic rate 0. Justesen (1972) found codes with positive asymptotic rate and positive relative minimum distance, but they are good only for long blocks (p. 212).

### 8.12 Feedback capacity (pp. 212–214)
All received symbols are sent back immediately and noiselessly to the transmitter (Figure 8.11). A $(2^{nR},n)$ *feedback code* is a sequence of maps $x_i(W,Y^{i-1})$ plus decoding functions $g:\mathcal Y^n\to\{1,\dots,2^{nR}\}$, with $P_e^{(n)}=\Pr\{g(Y^n)\ne W\}$ for uniform $W$ (8.126). The capacity with feedback $C_{FB}$ is the supremum of rates achievable by feedback codes (p. 213).

**Theorem 8.12.1.** $C_{FB}=C=\max_{p(x)}I(X;Y)$ (8.127).
*Proof.* A non-feedback code is a special case, so $C_{FB}\ge C$ (8.128). For the other direction, Lemma 8.9.2 fails: $X_i$ now depends on past outputs, so $Y_i$ is no longer conditionally independent of the future $X$'s in (8.101). Fix: work with $W$ instead of $X^n$ (p. 213).
$$nR=H(W)=H(W|Y^n)+I(W;Y^n)\le1+P_e^{(n)}nR+I(W;Y^n)\tag{8.129–8.130}$$
(Fano). Then
$$I(W;Y^n)=H(Y^n)-H(Y^n|W)=H(Y^n)-\sum_iH(Y_i|Y_1,\dots,Y_{i-1},W)\tag{8.131–8.132}$$
$$=H(Y^n)-\sum_iH(Y_i|Y_1,\dots,Y_{i-1},W,X_i)=H(Y^n)-\sum_iH(Y_i|X_i)\tag{8.133–8.134}$$
since $X_i$ is a function of $Y_1,\dots,Y_{i-1}$ and $W$, and given $X_i$, $Y_i$ is independent of $W$ and past $Y$'s. Then
$$I(W;Y^n)\le\sum H(Y_i)-\sum H(Y_i|X_i)=\sum I(X_i;Y_i)\le nC.\tag{8.135–8.138}$$
So $nR\le P_e^{(n)}nR+1+nC$ (8.139). Dividing by $n$ and letting $n\to\infty$ gives $R\le C$ (8.140), hence $C_{FB}=C$ (8.141) (p. 214).
The author notes that for the binary erasure channel feedback helps enormously in simplifying encoding and decoding, but cannot raise capacity (p. 214).

*Intuition note:* Feedback lets the sender adapt, but the proof still gives $I(W;Y^n)\le nC$ over $n$ uses. Adaptivity cannot create more.

### 8.13 The joint source–channel coding theorem (pp. 215–218)
**Motivation.** Combine data compression ($R>H$, Thm 5.4.2) and transmission ($R<C$, Thm 8.7.1). Is $H<C$ necessary and sufficient for sending a source over a channel? The worry: two-stage coding (compress, then channel-code) might lose something, since compression ignores the channel and channel coding ignores the source (p. 215).
**Claim.** The two-stage method is as good as any other, so system design splits into source coding and channel coding. The common binary representation lets e.g. ISDN carry speech and data on one channel. The author warns this is not always true: multiuser channels exist where the decomposition breaks down (p. 215).
**Cases where the theorem seems misleading** (author's examples, p. 215–216):
- English text over an erasure channel. A compressed binary form is hard to decode after erasures, but raw English remains readable after losing up to about half the letters.
- The human ear can distinguish speech under high white noise, so sending uncompressed speech may be appropriate. The author's reading: "the redundancy in the source is suited to the channel."

**Setup** (p. 216). Source $V$ over finite alphabet $\mathcal V$, any process satisfying the AEP (e.g. i.i.d., or states of a stationary irreducible Markov chain; any stationary ergodic source satisfies the AEP, shown in §15.7). Map $V^n$ to codeword $X^n(V^n)$; the receiver gets $Y^n$ and estimates $\hat V^n$ with decoder $g$:
$$P_e^{(n)}=\Pr(V^n\ne\hat V^n)=\sum_{y^n}\sum_{v^n}p(v^n)p(y^n|x^n(v^n))\,I(g(y^n)\ne v^n).\tag{8.142}$$

**Theorem 8.13.1.** If $V_1,\dots,V_n$ is a finite-alphabet process satisfying the AEP, a source-channel code with $P_e^{(n)}\to0$ exists if $H(\mathcal V)<C$. Conversely, for any stationary process, if $H(\mathcal V)>C$, the error is bounded away from zero (p. 216).

*Achievability* (pp. 216–217). The AEP gives a typical set $A_\epsilon^{(n)}$ of size $\le2^{n(H(\mathcal V)+\epsilon)}$ holding most of the probability. Encode only typical sequences; others count as errors, contributing at most $\epsilon$. Indexing needs $n(H+\epsilon)$ bits. The index can be sent with error $<\epsilon$ if
$$H(\mathcal V)+\epsilon=R<C.\tag{8.143}$$
The receiver enumerates $A_\epsilon^{(n)}$ and picks the sequence for the estimated index. For $n$ large:
$$P_e^{(n)}\le P(V^n\notin A_\epsilon^{(n)})+P(g(Y^n)\ne V^n|V^n\in A_\epsilon^{(n)})\le\epsilon+\epsilon=2\epsilon.\tag{8.144–8.146}$$
So reliable reconstruction is possible for large $n$ if $H(\mathcal V)<C$ (8.147).

*Converse* (pp. 217–218). Show $P_e^{(n)}\to0\Rightarrow H(\mathcal V)\le C$ for any source-channel codes $X^n(V^n):\mathcal V^n\to\mathcal X^n$, $g_n(Y^n):\mathcal Y^n\to\mathcal V^n$. Fano:
$$H(V^n|\hat V^n)\le1+P_e^{(n)}\log|\mathcal V^n|=1+P_e^{(n)}n\log|\mathcal V|.\tag{8.150}$$
Then
$$H(\mathcal V)\overset{(a)}{\le}\frac{H(V_1,\dots,V_n)}n=\frac{H(V^n)}n=\frac1nH(V^n|\hat V^n)+\frac1nI(V^n;\hat V^n)\tag{8.151–8.153}$$
$$\overset{(b)}{\le}\frac1n(1+P_e^{(n)}n\log|\mathcal V|)+\frac1nI(V^n;\hat V^n)\tag{8.154}$$
$$\overset{(c)}{\le}\frac1n(1+P_e^{(n)}n\log|\mathcal V|)+\frac1nI(X^n;Y^n)\tag{8.155}$$
$$\overset{(d)}{\le}\frac1n+P_e^{(n)}\log|\mathcal V|+C.\tag{8.156}$$
(a): definition of entropy rate of a stationary process; (b): Fano; (c): data processing ($V^n\to X^n\to Y^n\to\hat V^n$ is a Markov chain); (d): memorylessness of the channel. Letting $n\to\infty$ with $P_e^{(n)}\to0$: $H(\mathcal V)\le C$ (8.157) (p. 218).
The author concludes that a stationary ergodic source can be sent over the channel "if and only if" its entropy rate is less than capacity (p. 218).

**Summary of the two proofs** (p. 218). Compression comes from the AEP: a small subset of size $2^{nH}$ holds most probability, so $H$ bits per symbol suffice. Transmission comes from the joint AEP: the output is very likely jointly typical with the sent codeword, while any other codeword is jointly typical with probability $\approx2^{-nI}$, so about $2^{nI}$ codewords can be used with negligible error. The separation theorem says source and channel codes can be designed separately and combined for optimal performance.

*Intuition note:* Compression turns the source into about $nH$ bits. The channel can carry about $nC$ bits reliably. So the question reduces to whether $nH$ fits into $nC$.

### Summary of Chapter 8 (pp. 218–219)
The author restates: $C=\max I(X;Y)$; BSC $C=1-H(p)$; binary erasure $C=1-\alpha$; symmetric channel $C=\log|\mathcal Y|-H(\text{row})$. Properties: $0\le C\le\min\{\log|\mathcal X|,\log|\mathcal Y|\}$; $I(X;Y)$ is a continuous concave function of $p(x)$. Jointly typical set $A_\epsilon^{(n)}$ defined by three conditions (8.158–8.161): $-\frac1n\log p(x^n)$, $-\frac1n\log p(y^n)$ and $-\frac1n\log p(x^n,y^n)$ are each within $\epsilon$ of $H(X)$, $H(Y)$, $H(X,Y)$. Joint AEP: (1) $\Pr((X^n,Y^n)\in A_\epsilon^{(n)})\to1$; (2) $|A_\epsilon^{(n)}|\le2^{n(H(X,Y)+\epsilon)}$; (3) for independent $(\tilde X^n,\tilde Y^n)\sim p(x^n)p(y^n)$, the probability of being jointly typical is $\le2^{-n(I(X;Y)-3\epsilon)}$. Coding theorem: every $R<C$ is achievable with $\lambda^{(n)}\le\epsilon$ (8.162); conversely $\lambda^{(n)}\to0$ implies $R\le C$. Also $C_{FB}=C$, and the source–channel theorem (p. 219).

### Problems (pp. 220–222) and Historical notes (pp. 222–223)
Twelve problems (see Exercises). Historical notes (author's attributions): Shannon developed mutual information and capacity and outlined the typical-sequence proof; Feinstein gave the first rigorous proof; Gallager a simpler random-coding-exponent proof; this book's proof is based on Cover [62] and on Forney's unpublished course notes [115]. Fano proved the converse; Wolfowitz the strong converse; Arimoto and Blahut an iterative algorithm for capacity. Shannon introduced zero-error capacity and proved feedback does not increase DMC capacity. Lovász gave the first important result on zero-error capacity (pp. 222–223).

## Toy example (ours)
**Converse bound.** Suppose a channel has $C=0.5$ bit/use and we try rate $R=1$ with block length $n=10$. From $nR\le1+P_e^{(n)}nR+nC$: $10\le1+10P_e^{(n)}+5$, so $P_e^{(n)}\ge0.4$. Check with (8.112): $1-0.5/1-1/(10\cdot1)=1-0.5-0.1=0.4$. ✓. With uniform messages, no code with these parameters can have average error below 0.4.

**Hamming decoding.** $\mathbf c=0001111$ is a codeword: with rows of $H$ from (8.124), row 1 gives $1+1+1+1=4\equiv0$, row 2 gives $1+1=2\equiv0$, row 3 gives $1+1=2\equiv0$. Flip position 3: $\mathbf r=0011111$. Row 1: $1+1+1+1=4\equiv0$. Row 2 (entries $0,1,1,0,0,1,1$): positions 3, 6, 7 give $3\equiv1$. Row 3 (entries $1,0,1,0,1,0,1$): positions 3, 5, 7 give $3\equiv1$. So $H\mathbf r=(0,1,1)^T$, which is column 3 of $H$. Flip bit 3 to recover $0001111$. ✓

## Concepts
- [[channel-capacity]] — $C=\max_{p(x)}I(X;Y)$; also shown not to grow with $n$ uses of a DMC (Lemma 8.9.2) (p. 205).
- [[noisy-channel-coding-theorem]] — rates $R<C$ achievable; converse $\lambda^{(n)}\to0\Rightarrow R\le C$ (pp. 206, 219).
- [[fanos-inequality]] — $H(W|Y^n)\le1+P_e^{(n)}nR$ for uniform $W$ on $2^{nR}$ messages (pp. 204–205).
- [[data-processing-inequality]] — used for $W\to X^n\to Y^n$ and $V^n\to X^n\to Y^n\to\hat V^n$ (pp. 204, 218).
- [[mutual-information]] — $I(X;Y)$, additive bound over uses of a DMC (p. 205).
- [[entropy-rate]] — $H(\mathcal V)$ of a stationary source; compared with $C$ (p. 218).
- [[typical-set-aep]] — typical set of size $\le2^{n(H+\epsilon)}$ used for source coding; joint typicality in the summary (pp. 216, 219).
- [[source-channel-separation]] — two-stage design (compress, then channel-code) loses nothing for the single-user case proved here (pp. 215, 218).
- [[error-correcting-code]] — added structured redundancy; parity-check and Hamming codes (p. 209).
- [[redundancy]] — added deliberately by coding so loss can be repaired (p. 209); source redundancy may suit the channel (p. 216).
- [[weak-converse]] (new) — for $R>C$, $P_e^{(n)}\ge1-C/R-1/(nR)$; strong version has error $\to1$ exponentially (p. 207).
- [[feedback-capacity]] (new) — supremum of rates for feedback codes; equals $C$ for a DMC (p. 213).
- [[hamming-code]] (new) — linear code from parity-check matrix with all non-zero columns; $n=2^l-1$, $k=2^l-l-1$, $d=3$; corrects one error (p. 211).
- [[minimum-distance]] (new) — least number of places two codewords differ; equals minimum weight for a linear code (p. 211).
- [[zero-error-capacity]] (new) — bits per use transmittable with zero error probability; zero for the BSC (pp. 209, 222).

## Canonical instances
- [[noisy-typewriter]] — alternate-letter code with 13 codewords achieves $\log13$ and satisfies the equality conditions (p. 208).
- [[binary-symmetric-channel]] — zero-error capacity 0; repetition code has rate $\to0$ (pp. 209).
- [[binary-erasure-channel]] — feedback helps encoding and decoding but not capacity (p. 214).
- [[hamming-7-4-code]] — 16 codewords, minimum distance 3, single-error correction using $H\mathbf r$ (pp. 210–211).
- [[repetition-code]] — five-fold repetition, majority-vote decoding (p. 209).
- [[compact-disc-reed-solomon]] — interleaved (32,28,5) and (28,24,5) codes correcting bursts (p. 212).
- [[english-over-erasure-channel]] — raw redundant text survives erasures better than compressed bits (p. 215).

## Bridges (candidates)
- [structural-analogy] Equality conditions (distinct codewords, i.i.d. outputs with $p^*(y)$) ↔ maximum entropy principle: capacity achieved when outputs are as spread as the constraints allow.
- [same-math] Fano's inequality here ↔ Fano's inequality in estimation: the same bound $H(W|Y^n)\le1+P_e\log|\mathcal W|$ ties residual entropy to error.
- [structural-analogy] Source–channel separation ↔ rational inattention: both treat information-rate limits as the binding constraint on what can be passed along.
- [metaphor] Feedback does not raise capacity ↔ adaptive sampling: adaptivity helps convenience, not the information limit.

## Questions this raises
- The theorem leaves $H(\mathcal V)=C$ open; what happens exactly at the boundary?
- Which multiuser channels break the separation, and why does the proof fail there?
- Can codes with both low decoding complexity and rates near capacity be built for the BSC?
- If feedback cannot raise capacity, how much does it change the speed at which error falls with $n$?

## Exercises worth doing
- Ex. 1 (p. 220) — preprocessing the output cannot increase capacity (data processing inequality) — difficulty: easy
- Ex. 4 (p. 220) — channels with memory can have higher capacity than $1-H(p)$ — difficulty: medium
- Ex. 7 (p. 221) — noisy typewriter variants and zero-error block-length-one codes — difficulty: easy
- Ex. 8 (p. 221) — cascade of $n$ BSCs is a BSC with error $\tfrac12(1-(1-2p)^n)$; capacity $\to0$ — difficulty: medium
- Ex. 9 (p. 221) — capacity of the Z channel and its optimal input — difficulty: medium
- Ex. 11 (p. 222) — pentagonal channel: capacity and zero-error capacity via length-2 codes — difficulty: hard

## Reading notes
- This part starts mid-§8.7 at printed p. 203 (end of the proof of Theorem 8.7.1) and ends with Historical Notes at p. 223. The unit covers §8.8–8.13, the chapter summary, problems and notes. Printed = pdf − 22.
- Source is the 1991 first edition (per metadata), not the 2006 second edition; per the metadata, chapter numbering and content differ from the 2nd edition.
- Printed misprint/inconsistency (p. 209): the text says repetition-5 majority decoding errs "if and only if more than 3 of the bits are changed", but its own decoding rule (decode 1 if 3 or more bits are 1) implies error when 3 or more bits change.
- The author writes "if and only if" about $H<C$ (p. 218), but Theorem 8.13.1 states sufficiency for $H<C$ and impossibility for $H>C$. The case $H=C$ is not covered.
- OCR garbled many equations and symbols; all were checked against the page images. Problem 12's channel figure (p. 222) was not read in detail, and Problem 12 is not summarised here. In Problem 1(b) the page says "does not strictly decrease"; kept as printed.
