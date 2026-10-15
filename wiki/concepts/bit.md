---
id: bit
type: concept
fields: [information-theory, bayesian, complex-systems, control-theory]
fields_strong: [information-theory, bayesian, complex-systems, control-theory]
n_sources: 29
n_works: 11
tiers: [core, reference]
grounding: digests
sources: [ashby-1956-cybernetics/ch07-quantity, cover-2006-elements/ch01-introduction, cover-2006-elements/ch02-entropy, gibson-2019-efficiency/main, jaynes-2003-probability/ch22-introduction, mackay-2003-information/ch02-probability, mackay-2003-information/ch04-source, mackay-2003-information/ch18-crosswords, mackay-2003-information/ch19-have, mcgrayne-2011-theory/ch04-bayes, mitchell-2009-guidedtour/ch03-information, pierce-1980-introduction/ch01-world, pierce-1980-introduction/ch02-origins, pierce-1980-introduction/ch04-encoding, pierce-1980-introduction/ch05-entropy, pierce-1980-introduction/ch10-information, pierce-1980-introduction/ch12-information, pierce-1980-introduction/ch13-information, polyanskiy-2025-information/ch01-introduction, polyanskiy-2025-information/ch02-entropy, shannon-1948-mathematical/main-p1, stone-2022-information/appa-glossary, stone-2022-information/ch01-information, stone-2022-information/ch02-entropy, stone-2022-information/ch03-source, stone-2022-information/ch04-noisy, stone-2022-information/ch05-entropy, stone-2022-information/ch10-thermodynamic, stone-2022-information/ch11-information]
aliases: [information-theory-bit]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# bit

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `information-theory-bit` — 1 digest(s)

## Canon spine entry

- **bit** (information-theory): the unit of information: the uncertainty resolved by one fair yes/no question (HS)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 5): unit of entropy when logs are base 2
- [[cover-2006-elements/ch02-entropy]] (p. 13): unit of entropy when $\log$ is base 2; a fair coin has 1 bit; base $e$ gives nats
- [[gibson-2019-efficiency/main]] (p. 4): information unit when the log base is 2
- [[mackay-2003-information/ch02-probability]] (p. 32): the unit of $h$ and $H$; also a variable valued 0 or 1 [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch04-source]] (p. 73): here also "a binary symbol with two values", distinguished from the unit of information content [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch18-crosswords]] (p. 265): one unit of information content, alongside nat, ban and deciban; backup name shannon [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch19-have]] (pp. 269, 276): here the unit for the information gained by a species, and a genome bit's good/bad state [work fields: information-theory, bayesian]
- [[pierce-1980-introduction/ch01-world]] (p. 8): universal measure of information as choice; choosing between two equally probable alternatives is one bit
- [[pierce-1980-introduction/ch02-origins]] (pp. 37–38): here an independent "0-or-1 choice"; $\log_2$ of the number of symbols counts them
- [[pierce-1980-introduction/ch04-encoding]] (p. 73): named on p. 66 as the unit of the measure of information (called entropy); this chapter does not define either term. It does describe the binary digit (p. 70) as an elementary choice between two possibilities
- [[pierce-1980-introduction/ch05-entropy]] (pp. 98–100): here a measure of information: one binary choice between equally probable options; not the same as a binary digit
- [[pierce-1980-introduction/ch10-information]] (p. 202): here also the unit of the entropy of a message source
- [[pierce-1980-introduction/ch12-information]] (p. 230): measure of choice among equally likely alternatives, $\log_2 n$ (e.g. 8 lights = 3 bits)
- [[pierce-1980-introduction/ch13-information]] (p. 250): unit used to measure a composer's or speaker's choice, e.g. 300,000 bits/s of sample freedom
- [[polyanskiy-2025-information/ch01-introduction]] (p. xvii): unit of Shannon information, from Tukey's word
- [[polyanskiy-2025-information/ch02-entropy]] (p. 8): entropy unit with $\log_2$; nats use $\log_e$, bytes $\log_{256}$
- [[shannon-1948-mathematical/main-p1]] (p. 1): unit from base-2 logarithm; $N$ two-state devices store $N$ bits
- [[stone-2022-information/appa-glossary]] (p. 242): information to pick one of two equally probable alternatives; not the same as a binary digit
- [[stone-2022-information/ch01-information]] (pp. 3, 5, 11): the amount of information needed to choose between two equally probable alternatives
- [[stone-2022-information/ch02-entropy]] (p. 44): unit of information from base-2 logarithms; a binary variable conveys up to one bit (p. 43). The author prefers "Shannon" (Sh) because "bit" is often misused for binary digit
- [[stone-2022-information/ch03-source]] (p. 46): unit of information; one binary digit carries at most one bit
- [[stone-2022-information/ch04-noisy]] (p. 84, p. 88): unit of information; the author uses "bits per pair" and "bits per outcome" for emphasis
- [[stone-2022-information/ch05-entropy]] (p. 132): extended to fractions: half a bit shrinks uncertainty by a factor 0.71
- [[stone-2022-information/ch10-thermodynamic]] (p. 210): here tied to a physical change, $\Delta H=1$ bit for halving the available states
- [[stone-2022-information/ch11-information]] (p. 218, 222): here also identified with one nucleotide in MacKay's model; the author notes bit and binary digit are used loosely

### bayesian

- [[jaynes-2003-probability/ch22-introduction]] (p. 629): information in one yes–no decision; 1 bit = 0.69315 nits [work fields: bayesian, information-theory]
- [[mcgrayne-2011-theory/ch04-bayes]] (pp. 76–77): Shannon's logarithmic unit of information; in a perfect secrecy system prior equals posterior [alias `information-theory-bit`; new]

### complex-systems

- [[mitchell-2009-guidedtour/ch03-information]] (pdf 69): information from the answer to a yes/no question [new]

### control-theory

- [[ashby-1956-cybernetics/ch07-quantity]] (p. 126): unit of logarithmic variety; 1 bit = variety of two elements [new; work fields: control-theory, information-theory]

## Instances that use it

- [[insect-in-pool]] — three-state Markov chain (B, W, P); equilibrium (44.9, 42.9, 12.2); entropy 0.842 bits per step — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[traffic-lights-entropy-and-redundancy]] — entropy 1.63 bits (pp. 174–175); redundancy in two different sets of vectors — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[shannon-abcd-compression-code]] — 8 letters sent as 7, matching entropy $1\tfrac34$ bits — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[sent-received-0-1-equivocation]] — 1% errors give equivocation 0.081 bit, 0.919 bit gets through — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[card-pack-selection]] — 2 bits plus 3 bits leaves at least 0.7 bits still to select out of $\log_2 52 \approx 5.7$ — from [[ashby-1956-cybernetics/ch13-regulating]]
- [[thermostat-water-bath]] — 1000 bits of design against 36,500 bits of disturbance — from [[ashby-1956-cybernetics/ch14-amplifying]]
- [[uniform-32-outcomes]] — $H=\log 32=5$ bits, equal-length labels — from [[cover-2006-elements/ch01-introduction]]
- [[horse-race-8]] — $H=2$ bits, and a code reaching it — from [[cover-2006-elements/ch01-introduction]]
- [[noiseless-binary-channel]] — $C=1$ bit — from [[cover-2006-elements/ch01-introduction]]
- [[binary-entropy-function]] — $H(p)$, concave, 0 at $p\in\{0,1\}$, 1 bit at $p=1/2$ — from [[cover-2006-elements/ch02-entropy]]
- [[dyadic-four-symbol-source]] — probabilities $1/2,1/4,1/8,1/8$: $H=7/4$ bits, 1.75 expected questions — from [[cover-2006-elements/ch02-entropy]]
- [[kl-asymmetry-example]] — $D(p\|q)=0.2075\ne D(q\|p)=0.1887$ bits — from [[cover-2006-elements/ch02-entropy]]
- [[sum-of-fair-bits-example]] — $Z=X+Y$ gives $I(X;Y|Z)=\frac12>I(X;Y)=0$ — from [[cover-2006-elements/ch02-entropy]]
- [[typical-set-flag-bit-code]] — two-part code with flag bit 0/1 — from [[cover-2006-elements/ch03-asymptotic]]
- [[example-5-1-1-dyadic-code]] — $p=(1/2,1/4,1/8,1/8)$, $L=H=1.75$ bits — from [[cover-2006-elements/ch05-data-p1]]
- [[example-5-6-1-huffman-five-symbols]] — Huffman code, $L=2.3$ bits — from [[cover-2006-elements/ch05-data-p1]]
- [[shannon-vs-huffman-09999]] — Shannon code gives 14 bits to a symbol of probability 0.0001 — from [[cover-2006-elements/ch05-data-p1]]
- [[sfe-dyadic-example]] — dyadic SFE code: 2.75 bits vs entropy 1.75 — from [[cover-2006-elements/ch05-data-p2]]
- [[sfe-nondyadic-example]] — 5-symbol SFE code, 1.2 bits longer than Huffman — from [[cover-2006-elements/ch05-data-p2]]
- [[entropy-of-english]] — 4.76, 4.03, 2.8 (models), 1.3 (guessing), 1.34 (gambling) bits/letter — from [[cover-2006-elements/ch06-gambling]]
- [[fermat-goldbach-halting-programs]] — conjectures encoded as halting questions, decided by Ω bits — from [[cover-2006-elements/ch07-kolmogorov]]
- [[noiseless-binary-channel]] — $C=1$ bit — from [[cover-2006-elements/ch08-channel-p1]]
- [[english-over-erasure-channel]] — raw redundant text survives erasures better than compressed bits — from [[cover-2006-elements/ch08-channel-p2]]
- [[bernoulli-half-bound]] — $H=1$ vs bound 1.255 bits — from [[cover-2006-elements/ch09-differential]]
- [[telephone-line-capacity]] — 3300 Hz, 20 dB SNR gives about 22,000 bit/s; modems reach 19,200 — from [[cover-2006-elements/ch10-gaussian]]
- [[die-average-example]] — fair die, average $\ge4$: $D(P^*\|Q)=0.0624$ bits, probability $\approx2^{-624}$ for $n=10000$ — from [[cover-2006-elements/ch12-information-p1]]
- [[one-bit-gaussian-quantizer]] — points $\pm\sqrt{2/\pi}\sigma$, distortion $0.3633\sigma^2$ versus the block bound $\sigma^2/4$ — from [[cover-2006-elements/ch13-rate]]
- [[gotham-metropolis-weather]] — 150 bits instead of 200 with Slepian–Wolf — from [[cover-2006-elements/ch14-network-p2]]
- [[spanish-dutch-speaker]] — superposition beats time-sharing: 21 vs 20 bits/s — from [[cover-2006-elements/ch14-network-p3]]
- [[vision-oracle-256-reports]] — an eight-bit stand-in for the visual system, as an example of oversimplification — from [[dennett-1987-intentional-stance/ch09-fast]]
- [[paul-revere-one-bit]] — in a two-option context, one bit suffices — from [[gibson-2019-efficiency/main]]
- [[color-warm-cool-surprisal]] — warm colours cost fewer bits than cool in all languages tested — from [[gibson-2019-efficiency/main]]
- [[english-letter-ensemble]] — 27-symbol alphabet; monogram and bigram distributions; entropy about 4.11 bits — from [[mackay-2003-information/ch02-probability]]
- [[zipf-word-entropy]] — 9.7 bits per word under the $1/n$ law — from [[mackay-2003-information/ch02-probability]]
- [[sixty-three-game]] — six yes/no questions give a 6-bit binary encoding of x — from [[mackay-2003-information/ch04-source]]
- [[submarine-game]] — total information is 6 bits regardless of when the hit occurs — from [[mackay-2003-information/ch04-source]]
- [[wenglish]] — 2¹⁵ equiprobable 5-letter words; 15 bits per word, 3 bits per character — from [[mackay-2003-information/ch04-source]]
- [[strings-of-ch-extra-bit]] — nine highly predictable characters cost at least nine bits in Huffman, versus 0.13 bits of information — from [[mackay-2003-information/ch05-symbol]]
- [[random-bit-of-c3-stream]] — P(bit is 1) = 1/2; the bus-stop fallacy — from [[mackay-2003-information/ch05-symbol]]
- [[claude-shannon-integer]] — a 14-character file as a 98-bit integer — from [[mackay-2003-information/ch07-codes]]
- [[xor-three-variable-ensemble]] — $z=x+y \bmod 2$: $I(X;Y)=0$ but $I(X;Y|Z)=1$ bit — from [[mackay-2003-information/ch08-dependent]]
- [[binary-symmetric-channel]] — flips each bit with prob. f; C = 1 − H₂(f), 0.39 bits at f = 0.15 — from [[mackay-2003-information/ch09-communication]]
- [[file-comparison-hash]] — Alice and Bob compare 32-bit hashes; false-negative probability 2^{−M} — from [[mackay-2003-information/ch12-hash]]
- [[md5]] — widely used 128-bit one-way hash — from [[mackay-2003-information/ch12-hash]]
- [[binary-symmetric-channel]] — flips each bit with probability $f$; the channel analysed — from [[mackay-2003-information/ch14-very]]
- [[american-belarusian-broadcast]] — extra bits sent by choosing which language the next word comes from — from [[mackay-2003-information/ch15-further]]
- [[maynard-smith-1-bit-per-generation]] — the claimed rate of information acquisition, which the model confirms for asexuals — from [[mackay-2003-information/ch19-have]]
- [[urn-of-black-and-white-balls]] — $\log_2(1/f)$ bits to find a black ball, used to define acquired information — from [[mackay-2003-information/ch19-have]]
- [[repetition-code-r3-posterior]] — the example (26.4) as the posterior of three bits for $\mathbf r=(1,1,0)$, BSC flip probability 0.1 — from [[mackay-2003-information/ch26-exact]]
- [[error-correcting-code-as-latent-variable-model]] — source bits are latent; $\mathbf G$ normally known in advance — from [[mackay-2003-information/ch34-independent]]
- … 56 more instance lines mention this id

## Candidate bridges

- [structural-analogy] $\log_2 r$ bits per step through an $r$-state channel ↔ information theory: channel capacity — Ashby derives only an upper bound from state count, in a determinate setting — from [[ashby-1956-cybernetics/ch08-transmission]] (control-theory → information-theory)
- [same-math] quantity of selection as bits ↔ information theory: $\log_2$ of the number of equally available options — Ashby uses the same scale as information (pp. 255–256) — from [[ashby-1956-cybernetics/ch13-regulating]] (control-theory → information-theory)
- [structural-analogy] 20 questions / Huffman code ↔ decision trees: each yes/no split is one bit of a binary code. — from [[cover-2006-elements/ch05-data-p1]] (information-theory → llm)
- [structural-analogy] Generating $X$ from fair bits (tree of flips) ↔ simulation in computational social science: drawing categorical samples from a pseudo-random bit stream; $H(X)$ lower-bounds the random bits used. — from [[cover-2006-elements/ch05-data-p2]] (information-theory → other:sociology)
- [structural-analogy] Excess code length / lost growth $D(p\|b)$ (6.48) ↔ cross-entropy training loss of language models: a worse model estimate costs more bits. — from [[cover-2006-elements/ch06-gambling]] (information-theory → information-theory)
- [structural-analogy] Polynomially many types vs. exponentially many sequences ↔ MDL / universal coding: model cost is only $O(\log n)$ bits per parameter. — from [[cover-2006-elements/ch12-information-p1]] (information-theory → information-theory)
- [structural-analogy] "Opportunistic oversimplification" (vision oracle of 8 bits) ↔ simplified agent models in Bayesian theory of mind: simplify and hope the molar behaviour survives. — from [[dennett-1987-intentional-stance/ch09-fast]] (theory-of-mind → bayesian)
- [structural-analogy] Redundant gender marking ↔ error-correcting codes: parity bits add redundancy for robustness to noise. — from [[gibson-2019-efficiency/main]] (information-theory → information-theory)
- [structural-analogy] Informativeness–complexity trade-off in lexica ↔ rate–distortion theory: bits spent against loss of useful distinctions. — from [[gibson-2019-efficiency/main]] (information-theory → information-theory)
- [same-math] Evidence in db, $10\log_{10}$ odds ↔ information-theory: log-likelihood ratio in bits (change of log base). — from [[jaynes-2003-probability/ch05-queer]] (bayesian → information-theory)
- [structural-analogy] B's posterior as a product of two routes' distributions (6.136) ↔ information-theory: combining independent evidence by adding log-likelihoods (bits) — from [[jaynes-2003-probability/ch06-elementary-p2]] (bayesian → information-theory)
- [structural-analogy] Ockham factor / marginal likelihood ↔ information-theory: Minimum Description Length — model complexity is charged against fit, as bits for the model plus bits for the data. — from [[jaynes-2003-probability/ch20-model]] (bayesian → information-theory)
- [same-math] Raw bit content H₀ ↔ statistical mechanics: Boltzmann entropy k_B ln Ω for a microcanonical ensemble (p. 87). — from [[mackay-2003-information/ch04-source]] (information-theory → complex-systems)
- [structural-analogy] Mixture code with $\log K$-bit header and incompleteness ↔ Bayesian: model averaging over $K$ models with a uniform prior. The source only points to bits-back coding (p. 108), so the link is ours. — from [[mackay-2003-information/ch05-symbol]] (information-theory → bayesian)
- [structural-analogy] random hash into M < N bits ↔ information-theory: random codes in channel coding — same random-code idea, but here mapping down instead of up. — from [[mackay-2003-information/ch12-hash]] (information-theory → information-theory)
- [same-math] bit-by-bit match, ratio 2^r ↔ bayesian: sequential updating with likelihood ratios — odds multiply by the likelihood ratio. — from [[mackay-2003-information/ch12-hash]] (information-theory → bayesian)
- [same-math] Optimal block and bit decoding ↔ Bayesian: MAP codeword vs marginal posterior per bit — the text defines both decoders from $P(\mathbf x|\mathbf r)$ (p. 225). — from [[mackay-2003-information/ch13-binary]] (information-theory → bayesian)
- [structural-analogy] Selection as a 1-bit-per-individual teacher ↔ Bayesian: updating from weak, redundant feedback. — from [[mackay-2003-information/ch19-have]] (information-theory → bayesian)
- [structural-analogy] $I=\sum_g\log_2(f_g/\tfrac12)$ ↔ information-theory: bits gained relative to a uniform ½ prior per site. — from [[mackay-2003-information/ch19-have]] (information-theory → information-theory)
- [structural-analogy] choosing a bit order to shrink the trellis ↔ bayesian: choosing a variable elimination order to reduce the cost of exact inference. — from [[mackay-2003-information/ch25-exact]] (information-theory → bayesian)
- [same-math] MDL message length $L=-\log_2P$ ↔ information-theory: Shannon code length $-\log_2P(x)$ — the same relation, used to translate models into bits (p. 352) — from [[mackay-2003-information/ch28-model]] (information-theory → information-theory)
- [structural-analogy] Value of prospecting data ↔ information-theory: mutual information — both measure what a signal is worth, though here in utility units rather than bits. — from [[mackay-2003-information/ch36-decision]] (information-theory → information-theory)
- [structural-analogy] Capacity in bits per weight ↔ information-theory: channel capacity — memories pass through weights and attractors as through a noisy channel. — from [[mackay-2003-information/ch42-hopfield]] (information-theory → information-theory)
- [structural-analogy] $I(T;Y)$ for classifiers ↔ information-theory: channel from target to output, measured in bits. — from [[mackay-2003-information/ch44-supervised]] (information-theory → information-theory)
- [same-math] Sum–product (forward–backward) on a trellis ↔ bayesian: posterior distribution of each hidden variable given observations — the bit posterior given channel likelihoods. — from [[mackay-2003-information/ch48-convolutional]] (information-theory → bayesian)
- [metaphor] Yes/no questions to halve the search space ↔ bits of KL (§5.1.2.4). — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → unspecified)
- [structural-analogy] Parity-bit decoding ↔ bayesian: posterior over codewords from a likelihood (bit-flip noise) and a deterministic prior constraint. — from [[murphy-2023-pml2/ch05-information-p2]] (bayesian → bayesian)
- [same-math] Nyquist's $\log m$ for $m$ symbols ↔ information theory: bits per symbol for equiprobable symbols — same counting argument as $\log_2$ of the number of outcomes (pp. 37–38). — from [[pierce-1980-introduction/ch02-origins]] (information-theory → information-theory)
- [structural-analogy] Guessing the next letter (Shannon's experiment) ↔ next-token prediction by language models: both measure how predictable text is, in bits per symbol. — from [[pierce-1980-introduction/ch05-entropy]] (information-theory → llm)
- [structural-analogy] Fidelity criterion over long stretches ↔ rate–distortion theory: required bits depend on the allowed distortion measure. — from [[pierce-1980-introduction/ch07-efficient]] (information-theory → information-theory)
- [structural-analogy] minimum energy $0.693\,kT$ per bit (10.6) ↔ information theory/physics: Landauer's principle ($kT\ln 2$ per bit); the same numerical bound, though this unit derives it from capacity, not from erasure. — from [[pierce-1980-introduction/ch10-information]] (information-theory → information-theory)
- [structural-analogy] one-molecule engine's bit-for-work trade ↔ Kelly criterion: side information has a measurable, bounded value (it raises growth by its mutual information). — from [[pierce-1980-introduction/ch10-information]] (information-theory → information-theory)
- [structural-analogy] number of equally likely states, $\log_2 m$ bits ↔ source entropy: the same counting idea behind both entropies (p. 202). — from [[pierce-1980-introduction/ch10-information]] (information-theory → information-theory)
- [structural-analogy] fidelity criterion with penalties ↔ rate–distortion function — both ask how many bits suffice for a given tolerated damage (Pierce gives no formula). — from [[pierce-1980-introduction/ch14-back]] (information-theory → unspecified)
- [structural-analogy] Elias' extractor ↔ source coding: uniform-on-a-set to bits mirrors enumerative coding of a type class, although the author says the variable-length encoders are studied in Chapter 10. — from [[polyanskiy-2025-information/ch10-random]] (information-theory → information-theory)
- [structural-analogy] SDPI constant as the slope of F_I at 0 ↔ distributed inference: bits communicated replace sample size. — from [[polyanskiy-2025-information/ch18-hypothesis]] (information-theory → other:distributed-inference)
- [metaphor] "Bits as universal currency" (separation theorem) ↔ economics: common unit of exchange — the compressor and channel code interface only through bits (p. 392). — from [[polyanskiy-2025-information/ch21-channel]] (information-theory → economics-finance)
- [metaphor] Minimal energy per bit ↔ physics: Landauer's principle (energy cost of information) — both are energy-per-bit floors; the text only mentions $N_0=kT$ (p. 410). — from [[polyanskiy-2025-information/ch23-capacity]] (information-theory → other:physics)
- [metaphor] "bits as currency" ↔ economics: the text says the separation principle explains why bits are the natural currency of the digital age (p. 476). — from [[polyanskiy-2025-information/ch26-rate]] (information-theory → economics-finance)
- [structural-analogy] Capacity $\approx\inf_\epsilon\{\epsilon^2+\log N\}$ ↔ model selection / description length: trade-off between a quantization error and the bits naming the cell. — from [[polyanskiy-2025-information/ch35-entropic]] (information-theory → information-theory)
- [metaphor] distributed bit budget ↔ rational inattention: limited channel capacity per agent restricts aggregate inference. — from [[polyanskiy-2025-information/ch36-strong-p2]] (information-theory → information-theory)
- [structural-analogy] Capacity limit on received information ↔ rational inattention: an agent's attention treated as a channel with a bit-rate ceiling. — from [[shannon-1948-mathematical/main-p2]] (information-theory → information-theory)
- [structural-analogy] Descending the interlacing tree ↔ derandomization: the method of conditional expectations; fix one random bit at a time without worsening the quantity. — from [[spielman-2025-sagt/ch44-bipartite]] (linear-algebra → other:derandomization)
- [metaphor] efficient coding hypothesis ↔ neuroscience: neurons as channels with an energy cost per bit — from [[stone-2022-information/ch01-information]] (information-theory → other:neuroscience)
- [metaphor] Speed–accuracy trade-off ↔ rate–distortion trade-off — fast, low-bit responses are less accurate. — from [[stone-2022-information/ch08-rate]] (information-theory → unspecified)
- [same-math] "Entropy $n$ bits ≈ $2^n$ equiprobable states" ↔ language modelling: perplexity $=2^{\text{entropy}}$ — the effective number of choices. — from [[stone-2022-information/ch10-thermodynamic]] (information-theory → llm)
- [structural-analogy] genome gaining bits from selection ↔ Kelly criterion/doubling rate — both treat growth as information gained about an environment (the source does not make this link). — from [[stone-2022-information/ch11-information]] (information-theory → unspecified)
