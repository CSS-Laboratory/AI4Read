---
id: magnus-2025-forallx/ch43-natural
work: magnus-2025-forallx
unit: "43 Natural deduction for ML"
pages: 341-354
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
# Natural deduction for ML

## L0 — One line
Modal logic can be given proof rules in stages: system K handles □ with strict subproofs, and T, S4 and S5 each add one rule that makes □ behave more like necessity.

## L1 — The gist (≤ 120 words)
How can we prove things in modal logic (ML), the logic of "necessarily" (□) and "possibly" (◇)? The chapter starts from the rules of truth-functional logic (TFL) and adds strict subproofs, which let us reason about arbitrary alternate possibilities. Two rules, □I and □E, give system K. Possibility is defined as ¬□¬. Adding one rule at a time gives T (from □A infer A), S4 (import □A into strict subproofs) and S5 (import ¬□A into strict subproofs). Each addition is motivated by an intuition about necessity or possibility. S5 is strictly stronger than S4, and in S5 a string of boxes and diamonds collapses to its last symbol.

**Prerequisites:** natural deduction for truth-functional logic (TFL: subproofs, →I, ¬E, IP, ⊥); reading □ as "necessarily" and ◇ as "possibly".

## L2 — Key ideas (5–10 bullets)
- ⊢ with a subscript names the proof system: A₁,…,Aₙ ⊢K C (p. 341).
- K = all TFL rules plus strict subproofs and the rules □I and □E (p. 341).
- A strict subproof starts with □ instead of a formula. Inside it you may not cite outside lines unless a modal rule explicitly allows it. This stops bad proofs such as A ∴ □A (pp. 342–343).
- ◇ is defined as ¬□¬. The Def◇ and Modal Conversion rules add no power to K (pp. 346–347).
- T adds RT (□A ⊢ A), which K cannot prove. This gives □A → A (pp. 347–348).
- S4 adds R4 (import □A into a strict subproof). This gives □A → □□A and ◇◇A → ◇A (pp. 349–350).
- S5 adds R5 (import ¬□A). It is strictly stronger than S4, and strings of modal symbols collapse to the last one (pp. 351–353).

## L3 — Walkthrough

### Chapter opening (p. 341)
⊢ expresses provability. A subscript names the system, e.g. $A_1,\dots,A_n \vdash_{\mathbf K} C$ (p. 341).

### 43.1 System K (pp. 341–345)
- K contains all TFL rules, basic and derived, plus strict subproofs and two new basic rules for □ (p. 341).
- A **strict subproof** is a subproof whose assumption line holds □ instead of a formula. It lets us reason about alternate possibilities. What is proved inside holds in any alternate possibility, including ones where our current assumptions may not hold (p. 342).
- Inside it, assumptions are disregarded and lines outside may not be cited, except as the modal rules allow (p. 342).
- **□I:** if A is derived inside a strict subproof (lines m–n), conclude □A (pp. 342–343). The idea: if A is a theorem (provable with no undischarged assumptions), □A should be a theorem too (p. 342).
- Example (p. 342): 1 □ (AS); 2 A (AS); 3 A (R, 2); 4 A→A (→I, 2–3); 5 □(A→A) (□I, 1–4).
- The restriction is essential. The "proof" 1 A (PR); 2 □ (AS); 3 A (incorrect R, 1); 4 □A (□I, 2–3) would vindicate A ∴ □A. It is illegitimate because line 3 cites line 1, outside the strict subproof (p. 343).
- **□E:** from □A at line m, assert A at line n inside a strict subproof (assumption □). Condition: line m is outside that strict subproof, and that strict subproof is not part of another strict subproof that does not contain m (p. 344). So □E works only one strict level in. A nested case (□A at line 1; strict subproofs at lines 2 and 3; A at line 4) is an incorrect use (p. 344).
- Reason: assuming □A is assuming A holds in all alternate possibilities (p. 343).
- Examples (p. 345): □A, □B ⊢K □(A∧B), using a strict subproof with □E twice and ∧I.
- **Distribution Rule** (p. 345): from □(A→B): assume □A; open a strict subproof; get A (□E, line 2) and A→B (□E, line 1); get B (→E); close with □B (□I); then discharge to get □A → □B (→I). □ "distributes" over →.

*Intuition note:* A strict subproof is a place to reason about arbitrary alternate possibilities. Lines from outside may enter only through a modal rule (in K, □E, which needs a □ line outside), and what leaves is A with a box on it, via □I.

### 43.2 Possibility (pp. 346–347)
- Definition: $\Diamond A =_{df} \neg\Box\neg A$. "Possibly A" means "A is not necessarily false" (p. 346).
- The rules Def◇ (both directions, ¬□¬A ↔ ◇A) are added for convenience. They record the definition and add nothing real to K (p. 346).
- Modal Conversion (MC) rules: ¬□A ⇄ ◇¬A and ¬◇A ⇄ □¬A (p. 347). They can be derived from K's basic rules plus the definition of ◇ (p. 347).
- In K one can prove ◇A ↔ ¬□¬A. We could instead take ◇ as primitive and define $\Box A =_{df} \neg\Diamond\neg A$. So necessity is no more fundamental than possibility (p. 347).

### 43.3 System T (pp. 347–348)
- K is too weak to prove A from □A, but if □ means necessity we want this inference (pp. 347–348).
- **RT:** from □A at line m, infer A at line n. Line n must not lie in a strict subproof that begins after line m (p. 348).
- T proves things K cannot, e.g. □A → A (p. 348).

*Intuition note:* If A is necessarily true, it must be true (p. 348). RT may only be used at the same strict level as the box, not inside a strict subproof opened after it.

### 43.4 System S4 (pp. 348–350)
- If □A came from □I applied to a strict subproof of A that does not use □E, A is a tautology. Nesting that subproof in another strict subproof and applying □I again gives □□A. Example: □□(P→P) (pp. 348–349).
- If □E was used inside the strict subproof of A, then putting that subproof inside another strict subproof breaks □E's condition. If □A is just a premise, T cannot give □□A (p. 349).
- Intuition motivating a fix: it seems intuitive that if A is necessarily true, it couldn't have failed to be necessarily true, at least if □ is read as necessity (p. 349).
- **S4 = T + R4.** R4: from □A at line m, write □A inside a strict subproof at line n. It has the same restriction as □E (□A outside, no extra strict nesting). One more application of R4 would import it into a deeper subproof (p. 350).
- Proof of □A → □□A (p. 350): assume □A; open a strict subproof; □A (R4, 1); □□A (□I); →I.
- Likewise ◇◇A → ◇A is provable. So S4 can add boxes and delete a diamond from ◇◇A (p. 350).

### 43.5 System S5 (pp. 351–353)
- S4 does not generally give ◇A ⊢ □◇A. Intuition: if □ and ◇ are read as necessity and possibility, it seems intuitive that if A is possibly true, it couldn't have failed to be possibly true (p. 351).
- **S5 = S4 + R5.** R5: from ¬□A at line m, write ¬□A inside a strict subproof at line n. Restriction as for R4 (p. 351).
- Proof that ◇□A ⊢S5 □A (p. 352): 1 ◇□A (PR); 2 ¬□¬□A (Def◇, 1); 3 ¬□A (AS); 4 □ (AS, strict); 5 ¬□A (R5, 3); 6 □¬□A (□I, 4–5); 7 ⊥ (¬E, 2, 6); 8 □A (IP, 3–7).
- So S5 can delete diamonds in front of boxes (p. 352).
- Adding R5 to T and leaving out R4 gives an equivalent system, because RT with R5 reproduces R4's results. The text demonstrates only □A ⊢S5 □□A, via a proof using RT, R5 and IP (pp. 352–353).
- S5 is strictly stronger than S4: ◇□A → □A is provable in S5 but not in S4 (p. 353).
- In S5, in any string of boxes and diamonds all but the last can be deleted. For example, ◇□◇◇□□◇□A reduces to □A (p. 353).

*Intuition note:* Each system adds one way to move a modal symbol around. S5 adds so much that stacked modalities no longer matter.

## Toy example (ours)
Goal: show □P ⊢K □(P∨Q).
1. □P (PR)
2. □ (AS, opens strict subproof)
3. P (□E, 1) — line 1 is outside, and there is one strict level.
4. P∨Q (∨I, 3)
5. □(P∨Q) (□I, 2–4)

Variation: □P ⊢T P∨Q. 1 □P (PR); 2 P (RT, 1); 3 P∨Q (∨I, 2). K has no rule giving line 2, so the T-proof is not a K-proof. This shows how T adds strength.

## Concepts
- [[provability-turnstile]] (new) — ⊢ with a system subscript says a conclusion is provable from premises in that system (p. 341)
- [[system-K]] (new) — TFL rules plus strict subproofs, □I and □E (p. 341)
- [[strict-subproof]] (new) — subproof opened with □; no citing outside lines unless a modal rule allows it (p. 342)
- [[box-introduction-elimination]] (new) — □I: from A in a strict subproof infer □A; □E: import A from □A (pp. 342–344)
- [[diamond-definition]] (new) — ◇A defined as ¬□¬A; □ could instead be defined from ◇ (pp. 346–347)
- [[modal-conversion]] (new) — rules flipping □ and ◇ past ¬; derivable in K (p. 347)
- [[system-T]] (new) — K + RT (from □A infer A) (p. 348)
- [[system-S4]] (new) — T + R4 (import □A into a strict subproof) (p. 350)
- [[system-S5]] (new) — S4 + R5 (import ¬□A into a strict subproof) (p. 351)

## Canonical instances
- [[bad-proof-A-to-boxA]] — citing an outside line inside a strict subproof would "prove" A ∴ □A (p. 343)
- [[distribution-rule-K]] — □(A→B) ⊢ □A → □B (p. 345)
- [[box-implies-boxbox-S4]] — □A → □□A in S4 (p. 350)
- [[diamond-box-collapse-S5]] — ◇□A ⊢S5 □A (p. 352)

## Bridges (candidates)
- [structural-analogy] strict subproof with restricted citations ↔ first-order logic: universal-introduction rules that restrict which earlier lines may be used — both guard a "for any case" conclusion.
- [metaphor] "alternate possibilities" in strict subproofs ↔ possible-world semantics: the chapter gives only proof rules, so any link to worlds is an interpretation.

## Questions this raises
- Why is the restriction on RT different from that on □E, R4 and R5?
- Does each system prove only what is true in alternate possibilities? (This chapter gives no semantics.)
- Is S5 the right system for necessity, or only for some readings of □?
- Can any system between K and T be useful?

## Exercises worth doing
- Ex. A.1 (p. 353) — □(A∧B) ⊢K □A ∧ □B: practice □E and □I — easy
- Ex. A.4 (p. 354) — □(A↔B) ⊢K □A ↔ □B: mixes regular and strict subproofs — medium
- Ex. B.1–B.4 (p. 354) — derive the Modal Conversion rules without using them — medium
- Ex. D.1 (p. 354) — P ⊢T ◇P: uses RT and the definition of ◇ — medium
- Ex. E.3 (p. 354) — ◇◇A ⊢S4 ◇A: uses R4 — hard
- Ex. F.2 (p. 354) — A ⊢S5 □◇A: uses R5 — hard

## Reading notes
- Printed page = pdf page − 10.
- Misprints visible in the images: p. 345, the line 7 citation reads "□I, 3–7", but the strict subproof is lines 3–6. On p. 350, line 5 reads "→I, 1–6", but the assumption subproof is lines 1–4. On p. 342, "allow as to reason" should read "allow us".
- On p. 348 the text says the RT restriction is "the opposite" of □E's and that □E can only be used "in a nested strict subproof". This conflicts with p. 344, where □E cannot be used inside a nested strict subproof. I have followed the formal conditions on pp. 344 and 348.
- The statement that T proves □A → A is asserted without a proof (p. 348), as is ◇◇A → ◇A in S4 (p. 350).
