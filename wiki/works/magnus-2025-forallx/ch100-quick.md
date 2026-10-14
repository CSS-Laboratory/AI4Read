---
id: magnus-2025-forallx/ch100-quick
work: magnus-2025-forallx
unit: "Appendix C — Quick reference"
pages: 411–420
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
# Quick reference: truth tables, symbolization, deduction rules, equivalences

## L0 — One line
Appendix C is a lookup sheet of the book's formal toolkit: truth tables, English-to-symbol patterns, numerical quantifiers with identity, deduction rules (basic and derived), citation rules and equivalence laws.

## L1 — The gist (≤ 120 words)
The appendix has no argument. It collects, in nine short sections, the standard patterns a student needs when working in the book's formal languages. First come the truth tables for the five connectives. Then come patterns for translating English into symbols, including at least / at most / exactly $n$ and the $F$. Next are the natural-deduction rules for sentence logic (TFL) and quantifier logic (FOL), with the derived rules and the rules for citing lines and subproofs. The last section lists equivalence laws for rewriting formulas step by step. Use it to check a symbolization or proof step quickly. It explains nothing.

**Prerequisites:** the connectives ¬, ∧, ∨, →, ↔; quantifiers ∀, ∃; identity "="; the idea of a subproof (an indented block that starts from an assumption); natural deduction (proving by rules, line by line); a derived rule (an extra rule listed after the basic ones); a constant $c$ (a name for one individual).

## L2 — Key ideas (5–10 bullets)
- The truth tables fix each connective's meaning. → is false only when A is true and B is false (p. 411).
- Many English phrases have two listed symbolizations, joined by "or" in the table: "neither…nor", "not all", "no", "unless" (p. 412).
- *All Fs are Gs* uses →; *Some Fs are Gs* uses ∧. *Only Fs are Gs* reverses the direction of the conditional (p. 412).
- Identity lets us say *the $F$ is $G$*: there is an $F$, anything that is $F$ is that thing, and it is $G$ (p. 412).
- Identity also expresses quantity: "at least $n$", "at most $n$" and "exactly $n$" each have a pattern (pp. 413–414).
- Each connective has an introduction and an elimination rule. Quantifier rules ∀I and ∃E carry restrictions on the constant $c$ (pp. 415–418).
- Citation rules give conditions that a cited line or subproof must meet (pp. 418–419).
- Equivalence laws such as De Morgan and Distribution let you rewrite a formula in a chain of steps (p. 420).

## L3 — Walkthrough

### C.1 Characteristic truth tables (p. 411)
Negation: ¬A has the opposite value to A. Rows of (A, B) in order TT, TF, FT, FF:

| A | B | A∧B | A∨B | A→B | A↔B |
|---|---|---|---|---|---|
| T | T | T | T | T | T |
| T | F | F | T | F | F |
| F | T | F | T | T | F |
| F | F | F | F | T | T |

*Intuition note:* ∧ needs both parts true. ∨ needs at least one. → fails only when the "if" part is true and the "then" part is false. ↔ is true when both sides have the same value.

### C.2 Symbolization (p. 412)
**Sentential connectives**
- It is not the case that P: $\neg P$
- Either P or Q: $(P\lor Q)$
- Neither P nor Q: $\neg(P\lor Q)$ or $(\neg P\land\neg Q)$
- Both P and Q: $(P\land Q)$
- If P then Q: $(P\to Q)$
- P only if Q: $(P\to Q)$
- P if and only if Q: $(P\leftrightarrow Q)$
- P unless Q: $(\neg Q\to P)$ or $(P\lor Q)$

**Predicates**
- All Fs are Gs: $\forall x(F(x)\to G(x))$
- Some Fs are Gs: $\exists x(F(x)\land G(x))$
- Not all Fs are Gs: $\neg\forall x(F(x)\to G(x))$ or $\exists x(F(x)\land\neg G(x))$
- No Fs are Gs: $\forall x(F(x)\to\neg G(x))$ or $\neg\exists x(F(x)\land G(x))$
- Only Fs are Gs: $\forall x(G(x)\to F(x))$; a second form is listed on the next line: $\neg\exists x(\neg F(x)\land G(x))$

**Identity**
- Only $c$ is $G$: $\forall x(G(x)\leftrightarrow x=c)$
- Everything other than $c$ is $G$: $\forall x(\neg x=c\to G(x))$
- Everything except $c$ is $G$: $\forall x(\neg x=c\leftrightarrow G(x))$
- The $F$ is $G$: $\exists x(F(x)\land\forall y(F(y)\to x=y)\land G(x))$
- It is not the case that the $F$ is $G$: $\neg\exists x(F(x)\land\forall y(F(y)\to x=y)\land G(x))$
- The $F$ is non-$G$: $\exists x(F(x)\land\forall y(F(y)\to x=y)\land\neg G(x))$

*Intuition note:* The clause $\forall y(F(y)\to x=y)$ says nothing else is $F$. That is how "the" (exactly one) is built from plain quantifiers and identity.

### C.3 Using identity to symbolize quantities (pp. 413–414)
**At least $n$ Fs** (p. 413):
- one: $\exists x\,F(x)$.
- two: $\exists x_1\exists x_2(F(x_1)\land F(x_2)\land\neg x_1=x_2)$.
- three: $\exists x_1\exists x_2\exists x_3(F(x_1)\land F(x_2)\land F(x_3)\land\neg x_1=x_2\land\neg x_1=x_3\land\neg x_2=x_3)$.
- four: the same pattern, with all six distinctness clauses.
- general:
$$\exists x_1\ldots\exists x_n(F(x_1)\land\ldots\land F(x_n)\land\neg x_1=x_2\land\ldots\land\neg x_{n-1}=x_n)$$
The author abbreviates the list of distinctness clauses with dots.

**At most $n$ Fs** (p. 413). One way is to put a negation in front of "at least $n+1$". Equivalent forms are:
- one: $\forall x_1\forall x_2[(F(x_1)\land F(x_2))\to x_1=x_2]$.
- two: $\forall x_1\forall x_2\forall x_3[(F(x_1)\land F(x_2)\land F(x_3))\to(x_1=x_2\lor x_1=x_3\lor x_2=x_3)]$.
- general:
$$\forall x_1\ldots\forall x_{n+1}[(F(x_1)\land\ldots\land F(x_{n+1}))\to(x_1=x_2\lor\ldots\lor x_n=x_{n+1})]$$

**Exactly $n$ Fs** (pp. 413–414). One way is to conjoin "at least $n$" and "at most $n$". Shorter equivalent forms:
- zero: $\forall x\,\neg F(x)$.
- one: $\exists x[F(x)\land\forall y(F(y)\to x=y)]$.
- two: $\exists x_1\exists x_2[F(x_1)\land F(x_2)\land\neg x_1=x_2\land\forall y(F(y)\to(y=x_1\lor y=x_2))]$.
- general:
$$\exists x_1\ldots\exists x_n[F(x_1)\land\ldots\land F(x_n)\land\neg x_1=x_2\land\ldots\land\neg x_{n-1}=x_n\land\forall y(F(y)\to(y=x_1\lor\ldots\lor y=x_n))]$$

*Intuition note:* "At least" lists distinct witnesses. "At most" says any $n+1$ Fs must include a repeat. "Exactly" lists $n$ distinct witnesses and then says every F is one of them.

### C.4 Basic deduction rules for TFL (pp. 415–416)
In each rule, $m$, $n$, … are line numbers. AS appears on the first line of each subproof (an assumption).
- Reiteration: from A, write A (R).
- ∧I: from A and B, write A∧B. ∧E: from A∧B, write A, or write B.
- →I: assume A, derive B in the subproof, then write A→B (cite $m$–$n$). →E: from A→B and A, write B.
- ¬I: assume A, derive ⊥ (contradiction), then write ¬A. ¬E: from ¬A and A, write ⊥.
- IP (indirect proof): assume ¬A, derive ⊥, then write A.
- X (explosion): from ⊥, write any A.
- ∨I: from A, write A∨B, or write B∨A.
- ∨E: from A∨B, a subproof A…C and a subproof B…C, write C.
- ↔I: from subproofs A…B and B…A, write A↔B. ↔E: from A↔B and one side, write the other side.

### C.5 Derived rules for TFL (pp. 416–417)
- DS (disjunctive syllogism): from A∨B and ¬A, write B; from A∨B and ¬B, write A.
- MT (modus tollens): from A→B and ¬B, write ¬A.
- DNE: from ¬¬A, write A.
- LEM (excluded middle): from subproofs A…B and ¬A…B, write B.
- DeM: ¬A∧¬B to ¬(A∨B); ¬(A∨B) to ¬A∧¬B; ¬(A∧B) to ¬A∨¬B; ¬A∨¬B to ¬(A∧B).

### C.6 Basic deduction rules for FOL (pp. 417–418)
- ∀E: from $\forall x\,\mathscr A(\ldots x\ldots x\ldots)$, write $\mathscr A(\ldots c\ldots c\ldots)$.
- ∀I: from $\mathscr A(\ldots c\ldots c\ldots)$, write $\forall x\,\mathscr A(\ldots x\ldots x\ldots)$. Condition: $c$ must not occur in any undischarged assumption.
- ∃I: from $\mathscr A(\ldots c\ldots c\ldots)$, write $\exists x\,\mathscr A(\ldots x\ldots c\ldots)$. The image shows $x$ replacing only some occurrences of $c$.
- ∃E: from $\exists x\,\mathscr A(\ldots x\ldots x\ldots)$, assume $\mathscr A(\ldots c\ldots c\ldots)$ and derive $\mathscr B$. Then write $\mathscr B$. Condition: $c$ must not occur in any undischarged assumption, in $\exists x\,\mathscr A(\ldots x\ldots x\ldots)$, or in $\mathscr B$.
- =I: write $c=c$ at any point.
- =E: from $a=b$ and $\mathscr A(\ldots a\ldots a\ldots)$, write $\mathscr A(\ldots b\ldots a\ldots)$. Symmetrically, from $a=b$ and $\mathscr A(\ldots b\ldots b\ldots)$, write $\mathscr A(\ldots a\ldots b\ldots)$.

*Intuition note:* The conditions on $c$ are what let it act as an arbitrary name: it is not tied to any undischarged assumption (and, for ∃E, not to $\exists x\,\mathscr A$ or $\mathscr B$). This is our gloss; the page states only the conditions.

### C.7 Derived rules for FOL (p. 418)
CQ (quantifier exchange) has four directions: $\forall x\neg\mathscr A \Leftrightarrow \neg\exists x\mathscr A$ and $\exists x\neg\mathscr A\Leftrightarrow\neg\forall x\mathscr A$. Each can be applied either way, as a line-to-line rule.

### C.8 Subproofs and citations (pp. 418–419)
- **Citing a line:** it must come before the line where the rule is applied. It must not lie inside a subproof closed before that line.
- **Citing a subproof:** (1) it must lie entirely before the rule's application; (2) it must not lie within some other closed subproof that is closed at the line where it is cited; (3) its last line must not occur inside a nested subproof.

### C.9 Rules for chains of equivalences (p. 420)
Each law is written with ⇔:
- (DN) $\neg\neg P\Leftrightarrow P$.
- (Cond) $(P\to Q)\Leftrightarrow(\neg P\lor Q)$ and $\neg(P\to Q)\Leftrightarrow(P\land\neg Q)$.
- (Bicond) $(P\leftrightarrow Q)\Leftrightarrow((P\to Q)\land(Q\to P))$.
- (DeM) $\neg(P\land Q)\Leftrightarrow(\neg P\lor\neg Q)$ and $\neg(P\lor Q)\Leftrightarrow(\neg P\land\neg Q)$.
- (Comm) $P\lor Q\Leftrightarrow Q\lor P$ and $P\land Q\Leftrightarrow Q\land P$.
- (Dist) $P\land(Q\lor R)\Leftrightarrow(P\land Q)\lor(P\land R)$ and $P\lor(Q\land R)\Leftrightarrow(P\lor Q)\land(P\lor R)$.
- (Assoc) $P\lor(Q\lor R)\Leftrightarrow(P\lor Q)\lor R$ and $P\land(Q\land R)\Leftrightarrow(P\land Q)\land R$.
- (Id) $P\lor P\Leftrightarrow P$ and $P\land P\Leftrightarrow P$.
- (Abs) $P\land(P\lor Q)\Leftrightarrow P$ and $P\lor(P\land Q)\Leftrightarrow P$.
- (Simp) $P\land(Q\lor\neg Q)\Leftrightarrow P$ and $P\lor(Q\land\neg Q)\Leftrightarrow P$.
- Two further laws with no label: $P\lor(Q\lor\neg Q)\Leftrightarrow Q\lor\neg Q$ and $P\land(Q\land\neg Q)\Leftrightarrow Q\land\neg Q$.

## Toy example (ours, not from the text)
Domain $\{1,2,3\}$. Check "exactly two Fs" (the C.3 form for two) in two situations.
- Case A: $F$ is true of 1 and 2 only. Take $x_1=1$, $x_2=2$. Then $F(x_1)$, $F(x_2)$ and $\neg x_1=x_2$ are true. For $\forall y(F(y)\to(y=1\lor y=2))$: $y=1$ and $y=2$ satisfy the consequent. For $y=3$, $F(3)$ is false, so the conditional is true. The formula is **true**.
- Case B: $F$ is true of 1, 2 and 3. For $x_1,x_2$ distinct, pick $y$ as the third element. $F(y)$ is true but $y=x_1$ and $y=x_2$ are both false. So the conditional fails for every choice of distinct $x_1,x_2$. Choices with $x_1=x_2$ fail the clause $\neg x_1=x_2$. The formula is **false**.
- "At most one" in Case A: $x_1=1$, $x_2=2$ makes $F(x_1)\land F(x_2)$ true and $x_1=x_2$ false. So $\forall x_1\forall x_2[(F(x_1)\land F(x_2))\to x_1=x_2]$ is **false**, as expected.

## Concepts
- [[tfl-truth-tables]] (new) — the five connective tables fixing ¬, ∧, ∨, →, ↔ (p. 411)
- [[symbolization-patterns]] (new) — standard formulas for English phrases such as *only Fs are Gs* (p. 412)
- [[numerical-quantification-with-identity]] (new) — *at least / at most / exactly $n$* built from ∃, ∀ and identity (pp. 413–414)
- [[natural-deduction-rules]] (new) — introduction/elimination rules for connectives, quantifiers and identity (pp. 415–418)
- [[subproof-citation-rules]] (new) — conditions a line or subproof must meet to be cited by a rule (pp. 418–419)
- [[equivalence-laws]] (new) — ⇔ laws (DN, DeM, Dist…) for rewriting in chains (p. 420)
- [[theory-of-descriptions]] — canon link only: this unit gives the formula for *The $F$ is $G$* but does not name any theory (p. 412)

## Canonical instances
- [[the-F-is-G]] — uniqueness-plus-property formula for definite descriptions (p. 412)
- [[exactly-two-Fs]] — the standard two-witness formula with $\forall y$ closing clause (p. 414)

## Bridges (candidates)
- [structural-analogy] at most $n$ = ¬(at least $n+1$) ↔ counting/combinatorics: the pigeonhole-style idea that any $n+1$ items include a repeat — a similar counting idea; the unit gives only the formulas.
- [same-math] DeM and Distribution laws ↔ Boolean algebra / set theory: the same laws hold for complement, union and intersection, and Distribution has the same shape.
- [structural-analogy] ∀I/∃E "arbitrary $c$" restrictions ↔ mathematics: proving a claim for an arbitrary element, assuming nothing special about it.
- [structural-analogy] the *The $F$ is $G$* formula ↔ analytic-philosophy canon: theory of descriptions (canon link; not stated in this unit).

## Questions this raises
- Why do *P only if Q* and *If P then Q* get the same symbolization $(P\to Q)$?
- Why must $c$ in ∃E not occur in the conclusion $\mathscr B$?
- Which pairs of symbolizations listed with "or" are equivalent, and how could one show it with the C.9 laws?
- Are the derived rules (DS, MT, LEM, DeM, CQ) strictly needed, given the basic rules?

## Reading notes
- Printed page = pdf − 10 (pdf 421–430 are printed 411–420).
- The text layer is garbled for brackets in C.3 and for tables and subproofs in C.4–C.7. Formulas here were checked against the page images (pdf 422–428, 430). pdf 421 and 429 had no image, so C.1 and the top of p. 419 (the rest of C.8) follow the text layer only.
- On p. 417 the text layer lists the DeM rules in a confusing order. The images show the four directions given in C.5 above.
- The last two laws on p. 420 have no label in the image. The two lines above them are grouped under (Simp).
- C.8's first list is split across pages 418–419, and its item 2 reads *not occur within a subproof…*. I read *the line must…* as carried over from item 1.
- Section C.1 states no explicit definition of "TFL" or "FOL". The appendix uses these labels for the connective rules (C.4–C.5) and the quantifier/identity rules (C.6–C.7).
