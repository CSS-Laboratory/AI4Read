---
id: magnus-2025-forallx/ch21-derived
work: magnus-2025-forallx
unit: 21 Derived rules
pages: 174-181
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
# Derived rules

## L0 — One line
The chapter aims to show that the extra rules of chapter 19 are not strictly necessary, and it does so for several of them: any use can be replaced by extra lines using only the basic rules of chapter 17.

## L1 — The gist (≤ 120 words)
Why does the proof system come in two batches of rules? The chapter aims to show that the second batch (chapter 19) is not strictly necessary. For several extra rules, it gives a proof scheme built only from basic rules (chapter 17). A scheme is a recipe: put any sentences in for the variables and you get a real proof. So a derived rule adds convenience, not proving power. This matters because it explains what "derived" means: anything provable with the shortcut is provable without it, at the cost of more lines. The chapter covers R, DS, MT, DNE, LEM and the first two De Morgan rules; the other two are left as exercises.

**Prerequisites:** the basic rules of chapter 17 (∧I, ∧E, ∨I, ∨E, →E, ¬I, ¬E, IP, X, R); subproofs and assumptions; the shortcut rules of chapter 19.

## L2 — Key ideas (5–10 bullets)
- A rule is *derived* if anything justified with it can be justified with only other basic rules (p. 175).
- A *proof scheme* uses variables like 𝒜 instead of real sentences. It is a recipe for producing real proofs (p. 175).
- Reiteration (R) can be replaced by ∧I followed by ∧E, at the cost of one extra line (pp. 174–175).
- DS, MT and DNE each have a short scheme from basic rules. DS uses ∨E; MT uses →E and ¬I; DNE uses IP (pp. 176–177).
- LEM can be derived in two ways: via a proof of 𝒜 ∨ ¬𝒜 plus ∨E, or via an IP proof that embeds both subproofs (pp. 178–179).
- The first De Morgan scheme uses LEM, the second does not; the third and fourth are left as exercises (pp. 180–181).
- Adding DS made no new proofs possible; by the definition of "derived", the same holds for any derived rule, which only saves lines (pp. 175–176).

## L3 — Walkthrough

**Intro.** The author's aim is to show that the extra rules of chapter 19 are not strictly speaking necessary, but can be derived from the basic rules of chapter 17 (p. 174).

**21.1 Reiteration.** R is a basic rule, yet it is not necessary. From 𝒜 on line $m$:
- $k$: 𝒜∧𝒜 (∧I, $m$, $m$)
- $k{+}1$: 𝒜 (∧E, $k$) (pp. 174–175)

This is a *proof scheme*, not a proof, because it uses the variable 𝒜. Any TFL sentence put in for 𝒜 gives a real proof (p. 175). So whatever R proves, the basic rules prove with one more line. That is what "derived" means (p. 175).

*Intuition note:* A derived rule is a macro. It stands for a short fixed block of basic steps. Using it never lets you prove something new.

**21.2 Disjunctive Syllogism.** Given $m$: 𝒜∨ℬ and $n$: ¬𝒜, to reach ℬ on line $k{+}5$:
- $k$: assume 𝒜 (AS)
- $k{+}1$: ⊥ (¬E, $n$, $k$)
- $k{+}2$: ℬ (X, $k{+}1$)
- $k{+}3$: assume ℬ (AS)
- $k{+}4$: ℬ (R, $k{+}3$)
- $k{+}5$: ℬ (∨E, $m$, $k$–$k{+}2$, $k{+}3$–$k{+}4$) (p. 176)

The author concludes that DS added no new possible proofs. Any use of DS can be replaced by a few extra lines (p. 176).

**21.3 Modus Tollens.** Given $m$: 𝒜→ℬ and $n$: ¬ℬ:
- $k$: assume 𝒜 (AS)
- $k{+}1$: ℬ (→E, $m$, $k$)
- $k{+}2$: ⊥ (¬E, $n$, $k{+}1$)
- $k{+}3$: ¬𝒜 (¬I, $k$–$k{+}2$) (p. 177)

**21.4 Double-Negation Elimination.** Given $m$: ¬¬𝒜:
- $k$: assume ¬𝒜 (AS)
- $k{+}1$: ⊥ (¬E, $m$, $k$)
- $k{+}2$: 𝒜 (IP, $k$–$k{+}1$) (p. 177)

*Intuition note:* In MT and DNE, assume the opposite of the goal and derive ⊥. In DS, assume each disjunct and show that each leads to the goal (the first via ⊥). The basic rules then close the proof.

**21.5 Excluded Middle (LEM).** The LEM rule starts from two subproofs: one assumes 𝒜 and ends in ℬ; the other assumes ¬𝒜 and ends in ℬ. The goal is ℬ on line $l{+}1$ (pp. 177–178). The author gives two ways to get it from basic rules.

*Way 1.* Prove 𝒜∨¬𝒜 on line $i$, using only basic rules (done in section 18.6). Then apply ∨E: $i{+}1$: ℬ (∨E, $i$, $m$–$n$, $k$–$l$) (p. 178).

*Way 2.* Wrap both subproofs in an outer subproof that assumes ¬ℬ and ends in ⊥. The subproofs themselves are as given. The new lines are:
- $m$: assume ¬ℬ
- $m{+}1$: assume 𝒜 … $n$: ℬ
- $n{+}1$: ⊥ (¬E, $m$, $n$)
- $n{+}2$: assume ¬𝒜 … $l$: ℬ
- $l{+}1$: ⊥ (¬E, $m$, $l$)
- $l{+}2$: ¬𝒜 (¬I, $(m{+}1)$–$(n{+}1)$)
- $l{+}3$: ¬¬𝒜 (¬I, $(n{+}2)$–$(l{+}1)$)
- $l{+}4$: ⊥ (¬E, $l{+}3$, $l{+}2$)
- $l{+}5$: ℬ (IP, $m$–$(l{+}4)$) (p. 179)

Line numbers shift because of the new assumption. The author says you may need to stare at this for a while (p. 179).

*Intuition note:* If ¬ℬ were true, then both 𝒜 and ¬𝒜 would be refuted. That is a contradiction, so ℬ must hold.

**21.6 De Morgan rules.**

*First rule:* from ¬(𝒜∧ℬ), derive ¬𝒜∨¬ℬ.
- $m$: ¬(𝒜∧ℬ)
- $k$: assume 𝒜
- $k{+}1$: assume ℬ
- $k{+}2$: 𝒜∧ℬ (∧I, $k$, $k{+}1$)
- $k{+}3$: ⊥ (¬E, $m$, $k{+}2$)
- $k{+}4$: ¬ℬ (¬I, $(k{+}1)$–$(k{+}3)$)
- $k{+}5$: ¬𝒜∨¬ℬ (∨I, $k{+}4$)
- $k{+}6$: assume ¬𝒜
- $k{+}7$: ¬𝒜∨¬ℬ (∨I, $k{+}6$)
- $k{+}8$: ¬𝒜∨¬ℬ (LEM, $k$–$(k{+}5)$, $(k{+}6)$–$(k{+}7)$) (p. 180)

*Second rule:* from ¬𝒜∨¬ℬ, derive ¬(𝒜∧ℬ).
- $m$: ¬𝒜∨¬ℬ
- $k$: assume 𝒜∧ℬ
- $k{+}1$: 𝒜 (∧E, $k$)
- $k{+}2$: ℬ (∧E, $k$)
- $k{+}3$: assume ¬𝒜
- $k{+}4$: ⊥ (¬E, $k{+}3$, $k{+}1$)
- $k{+}5$: assume ¬ℬ
- $k{+}6$: ⊥ (¬E, $k{+}5$, $k{+}2$)
- $k{+}7$: ⊥ (∨E, $m$, $(k{+}3)$–$(k{+}4)$, $(k{+}5)$–$(k{+}6)$)
- $k{+}8$: ¬(𝒜∧ℬ) (¬I, $k$–$(k{+}7)$) (p. 180)

The third and fourth De Morgan rules are left as exercises (p. 181).

## Toy example (ours)
Take MT with 𝒜 = P and ℬ = Q. Premises: P→Q and ¬Q. Goal: ¬P.
1. P→Q (premise)
2. ¬Q (premise)
3. P (AS)
4. Q (→E, 1, 3)
5. ⊥ (¬E, 2, 4)
6. ¬P (¬I, 3–5)

One MT line has become four lines and uses only basic rules. Likewise R on P becomes: 1. P; 2. P∧P (∧I, 1, 1); 3. P (∧E, 2). The pattern is the same: one shortcut line becomes a fixed block.

## Concepts
- [[derived-rule]] (new) — a rule whose every use can be replaced by a block of other rules' steps (p. 175)
- [[basic-rule]] (new) — a rule of chapter 17; the derived rules are built from these (p. 174)
- [[proof-scheme]] (new) — a proof with variables for sentences; a recipe for real proofs (p. 175)

## Canonical instances
- [[derivation-of-reiteration]] (new) — R replaced by ∧I then ∧E (p. 174)
- [[derivation-of-DS]] (new) — DS replaced by ∨E with X and R (p. 176)
- [[derivation-of-LEM]] (new) — two ways: via 𝒜∨¬𝒜, or via an IP wrapper (pp. 178–179)
- [[derivation-of-De-Morgan]] (new) — first rule uses LEM; second does not (p. 180)

## Bridges (candidates)
- [structural-analogy] derived rule ↔ programming: macro or library function — expands into primitive steps without adding power.

## Questions this raises
- Is the same true the other way round: can any basic rule be dropped? Exercise D hints at trading IP for LEM.
- How much longer do real proofs get when every derived rule is expanded?
- Can the first De Morgan rule be proved without LEM? (Exercise E.)

## Exercises worth doing
- Ex. A (p. 181) — build the third and fourth De Morgan schemes yourself — difficulty: medium
- Ex. B (p. 181) — expand derived rules in earlier proofs and then streamline — difficulty: medium
- Ex. C (p. 181) — prove 𝒜∨¬𝒜, first freely, then with only basic rules — difficulty: hard
- Ex. D (p. 181) — show that IP is derivable if LEM is basic — difficulty: medium
- Ex. E (p. 181) — prove the first De Morgan rule directly, without LEM — difficulty: hard

## Reading notes
- Printed page = pdf − 10 (pdf 184–191 are printed pp. 174–181).
- The text layer shows script letters as plain A, B. The page images were used to check all proof schemes.
- In 21.5, the dots "…" stand for the given subproofs; the page images show them as vertical ellipses.
- The DS scheme uses X and R; the first De Morgan scheme uses LEM, itself a derived rule. Exercise E (p. 181) remarks that one can combine the LEM-based proof with the proof of LEM, and asks for a direct proof without LEM.
