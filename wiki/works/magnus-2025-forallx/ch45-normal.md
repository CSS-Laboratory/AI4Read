---
id: magnus-2025-forallx/ch45-normal
work: magnus-2025-forallx
unit: "45 Normal forms"
pages: 369-374
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 3
pipeline_version: 0.1
---
# Normal forms

## L0 — One line
Every TFL sentence is logically equivalent to a sentence in disjunctive normal form (an ∨ of ∧s of atomic or negated atomic sentences) and to one in conjunctive normal form (an ∧ of ∨s), and both can be read off the truth table.

## L1 — The gist (≤ 120 words)
The chapter asks whether every sentence can be rewritten in a very simple shape without changing its truth conditions. It defines disjunctive normal form (DNF) and conjunctive normal form (CNF). It then proves that the answer is yes. The proof works from the truth table. For DNF, write one conjunction for each line where the sentence is true, and join them with ∨. For CNF, write one disjunction for each line where the sentence is false, and join them with ∧. Since DNF and CNF sentences use only ¬, ∧ and ∨, every sentence has an equivalent that uses only these connectives, and the proof gives a step-by-step recipe for finding it.

**Prerequisites:** atomic sentences; the connectives ¬, ∧, ∨; truth tables; logical equivalence (same truth table).

## L2 — Key ideas
- A sentence is in DNF iff it uses only ¬, ∧, ∨; every ¬ sits directly before an atomic sentence; and no ∨ lies inside the scope of an ∧ (p. 369).
- DNF Theorem: every sentence has an equivalent sentence in DNF (p. 370).
- Construction: for each line where S is true, write a conjunction that is true on that line only. Disjoin these conjunctions (pp. 371–372).
- If S is false on every line, the contradiction $(\mathcal{A}_1 \land \lnot\mathcal{A}_1)$ is the DNF; it is a separate case (p. 372).
- Equivalence holds because S and the DNF sentence are true on exactly the same lines (p. 373).
- CNF is defined by swapping the roles of ∧ and ∨ in the DNF conditions (p. 373).
- CNF Theorem: use the false lines, with a disjunction per false line, joined by ∧. If S is true everywhere, use $(\mathcal{A}_1 \lor \lnot\mathcal{A}_1)$ (p. 374).

## L3 — Walkthrough

### 45.1 Disjunctive normal form
- The author wants sentences of a simple form. A DNF sentence is built in stages: atomic sentences, then (perhaps) negations, then (perhaps) ∧, then (perhaps) ∨ (p. 369).
- **Definition.** A sentence is in DNF iff all three hold (p. 369):
  - (dnf1) the only connectives are ¬, ∧, ∨;
  - (dnf2) every ¬ has minimal scope, i.e. is immediately followed by an atomic sentence;
  - (dnf3) no disjunction occurs within the scope of any conjunction.
- Examples in DNF (p. 370): $A$; $(A\land\lnot B\land C)$; $(A\land B)\lor(A\land\lnot B)$; $(A\land B)\lor(A\land B\land C\land\lnot D\land\lnot E)$; $A\lor(C\land\lnot P_{234}\land P_{233}\land Q)\lor\lnot B$.
- The author temporarily allows relaxed bracketing: conjunctions and disjunctions of any length (p. 370).
- Notation: $\pm\mathcal{A}$ means an atomic sentence that may or may not have a ¬ in front. A DNF sentence has this shape (p. 370):
$$(\pm\mathcal{A}_1\land\dots\land\pm\mathcal{A}_i)\lor(\pm\mathcal{A}_{i+1}\land\dots\land\pm\mathcal{A}_j)\lor\dots\lor(\pm\mathcal{A}_{m+1}\land\dots\land\pm\mathcal{A}_n)$$
- **DNF Theorem.** For any sentence, there is an equivalent sentence in DNF (p. 370).

*Intuition note:* DNF is a list of alternatives. Each alternative is a "this and this and not that" description. The theorem says any sentence can be turned into such a list.

### 45.2 Proof via truth tables
- **Illustration** (p. 371). S has atoms A, B, C and this truth table (lines 1–8):

| A | B | C | S |
|---|---|---|---|
| T | T | T | T |
| T | T | F | F |
| T | F | T | T |
| T | F | F | F |
| F | T | T | F |
| F | T | F | F |
| F | F | T | T |
| F | F | F | T |

- S is true on lines 1, 3, 7, 8. For each, write a conjunction true on that line only (p. 371):
  - line 1: $A\land B\land C$;
  - line 3: $A\land\lnot B\land C$;
  - line 7: $\lnot A\land\lnot B\land C$;
  - line 8: $\lnot A\land\lnot B\land\lnot C$.
- Join them: $(A\land B\land C)\lor(A\land\lnot B\land C)\lor(\lnot A\land\lnot B\land C)\lor(\lnot A\land\lnot B\land\lnot C)$. It is true exactly when one disjunct is true, i.e. on lines 1, 3, 7, 8. So it has the same truth table as S (pp. 371–372).
- **General proof** (p. 372). Take any S with atoms $\mathcal{A}_1,\dots,\mathcal{A}_n$. There are two exhaustive cases (p. 373).
  - **Case 1: S is false on every line.** Then S is a contradiction. The sentence $(\mathcal{A}_1\land\lnot\mathcal{A}_1)$ is in DNF and equivalent to S.
  - **Case 2: S is true on at least one line.** For each line $i$, let $\mathcal{B}_i$ be $(\pm\mathcal{A}_1\land\dots\land\pm\mathcal{A}_n)$ with these rules:
    - $\mathcal{A}_m$ is a conjunct of $\mathcal{B}_i$ iff $\mathcal{A}_m$ is true on line $i$;
    - $\lnot\mathcal{A}_m$ is a conjunct of $\mathcal{B}_i$ iff $\mathcal{A}_m$ is false on line $i$.
  - Then $\mathcal{B}_i$ is true on, and only on, line $i$.
  - Let $i_1,\dots,i_m$ be the lines where S is true, and let $\mathcal{D}=\mathcal{B}_{i_1}\lor\mathcal{B}_{i_2}\lor\dots\lor\mathcal{B}_{i_m}$.
  - $\mathcal{D}$ is well-defined because there is at least one true line. If there is exactly one, $\mathcal{D}$ is just $\mathcal{B}_{i_1}$.
  - $\mathcal{D}$ is in DNF by construction. On each line $i$, S is true iff one of $\mathcal{D}$'s disjuncts (namely $\mathcal{B}_i$) is true. So S and $\mathcal{D}$ have the same truth table and are equivalent (p. 373).
- After the proof, the author flags a return to the austere definition of a TFL sentence, under which any conjunction can be assumed to have exactly two conjuncts and any disjunction exactly two disjuncts (p. 373).

*Intuition note:* Each true line of the table becomes one fully detailed description of that situation. S says "one of these situations holds". Nothing else is needed.

### 45.3 Conjunctive normal form
- **Definition.** CNF is defined by exactly analogous conditions (p. 373):
  - (cnf1) the only connectives are ¬, ∧, ∨;
  - (cnf2) every ¬ has minimal scope;
  - (cnf3) no conjunction occurs within the scope of any disjunction.
- General shape (p. 373): $(\pm\mathcal{A}_1\lor\dots\lor\pm\mathcal{A}_i)\land(\pm\mathcal{A}_{i+1}\lor\dots\lor\pm\mathcal{A}_j)\land\dots\land(\pm\mathcal{A}_{m+1}\lor\dots\lor\pm\mathcal{A}_n)$.
- **CNF Theorem.** For any sentence, there is an equivalent sentence in CNF (p. 373).
- **Proof sketch** (p. 374): start from the full truth table of S.
  - If S is true on every line, S is equivalent to $(\mathcal{A}_1\lor\lnot\mathcal{A}_1)$.
  - If S is false on at least one line, then for each false line write a disjunction $(\pm\mathcal{A}_1\lor\dots\lor\pm\mathcal{A}_n)$ that is false on, and only on, that line. Let $\mathcal{C}$ be the conjunction of these. By construction $\mathcal{C}$ is in CNF and equivalent to S.
  - *(added step)* To make a disjunction false on exactly one line, include $\mathcal{A}_m$ if it is false on that line, and $\lnot\mathcal{A}_m$ if it is true there. Then every disjunct is false on that line, and on any other line some disjunct is true.

*Intuition note:* CNF works by exclusion. Each conjunct rules out one false line. Together they rule out all the false lines and nothing else.

### Practice exercises (p. 374)
Exercise A gives six sentences, and for each asks for an equivalent sentence in DNF and one in CNF.

## Toy example (ours, not from the text)
Take $S = (A\to B)$. Its truth table is:

| Line | A | B | S |
|---|---|---|---|
| 1 | T | T | T |
| 2 | T | F | F |
| 3 | F | T | T |
| 4 | F | F | T |

- **DNF:** S is true on lines 1, 3, 4. Conjunctions: $A\land B$, $\lnot A\land B$, $\lnot A\land\lnot B$. So $D=(A\land B)\lor(\lnot A\land B)\lor(\lnot A\land\lnot B)$.
  - Check line 2 (A=T, B=F): $A\land B$ is F, $\lnot A\land B$ is F, $\lnot A\land\lnot B$ is F, so D is F. ✓.
  - Lines 1, 3, 4 each make one disjunct true. ✓.
- **CNF:** S is false only on line 2 (A=T, B=F). The disjunction false only there is $\lnot A\lor B$: $\lnot A$ is F and $B$ is F.
  - Line 1: B is T. Line 3: $\lnot A$ is T. Line 4: $\lnot A$ is T. So it is true on all other lines. ✓.
  - With one false line, $\mathcal{C}$ is just $(\lnot A\lor B)$.

## Concepts
- [[disjunctive-normal-form]] (new) — a sentence using only ¬, ∧, ∨, with ¬ only on atoms and no ∨ inside an ∧ (p. 369).
- [[conjunctive-normal-form]] (new) — the same, but with no ∧ inside an ∨ (p. 373).
- [[logical-equivalence]] (new) — two sentences with the same truth table (p. 373).
- [[minimal-scope]] (new) — a ¬ that is immediately followed by an atomic sentence (p. 369).
- [[normal-form-theorem]] (new) — every sentence has an equivalent in DNF, and one in CNF (pp. 370, 373).

## Canonical instances
- [[three-atom-dnf-from-truth-table]] (new) — S true on lines 1, 3, 7, 8 gives a four-disjunct DNF (p. 371).
- [[contradiction-as-dnf]] (new) — the contradiction $(\mathcal{A}_1\land\lnot\mathcal{A}_1)$ serves as a DNF for an always-false sentence (p. 372).

## Bridges (candidates)
- [structural-analogy] DNF and CNF swap ∧ and ∨ ↔ duality in logic: the two definitions mirror each other, and so do the two constructions (true lines versus false lines).
- [structural-analogy] DNF as a list of true lines ↔ computing: a function is written as a table of inputs, with one clause per input that gives output 1.

## Questions this raises
- With $n$ atoms the table has $2^n$ lines. How long can the resulting DNF be?
- Is the construction's output the shortest equivalent DNF? The text does not say.
- The text calls this its "first proof" (p. 371). Can the theorem be proved without truth tables?
- Could we avoid the special contradiction case? What does the CNF case for "true everywhere" suggest?

## Exercises worth doing
- Ex. A.1–A.2 (p. 374) — $(A\to\lnot B)$ and $\lnot(A\leftrightarrow B)$: practise the table-to-DNF/CNF method on two atoms — difficulty: easy
- Ex. A.4 (p. 374) — $(\lnot(A\to B)\land(A\to C))$: three atoms, a fairly sparse true set — difficulty: medium
- Ex. A.5–A.6 (p. 374) — larger sentences, with three or four atoms: shows how big the tables become — difficulty: hard

## Reading notes
- Printed page numbers are visible; printed = pdf − 10.
- p. 370 has a typo: "here are are". Also, the CNF proof (p. 374) says "the conjunction of all of these disjuncts". The context shows it means the disjunctions written down.
- The CNF proof is only sketched in the source. It does not check the equivalence step by step, and the way to make a disjunction false on one line is not spelled out; the explanation above is marked as an added step.
- The chapter says the DNF proof is "first"; no second proof appears in these pages.
