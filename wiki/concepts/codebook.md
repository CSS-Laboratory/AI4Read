---
id: codebook
type: concept
fields: [information-theory, political-science]
fields_strong: [information-theory, political-science]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [grimmer-2022-textasdata/ch18-coding, stone-2022-information/ch07-channel]
generated_by: build_kg.py
---

# codebook

## Definitions in the sources

### information-theory

- [[stone-2022-information/ch07-channel]] (p. 163): table of $m$ codewords of length $n$, each tied to a message [new]

### political-science

- [[grimmer-2022-textasdata/ch18-coding]] (p. 306): written instructions defining categories, with examples and edge cases [new]

## Instances that use it

- [[boydstun-making-the-news]] — hand-coding 31,034 NYT front-page articles with an adapted Policy Agendas codebook — from [[grimmer-2022-textasdata/ch18-coding]]
- [[boydstun-policy-agendas-codebook]] — an existing codebook had to be updated and annotated for new documents — from [[grimmer-2022-textasdata/ch24-causal]]
- [[huffman-example-five-symbols]] — Example 10.3 with codebook 00, 10, 11, 010, 011 — from [[polyanskiy-2025-information/ch12-variable]]
- [[universe-lifetime-codebook]] — at most 2⁶⁰ codewords explored out of 2⁴⁰⁰ — from [[polyanskiy-2025-information/ch19-error]]
- [[fixed-composition-codebook-detectable]] — a permutation-invariant tester detects it — from [[polyanskiy-2025-information/ch28-rate]]
- [[white-gaussian-noise-channel]] — capacity $W\log(P+N)/N$ with white-noise coding by random codebooks — from [[shannon-1948-mathematical/main-p2]]
- [[morse-phrase-codebook]] — numbered phrase list as an early block codebook — from [[stone-2022-information/ch03-source]]
- [[gaussian-codebook-n20]] — $n=20$, $C=2$, $2^{40}\approx10^{12}$ messages — from [[stone-2022-information/ch07-channel]]

## Candidate bridges

- [structural-analogy] human labellers vs a few written principles ↔ computational social science codebooks for LLM annotation: a short instruction text steers many labels. — from [[bai-2022-constitutional/main]] (llm → llm)
- [structural-analogy] Final codebook applied to fresh documents ↔ held-out test data: avoids tuning to the development set (the text names overfitting, p. 304). — from [[grimmer-2022-textasdata/ch18-coding]] (political-science → other:held-out-test-data)
- [structural-analogy] VQ codebook moving-average update (21.80–21.83) ↔ EM M-step for GMM means: means are re-estimated from assigned points. The assignment is hard here. — from [[murphy-2023-pml2/ch21-variational]] (bayesian → other:em-m-step-for)
- [metaphor] Language as imperfect code with overlapping code books ↔ information-theory: a noisy channel where sender and receiver hold different codebooks. — from [[pierce-1980-introduction/ch06-language]] (information-theory → information-theory)
- [structural-analogy] channel $P_{Y|X}$ ↔ statistics: statistical model/experiment — both are conditional distributions, and the codebook is the main point of difference (p. xxii) — from [[polyanskiy-2025-information/ch01-introduction]] (information-theory → other:statistics)
- [structural-analogy] Greedy/random codebook selection ↔ submodular maximization (greedy $1-1/e$ guarantee, integrality gap of an LP relaxation) (pp. 367–369). — from [[polyanskiy-2025-information/ch20-random]] (information-theory → unspecified)
- [structural-analogy] Two-term code length (module switches + within-module names) ↔ information-theory: the two parts of a two-stage code — choose a codebook, then a word in it. — from [[rosvall-2008-maps/main-p2]] (information-theory → information-theory)
- [metaphor] Averaging over random codebooks to prove one good codebook exists ↔ probabilistic existence arguments in mathematics: a random object is good on average, so a good one exists. — from [[stone-2022-information/ch04-noisy]] (information-theory → other:mathematics)
- [structural-analogy] Model defaults to a generic label ("stereotype", "metaphor", "neutral") ↔ measurement validity: taxonomy mismatch between a coder's everyday concept and an expert codebook. — from [[ziems-2024-css/main-p1]] (llm → other:statistics)
- [metaphor] Human-in-the-loop prompt tuning ↔ codebook development in qualitative social science: iterating instructions as one iterates a codebook. — from [[ziems-2024-css/main-p1]] (llm → other:sociology)
