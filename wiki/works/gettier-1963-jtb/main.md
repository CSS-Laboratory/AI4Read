---
id: gettier-1963-jtb/main
work: gettier-1963-jtb
unit: paper
pages: 121–123
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 2
---
# Is Justified True Belief Knowledge? (Gettier, 1963)

## L0 — One line
Gettier argues, with two cases, that being justified in truly believing P does not suffice for knowing P, because in his cases S has a justified true belief that clearly is not knowledge.

## L1 — The gist (≤ 120 words)
Some philosophers (Gettier cites Chisholm and Ayer) give necessary and sufficient conditions for knowledge. Roughly: S knows P iff P is true, S believes P, and S is justified in believing P. Gettier asks whether these conditions are really enough. He builds two cases. In each, S validly infers a proposition from a well-supported but false one. The conclusion turns out true, but not because of S's evidence. S then has a justified true belief, yet clearly lacks knowledge. So the analysis fails as a sufficient condition. This matters because the analyses were offered as necessary and sufficient conditions, so they fail as complete definitions of knowledge.

**Prerequisites:** necessary vs. sufficient conditions; "iff"; logical entailment; "A or B" is true if at least one part is true; conjunction ("and").

## L2 — Key ideas (5–10 bullets)
- Gettier reports a family of analyses of "S knows that P", of the form: P is true, S believes P, S is justified in believing P. He cites Chisholm's (b) and Ayer's (c) as variants (p. 121).
- His target is narrow: he says (a) fails as a *sufficient* condition. He does not argue in this paper that any of its conditions is unnecessary (p. 121).
- Premise 1: the "justified" needed for knowledge can be had for a false proposition (p. 121).
- Premise 2: if S is justified in believing P, P entails Q, and S deduces Q from P and accepts Q because of that deduction, then S is justified in believing Q (p. 121).
- Case I: Smith is justified in believing (e), which is true. But it is true because of Smith's own coins, while his evidence concerns Jones. Smith does not know (e) (p. 122).
- Case II: Smith is justified in believing the disjunction (h). It is true only because of a coincidence about Brown's location. Smith does not know (h) (pp. 122–123).
- The same cases, suitably changed, are said to refute (b) and (c) as well (pp. 121, 123).

## L3 — Walkthrough
The paper has no numbered sections. I follow its order.

### Opening: the analyses under attack (p. 121)
Gettier says recent attempts to state necessary and sufficient conditions for knowing a proposition can often be put in this form:

(a) S knows that P **iff** (i) P is true, (ii) S believes that P, and (iii) S is justified in believing that P.

He adds two variants and attributes them:
- **Chisholm** (Gettier's report; source given as *Perceiving*, 1957, p. 16): (b) S knows that P iff (i) S accepts P, (ii) S has adequate evidence for P, and (iii) P is true.
- **Ayer** (Gettier's report; source given as *The Problem of Knowledge*, 1956, p. 34): (c) S knows that P iff (i) P is true, (ii) S is sure that P is true, and (iii) S has the right to be sure that P is true.

A footnote says Plato "seems to be considering some such definition" at *Theaetetus* 201 and "perhaps accepting one" at *Meno* 98 (p. 121, n. 1).

**Gettier's thesis:** (a) is false because its conditions are not a *sufficient* condition for "S knows that P". The same argument will show that (b) and (c) fail if "has adequate evidence for" or "has the right to be sure that" is substituted for "is justified in believing that" throughout (p. 121).

### Two preliminary points (p. 121)
1. In the sense of "justified" in which justification is a necessary condition of knowing, a person can be justified in believing a proposition that is in fact false.
2. For any P: if S is justified in believing P, P entails Q, and S deduces Q from P and accepts Q as a result of this deduction, then S is justified in believing Q.

*Intuition note:* Point 1 says good evidence does not guarantee truth. Point 2 says justification carries over along a deduction that S actually performs. Together they let a false-but-well-supported belief pass its justification to a new belief that happens to be true.

### Case I (p. 122)
Smith and Jones have applied for a job. Smith has strong evidence for the conjunction:

(d) Jones is the man who will get the job, and Jones has ten coins in his pocket.

His evidence might be the company president's assurance that Jones will be selected, plus Smith's own count of Jones's coins ten minutes ago.

(d) entails (e): *The man who will get the job has ten coins in his pocket.* Smith sees the entailment and accepts (e) on the grounds of (d). So Smith is "clearly justified" in believing (e) (p. 122).

Now suppose that, unknown to Smith, he himself will get the job, and he himself has ten coins in his pocket. Then (e) is true and (d) is false. All three hold:
- (i) (e) is true;
- (ii) Smith believes (e);
- (iii) Smith is justified in believing (e).

Gettier says it is equally clear that Smith does not know (e). Reason: (e) is true in virtue of the coins in Smith's pocket. Smith does not know how many coins those are. He bases his belief on a count of Jones's coins, and Jones is falsely believed to be the man who will get the job (p. 122).

*Intuition note:* Smith's reasons and the fact that makes (e) true are unconnected. His belief is right, but not because of anything he has checked.

### Case II (pp. 122–123)
Smith has strong evidence for:

(f) Jones owns a Ford.

His evidence might be that Jones has always owned a Ford, as far as Smith remembers, and has just offered Smith a ride in a Ford. Smith has a friend, Brown, whose whereabouts he does not know at all. He picks three place-names at random and builds:

(g) Either Jones owns a Ford, or Brown is in Boston;
(h) Either Jones owns a Ford, or Brown is in Barcelona;
(i) Either Jones owns a Ford, or Brown is in Brest-Litovsk.

(f) entails each of them. Smith sees this and accepts (g), (h), (i) on the basis of (f). So he is "completely justified" in believing each, though he has no idea where Brown is (p. 123).

Now add two conditions. First, Jones does not own a Ford; he is driving a rented car. Second, by sheer coincidence and unknown to Smith, Brown is in the place named in (h), Barcelona. Then (h) is true, Smith believes (h), and Smith is justified in believing (h). Yet Smith does not know that (h) is true (p. 123).

*Intuition note:* A disjunction is true if either part is true. Here the true part is the one Smith picked at random, and the part he has evidence for is false. The truth of (h) has nothing to do with his evidence.

### Conclusion (p. 123)
The two examples show that (a) does not state a sufficient condition for knowing. The same cases, "with appropriate changes," suffice to show that neither (b) nor (c) does so either (p. 123).

## Toy example (ours, not from the text)
Ann has strong evidence for F: "Bo owns a bike". She saw him ride one daily, but it was always borrowed, so F is false. She constructs D: "Bo owns a bike, or Cy is in Rome". She does not know where Cy is. Suppose Cy is in Rome by coincidence.

Check the conditions of (a) for D:
- D is true: F is false, R ("Cy is in Rome") is true, and "false or true" is true.
- Ann believes D: she deduced it from F.
- Ann is justified: she has strong evidence for F, F entails D, and she accepts D because of that deduction (premise 2).

All three conditions hold, yet Ann does not know D. Her evidence concerns the bike, and D is true only because of Cy's location, which she has no evidence about. This has Gettier's Case II structure.

## Concepts
- [[justified true belief (JTB)]] — the analysis (a): S knows P iff P is true, S believes P, and S is justified in believing P (p. 121)
- [[necessary-sufficient-conditions]] (new) — "necessary": knowledge cannot lack it. "Sufficient": having it guarantees knowledge. Gettier attacks only sufficiency (p. 121)
- [[epistemic luck]] — our label for what the cases share: the belief is true, but not because of S's evidence (Case I, p. 122). Gettier calls the match in Case II a coincidence (p. 123) and does not use the term "luck".
- [[fallible-justification]] (new) — justification of the kind needed for knowledge can attach to a false proposition (p. 121)
- [[closure-of-justification-under-deduction]] (new) — justification is transmitted to Q when S deduces Q from a justified P and accepts Q because of this (p. 121)

## Canonical instances
- [[gettier-case-coins]] — Case I: Smith, Jones, the job and the ten coins; justified true belief (e) without knowledge (p. 122)
- [[gettier-case-ford-barcelona]] — Case II: "Jones owns a Ford or Brown is in Barcelona"; justified true belief (h) without knowledge (pp. 122–123)

## Bridges (candidates)
- [structural-analogy] Gettier case ↔ statistics/modelling: a correct prediction produced by a misspecified model that is right only by coincidence — good fit with the evidence, but the truth is not connected to the model's reasons.
- [structural-analogy] Disjunction trick in Case II ↔ logic: from a well-supported P, "P or Q" is entailed for any Q, so a justified belief in the disjunction costs nothing and can be true via Q alone.

## Questions this raises
- What exactly is missing between "justified true belief" and knowledge? Is it a fourth condition, or a different kind of justification?
- Is premise 2 (justification transmitted by deduction) plausible in general? Would giving it up block the cases?
- Are conditions (i)–(iii) still necessary for knowledge? The paper argues only against sufficiency.
- Are Cases I and II alike in what goes wrong, or do they show two different failures?

## Reading notes
- The page labels give no printed numbers. The text layer shows running headers "122" and "123", and the page 1 image shows "121". So printed = pdf + 120, and I cite printed pages.
- Pages 121–123 contain Gettier's whole paper. The last part of pdf page 3 starts a different article (Achinstein, "Circularity and Induction"). I left it out.
- OCR problems in the text layer: footnote 1 reads "Mem 98"; the image shows *Meno* 98. The list markers "(/) … («) … (///)" stand for (i), (ii), (iii). "Brest-Iitovsk" stands for Brest-Litovsk.
- "Wayne State University" under the end of the paper appears after the end of Gettier's paper (presumably his affiliation; the pages do not say so).
- Pages 2 and 3 were checked from the text layer only. Only the page 1 image was supplied.
