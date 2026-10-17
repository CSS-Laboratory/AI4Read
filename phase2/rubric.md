---
name: phase2-rubric
description: Scoring rubric and error-severity scale used by the pedagogy critic, the fact-checker and the meta-manager for every AI4Read post. Version 1.0, derived from the Test 0 blind judgement and WRITING.md v0.4.
version: 1.0
date: 2026-10-17
---

# AI4Read post rubric (v1.0)

The release gate is: **0 critical errors, 0 major errors, and a score of at least 4 on every criterion.** Each section is scored on its own, and the post score for a criterion is the **minimum** over its sections, not the mean. One weak lens is enough to fail the gate.

## A. Error severity (fact-checker)

| Severity | Definition | Examples from post 01 |
|---|---|---|
| **Critical** | A claim that is false, or that reverses the source, on a point the argument depends on. Also: a citation to a page that does not support the claim at all, or a source that does not exist. | (pre-fix draft) a number taken from a summary line that the paper never reports |
| **Major** | The claim is in the source but is materially changed: a dropped hedge ("suggests" becomes "shows"), a dropped condition the reader needs, a wrong population or scope, a wrong page for a central claim, or our own inference presented as the author's. | "the mask lets each position use its own token" (verify-3); Theorem 1 presented as holding without well-specification |
| **Minor** | Correct in substance, but imprecise: a slightly strengthened word ("reaches" for "approaches in the limit"), a missing attribution (GPT-3 not named), a label slip, a toy whose meaning is ambiguous, a caption that points the wrong way. | Test 0 B-1 (caption direction), B-2 (eq. 1 called Bayes' rule) |

Every finding gives: the quoted text from the post, the source and page, what the source actually says (quoted, at most 25 words), the severity, and a fix in one sentence.

## B. Six criteria (pedagogy critic and judge), each scored 1–5

### 1. Factual accuracy and hedges
- **5:** Every claim is traceable to a page in the verified brief. The authors' hedges are kept, and our own reasoning is labelled "ours". Numbers are rerun in code and match.
- **4:** As 5, with 1–3 minor findings and no major ones.
- **3:** One major finding, or more than 5 minor ones.
- **2:** Several major findings.
- **1:** Any critical finding.

### 2. The ladder for a high-school reader (WRITING §2)
Each new concept follows the ladder: instance → question → mechanism in words → worked numbers → formula → check → what it means.
- **5:** Every new concept has the full ladder. The worked numbers are small enough to do by hand, and there is an explicit check, e.g. "at n = 2 the formula gives 0.941; the table says 0.941". No step needs a later section.
- **4:** Full ladders for the central concepts; a small concept skips the check.
- **3:** Instances and words are there, but the numbers or the check are missing, or the section sends the reader elsewhere for them (Test 0 A: "see rung 8").
- **2:** Abstract definitions first, with the instance last or missing.
- **1:** Jargon without explanation.

### 3. Clarity and English (B2–C1 reader)
- **5:** Short sentences, one idea each. Terms are defined before use with a term box. No internal jargon (e.g. "world W4"). The text reads aloud well.
- **4:** One or two long or dense sentences per section.
- **3:** Dense paragraphs that need rereading, or undefined terms.
- **2–1:** Hard to follow for the target reader.

### 4. Insight and connections (the lenses)
- **5:** Each lens says what it *adds* that the others cannot. It names a link type to other fields (analogy, shared mathematics, mechanism, tension) and states what the lens does **not** explain. The post connects to Kunhao's research (the 3C angle) and to earlier posts.
- **4:** Clear lens contributions; one link or one limit is missing.
- **3:** The lenses are parallel summaries with no comparison.
- **2–1:** A list of facts.

### 5. Illustrations and interactives (WRITING §5)
- **5:** Every mechanism has a figure or an interactive built from the component library, with a JSON config. The widget reproduces the numbers in the text. It works at 375 px and includes an edge case that teaches something (e.g. a prior of 0 never recovers).
- **4:** The main mechanisms are illustrated; a minor mechanism is text only.
- **3:** Some figures are decorative or do not match the text.
- **2:** One figure for the whole post.
- **1:** None.

### 6. Concision
- **5:** Nothing can be cut without loss. Deep material sits in "Look inside" fold-outs.
- **4:** About 10% could be cut.
- **3:** About 20% could be cut, or the same point is repeated.
- **2–1:** Padded.

Concision never outranks criteria 1–2: a missing ladder step is worse than 10% extra length.

## C. Render test (automatic, must all pass)
- The site build (`--site`) runs under the strict CSP with **0 console errors**.
- No horizontal page scroll at 390 px. Long math is in `.mjx` scroll containers.
- Every citation maps to a source entry (`review/cite-map.tsv` has no unmapped rows).
- Every widget's displayed numbers equal the numbers in the text (checked by a Playwright script that reads both).
- The audio script and the chapter IDs match the post sections. The MP3s carry the "AI4Read from CSS Lab" tags.

## D. How the scores are used
- **Writer:** gets the rubric verbatim and self-scores before handing over.
- **Pedagogy critic:** scores blind (without the writer's self-score), section by section, and gives each score below 5 one concrete fix.
- **Meta-manager:** audits 1 post in 3 in full. It reviews the rubric when Kunhao's notes show a problem the rubric did not catch: each such note becomes a new anchor or a new criterion, logged below.

## Change log
- 1.0 (2026-10-17): from the Test 0 judgement (6 criteria), the post 01 fact-check rounds (severity scale) and WRITING.md v0.4.
