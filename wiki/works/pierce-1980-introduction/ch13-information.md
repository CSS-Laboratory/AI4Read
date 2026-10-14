---
id: pierce-1980-introduction/ch13-information
work: pierce-1980-introduction
unit: "13 Information Theory and Art"
pages: 250-267
fields: [information-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Information Theory and Art

## L0 — One line
Pierce argues that art needs both order and surprise: pure randomness has the highest possible information rate, but listeners cannot tell one random thing from another, so art must be built from a learned "language" and keep its variety within human limits.

## L1 — The gist (≤ 120 words)
The chapter asks what information theory can say about art. Pierce thinks it offers very little of serious value beyond a point of view (p. 253). A composer could in principle choose 300,000 bits per second, but humans handle far fewer (p. 250–251). Random sound, text or dots are mathematically the most unpredictable, yet they look or sound alike to us. Art becomes distinctive only when it uses a familiar language (style, grammar) and releases variety slowly. Pierce supports this with dice music, Slepian's human-chain music, Hiller and Isaacson's computer music, random text and Julesz's random dots. A language of intelligible words and relations is necessary in art but not sufficient: mechanical sameness is dull (p. 267).

**Prerequisites:** bit, entropy as "variety/choice per symbol", redundancy; digram probabilities (Ch. III); sampling a waveform.

## L2 — Key ideas (5–10 bullets)
- A waveform can be written as 30,000 samples per second, each of about ten bits. A composer then has 300,000 bits per second of freedom, which is mostly wasted (p. 250–251).
- The fastest demonstrated human information rate (reading word lists) is no more than 40 bits per second, and appreciation may be even lower. White Gaussian noise is the most unpredictable sound, yet all of it sounds alike and dull (p. 251).
- To be recognised as new, something must be distinguishable from the old, so it must be partly familiar. Unfamiliar styles sound monotonous (p. 251).
- A composer keeps variety within human limits by using familiar units ("musical words"), expected order, sparing novelty and repetition in altered forms (p. 252).
- Knowing a style's "language" takes years of practice. To the untutored ear, rule-governed music seems to show free choice and variety, so its complexity overwhelms (p. 254).
- Random processes combined with rules produce music and text that hang together locally (dice waltzes, Slepian's experiment, Hiller–Isaacson), but they wander over the long range. Long-range order must relate parts, not just notes (p. 255–260).
- Random text can be amusing, but it cannot supply knowledge (p. 261–264).
- Julesz's dots show that removing some randomness improves a pattern. Pierce's minimum philosophy of art: it needs intelligible language, some surprise, and a sense of authorship (p. 265–267).

## L3 — Walkthrough

### Opening: composition as numbers (p. 250–251)
- A visiting composer said that whole compositions can be reduced to a series of numbers. Pierce notes that this is old news: pulse code modulation represents any wave as a sequence of sample amplitudes (p. 250).
- For high-quality music with a bandwidth of 15,000 cycles per second, one needs 30,000 samples per second. Each needs accuracy of about one part in a thousand, i.e. three decimal digits or about ten binary digits (p. 250).
- A composer specifying this freely could choose among twenty-minute compositions numbering "1 followed by 108 million 0's". His choice rate would be 300,000 bits per second (p. 250).
- Check (added step): $30{,}000 \times 10 = 300{,}000$ bits/s. Twenty minutes is 1200 s, so $3 \times 30{,}000 \times 1200 = 108{,}000{,}000$ decimal digits.
- Pierce points to the fastest demonstrated human rate, reading word lists, which is no more than 40 bits per second. He calls this scarcely more than a ten-thousandth of the composer's rate (p. 250–251).
- Pierce says that perhaps humans can appreciate information only at an even lower rate. An actor's speech is highly redundant English at moderate speed (p. 251).
- The freedom lets him produce a host of "compositions" that would sound indistinguishable and uninteresting to any human listener (p. 251).
- White Gaussian noise contains all frequencies equally. Mathematically it is the least predictable and most "original" sound, yet to a human all of it sounds alike: dull and monotonous (p. 251).
- To call something new we must distinguish it from the old, so sounds must be familiar to a degree. Analogies: we tell friends apart but find less that is distinctive in strangers. Listeners attached to one era's composers may find other eras' music alike (p. 251).

> **Intuition note.** The most random signal is not the most interesting one to us. We can only enjoy differences we have learned to notice, and Pierce says variety must be released at only a very few bits per second if we are to recognise it.

### The composer's answer (p. 252–253)
- A composer wants to be both free and recognisable. If listeners cannot tell his pieces apart, or from a whole school's, they will not buy many recordings (p. 252).
- Pierce's claim: a composer can make compositions distinctive "Only by keeping their entropy … within the bounds of human ability to make distinctions". Only when he doles variety out at a very few bits per second can he expect an audience to recognise and appreciate it (p. 252).
- This does not mean slow random notes. The composer builds from larger units that listeners already know. The order makes the next event partly expected. Surprises and new material are used sparingly, then repeated in altered forms (p. 252).
- Analogy with language: musical "words" (chords, scales, themes, ornaments) in grammatical order, with much repetition (p. 252).
- Pierce says none of this is new. He sees it as pertinent because artists face tempting technical resources (p. 252–253).
- Example: M. V. Mathews had a computer produce notes from punched cards, one card per note (wave form, duration, pitch, loudness). His rapid, almost unplayable rhythms "sounded, simply, chaotic" (p. 253).
- Varèse can evoke form by patching recorded sounds (musique concrète). Even so, abandoning traditional resources brings difficulty (p. 253).
- Pierce lists the composer's options: simplify, educate the audience, or remain unintelligible and await posterity. Perhaps there are other alternatives, certainly if the composer has real genius (p. 253).
- Pierce thinks information theory has very little of serious value to offer apart from a point of view, though he believes that point of view may be worth exploring (p. 253).

### Language as a model (p. 253–255)
- Language has a vocabulary and grammatical rules. Only the element of choice contributes to information per word; Shannon estimated 3.3–7.2 bits per word. Pierce says it must also be this choice that lets a writer convey meaning (p. 253–254).
- A frequent, attentive listener plausibly has a large unformulated knowledge of musical elements and their relations. He need not be able to state the rules, nor even to write music by them, any more than a mute who understands speech can speak (p. 254).
- Pierce calls such knowledge of a style knowing the language of music. It is acquired through years of practice, whatever the rules owe to physical laws (p. 254).
- Without it, rule-governed music sounds like a choice from all possible sounds, so its complexity overwhelms the listener (p. 254).
- Sense can survive rule-breaking (*me heap big injun*). Nonsense can obey grammar (*the alabaster word spoke silently to the purple*). Pierce goes on to the second case (p. 254–255).

### Random music (p. 255–261)
- **Dice music.** Mozart left numbered bars and rules (Köchel 294D). Throwing dice to choose bars lets an amateur compose waltzes that sound like "somewhat disorganized Mozart". Haydn, Stadler and C. P. E. Bach are said to have done similar things; John Cage used random processes (p. 255).
- **Shannon–Pierce rondos (1949).** M. E. Shannon and Pierce made a catalog of chords (only root-I chords listed; others derived by rules) and used three special dice plus random-number tables (p. 255–256).
  - The only chord-connection rule: succeeding chords share a common tone in the same voice. This let other voices jump wildly. Pierce likens it to a simple, consistent but incorrect digram probability in synthetic text (p. 256).
  - Long-range structure: eight measures of four quarter notes. Measures 5 and 6 repeat 1 and 2, while 3 and 4 differ from 7 and 8, making a primitive rondo. Chords 1, 16, 32 have root I, and chords 15 and 31 root IV or V, for a cadence effect (p. 256).
  - The results resemble hymns (Fig. XIII-2). They are clearly all by the same composer, yet recognisable as different after a few hearings. Pierce has grown fond of them (p. 256).
- **Slepian (1951).** Musically untrained mathematicians were shown a quarter bar, half bar or three half bars. Each added a sensible succeeding half bar, then the next subject saw a window including that addition. Subjects were told the intended style (p. 256).
  - Fig. XIII-3 shows a chorale (each half bar based on the preceding half bar) and a "romantic composition" (based on the preceding three half bars). Pierce finds it surprising that they hang together, despite inadmissible chords, and that the styles are distinct (p. 257–258).
  - His comment: the experiment shows human flexibility and fallibility. "True stochastic processes are apt to be more consistent but duller" (p. 258).
- **Computer statistics.** Pierce has "no doubt" that a computer given statistics of a composer's style could produce music resembling it (p. 258).
  - Pinkerton (1956) chose each note by its probability given the preceding note and its position in the bar. With nursery-tune probabilities he found an entropy of 2.8 bits per note. Pierce is "sure" this is quite a bit too high, since only digram probabilities were used (p. 258–259).
  - Pinkerton also gave a finite-state machine for banal tunes. Brooks, Hopkins, Neumann and Wright (1957) used a statistical study of hymn tunes. Burroughs (1956) and Klein and Bolitho (1957) reported computer-made music, including "Push Button Bertha" (p. 259).
- **Hiller and Isaacson.** They stated the rules of four-part, first-species counterpoint so that a computer chose notes randomly and rejected rule-breakers (p. 259).
  - Except at the cadence, the rules link only three successive notes, so the music tends to wander. Over a short range it sounds "surprisingly good" (p. 259).
  - They also generated rhythm and dynamics, and "Markoff-chain" music from probability tables (derived from overtones or harmonics). All this was published as the *Illiac Suite*: good local structure, weak and wandering as a whole (p. 259).
  - Pierce suggests that deterministic repetition (as in a rondo) or a Chomsky-type grammar might help. He concludes it is foolish to seek long-range structure by relating notes to preceding notes by digram, trigram or higher probabilities. The relation must be "among parts of the composition, not simply among notes" (p. 260).
- Pierce says Hiller and Isaacson show conclusively that computers can take over many musical chores. A composer might guide the main pattern and let the computer fill in harmony and counterpoint, or test new rules (p. 260–261).
- Pierce calls the idea of machines that learn what we like nonsense in our day, and probably to remain so for a long time (p. 261).

> **Intuition note.** A chain of "what follows what" rules gives believable short stretches but forgets where it is going. Large-scale shape needs rules about sections (repeats, cadences), not just rules about neighbouring notes.

### Random text (p. 261–264)
- The word frame shown to Captain Gulliver by a professor at the Grand Academy of Lagoda is, Pierce says, just the wrong application of a stochastic process, since random output gives no knowledge (p. 261).
- Shannon's letter-digram and trigram approximations (Ch. III) produce interesting "words" such as deamy, ilonasive, grocid and pondenome. Pierce reads pleasant or unpleasant tones into them (p. 261).
- Pierce finds Shannon's second-order word approximation disquieting: it seems to put an English writer in peril, but he cannot help because the latter part is garbled (p. 262).
- **Pierce's word-chain game:** each friend saw the last three words and added a fourth. After twenty friends, a seeming order of meaning persisted over groups of far more than four words, but the text wandered. Pierce attributes this to the absence of any long-range persistent purpose or meaning. He compares it to some schizophrenic utterances and to Uncle Anselmo in Hudson's *The Purple Land* (p. 262).
- A title adds some long-range order. In Dunn's examples each person saw one preceding word plus the title ("Men and Women"). In Bell Laboratories examples each saw three preceding words plus the title ("About Life", "Engineers", "Housecleaning", "Murder Story") (p. 262–263).
- Pierce finds this material amusing, with some admiration. He would never write "one frosty look of trees waving gracefully against the wall". In some sense a stochastic process can do better, since it at least has a chance of a good line, whereas poor poets are held by mediocrity to rhyming love with dove (p. 263–264).
- He thinks a computer might produce fresh "words" and amusing short passages, but a detective-novel machine is "very far away" (p. 264).

### Visual art (p. 264–266)
- A completely random visual pattern is, like random sound, mathematically the least predictable. It is also the dullest, since one random pattern looks like another. Fig. XIII-5 is an array of 10,000 randomly black or white dots (p. 264).
- **Julesz's procedure** (for studying stereoscopic vision and pattern): the computer examined sets of five points at the tips and centre of an X (Fig. XIII-6). If the centre point was the same colour as points 1 and 4, or as points 2 and 3, it was changed. This tends to remove black or white diagonals, except where 1 and 4 are black and 2 and 3 white, or vice versa (p. 265).
- This profoundly improves the pattern's appearance (Fig. XIII-7). An unpredictable component is desirable for variety or surprise, but some orderliness is necessary for pleasing patterns (p. 265).
- The mix of order and randomness is old in art: the kaleidoscope (sixfold symmetry on random glass), Duchamp's dropped threads, Tinguely's partly ordered, partly random designs (p. 265–266).

### Pierce's minimum philosophy of art (p. 266–267)
- It says nothing about the talent or genius that makes art worthwhile. Pierce does not blame information theory for it (p. 266).
- Appreciation depends on the audience: a closed mind leaves one cold, a wish to appreciate can make one like poor work. Pierce likes the hymn-like pieces he made, and fashions can win sincere but short-lived appreciation (p. 266–267).
- Audiences want a sense of authorship, so a work must be consistent enough to be recognisable as its artist's. An artist who produced all the great styles in succession would astonish us, but we could scarcely appreciate him as an artist. Pierce finds Picasso recognisable but disquieting, Matisse easier to appreciate (p. 267).
- To be appreciated, art must be intelligible to the audience and, to a degree, in a language familiar to it. Ten jokes in Chinese are no more amusing than one to most Americans. We can be surprised repeatedly "only by contrast with that which is familiar, not by chaos" (p. 267).
- Some artists use a language taught by earlier masters (Brahms); others teach a new one (the impressionists). Bach and Handel are no less original for speaking a language of the past (p. 267).
- A language with intelligible words and relations is "necessary in art" but "not sufficient": mechanical sameness is dull. Pierce prefers stochastic prose's surprises to the verses of Owen Meredith (p. 267).

> **Intuition note.** Familiarity makes surprise visible, but too much familiarity is boring. Pierce's advice is a learned shared language plus a little surprise from time to time.

## Toy example (ours, not from the text)
Suppose a composer writes eight measures and each measure is one of 8 equally likely patterns. Free choice for each measure is $\log_2 8 = 3$ bits. Eight measures give $8 \times 3 = 24$ bits.

Now impose Pierce's rondo rule: measures 5 and 6 repeat 1 and 2. Only measures 1, 2, 3, 4, 7, 8 are free. The choice is $6 \times 3 = 18$ bits. The six saved bits are redundancy, and they are what a listener can use to recognise the repeat and feel oriented.

For rate: at 2 measures per second, free choice means 6 bits/s. For comparison, the sample-level freedom in the text is 300,000 bits/s, about $300{,}000 / 6 = 50{,}000$ times higher. Only the low-rate, structured choice is within the human range Pierce discusses.

## Concepts
- [[bit]] — unit used to measure a composer's or speaker's choice, e.g. 300,000 bits/s of sample freedom (p. 250)
- [[entropy-H-X]] — here "variety/information rate" of a work, which must stay within human limits to be distinctive (p. 252)
- [[redundancy]] — repetition and rule-governed structure that make the next event partly expected (p. 251–252)
- [[entropy-rate]] — Pierce quotes Shannon's 3.3–7.2 bits per word and Pinkerton's 2.8 bits per note, which Pierce thinks is too high (p. 254, 259)
- [[pulse-code-modulation-sampling]] (new) — representing a wave by 30,000 samples per second of about ten bits each (p. 250)
- [[human-information-rate-limit]] (new) — demonstrated human rate of at most 40 bits/s, possibly lower in appreciation (p. 250–251)
- [[musical-language-as-learned-constraint]] (new) — style as vocabulary plus rules, learned over years. Only the remaining choice carries information (p. 254)
- [[stochastic-composition]] (new) — generating music or text by random choices under rules or probabilities (p. 255–260)
- [[digram-probability-model]] (new) — choosing an item given the preceding item. Pierce says it fails for long-range structure (p. 256, 260)

## Canonical instances
- [[white-gaussian-noise-as-dull]] — maximally unpredictable yet sounds alike to humans (p. 251)
- [[mozart-dice-waltz]] — dice-chosen bars (K. 294D) giving "disorganized Mozart" (p. 255)
- [[shannon-pierce-random-hymns]] — dice chords with common-tone rule and rondo structure (p. 255–256)
- [[slepian-human-chain-music]] — subjects add half bars; chorale vs "romantic" (p. 256–258)
- [[hiller-isaacson-illiac-suite]] — counterpoint rules plus random choice plus Markoff-chain music (p. 259–260)
- [[pierce-word-chain-text]] — friends add words; a title adds order (p. 262–263)
- [[julesz-random-dot-patterns]] — 10,000 dots, partial de-randomisation improves look (p. 264–265)

## Bridges (candidates)
- [structural-analogy] Pierce's "language that the listener knows" ↔ uniform information density / efficient communication: an audience can take in only a small variety rate, so signals are paced and predictable.
- [structural-analogy] Digram- and trigram-based generation of music ↔ n-gram language models: generating from short-context probabilities gives locally plausible but globally wandering output.
- [metaphor] Random pattern: maximum entropy yet perceptually uniform ↔ typical set: the details are information-rich but irrelevant to the observer.

## Questions this raises
- If appreciation depends on familiarity, can an audience's bit rate rise with training? Is the limit fixed or learned?
- Can long-range structure (repeats, sections) be put into a statistical model, and how would one measure its entropy per note?
- Pierce thinks information theory gives little beyond a point of view. Could one measure style or authorship numerically, e.g. entropy per note of a composer?
- Is "most unpredictable, therefore least interesting" a statement about the signal or about the observer's model of it?

## Reading notes
- Printed page = pdf page − 16 (pdf 266 = printed 250). All page citations use printed numbers.
- The chapter heading is garbled in the text layer ("CHAPTER y"). The running page headers give the book title and the chapter title. The unit metadata warns that this scan is the 1961 Harper & Brothers first edition, not the 1980 Dover edition. Its note is truncated, so I could not read the rest.
- The text layer is garbled in places: the time signature of the Mozart waltz reads "% time" and I did not resolve it; the musical scores and dot arrays are not reproduced in the text layer. The layout of points 1–4 in Fig. XIII-6 is taken from the text layer's rendering of the figure.
- Spelling as printed: Lagoda, Markoff-chain, Tinguley, musique concrete. The wording of Julesz's rule (centre point the same as either points 1 and 4 or points 2 and 3) is ambiguous. I read it as the same as both points of one pair, which fits the stated effect on diagonals, but this is an interpretation.
- The chapter is not divided into numbered sections; headings above are mine.
