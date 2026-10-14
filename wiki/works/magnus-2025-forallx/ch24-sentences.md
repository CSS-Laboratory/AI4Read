---
id: magnus-2025-forallx/ch24-sentences
work: magnus-2025-forallx
unit: "24 Sentences with one quantifier"
pages: 199–212
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Sentences with one quantifier

## L0 — One line
To symbolize English in first-order logic (FOL), paraphrase it, pick the domain (the things the quantifiers range over) and the predicates carefully, and usually pair ∀ with → and ∃ with ∧; the scope of a quantifier (the part of the sentence it governs) matters.

## L1 — The gist (≤ 120 words)
How do we turn everyday English sentences containing "every", "some", "no", "only", "any" into FOL? The chapter gives patterns. "Every F is G" becomes ∀x(F(x)→G(x)). "Some F is G" becomes ∃x(F(x)∧G(x)). "No F is G" has two equivalent forms. It also warns about empty predicates (vacuous truth), the effect of the chosen domain, the scope of a quantifier next to a conditional, and ambiguous predicates such as "skilled". Paraphrasing in plain English first often helps to show which pattern fits. This matters because a wrong symbolization can turn a bad English argument into a valid FOL one.

**Prerequisites:** TFL connectives (∧, ∨, ¬, →); names, predicates, domain and the quantifiers ∀, ∃ from chapter 23; logical equivalence.

## L2 — Key ideas (5–10 bullets)
- "Every F is G" is symbolized ∀x(F(x)→G(x)); "some F is G" is ∃x(F(x)∧G(x)). Swapping → and ∧ changes the meaning (pp. 200–201).
- "No F is G" has two equivalent symbolizations. "Only Fs are Gs" is symbolized like "everything that is G is F" (pp. 201–202).
- A predicate that applies to nothing in the domain is empty. Then ∀x(F(x)→…) is vacuously true (there is nothing in the domain that could be a counter-example), while ∃x(F(x)∧…) is false (pp. 202–203).
- The right symbolization depends on the symbolization key, above all on the domain. With a mixed domain, "everyone" must be read as "every person" (pp. 204–205).
- Paraphrase first. Pronouns and "any/anyone" can hide whether a universal quantifier, an existential quantifier, or a name is needed (pp. 205–207).
- ∀xB(x)→B(l) and ∀x(B(x)→B(l)) differ only in the scope of ∀x, yet they say very different things (pp. 207–208).
- Ambiguous predicates ("skilled", "big") can make an invalid argument look valid. Use separate predicates when the senses differ (pp. 209–210).

## L3 — Walkthrough

### Opening (p. 199)
Symbolizing complicated sentences means combining predicates, names, quantifiers and connectives. The authors say there is a knack to it and no substitute for practice (p. 199).

### 24.1 Common quantifier phrases (pp. 199–202)
Four sentences: (1) Every coin in my pocket is a quarter. (2) Some coin on the table is a dime. (3) Not all the coins on the table are dimes. (4) None of the coins in my pocket are dimes. The domain is all coins, since nothing else is discussed and no names are needed. Key: P(x) x is in my pocket; T(x) x is on the table; Q(x) x is a quarter; D(x) x is a dime (pp. 199–200).

- **Sentence 1.** Paraphrase: "for any coin, if that coin is in my pocket then it is a quarter". Symbolization: $\forall x\,(P(x)\to Q(x))$ (p. 200).
  - The conjunction $\forall x\,(P(x)\land Q(x))$ would instead say every coin is both a quarter and in my pocket (p. 200).
  - Rule: a sentence can be symbolized as $\forall x\,(F(x)\to G(x))$ if it can be paraphrased as "every F is G" (p. 200).
- **Sentence 2.** Paraphrase: "there is some coin which is both on the table and a dime". Symbolization: $\exists x\,(T(x)\land D(x))$ (p. 200).
  - Why not a conditional: $\exists x\,(T(x)\to D(x))$ is true if some object makes $\neg T(x)\lor D(x)$ true, because $A\to B$ is equivalent to $\neg A\lor B$ in FOL too (p. 200).
  - A coin that is not on the table makes it true, so it is very easy to satisfy (pp. 200–201).
  - Rule of thumb: do not put conditionals in the scope of existential quantifiers unless you are sure you need one (p. 201).
  - Rule: "some F is G" can be symbolized as $\exists x\,(F(x)\land G(x))$ (p. 201).
- **Sentence 3.** Two symbolizations: $\neg\forall x\,(T(x)\to D(x))$ ("not every coin on the table is a dime") and $\exists x\,(T(x)\land\neg D(x))$ ("some coin on the table is not a dime") (p. 201).
  - They are logically equivalent, via $\neg\forall x\,A \Leftrightarrow \exists x\,\neg A$ (chapter 23) and $\neg(A\to B)\Leftrightarrow A\land\neg B$ (p. 201).
- **Sentence 4.** Two symbolizations: $\neg\exists x\,(P(x)\land D(x))$ and $\forall x\,(P(x)\to\neg D(x))$. They are equivalent, and both are correct (p. 201).
  - Rule: "no F is G" can be symbolized as $\neg\exists x\,(F(x)\land G(x))$ and also as $\forall x\,(F(x)\to\neg G(x))$ (p. 201).
- **"Only".** Sentence 5: "Only dimes are on the table." Strategy: ask when the sentence would be false, namely when something on the table is a non-dime. So treat it like "No non-dimes are on the table" (pp. 201–202).
  - Symbolizations: $\neg\exists x\,(T(x)\land\neg D(x))$ or $\forall x\,(T(x)\to\neg\neg D(x))$. The second is as good as $\forall x\,(T(x)\to D(x))$, since double negations cancel (p. 202).
  - Rule: "only Fs are Gs" can be symbolized as $\neg\exists x\,(G(x)\land\neg F(x))$ and also as $\forall x\,(G(x)\to F(x))$ (p. 202).

*Intuition note.* ∀ talks about the whole domain, so the conditional "if it is F" narrows it to the Fs. ∃ only claims that something exists, so the narrowing is naturally done with a conjunction. A conditional under ∃ is very easy to satisfy, because something irrelevant (such as a non-F) can make it true.

### 24.2 Empty predicates (pp. 202–203)
A name must pick out exactly one object, but a predicate need not apply to anything. A predicate applying to nothing in the domain is an **empty predicate** (p. 202).

Sentences 6 "Every monkey knows sign language" and 7 "Some monkey knows sign language". Key: domain animals; M(x) x is a monkey; S(x) x knows sign language. Symbolizations: $\forall x\,(M(x)\to S(x))$ and $\exists x\,(M(x)\land S(x))$ (p. 202).

- It is tempting to think 6 entails 7, but that would be a mistake (pp. 202–203).
- If the domain had no monkeys, the first sentence would be vacuously true and the second false (p. 203).
- Second example: add R(x) "x is a refrigerator". $\forall x\,(R(x)\to M(x))$ ("every refrigerator is a monkey") is true given the key. The domain is animals, so it contains no refrigerators, and the sentence is vacuously true (p. 203).
- For the real sentence "All refrigerators are monkeys" you would most likely include kitchen appliances in the domain. Then R is not empty and the sentence is false (p. 203).
- Rule: when F is an empty predicate, any sentence $\forall x\,(F(x)\to\ldots)$ is vacuously true (p. 203).

*Intuition note.* "Every F is G" makes a promise only about Fs. If there are no Fs, nothing can break the promise. "Some F is G" needs a witness, so it fails when there are no Fs.

### 24.3 Picking a domain (pp. 204–205)
How a sentence is symbolized depends on the key. Sentence 8: "Every rose has a thorn." Key: R(x) x is a rose; T(x) x has a thorn (p. 204).

- If the domain is only things on my kitchen table, $\forall x\,(R(x)\to T(x))$ only comes close to covering the fact that every rose on the table has a thorn. It would be trivially true if there were no roses on the table (p. 204). To symbolize sentence 8 adequately, all roses must be in the domain.
- **Option 1:** restrict the domain to all roses and only roses. Then $\forall x\,T(x)$ is true iff every rose has a thorn. This is shorter, and useful if every sentence is about roses (p. 204).
- **Option 2:** a larger domain, needed if we also want sentence 9, "Every cowboy sings a sad, sad song". Key: domain people and plants; C(x) cowboy; S(x) sings a sad, sad song; R(x) rose; T(x) thorn (pp. 204–205).
  - Now $\forall x\,T(x)$ would mean "every person or plant has a thorn". So sentence 8 is $\forall x\,(R(x)\to T(x))$ and sentence 9 is $\forall x\,(C(x)\to S(x))$ (p. 205).
- "Everyone" can be ∀ alone if the domain contains only people. With other things in the domain, it must be treated as "every person" (p. 205).

### 24.4 The utility of paraphrase (pp. 205–207)
Sometimes you can go straight from English to FOL. Otherwise paraphrase one or more times, each time getting closer to something easy to symbolize (p. 205). Key: domain people; B(x) x is a bassist; R(x) x is a rock star; k Kim Deal (pp. 205–206).

- **Sentences 10 and 11** share the consequent "she is a rock star" but differ in meaning (p. 206).
  - 10: "If Kim Deal is a bassist, then she is a rock star". Paraphrase: "…then Kim Deal is a rockstar". Symbolization: $B(k)\to R(k)$ (p. 206).
  - 11: "If a person is a bassist, then she is a rock star". It is about no particular person, so it needs a variable. Paraphrase: "For any person x, if x is a bassist, then x is a rockstar". Symbolization: $\forall x\,(B(x)\to R(x))$, the same as for "Everyone who is a bassist is a rock star" (p. 206).
- **Sentences 12 and 13** share the antecedent "If anyone is a bassist…" (p. 206).
  - 12: "If anyone is a bassist, then Kim Deal is a rock star". Paraphrase: "If there is at least one bassist, then Kim Deal is a rock star". The main operator is a conditional with a quantified antecedent: $\exists x\,B(x)\to R(k)$ (p. 206).
  - 13: "If anyone is a bassist, then she is a rock star". Paraphrase: "For all people x, if x is a bassist, then x is a rock star", or "All bassists are rock stars". Symbolization: $\forall x\,(B(x)\to R(x))$, as for 11 (p. 207).
- Moral: "any" and "anyone" should typically be symbolized with quantifiers. If you cannot decide between ∃ and ∀, paraphrase using words other than "any" or "anyone" (p. 207).

### 24.5 Quantifiers and scope (pp. 207–208)
New name: l for Lars. Sentences 14 "If everyone is a bassist, then Lars is a bassist" and 15 "Everyone is such that, if they are a bassist, then Lars is a bassist" (p. 207).

- 14 is a conditional with antecedent "everyone is a bassist": $\forall x\,B(x)\to B(l)$. It is necessarily true. If everyone is a bassist, then Lars is one (p. 207).
- 15 is $\forall x\,(B(x)\to B(l))$. It can well be false. Suppose Kim Deal is a bassist (B(k) true) and Lars is a drummer (B(l) false). Then $B(k)\to B(l)$ is false, so the universal sentence is false (p. 207).
- $\forall x\,(B(x)\to B(l))$ is false exactly when $\exists x\,B(x)\to B(l)$ is false, so they are equivalent. Sentence 15 is a convoluted way of saying "Lars is a bassist, if anyone is" (pp. 207–208).
- The difference is the **scope** of the quantifier, which works like the scope of negation (p. 208):
  - In $\neg B(k)\to B(l)$, the scope of ¬ is only the antecedent. Likewise in $\forall x\,B(x)\to B(l)$, the scope of ∀x is only the antecedent (p. 208).
  - In $\neg(B(k)\to B(l))$, the scope of ¬ is the whole sentence. Likewise in $\forall x\,(B(x)\to B(l))$, the scope of ∀x is the whole sentence (p. 208).
- Moral: with conditionals, sort out the scope correctly (p. 208).

*Intuition note.* Parentheses decide how much of the sentence the quantifier governs. With ∀ outside the brackets, we test the whole conditional on every object, and one counter-example sinks it. With ∀ inside the antecedent, we only ask whether everyone is a bassist.

### 24.6 Ambiguous predicates (pp. 208–210)
Sentence 16, "Adina is a skilled surgeon", can simply be K(a), with K(x) "x is a skilled surgeon" (p. 208).

- **Billy argument:** the hospital will only hire a skilled surgeon; all surgeons are greedy; Billy is a surgeon but not skilled; so Billy is greedy but the hospital will not hire him (pp. 208–209). Here we must separate "skilled" from "surgeon". Key: domain people; G greedy; H(x) the hospital will hire x; R surgeon; K skilled; b Billy (p. 209).
  - Symbolization: $\forall x\,[\neg(R(x)\land K(x))\to\neg H(x)]$; $\forall x\,(R(x)\to G(x))$; $R(b)\land\neg K(b)$; therefore $G(b)\land\neg H(b)$ (p. 209).
- **Carol argument:** "Carol is a skilled surgeon and a tennis player; so Carol is a skilled tennis player" (p. 209).
  - With a single K and T(x) "x is a tennis player", c Carol: $(R(c)\land K(c))\land T(c)$ therefore $T(c)\land K(c)$. This is a valid FOL argument, though the English one is terrible. The authors call this symbolization "a disaster!" (p. 209).
  - Correct version: K₁(x) "skilled as a surgeon" and K₂(x) "skilled as a tennis player". Then $(R(c)\land K_1(c))\land T(c)$ therefore $T(c)\land K_2(c)$. This is invalid, like the English (pp. 209–210).
- Similar problems arise with good, bad, big, small: big dogs, big mice and big problems are big in different ways (p. 210).
- Is a single predicate "skilled surgeon" enough? Sometimes (sentence 16). Must we always distinguish kinds of skill? No (the Billy argument). With a domain of only dogs, "x is big" is fine. With dogs and mice, "x is big for a dog" is probably better (p. 210).

*Intuition note.* FOL treats each predicate letter as one fixed property. If one English word secretly means different things in two places, using one letter forces them to agree. That can create a validity that the English does not have.

### Practice exercises (pp. 210–212)
Four exercise sets: A, symbolize the 15 syllogistic figures (Barbara, Celarent, etc.); B, symbolize sentences with K, S, V, h, i; C, symbolize sentences about animals; D, symbolize six arguments with your own key. No solutions are printed.

## Toy example (ours, not from the text)
Domain: {1, 2, 3}. O(x): "x is odd". G(x): "x is greater than 5". The name e denotes 2. G is an empty predicate here.

- Vacuous truth: for each x, G(x) is false, so each $G(x)\to O(x)$ is true. Hence $\forall x\,(G(x)\to O(x))$ is true.
- $\exists x\,(G(x)\land O(x))$: each conjunction has a false first part, so each is false. The sentence is false.
- $\exists x\,(G(x)\to O(x))$: at x = 1, F→T is true. The sentence is true, a very weak claim.
- Scope: O(2) is false, so $\forall x\,O(x)$ is false (2 is not odd). Hence $\forall x\,O(x)\to O(e)$ is true (false antecedent).
- But $\forall x\,(O(x)\to O(e))$: at x = 1, O(1) is true and O(e) is false, so T→F is false. The universal sentence is false.

Same pieces, different scope, different truth value.

## Concepts
- [[logical form vs. grammatical form]] — English wording can hide whether a sentence needs ∀, ∃, a name, or a conditional in an antecedent; paraphrase exposes it (pp. 205–207)
- [[analysis]] — here, stepwise paraphrase of an English sentence toward something directly symbolizable in FOL (p. 205)
- [[validity / soundness]] — a symbolization that makes a bad English argument valid is faulty (p. 209)
- [[symbolization-key]] (new) — list of domain, predicates and names that fixes what a symbolization means (p. 199)
- [[domain-of-quantification]] (new) — the collection of things the quantifiers range over; the chosen domain affects the right symbolization (p. 204)
- [[universal-quantifier-conditional-pattern]] (new) — "every F is G" as ∀x(F(x)→G(x)); "some F is G" as ∃x(F(x)∧G(x)) (pp. 200–201)
- [[empty-predicate]] (new) — a predicate that applies to nothing in the domain (p. 202)
- [[vacuous-truth]] (new) — ∀x(F(x)→…) is true when F is empty (p. 203)
- [[scope-of-quantifier]] (new) — the part of a sentence a quantifier governs, like the scope of negation (p. 208)
- [[ambiguous-predicate]] (new) — one predicate letter used for properties that differ across uses, e.g. "skilled" (p. 209)

## Canonical instances
- [[coins-on-the-table]] — sentences 1–5 show the ∀/→ versus ∃/∧ patterns, "no" and "only" (pp. 199–202)
- [[monkeys-and-refrigerators]] — vacuous truth with empty predicates (pp. 202–203)
- [[kim-deal-bassist]] — "if a person is a bassist" versus "if anyone is a bassist" (pp. 205–207)
- [[lars-bassist-scope]] — ∀xB(x)→B(l) versus ∀x(B(x)→B(l)) (pp. 207–208)
- [[skilled-surgeon-carol]] — an ambiguous predicate turns an invalid argument into a valid one (pp. 209–210)

## Bridges (candidates)
- [structural-analogy] scope of a quantifier ↔ scope of negation in TFL — the authors explain one by the other (p. 208)
- [same-math] ∀x(F(x)→G(x)) with empty F ↔ a conditional with a false antecedent — the same truth-functional →, applied to every object (p. 203)
- [structural-analogy] "every F is G" and "some F is G" ↔ Aristotelian syllogistic forms — the exercises recast syllogisms in FOL (p. 210)

## Questions this raises
- Why is ∀x(F(x)→G(x)) true when F is empty, and is that what we want from "every F is G" in English?
- How does a reader decide when a predicate like "skilled" must be split into several predicates?
- Can the equivalences for "no" and "only" be proved from ¬∀ ⇔ ∃¬ plus TFL equivalences? (Sentence 3's justification, p. 201, suggests so.)
- Which of the 15 syllogistic figures remain valid in FOL if a term is empty?

## Exercises worth doing
- Ex. A (p. 210) — symbolize all 15 syllogistic figures. Practises the patterns for every, some, no, some-not — difficulty: medium
- Ex. B.3 (p. 211) — "No one knows the combination unless Ingmar does". Needs scope care and the "unless" paraphrase — difficulty: medium
- Ex. C.7 and C.8 (p. 212) — "If any animal is a reptile…" versus "If any animal is an alligator, then it is a reptile". Practises "any" in an antecedent — difficulty: medium
- Ex. D.2 (p. 212) — "Nothing on my desk escapes my attention…". Builds a key and symbolizes a short argument — difficulty: easy
- Ex. D.4 (p. 212) — the Holmes–Watson kangaroo argument, which has several names, a negation and an "only if" — difficulty: hard

## Reading notes
- Printed page = pdf page − 10. The page labels give printed numbers (199–212).
- Predicate letters are reused with different meanings in different keys, e.g. R is rock star (p. 205), surgeon (p. 209), refrigerator (p. 203), reptile (p. 211).
- Spelling varies: "rock star" and "rockstar" (p. 206).
- Exercise C.7 reads "an reptile" (p. 212), a typo.
- The text layer on p. 207 shows "∃x B(x) → B(l)" without quotation marks. This is only formatting.
- No solutions to the exercises are printed in these pages.
