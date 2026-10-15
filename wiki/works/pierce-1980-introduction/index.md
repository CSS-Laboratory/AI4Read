---
id: pierce-1980-introduction/index
work: pierce-1980-introduction
type: work-map
units: [pierce-1980-introduction/ch01-world, pierce-1980-introduction/ch02-origins, pierce-1980-introduction/ch03-mathematical, pierce-1980-introduction/ch04-encoding, pierce-1980-introduction/ch05-entropy, pierce-1980-introduction/ch06-language, pierce-1980-introduction/ch07-efficient, pierce-1980-introduction/ch08-noisy, pierce-1980-introduction/ch09-many, pierce-1980-introduction/ch10-information, pierce-1980-introduction/ch11-cybernetics, pierce-1980-introduction/ch12-information, pierce-1980-introduction/ch13-information, pierce-1980-introduction/ch14-back, pierce-1980-introduction/app-mathematical]
---

# Pierce, J. R. (1980). *An Introduction to Information Theory: Symbols, Signals and Noise* (2nd rev. ed.). Dover Publications. xii + 305 pp. (First published as *Symbols, Signals and Noise*, 1961.)

## In one paragraph
Pierce explains Shannon's communication theory with little formal mathematics. The theory grew from telegraph and telephone problems. It treats a message source as an ergodic random process. Its entropy, in bits, is the average number of binary digits per symbol that any good code needs. A noisy channel has a capacity. Below that capacity, the right redundancy lets errors be made as rare as we like. For a band-limited channel with Gaussian noise, a geometric argument gives $C = W\log(1+P/N)$. Pierce then tests the ideas against physics, language, psychology and art, and is frank about their limits. He says that the "indubitably valuable" core is electrical communication, and that "information" does not mean meaning. The book helps a reader build intuition before the mathematics.

## The path through the work
- [[pierce-1980-introduction/ch01-world]] — A scientific theory does not explain every use of a word like "communication"; it picks out the aspects of experience that can be related, and communication theory is a strongly mathematical, quite general theory whose important results are stated as proved theorems.
- [[pierce-1980-introduction/ch02-origins]] — Pierce argues that Shannon's theory of communication grew out of practical problems of telegraphy and telephony (Morse, Nyquist, Hartley), not out of statistical mechanics, although the two "entropies" are mathematically analogous.
- [[pierce-1980-introduction/ch03-mathematical]] — Pierce argues that a message source such as English text can be modelled as a stochastic (random-with-fixed-probabilities) process, specifically an ergodic source, which is simple enough for theorems yet close enough to real text to be useful.
- [[pierce-1980-introduction/ch04-encoding]] — Messages such as text and numbers, and speech after sampling and quantizing, can be turned into strings of binary digits, and how many digits it needs depends strongly on the chosen code, which hints that a "best" code might define the amount of information.
- [[pierce-1980-introduction/ch05-entropy]] — The entropy $H=-\sum p_i\log_2 p_i$ of a message source, measured in bits, equals the average number of binary digits per symbol needed to encode its messages, and long-block (Huffman) coding gets as close to it as we like.
- [[pierce-1980-introduction/ch06-language]] — Pierce offers, as openly labelled "informed ignorance", the idea that a grammar could show how much of English is choice, and suggests that meaning depends on intent, on lists of qualities tying words to the world, and on shared experience, none of which information theory has settled.
- [[pierce-1980-introduction/ch07-efficient]] — Entropy tells us the minimum number of binary digits needed, but Pierce argues that reaching it in practice is better served by exploiting the natural structure of a source and the limits of eye and ear than by applying a blind mechanical scheme (pp. 127–128, 142).
- [[pierce-1980-introduction/ch08-noisy]] — Shannon showed that a noisy channel has a capacity $C$ (the largest information rate it can carry), and that a source with entropy below $C$ can be sent with arbitrarily few errors by adding the right kind of redundancy.
- [[pierce-1980-introduction/ch09-many]] — By treating the 2WT samples of a band-limited signal as coordinates of a point in 2WT-dimensional space, and using the fact that most of a high-dimensional sphere's volume lies near its surface, Shannon's channel capacity C = W log(1 + P/N) for a Gaussian noise channel is derived (the counting gives the upper limit; Pierce says Shannon's further argument shows it can be approached).
- [[pierce-1980-introduction/ch10-information]] — Heat sets an unavoidable noise floor of kT watts per hertz, which (for ideal encoding) fixes a minimum energy of 0.693 kT joule per bit, and that same energy equals the most work a one-molecule engine could gain, so the engine does not beat the second law.
- [[pierce-1980-introduction/ch11-cybernetics]] — Pierce argues that "cybernetics" is not one field but a loose umbrella over information theory, prediction and filtering, negative feedback, and computers and automata, so the word can add "a little glamor" but says little about anyone's field (pp. 208–209, 226–228).
- [[pierce-1980-introduction/ch12-information]] — Human performance does not have one fixed information rate: how fast a person handles bits depends strongly on how well the task is encoded for human abilities, so bits are a useful measure of task difficulty but not a universal psychological constant.
- [[pierce-1980-introduction/ch13-information]] — Pierce argues that art needs both order and surprise: pure randomness has the highest possible information rate, but listeners cannot tell one random thing from another, so art must be built from a learned "language" and keep its variety within human limits.
- [[pierce-1980-introduction/ch14-back]] — Pierce says that, to him, the indubitably valuable core of information theory lies in electrical communication, and he then surveys further mathematically grounded or active work (Kelly's gambling result, secrecy theory, sampling problems, a fidelity criterion, two-way channels, better codes and modulation), ending in a sober vein.
- [[pierce-1980-introduction/app-mathematical]] — Mathematical notation is shorthand for ideas that could be said in words, and this appendix teaches the shorthand the book uses: probabilities, sums, exponents and base-2 logarithms.

## Big ideas across units
- **Information as a logarithmic measure of choice (the bit).** Hartley's logarithm of the number of sequences leads to binary digits and then to entropy. The appendix supplies the notation. Units: [[pierce-1980-introduction/ch02-origins]], [[pierce-1980-introduction/ch04-encoding]], [[pierce-1980-introduction/ch05-entropy]], [[pierce-1980-introduction/app-mathematical]].
- **Sources as statistical (ergodic) models.** English is treated as an approximately ergodic random source. The entropy results, the geometric capacity argument and the later discussions of language rest on this model. Units: [[pierce-1980-introduction/ch03-mathematical]], [[pierce-1980-introduction/ch05-entropy]], [[pierce-1980-introduction/ch06-language]], [[pierce-1980-introduction/ch09-many]].
- **Entropy as the limit of efficient coding.** Block coding and Huffman coding approach the entropy bound, and practical coding exploits the structure of the source and of eye and ear. Units: [[pierce-1980-introduction/ch04-encoding]], [[pierce-1980-introduction/ch05-entropy]], [[pierce-1980-introduction/ch07-efficient]], [[pierce-1980-introduction/ch14-back]].
- **Redundancy: remove it, then add the right kind.** Removing redundancy makes errors dangerous. Noise needs carefully designed redundancy. Art needs familiar order as well as surprise. Units: [[pierce-1980-introduction/ch02-origins]], [[pierce-1980-introduction/ch07-efficient]], [[pierce-1980-introduction/ch08-noisy]], [[pierce-1980-introduction/ch13-information]].
- **Channel capacity and its reach from discrete to continuous channels.** Equivocation leads to the capacity $C$ and the coding theorem. Sampling and geometry then give $W\log(1+P/N)$, with a trade between band width and power. Units: [[pierce-1980-introduction/ch02-origins]], [[pierce-1980-introduction/ch04-encoding]], [[pierce-1980-introduction/ch08-noisy]], [[pierce-1980-introduction/ch09-many]], [[pierce-1980-introduction/ch14-back]].
- **Physical limits and the link to thermodynamic entropy.** The entropy analogy is noted first. Later, thermal noise sets a minimum energy per bit, tied to the one-molecule engine and the second law. Units: [[pierce-1980-introduction/ch02-origins]], [[pierce-1980-introduction/ch09-many]], [[pierce-1980-introduction/ch10-information]].
- **What "information" does not mean: meaning and human limits.** Theory is limited to what can be related, language and meaning stay unsettled, there is no fixed human information rate, and art depends on learned language. Units: [[pierce-1980-introduction/ch01-world]], [[pierce-1980-introduction/ch06-language]], [[pierce-1980-introduction/ch12-information]], [[pierce-1980-introduction/ch13-information]], [[pierce-1980-introduction/ch14-back]].
- **A sober view of the theory's scope.** Pierce separates the core of the theory from loose extensions such as cybernetics and psychology. Units: [[pierce-1980-introduction/ch11-cybernetics]], [[pierce-1980-introduction/ch12-information]], [[pierce-1980-introduction/ch13-information]], [[pierce-1980-introduction/ch14-back]].

## How to read it
- **Essential core:** Chapters 4, 5, 8 and 9. They give encoding, entropy, the noisy-channel theorem and the continuous capacity formula. Chapter 14 states what Pierce himself regards as the valuable core: source entropy, channel capacity and efficient coding.
- **Dependencies from the units' stated prerequisites:**
  - Chapter 5 needs Chapters 3 and 4.
  - Chapter 6 needs Chapter 3.
  - Chapter 7 needs Chapter 5.
  - Chapter 8 needs Chapters 5 and 7.
  - Chapter 9 needs Chapters 3 and 5, and the idea of channel capacity.
  - Chapter 10 needs the Chapter 9 capacity formula.
  - Chapter 12 needs Chapter 8.
  - Chapter 13 needs Chapter 3.
  - Chapter 14 needs the earlier chapters on entropy and capacity.
- **Background, orientation and reference:** Chapter 1 sets the idea of a theory and of a theorem. Chapter 2 gives the history and the sampling and bandwidth background. The appendix is notation to consult when needed, for logarithms, sums and probabilities.
- **Can be skipped on a first pass (a judgement from the material):** Chapters 6, 11, 12 and 13 are excursions from the core, where Pierce sets the theory against language, cybernetics, psychology and art. Chapter 10 is an optional extension of the capacity formula to physics. Chapter 7 mainly applies Chapter 5's ideas to speech and TV. The warning about removing redundancy at its end leads into Chapter 8.

## Concepts introduced
- [[bit]] — [[pierce-1980-introduction/ch01-world]]
- [[noisy-channel]] — [[pierce-1980-introduction/ch01-world]]
- [[theory-generality]] — [[pierce-1980-introduction/ch01-world]]
- [[physical-vs-mathematical-theory]] — [[pierce-1980-introduction/ch01-world]]
- [[theorem-and-proof]] — [[pierce-1980-introduction/ch01-world]]
- [[constructive-proof]] — [[pierce-1980-introduction/ch01-world]]
- [[one-to-one-mapping]] — [[pierce-1980-introduction/ch01-world]]
- [[continuous-mapping]] — [[pierce-1980-introduction/ch01-world]]
- [[entropy-communication-sense]] — [[pierce-1980-introduction/ch02-origins]]
- [[entropy-thermodynamic]] — [[pierce-1980-introduction/ch02-origins]]
- [[redundancy]] — [[pierce-1980-introduction/ch02-origins]]
- [[intersymbol-interference]] — [[pierce-1980-introduction/ch02-origins]]
- [[fourier-analysis]] — [[pierce-1980-introduction/ch02-origins]]
- [[linear-circuit]] — [[pierce-1980-introduction/ch02-origins]]
- [[bandwidth]] — [[pierce-1980-introduction/ch02-origins]]
- [[nyquist-relation]] — [[pierce-1980-introduction/ch02-origins]]
- [[hartley-information]] — [[pierce-1980-introduction/ch02-origins]]
- [[stochastic-process]] — [[pierce-1980-introduction/ch03-mathematical]]
- [[conditional-probability]] — [[pierce-1980-introduction/ch03-mathematical]]
- [[n-th-order-approximation]] — [[pierce-1980-introduction/ch03-mathematical]]
- [[finite-state-machine]] — [[pierce-1980-introduction/ch03-mathematical]]
- [[stationary-source]] — [[pierce-1980-introduction/ch03-mathematical]]
- [[ergodic-source]] — [[pierce-1980-introduction/ch03-mathematical]]
- [[ensemble-vs-time-average]] — [[pierce-1980-introduction/ch03-mathematical]]
- [[encoding]] — [[pierce-1980-introduction/ch04-encoding]]
- [[sampling-theorem]] — [[pierce-1980-introduction/ch04-encoding]]
- [[quantization]] — [[pierce-1980-introduction/ch04-encoding]]
- [[binary-numeral-system]] — [[pierce-1980-introduction/ch04-encoding]]
- [[block-coding]] — [[pierce-1980-introduction/ch04-encoding]]
- [[tree-of-choice]] — [[pierce-1980-introduction/ch04-encoding]]
- [[entropy]] — [[pierce-1980-introduction/ch05-entropy]]
- [[entropy-rate]] — [[pierce-1980-introduction/ch05-entropy]]
- [[joint-and-conditional-entropy]] — [[pierce-1980-introduction/ch05-entropy]] (written "joint and conditional entropy" in Ch. 8 and Ch. 14)
- [[typical-set-aep]] — [[pierce-1980-introduction/ch05-entropy]]
- [[source-coding-theorem]] — [[pierce-1980-introduction/ch05-entropy]]
- [[huffman-arithmetic-coding]] — [[pierce-1980-introduction/ch05-entropy]]
- [[prefix-code-kraft]] — [[pierce-1980-introduction/ch05-entropy]]
- [[channel-capacity]] — [[pierce-1980-introduction/ch05-entropy]]
- [[noiseless-channel-theorem]] — [[pierce-1980-introduction/ch05-entropy]]
- [[zipf-law]] — [[pierce-1980-introduction/ch05-entropy]]
- [[grammar-as-generator]] — [[pierce-1980-introduction/ch06-language]]
- [[kernel-sentence-grammar]] — [[pierce-1980-introduction/ch06-language]]
- [[language-as-imperfect-code]] — [[pierce-1980-introduction/ch06-language]]
- [[feature-list-classification]] — [[pierce-1980-introduction/ch06-language]]
- [[understanding]] — [[pierce-1980-introduction/ch06-language]]
- [[entropy-H]] — [[pierce-1980-introduction/ch07-efficient]]
- [[fidelity-criterion]] — [[pierce-1980-introduction/ch07-efficient]]
- [[hyperquantization]] — [[pierce-1980-introduction/ch07-efficient]]
- [[pulse-code-modulation]] — [[pierce-1980-introduction/ch07-efficient]]
- [[companding]] — [[pierce-1980-introduction/ch07-efficient]]
- [[vocoder]] — [[pierce-1980-introduction/ch07-efficient]]
- [[predictive-coding]] — [[pierce-1980-introduction/ch07-efficient]]
- [[equivocation]] — [[pierce-1980-introduction/ch08-noisy]]
- [[chain-rule]] — [[pierce-1980-introduction/ch08-noisy]]
- [[mutual information I(X;Y)]] — [[pierce-1980-introduction/ch08-noisy]]
- [[noisy-channel-coding-theorem]] — [[pierce-1980-introduction/ch08-noisy]]
- [[error-correcting-code]] — [[pierce-1980-introduction/ch08-noisy]]
- [[binary-symmetric-channel]] — [[pierce-1980-introduction/ch08-noisy]]
- [[hamming-distance]] — [[pierce-1980-introduction/ch08-noisy]]
- [[parity-check-digit]] — [[pierce-1980-introduction/ch08-noisy]]
- [[random-coding-argument]] — [[pierce-1980-introduction/ch08-noisy]]
- [[shannon-hartley-formula]] — [[pierce-1980-introduction/ch09-many]]
- [[signal-space]] — [[pierce-1980-introduction/ch09-many]]
- [[high-dimensional-geometry]] — [[pierce-1980-introduction/ch09-many]]
- [[block-coding-continuous]] — [[pierce-1980-introduction/ch09-many]]
- [[bandwidth-power-tradeoff]] — [[pierce-1980-introduction/ch09-many]]
- [[threshold-effect]] — [[pierce-1980-introduction/ch09-many]]
- [[thermal-noise]] — [[pierce-1980-introduction/ch10-information]]
- [[noise-temperature]] — [[pierce-1980-introduction/ch10-information]]
- [[thermodynamic-entropy]] — [[pierce-1980-introduction/ch10-information]]
- [[free-energy]] — [[pierce-1980-introduction/ch10-information]]
- [[maxwells-demon]] — [[pierce-1980-introduction/ch10-information]]
- [[quantum-limits-on-communication]] — [[pierce-1980-introduction/ch10-information]]
- [[cybernetics]] — [[pierce-1980-introduction/ch11-cybernetics]]
- [[linear-prediction]] — [[pierce-1980-introduction/ch11-cybernetics]]
- [[nonlinear-prediction]] — [[pierce-1980-introduction/ch11-cybernetics]]
- [[smoothing-filtering]] — [[pierce-1980-introduction/ch11-cybernetics]]
- [[negative-feedback]] — [[pierce-1980-introduction/ch11-cybernetics]]
- [[servomechanism]] — [[pierce-1980-introduction/ch11-cybernetics]]
- [[feedback-stability]] — [[pierce-1980-introduction/ch11-cybernetics]]
- [[homeostasis]] — [[pierce-1980-introduction/ch11-cybernetics]]
- [[stored-program-computer]] — [[pierce-1980-introduction/ch11-cybernetics]]
- [[compiler]] — [[pierce-1980-introduction/ch11-cybernetics]]
- [[uniform-information-density]] — [[pierce-1980-introduction/ch12-information]]
- [[mandelbrot-zipf-generalization]] — [[pierce-1980-introduction/ch12-information]]
- [[latency-log-alternatives-law]] — [[pierce-1980-introduction/ch12-information]]
- [[miller-7-plus-minus-2]] — [[pierce-1980-introduction/ch12-information]]
- [[output-vs-input-information]] — [[pierce-1980-introduction/ch12-information]]
- [[entropy-H-X]] — [[pierce-1980-introduction/ch13-information]]
- [[pulse-code-modulation-sampling]] — [[pierce-1980-introduction/ch13-information]]
- [[human-information-rate-limit]] — [[pierce-1980-introduction/ch13-information]]
- [[musical-language-as-learned-constraint]] — [[pierce-1980-introduction/ch13-information]]
- [[stochastic-composition]] — [[pierce-1980-introduction/ch13-information]]
- [[digram-probability-model]] — [[pierce-1980-introduction/ch13-information]]
- [[kelly-criterion-doubling-rate]] — [[pierce-1980-introduction/ch14-back]]
- [[two-way-channel-capacity-region]] — [[pierce-1980-introduction/ch14-back]]
- [[mathematical-notation-vs-mathematics]] — [[pierce-1980-introduction/app-mathematical]]
- [[probability-as-fraction]] — [[pierce-1980-introduction/app-mathematical]]
- [[joint-probability]] — [[pierce-1980-introduction/app-mathematical]]
- [[summation-notation]] — [[pierce-1980-introduction/app-mathematical]]
- [[marginalization]] — [[pierce-1980-introduction/app-mathematical]]
- [[exponent-rules]] — [[pierce-1980-introduction/app-mathematical]]
- [[logarithm-base-2]] — [[pierce-1980-introduction/app-mathematical]]
- [[natural-logarithm]] — [[pierce-1980-introduction/app-mathematical]]
