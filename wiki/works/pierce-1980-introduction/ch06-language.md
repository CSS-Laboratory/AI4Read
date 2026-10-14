---
id: pierce-1980-introduction/ch06-language
work: pierce-1980-introduction
unit: "6 Language and Meaning"
pages: 107-124
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
# Language and Meaning

## L0 — One line
Pierce offers, as openly labelled "informed ignorance", the idea that a grammar could show how much of English is choice, and suggests that meaning depends on intent, on lists of qualities tying words to the world, and on shared experience, none of which information theory has settled.

## L1 — The gist (≤ 120 words)
After the mathematics of source entropy, Pierce pauses to ask what information theory can say about language. A satisfactory grammar would separate mechanical rule-following from real choice, and the choices are what contribute to entropy. Pierce reports Chomsky's argument against word-by-word generation and sketches his kernel-sentence grammar. Meaning is harder. Pierce thinks it fair to treat language as an imperfect code; if so, meaning goes back to the user's intent. He believes words attach to the world through lists of qualities, not ideal examples. He also says meaning depends on the structure of the world and on shared experience, which makes translation hard. He closes by saying these ideas suggest views but do not establish them.

**Prerequisites:** entropy as average choice per symbol; Markov-style word approximations (Chapter III); the idea of a finite-state machine.

## L2 — Key ideas (5–10 bullets)
- Pierce labels the chapter "informed ignorance": speculation guided by science, to be kept apart from established fact (p. 108).
- A satisfactory grammar would generate all grammatical sentences and only those. It would let us re-estimate English entropy and transmit only the choices (pp. 109–110).
- Word-by-word generation faces a trade-off. Using more than four words of context favours grammar over completeness, and using fewer favours completeness over grammar (p. 111).
- Chomsky rejects finite-state models and proposes generation from a kernel sentence by optional and obligatory rules. Pierce notes that a bounded sentence length makes it finite-state again (pp. 112–115).
- Grammar is not meaning: a grammatical sentence can be odd. Word choice can also be guided by sound and by emotional association (pp. 110, 116–117).
- Pierce thinks it fair to regard meaningful language as an imperfect code; if so, meaning must ultimately refer back to the user's intent. Grammatical sentences also have what might be called a formal meaning, regardless of intent (p. 118).
- Pierce believes that words pick out classes of things via lists of qualities, not ideal patterns. Machine recognisers that use features did better than template matchers (pp. 119–121).
- Meaning depends on the structure of the world and on shared skills and experience, which makes exact translation hard. Understanding has an ability side and an emotional side (pp. 122–124).

## L3 — Walkthrough

### Opening (pp. 107–109)
- The two great triumphs of information theory are the bits needed to transmit a source's information and the error-free rate of a noisy channel (p. 107). Pierce chooses to pause and look at language instead of moving on to noisy channels (pp. 107–108).
- **Warning (author):** science has a hard core of known fact, and also "informed ignorance". This is speculation constrained by established fact, and laymen find it hard to tell from fact (p. 108). He says the chapter dabbles in such ignorance about language (p. 108).
- Scope: only grammatical English. Much spoken English appears agrammatical, for example *Me heap big chief* (p. 109).
- A complete grammar would have to express all the constraints on English text. What counts as grammatical is hazy and changes with time: "fear not" was allowed in the King James Bible, but we now say "do not fear" (p. 109).

### Grammar as a source of choices (pp. 109–111)
- A grammar should allow all grammatical utterances and only those. It should also let us tell features set by the rules from other features (pp. 109–110).
- With such rules, we could estimate English entropy anew, seeing which part is mechanical rule-following and which is choice, and so contributes to entropy (p. 110).
- We could also transmit as the message only data about the choices. At the receiver, a "grammar machine" could build sentences embodying them (p. 110).
- Grammar is not the whole of language. If a grammatical machine made its choices at random, it might perhaps produce *The chartreuse semiquaver skinned the feelings of the manifold*. A man presumably chooses differently if he says *The blue note flayed the emotions of the multitude*. The difference lies in the choices, not in the rules (p. 110).
- Higher-order word approximations can be made with people. Show someone three connected words, ask for a sentence containing them, and have them add the next word. Chained from person to person, this gave fourth-order strings (pp. 110–111). Pierce lists four, and one reads *When cooked asparagus has a delicious flavor suggesting apples* (p. 111). They are astonishingly grammatical given that rules were applied to only four words at a time. The fourth is "perhaps dubiously grammatical" (p. 111).
- Arithmetic: if Shannon is right that English text involves a choice of about 1 bit per symbol, then choosing among a group of 4 words could involve about 22 binary choices. Pierce writes this as a choice among some 10 million 4-word combinations (p. 111).
- A computer could use such a list, but the result would not be assuredly grammatical or complete. Some word sequences are fine in one sentence and not in another (p. 111).
- **Trade-off (author):** using more than four words favours grammar over completeness. Using fewer favours completeness over grammar. He adds that we can't have both (p. 111).
- **Finite-state idea (tentative, "perhaps"):** Pierce suggests that a sentence-producing machine might be in a particular state at each point and move to another state. He also suggests it might deal with word classes, such as singular nouns or verbs of various tense and number, so that it would produce grammatical structures into which words can be fitted (p. 111).

*Intuition note:* A satisfactory grammar would let us tell which parts of a sentence are forced by rules and which involve choice, and the choice part is what contributes to entropy. A procedure based only on the last few words faces a trade-off: it either admits some ungrammatical sentences or fails to produce some grammatical ones.

### Chomsky's view (pp. 112–115)
- **Mechanist's argument (reported):** a finite-state machine seems appealing because a mechanist would say man is one, having only finitely many cells or atoms (p. 112).
- **Chomsky's view:** he rejects the finite-state machine as a possible or proper model of grammar (p. 112).
  - Example of a rule no finite-state machine can follow: write random letters until Z appears, then repeat the letters since the previous Z in reverse order, and continue. The length between Z's is unbounded (p. 112).
  - Chomsky points out that English sentences have no limit on length. He argues that English sentences are organised so that this is enough to rule out a finite-state machine (p. 112).
- **Author's doubt:** Pierce asks whether a sentence "miles long" can really be called grammatical when no one has produced or could understand it. The rhetorical wording shows he doubts it (p. 112).
- Pierce thinks Chomsky's real criterion is this: a sentence is grammatical if the speaker, or perhaps the hearer, deems it so when it is said aloud naturally and thoughtfully (p. 112).
- Pierce says Chomsky offers persuasive evidence that it is wrong and cumbersome to choose each next word solely from the words already written (p. 112).
- **Chomsky's generation scheme (as Pierce sketches it):** start with a general form, a *kernel sentence*, for example noun phrase + verb phrase. Expand each part: noun phrase → article + noun → "the man"; verb phrase → verb + object → "hit the ball". Result: *The man hit the ball*. Other choices at the last stages could give *A girl caught a cat* (p. 113).
- Choice is not exercised left to right. An overall plan is chosen first. Then choice is exercised at each branch of the tree, down to particular words (p. 113).
- There are optional rules, which allow choice, and obligatory rules, which are purely mechanical. Irregular word forms come from obligatory rules (p. 113).
- Pierce says his account is very incomplete and sketchy. To understand the approach further and to judge its merit, one must refer to Chomsky's *Syntactic Structures* (1957) and the references it gives (p. 113).
- **Ambiguity:**
  - *The lady scientist made the robot fast while she ate* has at least four meanings, allowing for the vernacular, according to its author, a learned information theorist; Pierce thinks it perhaps too complicated for detailed analysis (pp. 113–114).
  - Ambiguity can be lexical, as in "he was mad" (angry or insane) (p. 114).
  - Ambiguity can also be grammatical. In *the shooting of the hunters*, the hunters may be subject, as in *the growling of lions*, or object, as in *the growing of flowers* (p. 114).
  - *The picture was painted by a real artist* and *The picture was painted by a new technique* seem to match word for word grammatically. Only the first could have arisen as a transformation of *a real artist painted the picture*. Chomsky points out that different transformations of different kernel sentences can lead to the same grammatical elements; when the words as well as the grammatical elements are the same, the sentence is ambiguous (p. 114).
- The boundary between grammar and meaning is unclear. Pierce asks whether grammar should allow adjectives but not adverbs to modify nouns, which allows "colorless green", or should forbid some adjective–noun and noun–verb pairings. With the first choice, certain constructions are grammatical but meaningless; with the second, they are ungrammatical (p. 114).
- Chomsky's processes cannot be run by a finite-state machine, but can be run by a Turing machine: a finite-state machine plus an infinitely long tape (p. 114).
- If sentence length is bounded, even at 1 million words, Chomsky's grammar corresponds to a finite-state machine. Pierce thinks such a limit is reasonable in practice (p. 115).
- How to derive an entropy for a source following such a grammar is left to the mathematically skilled information theorist (p. 115).
- **Author's priorities:** a workable grammar, possibly incomplete, that matches how humans produce English and is simple enough for a computer. He believes computers must be used on the structure and statistics of English text (p. 115).
- **Others' view (reported):** some feel Chomsky's picture of sentence generation should be modified or narrowed if it is to describe actual generation by human beings (p. 115).
- **Author's impression:** subjectively, in speaking or listening, one has a strong impression that sentences are generated largely from beginning to end, and that the speaker elaborates the pattern as he goes along rather than holding a very elaborate one at any time (p. 115).
- **Author's suspicion:** Pierce suspects that studies of grammars and of the statistics of their use will in the not distant future tell us many new things about language and about men (p. 115).

*Intuition note:* In Chomsky's scheme as Pierce sketches it, the shape of the whole sentence is chosen first and then filled in, so the choices form a tree rather than a chain of next-word choices. Pierce adds that if sentence length is bounded, the grammar corresponds to a finite-state machine, and he calls such a bound very reasonable in practice.

### Words, sound, emotion (pp. 115–117)
- A grammar must divide words into classes by the places where they can appear in grammatical structures; linguists do this on grammatical function alone, without invoking meaning. So all we can expect of a grammar is grammatical sentences, including the "chartreuse semiquaver" example (p. 116).
- Pierce asks what influences word choice when a live human speaker, not a machine choosing at random, follows the grammar. He says this is not to be answered by a vague appeal to meaning. He says Bishop Berkeley's eighteenth-century writing on language is so sensible that one can scarcely comment reasonably without owing him credit (p. 116).
- A poet of the scanning, rhyming school chooses many words for rhythm, rhyme, alliteration and sound value, notably in Poe's "The Bells", "Ulalume" and "The Raven". The two sections of "The Bells" contrast tinkling with ringing and liquid sound (pp. 116–117). Blake's two lines beginning "Tyger, Tyger" can be moving without even the trivial literal meaning of Poe's verse (p. 117).
- Outside poetry, words may be chosen for euphony but are perhaps more often chosen for associations that excite passions such as those Berkeley lists: fear, love, hatred, admiration and disdain. Examples are hymns, epithets and dirty jokes (p. 117).
- **Author's addition:** Berkeley omits a sense of understanding. Familiar phrases applied to ill-understood matters may give a feeling of insight. Some common-word philosophy may be better seen as reassurance about man's feelings than as meaning (p. 117).

### Meaning as intent (pp. 117–118)
- Whatever meaning may be, all else seems lost without it. A Chinese poem has little effect on someone who does not understand Chinese (pp. 117–118).
- **Author's position:** meaningful language can fairly be regarded as a sort of code. It is not simple word-for-deed substitution. It is more like early cryptographic codes with many alternative code words, but with overlapping entries, and one person's code book may differ from another's (p. 118). Colin Cherry "appears to object" (p. 118).
- If we regard language as an imperfect code, we must ultimately refer meaning back to the user's intent. Hence the question *What do you mean?*, scholars seeking the intent of dead authors, and the Supreme Court seeking Congress's intent. A liar's words are read as intent to flatter or deceive (p. 118).
- Grammatical sentences have what might be called a formal meaning, regardless of intent. If we had a satisfactory grammar, a machine should be able to establish subject, verb, object and which phrase modifies which word (p. 118).
- The next problem is associating words with objects, qualities, actions or relations in the world (p. 118).

### Words and the world: lists of qualities (pp. 118–121)
- Simple sentences in simple, unambiguous surroundings, such as *close the east window*, cause no trouble. The window sentence would puzzle a shelterless savage even in translation, and the question whether a virus is living or dead can puzzle us (p. 119).
- **Pierce's diagnosis:** it appears to him that much of the confusion arose through an effort by philosophers, from Plato to Locke, to give meaning to words by tying them to general ideas or ideal examples. Berkeley points out that the abstract idea of a triangle must be "all and none" of the kinds of triangle at once (p. 119).
- Doctors diagnose from signs and symptoms, not by comparison with an ideal disease. Botanists use qualities of size, colour, leaf shape and so on; some can be decisive (monocot versus dicot leaves) and others merely indicative (size) (pp. 119–120). So the ideal disease or plant is absent as a useful criterion (p. 120).
- **Machine evidence (author's reading):**
  - Early work matched letters or spectrograms to ideal patterns, with terrible results. Audrey recognised spoken digits from one voice or a selected few, and was fallible (p. 120).
  - Later workers look for significant features. A Q might be described as a closed curve with no corners or reversals of curvature and something attached between four and six o'clock (p. 120).
  - In 1959 L. D. Harmon built a small Bell Labs device that almost infallibly recognised longhand digit words. It asked how often the stylus went above or below certain lines and whether i's were dotted or t's crossed, with no pattern matching (p. 120).
- Pierce thinks we should conclude that human recognition works by template matching in very simple cases only, if at all (p. 120).
- **Author's belief:** classes of objects, qualities and actions are delimited by lists of qualities. The lists cannot be expected to give logical, sharply delimited, all-embracing categories; the language of science may approach this in a narrow range. Everyday language divides experience arbitrarily and with overlap (p. 121).
- He thinks it is only through this approach that we can hope to make a machine classify objects and experience in terms of language. He also believes we have a right to be wary of a word that cannot offer a table of signs traceable to familiar experience (p. 121).

### Meaning, the world and translation (pp. 121–123)
- A grammar and a way of relating words to the world are not enough: if we are to regard sentences as meaningful, they must in some way correspond to life as we live it (p. 121). Our lives consist of familiar objects and action sequences regrouped (pp. 121–122).
- Words let us learn about, remember, instruct and influence. For words to be useful, the hearer must understand them in the sense the speaker means, that is, associate them with nearly enough the same objects or skills, so telling a man to shoot the aardvark and not the gnu is useless if he has seen neither (p. 122).
- For sequences of words to be useful, they must refer to real or possible sequences of events. Advising a London-to-New-York walk in the forenoon after a seven o'clock dinner is useless (p. 122).
- So meaningfulness depends on grammar, on word–thing association, and on the structure of the world. This seriously threatens the idea of translating while accurately preserving meaning (p. 122).
- **Classification differences:** Russians have one word for foot plus lower leg. Hungarians use one word for finger and toe (stated as "twenty fingers"). Earlier speakers separated dog from bitch. Eskimos are said to make many snow distinctions (pp. 122–123).
- **Graver problem:** differing ranges of experience, such as tying a shoelace for a shoeless people, or *he built a house* in a pioneer novel versus a modern one (p. 123).
- Word-for-word translation between close languages is possible but is said to have turned *out of sight, out of mind* into *blind idiot*. Distant cultures require the translator to think in terms of objects, actions and emotions (p. 123).
- A translating machine would have to deal with understanding. A screen writer can shift a dying uncle in Omsk to a dying father in Dubuque but rephrases a technical statement as nonsense, because he understands grief but not science (pp. 123–124).

### Understanding and conclusion (p. 124)
- Understanding has two sides. One is power to do or create, such as solving new problems or proving unseen theorems. To some degree, a computer proving new theorems in logic could perhaps be said to understand the subject (p. 124).
- The other is emotional: proving a theorem several ways and fitting it with others gives a warm, confident feeling. One can feel that warmth without the ability (p. 124).
- **Conclusion:** information theory has not solved the problems of linguistics, meaning or understanding. At best, he says, we can perhaps say that we are pushing a little beyond the mechanical constraints of language and getting at the amount of choice it affords; this suggests views about the use and function of language but does not establish them (p. 124).

## Toy example
*Ours, not from the text.* It counts the free choices in a tiny kernel-style grammar.

Rules: S → NP VP; NP → Art N; VP → V NP. Words: Art ∈ {the, a}; N ∈ {man, girl, cat, ball}; V ∈ {hit, caught}.
- Word order and the S → NP VP structure are obligatory, so they give 0 choices.
- Each NP: 2 articles × 4 nouns = 8 options.
- Verb: 2 options.
- Sentences: 8 × 2 × 8 = 128 = 2⁷.
- If every choice is equally likely, each sentence has probability 1/128, so the entropy is 7 bits. Check by parts: NP is log₂8 = 3 bits, V is 1 bit, second NP is 3 bits, and 3 + 1 + 3 = 7.
- *The man hit the ball* is one of the 128, and *A girl caught a cat* is another.
- Only 7 bits of choice need to be sent. A receiver holding the grammar rebuilds the sentence, as in Pierce's grammar-machine idea (p. 110). The uniform-choice assumption is ours; Pierce leaves the real entropy to mathematicians (p. 115).

## Concepts
- [[grammar-as-generator]] (new) — rules producing all and only grammatical sentences, separating forced features from choice (pp. 109–110)
- [[entropy-rate]] — Pierce says that, if Shannon is right, English text involves a choice of about 1 bit per symbol; a grammar could yield a new estimate (pp. 110–111)
- [[finite-state-machine]] (new) — a machine that is in a particular state at each point and moves to another state. Chomsky rejects it as a possible or proper model of English grammar, but Pierce notes that his grammar with a bounded sentence length corresponds to one (pp. 111–112, 115)
- [[kernel-sentence-grammar]] (new) — Chomsky's scheme of a general form, then branch-wise expansion by optional and obligatory rules (p. 113)
- [[language-as-imperfect-code]] (new) — Pierce thinks it fair to regard meaningful language as a sort of code with overlapping entries; if so, meaning must ultimately refer back to the user's intent (p. 118)
- [[feature-list-classification]] (new) — identifying a class by a list of qualities, some decisive and some indicative, not an ideal pattern (pp. 119–121)
- [[understanding]] (new) — power to do or create, plus an emotional side: a warm, confident feeling about one's ability to cope (p. 124)

## Canonical instances
- [[fourth-order-word-approximation-by-people]] — chained human sentence completion giving surprisingly grammatical strings (pp. 110–111)
- [[reverse-after-Z-process]] — a sequence rule with unbounded long-range order that no finite-state machine can follow (p. 112)
- [[the-man-hit-the-ball]] — kernel sentence expanded into a sentence by choices (p. 113)
- [[shooting-of-the-hunters]] — grammatical ambiguity (p. 114)
- [[audrey-and-harmon-digit-recognizers]] — template matching versus feature questions (p. 120)
- [[translation-difficulties]] — classification and cultural-range differences (pp. 122–123)

## Bridges (candidates)
- [structural-analogy] Grammar machine plus transmission of choices only ↔ information-theory: source coding, where only the information-carrying part of a message needs sending.
- [structural-analogy] Kernel-sentence tree of optional/obligatory rules ↔ computer science: generative grammars and the hierarchy of machines they need.
- [structural-analogy] Lists of decisive and indicative qualities ↔ machine learning: feature-based classification versus template matching.
- [metaphor] Language as imperfect code with overlapping code books ↔ information-theory: a noisy channel where sender and receiver hold different codebooks.

## Questions this raises
- How could the entropy of a source following a phrase-structure grammar actually be computed? Pierce says only that this is a question for mathematicians (p. 115).
- If a sentence length limit makes Chomsky's grammar finite-state, does that undo Chomsky's objection in practice, or only in principle (pp. 112, 115)?
- Can "intent" be built into a measure of information, given that Pierce treats meaning as intent (p. 118)?
- Which qualities in a feature list are "decisive" and which "indicative", and could a machine learn this (pp. 119–120)?

## Reading notes
- The text layer shows the chapter label garbled ("CHAPTER V 1"); the unit metadata titles it Chapter 6. Printed page = pdf − 16 (pdf 123 = p. 107).
- Edition: the running header reads *Symbols, Signals and Noise*. The metadata warns that this scan is the 1961 Harper & Brothers first edition, not the 1980 Dover one; no title page is in these pages. Page numbers refer to this scan.
- The text layer has scan noise (stray characters, irregular spacing); In the Harmon passage (p. 120) the text layer reads "Fs dotted or Ps crossed"; I take this to mean i's dotted and t's crossed, from context.
- Arithmetic check: 22 binary choices give 2²² ≈ 4.2 million, while Pierce writes some 10 million (p. 111). This is loose, not corrected in the source.
- Page references use the printed page numbers throughout.
