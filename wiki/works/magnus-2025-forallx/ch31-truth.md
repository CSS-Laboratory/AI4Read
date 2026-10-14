---
id: magnus-2025-forallx/ch31-truth
work: magnus-2025-forallx
unit: "31 Truth in FOL"
pages: 267–276
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Truth in FOL

## L0 — One line
A first-order sentence is true in an interpretation clause by clause: atomic sentences by what the interpretation says, connectives by truth tables, and quantifiers by asking whether all (or some) objects satisfy the formula, using a temporary new name.

## L1 — The gist (≤ 120 words)
How can we say exactly when any sentence of first-order logic (FOL) is true in an interpretation? The chapter handles the three kinds of sentence in turn. Atomic sentences are checked against the interpretation. Connective sentences follow the old truth-table rules. Quantified sentences are harder, because the domain may contain objects that have no name. The fix is to extend the interpretation temporarily with a new name for an object and ask whether the resulting instance is true. "Every object satisfies the formula" gives ∀, and "at least one object satisfies it" gives ∃. This gives a precise account of what it is for an arbitrary FOL sentence to be true or false in an interpretation.

**Prerequisites:** truth tables for ∧, ∨, ¬, →, ↔; FOL syntax (names, predicates, free and bound variables); the idea of an interpretation (domain plus meanings of names and predicates).

## L2 — Key ideas
- Three kinds of FOL sentence need three truth clauses: atomic, connective, quantifier (p. 267).
- An atomic sentence $R(a_1,\dots,a_n)$ is true iff $R$ is true of the named objects, in that order. $a=b$ is true iff both names name the same object (p. 268).
- The connective clauses are the TFL truth tables, restated in words (p. 269).
- Naive quantifier clauses fail. "True of everything" is not general enough, and "true for every name in the interpretation" fails because the go-to interpretation names only two of the many people in the domain (p. 270).
- The correct idea is to extend the interpretation temporarily with a new name for an object (p. 270–271).
- Technical tools: substitution instance, instantiating name, the interpretation $\mathbf{I}[d/c]$, and satisfaction (p. 272–273).
- $\forall xA$ is true iff every object satisfies $A$. $\exists xA$ is true iff at least one object does (p. 273).

## L3 — Walkthrough

**Opening (p. 267).** FOL has three kinds of sentence: atomic, main operator a connective, main operator a quantifier. Truth must be explained for each. The running "go-to" interpretation is:
- domain: all people born before 2000 CE
- $a$: Aristotle; $b$: Beyoncé
- $P(x)$: $x$ is a philosopher
- $R(x,y)$: $x$ was born before $y$

**31.1 Atomic sentences (p. 268).**
- Sentence letters are true or false as the interpretation says.
- $P(a)$ is true (Aristotle is a philosopher) and $P(b)$ is false. $R(a,b)$ is true and $R(a,a)$ is false.
- General rule: for an $n$-place predicate $R$ and names $a_1,\dots,a_n$, $R(a_1,\dots,a_n)$ is true in an interpretation iff $R$ is true of the objects named by $a_1,\dots,a_n$, in that order.
- Identity: $a=b$ is true iff $a$ and $b$ name the very same object. In the go-to interpretation, $a=b$ is false.

**31.2 Sentential connectives (p. 269).** The rules are exactly those of TFL (the truth-functional sentential logic), and they carry the same information as the truth tables:
- $A\wedge B$ is true iff both are true.
- $A\vee B$ is true iff at least one is true.
- $\neg A$ is true iff $A$ is false.
- $A\to B$ is true iff $A$ is false or $B$ is true.
- $A\leftrightarrow B$ is true iff $A$ and $B$ have the same truth value.

The author's examples, on the go-to interpretation:
- $a=a\wedge P(a)$ is true.
- $R(a,b)\wedge P(b)$ is false, since $R(a,b)$ is true but $P(b)$ is false.
- $a=b\vee P(a)$ is true.
- $\neg a=b$ is true.
- $P(a)\wedge\neg(a=b\wedge R(a,b))$ is true, since $P(a)$ is true and $a=b$ is false.

**31.3 Quantifiers (p. 270–273).**

*Failed attempts (p. 270).*
1. First naive thought: $\forall xF(x)$ is true iff $F(x)$ is true of everything in the domain. This is not general enough. The interpretation does not directly say what $\exists yL(x,y)$ is true of. That should follow from the domain, the meaning of $L$, and the quantifiers.
2. Second naive thought: $\forall x\exists yL(x,y)$ is true iff $\exists yL(a,y)$ is true for every name $a$ in the interpretation, and likewise for $\exists$. This also fails. The go-to interpretation has only two names, but the domain has many more people. The author does not want to name them all.
3. Third thought (the author calls it correct): each person *could* be given a name. So we extend the interpretation by adding a new name.

*Three examples (p. 271).*
- $\exists xR(b,x)$ is true. Add the name $c$ for Lady Gaga, who was born after Beyoncé. Then $R(b,c)$ is true in the extended interpretation, which suffices for the original sentence.
- $\exists x(P(x)\wedge R(x,a))$ is true. Add $c$ for Socrates. Then $P(c)\wedge R(c,a)$ is true in the extended interpretation.
- $\forall x\exists yR(x,y)$ is false. Take the last person born in 1999 and name them $d$. Whoever is named by a further name $e$, $R(d,e)$ is false. So $\exists yR(d,y)$ is false in the extended interpretation, which makes the universal sentence false.

*Intuition note.* To test "everyone" or "someone", pretend to point at one person and give them a fresh label. Then check the simpler statement about that person (the instance with the new label). The label is thrown away afterwards.

*Definitions (p. 272–273).*
- $A(\dots x\dots x\dots)$ is a formula with some free occurrences of $x$ (possibly none). $A(\dots c\dots c\dots)$ is the result of replacing *every* free $x$ with the name $c$. This is a **substitution instance** of $\forall xA$ and of $\exists xA$, and $c$ is the **instantiating name**.
- If $A$ has no free $x$, the instance is $A$ itself. Example: $\exists x(R(e,x)\leftrightarrow F(x))$ is an instance of $\forall y\exists x(R(y,x)\leftrightarrow F(x))$, with name $e$ and variable $y$.
- Only free variables are replaced. For $\exists x(\forall xF(x)\to G(x))$, the instance is $\forall xF(x)\to G(e)$, not $F(e)\to G(e)$, because the $x$ in $F(x)$ is bound by $\forall x$.
- If $\mathbf I$ is the interpretation and $c$ is a name not yet assigned, $\mathbf I[d/c]$ is just like $\mathbf I$ except that it also assigns the object $d$ to $c$.
- $d$ **satisfies** $A(\dots x\dots x\dots)$ in $\mathbf I$ iff $A(\dots c\dots c\dots)$ is true in $\mathbf I[d/c]$, where $c$ does not already occur in $A(\dots x\dots x\dots)$. If $d$ satisfies $A$, we also say that $A$ is "true of" $d$.
- Example: Socrates satisfies $P(x)$, because $P(c)$ is true in $\mathbf I[\text{Socrates}/c]$.

*The quantifier clauses (p. 273).*
- $\forall xA(\dots x\dots x\dots)$ is true in an interpretation iff every object in the domain satisfies $A(\dots x\dots x\dots)$.
- $\exists xA(\dots x\dots x\dots)$ is true in an interpretation iff at least one object in the domain satisfies $A(\dots x\dots x\dots)$.

The author says this is a pedantic formalization of the intuitive idea above, and that the spirit of the idea is what matters.

*Intuition note.* "True of" is the bridge. A formula can be true of an object (the object satisfies it). A quantified sentence is then true iff the formula is true of every object (for ∀) or of at least one object (for ∃).

**Practice exercises (p. 274–276).** Three sets ask whether sentences are true in small interpretations: A with Corwin and Benedict, B with Lemmy, Courtney and Eddy, and C with a five-point arrow diagram (p. 274–276).

## Toy example (ours, not from the text)
Domain $\{1,2,3\}$. Name $a$ names 1. $S(x,y)$ means $x<y$.

- $S(a,a)$: $1<1$ is false, so the atomic sentence is false.
- $\exists x\exists yS(x,y)$: extend with $c\mapsto1$ and $d\mapsto2$. $S(c,d)$ is $1<2$, which is true. So the sentence is true.
- $\forall x\exists yS(x,y)$: check every object as $c$.
  - $c\mapsto1$: $1<2$ is true.
  - $c\mapsto2$: $2<3$ is true.
  - $c\mapsto3$: try $d\mapsto1,2,3$. $3<1$, $3<2$ and $3<3$ are all false, so $\exists yS(c,y)$ is false.
  - Object 3 does not satisfy $\exists yS(x,y)$, so the universal sentence is false.
- This mirrors the "last person born in 1999" argument (p. 271).

## Concepts
- [[interpretation]] (new) — domain plus meanings for names and predicates; says which predicates are true of which objects, and truth is defined relative to it (p. 267)
- [[truth-in-an-interpretation]] (new) — truth defined clause by clause for atomic, connective and quantified sentences (p. 267)
- [[substitution-instance]] (new) — the formula obtained by replacing every free $x$ in $A$ with a name $c$ (p. 272)
- [[instantiating-name]] (new) — the name $c$ put in place of the variable (p. 272)
- [[extended-interpretation]] (new) — $\mathbf I[d/c]$: $\mathbf I$ plus the extra assignment of $d$ to a new name $c$ (p. 272)
- [[satisfaction]] (new) — $d$ satisfies $A(x)$ iff the instance with a new name for $d$ is true in $\mathbf I[d/c]$ (p. 272)

## Canonical instances
- [[go-to-interpretation]] — people born before 2000 CE, with Aristotle, Beyoncé, philosopher and born-before (p. 267)
- [[last-person-born-1999]] — shows $\forall x\exists yR(x,y)$ is false (p. 271)
- [[socrates-satisfies-P]] — a worked example of satisfaction (p. 273)

## Bridges (candidates)
- [same-math] Connective clauses ↔ TFL: the clauses restate the characteristic truth tables (p. 269).
- [structural-analogy] Quantifier clauses ↔ programming: "for every / for some object in the domain, test the formula" resembles looping over a list.

## Questions this raises
- What goes wrong if the new name $c$ already occurs in $A$? (The text requires that it does not.)
- Does the definition work when the domain is infinite? The go-to domain is large, and no one names everybody.
- How does this definition of truth lead to the FOL notions of validity and entailment?
- Does the truth of a sentence depend on which new name we pick?

## Exercises worth doing
- Ex. A (p. 274) — practice with sentences with one-place predicates and a single name, including trivially true cases like $\forall x(N(x)\vee\neg N(x))$ — easy
- Ex. B (p. 274–275) — mixed ∃/∀ sentences with several predicates, including nested quantifiers like item 15 — medium
- Ex. C (p. 275–276) — truth of relational sentences read off an arrow diagram — hard

## Reading notes
- Printed page = pdf page − 10.
- The text layer was clean. The diagram in Ex. C is visible only in the page image, and I did not solve it.
- Ex. C item 12 appears alone on p. 276.
