---
id: magnus-2025-forallx/ch26-identity
work: magnus-2025-forallx
unit: "26 Identity"
pages: 228-234
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Identity

## L0 — One line
Adding the symbol '=' (one and the same object as) to first-order logic lets us symbolize many sentences with *else*, *other than*, *only* and *except*, and also say how many things of a kind there are.

## L1 — The gist (≤ 120 words)
Plain quantifier logic cannot say *Pavel owes money to everyone else*, because the quantifier also covers Pavel. It also cannot make sure that two variables name different things. The chapter adds one two-place predicate, '=', written between terms, which always means *one and the same object*. With it, we can symbolize some sentences with *else*, *other than*, *only* and *except*. We can also express numerical claims, shown for at least one to three, at most one and two, and exactly one and two things of a kind. For *at most*, the author says two forms are equivalent. The chapter also notes that the treatment of *except* is disputed.

**Prerequisites:** FOL quantifiers ∀ and ∃, connectives, symbolization keys, negation, conjunction, and the difference between a name and a variable.

## L2 — Key ideas (5–10 bullets)
- Symbolizing *Pavel owes money to everyone* as ∀x O(p,x) entails that Pavel owes himself, because Pavel is in the domain. This motivates a new symbol (p. 228).
- '=' always means *identical*: both terms refer to one and the same object. It does not mean merely *indistinguishable* (p. 229).
- *Everyone else / other than Pavel* becomes ∀x(¬x=p → O(p,x)) (p. 229).
- *Only Pavel…* is plausibly *Pavel does, and no one else does*, compactly ∀x(O(x,h) ↔ x=p). *Everyone except Pavel…* adds that Pavel does not. This analysis of *except* is contested (p. 230).
- *At least two* and *at least three* need two or three existential quantifiers plus a non-identity claim for every pair of variables. Without non-identity, the variables could name the same thing (pp. 231–232).
- *At most one* and *at most two* each have two forms: negate *at least* one more, or say that any picks of one more than the limit include a repeat. The author calls the forms equivalent (p. 232).
- *Exactly one* and *exactly two* can be said as *at least* plus *at most*, or by a more efficient form: the right number of distinct things, and every such thing is one of them (p. 233).
- *Thing* and *object* need no predicate, since they apply to everything (p. 234).

## L3 — Walkthrough

**Opening problem (p. 228).** Domain: people. Key: $O(x,y)$: x owes money to y; $p$: Pavel. Sentence 1 (*Pavel owes money to everyone*) is symbolized $\forall x\, O(p,x)$. This requires that Pavel owes money to every member of the domain. Pavel is in the domain, so he owes himself (p. 228). Sentences 2 (*everyone else*) and 3 (*everyone other than Pavel*) leave that open, but we cannot yet express them (p. 228).

**26.1 Adding identity (p. 229).**
- '=' is a two-place predicate written *between* its terms. It always has the key $x = y$: x is identical to y (p. 229).
- It does not merely mean that the two objects are indistinguishable or share all properties. It means that both terms refer to one and the same object (p. 229).
- Sentence 4 (*Pavel is Mister Chekov*), with $c$: Mister Chekov, becomes $p = c$ (p. 229).
- Sentences 2 and 3 paraphrase as *For all x, if x is not Pavel, then x is owed money by Pavel*, giving
$$\forall x(\neg x = p \to O(p,x))$$
- '$\neg x = p$' negates the whole formula $x = p$ (p. 229).

*Intuition note:* '=' lets us talk about *which* object a variable picks out. So we can exclude one object from a quantifier's range.

**26.2 'Only' and 'except' (pp. 230–231).**
- Sentence 5 (*Only Pavel owes money to Hikaru*; $h$: Hikaru) is plausibly true iff both hold: 6, Pavel owes Hikaru; and 7, no one who is not Pavel owes Hikaru (p. 230).
- Sentence 7 can be written in any of three ways (p. 230):
$$\neg\exists x(\neg x = p \wedge O(x,h)),\quad \forall x(\neg x = p \to \neg O(x,h)),\quad \forall x(O(x,h) \to x = p)$$
- Sentence 5 is the conjunction of one of these with $O(p,h)$. More compactly it is $\forall x(O(x,h) \leftrightarrow x = p)$ (p. 230).
- Sentence 8 (*Everyone except Pavel owes money to Hikaru*) paraphrases as *Everyone who is not Pavel owes Hikaru, and Pavel does not*. It becomes $\forall x(\neg x = p \to O(x,h)) \wedge \neg O(p,h)$, or $\forall x(\neg x = p \leftrightarrow O(x,h))$ (p. 230).
- *But* and *besides* can be treated in similar ways (p. 230).
- The author says this treatment of exceptives is not uncontentious. Some linguists think 8 does not entail that Pavel doesn't owe Hikaru, so the symbolization would be just $\forall x(\neg x = p \to O(x,h))$ (p. 230).
- There are also uses of *except* that clearly lack that entailment, especially in mathematical writing. A calculus text may say *f is defined everywhere except possibly at a*. This means only that f is defined at every x other than a. Whether f is defined at a is left open (p. 231).

*Intuition note:* *Only* and *except* each package two claims: what holds for the named object, and what holds for all the others. The *except* reading with the extra claim about the exception is one analysis, not the only one.

**26.3 There are at least… (pp. 231–232).** Key: $A(x)$: x is an apple.
- At least one (9): $\exists x\, A(x)$. No identity is needed (p. 231).
- At least two (10): the tempting $\exists x\exists y(A(x)\wedge A(y))$ would be true even with one apple, since x and y may be the same apple. The form with identity is
$$\exists x\exists y((A(x)\wedge A(y))\wedge \neg x = y)$$
- At least three (11) (p. 231):
$$\exists x\exists y\exists z[((A(x)\wedge A(y))\wedge A(z))\wedge((\neg x = y\wedge\neg y = z)\wedge\neg x = z)]$$
- It is not enough to write $\neg x=y \wedge \neg y=z$ for *x, y, z are all different*, since $x=z$ could still hold. In general, to say $x_1,\dots,x_n$ are all different, we must have a conjunction of $\neg x_i = x_j$ for every different pair $i, j$ (p. 232).

**26.4 There are at most… (p. 232).**
- At most one (12) is the negation of *at least two*: $\neg\exists x\exists y[(A(x)\wedge A(y))\wedge\neg x=y]$ (p. 232).
- Another form: if you pick an apple and then an apple, you must have picked the same object: $\forall x\forall y[(A(x)\wedge A(y))\to x=y]$ (p. 232). The author says the two will turn out to be logically equivalent (p. 232).
- At most two (13) is paraphrased as *it is not the case that there are three or more distinct apples* (p. 232):
$$\neg\exists x\exists y\exists z[((A(x)\wedge A(y))\wedge A(z))\wedge((\neg x=y\wedge\neg x=z)\wedge\neg y=z)]$$
- The author says 13 can be approached in two equivalent ways. The other one: if you pick three apples, you pick at least one of these objects more than once (p. 232):
$$\forall x\forall y\forall z[((A(x)\wedge A(y))\wedge A(z))\to((x=y\vee x=z)\vee y=z)]$$

*Intuition note:* For these two cases, *at most n* can be said negatively (there are not n+1) or positively (any n+1 picks must repeat). The author says the two ways are equivalent.

**26.5 There are exactly… (pp. 233–234).**
- Exactly one (14) is *at least one and at most one* (sentences 9 and 12) (p. 233):
$$\exists x A(x)\wedge\forall x\forall y[(A(x)\wedge A(y))\to x=y]$$
- More straightforwardly: there is a thing x which is an apple, and everything which is an apple is x itself (p. 233):
$$\exists x[A(x)\wedge\forall y(A(y)\to x=y)]$$
- Exactly two (15), long form: *at least two* and *at most two* (p. 233):
$$\exists x\exists y((A(x)\wedge A(y))\wedge\neg x=y)\wedge\forall x\forall y\forall z[((A(x)\wedge A(y))\wedge A(z))\to((x=y\vee x=z)\vee y=z)]$$
- More efficient form: at least two different apples, and every apple is one of those two (p. 233):
$$\exists x\exists y[((A(x)\wedge A(y))\wedge\neg x=y)\wedge\forall z(A(z)\to(x=z\vee y=z))]$$
- Exactly two things or objects (17, 18) needs no predicate for *thing* or *object*. These words apply trivially to everything. Two symbolizations are offered (p. 234):
$$\exists x\exists y\,\neg x=y\wedge\neg\exists x\exists y\exists z((\neg x=y\wedge\neg y=z)\wedge\neg x=z)$$
$$\exists x\exists y[\neg x=y\wedge\forall z(x=z\vee y=z)]$$

*Intuition note:* *Exactly n* (shown here for one and two) means n different things and nothing beyond them. The short form says the second part as *every apple is one of them*.

## Toy example (ours)
Domain {1, 2}; let $A(x)$ hold of both 1 and 2. Test "exactly one apple", $\exists x[A(x)\wedge\forall y(A(y)\to x=y)]$.
- Try x = 1. $A(1)$ is true. Take y = 2: $A(2)$ is true, but $1=2$ is false, so $A(y)\to x=y$ is false. So the ∀y part fails for x = 1.
- Try x = 2. By the same reasoning, y = 1 gives a false conditional. So the formula fails.
- So the sentence is false, correctly, since there are two apples.

Now test "exactly two", $\exists x\exists y[(A(x)\wedge A(y))\wedge\neg x=y\wedge\forall z(A(z)\to(x=z\vee y=z))]$, with x = 1, y = 2. $A(1)$ and $A(2)$ are true, and $\neg 1=2$ is true. For z = 1, $1=1$ holds; for z = 2, $2=2$ holds. So it is true.

The naive "at least two" $\exists x\exists y(A(x)\wedge A(y))$ would also be true on a domain {1} with $A(1)$, taking x = y = 1. This shows why $\neg x=y$ is needed.

## Concepts
- [[identity-symbol]] (new) — '=': two-place predicate, written between terms, meaning one and the same object (p. 229)
- [[numerical-quantifiers]] (new) — at least, at most and exactly (shown for small n) expressed with quantifiers plus identity (pp. 231–233)
- [[exceptives]] (new) — *except*, *but*, *besides*: treated with identity; the author calls the treatment not uncontentious (p. 230)
- [[only-claims]] (new) — *Only Pavel…* as Pavel does, plus no one who is not Pavel does (p. 230)
- [[everyone-vs-everyone-else]] (new) — ∀x O(p,x) for *everyone* cannot express *everyone else*, because it also covers Pavel (p. 228)

## Canonical instances
- [[pavel-owes-everyone]] — ∀x O(p,x) entails Pavel owes himself (p. 228)
- [[apples-counting]] — at least, at most and exactly n apples (pp. 231–233)
- [[f-defined-except-at-a]] — a calculus use of *except* that leaves the exception open (p. 231)

## Bridges (candidates)
- [structural-analogy] "There are exactly n things" in FOL ↔ mathematics: cardinality of a set — both count objects, here by logical form rather than by counting.
- [metaphor] The author's remark that *thing* and *object* do not sort wheat from chaff (p. 234) ↔ predicates in general: a predicate that sorts nothing needs no symbol.

## Questions this raises
- Why is the three-variable "at most two" form equivalent to its negated "three or more" form? How would one prove it?
- How do the quantifier formulas grow for "exactly n" as n gets large?
- Is "except" better read with or without the claim about the exception?
- Does '=' mean the same for names ($p = c$) and for variables bound by quantifiers?

## Exercises worth doing
- Ex. A (p. 234) — symbolize "Every officer except Pavel owes money to Hikaru", then test your answer when Pavel is not an officer — difficulty: medium
- Ex. B1 (p. 234) — explain why $\exists x\forall y(A(y)\leftrightarrow x=y)$ symbolizes "exactly one apple" — difficulty: medium
- Ex. B2 (p. 234) — explain why the ↔ form symbolizes "exactly two apples" — difficulty: medium

## Reading notes
- Printed page = pdf − 10 (pdf 238 = printed 228).
- Text layer garbles bracket sizes in some formulas. I checked all formulas against the page images.
- The author says the "at most" pairs are logically equivalent but gives no proof on these pages (p. 232).
- Exercises A and B are printed without solutions in these pages.
