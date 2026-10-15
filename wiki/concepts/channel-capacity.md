---
id: channel-capacity
type: concept
fields: [information-theory, bayesian, control-theory, llm, complex-systems]
fields_strong: [information-theory, bayesian, control-theory, llm, complex-systems]
n_sources: 54
n_works: 9
tiers: [core, reference]
grounding: digests
sources: [ashby-1956-cybernetics/ch08-transmission, ashby-1956-cybernetics/ch09-incessant, cover-2006-elements/ch01-introduction, cover-2006-elements/ch08-channel-p1, cover-2006-elements/ch08-channel-p2, cover-2006-elements/ch10-gaussian, cover-2006-elements/ch13-rate, cover-2006-elements/ch14-network-p1, cover-2006-elements/ch14-network-p4, jaynes-2003-probability/ch22-introduction, mackay-2003-information/ch01-introduction, mackay-2003-information/ch09-communication, mackay-2003-information/ch10-noisy, mackay-2003-information/ch11-error, mackay-2003-information/ch13-binary, mackay-2003-information/ch15-further, mackay-2003-information/ch17-communication, mackay-2003-information/ch40-capacity, mackay-2003-information/ch42-hopfield, mackay-2003-information/ch47-low, mackay-2003-information/ch50-digital, mitchell-2009-guidedtour/ch03-information, pierce-1980-introduction/ch05-entropy, pierce-1980-introduction/ch08-noisy, pierce-1980-introduction/ch09-many, pierce-1980-introduction/ch10-information, pierce-1980-introduction/ch12-information, pierce-1980-introduction/ch14-back, polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch06-extremization, polyanskiy-2025-information/ch07-tensorization, polyanskiy-2025-information/ch15-universal, polyanskiy-2025-information/ch19-error, polyanskiy-2025-information/ch21-channel, polyanskiy-2025-information/ch22-channels, polyanskiy-2025-information/ch23-capacity, polyanskiy-2025-information/ch24-strong, polyanskiy-2025-information/ch25-channel, polyanskiy-2025-information/ch29-evaluating, polyanskiy-2025-information/ch33-mutual, polyanskiy-2025-information/ch34-lower, polyanskiy-2025-information/ch35-entropic, shannon-1948-mathematical/main-p1, shannon-1948-mathematical/main-p2, stone-2022-information/appa-glossary, stone-2022-information/appb-mathematical, stone-2022-information/appf-rules, stone-2022-information/ch02-entropy, stone-2022-information/ch03-source, stone-2022-information/ch04-noisy, stone-2022-information/ch06-mutual, stone-2022-information/ch07-channel, stone-2022-information/ch08-rate, stone-2022-information/ch11-information]
raw_ids: [channel capacity]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# channel-capacity

## Canon spine entry

- **channel capacity** (information-theory): the maximum mutual information between input and output; the highest rate of reliable communication (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 7): $\max_{p(x)} I(X;Y)$ [as `channel capacity`]
- [[cover-2006-elements/ch08-channel-p1]] (pp. 184, 194): $\max_{p(x)}I(X;Y)$ ("information" capacity); the operational version is the supremum of achievable rates, and they are equal
- [[cover-2006-elements/ch08-channel-p2]] (p. 205): $C=\max_{p(x)}I(X;Y)$; also shown not to grow with $n$ uses of a DMC (Lemma 8.9.2)
- [[cover-2006-elements/ch10-gaussian]] (pp. 241–242): here $C=\max_{EX^2\le P}I(X;Y)$, and also the supremum of achievable rates
- [[cover-2006-elements/ch13-rate]] (p. 367): dual of $R(D)$; same alternating algorithm computes it
- [[cover-2006-elements/ch14-network-p1]] (p. 378): here $C=\tfrac12\log(1+P/N)$ for the Gaussian channel
- [[cover-2006-elements/ch14-network-p4]] (p. 450): here, capacity regions of multi-user channels. Feedback can enlarge them, unlike the single-user memoryless case
- [[mackay-2003-information/ch01-introduction]] (pp. 14–15): maximum rate with arbitrarily small p_b; for the BSC, 1 − H₂(f) [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch09-communication]] (p. 150): C(Q) = max over P_X of I(X;Y) (9.10) [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch10-noisy]] (p. 162): $C=\max_{P_X}I(X;Y)$ for a discrete memoryless channel [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch11-error]] (pp. 180–181): maximum mutual information under the input cost constraint; for the Gaussian channel $\tfrac12\log(1+v/\sigma^2)$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch13-binary]] (p. 212): used as in the canon; here for the BSC with $C=1-H_2(f)$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch15-further]] (pp. 234–236, 239): to be derived for several channels (e.g. 15.11–15.15); $C=5$ bits for 15.12 [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch17-communication]] (p. 251): here $\lim\frac1N\log M_N$, with $M_N$ the number of valid length-$N$ strings [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch40-capacity]] (p. 484): here, the largest N for which all N target bits are reproduced with very small error through the weights; the author says this departs a little from Chapter 9 [work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch42-hopfield]] (p. 512, 515): memory viewed as a channel from memories to weights to stable states; capacity counted in bits [work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch47-low]] (pp. 565, 567): "Shannon limit" used as the benchmark for noise level and signal-to-noise ratio [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch50-digital]] (p. 589): for this channel (1−f)l bits per use, with or without feedback [work fields: information-theory, bayesian]
- [[pierce-1980-introduction/ch05-entropy]] (p. 97): highest entropy (bits/s) that can be sent over a given error-free channel
- [[pierce-1980-introduction/ch08-noisy]] (pp. 155–156, 164): maximum rate $R$ over message sources, in bits per symbol or per second
- [[pierce-1980-introduction/ch09-many]] (pp. 175–176): for a Gaussian channel, $C=W\log(1+P/N)$, the highest rate of negligible-error signalling
- [[pierce-1980-introduction/ch10-information]] (p. 192): here the Gaussian-channel result $C=W\log_2(1+P/N)$, used with $N=kTW$
- [[pierce-1980-introduction/ch12-information]] (pp. 234, 237): highest attainable rate after best encoding; the person is treated as such a channel
- [[pierce-1980-introduction/ch14-back]] (p. 269): capacity of noiseless and noisy channels, part of the core
- [[polyanskiy-2025-information/ch04-mutual]] (p. 49): only mentioned: the Fig. 3.2 caption says these mutual informations will be shown to be the channels' capacities [as `channel capacity`]
- [[polyanskiy-2025-information/ch06-extremization]] (p. 94): here $\sup_{P_X\in\mathcal P}I(X;Y)$ over a convex input set; may be written as a min over outputs
- [[polyanskiy-2025-information/ch07-tensorization]] (p. 106): max over inputs of mutual information; the unconstrained capacity is additive for memoryless channels
- [[polyanskiy-2025-information/ch15-universal]] (pp. 248, 251, 263): used with the meanings of the canon list
- [[polyanskiy-2025-information/ch19-error]] (p. 346): $C=\max I(X_1;Y_1)$; for BSC, log 2 − h(δ)
- [[polyanskiy-2025-information/ch21-channel]] (p. 373): $C=\lim_{\epsilon\to0}\liminf_n\frac1n\log M^*(n,\epsilon)$, an operational quantity [as `channel capacity`]
- [[polyanskiy-2025-information/ch22-channels]] (p. 395): here $C(P)$: the highest rate at which codewords satisfying a cost constraint can be sent with vanishing error
- [[polyanskiy-2025-information/ch23-capacity]] (p. 414): here, capacity-cost $C(P)$ and its derivative at 0
- [[polyanskiy-2025-information/ch24-strong]] (p. 425): the supremum of rates with vanishing error; here $C=\max I(X;Y)$ with $P_Y^*$ unique
- [[polyanskiy-2025-information/ch25-channel]] (p. 443): here $C=\sup_{P_X}I(X;Y)$ and $C_{fb}=C$ for stationary memoryless channels
- [[polyanskiy-2025-information/ch29-evaluating]] (p. 515): $C=\sup_{P_X}I(X;Y)$, appears in $C/R(D)$
- [[polyanskiy-2025-information/ch33-mutual]] (p. 585): $\sup_\pi I(\theta;X)$ for the model $P_{X|\theta}$ [as `channel capacity`]
- [[polyanskiy-2025-information/ch34-lower]] (p. 599–600): here C(T) = sup I(θ;X) over priors on T; equals the KL radius [as `channel capacity`]
- [[polyanskiy-2025-information/ch35-entropic]] (pp. 603, 608–609): here $C_n=\sup_\pi I(\theta;X^n)$, the capacity of $\theta\mapsto X^n$; for a general channel the capacity equals $\inf_\epsilon\{\epsilon^2+\log N_{\rm KL}(\epsilon)\}$ (Thm 32.4); for $C_n$ it is bounded by $\inf_\epsilon\{n\epsilon^2+\log N_{\rm KL}(\mathcal P,\epsilon)\}$
- [[shannon-1948-mathematical/main-p1]] (p. 22): noiseless: $\lim\log N(T)/T$ (p. 3); noisy: $\max[H(x)-H_y(x)]$
- [[shannon-1948-mathematical/main-p2]] (pp. 42–43): here $C=\lim\max\frac1T\iint P\log\frac{P(x,y)}{P(x)P(y)}$, coordinate-free; with independent additive noise $C=\max H(y)-H(n)$
- [[stone-2022-information/appa-glossary]] (p. 242): maximum rate of information from input to output
- [[stone-2022-information/appb-mathematical]] (p. 248): the maximum rate of communication through a channel, printed with $H(X)-H(X|Y)$
- [[stone-2022-information/appf-rules]] (p. 266): $\max_{p(X)}I(X,Y)$ [as `channel capacity`]
- [[stone-2022-information/ch02-entropy]] (p. 29): maximum information communicable from channel input to output; maximum rate over all codes
- [[stone-2022-information/ch03-source]] (pp. 46–48): here, the maximum bits/s a noiseless channel carries, $\max_{p(X)}H(X)$; equals the number of binary digits per second
- [[stone-2022-information/ch04-noisy]] (p. 104): $C=\max_{p(X)}I(X,Y)$
- [[stone-2022-information/ch06-mutual]] (p. 136): C = log m_max, with m_max Shannon's upper bound on discriminable inputs [as `channel capacity`]
- [[stone-2022-information/ch07-channel]] (pp. 153, 155): $\max_{p(X)}I(X,Y)$; here $\max H(Y)-H(\eta)$ [as `channel capacity`]
- [[stone-2022-information/ch08-rate]] (p. 174): identified with a rate R in this chapter [as `channel capacity`]
- [[stone-2022-information/ch11-information]] (p. 218, 228): for a noiseless binary channel, $C=1/\Delta t$ bits/s; 19.2 Mb/s for the satellite link

### control-theory

- [[ashby-1956-cybernetics/ch08-transmission]] (p. 154): a transducer with $r$ states transmits at most $\log_2 r$ bits per step [new; work fields: control-theory, information-theory]
- [[ashby-1956-cybernetics/ch09-incessant]] (p. 180): rate (bits per unit time) at which a channel can transmit variety; "channel" is defined behaviourally [new; work fields: control-theory, information-theory]

### bayesian

- [[jaynes-2003-probability/ch22-introduction]] (p. 629): here the exponential growth rate $\lim\frac1t\log W(t)$ of distinguishable messages; a property of the channel. Not defined as a maximum of mutual information in this unit [work fields: bayesian, information-theory]

### complex-systems

- [[mitchell-2009-guidedtour/ch03-information]] (pdf 77): maximum transmission rate over a channel, even with noise [new]

## Instances that use it

- [[binary-erasure-channel]] — capacity $1-q$ — from [[mackay-2003-information/ch10-noisy]]
- [[z-channel]] — capacity bounded via erasure emulation — from [[mackay-2003-information/ch10-noisy]]
- [[burst-channel-capacity-079-vs-053]] — interleaving's loss on a burst channel — from [[mackay-2003-information/ch11-error]]
- [[binary-symmetric-channel]] — capacity $1+p\log p+(1-p)\log(1-p)$; .53 at 1/10 errors and .92 at 1/100 — from [[pierce-1980-introduction/ch08-noisy]]
- [[two-way-channel-capacity-plot]] — horizontal and vertical lines, 45° line, intermediate curve — from [[pierce-1980-introduction/ch14-back]]
- [[group-noise-channel]] — capacity $\log|G|-H(Z)$ with uniform input — from [[polyanskiy-2025-information/ch21-channel]]
- [[countable-input-counterexample-channel]] — capacity $C$ but $C_\epsilon\ge2C$ for $\epsilon>e^{-1/2}$ — from [[polyanskiy-2025-information/ch24-strong]]
- [[white-gaussian-noise-channel]] — capacity $W\log(P+N)/N$ with white-noise coding by random codebooks — from [[shannon-1948-mathematical/main-p2]]

## Candidate bridges

- [structural-analogy] $\log_2 r$ bits per step through an $r$-state channel ↔ information theory: channel capacity — Ashby derives only an upper bound from state count, in a determinate setting — from [[ashby-1956-cybernetics/ch08-transmission]] (control-theory → information-theory)
- [metaphor] channel capacity as a limit on message flow ↔ a limit on how much information an agent can absorb (our suggestion, not in the source) — from [[cover-2006-elements/ch01-introduction]] (information-theory → unspecified)
- [structural-analogy] rate distortion $\min I(X;\hat X)$ s.t. distortion ↔ information-theory: channel capacity $\max I(X;Y)$ s.t. cost — dual optimizations with a random-coding proof and a shared alternating algorithm. — from [[cover-2006-elements/ch13-rate]] (information-theory → information-theory)
- [metaphor] The code $z$ as a bottleneck ↔ information theory: lossy compression with limited channel capacity. — from [[deisenroth-2020-mml/ch10-dimensionality]] (linear-algebra → information-theory)
- [same-math] $Z(\lambda)=\sum e^{-\lambda t_i}=1$ for channel capacity ↔ statistical mechanics: canonical partition function, with $t_i$ playing the role of energy — the same exponential-weights and multiplier calculation (pp. 631–632). — from [[jaynes-2003-probability/ch22-introduction]] (bayesian → complex-systems)
- [structural-analogy] Flattening by distraction ↔ Noise and channel capacity: disturbance degrades reception. — from [[lippmann-1922-publicopinion/ch05-speed]] (communication-theory → information-theory)
- [structural-analogy] Maximal tolerable mutation rate (error threshold) ↔ information-theory: noisy-channel capacity limit — mutation corrupts the genome "message", and sex raises the tolerable noise. — from [[mackay-2003-information/ch19-have]] (information-theory → information-theory)
- [structural-analogy] Capacity in bits per weight ↔ information-theory: channel capacity — memories pass through weights and attractors as through a noisy channel. — from [[mackay-2003-information/ch42-hopfield]] (information-theory → information-theory)
- [structural-analogy] two-way channel capacity region ↔ multi-user network capacity — trade-off between directions. — from [[pierce-1980-introduction/ch14-back]] (information-theory → unspecified)
- [same-math] $\mathcal R_n^*=\sup_\pi I(\theta;X^n)$ ↔ channel capacity: the "channel" is $\theta\to X^n$ — Theorem 5.9's minimax = maximin. — from [[polyanskiy-2025-information/ch15-universal]] (information-theory → information-theory)
- [structural-analogy] Capacity under a limit on information flow ↔ rational inattention (canon concept) — agents are limited by a channel capacity (canon link; not stated in this unit). — from [[polyanskiy-2025-information/ch21-channel]] (information-theory → unspecified)
- [structural-analogy] Single-letterization of $\phi_{S^n}$ ↔ Corollary 20.5 for channel capacity with separable cost — the text says it parallels it (p. 487). — from [[polyanskiy-2025-information/ch27-rate]] (information-theory → unspecified)
- [same-math] Fano's method with capacity C(T) ↔ channel capacity: C(T) is literally the capacity of the channel θ → X (p. 599). — from [[polyanskiy-2025-information/ch34-lower]] (information-theory → information-theory)
- [metaphor] distributed bit budget ↔ rational inattention: limited channel capacity per agent restricts aggregate inference. — from [[polyanskiy-2025-information/ch36-strong-p2]] (information-theory → information-theory)
- [structural-analogy] Channel capacity as a limit on reliable information rate ↔ rational inattention: agents with a bound on absorbed information — from [[shannon-1948-mathematical/main-p1]] (information-theory → information-theory)
- [metaphor] Channel capacity as a bucket's size ↔ everyday volume: the rate is the amount actually poured (the author's own analogy). — from [[stone-2022-information/ch02-entropy]] (information-theory → other:everyday-volume)
