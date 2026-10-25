# Review of English pack /2 · 2026-10-ai-finance

Reviewer: independent (did not write the pack). Date: 2026-10-26.
Checked: `english/english.json` against `src/content.html` (the five-jobs section, the Decide/Check/Declare/Answer table, the Gensler and Bailey quote, section 13 "So what happens?"), WRITING.md sections 8 and 9, the Margin request, and the calibration in `review/english-packs-check.md`. I have no live access to the English Vocabulary Profile (EVP) or English Grammar Profile (EGP); levels are my estimates in their style. Nothing but this file was written. A scratch copy of the pack with every edit below applied passes the checker (see "Verification").

## Counts

| critical | major | minor |
|---|---|---|
| 0 | 8 | 11 |

`python3 scripts/english_pack.py posts/2026-10-ai-finance --check` on the current pack: **exit 0**, "passage 189 words, 9 sentences, core 75 words, 9 expressions, 3 patterns, 3 fixes, 1 tip". The pack passes the mechanical checks, so every finding below is about content.

Nothing misreports the post outright (no critical). The passage keeps its hedges (might, caveat, "not measurements") and attributes the survey correctly in substance. The major items are scope losses, one logic slip, level problems and one unanswerable gist question.

---

## 1. Passage

### Major

**P1. Sentence 7 makes the definition the "verdict" (major, faithfulness and logic).**
- Current: "Our verdict, which rests on our definition, is that a society lets members rely on shared rules, contest them and find someone answerable."
- Problem. In the post, the definition is "a society is a group whose members can rely on shared rules, contest them, and find someone answerable" (ours), and the verdict is the conclusion that a system with nobody declaring or answering is "a machine system that people live next to" ("That is our verdict, and it rests on our definition"). The passage says the verdict rests on the definition and then states the definition as the verdict, which is circular. It also presents "a society lets members ..." as a plain fact, where the post labels it "ours".
- Fix. Make sentence 7 the definition ("By our definition") and let sentence 8 carry the verdict. The sentence still contains "contest them" and "answerable", so the expression items and fix 3 keep their anchors.
- Replacement sentence 7: `By our definition, a society lets members rely on shared rules, contest them and find someone answerable.`
- Replacement sentence 8: `So, with no person left to declare or answer, the result would be a machine system that people live next to, a far cry from a society.`
- Side effect: this deletes "Our verdict, which rests on our definition, is that", which was the anchor of the third pattern (see S3).

**P2. Sentence 2 drops the scope "in some markets" (major, WRITING.md section 9: keep the source's population and scope).**
- Current: "In finance, running is largely automated, ..."
- Problem. The post says "Largely automated at run time in some markets" and the 70% figure is for US equities. "In finance" reads as all finance. "Checking is automatic" (sentence 4) is the same, though the post says "Automatic at run time", which is narrower still.
- Replacement sentence 2: `In some financial markets, running is largely automated, but much of that is rule-based software, not AI, so we should not conflate algorithmic trading with AI trading.`
- Replacement sentence 4: `Checking is largely automatic, yet every automated checker needs a checker, so the chain must end somewhere: today, in rules people wrote.`

**P3. A listener cannot tell what "declare" and "answer" mean (major, stands alone).**
- Problem. Sentence 1 lists five jobs but never says what the last two are. The verdict (sentence 8) depends on "declare or answer", and sentence 6 never says that accepting what counts as money is the declare job. A listener who has not read the post cannot link them.
- Fix, with no extra words overall (see the word count in Verification). Gloss "declare" where it is used in sentence 6, and let sentence 7's "find someone answerable" gloss "answer".
- Replacement sentence 6: `Declaring is saying what counts: money is underpinned by people continuing to accept it, and what remains to be seen is whether machines could do that accepting.`
- This drops the what-clause subject (see S2), which is one of the two B2 patterns I also ask you to remove. It keeps "underpinned by" and "what remains to be seen is whether". "Money is underpinned by people continuing to accept it" is Searle's point in the post's words: "we must continue to accept it as money or it will become worthless".

### Minor

**P4. Sentence 3 (minor, listener).** "the IMF's outreach" is internal jargon. The post says the IMF "surveyed and interviewed market participants in 2024". Replacement: `Deciding is mostly human: participants in an IMF survey expect a human in the loop in the near term.` (Same length, 19 words.)

**P5. Sentence 5 is long to shadow (minor).** It runs to 29 words, with an inversion and a trailing caveat. Splitting is clearer for a listener but costs words, and the budget is full (189 of 190). Keep it as a single sentence unless you cut elsewhere. If you split, use: `Were firms to automate deciding with a few shared models, their failures might move in lockstep. We say that with the caveat that it rests on warnings and toy models, not measurements.` That adds a sentence, so core indexes and fix indexes would shift; I have not tested it against the 190-word cap.

**P6. "in lockstep" is a slight intensification (minor).** The post's own summary is "failures may arrive together". "Lockstep" is Gensler and Bailey's word for correlated *predictions*. "Move in lockstep" says the failures happen at the same time and in the same way, which is a little stronger than "together". Judgement: acceptable. "Might" and the caveat keep the hedge, and the toy models in the post (Haldane and May, the six-bank toy) are about failures that coincide. No change needed.

**P7. Register (minor).** "Were firms to ..." and "with the caveat that" read as written English rather than speech. That is acceptable for a C2 mini-talk, and both are taught items. Spelling is British throughout (no variant words); apostrophes are straight; no abbreviations with full stops.

**P8. Core sentences.** Sentences 4, 5 and 6 are worth memorising (the checker chain, the lockstep conditional with its caveat, and the acceptance point). Core words are 75 now and 78 after the edits above, both inside 60 to 90. No change to the `core` array.

---

## 2. Expressions and patterns

### Major

**E1. "human in the loop" is not C1 (major, level).**
- The phrase is a field term: "human" plus "in the loop" (B2), already known to anyone who reads AI papers. It does not teach a C1 or C2 lexical item, and it is the sort of compositional item the earlier review rejected.
- Fix: drop the item. The passage keeps the phrase naturally; the pack drops to 8 expressions, which is still within 8 to 12. Remove this whole object:
  `{"kind":"expression","headword":"human in the loop", ...}`
- List `ai4read:2026-10-ai-finance:human-in-the-loop` in the retired file if it was ever published.

**S2. "What-clause as subject" (labelled C1) is B2 (major, level).**
- A nominal wh-clause as subject ("What matters most is ...") is a standard B2 structure; the earlier review made the same call on the cleft pattern in pack 01. It also duplicates the "what remains to be seen is whether" expression.
- Fix: drop it (retire `ai4read:2026-10-ai-finance:what-clause-as-subject`).

**S3. "Non-defining relative clause inside the sentence" (labelled C1) is B2 (major, level).**
- Non-defining "which" clauses are B1 to B2 in EGP-style grading, and the medial position is a style choice, not a separate grammar point. P1 also removes the anchor sentence.
- Fix: drop it (retire `ai4read:2026-10-ai-finance:non-defining-relative-clause-inside-the-sentence`) and add one pattern that is really C1, anchored in the new sentence 8:

```json
{
  "kind": "pattern",
  "headword": "Absolute 'with' + noun phrase + participle",
  "level": "C1",
  "definition": "'With' plus a noun phrase and a participle, adjective or phrase gives the circumstances in which the main clause holds: 'With X left to do Y, ...'.",
  "anchor": "with no person left to declare or answer",
  "sentence": "With the data still unlabelled, we could not train the model.",
  "target": "With the data still unlabelled"
}
```

This leaves two patterns (inversion at C2, absolute "with" at C1), which is the minimum of 2 to 4.

### Minor

**E2. The other flagged items.**
- *"to contest" (C1): keep.* The competition sense ("contest" as a match) is B2, but the card's sense is "formally challenge a decision", which is a C1 to C2 use. The definition already says that. Usage in the passage ("contest them", where *them* is shared rules) is correct and natural. Second context is natural and free of named-source claims.
- *"answerable (to/for)":* label **C2**, not C1 (EVP lists the adjective at C2 as far as I can tell). The passage use, "find someone answerable", is natural. The second context is odd: editors being "answerable ... for every correction they publish" does not work, because you are answerable for errors, not for the corrections that fix them. Replace with:
  `"sentence": "Reviewers should be answerable to the editor for the quality of their reports.", "target": "answerable to the editor"`.
- *"a far cry from":* the definition "usually much less than" is wrong for some uses ("a far cry from what we expected"). Replace with `"definition": "very different from something, often because the real thing falls short of what you might expect"`. Second context is natural and in the same sense.
- *"to be underpinned by":* correct in the passage and in the second context. The definition "something that lies beneath it" is a metaphor inside a definition. Replacement: `"definition": "to be supported by, or to depend on, something that forms its basis"`.
- *Levels that may be one band up (optional):* "to conflate" (C2?), "with the caveat that" (C2?), "in lockstep" (C2?). C1 is safe, so I would leave them. "What remains to be seen" is borderline B2/C1 as a phrase, but the full frame "what remains to be seen is whether" is a C1 sentence frame. Keep.
- *"to conflate X with Y", "in lockstep", "with the caveat that", "what remains to be seen is whether", "Inversion with 'were ... to'":* correct, natural in the passage, accurate definitions, and natural second contexts with no claims about named sources. No change.

---

## 3. Fixes

Each `wrong` is the passage sentence with one change; the checker confirms `right` equals the anchored sentence. If you apply P1 and P2 the `wrong` strings must be regenerated from the new sentences (indexes 2, 3, 7 are unchanged).

### Minor

**F1. "uncountable noun: software" (C1): keep.** A real, persistent error ("a software"), one change, accurate rule. New `wrong` after P2:
`In some financial markets, running is largely automated, but much of that is a rule-based software, not AI, so we should not conflate algorithmic trading with AI trading.`

**F2. "article: in the near term" (C1): the rule overgeneralises (minor).** "Fixed time phrases keep their article" is untrue for "in future", "at present", "in time". New `wrong` (after P4 wording): `Deciding is mostly human: participants in an IMF survey expect a human in the loop in near term.`
New rule: `"definition": "'Near term', 'short term' and 'long term' take 'the' after 'in': 'in the near term', 'in the long run'. A few time phrases take none ('in future', 'at present'), so learn each as a unit."`

**F3. "contest (no preposition)" (C1): defensible but the weakest (minor).** "Contest against" is a plausible analogy with "fight against", but it is less common than "discuss about", and "contest against" does exist in the competition sense, so the rule should name the sense. New `wrong` after P1: `By our definition, a society lets members rely on shared rules, contest against them and find someone answerable.`
New rule: `"definition": "In the sense 'challenge', 'contest' takes a direct object: contest a rule, not 'contest against a rule' (compare discuss a plan, not 'discuss about a plan')."`
It tests the same word as the "to contest" card; that is acceptable, but a fix on a different word would add variety if you have a better error to hand.

---

## 4. Gist and retell

### Major

**G1. Gist question 1 has two correct answers (major).**
- Current question: "Which of the five jobs does the speaker say is already largely automated in finance, and is all of that automation AI?" Sentence 4 says "Checking is automatic", so a listener may answer *check* and be marked wrong against the key (*run*).
- Replacement:

```json
{
  "question": "The speaker says that running is largely automated in some financial markets. What does the speaker warn us not to conflate, and why?",
  "answer": "Algorithmic trading with AI trading, because much of that automated running is rule-based software, not AI."
}
```

Question 2 ("What is the speaker's verdict about a system in which no person is left to declare or answer?") is answerable from the passage alone and the answer is faithful. Keep it.

**R1. The retell model answer loses the survey population (major, section 9).**
- Current: "... people still write the rules and expect to stay in the loop." Read plainly, this says the *people who write the rules* expect to stay in the loop. The passage says *participants in the IMF survey* expect a human in the loop. It also states "In finance, running and checking are largely automated" without the scope.
- Replacement `modelAnswer` (uses all three `mustUse` expressions: *conflate*, *underpinned by*, *a far cry from*; plus *it remains to be seen*, which is a related form of the item "what remains to be seen is whether"):
  `"In some financial markets, running and checking are largely automated, but we should not conflate rule-based software with AI, and survey participants expect a human to stay in the loop. Money is underpinned by people accepting it, and it remains to be seen whether machines could do that accepting. By our definition, with nobody left to declare or answer, the result would be a far cry from a society: a machine system that people live next to."`

### Minor

**R2. Retell instruction (minor).** "what the evidence does not yet show" is vague. Replacement: `"In 2-3 sentences, explain to a colleague why a fully automated financial system would not count as a society by the speaker's definition, and what is still open."`

---

## Replacement passage (all passage edits together)

```
Could a society run itself on AI? We can split a society into five jobs: run, decide, check, declare and answer. In some financial markets, running is largely automated, but much of that is rule-based software, not AI, so we should not conflate algorithmic trading with AI trading. Deciding is mostly human: participants in an IMF survey expect a human in the loop in the near term. Checking is largely automatic, yet every automated checker needs a checker, so the chain must end somewhere: today, in rules people wrote. Were firms to automate deciding with a few shared models, their failures might move in lockstep, with the caveat that this rests on warnings and toy models, not measurements. Declaring is saying what counts: money is underpinned by people continuing to accept it, and what remains to be seen is whether machines could do that accepting. By our definition, a society lets members rely on shared rules, contest them and find someone answerable. So, with no person left to declare or answer, the result would be a machine system that people live next to, a far cry from a society.
```

Still 9 sentences; `core` stays `[4, 5, 6]`; fix `anchorSentence` values stay 2, 3, 7.

## Verification

I built a scratch copy outside the repo with every change above (passage, gist 1, model answer, the three dropped items, the new pattern, the "answerable" level and second context, and the three fix strings) and ran the checker on it: `source OK · passage 189 words, 9 sentences, core 78 words · {'expression': 8, 'pattern': 2, 'fix': 3, 'tip': 1}`, exit 0. The tip is untouched ("Five-jobs retell"); it is faithful and fine, and it only asks for "three expressions from this pack".

After the edits, re-record the passage audio (the text hash will otherwise flag it) and list the three dropped ids in `site/mewiki/packs/retired-<date>.json`.
