---
id: magnus-2025-forallx/ch44-semantics
work: magnus-2025-forallx
unit: "44 Semantics for ML"
pages: 355–367
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
# Semantics for ML (modal logic)

## L0 — One line
ML sentences are true or false *at possible worlds*, and □ and ◇ quantify over the worlds accessible from the current one, so each modal system (K, T, S4, S5) matches a property of the accessibility relation.

## L1 — The gist (≤ 120 words)
The chapter asks what makes a modal argument valid, and how K, T, S4 and S5 relate to that. An interpretation has a set of worlds, an accessibility relation (which worlds are possible from which) and a valuation. □A is true at a world iff A is true at every accessible world; ◇A is true iff A is true at some accessible world. Validity in K means no counter-interpretation (a world with true premises, false conclusion) exists. K allows any accessibility relation; T adds reflexivity (every world accesses itself), S4 transitivity, S5 symmetry (an equivalence relation); a universal relation gives the same S5 results. The authors state, without proof, that each system is sound and complete for its class.

**Prerequisites:** truth-tables for the TFL connectives; the ML proof rules (□E, □I, strict subproofs, RT, R4, R5); "for all / for some" notation; the idea of a relation.

## L2 — Key ideas (5–10 bullets)
- ML truth is relative to a world: a sentence may be true at one world and false at another (p. 355).
- An interpretation = non-empty set of worlds W + accessibility relation R + valuation ν; the nature of the "worlds" does not matter to the logic (pp. 356, 358).
- The connectives behave as in truth-tables, one world at a time. □A and ◇A are evaluated over worlds accessible from the current one (pp. 357–358).
- Modal validity: no world in any interpretation makes the premises true and the conclusion false. One shows invalidity by a counter-interpretation (pp. 359–360).
- K is stated to be sound and complete for unrestricted accessibility; T, S4 and S5 are unsound for ⊨K, e.g. □A ⊭K A (pp. 360–361).
- Reflexivity vindicates RT; transitivity vindicates R4; an equivalence relation vindicates R5 (pp. 362–365).
- A universal relation gives the same S5 results; the authors report that most philosophers assume their main necessities (logical, metaphysical) are of this kind, so S5 is the system most philosophers use most of the time (p. 366).

## L3 — Walkthrough

### 44.1 Interpretations of ML
- A semantics assigns truth-values to sentences. In ML a sentence is true or false *at a possible world*; □A is true iff A is true at every world, ◇A iff A is true at some world (p. 355). This is the "big idea", which gets refined below.
- Worlds: the authors say that for formal logic, worlds can be anything. The only demand is a non-empty collection (p. 356). The philosophical question "what is a world?" is postponed (p. 356).
- A **valuation function** ν takes a sentence and a world and returns a truth-value. ν_w(A)=T means A is true at w on ν (p. 356). It may give any atomic sentence any value at any world (p. 356). Complex sentences obey (p. 356–357):

$$\nu_w(\neg A)=T \iff \nu_w(A)=F \tag{1}$$
$$\nu_w(A\wedge B)=T \iff \nu_w(A)=T \text{ and } \nu_w(B)=T \tag{2}$$
$$\nu_w(A\vee B)=T \iff \nu_w(A)=T \text{ or } \nu_w(B)=T,\text{ or both} \tag{3}$$
$$\nu_w(A\to B)=T \iff \nu_w(A)=F \text{ or } \nu_w(B)=T,\text{ or both} \tag{4}$$
$$\nu_w(A\leftrightarrow B)=T \iff (\nu_w(A)=T \text{ and } \nu_w(B)=T)\text{ or }(\nu_w(A)=F \text{ and } \nu_w(B)=F) \tag{5}$$

  These work like TFL truth-tables, applied one world at a time (p. 357).
- The "most obvious" modal rules are $\nu_w(\Box A)=T \iff \forall w'(\nu_{w'}(A)=T)$ and $\nu_w(\Diamond A)=T \iff \exists w'(\nu_{w'}(A)=T)$. The authors find them too rigid, since ML is meant as a framework for many kinds of necessity (p. 357).
- An **accessibility relation** R holds between worlds. $Rw_1w_2$ means $w_1$ accesses $w_2$, i.e. $w_2$ is possible *relative to* $w_1$ (p. 357). The rules become:

$$\nu_{w_1}(\Box A)=T \iff \forall w_2\,(Rw_1w_2 \to \nu_{w_2}(A)=T) \tag{6}$$
$$\nu_{w_1}(\Diamond A)=T \iff \exists w_2\,(Rw_1w_2 \wedge \nu_{w_2}(A)=T) \tag{7}$$

- An **interpretation** is three things: W (non-empty), R (any relation on W for now) and ν obeying (1)–(7) (p. 358).
- Diagram example (p. 358): worlds 1 and 2. The arrows give R: a loop at 1 and an arrow from 2 to 1, so 1 and 2 both access 1, and neither accesses 2. The boxes give atoms: A true and B false at 1; A false and B true at 2. Only atoms or negated atoms may be written in boxes. At world 1 these are true: $A\wedge\neg B$, $B\to A$, $\Diamond A$, $\Box\neg B$ (p. 358).
- Same interpretation in list form (p. 359): $W:1,2$; $R:\langle1,1\rangle,\langle2,1\rangle$; $\nu_1(A)=T,\nu_1(B)=F,\nu_2(A)=F,\nu_2(B)=T$.

*Intuition note.* To check □A at a world, look only at the worlds it can "see" along arrows. If all of them make A true, □A is true. The arrows make "possible" depend on where you stand.

### 44.2 A semantics for system K
- Definitions (p. 359), with "modal" dropped later:
  - $A_1,\dots,A_n \therefore C$ is valid iff no world in any interpretation makes all $A_i$ true and $C$ false.
  - A is a modal truth iff true at every world in every interpretation.
  - A is a modal contradiction iff false at every world in every interpretation.
  - A is modally satisfiable iff true at some world in some interpretation.
  - Valid arguments are written $A_1,\dots,A_n\vDash_{\mathbf K} C$.
- **Counter-interpretation** (p. 360): to refute $\neg A\vDash_{\mathbf K}\neg\Diamond A$, take worlds 1 → 2, with ¬A at 1 and A at 2. Then ¬A is true at 1. A is true at 2 and 2 is accessible from 1, so ◇A is true and ¬◇A is false at 1.
- The authors state two results (p. 360). Soundness: if $\vdash_{\mathbf K}$ then $\vDash_{\mathbf K}$. Completeness: if $\vDash_{\mathbf K}$ then $\vdash_{\mathbf K}$. Soundness means K's proofs only vindicate valid arguments. Completeness means K's rules are broad enough to prove every valid argument. They do not prove these results (p. 360).
- Idea behind soundness of □I (p. 361): in K, a strict subproof can import information only by □E from outside □A. If □A is true at a world, A is true at all accessible worlds. So everything proved in a strict subproof is true in all accessible worlds. That is why □I is sound (p. 361).

*Intuition note.* A strict subproof is reasoning about "an arbitrary accessible world". The only facts it can use are those guaranteed at every accessible world, namely the formulas A for which □A holds outside.

### 44.3 A semantics for system T
- T, S4 and S5 are unsound relative to $\vDash_{\mathbf K}$; for example they allow inferring A from □A, though $\Box A\nvDash_{\mathbf K}A$ (p. 361). So one changes the definition of validity by restricting R (p. 361).
- **Reflexive**: $\forall w\,Rww$ (every world accesses itself) (p. 361).
- $A_1,\dots,A_n\vDash_{\mathbf T}C$ iff no world in any interpretation *with reflexive R* makes all $A_i$ true and $C$ false (p. 362). The authors state T is sound and complete for this (p. 362).
- Why RT is vindicated (p. 362): suppose □A is true at w and A false at w. □A true means A holds at every world w accesses. R is reflexive, so w accesses w, so A is true at w. A is then both true and false at w, a contradiction. So $\Box A\vDash_{\mathbf T}A$.

*Intuition note.* If a world counts as possible relative to itself, then whenever "A is necessary" is true at that world, A itself cannot be false there.

### 44.4 A semantics for S4
- **Transitive**: $\forall w_1\forall w_2\forall w_3((Rw_1w_2\wedge Rw_2w_3)\to Rw_1w_3)$ (p. 363).
- $\vDash_{\mathbf{S4}}$ quantifies over interpretations whose R is reflexive and transitive. S4 is stated to be sound and complete for it (p. 363).
- R4 rule means: whenever □A is true, □A is true in every accessible world. So $\Box A\vDash_{\mathbf{S4}}\Box\Box A$ (p. 364).
- Why (p. 364): suppose □A true and □□A false at $w_1$.
  1. Then $w_1$ accesses some $w_2$ where □A is false.
  2. Then $w_2$ accesses some $w_3$ where A is false.
  3. By transitivity, $w_1$ accesses $w_3$.
  4. □A is true at $w_1$, so A is true at $w_3$.
  5. A is both true and false at $w_3$, a contradiction.

*Intuition note.* Transitivity means "two steps of possibility" is already "one step". So whatever is necessary here also stays necessary at every world reachable from here.

### 44.5 A semantics for S5
- **Symmetric**: $\forall w_1\forall w_2(Rw_1w_2\to Rw_2w_1)$. A relation that is reflexive, symmetric and transitive is an **equivalence relation** (p. 364).
- $\vDash_{\mathbf{S5}}$ quantifies over interpretations whose R is an equivalence relation. S5 is stated to be sound and complete for it (pp. 364–365).
- R5 says $\neg\Box A\vdash_{\mathbf{S5}}\Box\neg\Box A$ (p. 365). Why (p. 365): suppose ¬□A true and □¬□A false at $w_1$.
  1. $w_1$ accesses some $w_2$ where A is false.
  2. $w_1$ accesses some $w_3$ where ¬□A is false.
  3. By symmetry, $w_3$ accesses $w_1$.
  4. By transitivity ($w_3\to w_1\to w_2$), $w_3$ accesses $w_2$.
  5. ¬□A is false at $w_3$, so A is true at every world $w_3$ accesses, including $w_2$.
  6. A is both true and false at $w_2$, a contradiction.
- **Universal** relation: $\forall w_1\forall w_2\,Rw_1w_2$. Defining $\vDash_{\mathbf{S5}}$ with it gives the same soundness and completeness results for S5 (p. 366).
- The authors conclude: if every world is possible relative to every world, use S5. They add that most philosophers assume logical and metaphysical necessity are of this kind, so S5 is the system most philosophers use most of the time (p. 366).

*Intuition note.* With a universal relation, "accessible" no longer limits anything, so we are back to the simple rule "□A = true at all worlds". The restrictions on R are what distinguish the systems.

### Practice and further reading
- Exercises A–C ask for counter-interpretations to false claims in K, S4 and T (pp. 366–367). Further reading: Hughes & Cresswell; Priest; Garson. The authors say Garson's formulation is closest to theirs (p. 367).

## Toy example (ours, not from the text)
Worlds $W=\{1,2,3\}$; $R=\{\langle1,2\rangle,\langle2,3\rangle\}$ (not reflexive, not transitive). Atom P: $\nu_1(P)=F$, $\nu_2(P)=T$, $\nu_3(P)=F$.
- $\Box P$ at 1: world 1 accesses only 2, and P is true at 2. By rule (6), $\Box P$ is true at 1.
- $P$ at 1 is false. So world 1 makes $\Box P$ true and $P$ false: $\Box P\nvDash_{\mathbf K}P$ (R is not reflexive).
- $\Box P$ at 2: world 2 accesses only 3, where P is false, so $\Box P$ is false at 2.
- $\Box\Box P$ at 1: it needs $\Box P$ true at every world 1 accesses, i.e. at 2, where it is false. So $\Box\Box P$ is false at 1. Hence $\Box P\nvDash_{\mathbf K}\Box\Box P$.
- Add $\langle1,3\rangle$ to make R transitive: then 1 accesses 3, where P is false, so $\Box P$ is false at 1. This counterexample disappears, as 44.4 predicts.

## Concepts
- [[possible-world-interpretation]] (new) — W, R and ν together; worlds can be anything if W is non-empty (p. 358)
- [[valuation-function]] (new) — ν maps a sentence and a world to T or F, obeying rules (1)–(7) (p. 356)
- [[accessibility-relation]] (new) — relation R; $Rw_1w_2$ means $w_2$ is possible relative to $w_1$ (p. 357)
- [[modal-validity]] (new) — no world in any (suitably restricted) interpretation has true premises and false conclusion (p. 359)
- [[counter-interpretation]] (new) — an interpretation with a world making premises true and conclusion false, showing invalidity (p. 360)
- [[validity / soundness]] — here applied to proof systems: ⊢ implies ⊨ (soundness); ⊨ implies ⊢ (completeness, new id [[completeness]]). Differs from the canon's sense, which is for arguments (p. 360)
- [[frame-conditions]] (new) — reflexive, transitive, symmetric, equivalence and universal relations, each matched to T, S4, S5 (pp. 361–366)
- [[strict-subproof]] (new) — a subproof that imports only formulas via □E, so it reasons about accessible worlds (p. 360)

## Canonical instances
- [[two-world-diagram]] — worlds 1, 2 with R as arrows; checks $A\wedge\neg B$, $B\to A$, ◇A, □¬B at world 1 (p. 358)
- [[not-A-to-not-diamond-A]] — counter-interpretation to $\neg A\vDash_{\mathbf K}\neg\Diamond A$ (p. 360)
- [[box-A-to-A]] — fails in K, valid in T via reflexivity (pp. 361–362)
- [[box-A-to-box-box-A]] — valid in S4 via transitivity (p. 364)
- [[not-box-A-to-box-not-box-A]] — valid in S5 via symmetry and transitivity (p. 365)

## Bridges (candidates)
- [structural-analogy] accessibility relation ↔ graph theory: R as a directed graph, with properties like reflexive and transitive on its edges — the diagrams are directed graphs.
- [metaphor] relative possibility ↔ social science: "possible relative to w" resembles a network of who can see or influence whom, with □ as "true of everyone visible".
- [same-math] equivalence relation for S5 ↔ set theory: an equivalence relation partitions a set into classes — the authors only call it an equivalence relation; the link to partitions is ours.

## Questions this raises
- What is a possible world really, and which kind of necessity is "every world possible relative to every world"? (The authors postpone this, p. 356.)
- Which properties of R (e.g. symmetry alone) correspond to other modal rules, and what other kinds of necessity might they model?
- How are the soundness and completeness results actually proved?
- Does the S5 assumption for logical and metaphysical necessity hold, or are there necessities where it fails?

## Exercises worth doing
- Ex. A1 (p. 366) — a counter-interpretation to $\neg P\vDash_{\mathbf K}\neg\Diamond P$ — difficulty: easy
- Ex. A3 (p. 366) — $\neg\Box(A\wedge\neg A)$ is not a K-truth, so a world must fail it — difficulty: medium
- Ex. A4 (p. 366) — $\Box A\vDash_{\mathbf K}A$ fails — difficulty: easy
- Ex. B1 (p. 366) — $\Diamond A\vDash_{\mathbf{S4}}\Box\Diamond A$ fails; needs reflexive, transitive R — difficulty: medium
- Ex. C2 (p. 367) — $\Box A\vDash_{\mathbf T}\Box\Box A$ fails; transitivity is not enforced — difficulty: medium
- Ex. B2 (p. 366) — multiple premises with nested modalities in S4 — difficulty: hard

## Reading notes
- Printed = pdf − 10.
- Typo on p. 361: "we can used A".
- The text layer garbles ν as "��"; the images show ν.
- The simple "every world / some world" rule (pp. 355, 357) is replaced by rules (6)–(7) with accessibility (p. 357); the authors call the simple rule less useful for a flexible framework.
- The authors say proofs of soundness and completeness are omitted (pp. 360, 362, 363, 365).
