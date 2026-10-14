---
id: pierce-1980-introduction/ch03-mathematical
work: pierce-1980-introduction
unit: "3 A Mathematical Model"
pages: 45-63
fields: [information-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# A Mathematical Model

## L0 — One line
Pierce argues that a message source such as English text can be modelled as a stochastic (random-with-fixed-probabilities) process, specifically an ergodic source, which is simple enough for theorems yet close enough to real text to be useful.

## L1 — The gist (≤ 120 words)
Communication theory needs a mathematical model of a message source. Pierce notes that letter, digram (letter-pair) and word frequencies in English are nearly constant. Random draws that respect such frequencies, or a finite-state machine (a machine with a fixed number of states that moves between them by chance), then produce text that looks increasingly English (Shannon's approximations). For proving theorems, the source is idealised as stationary (statistics do not depend on position) and ergodic (averages over one long message equal averages over all messages). Real writers are treated as approximately, not strictly, ergodic, so the theorems must be applied with caution. Using a random model does not imply that people act at random; for us, with incomplete knowledge, the source behaves as if some choices were random.

**Prerequisites:** ordinary probability as relative frequency; the idea of an average; the idea of a model that ignores irrelevant detail.

## L2 — Key ideas (5–10 bullets)
- A mathematical model keeps only what matters for the behaviour studied. Models may be accurate, crude or invalid (pp. 45–46).
- Deterministic models fit planets and networks. A deterministic model will not get us far with human communication, while a statistical model might; frequencies such as 0.13 for E are stable for groups and for single writers (pp. 46–48).
- Shannon's zero-, first-, second- and third-order letter approximations, and word approximations, resemble English more as more statistics are built in (pp. 49–53).
- A purely statistical scheme would not produce all sequences of words a person might utter; grammar is needed. A finite-state machine with random transitions can produce endless grammatical sentences of a limited kind (pp. 54–56).
- A source is stationary if starting probabilities can be chosen so that ensemble averages (averages across many sequences at one position) do not depend on position. An ergodic source is stationary and every ensemble average equals the corresponding time average (average along one sequence) (pp. 57–59).
- For an ergodic source, a longer stretch of one message gives better estimates of the source's statistics, and these apply to all its messages. This is one reason it is a profitable model (pp. 59–60).
- Real writers are treated as approximately, not strictly, ergodic. Mixing English and French writers is not ergodic, so exact theorems need cautious use (pp. 60–61).
- A random model does not imply that man acts at random. For us, with incomplete knowledge, the source behaves "as if" some choices were random, insofar as we cannot predict them (pp. 61–62).

## L3 — Walkthrough

### Models in general (pp. 45–47)
- A mathematical theory works with a simplified model that includes only what bears on the behaviour studied. The astronomer predicting an orbit needs only the sun's mass, the planet's distance, and its initial speed and direction (p. 45). Refinements add the planet's mass and other planets' pulls (p. 45).
- Models vary in accuracy. Planets can be treated as rigid bodies for orbits, but for very precise lunar motion the earth cannot be treated as rigid, because of the tides (p. 46). Real circuit components only approximate the properties of the ideal inductors, capacitors and resistors of network theory; sometimes the difference can be disregarded, sometimes not (p. 46). A model may even be crude or invalid: the "economic man" of early economic theory has fallen into disfavor (p. 46).
- Planets, networks and economic man are deterministic. A gamble makes the economic man's fate partly unpredictable (p. 46).
- A model for pure chance is possible. Drawing 3 balls from a half-white, half-black container gives, after many trials, all white about 1/8 of the time, two white one black 3/8, two black one white 3/8, and all black 1/8 (p. 47). (The text layer garbles these fractions; the values are what the equal-odds model gives, our check.) The model also says how much deviation to expect (p. 47).
- Human behaviour is neither fully determined nor simply random. A deterministic model "will not get us far", while a statistical one might (p. 47). Actuarial tables predict group death rates, not individual deaths (p. 47).

*Intuition note:* A good model throws away detail on purpose. For human communication, Pierce thinks a statistical model might work where a deterministic one will not, because letter frequencies are very nearly constant, even for single writers.

### Regularity of letters (pp. 47–48)
- Answering the objection that tables concern groups only, Pierce says E makes up about 0.13 of English letters and W about 0.02. Almost the same proportions appear in the writing of any one person (p. 47).
- This habit does not bind anyone. Burmann wrote 130 poems (20,000 words) without R (p. 48). Alcala y Herrera suppressed a different vowel in each of five stories (p. 48). Wright's 1939 novel *Gadsby* (267 pages) has no E (p. 48). Ordinarily we keep to about 0.13 E "with almost the consistency of a machine" (p. 48).
- Pierce says one cannot argue from this that a machine with such habits could write English, but Shannon showed English can be approximated by a machine-executable process (pp. 48–49).

### Shannon's approximations (pp. 49–54)
- **Zero order.** Draw from a hat with equal numbers of cards for each of 26 letters and the space, replacing each card. Symbols are independent and equiprobable. The result has too many Z and W and too few E and spaces (p. 49). Example 1 is "XFOML RXKHRJFFJTUJ …" (p. 49).
- **First order.** Symbols are independent but follow English frequencies, e.g. 13 of every 100 cards E and 2 W (p. 49). Example 2 begins "OCRO HLI RGWR …" (p. 49).
- **Digram probabilities.** The probability of TH is .037, of OR .010, of WE .006. QU is not 0 but too small to be listed in the tables Pierce consulted, and QX and QZ are essentially zero (p. 49). Meaning: with 10,001 letters there are 10,000 successive pairs. If TH occurs 370 times, the probability is 370/10,000 = .037 (p. 50).
- Use 27 hats, one for digrams beginning with each letter and one for those beginning with a space. Of 1,000 digrams, 37 are TH and 10 are WE (p. 50). The T hat holds as many digrams as there are T's, so $p(T)=.10$. Also $p(T,H)=.037$ (p. 50). Of the 100 T-digrams (out of 1,000), 37 are TH:
$$p_T(H)=\frac{37}{100}=.37$$
the **conditional probability** that the letter after a T is H (p. 51).
- **Generating second-order text.** Draw a first digram at random and write its letters. Then draw the next digram from the hat named by the previous digram's second letter, and write only its second letter. Repeat. The space is treated as a letter (p. 51). Example 3 (second order) results (p. 51).
- **Third order** uses trigram probabilities (p. 51), giving example 4 (p. 51). The resemblance to English grows from example 1 to 4: no wordlike combinations; OCRO and NAH somewhat resemble English words; all "words" pronounceable; eight English words (pp. 51–52). Guilbaud made a similar third-order Latin passage (p. 52).
- Given enough statistics and a random-choice ability, a machine could produce close approximations of text. More complete information gives a closer resemblance (p. 52). If the machine chooses groups of three letters by their probability, any three-letter combination it produces must be an English word or part of one, and any two-letter "word" must be an English word. It is still "less inhibited" than a person, who ordinarily misses writing PONDENOME or GROCID (p. 52). Using words instead of letters is simpler than lengthening the letter groups (pp. 52–53).
- **Word approximations.** First order: words drawn independently with English frequencies (example 5) (p. 53). Second order: no tables of word-pair probabilities exist, so Shannon picked a word pair at random in a novel, found the next occurrence of its second word, and appended the word that followed it, and so on (example 6) (p. 53). Several-word stretches resemble English (p. 53).
- Pierce's conclusion: letters, letter groups, words and word pairs occur with nearly constant frequency in English. A random process, possibly carried out by a machine, can reproduce those statistics (p. 54).

*Intuition note:* First order draws symbols independently with English frequencies. From second order on, the draw depends on the symbol before it (third order uses trigram statistics). Conditional probability is the rule for that dependence: look at the last symbol to choose the next.

### Limits of statistics, and the finite-state machine (pp. 54–56)
- Such a scheme, even if refined greatly, would not produce all sequences of words a person might utter; carried to an extreme it would be confined to combinations that have occurred, since there would be no data on others. Yet "The magenta typhoon whirled and farded bishop away" may never have been said (p. 54). The real rules involve classes of words and their association, that is, grammar. Linguists and engineers who try to make translating machines must find these rules (p. 54).
- Pierce describes a "machine" (Fig. III-1, p. 55; the page is an image with no text layer here) with finitely many numbered boxes (states). Each box has two outgoing arrows, each labelled 1/2. Flipping a coin chooses the arrow (heads: top, tails: bottom). On entering a state, the machine prints that box's word(s), then flips again (p. 54). It is a **finite-state machine** (p. 54).
- Example: starting in state 7, the flips T H H H T T H T T T H H H H (as printed) yield "THE COMMUNIST PARTY INVESTIGATED THE CONGRESS. THE COMMUNIST PARTY PURGED THE CONGRESS AND DESTROYED THE COMMUNIST PARTY AND FOUND EVIDENCE OF THE CONGRESS." (p. 56). This can go on and on, never retracing its whole course, producing "sentences" of unlimited length (p. 56).
- Both random choice from probability tables and a finite-state machine with random transitions are called **stochastic processes**, because of the random element (p. 56).
- The model wanted for a text source must produce text close enough to English that encoding and transmitting it is essentially the same problem as for real English. It must be defined so that useful theorems can be proved. It need not match real text with exactness (p. 56).

### Stationary and ergodic sources (pp. 57–60)
- Shannon's model is the **ergodic source**. First, **stationary** (pp. 56–57). "AEAEAEAE…" is stationary, since later is like earlier. "AEAAEEAAAEEE…" (runs growing forever) is not (p. 57). Sources with independent letters, digrams or trigrams are stationary (p. 57); Pierce cites them as examples 1–3, although by the numbering on pp. 49–51 they are examples 2–4.
- A difficulty: in a digram source, how it starts affects the early statistics (start on Q and the next letter must be U) (p. 57). Fix: imagine the source started infinitely many times, giving an **ensemble** of sequences, with starting letters assigned probabilities, e.g. 0.13 start with E, 0.02 with W (pp. 57–58).
- With starting letters assigned in this way, the fraction of E's at position 1, 2, 3 … over the ensemble is the same. The same holds for TH or WE among the first, second, … pairs (p. 58).
- **Definition (stationary):** if starting-condition probabilities can be chosen so that any statistic averaged over the ensemble does not depend on the distance from the start, the source is stationary (p. 58).
- An **ensemble average** is over all characters at one position across the ensemble. A **time average** lumps together all characters in one sequence (p. 58). They can differ.
- Example (p. 58): start with A (1/3), B (1/3) or E (1/3). The sequences are ABAB…, BABA…, EEEE…. This is stationary (p. 59). Table V compares time averages for each sequence with the ensemble average. Its body is empty in the text layer (p. 59).
- **Definition (ergodic):** a stationary source for which every possible ensemble average (letters, digrams, trigrams, …) equals the corresponding time average (p. 59). The later theorems are proved for ergodic sources (p. 59). Footnote: some work exists on nonstationary sources, not discussed here (p. 59). Continuous sources (speech waves, telephone currents) are also assumed ergodic (p. 59).

*Intuition note:* Stationary means the source's habits do not drift. Ergodic adds that one long message is representative of all messages the source could produce.

### Why ergodic? (pp. 59–61)
- In an ergodic source, statistics such as the frequency of E or TH do not vary along the message. A longer stretch gives better estimates of the source's probabilities (p. 59).
- Because time and ensemble averages agree, what is learned from one message applies to all messages from the source (pp. 59–60).
- An ergodic source is simple, and simple processes are easier mathematically, but it would not interest communication theory unless also reasonably realistic (p. 60).
- The theory has an exact side, dealing with hypothetical ergodic sources and infinite ensembles. A human cannot produce even one infinite sequence. But many long sequences are produced collectively, e.g. teletypewriter messages (p. 60).
- Americans writing telegrams, or speaking over telephones, are treated as approximately an ergodic source (p. 60). Men writing French plus men writing English could not be ergodic: the ensemble average would resemble neither language's time averages (p. 60).
- Pierce does not assert that all English writers form a strictly ergodic source. Statistics shift with subject and purpose, and speakers differ in loudness. He does assert remarkable uniformity in many statistics. Speech and writing as ergodic sources are "not quite true to the real world", but far truer than the economic man, and true enough to be useful (p. 61).
- Caution is needed. Mathematics says three exact points fix a circle's diameter, but nobody would measure a fuzzy real circle by three points a thousandth of an inch apart. One would measure the diameter directly (p. 61).

### Philosophical remarks (pp. 61–62)
- Using a random model does not imply that man acts at random. Perhaps with enough knowledge his next word could always be predicted (p. 61).
- In communication theory we assume that our only knowledge of the source comes from its messages or perhaps from some less-than-complete study of man. This knowledge narrows the probabilities, but uncertainty remains. For us, with incomplete knowledge, the source behaves as if certain choices were random, insofar as we cannot predict them. If we could predict them, we should build that knowledge into the statistics (pp. 61–62). With more knowledge we might see the choices are not really random (p. 62).
- Finite-state machines can also have inputs that determine or influence transitions, as a computer's program and data do (p. 62). Man may be a finite-state machine, with states of the nervous system as "states of mind", senses as inputs, and letters, words or actions as outputs (p. 62). The number of states would be fantastic. Yet a gas's configurations are also beyond detailed treatment, and pressure and temperature explain much of its behaviour (p. 62). Pierce asks whether we can say valid, simple and important things about the mind producing text. He notes we can already predict a good deal about the statistical nature of what a man writes, unless he deliberately behaves eccentrically (p. 62).

### Summary (pp. 62–63)
- Frequencies of letters, pairs, triplets and words are nearly constant (p. 63). Stochastic processes, including finite-state machines, can produce close approximations to English (p. 63).
- The chosen model is the ergodic source: an imagined machine producing an ensemble of infinite sequences whose statistics, roughly, do not change with time (stationary), and with one message's statistics valid for all messages (p. 63).
- Theorems are exact for truly ergodic sources. All English writers together constitute an approximately ergodic source. The model is close enough to be very useful, but results must be applied with care (p. 63).

## Toy example (ours, not from the text)
**Digram source on letters A, B.** Let $p(A,A)=\tfrac12$, $p(A,B)=\tfrac16$, $p(B,A)=\tfrac16$, $p(B,B)=\tfrac16$. The sum is $\tfrac{3+1+1+1}{6}=1$.
- Digrams beginning with A: $p(A)=\tfrac12+\tfrac16=\tfrac23$. Ending with A: $\tfrac12+\tfrac16=\tfrac23$, the same, as Pierce notes for T (p. 50). Then $p(B)=\tfrac13$.
- Conditional probabilities (as $p_T(H)=.37$): $p_A(A)=\tfrac{1/2}{2/3}=\tfrac34$, $p_A(B)=\tfrac{1/6}{2/3}=\tfrac14$, $p_B(A)=\tfrac{1/6}{1/3}=\tfrac12$, $p_B(B)=\tfrac12$.
- Hats, using 12 digrams: AA ×6, AB ×2, BA ×2, BB ×2. Hat A holds 8 (6 AA, 2 AB). Hat B holds 4 (2 BA, 2 BB). Hat A gives $6/8=\tfrac34$ AA, matching.
- Procedure (p. 51): draw first digram, say AB, so write A B. Next draw from hat B, say BA, and write A. The text so far is ABA. Next draw from hat A, and so on.

**Stationary but not ergodic (the author's ABAB/BABA/EEEE source, p. 58).** Time average of A: sequence 1 has $\tfrac12$, sequence 2 has $\tfrac12$, sequence 3 has 0. Ensemble average of A: at position 1 the letters are A, B, E, each with probability $\tfrac13$, so A has $\tfrac13$. At position 2 they are B, A, E, so again $\tfrac13$ (and likewise at every position, since the sequences alternate), which fits stationarity. The ensemble average $\tfrac13$ differs from every time average ($\tfrac12,\tfrac12,0$), so it is not ergodic by the definition (p. 59). (Our computation; the printed Table V body is not legible in the text layer.)

## Concepts
- [[stochastic-process]] (new) — a process with a random element that produces sequences with given statistics (p. 56)
- [[conditional-probability]] (new) — probability of one symbol given the previous one, $p_T(H)=.37$ (p. 51)
- [[n-th-order-approximation]] (new) — text generated using n-symbol (or word-pair) statistics of English (pp. 49–53)
- [[finite-state-machine]] (new) — machine with finitely many states, moving between them by random transitions (p. 54) or input-driven transitions (p. 62)
- [[stationary-source]] (new) — source whose ensemble statistics do not depend on distance from the start (p. 58)
- [[ergodic-source]] (new) — stationary source where every ensemble average equals the time average (p. 59)
- [[ensemble-vs-time-average]] (new) — average across many sequences at a position vs along one sequence (p. 58)

## Canonical instances
- [[shannon-text-approximations]] — zero- to third-order letter and first- and second-order word approximations of English (pp. 49–53)
- [[letter-e-frequency]] — E at about 0.13, W about 0.02, stable across writers (p. 47)
- [[lipogram-gadsby]] — Gadsby, Burmann and others break the letter habits (p. 48)
- [[finite-state-machine-fig-iii-1]] — coin-driven machine producing "COMMUNIST PARTY" sentences (pp. 54–56)
- [[abab-baba-eeee-source]] — stationary source whose time averages differ from its ensemble average (p. 58)
- [[circle-diameter-caution]] — warning about applying exact theory to inexact cases (p. 61)

## Bridges (candidates)
- [structural-analogy] second-order letter/word approximation ↔ language modelling: predict the next token from the previous one (the text shows only the generating side)
- [same-math] finite-state machine with coin-flip transitions ↔ probability: Markov chain with given transition probabilities (here, 1/2 per arrow)
- [metaphor] man as a possible finite-state machine with a fantastic number of states, beside a gas whose many molecular configurations are summarised by pressure and temperature ↔ statistical physics: summarising many micro-states by a few variables (p. 62)

## Questions this raises
- How can the "amount of uncertainty" in each Shannon approximation be measured, so we can say how much each order reduces it?
- If real writers are only approximately ergodic, how good is the approximation for the theorems to hold?
- How can a model combine grammar with probabilities, so it can produce sentences that never occurred before?
- What would the probability statistics of a non-ergodic source (for example a mix of English and French) look like when we encode it?

## Reading notes
- Printed page = pdf page − 16 (pdf 61 = p. 45).
- The PDF is the 1961 Harper & Brothers first edition (*Symbols, Signals and Noise*), not the 1980 Dover edition named in the work citation, so pagination may differ from the Dover edition.
- In the text layer provided, page 55 (Fig. III-1) has no text, so the figure's boxes and words are not reproduced here. Pierce's example numbering on p. 57 (examples 1–3 for first-order, digram and trigram sources) is off by one against pp. 49–51. Only the printed output (p. 56) is available.
- Table V (p. 59): headings are present but the numerical body is empty in the text layer. The values in the Toy example are our own calculation, not copied.
- The text layer garbles fractions on p. 47 (e.g. "% of the time"). I give the values from the equal-odds model (1/8, 3/8, 3/8, 1/8) as our check. The text layer also garbles probability notation on pp. 50–51 (e.g. "XT)" for $p(T)$, "^r(H)" for $p_T(H)$). The values .10, .037 and .37 are read from the numbers in the text.
- The unit has no exercises.
