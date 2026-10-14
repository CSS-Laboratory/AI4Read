---
id: magnus-2025-forallx/ch44-b
work: magnus-2025-forallx
unit: "Appendix B — Alternative proof systems"
pages: 404-410
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
# Alternative proof systems

## L0 — One line
Which natural-deduction rules count as basic and which as derived is a choice, and the authors justify their choices by cleanliness, ease of checking proofs, an intuitive treatment of the quantifiers, and by keeping rules that philosophers discuss, such as IP and explosion, visible as separate rules.

## L1 — The gist (≤ 120 words)
The book's natural deduction system takes some rules as basic and derives others. Other systems divide the rules differently. The appendix sketches three alternatives. Disjunctive syllogism (DS) could be basic, with ∨E derived. Two-conclusion negation rules could replace ⊥. The ∀ rules plus quantifier-exchange (CQ) rules could be basic, with the ∃ rules derived. For each, the authors give their reasons for choosing differently. The reasons are cleaner rules, easier proof-checking, a more intuitive treatment of the quantifiers, and a clear view of which rules depend on the contested indirect-proof rule. This matters for seeing what a logic without that rule would look like.

**Prerequisites:** the book's natural-deduction rules (→I, →E, ¬I, ¬E, IP, ∀I, ∀E, ∃I, ∃E, DS, MT, CQ); subproofs and assumptions; ⊥ (the contradiction symbol); LEM (excluded middle, A∨¬A); DNE (double negation elimination); X (explosion: from ⊥ infer any sentence).

## L2 — Key ideas (5–10 bullets)
- The basic/derived split is not forced. Different rule sets can be basic, and the rest are then derived. (p. 404)
- With DS basic, ∨E can be derived. The authors still take ∨E as basic because DS mentions ¬, and it is "in some sense 'cleaner'" for ∨E to avoid mentioning other connectives. (pp. 404–405)
- Rules ¬I* and ¬E* would make ⊥ unnecessary and give fewer rules. (p. 406)
- The authors keep ⊥ because it makes proofs considerably easier to work with; for instance, a subproof's conclusion is always the sentence on its last line, so it is easy to check. (pp. 406–407)
- Much philosophical discussion concerns whether IP (equivalently LEM or DNE) and explosion are acceptable. Keeping them as separate rules makes it easier to see what a system without them looks like. (p. 407)
- The authors' basic rules coincide with Gentzen's (1935) as refined by Prawitz (1965). (p. 407)
- ∃I and ∃E can be derived from ∀I, ∀E and CQ, but the derivations use IP. (pp. 407–409)
- So the ∃ rules are kept basic and CQ is derived. Without IP, LEM and DNE, the CQ step from ¬∀xA to ∃x¬A cannot be derived. (pp. 409–410)

## L3 — Walkthrough

**Opening.** The authors treated some rules as basic and others as derived. Other choices were possible. They look at disjunction, negation and quantifiers, and explain their choices. (p. 404)

### B.1 Alternative disjunction elimination (pp. 404–405)
- Some systems take DS as the basic ∨ elimination rule and treat ∨E as derived. (p. 404)
- **Derivation of ∨E from DS** (p. 405). Given $\mathscr A\lor\mathscr B$ (line $m$), a subproof $\mathscr A\vdash\mathscr C$ ($i$–$j$) and a subproof $\mathscr B\vdash\mathscr C$ ($k$–$l$):
  1. $n$: $\mathscr A\to\mathscr C$ by →I, $i$–$j$; $n{+}1$: $\mathscr B\to\mathscr C$ by →I, $k$–$l$.
  2. $n{+}2$: assume $\neg\mathscr C$. $n{+}3$: assume $\mathscr A$. $n{+}4$: $\mathscr C$ by →E, $n{+}3$, $n$. $n{+}5$: $\bot$ by ¬E, $n{+}2$, $n{+}4$.
  3. $n{+}6$: $\neg\mathscr A$ by ¬I, $n{+}3$–$n{+}5$.
  4. $n{+}7$: $\mathscr B$ by DS, $m$, $n{+}6$. $n{+}8$: $\mathscr C$ by →E, $n{+}7$, $n{+}1$. $n{+}9$: $\bot$ by ¬E, $n{+}2$, $n{+}8$.
  5. $n{+}10$: $\mathscr C$ by IP, $n{+}2$–$n{+}9$.
- **Why ∨E stays basic:** DS uses ¬ in its statement. It is "in some sense 'cleaner'" for a ∨ rule not to mention other connectives. Magnus's original version went the other way. (p. 405)

*Intuition note.* Assuming the opposite of what you want lets DS do the work of cases. The price is that the derivation needs negation rules, which a basic ∨E does not.

### B.2 Alternative negation rules (pp. 406–407)
- **¬I\*** (p. 406): assume $\mathscr A$; derive $\mathscr B$ (line $n{-}1$) and $\neg\mathscr B$ (line $n$); conclude $\neg\mathscr A$, citing $m$–$n$.
- **¬E\*** (p. 406): assume $\neg\mathscr A$; derive $\mathscr B$ and $\neg\mathscr B$; conclude $\mathscr A$. This is a version of IP.
- With these two rules, ⊥ could be avoided altogether, and the system would have fewer rules. Magnus's original went this way. (p. 406)
- Another route takes LEM or DNE as basic and derives IP. Such systems often rename rules: our ¬E is sometimes called ⊥I, and what we call X is sometimes called ⊥E. Button's version replaces IP with LEM, called TND ("tertium non datur"). (p. 406)
- **Reason 1:** with ⊥, the conclusion of a subproof is always clear: the last line (⊥ in IP or ¬I). In ¬I\* and ¬E\* a subproof has two conclusions, so you cannot check at a glance. (pp. 406–407)
- **Reason 2:** much philosophical discussion concerns IP (equivalently LEM or DNE) and explosion. As separate rules, they make it easier to know what a system lacking them would look like. (p. 407)
- The authors' basic rules coincide with Gentzen's system (1935) as refined by Prawitz (1965). They say these are the standard rules in philosophical and mathematical discussion beyond introductory courses. (p. 407)

*Intuition note.* Dropping ⊥ saves rules, but a subproof then has two conclusions that must be matched. Keeping ⊥, IP and explosion as separate named rules makes it easier to see what a system without them would look like.

### B.3 Alternative quantification rules (pp. 407–410)
- Alternative: take ∀I, ∀E (chapter 36) and two CQ rules (from $\forall x\,\neg\mathscr A$ to $\neg\exists x\,\mathscr A$ and back) as basic. Goldfarb takes this line. (p. 407)
- **Deriving ∃I.** Suppose $\mathscr A$ contains the name $c$ and no instances of $x$. (p. 407) From $m$: $\mathscr A(\ldots c\ldots c\ldots)$ (p. 408):
  - $m{+}1$: assume $\neg\exists x\,\mathscr A(\ldots x\ldots c\ldots)$.
  - $m{+}2$: $\forall x\,\neg\mathscr A(\ldots x\ldots c\ldots)$ by CQ, $m{+}1$.
  - $m{+}3$: $\neg\mathscr A(\ldots c\ldots c\ldots)$ by ∀E, $m{+}2$.
  - $m{+}4$: $\bot$ by ¬E, $m{+}3$, $m$.
  - $m{+}5$: $\exists x\,\mathscr A(\ldots x\ldots c\ldots)$ by IP, $m{+}1$–$m{+}4$.
- **Deriving ∃E** is "more subtle", since ∃E (like ∀I) has a constraint: $c$ must not occur in any undischarged assumption, in $\mathscr B$, or in $\exists x\,\mathscr A(\ldots x\ldots x\ldots)$. (p. 408) From $m$: $\exists x\,\mathscr A$; subproof $i$–$j$: assume $\mathscr A(\ldots c\ldots c\ldots)$, derive $\mathscr B$ (p. 409):
  - $k$: $\mathscr A(\ldots c\ldots c\ldots)\to\mathscr B$ by →I, $i$–$j$.
  - $k{+}1$: assume $\neg\mathscr B$. $k{+}2$: $\neg\mathscr A(\ldots c\ldots c\ldots)$ by MT, $k$, $k{+}1$.
  - $k{+}3$: $\forall x\,\neg\mathscr A(\ldots x\ldots x\ldots)$ by ∀I, $k{+}2$. $k{+}4$: $\neg\exists x\,\mathscr A(\ldots x\ldots x\ldots)$ by CQ, $k{+}3$.
  - $k{+}5$: $\bot$ by ¬E, $k{+}4$, $m$. $k{+}6$: $\mathscr B$ by IP, $k{+}1$–$k{+}5$.
- ∀I at $k{+}3$ is allowed because $c$ is not in any undischarged assumption or in $\mathscr B$. The constraint on $c$ is thus respected. (p. 409)
- With these derived rules, the two remaining CQ rules can be derived as in chapter 40. (p. 409)
- **Why the authors do the reverse (∃ rules basic, CQ derived):**
  1. It seems more intuitive to treat the quantifiers on a par, each with its own introduction and elimination rules. (p. 409)
  2. The derivations above used IP, which is contentious. To drop IP and still use ∃, one should take the quantifier rules as basic and CQ as derived. Without IP, LEM and DNE, the CQ rule from $\neg\forall x\,\mathscr A$ to $\exists x\,\neg\mathscr A$ cannot be derived. (pp. 409–410)

*Intuition note.* "No instance fails" is turned into "some instance holds" in these derivations by assuming the opposite and reaching a contradiction. That move is IP. The authors say a system that abandons IP but keeps ∃ should take the quantifier introduction and elimination rules as basic.

## Toy example (ours, not from the text)
Prove $\neg(P\land\neg P)$ with no premises, in two ways.
- **With ¬I\*:** 1. assume $P\land\neg P$. 2. $P$ (∧E, 1). 3. $\neg P$ (∧E, 1). 4. $\neg(P\land\neg P)$ by ¬I\*, 1–3, with $\mathscr B=P$ on line 2 and $\neg\mathscr B$ on line 3. Total: 4 lines.
- **With ⊥ (the book's way):** lines 1–3 as above, then 4. $\bot$ (¬E, 2, 3). 5. $\neg(P\land\neg P)$ by ¬I, 1–4. Total: 5 lines.
- The ⊥ version has one more line. But its subproof ends in a single conclusion, ⊥, on its last line. In the ¬I\* version you must check that lines 2 and 3 form a pair $\mathscr B,\neg\mathscr B$.

## Concepts
- [[basic-vs-derived-rule]] (new) — a basic rule is taken as primitive; a derived rule is shown from basic ones. The split is a choice. (p. 404)
- [[disjunctive-syllogism]] (new) — from $\mathscr A\lor\mathscr B$ and $\neg\mathscr A$, infer $\mathscr B$; can serve as basic ∨ elimination. (pp. 404–405)
- [[indirect-proof-IP]] (new) — assume $\neg\mathscr A$, reach ⊥, conclude $\mathscr A$; the text calls it equivalent to LEM or DNE (p. 407) and "contentious" (p. 409).
- [[explosion]] (new) — the rule from ⊥ to any sentence (symbol X); also philosophically discussed. (p. 407)
- [[quantifier-exchange-CQ]] (new) — rules moving between $\forall x\neg\mathscr A$ and $\neg\exists x\mathscr A$ (and the other pairs). (p. 407)
- [[eigenvariable-constraint]] (new) — ∃E needs a name $c$ absent from undischarged assumptions, from $\mathscr B$ and from the ∃-sentence (p. 408); the text notes that ∀I also has a constraint, checked at line $k{+}3$: $c$ not in undischarged assumptions or in $\mathscr B$ (p. 409).

## Canonical instances
- [[derive-or-elim-from-DS]] — ∨E derived from DS, →I, ¬I and IP. (p. 405)
- [[derive-exists-intro-via-IP]] — ∃I derived from CQ, ∀E and IP. (p. 408)
- [[derive-exists-elim-via-IP]] — ∃E derived with ∀I, MT, CQ and IP, respecting the constraint on $c$. (p. 409)

## Bridges (candidates)
- [structural-analogy] choice of basic vs derived rules ↔ analytic-philosophy: choosing which principles to take as primitive when analysing a concept — the same body of consequences can be organised differently.
- [metaphor] keeping IP as an explicit, removable rule ↔ analytic-philosophy: making a disputed assumption explicit so it can be examined or dropped.

## Questions this raises
- What exactly would a system without IP, LEM and DNE be able to prove, and what would it lose?
- Do ¬I\* and ¬E\* prove exactly the same sentences as the book's ¬I, ¬E, IP and explosion?
- Why is IP contested, given that it is standard in the Gentzen–Prawitz rules?
- Can ∃I and ∃E be derived without IP in some other way?

## Reading notes
- Printed page = pdf page − 10 (pdf 414 = p. 404).
- Source typo: "we could we could" (p. 406).
- On p. 409 the text says lines $k{+}4$ and $k{+}1$ "contradict each other". The derivation itself (¬E, $k{+}4$, $m$) shows the contradiction is between lines $k{+}4$ and $m$. The reason the text gives is that $c$ does not occur in the ∃-sentence.
- The unit has no exercises. The rule MT is cited on p. 409 but not defined here.
