---
id: magnus-2025-forallx/ch02-scope
work: magnus-2025-forallx
unit: "2 The scope of logic"
pages: 7-17
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# The scope of logic

## L0 — One line
An argument is valid if no possible case makes all its premises true and its conclusion not true, and logic wants to choose cases so that validity depends only on an argument's logical form, not on its content or on whether the sentences are actually true.

## L1 — The gist (≤ 120 words)
What does it mean for a conclusion to follow from premises? The chapter defines consequence as the absence of counterexamples: no case where all premises are true and the conclusion is not. Which arguments count as valid depends on what a "case" is. Logic wants a notion of case on which validity depends only on logical form (the pattern of an argument). Validity is not actual truth: valid arguments can have false conclusions, and invalid ones can have true premises and a true conclusion. An argument is sound if it is valid and its premises are all true. Inductive arguments (generalising from observed cases), even good ones, are not deductively valid, and the book sets them aside.

**Prerequisites:** the notions of sentence, premise, conclusion, argument (chapter 1); "true" and "false" in everyday use.

## L2 — Key ideas
- Consequence: A follows from B₁,…,Bₙ iff there is no case where all Bᵢ are true and A is not true (p. 9).
- A counterexample is a case with true premises and a non-true conclusion. One counterexample shows invalidity (pp. 8–10).
- Different notions of "case" give different validities: nomological (counterexamples must respect the laws of nature), conceptual (they must respect word meanings), and the formal kind logic wants (pp. 10–13).
- Logic wants validity to depend only on the argument's pattern (its logical form), not on its content. The book shows an argument is not formally valid by finding another argument of the same form that is clearly not valid (pp. 12–13).
- Every case makes each sentence true or false, never both (bivalence, an assumption of this book) (p. 14).
- Validity is not actual truth. Soundness adds true premises, and logic only helps with the validity part of rebutting an argument (p. 15).
- Inductive arguments (generalising from observed cases) are not deductively valid. The book studies only the valid/invalid sorting (p. 16).

## L3 — Walkthrough

### 2.1 Consequence and validity
- Logic is concerned with consequence: when a conclusion follows from premises. One might even say that logic is the science of what follows from what (p. 7).
- Argument 1: "Either the butler or the gardener did it. The butler didn't do it. ∴ The gardener did it." Even without context, you probably agree that if both premises are true, the conclusion cannot but be true. It is **valid** (p. 8).
- Argument 2: "If the driver did it, the maid didn't do it. The maid didn't do it. ∴ The driver did it." Both premises can be true while the conclusion is not, because someone else may have done it. The conclusion does not follow, so it is **invalid** (p. 8).

### 2.2 Cases and types of validity
- We showed argument 2 invalid by describing a scenario: neither driver nor maid did it, a third person did. Such a scenario is a **counterexample** (pp. 8–9).
- Definition: A is a **consequence** of B₁,…,Bₙ iff there is no case where B₁,…,Bₙ are all true and A is not true. Equivalent wording: A follows from, or B₁,…,Bₙ entail, A (p. 9).
- The authors call this definition "incomplete": it does not say what a case is or what it means to be true in a case (p. 9).
- An argument is valid iff its conclusion is a consequence of its premises. It is invalid iff it is not valid, i.e. has a counterexample (p. 10).
- If "case" means "hypothetical scenario", argument 1 is valid: imagining its premises true already means imagining the gardener did it (p. 10).
- Open questions: are scenarios limited by the laws of physics, or by what is conceivable? The answers change which arguments are valid (p. 10).
- Spaceship example: the Rocinante took six hours to reach Jupiter from Tycho space station, so the distance is less than 14 billion km. A counterexample would be a trip of over 14 billion km in 6 hours, exceeding the speed of light. It exists only if scenarios may break physics (pp. 10–11).
- Priya example: the premise is that Priya is an ophthalmologist, the conclusion that Priya is an eye doctor. It is valid if only conceivable scenarios count, because the meanings of the words rule out the counterexample (p. 11).
- Hence **nomologically valid** (no counterexample respecting the laws of nature) and **conceptually valid** (none respecting conceptual connections between words). For these, facts about the world and word meanings both matter (p. 11).

*Intuition note:* Whether an argument is valid depends on a choice of which cases count. Allowing more cases as counterexamples (as with the spaceship) leaves fewer arguments valid.

### 2.3 Formal validity
- Logical consequence should depend not on content but only on **logical form** (p. 12).
- Compare two arguments with the premises that Priya is either an ophthalmologist or a dentist and that Priya isn't a dentist: one concludes that Priya is an eye doctor, the other that Priya is an ophthalmologist. Both are valid. Only the second is **formally valid**, because the first needs the meanings of "ophthalmologist" and "eye doctor" (p. 12).
- Form of the second: "A is either an X or a Y. A isn't a Y. ∴ A is an X." A, X, Y are placeholders. The Mei argument (mathematician/botanist) has the same form (p. 12).
- The first argument has the same two premises as that pattern, but its conclusion is of the form A is a Z. The Mei argument with the conclusion that Mei is an acrobat has this form and is clearly not valid (we can imagine a mathematician Mei who is not an acrobat). Hence the first argument is not formally valid (p. 13).
- Strategy: choose a notion of "case" on which an argument is valid only if it is formally valid. Such a notion of case will have to violate not just some laws of nature but some laws of English. We allow a case where Priya is an ophthalmologist but not an eye doctor, even though it is not conceivable (p. 13).
- One assumption: every case makes every sentence under consideration true or not true. Scenarios leaving this undetermined are not considered. Example: a case where Priya is a dentist but not an ophthalmologist counts for the Priya arguments but not for the Mei arguments, since it says nothing about Mei (pp. 13–14).
- If a case does not make a sentence true, it makes it false. We assume that cases make sentences true or false, never both (p. 14).
- Footnote: this is **bivalence**. The footnote calls this assumption controversial: some logicians consider sentences with intermediate truth or neither true nor false, and some philosophers allow sentences to be both. Such systems are not discussed in the book (p. 14).

*Intuition note:* Replace the subject-matter words with placeholders. If another argument with the same pattern can have true premises and a conclusion that is not true, the original is not formally valid.

### 2.4 Sound arguments
- A valid argument supports its conclusion only if its premises are true. Validity does not rule out a conclusion that is simply not true (p. 14).
- "Oranges are either fruit or musical instruments. Oranges are not fruit. ∴ Oranges are musical instruments." It is valid, with an absurd conclusion (p. 14).
- True premises and a true conclusion are not enough for validity. "London is in England. Beijing is in China. ∴ Paris is in France." All are true, but if Paris were to declare independence, the conclusion would no longer be true while the premises remained true. So it is invalid (p. 15).
- Validity is about whether a case with true premises and a non-true conclusion is possible, not about actual truth. Footnote: there is one case where the facts do matter. If the premises are in fact true and the conclusion in fact not true, we live in a counterexample, so the argument is invalid (p. 15).
- An argument is **sound** iff it is valid and all its premises are true (p. 15).
- To rebut an argument, show a premise is not true or show the argument is invalid. Logic helps only with the latter (p. 15).

### 2.5 Inductive arguments
- "Every winter so far, it has snowed in Calgary. ∴ It will snow in Calgary this coming winter." This is an **inductive argument** (generalising from observed cases). It is invalid: a case with true premises and no snow is possible (p. 16).
- Even good inductive arguments are not deductively valid. Their conclusion can be false with true premises, however unlikely (p. 16).
- The book sets aside what makes a good inductive argument (p. 16).
- Terminology: entailment is a relation between premises and conclusion. Inference is something we do. Do not say that premises infer a conclusion. One may infer the conclusion from the premises (p. 16).

## Toy example
(Ours.) For simplicity, treat a "case" as an assignment of true (T) or false (F) to the sentences: P = "Ana plays piano", V = "Ana plays violin".

Argument: "P or V. Not P. ∴ V." Check all four cases:
- P=T, V=T: "Not P" is F. Not a counterexample.
- P=T, V=F: "Not P" is F. Not a counterexample.
- P=F, V=T: "P or V" is T, "Not P" is T, V is T. Conclusion true. Not a counterexample.
- P=F, V=F: "P or V" is F. Not a counterexample.

No case has true premises and a non-true conclusion, so the argument is valid. Now change the conclusion to a new sentence C = "Ana plays cello". Take P=F, V=T, C=F: "P or V" is T, "Not P" is T, C is F. This is a counterexample, so "P or V. Not P. ∴ C" is invalid. This mirrors the Mei/acrobat contrast (p. 13).

## Concepts
- [[consequence-entailment]] (new) — A follows from B₁,…,Bₙ iff no case has all Bᵢ true and A not true (p. 9)
- [[counterexample]] (new) — a case where the premises are true and the conclusion is not true (p. 9)
- [[validity / soundness]] — valid: conclusion is a consequence of the premises. Sound: valid plus all premises true (pp. 10, 15)
- [[formal-validity]] (new) — validity that depends only on logical form, not on content (p. 12)
- [[logical form vs. grammatical form]] — here, form is a pattern with placeholders (A, X, Y) that replace expressions (p. 12)
- [[bivalence]] (new) — every case makes each sentence true or false, never both (p. 14)
- [[inductive-argument]] (new) — an argument generalising from observed cases; not deductively valid (p. 16)

## Canonical instances
- [[butler-gardener-argument]] (new) — a valid argument whose subject matter we do not know (p. 8)
- [[oranges-musical-instruments]] (new) — a valid argument with an absurd conclusion (p. 14)
- [[london-beijing-paris]] (new) — true premises and a true conclusion, yet invalid (p. 15)
- [[calgary-snow]] (new) — a good inductive argument that is not deductively valid (p. 16)

## Bridges (candidates)
- [structural-analogy] Counterexample test for validity ↔ falsifiability: one case that violates the claim refutes it, and the claim's strength lies in having no such case.
- [metaphor] Formal validity as pattern-matching ↔ computing: checking form while ignoring content resembles type-checking.

## Questions this raises
- What exactly is a "case" once we make it precise, and how do we decide when a sentence is true in one?
- Which logical words (like "or", "not", "if") fix the form, and how are forms stated exactly?
- If the book sets inductive arguments aside, how could one judge a good inductive argument?
- What would logic look like if sentences could be neither true nor false?

## Exercises worth doing
- Ex. A (pp. 16–17) — sort six arguments into valid and invalid; items 3 and 6 test whether you attend to cases, not to actual truth — difficulty: easy
- Ex. B.1–B.3 (p. 17) — whether valid arguments can have false premises or a false conclusion — difficulty: medium
- Ex. B.4–B.5 (p. 17) — whether adding a premise can change validity — difficulty: medium

## Reading notes
- Printed page = pdf page − 10. Source pages 7–17 were used.
- The text layer matched the layout well. No math in this unit. One misprint: "perfectly possibly" for "perfectly possible" (p. 14).
- Footnotes 1 (bivalence, p. 14) and 2 (p. 15) are included above.
