---
id: magnus-2025-forallx/ch05-connectives
work: magnus-2025-forallx
unit: "5 Connectives"
pages: 32-48
fields: [analytic-philosophy]
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
# Connectives (TFL's five connectives and how to symbolize English with them)

## L0 — One line
Many English sentences built with not, and, or, if…then and if and only if can be paraphrased and symbolized with the five connectives of TFL (¬, ∧, ∨, →, ↔), at the cost of nuance such as tone and contrast, causal connection and time order.

## L1 — The gist (≤ 120 words)
How do we turn English sentences into TFL sentences? (TFL is the formal language used here; its sentence letters stand for whole sentences.) The chapter introduces five connectives, which build complex sentences from simpler ones. For each one it gives a paraphrase test: if a sentence can be rephrased in the given English pattern, it can be symbolized with that connective. Brackets mark scope, that is, how much of a sentence a connective (such as not) applies to. Only if, unless and exclusive or (an or that excludes both parts being true) need care. TFL's ∨ is always inclusive, and → says nothing about causes. Tone, contrast and time order are lost in symbolizing.

**Prerequisites:** the idea of a sentence letter and a symbolization key (from the previous chapter); the difference between a sentence and a part of a sentence.

## L2 — Key ideas
- TFL has five connectives, which build new sentences from old: ¬, ∧, ∨, →, ↔ (p. 32).
- Each connective has a paraphrase test: a sentence can be symbolized with that connective if it can be paraphrased in the matching English pattern (pp. 33, 36, 38, 40, 42).
- In the worked examples the author paraphrases first. Pronouns are replaced, hidden negations are exposed, and *Barbara is athletic and energetic* becomes two sentences joined by ∧ (pp. 34–36).
- TFL loses nuance: tone, the contrast of *but* and *although*, and the temporal order of *and* are not captured. ∧ is symmetric (pp. 35–37).
- Brackets mark scope. ¬(S₁ ∧ S₂) and (¬S₁ ∧ S₂) say very different things (p. 37).
- ∨ is always inclusive, but an exclusive or can be built from ∨, ∧, ¬ (pp. 38–39).
- *A only if B* is (A → B), not (B → A). The arrow says only that if the antecedent is true, the consequent is true, and nothing about causes (pp. 40–41).
- *Unless A, B* can be symbolized as (¬A → B) or (A ∨ B). Ordinary speakers often mean something more like the biconditional or an exclusive disjunction (p. 43).

## L3 — Walkthrough

### Chapter introduction (p. 32)
- Connectives are expressions that form new sentences out of old ones. TFL has five (p. 32):

| symbol | name | rough meaning |
|---|---|---|
| ¬ | negation | *It is not the case that…* |
| ∧ | conjunction | *Both… and…* |
| ∨ | disjunction | *Either… or…* |
| → | conditional | *If… then…* |
| ↔ | biconditional | *… if and only if …* |

- English also has *unless*, *neither… nor…* and *because*. The text says the first two can be expressed with the connectives discussed, while *because* cannot, since it is not *truth functional* (p. 32). This unit does not explain that term.

### 5.1 Negation (pp. 33–34)
- Key B: *Mary is in Barcelona.* The sentences *It is not the case that Mary is in Barcelona* and *Mary is not in Barcelona* are obviously equivalent. Both are symbolized ¬B (p. 33).
- **Test:** a sentence can be symbolized as ¬A if it can be paraphrased in English as *It is not the case that…* (p. 33).
- Key R: *The widget is replaceable.* *The widget is irreplaceable* does not contain the word not, but saying it means it is not the case that the widget is replaceable. So it is ¬R (pp. 33–34).
- *The widget is not irreplaceable* is first paraphrased as *It is not the case that the widget is irreplaceable*, and then as *It is not the case that it is not the case that the widget is replaceable*. So it is ¬¬R (p. 34).
- **Care needed:** *Jane is unhappy* would be a mistake to symbolize as ¬H (H: Jane is happy). If Jane is unhappy, she is not happy, but the sentence does not mean the same as *It is not the case that Jane is happy*: Jane might be neither happy nor unhappy, in a state of blank indifference. A new sentence letter is needed (p. 34).

*Intuition note:* A negation word may be hidden or absent in the English. The author symbolizes the widget sentence with ¬ although it lacks *not*. *Unhappy* says more than *not happy*.

### 5.2 Conjunction (pp. 34–37)
- Key A: *Adam is athletic*; B: *Barbara is athletic*. *Adam is athletic, and also Barbara is athletic* is (A ∧ B). A and B are its *conjuncts* (pp. 34–35).
- Words like both and also function to draw attention to the fact that two things are conjoined. The author allows that they may affect emphasis, but TFL does not and cannot symbolize that (p. 35).
- **Ex. 12** *Barbara is athletic and energetic.* Symbolizing it as *B and energetic* would be a mistake: B is a sentence letter, so any further structure is lost, and *energetic* is not a sentence. The target is *B and Barbara is energetic*, with E: *Barbara is energetic*. This gives (B ∧ E) (p. 35).
- **Ex. 13** *Barbara and Adam are both athletic* paraphrases to *Barbara is athletic, and Adam is athletic*, so (B ∧ A) (p. 35).
- **Ex. 14** *Although Barbara is energetic, she is not athletic.* Replace *she* with *Barbara*, then expose the negation: *Both Barbara is energetic and it is not the case that Barbara is athletic*. This gives (E ∧ ¬B). The difference in tone is lost (pp. 35–36).
- **Ex. 15** *Adam is athletic, but Barbara is more athletic than him.* Replace *him* with *Adam*. The second conjunct needs a new letter R: *Barbara is more athletic than Adam*. This gives (A ∧ R). The contrast suggested by *but* is ignored (p. 36).
- **Test:** (A ∧ B) if the sentence can be paraphrased as *Both…, and…*, *…, but…* or *although…, …* (p. 36).
- **Time order:** *Harry stood up and objected to the proposal* (16) and *Harry objected to the proposal and stood up* (17) can differ. If he stood up after he objected, 17 is true and 16 is false, so this use of *and* is asymmetric. ∧ is always symmetric ("commutative"), so TFL cannot deal with asymmetric *and*. The text assumes *and* is symmetric in all its examples and exercises (pp. 36–37).
- **Scope and brackets** (key S₁: you will get soup, S₂: you will get salad) (p. 37):
  - *It's not the case that you will get both soup and salad* negates the whole conjunction: ¬(S₁ ∧ S₂).
  - *You will not get soup but you will get salad* negates one conjunct only: (¬S₁ ∧ S₂).
  - Brackets help keep track of the *scope* of the negation.

*Intuition note:* In the worked examples, each part is first rewritten as a full sentence. Brackets show how far the negation reaches.

### 5.3 Disjunction (pp. 37–39)
- Key F: Fatima will play videogames; O: Omar will play videogames; M: Fatima will watch movies. *Either Fatima will play videogames, or she will watch movies* is (F ∨ M). F and M are the *disjuncts* (p. 38).
- *Either Fatima or Omar will play videogames* paraphrases to *Either Fatima will play videogames, or Omar will play videogames*: (F ∨ O) (p. 38).
- **Test:** (A ∨ B) if it can be paraphrased as *Either…, or…* (p. 38).
- **Exclusive or** excludes the possibility that both disjuncts are true. The text's example is a menu saying *Entrees come with either soup or salad*, where wanting both soup and salad means paying extra. **Inclusive or** allows both. Sentence 21 is probably inclusive: it merely says that at least one of them plays. The symbol ∨ always symbolizes an inclusive or (p. 38).
- With negation (p. 39):
  - *Either you will not get soup, or you will not get salad* (22): (¬S₁ ∨ ¬S₂).
  - *You will get neither soup nor salad* (23) negates the whole disjunction: ¬(S₁ ∨ S₂).
  - *You get either soup or salad, but not both* (24) is an exclusive or. First part: (S₁ ∨ S₂). Second part, *it is not the case both that you get soup and that you get salad*: ¬(S₁ ∧ S₂). *But* can usually be symbolized with ∧, so the whole is ((S₁ ∨ S₂) ∧ ¬(S₁ ∧ S₂)).
- So ∨ is always inclusive, but an exclusive or can be symbolized using a few other symbols as well (p. 39).

*Intuition note:* *Neither… nor…* is a negated or. *Either not… or not…* has a different symbolization. An exclusive or says that you get one or the other, and not both.

### 5.4 Conditional (pp. 39–41)
- Key P: Jean is in Paris; F: Jean is in France. *If Jean is in Paris, then Jean is in France* (25) is (P → F). P is the *antecedent*, F the *consequent* (p. 40).
- *Jean is in France only if Jean is in Paris* (26) has the word if in its second half, but symbolizing it as (P → F) would be a mistake. Geography alone makes 25 true. For 26, were Jean in Dieppe, Lyon or Toulouse, Jean would be in France without being in Paris, which would make 26 false. So the two sentences must mean different things (p. 40).
- Sentence 26 can be paraphrased as *If Jean is in France, then Jean is in Paris*: (F → P) (p. 40).
- **Test:** (A → B) if the sentence can be paraphrased as *If A, then B* or *A only if B* (p. 40).
- Four further sentences mean the same as *If Jean is in Paris, then Jean is in France*, so all are (P → F) (pp. 40–41):
  - 27: *For Jean to be in Paris, it is necessary that Jean be in France.*
  - 28: *It is a necessary condition on Jean's being in Paris that she be in France.*
  - 29: *For Jean to be in France, it is sufficient that Jean be in Paris.*
  - 30: *It is a sufficient condition on Jean's being in France that she be in Paris.*
- → tells us only that if the antecedent is true, the consequent is true. It says nothing about a causal connection. We lose a huge amount when we symbolize English conditionals this way. The text promises to return to this in section 10.3 and chapter 13 (p. 41).

*Intuition note:* Sentences 27–30 show that P is sufficient for F and F is necessary for P in (P → F). *A only if B* is symbolized (A → B), so B is the consequent and the arrow runs from A to B.

### 5.5 Biconditional (pp. 41–42)
- Key D: Laika is a dog; M: Laika is a mammal. Sentence 31, *dog only if mammal*, is (D → M). Sentence 32, *dog if mammal*, is the converse. Sentence 33, *dog if and only if mammal*, says something stronger than 31 or 32. It is the conjunction of 31 and 32: (D → M) ∧ (M → D) (p. 41).
- This is called a *biconditional*, because it amounts to stating both directions of the conditional. We could treat every biconditional this way, so we do not really need a new symbol, just as none is needed for exclusive or. Because it occurs so often, the text uses ↔: (D ↔ M) (pp. 41–42).
- *iff* abbreviates *if and only if*. One-f *if* is the English conditional, two-f *iff* is the English biconditional (p. 42).
- **Test:** (A ↔ B) if it can be paraphrased as *A iff B* (p. 42).
- **Caution:** ordinary speakers often use *if… then…* when they really mean something more like *iff*. Example: parents say *if you don't eat your greens, you won't get any dessert*. If the child ate the greens and still got no dessert, a tantrum would rightly ensue, even though the parents were only committed to the conditional (roughly *if you get dessert, then you will have eaten your greens*), not the biconditional. So be aware of this when interpreting people, but in your own writing use the biconditional iff you mean to (p. 42).

### 5.6 Unless (pp. 42–43)
- Sentences 34 and 35 (*Unless you wear a jacket, you will catch a cold*; *You will catch a cold unless you wear a jacket*) are clearly equivalent. Key J: you will wear a jacket; D: you will catch a cold (pp. 42–43).
- Three symbolizations are given, and the text says all three are correct (p. 43):
  - (¬J → D): both sentences mean that if you do not wear a jacket, you will catch a cold.
  - (¬D → J): both mean that if you do not catch a cold, you must have worn a jacket.
  - (J ∨ D): both mean that either you will wear a jacket or you will catch a cold.
- The text says that in chapter 12 we will see that all three are equivalent in TFL (p. 43).
- **Rule:** if a sentence can be paraphrased as *Unless A, B*, it can be symbolized as (¬A → B) or (A ∨ B) (p. 43).
- **Complication:** ordinary speakers often use *unless* to mean something more like the biconditional or an exclusive disjunction. *I will go running unless it rains* probably means *I will go running iff it does not rain*, or *either I will go running or it will rain, but not both*. Be aware of this when interpreting what others say, but be precise in your writing (p. 43).

*Intuition note:* Both unless sentences mean at least that if A fails, B holds, which is (¬A → B). Everyday speech may mean more, like the biconditional or an exclusive or, so be precise when you write.

### Practice exercises (pp. 44–48)
- The unit ends with exercises A–I (see Exercises worth doing). No solutions appear on these pages.

## Toy example (ours, not from the text)
Key: T: *Lena has tea.* C: *Lena has cake.*

Compare two English sentences.
1. *It is not the case that Lena has both tea and cake.*
   - *Both tea and cake* is (T ∧ C). Negating the whole thing gives **¬(T ∧ C)**.
2. *Lena has no tea but she has cake.*
   - Paraphrase: *Both it is not the case that Lena has tea, and Lena has cake.* This gives **(¬T ∧ C)**.

Scenario: Lena has neither tea nor cake.
- Sentence 1 says she does not have both. That is true in the scenario.
- Sentence 2 says she has cake. That is false in the scenario.

So the two symbolizations differ in meaning, and the brackets show the scope of the negation. Add a third sentence: *Lena has neither tea nor cake.* This negates a whole disjunction, so it is **¬(T ∨ C)**. It is true in the scenario.

## Concepts
- [[connective]] (new) — an expression that forms a new sentence from old ones; TFL has five (p. 32)
- [[negation]] (new) — ¬; paraphrase *It is not the case that…* (p. 33)
- [[conjunction]] (new) — ∧; *Both… and…*, also *but* and *although*; symmetric; its parts are conjuncts (pp. 35–37)
- [[disjunction]] (new) — ∨; *Either… or…*, always inclusive; its parts are disjuncts (p. 38)
- [[conditional]] (new) — →; *If A, then B* or *A only if B*; A is the antecedent, B the consequent; says nothing causal (pp. 40–41)
- [[biconditional]] (new) — ↔; *A iff B*; both directions of the conditional (pp. 41–42)
- [[inclusive-vs-exclusive-or]] (new) — or allowing both parts true vs. excluding both true (p. 38)
- [[scope]] (new) — how much of a sentence a connective such as ¬ applies to; shown by brackets (p. 37)
- [[truth-functional]] (new) — named here only as a property *because* lacks; not explained in this unit (p. 32)
- [[necessary-sufficient-condition]] (new) — in *If P then F*, P is sufficient for F and F is necessary for P (pp. 40–41)
- [[symbolization-key]] (new) — a list pairing sentence letters with English sentences (p. 33)
- [[hidden-negation]] (new) — a sentence such as *the widget is irreplaceable* is symbolized with ¬ although it lacks the word not (p. 34)

## Canonical instances
- [[widget-irreplaceable]] — a negation without the word not (p. 34)
- [[jane-unhappy]] — *unhappy* is not ¬H (p. 34)
- [[harry-stood-up-and-objected]] — asymmetric *and* that ∧ cannot capture (pp. 36–37)
- [[soup-and-salad]] — scope of negation; exclusive or built from ∨, ∧, ¬ (pp. 37, 39)
- [[jean-paris-france]] — *if* vs. *only if*; necessary vs. sufficient (pp. 40–41)
- [[laika-dog-mammal]] — biconditional as two conditionals (p. 41)
- [[eat-your-greens]] — speakers using *if* for *iff* (p. 42)
- [[jacket-cold-unless]] — three symbolizations of *unless* (p. 43)

## Bridges (candidates)
- [structural-analogy] paraphrase into ¬/∧/∨/→/↔ ↔ analytic-philosophy: analysis that rewrites a sentence to show what it asserts — both restate a sentence in a clearer form.
- [structural-analogy] *A only if B* as (A → B) ↔ analytic-philosophy: necessary vs. sufficient conditions in analyses of concepts — same direction-of-implication pattern.
- [metaphor] speakers using *if* for *iff* and *unless* for exclusive or ↔ pragmatics: conversational implicature — a stronger meaning conveyed beyond the literal one (canon link; not stated in this unit).

## Questions this raises
- What does *truth functional* mean, and why does *because* fail it?
- Section 10.3 and chapter 13 are said to return to what is lost in symbolizing English conditionals. What exactly is lost?
- Why are the three *unless* symbolizations equivalent (chapter 12)?
- How far can the five connectives be reduced? Is there a more minimal set?

## Exercises worth doing
- Ex. B.11–B.12 (p. 45) — sentences with *since* and *of course*: how to handle expressions beyond the five connectives — difficulty: medium
- Ex. C.3 and D.4 (pp. 45, 46) — *unless* combined with negation — difficulty: medium
- Ex. C.8 (p. 45) — a compound of two conditionals with negation — difficulty: medium
- Ex. G.1 (p. 47) — symbolizing a whole argument including *unless* — difficulty: medium
- Ex. H.3 (p. 48) — a long argument symbolized as well as possible, with context not to be symbolized — difficulty: hard
- Ex. I (p. 48) — exclusive or with only two connectives, or only one — difficulty: hard

## Reading notes
- Printed page = pdf page − 10 (pdf 42 = printed 32).
- Misprint-like point: on p. 41 the biconditional appears as (D → M) ∧ (M → D) without outer brackets. The text elsewhere puts brackets around conjunctions (e.g. (A ∧ B), p. 35), so this is an inconsistency.
- Page 33 says *representation key* where *symbolization key* is used elsewhere.
- The letter R is reused with different meanings (the widget, p. 33; *Barbara is more athletic than Adam*, p. 36). These are separate examples with separate keys.
- Footnote 1 (p. 37) cites two linguistics works on symmetric and asymmetric conjunction (Lakoff 1971; Schmerling 1975).
- The unit says section 10.3, chapter 12 and chapter 13 are to come. These are not in the pages given.
