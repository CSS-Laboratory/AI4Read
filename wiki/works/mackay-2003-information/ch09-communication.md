---
id: mackay-2003-information/ch09-communication
work: mackay-2003-information
unit: "9 Communication over a Noisy Channel"
pages: 145-160
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Communication over a Noisy Channel

## L0 — One line
The largest mutual information between a noisy channel's input and output, its capacity C, is proposed as the measure of what the channel can carry; the chapter states (proof in Chapter 10) that for any rate below C, communication with arbitrarily small error probability is possible.

## L1 — The gist (≤ 120 words)
Source coding implicitly assumed a noiseless channel. Real channels are noisy, for example flipping or erasing symbols. How fast can data be sent through one with negligible error? MacKay reviews conditional entropy and mutual information, defines model channels, and uses Bayes' theorem to infer inputs from outputs. He defines capacity as the maximum of I(X;Y) over input distributions. He then states the noisy-channel coding theorem (part one): any rate below C is achievable with arbitrarily small maximal block error. A counting sketch with typical output sets bounds the number of distinguishable inputs by 2^{NC}, suggesting that up to C bits per use, and no more, can be sent reliably. The rigorous proof is deferred to Chapter 10.

**Prerequisites:** entropy and typical sets (Ch. 2, 4); joint, conditional and marginal probability; Bayes' theorem; matrix–vector multiplication; derivatives of logarithms.

## L2 — Key ideas
- Channel coding aims to make a noisy channel behave like a noiseless one, by adding redundancy of a special sort to an already-compressed stream (p. 146).
- Rate of information is not "bits sent minus expected errors": the receiver does not know where errors happened. At f = 0.5 no information gets through (p. 146).
- Mutual information I(X;Y) = H(X) − H(X|Y) = H(Y) − H(Y|X) measures what the output says about the input. It depends on the input distribution (pp. 149–150).
- Capacity C(Q) = max over P_X of I(X;Y). The optimal input is not always uniform (Z channel: p₁* = 0.445) (pp. 150–151).
- Output-to-input inference is Bayes' theorem. The optimal block decoder picks the maximum-posterior codeword; with a uniform prior this is maximum likelihood (pp. 148, 152).
- Theorem (part one): for any R < C and ε > 0 there is, for large N, a rate ≥ R block code with maximal block error < ε (p. 152).
- Proof idea: for large N an extended channel resembles the noisy typewriter, and at most 2^{N I(X;Y)} ≤ 2^{NC} inputs have non-overlapping typical outputs (pp. 154–155).
- Pattern recognition can be framed as a noisy channel decoded by Bayes' theorem (generative modelling) (p. 156).

## L3 — Walkthrough

### 9.1 The big picture (p. 146)
Chapters 4–6 treated source coding and implicitly assumed a noise-free channel between compressor and decompressor. Channel coding is a second stage: an encoder and decoder around the noisy channel. Its aim is to make the noisy channel behave like a noiseless one (p. 146). The input is assumed to have been through a good compressor, so it has no obvious redundancy. The channel code puts back redundancy of a special sort so the noisy output can be decoded (p. 146).

Motivating question: send 1000 bits/s with p₀ = p₁ = 1/2 over a channel flipping bits with f = 0.1. **A tempting guess** is 900 bits/s (subtract expected errors). MacKay says this is not correct, because the recipient does not know where the errors occurred. At f = 0.5 the output is independent of the input, and no information is transmitted (p. 146). Hence the proposal: use mutual information, the source entropy minus the entropy of the source given the received signal. The chapter promises that for any channel Q there is a non-zero rate C(Q) up to which information can be sent with arbitrarily small error probability (pp. 146–147).

### 9.2 Review of probability and information (p. 147)
Joint distribution P(x,y) (from exercise 8.6), rows y, columns x:

| y \ x | 1 | 2 | 3 | 4 | P(y) |
|---|---|---|---|---|---|
| 1 | 1/8 | 1/16 | 1/32 | 1/32 | 1/4 |
| 2 | 1/16 | 1/8 | 1/32 | 1/32 | 1/4 |
| 3 | 1/16 | 1/16 | 1/16 | 1/16 | 1/4 |
| 4 | 1/4 | 0 | 0 | 0 | 1/4 |
| P(x) | 1/2 | 1/4 | 1/8 | 1/8 | |

H(X,Y) = 27/8, H(X) = 7/4, H(Y) = 2 bits. Conditional entropies of x given each y: H(X|y=1) = 7/4, H(X|y=2) = 7/4, H(X|y=3) = 2, H(X|y=4) = 0. Averaged: H(X|Y) = 11/8 bits (p. 147).

Observations (p. 147):
- H(X|y=3) > H(X), so learning y can increase uncertainty about x.
- P(x|y=2) differs from P(x), yet H(X|y=2) = H(X). Knowledge changes without the entropy falling.
- On average H(X|Y) < H(X).

Also H(Y|X) = 13/8 and I(X;Y) = H(X) − H(X|Y) = 3/8 bits (p. 147).

*Intuition note:* A single observation can leave you more confused (H(X|y=3) > H(X)), yet in this example, on average, learning y reduces uncertainty about x, since H(X|Y) < H(X). Mutual information is that average reduction.

### 9.3 Noisy channels (pp. 147–148)
A **discrete memoryless channel** Q has an input alphabet $\mathcal A_X$, an output alphabet $\mathcal A_Y$, and a conditional distribution P(y|x) for each x (p. 147). Transition matrix, with outputs indexing rows and inputs indexing columns, so each column is a probability vector (shape $|\mathcal A_Y| \times |\mathcal A_X|$):
$$Q_{j|i} = P(y=b_j \mid x=a_i)\tag{9.1}$$
$$\mathbf p_Y = \mathbf Q\,\mathbf p_X\tag{9.2}$$

Model channels (p. 148):
- **Binary symmetric channel (BSC):** inputs and outputs {0,1}; each bit flips with probability f, so P(y=0|x=0) = 1−f and P(y=1|x=0) = f.
- **Binary erasure channel (BEC):** outputs {0,?,1}; the bit is replaced by "?" with probability f, otherwise received correctly.
- **Noisy typewriter:** 27 letters in a circle; input G gives output F, G or H with probability 1/3 each.
- **Z channel:** input 0 always gives 0; input 1 gives 1 with probability 1−f and 0 with probability f.

### 9.4 Inferring the input given the output (pp. 148–149)
With input ensemble X, the joint is $P(x,y)=P(y|x)P(x)$ (9.3). Bayes' theorem gives the posterior of the input:
$$P(x\mid y)=\frac{P(y|x)P(x)}{P(y)}=\frac{P(y|x)P(x)}{\sum_{x'}P(y|x')P(x')}\tag{9.4}$$

**Example 9.1** (BSC, f = 0.15, p₀ = 0.9, p₁ = 0.1, observe y = 1):
$$P(x{=}1|y{=}1)=\frac{0.85\times0.1}{0.85\times0.1+0.15\times0.9}=\frac{0.085}{0.22}=0.39\tag{9.5}$$
So x = 1 is still less probable than x = 0, but less improbable than before (p. 149).

**Example 9.3** (Z channel, same f and prior, observe y = 1): $0.085/(0.085+0\times0.9)=1.0$. Output 1 makes us certain the input was 1 (9.6) (p. 149).

Printed solutions: P(x=1|y=0) = 0.019 for the BSC and 0.016 for the Z channel (p. 157).

*Intuition note:* The channel gives the likelihood, the input ensemble gives the prior, and the posterior says what the received symbol tells you. Here a rare input remains unlikely even after a "1" arrives.

### 9.5 Information conveyed by a channel (pp. 149–151)
For a given input ensemble X,
$$I(X;Y)\equiv H(X)-H(X|Y)=H(Y)-H(Y|X)\tag{9.7}$$
Conceptually I = reduction in uncertainty of the input; for computing, H(Y) − H(Y|X) is often handier (p. 149). Figure 9.1 shows the relation of H(X,Y), H(X), H(Y), conditional entropies and I(X;Y) (p. 149). Notation: $H_2(p)=p\log\frac1p+(1-p)\log\frac1{1-p}$, log means log₂ (p. 150).

**Example 9.5** (BSC, f = 0.15, p₁ = 0.1): P(y=0) = 0.78, P(y=1) = 0.22. H(Y|x) = H₂(0.15) for each x, so
$$I(X;Y)=H_2(0.22)-H_2(0.15)=0.76-0.61=0.15\text{ bits}\tag{9.8}$$
The source entropy is H(X) = H₂(0.1) = 0.47 bits (p. 150).

**Example 9.6** (Z channel, same input, P(y=1) = 0.085):
$$I(X;Y)=H_2(0.085)-[0.9H_2(0)+0.1H_2(0.15)]=0.42-(0.1\times0.61)=0.36\text{ bits}\tag{9.9}$$
This is bigger than for the BSC with the same f, so the Z channel is the more reliable channel (p. 150).

Printed results for exercises: uniform input, BSC: 0.39 bits; Z channel: 0.679 bits (p. 157–158).

**Capacity.** The mutual information depends on the input ensemble, so define
$$C(Q)=\max_{\mathcal P_X} I(X;Y)\tag{9.10}$$
The maximizing $\mathcal P_X^*$ is the optimal input distribution; it may be non-unique (p. 150). Chapter 10 will show that capacity measures the maximum error-free information per unit time (p. 150).

- **BSC, f = 0.15:** by symmetry (justified later) the optimal input is {0.5, 0.5}:
$$C(Q_{\rm BSC})=H_2(0.5)-H_2(0.15)=1.0-0.61=0.39\text{ bits}\tag{9.11}$$
Explicit maximization: $I(X;Y)=H_2((1-f)p_1+(1-p_1)f)-H_2(f)$ (9.12), plotted in figure 9.2 (p. 151). For general f the printed solution gives $C=1-H_2(f)$ (p. 158).
- **Noisy typewriter:** the optimal input is uniform and C = log₂ 9 bits (Example 9.10) (p. 151).
- **Z channel, f = 0.15:** P(y=1) = p₁(1−f) (9.13), and
$$I(X;Y)=H_2(p_1(1-f))-p_1H_2(f)\tag{9.14}$$
It is maximized at p₁* = 0.445 with C(Q_Z) = 0.685. The optimal input is not {0.5, 0.5}: using 0 more often communicates slightly more (p. 151).
- **BEC:** exercise 9.13 asks to show C = 0.85 for f = 0.15. The printed solution gives C = 1 − f for general f, "the fraction of the time that the channel is reliable", but notes it is far from obvious how to encode so as to achieve it (pp. 151, 158).

*Intuition note:* Capacity is the best you can do by choosing how to "talk" into the channel. Channel noise is fixed, but the input statistics are yours to choose, and the best choice is not always uniform.

### 9.6 The noisy-channel coding theorem (pp. 151–153)
The capacity may measure the rate of reliable block communication. This is not obvious and is proved in Chapter 10 (p. 151). Definitions:
- **(N,K) block code:** a list of $S=2^K$ codewords $\mathbf x^{(s)}\in\mathcal A_X^N$, each of length N. K = log₂S need not be an integer (p. 151).
- **Rate:** R = K/N bits per channel use (p. 152). The text notes a convention K/(N log q) for q-symbol inputs, not used here.
- **Decoder:** a map from $\mathcal A_Y^N$ to $\hat s\in\{0,1,\dots,2^K\}$, where $\hat s=0$ signals failure (p. 152).
- **Probability of block error** and **maximal probability of block error**:
$$p_{\rm B}=\sum_{s_{\rm in}}P(s_{\rm in})P(s_{\rm out}\ne s_{\rm in}\mid s_{\rm in})\tag{9.15}$$
$$p_{\rm BM}=\max_{s_{\rm in}}P(s_{\rm out}\ne s_{\rm in}\mid s_{\rm in})\tag{9.16}$$
- **Optimal decoder:** minimizes block error by choosing the maximum-posterior input:
$$P(s|\mathbf y)=\frac{P(\mathbf y|s)P(s)}{\sum_{s'}P(\mathbf y|s')P(s')}\tag{9.17}$$
$$\hat s_{\rm optimal}=\operatorname*{argmax}_s P(s|\mathbf y)\tag{9.18}$$
With a uniform prior on s (usually assumed) this is also the **maximum likelihood decoder**, maximizing $P(\mathbf y|s)$ (p. 152).
- **Bit error** $p_b$: average probability that a bit of $s_{\rm out}$ differs from the corresponding bit of $s_{\rm in}$, over the K bits (p. 152).

**Shannon's noisy-channel coding theorem (part one).** Associated with each discrete memoryless channel there is a non-negative number C with this property: for any ε > 0 and R < C, for large enough N there exists a block code of length N and rate ≥ R and a decoding algorithm such that the maximal probability of block error is < ε (p. 152; figure 9.4 shows the achievable region).

**Confirmation for the noisy typewriter** (pp. 152–153). Use N = 1 and only the letters B, E, H, …, Z (every third letter), a non-confusable subset (figure 9.5). Any output decodes uniquely, there are 9 inputs, so the error-free rate is log₂9 = C. In the theorem's terms: for any ε and R < C, set N = 1; the code has K = log₂9 > R; the decoder maps the received letter to the nearest code letter; the maximal block error is 0 < ε (p. 153).

### 9.7 Intuitive preview of proof (pp. 153–155)
**Extended channels.** N uses of a channel form an extended channel with $|\mathcal A_X|^N$ inputs and $|\mathcal A_Y|^N$ outputs (figures 9.6, 9.7 for BSC and Z, N = 1, 2, 4) (p. 153). Exercise 9.14 builds the N = 2 BEC extended channel; the printed solution picks columns 00 and 11, decoding "00" if the output is among the top four rows, "11" if among the bottom four, and giving up on "??" (pp. 154, 159).

**Sketch** (p. 154–155). For large N the extended channel looks like the noisy typewriter: a given input x very likely produces an output in a small typical output set, so one may find a non-confusable subset of inputs whose output sets are essentially disjoint (figure 9.8).
1. Draw x from $X^N$, X an arbitrary ensemble. By the source coding theorem the typical outputs number $2^{NH(Y)}$, all of similar probability.
2. For a typical input x there are about $2^{NH(Y|X)}$ probable outputs.
3. Disjointness bounds the number of non-confusable inputs by dividing the size of the typical y set by the size of each typical-y-given-x set:
$$\#\text{non-confusable inputs}\le 2^{NH(Y)-NH(Y|X)}=2^{NI(X;Y)}$$
4. The bound is largest when X maximizes I(X;Y), giving ≤ $2^{NC}$. MacKay concludes that asymptotically up to C bits per cycle, and no more, can be communicated with vanishing error probability (p. 155).

MacKay stresses the sketch has not rigorously proved reliable communication is possible; that is the next chapter's task (p. 155).

*Intuition note:* Think of the output space as a box and each input's noisy outputs as a small ball. You can pack at most about (box volume)/(ball volume) non-overlapping balls (a bound, p. 155). In the exponent, that ratio is $2^{NH(Y)}/2^{NH(Y|X)} = 2^{NI(X;Y)}$.

### 9.8 Further exercises (pp. 155–157)
Stated exercises (no worked solutions here):
- **9.15** (Z channel): (a) argue why p₁* < 0.5; (b) for general f show
$$p_1^*=\frac{1/(1-f)}{1+2^{(H_2(f)/(1-f))}}\tag{9.19}$$
(c) what happens as f → 1. Printed results: p₁* < 1/2 for all f; as f → 1 the expression tends to 1/e (p. 159). Rough intuition given: input 1 injects entropy into the output, input 0 does not (p. 159).
- **9.16:** printed result: for any f < 0.5 the BEC has the highest capacity of the three channels and the BSC the lowest (Z in between); figure 9.11 (p. 159).
- **9.17:** capacity of a five-input, ten-output channel with matrix (9.20) (p. 155).
- **9.18** Gaussian channel with $x\in\{-1,+1\}$, density $Q(y|x,\alpha,\sigma)=\frac1{\sqrt{2\pi\sigma^2}}e^{-(y-x\alpha)^2/2\sigma^2}$ (9.21). Printed results: log posterior ratio $a(y)=2\alpha y/\sigma^2$ (9.51), so $P(x{=}1|y)=1/(1+e^{-a(y)})$ (9.22, 9.52). The optimal decoder looks at the sign of a(y), and the error probability is $p_b=\Phi(-x\alpha/\sigma)$ (9.53), with Φ the Gaussian cumulative function (9.23) (pp. 155–156, 160).
- **Pattern recognition as a noisy channel** (p. 156): a digit author's choice from {0,…,9} is the input and a 256-pixel ink pattern in $\{0,1\}^{256}$ is the output. Strategy: model P(y|x) for each x and infer x by Bayes' theorem (9.24). This is **full probabilistic (generative) modelling**, said to be essentially how current speech recognition works, with a language model as prior P(x). Exercise 9.19 asks how many patterns look like a "2" and the entropy of P(y|x=2) (p. 156).
- **Random coding** (pp. 156–157): exercises 9.20–9.22 use the birthday problem. Printed solution to 9.20: with A = 365 days and S = 24 people, the probability all birthdays are distinct is $A(A-1)\cdots(A-S+1)/A^S$ (9.54), so a shared birthday has probability about 0.5. More instructive is the expected number of colliding pairs $\frac{S(S-1)}{2}\frac1A$ (9.55): tiny if $S\ll\sqrt A$, big if $S\gg\sqrt A$. For small S, $P(\text{distinct})\simeq\exp(-\frac{S(S-1)/2}{A})$ (9.57) (p. 160). Exercises 9.21–9.22 relate this to a coding scheme: send a birthday, or a random K-tuple of days assigned to each K-tuple of people (p. 157).

### 9.9 Solutions (pp. 157–160)
Final results are given inline above. Key printed steps: for the BSC with general input, $I(X;Y)=H_2(p_0f+p_1(1-f))-H_2(f)$ (9.40), whose only p-dependence is the first term, maximized when its argument is 0.5, i.e. $p_0=1/2$ (p. 158). For the BEC, $I(X;Y)=(1-f)H_2(p_1)$ (9.46), with maximum $1-f$ at $p_1=1/2$ (p. 158). For the Z channel, $\frac{d}{dp_1}I(X;Y)=(1-f)\log_2\frac{1-p_1(1-f)}{p_1(1-f)}-H_2(f)$ (9.48); setting it to zero gives $p_1^*(1-f)=1/(1+2^{H_2(f)/(1-f)})$ (9.49), hence (9.50) (p. 159). For the Gaussian channel, the error probability is $p_b=\int_{-\infty}^{0}dy\,Q(y|x{=}1,\alpha,\sigma)=\Phi(-x\alpha/\sigma)$ (9.53) (p. 160).

## Toy example (ours, not from the text)
Binary erasure channel with f = 0.5, uniform input.
- P(y=0) = 0.5×0.5 = 0.25, P(y=1) = 0.25, P(y=?) = 0.5.
- H(Y) = 0.25·2 + 0.25·2 + 0.5·1 = 1.5 bits.
- H(Y|X) = H₂(0.5) = 1 bit for each x.
- I(X;Y) = 1.5 − 1 = 0.5 bits.
- Cross-calculation via H(X) − H(X|Y): H(X) = 1. A "?" (probability 0.5) leaves x uncertain by 1 bit, otherwise 0, so H(X|Y) = 0.5·1 = 0.5 and I = 0.5.
- This equals 1 − f = 0.5, the capacity formula printed on p. 158.
- Code of N = 2 with codewords 00 and 11: K = 1, rate R = 1/2. The decoder fails only on "??", with probability 0.5×0.5 = 0.25. Rate = C here, but N = 2 is too short for a small error. The theorem needs large N.

## Concepts
- [[mutual-information]] — I(X;Y) = H(X) − H(X|Y) = H(Y) − H(Y|X); input-to-output information, depends on P_X (p. 149)
- [[joint-and-conditional-entropy]] — H(X|Y) averages H(X|y) over y; can exceed H(X) for a particular y (p. 147)
- [[noisy-channel]] — discrete memoryless channel: alphabets plus P(y|x), written as matrix Q with columns as probability vectors (p. 147)
- [[channel-capacity]] — C(Q) = max over P_X of I(X;Y) (9.10) (p. 150)
- [[noisy-channel-coding-theorem]] — part one: any R < C is achievable with arbitrarily small maximal block error for large N (p. 152)
- [[typical-set-aep]] — used for counting: ≈ 2^{NH(Y)} typical outputs, ≈ 2^{NH(Y|X)} per typical input (p. 154)
- [[bayes-theorem]] — used to infer inputs from outputs and in the optimal decoder (p. 148)
- [[posterior-distribution]] — P(x|y); the optimal decoder maximizes it (p. 152)
- [[block-code-rate-decoder]] (new) — (N,K) block code with S = 2^K codewords, rate R = K/N, decoder from output strings to labels (p. 151)
- [[block-error-probability]] (new) — average p_B (9.15) versus maximal p_BM (9.16) (p. 152)
- [[maximum-likelihood-decoding]] (new) — optimal (max-posterior) decoding equals max likelihood when the prior on s is uniform (p. 152)
- [[extended-channel]] (new) — N uses of a channel treated as one channel with |A_X|^N inputs (p. 153)
- [[non-confusable-subset]] (new) — inputs whose outputs are essentially disjoint; gives error-free communication (p. 152)
- [[generative-modelling]] (new) — model P(y|x), combine with prior P(x), invert by Bayes (p. 156)

## Canonical instances
- [[binary-symmetric-channel]] — flips each bit with prob. f; C = 1 − H₂(f), 0.39 bits at f = 0.15 (pp. 148, 151)
- [[binary-erasure-channel]] — erases with prob. f; C = 1 − f (pp. 148, 158)
- [[noisy-typewriter]] — C = log₂9 reached with a length-1 code on every third letter (pp. 148, 152)
- [[z-channel]] — asymmetric; optimal p₁* = 0.445, C = 0.685 at f = 0.15 (pp. 148, 151)
- [[handwritten-digit-channel]] — pattern recognition as decoding the output of a noisy channel (p. 156)
- [[birthday-problem]] — expected number of collisions S(S−1)/(2A) as insight for random coding (p. 160)

## Bridges (candidates)
- [same-math] Optimal block decoder argmax P(s|y) ↔ bayesian: MAP estimation with the codeword as the hypothesis and the channel as the likelihood.
- [same-math] Mutual information I(X;Y) = H(X) − H(X|Y) ↔ bayesian: expected reduction in uncertainty about an unknown (the input) after an observation (the output) — the same quantity, computed from the Bayes posterior P(x|y).
- [structural-analogy] Counting 2^{NH(Y)}/2^{NH(Y|X)} typical-set balls ↔ information-theory: sphere-packing bounds on code size.
- [structural-analogy] Generative classification via P(y|x)P(x) ↔ bayesian: posterior inference for pattern recognition (speech, digits).
- [metaphor] Adding structured redundancy so noise can be undone ↔ bayesian: priors that let an inference "correct" noisy data.

## Questions this raises
- Does the converse hold exactly: can rates above C never be achieved with small error? (The sketch only suggests "no more" than C, p. 155.)
- How can codes actually reach rates near C, for example on the BEC where C = 1 − f but the encoding is "far from obvious" (p. 158)?
- How does the proof in Chapter 10 turn the typical-set counting into a rigorous argument about block error?
- Why is the symmetry argument for the BSC's optimal input valid (promised "later", p. 151)?

## Exercises worth doing
- Ex. 9.7 and 9.8 (p. 150) — compute I(X;Y) for BSC vs Z channel with uniform input; shows channel asymmetry matters — difficulty: easy / medium
- Ex. 9.12 and 9.13 (p. 151) — capacity of the BSC and BEC for general f, and a comment on the BEC — difficulty: easy / medium
- Ex. 9.14 (p. 154) — build the N = 2 extended BEC and a rate-1/2 code with its decoder — difficulty: medium
- Ex. 9.15 (p. 155) — why the Z-channel optimum favours input 0, and the general-f optimum (9.19) — difficulty: hard
- Ex. 9.18 (p. 155) — Gaussian channel posterior and bit-error probability via Φ — difficulty: medium
- Ex. 9.21–9.22 (pp. 156–157) — birthday problem as a random coding scheme, K large; no solution printed here — difficulty: medium

## Reading notes
- Printed page = pdf page − 12 (pdf 157 = printed 145). All citations use printed numbers.
- The unit begins with a one-page "About Chapter 9" preface (p. 145) listing prerequisites: Chapter 1, exercise 2.26 and exercises 8.2–8.7.
- Extracted text of the noisy-typewriter and extended-channel figures (pp. 148, 153–154) is garbled; the images show matrix diagrams that were not transcribed.
- In the solution to exercise 9.8 (p. 158) the page shows "0.98 − 0.30 = 0.679 bits": rounded entries do not subtract exactly to 0.679 (unrounded values presumably give it).
- In Exercise 9.2's section, the text on p. 149 gives P(y=0) = 0.78 (used again in the printed solution, p. 157).
- Solutions for exercises 9.17, 9.19, 9.21, 9.22 are not printed in these pages.
-
