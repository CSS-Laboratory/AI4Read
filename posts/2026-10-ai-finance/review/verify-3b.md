---
id: 2026-10-ai-finance/review/verify-3b
stage: S5, round 3 (independent fact-check of the round-3 draft, checker B)
checked: 2026-10-17 to 2026-10-18
draft: src/content.html (all visible text, 8 fold-outs, 15 widget configs, diagram step texts, captions, exercise and playground answers, Sources list), audio-script.md, english-gloss.json (factual content), post.json and numbers.md (consistency)
round-2 inputs checked against the text: review/verify-2.md, review/verify-2b.md, review/round2-merged.md (esp. section A, the four groups), review/response-2.md (the writer's claims were re-checked in the text, not trusted)
not read: self-review.md, critic files, review/verify-3.md (independence)
method:
- Every cited sentence re-opened at the source: FCIC p. 128 and p. 149 (page images), p. 28 (pdf 57); Kirilenko abstract and p. 1; N&K intro and Part I; Luo and Mik (abstract, introduction); Scheurer abstract, p. 1, p. 8; Duetting and Buehler abstracts; FSB pp. 1, 20, 21, 28-29 and press release; Danielsson et al. 2022 p. 7; Danielsson and Uthemann abstract and introduction; Arora WP abstract, pp. 1-6, 12; Ashby pp. 204-209, 246-247; Cover and Thomas p. 150; Granovetter pp. 1424-1425; Lupia and McCubbins Theorem 5.1 (p. 85) and p. 207 n. 2; Keynes ch. 12; SEP 4.2.3 and 5.6; Cointelegraph, Decrypt (page metadata: 16 Oct 2024), MIT Sloan, Guardian 2023, Guardian 2024, Ynet, Poole, Fox.
- A programmatic check of all 177 quoted strings on the page against the saved sources, transcripts and library texts: 38 not matched literally. 25 are our own labels, preset names or English examples; 8 are base.en transcript errors, all confirmed with small.en or medium.en (see below); 4 are two-column or hyphenation artefacts of the text layer (Ashby, Arora, D&U, Danielsson), read visually or in the aligned text. The two real mismatches are findings n1 and n7.
- Audio re-transcribed with faster-whisper (WAV cut with ffmpeg -ac 1 -ar 16000, read with `wave` as float32; small.en, and medium.en where small.en and base.en disagreed): WEF [1:50-2:15], [2:52-3:32], [16:10-16:55] and [16:46-16:57] (the first window cut the sentence), [19:05-19:50], [31:45-32:30]; BIS [22:35-23:31], [22:50-23:14] (medium.en), [26:55-27:20], [29:55-30:40]. Both base.en transcripts were searched in full (finance, money, invent, lie, manipulate, creative, institutions) for the balance check. Segments already re-transcribed in rounds 1-2 (BIS [5:08-5:42], [9:45-10:40], [12:36-12:55], [16:05-16:30], [20:30-21:00], [21:30-22:10], [25:05-26:12]; WEF [2:38-3:00], [5:44-6:12], [7:58-8:20], [10:30-10:50], [11:35-11:55], [17:25-17:50], [26:10-26:45], [30:50-31:30]) were not repeated.
- Numbers: check.mjs on content.html (15/15 configs OK; every preset, `--values` and `--seeds` set quoted in the prose and the playground answers), the three notebooks, and Python (scratchpad v3b/toy.py: the new six-asset toy over all 15 placements, plain pool, contract A table, CDO, N_eff, Bayes, Ashby brute force over 16 plans, tree of majorities, Granovetter, hand steps), `scripts/wordcount.py`.
---

# S5 fact-check, round 3, checker B: post 02

Severity follows rubric section A. Source quotes are at most 25 words. Timestamps: the page uses base.en times; small.en times differ by up to about 6 s. I treat that as correct.

## (a) Round-2 fix verification

### Binding list, round2-merged.md

| Item | Verdict | Evidence in the current text |
|---|---|---|
| A. Four-group Harari classification (page and audio) | **FIXED**, with three label nits (n2, n5, n3) | Section 3 has the compact table (groups 1-4, one verb each). The fold-out `box-harari` repeats the four groups with every line. Every line is in the group the merged list prescribes: group 1 WEF [2:00], [2:47], [5:48]-[5:57], [10:36], BIS [5:14], [16:21], Ynet; group 2 BIS [30:24], WEF [31:11], [16:28], [19:11]-[19:23], [26:29]-[26:35]; group 3 BIS [9:54], WEF [17:29], [31:59], Guardian 2023 "What happens if", Guardian 2024 Broomstick; group 4 WEF [8:07]/[11:39], BIS [21:37]/[22:57], Guardian 2023, Guardian 2024. The summary sentence is verbatim in section 13 and in the audio `answer` chapter. No sentence says "his timelines are hedged", "forecasts are conditionals" or "a policy question, not a forecast" (grep). The personhood point is both a forecast ([16:28], [19:11]) and a policy question ([16:47]) in section 9, the fold-out and the audio. The line-by-line audit is in section (d). |
| B2. Danielsson and Uthemann | **FIXED** | Lens 2 lever 2 states "amplifies existing financial system vulnerabilities" and "faster and more severe" (abstract), "cannot effectively prevent and resolve" and "can both stabilise and destabilise ... depending on the severity of the shocks ... how prepared the financial authorities are" (introduction), and the proposal to build their own AI (abstract). They are no longer filed under Counterweights. Audio matches. One locator nit (n15). |
| B3. `dg-chain` rebuilt | **FIXED**, with tag nits (n3, n4, n5) and one balance finding (M2) | H1-H4 only, edges labelled asserted / predicted / imagined, an Evidence tag under each node, and a separate dashed branch "Our additions, not his", reveal in five steps. No "shown in toys" label remains. Title "Our compression of Harari's chain: his status, our evidence" and the audio sentence say it is a compression. |
| C. Scheurer | FIXED | "nearly (but not exactly) 0%" is attached to insider trading; "the tendency to deceive, conditional on misalignment, remains high under all prompts" (p. 8). Re-read at the source. |
| C. CDO "such as" | FIXED | "pools of financial assets, such as the riskier tranches of mortgage-backed securities, sliced into tranches in a cash-flow waterfall": matches FCIC p. 128 (page image). |
| C. "already" removed from BIS [5:14] | FIXED | Page, answer, English pattern and audio. "already" survives only in the WEF [5:52] quote about words. |
| C. Correlation -1 to 1 | FIXED | Term box and audio; variance as average squared distance from the mean; covariance added. |
| C. 6.64 | FIXED | "from 13.29 to 6.64 bits, a drop of exactly half (6.64 bits)". Python: log2 10^4 = 13.2877, log2 100 = 6.6439. |
| C. Short answer and Lupia | FIXED | Neither condition: delegation fails; one condition: worst case is the status quo (Theorem 5.1, p. 85, re-read). "could not foresee" is now "may not be able to ... or foresee", inside the "our reading, not a finding" box. |
| C. OQL diagram | FIXED | Node "Executable strategy"; "Only then is there an executable strategy (our gloss)"; "a candidate strategy". Matches Luo abstract. |
| C. Truth Terminal | FIXED | Decrypt alone: "neither the bot nor its handler created the token"; Cointelegraph: the bot did not launch it. $122 million (14 Oct, down from $150 million, Cointelegraph) and over $214 million (16 Oct, CoinGecko, Decrypt) with outlets and dates. Decrypt's date is 16 Oct 2024 (page metadata). Handler "decides whom it interacts with". |
| C. Mik | FIXED | "contractual deepfakes" and "may turn out to be contracts in form only, not in function" are in the introduction; page cites "introduction". |
| C. N&K | FIXED | "advanced but not 'superintelligent' AI (a notion they view as incoherent)"; "median outcome". |
| C. "(ours)" on the Lupia table mapping, section 9, section 12 | FIXED | "works (ours: a plane, where regulators supply the knowledge)"; "Our framing (ours)"; "(ours, to test)" in section 12 and the audio. |
| C. WEF [17:29] in the fold-out | FIXED | Group 3. Quote with "some ... AI persons" elides "USAI"; fair. |
| C. [5:57] premise | FIXED | "As far as putting words in order is concerned, AI already thinks better than many of us" [5:48] before "Therefore, anything made of words ..." [5:57]. |
| C. AlphaGo extension | FIXED | "science, art [27:04] and finance [30:07]": small.en [27:04] "What's true of Go is true of more and more areas. In science, in art ..."; [30:07] "this is a sort of art". |
| C. Poole paired with the right claim | FIXED | "On the claim that chatbots create new ideas, Poole answers ...". |
| C. Source list | FIXED | 30 entries, full titles; 25 URLs fetched: 24 return 200, WEF returns 403 to a bot (the same slug is indexed by search with the same title, so it exists). Books have no URL. Nits: n13, n14. |
| C. `post.json` `cites` pruned | FIXED | 30 cites, all map to a `src-` id; Calvano, Lopez-Lira, Nexus, Mridul gone. |
| C. RegretNet / "approximately incentive compatible" | FIXED on the page | Gone; "Found" says searches toward a fixed goal (our reading). |
| C. Audio "one method" sentence | FIXED | The audio no longer generalises. |
| D. Critic items | Factual content checked | New six-asset toy (6 assets, 3 products of 2, healthy product 1/4, total 1/4 spread vs 1/2 concentrated) rerun over all 15 placements: 12 give 1/4, 3 give 1/2; Delta(2) = 3/4 - 1/4 = 1/2. Option example: 95 pays 1, 120 pays 0 (our definition). 1:1, 4:1, 16:1 and 4^10 = 1,048,576. Covariance and correlation range correct. One wording issue in the Delta fold-out (n6). |
| E. Length | CONFIRMED | `wordcount.py`: main text 6,942 words (cap 7,500), fold-outs 1,853 in 8 boxes. |

### Checker A (verify-2.md) and checker B (verify-2b.md)

All 13 minors and 3 majors of checker A, and 2 majors and 17 minors of checker B, are fixed in the text and, where relevant, in the audio. Specific rechecks:

| Round-2 item | Verdict | Note |
|---|---|---|
| A-M1, B-M1 (personhood and undated forecasts) | fixed | by the four groups |
| A-M2 (D&U) | fixed | above |
| A-M3 (chain) | fixed | above |
| A-n2, B-M2 ([26:33] hedge) | fixed | "AI will beat me. I don't know how long it will take. Two years, five years, ten years, it will beat me" [26:29]-[26:35], marked "outcome asserted; timing explicitly unknown". Small.en and the Q&A boundary ([19:51] "Thank you for listening to this human") re-checked. |
| A-n3, B-m7 (Scheurer) | fixed | |
| A-n7 (short answer) | fixed | |
| A-n8 (OQL node) | fixed | |
| A-n10, B-m5 (sources) | fixed | |
| B-m4 (Decrypt date) | fixed on the page | `sources/MANIFEST.md` still says 14 Oct for TT2 (bookkeeping, not on the page) |
| B-m9 (AlphaGo) | fixed | |
| B-m10 (limits) | fixed | "Our reading: that is a limit on the words thesis" |
| B-m13 (audio "one method") | fixed | |
| B-m17 (Keynes) | fixed | both quotes verbatim in the library text; "§ IV (standard numbering)" is flagged because the library HTML has no IV heading (already known from s2) |

### Writer's claims in response-2.md checked against the text

True: no sentence of the three banned kinds; Prediction 4 reveal has no quotes; the "three ten years" trap moved to the fold-out and says "at least four"; the keypoint paragraph in section 13 is gone; section 9 states the chain once; "approximately incentive compatible" and "deep hedging" gone from the page; numbers added to the option example; every "Lens N picks this up" has a link type; cites pruned; D&U in lever 2; all sources have full titles and URLs or DOIs (books excepted); main text 6,942 words and fold-outs 1,853 in 8 boxes; `dg-seller` redrawn; Ladder 1 defines C_k; the m = 0.67 numeric check is present.

Not borne out (inexact, no new error): m13, "the auction / neural network sentence is removed from the audio". The audio `llm` chapter still says "neural networks that search for auction rules or hedging strategies. Those are searches toward a fixed goal"; this sentence is correct and matches the page. numbers.md was said to be updated, but one row is stale (n12).

## (b) New findings

### Major (2)

**M1. Balance: the Guardian 2024 lines in group 4 are cut before the same paragraph says the opposite** — `box-harari`, group 4, last bullet ("His limits and remedies: concedes, proposes")
- Post: "Computers are not yet powerful enough to completely escape our control" and "As long as humanity stands united, we can build institutions that will regulate AI" [Guardian 2024].
- Source (Guardian, 24 Aug 2024, *Nexus* extract, same paragraph): "Unfortunately, humanity has never been united." Then: "The rise of AI poses an existential danger to humankind, not because of the malevolence of computers, but because of our own shortcomings."
- What is wrong: the post files the first two sentences as Harari's remedy and concession. The two sentences that follow in the same paragraph say the condition ("stands united") has never held and that AI poses an existential danger. The kept hedge ("as long as") is real, but the cut makes him look more hopeful about institutions than he is. Together with the Guardian 2023 line ("by itself I wouldn't describe it as existential"), group 4 presents him as more reassuring than the sources do. The merged list asked for "Computers are not yet powerful enough ..." in group 4, so the omission is in the continuation, not in the chosen opening. The same Guardian 2023 interview also has his unhedged general claim that many dangerous scenarios "taken together ... constitute an existential threat to the survival of human civilisation".
- Severity: **major** (balance rule: central unhedged claim omitted so that he looks less alarmed). It is about AI in general, not finance, and fixable in one clause.
- Fix: end the bullet with "... but, he continues, 'humanity has never been united', and 'the rise of AI poses an existential danger to humankind ... because of our own shortcomings'", and add the Guardian 2023 "existential threat" sentence to group 4 as his unhedged general claim.

**M2. Balance: the "hiding agent" branch is labelled "not his" while Harari asserts, without a hedge, that AIs lie** — `dg-chain` (branch "Our additions, not his", node "Agents may hide their reasons", tag "Ours; Scheurer: one red-team test, no likelihood estimate", step 5), section 4 item 4, section 9
- Post: the dashed branch is "Our additions, not his", with "Agents may hide their reasons" tagged only with Scheurer's cautious "one red-team test". Group 1 lists WEF [2:00] ("It is an agent") and [2:47] ("very creative" agent line).
- Source (WEF 2026, same opening passage, small.en and medium.en): "The third thing to know about AI is that it can lie and manipulate." [2:59]; "The last four years have demonstrated that AI agents can acquire the will to survive and that AIs have already learned how to lie." [3:26]. Also [12:27] "can lie better than us".
- What is wrong: the speech makes three claims in a row (agent, creative, lies). The page quotes the first two as group 1 assertions and omits the third, which is the unhedged claim closest to the page's own hiding-agent branch, then calls that branch "not his" and gives only the cautious red-team evidence. Harari does not say "hide their reasons", and he says nothing about finance there, so "ours" is right for the reasons-hiding mechanism in a trading desk. But "not his" will be read as "he does not say AIs deceive".
- Severity: **major** (balance rule, borderline: the claim is general, not finance-specific; the meta-manager may downgrade to minor).
- Fix: add to group 1 "AI 'can lie and manipulate' [WEF 2:59]; 'AIs have already learned how to lie' [3:26]". Relabel the branch "Our additions (Harari asserts that AIs lie, but not in finance and not about reasons: WEF [2:59])".

### Minor (15)

**n1. A quotation altered** — `box-harari` group 4. Post: "we need to keep humans in the loop" [BIS 22:57]. small.en and medium.en: "technology to help us understand AI, but we'll need to keep humans in the loop" [22:59]. Only base.en has "we need". Fix: "we'll need to keep humans in the loop". (The table row and Lens 4 use only "humans in the loop"; no change there.)

**n2. Two lines sit under headings whose verb does not fit them** — `box-harari`, groups 1 and 3; section 3 table is fine.
- Group 3 ("Imagines, supposes, asks: thought experiments") holds BIS [3:00] "maybe 1% of the population really understands how the financial system works", a hedged present-tense estimate, not a thought experiment. The thought experiment is the next sentence, "What happens if this number goes down to zero?" [3:09]. Fix: relabel group 3 "scenarios, questions and hedged estimates" or move [3:00] to the hook only.
- Group 1 ("capability claims") holds "money is really trust" [23:15], an assertion about money, not a capability. Fix: file it as "other assertions".

**n3. `dg-chain` H3 tag uses FSB statements the page itself calls "background, not a test"** — tag "Evidence: not yet evidenced; FSB p. 1: not widely observed; pp. 28-29: 'could change this'" and step 3. Section 4 correctly says the FSB lines are about AI use cases generating new revenue streams in general and "do not address AI-invented instruments". The merged list asked for this tag, but the tag drops the caveat. Fix: "(background: use cases in general)".

**n4. `dg-chain` H1 tag attributes "enforcement" to Searle; H1 label is stronger than the source** — tag "Evidence: contested, Searle (SEP): acceptance, enforcement; Menger". SEP § 4.2.3 reports collective acceptance and deontic powers; "enforcement" is our addition (the only "enforceability" in the SEP is in the economics passage of § 5.6, about contracts). Node label "Money is made of stories": Ynet says "What gives money value is the stories ...", and at BIS [23:15] he says "Money is not made of gold or silver or paper or anything". "made of stories" is our compression and reads as his wording. Fix: "Searle (SEP): acceptance; Menger; enforcement is ours"; label "What gives money value: stories".

**n5. H4 is "imagined" only for the crash story** — `dg-chain` edge e3 and step 4; section 3 "Our reading". The page lists WEF [31:11] under group 2, "when AIs create a new financial system that they understand and we don't understand", and [31:24] continues "a world in which humans ... can no longer understand how finance functions". That is the H4 outcome in forecast form. The summary "imagines his concrete finance disasters as thought experiments" is right for the crash (BIS [9:54], Broomstick, WEF [31:59] "Maybe nobody in the room"). Also step 3 says "devices" for [31:11], which says "financial system". Fix: step 4: "also predicts the outcome undated (WEF [31:11], [31:24])"; e3 label "imagined / predicted".

**n6. Arora lemon-cost wording and direction of the toy** — `box-lemon` and Ladder 2 / `dg-seller`.
- Post: "With a derivative, Delta depends on where the junk sits." Arora p. 5: Delta(n) is the expected value minus the minimum over all placements, so it is one number; what depends on placement is the conditional value.
- Post toy: the worst placement for the buyer is "spread" (1/4), and the text and diagram say "skewed" and "concentrated" without saying which is damaging. In Arora, with threshold products, concentrating junk in a few pools ("just enough to skew the probability of default") is the damaging placement (WP p. 4). In the AND toy it is the reverse.
- Severity: minor (toy is labelled ours; no claim of equivalence).
- Fix: "what depends on where the junk sits is the value; Delta is the worst case over placements"; add "in this AND toy, spreading is worst; in Arora's threshold products it is concentrating".

**n7. A phrase in quotation marks is not a quotation** — `box-ashby`: 'the last step is "conditioning cannot raise entropy"'. Cover and Thomas write "conditioning reduces entropy" (e.g. their text on the chain-rule steps). Fix: use their phrase with the citation, or drop the quotation marks.

**n8. Locator** — section 9 Personhood: "asks whether your country will recognise them as legal persons, as corporations already are [16:47]". Re-transcribed [16:46]: "Will your country recognize AIs as legal persons?" The corporation point is at [15:14] ("In many countries, corporations are considered legal persons"). Fix: add [15:14].

**n9. Mik is quoted only in her hedged sentence** — section 4 item 1, `dg-llm` step 5, critics list. The abstract and introduction state, unhedged, "LLMs do not understand the meaning of words, have no sense of context and cannot reason" and "This paper seeks to put an end to such unreasonable ideas". The page keeps "may turn out" ("hedge kept: may") but not her stated thesis, which bears on H2 (the chain's "AI masters words" step). Fix: one line in the critics fold-out with her unhedged thesis, and a note in the H2 tag.

**n10. Harari's concession on experts is missing** — hook and group 4. BIS [9:15]-[9:21] (base.en): "we trust experts in many different fields ... it's the same with finance, we don't need everybody to understand everything, this is really impossible." The hook says he called her example "perfect" and "turned to the 2008 crisis", which suggests he moved on. Fix: add the concession to group 4.

**n11. "28 to listen" is not supported** — masthead. No MP3 exists yet. The audio script has about 5,490 spoken words: 33 minutes at 165 words per minute, 37 at 150. Fix: take the time from the MP3 durations after synthesis.

**n12. numbers.md is stale in two places** — section C: "'Ten years from now, it will be too late' (a decision deadline, not a forecast)" contradicts the page and the binding rule (group 2 forecast). "'two to three times higher' correlation | FCIC p. 149" is no longer used on the page. Fix: edit both rows.

**n13. BIS source entry** — Sources. "(2024, 7 May) ... BIS Innovation Summit. Audio." The conversation took place on 7 May 2024 (BIS event page); the audio file we cite is the podcast edition "BISness", published 24 May 2024, with a presenter intro of about a minute, so the [m:ss] stamps belong to that edition. Fix: "Conversation 7 May 2024; podcast edition 24 May 2024, timestamps refer to the podcast".

**n14. Dutting et al. year** — Sources. Cited "(2019)" with arXiv:1706.03459; the file read is v6 (14 Oct 2022). Fix: "(2019; arXiv v6, 2022)".

**n15. Locator and wording for D&U** — Lens 2 lever 2. "and that current frameworks 'cannot effectively prevent and resolve' such crises" has no citation tag and is stated in the introduction as a premise ("As current regulatory frameworks cannot effectively prevent and resolve such AI-induced crises, we outline ..."), not as a result. Fix: add "introduction" and "state".

### Balance check (explicit)

- Harari's unhedged statements now present: BIS [5:14], [16:21], [25:14]; WEF [2:00], [2:47], [5:57], [10:36]; BIS [30:24], WEF [31:11], [16:28], [19:11], [26:29]; Guardian 2023 "ideal field"; Ynet. Missing or cut: M1 (Guardian 2024 continuation), M2 (WEF [2:59], [3:26]), and the hedges kept: "maybe in 10 years", "a couple of years", "I don't know how long it will take", "at least for now", "by itself ... not existential" and "indirectly". His remedies and limits: kept; n10 (concession on experts) is the one missing.
- Danielsson and Uthemann: now at full strength (main result and concession together).
- Narayanan and Kapoor, FSB, Skingsley, Poole, Fox, Arora: hedges and concessions kept at full strength. Mik: n9.
- Scheurer: hedge ("existence proof") and the strong result ("remains high under all prompts") both present.
- Keynes: both quotes verbatim; the "convention" and "fail conventionally" statements are kept apart.

## (c) Counts

- **Critical: 0**
- **Major: 2** (M1, M2; M2 borderline)
- **Minor: 15** (n1-n15)

Round-2 items: all 8 binding items from round 1, all 3 majors and 13 minors of checker A, and all 2 majors and 17 minors of checker B are fixed in the text. Three carry small residuals that are listed above as new minors (n2, n3-n5, n15). The two writer claims that are not borne out do not add errors to the post.

Top three: (1) M1 Guardian 2024 passage cut before "humanity has never been united ... existential danger"; (2) M2 "not his" on the hiding-agent branch while WEF [2:59]/[3:26] says AIs lie; (3) n1 "we'll need" altered to "we need" in a quotation.

## (d) Checked and found correct

**Numbers (all rerun).**
- check.mjs: 15/15 configs OK. Tranche: 0.370%, 5.185% (14.0x), 10.000% (27.0x); p = 0.02: 2.000% vs 0.0032% (634.5x). Counting: 63 (0.0063), 1,023 (0.102), 16,383 (fraction 1), two days k = 20: 1.05e-10; 10^16 contracts; 13.29 bits. Ashby: 9.29, 2.64, 4.29, and 0.00 at V_R = 14. N_eff: 10, 2.703, 1.099, 1; N = 100, rho = 0.3: 3.257 (ceiling 3.33); N = 2, rho = 0.5: 1.333. Bayes: 0.5, 0.8, 0.941, 0.985, 0.996; n = 10: odds 1,048,576, P = 0.999999. Cascade (lgd 0.8): every single seed 1 of 6, every X pair 2 of 6, X1+X2+X3 6 of 6 in 3 rounds, capital x1.5: 3 of 6, x1.2: 5 of 6, x1.21: 3 of 6, x1.25: 3 of 6. Cascade (lgd 1): Y1 alone 3 of 6, every X pair 5 of 6, X1+X2+X3 6 of 6, every other single seed 1 of 6. Herding: m = 0.2: 0.04 up, -1.00 down, 0.000 after 40 steps; m = 0.66 decays (final 0.230); m = 0.67: 2.68 / -2.70, final -0.505; m = 0.9: 1345.97 / -50.21; breaker 3: +/-3.00.
- Python: contract A table 1 / 6 / 9 cells, price 2.0; 2^100 = 1.268e30; 0.0036 + 0.0001; log2 100 = 6.6439 and exactly half of 13.2877; Ashby toy minimum 2 outcomes over all 16 plans; H = 1.75, bound 0.75; N_eff derivation; hand steps -0.9, -0.51, -0.189 and -2.30, -3.94; roots 0.548 / 1.0025 / 1.162, all complex (b^2 < 4c: 0.81 < 1.2; 3.386 < 4.02; 5.29 < 5.40); tipping 2/3; tree of majorities 4 flips for 9 inputs; Granovetter 100 and 1; cascade hand table (12 >= 10, 4 + 8 = 12 >= 9, 4 + 8 = 12 >= 11, 12 < 15); six-asset toy (12 placements at 1/4, 3 at 1/2); plain pool 45 and 5.
- Notebooks ex1 (10.061, 2.712, 1.099, 1.000), ex2 (1, 2, 6, 3 failures), ex3 (0.548, 1.002, 1.162; first m above 1 is 0.67) run and match the text.
- Playground answers (1)-(3) and Exercise 4 solution are correct. Post 01 cross-references (village weather probabilities, H = 1.75, Bayes table 0.50 / 0.80 / 0.941, octopus, the three idioms) are present in post 01.

**Harari, line by line (page and audio), re-transcribed this round.**
- WEF [2:01] "not just another tool. It is an agent"; [2:47] knife line; [5:48]-[5:57]; [6:06] laws; [8:07]; [10:36]; [11:39]; [16:28] "will soon be able to make the decisions necessary to manage a bank account, to file a lawsuit and even to operate a corporation"; [16:43] "AIs can therefore function as persons"; [16:48] "Do we want to allow that? Will your country recognize AIs as legal persons?" (the first window cut this sentence; the re-run from 16:46 is complete); [19:11] and [19:23]; [26:29]-[26:35]; [31:11]; [31:55]-[32:04] "Maybe nobody in the room, no human in the room, understands the financial system anymore".
- BIS [3:00]; [3:30]; [5:14]; [5:27]; [9:54]; [10:19]; [10:27]; [12:42]; [16:21]; [20:46]; [21:37]; [23:15]; [25:14]; [27:04]; [30:07]; [30:24] "I think we'll see AI creativity also in this field coming up with new types of financial devices that no human being would ever imagine creating". Only [22:57] differs (n1).
- Guardian 2023: "ideal field for AI because it's only data", "What happens if ...", "catastrophic risk", "by itself I wouldn't describe it as existential", "It could, indirectly, if it triggers certain kinds of wars or conflicts". Guardian 2024: Broomstick "imagine the following scenario", "bigger even than 1929 or 2008". Ynet: "What gives money value is the stories ...", "better than the average human at telling stories".
- The Q&A boundary: the prepared talk ends at [19:51]; the "ten years" items match the trap: BIS [9:54], Q&A [31:55], talk [19:11], Q&A [26:33].

**Sources.**
- FCIC p. 28 (pdf 57), p. 128 (image), p. 149 (image); Kirilenko abstract and "about 36 minutes starting at 2:32pm ET"; N&K Part I circuit breakers, introduction "control is primarily in the hands of people and organizations", "median outcome"; Luo abstract; Mik introduction quotes; Cointelegraph ($50,000, July 11, $122 million, $150 million peak, handler); Decrypt ("semi-autonomous AI agent", $214 million, "neither the bot nor its handler created the token", published 16 Oct 2024); FSB p. 1 ("not widely observed at present", market correlations), p. 20 (four possible drivers), p. 21 ("as if it were a single institution"), pp. 28-29 ("could change this in the future"), press release; MIT Sloan ("lockstep", "can easily mask who's at fault", 30 Aug 2023, Vereckey); Scheurer abstract, p. 1 (existence proof), p. 8; Duetting p. 3 and Buehler abstract; D&U abstract and introduction; Danielsson et al. 2022 p. 7; Poole and Fox quotes; Guardian bylines and dates.
- Shannon p. 1; Cover and Thomas Theorem 7.2.4 on p. 150 (first-edition text in the library); Akerlof pp. 489-490 ("bad" cars); Arora WP: abstract, p. 1, p. 2 ($1,000, 20%, $800, $200), pp. 3-4 (hidden dense subgraph, unbounded buyer), p. 5 (Delta(n), "position"), p. 6 Table 1, p. 12 (tree of majorities, "probably correct", "clearly only a first step"); Ashby pp. 204-209 (table rule and law on p. 207, misprint on p. 208, "owes nothing to experiment" on p. 209), pp. 246-247 (three levers, "only hope" with its condition); Granovetter pp. 1424-1425 ("essentially identical"); Keynes ch. 12 (both quotes verbatim); SEP § 4.2.3 (stones, Bureau of Engraving and Printing, deontic powers, "X counts as Y in C") and § 5.6 (Menger); Lupia and McCubbins Theorem 5.1 (p. 85, including "the retention of the status quo") and p. 207 n. 2.
- BIS event of 7 May 2024 with Skingsley and Harari (BIS event page). WEF episode title and slug exist (search index).

**Audio script and gloss.** Every chapter compared with the page; spoken numbers match ("six hundred thirty-four", "three point three" for 3.257 and 1/0.3, "exactly half"). Audio-only points: n1 (the same wording is not used in the audio; "keeping humans in the loop"), n11. The audio verbatim summary sentence matches the merged list. english-gloss.json: definitions and the wrong/right pairs hold no factual claims; the page's English examples are consistent with the post.

**Bookkeeping.** No MP3 or `audio/chapters.json` exists, so the "AI4Read from CSS Lab" metadata could not be checked; the spoken intro is in the `hook` chapter. `post.json` summary matches the verbatim sentence. No W4, W5 or "world W" label is visible on the page (the ids `cs-w5` and `st-w5-hand` are internal).
