---
id: magnus-2025-forallx/ch30-extensionality
work: magnus-2025-forallx
unit: "30 Extensionality"
pages: 258-266
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Extensionality

## L0 — One line
FOL cares only about what its predicates are true of (their extensions), not what they mean, so we *symbolize* English in FOL instead of translating it, and an interpretation is just a domain plus truth values, referents and extensions.

## L1 — The gist (≤ 120 words)
The chapter asks what a formal interpretation of FOL really fixes. Answer: for predicates, only extensions (what they are true of). A predicate is settled by the things (or ordered pairs of things) it is true of, however we specify them. Two predicates with different meanings but the same extension are the same to FOL, so FOL does not translate English. Identity is special: its meaning is fixed, and co-referring names are interchangeable. The converse (identity of indiscernibles) is not part of the logic. An interpretation is then defined as a domain, truth values, referents and extensions, and can be shown by a key, a list or a diagram.

**Prerequisites:** FOL syntax (names, predicates, quantifiers), symbolization keys, truth values and biconditionals, use vs. mention.

## L2 — Key ideas (5–10 bullets)
- A symbolization key only stipulates what a predicate is true of. It does not carry English meaning across (p. 259).
- The extension of a predicate is the things it is true of. FOL is "extensional" because it cannot register meaning differences between predicates with the same extension (p. 259).
- Extensions can be given by enumeration or by an English predicate. They may be arbitrary or empty (pp. 260–261).
- Two-place predicates have extensions made of ordered pairs, since order matters (pp. 261–262).
- Identity has a fixed meaning. Co-referring names can be swapped without changing truth value (p. 262).
- The converse, identity of indiscernibles, is not accepted by this logic, and a two-object interpretation shows why (p. 263).
- An interpretation has four parts: domain, sentence-letter values, referents of names, extensions of predicates (p. 264).
- Interpretations can be shown by keys, enumerations or arrow diagrams (pp. 264–265).

## L3 — Walkthrough

### Opening (p. 258)
TFL's connectives are all truth-functional, and all TFL can do is key sentences to truth values. A key such as "P: Big Ben is in London" amounts to something like the stipulation that 'P' is true iff Big Ben is in London (p. 258). TFL cannot handle meaning differences beyond truth value (p. 258).

### 30.1 Symbolizing versus translating (pp. 258–259)
FOL goes beyond truth values: it splits sentences into terms, predicates and quantifiers. But it goes no further (p. 258).
- The key "C(x): x teaches Logic III in Calgary" does not carry the English meaning over. It is simply stipulating something like this: 'C(x)' and the English predicate are to be true of exactly the same things (p. 259).
- The extension of a predicate is the things it is true of. We may stipulate it directly. For example, 'C(x)' is true of Richard Zach alone. This has the same effect as the indirect stipulation, since he alone teaches Logic III in Calgary (p. 259).
- The English predicates "is Richard Zach" and "teaches Logic III in Calgary" have very different meanings, yet the same extension here (p. 259).
- FOL is an **extensional language**: it does not represent meaning differences between predicates with the same extension (p. 259). If translation has to preserve meaning, we are not translating English into FOL. We symbolize (p. 259).

*Intuition note:* FOL sees only "which things", never "why those things". Two descriptions that pick out the same things look identical to it.

### 30.2 Extensions (pp. 260–261)
- Stipulations can be arbitrary. Example: 'H(x)' is true of Aristotle, a number (the numeral is garbled in the source text), and every top-F key on every piano ever made (p. 260). With a: Aristotle, h: Hypatia, p: that number, 'H(a)' and 'H(p)' are true and 'H(h)' is false (p. 260).
- The listed objects need not have anything in common. To logic, all objects are on an equal footing (p. 260).
- Any well-defined collection is a potential extension of a one-place predicate. We can give it by **enumeration** (listing) or by an English predicate. "x is an even integer between 3 and 9" gives 4, 6 and 8 (p. 260).
- Some predicates, such as "x is a round square", are true of nothing. Their extension is **empty**, and this is allowed. We can make 'H(x)' empty by listing no members (pp. 260–261).

### 30.3 Many-place predicates (pp. 261–262)
- Key: L(x,y): "x loves y". It means 'L(x,y)' is true of x and y, *in that order*, iff x loves y (p. 261). Order matters because love is not always reciprocated.
- Use/mention remark: the 'x' and 'y' in the English side are used. The 'x' and 'y' inside 'L(x,y)' are mentioned (p. 261).
- A direct stipulation needs order, so two-place predicates are true of **ordered pairs**, written with angle brackets (p. 261).
- Example: 'B(x,y)' is true of exactly ⟨Lenin, Marx⟩, ⟨de Beauvoir, Sartre⟩ and ⟨Sartre, de Beauvoir⟩ (pp. 261–262). With l, m, b, r as names, 'B(l,m)' is true and 'B(m,l)' is false. 'B(b,r)' and 'B(r,b)' are both true (p. 262).
- A precise treatment needs elementary set theory, which this book does not cover (p. 262).

*Intuition note:* A two-place predicate is a list of ordered pairs. ⟨a,b⟩ being on the list does not put ⟨b,a⟩ on it.

### 30.4 Semantics for identity (pp. 262–263)
- Identity is written 'x = y'. Its interpretation is fixed once and for all (p. 262).
- If two names refer to the same object, swapping them changes no sentence's truth value. If 'a' and 'b' name the same object, these are all true (p. 263):
$$A(a)\leftrightarrow A(b),\quad B(a)\leftrightarrow B(b),\quad R(a,a)\leftrightarrow R(b,b),$$
$$R(a,a)\leftrightarrow R(a,b),\quad R(c,a)\leftrightarrow R(c,b),\quad \forall x\,R(x,a)\leftrightarrow \forall x\,R(x,b)$$
- **Identity of indiscernibles** is the reverse claim: if exactly the same sentences (without '=') are true of x and y, they are the same object. The author calls it highly controversial. Our logic does not subscribe to it (p. 263).
- Counterexample interpretation: domain = P. D. Magnus, Tim Button; a: Magnus; b: Button; every primitive predicate is true of nothing (p. 263).
  - Every atomic sentence without '=' is false.
  - So every biconditional linking two such sentences is true, e.g. 'A(a) ↔ A(b)' and 'R(a,a) ↔ R(a,b)'.
  - Yet Button and Magnus are two distinct people (p. 263).

*Intuition note:* If two names refer to the same object, swapping them changes no truth value. The converse is not built into this logic: it allows two distinct objects to satisfy exactly the same identity-free sentences, as in the Magnus–Button interpretation.

### 30.5 Interpretations (pp. 264–266)
An FOL **interpretation** consists of four things (p. 264):
1. a non-empty domain;
2. a truth value for each sentence letter we consider;
3. for each name we consider, exactly one object in the domain (its referent);
4. for each predicate other than '=', its extension: objects from the domain for one-place predicates, ordered pairs for two-place predicates, and so on.

- No specification is needed for '=': everything is identical to itself, and only to itself (p. 264).
- Interpretations are also called "models" or "structures" (footnote, p. 264).
- Symbolization keys present interpretations conveniently. Enumerations on the right side are now allowed. Examples: domain philosophers and numbers with H(x): Aristotle, Hypatia and a number. Or domain 0, 1, 2 with L(x,y): ⟨0,1⟩, ⟨0,2⟩, ⟨1,2⟩, which equals "x is less than y" on that domain (p. 264).
- **Diagrams:** an arrow from x to y means 'R(x,y)' holds of x and y (p. 265).
  - Diagram 1 (domain 1, 2, 3, 4): arrows give ⟨1,2⟩, ⟨2,3⟩, ⟨3,4⟩, ⟨4,1⟩, ⟨1,3⟩ (p. 265).
  - Diagram 2 (same domain): extension ⟨1,3⟩, ⟨3,1⟩, ⟨3,4⟩, ⟨1,1⟩, ⟨3,3⟩, with loops at 1 and 3 and no arrow at 2 (p. 265).
- Diagrams can be extended. Names can be added as labels. A circle around objects can show a one-place extension. Colored, dashed or dotted lines can distinguish several predicates (pp. 265–266).

## Toy example (ours)
Domain: 1, 2, 3, 4, 5, 6.
- P(x): "x is even and between 3 and 7". Check each: 2 is not above 3, 4 passes, 6 passes. Extension {4, 6}.
- Q(x): "x is 2 times 2, or 2 times 3". 2·2 = 4 and 2·3 = 6. Extension {4, 6}.
- The English meanings differ, but the extensions are the same. On this domain, 'P(x)' and 'Q(x)' are indistinguishable to FOL.
- For a two-place case, let domain = 1, 2, 3 and L(x,y) be true of ⟨1,2⟩, ⟨1,3⟩, ⟨2,3⟩ ("x is less than y"). 'L(1,2)' is true because ⟨1,2⟩ is listed. 'L(2,1)' is false because ⟨2,1⟩ is not listed.

## Concepts
- [[extension]] (new) — the things (or ordered tuples) a predicate is true of (p. 259)
- [[extensional-language]] (new) — a language that ignores meaning differences between predicates with the same extension; FOL is one (p. 259)
- [[symbolizing-vs-translating]] (new) — symbolizing only stipulates what predicates are true of, while translating would have to preserve meaning (p. 259)
- [[enumeration]] (new) — specifying an extension by listing its members (p. 260)
- [[empty-extension]] (new) — a predicate true of nothing; allowed (pp. 260–261)
- [[ordered-pair]] (new) — a pair whose order matters, written ⟨x, y⟩; extension of a two-place predicate (p. 261)
- [[identity-of-indiscernibles]] (new) — if the same identity-free sentences hold of x and y, then x = y; controversial and not part of this logic (p. 263)
- [[interpretation]] (new) — domain, truth values, referents and extensions; also called a model or structure (p. 264)
- use vs. mention — the 'x', 'y' in the English side are used, those in 'L(x,y)' are mentioned (p. 261)

## Canonical instances
- [[logic-III-predicate]] (new) — 'C(x)' has the same extension as "is Richard Zach" despite a different meaning (p. 259)
- [[arbitrary-extension-H]] (new) — 'H(x)' true of Aristotle, a number and piano keys, which shows that extensions need no natural unity (p. 260)
- [[B-pairs-order]] (new) — ⟨Lenin, Marx⟩ is listed but ⟨Marx, Lenin⟩ is not, which shows that order matters (pp. 261–262)
- [[Magnus-Button-interpretation]] (new) — two distinct objects satisfying the same identity-free sentences (p. 263)
- [[arrow-diagram-interpretation]] (new) — interpretations of 'R(x,y)' drawn as arrows over 1, 2, 3, 4 (p. 265)

## Bridges (candidates)
- [structural-analogy] FOL's extensional view ↔ analytic-philosophy: Frege-style sense vs. reference, since extension tracks reference-like content and meaning differences are ignored. (Canon link; not stated in this unit.)
- [structural-analogy] Arrow-diagram interpretation of a two-place predicate ↔ network science: a directed graph, whose edges are the ordered pairs.
- [same-math] Extension of a two-place predicate as a list of ordered pairs ↔ set theory: a binary relation as a set of ordered pairs (the author says set theory is not covered, p. 262).

## Questions this raises
- If FOL ignores meaning, what do we lose when we symbolize English arguments whose validity depends on meaning?
- How can the identity predicate '=' be used in FOL to say that two things are distinct? Can '=' separate the two indiscernible objects of the Magnus–Button interpretation?
- How should three-place predicates be treated? The text only says "etc." (p. 264).
- What precisely is a "well-defined collection" (p. 260), and what role would set theory play in making it precise?

## Reading notes
- Printed page = pdf page − 10 (pdf 268 = printed 258).
- Numerals in the text layer are garbled in two places: "the number ��" on p. 260 and the third item in 'H(x)' on p. 264. No page image of p. 260 was provided, so the number is [unreadable p. 260]. The p. 264 value is likewise unread.
- Pages 263 and 265 were checked against the images. The page 265 arrows were read from the image.
- These pages contain no exercises.
- The source text refers to chapter 10 (p. 258) and part V (p. 264) of the book, which are not in these pages.
