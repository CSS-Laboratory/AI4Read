---
id: polyanskiy-2025-information/ch19-error
work: polyanskiy-2025-information
unit: "Chapter 17 (printed). Error correcting codes (unit id ch19-error)"
pages: 342-349
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Error correcting codes

## L0 — One line
A code is an encoder/decoder pair judged by its error probability, and for any code with average error at most ε, log M cannot exceed (capacity + h(ε))/(1−ε), a bound proved by treating the code as a hypothesis test.

## L1 — The gist (≤ 120 words)
How many bits can be sent through a noisy channel with error probability at most ε? The chapter defines codes, error metrics and the fundamental limits M\*(ε). It uses the binary symmetric channel (n = 1000, δ = 0.11, ε = 10⁻³) to compare repetition codes (47 bits), Reed–Muller blocks (112 bits, using 1024 channel uses), Shannon's prediction (about 500 bits) and finite-blocklength bounds (414 to 416 bits). The optimal decoder is MAP/ML, and for average error randomness in the code does not help. A weak converse proof, via data processing for divergence, shows no code beats capacity by more than a factor 1/(1−ε), plus h(ε)/(1−ε). This matters because it separates what is achievable from what is impossible.

**Prerequisites:** conditional probability; binomial distribution; mutual information and capacity; KL divergence and the data-processing inequality; binary entropy h.

## L2 — Key ideas
- An M-code is an encoder f:[M]→𝒳 plus a decoder g:𝒴→[M]∪{e}. With W uniform it gives the Markov chain W→X→Y→Ŵ (pp. 342–343).
- Average error Pe never exceeds maximal error Pe,max. The limits M\*, M\*_max, ε\*, ε\*_max are defined from each (p. 343).
- On BSC(0.11), n = 1000, ε = 10⁻³: repetition codes send 47 bits and Reed–Muller blocks 112 bits (using 1024 channel uses). Before Shannon it was almost universally accepted that vanishing error forces vanishing rate (pp. 344–345).
- Shannon's expansion log M\* = nC + o(n) predicts, not completely rigorously, about 500 bits. Rigorous finite-length bounds give 414 ≤ log₂M\* ≤ 416, so the prediction is about 20% too optimistic (p. 346).
- Codes must be prepared for every message, even though almost all codewords are never used. The text says this is at the heart of the concept of information (p. 346).
- The error-minimizing decoder is MAP, which equals ML when W is uniform, and it is deterministic. On the BSC, for a deterministic encoder, it is minimum Hamming distance, giving Voronoi cells (p. 347).
- For Pe, randomized encoders do not enlarge M\*(ε). For Pe,max, the text says randomized encoders and decoders do have to be considered (pp. 347–348).
- Weak converse: any (M,ε)-code has log M ≤ (sup I(X;Y) + h(ε))/(1−ε), proved by a hypothesis-test argument plus data processing (pp. 348–349).

## L3 — Walkthrough

### 17.1 Codes and probability of error
**Definition 17.1.** An M-code for P_{Y|X} is a pair (f,g) of (possibly randomized) functions: encoder f:[M]→𝒳, decoder g:𝒴→[M]∪{e}, with an extra output symbol e (p. 342). For deterministic f, g: codewords c_i ≜ f(i), codebook 𝒞={c_1,…,c_M}, and decoding region D_i ≜ g⁻¹({i}) (p. 342). Randomized f, g are identified with kernels P_{X|W}, P_{Ŵ|Y} (p. 342).

The probability space is the chain $W \xrightarrow{f} X \xrightarrow{P_{Y|X}} Y \xrightarrow{g} \hat W$ with $W\sim\mathrm{Unif}([M])$ (p. 343), tag (17.1). For discrete spaces:
- general: $P_{W,X,Y,\hat W}(m,a,b,\hat m)=\frac1M P_{X|W}(a|m)P_{Y|X}(b|a)P_{\hat W|Y}(\hat m|b)$;
- deterministic f, g: $P_{W,X,Y,\hat W}(m,c_m,b,\hat m)=\frac1M P_{Y|X}(b|c_m)\mathbf 1\{b\in D_{\hat m}\}$ (p. 343).

**Metrics (p. 343).** Maximum error $P_{e,\max}(f,g)\triangleq\max_{m}\mathbb P[\hat W\ne m|W=m]$. Average error $P_e(f,g)\triangleq\mathbb P[W\ne\hat W]$. Clearly $P_e\le P_{e,\max}$, so small $P_{e,\max}$ is stricter and protects all codewords uniformly. Some codes, such as linear codes (Section 18.6), have $P_e=P_{e,\max}$ by construction; in general the two can differ a lot.

**Definition 17.2 (p. 343).** An (M,ε)-code has $P_e\le\epsilon$; an (M,ε)_max-code has $P_{e,\max}\le\epsilon$. Then $M^*(\epsilon)=\max\{M:\exists(M,\epsilon)\text{-code}\}$, $\epsilon^*(M)=\inf\{\epsilon:\exists(M,\epsilon)\text{-code}\}$, and likewise $M^*_{\max},\epsilon^*_{\max}$. So $\log_2M^*(\epsilon)$ is the maximum number of bits pushed through the channel with error at most ε (p. 344).

**Example 17.1 (p. 344).** BSC$_\delta^{\otimes n}$ has $\mathcal X=\mathcal Y=\{0,1\}^n$ and $Y^n=X^n\oplus Z^n$, with $Z^n\sim\mathrm{Ber}(\delta)$ i.i.d. and independent of $X^n$. Each bit flips independently with probability δ.

### 17.2 Coding for binary symmetric channels
Setting: δ = 0.11, n = 1000, ε = 10⁻³ (p. 344).
- **Uncoded** (k = 1000): $P_e=1-(1-\delta)^n\approx1$. Coding is needed, and there is a tradeoff: fewer data bits, more redundancy (p. 344).
- **Repetition** (each bit repeated ℓ times, majority vote): $P_b=\mathbb P[\mathrm{Binom}(\ell,\delta)>\ell/2]$ and $P_e\le k\,P_b$ (essentially tight here). Constraints: $k\ell\le n=1000$ and $k\,\mathbb P[\mathrm{Binom}(\ell,\delta)>\ell/2]\le10^{-3}$. Solution: ℓ = 21, k = 47 bits (p. 345).
- For repetition coding, better reliability needs larger ℓ, so the rate $k/n=1/\ell$ drops. Before Shannon it was almost universally accepted that vanishing error forces vanishing rate (p. 345).
- **First-order Reed–Muller code (1,r)**: data $a\in\mathbb F_2^r$ is read as the polynomial $f_a(x)=\sum_{i=1}^{r-1}a_ix_i+a_0$, evaluated at all $x\in\mathbb F_2^{r-1}$. It maps r bits to $2^{r-1}$ bits, with $d_{\min}=2^{r-2}$ (p. 345). So (1,7) is a [64,7,32] code. The text states, without proof, that its optimal decoder has error ≤ 6·10⁻⁶ on BSC$_{0.11}^{\otimes64}$ (p. 345). Using 16 blocks on 1024 uses, the union bound gives $P_e\lesssim10^{-4}<10^{-3}$, so 7·16 = 112 bits are sent (p. 345).
- **Shannon:** $\log M^*(\epsilon;P_{Y^n|X^n})=nC+o(n)$ (17.2) as n→∞, for any ε∈(0,1). Here $C=\max_{P_{X_1}}I(X_1;Y_1)$. For the BSC, $C=\log2-h(\delta)\approx\tfrac12$ bit, so about 500 bits are predicted, though not completely rigorously because of the $o(n)$ residual (pp. 345–346). This is not quite possible at n = 1000 (p. 346).
- **Finite-blocklength bounds [334]:** $414\le\log_2M^*(10^{-3})\le416$ bits (17.3). Shannon's prediction is about 20% too optimistic (p. 346).
- **History (p. 346):** about 60 years passed before practical codes met such performance. Turbo codes were the first to approach the bounds; this class is known as sparse-graph codes, of which Gallager's LDPC codes are well studied. As a rule of thumb they reach 80–90% of log M\* for n ≈ 10³–10⁴. For n ≈ 100–1000, polar codes with list decoding are an alternative.
- **Paradigm shift (p. 346):** a good code has M ≈ 2⁴⁰⁰ points in {0,1}¹⁰⁰⁰. Using it once a second for the universe's lifetime (≈10¹⁸ s) explores at most 2⁶⁰ codewords. Yet all must be placed carefully, because to transmit information is to convey a selection of W from [M], and we cannot know in advance which W will occur.

*Intuition note:* The text contrasts simple repetition with more sophisticated ways of injecting redundancy into the whole block, such as Reed–Muller codes. The gap between 47, 112 and 414–416 bits shows how much code design matters.

### 17.3 Optimal decoder
For a given encoder, the error-minimizing decoder is MAP, which equals ML because W is uniform (p. 347):
$$g^*(y)=\arg\max_m\mathbb P[W=m|Y=y]=\arg\max_m\mathbb P[Y=y|W=m]\tag{17.4}$$
It is deterministic. For deterministic encoders with image 𝒞 (p. 347):
$$P_{e,\mathrm{MAP}}(\mathcal C)=1-\frac1M\sum_{y\in\mathcal Y}\max_{x\in\mathcal C}P_{Y|X}(y|x)\tag{17.5}$$
**Remark 17.1.** For BSC$_\delta^{\otimes n}$, with Hamming distance $d_H(x^n,y^n)=|\{i:x_i\ne y_i\}|$,
$$g^*(y^n)=\arg\min_m d_H(c_m,y^n)\tag{17.6}$$
So the decoding regions are Voronoi cells of the Hamming space. AWGN gives Voronoi cells in ℝⁿ (Section 20.3) (p. 347).

**Randomized encoders.** Write $X=f(W,U)$ with $U\perp W$ and f deterministic. Then $\mathbb P[W\ne\hat W]=\mathbb E[\mathbb P[W\ne\hat W|U]]$. So if $\mathbb P[W\ne\hat W]\le\epsilon$, some $u_0$ has $\mathbb P[W\ne\hat W|U=u_0]\le\epsilon$. Hence $M^*(\epsilon)$ is unchanged by restricting to deterministic encoders and decoders (p. 347).

This does not apply to $P_{e,\max}$: the text says $M^*_{\max}(\epsilon)$ does require considering randomized encoders and decoders. For M = 2, decoding is binary hypothesis testing. The optimal test minimizing $\max\{1-\alpha,\beta\}$ is not deterministic if that max is not attained at a vertex of the Neyman–Pearson region $\mathcal R(P_{Y|W=1},P_{Y|W=2})$ (pp. 347–348).

### 17.4 Weak converse bound
A converse bound is an impossibility result bounding M from above or ε from below (p. 348).

**Theorem 17.3 (Weak converse).** Any (M,ε)-code for $P_{Y|X}$ satisfies
$$\log M\le\frac{\sup_{P_X}I(X;Y)+h(\epsilon)}{1-\epsilon},$$
with $h(x)=H(\mathrm{Ber}(x))$ (p. 348).

*Proof (pp. 348–349).* The text notes Fano's inequality gives a one-line proof, but proceeds differently, with meta-converse (Section 22.3) in mind.
1. Use the code as a test between $P_{X,Y}$ and $P_XP_Y$: given (X,Y), sample $(W,\hat W)$ from $P_{W|X}P_{\hat W|Y}$ and set $Z=\mathbf 1\{W\ne\hat W\}$.
2. Under $P_XP_Y$, $\hat W\perp W\sim\mathrm{Unif}([M])$, so $P_XP_Y[Z=1]=1/M$.
3. Under $P_{X,Y}$, $P_{X,Y}[Z=1]=1-P_e$.
4. Data processing for divergence, with $d(\cdot\|\cdot)$ the binary divergence:
$$D(P_{X,Y}\|P_XP_Y)\overset{\rm DPI}{\ge}d\!\left(1-P_e\,\Big\|\,\tfrac1M\right)\ge-h(\mathbb P[W\ne\hat W])+(1-P_e)\log M.$$
(added step: $d(p\|q)=-h(p)+p\log\frac1q+(1-p)\log\frac1{1-q}\ge-h(p)+p\log\frac1q$, with $p=1-P_e$, $q=1/M$, $h(1-P_e)=h(P_e)$.)
5. The left side is $I(X;Y)\le\sup_{P_X}I(X;Y)$, so $\log M\le\frac{\sup I+h(P_e)}{1-P_e}$.
6. Since $p\mapsto h(p)/(1-p)$ is monotonically increasing, $P_e\le\epsilon$ gives the theorem. ∎

*Intuition note:* If the decoder is usually right, the pair (X,Y) looks very different from an independent pair. The divergence between the two is I(X;Y), and data processing keeps the test from separating them by more than that, which limits how many messages can be told apart.

**Remark 17.2.** Other divergences in the data-processing step improve the bound. This gives the "strong" converse (Section 22.1) and the meta-converse technique (Section 22.3) (p. 349).

## Toy example (ours)
*Repetition and MAP.* Let BSC with δ = 0.1 and code {000, 111} (ℓ = 3, k = 1). The error probability is $\mathbb P[\mathrm{Binom}(3,0.1)>1.5]=\mathbb P[\ge2\text{ flips}]=3(0.1)^2(0.9)+(0.1)^3=0.027+0.001=0.028$. For y = 010, distances are $d_H(000,y)=1$ and $d_H(111,y)=2$, so MAP/ML decoding (17.6) gives message 0.

*Converse check, one channel use.* Take n = 1, M = 2, f(i) = i, so $P_e=\delta=0.1$. Here $h(0.1)=0.1\cdot3.3219+0.9\cdot0.1520\approx0.469$ and $C=1-0.469=0.531$. The bound reads $\log_22=1\le(0.531+0.469)/0.9=1.111$. It holds, but is not tight.

## Concepts
- [[error-correcting-code]] — an M-code (f,g) built so decoding recovers W with small error (p. 342)
- [[m-code]] (new) — encoder f:[M]→𝒳 with decoder g:𝒴→[M]∪{e} (p. 342)
- [[max-vs-average-error]] (new) — $P_{e,\max}\ge P_e$; maximal error protects every codeword (p. 343)
- [[fundamental-limits-M-star]] (new) — $M^*(\epsilon)$, the largest M with an (M,ε)-code (p. 343)
- [[noisy-channel]] — here BSC$_\delta^{\otimes n}$, bits flipped independently with probability δ (p. 344)
- [[channel-capacity]] — $C=\max I(X_1;Y_1)$; for BSC, log 2 − h(δ) (p. 346)
- [[noisy-channel-coding-theorem]] — $\log M^*=nC+o(n)$ (p. 345)
- [[map-ml-decoder]] (new) — decoder maximizing posterior; equals ML under uniform W (p. 347)
- [[weak-converse]] (new) — $\log M\le(\sup I+h(\epsilon))/(1-\epsilon)$ (p. 348)
- [[finite-blocklength-bounds]] (new) — rigorous, computable bounds on log M\* at fixed n (p. 346)
- [[data-processing-inequality]] — used for divergence in the converse proof (p. 348)
- [[relative-entropy-kl-divergence]] — $I(X;Y)=D(P_{X,Y}\|P_XP_Y)$ (p. 349)
- [[fano-inequality]] — gives the same bound in one line (p. 348)

## Canonical instances
- [[bsc-n1000-delta011]] — running example: 47 bits (repetition), 112 (Reed–Muller), 414–416 (bounds) (pp. 344–346)
- [[reed-muller-1-7]] — [64,7,32] code (p. 345)
- [[universe-lifetime-codebook]] — at most 2⁶⁰ codewords explored out of 2⁴⁰⁰ (p. 346)
- [[hamming-voronoi-decoding]] — minimum-distance decoding on the BSC (p. 347)

## Bridges (candidates)
- [structural-analogy] Decoding as M-ary hypothesis testing ↔ statistics: Neyman–Pearson tests (pp. 347–348)
- [same-math] Weak converse proof via DPI on $d(1-P_e\|1/M)$ ↔ Fano's inequality (p. 348)
- [structural-analogy] Voronoi decoding cells ↔ geometry/clustering: nearest-center classification (p. 347)

## Questions this raises
- Why does the 1/(1−ε) factor make this converse "weak", and how does the strong converse remove it?
- What do achievability bounds look like at finite n, and how do they compare with 414–416?
- When does $M^*_{\max}$ differ from $M^*$ in a way that matters?
- How can codes such as LDPC or polar codes be decoded efficiently, when MAP decoding needs a search over all M codewords?

## Reading notes
- The unit id says "ch19-error", but the printed chapter number is 17 ("Error correcting codes"). Printed = pdf − 25.
- Pages carry a proof-style header ("itbook-export … August 16, 2024"). They contain extraction artefacts, but the equations were checked against the images.
- Cross-references to Sections 18.6, 19.3, 20.3, 22.1, 22.3, Theorem 19.9 and Part III point outside this unit. Their content is not covered here.
- The Reed–Muller error bound (≤ 6·10⁻⁶) and the bounds in (17.3) are stated without proof. The toy example's numbers are ours.
