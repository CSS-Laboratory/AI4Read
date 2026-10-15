---
id: shannon-1948-mathematical/index
work: shannon-1948-mathematical
type: work-map
units: [shannon-1948-mathematical/main-p1, shannon-1948-mathematical/main-p2]
---

# Shannon, C. E. (1948). *A Mathematical Theory of Communication*. Bell System Technical Journal, 27(3), 379–423 and 27(4), 623–656. DOI 10.1002/j.1538-7305.1948.tb01338.x (Part 1); 10.1002/j.1538-7305.1948.tb00917.x (Part 2).

## In one paragraph
Shannon asks how to measure the information a source produces and how fast it can be sent over a channel. He ignores meaning: a message is just one choice from a set of possible messages. Information is measured by entropy, $H=-\sum p_i\log p_i$. On a noiseless channel, good coding sends about $C/H$ symbols per second and no more. On a noisy channel, the capacity $C=\max[H(x)-H_y(x)]$ is the best reliable rate. Below $C$, errors can be made as rare as desired. Above $C$, some equivocation cannot be avoided. The second half extends these ideas to continuous signals. White Gaussian noise gives capacity $W\log(1+P/N)$, and a continuous source has a finite rate only relative to a fidelity criterion. The paper founded the field, and it separates the source from the channel.

## The path through the work
- [[shannon-1948-mathematical/main-p1]] — Information produced by a source is measured by entropy $H=-\sum p_i\log p_i$; $H$ determines the channel capacity needed on a noiseless channel, and on a noisy channel the best reliable rate is the capacity $C=\max[H(x)-H_y(x)]$, a property of the channel.
- [[shannon-1948-mathematical/main-p2]] — Entropy, channel capacity and source rate carry over to continuous signals; the key results are that white noise, whose samples are Gaussian, has maximum entropy for a given power, that capacity is $W\log(1+P/N)$ with white Gaussian noise, and that a continuous source has a finite rate only relative to a chosen fidelity measure.

## Big ideas across units
- **Information as a measure of choice, not meaning.** Only the selection from a set of possible messages counts, and entropy measures it. Discrete case in main-p1; continuous analogue in main-p2. Units: main-p1, main-p2.
- **Entropy as the typical-sequence count.** For long sequences, about $2^{HN}$ sequences matter, and this idea underlies coding in the discrete case. The continuous case again uses typical-sequence arguments. Units: main-p1, main-p2.
- **Capacity as a maximum over input sources.** In the noiseless case, capacity is $\lim \log N(T)/T$. In the noisy case, it is $\max[H(x)-H_y(x)]$. In the continuous case, it is $\max[H(y)-H(n)]$. Units: main-p1, main-p2.
- **Equivocation and the noisy-channel theorem.** Rates below $C$ allow arbitrarily small error, proved by averaging over random codes. Above $C$, the equivocation is at least the excess. The same capacity bound governs delivery of a continuous source. Units: main-p1, main-p2.
- **Maximum entropy and the Gaussian.** Entropy-maximising distributions appear in the choice of source and channel statistics. For a given power, white Gaussian noise has the largest entropy, which gives the entropy power and the capacity formula. Units: main-p1, main-p2.
- **Differences of entropies are what matter.** Continuous entropy depends on the coordinate system and can be negative. Rates and capacities use differences of entropies, so they do not depend on coordinates. Units: main-p2 (building on main-p1).
- **Rate relative to fidelity.** A continuous source has no finite exact rate. The rate becomes finite once a distortion measure is fixed, and it is the minimum mutual information at fixed average distortion. Units: main-p2.

## How to read it
- **Essential:** main-p1 first. It has the entropy definition, the noiseless coding theorem (Theorem 9), equivocation, the noisy capacity and the fundamental theorem (Theorem 11). The catalog entry names Part I and Part II as the focus.
- **Within main-p1 (skippable on a first pass):** the Lagrange-multiplier steps (§§15–16 only), the determinant equation in Theorem 1, and the worked channel cases and Hamming code near the end.
- **Dependency:** main-p2 builds on main-p1. Its stated prerequisites are discrete entropy and channel capacity.
- **Within main-p2:** the capacity $W\log\frac{P+N}{N}$ and the fidelity-based rate (Part V, which introduces rate–distortion) are the main payoffs. The catalog suggests skimming Part IV (the continuous channel) on a first pass. The bounds for arbitrary noise and peak-power limits and the appendices can be skipped at first.

## Concepts introduced
From main-p1:
- [[bit]]
- [[entropy]]
- [[self-information]]
- [[joint-and-conditional-entropy]]
- [[chain-rule]]
- [[mutual-information]]
- [[redundancy]]
- [[entropy-rate]]
- [[typical-set-aep]]
- [[source-coding-theorem]]
- [[huffman-arithmetic-coding]]
- [[noisy-channel]]
- [[channel-capacity]]
- [[noisy-channel-coding-theorem]]
- [[error-correcting-code]]
- [[maximum-entropy-principle]]
- [[equivocation]]
- [[relative-entropy-shannon]]
- [[markoff-source]]
- [[ergodic-source]]
- [[discrete-transducer]]

First appearing in main-p2:
- [[differential-entropy]]
- [[shannon-hartley-formula]]
- [[rate-distortion-function]]
- [[data-processing-inequality]]
- [[entropy-power]]
- [[ensemble-of-functions]]
- [[band-limited-sampling]]
- [[fidelity-criterion]]
- [[dimension-rate]]
