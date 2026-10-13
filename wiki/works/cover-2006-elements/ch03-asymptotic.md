---
id: cover-2006-elements/ch03-asymptotic
work: cover-2006-elements
unit: "3 The Asymptotic Equipartition Property"
pages: 50-59
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# The Asymptotic Equipartition Property

## L0 — One line
For i.i.d. data, the per-symbol surprisal of a long observed sequence converges in probability to the entropy H, so almost all probability sits on about 2^{nH} sequences of probability about 2^{-nH}.

## L1 — The gist (≤ 120 words)
The chapter asks how likely an observed long sequence is, and how many sequences really matter. The answer is the AEP: for i.i.d. variables, −(1/n) log p(X₁,…,Xₙ) → H in probability. This follows from the weak law of large numbers. The sequences whose probability is close to 2^{−nH} form the typical set. For large n it holds nearly all the probability, and it has at most 2^{n(H+ε)} elements. This gives a simple compression scheme using about nH bits per block on average. The typical set is also, to first order in the exponent, as small as any set with probability near 1.

**Prerequisites:** entropy as E[−log p(X)]; i.i.d. variables; weak law of large numbers (convergence in probability); logarithms base 2.

## L2 — Key ideas
- The AEP is the law of large numbers applied to the i.i.d. variables log p(Xᵢ). The sample entropy −(1/n) log p(X₁,…,Xₙ) converges in probability to H(X) (Thm 3.1.1, p. 51).
- "Almost all events are almost equally surprising": with high probability, an observed sequence has probability 2^{−n(H±ε)} (p. 51).
- The typical set A_ε^(n) is defined by the probability bounds (3.6). It has probability > 1−ε for large n, and |A| ≤ 2^{n(H+ε)}. For large n, |A| ≥ (1−ε)2^{n(H−ε)} (Thm 3.1.2, pp. 51–52).
- Coding scheme: index typical sequences with ≤ n(H+ε)+2 bits and use a brute-force code with a flag bit for the rest. Average length per symbol is ≤ H+ε for large n (pp. 53, 55).
- Any set B_δ^(n) with probability ≥ 1−δ (δ<½) needs at least about 2^{nH} elements (to first order in the exponent), so the typical set is nearly the smallest high-probability set (Thm 3.3.1, p. 55).
- The notation a_n ≐ b_n means equality to first order in the exponent (3.26). Both set sizes are ≐ 2^{nH} (pp. 55–56).
- The typical set is not the set containing the single most likely sequence. For Bernoulli(0.9), the all-1s sequence is not typical but is in B_δ (p. 56).

## L3 — Walkthrough

**Introduction (pp. 50–51).** The AEP is the information-theory analogue of the law of large numbers. It is a direct consequence of the weak law (p. 50). The law of large numbers says (1/n)ΣXᵢ is close to EX. The AEP says (1/n) log(1/p(X₁,…,Xₙ)) is close to H, so the observed sequence has probability close to 2^{−nH} (p. 50).

The sequences split into a *typical set* (sample entropy near true entropy) and a *non-typical set*. A property proved for typical sequences holds with high probability (p. 50).

*Example (Bernoulli).* X ∈ {0,1}, p(1)=p, p(0)=q, i.i.d. A sequence has probability ∏p(xᵢ) = p^{Σxᵢ} q^{n−Σxᵢ}. For (1,0,1,1,0,1) this is p⁴q². Not all 2ⁿ sequences are equally probable (p. 50). Asking for p(X₁,…,Xₙ) of the sequence actually drawn is "insidiously self-referential, but well defined" (p. 50). The slogan is "Almost all events are almost equally surprising", i.e.
$$\Pr\{(X_1,\dots,X_n): p(X_1,\dots,X_n)=2^{-n(H\pm\epsilon)}\}\approx 1 \tag{3.1}$$
In the example, the number of 1s is close to np with high probability. All such sequences have roughly the same probability 2^{−nH(p)} (p. 51).

**3.1 The AEP (pp. 51–52).**

*Theorem 3.1.1 (AEP).* If X₁,X₂,… are i.i.d. ∼ p(x), then
$$-\frac1n\log p(X_1,\dots,X_n)\to H(X)\quad\text{in probability}\tag{3.2}$$
*Proof.* Functions of independent variables are independent, so the log p(Xᵢ) are i.i.d. By the weak law (p. 51):
$$-\frac1n\log p(X_1,\dots,X_n)=-\frac1n\sum_i\log p(X_i)\tag{3.3}$$
$$\to -E\log p(X)\ \text{ in probability}\tag{3.4}$$
$$=H(X)\tag{3.5}$$

*Definition (typical set).* A_ε^(n) is the set of (x₁,…,xₙ) ∈ 𝒳ⁿ with
$$2^{-n(H(X)+\epsilon)}\le p(x_1,\dots,x_n)\le 2^{-n(H(X)-\epsilon)}\tag{3.6}$$

*Theorem 3.1.2.* (p. 52)
1. If (x₁,…,xₙ) ∈ A_ε^(n), then H(X)−ε ≤ −(1/n) log p(x₁,…,xₙ) ≤ H(X)+ε.
2. Pr{A_ε^(n)} > 1−ε for n sufficiently large.
3. |A_ε^(n)| ≤ 2^{n(H(X)+ε)}.
4. |A_ε^(n)| ≥ (1−ε)2^{n(H(X)−ε)} for n sufficiently large.

*Proof.* (1) is immediate from (3.6). (2) follows from Theorem 3.1.1: for any δ>0 there is n₀ such that for n ≥ n₀
$$\Pr\Big\{\Big|-\tfrac1n\log p(X_1,\dots,X_n)-H(X)\Big|<\epsilon\Big\}>1-\delta\tag{3.7}$$
Setting δ=ε gives (2). (The text notes that it uses ε for two purposes, p. 52.)

For (3):
$$1=\sum_{x\in\mathcal X^n}p(x)\tag{3.8}$$
$$\ge\sum_{x\in A_\epsilon^{(n)}}p(x)\tag{3.9}$$
$$\ge\sum_{x\in A_\epsilon^{(n)}}2^{-n(H(X)+\epsilon)}\tag{3.10}$$
$$=2^{-n(H(X)+\epsilon)}|A_\epsilon^{(n)}|\tag{3.11}$$
The second inequality uses (3.6). Hence
$$|A_\epsilon^{(n)}|\le 2^{n(H(X)+\epsilon)}\tag{3.12}$$
For (4), for n large, Pr{A} > 1−ε, so
$$1-\epsilon<\Pr\{A_\epsilon^{(n)}\}\tag{3.13}$$
$$\le\sum_{x\in A_\epsilon^{(n)}}2^{-n(H(X)-\epsilon)}\tag{3.14}$$
$$=2^{-n(H(X)-\epsilon)}|A_\epsilon^{(n)}|\tag{3.15}$$
Hence
$$|A_\epsilon^{(n)}|\ge(1-\epsilon)2^{n(H(X)-\epsilon)}\tag{3.16}$$
(pp. 52–53). The typical set has probability nearly 1, its elements are nearly equiprobable, and it has nearly 2^{nH} elements (p. 52).

*Intuition note.* For a long random sequence, with high probability, its "−log probability per symbol" settles near H. Sequences with that value share almost all the probability and each has probability about 2^{−nH}, so they cannot be more numerous than about 2^{nH}.

**3.2 Consequences of the AEP: data compression (pp. 53–55).** Split 𝒳ⁿ into A_ε^(n) and its complement (Fig. 3.1). Order the elements of each set (say lexicographically).
- A typical sequence is described by its index. There are ≤ 2^{n(H+ε)} of them, so the index needs ≤ n(H+ε)+1 bits (the extra bit because n(H+ε) may not be an integer). Prefixing a 0 gives ≤ n(H+ε)+2 bits (p. 53).
- A non-typical sequence is indexed with ≤ n log|𝒳|+1 bits, prefixed by 1 (p. 53).

Features of the code (p. 53):
- It is one-to-one and easily decodable. The first bit is a flag telling the length of the codeword that follows.
- The atypical set is enumerated by brute force, ignoring that it is smaller than 𝒳ⁿ. This is "good enough" for an efficient description.
- Typical sequences get descriptions of length ≈ nH.

[unreadable p. 54]: the text layer is garbled and no page image was supplied. The length computation that leads to the next result is therefore not digested here. The result visible on p. 55 is
$$E\Big[\tfrac1n\,\ell(X^n)\Big]\le H(X)+\epsilon\tag{3.23}$$
for n sufficiently large. (The meaning of ℓ(Xⁿ) is not defined on the pages visible here.) The author concludes that sequences Xⁿ can be represented using nH(X) bits on average (p. 55).

*Intuition note.* Typical sequences are cheap (≈ nH bits). Atypical ones need more bits (not more than n log|X|+1, plus the flag bit, p. 53), but the typical set has probability above 1−ε for large n (p. 52). How these combine into (3.23) is on p. 54 and is not digested.

**3.3 High probability sets and the typical set (pp. 55–56).** The typical set is small and holds most of the probability, but it is not obvious that it is the smallest such set (p. 55).

*Definition.* For each n let B_δ^(n) ⊂ 𝒳ⁿ be any set with
$$\Pr\{B_\delta^{(n)}\}\ge1-\delta\tag{3.24}$$
The author argues that B must intersect A substantially and so must have about as many elements. The proof is outlined in Problem 7 (p. 55).

*Theorem 3.3.1.* Let X₁,…,Xₙ be i.i.d. ∼ p(x). For δ < ½ and any δ′ > 0, if Pr{B_δ^(n)} > 1−δ, then
$$\tfrac1n\log|B_\delta^{(n)}|>H-\delta'\quad\text{for } n \text{ sufficiently large}\tag{3.25}$$
So B must have at least about 2^{nH} elements, to first order in the exponent. A has 2^{n(H±ε)}, so A is about the size of the smallest high-probability set (p. 55).

*Definition.* a_n ≐ b_n means
$$\lim_{n\to\infty}\frac1n\log\frac{a_n}{b_n}=0\tag{3.26}$$
that is, equality to first order in the exponent. The results restate as
$$|B_\delta^{(n)}|\doteq|A_\epsilon^{(n)}|\doteq 2^{nH}\tag{3.27}$$
(pp. 55–56).

*Example (Bernoulli, p = 0.9).* Typical sequences have a proportion of 1s close to 0.9. This excludes the most likely single sequence, all 1s. B_δ includes all the most probable sequences, so it includes all 1s. By Theorem 3.3.1, A and B both contain the sequences with about 90% 1s, and they are almost equal in size (p. 56).

*Intuition note.* "Typical" does not mean "most likely individual outcome". It means "the kind of outcome that carries the bulk of the probability". For δ < ½, even the cheapest high-probability set cannot be exponentially smaller than the typical set (Thm 3.3.1, p. 55).

**Summary and notes (pp. 56, 59).** The summary restates (3.28)–(3.30), with B_δ^(n) defined as the smallest set with probability ≥ 1−δ and |B_δ^(n)| ≐ 2^{nH} for δ < ½ (p. 56). The historical notes credit the AEP to Shannon's 1948 paper for i.i.d. processes. They list later extensions (McMillan, Breiman, Chung and others) to ergodic, countable-alphabet and continuous-valued sources (p. 59).

## Toy example (ours, not from the text)
Let X ∈ {0,1} with p(1)=1/4, p(0)=3/4, n=4, ε=0.1. Surprisal of a 1 is 2 bits. Surprisal of a 0 is log₂(4/3)=0.41504 bits.
- H = 0.25·2 + 0.75·0.41504 = 0.5 + 0.31128 = 0.81128 bits.
- A sequence with k ones has −(1/4) log p = (2k + 0.41504(4−k))/4:
  - k=0: 0.41504
  - k=1: (2+1.24511)/4 = 0.81128
  - k=2: (4+0.83008)/4 = 1.20752
  - k=3: (6+0.41504)/4 = 1.6038
  - k=4: 2
- Typical means within 0.1 of 0.81128, so only k=1 qualifies. A has 4 sequences, each with probability (1/4)(3/4)³ = 27/256 = 0.1055 = 2^{−4·0.81128}. This is as predicted.
- The bound |A| ≤ 2^{n(H+ε)} = 2^{3.645} ≈ 12.5 holds (4 ≤ 12.5).
- Pr(A) = 4·27/256 = 0.4219. This is below 1−ε, so n=4 is too small for property 2. The AEP is asymptotic.
- The most likely sequence, 0000 (probability 81/256 = 0.316), is not typical. This parallels the all-1s remark on p. 56.

## Concepts
- [[typical-set-aep]] — AEP: −(1/n)log p(X¹ⁿ) → H in probability. Typical set A_ε^(n): sequences with probability in [2^{−n(H+ε)}, 2^{−n(H−ε)}] (pp. 51–52)
- [[entropy-hx]] — H(X) = −E log p(X), the limit of sample entropy (p. 51)
- [[self-information-surprisal]] — −log p(x), used in "almost all events are almost equally surprising" (p. 51)
- [[source-coding-theorem]] — here only a consequence: typical-set code of ≈ nH bits per block (pp. 53, 55); the theorem is not stated in this unit
- [[high-probability-set]] (new) — B_δ^(n) ⊂ 𝒳ⁿ with Pr ≥ 1−δ; the smallest such set has size ≐ 2^{nH} for δ<½ (pp. 55–56)
- [[first-order-exponent-equality]] (new) — a_n ≐ b_n iff (1/n) log(a_n/b_n) → 0 (p. 55)
- [[weak-law-of-large-numbers]] (new) — sample mean → mean in probability; the main tool of the AEP proof (pp. 50–51); Problem 1 (p. 57) outlines its proof

## Canonical instances
- [[bernoulli-sequence-typicality]] — sequences with ≈ np ones share probability ≈ 2^{−nH(p)} (p. 51)
- [[bernoulli-0.9-typical-vs-smallest-set]] — all-1s sequence is most likely but not typical (p. 56)
- [[typical-set-flag-bit-code]] — two-part code with flag bit 0/1 (p. 53)

## Bridges (candidates)
- [same-math] AEP ↔ probability: weak law of large numbers applied to the i.i.d. variables −log p(Xᵢ)
- [structural-analogy] typical set ↔ statistical mechanics: a small set of near-equiprobable microstates carries almost all probability
- [structural-analogy] 2^{nH} typical sequences ↔ coding theory: count of codewords needed, prefiguring compression and channel-coding arguments

## Questions this raises
- How quickly does Pr(A_ε^(n)) approach 1, i.e. how large must n be for a given ε?
- Does the AEP hold for dependent sources (stationary ergodic), as the historical notes suggest (p. 59), with the entropy rate in place of H?
- Is the typical-set code optimal at finite n, and how do prefix codes with variable lengths compare?
- What is the role of the exponent-only equality ≐ if one needs exact set sizes?

## Exercises worth doing
- Ex. 1 (p. 57) — Markov, Chebyshev and the weak law, the tools behind the AEP — difficulty: easy
- Ex. 2 (p. 57) — the limit of [p(X₁,…,Xₙ)]^{1/n} — difficulty: easy
- Ex. 3 (p. 57) — typical-set-like code for p(1)=0.005, n=100; compare exact and Chebyshev bounds — difficulty: medium
- Ex. 5 (p. 58) — log-likelihood ratio between p and q under p — difficulty: medium
- Ex. 7 (p. 58) — proof of Theorem 3.3.1 — difficulty: hard

## Reading notes
- The PDF is the 1991 first edition (page header of p. 50: Copyright 1991 John Wiley & Sons, Inc.; Print ISBN 0-471-06259-6). It is not the 2006 2nd edition cited in the metadata. Numbering and content may differ.
- Printed = pdf − 22.
- The OCR is poor in places (e.g. Theorem 3.1.2, eqs 3.7–3.16, problems), so equations were checked against page images.
- Printed page 54 is garbled in the text layer and no image was supplied. Eqs 3.17–3.22 and the theorem leading to (3.23) are not digested ([unreadable p. 54]).
- Eq. (3.1) prints "p(X₁,…,Xₙ) = 2^{−n(H±ε)}" with "≈ 1" for the probability. This is copied as printed.
- In the summary (p. 56), property 4 of the typical set is omitted. It appears in Theorem 3.1.2 (p. 52).
