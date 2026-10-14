---
id: magnus-2025-forallx/ch46-functional
work: magnus-2025-forallx
unit: "46 Functional completeness"
pages: 375-380
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Functional completeness

## L0 — One line
Every possible truth table can be expressed using only ¬ with ∨ (or ¬ with ∧, or ¬ with →), and even a single connective, ↑ or ↓, is enough, so TFL never needs new connectives.

## L1 — The gist (≤ 120 words)
The chapter asks whether TFL needs extra connectives to express truth tables such as an invented three-place one. It answers no. The DNF method from chapter 45 writes a scheme for any truth table. Logical equivalences then shrink the connectives to ¬ and ∨, ¬ and ∧, or ¬ and →. The single connectives ↑ ("nand") and ↓ ("nor") are each enough alone. The chapter also gives an intuitive reason, based on the top line of the table, why ∨, ∧, →, ↔ alone cannot express negation. It states, without proof, that ↑ and ↓ are the only two-place connectives that are complete alone. This shows how little a truth-functional language needs.

**Prerequisites:** truth tables; logical equivalence; the connectives ¬, ∧, ∨, →, ↔; the DNF theorem (ch. 45).

## L2 — Key ideas (5–10 bullets)
- Connectives can take n places, not only one or two, and a three-place table can be stipulated freely (p. 375).
- "Jointly functionally complete" means that every possible truth table has a sentence using only those connectives (p. 376).
- The TFL connectives are complete, because the DNF/CNF method yields a scheme for any table (p. 376).
- ¬ with ∨, ¬ with ∧, and ¬ with → are each complete, via equivalences that eliminate the other connectives (pp. 376–377).
- ↑ and ↓ are each complete alone, so one primitive connective would suffice (pp. 378–379).
- To show failure, find one truth table the connectives cannot express. For ∨ alone, negation fails because the top line of any ∨-only scheme is True (p. 380).
- The only two-place connectives complete alone are ↑ and ↓. The source calls this harder to prove and gives no proof (p. 380).

## L3 — Walkthrough

**Opening: n-place connectives (p. 375).** An n-place connective takes n sentences. The text stipulates a three-place connective ♥ with this table. Its rows are (A,B,C) ↦ value: TTT↦F, TTF↦T, TFT↦T, TFF↦F, FTT↦F, FTF↦T, FFT↦F, FFF↦F. The question is whether we must add a new connective to TFL, or can get by with the old ones, as we can for "neither… nor" (pp. 375–376).

**Definition (p. 376).** Some connectives are *jointly functionally complete* iff, for any possible truth table, there is a sentence containing only those connectives with that truth table.

**Functional Completeness Theorem (p. 376).** The connectives of TFL are jointly functionally complete. So are these pairs: (1) ¬ and ∨; (2) ¬ and ∧; (3) ¬ and →.

*Proof for TFL (p. 376).* Take any truth table and use the DNF (or CNF) truth-table method of chapter 45. For ♥ this gives a scheme with the same table:
$$(A \land B \land \lnot C) \lor (A \land \lnot B \land C) \lor (\lnot A \land B \land \lnot C)$$
(added step: these are the three lines where ♥ is T: TTF, TFT, FTF.)

*Subsidiary Result 1: ¬ and ∨ (pp. 376–377).* The DNF method produces schemes with only ¬, ∧, ∨. So it suffices to find an equivalent scheme with only ¬ and ∨. Use
$$(\mathcal{A} \land \mathcal{B}) \Leftrightarrow \lnot(\lnot\mathcal{A} \lor \lnot\mathcal{B}).$$

*Subsidiary Result 2: ¬ and ∧ (p. 377).* The same, using
$$(\mathcal{A} \lor \mathcal{B}) \Leftrightarrow \lnot(\lnot\mathcal{A} \land \lnot\mathcal{B}).$$

*Subsidiary Result 3: ¬ and → (p. 377).* The same, using
$$(\mathcal{A} \lor \mathcal{B}) \Leftrightarrow (\lnot\mathcal{A} \to \mathcal{B}), \qquad (\mathcal{A} \land \mathcal{B}) \Leftrightarrow \lnot(\mathcal{A} \to \lnot\mathcal{B}).$$
Alternatively, one can rely on Result 1 or 2 and repeatedly invoke only one of these two equivalences (p. 377).

The text concludes that there is never any need to add new connectives to TFL. There is already some redundancy among the connectives, and we could have made do with just two (p. 377).

Footnote 1 (p. 377): ⇔ abbreviates "is equivalent to". It is a metalinguistic symbol, like ⊨, not a connective like ↔.

*Intuition note.* DNF turns any table into a big "or" of "and" lines. An equivalence then hides ∧ (or ∨) behind negation. So no table is out of reach, and some of our connectives are redundant (p. 377).

**46.1 Individually functionally complete connectives (pp. 377–379).** Some two-place connectives are complete alone. They are not standard in TFL, because they are cumbersome (p. 377). So we could have defined a complete truth-functional language with a single primitive connective (p. 378).

*↑ (Sheffer stroke, "nand").* Its table is: TT↦F, TF↦T, FT↦T, FF↦T. It is the negation of ∧'s table (p. 378). The text credits Sheffer, who used it to reduce the connectives of Principia Mathematica. It adds that Peirce anticipated him by about 30 years without publishing, and that Stamm published the result two years earlier (p. 378).

*Claim: ↑ is functionally complete alone (p. 379).* By Result 1, it suffices to rewrite ¬ and ∨ using ↑ only. The equivalences are:
$$\lnot\mathcal{A} \Leftrightarrow (\mathcal{A} \uparrow \mathcal{A}), \qquad (\mathcal{A} \lor \mathcal{B}) \Leftrightarrow ((\mathcal{A}\uparrow\mathcal{A}) \uparrow (\mathcal{B}\uparrow\mathcal{B})).$$

*↓ (Peirce arrow, "nor").* Its table is: TT↦F, TF↦F, FT↦F, FF↦T. It is the negation of ∨'s table (p. 379). Peirce called it "ampheck".

*Claim: ↓ is functionally complete alone (p. 379).* Use Result 2 with:
$$\lnot\mathcal{A} \Leftrightarrow (\mathcal{A} \downarrow \mathcal{A}), \qquad (\mathcal{A} \land \mathcal{B}) \Leftrightarrow ((\mathcal{A}\downarrow\mathcal{A}) \downarrow (\mathcal{B}\downarrow\mathcal{B})).$$

*Intuition note.* ↑ is exactly the negation of ∧, and ↓ is the negation of ∨. Feeding either one the same sentence twice gives negation. The ∨ (for ↑) or the ∧ (for ↓) is then rewritten in the same way, so Result 1 or Result 2 applies.

**46.2 Failures of functional completeness (pp. 379–380).** The text states that the only two-place connectives complete alone are ↑ and ↓ (p. 379). To show some connectives are not jointly complete, find a truth table they cannot express. This takes "a bit of an art" (p. 379).

*Example: ∨ alone (p. 380).* The text says it should be clear, after a little reflection, that no scheme containing only ∨ can have the table of ¬ (A: T↦F, F↦T). The desired top line is False, but the top line of any ∨-only scheme is always True. The same holds for ∧, →, ↔. So each of ∨, ∧, →, ↔ is not complete by itself.

*Harder cases (p. 380).* The "only ↑ and ↓" claim is harder to prove. "Exclusive or" has no T in its first line, so the top-line method no longer suffices to show that it cannot express all truth tables. It is also harder to show that ↔ and ¬ together are not complete. No proofs are given.

*Intuition note.* (Our gloss.) One way to show non-completeness is to find a property that every sentence built from the connectives has, such as "True on the top line". The text says this method no longer suffices for exclusive or, and that showing ↔ with ¬ is not complete is harder.

## Toy example (ours)
Exclusive or, "exactly one of A, B": T on the lines TF and FT, F elsewhere.
1. DNF: $(A \land \lnot B) \lor (\lnot A \land B)$.
2. Check: TT: F∨F=F; TF: T∨F=T; FT: F∨T=T; FF: F∨F=F. This matches the table.

Now check $(A\lor B) \Leftrightarrow ((A\uparrow A)\uparrow(B\uparrow B))$:
- TT: A↑A=F and B↑B=F, so F↑F=T. A∨B=T. ✓
- TF: A↑A=F, B↑B=T, F↑T=T. A∨B=T. ✓
- FT: T, F, T↑F=T. A∨B=T. ✓
- FF: T, T, T↑T=F. A∨B=F. ✓

## Concepts
- [[functional-completeness]] (new) — connectives are jointly functionally complete iff every possible truth table is matched by a sentence using only them (p. 376)
- [[n-place-connective]] (new) — a connective combining n sentences. ¬ takes one, the others two, and ♥ takes three (p. 375)
- [[dnf-method]] (new) — the chapter-45 truth-table method that writes a scheme in ¬, ∧, ∨ for any table (p. 376)
- [[sheffer-stroke]] (new) — ↑, "nand", whose table is the negation of ∧'s (p. 378)
- [[peirce-arrow]] (new) — ↓, "nor", whose table is the negation of ∨'s (p. 379)
- [[logical-equivalence]] (new) — two schemes that the text calls logically equivalent; no definition is given on these pages. Written ⇔, a metalinguistic symbol (p. 377)

## Canonical instances
- [[three-place-connective-heart]] — a stipulated table showing that new truth tables are expressible in old terms (p. 375)
- [[neither-nor]] — an existing example of a connective definable from others (p. 376)
- [[negation-from-disjunction-fails]] — ∨-only schemes are True on the top line, so cannot express ¬ (p. 380)

## Bridges (candidates)
- [structural-analogy] functional completeness of ↑ or ↓ ↔ digital logic: a single gate type (NAND or NOR) can build any Boolean function — the text itself does not mention circuits.
- [structural-analogy] a failure proof by an invariant ("top line is T") ↔ other impossibility proofs: show that every construction preserves a property that the target lacks.

## Questions this raises
- Why can't any connective that is F on the top line and T on the bottom be built from ∧, ∨ alone? What invariants work for other connective sets?
- How would one prove that ↔ and ¬ together are not complete (p. 380)?
- Why are ↑ and ↓ the only complete two-place connectives, and how many two-place connectives are there?

## Reading notes
- Printed page = pdf − 10.
- The source prints "to the Subsidiary Result 1.." and "Result 2.." (double period). This looks like a typographical slip; the double period is visible in the page image on p. 379.
- The source does not verify the ↑/↓ equivalences by table. The check in the toy example is ours.
- The claim that only ↑ and ↓ are complete alone is stated without proof (p. 380). The footnote refers to section 12.6, which is not in this unit.
