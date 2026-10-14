---
id: magnus-2025-forallx/ch04-first
work: magnus-2025-forallx
unit: 4 First steps to symbolization
pages: 27-31
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# First steps to symbolization

## L0 — One line
Many arguments are valid because of their form, so we replace whole sentences with letters to show that form; TFL does this, but at best it helps us understand arguments that are valid because of their form.

## L1 — The gist (≤ 120 words)
The chapter looks at why some arguments are valid. Its examples illustrate validity in virtue of form: arguments about rain or about Tolstoy can share one pattern, and their validity has little to do with the topic. The authors then introduce TFL (truth-functional logic), a formal language whose basic units are sentence letters standing for whole English sentences. They warn that some valid arguments (vixen/fox, green/red) are valid for reasons other than form, so at best TFL helps with arguments that are valid due to their form. Finally they explain sentence letters and symbolization keys. These letters are the building blocks from which more complex TFL sentences are built.

**Prerequisites:** the notion of a valid argument (premises cannot all be true with a false conclusion); sentence connectives such as "and", "or", "not", "if…then".

## L2 — Key ideas
- Different arguments can share one structure, shown by replacing subsentences with letters (p. 27–28, 30).
- Validity in virtue of form: the validity of the examples has little to do with the meanings of English expressions like 'Jenny is miserable' (p. 28).
- If meanings matter at all, they are those of "and", "or", "not", "if…then" (p. 28).
- TFL is the formal language, developed in parts II–IV, for showing form-based validity (p. 28–29).
- Some arguments are valid for special reasons (word meaning, colour incompatibility) that form does not explain (p. 29–30).
- At best, TFL helps with arguments valid due to their form (p. 30).
- Sentence letters are TFL's atomic sentences. Subscripts give unlimited supply (p. 30).
- A symbolization key assigns English sentences to letters only temporarily, and a letter has no inner structure (p. 30–31).

## L3 — Walkthrough

### 4.1 Validity in virtue of form
- Two valid arguments are given (p. 27). (1) It is raining outside; if it is raining outside, then Jenny is miserable; therefore Jenny is miserable. (2) The same pattern with Jenny being an anarcho-syndicalist and Dipan being an avid reader of Tolstoy.
- They share a structure (p. 27): A; If A, then C; ∴ C. The authors say "surely" any argument with this structure is valid (p. 28).
- Two further structures, each illustrated by a valid argument (p. 28):
  - Jenny is either happy or sad; Jenny is not happy; therefore Jenny is sad. Structure: A or B; not-A; ∴ B.
  - It is not the case that Jim both studied hard and acted in lots of plays; Jim studied hard; therefore Jim did not act in lots of plays. Structure: not-(A and B); A; ∴ not-B.
- Conclusion: validity in virtue of form. Validity has "nothing very much" to do with the meanings of the sentences about Jenny, Dipan or Jim. If meanings matter at all, they are those of "and", "or", "not" and "if…, then…" (p. 28).
- Plan: parts II–IV build a formal language, truth-functional logic (TFL), to symbolize many arguments so as to show validity in virtue of form (p. 28–29). Footnote: TFL is also often called (classical) "propositional" or "sentential" logic (p. 29).
- *Intuition note:* Two arguments about different things can be "the same argument" once the topic words are blanked out. If the pattern guarantees validity, every filling-in of the blanks gives a valid argument.

### 4.2 Validity for special reasons
- Formal validity was introduced in section 2.3. Some arguments are valid but not because of form (p. 29).
- Vixen case: Juanita is a vixen; therefore Juanita is a fox. The premise cannot be true with a false conclusion, since "vixen" just means "female fox", so the argument is (conceptually) valid (p. 29).
  - A same-form invalid argument: Juanita is a vixen; therefore Juanita is a cathedral. So form does not explain the validity (p. 29).
- Colour case: The sculpture is green all over; therefore it is not red all over. It seems there can be no case where the premise is true and the conclusion false, since nothing can be both green all over and red all over; so the argument is valid (p. 29).
  - A same-form invalid argument: the conclusion is that the sculpture is not shiny all over. It is invalid because a sculpture can be green and shiny all over, e.g. with shiny green varnish (p. 29–30).
  - The authors say it is plausible that the validity of the colour argument is keyed to how colours (or colour-words) interact; but whether or not that is right, form alone does not make it valid (p. 30).
- Moral: at best, TFL will help us understand arguments that are valid due to their form (p. 30).
- *Intuition note:* A test for validity because of form: keep the pattern, change the content words. If an invalid argument appears, the pattern was not what guaranteed validity.

### 4.3 Atomic sentences
- Form was isolated by replacing subsentences with single letters, e.g. the subsentence about rain inside the conditional about Jenny's misery became A (p. 30).
- TFL takes this idea "absolutely ruthlessly" (p. 30). Its basic building blocks are sentence letters, the "atomic" sentences, written as single uppercase letters (p. 30).
- There are only twenty-six letters of the alphabet, but there is no limit to the sentence letters we might want, and subscripts give new ones. Five examples: $A, P, P_1, P_2, A_{234}$ (p. 30).
- A symbolization key pairs letters with English sentences, e.g. A: It is raining outside; C: Jenny is miserable (p. 30). This is not fixed once and for all: for the time being the letters symbolize those sentences. A new key can be given for new arguments, e.g. A: Jenny is an anarcho-syndicalist; C: Dipan is an avid reader of Tolstoy (p. 31).
- Whatever structure an English sentence has is lost when it is symbolized by a letter. From TFL's viewpoint a letter is just a letter. It can build more complex sentences but cannot be taken apart (p. 31).
- *Intuition note:* A sentence letter works like a sealed box. TFL sees only the label on the box, not the sentence inside.

## Toy example (ours, not from the text)
Argument: Mina plays chess; if Mina plays chess, then Omar is happy; therefore Omar is happy.
- Key: A: Mina plays chess; C: Omar is happy.
- Symbolized pattern: A; if A then C; ∴ C, the same as the Jenny pattern (p. 27).
- New key: A: The tea is hot; C: The cup is full. This yields a different argument with the same pattern.
- Check with the ordinary reading of "if…, then…" (ours): for the pattern to fail we would need A true, "if A then C" true and C false. But if A is true and C false, "if A then C" is false. So there is no such case, whichever key is used.
- Contrast: the argument from Mina being a vixen to Mina being a fox would be symbolized with two unrelated letters, say V and F. The letters hide the meaning link between "vixen" and "fox", so the letter pattern V; ∴ F does not show why it is valid (cf. p. 29–31).

## Concepts
- [[validity / soundness]] — an argument is valid if the premise(s) cannot be true while the conclusion is false (as described for the vixen example); this unit does not define it afresh (p. 29)
- [[validity in virtue of form]] (new) — validity that comes from the argument's pattern, not from the content words (p. 28)
- [[logical form vs. grammatical form]] — the pattern revealed by replacing subsentences with letters; these pages do not discuss grammatical form (p. 27–28, 30)
- [[truth-functional logic (TFL)]] (new) — the formal language built in parts II–IV, also called propositional or sentential logic (p. 29)
- [[conceptual validity]] (new) — validity from word meaning or concept relations, not from form (p. 29)
- [[sentence letter / atomic sentence]] (new) — an uppercase letter, possibly subscripted, that cannot be taken apart (p. 30–31)
- [[symbolization key]] (new) — a temporary list pairing letters with English sentences (p. 30)

## Canonical instances
- [[jenny-raining-modus-ponens-pattern]] (new) — rain/Jenny and Tolstoy/Dipan share the form A; if A then C; ∴ C (p. 27)
- [[vixen-fox]] (new) — valid, but not by form (p. 29)
- [[green-red-sculpture]] (new) — seems valid because nothing can be both green and red all over; the same-form "shiny" variant is invalid (p. 29–30)

## Bridges (candidates)
- [structural-analogy] sentence letters hiding inner structure ↔ programming: abstraction of a function's inner workings behind a name — a letter exposes only how it is used.
- [metaphor] swapping content words while the pattern stays ↔ algebra: substituting values for variables, which keeps the equation's form.

## Questions this raises
- How can we tell whether a pattern such as "A or B; not-A; ∴ B" is valid for every filling-in?
- What exactly are "and", "or", "not" and "if…then" doing, and how does TFL treat their meanings?
- Is the vixen/fox case really different in kind from form-based validity, or could a richer formal language capture it?
- What is lost when a sentence's internal structure disappears into a letter?

## Reading notes
- Printed page = pdf − 10 (pdf 37–41 = printed 27–31).
- The text on these pages is plain prose. No equations in this unit beyond the example letters.
- Section 4.3 (p. 30) refers to the rain example as belonging to "this section", but that example is in section 4.1 (p. 27); this looks like a wording slip.
- No exercises appear in these pages.
