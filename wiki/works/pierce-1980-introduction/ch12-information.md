---
id: pierce-1980-introduction/ch12-information
work: pierce-1980-introduction
unit: 12 Information Theory and Psychology
pages: 229-249
fields: [information-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Information Theory and Psychology

## L0 — One line
Human performance does not have one fixed information rate: how fast a person handles bits depends strongly on how well the task is encoded for human abilities, so bits are a useful measure of task difficulty but not a universal psychological constant.

## L1 — The gist (≤ 120 words)
The unit examines the early idea that entropy (an information measure in bits) can measure human performance: that task difficulty or response time is proportional to bits. Latency (response delay) does grow with the logarithm of the number of alternatives in some tasks. But reading experiments give very different rates, so Pierce concludes that no unique human information rate exists. He then looks at Zipf's law (word probability roughly inversely proportional to rank), Mandelbrot's derivations of it, and Miller's 7 ± 2 memory limit. He says these experiments measure output, not input. His view: information theory gave psychology a new picture of communication and a new measure of task complexity, but is only an attractive area there.

**Prerequisites:** bits as log₂ of the number of equally likely alternatives; entropy of a source; the idea of channel capacity (Ch. VIII); logarithms; reading a log–log plot.

## L2 — Key ideas (5–10 bullets)
- Early idea of psychologists: task difficulty, perhaps response time, must be proportional to bits. In Hyman's light experiment, latency rose about 0.15 s per bit. (pp. 229–230)
- Dividing extra time by extra bits does not give a valid information rate. After much practice, and perhaps in other tasks, the effect is small or absent, and the same logic applied to reading data gives an infinite "rate". (pp. 231–234)
- Reading randomized word lists gave the highest demonstrated rate, about 42–44 bits/s. The limit seems mental, not mechanical. A person is better seen as a flexible information-handling channel (a path that carries information) that works best when information is well encoded. (pp. 234–237)
- Zipf's law says the rth most common word has probability about A/r. If Zipf's law holds and words are chosen independently to maximise information per unit time, reading time should be $t_r=a+b\log r$. Reading-time data are too scattered to confirm this. (pp. 238–242)
- Zipf's curves suggest that many written languages have similar word distributions, perhaps set by the brain, though Pierce says we do not really know. Zipf's data have been criticised, and Pierce doubts the strict form. (pp. 242–245)
- Mandelbrot derives $p(r)=P(r+V)^{-B}$ in two ways. It fits better than Zipf's original law, but Pierce says this does not mean Mandelbrot's derivation is necessarily correct. (pp. 246–247)
- Taken as input rates, Miller's 7 ± 2 and the reading rates would seem to imply that pictures or TV could be sent with very few bits. Pierce believes not: these experiments measure what comes out of the person, not what goes in. Averbach and Sperling's results seem to show that more items are briefly stored than are reported. (pp. 248–249)
- Pierce thinks information theory gave psychology a new picture and measure, but is only an attractive area there. (p. 249)

## L3 — Walkthrough

### Opening: caution (p. 229)
Pierce says much writing on information theory and psychology merely attached new terms to old, vague ideas. He limits himself to experiments concrete enough to discuss, chosen largely by personal interest. Early psychologists reasoned that entropy measures amount of information and people use information. So task difficulty, perhaps task time, "must be" proportional to information. (p. 229)

### Hyman's experiment: latency versus bits (pp. 230–231)
- **Set-up.** Several lights, each with a monosyllabic name known to the subject. After a warning, one light flashed (chosen at random, equal probabilities). The subject said its name as fast as possible, and the latency (response time) was measured. (p. 230)
- **Information per trial.** $\log_2 8 = 3$ bits for 8 lights; 7 lights give 2.81 bits, 6 give 2.58, 5 give 2.32, 4 give 2.00, 3 give 1.58, 2 give 1, and 1 light gives 0 bits. (p. 230)
- **Result (Fig. XII-1).** There is a latency even at 0 bits. Beyond that, latency increases in proportion to the bits, about 0.15 s per bit. Merkel had noted a rise of latency with the logarithm of the number of alternatives in 1885. (p. 230)
- **The hasty inference.** "Some unwary psychologists" concluded that a person takes 0.15 s per bit, so capacity is about $1/0.15 \approx 7$ bits/s. Pierce asks whether this is a universal constant of human perception or thought, and then goes on to give reasons for doubt. (p. 230)
- **Why not.** Different experimenters get different seconds-per-bit rates. Mowbray and Rhoades (1959) found that after much practice latency shows little or no effect of information content. This suggests one way of handling information in learning, where alternatives matter, and another after much learning. In a key-pressing task with a vibration signal, there may be little increase in latency even from the start. (p. 231)

> **Intuition note.** In some tasks, each doubling of alternatives adds a fixed time. That is a fact about those tasks. It is not a speed limit on the person.

### Reading-rate experiments (pp. 232–237)
- **The same logic breaks down.** Even if latency were constant plus a term proportional to bits, dividing time by bits would not give a meaningful rate. (p. 232)
- **Method (Karlin and Pierce).** The sender picks words at random, equally likely, from an alphabet of 16 words. That is $\log_2 16 = 4$ bits per word. If the subject reads aloud 4 words/s, the rate is $4\times 4 = 16$ bits/s. (p. 232)
- **Fig. XII-2.** Words came from the 500 most common English words. Reading rate drops somewhat from 2 to 4 word vocabularies (1 to 2 bits). It is almost constant from 4 to 256 words (2 to 8 bits per word). (p. 232)
- **Infinity.** Between 2 and 8 bits the reading rate does not change, so the time change is 0 while bits rise by 6. Dividing 6 by 0 gives an "infinite rate". Pierce calls this ridiculous, but scarcely more so than the Hyman-style inference. (p. 232)
- **Direct rates.**
  - Reader A reads 8-bit words at 3.8 per second, about 30 bits/s. (p. 234)
  - From a 5,000-word dictionary (12.3 bits per word), A reads 2.7 words/s, about 33 bits/s. (p. 234)

  Thus no unique rate describes a person. He is an information-handling channel with built-in limits, flexible, and best when information is "properly encoded". He is little slowed by complexity but is not fast. (p. 234)
- **Optimum vocabulary (Fig. XII-3).** Reading speed falls with more syllables and, just as strongly, with lower familiarity (word from the first, tenth or nineteenth thousand in commonness). (p. 234)
- **Highest rates demonstrated.**
  - Preferred vocabulary: the 2,500 most common monosyllables, 11.3 bits per word. A reader reached 3.7 words/s, so 42 bits/s. (p. 236)
  - "Scrambled prose" (words chosen at random with prose probabilities, no grammar): entropy about 11.8 bits per word, 3.7 words/s, so 44 bits/s. (p. 236)

  Pierce thinks little more could be gained. The rate is slow for electrical communication but is about 2,500 binary choices a minute. (p. 236)
- **What limits the rate?**
  - Letter-by-letter reading? Chinese readers who read both scripts read random Chinese characters and the equivalent English words at almost exactly the same speed. (p. 236)
  - A mechanical limit? In Fig. XII-4, a memorized phrase is repeated over twice as fast as the preferred list is read, and prose is read appreciably faster. So the limit seems mental rather than mechanical. (p. 236)
- **Analogy to coding.** Tailoring a task to human abilities by experiment is like encoding a source to reach the highest rate over a noisy channel (the channel capacity, Ch. VIII). The preferred list was an attempt at this. (pp. 236–237)

> **Intuition note.** The bit count of the message alone does not set the speed. How the message is packaged (familiar short words, or random choices from a big list) matters a lot. Like a channel, a person seems to have a best code.

### Zipf's law and effort (pp. 237–241)
- Random words with English frequencies give as high a rate or a little higher. Perhaps English words and frequencies were fitted to human abilities by long unconscious evolution. (pp. 237–238)
- **Zipf's law.** From Ch. V: the probability of a word is very nearly inversely proportional to its rank. The hundredth word occurs about a hundredth as often as the first. Zipf ascribed this to a principle of least effort. (p. 238)
- It cannot be right for all words in this simple form: the probabilities would sum to more than 1. Pierce treats it first as an approximate empirical description. (p. 238)
- **Cost as reading time.** Letter counts are unlikely to be the cost, since reading speed is about the same for Chinese characters and English words and familiarity matters as much as syllables. Perhaps reading time measures the accessibility, hence cost, of a word. (p. 238)
- **Maximising information per unit time.** Pierce says it is easy to show (he does not show it here) that, for randomly chosen words with speaking time $t_r$ for the rth word in order of commonness, the information rate is greatest when
$$p(r)=2^{-c\,t_r}\tag{12.1}$$
  with $c$ chosen so the probabilities sum to 1. Longer words are then used less often. (p. 239)
- **Combining with Zipf.** With Zipf's law, the text gives
$$p(r)=\frac{A}{r}\tag{12.2}$$
  (the text layer is blank here; the form is inferred from "inversely proportional to rank", p. 238, and from 12.3). $A$ is another constant. Equating the two:
$$\frac{A}{r}=2^{-c\,t_r}\tag{12.3}$$
  By a relation in the Appendix this becomes
$$t_r=a+b\log r\tag{12.4}$$
  (added step: taking $\log_2$ of 12.3 gives $\log A-\log r=-c\,t_r$, so $t_r=(\log r-\log A)/c$; hence $b=1/c$, $a=-(\log A)/c$.) If Zipf's law holds and rate is maximised for independent random words, 12.4 should fit reading data. Real text is not random and independent, so 12.1 need not truly maximise transmission, but the prediction is worth testing. (pp. 239–240)
- **Test (Riesz; Mandelbrot with Howes's data).** It seems fairly clear that recognition limits reading speed, not utterance, so Riesz timed three successive words and compared with the sum from 12.4. In Fig. XII-5 a straight line fits the data as well as any curve would, but the points are too scattered to prove 12.4. Scatter is expected. Rank reflects prose in general, not the subject's familiarity. Word length matters, and relations between successive words were ignored. (p. 240)
- Pierce finds such work "exasperating": further experiments are possible but unlikely to establish anything clear-cut. (p. 240)
- It suggests word use may be governed by economy of effort, measured as time. (p. 242)

### Vocabulary size and Zipf's graphs (pp. 242–245)
- Pierce argues that vocabulary size can be traded against word combinations ("blonde girl" versus "girl with light hair"). Even the 26-letter alphabet can be seen as a reduced language. So perhaps all languages tend to a basic vocabulary size set by the brain, to which clever people add special words. (p. 242)
- **Fig. XII-6 (Zipf).** Frequency versus rank for 260,430 running words of *Ulysses* (A) and 43,989 newspaper words (B). Line C is the idealised 45° Zipf line. Heights depend on sample size. The slope and its constancy matter. The steps at the lower right appear because rare words occur 1, 2, 3 … times. (pp. 242–243)
- **Consequences of the strict 45° line.** Both scales start at 1, so the number of different words equals the number of occurrences of the most frequent word. Also, a number of words equal to the square root of the number of different words makes up half the sample. In Fig. XII-7, about 170 words make up half of the Joyce passage, and Fig. XII-6 says the same holds for newspaper writing. (pp. 243–245)
- **Other languages (Zipf's curves).**
  - The law holds well for Gothic, if anything spaced as a word counts as a word.
  - It holds fairly well for Yiddish and some Old and Middle High German authors, with irregularities at the upper left.
  - Norwegian curves are steeper at the lower right.
  - Plains Cree has about three-fourths the Zipf slope, meaning more different words, a larger vocabulary.
  - Chinese characters zoom up at the left, indicating a smaller vocabulary. (p. 245)
- Pierce thinks the similarity across languages is remarkable. Perhaps languages adapt to a pattern set by the human brain and minimise effort. Pierce adds that we do not really know whether this is so. (p. 245)
- **Criticism.** Pierce cannot believe the number of different words is dictated entirely by sample length. Certainly the frequency of a word such as "the" cannot change with sample length, as the simple law implies. It is said Zipf's law holds best for samples of about 120,000 words, with too many once-only words in smaller samples and too few in larger ones. He thinks it most reasonable that only multiple authorship gave the newspaper the same vocabulary as Joyce. (p. 245)

### Mandelbrot's derivations (pp. 245–248)
- Another approach is to show Zipf's law must follow from simple assumptions. Mandelbrot did the first satisfactory work. (pp. 245–246)
- **Derivation 1.** Text is a random sequence of letters and spaces with unequal probabilities (as in Ch. III's first-order approximation). This allows infinitely many "words". Mandelbrot shows that the probability of the rth "word" in order of commonness is
$$p(r)=P\,(r+V)^{-B}\tag{12.5}$$
  $B$ and $V$ can be computed from the letter and space probabilities. $B>1$, and $P$ makes the probabilities sum to 1. If $V$ is very small and $B$ very nearly 1, this is practically Zipf's law. In general it is less steep at upper left and steeper at lower right than the 45° line, and fits data on much actual text better. (p. 246)
- **Objections (as Pierce reports).** It has been asserted that word lengths from this random process do not match English. Language has non-random features (words shorten with use: taxi, cab from taxicab; cab from cabriolet). Pierce asks whether the random production of "words" that obey Zipf's law explains the law, and says it seems to him this can be asserted only if we can show how the forces shaping language imitate the random process. (p. 246)
- **Derivation 2.** Word frequencies maximise information for a given cost. In the simple case each letter has a cost and a word's cost is the sum of its letter costs. This yields the same 12.5, with different interpretations of the symbols. $B$ can be less than 1 if the number of allowable words is finite. (p. 247)
- **Fitting.** $P$, $V$, $B$ can be chosen to best fit data, and this fits better than $V=0$, $B=1$. With such choices it can be made to fit available data very well in all but a few exception cases. Modern Hebrew of about 1930 and Pennsylvania Dutch (a mixture of languages) are best fitted by $B<1$. (p. 247)
- **Meaning of $B$ (Mandelbrot).** Wealth of vocabulary is measured chiefly by $B$. If $B$ is much greater than 1, a few words are used over and over. If $B$ is nearer 1, there is greater variety. As a child grows, $B$ falls from about 1.6 to about 1.15, or to about 1 for James Joyce. (p. 247)
- **Caution.** Equation 12.5 fits better and removes the objection that the probability of "the" depends on sample length. This does not mean Mandelbrot's explanation is necessarily correct. Another expression might fit even better, and a more thorough study would be needed. (p. 247)
- Zipf's law also holds for city populations in most countries (the tenth city has about a tenth of the largest's population). This may be fortuitous, as the inverse-square law holds both for gravity and for light intensity, yet these cannot be derived from a common theory. (pp. 247–248)

> **Intuition note.** A formula with free constants can be tuned to fit data, so a good fit alone does not show that the derivation is right. For the random-letter derivation Pierce asks us to show how the forces that shape language imitate the random process.

### Limits of the nervous system: Miller's 7 ± 2 (pp. 248–249)
- **Miller's law.** After a short observation, a person can remember and repeat the names of 5 to 9 simple familiar objects (digits, letters, familiar words). (p. 248)
- **Bits recalled.**
  - Black beans: up to 9, so 10 possibilities, $\log 10 = 3.3$ bits. (p. 248)
  - Binary digits: perhaps 7, so 7 bits. (p. 248)
  - Letters: 4 or 5, so as much as $5\log 26 \approx 23$ bits. (p. 248)
  - Common words: 3 or 4 from the 500 most common, $3\log 500\approx 27$ bits. (p. 248)

  As with reading, gain from complexity outweighs loss from fewer items. (p. 248)
- **Embarrassing implications.** If a man gets only 27 bits from a picture, could 27 bits transmit any picture? If he handles only about 40 bits/s, could TV or voice of good quality be sent at 40 bits/s? Pierce believes "no" in each case. We measured what comes out of the person, not what goes in. He chooses what to notice, and may notice more that is lost before he can report it. (pp. 248–249)
- **Averbach and Sperling.** They projected 16 or 18 letters briefly, then cued a randomly chosen letter to report. Reliable report of any cued letter would mean all letters "got in". Results seem to show far more than 7 ± 2 items are seen and briefly stored, for a few tenths of a second. It appears that about 7 ± 2 are transferred to a more permanent memory at about one item per hundredth of a second, or less. That memory keeps them for several seconds. It appears the size limit of this memory gives Miller's figure. (p. 249)

> **Intuition note.** A small report does not mean a small intake. The 7 ± 2 limit appears to come from the size of the longer-lasting memory, not from what is first taken in.

### Closing judgement (p. 249)
Pierce says he has covered only a few aspects. Pierce says he himself thinks information theory gave psychologists a new and important picture of communication and a new and important measure of task complexity, and that it stirred them to re-evaluate old data and seek new data. It seems to him, however, that for electrical communication it provides a central, universal structure, while in psychology it is only an attractive area. It also adds a few new expressions to the vocabulary of workers in other areas. (p. 249)

## Toy example (ours, not from the text)
A subject reads aloud random lists of equally likely words. Suppose (invented numbers) the subject reads 3.5 words/s whether the list has 4 or 64 words.
- 4 words: 2 bits each, so $2\times3.5=7$ bits/s.
- 64 words: 6 bits each, so $6\times3.5=21$ bits/s.

The slope method gives Δbits = 6 − 2 = 4 and Δtime per word = 0, so "rate" = 4/0 = ∞. The direct method (bits per word × words per second) gives 7 and 21 bits/s, which differ. So the same person has no single "bits per second" constant. If instead latency rose 0.15 s per bit in a different task, the slope method would give $1/0.15\approx 6.7$ bits/s. This is a fact about that task only.

## Concepts
- [[bit]] — measure of choice among equally likely alternatives, $\log_2 n$ (e.g. 8 lights = 3 bits) (p. 230)
- [[entropy]] — average information per symbol, applied to words as sources (11.8 bits per word for scrambled prose) (p. 236)
- [[channel-capacity]] — highest attainable rate after best encoding; the person is treated as such a channel (pp. 234, 237)
- [[redundancy]] — not named in this unit; not listed here.
- [[uniform-information-density]] — nearest canon item: words used so as to convey most information for a given cost (time) (p. 239)
- [[zipf-law]] (new) — word probability about inversely proportional to rank; only approximate (p. 238)
- [[mandelbrot-zipf-generalization]] (new) — $p(r)=P(r+V)^{-B}$; $B$ chiefly measures vocabulary wealth, per Mandelbrot (pp. 246–247)
- [[latency-log-alternatives-law]] (new) — latency grows with the log of the number of alternatives in some tasks (p. 230)
- [[miller-7-plus-minus-2]] (new) — short-term recall of 5–9 simple items (p. 248)
- [[output-vs-input-information]] (new) — experiments measure what the person reports, not what enters (p. 248)

## Canonical instances
- [[hyman-light-experiment]] — latency versus bits; 0.15 s per bit (p. 230)
- [[karlin-pierce-reading-rate]] — about 30–44 bits/s depending on vocabulary (pp. 234–236); the 16 bits/s on p. 232 is only a worked illustration
- [[zipf-ulysses-newspaper]] — rank-frequency curves; about 170 words make half of the Joyce passage (pp. 243–245)
- [[mandelbrot-two-derivations]] — random letters; maximum information per cost (pp. 246–247)
- [[averbach-sperling-partial-report]] — results seem to show more is stored than reported (p. 249)

## Bridges (candidates)
- [structural-analogy] Tailoring a task to a person ↔ channel coding: choosing a good code to approach capacity (pp. 236–237)
- [structural-analogy] Words used to maximise information per time cost ↔ efficient communication: word length and use trade off against cost (p. 239)
- [metaphor] Zipf's law in text and city sizes ↔ power laws across social data: similar shape, which Pierce says may be fortuitous (pp. 247–248)

## Questions this raises
- If latency–log laws hold early in learning but vanish with practice, what changes in how the person encodes the task? (p. 231)
- Does a better-fitting formula (12.5) tell us anything about how language develops, or only that it has more constants? (pp. 246–247)
- How would an experiment separate what enters from what is reported? (Averbach–Sperling is one attempt.) (p. 249)
- Is the similarity of word distributions across languages caused by brain limits, or by simple statistics of text? (pp. 245–246)

## Reading notes
- Printed page = pdf page − 16. Unit covers printed pp. 229–249.
- Edition: the source pages carry a running header with the book title, and the figures are numbered XII-1 to XII-7 (the chapter heading itself is garbled in the text layer). The unit metadata notes say this is the 1961 Harper & Brothers edition scan, not the 1980 Dover revision the work citation names; that is not visible on these pages. I could not confirm edition differences.
- I worked from the text layer. It is garbled in places: Eq. 12.2 is blank, Eq. 12.1 appears as "2~ c 'r", and 12.5 appears as "P(r + V)-B". I reconstructed these from the surrounding text (12.2 is inferred, not read). Figures (XII-1 to XII-7) are not legible in the text layer, so I give only what the text says about them.
- Pierce's statement that the maximisation giving 12.1 is an easy task is not proved in the unit; I give no proof. The step from 12.3 to 12.4 is marked (added step).
- Pierce's remark on a tremendous number of binary choices per minute has its words out of order in the text layer. I read it as about 2,500 choices a minute, which matches 42 bits/s × 60 s ≈ 2,520.
- The source prints the psychologist's name as "Averback"; the digest writes Averbach.
