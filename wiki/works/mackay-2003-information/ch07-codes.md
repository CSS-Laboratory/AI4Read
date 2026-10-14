---
id: mackay-2003-information/ch07-codes
work: mackay-2003-information
unit: "7 Codes for Integers"
pages: 132-136
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Codes for Integers

## L0 — One line
Every complete code for integers is optimal for some implicit prior over n, so choosing a code means choosing a prior (or, alternatively, a universal code that does reasonably well across a class of priors).

## L1 — The gist (≤ 120 words)
How can integers be sent as bit strings so that the receiver knows where each one ends? MacKay builds two families of uniquely decodeable codes. Self-delimiting codes (C_α, C_β, …) first send the length of n. End-of-file codes use fixed-size blocks with one reserved block. Each complete code matches an implicit probability distribution, so, MacKay argues, it is better to think about the implicit priors than to ask which code is superior for which n. Codes cannot be switched freely without a cost. Elias's code C_ω is a "universal" code for the class of monotonically decreasing, finite-entropy priors. The chapter is an aside that may be skipped.

**Prerequisites:** binary numbers; prefix codes and the Kraft inequality (complete = Kraft equality); code length ↔ probability, ℓ = −log₂ p; expected value.

## L2 — Key ideas (5–10 bullets)
- Standard binary c_b(n) is not uniquely decodeable, because nothing marks where it ends. Two fixes: send the length first, or use an end-of-file block (p. 132).
- The unary code has length n and is optimal for p_U(n)=2^{-n} (p. 133).
- C_α sends the length in unary; it has length 2l_b(n)−1 and implicit prior P(l)=2^{-l}. Sending the length with the previous code instead gives C_β, C_γ, C_δ (p. 133).
- Byte codes with one end-of-file symbol (base 2^k−1) are almost complete. They match an exponential prior over the number of characters (pp. 134, 136).
- Every complete code is optimal for some prior, so the author says the implicit priors should be thought about, rather than ranking codes by which is shorter for which n (p. 135).
- Choosing the shorter of two codes per message means the message must be lengthened to say which code is used. If this is done by a single leading bit, the result is suboptimal because it fails Kraft equality (p. 135).
- A universal code has, for any distribution in a given class, an average length within some factor of the ideal average length. Elias's C_ω effectively chooses among all C_α, C_β, … (p. 135).

## L3 — Walkthrough

### Definitions (p. 132)
- c_b(n) is the standard binary string, e.g. c_b(5)=101, c_b(45)=101101. l_b(n) is its length (l_b(5)=3, l_b(45)=6).
- c_b is not uniquely decodeable: c_b(5)c_b(5) equals c_b(45). It would be if the length were known (p. 132).
- Every c_b(n) starts with 1. The **headless** representation c_B(n) drops that 1: c_B(5)=01, c_B(45)=01101, c_B(1)=λ (the null string) (p. 132).
- Two strategies: (1) **self-delimiting**: send l_b(n) somehow, then c_B(n); (2) **end-of-file**: use b-bit blocks and reserve one of the 2^b symbols as "end of file" (p. 132).

### Unary code (p. 133)
c_U(n) = n−1 zeros then a 1; length l_U(n)=n. It is optimal if p_U(n)=2^{-n} (p. 133).

### Self-delimiting codes (pp. 133–134)
$$c_\alpha(n)=c_U[l_b(n)]\,c_B(n)\tag{7.1}$$
- Equivalently: (l_b(n)−1) zeros, then c_b(n). Length l_α(n)=2l_b(n)−1 (p. 133).
- Implicit distribution (p. 133):
$$P(l)=2^{-l}\tag{7.2}$$
$$P(n\mid l)=\begin{cases}2^{-l+1}& l_b(n)=l\\0&\text{otherwise}\end{cases}\tag{7.3}$$
- The header always takes about as many bits as the standard binary form (give or take one). If large integers are expected, this seems suboptimal, since files double in size (p. 133). So send the length with C_α instead of unary:
$$c_\beta(n)=c_\alpha[l_b(n)]\,c_B(n)\tag{7.4}$$
$$c_\gamma(n)=c_\beta[l_b(n)]\,c_B(n)\tag{7.5}$$
$$c_\delta(n)=c_\gamma[l_b(n)]\,c_B(n)\tag{7.6}$$
- Table 7.2 example: c_β(2)=0100, c_γ(2)=01000 (p. 133).

*Intuition note:* The header says "how many bits follow". The aim of coding the header with a better code is to make it shorter when integers are large. Each code in the sequence has a different implicit prior over n.

### Codes with end-of-file symbols (p. 134)
- "Byte" means any fixed-length bit string. Decimal digits in 4-bit bytes leave six unused symbols (1010–1111) that can mark the end (p. 134).
- More than one end symbol is redundant. So use base 15 with 1111 as the only end symbol. The same works for bases 3 and 7, and any base 2^n−1 (p. 134).
- Table 7.3: c_3(1)=01 11; c_3(45)=01 10 00 00 11; c_7(1)=001 111 (p. 134).
- These codes are almost complete (complete = satisfies Kraft with equality). The remaining inefficiency: they can encode zero and the empty string, which are not needed (p. 134).
- **Ex. 7.1 solution (p. 136):** with base q, the code assumes probability 1/(q+1) that the current character is the last one. So its prior over length is exponential. (a) For eight-bit blocks (q=255), the expected number of characters is q+1=256, giving ≈ 256×8 ≈ 2000 bits. (b) For files of about 100 kilobytes, require q log q ≃ 800 000 bits. A q between 2^15 and 2^16 satisfies this, so 16-bit blocks are roughly optimal with one end-of-file symbol.

### Encoding a tiny file (p. 134)
"Claude Shannon." as seven-bit ASCII is the 30-digit decimal integer n = 167 987 786 364 950 891 085 602 469 870. Its unary code would need that many (less one) zeros; the author says that if all the oceans were turned into ink and a hundred bits were written per cubic millimeter, there might be enough ink to write it. c_b(n) has length 98 (p. 134). For Ex. 7.2, the text says the shortest representation is c_15 (p. 134).

### Comparing the codes (p. 135)
- **Author's view:** "for n>k code 1 is better" misses the point. Any complete code is optimal for the prior it implies; no other code is "superior" to it. Think about the implicit priors and pick the best for your application (p. 135).
- You cannot switch for free to whichever code is shorter. If one did, the message would have to be lengthened to say which code was used. If this is done with one leading bit, the result is suboptimal, because it fails Kraft equality (exercise 5.33) (p. 135).
- **Alternative world view:** a code is **universal** for a class of distributions if, for any distribution in the class, its average length is within some factor of the ideal. The conventional class: priors that assign monotonically decreasing probability over integers and have finite entropy (p. 135). Several codes above are universal (p. 135).
- **Elias's code C_ω** (Elias, 1975) effectively chooses from all C_α, C_β, …. It sends a sequence of messages. Each encodes the length of the next, and a single bit says whether a message is the final integer. Leading 1s are omitted, since every positive integer starts with 1 (p. 135).
- Algorithm 7.4, generated right to left (p. 135):
  - Write '0'.
  - Loop: if ⌊log n⌋=0, halt; prepend c_b(n); set n := ⌊log n⌋.
- Table 7.5: c_ω(1)=0, c_ω(2)=100, c_ω(4)=101000, c_ω(1025)=111010100000000010 (p. 136).
- Ex. 7.3 asks the reader to show that C_ω is not best for a prior expecting very large integers (p. 135).

*Intuition note:* A universal code is not tuned to one prior. It is only required to have an average length within some factor of the ideal for each prior in the class. A complete code is optimal for the prior it implies.

## Toy example (ours)
Implicit prior of C_α for n=6.
- c_b(6)=110, so l_b=3. c_U(3)=001. c_B(6)=10. So c_α(6)=00110 (matches Table 7.1), length 5 = 2·3−1.
- Probability from the code: 2^{-5}=1/32. From (7.2)–(7.3): P(3)=2^{-3}=1/8, and P(6|3)=2^{-3+1}=1/4. Product = 1/32.
- Check: the integers with l_b=3 are 4,5,6,7, so 4×(1/32)=1/8=P(3).

Elias C_ω(6): write 0; ⌊log 6⌋=2≠0, prepend c_b(6)=110 → 1100; n=2; ⌊log 2⌋=1≠0, prepend c_b(2)=10 → 101100; n=1; ⌊log 1⌋=0, halt. Result 101100, as in Table 7.5.

## Concepts
- [[prefix-code-kraft]] — complete code = Kraft equality; any complete code is optimal for the prior it implies (pp. 134–135)
- [[universal-coding]] — a code within some factor of the ideal average length for every prior in a class, here monotone decreasing with finite entropy (p. 135)
- [[prior-distribution]] — here, the distribution over n implied by a code's lengths (p. 135)
- [[self-delimiting-code]] (new) — first send the length of n, then c_B(n), so the end is known (p. 132)
- [[unary-code]] (new) — n−1 zeros then 1; optimal for 2^{-n} (p. 133)
- [[headless-binary]] (new) — c_b(n) without its leading 1 (p. 132)
- [[end-of-file-code]] (new) — fixed-size blocks with one reserved terminating block (p. 132)
- [[elias-omega-code]] (new) — C_ω, recursive length messages with a one-bit continue flag (p. 135)

## Canonical instances
- [[unary-optimal-for-geometric-prior]] — unary code is optimal for p_U(n)=2^{-n} (p. 133)
- [[eof-code-exponential-prior]] — end-of-file code in base q implies probability 1/(q+1) of stopping at each character (p. 136)
- [[claude-shannon-integer]] — a 14-character file as a 98-bit integer (p. 134)

## Bridges (candidates)
- [structural-analogy] code choice ↔ bayesian: choosing a prior; each complete code is Bayes-optimal for one prior over n (p. 135).
- [structural-analogy] universal code for a class of priors ↔ information-theory: universal coding / MDL-style codes (canon link; not stated in this unit).
- [metaphor] Elias's recursive length headers ↔ recursion: a length is itself an integer, so it is encoded the same way.

## Questions this raises
- How large must n be before another code beats Elias's C_ω for a prior expecting huge integers (Ex. 7.3)?
- What is the implicit prior of C_ω, and how does its tail compare with the 2^{-n} or 1/n^k tails?
- How much overhead does a universal code pay, relative to the ideal code for each prior in its class?

## Exercises worth doing
- Ex. 7.1 (p. 134) — turns an end-of-file code into an exponential prior and gives the optimal block size — difficulty: medium
- Ex. 7.2 (p. 134) — builds C_α…C_δ and c_3, c_7, c_15 for a 98-bit integer; shows the effect of the length header — difficulty: easy
- Ex. 7.3 (p. 135) — shows that "universal" is not "best for every prior" — difficulty: medium

## Reading notes
- Printed = pdf − 12.
- The chapter opens with "Solution to exercise 6.22 (p. 127)", so the definitions double as that solution.
- The text layer of Tables 7.1 and 7.2 loses the overlines (which mark the c_U and c_B parts); the images show them.
- The base of "log" in the Ex. 7.1(b) solution is not stated (presumably 2), and the step from "100 kilobytes" to "q log q ≃ 800 000" is not derived.
- Ex. 7.2 prints only the answer (c_15 is shortest), not the codewords.
