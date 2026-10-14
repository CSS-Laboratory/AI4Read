---
id: lycan-2019-language/ch11-semantic
work: lycan-2019-language
unit: "11 Semantic Pragmatics"
pages: 141-149
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Semantic Pragmatics

## L0 — One line
Context fixes *what proposition* many sentences express (semantic pragmatics), and Harman's open-ended assignment function α, unlike fixed lists of contextual variables, lets truth theories handle this.

## L1 — The gist (≤ 120 words)
Pragmatics studies how expressions are used in context. Following Cresswell, Lycan separates two kinds. Semantic pragmatics asks how context determines propositional content, as with "I", "now" and "tomorrow". Pragmatic pragmatics asks what else a sentence with fixed content can do in context. Davidson's speaker-and-time T-sentences and the possible-worlds "index" both list a fixed set of contextual factors. Lycan argues that we can never be sure such lists are complete, and advises using Harman's function α instead. Cappelen and Lepore defend a small fixed basic set of context-sensitive terms, but Lycan finds their account of the remaining data unhelpful. Semantic pragmatics also faces disambiguation.

**Prerequisites:** truth conditions and Davidson-style T-sentences; propositions; intensions as functions from possible worlds to extensions; the idea of deixis (words like "I", "now").

## L2 — Key ideas (5–10 bullets)
- Cresswell's split: semantic pragmatics is how context fixes propositional content; pragmatic pragmatics takes content as given and studies further uses (p. 143, p. 147–148).
- In an important sense most sentence types lack acontextual meaning, and propositional content depends on context. Without knowing context, we do not know what a deictic sentence such as the blackboard sentence says (p. 142–143).
- Fixed lists of context variables, whether Davidson's speaker-and-time or the eight-element index, are unsatisfactory because they arbitrarily restrict the factors that can be cited, and further variables seem to turn up without limit (p. 144–145).
- Harman's α maps each deictic element in a context C to its contribution to content. This handles deixis without a fixed list (p. 143–144).
- Cappelen and Lepore's semantic minimalism: only a small basic set of terms is truly deictic, and other context-effects concern what is *said*, not propositional content (p. 145). Their two tests do separate "I" and "now" from "ready" and "enough" (p. 145–146).
- Lycan's complaint: Cappelen and Lepore offer no method for getting from minimal content to what is said, and he calls appeal to implicature a false hope (p. 146).
- Even the rules for "I" and "now" need refinement. Kaplan treats the composite rule as a function from contexts to contents ("character") (p. 146–147).
- Disambiguation is a further, much harder task for semantic pragmatics (p. 147).

## L3 — Walkthrough

### Overview and Morris's division (p. 141–142)
- Morris divided linguistic study into syntax (which strings are well-formed sentences), semantics (meaning, mainly as relations of expressions to the world) and pragmatics (uses of expressions in social practices, not only conversation) (p. 141).
- In these terms, Wittgenstein's view is that semantics is either entirely misguided or collapses into pragmatics (p. 142).
- Syntax and semantics have aimed to be contextless. Semantics has studied sentence-type meaning, abstracted from any use. Wittgenstein, Strawson and Austin remind us that the idea of a sentence type is a violent abstraction from linguistic reality. Lycan adds that an uttered sentence is invariably uttered in a particular context by a particular speaker for a particular purpose (p. 142).
- The semantics/pragmatics line ("acontextual meaning" vs. "social use") is too simple for two reasons. (i) Most sentence types lack acontextual meanings. (ii) Social-use factors interpenetrate propositional meaning in special ways (p. 142). Lycan says his use of the terms is stipulative (p. 142).

### Why sentence types lack acontextual meaning (p. 142–143)
- Example (1): "I am ill and will not hold class today," found on a blackboard. Unless we know who wrote it, when, and to whom, we do not know what proposition it expresses, i.e. its intension (p. 142).
- If it was only written as a linguistic example, with no referents assigned, it expresses no proposition and has no intension (p. 143).
- Moral: a sentence's complete truth condition, and so its propositional content, depends on context (p. 143).
- **Cresswell's distinction:** *semantic pragmatics* covers the elements of propositional content that depend on context and says how context determines content. *Pragmatic pragmatics* is the contrast case, treated at the end of the chapter (p. 143; see p. 147–148).

### The Problem of Deixis (p. 143–146)
- Davidson needs T-sentences that handle deictic (indexical) elements. His own proposal limits the relevant factors to speaker and time. Lycan presents Harman's idea instead (p. 143).
- Other relevant factors: pointing gestures ("This one is more expensive than that one") and hemisphere. "It is autumn" is true in Connecticut but not in Sydney. The relevant hemisphere can depend on audience and purpose, not only the speaker's location (p. 143).
- **Harman's α.** Relativize "true" to contexts. α looks at a deictic element in a context C and returns its contribution to content (p. 143).
  - If (as is widely thought) "I" always denotes the speaker, α("I", C) is the speaker in C. If "now" denotes roughly the time of utterance, α("now", C) is that time. α("tomorrow", C) would be the day immediately following the uttering in C (p. 143–144).
  - Example T-sentences (p. 144):

$$\text{“I am sick now” is true in } C \iff \alpha(\text{“I”}, C) \text{ is sick at } \alpha(\text{“now”}, C).$$

  - Tense is treated roughly, e.g. α(present tense, C), and Lycan calls this a fudge for convenience (n. 4, p. 149). His other examples are the "I am ill…" sentence and a karaoke sentence with "She", "you" and "tomorrow" (p. 144).
  - Lycan: "Problem solved", but only as Davidson's technical problem. Further philosophical questions about α remain (p. 144).
- **Intensional logicians' index.** Montague and Scott relativize truth to an index $\langle w,t,l,p,a,i,d,s\rangle$: world, time, place, speaker, audience, indicated objects, discourse segment, sequence of assignments to free variables (p. 144).

$$\text{“I am sick now” is true at } \langle w,t,l,p,a,i,d,s\rangle \iff \text{in } w,\ p \text{ is sick at } t.$$

  - This shares Davidson's drawback, though less severely: it arbitrarily restricts the contextual features that can be cited (p. 144).
- **More variables, "seemingly without limit"** (p. 144–145):
  - Time zone: "It is 5:00 p.m." depends on it. "It is 5:00 p.m. on the sun" has no truth-value, as Wittgenstein noted (p. 144).
  - Vantage point: (2a) "Zonker went to Uncle Duke's party" and (2b) "Zonker came…" can have the same truth condition. (2b) is proper only for a speaker whose assumed vantage point is the party location, at the time of the party (the reference time). In (2c) from Frost, the vantage point shifts within the passage (p. 144–145).
  - "Is prostitution legal?" depends on the jurisdiction. "Is Henry ready?" and "Has Sandy had enough?" leave open ready for what and enough of what (p. 145).
  - Deictic terms with unusual referents (Nunberg): "Are you here now?" asks about employing institution, not physical location. In (3) "Tomorrow is always the biggest party night of the year," uttered the Friday before classes, "tomorrow" refers to the annual Saturday before classes begin (p. 145).
- Lycan's moral: we cannot ever be sure we have anticipated all the context variables that can affect truth-value, so he advises intension theorists to use Harman's α instead (p. 145).

> **Intuition note.** A fixed list of contextual "slots" is like a form with a fixed number of boxes. Lycan argues we cannot be sure we have foreseen every box. α does not presuppose a fixed number of contextual variables: it simply tells us what each deictic element contributes in a context (p. 143, 145).

- **Cappelen and Lepore's semantic minimalism** (their view). There is a small basic set of obviously context-sensitive expressions. Beyond fixing their values, context has no effect on the proposition semantically expressed. What varies widely with context is what is *said*, meaning explicitly said (p. 145). Lycan agrees that indirect-speech reports are "pretty forgiving" (p. 145).
- Their tests (p. 145–146):
  - *Disquotation test:* for basic-set terms, there can be false utterances of "S" even though S. For example, "I am sick now" can be uttered falsely by a speaker even though I am sick now (p. 145).
  - *Indirect discourse test:* a speaker may have uttered S, yet "the speaker said that S" can be false. Ernie said "I am sick now," but did not say that Lycan is sick now (p. 145–146).
  - (4) "Henry is ready" and (5) "Sandy has had enough" fail both tests (p. 146).
- Their claim: (4) and (5) have simple, uninteresting propositional contents ("Henry is ready, period"). What varies with context is what they could be used to say (p. 146). In note 6 Lycan reports that, on Cappelen and Lepore's position, the felt incompleteness of "ready, period" and "enough, period" is metaphysical only, not semantic (n. 6, p. 149).
- **Lycan's assessment.** The tests are appropriate. They seem to show that "ready" and "enough" are not as thoroughly context-dependent as "you", "now" and "that" (p. 146). The problem is that we then need a way to calculate what the speaker actually said from the minimal content. Cappelen and Lepore give no help. Implicature will not do, since it concerns what is merely conveyed, not explicitly said (p. 146).

> **Intuition note.** Minimalists move the context-dependence from "what the sentence means" to "what the speaker says". Lycan's complaint is that once this move is made, Cappelen and Lepore give no method for calculating what is said from the minimal content (p. 146).

### The Work of Semantic Pragmatics (p. 146–148)
- The task is to find how α is computed, with presumably a rule for each deictic element (p. 146).
- Simple rules ("I" always denotes the speaker; "now" the time of utterance) are too simple. "I" can give deferred reference to a role (the condemned prisoner's last meal) or occur in generalizations ("If I'm a music department, I'm a snake pit") (p. 146–147). "Now" can be deferred ("Now the dinosaurs appear"; the answering-machine "right now"), spatial ("Now Hillsborough Road crosses Airport Road…"), or not spatio-temporal ("Now comes the first prime number whose square is greater than 1,000") (p. 147).
- **Kaplan:** an intension is a function from worlds to extensions. For a sentence it is a function from worlds to truth-values, which Kaplan calls *content* (the traditional proposition). A semantic–pragmatic rule is a function from contexts to intensions, and the composite rule is a function from contexts to contents, which he calls *character* (p. 147).
  - For the blackboard sentence, character tells us to look for the speaker, hearer and date. Once we know them, we know what must hold in a world for the sentence to be true there (p. 147).
  - Kaplan argues that "meaning" should be reserved for character. Lycan says virtually any English speaker understands "I am sick now" out of context. Kaplan's stated ground is that speakers know the meanings of everyday deictic sentences even when they do not know the contextual parameters that fix their contents. Lycan notes that content is also a fine thing to call meaning, and this is not a matter for heated dispute (p. 147).
- **Disambiguation.** Examples: "Visiting philosophers can be boring," "Ted is lying about meditating," Ziff's "The mouse tore up the street." Nearly every sentence is technically ambiguous. We rarely notice choosing among meanings. Lycan calls this a much deeper question than computing α, too deep for this book, though Chapter 13 will give some hints (p. 147).
- **Pragmatic pragmatics** takes propositional content as given and asks how one sentence with fixed content can do different things in different contexts (p. 147–148).

> **Intuition note.** Character is a recipe; content is the dish it yields in one context. Understanding the recipe is knowing the sentence's meaning in Kaplan's sense, even if no context is available to cook it.

## Toy example (ours)
Sentence type: "I am sick now." Let α("I", C) = speaker of C and α("now", C) = time of C.
- C1: speaker Ann, time Monday. Content: *Ann is sick on Monday*.
- C2: speaker Bob, time Tuesday. Content: *Bob is sick on Tuesday*.
- Suppose, in the actual world, Ann is sick on Monday (yes) and Bob is sick on Tuesday (no).
- Then the same sentence type is true in C1 and false in C2. It is true in $C_1$ iff Ann is sick on Monday (she is, so true). It is true in $C_2$ iff Bob is sick on Tuesday (he is not, so false).
- Kaplan's character is the map $C_1 \mapsto$ "Ann sick on Mon", $C_2 \mapsto$ "Bob sick on Tue". Each content is then a map from worlds to truth-values.
- Adding the "hemisphere" variable for "It is autumn" would just be another α-rule (C ↦ relevant hemisphere), with no change to the framework.

## Concepts
- [[semantic-pragmatics]] (new) — how context determines propositional content (p. 143)
- [[pragmatic-pragmatics]] (new) — study of further uses of a sentence once its content is fixed (p. 143, 147–148)
- [[deixis]] (new) — context-sensitive elements (pronouns, tense, "now") whose contribution varies by context (p. 141)
- [[assignment-function-alpha]] (new) — Harman's α(expression, C): what a deictic element contributes in context C (p. 143)
- [[context-index]] (new) — Montague/Scott's fixed eight-element tuple that relativizes truth (p. 144)
- [[semantic-minimalism]] (new) — Cappelen and Lepore: only a small basic set of terms is truly context-sensitive (p. 145)
- [[character-vs-content]] (new) — Kaplan: character = function from contexts to contents; content = function from worlds to truth-values (p. 147)
- [[disambiguation]] (new) — picking the intended one of a sentence's possible meanings (p. 147)
- [[t-sentence]] (new) — Davidson's truth-condition biconditional, here relativized to a context (p. 143–144)
- [[conversational implicature]] — merely conveyed, not explicitly said; Lycan says it cannot supply what is *said* (p. 146)

## Canonical instances
- [[blackboard-sentence]] — "I am ill and will not hold class today": without knowing who wrote it, when, and to whom, we do not know what proposition it expresses (p. 142)
- [[hemisphere-autumn]] — "It is autumn": truth depends on hemisphere, a factor beyond Davidson's speaker and time (p. 143)
- [[zonker-came-went]] — vantage point and reference time as context variables (p. 144–145)
- [[tomorrow-party-night]] — "tomorrow" referring to a type of date (p. 145)
- [[henry-is-ready]] — fails Cappelen and Lepore's tests (p. 146)
- [[condemned-prisoner-I]] — "I" as deferred reference to a role (p. 146)

## Bridges (candidates)
- [structural-analogy] Kaplan's character (context → content) ↔ programming: a function that returns a different value for each environment/argument.
- [structural-analogy] α-rules per deictic word ↔ text-as-data: meaning of a message depends on metadata (author, timestamp, audience) that must be supplied to interpret it.
- [structural-analogy] Disambiguation ↔ NLP: word-sense disambiguation, choosing among possible readings in context.

## Questions this raises
- Does α simply relocate the problem, since the rules for computing α may need open-ended knowledge of context (p. 144, 146–147)?
- How exactly do "ready"/"enough" differ from "I"/"now" beyond the two tests (p. 146)?
- How can the intended meaning be chosen so quickly from the many possible ones (p. 147)?
- What method could get from minimal content to what is said (p. 146)?

## Exercises worth doing
- Ex. 1 (p. 148) — whether α creates new difficulties of its own — difficulty: hard
- Ex. 2 (p. 148) — how the apparent content-dependence of "ready"/"enough" differs from what Cappelen and Lepore concede — difficulty: hard
- Ex. 3 (p. 148) — state the exact rule for "I", "now", "tomorrow" etc. — difficulty: medium
- Ex. 4 (p. 148) — make a start on disambiguation — difficulty: hard

## Reading notes
- Printed = pdf − 15 (pdf 156 = p. 141).
- The text layer was clean. The α and index biconditionals on p. 144 are plain text and match the page image.
- The chapter ends with a bullet Summary and four author's discussion questions (p. 148), then notes and a reading list (p. 149). Footnote 1 on p. 148–149 offers other ways to draw the semantics/pragmatics line (e.g. literal saying vs. conveying; relevance-theory processing). Lycan's own use is stipulative (p. 142).
- The objection 3 and Chapter 13 are referred to but not included here.
