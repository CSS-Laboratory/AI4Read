---
id: magnus-2025-forallx/ch25-multiple
work: magnus-2025-forallx
unit: 25 Multiple generality
pages: 213-227
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
# Multiple generality

## L0 — One line
With many-place predicates and several quantifiers, the order of the gaps and the order of the quantifiers change what a sentence says.

## L1 — The gist (≤ 120 words)
The chapter asks how to symbolize sentences about relations ("loves", "owns") and sentences with more than one "every" or "some". Its answer has four parts. Keep track of each predicate's gaps by naming them with variables. Treat quantifier order as meaningful: "everyone loves someone" can mean that each person loves someone, or that one person is loved by everyone. Build complex symbolizations in "stepping-stone" stages, and never let one variable serve two quantifiers at once. The same care can expose ambiguity in ordinary arguments, as in Mary Astell's reply to Nicholls. This matters because the full power of FOL (first-order logic) really comes out with many-place predicates and multiple quantifiers.

**Prerequisites:** one-place predicates; ∀, ∃, ∧, ∨, ¬, →; symbolization keys; the idea of a quantifier's scope.

## L2 — Key ideas (5–10 bullets)
- Predicates can have two, three or more places. Deleting singular terms (such as names) from a sentence yields them, and there is no principled upper limit (pp. 213–214).
- The gaps in a predicate are different gaps. Their order matters, so we label them with variables, as in $L(x,y)$ (pp. 214–216).
- Two keys can use the same English word with swapped gaps ($L$ vs. $M$), so $L(i,k)$ and $M(i,k)$ symbolize different sentences. Always check the order of the gaps (pp. 215–216).
- Swapping $\forall\exists$ for $\exists\forall$ changes the meaning. Doing so inside an argument is the quantifier shift fallacy, which makes the argument invalid. Mathematics shows the same sensitivity (two definitions of continuity, pointwise and uniform) (pp. 216–217).
- Complex sentences are symbolized by paraphrasing in stages. A single variable cannot serve two quantifiers at once, so choose fresh variables (pp. 218–220).
- "Someone", "everyone" and "no one" need an explicit person predicate when the domain contains dogs as well as people, because they (at least arguably) do not include dogs. Other sentences do not (p. 221).
- Quantifier order can disambiguate an argument. Astell's reply to Nicholls, and the authors' symbolization of it, show that a claim with suppressed quantifiers can have several readings, and the readings can differ in truth (pp. 222–224).

## L3 — Walkthrough

### 25.1 Many-placed predicates
- One-place predicates have one gap and express properties. Relational predicates such as *loves*, *is to the left of* and *is in debt to* are two-place predicates: they need two terms to make a sentence (pp. 213–214).
- Deleting two singular terms from the sentence *Vinnie borrowed the family car from Nunzio* gives any of three different two-place predicates. Deleting all three gives a three-place predicate. There is no in-principle upper limit on the number of places (p. 214).
- The chapter says that, for the insight that many-place predicates and multiple quantifiers bring out the full power of FOL, we largely have Frege (1879) to thank, but also C. S. Peirce (p. 213).

### 25.2 Mind the gaps
- Frege emphasized that the gaps are different gaps. We can fill them with the same term or different terms, in different orders (p. 214).
- "Karl loves Imre", "Imre loves Karl" and "Karl loves Karl" all come from "___ loves ___". They have different meanings (p. 214).
- To track the gaps, give them variables. Key: domain people; $i$: Imre; $k$: Karl; $L(x,y)$: $x$ loves $y$. Then:
  - 1–3 are $L(k,i)$, $L(i,k)$, $L(k,k)$ (p. 215).
  - "Imre loves himself" is $L(i,i)$ (p. 215).
  - *Karl loves Imre, but not vice versa* is $L(k,i)\land\lnot L(i,k)$ (p. 215).
  - The passive *Karl is loved by Imre* is $L(i,k)$. Tone is lost, but truth conditions are preserved (p. 215).
- Add $M(x,y)$: $y$ loves $x$. It uses the same English word with the gaps swapped. Reading $M(i,k)$: put $i$ in gap $x$ and $k$ in gap $y$, giving "Karl loves Imre". So $L(i,k)$ and $M(k,i)$ both say "Imre loves Karl". $L(k,i)$ and $M(i,k)$ both say "Karl loves Imre". These differ because love can be unrequited (pp. 215–216).
- With $P(x,y)$: $x$ prefers $x$ to $y$, we get $P(i,k)$: *Imre prefers Imre to Karl*. The same effect comes from *$x$ prefers themselves to $y$* (p. 216).
- **Moral:** with several places, pay careful attention to the order of the gaps (p. 216).

*Intuition note.* A many-place predicate is like a form with numbered boxes. $L(x,y)$ says which box gets the lover and which gets the loved one. Swap the names and you get the reverse sentence.

### 25.3 The order of quantifiers
- "Everyone loves someone" is potentially ambiguous (p. 216):
  - 7: for every person $x$, there is some person that $x$ loves, symbolized $\forall x\exists y\,L(x,y)$.
  - 8: there is some particular person whom every person loves, symbolized $\exists y\forall x\,L(x,y)$ (pp. 216–217).
- Situation: the domain is Imre, Juan, Karl. Karl loves Imre but not Juan. Imre loves Juan but not Karl. Juan loves Karl but not Imre. Sentence 7 is true. Sentence 8 is not, since no single person is loved by everyone (pp. 216–217).
- Switching the quantifiers is called the **quantifier shift fallacy** (p. 217). Examples of the invalid form:
  - The step from each person having some truth they cannot know (∀∃) to there being one truth that no person can know (∃∀).
  - The step from every dog having its day (∀∃) to there being one day for all the dogs (∃∀) (p. 217).
- Order also matters in mathematics (p. 217):
  - $f$ is pointwise continuous if $\forall\epsilon\,\forall x\,\exists\delta\,\forall y\,(|x-y|<\delta\to|f(x)-f(y)|<\epsilon)$.
  - $f$ is uniformly continuous if $\forall\epsilon\,\exists\delta\,\forall x\,\forall y\,(|x-y|<\delta\to|f(x)-f(y)|<\epsilon)$.
  - Comparing the two formulas (added step), they differ in where $\exists\delta$ sits. The text says there is a big difference between the two definitions.

*Intuition note.* In "∀x∃y", the $y$ may differ for each $x$. In "∃y∀x", one $y$ must work for all $x$. In the same way, $\exists\delta$ placed after $\forall x$ may depend on $x$, whereas placed before it, it cannot.

### 25.4 Stepping-stones to symbolization
Key: domain people and dogs; $D(x)$: $x$ is a dog; $F(x,y)$: $x$ is a friend of $y$; $O(x,y)$: $x$ owns $y$; $g$: Geraldo (p. 218).

- **9. Geraldo is a dog owner.** Paraphrase: *There is a dog that Geraldo owns*. Symbolization: $\exists x(D(x)\land O(g,x))$ (p. 218).
- **10. Someone is a dog owner.** Stepping-stone: $\exists y\,(y \text{ is a dog owner})$. The text stresses that this is neither FOL nor English, only rough working (pp. 218–219). Result: $\exists y\exists x(D(x)\land O(y,x))$ (p. 218).
- **11. All of Geraldo's friends are dog owners.** Stepping-stone: $\forall x[F(x,g)\to x\text{ is a dog owner}]$ (p. 219).
  - Writing $\forall x[F(x,g)\to\exists x(D(x)\land O(x,x))]$ is a **clash of variables**. The inner $x$ would fall under both $\forall x$ and $\exists x$, and the sentence becomes ambiguous (if meaningful at all). A single variable cannot serve two quantifier-masters at once (p. 219).
  - Correct: $\forall x[F(x,g)\to\exists z(D(z)\land O(x,z))]$ (p. 219).
- **12. Every dog owner is a friend of a dog owner.** Stepping-stone: $\forall x[x\text{ is a dog owner}\to\exists y(y\text{ is a dog owner}\land F(x,y))]$. Result: $$\forall x\big[\exists z(D(z)\land O(x,z))\to\exists y\big(\exists z(D(z)\land O(y,z))\land F(x,y)\big)\big]$$ (p. 219).
  - The letter $z$ is reused in antecedent and consequent. This is fine, because each $z$ is governed by a different quantifier, as the scope diagram shows (p. 220).
- **13. Every dog owner's friend owns a dog of a friend.** Paraphrase: *For any $x$ that is a friend of a dog owner, $x$ owns a dog which is also owned by a friend of $x$* (p. 220). Stages:
  1. $\forall x[x\text{ is a friend of a dog owner}\to x\text{ owns a dog which is owned by a friend of }x]$.
  2. $\forall x[\exists y(F(x,y)\land y\text{ is a dog owner})\to\exists y((D(y)\land O(x,y))\land y\text{ is owned by a friend of }x)]$.
  3. Final: $$\forall x\big[\exists y(F(x,y)\land\exists z(D(z)\land O(y,z)))\to\exists y((D(y)\land O(x,y))\land\exists z(F(z,x)\land O(z,y)))\big]$$ (p. 220).
- **Person predicate.** The domain includes dogs, and "someone" (at least arguably) does not include dogs. So sentence 10 is better paraphrased *some $y$ is a person and a dog owner*. With $P(x)$: $x$ is a person: $\exists y(P(y)\land\exists x(D(x)\land O(y,x)))$ (p. 221).
  - Likewise *Everyone is a friend of Geraldo* is $\forall x(P(x)\to F(x,g))$. *No one is a friend of Geraldo* is $\forall x(P(x)\to\lnot F(x,g))$ (p. 221).
  - Only "someone", "everyone" and "no one" need this. Sentences 9 and 11 need no person predicate, because, even if only people can own dogs or be friends with Geraldo, that is not part of what the sentences say (p. 221).
  - Footnote, answering a possible objection: $P$ is chosen rather than "is human". In a Mickey Mouse domain, Goofy is a person and a dog, while Pluto is only a dog (p. 221).

*Intuition note.* Build the formula from outside in: write the outer quantifier, leave English where you are unsure, then replace each English fragment. Fresh variable letters keep each quantifier's job clear.

### 25.5 Suppressed quantifiers
- Logic can often help with English claims, especially where the quantifiers are implicit or their order is ambiguous or unclear (p. 222).
- **Astell's reply to Nicholls.** Nicholls argued that women are naturally inferior to men. Astell replies that his claim has different readings (pp. 222–223):
  - **Reading 1 (every–every):** every man is by nature superior to every woman. Astell calls this the "obvious meaning". Symbolization: $\forall x(M(x)\to\forall y(W(y)\to S(x,y)))$ (p. 223).
    - Astell's consequences: it would be a sin for any woman to have dominion over any man, and the greatest Queen ought to obey her footman. The Salique law (which barred female heirs to the French crown) would then hold over all the Earth. Glorious reigns would be violations of the Law of Nature (pp. 222–223).
  - **Reading 2 (some–some):** some men are superior to some women. Symbolization: $\exists x(M(x)\land\exists y(W(y)\land S(x,y)))$. This is true, but so is $\exists y(W(y)\land\exists x(M(x)\land S(y,x)))$, so it is "no great discovery" (p. 223).
  - **Further truth:** since the Queen is superior to all her subjects, $\exists y(W(y)\land\forall x(M(x)\to S(y,x)))$ is true (p. 223).
- The authors' conclusion: this last sentence is incompatible with the first reading. So what Nicholls claims amounts, in the authors' words, to treason against the Queen (p. 224).

*Intuition note.* "Some", "every" and their order produce several truth conditions from one English sentence. In the authors' symbolization, the strong reading is incompatible with a truth about the Queen, and the weak reading is no great discovery.

## Toy example (ours)
Domain $\{1,2,3\}$. $R(x,y)$: $x$ sends a card to $y$. Suppose the cards go $1\to2$, $2\to3$, $3\to2$ and nobody else sends anything.
- $\forall x\exists y\,R(x,y)$: for $x=1$, $y=2$; for $x=2$, $y=3$; for $x=3$, $y=2$. True.
- $\exists y\forall x\,R(x,y)$: try $y=1$: $R(1,1)$ false. $y=2$: $R(1,2)$ true but $R(2,2)$ false. $y=3$: $R(1,3)$ false. No $y$ works, so false.
- Add one card, $2\to2$. For $y=2$: $R(1,2)$, $R(2,2)$, $R(3,2)$ are all true, so $\exists y\forall x\,R(x,y)$ is now true.

So $\forall\exists$ can be true while $\exists\forall$ is false. This is exactly what the invalid step of the quantifier shift fallacy ignores.

## Concepts
- [[many-place-predicate]] (new) — a predicate with two or more gaps, formed by deleting singular terms from a sentence (p. 214)
- [[gap-order]] (new) — the order in which terms fill a predicate's gaps; variables track it (pp. 214–216)
- [[quantifier-order]] (new) — the sequence of quantifiers, which changes truth conditions (p. 217)
- [[quantifier-shift-fallacy]] (new) — invalidly swapping ∀∃ for ∃∀ (p. 217)
- [[variable-clash]] (new) — one variable under two quantifiers at once, causing ambiguity (p. 219)
- [[stepping-stones]] (new) — partial paraphrases mixing English and FOL, used only as rough working (pp. 218–219)
- [[validity / soundness]] — here: the shift argument is invalid (p. 217)
- [[logical form vs. grammatical form]] — here: ambiguous English quantifier order gets resolved in FOL (pp. 216, 222)

## Canonical instances
- [[karl-imre-juan-love]] — ∀∃ true, ∃∀ false in a three-person situation (pp. 216–217)
- [[every-dog-has-its-day]] — quantifier shift fallacy example (p. 217)
- [[pointwise-vs-uniform-continuity]] — quantifier order in mathematical definitions (p. 217)
- [[geraldo-dog-owners]] — stepping-stone symbolization, sentences 9–13 (pp. 218–220)
- [[astell-vs-nicholls]] — disambiguating suppressed quantifiers (pp. 222–224)

## Bridges (candidates)
- [same-math] ∀∃ vs. ∃∀ here ↔ analysis: pointwise vs. uniform continuity (the text gives both formulas) — the same quantifier pattern.
- [structural-analogy] variable clash ↔ programming: two nested scopes using the same variable name — names must be tied to one binder.
- [metaphor] Astell's disambiguation ↔ argument analysis: strong vs. weak readings of a claim.

## Questions this raises
- When are $\forall x\exists y$ and $\exists y\forall x$ equivalent? Does the order matter in every case (e.g. $\forall\forall$)?
- How would the sentence 13 symbolization be tested against a concrete model?
- Why does "someone" need a person predicate while "a dog owner" does not? Where is the line between what a sentence says and what is presupposed?
- Can the other (non-obvious) readings of everyday ambiguous sentences be listed systematically?

## Exercises worth doing
- Ex. A.5–A.7 (p. 224) — relations between animals; "love him back" and non-reciprocation — medium
- Ex. B.5 (p. 225) — "Only dogs like samurai movies" (direction of the conditional) — medium
- Ex. B.14–B.16 (p. 225) — quantifier order with "larger than" — hard
- Ex. C.8–C.9 (p. 226) — "any … better than any …" (double universal) — medium
- Ex. D.8 (p. 226) — nested "likes the people that he likes" — hard
- Ex. E.11–E.12 (p. 227) — family relations with existentials — hard

## Reading notes
- 
- The section title "25.5 Supressed quantifiers" is misspelled in the source ("Supressed").
- The text layer drops the blank lines of the gaps but keeps the subscript letters. Page images were supplied only for pp. 217–221, 223, 224 and 227. The keys and formulas on pp. 213–216, 222, 225 and 226 (including $P(x,y)$ on p. 216) are read from the text layer.
- The source quotes the Astell passage in full (pp. 222–223) and cites it in footnote 5 as the 1706 preface to *Reflections upon Marriage*.
- No solutions appear on these pages.
