---
id: mackay-2003-information/ch49-repeat
work: mackay-2003-information
unit: "49 Repeat–Accumulate Codes"
pages: 582-587
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
# Repeat–Accumulate Codes

## L0 — One line
A repetition code followed by a random permutation and a running mod-2 sum gives a very simple sparse-graph code that decodes well with the sum–product algorithm, and "generalized parity-check matrices" put many such codes in one notation.

## L1 — The gist (≤ 120 words)
Can a code almost as simple as repetition perform very well? Repeat–accumulate (RA) codes repeat each bit three times, permute the bits, and transmit their running mod-2 sum. Decoding runs sum–product on a factor graph containing an accumulator trellis. On the Gaussian channel the performance is "staggeringly good" for such a simple code, apart from an error floor near block error probability 10⁻⁴. Empirically, the histogram of the number of decoding iterations follows a power law for large iteration counts. The chapter ends with generalized parity-check matrices, a common picture for repetition, LDGM, LDPC, MN, convolutional, turbo and RA codes. This gives one common notation for relating these codes.

**Prerequisites:** mod-2 arithmetic; parity checks and parity-check matrices; factor graphs and the sum–product algorithm (earlier chapters); block error probability; Eb/N0. Terms used above: LDGM = low-density generator-matrix; LDPC = low-density parity-check; a linear MN code is a non-systematic LDPC code (p. 587); puncturing = removing bits before transmission (p. 584); the accumulator trellis is the box in the decoding graph that handles the running-sum chain (p. 583).

## L2 — Key ideas (5–10 bullets)
- The RA encoder takes K source bits, then repeats each ×3, applies a fixed random permutation, and accumulates mod 2. With N = 3K, its rate is 1/3. (p. 582)
- Its factor graph has four node types: equality constraints, parity constraints, intermediate variables and transmitted bits. It is a graph for the prior over codewords. (pp. 582–583)
- Decoding uses sum–product on a graph whose top box is the accumulator trellis, which runs forward–backward. (p. 583)
- Stop-when-done decoding separates detected errors from undetected errors. The text attributes undetected errors to low-weight codewords. (p. 583)
- Six random RA codes (N = 204 to 30 000) perform very well on the Gaussian channel if one does not mind an error floor that starts near block error probability 10⁻⁴. (p. 583)
- The author finds empirically that decoding times have a power-law tail for large τ, P(τ) ∝ τ^{−p}. The tail gets heavier as the signal-to-noise ratio falls. Exercise 49.1 (rated [5]) asks whether density evolution predicts it. (p. 584)
- A generalized parity-check matrix {A, p} adds punctured state columns. It gives a rate bound R ≥ 1 − (M′−S)/(L−S). (p. 585)
- In this notation, a non-systematic LDGM code keeps a simple description although its ordinary parity-check matrix is typically complex and dense. Several known codes are drawn side by side. (pp. 586–587)

## L3 — Walkthrough

**Intro.** The author contrasts RA codes with the repetition code of Chapter 1. RA codes were studied by Divsalar et al. (1998) as simple turbo-like codes that might be easier to analyse than turbo codes. In practice they performed as well as other sparse-graph codes. (p. 582)

**49.1 The encoder.** (p. 582)
1. Take K source bits $s_1\dots s_K$.
2. Repeat each bit three times, so $N=3K$.
3. Permute the N bits with a fixed random permutation, the same for every codeword. Call the result $\mathbf u$.
4. Transmit the accumulated sum:
$$t_1=u_1,\quad t_2=t_1+u_2 \pmod 2,\ \dots,\ t_n=t_{n-1}+u_n \pmod 2,\ \dots,\ t_N=t_{N-1}+u_N \pmod 2 \tag{49.1}$$

*Intuition note:* Repetition gives redundancy. The permutation scrambles which bits sit next to each other. The accumulator links each transmitted bit after the first to the one before it.

**49.2 Graph.** Figure 49.1a uses four node types (p. 582):
- equality constraints;
- intermediate binary variables (black circles);
- parity constraints;
- transmitted bits (white circles).

The source sets the black bits three at a time. The accumulator computes the transmitted bits along the top. This is a factor graph for the *prior probability over codewords*. Each parity node contributes $\mathbb 1[\sum x = 0 \bmod 2]$. Each equality node contributes $\mathbb 1[x_1=x_2=x_3]$. (p. 583)

**49.3 Decoding.** (p. 583)
- The code is normally decoded by sum–product on the graph of figure 49.1b. Its top box is the accumulator trellis, including the channel likelihoods.
- First half of each iteration: the trellis receives likelihoods for every transition. It runs forward–backward to produce likelihoods for each variable node.
- Second half: these likelihoods are multiplied at the equality nodes, giving new messages sent back to the trellis.
- As with Gallager and turbo codes, stop-when-done decoding is possible. It distinguishes undetected errors (caused by low-weight codewords) from detected errors (the decoder gets stuck and knows it failed).
- Figure 49.2 shows six randomly constructed rate-1/3 RA codes on the Gaussian channel, with N from 204 to 30 000. The error floor starts at about block error probability 10⁻⁴. If one does not mind it, performance is "staggeringly good for such a simple code".

*Intuition note:* The decoder is a message-passing loop between a chain (the accumulator) and many small equality checks. It stops when a valid codeword is found. If it never finds one, it knows it failed.

**49.4 Empirical distribution of decoding times.** (p. 584)
- For one code and fixed channel conditions, the number of iterations τ varies randomly.
- The histogram follows a power law for large τ: $P(\tau)\propto\tau^{-p}$.
- The power p depends on the signal-to-noise ratio. It becomes smaller (heavier tail) as the signal-to-noise ratio decreases.
- The author has seen this in RA codes and in irregular and regular Gallager codes.
- Figure 49.3 uses an RA code with K = 10 000, N = 30 000. Fits are $1/\tau^6$ at Eb/N0 = 0.749 dB and $1/\tau^9$ at 0.846 dB. The power laws span several orders of magnitude.
- Exercise 49.1 asks whether density evolution predicts these laws, and whether code design can manipulate them usefully.

**49.5 Generalized parity-check matrices.** (pp. 584–585)
- Motivation: a common representation for relating sparse-graph codes.
- Forney (2001) introduced *normal graphs*. Their only nodes are parity and equality nodes, and variable nodes have degree one or two.
- In an ordinary parity-check matrix, columns are transmitted bits and rows are linear constraints. A generalized one may add columns for state variables that are not transmitted, as if punctured (removed) before transmission.
- State columns are marked by a horizontal line above them. Notation (p. 585):
  - A diagonal line in a square means an identity matrix.
  - Parallel diagonals mean a band-diagonal matrix.
  - A horizontal ellipse with an arrow means the block's columns are randomly permuted.
  - A vertical ellipse with an arrow means the rows are randomly permuted.
  - A circled integer means that many superposed random permutation matrices.

**Definition.** A generalized parity-check matrix is a pair {A, p}. A is a binary matrix and p lists the punctured bits. It defines valid vectors x with
$$\mathbf A\mathbf x=0 \tag{49.2}$$
Each valid x gives a codeword $\mathbf t(\mathbf x)$ by puncturing the bits in p. One code has many such matrices. (p. 585)

**Rate.** Let A be $L\times M'$, p puncture S bits, and N bits be transmitted, with $L=N+S$. Then (p. 585):
$$M=M'-S \tag{49.3}$$
$$K=N-M=L-M' \tag{49.4}$$
$$R\ \ge\ 1-\frac MN=1-\frac{M'-S}{L-S} \tag{49.5}$$
(added step: $K=N-M=(L-S)-(M'-S)=L-M'$.) The text gives "greater than or equal to"; it does not give the reason for the inequality.

*Intuition note:* Punctured columns are not transmitted. The text counts the effective constraints on the codeword as $M=M'-S$, that is, S fewer than the M′ constraints in A. It gives no further reason.

**Examples** (pp. 586–587):
- *Repetition code, rate 1/3:* generator, parity-check and generalized matrices in figure 49.4. (p. 586)
- *Systematic low-density generator-matrix (LDGM) code:* no state variables. $\mathbf t=\mathbf G^{\mathsf T}\mathbf s$ (49.6) with $\mathbf G^{\mathsf T}=\begin{bmatrix}\mathbf I_K\\ \mathbf P\end{bmatrix}$ (49.7). P is a very sparse $M\times K$ matrix, $M=N-K$. The parity-check matrix is $\mathbf H=[\mathbf P|\mathbf I_M]$ (49.8). For rate 1/3 it might be drawn as in figure 49.5. (p. 586)
- *Non-systematic LDGM code:* $\mathbf t=\mathbf G^{\mathsf T}\mathbf s$ (49.9) with $\mathbf G^{\mathsf T}$ a very sparse $N\times K$ matrix. The generalized matrix is $\mathbf A=[\overline{\mathbf G^{\mathsf T}}|\mathbf I_N]$ (49.10), and $\mathbf A\mathbf x=0$ with $\mathbf x=\begin{bmatrix}\mathbf s\\ \mathbf t\end{bmatrix}$ (49.11). The ordinary parity-check matrix is typically complex and dense, but the generalized one stays simple. In the rate-1/2 case the generalized matrix might be represented as in figure 49.6. (p. 586)
- *LDPC and linear MN codes:* figure 49.7a shows a rate-1/3 Gallager code with M/2 columns of weight 2. A linear MN code is a non-systematic LDPC code whose K state bits are the source bits. Figure 49.7b shows rate 1/2. (pp. 586–587)
- *Convolutional codes* (non-systematic, non-recursive): the source bits act as state bits and feed a delay-line. Two linear functions of the delay-line are transmitted, drawn as two parity vectors of length K (figure 49.8a). (p. 587)
- *Concatenation:*
  - Parallel: align the matrices so the source bits line up, and add zero blocks so state and parity bits occupy separate columns.
  - Serial: align the first code's *transmitted* columns with the second code's *source* columns. (p. 587)
- *Turbo code:* the parallel concatenation of two convolutional codes (rate 1/3 in figure 49.8b). (p. 587)
- *RA code:* figure 49.9 shows the rate-1/3 matrix. RA codes are equivalent to staircase codes (section 47.7). (p. 587)
- *Intersection of two codes:* stack their matrices, with transmitted columns aligned and punctured bits in separate columns. (p. 587)

## Toy example (ours, not from the text)
K = 2, s = (1, 0).
- Repeat: 1 1 1 0 0 0, so N = 6 and rate 2/6 = 1/3.
- Permute (we choose positions 1, 4, 2, 5, 6, 3): u = (1, 0, 1, 0, 0, 1).
- Accumulate mod 2:
  - t₁ = 1
  - t₂ = 1+0 = 1
  - t₃ = 1+1 = 0
  - t₄ = 0+0 = 0
  - t₅ = 0+0 = 0
  - t₆ = 0+1 = 1
  - So t = (1, 1, 0, 0, 0, 1).
- Decoder's check: $u_n=t_{n-1}+t_n$ recovers u. The equality constraints say that (u₁,u₃,u₆) are equal and (u₂,u₄,u₅) are equal. Both hold: (1,1,1) and (0,0,0).
- Now flip t₃ to 1. The differences give u = (1,0,0,1,0,1). The first group is (1,0,1) and the second is (0,1,0). Both equality checks fail, so the error is visible.

## Concepts
- [[repeat-accumulate-code]] (new) — repeat each bit ×3, permute, transmit running mod-2 sum; rate 1/3 (p. 582)
- [[factor-graph]] (new) — graph of variable nodes and constraint factors representing the prior over codewords (p. 583)
- [[sum-product-algorithm]] (new) — message passing on the factor graph; the accumulator part runs forward–backward (p. 583)
- [[stop-when-done-decoding]] (new) — stop at a valid codeword; failure is then known (detected error) (p. 583)
- [[error-floor]] (new) — flattening of the error curve near block error probability 10⁻⁴ for these RA codes (p. 583)
- [[decoding-time-power-law]] (new) — P(τ) ∝ τ^{−p} for large τ (p. 584)
- [[generalized-parity-check-matrix]] (new) — pair {A, p}: A binary, p lists punctured state bits (p. 585)
- [[error-correcting-code]] — structured redundancy to correct errors; here the RA code and relatives (p. 582)
- [[noisy-channel]] — here the Gaussian channel for RA tests (p. 583)

## Canonical instances
- [[repetition-code]] — the starting component of the RA code (pp. 582, 585)
- [[turbo-code]] — parallel concatenation of two convolutional codes (p. 587)
- [[low-density-parity-check-code]] — Gallager and MN codes shown in the same notation (pp. 586–587)

## Bridges (candidates)
- [structural-analogy] Factor graph of the prior over codewords with channel likelihoods multiplied in ↔ bayesian: posterior ∝ prior × likelihood; sum–product computes marginal beliefs.
- [structural-analogy] Heavy-tailed decoding times ↔ information-theory/MCMC: convergence-time diagnostics. Only the heavy-tail idea is shared.
- [structural-analogy] Puncturing/state variables ↔ bayesian: latent variables that are marginalized, not observed.

## Questions this raises
- Why does a power law arise, and can density evolution predict p (Exercise 49.1)?
- What causes the error floor, and how do low-weight codewords relate to the permutation?
- Why is the rate in (49.5) only bounded below?
- How do other repeat counts or non-random permutations change performance?

## Exercises worth doing
- Ex. 49.1 (p. 584) — investigate decoding-time power laws and whether code design can shape them — difficulty: hard (marked [5])

## Reading notes
- Printed page = pdf − 12. Source pages 582–587.
- The text layer for the figures is garbled. The figure descriptions above come from the captions and images. Matrix diagrams (figs 49.4–49.9) are only partly captured in words.
- Eq. (49.10) marks the state columns ($\overline{\mathbf G^{\mathsf T}}$) by an overline in the image; (49.11) has none. The text writes A as $L\times M'$, although x has L entries (L = N + S), so the printed dimensions look reversed. The digest copies the source.
- Figure 49.3 panel labels in the image are (a), (ii.b), (ii.c), (iii.b), (iii.c); there is no (i) panel.
