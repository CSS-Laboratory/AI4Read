---
id: mackay-2003-information/ch13-binary
work: mackay-2003-information
unit: "13 Binary Codes"
pages: 205-227
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
# Binary Codes (MacKay, ch. 13)

## L0 — One line
Maximizing the distance between codewords (sphere packing) is only loosely related to Shannon's goal of reliable communication: good codes must decode far beyond half their minimum distance.

## L1 — The gist (≤ 120 words)
Does the coding theorist's aim of packing codewords far apart match Shannon's aim of reliable communication over a binary symmetric channel? Only loosely. Perfect codes are almost nonexistent. A bounded-distance decoder tolerates only half the noise level Shannon proved tolerable (for good codes whose minimum distance is near the Gilbert–Varshamov distance). Concatenated Hamming codes perform well despite "bad" distance. Distance still matters at low noise, but the whole weight enumerator function is relevant to whether a code is good. The chapter also treats random linear codes, the union bound, dual codes, and maximum-distance-separable codes, which are the erasure-channel analogue of perfect codes. Theorem 13.1 links bitwise and block decoding error.

**Prerequisites:** mod-2 arithmetic; binomial coefficients; binary entropy $H_2$; generator and parity-check matrices of linear codes; BSC capacity $1-H_2(f)$; expectation.

## L2 — Key ideas
- Over a binary symmetric channel (BSC), the optimal decoder picks the codeword nearest in Hamming distance. A code of minimum distance $d$ corrects any $t=\lfloor (d-1)/2\rfloor$ errors. For linear codes the weight enumerator $A(w)$ summarizes all distances (pp. 206–207).
- Bounded-distance decoders give up beyond $t$ errors ("worst-case-ism"). They cannot reach the Shannon limit, because a good decoder must often correct more than $t$ errors (p. 207).
- The only nontrivial perfect binary codes are Hamming codes, odd-length repetition codes and the binary Golay code. For most codes almost all of Hamming space lies between the $t$-spheres. For $f>1/3$ no perfect $fN$-error-correcting code exists (pp. 209–211).
- Random linear codes have $\langle A(w)\rangle=\binom Nw 2^{-M}$ and typical distance near the Gilbert–Varshamov distance $d_{GV}$. A bounded-distance decoder then tolerates only $f_{bd}=f/2$ (pp. 211–212).
- Berlekamp's bats: the minimum distance is relevant to the error probability at low noise. At higher noise errors depend on the weight enumerator function, because distant codewords are far more numerous (pp. 213–214).
- Concatenated Hamming codes have bad distance ($d/N\to0$) yet give vanishing error at rate 0.093 for $f=0.0588$. A single weight-$d$ codeword contributes error about $[\beta(f)]^d$, so moderate $d$ already suffices in practice (pp. 214–215).
- The union bound $P(\text{block error})\le\sum_{w>0}A(w)[\beta(f)]^w$ is accurate at low noise (p. 216). Dual codes swap $\mathbf G$ and $\mathbf H$. Many state-of-the-art codes have bad duals (pp. 216–219).
- MDS codes are the perfect-code analogue for erasure channels. No binary ones exist apart from repetition and simple parity codes. For $q>2$ there are many (Reed–Solomon codes are the most famous), and MDS codes of any rate can be found when $q>N$. Theorem 13.1: $p_B\ge p_b\ge \frac12\frac{d_{min}}N p_B$ (pp. 219–221, 224–226).

## L3 — Walkthrough

### Intro and 13.0 framing (pp. 205–206)
Chapters 8–11 proved the noisy-channel coding theorem for general alphabets. This chapter specializes to binary inputs, first the BSC (p. 205). Many coding theorists try to pack as many non-overlapping spheres as possible into $N$-dimensional space. MacKay says this has only a tenuous relationship to Shannon's aim (p. 205).

On a BSC the optimal decoder returns the codeword closest to the received vector $\mathbf r$ in **Hamming distance**, the number of coordinates in which two binary vectors differ. For example, the distance between 00001111 and 11001101 is 3. A decoding error occurs if noise takes the transmitted $\mathbf t$ to an $\mathbf r$ closer to another codeword (p. 206).

### 13.1 Distance properties of a code (p. 206)
- The **distance** (minimum distance, $d$ or $d_{min}$) is the smallest separation between two codewords. The (7,4) Hamming code has $d=3$, so $t=1$. A code of distance $d$ is $\lfloor (d-1)/2\rfloor$-error-correcting. Equivalently $d=2t+1$ for odd $d$ and $d=2t+2$ for even $d$.
- In a **linear code** all codewords have identical distance properties. So it suffices to count distances from the all-zero codeword.
- The **weight enumerator function** $A(w)$ is the number of codewords of weight $w$, also called the distance distribution.
- (7,4) Hamming code: $A(0)=1,\ A(3)=7,\ A(4)=7,\ A(7)=1$, total 16 (Fig. 13.1, p. 206).
- The (30,11) dodecahedron code has 2048 codewords in total. Its smallest nonzero weight is 5, with $A(5)=12$ (Fig. 13.2, p. 207).

### 13.2 Obsession with distance (p. 207)
- Since $t$ is the number of errors a code can *guarantee* to correct, many theorists seek codes with the biggest possible $d$. Much practical decoding is built to be optimal for all error patterns up to weight $t$ (p. 206).
- A **bounded-distance decoder** returns the closest codeword if its distance from $\mathbf r$ is $\le t$, and otherwise returns a failure message (p. 207).
- The rationale is "we can't guarantee more than $t$, so we won't bother". MacKay calls this worst-case-ism, a "widespread mental ailment which this book is intended to cure" (p. 207).
- Claim: bounded-distance decoders cannot reach the Shannon limit of the BSC. Only a decoder that often corrects more than $t$ errors can (p. 207).
- Distance categories for code families with rates tending to $R>0$ (p. 207):
  - 'good' distance: $d/N\to$ a constant $>0$;
  - 'bad' distance: $d/N\to0$;
  - 'very bad' distance: $d\to$ a constant.
- Example 13.3: a low-density generator-matrix code has at most $d'$ ones per row of its $K\times N$ generator matrix $\mathbf G$. Its minimum distance is at most $d'$, so its distance is 'very bad' (p. 207).

### 13.3 Perfect codes (pp. 208–209)
- A **$t$-sphere** about $\mathbf x$ is the set of points within Hamming distance $t$ of $\mathbf x$. A code is **perfect $t$-error-correcting** if $t$-spheres centred on its codewords fill Hamming space without overlapping (p. 208).
- Counts: $S=2^K$ codewords; $2^N$ points in the space; a $t$-sphere holds $\sum_{w=0}^t\binom Nw$ points.

$$\sum_{w=0}^{t}\binom{N}{w}\tag{13.1}$$

$$\text{perfect code: } 2^K\sum_{w=0}^{t}\binom Nw=2^N \tag{13.2}$$

$$\text{equivalently } \sum_{w=0}^{t}\binom Nw=2^{N-K} \tag{13.3}$$

The number of noise vectors in one sphere equals the number of syndromes (p. 208). The (7,4) Hamming code satisfies this since

$$1+\binom71=2^3 .\tag{13.4}$$

- Perfect codes would solve Shannon's problem: pick a perfect $t$-error-correcting code with $t=f^*N$, $f^*=f+\delta$, so that more than $t$ flips are unlikely (p. 209).
- The only nontrivial perfect binary codes are (p. 209):
  1. Hamming codes ($t=1$, $N=2^M-1$, rate $\to1$);
  2. repetition codes of odd $N$ ($t=(N-1)/2$, rate $\sim1/N$);
  3. the binary Golay code, a 3-error-correcting code with $2^{12}$ codewords and $N=23$.
- Golay numerology: $1+\binom{23}1+\binom{23}2+\binom{23}3=2^{11}$ (13.5). (Added step: $1+23+253+1771=2048$.)
- Almost-perfect codes are not plentiful. For most codes, good or bad, almost all of Hamming space is *between* the $t$-spheres. The picture in Fig. 13.5 is misleading (p. 209).

*Intuition note:* For most codes in high dimensions, the space between the spheres takes up nearly all of Hamming space. So "fill the space" is the wrong picture of a good code.

**Hamming codes (p. 210).** Choose $M$ parity checks. Then $N=2^M-1$, and the $M\times N$ parity-check matrix has as columns all $N$ nonzero vectors of $M$ bits. All single-bit errors give distinct syndromes and so are corrected. Rates, as (N,K), R: $M=2$: (3,1), 1/3 (repetition code $R_3$); $M=3$: (7,4), 4/7; $M=4$: (15,11), 11/15; $M=5$: (31,26), 26/31; $M=6$: (63,57), 57/63.

### 13.4 Perfectness is unattainable – first proof (pp. 210–211)
Shannon: for a BSC with any $f$, codes exist with rates near $C(f)=1-H_2(f)$ and arbitrarily small error. Typically $\approx fN$ errors occur per block (p. 210).

Take $f\in(1/3,1/2)$ and suppose a large perfect $fN$-error-correcting code exists. Examine three codewords (p. 210):
- Take one as all-zero.
- The second differs from it in a fraction $u+v$ of coordinates. The third differs from the first in $v+w$ and from the second in $u+w$.
- A fraction $x$ of coordinates are zero in all three (Fig. 13.6).

The minimum distance must exceed $2fN$ (p. 210), so

$$u+v>2f,\quad v+w>2f,\quad u+w>2f. \tag{13.6}$$

Summing and dividing by two:

$$u+v+w>3f. \tag{13.7}$$

If $f>1/3$ then $u+v+w>1$, so $x<0$, which is impossible. So no such code can even have three codewords, let alone $2^{NR}$ (p. 211).

*Intuition note:* Three codewords pairwise farther apart than $2fN$ would need more coordinates than exist. Shannon codes for $f>1/3$ exist, but they cannot be perfect.

### 13.5 Weight enumerator function of random linear codes (pp. 211–212)
Take an $M\times N$ parity-check matrix $\mathbf H$ (Fig. 13.7) with random binary entries. For one code, with $\mathbb 1[\cdot]$ the indicator (1 if true, 0 if false),

$$A(w)_{\mathbf H}=\sum_{\mathbf x:|\mathbf x|=w}\mathbb 1[\mathbf H\mathbf x=\mathbf 0]. \tag{13.8}$$

$$\langle A(w)\rangle=\sum_{\mathbf H}P(\mathbf H)A(w)_{\mathbf H} \tag{13.9}$$

$$=\sum_{\mathbf x:|\mathbf x|=w}\ \sum_{\mathbf H}P(\mathbf H)\,\mathbb 1[\mathbf H\mathbf x=\mathbf 0]. \tag{13.10}$$

For a word of weight $w>0$ the probability depends only on $w$. Each of the $M$ syndrome bits $z_m$ is a mod-2 sum of $w$ random bits, so $P(z_m=0)=1/2$. Hence

$$\sum_{\mathbf H}P(\mathbf H)\,\mathbb 1[\mathbf H\mathbf x=\mathbf 0]=(1/2)^M=2^{-M},\tag{13.11}$$

independent of $w$. There are $\binom Nw$ words of weight $w$, so

$$\langle A(w)\rangle=\binom Nw2^{-M}\quad\text{for any }w>0.\tag{13.12}$$

For large $N$, using $\log\binom Nw\simeq NH_2(w/N)$ and $R\simeq 1-M/N$:

$$\log_2\langle A(w)\rangle\simeq NH_2(w/N)-M \tag{13.13}$$

$$\simeq N[H_2(w/N)-(1-R)]\quad\text{for any }w>0.\tag{13.14}$$

Fig. 13.8 shows the case $N=540$, $M=360$ (rate 1/3).

**Gilbert–Varshamov distance.** $\langle A(w)\rangle<1$ if $H_2(w/N)<1-R$ and $>1$ if $H_2(w/N)>1-R$. So the minimum distance of a random linear code is expected, for large $N$, to be near $d_{GV}$ (p. 212):

$$H_2(d_{GV}/N)=1-R,\qquad d_{GV}\equiv NH_2^{-1}(1-R).\tag{13.15}$$

The **Gilbert–Varshamov conjecture**, widely believed, says that for large $N$ binary codes cannot have minimum distance significantly greater than $d_{GV}$. The **Gilbert–Varshamov rate** $R_{GV}$ is the maximum rate for reliable communication with a bounded-distance decoder, assuming the conjecture is true (p. 212).

**Why sphere packing is a bad perspective.** A bounded-distance decoder tolerates a flip fraction $f_{bd}=\frac12 d_{min}/N$. Taking $d_{min}=d_{GV}$ (p. 212):

$$H_2(2f_{bd})=1-R_{GV}\tag{13.16}$$

$$R_{GV}=1-H_2(2f_{bd}).\tag{13.17}$$

Shannon's capacity is

$$C=1-H_2(f),\tag{13.18}$$

so for a given $R$ the maximum noise level Shannon allows satisfies

$$H_2(f)=1-R.\tag{13.19}$$

Comparing (13.16) and (13.19) for a good code of rate $R$:

$$f_{bd}=f/2.\tag{13.20}$$

Bounded-distance decoders can cope with only half the noise level that Shannon proved tolerable (p. 212).

Link to perfectness (p. 213): near the Shannon limit, a typical random linear code sees about $fN$ flips, while its minimum distance is also about $fN$ or a bit more. The $fN$-spheres therefore overlap so much that each almost contains its nearest neighbour's centre. This is not disastrous because, in high dimensions, the overlap volume is a tiny fraction of either sphere (Fig. 13.10). The moral is that worst-case-ism can halve your noise tolerance. You must decode well beyond the minimum distance. Still, the minimum distance can matter in practice because under some conditions it dominates the errors (p. 213).

*Intuition note:* $f_{bd}=f/2$ arises because the guaranteed radius is half the code's distance, while the distance itself is only about $fN$. A decoder that insists on unique decoding inside radius $t$ throws away the typical noise level.

### 13.6 Berlekamp's bats (pp. 213–214)
A blind bat flies about the centre of a cave (one codeword). Its distance from the centre, the noise vector, is set by a friskiness parameter $f$. The cave wall is made of stalactites, each a tiny-volume region like the shaded overlap in Fig. 13.10. A decoding error corresponds to the bat's trajectory passing inside a stalactite (p. 213).
- **Low friskiness (low noise):** collisions are rare and involve the stalactites whose tips are closest to the centre, i.e. low-weight codewords. Here the minimum distance is relevant to the (very small) error probability (p. 213).
- **Higher friskiness:** the bat collides most often with more distant stalactites because there are many more of them. Only a tiny number sit at the minimum distance. So errors depend on the weight enumerator function (p. 214).
- **Very high friskiness:** collisions involve distant stalactites, and the collision frequency has nothing to do with the closest stalactite's distance (p. 214).

### 13.7 Concatenation of Hamming codes (pp. 214–215)
Each Hamming code has $N=2^M-1$, $K=N-M$, $d=3$, and block error $p_B=\frac3N\binom N2f^2$ to leading order (p. 214). Concatenating $C$ Hamming codes with parameters $\{M_c\}$ gives rate

$$R_C=\prod_{c=1}^{C}\frac{N_c-M_c}{N_c}.\tag{13.21}$$

With $M_1=2,M_2=3,M_3=4,\dots$ the asymptotic rate is 0.093 (Fig. 13.12). Blocklength grows very fast with $C$, so these codes are impractical. The product code has distance $3^C$ but $N$ grows faster than $3^C$, so $d/N\to0$: 'bad' distance. By contrast, for typical random codes $H_2(d/N)=1-R$ (p. 214).

Numerically, with the constituent codes decoded one at a time (suboptimal, see section 11.4), for $f=0.0588$ the bit error probability falls towards zero while the rate tends to 0.093 (Fig. 13.14). So this family is 'good' but not 'very good'. 0.0588 is stated to be the highest noise level this concatenated code can tolerate (pp. 214–215). The message is that "distance isn't everything" (p. 215).

*Intuition note:* A code family can have vanishing relative distance and still drive error to zero at a fixed positive rate. Relative distance is therefore not essential for a good code family (MacKay: distance 'isn't everything').

### 13.8 Distance isn't everything (p. 215)
Take a code with two codewords that differ in $d$ places ($d$ even) on a BSC. Only the differing places matter, since the optimal decoder ignores the rest. The error is dominated by $d/2$ flips among them:

$$P(\text{block error})\simeq\binom d{d/2}f^{d/2}(1-f)^{d/2}\tag{13.22}$$

$$\simeq\left[2f^{1/2}(1-f)^{1/2}\right]^d\tag{13.23}$$

$$\equiv[\beta(f)]^d,\tag{13.24}$$

using approximation (1.16) for the binomial. Here $\beta(f)=2f^{1/2}(1-f)^{1/2}$ is the **Bhattacharyya parameter** of the channel.

A general linear code with distance $d$ has block error probability at least $\binom d{d/2}f^{d/2}(1-f)^{d/2}$, independent of $N$. So a sequence of codes with constant $d$ ('very bad' distance) cannot have error tending to zero on any BSC. But pragmatically (p. 215):
- Disk drives need error below about $10^{-18}$ (Chapter 1).
- Raw error 0.001: one codeword at $d=20$ contributes less than $10^{-24}$.
- Raw error 0.01: one codeword at $d=30$ contributes less than $10^{-20}$.
- So good distance is not essential in practice. Codes of blocklength 10 000 with many weight-32 codewords can still correct errors of weight 320 with tiny error probability.

MacKay does not recommend bad-distance codes. His favourite codes, low-density parity-check codes (Chapter 47), have both excellent performance and good distance (p. 216).

### 13.9 The union bound (p. 216)

$$P(\text{block error})\le\sum_{w>0}A(w)[\beta(f)]^w.\tag{13.25}$$

This is a union bound. It is accurate for low noise $f$ but inaccurate for high noise, because it overcounts errors that confuse more than one codeword at once. Exercise 13.6 asks for the rate $R_{UB}(f)$ obtained by using the average $A(w)$ of (13.14). The next chapter will use syndrome decoding plus a union bound to prove the noisy-channel theorem for symmetric binary channels, showing that very good linear codes exist (p. 216).

### 13.10 Dual codes (pp. 216–219)
- An $(N,K)$ linear code has $2^K$ codewords, built from the $K$ rows of the generator matrix $\mathbf G$ ($K\times N$). It is also the set of $\mathbf t$ with $\mathbf H\mathbf t=\mathbf 0$ (13.27), with $\mathbf H$ of shape $M\times N$, $M=N-K$. Each row of $\mathbf H$ is a vector to which codewords are orthogonal (pp. 216–217).
- For the (7,4) Hamming code (13.26):
$$\mathbf G=\begin{bmatrix}1&0&0&0&1&0&1\\0&1&0&0&1&1&0\\0&0&1&0&1&1&1\\0&0&0&1&0&1&1\end{bmatrix}$$
- $\mathbf G$ gives $K$ vectors *from which* all codewords are built. $\mathbf H$ gives $M$ vectors *to which* all codewords are orthogonal. The **dual** $\mathcal C^\perp$ is the set of all length-$N$ vectors orthogonal to all codewords. It is obtained by exchanging $\mathbf G$ and $\mathbf H$, and equals the set of all combinations of the rows of $\mathbf H$ (p. 217).
- (7,4) Hamming parity-check matrix (13.28), $\mathbf H=[\mathbf P\ \mathbf I_3]$:
$$\mathbf H=\begin{bmatrix}1&1&1&0&1&0&0\\0&1&1&1&0&1&0\\1&0&1&1&0&0&1\end{bmatrix}$$
  Its dual has eight codewords (Table 13.16: 0000000, 0010111, 0101101, 0111010, 1001110, 1011001, 1100011, 1110100). Every dual codeword is a codeword of the Hamming code:
$$\mathcal H_{(7,4)}^\perp\subset\mathcal H_{(7,4)}.\tag{13.29}$$
  This is possible because in mod-2 arithmetic many nonzero vectors are orthogonal to themselves. Result (solution to Ex. 13.7): a binary vector is orthogonal to itself if it has even weight, i.e. an even number of ones (p. 223); the exercise asks for a rule that distinguishes the cases.
- Systematic form: $\mathbf G=[\mathbf I_K|\mathbf P^{\mathsf T}]$ (13.30) goes with $\mathbf H=[\mathbf P|\mathbf I_M]$ (13.31), where $\mathbf P$ is $K\times M$ (p. 217).
- **Example 13.8 (p. 218).** $R_3$ has $\mathbf G=[1\ 1\ 1]$ (13.32), $\mathbf H=\begin{bmatrix}1&1&0\\1&0&1\end{bmatrix}$ (13.33), and codewords [1 1 1], [0 0 0]. The dual has generator matrix $\mathbf G^\perp=\mathbf H$ (13.34), or in systematic form $\begin{bmatrix}1&0&1\\0&1&1\end{bmatrix}$ (13.35). This is the simple parity code $P_3$, with codewords [1 1 0], [1 0 1], [0 0 0], [0 1 1]. Here the only vector common to code and dual is the all-zero codeword.
- **Goodness of duals (p. 218).** Examples exist of good codes with good duals (random linear codes), bad with bad, and good with bad duals. The last case is important: many state-of-the-art codes have bad duals. The classic example is the low-density parity-check code, whose dual is a low-density generator-matrix code. Exercise 13.9 asks to show that low-density generator-matrix codes are bad. Exercise 13.10 asks to show that LDPC codes are good with good distance (solutions in Gallager 1963, MacKay 1999b).
- **Self-orthogonal and self-dual (pp. 218–219).** A code is self-orthogonal if contained in its dual, e.g. the dual of the (7,4) Hamming code. One way to see this is that the overlap between any pair of rows of $\mathbf H$ is even. Such codes matter in quantum error correction (Calderbank and Shor, 1996). A code is self-dual if
$$\mathcal C^\perp=\mathcal C.\tag{13.36}$$
  Properties deduced: (1) $\mathbf G$ is also a parity-check matrix; (2) rate 1/2, $M=K=N/2$; (3) all codewords have even weight (p. 219).
- **Examples.** $R_2$: $\mathbf G=\mathbf H=[1\ 1]$ (13.37). The smallest nontrivial self-dual code is the (8,4) code (13.38), $\mathbf G=[\mathbf I_4|\mathbf P^{\mathsf T}]$ with $\mathbf P^{\mathsf T}$ rows 0111, 1011, 1101, 1110 (p. 219).
- **Solution to Ex. 13.11 (p. 223).** If $\mathbf G=[\mathbf I_K|\mathbf P^{\mathsf T}]$ is self-dual, then $\mathbf H_1=\mathbf G=[\mathbf I_K|\mathbf P^{\mathsf T}]$ and $\mathbf H_2=[\mathbf P|\mathbf I_K]$ are equivalent by row additions: $\mathbf U\mathbf H_2=\mathbf H_1$, i.e. $[\mathbf U\mathbf P|\mathbf U\mathbf I_K]=[\mathbf I_K|\mathbf P^{\mathsf T}]$ (13.42). So $\mathbf U=\mathbf P^{\mathsf T}$, giving
$$\mathbf P^{\mathsf T}\mathbf P=\mathbf I_K.\tag{13.43}$$
  So $\mathbf P$ is orthogonal mod 2 (and vice versa).
- **Solution to Ex. 13.12 (p. 223).** The (8,4) code has parity-check matrix $[\mathbf P\ \mathbf I_4]$ (13.44). It is obtained from the (7,4) Hamming code by (a) appending an extra parity bit, the parity of all seven bits, and (b) reordering the first four bits.
- **Duals and graphs (p. 219).** Represent a code by a graph of parity-check nodes and equality nodes joined by edges (bits). The dual's graph swaps the two node types. Forney (2001) calls this a normal graph.
- **Further reading (p. 219).** Functions on a code, such as the posterior over codewords, can be Fourier transformed into functions over the dual code (Terras 1999; MacWilliams and Sloane 1977).

*Intuition note:* The dual swaps "what builds codewords" and "what checks codewords". Because arithmetic is mod 2, a code and its dual can overlap, even coincide.

### 13.11 Generalizing perfectness to other channels (pp. 219–220)
- A "perfect $u$-error-correcting code for the binary erasure channel" restores any $u$ erased bits and never more. The usual term is **maximum distance separable (MDS) code**. It needs $N-K=u$ redundant bits (margin note, p. 219).
- The (7,4) Hamming code is not MDS. It recovers some sets of 3 erased bits but not all. If the 3 erased bits form a weight-3 codeword, one bit of information is lost, so it is a poor choice for a RAID system (p. 219).
- The simple parity code $P_3$ ($\mathbf H=[1\ 1\ 1]$) is MDS. It has 4 codewords, all of even parity, at distance 2. An erased bit is restored as the parity of the other two. Repetition codes are also MDS (p. 220).
- For the $q$-ary erasure channel with $q>2$, large numbers of MDS codes exist. Reed–Solomon codes are the most famous and widely used. If the field size $q$ exceeds the blocklength $N$, MDS block codes of any rate can be found (p. 220).
- **Solution to Ex. 13.13 (p. 224).** An $(N,K)$ code that recovers from any $M=N-K$ erasures is MDS. No MDS binary codes exist apart from repetition and simple parity codes. For $q>2$ some exist. Example: a (9,2) code for the 8-ary erasure channel over GF(8), with $\mathbf G=\begin{bmatrix}1&0&1&A&B&C&D&E&F\\0&1&1&1&1&1&1&1&1\end{bmatrix}$ (13.45), giving 64 codewords.

### 13.12 Summary (p. 220)
Shannon's BSC codes can almost always correct $fN$ errors but are not $fN$-error-correcting codes. Reasons why distance has little relevance:
1. The best codes must cope with noise twice as large as a bounded-distance decoder can.
2. When $f>1/4$, no code with a bounded-distance decoder can communicate at all, yet Shannon says good codes exist for such channels.
3. Concatenation shows that good performance is possible with bad distance.

The whole weight enumerator function is relevant to whether a code is good.

### 13.13 Further exercises and 13.14 Solutions (pp. 220–227)
**Theorem 13.1 (p. 221).** If a binary linear code has minimum distance $d_{min}$, then for any given channel the bit error probability $p_b$ of the optimal bitwise decoder and the block error probability $p_B$ of the maximum likelihood decoder satisfy

$$p_B\ge p_b\ge\frac12\frac{d_{min}}{N}p_B.\tag{13.39}$$

(Setting: a codeword from a linear $(N,K)$ code is sent over a memoryless channel $P(\mathbf y|\mathbf t)$ (p. 220).)

*Quick rough proof (p. 224).* Let $\mathbf x$ be the difference between reconstructed and transmitted codewords. Given the output $\mathbf r$, the posterior $P(\mathbf x|\mathbf r)$ is positive only on codewords.

$$p_B=\sum_{\mathbf x\ne0}P(\mathbf x|\mathbf r)\tag{13.46}$$

$$p_b=\sum_{\mathbf x\ne0}P(\mathbf x|\mathbf r)\frac{w(\mathbf x)}{N}\tag{13.47}$$

Nonzero codeword weights satisfy $1\ge w(\mathbf x)/N\ge d_{min}/N$ (13.48). So $p_B\ge p_b\ge\frac{d_{min}}Np_B$ (13.49). This is a factor of two stronger than (13.39); the careful proof weakens it slightly.

*Careful proof (pp. 224–226).* Decoders: the optimal block decoder maximizes $P(\mathbf x|\mathbf r)$, which is proportional to the likelihood (error $p_B$). The optimal bit decoder maximizes each $P(x_n=a|\mathbf r)$ (error $p_b$). The block-guessing decoder samples a codeword from the posterior (error $p_B^G$). The bit-guessing decoder samples each bit from its marginal posterior (error $p_b^G$).
- Left inequality: if a block is correct, all its bits are correct, so the optimal block decoder cannot beat the optimal bit decoder.
- (a) $p_b^G\le2p_b$ (13.50). For one bit with posterior $\{p_0,p_1\}$, $P^{optimal}=\min(p_0,p_1)$ (13.53). The guesser's error is $P^{guess}=2p_0p_1\le2\min(p_0,p_1)=2P^{optimal}$ (13.54). Averaging over bits gives (13.50).
- (b) $p_b^G\ge\frac{d_{min}}Np_B^G$ (13.51). Draw $(x_n,\mathbf x)$ jointly and discard $\mathbf x$. Then $p_b^G=P(\mathbf x\text{ correct})\cdot0+p_B^GP(\text{bit error}|\mathbf x\text{ incorrect})$. Whenever the guessed $\mathbf x$ is wrong, it differs from the truth in at least $d$ bits, so the bit error probability is at least $d/N$.
- Since $p_B^G\ge p_B$: $p_b\ge\frac12p_b^G\ge\frac12\frac{d_{min}}Np_B^G\ge\frac12\frac{d_{min}}Np_B$ (13.52).

*Intuition note:* A wrong codeword differs from the truth in at least $d_{min}$ of $N$ bits. So a block error costs at least a fraction $d_{min}/N$ of bit errors. Guessing from the posterior loses at most a factor 2 relative to optimal bit decoding.

**Solution to Ex. 13.20 (p. 226).** The number of typical noise vectors is roughly $2^{NH_2(f)}$ and the number of syndromes is $2^M$. Reliable communication needs $M\ge NH_2(f)$ (13.55), i.e. $R\le1-H_2(f)$ (13.56). This agrees precisely with the capacity. The next chapter turns the argument into a proof.

**Solution to Ex. 13.24, hat puzzle (pp. 226–227).** For three players the group can win 3/4 of the time. Each player passes if the other two hats differ, and otherwise guesses that his own hat has the opposite colour. Whenever the hats split 2–1 exactly one player guesses, correctly. When all hats match (probability 1/4) all three guess wrongly. For $N=2^r-1$ players, the optimal strategy uses a Hamming code of length $N$ and wins with probability $N/(N+1)$ (7/8 for 7 players, 15/16 for 15). Hat states map to binary vectors. A random vector is a codeword with probability $1/(N+1)$, and otherwise differs from a codeword in exactly one bit. Each player guesses the colour that would make the state a non-codeword whenever the state could be completed to a codeword by his own bit. If the state is a codeword, all guess wrong. Otherwise only one player guesses, and he is right.

**Other exercises (pp. 221–223).** They cover: minimum distance of Hamming codes (13.15); $\langle A(1)\rangle$ for $N=540,M=360$ (13.16); a (15,5) code, a Petersen-graph LDPC code and a replication of Fig. 13.12 (13.17–13.19); the Z-channel and linear codes, where the printed answer is "about 6%" (13.21); very bad distance implies bad codes (13.22); puncturing, shortening and intersection (13.23); counting LDPC codes with self-orthogonal duals (13.25); a Gaussian-channel version of Fig. 13.15 (13.26).

## Toy example (ours, not from the text)
Code of length 6 with three codewords: $\mathbf c_1=000000$, $\mathbf c_2=111100$, $\mathbf c_3=001111$.

- Distances: $d(\mathbf c_1,\mathbf c_2)=4$ and $d(\mathbf c_1,\mathbf c_3)=4$. $\mathbf c_2\oplus\mathbf c_3=110011$ has weight 4, so $d(\mathbf c_2,\mathbf c_3)=4$. So $d=4$ and $t=\lfloor3/2\rfloor=1$. The enumerator is $A(0)=1$, $A(4)=2$.
- Send $\mathbf c_1$ over a BSC; two bits (positions 1 and 6) flip, so $\mathbf r=100001$.
- Distances from $\mathbf r$: to $\mathbf c_1$ the weight is 2. To $\mathbf c_2$, $100001\oplus111100=011101$ has weight 4. To $\mathbf c_3$, $100001\oplus001111=101110$ has weight 4.
- A bounded-distance decoder (radius $t=1$) sees no codeword within 1, so it reports failure. The nearest-codeword decoder returns $\mathbf c_1$, correctly, since 2 < 4 for both other codewords. It corrects a pattern of weight $2>t$.
- Error contribution of one weight-4 codeword at $f=0.01$ by (13.22): $\binom42f^2(1-f)^2=6\times0.0001\times0.9801\approx5.9\times10^{-4}$.

This shows the chapter's point on a tiny scale: guaranteed radius $t$ undersells what an optimal decoder can do.

## Concepts
- [[hamming-distance]] (new) — number of coordinates in which two binary vectors differ (p. 206)
- [[minimum-distance]] (new) — smallest separation between two codewords; a code corrects $\lfloor(d-1)/2\rfloor$ errors (p. 206)
- [[weight-enumerator-function]] (new) — $A(w)$, the number of codewords of weight $w$; for linear codes it describes all distances (p. 206)
- [[bounded-distance-decoder]] (new) — decodes only if within $t$ of a codeword; cannot reach the Shannon limit (p. 207)
- [[worst-case-ism]] (new) — MacKay's term for designing only for guaranteed correction patterns (p. 207)
- [[good-bad-distance]] (new) — good: $d/N\to$ constant $>0$; bad: $d/N\to0$; very bad: $d\to$ constant (p. 207)
- [[perfect-code]] (new) — $t$-spheres around codewords fill Hamming space without overlap (p. 208)
- [[hamming-code]] (new) — single-error-correcting code whose $\mathbf H$ columns are all nonzero $M$-bit vectors, $N=2^M-1$ (p. 210)
- [[gilbert-varshamov-distance]] (new) — $d_{GV}=NH_2^{-1}(1-R)$, the typical minimum distance of random linear codes (p. 212)
- [[bhattacharyya-parameter]] (new) — $\beta(f)=2f^{1/2}(1-f)^{1/2}$; one weight-$d$ codeword gives error about $\beta^d$ (p. 215)
- [[union-bound]] (new) — $P(\text{block error})\le\sum_{w>0}A(w)\beta(f)^w$ (p. 216)
- [[dual-code]] (new) — all vectors orthogonal to every codeword; swap $\mathbf G$ and $\mathbf H$ (p. 217)
- [[self-dual-code]] (new) — a code with $\mathcal C^\perp=\mathcal C$; rate 1/2, even weights (p. 218)
- [[mds-code]] (new) — a code recovering any $N-K$ erasures; the erasure-channel analogue of perfect (p. 219)
- [[concatenated-code]] (new) — several codes applied in succession; rate is the product of the rates (p. 214)
- [[noisy-channel]], [[channel-capacity]], [[noisy-channel-coding-theorem]], [[error-correcting-code]] — used as in the canon; here for the BSC with $C=1-H_2(f)$ (p. 212)
- [[posterior-distribution]] — optimal decoders maximize the posterior over codewords or bits (p. 225)

## Canonical instances
- [[hamming-7-4-code]] — perfect, $d=3$, $A(w)=1,7,7,1$ (pp. 206, 208)
- [[binary-golay-code]] — 3-error-correcting perfect code, $N=23$, $2^{12}$ codewords (p. 209)
- [[repetition-code-r3]] — perfect; dual is the simple parity code $P_3$; MDS (pp. 218, 220)
- [[berlekamps-bats]] — picture of when minimum distance matters (p. 213)
- [[concatenated-hamming-codes]] — bad distance yet good code family; rate 0.093 at $f=0.0588$ (pp. 214–215)
- [[ebert-hat-puzzle]] — optimal strategy uses a Hamming code (pp. 222, 226–227)
- [[reed-solomon-codes]] — famous MDS codes for $q$-ary erasure channels (p. 220)

## Bridges (candidates)
- [same-math] Hat-puzzle strategy ↔ coding: Hamming-code decoding (win prob. $N/(N+1)$) — the strategy literally uses the code's decoder (p. 227).
- [same-math] Optimal block and bit decoding ↔ Bayesian: MAP codeword vs marginal posterior per bit — the text defines both decoders from $P(\mathbf x|\mathbf r)$ (p. 225).
- [structural-analogy] Sphere overlap "not disastrous" in high dimensions ↔ typical set: probability sits in tiny-volume regions, not where volume intuition suggests.
- [structural-analogy] Berlekamp's bats ↔ rare-event analysis: which terms of a weight-sum dominate depends on the noise level.
- [metaphor] Worst-case-ism ↔ guaranteed-correction design versus average-case probabilistic performance.

## Questions this raises
- If the whole weight enumerator matters, which features of $A(w)$ make a code good beyond $d_{min}$?
- How close can a syndrome decoder with a union bound get to capacity (the next chapter's proof)?
- Why should many state-of-the-art codes (LDPC) have bad duals, and what use is the dual's goodness?
- Does the "decode beyond $t$" lesson carry over to non-binary or non-symmetric channels, such as the Gaussian channel (Ex. 13.26)?

## Exercises worth doing
- Ex. 13.5 (p. 215) — families with 'bad' distance can still be 'very good' codes — difficulty: medium
- Ex. 13.6 (p. 216) — "poor man's" capacity from the union bound and random-code $A(w)$ — difficulty: medium
- Ex. 13.9 (p. 218) — low-density generator-matrix codes are bad, via low-weight codewords — difficulty: medium
- Ex. 13.16 (p. 221) — estimate $\langle A(1)\rangle$ for the $N=540$, $M=360$ random code — difficulty: easy
- Ex. 13.19 (p. 221) — replicate the concatenated-Hamming rate and noise-level calculations — difficulty: medium

## Reading notes
- Printed page = pdf − 12 (pdf 217 = printed 205). Page labels carry printed numbers.
- Equations were checked against page images. In (13.52) the printed first inequality is "$p_b>\frac12p_b^G$"; given (13.50) it should read "$\ge$". I kept this as a likely misprint.
- The (9,2) code's list of 64 codewords on p. 224 is not reproduced here.
- The dodecahedron code's weight table (p. 207) is only summarized.
- Section 13.12's claim 2 ("$f>1/4$, no bounded-distance code communicates") is stated without derivation on p. 220.
- Ex. 13.17–13.19 and 13.26 carry a 'C' in their difficulty marker (e.g. [3C]); Ex. 13.18 says 'Using a computer', but these pages do not explain the marker.
- The margin hat-puzzle variants ('Scottish', 'Reformed Scottish', p. 223) are not treated here.
