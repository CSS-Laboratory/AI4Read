---
id: lycan-2019-language/ch09-truth
work: lycan-2019-language
unit: "9 Truth-Condition Theories: Davidson's Program"
pages: 114-128
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Truth-Condition Theories: Davidson's Program

## L0 — One line
Davidson proposes that a theory of meaning should assign each sentence its truth condition rather than its verification condition; a compositional truth definition modelled on formal logic can (as shown for a toy language) derive the truth conditions of infinitely many sentences from finitely many words and rules, and the hope is that this also captures meaning.

## L1 — The gist (≤ 120 words)
Davidson asks what form a "theory of meaning for" a particular language should take. His answer replaces verification conditions with truth conditions. A truth definition, modelled on the semantics of formal logic (illustrated with a toy language), derives each sentence's truth condition from finitely many word-meanings and combination rules. Davidson argues that compositionality of this kind is needed to explain how we understand long novel sentences. For English, whose surface grammar diverges from logical form, syntax and transformations must link the two. Lycan then lists objections: sentences without truth-values, context-dependent expressions, coextensive but non-synonymous predicates, constructions that are not truth-functional, and dependence on a theory of truth such as deflationism. Several get a reply or rejoinder.

**Prerequisites:** the idea of a sentence connective ("and", "not"); verification theory and Russell's theory of descriptions (earlier chapters); "if and only if".

## L2 — Key ideas (5–10 bullets)
- Davidson replaces verification conditions with truth conditions: to know a sentence's meaning is to know when it would be true, not how to test it (p. 115).
- Main argument: compositionality is needed to account for our understanding of long novel sentences, and a sentence's truth condition is its most obviously compositional feature (pp. 114, 116–117).
- Model: the toy language "Oafish" has a finite truth definition that fixes the truth condition of every one of its infinitely many sentences (pp. 117–118).
- Davidson asks what more could reasonably be asked of a theory of meaning if each T-sentence ("'S' is true iff …") gets its target sentence's truth condition right. Lycan adds that if the truth definition also does everything we expect of a theory of meaning, it would be reasonable to identify meaning with truth condition (p. 119).
- On the truth-condition view, synonymy, ambiguity and entailment are accounted for in terms of truth conditions (pp. 115, 119).
- For English, whose surface grammar differs from logical form, syntax (phrase markers and transformations) is meant to link the two; given that transformations preserve meaning or at least truth properties, English sentences could get their meanings via truth conditions (pp. 120–123).
- Objections 1–2: questions and commands, and (it is argued) some declaratives such as indicative conditionals and moral judgments, seem to lack truth-values (pp. 123–124).
- Objections 3–5: indexicals, coextensive predicates and non-truth-functional constructions are hard cases (pp. 124–126).
- Objection 6: the theory depends on a conception of truth; Lycan replies that only a valid, non-question-begging argument against it would count (p. 126).

## L3 — Walkthrough

### Overview and "Truth Conditions" (pp. 114–120)
**Setup.** Davidson wants to replace the verificationist's verification condition with the sentence's truth condition: the condition under which it is or would be true, not evidence of its truth (p. 114). Lycan's assessment of the rivals: the Proposition Theory only reified meanings. Grice passed the question to the philosophy of mind and took the contents of intentions for granted. Verificationism offered a test, but it often predicts the wrong content (pp. 114–115).

**Definitions on this view (p. 115).**
- To know a meaning is to know the conditions under which the sentence would be true.
- Two sentences are synonymous iff they are true under just the same conditions.
- A sentence is ambiguous iff it is both true and false in the same circumstance, without self-contradiction.
- One sentence entails another iff it is impossible for the first to be true without the second.

Russell's Theory of Descriptions already proceeded by sketching truth conditions (p. 115).

**Davidson's constraints.** Davidson asks for a "theory of meaning for" a particular language (English, Mandarin) that specifies the meaning of its sentences one by one (p. 115).
- Constraint 1: since there is no clear limit to the number of meaningful expressions, a theory must account for each meaning "on the basis of the patterned exhibition of a finite number of features" (p. 115).
- Lycan's gloss: the answer must be that we have mastered a finite set of meaning "atoms" plus rules of composition (pp. 115–116).
- Davidson contends that a sentence's meaning is a function of the meanings of its constituent words. This is compositionality ("Frege's Principle") (p. 116).
- Lycan calls compositionality the obvious hypothesis explaining understanding of long novel sentences (p. 116).
- The target is a potentially infinite list such as "Snow is white" means that snow is white. The same should work for German sentences (p. 116).

**Truth conditions also seem to be grasped on sight.** Given enough facts, we can tell the truth-value of a novel sentence. Lycan's example is the Katherine Dienes "Ave Maria" sentence, which he knows to be true; a variant with "medieval convent music" replaced by "hip-hop in the style of DJ Khaled" and a clause added saying Dienes has recently moved to Newark, New Jersey, he would instantly know to be false (pp. 116–117). Davidson thinks this is no coincidence. The truth conditions of long sentences are determined by those of the shorter sentences composing them, because syntactic processes carry truth-related properties along (p. 117).

**The model: Oafish (pp. 117–118).** Predicates $F$ ("fat") and $G$ ("greedy"); names $a$ (Albert) and $b$ (Betty); connectives "not" and "and". The truth definition:
- "F" applies to fat things; "G" applies to greedy things; "a" denotes Albert; "b" denotes Betty.
- A sentence "Pn" is true iff what "n" denotes is a member of the class of things "P" applies to.
- "Not A" is true iff "A" is not true.
- "A and B" is true iff "A" and "B" are both true.

The class of things a term applies to is its extension (p. 118). The definition covers indefinitely many and indefinitely long sentences ("Fa and not Ga and Fb and not Gb", and so on) and gives each one's truth condition. Worked example: "Fa" is true iff Albert is in the class of fat things, i.e. iff Albert is fat. The result for the long sentence: "Fa and not Ga and Fb and not Gb" is true iff Albert is fat and Albert is not greedy and Betty is fat and Betty is not greedy (p. 118). Lycan's point: a potentially infinite capacity is explained by finite, minuscule means, and this truth condition also seems to give the sentence's meaning, compositionally (p. 118).

*Intuition note.* A few word-level rules plus rules for "not" and "and" let you compute, step by step, when any sentence of the language is true. The finite theory covers infinitely many sentences; if the computed condition also seems to say what the sentence means, it may serve as a theory of meaning for them too.

**T-sentences (p. 119).** A truth definition for English would yield, for each sentence, a "Tarski biconditional" or T-sentence, "'——' is true iff ——". Davidson asks what more could reasonably be asked of a theory of meaning if each T-sentence gets its truth condition right (p. 119).
- Lycan's caveat: Davidson sometimes writes as if right-hand sides are plain English, but no actual truth definition could deliver such T-sentences (Stich; Blackburn). The theory must be formulated in a regimented, logic-like language (p. 119).
- Example, from a version of Davidson's theory of action sentences: "Jones buttered the toast at midnight" is true iff $(\exists e)(\text{BUTTERING}(e) \;\&\; \text{PROTAG}(\text{Jones}, e) \;\&\; \text{VICTIM}(\text{the toast}, e) \;\&\; \text{OCCURRED-AT}(e, \text{midnight}))$. Read: there occurred an event, a buttering of the toast, by Jones at midnight (p. 119).
- Making the event the underlying subject explains entailments such as "Jones buttered the toast", "Jones buttered something", "Something happened at midnight" (p. 119).

**Further argument.** A correct meaning assignment should determine a truth condition. So an adequate theory of meaning should yield at least a truth definition (the verificationist must agree). If the truth definition also does everything we expect of a theory of meaning, it would be reasonable to identify meaning with truth condition (p. 119).

**Meaning facts.** Entailment: "Fa and not Fb" entails "Fa" because by the truth definition the former could not be true unless the latter were. The truth definition predicts felt synonymies and entailments from its compounding rules (p. 119). Method: like Russell, the theorist gathers meaning facts (synonymy, ambiguity, entailment) about a class of sentences and proposes truth conditions that explain them (pp. 119–120). The theory treats meaning as representation: it returns to the Referential Theory's mirroring idea, but without claiming all words are names (p. 120).

### Truth-Defining Natural Languages (pp. 120–123)
**The problem.** Oafish sentences wear their truth conditions on their sleeves: surface grammar equals logical form. English does not, since surface forms differ unpredictably from logical forms. The truth-condition theorist replies: not quite unpredictably, and syntax is what connects them (p. 120).

**Syntax.** A grammar sorts well-formed sentences from other word strings. Oafish sentences are parsed by phrase markers (tree diagrams); e.g. "Fa and not Fb" is built from the sentences "Fa" and "not Fb" joined by "and" (Fig. 9.1, p. 121). Simple English sentences are diagrammed alike: "The boy hit the colorful ball" (NP + VP, Fig. 9.2, p. 122). Few English sentences are this simple. Chomsky argued that context-free phrase markers need augmenting with transformations, rules turning one phrase marker into another (e.g. the passive: "The colorful ball was hit by the boy") (p. 121). Lycan says his terminology is antiquated, and that present-day grammars no longer have this simple architecture (pp. 120–122).

**From grammar to meaning.** Word order matters to meaning: "John loves Marsha" differs from "Marsha loves John," so the projection rules need finer tuning than word identity. The syntactic rules that build strings seem well suited to be those rules. In the late 1960s many linguists held that transformations preserve meaning; the thesis was qualified and partly abandoned in the 1970s (p. 122).

**Lycan's picture.** Suppose a phrase-structure grammar for a truth-defined formal language, plus independently motivated (mainly syntactic) transformations that convert its formulas into English strings. Given that transformations preserve meaning, or more narrowly truth properties, English sentences have meanings in virtue of truth conditions, which they have in virtue of being transformationally derived from truth-defined formulas. Synonymous sentences are transformational variants; ambiguous ones result from more than one possible transformational process (pp. 122–123).

**Contrast with Russell.** Russell worked a priori, comparing an English sentence with a logical formula by eye, though he also appealed to puzzle-solving power. A contemporary theorist should also answer to plausible syntactic theories (p. 123).

*Intuition note.* English is not truth-defined directly. The hope is that English sentences are derived by meaning-preserving (or truth-preserving) transformations from underlying logic-like formulas that are truth-defined.

### Objections to the Davidsonian Version (pp. 123–126)
**Objection 1: non-declaratives (p. 123).** Like verificationism, the theory seems to cover only fact-stating language; questions and commands are not true or false.
- *Reply:* they have bipolar, truth-like values (a question is answered "yes" or "no"; a command is obeyed or disobeyed), and for semantics we may treat these as truth-values, though this is a nonstandard use of "true".
- *Rejoinder:* not all non-declaratives are bipolar. "Wh-" questions ("Who robbed the diaper service?") have no yes/no answer and admit many correct answers (p. 123).

**Objection 2: declaratives without truth conditions (p. 124).**
- Some argue (Adams 1965 and others) that indicative conditionals lack truth conditions and truth-values, having only assertibility conditions.
- Emotivists hold that moral judgments merely express attitudes, like groans or cheers. If so, the T-sentence "'Murder is wrong' is true iff murder is wrong" should come out false or anomalous (according to the objection).
- Some ordinary words and sentences almost uncontroversially just express feelings; these are taken up in Chapter 14 (p. 124).

**Objection 3: deictic (indexical) elements (p. 124).** Deictic elements are those whose interpretation varies with context of utterance (tense markers, demonstratives). "'I am sick now' is true iff I am sick now" would not do, since its truth-value depends on speaker and time.
- Davidson's response: relativize truth to a speaker and time, "'I am sick now' is true as potentially spoken by p at t iff p is sick at t."
- Lycan says this is unsatisfactory in several ways, not least because speaker and time are not the only contextual factors (cf. "This is a fine red one"). The issue returns in Chapter 11 (p. 124).

**Objection 4: coextensive but non-synonymous terms (pp. 124–125).** "Renate" (creature with kidneys) and "cordate" (creature with a heart) are stipulated to have the same extension, so a truth theory seems unable to distinguish sentences containing them (p. 124).
- *Reply:* they differ in modal and belief sentences, and Davidson's semantics for these must predict non-interchangeability (p. 125).
- *Rejoinder:* such intensional sentences (substitution of coextensives may change truth-value; a generalization of referential opacity) are puzzling in themselves. The phrase "whatever semantics Davidson gives" is not innocent, since the problem will be hard given his format (p. 125).
- Davidson (1968) addresses intensionality roughly by treating intensional sentences as tacitly referring to the words occurring in them (p. 125).

**Objection 5: non-truth-functional constructions (pp. 125–126).** "And" is truth-functional. "A because B" is not, since it may be false even if A and B are true. How would one write truth rules for "because", "slowly", "very", or "believes that" ("n believes that A" is true iff … what?) (p. 125).
- A strategy: quantify over a domain of helpful entities (propositions; events, with adverbs made predicates of events).
- Its main problem is that it strains syntax, since transformations must work harder to reach familiar English. Blackburn (1984) says this kind of treatment requires at least a heavy commitment to concealed logical forms (p. 126).

**Objection 6: hostage to a conception of truth (p. 126).**
- Strawson (1970): truth must be understood via stating or asserting, hence via communication in Grice's style. On this objection, truth-conditional semantics collapses into Griceanism.
- Horwich (1990) and Brandom (1994), following Dummett: on deflationary (minimalist) theories "true" is a device for semantic ascent; "'Snow is white' is true" adds nothing to "Snow is white." If so, it is argued, the meaning of "S is true" is parasitic on that of S, and offering S's truth condition to explain S's meaning would be circular. Horwich's image: a T-sentence cannot solve for both meaning and truth, like one equation with two unknowns.
- *Reply (Lycan):* each such objection must be examined. A threat needs a deductively valid argument, with no question-begging premises, from the theory of truth to the falsity of the Truth-Condition Theory. Lycan has never seen a convincing one. If one is accepted, we must choose between the two theories (p. 126).
- Note 8 (p. 128) reports that Horisk, Bar-On and Lycan (2000) argue that deflationism is false or compatible with the theory, whereas Horisk (2007) offers a deductive argument from one specific deflationism to the falsity of Davidsonian semantics.

### Summary (p. 127)
Lycan repeats: compositionality as main argument; Tarskian truth definition as model; syntax needed; and the objections. He calls the most damaging perhaps that many meaningful sentences lack truth-values because they do not state facts (p. 127).

## Toy example (ours, not from the text)
Take Oafish with a model: fat things = {Albert}; greedy things = {Albert, Betty}.
Evaluate "Fa and not Gb" step by step:
1. "Fa": Albert is in {Albert}, so true.
2. "Gb": Betty is in {Albert, Betty}, so true.
3. "not Gb" is true iff "Gb" is not true. "Gb" is true, so "not Gb" is false.
4. "Fa and not Gb" is true iff both parts are true. Part 2 is false, so the sentence is false.

The T-sentence derived: "Fa and not Gb" is true iff Albert is fat and Betty is not greedy. In this model Betty is greedy, so the right-hand side is false. A longer sentence such as "Fa and not Gb and Ga" uses the same three rules and needs no new ones.

## Concepts
- [[truth-condition-theory]] (new) — meaning of a sentence is given by the condition under which it is true (p. 115)
- [[compositionality]] (new) — a sentence's meaning (or truth condition) is a function of its parts' meanings and their syntactic combination (p. 116)
- [[truth-definition]] (new) — finite set of rules assigning each sentence of a language a truth condition (p. 117)
- [[T-sentence]] (new) — theorem of the form "'S' is true iff …" (Tarski biconditional) (p. 119)
- [[logical form vs. grammatical form]] — surface grammar of English differs from logical form, which syntax is meant to bridge (p. 120)

- [[theory of descriptions]] — Russell's sketching of truth conditions, cited as precedent (p. 115)
- [[validity / soundness]] — Lycan's reply to Objection 6 requires a deductively valid argument (p. 126)
- [[transformation]] (new) — Chomskyan rule turning one phrase marker into another (p. 121)
- [[intensional-context]] (new) — sentence where substituting coextensive terms can change truth-value (p. 125)
- [[deflationism-about-truth]] (new) — on deflationary theories, "true" is just a device of semantic ascent, adding nothing to the sentence (p. 126)

## Canonical instances
- [[oafish-language]] — toy truth-defined language with $F, G, a, b$, "not", "and" (pp. 117–118)
- [[renate-cordate]] — coextensive, non-synonymous terms (p. 124)
- [[jones-buttered-the-toast]] — event-based T-sentence for an action sentence (p. 119)
- [[i-am-sick-now]] — indexical sentence and Davidson's relativization (p. 124)
- [[ave-maria-sentence]] — long novel sentence whose truth condition we grasp on sight (pp. 116–117)

## Bridges (candidates)
- [structural-analogy] Truth definition for Oafish ↔ logic: recursive semantics of propositional/predicate calculus — Lycan says it is the model, formulated by logicians (p. 117).
- [same-math] "A and B" true iff both true; "not A" true iff A is not true ↔ propositional logic: truth tables for ∧, ¬ — the rules are the same.
- [structural-analogy] Compositionality as explanation of unbounded understanding ↔ linguistics: finite grammar generating infinitely many strings (pp. 116, 121).
- [metaphor] T-sentence as "one equation with two unknowns" (Horwich) ↔ algebra: underdetermined system (p. 126).

## Questions this raises
- Can any truth definition yield T-sentences whose right-hand sides are correct without already using the meanings of the very words it interprets?
- Does the transformation-preserves-truth thesis, partly abandoned by 1970s linguistics, survive in later syntactic theories?
- How could a truth rule for "because" or "believes that" be stated without heavy concealed logical forms?
- Is a deflationary view of truth compatible with a truth-condition theory of meaning?

## Exercises worth doing
The chapter lists discussion questions, not problems with solutions.
- Q. 1 (p. 127) — evaluate the compositionality-plus-Tarski argument — difficulty: medium
- Q. 2 (p. 127) — test the argument that a truth definition does all a theory of meaning should — difficulty: medium
- Q. 4 (p. 127) — adjudicate one of the objections — difficulty: medium
- Q. 5 (p. 127) — decide if deflationism undermines the theory — difficulty: hard

## Reading notes
- Printed = pdf − 15 (pdf 129 = printed 114).
- Figures 9.1 and 9.2 (phrase markers) are described in words only; the layout was checked against the page images.
- Lycan's own sympathies show in note 5 (p. 128), where he says he believes the Truth-Condition Theory is correct. The Replies and Rejoinders are written in Lycan's voice, but only some (e.g. in Objection 6) are explicitly marked as his own judgment.
- On p. 119 Lycan notes that Davidson sometimes talks as if the right-hand sides of his T-sentences will be in English, and says no actual truth definition could deliver such T-sentences; this qualification is Lycan's (citing Stich and Blackburn), not Davidson's.
