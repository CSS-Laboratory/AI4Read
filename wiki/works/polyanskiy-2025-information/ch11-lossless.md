---
id: polyanskiy-2025-information/ch11-lossless
work: polyanskiy-2025-information
unit: Part II opening — Lossless data compression
pages: 193-196
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Part II opening: Lossless data compression

## L0 — One line
The main reason compression is possible is the empirical law that real-world sources produce very restricted sets of sequences (often well described probabilistically), and the book will study three modes: variable-length lossless, fixed-length almost lossless, and lossy.

## L1 — The gist (≤ 120 words)
Why can data be compressed at all, and what kinds of compression does the book study? The authors say the main reason is an empirical law that real-world sources produce very restricted sets of sequences. Shannon's lesson is that these restrictions can be described probabilistically, by i.i.d., Markov or similar models, though sometimes a suitable representation must be found first. The book starts with one random variable X, later an n-letter block. It previews three modes. Variable-length lossless compression has optimal length about H(X) (up to stated correction terms). Fixed-length almost lossless compression also reaches the entropy rate and no further, under mild assumptions. Lossy compression is deferred to Part V.

**Prerequisites:** entropy H(X) and entropy rate; i.i.d. and Markov processes; probability of error.

## L2 — Key ideas (5–10 bullets)
- Reducing bits is generally impossible unless only a small subset of sequences captures most of the probability (p. 195).
- The main reason compression is possible is an empirical law: real-world sources give very restricted sets of sequences (p. 195).
- Shannon's empirical law: structure can be described probabilistically with growing precision (i.i.d., first-order, second-order Markov…) (p. 195).
- The choice of representation (characters or words; wavelets rather than raw pixels) matters, but the book assumes it is already made (p. 195).
- Variable-length lossless: optimal length is $H(X) - O(\log(1+H(X)))$; for prefix-free or uniquely decodable codes it is $H(X)+O(1)$ (p. 195).
- Fixed-length almost lossless: error probability at most ϵ is allowed; under mild assumptions one compresses to entropy rate and no further (p. 196).
- Lossy compression requires only $\mathbb{E}[d(X,\hat X)]\le\epsilon$ and is the topic of Part V (p. 196).

## L3 — Walkthrough

**Goal and when it is possible (p. 195).** The engineering goal is to represent a source sequence $a_1,\dots,a_n$ in as few bits as possible, perhaps under algorithmic constraints. Reducing bits is generally impossible unless only a small subset of sequences occurs in practice. More precisely, the restriction is that only a small subset captures the majority of the probability. (p. 195)

**Is this true of real data?** Demonstration: compute letter frequencies in two English novels. They come out approximately the same, so English text has structure restricting its outputs. The structure goes beyond letter frequencies (digrams, word frequencies, etc. may show more). (p. 195)

*Intuition note.* Without such statistical restrictions, reducing the number of bits is generally impossible (p. 195). Compression is possible because only a small subset of sequences captures most of the probability.

**Modeling the restrictions (p. 195).** Experiments with language, music and images suggest the structure is well described by probabilistic generation. Shannon's lasting empirical law: real-world sequences can be described probabilistically with increasing precision by i.i.d., then first-order Markov, then second-order Markov, etc. Sometimes one must find a suitable basis. For language: characters or words. For images: a rasterized pixel sequence shows no stable local structure, whereas wavelets or local Fourier transforms reveal it. The book assumes this step is done and that we face a simple stochastic process (iid, Markov or ergodic). (p. 195)

*Footnote 6 (author's caveat, p. 195).* The "laws" should not be pushed too far. A finite-state Markov assumption is too simplistic to generate all proper sentences (cf. Chomsky). Yet modern high-order Markov models such as GPT-4 are, say the authors, very hard to distinguish from true language.

**Plan (p. 195).** First, represent one random variable X by a minimal number of bits. Later, X is an n-letter chunk $X=S^n=(S_1,\dots,S_n)$ of the process.

**Three compression types.**
1. *Variable-length lossless* (p. 195): require $\mathbb{P}[X\ne\hat X]=0$, where $\hat X$ is the decoded version. X is compressed into a variable-length binary string. The optimal length is $H(X)-O(\log(1+H(X)))$. Restricting to prefix-free or uniquely decodable codes, it is $H(X)+O(1)$. For $X=S^n$, the optimal length divided by n converges to the entropy rate (Section 6.3) of $\{S_j\}$.
2. *Fixed-length, almost lossless* (p. 196): allow $\mathbb{P}[X\ne\hat X]\le\epsilon$ (vanishing as $n\to\infty$ when $X=S^n$). Under mild assumptions on $\{S_j\}$, one can again compress to entropy rate "but no more". This mode permits results with side-information (Slepian–Wolf, etc.).
3. *Lossy* (p. 196): require only $\mathbb{E}[d(X,\hat X)]\le\epsilon$, with $d(\cdot,\cdot)$ a loss function. Topic of Part V.

*Intuition note.* Allowing a tiny error probability does not change the best rate (the entropy rate) in the stated setting. Lossy compression instead requires only that the expected loss $\mathbb{E}[d(X,\hat X)]$ be at most ϵ.

**Terminology (p. 196).** For $X=S^n$, the first two types are better called "fixed-to-variable" and "fixed-to-fixed", since they take a fixed number of input letters. Other types exist, such as Tunstall's variable-to-fixed compressor, which are not discussed. (p. 196)

## Toy example
(Our own.) X takes values $a,b,c,d$ with probabilities $1/2,1/4,1/8,1/8$.
- Fixed-length code: 2 bits for every value, average 2.
- Variable-length prefix-free code: $a\to0$, $b\to10$, $c\to110$, $d\to111$. Average length $=\tfrac12\cdot1+\tfrac14\cdot2+\tfrac18\cdot3+\tfrac18\cdot3=0.5+0.5+0.375+0.375=1.75$.
- Entropy: $H(X)=\tfrac12\cdot1+\tfrac14\cdot2+\tfrac18\cdot3+\tfrac18\cdot3=1.75$ bits. This code meets the entropy, and uses fewer bits than the fixed-length code because the distribution is skewed.

## Concepts
- [[entropy-rate]] — entropy per symbol of the process; the limit of normalized optimal length (p. 195)
- [[source-coding-theorem]] — previewed: optimal lengths $H(X)-O(\log(1+H))$ or $H(X)+O(1)$ (p. 195)
- [[prefix-code-kraft]] — if one restricts to prefix-free or uniquely decodable codes, the optimal length is $H(X)+O(1)$ (p. 195)
- [[lossless-variable-length-compression]] (new) — $\mathbb{P}[X\ne\hat X]=0$, variable-length output (p. 195)
- [[almost-lossless-fixed-length-compression]] (new) — error probability ≤ ϵ, fixed-length output (p. 196)
- [[rate-distortion-function]] — lossy compression with $\mathbb{E}[d(X,\hat X)]\le\epsilon$, deferred to Part V (p. 196)

## Canonical instances
- [[english-letter-frequencies]] — two novels give approximately equal letter frequencies, evidence of structure (p. 195)
- [[pixels-vs-wavelets]] — raster pixels show no stable local structure; wavelet or local Fourier bases do (p. 195)

## Bridges (candidates)
- [structural-analogy] Shannon's i.i.d.→Markov hierarchy ↔ language modeling: higher-order Markov models approximate language (the authors cite GPT-4, p. 195).
- [structural-analogy] Choosing a representation basis ↔ feature engineering: structure sometimes becomes visible only after a change of basis.

## Questions this raises
- How does $H(X)-O(\log(1+H(X)))$ for general codes differ from $H(X)+O(1)$ for prefix-free codes?
- What are the "mild assumptions" under which fixed-length compression reaches the entropy rate and no further?
- How can side-information (Slepian–Wolf) change what is achievable?

## Reading notes
- Printed = pdf − 25. Pages 193–194 are the Part II title page and a blank page; the content is on pp. 195–196.
- The text layer has symbol glitches (for example ≠ appears as "6="); the page 196 image shows the correct symbols, and the equations were read from it. Page 195 was checked against the text layer only.
- Footnote 6 and the "[378, Sec. III]" and "[425]" references are as printed; the bibliography is not in these pages.
