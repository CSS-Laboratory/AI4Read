# Review of English pack /2 · 2026-10-llm-next-word

Reviewer: independent (did not write the pack). Date: 2026-10-26.
Scope: `posts/2026-10-llm-next-word/english/english.json` against `src/content.html` (mainly "So what does it know?", Lens 1, Lens 4 and Lens 5), WRITING.md §8 and §9, the Margin request, and the calibration review `posts/2026-10-ai-finance/review/english-packs-check.md`. No file other than this one was edited.

Levels are my estimates in the style of the English Vocabulary Profile (EVP) and English Grammar Profile (EGP). I have no live access to either, so verify the flagged ones.

`python3 scripts/english_pack.py posts/2026-10-llm-next-word --check` passes on the current pack: passage 184 words, 12 sentences, core 73 words; 8 expressions, 3 patterns, 4 fixes, 1 tip.

I tested every replacement below on a scratch copy of the pack (outside the repo). It passes `--check`: passage 190 words, 12 sentences, core 80 words; 8 expressions, 2 patterns, 4 fixes, 1 tip. The sentence count and the fix indices are unchanged.

## Counts

| | critical | major | minor |
|---|---|---|---|
| Passage | 0 | 2 | 6 |
| Expressions | 0 | 0 | 2 |
| Patterns | 0 | 3 | 0 |
| Fixes | 0 | 2 | 1 |
| Gist and retell | 0 | 0 | 2 |
| Tip / pack shape | 0 | 0 | 1 |
| **Total** | **0** | **7** | **12** |

No item misreports the post. The passage is faithful in structure and keeps its hedges. All the major findings are about level, a stronger claim, or a listener who cannot follow.

---

## 1. Passage

Strengths: it is natural spoken British English, with no British-spelling problems. Sentence rhythm is good for shadowing, with no tongue-twisters and short sentences before the long ones. Core sentences 7 to 10 (jury, pause, same token, tantamount, in and of itself) are the right ones to memorise: they hold the contested-minds point and the thesis that loss cannot tell you the kind of knowledge.

### Major

**P1. Sentence 7: "As for minds, the jury is still out." A listener cannot tell what "minds" means.** (major, listener)
- *Problem.* The post's fourth layer is theory of mind, meaning tracking what other people believe. The passage never says so. A listener who has not read the post hears "minds" and "Many tests are passed" with no idea what is being tested. Sentence 7 is also a core sentence.
- *Fix.* Replace sentence 7 with: "As for minds, that is, tracking what people believe, the jury is still out." This costs 6 words; with the changes in P2 and P3 the total is exactly 190. The "that is," keeps the anchor "the jury is still out" intact.

**P2. Sentence 11: "To tease apart the kinds, you have to change the test in small ways and see what breaks." This turns the post's "or" into "only".** (major, stronger claim)
- *Problem.* The post says: "you have to change the test in small ways and see what breaks (Ullman's method), *or look inside at the relations the model has built* (Piantadosi and Hill's suggestion)". The passage keeps "you have to" and drops the alternative, so Ullman's method becomes the only route. That is a stronger claim than the post makes.
- *Fix.* "You can tease apart the kinds by changing the test in small ways and seeing what breaks." "You can" permits the method without making it the only one. The anchor "tease apart" survives. Update gist 2 and the model answer (section 4).

### Minor

**P3. Sentence 9: "Yet people fail some of those changes too, so if a failure counts against the model, then by the same token it counts against us."** (minor)
- *Problem 1.* People fail *tests*, not "changes". The post writes "Humans fail some of those changes too", but spoken English needs a different noun.
- *Problem 2.* The conditional reasoning (a failure counts against us too) is not in the post. The post only reports the fact and the Kosinski/Ullman disagreement about whether one failure decides. It is a conditional and asserts nothing new, so it passes under §9, but it is the speaker's inference. The brief's line "Humans fail some of those changes too" is all the post says.
- *Problem 3.* "Counts against us" does not say what is counted against us.
- *Fix.* "Yet people get some of those altered tests wrong too, so if a failure counts against the model, by the same token it counts against us." The "then" is dropped to keep the passage inside 190 words. If you want it labelled as ours, add "on our reading" and cut elsewhere (see P6).
- *Check.* The proposed text passes `--check` at 190 words. The anchor "by the same token" survives.

**P4. Sentence 4 and 5 vs the post: "his theory sidesteps the question of meaning".** (minor)
- *Problem.* The post says Shannon sets meaning aside and calls it "irrelevant to the engineering problem". "Sidesteps" can sound as if he dodged an awkward issue. The calibration review raised the same point. It is acceptable and the item is correct as a headword, so I leave it.
- *Optional fix.* None required.

**P5. "Shannon" is not introduced.** (minor, listener)
- *Problem.* "Knowledge in Shannon's sense" is hard to follow cold. "Claude Shannon's sense" would help, but the passage is already at 190 words with the P1 and P3 changes, so it needs a cut elsewhere. Left as optional.

**P6. Word budget.** (minor)
- *Problem.* The recommended passage is exactly 190 words, the upper limit. Any addition (for example "Claude", "on our reading") needs an equal cut.
- *Fix.* If you add words, shorten sentence 4 or sentence 10 and re-run `--check`.

**P7. Sentence 10: "A low loss is not tantamount to understanding."** (minor, faithfulness)
- *Problem.* The post never uses "understanding" for the loss; it says the loss "tells you how much a model knows about text" but "cannot tell you what kind of knowledge that is". The sentence is consistent with that, and "not tantamount to" claims only non-equivalence, but the post's "how much" half never appears in the passage.
- *Fix.* No change required. If you want it fuller, the model answer (section 4) now supplies the "how much" half.

**P8. Sentence 8: "Many tests are passed".** (minor, spoken style)
- *Problem.* The bare passive is lifted from the post's list. Spoken English would say "Models pass many tests". It is not wrong, and changing it costs nothing in words, but "Many tests are passed" is a little written.
- *Optional fix.* "Models pass many tests, but small changes often break the result, which should give us pause." This is the same word count (+1: "Models pass" for "are passed" is 1 word more). Skip if the budget is tight.

---

## 2. Expressions

All eight are C1 or C2 in my estimate, all occur naturally in the passage, and the headwords match pack 1, so the externalIds survive. Definitions, parts of speech and second contexts are sound. Second contexts are in the same sense as the passage and make no claim about a named source. None copies a passage sentence.

### Minor

**E1. "to be tantamount to": definition.** (minor)
- *Problem.* "usually something stronger or worse" is awkward. The point is that the second thing is typically more serious or negative (tantamount to treason). The passage uses it with a positive noun ("understanding"), which is fine but not the typical case.
- *Replacement JSON field:* `"definition": "to be virtually the same as something else, in effect; the second thing is usually more serious or negative"`

**E2. Thin margin.** (minor)
- *Problem.* The pack has exactly 8 expressions, the minimum. If any one is dropped after another review, the pack fails the 8 to 12 rule. If the passage ever has room for a ninth natural C2 item (not forced), add it. Nothing here needs forcing.

Level notes: *in and of itself* (C1) and *tease apart* (C1) might be C2 in EVP, but both pass the rule either way. *stand or fall on*, *the jury is still out*, *give someone pause*, *by the same token*, *tantamount*, *sidestep* are fairly C2. No expression is B2 or below.

---

## 3. Patterns

### Major

**PT1. "Double superlative range (from the most X to the most Y)" (C1).** (major, level)
- *Problem.* A superlative inside a from...to range is built from B1 material (*the most + adjective*, *from ... to*). Nothing in the structure is C1.
- *Fix.* Remove it. Replace with the item in PT4 below.

**PT2. "As for + topic" (C1).** (major, level)
- *Problem.* "As for" is a topic-shift marker that sits at B2 in EVP/EGP style grading (I believe EVP lists it at B2). It is useful but not a C1 pattern.
- *Fix.* Remove it. Replace with the item in PT5 below. The phrase stays in the passage; it just stops being a taught pattern.

**PT3. "Sentential relative clause (, which ...)" (C1).** (major, level)
- *Problem.* Non-defining *which* referring to a whole clause ("He failed, which surprised us") is B2 or lower in EGP. It also duplicates fix 3 (which versus that), which is B2 as well.
- *Fix.* Remove it. Two patterns remain after the two replacements below, which is the minimum (2 to 4).

### Replacement patterns (JSON for `items`, replacing the three above)

```json
{
  "kind": "pattern",
  "headword": "Inversion after a fronted ordinal (First come X, next comes Y)",
  "level": "C1",
  "definition": "Put an ordinal or sequencing word first and the verb before its subject, so the list reads as a sequence: 'First come bits about text'. The verb agrees with the subject that follows, not with the fronted word.",
  "anchor": "First come bits about text",
  "sentence": "First come the interviews; next comes the coding, and only then the analysis.",
  "target": "First come the interviews; next comes the coding"
},
{
  "kind": "pattern",
  "headword": "Nominal clause 'what you take X to be'",
  "level": "C1",
  "definition": "'What you take X to be' asks for the speaker's view of X's nature and fits after 'depends on' or 'stands or falls on': 'Whether A is true stands or falls on what you take B to be'.",
  "anchor": "what you take meaning to be",
  "sentence": "Whether the corpus is representative depends on what you take the target population to be.",
  "target": "what you take the target population to be"
}
```

Both anchors lie inside one sentence (sentence 3 and sentence 6) and are found by the builder. The second pattern's level is the weaker call: a *take + object + to be* complement inside a wh-clause is plausibly C1 in EGP, but check it. The first is a fairly safe C1 to C2 (fronted-element inversion with plural agreement). The two example sentences are my own, and make no claim about a named source.

---

## 4. Fixes

### Major

**F3. "which, not that, after a comma" (C1).** (major, weak fix)
- *Problem.* That versus which in a non-defining clause is a B1 to B2 relative-pronoun contrast, which the brief rules out. Few C1 writers write ", that should give us pause".
- *Fix.* Replace with an error C1 writers do make: an article added to a fixed idiom. Anchored on sentence 8, which is unchanged.

**F4. "no inversion in an embedded question" (C1).** (major, weak fix)
- *Problem.* Inversion in an embedded question ("what kind of knowledge has the model") is a B1 to B2 error, and the wrong sentence is not something a C1 writer would produce.
- *Fix.* Replace with subject-verb agreement after inversion, which is a real C1 slip, ties to the new inversion pattern, and is anchored on sentence 3 (unchanged).

### Replacement JSON (replace the two fixes above)

```json
{
  "kind": "fix",
  "headword": "verb agrees with the subject after inversion",
  "level": "C1",
  "anchorSentence": 3,
  "wrong": "First comes bits about text, which are measurable.",
  "definition": "After a fronted 'First' or 'Next', the verb still agrees with the subject that follows: 'First come bits', but 'Next comes structure'."
},
{
  "kind": "fix",
  "headword": "no article in 'give someone pause'",
  "level": "C1",
  "anchorSentence": 8,
  "wrong": "Many tests are passed, but small changes often break the result, which should give us a pause.",
  "definition": "In the idiom 'give someone pause', 'pause' takes no article; 'a pause' means a short break in time or speech."
}
```

Each `wrong` has exactly one error ("comes" for "come"; "a pause" for "pause"). The `right` text is the passage sentence. The order of fixes in the file should be by sentence index: 3, 4, 6, 8.

### Minor

**F1. "no article with uncountable abstract noun": rule wording.** (minor)
- *Problem.* "Knowledge is uncountable: no 'a'" is too absolute: "a good knowledge of French" and "a working knowledge of" are standard. The error in `wrong` is still an error ("That is a knowledge in Shannon's sense" has no modifier and no "of"). Also, "a knowledge" is on the easier side for C1, but the brief names uncountables, so I keep it.
- *Fix (definition only).* `"definition": "'Knowledge' is uncountable and takes no 'a' or plural in general use. 'A knowledge of X' is possible only with a modifier ('a working knowledge of X'). Say 'knowledge' or 'a piece of knowledge'."`

**F2. "whether, not if, in a subject clause".** (no finding)
- Sound: one-word error, accurate rule, real C1 slip.

---

## 5. Gist and retell

Gist 1 is answerable from the passage alone, by order: the four layers are named in sequence, and the speaker says they run from most certain to most contested, so the last (minds) is the most contested. Meaning is the third layer by position only. This is acceptable.

Gist 2 needs updating after P2.

### Minor

**G1. Gist 2 answer.** (minor, follows P2)
```json
{
  "question": "What does a low loss not tell you, and how can you find out more?",
  "answer": "It does not tell you what kind of knowledge the model has. One way to find out is to change the test in small ways and see what breaks."
}
```

**G2. Retell model answer.** (minor)
- *Problem.* The old answer says "have anything like a mind", which blurs the post's layer (tracking what other people believe), and it says "you change the test" as the only route. Its first sentence also adds "how much a model knows about text", which is faithful to the post but not to the passage.
- *Fix.* The new answer keeps all three mustUse expressions ("in and of itself", "to tease apart", "the jury is still out") and matches both the post and the revised passage:
```json
"modelAnswer": "A low loss, in and of itself, tells you how much a model knows about text, but not what kind of knowledge it is. One way to tease apart the kinds is to change the test in small ways and see what breaks. On whether models can track what people believe, the jury is still out."
```
The mustUse strings match the headwords exactly; keep them as they are.

---

## 6. Tip

### Minor

**T1. "Loop the four core sentences ... the expressions will come with them".** (minor)
- *Problem.* The core sentences (7 to 10) carry five of the eight expressions (jury, pause, same token, tantamount, in and of itself). "stand or fall on", "sidestep" and "tease apart" are outside the core. "The expressions" overstates.
- *Fix.* `"sentence": "Loop the four core sentences until you can say them without the text; five of the pack's expressions will come with them, already in a natural rhythm."`

---

## Revised passage (for the author to apply)

```json
"text": "A language model is trained to do one job: guess the next piece of text. It is scored by its loss, which measures how closely those guesses match real text. What it knows comes in four layers, from the most certain to the most contested. First come bits about text, which are measurable. That is knowledge in Shannon's sense, and his theory sidesteps the question of meaning. Next is structure, such as grammar, and that is well supported. Whether the model grasps meaning stands or falls on what you take meaning to be. As for minds, that is, tracking what people believe, the jury is still out. Many tests are passed, but small changes often break the result, which should give us pause. Yet people get some of those altered tests wrong too, so if a failure counts against the model, by the same token it counts against us. A low loss is not tantamount to understanding, and in and of itself it cannot tell you what kind of knowledge the model has. You can tease apart the kinds by changing the test in small ways and seeing what breaks."
```

Checked: 190 words, 12 sentences, `core: [7, 8, 9, 10]` is 80 words. All eight expression anchors still match: "stands or falls on", "the jury is still out", "give us pause", "by the same token", "tantamount to", "in and of itself", "tease apart", "sidesteps the question". Because the passage text changes, any existing passage audio is stale (the text hash will catch it): re-record with `tts_english_passage.py` before building.

Faithfulness against the post's synthesis, sentence by sentence: layers in the post's order; "certain and measurable", "well supported", "depends on your theory", "contested" all kept; "Many tests are passed, but small changes often break the result" and "Humans fail some of those changes too" kept; "how much ... what kind" kept; "change the test in small ways and see what breaks" kept (now as one route, not the only one).

## Summary of what to change

| ID | Where | Severity | Action |
|---|---|---|---|
| P1 | Passage S7 | major | Explain "minds" |
| P2 | Passage S11 | major | "You can ...", not "you have to" |
| PT1 | Pattern: double superlative | major | Replace with fronted-ordinal inversion |
| PT2 | Pattern: As for | major | Replace with "what you take X to be" |
| PT3 | Pattern: sentential which | major | Remove |
| F3 | Fix: which/that | major | Replace with "give us a pause" fix |
| F4 | Fix: embedded inversion | major | Replace with agreement-after-inversion fix |
| P3 | Passage S9 | minor | "get ... wrong", drop "then" |
| P4 | S4 "sidesteps" | minor | No change |
| P5 | "Shannon" unintroduced | minor | Optional, needs a cut |
| P6 | Word budget at 190 | minor | Note |
| P7 | S10 "understanding" | minor | No change |
| P8 | S8 passive | minor | Optional |
| E1 | tantamount definition | minor | New definition |
| E2 | Only 8 expressions | minor | Note |
| F1 | Uncountable rule | minor | New definition |
| G1 | Gist 2 | minor | New answer |
| G2 | Retell model answer | minor | New answer |
| T1 | Tip | minor | New sentence |


---

## Response (2026-10-26)

Applied to `english.json`. `--check`: source OK, passage 190 words, 12 sentences, core 80 words; 9 expressions, 2 patterns, 4 fixes, 1 tip. Passage text changed, so the audio must be re-recorded.

| ID | What changed |
|---|---|
| P1 | Sentence 7 now reads "As for minds, that is, tracking what people believe, the jury is still out." The post defines theory of mind as thinking about what other people believe (Lens 5). |
| P2 | Sentence 11 now reads "You can tease apart the kinds by changing the test in small ways and seeing what breaks." The post's alternative (look inside) is no longer ruled out. |
| P3 | Sentence 9 now reads "Yet people get some of those altered tests wrong too, so if a failure counts against the model, by the same token it counts against us." "Then" dropped. The conditional is the speaker's inference, as the review notes; it asserts no new fact. |
| P4 | No change (as the review says). |
| P5 | Applied: "Claude Shannon's sense" (the post names him once as Claude Shannon). Paid for with P6 below. |
| P6 | Budget kept at 190: "and that is well supported" became "which is well supported". |
| P7 | No change needed (as the review says). The retell model answer now carries the "how much" half. |
| P8 | Applied: "Models pass many tests, but ..." (same word count). The new `give someone pause` fix (F3) was built on this wording. |
| E1 | `to be tantamount to` definition replaced with the reviewer's text. |
| E2 | Ninth expression added so the pack is not at the floor: `to count against` (C2, my estimate; check it), anchored on "counts against" in sentence 9, with a new second context. It occurs naturally; it is not forced. |
| PT1 | Pattern "Double superlative range" removed. Replaced by "Inversion after a fronted ordinal". |
| PT2 | Pattern "As for + topic" removed. Replaced by "Nominal clause 'what you take X to be'" (the weaker level call, as the review says). |
| PT3 | Pattern "Sentential relative clause" removed. Two patterns remain, the minimum. |
| F1 | Definition replaced with the reviewer's wording; `wrong` rebuilt for "Claude Shannon's". |
| F2 | No finding. Kept unchanged. It is the subject-clause use of whether, which is the only form I treat as C1. |
| F3 | Replaced with the "give someone pause" article fix, anchored on sentence 8. |
| F4 | Replaced with the agreement-after-inversion fix, anchored on sentence 3. The definition uses "First comes grammar" as the singular example, so it does not suggest that the passage's "Next is structure" is wrong. Fix order is now by sentence: 3, 4, 6, 8. |
| G1 | Gist 2 answer replaced. |
| G2 | Retell model answer replaced; the three `mustUse` headwords are unchanged. |
| T1 | Tip now says "six of the pack's nine expressions", because the core sentences (7 to 10) hold jury, pause, same token, count against, tantamount and in and of itself. |

Headwords kept unchanged: all eight original expressions and F2's and F1's headwords. Headwords dropped (for the retired list, which I was not asked to edit): the three removed patterns, "which, not that, after a comma" and "no inversion in an embedded question".
