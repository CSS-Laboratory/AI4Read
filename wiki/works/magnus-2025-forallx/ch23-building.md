---
id: magnus-2025-forallx/ch23-building
work: magnus-2025-forallx
unit: 23 Building blocks of FOL
pages: 190–198
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
# Building blocks of FOL

## L0 — One line
Because TFL cannot look inside a sentence, we build first-order logic (FOL) from names, predicates, quantifiers and a domain, so that structure like "all logicians…" is kept (pp. 190–198).

## L1 — The gist (≤ 120 words)
Some English arguments are obviously valid, yet their TFL symbolization fails the truth-table test. The reason is that TFL treats a sentence like *All logicians wear funny hats* as one unanalysable letter. The chapter introduces FOL, which splits such sentences into names (like "Bertie"), predicates (like "is a dog") and quantifiers ("for all", "there is"). It adds the domain, the collection of things the quantifiers talk about. In FOL every name must pick out exactly one thing in a non-empty domain. This rules out empty names such as "Chimera". The chapter flags that this raises a classic philosophical problem, to which it will return.

**Prerequisites:** TFL: sentence letters, connectives (∧, →, ¬), truth tables, validity; the idea of a symbolization key.

## L2 — Key ideas
- TFL cannot show why *Willard is a logician; all logicians wear funny hats; so Willard wears a funny hat* is valid, because its smallest units are sentence letters (pp. 190–191).
- FOL "splits the atom" using names, predicates and quantifiers. It keeps all TFL connectives (pp. 191, 194).
- A name is a singular term that picks out exactly one thing. Different names may pick out the same thing, and some things have no name (pp. 192–193).
- A predicate can be made from a sentence by removing a singular term. Quantifiers ∀ and ∃ must be followed by a variable, which works as a kind of placeholder (pp. 193–195).
- The text says it will transpire that ∀x¬A and ¬∃xA are in general logically equivalent. It already counts both forms as acceptable for "No one is angry", so some sentences have more than one good symbolization (p. 195).
- The domain fixes what the quantifiers range over. It must be non-empty, and every name must pick out exactly one member of it (pp. 196–197).
- Names that refer to nothing (e.g. "Chimera") are not allowed. To talk about myths or fiction, put those things in the domain (p. 198).

## L3 — Walkthrough

### 23.1 The need to decompose sentences
- The argument *Willard is a logician. All logicians wear funny hats. ∴ Willard wears a funny hat.* is obviously valid in English (p. 190).
- TFL key: L = *Willard is a logician*, A = *All logicians wear funny hats*, F = *Willard wears a funny hat*. The argument becomes $L, A \therefore F$. The truth-table test says it is invalid (p. 190).
- The authors say the fault is not a symbolizing mistake. This is the best TFL symbolization. The fault lies with TFL itself. *All logicians wear funny hats* is about both logicians and hat-wearing, and sentence letters lose that connection (p. 191).
- Remedy: the language FOL, which will "split the atom" (p. 191). It has three ingredients:
  - **Names:** lowercase italic letters (e.g. $b$ for Bertie).
  - **Predicates:** uppercase italic letters. English predicates such as *___ is a dog* are not complete sentences. If $D$ symbolizes *___ is a dog*, then $D(b)$ symbolizes *Bertie is a dog*.
  - **Quantifiers:** ∃ roughly means *there is at least one…*. *There is a dog* becomes $\exists x\, D(x)$, read *there is at least one thing, x, such that x is a dog* (pp. 191–192).
- FOL is also called classical predicate or quantificational logic (fn. 1, p. 191).

*Intuition note:* In TFL a sentence like *All logicians wear funny hats* is a single block, so the structure of what it is about is lost. FOL lets a sentence mention a thing and a property separately, so an argument can use the link between them.

### 23.2 Names
- A singular term refers to a specific person, place or thing. "Bertie" and "Philip's dog" are singular terms; "dog" is not. A proper name picks out an individual without describing it (p. 192).
- FOL names are lowercase letters $a$ to $r$, with optional subscripts, e.g. $a_1, f_{32}, j_{390}, m_{12}$ (p. 192).
- Unlike English, FOL does not tolerate ambiguity in names (English lets context settle which Tim Button is meant): each name picks out exactly one thing. Different names may pick out the same thing, and things may lack names (pp. 192–193).
- A symbolization key says temporarily what a name picks out, e.g. $e$: Elsa, $g$: Gregor, $m$: Marybeth (p. 193).

### 23.3 Predicates
- Predicates combine with singular terms to make sentences. Removing a singular term from a sentence gives a predicate. From *Vinnie borrowed the family car from Nunzio* we get three different predicates, one for each removable term (p. 193).
- FOL predicates are capital letters $A$ to $Z$, with optional subscripts. Keys look like $A(x)$: "x is angry" and $H(x)$: "x is happy". The reason for the subscripted gaps is left to chapter 25 (pp. 193–194).
- Examples with $e, g, m$ (p. 194):
  1. "Elsa is angry": $A(e)$.
  2. *Gregor and Marybeth are angry*: $A(g) \land A(m)$.
  3. *If Elsa is angry, then so are Gregor and Marybeth*: $A(e) \to (A(g) \land A(m))$.
- FOL has all the truth-functional connectives of TFL (p. 194).

### 23.4 Quantifiers
- "Everyone is happy" should not be $H(e) \land H(g) \land H(m)$. That only says three named people are happy. We want to cover those with no names (p. 194).
- The universal quantifier is ∀. A quantifier must always be followed by a variable. Variables are lowercase italic letters $s$ to $z$, with optional subscripts. "Everyone is happy" is $\forall x\, H(x)$. Here $x$ is a placeholder: ∀x intuitively means you can pick anyone and put them in as $x$ (p. 195).
- The choice of variable does not matter. $\forall x H(x)$, $\forall y H(y)$, $\forall z H(z)$ and $\forall x_5 H(x_5)$ are all logically equivalent (p. 195).
- The existential quantifier is ∃. "Someone is angry" is $\exists x\, A(x)$, read *there is something, x, such that x is angry* (p. 195).
- Further examples (pp. 195–196):
  - 6. *No one is angry*: $\neg\exists x\, A(x)$, or *Everyone is not angry*, $\forall x\, \neg A(x)$. Both are acceptable. The text says it will transpire that, in general, $\forall x\,\neg\mathcal{A}$ is logically equivalent to $\neg\exists x\,\mathcal{A}$, where $\mathcal{A}$ is a metavariable (a stand-in for any formula) (p. 195).
  - 7. *There is someone who is not happy*: $\exists x\, \neg H(x)$.
  - 8. *Not everyone is happy*: $\neg\forall x\, H(x)$. The text calls $\neg\forall x H(x)$, read as *it is not the case that everyone is happy*, a perfectly adequate symbolization of sentence 8. It introduces it as something we "could equally have written" right after giving $\exists x\,\neg H(x)$ for 7 (p. 196).
- Choosing one form over the other is "not much more than a matter of taste" (p. 195).

*Intuition note:* ∀ and ∃ speak about a whole collection without listing its members. *No one is angry* can be symbolized in two ways, as ¬∃x A(x) or as ∀x ¬A(x). The text calls both acceptable.

### 23.5 Domains
- In English, *everyone* usually does not mean everyone now alive on Earth, and certainly not everyone who ever lived or will live. It usually means something more modest, such as everyone in the building (p. 196).
- To remove this ambiguity we specify a domain, "the collection of things that we are talking about", written at the start of the key, e.g. `domain: people in Chicago`. The quantifiers range over the domain (p. 196).
- Rules (p. 197):
  - The domain must have at least one member.
  - Every name must pick out exactly one member of the domain.
  - A member may be picked out by one name, many names, or none.
- Reason for the name rule: English lets us infer "something is angry" from "Gregor is angry", so FOL should let us infer $\exists x A(x)$ from $A(g)$ (p. 196).
- Example: `domain: the Eiffel Tower`, $P(x)$: x is in Paris. Then $\forall x\, P(x)$ means only that everything in the domain is in Paris, i.e. the Eiffel Tower is in Paris. Reading it as *Everything is in Paris* would mislead (p. 197).

### 23.6 Non-referring terms
- Each name must pick out something. This is tied to the classic problem of non-referring terms, which medieval philosophers illustrated with the chimera, a mythological creature that does not exist (p. 197).
- Key: domain: creatures on Earth; $A(x)$: x is angry; $c$: chimera. Sentence 9 "Chimera is angry" is $A(c)$; sentence 10 *Chimera is not angry* is $\neg A(c)$ (pp. 197–198).
- **Option 1 (considered and rejected):** say 9 is false because there is no chimera. Then 10 is false for the same reason, so $A(c)$ and $\neg A(c)$ are both false. Given the truth conditions for negation, this cannot be so (p. 198).
- **Option 2 (considered and rejected):** say 9 is meaningless. Then $A(c)$ would be meaningful under some interpretations and not others. That would make the language "hostage to particular interpretations", and we could not study logical form apart from interpretation (p. 198).
- Conclusion: each FOL name must refer to something in the domain, but the domain can contain any things we like. To symbolize arguments about mythological creatures or fiction (e.g. Sherlock Holmes at 221B Baker Street), put them in the domain. The problem is revisited in chapter 28 (p. 198).

*Intuition note:* FOL avoids empty names by a design choice: a name always needs an object. If you want a chimera to be nameable, you must first admit it into the domain.

## Toy example (ours)
Key: domain: {Ann, Bo, Cy}; names $a$: Ann, $b$: Bo (Cy has no name); $H(x)$: x is happy. Suppose Ann and Bo are happy and Cy is not.
- $H(a) \land H(b)$: both conjuncts true, so true.
- $\forall x\, H(x)$: needs all three happy. Cy is not, so false. The named conjunction cannot capture "everyone" (as p. 194 says).
- $\exists x\, H(x)$: Ann is happy, so true.
- $\exists x\, \neg H(x)$: Cy is not happy, so true. $\neg\forall x\, H(x)$ is also true, since $\forall x H(x)$ is false. Both agree, as p. 196 says.
- $\forall x\, \neg H(x)$: Ann is happy, so false. $\neg\exists x\, H(x)$: $\exists x H(x)$ is true, so false. Both are false, matching the equivalence on p. 195.

## Concepts
- [[logical form vs. grammatical form]] — the TFL symbolization hides the inner structure of "All logicians…", which FOL aims to expose (p. 191).
- [[validity / soundness]] — the Willard argument is obviously valid, but its TFL form fails the truth-table test (p. 190).
- [[fol-name]] (new) — lowercase letter $a$–$r$ picking out exactly one thing in the domain (pp. 192, 197).
- [[singular-term]] (new) — word or phrase meant to refer to one specific person, place or thing (p. 192).
- [[fol-predicate]] (new) — capital letter $A$–$Z$ for a sentence with a singular term removed (pp. 191, 193).
- [[universal-quantifier]] (new) — ∀, followed by a variable; "for all" over the domain (pp. 194–195).
- [[existential-quantifier]] (new) — ∃, followed by a variable; *there is at least one* in the domain (p. 195).
- [[variable]] (new) — letter $s$–$z$ that works as a placeholder after a quantifier (p. 195).
- [[domain]] (new) — the collection of things we talk about; non-empty (pp. 196–197).
- [[non-referring-terms]] (new) — the problem posed by names, like "Chimera", that refer to nothing; FOL requires every name to refer (pp. 197–198).

## Canonical instances
- [[willard-funny-hat-argument]] — valid in English but invalid in TFL; motivates FOL (p. 190).
- [[eiffel-tower-domain]] — a one-member domain makes ∀x P(x) mean just that the Tower is in Paris (p. 197).
- [[chimera-sentences]] — A(c) and ¬A(c) show why empty names cause trouble (pp. 197–198).
- [[sherlock-holmes-domain]] — fictional characters can be handled by putting them in the domain (p. 198).

## Bridges (candidates)
- [structural-analogy] FOL predicate (a sentence with a gap) ↔ computing: a Boolean-valued function that takes an object and returns true or false — both give a truth value once the gap is filled.
- [structural-analogy] The domain as the range of quantifiers ↔ set theory: the universe of discourse for a statement "for all x in S".
- [metaphor] "Splitting the atom" ↔ physics: breaking a basic unit into parts to see structure inside.

## Questions this raises
- How can FOL symbolize "All logicians wear funny hats" so that the Willard argument comes out valid? (The unit only promises to build toward this.)
- Why are subscripts on predicate gaps needed (promised in chapter 25)?
- Is requiring a non-empty domain and referring names a harmless convenience, or does it have costs? (Chapter 28 returns to this.)
- Does putting fictional characters in the domain commit us to saying they exist?

## Reading notes
- Printed page = pdf − 10 (pdf 200 = printed 190). All citations use printed pages.
- Text layer is mostly clean. On p. 194, the image shows the subscript $x$ on the gap in "$H(x)$: ___$_x$ is happy"; the text layer drops it.
- On p. 191 the key letter for Willard is given as $i$ (not $w$), as printed.
- On p. 196 the text introduces ¬∀x H(x) as something we could equally have written after ∃x ¬H(x) (sentence 7), but says it is an adequate symbolization of sentence 8. The digest reports it as printed.
- No exercises in this unit.
