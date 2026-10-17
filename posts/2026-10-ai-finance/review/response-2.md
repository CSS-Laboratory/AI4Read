# Response to round 2 (post 02), writer, round 3

Every line below was checked against `src/content.html`, `audio-script.md`, `post.json` and `numbers.md` after the last build. "Page" means content.html; section numbers are the page's own. Declined or partly done items say so.

Corrections to response-1.md (two claims were not true there):
- It said "RegretNet named" and that the OQL "the LLM proposed, the checker decided" gloss was removed. Neither was true in the text. Round 3 removes the RegretNet / "approximately incentive compatible" claim from page and audio, and removes the OQL gloss from `dg-llm`.
- It said URLs or DOIs were added to all source entries. Several were truncated. All 30 entries now carry a full title and a full URL or DOI, except the three books (Cover and Thomas, Keynes, Lupia and McCubbins), which have no free URL.

## Merged list (round2-merged.md)
- A (four-group Harari classification): done. Section 3 has one compact table (groups 1-4 with verbs asserts / predicts / imagines-supposes / concedes-proposes). The fold-out `box-harari` is organised by the same four groups and holds every line with its timestamp. The short answer (section 13) and the audio `answer` chapter use the verbatim summary sentence. Section 9 (Lens 4) and `dg-chain` use the groups. No sentence says "his timelines are hedged", "his forecasts are conditionals" or "a policy question, not a forecast" (grep'd). The personhood point is now both a forecast ([16:28], [19:11]) and a policy question ([16:47]) in section 9 and in the fold-out.
- B1 classification: see A.
- B2 Danielsson and Uthemann: lever 2 in Lens 2 now states their main result ("amplifies existing financial system vulnerabilities", crises "faster and more severe", frameworks "cannot effectively prevent and resolve") next to "can both stabilise and destabilise", with the condition (depending on the shocks and how prepared the authorities are). They are no longer listed under Counterweights. Same in the audio `lens-control` chapter.
- B3 `dg-chain`: rebuilt. Harari nodes H1-H4 only, with edges labelled by his status (asserted / predicted / imagined). Under each node an "Evidence" tag (H1 contested; H2 partly; H3 not yet evidenced, FSB pp. 1 and 28-29; H4 2008 only, FCIC pp. 28 and 149). Our additions (shared models; hidden reasons) are in a separate dashed branch labelled "Our additions, not his", tagged "Ours; FSB 'could'" and "Ours; Scheurer: one red-team test". No "shown in toys" label remains. It reveals in five steps. At step 1 the lower half of the frame is empty; that is the cost of the stepwise reveal that the merged list asked for.
- C key minors: each is answered in the checker sections below.
- D1 Lens 1 ladder 2: done (see critic D1 below).
- D2 section 3 repetition: done (see critic D2).
- D3 section 4: done (see critic D3).
- D4 short answer: done (see critic D4).
- D5 covariance and odds line: done (see critic D5).
- D6 wide formulas: done (see critic D6).
- E length: `python3 scripts/wordcount.py` reports main text 6,942 words (cap 7,500). Fold-outs now hold 1,853 words in 8 boxes (round 1 allowed about 1,500). The overshoot is `box-harari` (the full four-group list the merged list asked for, plus the trap) and the longer `box-lemon`.

## Checker A (verify-2.md)
- M1 personhood forecasts mislabelled: fixed as in A above. [16:28] and [16:36] are listed under group 2 (predicts), with "Do we want to allow that?" [16:47] marked as the policy question; [19:11]-[19:23] under group 2. Audio `home` no longer says "a deadline for a decision, not a forecast"; it lists the [16:28] claim in group two (predicts) and only mentions that the fold-out holds the "at least four ten years" trap.
- M2 Danielsson and Uthemann: fixed (merged B2 above).
- M3 chain diagram: fixed (merged B3 above). Title is "Our compression of Harari's chain: his status, our evidence"; the audio `answer` chapter says "our compression of his chain".
- n1 CDO "mostly": now "pools of financial assets, such as the riskier tranches of mortgage-backed securities, sliced into tranches" (FCIC p. 128), page and audio.
- n2 [26:33] hedge: the line is quoted in full in the fold-out under group 2, "AI will beat me. I don't know how long it will take. Two years, five years, ten years, it will beat me", marked "outcome asserted; timing explicitly unknown".
- n3 Scheurer "nearly 0%": now says the discouraging prompts bring the trading to "nearly (but not exactly) 0%", and that once the model does trade its tendency to deceive "remains high under all prompts" (p. 8). Page and audio.
- n4 "already": removed from the BIS [5:14] paraphrase everywhere. "already" remains only inside the WEF [5:48] quote about words.
- n5 correlation and variance: the term box says correlation runs from -1 to 1 (we use 0 to 1) and gives variance as the average squared distance from the mean; covariance is added. Audio matches.
- n6 6.64: Lens 2 now says V_D goes from 13.29 to 6.64 bits, "a drop of exactly half (6.64 bits)". Audio too.
- n7 short answer: "People stay accountable only if..." replaced by the Lupia pattern (neither condition: delegation fails; one condition: worst case is the status quo; hiding removes the first). "could not ... foresee" is now "may not be able to check what nobody can state in a page, or foresee a shared model's failures", inside a box labelled "our reading, not a finding".
- n8 OQL diagram: node "Trade" is "Executable strategy"; step 4 reads "Only then is there an executable strategy (our gloss)".
- n9 handler: "only approves its X posts and decides whom it interacts with" (Cointelegraph). Page and audio.
- n10 source list: full titles and full URLs for all entries (Scheurer, Luo, Dütting now titled; WEF, Guardian, FCIC, KKST, MIT Sloan, Poole, Fox URLs complete).
- n11 Narayanan and Kapoor: "a world with advanced but not 'superintelligent' AI (a notion they view as incoherent)", in Lens 2 and in the critics list.
- n12 "works (a plane)": now "works (ours: a plane, where regulators supply the knowledge)".
- n13 WEF [17:29]: added to the fold-out under group 3.

## Checker B (verify-2b.md)
- M1 undated finance forecasts classed as hedged: fixed. BIS [30:24] and WEF [31:11] are group 2 (predicts) in the table and the fold-out. The key point that said "forecasts ... are conditionals" is deleted. `dg-chain` labels the H2 to H3 link "predicted".
- M2 dropped hedge in [26:33]: same fix as A-n2.
- m1 Truth Terminal "both say": now "Decrypt says neither the bot nor its handler created the token; Cointelegraph says the bot did not launch it", with the two valuations dated and attributed ($122 million on 14 October, from a $150 million peak, Cointelegraph; over $214 million on 16 October, Decrypt).
- m2 handler role: same as A-n9.
- m3 Mik: cited to the introduction, page and diagram.
- m4 Decrypt date: 16 Oct 2024 in the sources and in the numbers.
- m5 source completeness: see A-n10; `post.json` `cites` no longer lists Calvano, Lopez-Lira, Nexus or Mridul, and has a "Guardian 2024" entry.
- m6 Danielsson and Uthemann condition: added (merged B2).
- m7 Scheurer: same as A-n3.
- m8 Poole: now "On the claim that chatbots create new ideas, Poole answers ..."; in the critics list "Poole answers Harari's claim that chatbots create new ideas". Audio the same.
- m9 AlphaGo: "he extends it to science, art [27:04] and finance [30:07]" in the body and the fold-out.
- m10 "limits the thesis": now "Harari adds that, at least for now, there is 'zero evidence that AIs can feel anything' [8:07], and that humans' place 'depends on the place we assign our non-verbal feelings' [11:39]. Our reading: that is a limit on the words thesis." The earlier "locates the human role" sentence is gone.
- m11 [5:57] premise: the premise ("AI already thinks better than many of us" at putting words in order, [5:48]) is quoted in section 3, the fold-out and section 9; [10:36] is in the fold-out.
- m12 "LLMs now translate": "A research pipeline improves LLM translation of plain-language intents into option strategies". Audio the same.
- m13 audio "one method": the auction / neural network sentence is removed from the audio (and the page's "approximately incentive compatible" wording is removed, see critic D3).
- m14 Fox: "Fox notes that in Nexus 'capitalism is hardly mentioned at all'".
- m15 Lens 4 intro: "Our framing (ours): ..." and the "Only this lens shows..." sentence is deleted.
- m16 section 12: "(ours, to test)" added to the base-model correlation claim and the five-prompts claim; audio `work` the same.
- m17 Keynes: "we have tacitly agreed, as a rule, to fall back on what is, in truth, a convention" (§ IV) and "worldly wisdom teaches that it is better for reputation to fail conventionally than to succeed unconventionally" (§ V). Audio the same.

## Critic (critic-2.md)
- Both halves: the short answer now has separate (a) and (b) paragraphs, the literal conditional ("If an AI did invent an instrument nobody can state in a page, then (each step ours, conjectured): (i) ... (iv) ..."), named consequences (losses fall on buyers and lenders; supervisors and auditors can still verify standard menus), and the verbatim Harari sentence.
- D1 (Lens 1, ladder 2): the plain pool stays; "derivative" is defined at first use; a three-sentence tiny toy (6 assets, 3 products of 2, junk placed in two products versus one) gives totals 1/4 versus 1/2, computed in Python (numbers.md); "intractable" is explained as "no known fast method, and none is expected (a conjecture)"; the C(100,10) aside is removed from the text and from the diagram; the unused "metaphor" tag is removed; `dg-seller` is redrawn to show the two placements; Instance / Question / Mechanism / Formula / Check are short separate lines in Ladders 1 and 2. Ladder 1 now defines \(C_k\) so that the formula is one short line. (Ladders 3 and 4 keep the run-in layout; not changed.)
- D2 (section 3): one table; the "three ten years" trap moved into the fold-out (now "at least four"); the Prediction 4 reveal has no quotes; the keypoint paragraph in section 13 is deleted; section 9 states the chain once, using the groups (the compression is stated once there; the [5:57] quote still appears in sections 3 and 9, because Lens 4 tests it).
- D3 (section 4): "approximately incentive compatible" and "deep hedging" are gone (Found now says searches toward a fixed goal, our reading); the option example has numbers (index at 95 pays 1, at 120 pays 0); every "Lens N picks this up" note carries a link type.
- D4: see "Both halves" above.
- D5: the term box defines covariance; the Lens 3a text has "1:1, 4:1, 16:1".
- D6: wide formulas split or shortened; I measured every display equation at 390 px with Playwright: 0 of 11 clipped now (before: 5).
- Other critic items done: table rule is its own paragraph (Lens 2); Lens 3a meta line renamed ("Decision lens: correlation, Bayes and conventions"); Ladder 4 has a numeric check at m = 0.67 (Am = 1.005); the Lupia broker example is plugged back into the table ("knowledge no, incentive no is the broker who sells you whatever he likes"); "Our test (ours)" is shorter and marks "(ours)" once; "Link to the lenses" sentence added to the 2008 section.
- DECLINED: turning Ladder 4's worked numbers into a table (the paragraph stays; the new m = 0.67 sentence covers the missing check). Reason: words and layout risk with no new fact.
- DECLINED: moving "What to try" next to the toys. It is short and the toys are linked from it.
- DECLINED: cutting "Small fixes" in section 15. WRITING section 8 requires small error fixes.
- DECLINED: cutting the $122M / $214M detail. The merged list asks for those figures with their dates and outlets, so they stay.
- Audio: the home chapter now gives the four groups once; the chapter says what `RANGE(index, 90, 110)` means. I did not shorten the "three layers" sentence further. The audio has not been synthesised, so I checked the new quotes against the page text and the saved transcripts, not by listening.
