---
id: magnus-2025-forallx/ch17-basic
work: magnus-2025-forallx
unit: "16 The very idea of natural deduction; 17 Basic rules for TFL"
pages: 110–141
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
# Basic rules for TFL (with ch. 16, The very idea of natural deduction)

## L0 — One line
Instead of checking every truth-table line, we can show an argument is valid by chaining a few simple introduction and elimination rules, tracking extra assumptions in subproofs.

## L1 — The gist (≤ 120 words)
Truth tables test validity by brute force. They may show little about why an argument is valid, and they can become impractical as sentence letters multiply (twenty letters need 1,048,576 lines). The authors therefore build a natural deduction system. Each connective gets an introduction rule and an elimination rule. Further rules cover reiteration (repeating a line), contradiction (⊥), indirect proof and explosion (anything follows from ⊥). A proof is a list of numbered lines. Extra assumptions are opened in subproofs and later discharged. Strict citation rules stop lines from closed subproofs being reused, which would let us "prove" any sentence letter from any other. The unit then says these are all the basic rules and gives practice exercises.

**Prerequisites:** TFL connectives (∧, ∨, →, ↔, ¬) and main logical operator; validity and entailment via valuations; truth tables; the idea of a metalanguage.

## L2 — Key ideas (5–10 bullets)
- Truth tables decide validity but may give little insight into why an argument is valid, and can become intractable (1,024 lines, then 1,048,576); for FOL there is no truth-table-like test at all, so natural deduction is the chosen route (pp. 110–112).
- A formal proof is a numbered sequence of sentences, with premises (PR) above a line and later lines justified by rules or marked as new assumptions (AS) (pp. 113–114).
- Each connective has an introduction rule (to prove a sentence with that main operator) and an elimination rule (to use one) (p. 113); rules are stated schematically with metavariables (pp. 115–117).
- →I, ↔I, ∨E, ¬I and IP use subproofs: assume something, derive something, then close (discharge) the assumption (pp. 122–123, 130–137).
- Citation restrictions stop lines depending on discharged assumptions from being used; without them any sentence letter could be proved from any other (pp. 125–129).
- Negation is handled via ⊥: ¬E turns a sentence and its negation into ⊥, ¬I and IP turn a subproof ending in ⊥ into ¬A or A, and explosion (X) gives any sentence from ⊥ (pp. 135–138).
- Explosion matches the entailment definition: ⊥ ⊨ B for any B, since no valuation makes ⊥ true; intuitionists and relevance logicians dissent from IP or explosion (pp. 137–139).

## L3 — Walkthrough

### Chapter 16: The very idea of natural deduction
- Chapter 2's definition: an argument is valid iff there is no case where all premises are true and the conclusion false. For TFL each truth-table line is a valuation, so a table checks this directly (p. 110).
- $P \lor Q, \neg P \therefore Q$ and $P \to Q, P \therefore Q$ are both valid, but we might say they use different forms of reasoning. A table does not record this (p. 110).
- A natural deduction system aims to show arguments valid so that we can understand the reasoning. We start with basic rules, which combine into more complicated arguments. The authors "hope" a small starter pack captures all valid arguments (p. 111).
- Truth tables consider ways of making sentences true or false. Natural deduction manipulates sentences by rules set down as good rules. This promises a better, or at least a different, insight (p. 111).
- Necessity. For $A_1 \to C_1 \therefore (A_1 \land (A_2 \land \dots \land A_5)) \to (((C_1 \lor C_2) \lor \dots) \lor C_5)$ a table has 1,024 lines. Replace 5 with 10 and it needs $2^{20} = 1{,}048{,}576$ lines. Both arguments are valid. A machine could do it in principle, but complicated TFL arguments become intractable in practice (pp. 111–112).
- FOL (from chapter 23) is worse: there is nothing like a truth-table test. Validity requires reasoning about all interpretations, and there are infinitely many, so a machine would never finish (p. 112).
- Systems for reasoning about all interpretations were developed in the 1950s by Beth and Hintikka; the book does not follow them. Modern natural deduction dates from independent 1934 papers by Gentzen and Jaśkowski. The system used is based largely on Fitch's work (first published 1952) (p. 112).

*Intuition note:* A truth table checks every possible case, like testing a bridge by driving every vehicle over it. A proof explains the argument from a few trusted steps, and can be much shorter than the table (a 4-line proof against a 256-line table, p. 119).

### 17.1 The idea of a formal proof
- A formal proof (derivation) is a sequence of sentences, some marked as initial assumptions (premises). The last line is the conclusion (p. 113).
- Natural deduction has, for each connective, introduction rules (prove a sentence with that connective as main logical operator) and elimination rules (prove something from such a sentence) (p. 113).
- Every line is numbered so it can be cited. A line under the premises separates assumptions (above) from what follows from them or from new assumptions (below). Any line number for the conclusion is fine, but short proofs are preferred (p. 114).
- Example setups: $\neg(A \lor B) \therefore \neg A \land \neg B$ (premise labelled PR); and $A \lor B, \neg(A \land C), \neg(B \land \neg D) \therefore \neg C \lor D$ with three premises (pp. 113–114).

### 17.2 Reiteration
- Rule R: if $\mathscr A$ is on line $m$, we may write $\mathscr A$ on a later line, citing "R, m" (p. 115).
- $\mathscr A$ is a metalanguage symbol for any TFL sentence, not a TFL sentence. $m$ is a metalanguage symbol for any line number; real proofs use 1, 2, 3, … (pp. 115–116).

### 17.3 Conjunction
- **∧I:** from $\mathscr A$ (line $m$) and $\mathscr B$ (line $n$) infer $\mathscr A \land \mathscr B$, cited "∧I, m, n". The two lines may be apart and in either order. Example: from R on line 8 and L on line 15, infer $R \land L$ (∧I, 8, 15) or $L \land R$ (∧I, 15, 8) (pp. 116–117).
- **∧E:** from $\mathscr A \land \mathscr B$ (line $m$) infer $\mathscr A$, or infer $\mathscr B$, cited "∧E, m" (pp. 117–118).
- ∧E applies only when ∧ is the main logical operator: we cannot infer D from $C \lor (D \land E)$ (p. 118).
- Example (4 lines): $[(A\lor B)\to(C\lor D)] \land [(E\lor F)\to(G\lor H)] \therefore [(E\lor F)\to(G\lor H)] \land [(A\lor B)\to(C\lor D)]$. Line 1 PR; lines 2, 3 are the conjuncts by ∧E, 1; line 4 is ∧I, 3, 2. A truth table would need 256 lines (pp. 118–119).
- Example (7 lines): $A \land (B \land C) \therefore (A \land B) \land C$ (pp. 119–120):

```
1 A ∧ (B ∧ C)   PR
2 A             ∧E, 1
3 B ∧ C         ∧E, 1
4 B             ∧E, 3
5 C             ∧E, 3
6 A ∧ B         ∧I, 2, 4
7 (A ∧ B) ∧ C  ∧I, 6, 5
```
- The official syntax allows only two conjuncts, so inner brackets are not dropped; outermost brackets may be (p. 120).
- ∧I may be applied to the same line twice: $A \therefore A \land A$ by "∧I, 1, 1" (p. 120).

*Intuition note:* ∧I glues two shown facts together. ∧E takes a conjunction apart, but only at its outermost ∧, never from inside another connective.

### 17.4 Conditional
- **→E (modus ponens):** from $\mathscr A \to \mathscr B$ (line $m$) and $\mathscr A$ (line $n$) infer $\mathscr B$, "→E, m, n". The lines may be apart and in either order; convention is to cite the conditional first (p. 121).
- Motivation for →I: from "Ludwig is reactionary" we should be able to reach "if Ludwig is libertarian, then he is both reactionary and libertarian". We additionally assume L, use ∧I, and note the result holds conditional on that assumption (p. 121).
- The additional assumption is written on a new indented line, marked AS, with no justification. A line under it marks it as an assumption, and the extra vertical line marks it as additional (p. 122):

```
1 R              PR
2   L            AS
3   R ∧ L        ∧I, 1, 2
4 L → (R ∧ L)    →I, 2–3
```
- Back to one vertical line, we have discharged the assumption L, since the conditional follows from R alone (p. 123).
- **→I:** assume $\mathscr A$ (line $i$, AS); derive $\mathscr B$ (line $j$); conclude $\mathscr A \to \mathscr B$, "→I, i–j". Any number of lines may lie between $i$ and $j$ (p. 123).
- Example $P \to Q, Q \to R \therefore P \to R$ (p. 124):

```
1 P → Q    PR
2 Q → R    PR
3   P      AS
4   Q      →E, 1, 3
5   R      →E, 2, 4
6 P → R    →I, 3–5
```

*Intuition note:* To prove "if A then B", pretend A is true for a moment, derive B, then step back out. The conclusion no longer relies on the pretence.

### 17.5 Additional assumptions and subproofs
- Valid: $A$ (PR); $B$ (AS); $B$ (R, 2); $B \to B$ (→I, 2–3). This is fine, since $B \to B$ is a tautology and needs no particular premises (p. 124).
- Naughty continuation: line 5, $B$, by →E, 4, 3. This would prove any sentence letter from any other (Anne is fast, so Boudica stood twenty feet tall) (p. 125).
- A subproof is a subsidiary proof within the main proof. It asks what we could show if we also made the additional assumption. Inside it we may use its assumption and anything obtained from earlier assumptions still in effect. When its vertical line ends, the subproof is closed and its assumptions are discharged (p. 125).
- **Individual-line citation rule:** the cited line must come before the line where the rule is applied, and must not lie within a subproof closed before that line. This blocks line 5 above, because line 3 is in the closed subproof 2–3 (p. 126). You cannot refer to anything obtained using a discharged assumption (p. 126).
- Nested subproofs are allowed. Example (p. 127):

```
1 A                      PR
2   B                    AS
3     C                  AS
4     A ∧ B              ∧I, 1, 2
5   C → (A ∧ B)          →I, 3–4
6 B → (C → (A ∧ B))      →I, 2–5
```
  Line 4 cites lines 1 and 2, which is fine since neither assumption is yet discharged (p. 127).
- Naughty line 7, $C \to (A \land B)$ by →I, 3–4, is illegal. The subproof 3–4 depended on assumption B, but B was discharged by line 6. A subproof may be cited only if it does not lie within another subproof already closed at that line (pp. 127–128).
- Another exclusion: citing →I, 2–5 for $B \to C$, where line 5 lies inside the still-open subproof starting at line 3. →I needs the last line to rely only on the cited subproof's assumption (and earlier ones), so it must not lie within a nested subproof (p. 128).
- **Subproof citation rule (three conditions):** (1) the subproof lies entirely before the rule application; (2) it does not lie within another subproof that is closed at that line; (3) its last line is not inside a nested subproof (p. 129).
- A rule that needs an individual line cannot be given a subproof, and vice versa. Example: "R, 3–5" is incorrect even though the subproof contains C. Citing lines 3 or 5 directly is also inadmissible, as they lie in a closed subproof (pp. 129–130).
- Opening a subproof with any assumption, or closing one at any point, is always permitted. But a "wacky" assumption would just waste lines, and closing a subproof is not helpful until something useful has been reached. To get a conditional by →I you must assume its antecedent. A subproof cited for →I must end with the consequent $\mathscr B$ of the conditional proved, and begin with its antecedent $\mathscr A$ (p. 130).

*Intuition note:* A subproof is a "what if" box. What is inside is true only under the what-if; once you leave the box, you may use only the box as a whole, never its inner lines.

### 17.6 Biconditional
- **↔I:** two subproofs. Assume $\mathscr A$ (AS, line $i$), derive $\mathscr B$ (line $j$); assume $\mathscr B$ (AS, line $k$), derive $\mathscr A$ (line $l$); conclude $\mathscr A \leftrightarrow \mathscr B$, "↔I, i–j, k–l". The subproofs may come in either order and need not be adjacent (pp. 130–131).
- **↔E:** from $\mathscr A \leftrightarrow \mathscr B$ (line $m$) and $\mathscr A$ (line $n$) infer $\mathscr B$; or from $\mathscr B$ infer $\mathscr A$, "↔E, m, n". The lines may be apart and in any order; good practice is to cite the biconditional first (pp. 131–132).

### 17.7 Disjunction
- **∨I:** from $\mathscr A$ (line $m$) infer $\mathscr A \lor \mathscr B$, or $\mathscr B \lor \mathscr A$, "∨I, m". This is sound because a disjunction is weaker than a disjunct. $\mathscr B$ can be any sentence, e.g. kumquats; odd inferences may break conversational norms but nothing is logically wrong (p. 132).
- Example: $M$ (PR) gives $M \lor ([(A\leftrightarrow B)\to(C\land D)] \leftrightarrow [E\land F])$ by ∨I, 1. A table would need 128 lines (pp. 132–133).
- From $\mathscr A \lor \mathscr B$ alone we cannot conclude either disjunct (p. 133).
- **∨E:** from $\mathscr A \lor \mathscr B$ (line $m$), a subproof assuming $\mathscr A$ and ending in $\mathscr C$ (lines $i$–$j$), and a subproof assuming $\mathscr B$ and ending in the same $\mathscr C$ (lines $k$–$l$), infer $\mathscr C$, "∨E, m, i–j, k–l". Lines and subproofs may come in any order and need not be adjacent (p. 133).
- Example $(P\land Q)\lor(P\land R) \therefore P$ (p. 134):

```
1 (P ∧ Q) ∨ (P ∧ R)   PR
2   P ∧ Q             AS
3   P                 ∧E, 2
4   P ∧ R             AS
5   P                 ∧E, 4
6 P                   ∨E, 1, 2–3, 4–5
```
- Example $A \land (B\lor C) \therefore (A\land B)\lor(A\land C)$ (p. 134):

```
1  A ∧ (B ∨ C)           PR
2  A                     ∧E, 1
3  B ∨ C                 ∧E, 1
4    B                   AS
5    A ∧ B               ∧I, 2, 4
6    (A ∧ B) ∨ (A ∧ C)   ∨I, 5
7    C                   AS
8    A ∧ C               ∧I, 2, 7
9    (A ∧ B) ∨ (A ∧ C)   ∨I, 8
10 (A ∧ B) ∨ (A ∧ C)     ∨E, 3, 4–6, 7–9
```
- Finding such proofs comes with practice (strategies in chapter 18). The key question now is whether you can check that each line follows the rules (p. 135).

*Intuition note:* With "A or B" we do not know which holds. If both options lead to the same C, then C holds either way, so we can assert it.

### 17.8 Contradiction and negation
- New symbol ⊥, read as "contradiction!", "reductio!" or "but that's absurd!" (p. 135).
- **¬E:** from $\neg\mathscr A$ (line $m$) and $\mathscr A$ (line $n$) infer ⊥, "¬E, m, n". Order and adjacency do not matter; convention cites the negation first. It is called an elimination rule since it is the most basic rule going from a premise containing ¬ to a sentence without it (pp. 135–136).
- Three ways to treat ⊥ (p. 136): (1) a new atomic sentence that is always false; (2) an abbreviation for a canonical contradiction such as $A \land \neg A$; (3) not a TFL symbol but a punctuation mark in proofs (like line numbers). The authors say the third is philosophically attractive but officially adopt the first, so ⊥ can be manipulated like any sentence (p. 136).
- **¬I:** assume $\mathscr A$ (line $i$, AS), derive ⊥ (line $j$), conclude $\neg\mathscr A$, "¬I, i–j". If an assumption leads to a contradiction, the assumption must be wrong (p. 136). Example (p. 137):

```
1 D        AS
2   ¬D     AS
3   ⊥      ¬E, 2, 1
4 ¬¬D      ¬I, 2–3
```
- **IP (indirect proof):** assume $\neg\mathscr A$ (line $i$, AS), derive ⊥ (line $j$), conclude $\mathscr A$, "IP, i–j". It is like ¬I with $\mathscr A$ and $\neg\mathscr A$ swapped. It introduces no connective, and eliminates none, because it has no free-standing premise containing ¬ (p. 137).
- Going the other way, from $\neg\neg D$ (PR) to $D$: line 2 $\neg D$ (AS); line 3 ⊥ by ¬E, 1, 2; line 4 $D$ by IP, 2–3 (p. 138).
- *Footnote 1 (p. 137):* intuitionists have qualms about IP but not ¬E. They do not accept that every sentence is true or false. For them a proof of ⊥ from $\mathscr A$ guarantees $\neg\mathscr A$, but a proof of ⊥ from $\neg\mathscr A$ guarantees only $\neg\neg\mathscr A$, so $\mathscr A$ and $\neg\neg\mathscr A$ are not equivalent.
- **X (explosion, ex contradictione quodlibet):** from ⊥ (line $m$) infer any sentence $\mathscr A$, "X, m". It is motivated by "…and if that's true, I'll eat my hat". Use it only when you already have ⊥, which arises only when your assumptions are contradictory (p. 138).
- Justification via entailment: $\mathscr A$ entails $\mathscr B$ iff no valuation makes $\mathscr A$ true and $\mathscr B$ false. No valuation makes ⊥ true, so none makes ⊥ true and $\mathscr B$ false, hence ⊥ ⊨ $\mathscr B$ for any $\mathscr B$ (pp. 138–139).
- *Footnote 3 (p. 139):* some logicians reject this. They hold that entailment needs a relevant connection between premise and conclusion, and develop "relevant" logics without explosion.
- These are all the basic rules for the TFL proof system (p. 139).

*Intuition note:* If your assumptions clash, you have reached an impossible situation, and from it any conclusion follows trivially. That is why ⊥ must be earned from the assumptions before X may be used. ¬I and IP use the clash to reject the assumption.

### Practice exercises (pp. 139–141)
A: two incorrect "proofs" to diagnose. B: three proofs missing citations, to be completed with the corresponding arguments written down. C: twelve arguments to prove (e.g. $J \to \neg J \therefore \neg J$; $\neg(P\to Q) \therefore P$).

## Toy example (ours, not from the text)
Argument: $P \to Q \therefore (P \land R) \to Q$. Three sentence letters, so a table needs $2^3 = 8$ lines. A proof needs 5:

```
1 P → Q          PR
2   P ∧ R        AS
3   P            ∧E, 2
4   Q            →E, 1, 3
5 (P ∧ R) → Q    →I, 2–4
```
- Line 3: ∧E applies since ∧ is the main operator of line 2.
- Line 4: →E cites the conditional (line 1) first, then its antecedent (line 3).
- Line 5: →I cites subproof 2–4. Its assumption is the antecedent and its last line is the consequent.
- Illegal use: after line 5, writing Q "by →E" citing line 3 would break the rule, because line 3 sits in subproof 2–4, which is closed.

## Concepts
- [[natural-deduction]] (new) — proving validity by applying fixed rules to numbered lines, not by checking valuations (p. 111)
- [[truth-table-intractability]] (new) — the example tables have 1,024 and $2^{20} = 1{,}048{,}576$ lines; there is nothing like the truth-table test for FOL (pp. 111–112)
- [[validity / soundness]] — valid iff no case has all premises true and conclusion false; used to motivate the system and ⊥ ⊨ B (pp. 110, 139)
- [[introduction-elimination-rules]] (new) — rules that prove a sentence with a given main operator, and rules that use one (p. 113)
- [[formal-proof]] (new) — numbered sequence of sentences, premises (PR) first, last line the conclusion (p. 113)
- [[metavariable]] (new) — symbols like $\mathscr A$ and $m$ that talk about any sentence or line number (p. 115)
- [[subproof-discharge]] (new) — an extra assumption opened in an indented subproof; closing it discharges it, and its lines then cannot be cited individually (pp. 125–126)
- [[contradiction-symbol]] (new) — ⊥, treated officially as an always-false sentence letter (p. 136)
- [[indirect-proof]] (new) — assume ¬A, derive ⊥, conclude A (IP) (p. 137)
- [[explosion]] (new) — from ⊥ infer any sentence (rule X) (p. 138)

## Canonical instances
- [[truth-table-1024-and-2-to-the-20]] (new) — two valid arguments whose tables have 1,024 and 1,048,576 lines (pp. 111–112)
- [[ludwig-reactionary-libertarian]] (new) — motivates ∧I, ∧E and →I; ∨E example (Austrian economist) (pp. 116, 121, 133)
- [[naughty-proof-B-from-A]] (new) — citing a closed subproof would prove any letter from any other (pp. 124–126)
- [[distribution-proof]] (new) — $A\land(B\lor C) \therefore (A\land B)\lor(A\land C)$ via ∨E (p. 134)
- [[double-negation-proofs]] (new) — $D \therefore \neg\neg D$ by ¬I and $\neg\neg D \therefore D$ by IP (pp. 137–138)

## Bridges (candidates)
- [structural-analogy] Subproofs and discharge ↔ programming: a nested block's local assumptions cannot be used outside it — scope-like restriction on what may be cited.
- [structural-analogy] Table size $2^n$ ↔ computational complexity: brute-force enumeration blows up while a rule-based proof stays short.
- [structural-analogy] ∨I allowing odd disjunctions ↔ analytic-philosophy: conversational implicature — the text says such inferences may "violate implicit conversational norms" yet are logically fine (p. 132).
- [metaphor] ⊥ as "reductio!" ↔ arguing an opponent into self-contradiction, as the text puts it (p. 135).

## Questions this raises
- Do the basic rules capture every valid TFL argument, as the authors hope (p. 111)?
- How should one choose assumptions to find a proof (chapter 18 promises strategies) (p. 135)?
- If intuitionists or relevance logicians reject IP or explosion, what exactly do they lose or keep?
- How will these rules extend to quantifiers and identity in FOL (p. 112)?

## Exercises worth doing
- Ex. A (p. 139) — spot the citation errors in two faulty proofs; tests the cite-line and cite-subproof rules — difficulty: medium
- Ex. B (p. 140) — add citations to bare proofs and state the argument; builds reading-proofs skill — difficulty: easy
- Ex. C.1 (p. 140) — $J \to \neg J \therefore \neg J$; practice with →E and ¬I — difficulty: medium
- Ex. C.3 (p. 141) — $A\to(B\to C) \therefore (A\land B)\to C$; nested →I and →E — difficulty: medium
- Ex. C.6 (p. 141) — $A\leftrightarrow B, B\leftrightarrow C \therefore A\leftrightarrow C$; ↔I with two subproofs — difficulty: medium
- Ex. C.12 (p. 141) — $\neg(P\to Q)\therefore P$; typically uses IP and X — difficulty: hard

## Reading notes
- Page offset: printed = pdf − 10 (pdf 120 = printed 110). Chapter 16 is printed pp. 110–112; chapter 17 is pp. 113–141, including practice exercises. The unit includes ch. 16 as stated.
- The text layer printed "220" for $2^{20}$ (p. 111); the image shows $2^{20}$.
- Typo in source (p. 128): "one another assumption" (probably "one other").
- Exercise C.9 (p. 141) has the conclusion $Q \lor E$, with E not in the premises. This is as printed. (Added observation: the argument is still provable, since $Q$ follows from the premises and ∨I gives $Q \lor E$.)
- Exercise B's first proof contains the line "R ∨E", which is the sentence $R \lor E$ with its citation missing (p. 140).
- Solutions are not printed in these pages.
