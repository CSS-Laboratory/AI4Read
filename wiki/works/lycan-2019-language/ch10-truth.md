---
id: lycan-2019-language/ch10-truth
work: lycan-2019-language
unit: "10 Truth-Condition Theories: Possible Worlds and Intensional Semantics"
pages: 129-138
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Truth-Condition Theories: Possible Worlds and Intensional Semantics

## L0 — One line
If a sentence's truth condition (and, for the truth-condition theorist, its meaning) is the set of possible worlds in which it is true, and word meanings are functions from worlds to extensions, meaning can be computed compositionally and several of Davidson's problems are avoided.

## L1 — The gist (≤ 120 words)
Can the Truth-Condition Theory of meaning be improved by using Kripkean possible worlds? Lycan presents intensional semantics: a sentence's truth condition is the set of worlds where it is true, and a word's "intension" is a function from worlds to extensions. This handles coextensive-but-different terms and non-truth-functional connectives. It also gives accounts of modality, counterfactuals and belief sentences. Carnap's "intensional isomorphism" repairs the consequence that necessarily equivalent sentences come out synonymous. Still, the view inherits the rest of Davidson's difficulties (deixis comes in the next chapter). It also faces objections of its own: substitutivity of synonyms (obj. 7) and the Dummett–Putnam worry about understanding and behaviour (obj. 8).

**Prerequisites:** Kripke's possible worlds, rigid designators (Ch. 4); extension vs. sense; Davidson's Truth-Condition Theory and its objections 1–6 (Ch. 9); basic set theory (subset); "function".

## L2 — Key ideas (5–10 bullets)
- A sentence's truth condition, and so (for the truth-condition theorist) its meaning, is first taken as the set of worlds where it is true (p. 130).
- An intension is a function from worlds to extensions. Composing the intensions of parts gives a sentence's truth set (pp. 130–131).
- Meaning relations become set relations: synonymy is the same set of worlds, and entailment is the subset relation (p. 131).
- Lycan reads Lewis's direct argument this way: someone who understands S and is made omniscient about a world can tell whether S is true there. So a meaning is at least a truth condition (p. 132).
- Coextensive terms ("renate"/"cordate") differ in intension. Modal operators, kinds of possibility and counterfactuals get truth conditions in terms of worlds (pp. 132–134).
- Belief sentences: coreferring terms can differ in intension, which deepens Frege's solution to substitutivity (p. 134).
- On the simple sameness-of-truth-set account, all necessary truths would be synonymous. Carnap's intensional isomorphism fixes this (p. 135).
- Remaining troubles: Davidson's objections 1, 2, 3, 6; weirdness and alienness of worlds; objection 7 (synonyms failing substitution in some contexts); objection 8 (understanding vs. wide truth conditions) (pp. 135–137).

## L3 — Walkthrough

### Overview and "Truth Conditions Reconceived" (pp. 129–132)
- Overview: the view avoids several of Davidson's objections, most notably objection 4 (coextending but nonsynonymous terms) and objection 5 (non-truth-functional connectives). It gives attractive treatments of kinds of necessity and possibility, counterfactuals and belief sentences, and helps with the Problem of Substitutivity. But it inherits the rest of Davidson's difficulties and incurs one or two more (p. 129).
- Possible worlds give a new notion of truth condition. A sentence is true in some worlds and not others. **First approximation:** its truth condition is the set of worlds where it is true (p. 130).
- For the truth-condition theorist this set is also its meaning. So synonymous sentences are true in just the same worlds. Nonsynonymous ones differ in at least one world (p. 130).
- Background: Frege gave singular terms abstract senses and held that a sentence's sense is composed of the senses of its parts (compositionality). That sounds like the Proposition Theory and is prey to its objections. Carnap, Montague and Hintikka gave senses a possible-worlds interpretation (p. 130).
- **Intension** = function from worlds to extensions. A predicate's intension maps each world to the set of things that satisfy it there. The intension of "fat" looks from world to world and picks out the class of fat things in each (p. 130).
- Intensions of singular terms map worlds to individuals. A rigid designator is a constant function. A flaccid designator, such as the phrase for the British Prime Minister in 2017, changes referent across worlds, and in some worlds has none (p. 131).
- Sentence (1): "The present British Prime Minister is fat." In world $w$, (1) is true iff the Prime Minister of $w$ belongs to the extension of "fat" in $w$. The two intensions combine into a composite function from worlds to truth-values. That fixes (1)'s truth set, so its proposition and meaning. Strictly, the sentence's intension is the function, not the truth set, but Lycan ignores this (p. 131). Lycan adds that talk of "knowing" here is metaphorical, about computing a complex intension from simple ones, and is not verificationism (p. 131).
- Consequences (p. 131):
  - Synonymy: two sentences are synonymous iff true in just the same worlds.
  - Ambiguity: a sentence is ambiguous if some world makes it both true and false without contradiction.
  - Entailment: $S_1$ entails $S_2$ iff $S_2$ is true in any world in which $S_1$ is. The set of $S_1$-worlds is then a subset of the set of $S_2$-worlds (added step; see Reading notes).
- A proposition is a set of worlds. This answers Harman's objection 3 to the Proposition Theory. An abstract concept is a function from worlds to extensions, which answers the second objection to ideational theories (pp. 131–132).
- **Lewis (1970)** says that "A meaning for a sentence is something that determines the conditions under which the sentence is true or false" (p. 132). Lycan's reading ("I believe the idea is this"): if you understand S, you know S's truth value in any world, given full knowledge of that world's facts. So a meaning is at least a truth condition, and may include more (p. 132).

*Intuition note:* For the truth-condition theorist, a meaning acts like a test that can be run on any imagined world, answering true here or false here. The set of worlds that pass is the meaning, and word intensions are the small tests that combine into the big test.

### Advantages over Davidson (pp. 132–135)
- **Objection 4 (coextensive, nonsynonymous terms).** "Renate" and "cordate" apply to the same things actually, but their extensions diverge in other worlds, so their meanings differ (p. 132).
- **Objection 5 (non-truth-functional connectives).** A sentence saying it is possible that S is true iff S is true in some world. A necessity claim that, if there is a U.S. President, the United States exists is true iff that conditional holds in every world (p. 132).
- So not every intension maps worlds to extensions. Some map intensions to intensions: the operator "possible", and adverbs such as "slowly". "Jane swims slowly" is handled by turning the intension of "swims" into one picking out the slow swimmers in each world (p. 133).
- **Kinds of possibility** come from restricting the worlds considered. Physical possibility is truth in some world obeying our laws of nature. Moral possibility is truth in some world where all moral standards M are obeyed. Epistemic possibility is truth in some world compatible with what we know. So the implication from actual to possible fails for moral possibility, since the actual world is not morally possible in that sense (p. 133).
- **Counterfactuals** include (2), about Jerry knowing what awaited him in Birmingham and so keeping away, and (3), about what Lycan would do if he were king. Write a conditional as $A > C$. **Stalnaker (1968):** $A > C$ is true iff $C$ is true at the $A$-world otherwise most similar overall to the actual world (p. 134).
- Example (4): had I thrown this table lamp out this fourth-story window, it would have smashed on the pavement. Among worlds where I threw it, the most similar one keeps our laws of nature. So the lamp falls and smashes (p. 134). For (2) and (3), Lycan only poses the question of which A-world is most similar. Lewis (1973) elaborated the proposal (p. 134).
- **Belief sentences.** Frege's answer to substitutivity is that coreferring terms may have different senses. Possible worlds add content: the terms diverge in other worlds, so their intensions differ. If belief is a relation to a proposition (a sentence intension), one may believe one intension without the other. This assumes at least one term is flaccid (p. 134).
- **Adjustment.** If synonymy is sameness of truth set, all necessary truths are synonymous. Examples: "Either pigs have wings or they don't" and "If there are edible mice, then some mice are edible" would mean exactly the same. Likewise, "Snow is white" would mean the same as a necessarily equivalent complicated sentence, and believing one would count as believing the other (p. 135).
- **Carnap's fix, intensional isomorphism:** synonymous sentences need the same intension, composed in the same (or much the same) way from the same atomic intensions. The two necessary truths above are built from different atomic intensions (pig and wing vs. mouse and edible or eat), so they come out nonsynonymous (p. 135).

*Intuition note:* Sets of worlds are too coarse for necessary truths, since every one is true everywhere. Carnap adds how the meaning is built, so structure as well as truth set counts.

### Remaining objections (pp. 135–137)
- Inherited from Davidson: objections 1 (nondeclaratives), 2 (non-fact-stating sentences) and 6 (taking truth for granted). Objection 3 (deixis) also arises, since nothing yet handles it, and is the topic of the next chapter (p. 135).
- Inherited from the Proposition Theory: weirdness and alienness. Treating possible worlds as a metaphor (as in Ch. 4) is one thing, but using them directly in serious theory is another. Lycan does not pursue this (p. 135). The "dynamic feature" objection also applies, and has been pushed against both versions of the Truth-Condition Theory (p. 135).
- **Objection 7.** There seem to be contexts in which even synonymous terms cannot be intersubstituted without possible change of truth-value. Supposing "ophthalmologist" and "eye doctor" are synonymous, if Sheila does not know that, a belief report about eye doctors may be true while the one about ophthalmologists is false. Likewise, "Irving went to an ophthalmologist because an ophthalmologist is an eye doctor" is true, but the version ending "because an eye doctor is an eye doctor" is false (p. 136).
- **Objection 8** (Lycan's simple statement of a concern of Dummett and Putnam). Some Davidsonians and intension theorists see the semantic syntax as a machine program, run in speakers' and hearers' brains, for computing large meanings from small ones (p. 136). The concern: a sentence's meaning is what one knows when one understands it, and understanding is a psychological state that affects behaviour. But truth conditions are often "wide" ("ain't in the head"), as Twin-Earth cases show. "Dogs drink water" has different truth conditions here and on Twin Earth, yet the difference is irrelevant to behaviour and cannot affect it. So understanding is not, or not merely, knowing a truth condition, and meaning is not, or not simply, truth condition (p. 136).
  - **First reply (Lycan):** the argument assumes understanding is a narrow concept, which is not obvious. It also invites rethinking the simple equation of knowing meaning with understanding (p. 136).
  - **Second reply (Lycan):** the argument assumes wide states cannot figure in the causes of behaviour. Behaviour does depend counterfactually on wide states: had I wanted water ($\mathrm{H_2O}$), I would have fetched some. Lycan thinks this is the strongest causal notion guaranteed by common sense. Anyone claiming a stronger link between understanding and behaviour owes a defence (pp. 136–137).
- Footnote 1: Montague built higher-order intensions for more abstract parts of speech, even for "sake", "behalf" and "dint". The words are not taken to name their intensions (pp. 137–138).

## Toy example (ours)
Worlds $w_1,w_2,w_3$; individuals $a,b$. Intensions:
- "fat": $w_1\mapsto\{a\}$, $w_2\mapsto\{a,b\}$, $w_3\mapsto\{b\}$.
- "the PM" (flaccid): $w_1\mapsto a$, $w_2\mapsto b$, $w_3\mapsto$ nobody.

$S_1$ = "The PM is fat" is true in $w$ iff the PM of $w$ is in fat($w$). Our convention: with no PM, $S_1$ is not true.
- $w_1$: $a\in\{a\}$, true.
- $w_2$: $b\in\{a,b\}$, true.
- $w_3$: no PM, not true.

Truth set of $S_1$ is $\{w_1,w_2\}$.

$S_2$ = "Someone is fat" is true iff fat($w$) is nonempty: $\{a\}$, $\{a,b\}$ and $\{b\}$ are all nonempty. Truth set is $\{w_1,w_2,w_3\}$.

$\{w_1,w_2\}\subseteq\{w_1,w_2,w_3\}$, so $S_1$ entails $S_2$: no world makes $S_1$ true and $S_2$ false. "It is possible that the PM is fat" is true because $w_1$ is such a world.

## Concepts
- [[possible-worlds-truth-condition]] (new) — a sentence's truth condition and (for the theorist) meaning is the set of worlds where it is true (p. 130)
- [[intension]] (new) — function from worlds to extensions (to individuals, for singular terms); sometimes from intensions to intensions (pp. 130, 133)
- [[extension]] (new) — what a term applies to in a given world (p. 130)
- [[sense (Sinn) vs. reference (Bedeutung)]] — intensions are a possible-worlds explication of Fregean senses (p. 130)
- [[rigid designator]] — constant intension; a flaccid designator (new) varies across worlds (p. 131)
- [[compositionality]] (new) — a sentence's intension is computed from the intensions of its parts (pp. 130–131)
- [[counterfactual-conditional-semantics]] (new) — Stalnaker: true iff C holds at the most similar A-world (p. 134)
- [[intensional-isomorphism]] (new) — Carnap: synonymy needs the same intension built the same way from the same atoms (p. 135)
- [[wide-vs-narrow-content]] (new) — wide: not "in the head"; narrow: "in the head" (p. 136)

## Canonical instances
- [[renate-cordate]] — coextensive, nonsynonymous predicates separated by other worlds (p. 132)
- [[british-prime-minister]] — flaccid designator whose intension hops across worlds (p. 131)
- [[lamp-counterfactual]] — Stalnaker test with the lamp thrown from a window (p. 134)
- [[ophthalmologist-eye-doctor]] — synonyms failing substitution in belief and "because" contexts (p. 136)
- [[twin-earth-dogs-drink-water]] — wide truth condition irrelevant to behaviour (p. 136)

## Bridges (candidates)
- [structural-analogy] Intension as function from worlds to extensions ↔ computer science: a function or method evaluated on different inputs (Lycan mentions a machine program, p. 136).
- [structural-analogy] Entailment as subset of world-sets ↔ set theory/probability: events as sets of outcomes, with "A implies B" as $A\subseteq B$.
- [structural-analogy] Stalnaker's most-similar-world test ↔ causal inference: counterfactuals as "change one thing, hold the rest fixed".

## Questions this raises
- If a proposition is just a set of worlds, can it capture the difference between believing one necessary truth and another? Is Carnap's isomorphism enough?
- How should "overall similarity" of worlds be measured for (2) and (3)?
- Can the objection 7 cases be solved by isomorphism, if "eye doctor" and "ophthalmologist" count as built from different atoms?
- How would deixis ("I", "now") be added to intensions?

## Reading notes
- Printed page = pdf − 15 (pdf 144 = p. 129).
- On p. 131 the text says the set of worlds that is S2's meaning "is a subset of S1's meaning". That contradicts the sentence before it, which says S2 is true in any world in which S1 is, and so implies S1's set is the subset. I follow the earlier sentence and treat the later wording as a slip in the source.
- On p. 132 the sentence about necessity is awkwardly worded (it reads "true if, and only if in every world, there is a U.S. President, the United States exists"). I read it as: true iff, in every world, if there is a President, the U.S. exists.
