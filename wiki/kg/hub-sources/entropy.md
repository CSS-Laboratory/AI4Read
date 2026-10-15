---
id: entropy
type: concept
fields: [information-theory, bayesian, complex-systems, communication-theory, control-theory]
fields_strong: [information-theory, bayesian, complex-systems, communication-theory, control-theory]
n_sources: 55
n_works: 16
tiers: [core, reference, deep]
grounding: digests
sources: [ashby-1956-cybernetics/ch09-incessant, carey-1989-cultural/ch01-cultural, cover-2006-elements/ch01-introduction, cover-2006-elements/ch02-entropy, cover-2006-elements/ch03-asymptotic, cover-2006-elements/ch05-data-p1, cover-2006-elements/ch05-data-p2, cover-2006-elements/ch07-kolmogorov, cover-2006-elements/ch16-inequalities, gibson-2019-efficiency/main, jaynes-1957-information/main, jaynes-2003-probability/ch09-repetitive-p1, jaynes-2003-probability/ch11-discrete, jaynes-2003-probability/ch13-decision, jaynes-2003-probability/ch14-simple, jaynes-2003-probability/ch22-introduction, mackay-2003-information/ch01-introduction, mackay-2003-information/ch02-probability, mackay-2003-information/ch04-source, mackay-2003-information/ch05-symbol, mackay-2003-information/ch14-very, mackay-2003-information/ch15-further, mackay-2003-information/ch17-communication, mackay-2003-information/ch18-crosswords, mackay-2003-information/ch30-efficient, mackay-2003-information/ch31-ising, mcelreath-2020-rethinking/ch06-overfitting-p1, mcelreath-2020-rethinking/ch09-big, mitchell-2009-guidedtour/ch03-information, mitchell-2009-guidedtour/ch07-defining, murphy-2023-pml2/ch05-information-p1, pierce-1980-introduction/ch02-origins, pierce-1980-introduction/ch05-entropy, pierce-1980-introduction/ch07-efficient, pierce-1980-introduction/ch10-information, pierce-1980-introduction/ch12-information, pierce-1980-introduction/ch13-information, polyanskiy-2025-information/ch01-introduction, polyanskiy-2025-information/ch02-entropy, polyanskiy-2025-information/ch09-entropy, polyanskiy-2025-information/ch10-random, polyanskiy-2025-information/ch12-variable, rosvall-2008-maps/main-p1, rosvall-2008-maps/main-p2, shannon-1948-mathematical/main-p1, shannon-1951-prediction/main, stone-2022-information/appa-glossary, stone-2022-information/appb-mathematical, stone-2022-information/appd-probability, stone-2022-information/appf-rules, stone-2022-information/ch02-entropy, stone-2022-information/ch03-source, stone-2022-information/ch05-entropy, stone-2022-information/ch10-thermodynamic, stone-2022-information/ch11-information]
aliases: [entropy-communication-sense, entropy-h, entropy-h-x, entropy-hx, information-entropy, shannon-entropy]
canon_spine: [communication-theory, information-theory]
generated_by: build_kg.py
---

# entropy

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `entropy-communication-sense` — 1 digest(s)
- `entropy-h` — 2 digest(s)
- `entropy-h-x` — 5 digest(s)
- `entropy-hx` — 15 digest(s)
- `information-entropy` — 2 digest(s)
- `shannon-entropy` — 1 digest(s)

## Canon spine entry

- **Entropy** (communication-theory): average uncertainty of a source, H = −Σ p log p; the limit for lossless compression (grad)

## Canon spine entry

- **entropy H(X)** (information-theory): average surprisal; the irreducible uncertainty of a source in bits per symbol (HS)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 5): $-\sum p(x)\log_2 p(x)$; average bits needed to describe $X$ [as `entropy H(X)`; alias `entropy-hx`]
- [[cover-2006-elements/ch02-entropy]] (pp. 13–14, 27): $H(X)=-\sum p\log p=E\log\frac1{p(X)}$; depends only on probabilities; $0\le H\le\log|\mathcal X|$ [as `entropy-HX`; alias `entropy-hx`]
- [[cover-2006-elements/ch03-asymptotic]] (p. 51): H(X) = −E log p(X), the limit of sample entropy [alias `entropy-hx`]
- [[cover-2006-elements/ch05-data-p1]] (p. 86): the lower bound $H_D(X)$ on expected length of instantaneous codes
- [[cover-2006-elements/ch05-data-p2]] (pp. 103, 112): lower bound for compression and for coin-flip generation
- [[cover-2006-elements/ch07-kolmogorov]] (p. 154): $H(X)$; here $\frac1n EK(X^n|n)$ tends to it for i.i.d. sources
- [[cover-2006-elements/ch16-inequalities]] (p. 483): $-\sum p\log p$, bounded by $\log|\mathcal X|$ [as `entropy-H(X)`; alias `entropy-hx`]
- [[gibson-2019-efficiency/main]] (p. 4): average surprisal of a random variable, as uncertainty about its value [as `entropy-H-X`; alias `entropy-h-x`]
- [[jaynes-1957-information/main]] (p. 622): $-K\sum p_i\ln p_i$, read as the amount of uncertainty in a distribution [alias `entropy-hx`]
- [[mackay-2003-information/ch01-introduction]] (p. 2): here appears as the binary entropy function H₂(x), used in the counting approximation and in capacity [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch02-probability]] (p. 32): $H(X)=\sum P(x)\log\frac1{P(x)}$, the average information content, also called uncertainty [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch04-source]] (p. 67, p. 70): Σ p_i log₂(1/p_i), the average Shannon information content; maximal for the uniform distribution [as `entropy H(X)`; alias `entropy-hx`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch05-symbol]] (p. 97): lower bound on expected length of any uniquely decodeable code [alias `entropy-h-x`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch14-very]] (p. 230): here $H(X)=H_2(f)$ is the noise entropy per bit [alias `entropy-hx`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch15-further]] (pp. 233, 234, 237): average surprisal; used for bit-position entropies and the joint/conditional entropies of Ex. 15.2, 15.7, 15.17 [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch17-communication]] (p. 250): used as information per source symbol, $H_2(f)$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch18-crosswords]] (pp. 261, 264): average information content (18.14); for Wenglish, $H_W=\log_2W/(L+1)$ per character, spaces included [as `entropy H(X)`; alias `entropy-hx`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch30-efficient]] (p. 394): $H_2(f)$ caps information per Metropolis step [alias `entropy-hx`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch31-ising]] (p. 402): here called $S=\sum p\ln(1/p)$ and tied to $\ln Z$ and free energy (Ex. 31.1) [alias `entropy-h-x`; work fields: information-theory, bayesian, complex-systems]
- [[pierce-1980-introduction/ch02-origins]] (p. 23): measure of uncertainty about which message a source will produce; more uncertainty means more information conveyed [alias `entropy-communication-sense`; new]
- [[pierce-1980-introduction/ch05-entropy]] (pp. 79–85, 105): $H=-\sum p_i\log_2 p_i$; the source's choice, the recipient's uncertainty, and the average digits per symbol needed
- [[pierce-1980-introduction/ch07-efficient]] (p. 127): minimum average binary digits per symbol (or per second) needed to send a source's messages [as `entropy-H`; alias `entropy-h`]
- [[pierce-1980-introduction/ch10-information]] (p. 202): communication-theory entropy: uncertainty about which message; average number of binary digits needed
- [[pierce-1980-introduction/ch12-information]] (p. 236): average information per symbol, applied to words as sources (11.8 bits per word for scrambled prose)
- [[pierce-1980-introduction/ch13-information]] (p. 252): here "variety/information rate" of a work, which must stay within human limits to be distinctive [as `entropy-H-X`; alias `entropy-h-x`]
- [[polyanskiy-2025-information/ch01-introduction]] (p. xviii): average, over outcomes, of the KL dissimilarity between prior and the posterior that puts all mass on the observed outcome [as `entropy-H-X`; alias `entropy-h-x`]
- [[polyanskiy-2025-information/ch02-entropy]] (p. 8): $\mathbb E[\log 1/P_X(X)]$, units set by the log base
- [[polyanskiy-2025-information/ch09-entropy]] (p. 158): joint entropy of $X$ equals $\log|C|$ for uniform $X$ on $C$
- [[polyanskiy-2025-information/ch10-random]] (p. 167): here the binary entropy $h(p)$ is the upper limit of any extractor's rate
- [[polyanskiy-2025-information/ch12-variable]] (p. 199): average of $\log_2 1/P_X(X)$; the benchmark for mean code length [as `entropy H(X)`; alias `entropy-hx`]
- [[rosvall-2008-maps/main-p1]] (pdf 2): average surprisal; here it bounds codeword length per step of a walk [work fields: information-theory, complex-systems]
- [[rosvall-2008-maps/main-p2]]: behind the bar charts only by inference; not defined on these pages. [weak: not really used in this unit; work fields: information-theory, complex-systems]
- [[shannon-1948-mathematical/main-p1]] (p. 11): $H=-\sum p_i\log p_i$ (Shannon: choice/uncertainty); $K$ only sets the unit
- [[shannon-1951-prediction/main]] (p. 50): Shannon's $H$: average binary digits per letter in the most efficient binary translation
- [[stone-2022-information/appa-glossary]] (pp. 243, 246): average of $h(x)$; the glossary defines it only as overall variability, and uses "uncertainty" for surprisal or entropy
- [[stone-2022-information/appb-mathematical]] (p. 248): $H(X)$, the average Shannon information of $p(X)$
- [[stone-2022-information/appd-probability]] (p. 258): expected Shannon information, $\sum p\log(1/p)$ [as `entropy H(X)`; alias `entropy-hx`]
- [[stone-2022-information/appf-rules]] (p. 265): $\sum p\log(1/p)$, or its integral form [as `entropy H(X)`; alias `entropy-hx`]
- [[stone-2022-information/ch02-entropy]] (p. 33, p. 38): average Shannon information $H(X)=\sum p(x_i)\log(1/p(x_i))=E[\log(1/p(x))]$; strictly a property of the distribution
- [[stone-2022-information/ch03-source]] (pp. 52, 57–58): average information per symbol, $\sum p\log(1/p)$; used as the lower limit for average codeword length [as `entropy-H(X)`; alias `entropy-hx`]
- [[stone-2022-information/ch05-entropy]] (p. 114, p. 116): here, average surprisal of histogram bins; infinite for a continuous variable as bin width → 0
- [[stone-2022-information/ch10-thermodynamic]] (pp. 207–208): Shannon entropy; equals $\log W$ for $W$ equally probable outcomes [as `entropy-H`; alias `entropy-h`]
- [[stone-2022-information/ch11-information]] (p. 228–229): average Shannon information; applied to spike trains as the log of the number of possible trains

### bayesian

- [[jaynes-2003-probability/ch09-repetitive-p1]] (p. 286): here the entropy of the frequency distribution, $-\sum f_j\log f_j$, as the growth rate of multiplicity [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch11-discrete]] (p. 350): $H=-\sum p_i\log p_i$, here called information entropy, derived from the Shannon conditions [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch13-decision]] (p. 403): the pay-off ceiling B[log n − H] [alias `entropy-hx`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch14-simple]] (pp. 429–430): used as expected entropy $\overline H_D(Y)$; extra conditioning never raises it on average [as `entropy H(X)`; alias `entropy-hx`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch22-introduction]] (pp. 634–635): $-\sum p\log p$; here the engineer's ignorance about messages, not the sender's information [work fields: bayesian, information-theory]
- [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 178): $H(p)=-\sum p_i\log p_i$; uncertainty in a distribution [alias `information-entropy`; new]
- [[mcelreath-2020-rethinking/ch09-big]] (pp. 268, 270): $H(p)=-\sum p_i\log p_i$; here treated as approximately log number of ways per observation [alias `information-entropy`; new]
- [[murphy-2023-pml2/ch05-information-p1]] (p. 235): $-\sum p\log p$; $\log K$ minus KL to the uniform [new; work fields: bayesian, information-theory]

### complex-systems

- [[mitchell-2009-guidedtour/ch03-information]] (pdf 65, 75): in physics, energy unavailable for more work; in Boltzmann's sense, a function of the number of microstates behind a macrostate [new]
- [[mitchell-2009-guidedtour/ch07-defining]] (pdf 128): average information or surprise of a message source; maximal for random sequences [alias `shannon-entropy`; new]

### communication-theory

- [[carey-1989-cultural/ch01-cultural]] (p. 20): Carey's own gloss: the world is not strictly ordered, so the mind imposes order (p. 20) (differs from canon: Carey means only that the world is loosely ordered, not Shannon entropy)

### control-theory

- [[ashby-1956-cybernetics/ch09-incessant]] (pp. 174–175): Shannon's $H=-\sum p\log p$; Ashby uses the word only in this sense [new; work fields: control-theory, information-theory]

## Instances that use it

- [[insect-in-pool]] — three-state Markov chain (B, W, P); equilibrium (44.9, 42.9, 12.2); entropy 0.842 bits per step — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[traffic-lights-entropy-and-redundancy]] — entropy 1.63 bits (pp. 174–175); redundancy in two different sets of vectors — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[shannon-abcd-compression-code]] — 8 letters sent as 7, matching entropy $1\tfrac34$ bits — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[merging-a-and-d-to-x]] — merging states without loss of entropy — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[tetris-cross-entropy]] — cross-entropy method used with impressive success — from [[bertsekas-2026-rlcourse/ch03-learning-p4]]
- [[binary-entropy-function]] — $H(p)$, concave, 0 at $p\in\{0,1\}$, 1 bit at $p=1/2$ — from [[cover-2006-elements/ch02-entropy]]
- [[conditioning-can-raise-entropy-example]] — $H(X|Y=2)=1>H(X)=0.544$ but $H(X|Y)=0.25$ — from [[cover-2006-elements/ch02-entropy]]
- [[non-converging-entropy-average]] — independent source with $p_i$ from (4.13); no entropy rate — from [[cover-2006-elements/ch04-entropy]]
- [[sfe-dyadic-example]] — dyadic SFE code: 2.75 bits vs entropy 1.75 — from [[cover-2006-elements/ch05-data-p2]]
- [[entropy-of-english]] — 4.76, 4.03, 2.8 (models), 1.3 (guessing), 1.34 (gambling) bits/letter — from [[cover-2006-elements/ch06-gambling]]
- [[normal-distribution]] — $h=\tfrac12\log2\pi e\sigma^2$; entropy maximizer — from [[cover-2006-elements/ch09-differential]]
- [[maxwell-boltzmann-gas]] — the velocity law as max entropy under a temperature constraint — from [[cover-2006-elements/ch11-maximum]]
- [[hadamard-inequality]] — $|K|\le\prod K_{ii}$ via independence bound on entropy — from [[cover-2006-elements/ch16-inequalities]]
- [[toeplitz-determinant-monotonicity]] — stationary-process entropy rate analogue for $|K_k|^{1/k}$ — from [[cover-2006-elements/ch16-inequalities]]
- [[cesaro-limit-entropy-rate]] — $\lim h(X^n)/n=\lim h(X_n|X^{n-1})$ used for determinants — from [[cover-2006-elements/ch16-inequalities]]
- [[negative-entropy-convexity]] — Example 7.3: $x\log_2x$ checked against (7.30) and (7.31) — from [[deisenroth-2020-mml/ch07-continuous]]
- [[boltzmann-distribution]] — max-entropy estimate when only $\langle E\rangle$ is known — from [[jaynes-1957-information/main]]
- [[grand-canonical-ensemble]] — max-entropy estimate with $\langle E\rangle$, $\langle n_i\rangle$ given — from [[jaynes-1957-information/main]]
- [[pressure-ensemble]] — max-entropy with $\langle E\rangle,\langle V\rangle$ given — from [[jaynes-1957-information/main]]
- [[gibbs-quantum-clue]] — a failed maximum-entropy prediction pointed to discrete energy levels — from [[jaynes-2003-probability/ch11-discrete]]
- [[widget-problem]] — four-stage factory decision; maximum-entropy priors, no new data — from [[jaynes-2003-probability/ch14-simple]]
- [[final-cause-and-entropy]] — macroscopic purpose, entropy as the number of ways of realising it — from [[jaynes-2003-probability/ch20-model]]
- [[english-letter-ensemble]] — 27-symbol alphabet; monogram and bigram distributions; entropy about 4.11 bits — from [[mackay-2003-information/ch02-probability]]
- [[zipf-word-entropy]] — 9.7 bits per word under the $1/n$ law — from [[mackay-2003-information/ch02-probability]]
- [[triangular-antiferromagnet]] — frustrated lattice; no fluctuation peak ($N=4096$), entropy appears to be about 0.3 at $T\to0$ — from [[mackay-2003-information/ch31-ising]]
- [[pebbles-in-buckets]] — counting arrangements links entropy to number of ways — from [[mcelreath-2020-rethinking/ch09-big]]
- [[generalized-normal-family]] — equal-variance densities with Gaussian entropy maximum at shape 2 — from [[mcelreath-2020-rethinking/ch09-big]]
- [[marbles-expected-value-simulation]] — 100000 random distributions with mean 1.4 never beat the binomial's entropy — from [[mcelreath-2020-rethinking/ch09-big]]
- [[maxwells-demon]] — apparent entropy decrease; led to information-entropy link — from [[mitchell-2009-guidedtour/ch03-information]]
- [[uniform-negative-entropy]] — $U(0,1/8)$ has $h=-3$ bits — from [[murphy-2023-pml2/ch05-information-p1]]
- [[height-entropy-units]] — one height distribution, entropy 0.43, 5.4 or $-1.3$ bits by unit — from [[murphy-2023-pml2/ch05-information-p1]]
- [[kl-as-bregman-mixture-family]] — forward KL from negative entropy — from [[nielsen-2020-elementary/main-p2]]
- [[winogender]] — 120 binary pairs; bias via entropy — from [[ouyang-2022-instructgpt/main-p3]]
- [[crows-pairs]] — 1508 pairs; bias via entropy — from [[ouyang-2022-instructgpt/main-p3]]
- [[gas-expansion-partition]] — entropy increases though energy is constant — from [[pierce-1980-introduction/ch02-origins]]
- [[biased-coin-entropy]] — heads $\tfrac34$ gives .811 bit; Fig. V-1 curve — from [[pierce-1980-introduction/ch05-entropy]]
- [[english-word-entropy-shannon]] — 11.8 bits per word from the 8,727-word Zipf model — from [[pierce-1980-introduction/ch05-entropy]]
- [[shannon-guessing-experiment]] — English entropy between .6 and 1.3 bits per letter — from [[pierce-1980-introduction/ch05-entropy]]
- [[repeat-three-source]] — random digit repeated three times; entropy ⅓ bit per character, so mechanical block coding is unnecessary — from [[pierce-1980-introduction/ch07-efficient]]
- [[shannon-guessing-experiment]] — a human predicts the next letter; entropy of English 0.6–1.3 bits per letter — from [[pierce-1980-introduction/ch07-efficient]]
- [[hilbert-13th-problem]] — resolved using metric entropy — from [[polyanskiy-2025-information/ch01-introduction]]
- [[bernoulli-entropy]] — $h(p)$ is maximal at $\frac12$, zero at 0 and 1 — from [[polyanskiy-2025-information/ch02-entropy]]
- [[noisy-channel-conditional-entropy]] — $H(X|Y)=h(\delta)$ for XOR noise — from [[polyanskiy-2025-information/ch02-entropy]]
- [[ant-scout-experiment]] — communication time proportional to entropy of the food location — from [[polyanskiy-2025-information/ch02-entropy]]
- [[ideal-gas-entropy]] — $S=kn\sum p_j\log(1/p_j)$ — from [[polyanskiy-2025-information/ch02-entropy]]
- [[or-gate-conditioning]] — conditioning raises entropy for Y=0 but lowers it on average — from [[polyanskiy-2025-information/ch04-mutual]]
- [[identity-channel-infinite-entropy]] — shows finiteness of $C$ is needed in Cor. 5.5 — from [[polyanskiy-2025-information/ch06-extremization]]
- [[gilbert-elliott-hmm]] — binary-state HMM with BSC emissions; entropy rate via a Blackwell measure that can be fractal-like — from [[polyanskiy-2025-information/ch07-tensorization]]
- [[irrational-rotation]] — ergodic with zero KS entropy — from [[polyanskiy-2025-information/ch14-entropy]]
- [[hilbert-13th-problem]] — impossibility of superposition by entropy comparison — from [[polyanskiy-2025-information/ch30-metric]]
- … 16 more instance lines mention this id

## Candidate bridges

- [structural-analogy] Capacity must at least match source entropy rate (p. 183) ↔ control-theory: law of requisite variety (canon link; not stated in this unit). — from [[ashby-1956-cybernetics/ch09-incessant]] (control-theory → control-theory)
- [same-math] Ashby's entropy form ($H(E)\ge H(D)-H(R)$ when $H_D(R)=0$) ↔ information theory: limit on noise removable by a correction channel (Shannon's Theorem 10, as stated on p. 211). — from [[ashby-1956-cybernetics/ch11-requisite]] (control-theory → information-theory)
- [same-math] Eq. 1 with softmax and log-likelihood training ↔ LLM: next-token prediction trained by cross-entropy (the same objective with a different $g$) — from [[bengio-2003-nplm/main]] (llm → llm)
- [structural-analogy] cross-entropy method ↔ evolutionary search: a population is resampled around the best members. — from [[bertsekas-2026-rlcourse/ch03-learning-p4]] (control-theory → other:computer-science)
- [same-math] relative entropy $D(p\|q)$ ↔ statistics: error exponent in hypothesis testing between $p$ and $q$ (pp. 8–9) — from [[cover-2006-elements/ch01-introduction]] (information-theory → other:statistics)
- [structural-analogy] doubling rate $W$ ↔ entropy rate: the authors call $W$ a "dual" of the entropy rate (p. 4) — from [[cover-2006-elements/ch01-introduction]] (information-theory → information-theory)
- [same-math] $\log$ (number of equally likely microstates) = $H$ ↔ statistical thermodynamics: Boltzmann's entropy equals Shannon's $H$ when all states are equally likely (p. 33). — from [[cover-2006-elements/ch02-entropy]] (information-theory → other:statistics)
- [same-math] $-\sum\mu_iP_{ij}\log P_{ij}$ ↔ conditional entropy $H(X_2|X_1)$ under the stationary law — literally the same quantity. — from [[cover-2006-elements/ch04-entropy]] (information-theory → unspecified)
- [structural-analogy] Hidden Markov entropy bounds ↔ estimation with a latent state: observing the hidden state sandwiches the true rate. — from [[cover-2006-elements/ch04-entropy]] (information-theory → other:estimation-with-a-latent)
- [structural-analogy] Theorem 5.4.3 penalty $D(p\|q)$ ↔ machine learning: log-loss of a model $q$ on data from $p$ (cross-entropy minus entropy; the ceiling aside). — from [[cover-2006-elements/ch05-data-p1]] (information-theory → llm)
- [structural-analogy] Excess code length / lost growth $D(p\|b)$ (6.48) ↔ cross-entropy training loss of language models: a worse model estimate costs more bits. — from [[cover-2006-elements/ch06-gambling]] (information-theory → information-theory)
- [structural-analogy] Equality conditions (distinct codewords, i.i.d. outputs with $p^*(y)$) ↔ maximum entropy principle: capacity achieved when outputs are as spread as the constraints allow. — from [[cover-2006-elements/ch08-channel-p2]] (information-theory → information-theory)
- [same-math] Fano's inequality here ↔ Fano's inequality in estimation: the same bound $H(W|Y^n)\le1+P_e\log|\mathcal W|$ ties residual entropy to error. — from [[cover-2006-elements/ch08-channel-p2]] (information-theory → other:fanos-inequality-in-estimation)
- [same-math] Optimal Gaussian input via maximum entropy ↔ information-theory: maximum entropy principle — a normal maximizes entropy for fixed variance. — from [[cover-2006-elements/ch10-gaussian]] (information-theory → information-theory)
- [same-math] Max-entropy form $e^{\lambda_0+\sum\lambda_ir_i}$ ↔ statistics: exponential family with sufficient statistics $r_i$ — same functional form. — from [[cover-2006-elements/ch11-maximum]] (information-theory → other:statistics)
- [same-math] Entropy rate ↔ prediction: (11.40) links entropy rate to minimum mean squared prediction error for Gaussian processes. — from [[cover-2006-elements/ch11-maximum]] (information-theory → other:prediction)
- [same-math] Sanov's $P^*\propto Q\,e^{\sum\lambda_ig_i}$ ↔ maximum entropy / exponential families: the same tilted form as MaxEnt solutions under expectation constraints. — from [[cover-2006-elements/ch12-information-p1]] (information-theory → information-theory)
- [structural-analogy] Rare-event exponent $D(P^*\|Q)$ ↔ cross-entropy / likelihood-ratio testing: the cost of a wrong model is measured in $D$. — from [[cover-2006-elements/ch12-information-p1]] (information-theory → information-theory)
- [structural-analogy] Decision boundary D(P‖P₂)−D(P‖P₁)=const ↔ classification: a nearest-prototype rule with relative entropy as distance. — from [[cover-2006-elements/ch12-information-p2]] (information-theory → llm)
- [same-math] Fisher information $J(\theta)$ ↔ relative entropy: Problem 7 asks the reader to show $\lim_{\theta'\to\theta}\frac{D(p_\theta\|p_{\theta'})}{(\theta-\theta')^2}=\frac1{\ln4}J(\theta)$. Fisher information is the local, second-order form of KL. — from [[cover-2006-elements/ch12-information-p3]] (information-theory → information-theory)
- [structural-analogy] Slepian–Wolf binning error sum (14.192) ↔ MAC error sum (14.190) — same three-term structure with rates and entropies exchanged. — from [[cover-2006-elements/ch14-network-p3]] (information-theory → unspecified)
- [structural-analogy] Doubling-rate loss $\le D(f\|g)$ ↔ cross-entropy/KL in model fitting: Thm 15.4.1 bounds the growth-rate cost of acting on model $g$ by a KL divergence (p. 467). — from [[cover-2006-elements/ch15-information]] (information-theory → information-theory)
- [structural-analogy] Cesàro-mean proof of $W^*_\infty$ ↔ entropy rate of stationary processes: parallel limit structure, since the chain rule for $W$ is formally that of $H$ (p. 470). — from [[cover-2006-elements/ch15-information]] (information-theory → information-theory)
- [same-math] Entropy power inequality ↔ Matrix theory: Minkowski determinant inequality (via Gaussians, p. 505). — from [[cover-2006-elements/ch16-inequalities]] (information-theory → linear-algebra)
- [structural-analogy] Entropy power of a density ↔ Geometry: $n$th-root of volume of support (p. 501). — from [[cover-2006-elements/ch16-inequalities]] (information-theory → other:mathematics)
- [same-math] Surprisal, entropy, conditional entropy, mutual information in Box 2 ↔ information theory: the standard definitions (I)–(V). — from [[gibson-2019-efficiency/main]] (information-theory → information-theory)
- [same-math] Max-entropy solution under expectation constraints ↔ information-theory: exponential family / Gibbs distribution — the same form $p\propto\exp(\sum\lambda_if_i)$. — from [[jaynes-1957-information/main]] (information-theory → information-theory)
- [metaphor] "infinitely educated brain" as the limit of a dense lattice ↔ information-theory: a code approaching the entropy bound only in the limit — an ideal reached only asymptotically. — from [[jaynes-2003-probability/appa-other]] (bayesian → information-theory)
- [structural-analogy] Gaussian has only two cumulants ↔ information-theory: maximum-entropy / exponential-family distributions with mean and variance constraints. — from [[jaynes-2003-probability/appc-convolutions]] (bayesian → information-theory)
- [structural-analogy] Desideratum (IIIc), equivalent knowledge gives equal plausibilities ↔ bayesian: principle of indifference/maximum entropy — from [[jaynes-2003-probability/ch01-plausible]] (bayesian → bayesian)
- [structural-analogy] Principle of indifference (uniform $1/n$) ↔ maximum entropy: the uniform distribution is the most uncommitted one when only normalization is known (canon link; not stated in this unit). — from [[jaynes-2003-probability/ch02-quantitative]] (bayesian → information-theory)
- [same-math] $H(f,p)$, entropy of $(f,1-f)$ relative to $(p,1-p)$ ↔ information-theory: negative KL divergence $-D(f\|p)$; likelihood ratio $=e^{-nD}$. — from [[jaynes-2003-probability/ch05-queer]] (bayesian → information-theory)
- [structural-analogy] Gaussian as maximum entropy under fixed mean and variance ↔ information-theory: the maximum-entropy principle and exponential families (pp. 216–217) — from [[jaynes-2003-probability/ch07-central-p1]] (bayesian → information-theory)
- [structural-analogy] Gaussian as maximum-entropy attractor under variance-conserving operations ↔ information theory: maximum entropy principle and the typical set — repeated information-losing steps approach a maximum-entropy law. — from [[jaynes-2003-probability/ch07-central-p2]] (bayesian → information-theory)
- [same-math] Sufficiency factorization (8.9) ↔ information-theory: zero information loss (in entropy) from $D$ to $r$ iff $r$ sufficient — the text states this only in footnote 2, with the proof deferred to Chapter 11. — from [[jaynes-2003-probability/ch08-sufficiency]] (bayesian → information-theory)
- [structural-analogy] Fundamental domain of a symmetry group fixing the prior ↔ bayesian: Principle of indifference / maximum entropy — symmetry as the formal basis for uninformative priors. — from [[jaynes-2003-probability/ch10-physics]] (bayesian → bayesian)
- [same-math] Lemma (11.55), $H\le\sum p_i\log(1/u_i)$ with equality iff $p=u$ ↔ information-theory: non-negativity of relative entropy / cross-entropy $\ge$ entropy — the same inequality — from [[jaynes-2003-probability/ch11-discrete]] (bayesian → information-theory)
- [same-math] weatherman log-pay expectation ↔ information-theory: cross-entropy / log scoring rule — expected pay B[log n + Σp_i log q_i] is maximised at q = p, a Gibbs-type inequality. — from [[jaynes-2003-probability/ch13-decision]] (bayesian → information-theory)
- [same-math] expected log fortune with tips ↔ information-theory: Kelly criterion — the growth-rate limit H₀ − H is the log-wealth/entropy link in the canon list. — from [[jaynes-2003-probability/ch13-decision]] (bayesian → information-theory)
- [same-math] Stage-2 maximum-entropy priors (14.56)–(14.59) ↔ information-theory: exponential-family/Gibbs distribution from mean constraints — same partition-function mathematics. — from [[jaynes-2003-probability/ch14-simple]] (bayesian → information-theory)
- [structural-analogy] "Jeffreys prior is uninformative for a scale parameter" ↔ information-theory: the group-invariance / maximum-entropy prior constructions Jaynes mentions (pp. 484–485). — from [[jaynes-2003-probability/ch15-paradoxes]] (bayesian → information-theory)
- [structural-analogy] Underdetermined solution $x^*=\tilde A(A\tilde A)^{-1}y$ chosen by minimum length or maximum entropy ↔ information-theory: choosing among data-consistent models by an entropy criterion (p. 594–595) — from [[jaynes-2003-probability/ch19-physical]] (bayesian → information-theory)
- [structural-analogy] Gaussian as the maximum-entropy law under moment constraints ↔ information-theory: exponential family / Gibbs distribution (p. 592) — from [[jaynes-2003-probability/ch19-physical]] (bayesian → information-theory)
- [same-math] Digram maximum entropy via $Q^{N}$ and $q_{\max}$ ↔ statistical mechanics: transfer-matrix-style calculation with periodic boundary conditions — the author notes that physicists use the term 'periodic boundary conditions' for this device (p. 642). — from [[jaynes-2003-probability/ch22-introduction]] (bayesian → complex-systems)
- [structural-analogy] Maximum capacity for given time ↔ minimum time for given $W$ ↔ maximum entropy for given energy / minimum energy for given entropy — dual forms of one variational problem (p. 632). — from [[jaynes-2003-probability/ch22-introduction]] (bayesian → unspecified)
- [same-math] $H_2\le H_1$ via $\log x\le x-1$ ↔ information-theory: conditioning does not increase entropy (canon link; not stated in this unit). — from [[jaynes-2003-probability/ch22-introduction]] (bayesian → information-theory)
- [structural-analogy] Maximum-entropy assignment ↔ statistical mechanics: the Preface says all presently known statistical mechanics is included in the maximum-entropy approach (pdf 25). — from [[jaynes-2003-probability/front-preface]] (bayesian → complex-systems)
- [same-math] log C(N,r) ≃ N·H₂(r/N) ↔ information-theory: entropy as the exponential growth rate of the count of typical sequences. — from [[mackay-2003-information/ch01-introduction]] (information-theory → information-theory)
- [same-math] $D_{\rm KL}(P\|Q)\ge0$ (Gibbs) ↔ information-theory: cross-entropy $=H+D_{\rm KL}$ is minimized by the true distribution — same quantity, as the concept list defines it (the unit does not state this). — from [[mackay-2003-information/ch02-probability]] (information-theory → information-theory)
- [structural-analogy] Entropy decomposition (2.43) ↔ information-theory: chain rule $H(X,Y)=H(X)+H(Y\mid X)$ — information revealed in stages. — from [[mackay-2003-information/ch02-probability]] (information-theory → information-theory)
- … 93 more bridge lines mention this id (see wiki/kg/bridges.jsonl)
