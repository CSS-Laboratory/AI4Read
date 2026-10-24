# English packs check: C1/C2 rule, English, faithfulness, mechanics

Reviewer: independent (did not write the packs). Date: 2026-10-25.
Scope: `posts/2026-10-llm-next-word/english/english.json` and `posts/2026-10-ai-finance/english/english.json`, checked against each post's `src/content.html`. For a few claims I also checked the wiki digests and the verified source brief. No pack or post file was edited.

Severity: **critical** = wrong English taught as correct, or a misreported fact. **major** = wrong level under the C1/C2 rule, or a misleading definition, rule or attribution. **minor** = polish.

About the levels: I have no live access to the English Vocabulary Profile (EVP) or the English Grammar Profile (EGP). The level judgements below are my estimates using their conventions. Check the flagged items in EVP/EGP before changing them.

## Counts

| | critical | major | minor |
|---|---|---|---|
| 01 llm-next-word | 2 | 4 | 13 |
| 02 ai-finance | 0 | 7 | 10 |
| Mechanics | 0 | 0 | 4 |
| **Total** | **2** | **11** | **27** |

Both packs pass `scripts/english_pack.py`: 27 and 29 items, exit 0, target offsets round-trip.

---

## Pack 01 · 2026-10-llm-next-word

### Critical

**1. Loop: "By the same token, people stumble on some of those changes too, …"** (critical)
- *Problem.* "By the same token" means "for the same reason, the same conclusion also holds". Here it introduces a contrast: models collapse, *but* people fail some of these changes too. A careful native speaker would say "Then again" or "Yet". This is a loop target, so Kunhao would learn the misuse by shadowing it. The pack's own expression item uses the phrase correctly, so the loop also contradicts the pack.
- *Fix.* Use the phrase for real parallel reasoning and mark the contrast separately: "Yet people stumble on many of those changes too, and if a collapse counts against the model, then by the same token it should count against us."

**2. Loop: "Xie's account of in-context learning is predicated on the model fitting its training *data* exactly"** (critical)
- *Problem.* This misstates the source. Xie assumes that the LM fits the pretraining *distribution* exactly (post, Lens 3; wiki `xie-2022-icl/main.md`: "The authors assume the LM fits the pretraining distribution p exactly"). In ML, "fitting the training data exactly" means memorising it, with zero training error. That is a different assumption, and a worse one. The expression item says "training distribution" correctly, so only the loop is wrong.
- *Fix.* "…is predicated on the model fitting its training distribution exactly…". Then re-record the loop audio (see M3).

### Major

**3. Loop: "…so the burden of proof lies with whoever claims more."** (major)
- *Problem.* This is a non sequitur. That people also fail the changes does not put the burden on "whoever claims more". If anything, it weakens the inference from model failure. "Whoever claims more" is also vague: more than what?
- *Fix.* Make it a separate, plainly evaluative sentence: "Even so, the burden of proof lies with those who claim the ability has emerged." This is consistent with Ullman's skeptical default; see item 7.

**4. Pattern "Cleft sentence for focus" (C1): "What Shannon showed was that…"** (major, level)
- *Problem.* Basic wh-clefts ("What X did was…") and it-clefts are B1–B2 in EGP-style grading. C1 territory is the less common cleft types. Also, "prediction and compression are the same problem" overstates the post, which says "a good predictor is also a good compressor". The loop hedges with "in effect", but the item does not.
- *Fix.* Teach a C1+ cleft. One option is an all-cleft: "All that a low loss tells us is how many bits the model saves." Another is the not-until cleft: "It is not until the output layer is made cheap that the hidden layer becomes the bottleneck." If you keep the Shannon sentence, add "in effect" and relabel the item B2, which means dropping it under the rule.

**5. Pattern "Concessive clause before the claim" (C1): "While it is true that…, …"** (major, level)
- *Problem.* Concessive "while" is a standard B2 (FCE) structure.
- *Fix.* Use a C1–C2 concessive. "Smooth as the loss curve is, it tells us little about when a particular skill appears" (adjective + as + clause, C2). Or "Granted that the loss falls smoothly with scale, it does not follow that skills appear smoothly." Both stay faithful to Kaplan p. 19 as the post reports it.

**6. Fix "respectively" (C2)** (major)
- *Problem.* (a) The "wrong" sentence is not ungrammatical. Placing *respectively* before the paired list ("cost respectively 5.6 and 4.8 bits") is acceptable formal English, just less common. So the rule "Put 'respectively' at the end" teaches a style preference as an error. (b) "GPT-2 cost 5.6 … bits per token" has an odd subject: in the post the *sentences* cost bits, not the model. (c) *Respectively* is more plausibly C1 than C2.
- *Fix.* Choose a real error: *respectively* with only one list, or with lists in mismatched order. Wrong: "Shannon and Kaplan respectively studied entropy." Right: "Shannon and Kaplan studied letters and tokens, respectively." Correct the subject: "Under GPT-2, the English and Japanese sentences cost 5.6 and 4.8 bits per token, respectively." Relabel C1.

### Minor

**7. "the burden of proof lies with" (C1): "Ullman thinks the burden of proof lies with those who claim the ability has emerged."** (minor)
- *Problem.* The post never says this about Ullman. It reports "one clear failure can outweigh many average successes" and "Probably not". The source does support it: the wiki digest of Ullman p. 8 has "presume strongly they have not", a skeptical default. So this is not a misreport, but it goes beyond the post.
- *Fix.* "Ullman argues for a skeptical default: the burden of proof lies with those who claim the ability has emerged." Alternatively, add one clause to Lens 5 of the post.

**8. "throw something into sharp relief": "…throws the tokenizer's bias into sharp relief."** (minor)
- *Problem.* The post never calls the tokenizer biased. Its point is that a per-token metric misleads ("Per-token numbers can point the wrong way"). The Japanese cost also reflects training on English text, not only tokenization.
- *Fix.* "Comparing bits per token with bits per character throws into sharp relief how misleading per-token loss can be."

**9. "to be contingent on": "Whether prompting resembles Bayesian inference is contingent on strong assumptions about the training data."** (minor)
- *Problem.* Xie's conditions also concern the model (exact fit) and the prompt (the concept must have been seen in training, distinguishability), not only the data. Also, what is contingent is the theorem, not whether prompting resembles inference.
- *Fix.* "Xie's result that prompting amounts to Bayesian inference is contingent on strong assumptions about the data, the model and the prompt."

**10. "to be agnostic about": "The GPT-3 authors are agnostic about whether the model learns tasks from scratch."** (minor)
- *Problem.* The post says their *terms* are "agnostic" (Brown p. 4, fn. 1). The sentence also drops the other half of the question.
- *Fix.* "The GPT-3 authors keep their terms agnostic about whether the model learns tasks from scratch or recognises patterns from training."

**11. "to sidestep a question": "Shannon deliberately sidesteps the question of meaning."** (minor)
- *Problem.* *Sidestep* suggests dodging an awkward issue. Shannon openly declares meaning "irrelevant to the engineering problem". The register is slightly unfair to the source.
- *Fix.* "Shannon openly sidesteps the question of meaning: he calls it irrelevant to the engineering problem." Or switch the item to "to bracket a question", which is C2 and academic.

**12. "by the same token" item: "…human failures on such changes count against people."** (minor)
- *Problem.* "Count against people" is vague.
- *Fix.* "…count against people's theory of mind."

**13. Fix "dangling modifier"** (minor)
- *Problem.* (a) "Japanese costs it far more bits per character" generalises from one test sentence to the whole language; the post says "the Japanese one", meaning the sentence. (b) The right version replaces the participle instead of showing how to attach it correctly.
- *Fix.* Right: "Trained on English web text, GPT-2 needs far more bits per character for our Japanese sentence." Then add the Because-version as an alternative.

**14. Fix "stacked hedges", right version: "…the model selects a latent concept."** (minor)
- *Problem.* The post is careful here: the model "in effect 'selects'" a concept, and only inside a stylised model.
- *Fix.* "These results suggest that the model, in effect, selects a latent concept."

**15. Pattern "Inversion after a restrictive adverbial" (C2): definition lists "not only"** (minor)
- *Problem.* Inversion after "not only" is B2. Listing it in a C2 item blurs the level.
- *Fix.* Drop "not only" and add "not until" or "little" ("Little did they expect…").

**16. Fix "comprise (no 'of')"** (minor)
- *Problem.* The fix is correct, but it does not mention that "is comprised of" is widespread and disputed. A C1–C2 learner will meet it in published papers.
- *Fix.* Add: "'is comprised of' is common but criticised by careful editors; avoid it in submissions."

**17. Part-of-speech labels are inconsistent** (minor)
- *Problem.* "to be tantamount to" and "to be predicated on" are labelled *verb phrase*, while "to be contingent on" and "to be agnostic about" are *adjective phrase*. All four have the same structure: be + adjective/participle + preposition. "stop short of" is labelled *phrasal verb*, but it is an idiom (verb + adverb + preposition).
- *Fix.* Label all four "adjective + preposition (with be)". Label "stop short of" as idiom.

**18. Level labels that look off, though both levels pass the rule** (minor)
- *Problem.* Several items labelled C1 are probably C2 in EVP style: *gloss over*, *by the same token*, *give someone pause*, *the jury is still out*, *lend weight to*, *sidestep*. *respectively* is labelled C2 but is likely C1 (item 6).
- *Fix.* Check these in EVP and relabel. No item needs removing on this ground.

**19. Loop paragraph density** (minor)
- *Problem.* Every sentence carries a target, and sentence 3 stacks "predicated on … so … contingent on". It works for shadowing, but a careful native academic would not speak quite this densely.
- *Fix.* After items 1–3 are fixed, consider dropping one target (for example "contingent on" from the loop only) so that sentence 3 breathes.

Clean items (no finding): *tantamount to*, *predicated on* (expression item), *stand or fall on*, *in and of itself*, *gloss over*, *tease apart*, *stop short of*, *lend weight to*, *give someone pause* (97.5% → 0% matches Shapira as the post reports it), *the jury is still out*, the nominalisation pattern, the inversion sentence (it is faithful to Mikolov p. 3 as the post reports it), and both tips.

---

## Pack 02 · 2026-10-ai-finance

### Major

**1. Loop: "We should not read too much into a toy with ten banks, with the caveat that it shows what could happen, not what will."** (major)
- *Problem.* A caveat limits the claim it is attached to. Here the clause after "with the caveat that" is the *reason* for the advice, not a limit on it, so the sentence is illogical as spoken English. This is a loop target, so the misuse would be shadowed. The expression item uses the phrase correctly.
- *Fix.* "A toy with ten banks is useful, with the caveat that it shows what could happen, not what will, so we should not read too much into it."

**2. Loop: "Most participants in the IMF's outreach want a human in the loop, partly because accountability presupposes someone who can be asked why."** (major, attribution)
- *Problem.* This gives the participants a reason that is the post's own gloss ("Accountability needs someone who can be asked why (ours)", Lens 4). The source's reasons are "regulatory, risk management, liability, and ethical" (IMF p. 78), and the post reports "partly for 'liability' reasons".
- *Fix.* "…want a human in the loop, partly for reasons of liability; on our reading, accountability presupposes someone who can be asked why."

**3. Fix "imply vs infer": "The survey implies that most managers are cautious; from it we infer that deciding is still mostly human."** (major, faithfulness)
- *Problem.* The post never says that "most managers are cautious", and "the survey" is never identified. The 59% Mercer figure is in the source brief but not in the post. The verified brief also warns that the IMF outreach is "not a representative survey of practice".
- *Fix.* "The IMF's finding that a human trader 'may ultimately make the trading decision' implies that deciding is still mostly human; from it we infer that full automation is not near." Alternatively, use a neutral non-post example. The wrong/right pair is fine.

**4. "by no means" (C1)** (major, level)
- *Problem.* The project's own `posts/2026-10-ai-finance/english-gloss.json` labels this item **B2**. The new pack relabels it C1 with no reason given. It sits on the B2/C1 boundary at best, so it looks relabelled to fit the rule.
- *Fix.* Confirm in EVP. If it is B2, replace it with a clearly C2 item that fits the same slot. Options: "a far cry from" ("Running a market is a far cry from answering for it"), or "not by any stretch" ("Running a market is not, by any stretch, the same as answering for it"). Update the loop target to match.

**5. "a human in the loop" (C1)** (major, level)
- *Problem.* This is a transparent technical compound of A1–B1 words, and EVP gives it no grade, so calling it "C1" does not mean anything. It is also everyday jargon in Kunhao's own field (LLM labelling, safety), so it teaches him nothing. The definition ("must check or approve … before it takes effect") is narrower than common use, which covers any required human involvement.
- *Fix.* Drop it from the expression list, or move it to an untagged "domain terms" group outside the C1/C2 rule. If you keep it, loosen the definition: "human judgement built into an automated process, often as approval before action".

**6. "a single point of failure" (C1)** (major, level)
- *Problem.* Same issue as item 5: a transparent technical compound with no EVP grade.
- *Fix.* Same as item 5. A C1–C2 lexical item for the same idea: "an Achilles' heel" ("One shared model could become the system's Achilles' heel").

**7. Pattern "Cleft sentence for focus" (C1): "It is declaring and answering, not running, that make a group of people a society, on our reading."** (major, level, plus polish)
- *Problem.* The basic it-cleft is B2 (see Pack 01, item 4). The tag ", on our reading" at the end is clumsy, and a native speaker would front it. The agreement ("make") is correct.
- *Fix.* "On our reading, it is not until people declare and answer that a group becomes a society." This is a not-until cleft, C1+. Or keep the original but front the tag ("On our reading, it is declaring and answering…") and relabel B2, which means dropping it.

### Minor

**8. Loop: "…hinges on whether machines can do the accepting, and what remains to be seen is whether they ever could."** (minor)
- *Problem.* Three "whether" clauses in one sentence, and the tense slips from *can* to *could*.
- *Fix.* "…so whether a machine-only token is money hinges on the accepting. What remains to be seen is whether machines could ever do it."

**9. Fix "comprise", right version: "The five jobs comprise running, deciding, checking, declaring and answering."** (minor)
- *Problem.* *Comprise* needs the whole as subject. "The five jobs" are the parts themselves, so the sentence is nearly tautological.
- *Fix.* "A society's work comprises five jobs: running, deciding, checking, declaring and answering." Wrong version: "…comprises of five jobs…".

**10. "to devolve onto" (C2)** (minor)
- *Problem.* (a) The standard prepositions are *on*, *upon* and *to* (Cambridge, Oxford); "onto" is marginal. (b) It is a prepositional verb, not a *phrasal verb*. (c) The sentence states a legal position flatly, but the post says "We have no legal sources and state no legal position". The post's own claim is limited to "under current capital-market rules".
- *Fix.* Headword "to devolve on/upon", label it prepositional verb. Sentence: "Under current rules, responsibility does not devolve upon the AI system; it stays with the institution that deploys it."

**11. "to be held accountable (for)": "Institutions are held accountable for the AI systems they deploy."** (minor)
- *Problem.* The IMF states a rule ("are responsible"); "are held accountable" describes enforcement in practice, which is slightly stronger.
- *Fix.* "Under the IMF's reading of current rules, institutions can be held accountable for the AI systems they deploy."

**12. Pattern "Reporting verbs calibrated to strength"** (minor)
- *Problem.* (a) "Common models could correlate trading" is unidiomatic. The FSB's wording is "could lead to increased correlations in trading" (FSB p. 1, per `outline.md`), and the post itself quotes only p. 21. (b) "hypothesise a monoculture" is a little odd; *hypothesise* usually takes a that-clause. (c) The target highlights only "judges".
- *Fix.* "…the FSB warns that common models could increase correlations in trading; Gensler and Bailey hypothesise that broad adoption could produce a monoculture." Highlight all three verbs, or the first.

**13. Fix "stacked hedges": "could possibly perhaps"** (minor)
- *Problem.* Nobody writes "possibly perhaps", so the example is a strawman.
- *Fix.* Use a realistic stack: "Shared models may potentially be likely to make failures coincide." → "Shared models could make failures coincide."

**14. Pattern "Inversion with 'were … to'": "…their errors would be likely to coincide."** (minor)
- *Problem.* "Would be likely to" is clunky.
- *Fix.* "…their errors would tend to coincide." (The loop has the same phrase.)

**15. Pattern "Inversion after a negative adverbial"** (minor)
- *Problem.* It overlaps with Pack 01's inversion item. Its definition lists "only when", which is restrictive, not negative.
- *Fix.* Either merge the two items, or keep this one for "rarely/seldom/little" only.

**16. "in lockstep": "Models trained on the same data may move in lockstep."** (minor)
- *Problem.* In the source, the *predictions* "proceed in lockstep", not the models.
- *Fix.* "Models trained on the same data may make predictions that move in lockstep."

**17. "to cut both ways": "…but they make firms more alike."** (minor)
- *Problem.* The post qualifies this as "ours" and says that standardising only the form might avoid sameness. The sentence states it flatly.
- *Fix.* "…but they can make firms more alike."

Clean items (no finding): *conflate*, *confer … on*, *underpinned by*, *presuppose*, *compound*, *at odds with* (fix only the part-of-speech label: idiom, not adjective phrase), *hinge on*, *that's a big if*, *read too much into*, *with the caveat that* (expression item), *what remains to be seen is whether*, the dangling-modifier fix, both tips. The "human in the loop … in any AI-based strategy" sentence is faithful to IMF p. 78 (verified brief), even though the post quotes a shorter form.

---

## Mechanics

**M1. Validation passes** (no finding)
`python3 scripts/english_pack.py posts/2026-10-llm-next-word` gives 27 items (16 expressions, 4 patterns, 4 fixes, 2 tips, 1 shadowing), exit 0. `… posts/2026-10-ai-finance` gives 29 items (18, 4, 4, 2, 1), exit 0. Every level is C1 or C2, every target is found, offsets round-trip in UTF-16, there are no duplicate externalIds, and all loop targets are present. Running the script rewrites `site/mewiki/packs/*.json/.md`.

**M2. Markdown preview prints a double period** (minor)
Pattern definitions end in "." and the script appends another, which gives "falls.. *What…*" in both `.md` files.
- *Fix.* In `english_pack.py`, write `x.get('definition','').rstrip('.')` in the expression/pattern line.

**M3. The loop audio must be re-recorded after loop fixes** (minor, process)
`site/mewiki/packs/audio/*-loop.mp3` (02:06–02:07) was recorded from the current loop text. After fixing P01 items 1–3 and P02 items 1, 2, 4 and 8, re-run `english_pack.py` first, then `tts_english_loop.py <slug>`, because the TTS script reads the pack JSON.

**M4. Items repeated across the two packs** (minor)
These appear in both packs: *comprise*, *stacked hedges*, *dangling modifier*, *cleft*, *inversion*, *Production drill*. The externalIds differ by slug, so Margin will hold near-duplicate cards.
- *Fix.* Decide whether this is intended. If not, keep each item in one pack only.

**M5. The pack note's promise is not kept** (minor)
The note says "claims that are our reading say so", but only one sentence does ("on our reading", P02 cleft). Several sentences are readings without a label: P01 "lend weight to", "by the same token"; P02 "presuppose", "devolve", "cut both ways".
- *Fix.* Add short labels where a sentence goes beyond the post, or reword the note to "example sentences may state our reading".

**Blog separation (checked, no finding).** When I started, `posts/2026-10-ai-finance/src/content.html` still contained §15 "How to say it in English", and the built `index.html`/dist of post 01 still had its old English section. A rebuild at 02:10 removed both. I re-extracted both posts and diffed them: the only changes are the removed English section, the TOC entry, the renumbered "15 · Sources" and the audio time (37 → 35 min). No leftover references were found.

---

## Round 2 (re-check of the changes only)

Scope: both loops, and every item that was edited or added, in both `english.json` files as they stood at 02:19. Unchanged items were not re-reviewed. `english_pack.py` passes for both packs: 27 and 28 items, exit 0. The ".." in the Markdown previews is gone.

**Counts (round 2): 0 critical, 2 major, 9 minor.**

All round-1 critical and major findings are resolved. The resolved points are:
- P01 loop: "training distribution" is restored, "by the same token" now introduces a real parallel, and the burden-of-proof sentence stands on its own.
- New C1+ patterns: the all-cleft, "Smooth as …", and "it is not until … that".
- The "respectively" fix now teaches a real error.
- P02 loop: "with the caveat that" is used correctly, and the IMF's liability reason is now separated from our gloss.
- The imply/infer example sentence now matches the post.
- "by no means", "a human in the loop" and "a single point of failure" are dropped. Their replacements, "a far cry from" and "an Achilles' heel", are plausible C2 items.
- Round-1 minor items are applied. The remaining exceptions are listed below.

### Major

**R2-1. The loop audio is stale** (major, mechanics)
- *Problem.* `site/mewiki/packs/audio/2026-10-llm-next-word-loop.mp3` (02:06) and `…ai-finance-loop.mp3` (02:07) were recorded before both loops were rewritten. The packs (02:19) still point to them. Kunhao would shadow the old text, including the two round-1 critical errors.
- *Fix.* Run `tts_english_loop.py 2026-10-llm-next-word` and `tts_english_loop.py 2026-10-ai-finance` now, since the packs are already rebuilt. Check that each mp3's mtime is later than its pack JSON.

**R2-2. P02 fix "principal vs principle" (C1)** (major, level)
- *Problem.* As a spelling confusion this is B2: both words are B2-band in the English Vocabulary Profile, and it is the same kind of item that was dropped in round 1. Only the agency-theory sense of "principal" is above B2, and the item does not test that sense.
- *Fix.* Replace it with a C1 fix grounded in the post. Wrong: "Knowledge is one criteria for successful delegation." Right: "Knowledge is one criterion for successful delegation; an incentive is the other." Definition: "criterion" is singular, "criteria" plural (likewise phenomenon/phenomena).

### Minor

**R2-3. P01 loop: "…then by the same token it should count against us."** (minor)
- *Problem.* "It" grammatically points back to the model's collapse.
- *Fix.* "…then by the same token our own failures should count against us."

**R2-4. P01 "the burden of proof lies with": "Ullman argues for a sceptical default: …"** (minor, carried over)
- *Problem.* This is accurate to Ullman p. 8 (wiki digest), but the post still does not say it. The pack's new note promises sentences "never" state a source's claim beyond the post.
- *Fix.* Add one clause to Lens 5 of the post. Or drop the attribution: "On a sceptical default, the burden of proof lies with those who claim the ability has emerged."

**R2-5. P02 "a far cry from": "Running a market is a far cry from answering for it."** (minor, optional)
- *Problem.* The idiom most often contrasts a reality with an ideal or an earlier state. Here it compares two activities. It is acceptable, but it is not the prototypical use.
- *Fix (optional).* Add a second sentence showing the prototypical use: "Today's markets are a far cry from a society that runs itself."

**R2-6. P02 pattern "It is not until … that": "On our reading, it is not until people declare and answer that a group becomes a society."** (minor)
- *Problem.* "Not until" reads as a time sequence, but the claim is a condition. (This was my own round-1 suggestion.)
- *Fix.* Keep the item, but use a temporal claim from the post: "It was not until a pre-set rule paused trading that prices stabilised." Faithfulness caution: the post says the pause was not shown to cause the stabilisation, and "not until … that" only orders the events, so it is acceptable. Or keep the society sentence as an "it is only when … that" cleft.

**R2-7. P02 fix "imply vs infer": the wrong/right pair still says "From the survey…"** (minor)
- *Problem.* The example sentence was fixed, but the pair still refers to "the survey" without saying which one.
- *Fix.* Wrong: "From the IMF's finding we imply that deciding is still largely human." Right: "From the IMF's finding we infer that deciding is still largely human."

**R2-8. P02 fix "the reason is that"** (minor)
- *Problem.* The right version adds "partly", so the pair differs by more than the error being taught. "The reason … is partly that" is also a little stiff.
- *Fix.* Wrong: "Part of the reason most participants want a human in the loop is because someone must bear liability." Right: "Part of the reason most participants want a human in the loop is that someone must bear liability."

**R2-9. P02 loop: "…hinges on the accepting."** (minor)
- *Problem.* The phrase is elliptical; it leaves out who does the accepting.
- *Fix.* "…hinges on who does the accepting. What remains to be seen is whether machines could ever do it."

**R2-10. P02 pattern "Reporting verbs": the target is still only "judges"** (minor, carried over)
- *Problem.* The item teaches a choice among three verbs, but only one is highlighted.
- *Fix.* Highlight the full verb sequence, or rewrite the item as three sentences.

**R2-11. Retired list misses round-1 IDs** (minor, mechanics)
- *Problem.* `retired-2026-10-25.json` (02:19) records the dropped "by no means", "a human in the loop", "a single point of failure" and P01's "Cleft sentence for focus". It does not record these externalIds, which were in the round-1 packs and are now gone or renamed:
  - P01: "Concessive clause before the claim".
  - P02: "Cleft sentence for focus", "comprise (no 'of')", "stacked hedges", "dangling modifier", "Production drill", "to devolve onto".
- *Fix.* If the round-1 packs were ever imported into Margin, add these IDs so their review history is kept. If they were never imported, add a note saying so.

No finding on these new items: all-cleft (C1), "Smooth as …" (C2), the inversion definition, "comprise", stacked hedges, "respectively", the dangling modifier (P01), "an Achilles' heel", "devolve upon", "held accountable", "presuppose", "in lockstep", "cut both ways", the reporting-verb wording, "raise the question (not 'beg')" (the definition rightly limits the rule to careful academic English), and the "Shadow, then summarise" tip. The P01 loop still opens with a basic wh-cleft, but it is not a target, so this is no finding.
