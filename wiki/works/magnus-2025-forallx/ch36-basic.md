---
id: magnus-2025-forallx/ch36-basic
work: magnus-2025-forallx
unit: "Chapter 35 (Properties of relations) and Chapter 36 (Basic rules for FOL), §§36.1–36.6"
pages: 293–315
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
# Properties of relations; basic natural-deduction rules for the quantifiers

## L0 — One line
FOL proofs get four quantifier rules (∀E, ∃I, ∀I, ∃E); ∀I and ∃E need side-conditions on the names they use, so that the reasoning is general (for ∀I the name must be "arbitrary").

## L1 — The gist (≤ 120 words)
How can a proof system for first-order logic (FOL) handle "all" and "some"? Chapter 35 shows that the validity of some arguments depends on a property of a relation, such as transitivity. If that property can be written in FOL, it can be added as a premise. Chapter 36 adds four quantifier rules. Dropping "all" (∀E) and adding "some" (∃I) come first, with simple examples. Adding "all" (∀I) needs a name about which nothing special is assumed, and using "some" (∃E) needs a new name. Restrictions on names block invalid "proofs". The chapter also notes that the rules assume a non-empty domain, and that careless substitution with vacuous quantifiers can break the rules.

**Prerequisites:** TFL natural-deduction rules (subproofs, assumptions, discharge); FOL syntax (names, variables, free vs bound); substitution instances; interpretations and domains.

## L2 — Key ideas (5–10 bullets)
- A relation's property (transitive, reflexive, symmetric, anti-symmetric) can be written in FOL. When an argument's validity depends only on such a property, adding it as a premise gives an argument valid in FOL (pp. 293–294).
- Reflexive + symmetric + transitive = equivalence relation. Reflexive + transitive + anti-symmetric = partial order (p. 295).
- ∀E: from ∀xA infer any substitution instance. ∃I: from A(…c…) infer ∃xA with some or all occurrences of c replaced by x. As with every elimination rule, ∀E can be applied only when the quantifier is the main logical operator (pp. 298–299).
- The rules plus copy-and-paste of proofs yield ∀xF(x) ⊢ ∃xF(x), so the proof system alone says that something exists. This matches the stipulation of non-empty domains; the author suggests we might regard it as only a very slight limitation (pp. 300–301).
- ∀I is licensed only when the name c is not in any premise or undischarged assumption. The name may occur in a discharged assumption (pp. 302–304).
- ∃E: assume an instance with a *new* name c. c must not occur in the ∃-sentence, in any earlier undischarged assumption, or in the conclusion B (pp. 305–308).
- The word "free" in the substitution notation, and the proviso that c not occur in the scope of a quantifier binding x, matter because vacuous quantification is allowed. Without these clauses invalid arguments could be "proved" (pp. 308–310).

## L3 — Walkthrough

### Chapter 35. Properties of relations
**Why they matter.** The argument that Rudolf is older than Kurt, Kurt is older than Julia, so Rudolf is older than Julia, is valid. Its FOL form $R(r,k), R(k,j) \therefore R(r,j)$ is not valid in FOL. The validity depends on a property of "older than": **transitivity** (p. 293). A property can itself be written in FOL:
$$\forall x\forall y\forall z\,((R(x,y)\land R(y,z))\to R(x,z))$$
When an argument's validity depends only on a property of a relation, and that property can be symbolized in FOL, we can add it as a premise. The result is valid in FOL (p. 294).

**Definitions** (p. 294), with FOL forms (pp. 294–295):
- Transitive: whenever $R(x,y)$ and $R(y,z)$, then $R(x,z)$.
- Reflexive: for any $x$, $R(x,x)$. In FOL: $\forall x\,R(x,x)$.
- Symmetric: whenever $R(x,y)$, then $R(y,x)$. In FOL: $\forall x\forall y\,(R(x,y)\to R(y,x))$.
- Anti-symmetric: for no two *different* $x,y$ do $R(x,y)$ and $R(y,x)$ both hold. In FOL: $\neg\exists x\exists y\,((R(x,y)\land R(y,x))\land\neg x=y)$, or equivalently $\forall x\forall y\,((R(x,y)\land R(y,x))\to x=y)$.

**Examples.** The order relations $<,\le,>,\ge$ and identity $=$ are transitive (p. 294).
- Relations that express an equivalence in some respect (being the same age as, being as tall as, $=$) are reflexive and symmetric (p. 295).
- Reflexive + symmetric + transitive relations are called **equivalence relations**. Being a sibling of is symmetric but not reflexive, since no one is their own sibling (p. 295).
- Reflexive + transitive + anti-symmetric relations are **partial orders**. $\le$ and $\ge$ are examples (p. 295).
- Being no older than is reflexive and transitive but not anti-symmetric, because two different people can be the same age (p. 295).

*Intuition note:* Some arguments need a hidden premise about the relation itself. Writing that premise in FOL makes the argument formally valid. Names such as "equivalence relation" and "partial order" are labels for bundles of these properties.

### Chapter 36. Basic rules for FOL
All TFL rules (basic and derived) and the symbol ⊢ carry over. New basic rules are needed for the quantifiers and for identity (p. 297). Identity rules are not covered in these pages.

**36.1 Universal elimination (∀E).** From "everything is F" we may infer that any particular thing is F, e.g. from $\forall x\,R(x,x,d)$ infer $R(a,a,d)$ or $R(d,d,d)$ (pp. 297–298). Rule: from $\forall x\,\mathscr{A}(\ldots x\ldots x\ldots)$ at line $m$, infer $\mathscr{A}(\ldots c\ldots c\ldots)$, citing ∀E, $m$. Here every free occurrence of the variable is replaced by any name you like (p. 298). As with every elimination rule, the quantifier must be the main logical operator. So from $\forall x\,B(x)\to B(k)$ you may *not* infer $B(b)\to B(k)$ (p. 298).

**36.2 Existential introduction (∃I).** From the claim that some particular thing is F we may infer that something is F. From $R(a,a,d)$ we may infer $\exists x\,R(a,a,x)$, or $\exists x\,R(x,x,d)$, or $\exists x\,R(x,a,d)$. The last replaces only one occurrence of $a$ (if Narcissus loves himself, someone loves Narcissus) (p. 299). Notation: $\mathscr{A}(\ldots x\ldots c\ldots)$ is any formula got by replacing *some or all* occurrences of $c$ by $x$, provided $c$, wherever replaced, does not occur in the scope of a quantifier binding $x$ (p. 299). Rule: from $\mathscr{A}(\ldots c\ldots c\ldots)$ at $m$ infer $\exists x\,\mathscr{A}(\ldots x\ldots c\ldots)$, citing ∃I, $m$ (p. 299).

*Intuition note:* ∀E "plugs in" a name: you name it; it is F. ∃I "forgets" which thing it was. The author presents both as natural steps, but 36.3 shows that together they commit us to there being something.

**36.3 Empty domains.** The proof $\forall xF(x)$ (PR); $F(a)$ (∀E, 1); $\exists xF(x)$ (∃I, 2) looks fine if anything exists (p. 300). If nothing existed, "everything is F" would be vacuously true but "something is F" false. So the proof claims, as a matter of logic alone, that there is something rather than nothing (p. 300).
- This commitment already exists: chapter 23 stipulated that domains have at least one member, and $\exists x\,x=x$ is true in every interpretation (p. 300).
- Three things we want: (1) $\forall xF(x)\vdash F(a)$; (2) $F(a)\vdash\exists xF(x)$; (3) copy-and-paste of proofs. Together they give $\forall xF(x)\vdash\exists xF(x)$. Refusing that means giving up one of the three (pp. 300–301).
- The author's view (tentative): we might well be cheating a bit here. Granted, it may make theological debates about why there is something rather than nothing harder, but otherwise we get along fine. So maybe we should regard FOL and its proof system as having "a very slightly limited purview". Allowing for nothing would need a more complicated system. For as long as we are content to ignore that possibility, the system is "perfectly in order" (pp. 300–301).

**36.4 Universal introduction (∀I).**
- A rule requiring every substitution instance to be proved would be unusable, because FOL has infinitely many names (p. 301).
- Idea: after $\forall xF(x)$ (PR), $F(a)$ (∀E, 1), the same justification works for any name. So we may infer $\forall yF(y)$ (∀I, 2). The crucial thought is that $a$ was an *arbitrary* name (p. 302).
- Rule: from $\mathscr{A}(\ldots c\ldots c\ldots)$ at $m$ infer $\forall x\,\mathscr{A}(\ldots x\ldots x\ldots)$, citing ∀I, $m$. **Constraint:** the name $c$ must not occur in a premise or an undischarged assumption (p. 302).
- The rule replaces *every* occurrence of $c$ by $x$, and only if $c$ does not occur in the scope of a quantifier binding $x$ in $\mathscr{A}$ (pp. 302–303).
- *Why the constraint:* "Everyone loves Kylie Minogue; so everyone loves themselves", i.e. $\forall xL(x,k)\therefore\forall xL(x,x)$, is invalid. The attempt $\forall xL(x,k)$ (PR); $L(k,k)$ (∀E); $\forall xL(x,x)$ (∀I) is banned, because $k$ occurs in premise 1 (p. 303). If we have made any assumptions about the object we are working with, we are not reasoning generally enough to license ∀I (p. 303).
- The name *may* occur in a *discharged* assumption. Valid example: $G(d)$ (AS, at line 1); $G(d)$ (R, 1); $G(d)\to G(d)$ (→I, 1–2); $\forall z(G(z)\to G(z))$ (∀I, 3). So this is a theorem (p. 304).
- *Why replace every occurrence:* "Everyone is as old as themselves; so everyone is as old as Judi Dench", $\forall xO(x,x)\therefore\forall xO(x,d)$, is invalid. From $O(d,d)$ the step to $\forall xO(x,d)$ is banned because not every $d$ was replaced (p. 304).

*Intuition note:* ∀I says: if you proved F of something you know nothing special about, you proved it of everything. The name restriction is what "nothing special" means in the proof.

**36.5 Existential elimination (∃E).**
- Knowing that something is $F$ does not tell us which thing is $F$. So it would seem that from $\exists xF(x)$ we cannot immediately conclude $F(a)$, or any other substitution instance (pp. 304–305).
- The author gives an English argument: call the F-thing "Becky". Becky is F. All F are G, so Becky is G. So something is G. Nothing depended on who Becky was (p. 305).
- Proof (p. 305): premises $\exists xF(x)$ and $\forall x(F(x)\to G(x))$. Assume $F(b)$ (AS, 3). Then $F(b)\to G(b)$ (∀E, 2); $G(b)$ (→E, 4, 3); $\exists xG(x)$ (∃I, 5). Discharge: $\exists xG(x)$ (∃E, 1, 3–6). The assumption about $b$ is only that it satisfies $F(x)$, so the pattern is general (pp. 305–306).
- Rule (p. 306): from $\exists x\,\mathscr{A}(\ldots x\ldots x\ldots)$ at $m$, assume $\mathscr{A}(\ldots c\ldots c\ldots)$ at $i$ (AS), derive $\mathscr{B}$ at $j$, infer $\mathscr{B}$ (∃E, $m$, $i$–$j$). Constraints:
  - $c$ must not occur in any assumption undischarged before line $i$.
  - $c$ must not occur in $\exists x\,\mathscr{A}(\ldots x\ldots x\ldots)$.
  - $c$ must not occur in $\mathscr{B}$.
- Three banned "proofs", each testing one constraint:
  - $L(b)$, $\exists x\neg L(x)\therefore L(b)\land\neg L(b)$. Assume $\neg L(b)$ and derive $L(b)\land\neg L(b)$. ∃E is banned because $b$ occurs in the conclusion (p. 307).
  - The same, concluding $\exists x(L(x)\land\neg L(x))$. Still banned, because $b$ occurs in the undischarged assumption on line 1, $L(b)$ (p. 307).
  - From $\exists xL(a,x)$, assume $L(a,a)$, get $\exists xL(x,x)$. Banned, because $a$ occurs in line 1, the ∃-sentence. "Someone likes themselves" does not follow from "Alex likes someone" (p. 308).
- **Moral:** to get information out of an existential quantifier, choose a *new* name for the substitution instance (p. 308).

*Intuition note:* ∃E treats "the thing that is F" as an unknown with a temporary name. Whatever you conclude must not mention that name, or the conclusion would secretly depend on which thing it was.

**36.6 Quantifier rules and vacuous quantification.** Vacuous quantification (a quantifier binding no variable) is allowed in the syntax. So the substitution notation only replaces *free* occurrences (p. 308).
- Incorrect ∀E: from $\forall x(F(x)\land\exists xG(x))$ to $F(a)\land\exists xG(a)$. The second $x$ is bound by $\exists x$. $\exists xG(a)$ is vacuous, hence equivalent to $G(a)$. Line 1 is equivalent to $\forall x(F(x)\land\exists yG(y))$, which does not entail $F(a)\land G(a)$ (p. 309). Exercises will likely keep variables separate (p. 309).
- ∃I restriction: $\exists x\forall xL(x,x)$ is a legal sentence, equivalent to $\forall xL(x,x)$. Without the scope restriction one could "infer" $\exists x\forall xL(x,x)$ from $\forall xL(a,x)$ by ∃I. That is invalid: "Alex likes everyone" does not give "everyone likes everyone" (p. 309).
- ∀I restriction: $\forall x\exists xL(x,x)$ is equivalent to $\exists xL(x,x)$. Without the restriction one could go from $\forall y\exists xL(y,x)$ (PR), $\exists xL(a,x)$ (∀E, 1), to $\forall x\exists xL(x,x)$ (∀I, 2). That is invalid: "Someone likes themselves" does not follow from "Everyone likes someone" (p. 310).
- The author says these restrictions are rarely at risk in practice but are needed to make the rules correct (pp. 309–310).

## Toy example (ours)
Why does the ∀I restriction matter? Take the invalid argument $\forall xL(x,k)\therefore\forall xL(x,x)$. Interpretation: domain $\{k, m\}$; $L(u,v)$ true iff $v=k$.
- Premise: $L(k,k)$ is true (second place is $k$); $L(m,k)$ is true. So $\forall xL(x,k)$ is true.
- Conclusion: $L(m,m)$ is false (second place is $m$, not $k$). So $\forall xL(x,x)$ is false.
- True premise and false conclusion, so the argument is invalid. A proof system that derived it (by ∀I on $L(k,k)$ while $k$ is in a premise) would be unsound. The restriction rules this out.

## Concepts
- [[validity / soundness]] — used here for arguments in FOL; an argument's validity can depend on a property of a relation, which can be added as a premise (pp. 293–294)
- [[transitive-relation]] (new) — $R(x,y)$ and $R(y,z)$ give $R(x,z)$ (p. 294)
- [[reflexive-relation]] (new) — $R(x,x)$ for every $x$ (p. 294)
- [[symmetric-relation]] (new) — $R(x,y)$ gives $R(y,x)$ (p. 294)
- [[anti-symmetric-relation]] (new) — no two different $x,y$ with both $R(x,y)$ and $R(y,x)$ (p. 294)
- [[equivalence-relation]] (new) — reflexive, symmetric and transitive (p. 295)
- [[partial-order]] (new) — reflexive, transitive and anti-symmetric (p. 295)
- [[universal-elimination]] (new) — ∀E: from ∀xA infer any substitution instance (p. 298)
- [[existential-introduction]] (new) — ∃I: from A(…c…) infer ∃xA, replacing some or all occurrences of c (p. 299)
- [[universal-introduction]] (new) — ∀I: from A(c) infer ∀xA(x) if c is in no premise or undischarged assumption (p. 302)
- [[existential-elimination]] (new) — ∃E: assume an instance with a new name; discharge to a conclusion free of that name (p. 306)
- [[arbitrary-name]] (new) — a name about which nothing special is assumed, so reasoning with it is general (p. 302)
- [[non-empty-domain]] (new) — every FOL domain has at least one member; the proof system builds this in (pp. 300–301)
- [[vacuous-quantification]] (new) — a quantifier that binds no variable in its scope; legal in FOL and the source of subtle substitution problems (pp. 308–309)

## Canonical instances
- [[older-than-transitivity]] — Rudolf/Kurt/Julia: validity depends on a relation's property (p. 293)
- [[kylie-minogue-argument]] — shows why ∀I forbids names in premises (p. 303)
- [[judi-dench-argument]] — shows ∀I must replace every occurrence of the name (p. 304)
- [[becky-argument]] — motivates ∃E (p. 305)
- [[tim-button-lecturer]] — shows ∃E's constraints on the conclusion and assumptions (p. 307)
- [[alex-likes-someone]] — shows ∃E's constraint on the ∃-sentence (p. 308)

## Bridges (candidates)
- [structural-analogy] ∀I with an arbitrary name ↔ mathematics: choosing an arbitrary $n$ and then concluding something for all $n$ — both generalize only from a case with no special assumptions.
- [structural-analogy] ∃E with a new name ↔ mathematics: naming an element that has the property — a temporary name for an unspecified witness.
- [same-math] Equivalence relation (reflexive, symmetric, transitive) ↔ set theory: the same three properties define equivalence relations there — same definition.
- [metaphor] Non-empty domain stipulation ↔ modelling: the assumption that the set of individuals is not empty is built into the framework.

## Questions this raises
- Which of the three desiderata (∀E, ∃I, copy-and-paste) would a system for possibly empty domains give up?
- Are the name restrictions on ∀I and ∃E enough to make the rules sound, and how would one show it?
- How do the identity rules (announced on p. 297) let us prove properties such as the transitivity of $=$?
- Can symmetric and anti-symmetric hold together for a non-trivial relation? (Exercise 35B asks this.)

## Exercises worth doing
- Ex. 35A (p. 295) — find relations with given combinations of properties — difficulty: easy
- Ex. 35B (p. 295) — a relation can be both symmetric and anti-symmetric — difficulty: easy
- Ex. 36A (p. 310) — explain why two "proofs" are wrong and give countermodels — difficulty: medium
- Ex. 36B (p. 311) — add rule citations to given proofs, testing the quantifier rules — difficulty: easy
- Ex. 36F (p. 314) — write a key for, symbolize and prove an argument whose premise says that someone likes everyone who likes everyone she likes, and whose conclusion says that someone likes herself — difficulty: hard
- Ex. 36I (p. 314) — decide validity of each argument: proof or interpretation — difficulty: medium

## Reading notes
- Printed pages 293–315 (pdf 303–325). Printed = pdf − 10. Pdf 306 (printed 296) is the Part VII divider ("Natural deduction for FOL").
- The unit contains Chapter 35 and Chapter 36 §§36.1–36.6 with exercises. The chapter intro (p. 297) mentions new rules for identity, but no identity rules appear in these pages.
- Misprints seen in the images: "naughy attempt" for "naughty" (p. 298); "it does not following" (p. 300); "There are a two important things" (p. 303).
- The text layer was clean for the formulas I used. I checked rule boxes and proofs against the images. Exercise solutions are not printed.
