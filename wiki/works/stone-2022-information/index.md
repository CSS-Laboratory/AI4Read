---
id: stone-2022-information/index
work: stone-2022-information
type: work-map
units: [stone-2022-information/ch01-information, stone-2022-information/ch02-entropy, stone-2022-information/ch03-source, stone-2022-information/ch04-noisy, stone-2022-information/ch05-entropy, stone-2022-information/ch06-mutual, stone-2022-information/ch07-channel, stone-2022-information/ch08-rate, stone-2022-information/ch09-transfer, stone-2022-information/ch10-thermodynamic, stone-2022-information/ch11-information, stone-2022-information/appa-glossary, stone-2022-information/appb-mathematical, stone-2022-information/appd-probability, stone-2022-information/appf-rules]
---

# Stone, J. V. (2022). *Information Theory: A Tutorial Introduction* (2nd ed.). Sebtel Press. ISBN 9781739672706. (1st ed. 2015.)

## In one paragraph
Stone explains Shannon's information theory through worked examples. A bit is a measurable amount of information, and entropy is the average surprise of a variable. Entropy sets the limit for compressing a source (the source coding theorem). Mutual information and channel capacity set the limit for reliable communication over a noisy channel (the noisy channel coding theorem). The book extends these ideas to continuous variables and Gaussian channels. The second edition adds rate–distortion theory, which covers sending fewer bits than the source entropy, and transfer entropy, a directed measure of dependence between time series. It then links information to physical entropy and to biological systems, which appear to work close to the theory's limits. Appendices give the notation, logarithm, probability and Gaussian background.

## The path through the work
- [[stone-2022-information/ch01-information]] — One bit is the information needed to choose between two equally probable alternatives, and a bit (an amount of information) is a different kind of thing from a binary digit (a 0 or a 1).
- [[stone-2022-information/ch02-entropy]] — The entropy of a discrete variable is the average surprise, $-\log_2 p(x)$ averaged over its outcomes, and it equals $\log_2 m$ bits when $m$ outcomes are equally probable.
- [[stone-2022-information/ch03-source]] — A source with entropy H bits/symbol can be encoded so that, on average, each symbol needs only a little more than H binary digits, and not fewer, because in practice a source of n-digit binary messages produces only about $2^{nH}$ of its $2^n$ possible messages.
- [[stone-2022-information/ch04-noisy]] — Mutual information $I(X,Y)=H(X)+H(Y)-H(X,Y)$ measures how much a noisy channel's output tells us about its input, and Shannon's theorem says reliable communication is possible at rates up to the capacity $C=\max_{p(X)} I(X,Y)$ but not above it.
- [[stone-2022-information/ch05-entropy]] — The entropy of a continuous variable is infinite, so we use differential entropy, which drops the infinite term and must be read together with the measurement precision.
- [[stone-2022-information/ch06-mutual]] — For continuous channel input X and output Y, mutual information is the average reduction in uncertainty about one variable from observing the other, and it can be written several equivalent ways without any infinities.
- [[stone-2022-information/ch07-channel]] — For a Gaussian channel, capacity $C=\tfrac12\log(1+P/N)$ per value is reached by a Gaussian input; for a bounded-range channel with negligible noise, the best input is uniform, obtained by encoding with the cdf of the message distribution.
- [[stone-2022-information/ch08-rate]] — If some distortion D is tolerated, the minimum number of bits per element needed to represent a source is the rate distortion function R(D), the smallest mutual information I(X; X̂) over encodings that meet D.
- [[stone-2022-information/ch09-transfer]] — Transfer entropy measures how much the past of X reduces uncertainty about the present of Y beyond what Y's own past already does, so it is a directed (time-asymmetric) measure of dependence.
- [[stone-2022-information/ch10-thermodynamic]] — Shannon's information entropy and physical (Boltzmann–Gibbs) entropy are syntactically similar in form, and one bit has a minimum energy cost of 0.693kT joules, which is why Maxwell's demon cannot get free power.
- [[stone-2022-information/ch11-information]] — Information theory gives an absolute scale (bits) for judging how well engineered and biological systems, such as TV links, genomes and neurons, handle information, and the neural systems studied look close to the limits it sets.
- [[stone-2022-information/appa-glossary]] — A short reference list fixing how Stone uses the vocabulary of information theory and the probability and statistics it needs.
- [[stone-2022-information/appb-mathematical]] — This unit is the book's notation key plus a short log tutorial: a logarithm is the power a base must be raised to, and logs turn products into sums.
- [[stone-2022-information/appd-probability]] — A pdf is the limit of a normalised histogram as bins shrink, and an average over a distribution is a probability-weighted sum (or integral), which turns Shannon information into entropy.
- [[stone-2022-information/appf-rules]] — Joint probabilities of independent outcomes multiply, and the product, sum and Bayes rules, the Gaussian density and a list of the book's key entropy equations are collected in these appendices.

## Big ideas across units
- **A bit is an amount of information, not a binary digit.** It is fixed in ch01, reinforced in ch02 and in the glossary, and it underlies the efficiency and cost arguments of ch03 and ch10. Units: [[stone-2022-information/ch01-information]], [[stone-2022-information/ch02-entropy]], [[stone-2022-information/ch03-source]], [[stone-2022-information/ch10-thermodynamic]], [[stone-2022-information/appa-glossary]].
- **Entropy is average surprise.** It is defined for discrete variables, extended to continuous ones as differential entropy (which depends on bin width or noise), and derived as an expectation in the appendix. Units: [[stone-2022-information/ch02-entropy]], [[stone-2022-information/ch05-entropy]], [[stone-2022-information/ch06-mutual]], [[stone-2022-information/appd-probability]].
- **Redundancy and compression have a limit set by entropy.** Compression removes redundancy, and the source coding theorem gives the limit. Units: [[stone-2022-information/ch01-information]], [[stone-2022-information/ch03-source]], [[stone-2022-information/ch11-information]].
- **Mutual information and capacity bound reliable communication.** Mutual information is built in the discrete case, redone for continuous variables, and used to get Gaussian and fixed-range capacities. Units: [[stone-2022-information/ch04-noisy]], [[stone-2022-information/ch06-mutual]], [[stone-2022-information/ch07-channel]], [[stone-2022-information/ch08-rate]].
- **Maximum entropy and efficient encoding.** The entropy-maximising distributions (uniform, exponential, Gaussian) lead to Gaussian-input capacity and cdf encoding, which appears in Laughlin's fly data. Units: [[stone-2022-information/ch05-entropy]], [[stone-2022-information/ch07-channel]], [[stone-2022-information/ch11-information]].
- **Trading information for fidelity or direction.** Rate–distortion theory builds on equivocation and capacity. Transfer entropy adds time direction to mutual information. Units: [[stone-2022-information/ch04-noisy]], [[stone-2022-information/ch08-rate]], [[stone-2022-information/ch09-transfer]].
- **Information has a physical and biological price.** Entropy links to physics through the Landauer limit and Maxwell's demon, and to biology through genomes, neurons and sensory coding. Units: [[stone-2022-information/ch10-thermodynamic]], [[stone-2022-information/ch11-information]].
- **Noise discretises signals and makes counting possible.** Noise limits how many inputs can be told apart, and gives "cross-talk" in the discrete case. Units: [[stone-2022-information/ch04-noisy]], [[stone-2022-information/ch05-entropy]], [[stone-2022-information/ch07-channel]].

## How to read it
- **Essential, in order:** ch01 → ch02 → ch03 → ch04. These give the bit, entropy, source coding and the noisy channel theorem, and every later chapter depends on them.
- **Continuous branch:** ch05 builds on ch02. ch06 needs the discrete mutual information of ch04 together with ch05. ch07 needs ch05's maximum-entropy results (Sec. 5.5–5.6) and ch06.
- **Extensions:** ch08 (rate distortion) assumes entropy, mutual information and the noisy channel theorem (ch02–ch04); its Gaussian case also uses the variance and correlation material. ch09 (transfer entropy) needs conditional entropy and mutual information (ch04 and ch06). It can be read after ch06 without ch07 or ch08, though the material does not say so explicitly.
- **Can be skipped on a first pass:** ch10 (thermodynamics) and ch11 (applications) need only entropy and bits. The proofs, Kolmogorov complexity and the Stirling-based argument at the end of ch03 can also wait.
- **Reference units:** the glossary, notation and logarithm key, and the probability, Gaussian and key-equation appendices. Dip into them when a symbol or rule is unclear. ch01 and ch02 are easier with the logarithm appendix open.

## Concepts introduced
Variant spellings of the same concept have been merged and are listed under the form used where each first appears.

- [[bit]] — ch01
- [[redundancy]] — ch01
- [[self-information-surprisal]] — ch01
- [[source-coding-theorem]] — ch01
- [[entropy]] — ch02
- [[channel-capacity]] — ch02
- [[noisy-channel]] — ch02
- [[random-variable]] — ch02
- [[probability-distribution]] — ch02
- [[encoder-codeword-code]] — ch02
- [[lossless-vs-lossy-compression]] — ch02 (also written lossy-vs-lossless-compression in ch11)
- [[shannon-desiderata]] — ch02
- [[iid-and-stationary-source]] — ch02
- [[nats-bans-shannons]] — ch02
- [[coding-efficiency]] — ch03
- [[huffman-arithmetic-coding]] — ch03
- [[prefix-code-kraft]] — ch03
- [[entropy-rate]] — ch03
- [[correlation-length]] — ch03
- [[typical-set-aep]] — ch03
- [[kolmogorov-complexity]] — ch03
- [[mutual-information]] — ch04
- [[joint-and-conditional-entropy]] — ch04
- [[noisy-channel-coding-theorem]] — ch04
- [[error-correcting-code]] — ch04
- [[rate-distortion-function]] — ch04 (referenced; developed in ch08)
- [[marginalisation]] — ch04
- [[statistical-independence]] — ch04 (also written independence in appf)
- [[equivocation]] — ch04
- [[transmission-efficiency]] — ch04
- [[cross-talk-fan-diagram]] — ch04
- [[binary-symmetric-channel]] — ch04
- [[differential-entropy]] — ch05
- [[bin-width-dependence]] — ch05
- [[maximum-entropy-principle]] — ch05
- [[mle-entropy-bias]] — ch05
- [[residual-uncertainty]] — ch05
- [[chain-rule]] — ch06
- [[relative-entropy-kl]] — ch06
- [[invariance-of-mutual-information]] — ch06
- [[shannon-hartley-formula]] — ch07
- [[signal-to-noise-ratio]] — ch07
- [[correlation-coefficient]] — ch07
- [[codebook]] — ch07
- [[cdf-encoding]] — ch07 (also written cdf-optimal-encoding in ch11)
- [[transfer-entropy]] — ch08 (referenced; developed in ch09)
- [[rate-equivocation-function]] — ch08
- [[distortion-measure]] — ch08
- [[stochastic-encoding]] — ch08
- [[blahut-arimoto-algorithm]] — ch08
- [[conditional-mutual-information]] — ch09
- [[granger-causality]] — ch09
- [[confounding-common-cause]] — ch09
- [[microstate-macrostate]] — ch10
- [[thermodynamic-entropy]] — ch10
- [[ensemble]] — ch10
- [[landauer-principle]] — ch10
- [[second-law-thermodynamics]] — ch10
- [[efficient-coding-hypothesis]] — ch11
- [[sum-difference-recoding]] — ch11
- [[transmission-rate]] — appa-glossary
- [[logarithm]] — appb-mathematical
- [[log-base-change]] — appb-mathematical
- [[information-rate]] — appb-mathematical
- [[distortion]] — appb-mathematical
- [[probability-density-function]] — appd-probability
- [[histogram-normalisation]] — appd-probability
- [[expected-value]] — appd-probability
- [[conditional-probability]] — appf-rules
- [[product-rule]] — appf-rules
- [[bayes-rule]] — appf-rules
- [[gaussian-distribution]] — appf-rules
- [[central-limit-theorem]] — appf-rules
