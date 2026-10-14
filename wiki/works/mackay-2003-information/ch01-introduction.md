---
id: mackay-2003-information/ch01-introduction
work: mackay-2003-information
unit: "About Chapter 1 + Chapter 1: Introduction to Information Theory"
pages: 1-21
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Introduction to Information Theory (MacKay, ch. 1, with the "About Chapter 1" primer)

## L0 — One line
Adding structured redundancy lets us correct errors from a noisy channel, and Shannon showed that arbitrarily small error is possible at a non-zero rate, up to the channel capacity C.

## L1 — The gist (≤ 120 words)
How can we communicate reliably over a noisy channel such as a disk drive? Repetition codes lower the error probability but cut the rate: about 60 noisy drives are needed to reach error probability 10⁻¹⁵ when f = 0.1. The (7,4) Hamming code corrects any single flipped bit in a block at rate 4/7. Decoding is Bayesian inference: pick the most probable source given the received bits. Shannon's noisy-channel coding theorem says that for any channel there are codes with arbitrarily small error at rates up to the capacity (C ≃ 0.53 for f = 0.1). The first half of the book (Parts I–III) is devoted to understanding this result (p. 14). The unit also sets out the binomial distribution and Stirling's approximation.

**Prerequisites:** probability basics (Bayes' theorem, independence); binomial coefficients; logarithms; matrix–vector multiplication; arithmetic modulo 2.

## L2 — Key ideas (5–10 bullets)
- Two ways to get reliable communication: improve the physical channel (incremental gains at an ever-increasing cost), or add an encoder and decoder that use redundancy to detect and correct errors (cost is computation) (pp. 4–5).
- Repetition code R₃ with majority vote has p_b ≈ 3f², but its rate falls to 1/3; reaching 10⁻¹⁵ at f = 0.1 needs about 60 repetitions (pp. 7–8, 16–17).
- Majority-vote decoding is the optimal decoder, in the sense of smallest error probability, if the channel is a binary symmetric channel with f < 0.5 and the two source bits are equally likely a priori. This follows from Bayes' theorem and likelihood ratios (pp. 6–7).
- The (7,4) Hamming code adds three parity bits. The syndrome (the pattern of violated parity checks) points to the single most probable flipped bit. Its error probability is also O(f²), at the better rate 4/7 (pp. 9–13).
- Counting syndromes limits what linear codes can do: a (14,8) code cannot correct all double errors, and the same counting works for nonlinear codes (pp. 20–21).
- Shannon: the boundary between achievable and non-achievable (R, p_b) meets the R axis at C = 1 − H₂(f), not at the origin. Reliable communication at any rate above C is impossible (pp. 14–16).
- Stirling's approximation gives log₂ C(N,r) ≃ N·H₂(r/N), linking binomial counting to entropy (pp. 2, 16).

## L3 — Walkthrough

### About Chapter 1: mathematical primer (pp. 1–2)

**Binomial distribution (Example 1.1).** A bent coin shows heads with probability f. It is tossed N times, and r is the number of heads. Then
$$P(r\mid f,N)=\binom{N}{r}f^{r}(1-f)^{N-r}.\tag{1.1}$$
Mean and variance are defined as
$$\mathcal E[r]\equiv\sum_{r=0}^{N}P(r\mid f,N)\,r,\tag{1.2}$$
$$\operatorname{var}[r]\equiv\mathcal E[(r-\mathcal E[r])^2]=\mathcal E[r^2]-(\mathcal E[r])^2=\sum_{r=0}^{N}P(r\mid f,N)r^2-(\mathcal E[r])^2.\tag{1.3, 1.4}$$
(p. 1). Instead of evaluating the sums, write r as a sum of N independent single-toss variables and use
$$\mathcal E[x+y]=\mathcal E[x]+\mathcal E[y]\ \text{(any } x,y),\qquad \operatorname{var}[x+y]=\operatorname{var}[x]+\operatorname{var}[y]\ \text{(if } x,y \text{ independent)}.\tag{1.5}$$
One toss has mean $f\cdot1+(1-f)\cdot0=f$ and variance $[f\cdot1^2+(1-f)\cdot0^2]-f^2=f-f^2=f(1-f)$ (1.6). Hence
$$\mathcal E[r]=Nf,\qquad \operatorname{var}[r]=Nf(1-f).\tag{1.7}$$
(p. 1)

**Stirling's approximation by an "unconventional route" (p. 2).**
1. Start from the Poisson distribution with mean λ: $P(r\mid\lambda)=e^{-\lambda}\lambda^r/r!$ for $r\in\{0,1,2,\dots\}$ (1.8).
2. For large λ, at least near r ≃ λ, it is well approximated by a Gaussian with mean λ and variance λ:
$$e^{-\lambda}\frac{\lambda^r}{r!}\simeq\frac{1}{\sqrt{2\pi\lambda}}e^{-(r-\lambda)^2/2\lambda}.\tag{1.9}$$
3. Put r = λ: $e^{-\lambda}\lambda^\lambda/\lambda!\simeq 1/\sqrt{2\pi\lambda}$ (1.10). So $\lambda!\simeq\lambda^\lambda e^{-\lambda}\sqrt{2\pi\lambda}$ (1.11).
4. Therefore
$$x!\simeq x^xe^{-x}\sqrt{2\pi x}\iff \ln x!\simeq x\ln x-x+\tfrac12\ln 2\pi x.\tag{1.12}$$
The author notes this gives the leading behaviour $x^xe^{-x}$ and also the correction factor $\sqrt{2\pi x}$.

**Binomial coefficients and binary entropy (p. 2).** Applying (1.12) to the binomial coefficient:
$$\ln\binom Nr\equiv\ln\frac{N!}{(N-r)!\,r!}\simeq (N-r)\ln\frac{N}{N-r}+r\ln\frac Nr.\tag{1.13}$$
All terms are logarithms, so any base works. "ln" means natural log and "log" means base 2. The **binary entropy function** is
$$H_2(x)\equiv x\log\frac1x+(1-x)\log\frac1{1-x}.\tag{1.14}$$
Then
$$\log\binom Nr\simeq N H_2(r/N),\quad\text{i.e.}\quad \binom Nr\simeq 2^{NH_2(r/N)}.\tag{1.15, 1.16}$$
Keeping the next-order Stirling term:
$$\log\binom Nr\simeq NH_2(r/N)-\tfrac12\log\Big[2\pi N\frac{N-r}{N}\frac rN\Big].\tag{1.17}$$
Figure 1.3 shows $H_2$ on [0,1]. It is 0 at both ends and has its maximum, 1, at x = 0.5.

*Intuition note.* The number of ways to place r heads among N tosses grows like $2^{N H_2(r/N)}$. So $H_2$ gives the exponential growth rate of this count. The approximation is used in the solution to Exercise 1.3 (p. 16).

### 1.1 How can we achieve perfect communication over an imperfect, noisy channel? (pp. 3–5)

- Shannon's framing (1948): the fundamental problem is reproducing at one point, exactly or approximately, a message selected at another point (p. 3).
- Examples of noisy channels: modems over a phone line; Galileo's radio link to Earth; DNA copying from parent to daughter cells; a disk drive. In a disk drive the data go from one *time* to a later time, not from one place to another (p. 3).
- In every case, the received message may differ from the transmitted one with some probability (pp. 3–4).
- **Binary symmetric channel (BSC):** each bit is received correctly with probability 1−f and flipped with probability f. $P(y{=}0\mid x{=}0)=P(y{=}1\mid x{=}1)=1-f$ and $P(y{=}1\mid x{=}0)=P(y{=}0\mid x{=}1)=f$ (fig. 1.4, p. 4).
- Example: f = 0.1. A gigabyte per day for ten years requires a bit-error probability of order 10⁻¹⁵ or smaller (p. 4).
- **Physical solution:** better components, evacuating the air from the enclosure, bigger magnetic patches, higher-power signals or cooling. These typically raise cost (p. 4).
- **System solution:** accept the channel as it is. Add an encoder (turns source message **s** into transmitted message **t**, adding redundancy) and a decoder (uses the known redundancy to infer both **s** and the noise, from received **r**) (p. 4, fig. 1.6, p. 5).
- The author contrasts the two. Physical fixes give incremental improvement at ever-increasing cost. System solutions can make reliable channels with only a computational cost (p. 5).
- *Information theory* studies the theoretical limits and potentials ("What is the best error-correcting performance we could achieve?"). *Coding theory* creates practical encoders and decoders (p. 5).

### 1.2 Error-correcting codes for the binary symmetric channel (pp. 5–14)

Rules of the game: errors must be both detected and corrected; retransmission is not allowed (p. 5).

**Repetition codes.** R₃ encodes each source bit by repeating it three times (0 → 000, 1 → 111; table 1.7). The channel is described as adding a sparse noise vector **n** to **t**, in modulo-2 arithmetic (1+1 = 0), so **r** = **t** + **n** (p. 5). Figure 1.8 gives an example with **s** = 0010110.

*Optimal decoding of R₃ (pp. 6–7).*
1. "Optimal" means smallest probability of being wrong. The decoder should choose the s that is most probable given **r**.
2. Bayes' theorem: $P(s\mid r_1r_2r_3)=P(r_1r_2r_3\mid s)P(s)/P(r_1r_2r_3)$ (1.18). The posterior for s = 1 and s = 0 is written out in (1.19) and (1.20).
3. The posterior is the prior P(s) times the likelihood $P(\mathbf r\mid s)$. The normalizer $P(r_1r_2r_3)$ need not be computed. The rule is: guess ŝ = 0 if $P(s{=}0\mid\mathbf r)>P(s{=}1\mid\mathbf r)$, otherwise ŝ = 1 (p. 6).
4. Assumptions: equal priors $P(s{=}0)=P(s{=}1)=0.5$, so maximizing the posterior equals maximizing the likelihood. The channel is a BSC with f < 0.5, so
$$P(\mathbf r\mid s)=P(\mathbf r\mid\mathbf t(s))=\prod_{n=1}^NP(r_n\mid t_n(s)),\tag{1.21}$$
$$P(r_n\mid t_n)=\begin{cases}1-f&r_n=t_n\\ f&r_n\ne t_n.\end{cases}\tag{1.22}$$
Here N = 3.
5. Likelihood ratio:
$$\frac{P(\mathbf r\mid s{=}1)}{P(\mathbf r\mid s{=}0)}=\prod_{n=1}^N\frac{P(r_n\mid t_n(1))}{P(r_n\mid t_n(0))}.\tag{1.23}$$
Each factor is $(1-f)/f$ if $r_n=1$ and $f/(1-f)$ if $r_n=0$. With $\gamma\equiv(1-f)/f>1$ (because f < 0.5), the winner is the hypothesis with the most "votes", each vote counting a factor γ.
6. Algorithm 1.9 tabulates this. The ratio is γ⁻³ for 000, γ⁻¹ for 001, 010, 100, γ¹ for 101, 110, 011, and γ³ for 111. The decoded bit is 0 for the first four and 1 for the last four (p. 6).
7. Conclusion: majority vote is the optimal decoder if the channel is a BSC (f < 0.5) and the two source messages have equal prior probability (p. 7).

*Applying it (p. 7).* In figure 1.8, the second triplet (001) has one error, which majority vote corrects. The fifth triplet has two errors (010 decoded as 0, but the source bit was 1), which is wrong (fig. 1.10).

*Exercise 1.2 result (solution, p. 16).* R₃ errs if two or more bits in a block flip. Since P(r = 2) and P(r = 3) come from example 1.1:
$$p_b=p_B=3f^2(1-f)+f^3=3f^2-2f^3.\tag{1.36}$$
For small f this is dominated by 3f². At f = 0.1 the text gives p_b ≃ 0.03 (p. 7). The **rate** falls to 1/3 (fig. 1.11, p. 7). So three noisy gigabyte drives are needed to build one gigabyte drive with p_b = 0.03 (p. 8).

*Exercise 1.3 (R_N for odd N) (pp. 8, 16–17).* The error probability is
$$p_b=\sum_{n=(N+1)/2}^{N}\binom Nn f^n(1-f)^{N-n}.\tag{1.24}$$
- Dominant term: $\binom{N}{\lceil N/2\rceil}f^{(N+1)/2}(1-f)^{(N-1)/2}$ (1.37).
- First approximation: $\frac1{N+1}2^{NH_2(K/N)}\le\binom NK\le2^{NH_2(K/N)}$, so $\binom NK\simeq2^{NH_2(K/N)}$ (1.38). This is in error by a factor of order √N, as in (1.17).
- Then $p_b\simeq2^N(f(1-f))^{N/2}=(4f(1-f))^{N/2}$ (1.39). Setting this to 10⁻¹⁵ with f = 0.1 gives $N\simeq2\log10^{-15}/\log4f(1-f)=68$. This is a little too large because the approximation overestimates $\binom NK$ and ⌈N/2⌉ was not distinguished from N/2.
- Better: $\binom N{N/2}\simeq2^N/\sqrt{2\pi N/4}$ (1.40). The author proves this from an accurate Stirling formula, or from the binomial with p = 1/2 summed as a Gaussian with $\sigma=\sqrt{N/4}$: $1\simeq2^{-N}\binom N{N/2}\sqrt{2\pi}\sigma$ (1.41).
- Then $p_b\simeq\frac1{\sqrt{\pi N/8}}f[4f(1-f)]^{(N-1)/2}$ (1.42, 1.43).
- Solving $p_b=10^{-15}$ gives $(N-1)/2\simeq[\log10^{-15}+\log(\sqrt{\pi N/8}/f)]/\log4f(1-f)$ (1.44). Iterating from N̂₁ = 68: $(\hat N_2-1)/2\simeq(-15+1.7)/(-0.44)=29.9$, so N̂₂ ≃ 60.9 (1.45). It is stable, so N ≃ 61. The exercise text states "about 60" (p. 8).
- Consequence: a single gigabyte drive with p_b ≈ 10⁻¹⁵ needs about sixty noisy drives at f = 0.1 (p. 8). Figure 1.12 shows the rate/error trade-off for repetition codes: lower p_b only with lower rate (p. 8).

*Intuition note.* Repetition buys reliability with rate: error probability drops exponentially in N, but rate is 1/N. The approach works, but reaching 10⁻¹⁵ at f = 0.1 needs about sixty noisy drives.

**Block codes: the (7,4) Hamming code (pp. 8–13).**
- A **block code** maps K source bits **s** to N transmitted bits **t**, with N > K. In a **linear** block code the extra N−K bits (**parity-check bits**) are linear functions of the K source bits. The (7,4) Hamming code has N = 7, K = 4 (p. 9).
- *Encoding (fig. 1.13).* Arrange the 7 bits in three intersecting circles. t₁t₂t₃t₄ = s₁s₂s₃s₄. The parity bits t₅, t₆, t₇ make each circle's parity even: t₅ is the parity of s₁s₂s₃, t₆ of s₂s₃s₄, t₇ of s₁s₃s₄. Example: **s** = 1000 gives **t** = 1000101. Table 1.14 lists all 2⁴ = 16 codewords. Any pair of codewords differ in at least three bits (p. 9).
- *Matrix form.* With **s**, **t** as column vectors, $\mathbf t=\mathbf G^{\mathsf T}\mathbf s$ (1.25), modulo 2, with
$$\mathbf G^{\mathsf T}=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\\1&1&1&0\\0&1&1&1\\1&0&1&1\end{bmatrix}\ (7\times4).\tag{1.26}$$
For row vectors, $\mathbf t=\mathbf s\mathbf G$ (1.27) with
$$\mathbf G=\begin{bmatrix}1&0&0&0&1&0&1\\0&1&0&0&1&1&0\\0&0&1&0&1&1&1\\0&0&0&1&0&1&1\end{bmatrix}\ (4\times7).\tag{1.28}$$
The rows of **G** are four basis vectors in a 7-dimensional binary space, and the 16 codewords are all their linear combinations (p. 10).

*Decoding (p. 10).* Any bit, including parity bits, may flip. If the channel is a BSC and all source vectors are equiprobable, the optimal decoder picks the **s** whose **t**(**s**) differs from **r** in the fewest bits (via the likelihood (1.23)). Checking all 16 codewords would work; the author asks whether there is a more efficient way, and answers with syndrome decoding below.

*Syndrome decoding (pictorial; pp. 10–11).*
1. Write **r** into the three circles. A circle whose parity is not even is "unhappy". The pattern of violations is the **syndrome** **z**. Example: **t** = 1000101, noise flips bit 2, **r** = 1100101. Circles 1 and 2 are unhappy, circle 3 is happy, so **z** = (1,1,0).
2. Find the smallest set of flipped bits that explains the syndrome. Ask whether a unique bit lies inside all unhappy circles and outside all happy ones. Here r₂ is the only such bit.
3. Other cases (fig. 1.15): t₅ flipped violates one check, so r₅ is the suspect. The central bit r₃ flipped violates all three, so r₃ is the suspect.
4. Flipping any one of the 7 bits gives 7 different non-zero syndromes. The only other syndrome is 000. Algorithm 1.16 (checks in the order r₅, r₆, r₇):

| z | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---|---|---|---|---|---|---|---|
| unflip | none | r₇ | r₆ | r₄ | r₅ | r₁ | r₂ | r₃ |

5. For a BSC with small f, the optimal decoder unflips at most one bit. A given syndrome can come from other noise patterns, but any such pattern is less probable because it involves more noise events (p. 11).
6. If two bits flip (e.g. r₃ and r₇ in fig. 1.15e; syndrome 110), the decoder flips r₂, and the decoded vector has three errors. Any two-bit error pattern leads to a decoded 7-bit vector with three errors (p. 11).

*General linear-code syndrome decoding (pp. 11–12).* The received bits r₁…r₄ purport to be source bits, and r₅r₆r₇ purport to be their parities. The syndrome is the modulo-2 difference between the recomputed parities and the received r₅r₆r₇. If it is zero, **r** is a codeword and the decoding is its first four bits. Writing $\mathbf G^{\mathsf T}=\begin{bmatrix}\mathbf I_4\\ \mathbf P\end{bmatrix}$ (1.29), with **P** a 3×4 matrix, the syndrome is $\mathbf z=\mathbf H\mathbf r$ with $\mathbf H=[-\mathbf P\ \ \mathbf I_3]$. Modulo 2, −1 ≡ 1, so
$$\mathbf H=[\mathbf P\ \ \mathbf I_3]=\begin{bmatrix}1&1&1&0&1&0&0\\0&1&1&1&0&1&0\\1&0&1&1&0&0&1\end{bmatrix}\ (3\times7).\tag{1.30}$$
Every codeword satisfies $\mathbf H\mathbf t=\mathbf 0$ (1.31); Exercise 1.4 asks to check this via $\mathbf H\mathbf G^{\mathsf T}$. Since $\mathbf r=\mathbf G^{\mathsf T}\mathbf s+\mathbf n$, the decoding problem is to find the most probable noise vector satisfying
$$\mathbf H\mathbf n=\mathbf z.\tag{1.32}$$
An algorithm that solves this is called a **maximum-likelihood decoder** (p. 12).

*Properties summary (p. 12).* Every 7-bit vector is either a codeword or one flip away from one. There are 2×2×2 = 8 syndromes: seven non-zero (one per one-bit error) plus the all-zero one.

*Error measures (p. 13).* Probability of block error: $p_B=P(\hat{\mathbf s}\ne\mathbf s)$ (1.33). Probability of bit error: $p_b=\frac1K\sum_{k=1}^KP(\hat s_k\ne s_k)$ (1.34). For the Hamming code, a decoding error occurs whenever more than one bit in the block of seven is flipped. So p_B is the probability that two or more bits flip, which is O(f²), like R₃. The rate is R = 4/7, which is higher than R₃'s. In figure 1.17 (f = 0.1) about 7% of decoded bits are in error, and the errors are correlated: often two or three successive decoded bits are flipped (p. 13).

*Exercise 1.6 results (solution, p. 17–18).*
- (a) $p_B=\sum_{r=2}^7\binom7rf^r(1-f)^{7-r}$ (1.46) $\simeq\binom72f^2=21f^2$ (1.47).
- (b) In the most probable case the noise has weight two, and the decoder adds a third wrong flip, so the decoded vector differs from the transmitted one in three bits. Averaged over all seven bits, the probability that a randomly chosen bit is flipped is 3/7 times p_B, to leading order. The code protects all seven bits equally, assuming a binary symmetric channel (see symmetry below). So $p_b\simeq\frac37p_B\simeq9f^2$ (1.48).

*Symmetry of the (7,4) code (pp. 18–19).* The author reorders the bits by $(t_1\dots t_7)\to(t_5t_2t_3t_4t_1t_6t_7)$, which gives
$$\mathbf H=\begin{bmatrix}1&1&1&0&1&0&0\\0&1&1&1&0&1&0\\0&0&1&1&1&0&1\end{bmatrix}.\tag{1.50}$$
(p. 18). The sum of two parity constraints is another constraint. Row 1 (t₅+t₂+t₃+t₁ even) plus row 2 (t₂+t₃+t₄+t₆ even) gives t₅+2t₂+2t₃+t₁+t₄+t₆ even (1.51), i.e. t₅+t₁+t₄+t₆ even. Adding this as a fourth row gives $\mathbf H'$ (1.52), whose rows 2–4 are cyclic shifts of row 1. Dropping the first row gives $\mathbf H''$ (1.53). It satisfies $\mathbf H''\mathbf t=\mathbf 0$ and looks like (1.50) with all columns shifted one place right cyclically. Iterating, seven different **H** matrices give each bit a different role. The super-redundant seven-row cyclic matrix $\mathbf H'''$ (1.54) has a row space of dimension only three (p. 19).
- A linear code with a cyclic parity-check matrix, for some ordering of the bits, is a *cyclic code*. Any cyclic permutation of a codeword is a codeword. Here the code consists of all seven cyclic shifts of 1110100 and of 1011000, plus 0000000 and 1111111. Cyclic codes are a cornerstone of the algebraic approach, but are not used again in the book, having been superseded by sparse-graph codes (p. 19).
- Exercise 1.7: there are fifteen non-zero noise vectors giving the all-zero syndrome, namely the fifteen non-zero codewords. Because the code is linear, the sum of two codewords is a codeword (p. 19).

*Intuition note.* The Hamming code keeps the same O(f²) error scaling as R₃ but spends only 3 extra bits per 4 instead of 8 extra per 4. That is a better rate for the same type of protection. Its seven distinct non-zero syndromes match the seven single-bit errors exactly.

**Codes compared (pp. 13–14).** Figure 1.18 shows repetition codes, the Hamming code, and BCH codes (a family generalizing Hamming codes) with blocklengths up to 1023, at f = 0.1. Linear block codes beat repetition codes, but "the asymptotic situation still looks grim" (p. 13).

**Graphs and codes (solution to 1.9; pp. 19–20).**
- Replace each circle of fig. 1.13 by a parity-check node linked to its bits. The result is a *bipartite graph* with bit nodes and check nodes, and edges only between the two classes (fig. 1.20). Each check node is a row of **H**, each bit node a column, and each 1 in **H** is an edge.
- Example: take a dodecahedron, make its vertices the parity checks, and put a bit on each edge. Every column of **H** has weight 2 and every row weight 3 (weight = number of 1s). N = 30 bits and 20 apparent checks, but only M = 19 independent ones (the 20th is redundant), so K = N − M = 11. It is a (30,11) code.
- Flipping the bits around one face satisfies all checks, so there are 12 codewords of weight 5. The code's *distance* is d = 5 (the Hamming code had d = 3). A code with distance 5 can correct all double errors but not some triple errors. So its error probability, for a BSC and at least at low f, is dominated by an f³ term, "perhaps something like" $12\binom53f^3(1-f)^{27}$ (1.55).
- The author says the best linear codes have tangled graphs, as in the (16,4) low-density parity-check code of fig. 1.22. Nonlinear codes can also have good properties, but encoding and decoding them is trickier (p. 20).

**Counting bound (Exercises 1.10–1.11; pp. 14, 20–21).**
- Question (Ex. 1.10): can a (14,8) code correct any two errors?
- Linear case with syndrome decoding: the number of error patterns of weight up to two is $\binom N2+\binom N1+\binom N0$ (1.56). For N = 14 this is 91 + 14 + 1 = 106. The syndrome has M = N−K = 6 bits, so at most 2⁶ = 64 syndromes. Since 106 > 64, no such code exists.
- General case, linear or not: if the sender picks from S_t codewords and the channel from S_n noise vectors, and both can be recovered from **r** (one of at most 2^N strings), then
$$S_{\mathbf t}S_{\mathbf n}\le2^N.\tag{1.57}$$
For a two-error-correcting (N,K) code:
$$2^K\Big[\binom N2+\binom N1+\binom N0\Big]\le2^N.\tag{1.58}$$
(p. 21). The (30,11) dodecahedron code and a (15,6) pentagonful code (introduced on p. 221, outside these pages) are given as two-error-correcting examples.

*Intuition note.* Every correctable error pattern needs its own "label" in the received string. If there are more patterns than labels, some must be confused. This holds with or without linearity.

### 1.3 What performance can the best codes achieve? (pp. 14–15)

- There seems to be a trade-off between p_b (want small) and rate R (want large). The question is which points in the (R, p_b) plane are achievable. Shannon addressed this in 1948 (p. 14).
- **Widespread belief at that time** (as reported by the author, not Shannon): the boundary between achievable and non-achievable points was a curve through the origin (0,0). Then a vanishing p_b would require R close to 0. "No pain, no gain" (p. 14).
- **Shannon's result:** the boundary meets the R axis at a non-zero value R = C (fig. 1.19). For any channel, there exist codes that give arbitrarily small p_b at non-zero rates. This is the *noisy-channel coding theorem*, to which the first half of the book (Parts I–III) is devoted (p. 14).
- **Capacity** is the maximum rate at which communication with arbitrarily small p_b is possible. For the BSC:
$$C(f)=1-H_2(f)=1-\Big[f\log_2\tfrac1f+(1-f)\log_2\tfrac1{1-f}\Big].\tag{1.35}$$
For f = 0.1, C ≃ 0.53 (p. 15).
- The Shannon limit curve in fig. 1.19 is $R=C/(1-H_2(p_b))$ (caption, p. 15).
- Disk-drive reading (Shannon speaking, in the author's imagined dialogue): since 1/2 < 0.53, two drives would reach 10⁻¹⁵, or 10⁻¹⁸, or anything, instead of sixty (p. 15).
- Caveat in the text: Shannon proved the theorem with block codes of ever-increasing blocklength. The needed blocklength might exceed a gigabyte, in which case one would need two noisy terabyte drives (p. 15).

*Intuition note.* Shannon's result contradicts the widespread belief ("No pain, no gain") that a vanishing error probability needs a rate close to zero. Below capacity, error can be pushed arbitrarily low without driving the rate to zero. The textbook codes plotted in fig. 1.19 lie well away from the Shannon limit curve.

### 1.4 Summary (pp. 15–16)
- By including three parity bits in a block of 7, the (7,4) Hamming code can detect and correct any single bit error in each block (p. 15).
- Shannon's theorem: information can be communicated over a noisy channel at a non-zero rate with arbitrarily small error probability (p. 15).
- Information theory addresses both limitations and possibilities. The theorem, to be proved in Chapter 10, asserts both that reliable communication beyond capacity is impossible and that it is possible at all rates up to capacity (p. 16). The next chapters cover measuring information content and data compression (p. 16).

### 1.5 Further exercises and 1.6 Solutions: concatenation (Ex. 1.12; pp. 16, 21)
R₉ can be viewed as R₃ concatenated with R₃ ("R₃²"): decode each triplet with the R₃ decoder, then decode the decoded bits again. Results given:
- $p_b(\mathrm R_3^2)\simeq3[p_b(\mathrm R_3)]^2=3(3f^2)^2+\dots=27f^4+\dots$ (1.59).
- $p_b(\mathrm R_9)\simeq\binom95f^5(1-f)^4\simeq126f^5+\dots$ (1.60).
- The concatenated decoder is suboptimal, since some weight-four noise vectors make it err. It needs less computation: memorizing three bits and counting to three, instead of counting to nine. Concatenated codes are widely used because they allow large codes with simple hardware, and some of the best known practical codes are concatenated (p. 21).

## Toy example (ours, not from the text)
**R₃ on a BSC with f = 0.1: check the claims numerically.**
- Number of flips among 3 bits is binomial (1.1). P(0) = 0.9³ = 0.729. P(1) = 3 × 0.1 × 0.9² = 3 × 0.1 × 0.81 = 0.243. P(2) = 3 × 0.1² × 0.9 = 0.027. P(3) = 0.1³ = 0.001. Sum = 0.729 + 0.243 + 0.027 + 0.001 = 1.000.
- Majority vote errs on 2 or 3 flips: p_b = 0.027 + 0.001 = 0.028. Check with (1.36): 3(0.01) − 2(0.001) = 0.03 − 0.002 = 0.028 ✓. This is the book's "≃ 0.03". The rate is 1/3.
- Likelihood check for r = 010. Under t = 000: bits match, mismatch, match, so 0.9 × 0.1 × 0.9 = 0.081. Under t = 111: 0.1 × 0.9 × 0.1 = 0.009. Ratio = 0.009/0.081 = 1/9 = γ⁻¹ with γ = 0.9/0.1 = 9 ✓ (algorithm 1.9). With equal priors, decode 0.
- Hamming syndrome check: **s** = 1000, **t** = 1000101. Noise flips bit 6, so **r** = 1000111. With **H** from (1.30), row 1 (r₁+r₂+r₃+r₅) = 1+0+0+1 = 0 (mod 2). Row 2 (r₂+r₃+r₄+r₆) = 0+0+0+1 = 1. Row 3 (r₁+r₃+r₄+r₇) = 1+0+0+1 = 0. So **z** = (0,1,0), and algorithm 1.16 says unflip r₆, giving 1000101 and ŝ = 1000 ✓.

## Concepts
- [[binary-symmetric-channel]] (new) — channel flipping each bit independently with probability f (p. 4)
- [[noisy-channel]] — a medium whose output may differ from its input with some probability (p. 3)
- [[error-correcting-code]] — encoder/decoder pair that adds structured redundancy to detect and correct errors (p. 4)
- [[redundancy]] — extra bits added by the encoder, which the decoder uses to infer both message and noise (p. 4)
- [[code-rate]] (new) — ratio of source bits to transmitted bits, e.g. 1/3 for R₃, 4/7 for the (7,4) Hamming code (pp. 7, 13)
- [[repetition-code]] (new) — repeat each bit N times; decode by majority vote (p. 5)
- [[linear-block-code]] (new) — maps K source bits to N bits, extra bits being modulo-2 linear functions of the source (p. 9)
- [[hamming-code]] (new) — the (7,4) linear block code with three parity checks that corrects any single flip (p. 9)
- [[syndrome-decoding]] (new) — compute the pattern of violated parity checks, **z** = **H r**, and map it to the most probable noise pattern (pp. 10–12)
- [[maximum-likelihood-decoding]] (new) — find the most probable noise vector with **H n** = **z** (p. 12)
- [[bayes-theorem]] — used for optimal decoding, with posterior ∝ likelihood × prior (p. 6)
- [[likelihood]] — the data-dependent term P(**r** | s) (p. 6)
- [[prior-distribution]] — here, P(s) = 0.5 for each source bit (p. 6)
- [[posterior-distribution]] — P(s | **r**), maximized by the optimal decoder (p. 6)
- [[entropy]] — here appears as the binary entropy function H₂(x), used in the counting approximation and in capacity (p. 2)
- [[channel-capacity]] — maximum rate with arbitrarily small p_b; for the BSC, 1 − H₂(f) (pp. 14–15)
- [[noisy-channel-coding-theorem]] — rates up to C are achievable with arbitrarily small error, and rates beyond C are not (pp. 14–16)
- [[stirling-approximation]] (new) — x! ≃ x^x e^{−x} √(2πx), used to approximate binomial coefficients (p. 2)

## Canonical instances
- [[noisy-disk-drive]] — the running example: BSC with f = 0.1, needing p_b ≈ 10⁻¹⁵ (p. 4)
- [[repetition-code-R3]] — p_b ≈ 3f², rate 1/3 (pp. 5–8)
- [[hamming-code-7-4]] — p_B ≃ 21f², p_b ≃ 9f², rate 4/7 (pp. 9–13, 17–19)
- [[dodecahedron-code-30-11]] — graph-defined code with distance 5 (p. 20)
- [[binomial-distribution-bent-coin]] — mean Nf, variance Nf(1−f) (p. 1)

## Bridges (candidates)
- [same-math] Optimal decoding of R₃ (maximize P(s|**r**) with equal priors = maximize likelihood) ↔ bayesian: posterior ∝ likelihood × prior; it is the same equation (1.18).
- [structural-analogy] Majority vote as likelihood ratio γ^(votes) ↔ bayesian: independent observations multiply likelihood ratios (evidence accumulation).
- [same-math] log C(N,r) ≃ N·H₂(r/N) ↔ information-theory: entropy as the exponential growth rate of the count of typical sequences.
- [structural-analogy] The syndrome-counting bound 2^K·(number of correctable patterns) ≤ 2^N ↔ information-theory: a counting form of the converse to coding theorems.

## Questions this raises
- What exactly is "information content", and how do bits and entropy measure it? (The next chapters promise this.)
- Why is the capacity of the BSC exactly 1 − H₂(f), and how is the theorem proved (Chapter 10)?
- Can practical codes with efficient decoders get close to the Shannon limit, given that the figure shows textbook codes far from it?
- How do error-correction and data compression relate, given that both rely on redundancy?

## Exercises worth doing
- Ex. 1.4 (p. 12) — verify **H G**ᵀ = 0, so every codeword satisfies **H t** = **0** — difficulty: easy
- Ex. 1.5 (p. 13) — decode four received strings with the syndrome table (practice with algorithm 1.16) — difficulty: easy
- Ex. 1.8 (p. 13) — show that two or more flips in a block always cause a block decoding error (parity-only corruption cannot occur) — difficulty: medium
- Ex. 1.11 (p. 14) — design a two-error-correcting code other than repetition, using the counting bound — difficulty: hard
- Ex. 1.12 (p. 16) — compare concatenated R₃² decoding against optimal R₉ decoding — difficulty: medium

## Reading notes
- Page offset: printed = pdf − 12 (pdf 13 = printed 1). The "About Chapter 1" primer is on printed pp. 1–2, before the chapter proper.
- Source is the Cambridge University Press 2003 on-screen version, and each page carries a copyright header.
- The text layer is garbled for equations (fractions, square roots, hats); I checked the equations against the page images.
- The Figure 1.15 caption speaks of flipped bits "s₃ and t₇" in example (e), while the body text (p. 11) says "r₃ and r₇". They presumably refer to the same positions (bits 3 and 7).
- The heading "Graphs corresponding to codes" on p. 19 sits under the solution to Exercise 1.7. The text beneath it solves Exercise 1.9.
- Exercise 1.3 states "about 60" (p. 8), while the solution works out N ≃ 61 after an initial rough estimate of 68 (p. 17).
- Solutions given by the author to exercises 1.2, 1.3, 1.6, 1.7, 1.9, 1.10, 1.11, 1.12 appear on pp. 16–21. Ex. 1.4, 1.5 and 1.8 have no printed solution here.
