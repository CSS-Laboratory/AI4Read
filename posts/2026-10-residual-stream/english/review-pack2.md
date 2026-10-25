# Review of the passage-centred English pack (schema /2), post 03

Reviewer: independent (did not write the pack). Date: 2026-10-26.
Scope: `posts/2026-10-residual-stream/english/english.json` against `src/content.html`, `numbers.md`, WRITING.md sections 7 to 9, section 8 (pack rules) and `site/mewiki/REQUEST-passage-pack-2026-10-26.md`. `review/english-check.md` was used for calibration. Nothing else was edited.
Levels are my estimates in the style of the English Vocabulary Profile (EVP) and English Grammar Profile (EGP); I had no live access to either. The first run of `python3 scripts/english_pack.py posts/2026-10-residual-stream --check` passes on the current source: passage 190 words, 9 sentences, core 81 words; 10 expressions, 3 patterns, 3 fixes.

Every replacement below was applied to a copy of the pack in the scratchpad and passes the same `--check` (190 words, core 86 words, 10 expressions, 4 patterns, 3 fixes). The passage text changes, so the audio must be re-recorded (the text hash will refuse the old file). Sentence indexes stay 0 to 8, so the fix anchors are unchanged.

## Counts

| critical | major | minor |
|---|---|---|
| 0 | 6 | 12 |

Major: M1 (sentence 0 scope), M2 (sentence 3 hedge), M3 ("up to (rounding)" level), M4 (fix 2 is a trick), M5 ("tantamount" second context), M6 (retell does not elicit "hinge on").
Nothing misreports the post. The passage keeps the key hedges: a probe score shows only that information is present, the algebra does not say what a score means, and "concepts are directions" is scoped to a trained language model's stream.

---

## 1. Passage

Faithful on the points the earlier rounds cared about (see above). Natural British spoken English and British spelling ("behaviour"). No full-stop abbreviations. Sentences 2 and 8 are long for shadowing but still speakable. Two sentences say more or less than the post.

### M1 (major). Sentence 0 states the running sum flatly for "a language model's hidden state"
The post tests the identity only for GPT-2 small, entries 0 to 11, on one prompt in float32. It says "we ran no trained Qwen3, Llama, Gemma or Mistral model", and the library's last entry "is not a stream vector". Sentence 0 gives the claim without scope, and sentence 2 then contradicts it for the last entry. The post itself labels its short answer "our reading, not a finding". Replacement for sentence 0 (+3 words, "On our reading,"):

> On our reading, every attention and MLP part adds its write to one shared list, so a language model's hidden state is a running sum.

### M2 (major). Sentence 3: "To a first approximation" hedges the wrong thing
The post says the read is exact: "All this is exact arithmetic", and "It is exact in the account Elhage and colleagues give, which says: We also ignore layer normalization". The departure in real models is the norm that comes before each read. The passage hedges the dot-product claim itself, which clashes with sentence 8 ("firm ground with the arithmetic"). Name the departure; the headword stays. Replacement for sentence 3 (the full text below stays at 190 words):

> To a first approximation, norm aside, a read is a dot product with that sum, so it splits into one share per writer, and a writer at right angles goes unheard.

(The phrase "norm aside" also supports the new pattern m8 below.)

### Minor passage points
- **m1. A listener who has not read the post meets "probe" and "steering push" undefined.** Sentence 4: "A probe is such a read" is true only of the linear probe the post uses. Replace with "A linear probe is such a read, and a high score shows only that information is present." I could not afford a gloss for "push" within 190 words; I cut "by the same amount" (redundant with "in lockstep") and let the retell and gist carry it. If a gloss is wanted, the cost is about +6 words ("A steering push, which adds one vector to every list, ...") and one other cut.
- **m2. "Up to rounding" has no frame.** There is no number, so section 7 does not force it, but a listener cannot tell that it is one short prompt, float32, GPT-2 small, entries 0 to 11. Sentences 1 and 2 together carry "GPT-2 small" and the last-entry exception; that is enough for a talk. Optional, if words allow: "a notebook run on GPT-2 small bears it out".
- **m3. "our three sources" (sentence 8) is undefined for a listener.** Left as it is, because the post introduces them as a set. "give" is a slightly odd verb for tests (provide, supply); it echoes the post's "give no test". Keep.
- **m4. Core sentences.** [0, 3, 5, 7] is fine (86 words with the changes). Sentence 3 is the longest core sentence (31 words). If Kunhao finds it too heavy to memorise word for word, [0, 4, 5, 7] gives 72 words but sentence 4 depends on "such a read". Leave as is.

Full replacement of `passage.text` (190 words, 9 sentences; sentence 2 is shortened to "the library's last entry" only to stay within 190, and the original "the last entry a library returns" is clearer if a word can be found elsewhere):

```json
"text": "On our reading, every attention and MLP part adds its write to one shared list, so a language model's hidden state is a running sum. In our toy that is true by construction, and a notebook on GPT-2 small bears it out, up to rounding. Names can mislead: the library's last entry, having been through the final norm, is a case in point, and is not to be taken at face value. To a first approximation, norm aside, a read is a dot product with that sum, so it splits into one share per writer, and a writer at right angles goes unheard. A linear probe is such a read, and a high score shows only that information is present. To say the model therefore uses it would be tantamount to confusing seeing with doing. A steering push shifts every score in lockstep. What a score means, or whether a push changes behaviour, the algebra does not say. Whether concepts are directions in a trained language model's stream hinges on tests that our three sources do not give, so we are on firm ground with the arithmetic, not the interpretation."
```

---

## 2. Expressions and patterns

| Item | Level | Fit in passage | Definition | Second context |
|---|---|---|---|---|
| by construction | C1 ok (see m5) | correct | accurate | natural, same sense |
| to bear out | C2 ok | correct ("bears it out") | accurate | m6 |
| up to (rounding) | not supportable | correct | loose | natural, same sense |
| a case in point | C1 ok | correct | accurate | natural |
| to take something at face value | C1 ok | correct | accurate | natural |
| to a first approximation | C1 ok | see M2 | accurate | natural |
| in lockstep | C1 ok | correct | accurate | natural |
| to be tantamount to | C2 ok | correct | accurate | M5 |
| to hinge on | C1 ok | correct | accurate | natural |
| to be on firm ground | C1 ok | correct | accurate | natural |
| Fronted wh-clause object | C2 ok | correct | accurate | natural |
| Whether-clause as subject | C1, borderline (m7) | correct | accurate | natural |
| Perfect participle clause | C1 ok | correct; the participle's subject matches the main subject | accurate | natural |

### M3 (major). "up to (rounding)": the level cannot be supported from EVP or EGP, and the headword is awkward
The sense is the mathematical "equal up to X" (as in "up to isomorphism"): X is ignored. It is useful in Kunhao's field and the passage uses it correctly. But every word is A2 to B1, the sense is not an EVP entry at any level, and a C1/C2 label would not survive an EVP check. The parenthesis in the headword is also awkward (the `externalId` becomes `up-to-rounding`). The definition's "or choice" is vague.
Recommended: replace it with an expression that is graded C1/C2, occurs in the passage, and is more transferable, "to go unheard" (the same family as "go unnoticed" or "go unchecked"; EVP lists the latter near C2). The phrase "up to rounding" stays in the passage unannotated.

```json
{
 "kind": "expression",
 "headword": "to go unheard",
 "level": "C2",
 "partOfSpeech": "verb phrase",
 "register": "neutral/formal",
 "definition": "to exist or be said without being noticed, taken into account or dealt with",
 "anchor": "goes unheard",
 "sentence": "If we only report the majority label, the minority view among the coders goes unheard.",
 "target": "goes unheard"
}
```

If Kunhao wants to keep "up to rounding" for his own writing, the honest options are (a) a tip, with no level, or (b) keep it as C2 and say in `note` that the level is a technical-register judgement, not an EVP entry. Option (a):

```json
{
 "kind": "tip",
 "headword": "Equal up to something",
 "sentence": "In research English, 'X equals Y up to Z' means they are the same except for Z, which you choose to ignore: up to rounding, up to a relabelling of the categories, up to a constant."
}
```

### M5 (major). "to be tantamount to": the second context is unnatural
"Tantamount to claiming an experiment we never ran": you report or claim the results of an experiment; you cannot claim an experiment. Replace:

```json
"sentence": "Treating a correlation as a mechanism would be tantamount to reporting an experiment we never ran."
```

### Minor expression and pattern points
- **m5. "by construction" (C1).** A mathematical idiom whose words are B2; not an EVP entry, but it carries a meaning that cannot be guessed from the words, and it reads as C1 in academic writing. Keep. Definition and second context are fine.
- **m6. "to bear out" second context.** "Bears out the original estimate" is slightly loose: *bear out* takes a claim, finding, view or suspicion. Replace with "If the replication bears out the original finding, we can report the effect with more confidence."
- **m7. "Whether-clause as subject" (C1).** Borderline B2 in EGP style (a *whether* clause as subject is taught late B2). It is defensible at C1 because of the *whether*-not-*if* contrast, which is the common error (fix M4 below). Keep, but do not count on it alone for the C1/C2 spread.
- **m8. Add a pattern that the revised sentence 3 makes available and that is clearly C1/C2** (allowed up to 4 patterns; the pack then has 4): the absolute phrase "Noun + aside".

```json
{
 "kind": "pattern",
 "headword": "Noun + aside (absolute phrase)",
 "level": "C1",
 "definition": "A noun followed by 'aside' (or 'apart') opens a sentence as a short phrase meaning 'if we set that to one side': 'Norm aside, a read is a dot product'. It is formal, takes no verb, and the noun names the thing being set aside.",
 "anchor": "norm aside",
 "sentence": "Sampling error aside, the two surveys tell much the same story.",
 "target": "Sampling error aside"
}
```

- **m9. "in lockstep".** The register "neutral/journalistic" is fine. After my cut of "by the same amount", the passage sentence is "shifts every score in lockstep", which is the most typical use.

Not changed (checked, correct): the fronted wh-clause definition ("no pronoun is added" is accurate); the perfect participle definition; the "hinge on" and "on firm ground" second contexts make no claim about a named source.

---

## 3. Fixes

Each current `wrong` has exactly one error and each `right` equals its passage sentence.

| Current fix | Verdict |
|---|---|
| tantamount to + -ing (S5) | Keep. A real slip, with a rule that generalises. Reword the rule (m10). |
| no pronoun after a fronted object (S7) | Replace (M4). |
| firm ground, no article (S8) | Keep, reword the rule (m11). |

### M4 (major). Fix 2 ("the algebra does not say it") is a trick
It only arises when a writer fronts an object, which C1 writers rarely do, and it duplicates the pattern item it comes from. A better C1 error, built on passage sentence 8, is the one the Whether-clause pattern guards against: *if* for a subject clause. It is common in academic writing by East Asian-language writers (是否, 〜かどうか written as "if"), has one clear rule, and is useful in a methods or limitations section. Replace with (anchorSentence 8):

```json
{
 "kind": "fix",
 "headword": "whether (not 'if') for a subject clause",
 "level": "C1",
 "anchorSentence": 8,
 "wrong": "If concepts are directions in a trained language model's stream hinges on tests that our three sources do not give, so we are on firm ground with the arithmetic, not the interpretation.",
 "definition": "A clause that is the subject of a sentence begins with 'whether', not 'if'. 'If' introduces conditions and object clauses (we do not know if/whether it works), but not a subject: 'Whether it works hinges on ...'."
}
```

Both this and the firm-ground fix use sentence 8, but they test different rules. If a different sentence is wanted for variety, "taken in face value" (S2, preposition in a fixed phrase) is a one-error alternative.

### m10. Fix 1 rule: generalise
The `wrong` sentence and the rule are accurate. Make it transfer beyond *tantamount*:

```json
"definition": "Here 'to' is a preposition, not part of an infinitive, so a verb after it takes -ing: tantamount to confusing, not tantamount to confuse. The same holds for amount to, committed to, object to and in addition to."
```

### m11. Fix 3 rule: too absolute
"Ground is uncountable and takes no article" overstates: *the ground* and *a ground for* exist in other senses. Reword:

```json
"definition": "In the idiom 'on firm ground' (also 'on solid ground') there is no article: 'on firm ground', not 'on a firm ground'. Adding 'a' is a common slip."
```

Other candidates I considered and did not choose, because their `wrong` is ambiguous or the contrast is B1/B2: "an information" (B1), "bears out it" (B2 particle placement), "in first approximation" (two changes), a tense change in "bears it out" (not clearly wrong).

---

## 4. Gist and retell

- **Gist 1** ("Why is a model's hidden state described as a running sum?") is answerable from sentence 0 alone. The answer is faithful. Keep.
- **Gist 2** (probe score) is answerable from sentences 4 and 5, but the model answer adds "along that direction", which the passage does not say (it is in the post). **m12** replacement answer: "It shows only that the information is present; it does not show that the model uses it."
- **Retell.** The three `mustUse` expressions are in the model answer ("by construction", "tantamount to", "hinges on") and in the pack.

### M6 (major). The retell instruction does not elicit "to hinge on", and the model answer drifts beyond the instruction
The instruction asks for what a hidden state is and what a probe score does and does not show. "To hinge on" belongs to the last sentence of the passage (the open question about concepts as directions), which the instruction never mentions, so a learner has no reason to say it. The model answer then adds that sentence anyway. Replace the instruction, and add the scope phrase to the model answer. The model answer stays within the passage's claims and uses all three expressions.

```json
"retell": {
 "instruction": "In 2-3 sentences, explain to a colleague what a hidden state is, what a probe score does and does not show, and what the open question about concepts depends on.",
 "mustUse": ["by construction", "to be tantamount to", "to hinge on"],
 "modelAnswer": "On our reading, a hidden state is a running sum: every attention and MLP part adds its write, which is true by construction in our toy and holds up to rounding in GPT-2 small, apart from the last library entry. A probe score shows only that information is present, and to say the model uses it would be tantamount to confusing seeing with doing. Whether concepts are directions in a trained language model's stream hinges on tests that our three sources do not give."
}
```

Also replace gist 2's answer as in m12:

```json
{"question": "What does a high probe score show, and what does it not show?", "answer": "It shows only that the information is present; it does not show that the model uses it."}
```

---

## 5. Check run

`python3 scripts/english_pack.py posts/2026-10-residual-stream --check` on the current source: `source OK · passage 190 words, 9 sentences, core 81 words · {'expression': 10, 'pattern': 3, 'fix': 3, 'tip': 0}`.
With every replacement above applied to a scratchpad copy: `source OK · passage 190 words, 9 sentences, core 86 words · {'expression': 10, 'pattern': 4, 'fix': 3, 'tip': 0}`.

Housekeeping if the replacements are accepted: the headword "up to (rounding)" (`ai4read:2026-10-residual-stream:up-to-rounding`) and the headword "no pronoun after a fronted object" are new in this pack, so they do not need an entry in `site/mewiki/packs/retired-<date>.json`. All other headwords are unchanged, so their `externalId`s and review history survive.

## Summary of every change, in one place

1. `passage.text`: replace as in section 1 (M1, M2, m1).
2. Expression "up to (rounding)": replace with "to go unheard" (M3), or demote to a tip.
3. "to be tantamount to": new second-context sentence (M5).
4. "to bear out": second-context sentence "original finding" (m6).
5. Fix 2: replace with the "whether, not if" fix (M4). Fixes 1 and 3: new `definition` text (m10, m11).
6. Optional new pattern "Noun + aside" (m8).
7. `retell.instruction` and `modelAnswer` (M6); gist 2 answer (m12).
8. Re-record the audio.


---

## Response (2026-10-26)

Applied to `english.json`. `--check`: source OK, passage 190 words, 9 sentences, core 86 words; 10 expressions, 4 patterns, 3 fixes. Passage text changed, so the audio must be re-recorded.

| ID | What changed |
|---|---|
| M1 | Sentence 0 now opens "On our reading,". |
| M2 | Sentence 3 now reads "To a first approximation, norm aside, a read is a dot product ...". |
| M3 | Expression `up to (rounding)` replaced by `to go unheard` (C2, my estimate; check it). "Up to rounding" stays in the passage unannotated. I did not add the optional tip. |
| M4 | Fix `no pronoun after a fronted object` replaced by `whether (not 'if') for a subject clause`, anchored on sentence 8, labelled C1. Per the "whether, not if" caution, it is the subject-clause form only: the definition does not mention indirect questions, and says "if" opens a condition, never a subject clause. The pattern "Whether-clause as subject" (C1) is unchanged. |
| M5 | `to be tantamount to` second context now "reporting an experiment we never ran". |
| M6 | Retell instruction and model answer replaced; the instruction now asks what the open question about concepts depends on, which elicits `to hinge on`. |
| m1 | Sentence 4 now "A linear probe is such a read". Nanda's glossary, quoted in the post, calls a probe a "1D linear map", so "linear" is the post's. "By the same amount" was cut from sentence 6, as the review did. |
| m2 | Not applied (optional; no word budget). |
| m3, m4 | No change (as the review says). Core stays [0, 3, 5, 7]. |
| m5, m9 | No change (as the review says). |
| m6 | `to bear out` second context now "original finding". |
| m7 | Kept `Whether-clause as subject` at C1 (subject-clause form only). |
| m8 | Pattern `Noun + aside (absolute phrase)` added (C1), anchored on "norm aside" in sentence 3. |
| m10 | Fix 1 rule replaced. |
| m11 | Fix 3 rule replaced. |
| m12 | Gist 2 answer replaced. |

Headwords kept unchanged: nine of the ten expressions, the four patterns that existed or were added, and fixes 1 and 3. Headwords dropped (for the retired list, which I was not asked to edit): `up to (rounding)` and `no pronoun after a fronted object`, both new in this pack.

---

## Round 2 (independent reviewer, 2026-10-26)

Fresh reviewer; did not write the pack or the round-1 review. Checked `english.json` against `src/content.html` (sections 3 to 7, the short answer (a) to (c), Lens 1 "Seeing is not doing"), WRITING.md §8 and §9 and the Margin request. Levels are estimates in EVP/EGP style. Only this file was edited.

`python3 scripts/english_pack.py posts/2026-10-residual-stream --check`: source OK · passage 190 words, 9 sentences, core 86 words · 10 expressions, 4 patterns, 3 fixes, 0 tips. With R2-1 applied to a scratch copy, the result is the same. None of the findings touches the passage text, so they can be applied after recording.

### Counts

| critical | major | minor |
|---|---|---|
| 0 | 0 | 5 |

### Findings

**R2-1 (minor, faithfulness). Gist 1 answer leaves out the starting list.**
- Answer: "... so the state at any point is the sum of the writes made so far." The post says the list is "the embedding ... plus every earlier write", and the embedding is not a write: the model "keeps one working list for the token, and every attention part ... and every MLP part ... changes it by adding to it". The passage's "adds its write to one shared list" also implies a list that is already there.
- Replacement `answer`: `Because every attention and MLP part adds its write to one shared list, so the state at any point is the starting list plus every write made so far.`

**R2-2 (minor). `to be tantamount to`: definition differs from the same headword in pack 01.**
- In post 01, round 1 (E1) replaced "usually something stronger or worse" as awkward. The same headword should carry the same definition in both packs.
- Replacement `definition`: `to be virtually the same as something else, in effect; the second thing is usually more serious or negative`

**R2-3 (minor). `Noun + aside`: the definition says the phrase "opens a sentence", but the anchor does not.**
- In the passage, "norm aside" comes after "To a first approximation,".
- Replacement `definition`: `A noun followed by 'aside' (or 'apart') makes a short verbless phrase, usually at the front of a clause, meaning 'if we set that to one side': 'Norm aside, a read is a dot product'. It is formal, and the noun names the thing being set aside.`

**R2-4 (minor, usage). `by construction`: the second context is awkward ("denser inside than between").**
- Replacement `sentence`: `In a simulated network, ties are denser within the two communities than between them by construction, because we wrote the generating rule that way.` (the `target` "by construction" is unchanged)

**R2-5 (minor). `note` is out of date.**
- It says "Ten headwords are reused from pack 1 or earlier packs", but `to go unheard` is new (it replaced "up to (rounding)" in round 1). Nine are reused from this post's pack 1.
- Replacement `note`: `Passage-centred pack, C1-C2, British English: a spoken mini-talk on post 03's main answer (the stream as a running sum, reads as dot products, the last library entry, probe versus push, and the limits). Levels are AI4Read estimates in the style of the English Vocabulary Profile and English Grammar Profile. Nine headwords are reused from this post's pack 1; 'to go unheard' is new.`

### Checked with no finding

- Faithfulness. S0 is labelled "On our reading" (the post: "Short answer (our reading, not a finding)"). S1 and S2 keep the GPT-2 small scope and the last-entry exception ("has been through the final norm, so it is the exception"). S3 matches "A part reads the list by dot products, which split into one share per writer (a writer at right angles to the reader goes unheard)". "Norm aside" names the departure ("a rescaling step applied to the stream before each read"). S4 and S5: "A high probe score shows that information is present along a direction, not that later parts of the model use it", under the post's "Seeing is not doing". S6: "every score moves by the same amount". S7 is the post's sentence verbatim. S8 keeps the scope: "For the trained language models people use now, the three sources give no test ... none of the three tests concepts as directions". It does not overreach to "none of the sources" on anything wider. Gist 2 and the retell model answer are faithful.
- Levels. All ten expressions are C1 or C2. The patterns (fronted wh-object C2; whether-clause subject, perfect participle and noun + aside C1) are acceptable; whether-clause and perfect participle are the closest to B2, so verify them if a live EGP check is possible. No item is clearly B2 or below.
- Fixes. Each `wrong` has exactly one error ("tantamount to confuse", "If ... hinges on", "on a firm ground"); all are real C1 errors.
- Usage and spelling. All anchors are natural in the passage. The other second contexts keep the same sense and name no source. Spelling is British ("behaviour"). Cross-post repeats (`to be tantamount to` from post 01, `in lockstep` from post 02) are within the 1 to 2 allowed for spaced review, and both also come from this post's pack 1.

### Round 1 status

Resolved: M1 to M6, m1, m6, m8, m10, m11, m12. Reasonably declined or no change needed: m2, m3, m4, m5, m7, m9.

### Verdict

Ready to record (all five findings are minor and outside the passage text).
