---
id: noisy-channel
type: concept
fields: [information-theory, bayesian, llm]
fields_strong: [information-theory, bayesian, llm]
n_sources: 37
n_works: 8
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch08-channel-p1, cover-2006-elements/ch14-network-p1, gibson-2019-efficiency/main, jaynes-2003-probability/ch22-introduction, mackay-2003-information/ch01-introduction, mackay-2003-information/ch08-dependent, mackay-2003-information/ch09-communication, mackay-2003-information/ch13-binary, mackay-2003-information/ch15-further, mackay-2003-information/ch25-exact, mackay-2003-information/ch40-capacity, mackay-2003-information/ch42-hopfield, mackay-2003-information/ch47-low, mackay-2003-information/ch49-repeat, pierce-1980-introduction/ch01-world, pierce-1980-introduction/ch02-origins, pierce-1980-introduction/ch08-noisy, pierce-1980-introduction/ch09-many, pierce-1980-introduction/ch11-cybernetics, polyanskiy-2025-information/ch01-introduction, polyanskiy-2025-information/ch03-divergence, polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch19-error, polyanskiy-2025-information/ch20-random, polyanskiy-2025-information/ch21-channel, polyanskiy-2025-information/ch23-capacity, polyanskiy-2025-information/ch31-basics, polyanskiy-2025-information/ch36-strong-p1, polyanskiy-2025-information/ch36-strong-p2, shannon-1948-mathematical/main-p1, stone-2022-information/appa-glossary, stone-2022-information/ch02-entropy, stone-2022-information/ch04-noisy, stone-2022-information/ch05-entropy, stone-2022-information/ch06-mutual, stone-2022-information/ch07-channel]
raw_ids: [noisy channel]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# noisy-channel

## Canon spine entry

- **noisy channel** (information-theory): a conditional distribution p(y|x) that corrupts transmitted symbols (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 6): output depends probabilistically on input, given by a transition matrix [as `noisy channel`]
- [[cover-2006-elements/ch08-channel-p1]] (p. 184): discrete channel $(\mathcal X,p(y|x),\mathcal Y)$, memoryless if output depends only on current input
- [[cover-2006-elements/ch14-network-p1]] (p. 375): here $p(y^{(1)},\dots,y^{(m)}|x^{(1)},\dots,x^{(m)})$ for the network
- [[gibson-2019-efficiency/main]] (p. 3): transmission with errors from speech errors, noise or inattention
- [[mackay-2003-information/ch01-introduction]] (p. 3): a medium whose output may differ from its input with some probability [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch08-dependent]] (p. 138): a joint ensemble with dependent input and output [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch09-communication]] (p. 147): discrete memoryless channel: alphabets plus P(y|x), written as matrix Q with columns as probability vectors [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch13-binary]] (p. 212): used as in the canon; here for the BSC with $C=1-H_2(f)$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch15-further]] (pp. 234–236): a transition matrix $Q$; columns are inputs in these exercises [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch25-exact]] (p. 324): here memoryless, e.g. Gaussian, described by $P(y\mid t)$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch40-capacity]] (p. 483): the trained weights are treated as a channel from training data to a future user [work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch42-hopfield]] (p. 512, 515): memory viewed as a channel from memories to weights to stable states; capacity counted in bits [work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch47-low]] (p. 557): memoryless channel $P(r_n\mid t_n)$ assumed for decoding [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch49-repeat]] (p. 583): here the Gaussian channel for RA tests [work fields: information-theory, bayesian]
- [[pierce-1980-introduction/ch01-world]] (p. 8): Pierce mentions perfect and imperfect channels only; no definition yet
- [[pierce-1980-introduction/ch02-origins]] (p. 29): a circuit that is subject to unwanted extraneous currents ("noise")
- [[pierce-1980-introduction/ch08-noisy]] (p. 151): channel where the received character is chance-dependent on the sent one, with probabilities $p_x(y)$
- [[pierce-1980-introduction/ch09-many]] (pp. 173–174): a channel with white Gaussian noise of power N added to the signal
- [[pierce-1980-introduction/ch11-cybernetics]] (p. 214): here contrasted: communication theory encodes for a noisy channel, prediction estimates the signal [as `noisy channel`]
- [[polyanskiy-2025-information/ch01-introduction]] (p. xxii): a conditional distribution $P_{Y|X}$, also the statistical model in inference
- [[polyanskiy-2025-information/ch03-divergence]] (p. 29): a Markov kernel $P_{Y|X}$ with input $X$ and output $Y$ [as `noisy channel`]
- [[polyanskiy-2025-information/ch04-mutual]] (pp. 48–50): Markov kernels AWGN, BI-AWGN, BSC [as `noisy channel`]
- [[polyanskiy-2025-information/ch19-error]] (p. 344): here BSC$_\delta^{\otimes n}$, bits flipped independently with probability δ
- [[polyanskiy-2025-information/ch20-random]] (p. 350): a fixed $P_{Y|X}$; the encoder is the design variable
- [[polyanskiy-2025-information/ch21-channel]] (p. 371): here a *sequence* of Markov kernels $P_{Y^n|X^n}$ indexed by blocklength, not a single kernel [as `noisy channel`]
- [[polyanskiy-2025-information/ch23-capacity]] (p. 416): AWGN channel (p. 410) and fading channel
- [[polyanskiy-2025-information/ch31-basics]] (p. 560): the GLM corresponds to the Gaussian channel
- [[polyanskiy-2025-information/ch36-strong-p1]] (p. 626): the known channel $P_{Y|X}$ through which the chain factors
- [[polyanskiy-2025-information/ch36-strong-p2]] (pp. 649, 654): BSC, BEC, BI-AWGN as edge/observation channels
- [[shannon-1948-mathematical/main-p1]] (p. 19): $E=f(S,N)$ with probabilities $p_{\alpha,i}(\beta,j)$
- [[stone-2022-information/appa-glossary]] (p. 241): no entry of this name; the glossary defines noise (p. 244) and the binary symmetric channel
- [[stone-2022-information/ch02-entropy]] (p. 28): channel that may corrupt codewords by noise, so $y_j\ne x_j$
- [[stone-2022-information/ch04-noisy]] (p. 93): channel whose output is the input plus noise, $Y=X+\eta$
- [[stone-2022-information/ch05-entropy]] (p. 130; canon link, not developed here): noise limits information per continuous value, making it effectively discrete
- [[stone-2022-information/ch06-mutual]] (p. 136): output y = x + η with encoder x = g(s) [as `noisy channel`]
- [[stone-2022-information/ch07-channel]] (p. 154): here an additive channel $Y=X+\eta$ [as `noisy channel`]

### bayesian

- [[jaynes-2003-probability/ch22-introduction]] (p. 648): each letter flipped independently with probability $\epsilon$ [work fields: bayesian, information-theory]

## Instances that use it

- [[kelly-gambler-noisy-channel]] — Exercises 33–36: betting on information over a noisy channel — from [[bellman-1957-dp/ch04-iv]]
- [[private-wire-gambler]] — gambler receives results through a noisy channel before the odds adjust — from [[kelly-1956-information/main]]
- [[handwritten-digit-channel]] — pattern recognition as decoding the output of a noisy channel — from [[mackay-2003-information/ch09-communication]]
- [[spelling-correction-hmm]] — noisy channel plus bigram prior, silent state for merges and splits — from [[murphy-2023-pml2/ch29-state-p1]]
- [[noisy-channel-conditional-entropy]] — $H(X|Y)=h(\delta)$ for XOR noise — from [[polyanskiy-2025-information/ch02-entropy]]

## Candidate bridges

- [structural-analogy] Chain $s\to n\to c$ with low efficiency $\phi$ (Fig. 6.1) ↔ information-theory: data processing through a noisy channel — outputs carry limited information about upstream fluctuations. — from [[jaynes-2003-probability/ch06-elementary-p1]] (bayesian → information-theory)
- [structural-analogy] Maximal tolerable mutation rate (error threshold) ↔ information-theory: noisy-channel capacity limit — mutation corrupts the genome "message", and sex raises the tolerable noise. — from [[mackay-2003-information/ch19-have]] (information-theory → information-theory)
- [structural-analogy] MCMC acceptance string as a bottleneck channel ↔ information-theory: noisy channel with capacity limit — a binary decision stream caps information per use. — from [[mackay-2003-information/ch30-efficient]] (information-theory → information-theory)
- [structural-analogy] Capacity in bits per weight ↔ information-theory: channel capacity — memories pass through weights and attractors as through a noisy channel. — from [[mackay-2003-information/ch42-hopfield]] (information-theory → information-theory)
- [structural-analogy] Translation as noisy-channel decoding ↔ information theory: recover a message through a corrupted channel (p. 245) — from [[mcgrayne-2011-theory/ch17-rosetta]] (bayesian → information-theory)
- [metaphor] Language as imperfect code with overlapping code books ↔ information-theory: a noisy channel where sender and receiver hold different codebooks. — from [[pierce-1980-introduction/ch06-language]] (information-theory → information-theory)
