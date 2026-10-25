# English pack check: post 03 (2026-10-residual-stream)

Reviewer: independent (did not write the pack). Date: 2026-10-25.
Scope: `posts/2026-10-residual-stream/english/english.json` against `src/content.html`, WRITING.md section 8, and the calibration review `posts/2026-10-ai-finance/review/english-packs-check.md`. Earlier packs were read for headword reuse. No file other than this one was edited or built.

Notes on method:
- I have no live access to the English Vocabulary Profile (EVP) or English Grammar Profile (EGP). Level calls are my estimates in their style. Check the flagged items there before accepting a replacement.
- `site/mewiki/packs/2026-10-residual-stream.md` does not exist yet (only the two earlier packs are built), so I reviewed the JSON directly. `scripts/english_pack.py` was not run. I checked its rules by hand: every target is a substring of its sentence, every fix has `sentence == right` and `wrong != right`, and every loop target is in the loop text.

Severity: **critical** = wrong English taught as correct, or a misreported source. **major** = wrong level under the C1/C2 rule, a misleading rule, a new claim about a source, or the loop failing its brief. **minor** = polish.

## Counts

Pack shape is right: 17 expressions (15-18), 4 patterns, 4 fixes, 2 tips, one loop.

| critical | major | minor |
|---|---|---|
| 0 | 8 | 12 |

Items to replace in full: 4 fixes (fewer/less, affect/effect, number of, orthogonal to), 1 pattern (What matters is), 1 expression (a matter of convention), and the loop. Definition or sentence edits only: mandative subjunctive, to square with, to hold up, to hinge on, a case in point, to be at pains to, to a first approximation, to bear out, perfect participle clause, the retell tip.

Reuse check (item 5): passes. `in lockstep` and `to hinge on` match pack 02, and `to be tantamount to` matches pack 01, headword for headword (case, "to be", spacing). Their `externalId`s will survive. Three rotated items is within the "2-3" rule. No other new headword collides with an earlier pack.

---

## Major

### M1. Fix "fewer vs less" is B1/B2, not C1
Taught in school at B1; EVP lists *fewer* at B1-B2. This is one of the named suspects. The sentence also adds a claim the post does not make (that fewer dimensions than features "cannot give every feature its own perpendicular direction"). Replace with a real C1 slip that uses the post's own wording (see R1 to R4 below).

### M2. Fix "affect vs effect" is B2, not C1
Same problem. Replace.

### M3. Fix "the number of / a number of" is B2, not C1
Same problem. Replace.

### M4. Fix "orthogonal to (not 'with')": level and overclaim
(a) A dependent preposition after an adjective is a B1-B2 topic. (b) The definition says "'Orthogonal with' is not used". That overclaims, because *orthogonal with* does occur, rarely. (c) The sentence "Attention 1 is orthogonal to the reader (1, 2)" is faithful, but the same figure "(1, 2)" is also the embedding in the post, so it is ambiguous out of context. Replace.

### M5. Pattern "What matters is … (pseudo-cleft)" is B2
The basic wh-cleft is B1-B2 in EGP style, and the calibration review made the same call for the same item type. Replace with a C2 fronted wh-clause taken straight from the post (R5).

### M6. Pattern "Mandative subjunctive": the rule is misleading
The definition says formal English uses the bare verb "not 'is run' or 'should be run'". That wrongly bans *should be run*, which is standard British formal English. A learner would "correct" correct writing. Level C2 is fine. Fix the definition and make the target the whole clause (R6).

### M7. Expression "a matter of convention": a new fact about the sources
The sentence says "since the sources give none". The post never says that. It says only "A direction here is an arrow from the origin with length 1 (our convention)", and gives the reason: "So scores from different arrows can be compared." The sentence must not make a claim about the sources that the post does not make. Replace the sentence (R7). The level C1 is borderline (*convention* is C1 in EVP style, the phrase is a transparent collocation); keep it, but check it.

### M8. Loop paragraph: 198 words, and several faithfulness and logic slips
- Length: 198 words against about 150, and 11 targets (the top of the 8-11 range). Trim to 155 words with 9 targets (R8).
- "Every part of the model adds its write": the post says every *attention* and *MLP* part. The embedding, norm and unembedding do not write this way.
- "That much is true by construction in the toy": "that much" has no clear antecedent after the reordered sentence.
- "The last entry … is a case in point:" has nothing for it to be a case in point of, because the preceding sentence is about *other models*, while the last entry is an exception inside GPT-2 small.
- "to take it at face value would be a mistake" is fine, but "it has been normalised" is looser than the post ("it has been through the final norm").
- "A steering push moves every score in lockstep, yet to say …": "yet" signals a contradiction that is not there. The two ideas are parallel (a push shifts scores; a score does not show use). Use "but" or "and".
- "the notebook bears it out on GPT-2 small, where the writes add up to the stream within rounding error" omits that this holds for entries 0 to 11, not the last. The trimmed version says "up to rounding" and gives the last entry its own sentence, which also fixes the case-in-point antecedent.

---

## Minor

**m1. "to square with" (C2).** The sentence says the idea "squares with the toy, where attention 1 is silent to the reader (1, 2)". "Silent to" is unidiomatic (use *inaudible to* or *unheard by*), and the toy fact (a zero share) does not illustrate "hears only the sum" as well as the shares adding up to the direct read does. Replacement in R9.

**m2. "to bear out" (C2).** Usage fine. *Bear out* takes a claim ("bears out the claim that …"), and "bears out the identity" is slightly loose; the post calls it "the identity" and "tests" it. Faithful otherwise (6.2e-6 relative, entries 0 to 11). Optional: "bears out the claim that the writes add up to the stream".

**m3. "to a first approximation" (C1).** The sentence suggests the dot-product read is approximate. In the post the read is exact and linear in the stream; the norm in front of it is the non-linear part. Say that (R10).

**m4. "to pin down" (C1).** Faithful but vague: "until you say where in the model it was read". The post's point is which *entry* of the library's list is the stream (entries 0 to 11, not the last). Optional sharper sentence in R11. Level is safe (likely C2 in EVP).

**m5. "to hold up" (C1).** "The additivity check holds up for GPT-2 small" overstates a little, since the last entry fails. Add "entries 0 to 11" and "trained" (the post ran tiny random Qwen3 and Gemma 3 models, but no trained ones). R12.

**m6. "to rest on the assumption that" (C1).** Faithful (Elhage "assert" an idealised stream, and the post's dot-product advice rests on "no privileged basis"). But the headword is a free combination of B2 words, so the C1 label is weak. Optional swap to *to be premised on* (R13). Keep if the EVP check passes.

**m7. "to be at pains to" (C2).** "At pains to call their three claims speculative" overstates the effort; the post says only that they called them "deliberately speculative". The post does show care elsewhere: the evidence for universality is "anecdotal", with "further work will be needed". Use that (R14).

**m8. "to fall out of" (C2).** Faithful and fine in maths prose. The register is mathematical or informal-technical, not "academic" in the humanities sense. Relabel `register` to "academic/mathematical". Level stays; check EVP.

**m9. "to be on firm ground" (C1).** Fine. The loop uses "on firmer ground", which is not the headword form. Not an error (the target is exact in the text), but note it when building the shadowing card.

**m10. "to hinge on" (C1).** The sentence says whether a probe's direction is used "hinges on tests that this post does not run". The tests do not decide the fact; they decide whether we know it. Better to hinge on something the post says is untested (R15). Headword unchanged.

**m11. "a case in point" (C1).** As a stand-alone sentence it has no antecedent. Give it one (R16).

**m12. Perfect participle clause (C1) and the retell tip.** (a) "(see dangling modifiers)" points to a fix in a different pack, so a learner who opens this pack alone has nothing to look at. Delete it (R17). (b) The tip is titled "Four-step retell" but gives three steps. Rename it (R18). Level C1 for the participle clause is acceptable.

Clean items (no finding): `by construction`, `to carry over (to)`, `to take something at face value`, `in lockstep`, `to be tantamount to`, the "Should" inversion pattern (C2 is plausible; confirm in EGP), and tip 2.

---

## Replacement JSON

Drop each replacement in place of the item with the same position. Where the old item is fully replaced, the old `headword` changes, so its `externalId` changes too. That is intended: the old fixes taught B2 material.

### R1. Fix: whether, not "if" (replaces "fewer vs less")
```json
{
 "kind": "fix",
 "headword": "whether (not 'if')",
 "level": "C1",
 "sentence": "The toy settles that cancellation is possible; it leaves open the question of whether real models cancel writes.",
 "wrong": "The toy settles that cancellation is possible; it leaves open the question of if real models cancel writes.",
 "right": "The toy settles that cancellation is possible; it leaves open the question of whether real models cancel writes.",
 "definition": "After a noun ('the question of') or a preposition ('depends on'), and when the clause is the subject, use 'whether', not 'if'. 'If' belongs to conditions and to casual speech after verbs such as ask or wonder."
}
```
Source: the post says the toy shows cancellation "is possible by arithmetic, not that models do it", and that real cancellation is a hint worded with "may".

### R2. Fix: however is not a conjunction (replaces "affect vs effect")
```json
{
 "kind": "fix",
 "headword": "however (not a conjunction)",
 "level": "C1",
 "sentence": "The sum is exact in the account Elhage and colleagues give, which ignores layer normalisation; however, a real model adds a norm.",
 "wrong": "The sum is exact in the account Elhage and colleagues give, which ignores layer normalisation, however a real model adds a norm.",
 "right": "The sum is exact in the account Elhage and colleagues give, which ignores layer normalisation; however, a real model adds a norm.",
 "definition": "'However', 'therefore' and 'moreover' are adverbs. A comma alone cannot join two main clauses with them (a comma splice). Use a full stop or a semicolon before the adverb and a comma after it, or use a real conjunction such as 'but' or 'although'."
}
```
Source: "It is exact in the account Elhage and colleagues give, which says: 'We also ignore layer normalization.' … Real models add a norm."

### R3. Fix: compare like with like (replaces "the number of / a number of")
```json
{
 "kind": "fix",
 "headword": "compare like with like ('those in')",
 "level": "C1",
 "sentence": "Every coordinate differs, but the dot products in model B are the same as those in model A.",
 "wrong": "Every coordinate differs, but the dot products in model B are the same as model A.",
 "right": "Every coordinate differs, but the dot products in model B are the same as those in model A.",
 "definition": "Both sides of a comparison must be the same kind of thing. Dot products are compared with dot products, not with a model. 'Those in', 'those of', 'that of' and 'the one in' stand in for the repeated noun."
}
```
Source: "Let 'model B' be model A with everything rotated. Every coordinate differs, but every dot product in B equals the one in A."

### R4. Fix: hyphenated number modifiers (replaces "orthogonal to (not 'with')")
```json
{
 "kind": "fix",
 "headword": "a 768-dimensional stream (hyphen)",
 "level": "C1",
 "sentence": "GPT-2 small keeps a 768-dimensional stream for each position.",
 "wrong": "GPT-2 small keeps a 768 dimensional stream for each position.",
 "right": "GPT-2 small keeps a 768-dimensional stream for each position.",
 "definition": "When a number and a noun or adjective modify a following noun, join them with a hyphen and keep any noun singular: a 768-dimensional stream, a 12-block model, a two-word input. After the noun the hyphen goes: the stream has 768 dimensions."
}
```
Source: "GPT-2 small has 768 numbers in it", "the number of entries in it is its dimension", and Nanda's "there is a separate residual stream for each position". If EVP/EGP place this orthographic point at B2, swap it for the "which / that" fix on non-defining clauses at C1 and tell me.

### R5. Pattern: fronted wh-clause (replaces "What matters is … (pseudo-cleft)")
```json
{
 "kind": "pattern",
 "headword": "Fronted wh-clause object (contrast)",
 "level": "C2",
 "sentence": "What a score means, or whether a push changes behaviour, the algebra does not say.",
 "target": "What a score means",
 "definition": "Put a 'what' clause first, as the object of a verb that comes later, to make it the topic: 'What a score means, the algebra does not say.' The rest keeps normal subject-verb order, and no pronoun is added. It sets what is settled against what is not."
}
```
Source: the post's Short answer (b), verbatim. I rate this C2 on the strength of fronted objects in EGP; confirm the band.

### R6. Pattern: mandative subjunctive (definition and target)
```json
{
 "kind": "pattern",
 "headword": "Mandative subjunctive",
 "level": "C2",
 "sentence": "It is essential that the additivity check be run on the model you actually use.",
 "target": "that the additivity check be run",
 "definition": "After words like essential, important, insist or recommend, formal English uses the bare base form: 'that the check be run'. British English also allows 'should be run'; 'is run' is the informal option."
}
```
Source: "Before you trust the additivity of any model, run the check of notebook 02 on it."

### R7. Expression: a matter of convention (sentence)
```json
{
 "kind": "expression",
 "headword": "a matter of convention",
 "level": "C1",
 "partOfSpeech": "noun phrase",
 "register": "academic",
 "sentence": "Giving a direction length one is a matter of convention in this post, chosen so that scores from different arrows can be compared.",
 "target": "a matter of convention",
 "definition": "something decided by agreement, not by necessity"
}
```

### R8. Loop paragraph (155 words, 9 targets)
```json
{
 "headword": "A paragraph to loop",
 "level": "C2",
 "text": "Every attention and MLP part adds its write to one shared list, so the stream is a running sum. In the toy this is true by construction, and the notebook bears it out on GPT-2 small, up to rounding. To a first approximation, a read is a dot product with that sum; the division inside the norm in front of it is not linear. Names can mislead: the last entry of a library's list is a case in point, because it has been through the final norm and should not be taken at face value as a stream vector. The claim that concepts are directions hinges on evidence the sources do not supply, so we are on firmer ground with the arithmetic than with the interpretation. A steering push moves every score in lockstep, but to say that a high score shows the model uses the direction would be tantamount to confusing seeing with doing.",
 "targets": [
  "To a first approximation",
  "by construction",
  "bears it out",
  "a case in point",
  "at face value",
  "hinges on",
  "on firmer ground",
  "in lockstep",
  "tantamount to"
 ]
}
```
Checks: word count 155 (counted by `split()`); all nine targets are exact substrings (I asserted this); every sentence maps to the post (running sum and "every attention part … every MLP part"; notebook identity "up to rounding"; read = dot product, norm division non-linear; last entry "through the final norm", "not a stream vector"; "none tests concepts as directions in a language model's stream"; "Seeing is not doing"; score shift by the same amount). The "carry over" and "hold up" targets leave the loop (they remain as expression items). The three rotated expressions keep their wording: "in lockstep" and "tantamount to" are still in the loop, and "hinges on" too.

### R9. to square with (sentence)
```json
{
 "kind": "expression",
 "headword": "to square with",
 "level": "C2",
 "partOfSpeech": "phrasal verb",
 "register": "formal",
 "sentence": "The idea that a reader sees only the sum squares with the toy, where the four shares of a read add up to the direct read, 5.",
 "target": "squares with",
 "definition": "to be consistent with something; to fit with it"
}
```

### R10. to a first approximation (sentence)
```json
{
 "kind": "expression",
 "headword": "to a first approximation",
 "level": "C1",
 "partOfSpeech": "adverbial phrase",
 "register": "academic",
 "sentence": "To a first approximation, a read is a dot product with the stream; the norm in front of it adds a division, which is not linear.",
 "target": "To a first approximation",
 "definition": "as a rough first description that ignores smaller details"
}
```

### R11. to pin down (optional sharper sentence)
```json
{
 "kind": "expression",
 "headword": "to pin down",
 "level": "C1",
 "partOfSpeech": "phrasal verb",
 "register": "neutral",
 "sentence": "It is hard to pin down what a library's hidden state is until you say which entry you mean: entries 0 to 11 are stream vectors in GPT-2 small, and the last is not.",
 "target": "pin down",
 "definition": "to identify or define something exactly"
}
```

### R12. to hold up (sentence)
```json
{
 "kind": "expression",
 "headword": "to hold up",
 "level": "C1",
 "partOfSpeech": "phrasal verb",
 "register": "neutral",
 "sentence": "The additivity check holds up for GPT-2 small, entries 0 to 11, but we did not run it on a trained Qwen3, Llama, Gemma or Mistral model.",
 "target": "holds up",
 "definition": "to remain true or valid when tested"
}
```

### R13. to rest on the assumption that (optional swap)
```json
{
 "kind": "expression",
 "headword": "to be premised on",
 "level": "C2",
 "partOfSpeech": "adjective + preposition (with be)",
 "register": "formal/academic",
 "sentence": "Comparing two models through each one's own dot products is premised on the stream having no privileged basis, which Elhage and colleagues assert for an idealised stream.",
 "target": "is premised on",
 "definition": "to be based on something taken as true at the start"
}
```

### R14. to be at pains to (sentence)
```json
{
 "kind": "expression",
 "headword": "to be at pains to",
 "level": "C2",
 "partOfSpeech": "verb phrase",
 "register": "formal",
 "sentence": "Olah and colleagues are at pains to say that their evidence for universality is, so far, anecdotal.",
 "target": "are at pains to",
 "definition": "to make a special effort to do something, often to be clear or careful"
}
```

### R15. to hinge on (sentence, headword unchanged)
```json
{
 "kind": "expression",
 "headword": "to hinge on",
 "level": "C1",
 "partOfSpeech": "phrasal verb",
 "register": "neutral",
 "sentence": "Whether a steering push changes behaviour as intended hinges on how real models respond, which this post does not test.",
 "target": "hinges on",
 "definition": "to depend completely on one particular thing"
}
```

### R16. a case in point (sentence)
```json
{
 "kind": "expression",
 "headword": "a case in point",
 "level": "C1",
 "partOfSpeech": "noun phrase",
 "register": "neutral/formal",
 "sentence": "The identity holds only for some entries, and the last entry of a library's list is a case in point: it has been through the final norm, so it is not a stream vector.",
 "target": "a case in point",
 "definition": "a good example of what has just been said"
}
```

### R17. Perfect participle clause (definition and sentence)
```json
{
 "kind": "pattern",
 "headword": "Perfect participle clause",
 "level": "C1",
 "sentence": "Having added the four writes to the embedding, we get the stream after two blocks, (4, 2).",
 "target": "Having added",
 "definition": "'Having + past participle' shows that one action was finished before the next. The subject of the main clause must be the one who did the first action."
}
```

### R18. Tip: retell
```json
{
 "kind": "tip",
 "headword": "Three-step retell",
 "sentence": "Without looking, explain in two minutes how a hidden state is built, using three expressions from this pack: start from the embedding, add each write, then say what a reader can and cannot hear."
}
```

---

## Level table (my estimates; confirm in EVP/EGP)

| Item | Pack level | My call | Action |
|---|---|---|---|
| to bear out | C2 | C2 | keep |
| to square with | C2 | C2 | sentence (R9) |
| to a first approximation | C1 | C1 | sentence (R10) |
| by construction | C1 | C1 (technical) | keep |
| to carry over (to) | C1 | C1 | keep |
| to pin down | C1 | C1-C2 | optional (R11) |
| to take something at face value | C1 | C1-C2 | keep |
| a case in point | C1 | C1-C2 | sentence (R16) |
| to hold up | C1 | C1 | sentence (R12) |
| to rest on the assumption that | C1 | B2-C1 | optional swap (R13) |
| to be at pains to | C2 | C2 | sentence (R14) |
| to fall out of | C2 | C1-C2 | relabel register (m8) |
| a matter of convention | C1 | C1 (borderline) | sentence (R7) |
| to be on firm ground | C1 | C1-C2 | keep |
| in lockstep, to hinge on | C1 | C1 | keep headwords (R15 sentence) |
| to be tantamount to | C2 | C2 | keep |
| What matters is … | C1 | B2 | replace (R5) |
| Perfect participle clause | C1 | C1 | definition (R17) |
| Mandative subjunctive | C2 | C2 | definition (R6) |
| Inversion with 'Should' | C2 | C1-C2 | keep; confirm |
| fewer vs less | C1 | B1-B2 | replace (R1) |
| affect vs effect | C1 | B2 | replace (R2) |
| the number of / a number of | C1 | B2 | replace (R3) |
| orthogonal to (not 'with') | C1 | B1-B2 | replace (R4) |

After applying the replacements, run `python3 scripts/english_pack.py posts/2026-10-residual-stream`. It should exit 0 with 27 items plus the loop. The `note` field in the JSON still says "Three expressions … are repeated" (correct) and says example sentences are "labelled where they go beyond" the post; none now goes beyond it, so that clause can go.

---

## Response

Writer, 2026-10-25. All findings applied to `english/english.json`; `python3 scripts/english_pack.py posts/2026-10-residual-stream` exits 0 (28 items). Rotated headwords unchanged. Where a replacement said more than the post, I narrowed it (noted below). The `note` field no longer says sentences are "labelled where they go beyond" the post.

- **M1** "fewer vs less" replaced by "whether (not 'if')" (R1). Verb changed from "settles" to "shows", the post's word.
- **M2** "affect vs effect" replaced by "however (not a conjunction)" (R2).
- **M3** "the number of / a number of" replaced by "compare like with like ('those in')" (R3).
- **M4** "orthogonal to" replaced, but not by R4 (hyphenated number modifier, which I judge B2). I used "imply vs infer" instead, the C1 slip listed in WRITING.md section 8. Sentence stays inside the post: "A high probe score shows that information is present along a direction, not that later parts of the model use it."
- **M5** pseudo-cleft replaced by the fronted wh-clause (R5), verbatim from the post.
- **M6** mandative subjunctive: definition corrected so that "should be run" is allowed (R6); target is the whole clause. The sentence now reads "The post recommends that ... be run", because "essential" was stronger than the post's "Before you trust the additivity of any model, run the check".
- **M7** "a matter of convention": sentence now gives the post's reason, with no claim about the sources (R7).
- **M8** Loop rewritten from 198 to 158 words, 9 targets, all verbatim. Changes: "attention and MLP part"; the last entry gets its own sentence, so "a case in point" has an antecedent ("Names can mislead"); "but" replaces "yet". Two departures from R8: "hinges on tests that none of the three sources runs" (the post's scope statement) replaces "evidence the sources do not supply"; "To a first approximation" now reads "setting aside the norm ... whose division is not linear", because the post says a read is exact and a norm sits in front of it. About 8 words over the target.
- **m1** "to square with": R9 sentence (the four shares add up to the direct read, 5).
- **m2** "to bear out": now "bears out the claim that the writes add up to the stream, up to rounding, for entries 0 to 11".
- **m3** "to a first approximation": the read is exact; the approximation is setting aside the norm (as in M8).
- **m4** "to pin down": R11 sentence, with "up to rounding" added.
- **m5** "to hold up": R12 sentence.
- **m6** "to rest on the assumption that" swapped for "to be premised on" (R13), level C2.
- **m7** "to be at pains to": R14 sentence (anecdotal evidence).
- **m8** "to fall out of": register relabelled "academic/mathematical".
- **m9** Noted only: the loop uses "on firmer ground", the headword is "to be on firm ground". The target is an exact substring.
- **m10** "to hinge on": headword unchanged. R15 said the post "does not test" real-model steering. The post says "the algebra does not say" whether a push changes behaviour, so the sentence uses that.
- **m11** "a case in point": the sentence now opens with "Library names can mislead", not R16's "The identity holds only for some entries" (the last entry is the exception, not a case of holding).
- **m12** Dangling-modifier pointer removed from the participle clause (R17). Tip renamed "Three-step retell" (R18).

---

## Round 2

Reviewer: independent, fresh agent, 2026-10-25. Read: WRITING.md section 8, `english/english.json`, built `site/mewiki/packs/2026-10-residual-stream.md`, the round-1 review with Response, and `src/content.html`. Only this section was added. I have no live EVP/EGP access, so level calls are estimates in their style, and the two I cannot settle are named below.

### Counts

| critical | major | minor |
|---|---|---|
| 0 | 0 | 6 |

Shape is right: 17 expressions, 4 patterns, 4 fixes, 2 tips, one loop (158 words, 9 targets, all verbatim substrings; I asserted this). Every example sentence was checked against the post (6.2e-6, entries 0 to 11, last entry normed, "we ran no trained Qwen3, Llama, Gemma or Mistral model", x_2 = (4, 2) from the embedding plus four writes, the four shares adding to 5, "anecdotal", "our convention" with "So scores from different arrows can be compared", "What a score means ... the algebra does not say", "Before you trust the additivity of any model, run the check"). None says more than the post. No item is at B2 or below on my reading.

### Round-1 findings: all resolved

- M1 to M3: replaced. `whether`, `however` and `compare like with like` are real slips of advanced writers; M1's level is borderline (see n1 below).
- M4: replaced by `imply vs infer`, which is on the WRITING.md list and faithful. Accepted instead of R4.
- M5: fronted wh-clause is verbatim from Short answer (b). Resolved.
- M6: mandative definition no longer bans "should be run". Resolved (one polish, n6).
- M7: matter-of-convention sentence now gives the post's own reason. Resolved.
- M8: loop 198 to 158 words, 9 targets, "attention and MLP", last entry has its own sentence, "but" for "yet", "up to rounding". Resolved (clarity points in n4).
- m1 to m12: all applied or answered. The writer's narrowing of R15 and R16 is correct (the post says "the algebra does not say", and the last entry is an exception, not a case of the identity holding). m9 is noted only, as agreed.

### Minor findings

**n1. Fix "whether (not 'if')": definition slightly wrong; level borderline.** (a) "'If' belongs to conditions and to casual speech after verbs such as ask or wonder" is inaccurate: "ask if" and "wonder if" are standard in formal writing too. The firm rules are: use *whether* after a noun or preposition, before *or not*, before *to*, and as a subject. (b) *if/whether* in indirect questions is B1-B2 in EGP style; only the noun-plus-whether point ("the question of whether") is plausibly C1. Keep the item only if EGP puts that point at C1; otherwise swap for the WRITING.md fix below. Replacement definition (keep the item):
```json
"definition": "After a noun ('the question of'), after a preposition ('depends on'), before 'or not' or 'to', and when the clause is the subject, use 'whether'. 'If' is fine after 'ask' or 'wonder', but in careful writing 'whether' is safer after nouns."
```
Optional swap (a WRITING.md fix, faithful to the post's "the stream is the embedding plus every write"):
```json
{
 "kind": "fix",
 "headword": "comprise (not 'comprised of')",
 "level": "C1",
 "sentence": "The stream after one block comprises the embedding and the block's two writes.",
 "wrong": "The stream after one block is comprised of the embedding and the block's two writes.",
 "right": "The stream after one block comprises the embedding and the block's two writes.",
 "definition": "'Comprise' means 'consist of' and is followed directly by its parts: the whole comprises the parts. 'Comprised of' is common but still marked as an error by many editors; 'is composed of' or 'consists of' are always safe."
}
```

**n2. "to hold up": odd subject.** A check does not "hold up"; a result or identity does. Replacement sentence (headword and target unchanged):
```json
"sentence": "The additivity identity holds up for GPT-2 small, entries 0 to 11, but we did not run it on a trained Qwen3, Llama, Gemma or Mistral model."
```

**n3. "to be at pains to": still a little stronger than the post.** The post's wording is the plain concession "the only evidence we can offer today is anecdotal". "At pains to say" implies effort that the post does not show. Closer sentence:
```json
"sentence": "Olah and colleagues are at pains to point out that the only evidence they can offer for universality today is anecdotal."
```

**n4. Loop: three small clarity slips for a listener who has not read the post.** (a) "A push moves every score ..., but to say that a high score shows ..." has no antecedent for "push", and "but" sets steering against probing, which are parallel points, not opposed ones. (b) "the notebook" and "the three sources" are undefined in audio. (c) "whose division is not linear" is awkward. The facts are all faithful. Replacement (160 words, same 9 targets, all verbatim, asserted):
```json
{
 "headword": "A paragraph to loop",
 "level": "C2",
 "text": "Every attention and MLP part adds its write to one shared list, so the stream is a running sum. In the toy this is true by construction, and a notebook run on GPT-2 small bears it out, up to rounding. To a first approximation, a read is a dot product with that sum, setting aside the norm, which divides and so is not linear. Names can mislead: the last entry of a library's list is a case in point, because it has been through the final norm, so it should not be taken at face value. Whether concepts are directions in a model's stream hinges on tests that none of the three sources runs, so we are on firmer ground with the arithmetic than with the interpretation. A steering push moves every score in lockstep, and a high probe score shows only that information is present; to say the model uses it would be tantamount to confusing seeing with doing.",
 "targets": ["To a first approximation", "by construction", "bears it out", "a case in point", "at face value", "hinges on", "on firmer ground", "in lockstep", "tantamount to"]
}
```
If the writer keeps the current loop, change at least "A push" to "A steering push" and "but" to "and". Re-record the audio after any change.

**n5. Typography.** One example uses a curly apostrophe ("language model’s stream", "to be on firm ground") where the rest of the pack uses straight ones. Harmless, but make it consistent before the TTS and Margin import so the target matching never depends on the apostrophe.

**n6. Mandative subjunctive definition.** "'is run' is the informal option" is too strong: the indicative after *recommend* is normal in British writing. Replacement:
```json
"definition": "After words like essential, important, insist or recommend, formal English uses the bare base form: 'that the check be run'. British English also allows 'should be run', and the plain indicative 'is run' is common in everyday writing."
```

### Not changed, for the record

- `a matter of convention` is a transparent collocation and is C1 only because *convention* is; keep.
- `Inversion with 'Should'` is C2 on my reading; I cannot confirm the EGP band, so check it with the other flagged levels.
- `to fall out of` (sense: to emerge as a by-product of a calculation) is a mathematical-register idiom; C2 is fair.
- All 9 loop targets are headwords; "bears it out" and "on firmer ground" are inflected forms of "to bear out" and "to be on firm ground", as in round 1.

### Round 2 response (meta-manager, 2026-10-25)
Applied n1 (swapped to comprise), n2, n3, n4 (new loop; "a model's stream" narrowed to "a language model's stream", as S5 V2-01 required), n5 (straight apostrophes), n6.
