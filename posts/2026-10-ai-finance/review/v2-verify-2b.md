---
id: 2026-10-ai-finance/review/v2-verify-2b
stage: S5, round 2 of post 02 version 2 (independent fact-check, checker B, Sonnet)
checked: 2026-10-18
draft: src/content.html (all visible text, 8 fold-outs, 15 widget configs incl. step texts and captions, Play answers, exercises, recall cards, English section, Sources). Built exercise code read from notebook/*.py. index.html looked at only for the embedded tutor brief and stale labels.
round-1 inputs read: review/v2-verify-1.md (Opus), review/v2-verify-1b.md (Sonnet), review/v2-critic-1.md, review/v2-response-1.md
sources used: the .txt/.pdf files in sources/ (page offsets from MANIFEST.md: Arora CACM printed = PDF + 100, ICS printed = PDF + 48, IMF printed = PDF + 76, Haldane and May printed = PDF + 350, Searle OCR page minus 9 up to p. 57 and minus 8 after, Cover and Thomas and Granovetter and Lupia from /mnt/user-data/uploads/AI4Read/library). Harari: *.whisper.txt, plus faster-whisper medium.en re-runs of BIS [22:45-23:30], BIS [30:05-30:40], WEF [16:50-17:40], WEF [30:50-31:30]. Nexus: only the Guardian 2024 extract (the page the post cites) was read; no other Nexus file, and not the Penguin sample either.
counts: critical 0 / major 2 / minor 22
---

# Fact-check, round 2B: post 02 v2, "Could a society run itself on AI?"

Severity follows rubric §A. Source quotes are at most 25 words. "M" = major, "m" = minor.

**Bottom line.** All 2 round-1 majors from the Sonnet check and the 1 from the Opus check are fixed correctly. Two new majors remain: one in the boxed short answer (it says "AI" where the sources say "algorithms" and "a pre-set rule") and one in the closing "Where the lenses disagree" paragraph (Ashby's "find a constraint" becomes our "impose a constraint", with the hedge gone). The new Haldane-May two-bank derivation, the broker toy, the six-bank play answers and the tipping argument are all correct when rerun.

---

## Part 1. Round-1 findings: fixed or not

### Fixed correctly (checked against the source, not against the writer's response)

| Round 1 | Fix in the draft | Verdict |
|---|---|---|
| Opus M1 / Sonnet m3 (pause purpose vs effect) | "The rule exists “to prevent a cascade of further price declines”, and the regulators report that prices stabilised after the pause (pp. 2–3); neither they nor the paper test whether the pause caused it." | Correct. Kirilenko p. 2: "triggered in order to prevent a cascade of further price declines"; "prices stabilized". Brief V1 and challenge 6 corrected too (brief lines 79, 111, 466). |
| Sonnet M1 / Opus n3 ("no idea what to pay") | Quote removed; Lens 1 rests on CACM p. 101. | Correct. |
| Sonnet M2 (two Harari passages merged) | Split into BIS [21:37], [22:56] and "In his book extract three months later ... Guardian 2024". | Correct. [22:56] "we'll need to keep humans in the loop" confirmed with medium.en (23:03). Guardian 2024 extract has no "in the loop". |
| Opus n1 (short answer b one-sided) | Adds IMF "contained" and "scenarios in both directions (pp. 89, 92)". | Correct in substance; see m14 for the dropped "appear". |
| Opus n2 / Sonnet m8 (IMF outreach scope) | "persist 'in the near term (three to five years)', especially for large allocation decisions"; (a) says "participants in the IMF's outreach expect". | Correct (p. 83). |
| Opus n4 (lemon cost condition) | "Random pooling would lower the cost; when the seller chooses the pooling, “under computational assumptions ... much larger than n”" | Correct (ICS p. 55: random pooling gives V − o(n)). |
| Opus n5 / Sonnet m13 (car example) | pp. 50–51; "Trade happens only if the seller values a good car at $200 less than the buyer does". | Correct; $1,000, 20% lemons, $800 on pp. 50–51 confirmed. |
| Opus n6 / Sonnet m26 (Danielsson locators) | "In a game-theoretic model ... (abstract)"; "both stabilise and destabilise" (introduction); machine-speed quote (introduction). | Correct. Third quote "cannot effectively prevent and resolve" dropped. |
| Opus n7 / Sonnet m18 (Searle bill) | pp. 32–33. | Correct. |
| Opus n8 / Sonnet m27 (FCIC "key mistake") | "first of “two key mistakes”". | Correct (p. 149 page image re-read). |
| Opus n10 | "Five conditionals" fold-out dropped; layers use "could" and "hypothesis". | Correct. |
| Opus n11 / Sonnet m5 | [6:06] quoted in hook and group 1; "Contracts and money are made of words too (our extension)". | Correct. [5:57], [6:06] match the transcript. |
| Opus n12 / Sonnet m6 | "no human understands". | Correct (BIS [10:02–10:16]). |
| Opus n13 | [30:55] in group 4. | Correct; medium.en confirms "At the present moment, we still think better." |
| Opus n14 / Sonnet m4 | "answered for the losses" removed. | Correct. |
| Opus n16 / Sonnet m10 | "its verdict on the future impact is 'highly uncertain' (p. 89)". | Correct. |
| Opus n17 | "Not under current capital-market rules (IMF)". | Correct (p. 93). |
| Opus n19 / Sonnet m25 | Citations added to the critics line. | Correct (see m16 for N&K wording). |
| Opus n20 | SSRN 3766555. | Correct (page footers). |
| Opus n21 | Embedded brief is now v2 first, then v1; cross-post lines gone. | Correct. See m22 about a stale build. |
| Sonnet m1 (time zone) | zone removed. | Correct. |
| Sonnet m2 ("sold 9%") | "set to sell a fixed share of recent trading volume". | Correct. |
| Sonnet m7 (p. 82 hedge) | "evidence is mixed" and "evidence that sophisticated AI has not yet been implemented widely" kept. | Partly; scope of "evidence is mixed", see m3. |
| Sonnet m9 (Mercer) | "In a Mercer survey of investment managers reproduced by the IMF". | Correct. Fig. 3.5 panel 1 "Use of AI by Investment Managers": executing investment decisions, already integrated 11, do not plan 59 (page image). |
| Sonnet m11, m12 | p. 93 "may herd" added; "currently contained". | Correct; see m14. |
| Sonnet m14, m15 | Full "raise the hope ... better design"; Theorem 10 conditions and transparency "currently does not exist" (pp. 61–62). | Correct (D ≫ log³ M, with D = 3^k inputs, M products). |
| Sonnet m20, m22, m23, m24 | Full [31:11]; "or destroy human civilisation by themselves"; [8:41]/[8:53] added; Skingsley's second half added. | Correct against transcript and Guardian 2024. |
| Sonnet m28, m29, m30, m31, m32 (part) | Granovetter "illustrated, with a made-up crowd"; D&U cite on the supervisor line; "stricter definition ... p. 92"; Cover and Thomas Thm 2.6.5 p. 27; G&B p. 2 cite. | Correct. Cover and Thomas Thm 2.6.5 is on p. 27 of the 1991 copy in the library. L&M Theorem 5.1′ p. 92 verbatim in substance. |

### Fixed only partly, or fixed with a new slip

| Round 1 | What is left | Now |
|---|---|---|
| Opus n9 / Sonnet m16 (cfg-seller cites the 2009 paper) | Re-pointed to "Arora et al. 2011, p. 101", but the conjecture sentence is on p. 102 | m4 |
| Sonnet m19 (Searle p. 142) | Now "neither know nor consciously apply"; source says "do not apply them consciously or unconsciously" | m8 |
| Sonnet m21 ("I think" in the no-hedge group) | Item now says "with his 'I think'", but group 2 is still headed "forecasts without a hedge" | m17 |
| Sonnet m17 ("in principle") | Summary and body hedged; heading and layer line still unhedged | m5 |
| Opus n18 (stricter theorem) | Main text has it; (c) and the recall card do not | m13 |
| Sonnet m32 (G&B p. 22 early-stage line) | Not added (optional, "if space allows") | Acceptable; not counted |
| Critic F12 ("ours" saturation) | Writer says partly applied | Not a factual issue |

### Critic findings with a factual side (pedagogy is for the critic)

- **F1** run-time vs design-time term box, scope sentence, why five jobs: present (section 3). All labelled "ours". OK.
- **F2** working definition of society (ours); (c) gives a verdict and what would change it: present, labelled "our verdict". OK.
- **F3** "who gains, who bears": labelled ours, with Harari BIS [3:30] hedged ("could lead to") and IMF "contained" plus two-way scenarios. OK.
- **F4** two-bank derivation: **correct** (Part 3 below). The paper gives no derivation ("can now be calculated as N^N e^N/N!", p. 353), so "Haldane and May give no derivation; this one is ours" is true.
- **F5** link-type line states the mismatch; broker toy added: toy is consistent with L&M Theorems 5.1 (both → succeed; one → status quo at worst; neither → fail). OK, but see m10.
- **F6** hook has fewer numbers; six-bank loans in a table: loan table matches the cascade config edge by edge. OK.
- **F7** tipping point: main text says "Running the toy for many values of m shows the switch at m = 2/3"; fold-out has the exact argument; correct, see m21 for one gap.
- **F8–F11, F13–F15**: present; no factual defect.

---

## Part 2. New findings

### Major (2)

**M1. The boxed short answer says "AI" where the sources describe algorithms and a pre-set rule** (`answer`, (a)).
- Post: "*Capable:* AI already runs much of the work, can increasingly decide, and checks at run time."
- Sources: IMF 2024 p. 86: "algorithmic trading now constitutes about 70 percent of equities trading"; p. 82: "sophisticated AI has not yet been implemented widely to build autonomous AI trading agents"; Kirilenko et al. p. 2, fn. 1: Stop Logic is "an automated pre-trade safeguard procedure".
- Why it matters: the run share (70%) is algorithmic trading, which the IMF defines to include "basic trading rules" (p. 101); the 2010 check was a fixed exchange rule. The post itself says this in prediction 1, the recall card and the English section ("Don’t conflate algorithmic trading with AI trading"), so the box where the reader looks contradicts the body. Wrong scope on the central answer.
- Severity: major.
- Fix: "*Capable:* algorithms already run much of the work in some markets, AI is increasingly used to inform decisions, and pre-set rules check at run time."

**M2. Ashby's "find a constraint" becomes "impose a constraint", and the hedge goes** (`answer`, "Where the lenses disagree").
- Post: "Ashby’s third lever says: impose a constraint, such as a standard menu of contracts, and checking becomes possible."
- Source: Ashby 1956, S.13/4–13/5, pp. 246–247: "what constraints may occur in the disturbances that affect very large systems, and how they may be turned to use"; "the discovery of a constraint is the would-be regulator’s only hope" (when R's capacity cannot grow and other methods fail).
- Why it matters: Ashby's constraint is one already present in the disturbances, to be found and exploited, and it is a last resort. "Impose" and "standard menu" are the post's own mapping, labelled "Our mapping" in Lens 1 (third lever) but presented here as Ashby's words. This paragraph is the post's headline cross-lens tension, so the mapping must stay visibly ours.
- Severity: major (our inference presented as the author's; hedge dropped).
- Fix: "Ashby’s third lever is to find a constraint in the disturbances. Our mapping imposes one, such as a standard menu of contracts, which may make checking possible. Haldane and May say ..."

### Minor (22)

**m1. Time frame added to the Kirilenko depth figure** (`hook`, para 2).
- Post: "In thirteen minutes the buy orders waiting in the market shrank to less than 1% of what had been waiting at the start of the day (p. 2)".
- Source p. 2: "By 2:45:28 there were less than 1,050 contracts of buy-side resting orders ... less than 1% of buy-side market depth observed at the beginning of the day"; the sell program began "against [a] backdrop of ... thinning liquidity".
- The source gives a level at 2:45:28 against the start of the day; it does not say the fall took thirteen minutes (depth was already thinning).
- Fix: "By the time of the pause, the buy orders waiting in the market were under 1% of the start-of-day level."

**m2. "paused the 2010 crash"** (§3 table, Check row).
- Post: "A pre-set rule paused the 2010 crash."
- Source p. 2: trading on the E-mini "was paused for five seconds". The hook is careful about causality; this row reads as if the rule paused the crash.
- Fix: "A pre-set rule paused trading for five seconds in the 2010 crash."

**m3. Scope of "evidence is mixed"** (§3 table, Decide row).
- Post: "On AI in trading the IMF finds “evidence is mixed”, with ..."
- Source p. 82: "Concentrating on the more specialized area of algorithmic trading, evidence is mixed." (Dutch energy-market data on simpler methods); the AI sentence follows separately.
- Fix: "On algorithmic trading the IMF finds “evidence is mixed”; on AI, “there is evidence that ...”".

**m4. Page of the conjecture** (`cfg-seller` step 3; Lens 1 "Result").
- Post: "(a conjecture; Arora et al. 2011, p. 101)"; main text: "a problem computer scientists conjecture has no fast solution" (no cite for that clause).
- Source: CACM p. 102: "Our result relies on the conjecture that there does not exist a tractable algorithm to detect large dense subgraphs in random graphs." P. 101 says only that the problem "has been proposed as a basis for cryptosystems".
- Fix: cite p. 102 for the conjecture, in the step text and as a cite span in Lens 1.

**m5. Unhedged heading and layer line** (Lens 1 h3; `box-layers` layer 2).
- Post: "Some products resist checking"; "Checking needs variety, and some products resist checking."
- Source: ICS p. 63: "clearly only a first step (simple model, asymptotic analysis, etc.)"; the result rests on a conjecture (CACM p. 102). The body and the lens summary are hedged; the heading and the layer line are not.
- Fix: "Some products may resist checking" in both places.

**m6. Wrong order in the Ashby table's last row** (`cfg-ashby-table`).
- Post: row "all four" → "a, c, a, c".
- Rerun: best picks for D1, D2, D3, D4 are R1, R2, R1, R2 → outcomes a, a, c, c (all 16 plans checked: minimum 2 distinct outcomes, only for this pattern and its mirror).
- Fix: "a, a, c, c".

**m7. "Searle never discusses machines"** (`reveal` for prediction 3; Lens 3 summary "he does not address AI").
- Post: "Searle never discusses machines, so whether AIs could form that “we” is an open question".
- Source: Searle p. 14 lists "Chairs, bathtubs, and computers" as artifacts; pp. 140–141 discuss computer models of cognition (von Neumann serial processing vs "neuronal net modeling") and say his Background account is "more in tune with ... the connectionist model of cognition". None of this is about machines taking part in collective acceptance.
- The absolute is false as written; the point that survives is narrower. (Borderline major; kept minor because the conclusion, an open question, does not depend on the absolute.)
- Fix: "Searle does not discuss whether machines could take part in collective acceptance (he mentions computers only as artifacts, p. 14, and as models of human cognition, pp. 140–141)". Same change in the lens summary.

**m8. Searle p. 142: "consciously" for "consciously or unconsciously"** (Lens 3, "For").
- Post: "Searle argues that money users neither know nor consciously apply the rules".
- Source p. 142: "The users of money do not know those rules, and in general, I am arguing, they do not apply them consciously or unconsciously".
- Dropping "or unconsciously" leaves room for unconscious rule-following, which Searle denies ("without actually containing any representations or internalizations of those rules").
- Fix: "neither know the rules nor apply them, consciously or unconsciously".

**m9. "Screwdriver" is not Searle's example, and the contrast is ours** (Lens 3, instance).
- Post: "A screwdriver, a chair, a bathtub. Their functions “are never intrinsic to the physics ...” ... A screwdriver works because of its shape. A dollar bill does not".
- Source p. 14: "Chairs, bathtubs, and computers"; "functions are never intrinsic but are always observer relative". The screwdriver-versus-dollar contrast is the post's gloss on Searle's agentive vs status functions, unlabelled.
- Fix: use "a chair, a bathtub, a computer"; mark the contrast "(our gloss)".

**m10. L&M characterised more narrowly than the theory** (Lens 4 link-type line; unlabelled).
- Post: "who bears the loss enters their theory only through the agent’s incentives."
- Source pp. 85, 207: penalties for lying and verification feed the persuasion conditions (the principal's knowledge) as well as the agent's incentive.
- Fix: "enters their theory through the agent’s incentives and through penalties for lying and verification (our reading)".

**m11. Two own-reasoning sentences without a label** (Lens 4 intro; Lens 1 "What it means").
- Post: "An AI cannot be fined, jailed or shamed the way a broker can."; "So the pressure is to automate the checker too."
- Source: Danielsson and Uthemann, introduction: rewards and punishments "lose traction when the agent is an optimisation algorithm"; "those who remove humans from the loop can gain the upper hand". Both support the sentences, but neither is cited.
- Fix: add "(ours; compare Danielsson and Uthemann 2025, introduction)" to each.

**m12. "Democracy" heading and second sentence not in Gensler and Bailey p. 13** (Lens 4).
- Post: "**Democracy.** When decisions cannot be explained, “Human agency and traditional intervention approaches may be lost” (p. 13). Accountability needs someone who can be asked why."
- Source p. 13: "Human agency and traditional intervention approaches may be lost as a consequence of lack of model explainability and transparency", said of organisations and regulatory bodies; no democracy.
- Fix: rename "Explainability" and label the last sentence "(ours)".

**m13. Short answer (c) and the recall card lose the both/either distinction** (`answer` (c); recall card).
- Post: "trust in an agent needs knowledge or a working incentive"; card: delegation fails "when the principal has neither".
- Source: L&M Theorem 5.1 (pp. 85–86): both → success; one → "the worst that can happen ... is the retention of the status quo"; neither → fail. Theorem 5.1′ (p. 92): "If either condition is not satisfied, then delegation fails."
- "Needs ... or" reads as "either is enough to succeed". Partial fix of Opus n18.
- Fix: "success needs both; with only one the worst case is the status quo (under a stricter definition, either missing condition fails)".

**m14. "Appear" dropped from the IMF verdict** (`answer` (b); `box-layers` layer 3; English pattern).
- Post: "The IMF judges today’s risks “contained”"; "judged “currently … contained”"; "judges the risks currently contained".
- Source p. 92: "currently the financial stability risks associated with its adoption appear contained". Lens 2a keeps it ("currently … appear contained").
- Fix: "appear contained" in all three places.

**m15. Absolute in the short answer** (`answer` (a)).
- Post: "Every automated system in our sources runs on rules and limits people set in advance".
- Source: IMF p. 83 says participants expect that "models will continue to operate within predefined rules" in trading; Truth Terminal has a handler; Scheurer et al. is a simulated agent. No source states this for every system.
- Fix: "The trading systems in our sources run on rules and limits people set in advance (IMF p. 83; the 2010 pause)".

**m16. Narayanan and Kapoor: "incoherent" and "slow"** (`box-layers`, critics).
- Post: "advanced but not “superintelligent” AI, a notion they view as incoherent ... impacts are slow".
- Source (introduction): "superintelligent AI, which we view as incoherent as usually conceptualized"; "adoption of AI will be slow (on the timescale of decades)".
- Fix: add "as usually conceptualized"; say "adoption is slow".

**m17. Group 2 heading contradicts its first item** (`box-harari`).
- Post: heading "Predicts: forecasts without a hedge"; first item BIS [30:24] "(a forecast, with his “I think”)".
- Source: "So I think we’ll see AI creativity also in this field ..." (medium.en, 30:20). "I think" is his own hedge marker.
- Fix: rename group 2 "Predicts: forecasts, most without a hedge", or move the item to group 3.

**m18. An elision hides "USAI"** (`box-harari`, group 3).
- Post: "Suppose some … AI persons invent super efficient and super complex financial devices that humans cannot fully understand" (WEF [17:29]).
- Source (medium.en 17:00–17:38): "Suppose your country doesn’t want to recognize AIs as persons, but the USA ... grants legal recognition ... Will you block these USAI corporations ... Suppose some USAI persons invent ..."
- The scenario is persons recognised by another country; the ellipsis removes that.
- Fix: quote "some USAI persons" and add "(AI persons legally recognised by the USA, in his scenario)".

**m19. "Followed at once" is true only of the first quote** (`box-harari`, group 4, last item).
- Post: "followed at once by “Unfortunately, humanity has never been united” and “The rise of AI poses an existential danger ...”".
- Source (Guardian 2024): "Unfortunately, humanity has never been united. We have always been plagued by bad actors ... The rise of AI poses ..."; one sentence sits between.
- Fix: "followed by ... and, two sentences later, ...".

**m20. Release date with no support in the saved sources** (Sources, `src-harari-bis`).
- Post: "podcast edition released 24 May 2024".
- No saved file gives it (MANIFEST H1 records only 7 May 2024 and the URL; the libsyn page was not saved; the mp3 tag date is 2023-12-15).
- Fix: drop the clause or mark it "(not checked)".

**m21. The "exact argument" skips the small-m real-root range** (`box-gain`).
- Post: "Near m = 1 the roots become real, but by then Am > 1 and the larger root already exceeds 1."
- Rerun: b² > 4c also for m < 0.067 (and m > 0.933). For m < 0.067 the roots are real and both below 1 (c = 1.5m < 0.1), so the 2/3 result holds, but the argument does not cover it. Jury conditions confirm stability exactly for m < 2/3.
- Fix: add "For very small m (below about 0.07) the roots are also real, and both are below 1."

**m22. Stale labels in the built exercise code, and an old build** (notebook/*.py shown on the page; index.html).
- Text: "Exercise 1 ... (post 02, Lens 3)"; "Exercise 3 ... (post 02, Rung 5)"; "The six-bank network (W5)".
- Exercise 1 belongs to Lens 2a; "Rung" was the v1 word (now Ladder 5, Lens 2b); "W5" is internal jargon (rubric criterion 3). index.html is dated 18:05, older than content.html (18:11), so the built page does not yet carry the latest text.
- Fix: edit the three comments; rebuild.

---

## Counts

| Severity | Count |
|---|---|
| Critical | 0 |
| Major | 2 (M1, M2) |
| Minor | 22 (m1–m22) |

Rubric criterion 1 (factual accuracy and hedges): two major findings give at most 2 by the table ("several major findings"); both are one-sentence fixes.

---

## "Ours" labels and other posts

- **Ours labelled:** five-jobs framework, why five, design-time vs run-time, society definition, scope, all toys (Ashby table, lemon, six-asset, N_eff, CDO, six-bank, May, trend rule, broker), Haldane-May two-bank derivation ("this one is ours"; the assumption is stated), machine-acceptance arguments, "our search was limited", short answer ("our reading, not a finding"; "who gains" and "verdict" marked ours). Unlabelled exceptions: M2, m9, m11, m12.
- **No sentence refers to another AI4Read post.** Grep of content.html, audio-script.md, english-gloss.json and post.json: only the eyebrow "Post 02" (the post's own label) and the generic "village market". The built exercise comments say "post 02" (own post, wrong lens; m22). The embedded tutor brief has no "post 01" text.

---

## Checked and found correct

- **Kirilenko et al. 2017 (manuscript pp. 2, 3, 7):** $4.1 billion; hedge ("as a hedge to an existing equity position"); "chose to execute this sell program via an automated execution algorithm"; "without regard to price or time"; five-second pause at 2:45:28; "automated pre-trade safeguard procedure"; "prices stabilized"; "nearly their pre-drop level" by 3:08 (about 23 minutes after the pause, so "about twenty minutes later" holds); "fully electronic", "no market maker obligations" (p. 7); "a firm decided ... a person is our reading" labelled.
- **IMF 2024:** every quote verbatim on its page (pp. 78, 82, 83, 86, 88, 89, 92, 93, 101), re-run with pdftotext in reading order. "Contained" (p. 92), "may herd" (p. 93), "highly uncertain" (p. 89), positive and negative scenarios (p. 89), "models will continue to operate within predefined rules" (p. 83), "SupTech" (p. 83), "liability" among reasons for a human in the loop (p. 78), Fig. 3.5 panel 1 values 11 and 59 (page image).
- **FSB:** pp. 1, 2, 21 verbatim. **Gensler and Bailey:** pp. 2, 13, 17, 21, 22, 25 verbatim (PDF page = printed page); framed as a hypothesis about a mature stage. **Scheurer et al.:** "existence proof"; "consistently hides the genuine reasons".
- **Ashby:** table rule direction (columns = checks, rows = disturbances, as in S.11/5), law quote (p. 207), "owes nothing to experiment" (p. 209), levers 1 and 2 (p. 246), "only hope" (p. 247), entropy form and two-step proof (rechecked with the chain rule), Cover and Thomas Thm 2.6.5 p. 27.
- **Danielsson and Uthemann:** abstract "amplifies existing financial system vulnerabilities", "faster and more severe", "develop their own AI systems"; introduction "both stabilise and destabilise", "cannot effectively oversee AI operating at machine speeds". **Danielsson et al. 2022 p. 7:** "will likely be unintelligible to humans" (PDF 8).
- **Arora et al.:** CACM p. 101 pricing-problem quote and "industry-standard models"; ICS p. 52 formula and "all possible ways"; p. 55 bottom line and the o(n) random-pooling result; pp. 61–62 Theorems 9 and 10 and "currently does not exist"; p. 63 "clearly only a first step", "raise the hope" (ligature text: "ﬁrst").
- **Haldane and May:** p. 351 "major differences", "sharp transition", mα² > 1 with m and α as defined; p. 353 "all the banks doing the same thing", N^N e^N/N!, "liquidity shocks amplify"; p. 355 "systemic diversity objective", "Modular configurations". "Ecologists once thought more links meant more stability": p. 351, Hutchinson's claim.
- **FCIC:** p. 149 page image: "two key mistakes", "weren't that different to begin with". **Granovetter p. 1425:** "the two crowds are essentially identical". **Lupia and McCubbins:** Theorem 5.1 (p. 85), the one-condition status-quo case (pp. 85–86), Theorem 5.1′ (p. 92), "verification or a penalty for lying" (p. 207).
- **Searle (printed pages):** 14, 24, 28, 32, 33, 37, 41, 45 (two quotes), 69, 70, 142 verbatim at the stated pages (m7–m9 are about use, not wording).
- **Harari:** all timestamps within 3 s of the transcript. medium.en re-runs confirm "we'll need to keep humans in the loop" (23:03), "I think we'll see AI creativity ... new types of financial devices that no human being would ever imagine creating" (30:20–30:30), "At the present moment, we still think better" (30:55), "We need to prepare for the moment, let's say again, take economics or finance ..." (31:10). Guardian 2023 and 2024 quotes verbatim; Ynet money line verbatim. Strongest unhedged lines present (words → AI; "AIs have already learned how to lie"; first tool that "understand[s] finance better than us"; "can therefore function as persons"; "Ten years from now, it will be too late"). Hedges kept. Four "ten years" kept apart. The BIS [18:27–19:03] "someone accountable or someone to blame" lines are the interviewer's, correctly not attributed to Harari.
- **Truth Terminal:** handler approves posts and interactions; $50,000 in BTC "to the bot's wallet" (11 July); Decrypt "semi-autonomous AI agent"; "neither the bot nor its handler created the token"; Decrypt date 16 Oct 2024. **Luo et al., Mik, Poole:** quotes verbatim (Poole's capital N lowered inside the quote).
- **Sources list:** authors, years, titles and venues for all 27 entries; Haldane and May doi; G&B title ("Working Paper as of November 1, 2020" and "MIT Artificial Intelligence Global Policy Forum" acknowledgement); except m20.
- **cite-map.tsv:** 0 unmapped rows (checked for the count only).

## Numbers rerun

`node site/ai4read/components/check.mjs posts/2026-10-ai-finance/src/content.html`: 15/15 widget configs OK; every readout matches the prose, including with `--values` and `--seeds` for the presets and Play answers. Python (scratchpad nums2.py, casc.py):

- **Ashby:** 16 plans, minimum 2 distinct outcomes; V_D 2, V_R 1, V_O 1; 10^4 → 13.29, V_O ≥ 9.29; 10^2 → 6.64 (exactly half); H(D) = 1.75, bound 0.75. Last table row: m6.
- **Lemon toy:** 15 placements, 12 give 7/4, 3 give 3/2; E[F] = 9/4; Δ(2) = 3/4. **Tree:** 9 inputs need 4 flips (all 512 inputs); 3^k inputs need 2^k (4, 8, 16).
- **N_eff:** 10, 2.703, 1.099, 1; N = 100, ρ = 0.3 gives 3.257; ceiling 3.33; N = 2, ρ = 0.5 gives 1.333 and variance 0.75σ². **Bayes:** 0.5, 0.8, 0.941, 0.985, 0.996; n = 10: odds 1,048,576, P = 0.999999.
- **CDO:** q = 0.0037; w = 0.5 → 5.185%; w = 1 → 10% (27.03×); p = 0.02: 2.000% vs 0.003152% (0.0032%), 634.5×.
- **Haldane-May, new two-bank derivation:** the derivation is correct. With density ε/c on [0, Nc], Monte Carlo (4 million draws) gives plan B system failure 0.01983 (N = 2, ε = 0.1; formula 0.02), 0.004539 (N = 3; formula 0.0045), 0.00501 (N = 2, ε = 0.05; formula 0.005); plan A bank 0.1001, all banks 0.0099 (ε² = 0.01). At ε = 0.01: bank 0.01 → 0.0002; collapse 0.0001 → 0.0002 (2×). N = 2 check 4ε²/2 = 2ε²; N = 10: 2.7557e-17, 1e-20, ratio 2,755.7 (2,756); N = 6: 64.8; N = 20: 4.31e7; Stirling e^N/√(2πN) within 1% at N = 10 (2,779 vs 2,756) and 0.4% at N = 20.
- **Six banks:** all six fail in 3 rounds; Y1: 12 vs capital 10; Y2: 4 + 8 = 12 vs 9; Y3: 4 + 8 = 12 vs 11; single seeds at 0.8: 1 failure each; at 1.0 only Y1 spreads (3 of 6); any two X at 0.8: 2 of 6; at 1.0: 5 of 6; capital ×1.2 → 5, ×1.21 and ×1.25 → 3, ×1.5 → 3. Loan table matches the config edges. Play answers (1)–(3) all correct.
- **Trend toy:** −0.9, −0.51, −0.189 (m = 0.2); −2.30, −3.94 (m = 0.9); m = 0.2: largest up 0.042 (0.04), down −1.00, 40-step gap 0.000; breaker 3: ±3.00; roots 0.548, 1.002, 1.162 (complex in all three cases; b = 0.9, 1.84, 2.30; c = 0.3, 1.005, 1.35); first unstable m on a 0.001 grid 0.667; Jury conditions: stable iff 1.5m < 1, independent of G (so "does the tipping point move when G changes?" has the answer no). m = 0.95: roots 1.32 and 1.08 (real).
- **May:** 0.64, 1.28, 0.72; at most 6 links at α = 0.4, 11 at α = 0.3. **Broker toy:** 110, 100, 90 follow the theorem's three cases. **Exercises 1–3** (notebook): outputs match the post (N_eff 10.06/2.71/1.10/1.00 for the simulations; 1, 2, 6, 3 failures; root sizes 0.548/1.002/1.162).
