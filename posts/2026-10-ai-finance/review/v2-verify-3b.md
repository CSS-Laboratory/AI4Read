---
id: 2026-10-ai-finance/review/v2-verify-3b
stage: S5, round 3 (final) of post 02 version 2 (independent fact-check, checker B, Sonnet)
checked: 2026-10-18, 18:25 to 18:47 (JST)
draft checked: src/content.html as of 18:37:38 (110,310 bytes, 653 lines, main text 7,402 words). The file changed during the review (18:29 version: 640 lines; 18:37 version: 653 lines, with the new two-bank figure, a new Ladder 3 "What it means", a shortened short answer (a), a trimmed Signs to watch). I re-read the whole 18:37 file and confirmed by `cmp` that it did not change again before I finished. All findings refer to the 18:37 version.
inputs read: phase2/prompts/factcheck.md, phase2/rubric.md §A, WRITING.md v0.6, review/v2-verify-2.md (Opus, 0/2/17), review/v2-verify-2b.md (Sonnet, 0/2/22), review/v2-response-2.md
sources used: sources/*.txt and *.pdf (page offsets from MANIFEST.md: Arora CACM printed = PDF + 100, ICS printed = PDF + 48, IMF printed = PDF + 76, Haldane and May printed = PDF + 350, Searle OCR printed = OCR − 9 up to p. 57, then − 8, FCIC printed = PDF − 29); Lupia and McCubbins, Cover and Thomas from /mnt/user-data/uploads/AI4Read/library. Harari: both *.whisper.txt, plus fresh faster-whisper medium.en runs of BIS [2:50–3:35], [7:10–7:50], [8:45–9:30], [22:45–23:15], [30:10–30:35] and WEF [5:45–6:15], [16:20–16:50], [26:22–26:40], [30:50–31:00], [31:04–31:40]. Page images: IMF printed p. 83 (Figure 3.5). No Nexus file used.
counts: critical 0 / major 1 / minor 16
---

# Fact-check, round 3B: post 02 v2, "Could a society run itself on AI?"

Severity follows rubric §A. Source quotes are at most 25 words.

**Bottom line.** All round-2 majors and nearly all round-2 minors are fixed correctly. One new major remains, in a sentence that is new in this round: the gloss of Haldane and May's "liquidity shocks" in Ladder 3 describes a different mechanism from the one they mean. Sixteen minors remain, several of them new wording introduced by the round-2 fixes. Rubric criterion 1 reads: 3 (one major, more than five minor); with the major fixed and the first seven minors fixed it would reach 4 (the rest are consistency items).

---

## Critical (0)

None.

## Major (1)

**M1. "Liquidity shocks" is glossed as funding withdrawal; Haldane and May mean losses on asset values** — `lens-cascade`, Ladder 3, "What it means".
- Post: "Haldane and May add that “liquidity shocks” (banks suddenly unable to borrow cash) “amplify as more banks fail”".
- Source: Haldane and May 2011, p. 353. The quoted sentence belongs to the second mechanism: "Such market liquidity shocks are conventionally and sensibly represented by discount factors … proportional to the number of failing banks holding the asset". They are defined as "losses in the value of a bank’s external assets, caused by a generalized fall in market prices … or a failing bank’s ‘fire sale’ actions". "Diminished availability of interbank loans" is a third, separate mechanism, called "funding liquidity shocks", also on p. 353.
- Why major: the parenthesis is our gloss, not marked "ours", and it attaches the third mechanism to a result that the authors state for the second. A reader learns the wrong picture of what amplifies in their model (fire-sale price falls, not funding runs). The gloss is new since round 1 (added after critic F-items asked for glosses), and neither round-2 checker caught it.
- Fix: "“liquidity shocks” (here, falls in the market value of banks’ assets, for example from fire sales: the more failing banks hold an asset, the deeper its discount)".

## Minor (16)

**m1. "Mostly rule-based" and "Most market algorithms are fixed rules" generalise one survey, and the second sentence has no source or label** — `answer` (a); `llm` first paragraph.
- Post: "though mostly by rule-based software rather than AI" (short answer (a)); "Most market algorithms are fixed rules." (§4, no cite, no "ours").
- Source: IMF 2024, p. 82: "evidence is mixed … more autonomous algorithms may still be based on simpler methods", from "participants of a major energy market (The Netherlands)". Figure 3.5 panel 2 (p. 83, page image): ML share about 87% of signal generators, 33% of trading algorithms, 10% of execution algorithms. Footnote 8 (p. 82): Dutch regulator, ML "implicitly or explicitly used in 80 to 100 percent" of firms’ trading algorithms.
- The data support "execution is mostly not ML" for that market. They do not support "most market algorithms are fixed rules" for markets in general, and footnote 8 points the other way. The table row keeps "evidence is mixed"; the box and §4 drop it.
- Fix: §4: "Many market algorithms are still fixed rules (IMF 2024, p. 82; in one Dutch energy-market survey only about a tenth of execution algorithms used machine learning)". In (a): "…though much of it by rule-based software (the IMF’s evidence is mixed)".

**m2. Searle: "only as artifacts and as models of human cognition" is an absolute that the book contradicts** — `lens-social`, Prediction 3 reveal.
- Post: "he mentions computers only as artifacts and as models of human cognition, pp. 14, 140–141".
- Source: Searle 1995, p. 34: "Most money is now in the form of magnetic traces on computer disks"; p. 56 ("a blip on a computer disk"); p. 84 (carrying "my computer"); p. 168 ("a computer screen"). Pp. 14 and 140–141 are correctly described.
- The point that survives: he never treats a computer as a possible participant in collective acceptance.
- Fix: "(he mentions computers as artifacts, as a medium for money, and as models of cognition, for example pp. 14, 34, 140–141, but never as possible parties to collective acceptance)".

**m3. Narayanan and Kapoor: the quoted timescale belongs to "impacts", not "adoption"** — `box-layers`, critics.
- Post: "adoption is slow (“on the timescale of decades”)".
- Source: Part I overview: "transformative economic and societal impacts will be slow (on the timescale of decades), making a critical distinction between AI methods, AI applications, and AI adoption". On adoption: "Diffusion occurs over decades, not years" (diffusion section).
- The substance is supported elsewhere in the essay. The round-2 fix (Sonnet m16) assumed the sentence said "adoption of AI will be slow (on the timescale of decades)"; that wording is not in the saved text.
- Fix: "economic and societal impacts are slow (“on the timescale of decades”)".

**m4. Ladder 3: "whose likelihood Lens 2a estimated"** — `lens-cascade`, "What it means".
- Post: "The toy starts *after* the shared failure, whose likelihood Lens 2a estimated."
- Source: our own Lens 2a. It computes toy arithmetic with ρ assumed ("how correlated real AI-driven desks are; ρ is assumed"). It does not estimate any real likelihood.
- Fix: "…whose likelihood Lens 2a showed in a toy (with ρ assumed)". The previous wording ("showed how a shared model makes joint failure likelier") was accurate.

**m5. Short answer (b): the cross-reference to Lens 1 does not support the claim** — `answer` (b).
- Post: "power would tend to move to whoever writes the models and the rules, since the regulator with more variety sets the terms for the rest (Lens 1)".
- Source: Lens 1 says only that the pressure is to automate the checker too (ours; Danielsson and Uthemann §3, p. 10: "those who remove humans from the loop can gain the upper hand"). It never says the higher-variety regulator "sets the terms".
- The sentence is inside "(ours)", so this is a mislabelled pointer, not a false source claim.
- Fix: drop "(Lens 1)", or write "(our extension of Ashby’s law)".

**m6. Short answer (c) again presents one route to the incentive condition** — `answer` (c).
- Post: "Delegation can be trusted when those who delegate have knowledge and the agent an incentive (Lupia and McCubbins); someone answerable supplies the incentive."
- Source: Lupia and McCubbins 1998, p. 85: the incentive condition "is satisfied either if the agent and principal have common interests or if external forces motivate the agent".
- Residue of round-2 Opus M2. Lens 4 is now correct ("two routes"). (c) says "someone answerable supplies the incentive" and its change-the-verdict line names only accountable AIs, not AIs whose objective matches ours.
- Fix: "… the agent an incentive (common interests, or outside pressure such as being answerable)". Add to the verdict-changers: "or AIs whose objectives are reliably aligned with ours".

**m7. Lens 4 states a legal fact, then disclaims any legal position** — `lens-answer`, first paragraph and "Personhood".
- Post: "today it is not a legal person that can own assets and be fined (ours; compare Danielsson and Uthemann below)"; later: "We have no legal sources and state no legal position."
- Source: none in the saved files. Danielsson and Uthemann do not mention legal personhood.
- Fix: "and, as far as we know, is not a legal person that can own assets and be fined (ours; no legal source checked)".

**m8. Arora: "a small, unusually crowded patch" against "large dense subgraphs"** — `lens-control`, "Some products may resist checking", Result.
- Post: "finding a small, unusually crowded patch in a huge random network" (followed at once by the conjecture quote).
- Source: CACM p. 102: "the conjecture that there does not exist a tractable algorithm to detect large dense subgraphs in random graphs"; p. 105: "even quite large boobytraps may be undetectable".
- The gloss contradicts the word in the quotation beside it. "Small" is true only relative to the whole network.
- Fix: "a hidden, unusually crowded patch (a dense subgraph) in a huge random network".

**m9. Diagram step still cites p. 101 for the conjecture** — `cfg-seller`, step 3.
- Post: "finding the few where junk was concentrated is the hard part (a conjecture; Arora et al. 2011, p. 101)".
- Source: the conjecture sentence is on p. 102 (Sonnet round-2 m4). Lens 1 body was corrected; the diagram step was not.
- Fix: "p. 102".

**m10. "Most firms the IMF asked" and "big trading decisions"** — `english` (phrase and loop paragraph).
- Post: "Most firms the IMF asked still want a human in the loop for big trading decisions."
- Source: IMF 2024, p. 78: "most participants view having a ‘human in the loop’ as an essential part of any AI-based strategy". The outreach included supervisors, banks, market infrastructure providers and academia (pp. 82–83). P. 83: "all participants … expected" it "especially for large capital allocation decisions".
- Residue of Opus n10. "Firms" is narrower than "participants", and "big trading decisions" blends p. 78 (any AI strategy) with p. 83 (large allocation decisions).
- Fix: "Most participants in the IMF’s outreach want a human in the loop in any AI-based strategy." Same change in the loop paragraph.

**m11. Ashby's table rule is stated on p. 206, and restated on p. 207** — `lens-control` Mechanism; `box-ashby` step (1).
- Post: "Ashby’s tables assume that in each column (each check), no state appears twice (Ashby 1956, p. 207)".
- Source: S.11/5, p. 206 (left column): "If no two elements in the same column are equal … the variety in the selected set of outcomes cannot be fewer than r/c". P. 207 restates it as "The condition introduced in S.11/5 (that no element shall occur twice in a column)".
- The new r/c = 4/2 = 2 sentence in the Mechanism is Ashby's own p. 206 result and is not credited to him.
- Fix: cite "pp. 206–207" and mark the 4/2 step "(Ashby’s r/c rule)".

**m12. Term box: "in our question’s words, without any necessity of human intervention"** — `home`, term box.
- Post: "…not running, in our question’s words, without any necessity of human intervention."
- Source: the post states its question as "with no human intervention at all" (hook) and "with no person ever stepping in" (lede). The quoted-looking phrase appears nowhere else.
- Fix: "…not running with no human intervention at all."

**m13. Records lag the final text** — `numbers.md`, `audio-script.md`, `audio/*.mp3`.
- numbers.md (18:24) has no rows for the new 4/2 = 2, the figure areas c² and 2c², or the Nε ≤ 1 condition.
- audio-script.md (18:31) is behind the 18:37 text. Line 143 still says "neither know nor consciously apply the rules" (Searle p. 142 says "consciously or unconsciously"). Line 184 still says "nothing we read shows it, and two lenses give reasons to doubt it"; the text now says "not shown, and not ruled out".
- All MP3s are dated 00:44–00:45 on 18 October, before any v2 work, so the audio voices the v1 script. The masthead "36 to listen" matches that v1 audio (all.mp3 = 2,141 s = 35.7 min).
- Fix: update numbers.md; resynchronise the script; re-render the audio and re-measure the listening time.

**m14. Granovetter is named and listed in Sources but cited nowhere** — `turn` Exercise 4; `sources`.
- Post: "Exercise 4 · Granovetter’s riot"; no cite span after the Ladder 3 sentence was removed. Sources still carries src-granovetter.
- Source: Granovetter 1978, p. 1425: thresholds 0 to 99; "the two crowds are essentially identical" (checked in earlier rounds).
- Fix: add a cite span to the Exercise 4 title or text ("Granovetter 1978, p. 1425; the numbers here are the textbook version").

**m15. Own reasoning not labelled in the closing section** — `answer`, "Where the lenses disagree" and "Signs to watch".
- Post: "A standard menu makes checking easier *and* firms more alike." (unlabelled; only the last sentence of the paragraph carries "(ours)"); Signs 1–3 (own indicators, unlabelled).
- Source: none; the first half rests on the Lens 1 toy (lower V_D) and the second half is our inference.
- Fix: put "(ours)" after the first two claims, and "(our indicators)" on the Signs heading.

**m16. Lens 4 toy: "succeeds" is not Lupia and McCubbins's definition** — `lens-answer`, Mechanism.
- Post: "Here delegation “succeeds” if you never end up below your cash."
- Source: Lupia and McCubbins 1998, p. 79: "We say that delegation succeeds when an agent’s actions improve a principal’s welfare … fails when … reduce".
- Under the post’s own definition, "only one condition" (you keep 100) would count as success. Under theirs it is neither success nor failure, which is why the next sentence and the p. 92 line (stricter K) are needed. The mix is easy to misread.
- Fix: "Following Lupia and McCubbins (p. 79), delegation “succeeds” if you end up better off than your cash and “fails” if worse off; keeping your cash is neither."

---

## Counts

| Severity | Count |
|---|---|
| Critical | 0 |
| Major | 1 (M1) |
| Minor | 16 (m1–m16) |

Release gate (0 critical, 0 major): not met until M1 is fixed. Cheapest minors to clear first, because they touch a source: m1, m2, m3, m8, m9, m10, m16.

---

## Round-2 findings: verification

### Fixed correctly (checked against the source, not the writer's response)

| Round 2 | Draft now | Verdict |
|---|---|---|
| Opus M1 / Sonnet M1 ("AI" vs algorithms in the short answer) | (a) rewritten: run time / design time / stable and accepted; "mostly by rule-based software rather than AI"; table Run row "in some markets, on rules written by people" | Fixed; the new "mostly" generalisation is m1. |
| Opus M2 (L&M incentive has two routes) | Lens 4 "Applied to AI": "two routes: common interests, or “external forces”" (p. 85); D&U §3, p. 10 "lose traction" quoted verbatim | Fixed in Lens 4; residue in (c) is m6. |
| Sonnet M2 / Opus n1 (Ashby "impose") | §13: "find a constraint, and regulation may become possible; imposing one … is our mapping"; Lens 1 lever 3 "Our mapping" | Fixed. Ashby p. 247 verified in the page layout. |
| Opus n2 (who gains / who bears) | "in that case … would tend to move…, users may gain speed and lower costs…"; "lower flash-crash risk" (IMF p. 89, Table 3.1 positive column) | Fixed. See m5 for the pointer. |
| Opus n3 (Harari [3:30]) | "if nobody understands finance any more, it “could lead to power shifting from humans to algorithms to alien forms of intelligence” BIS [3:09], [3:30]" | Fixed. Transcript and medium.en agree. |
| Opus n4 (D&U locator) | "§3, p. 10" for both quotes | Fixed (both sentences are on printed p. 10, §3). |
| Opus n5 / Sonnet m8 (Searle "consciously") | "neither know the rules nor apply them, consciously or unconsciously" | Fixed in the post (the audio script is not, m13). |
| Opus n6 (Skingsley) | "restating his point, she grants that…" | Fixed (BIS [7:35], medium.en). |
| Opus n7 (N&K "incoherent") | "as usually conceptualized" present | Fixed; m3 is a different slip. |
| Opus n8 (broker "neither") | "worse than your cash: 90" | Fixed. |
| Opus n9 (Democracy heading) | "Accountability", "(ours)" | Fixed. |
| Opus n10 | Lens 4 "most participants in the IMF’s outreach … liability (p. 78)"; Signs "the outreach participants’ expected…" | Fixed except the English section (m10). |
| Opus n11, n12, n13, n14 | quote marks gone; "one of the most automated corners" and "(our judgement)"; "paused trading during the 2010 crash"; "the quoted passage does not say the pause caused this, and the paper does not test it" | Fixed. In Kirilenko et al. the "up" phase is only described, not tested; p. 2 verified. n11 leaves m12. |
| Opus n15 (under the diagonal) | "triangle below the slanted line", plus a new SVG: triangle (0,0)–(0,2c)–(2c,0), small square [0,c]², areas 2c² and c² | Fixed. Figure coordinates, caption and text agree. |
| Opus n16 (IMF "more AI in decisions") | table Decide row adds p. 82 | Fixed. |
| Opus n17 (records) | notebook comments now "(Lens 2a)", "(Lens 2b, Ladder 5)"; index.html (18:37:39) is built from the 18:37:38 text | Partly; numbers.md and audio lag (m13). |
| Sonnet m1, m2, m3, m5, m6 | hook "By 2:45 p.m., … less than 1% of their level at the start of the day"; "paused trading"; "evidence is mixed" scoped to algorithmic trading; "may resist checking"; table row "a, a, c, c" | Fixed. Ashby table rerun over all 16 plans: minimum 2 outcomes. |
| Sonnet m9, m10, m11, m12 | chair, bathtub, computer + "(our contrast)"; L&M link-type wording; "(ours)" labels; "Accountability" | Fixed. |
| Sonnet m13, m14, m15 | recall card keeps both/either; "appear contained" in all places; "Every automated system" removed | Fixed. |
| Sonnet m17, m18, m19, m20, m21 | group 2 heading "most without a hedge"; "USAI persons" with gloss; "two sentences later"; BIS release date dropped; small-m real roots added | Fixed. WEF [17:29], [17:05] and [31:11] ("AIs create a new financial system that they understand and we don’t understand") re-confirmed with medium.en. |
| Sonnet m22 | notebook labels | Fixed. |

### Fixed only partly

| Round 2 | Left over |
|---|---|
| Sonnet m4 (conjecture on p. 102) | Lens 1 body fixed; `cfg-seller` step 3 still p. 101 (m9). |
| Sonnet m7 (Searle "never discusses machines") | Rewritten, but "only" is still an absolute (m2). |
| Sonnet m16 / Opus n7 (N&K) | "as usually conceptualized" added; "adoption … decades" now misplaces the quote (m3). |
| Opus n10 | English section still "firms" (m10). |
| Opus n17 | numbers.md and audio lag (m13). |

### Critic items with a factual side

F7 square-and-triangle figure: now present and correct. F4 two-bank derivation: re-verified (Python, Monte Carlo 4 million draws: N = 2, ε = 0.1 gives 0.01983 against 0.0200; N = 3 gives 0.004539 against 0.0045; ε = 0.01 gives 0.000208 against 0.0002). The condition Nε ≤ 1 is stated. Prediction 4 and the "What it means" remedy quote ("should probably be given much greater prominence", p. 355) are verbatim.

---

## "Ours" labels and other posts

- **No sentence refers to another AI4Read post.** Grep of src/content.html for "post 0/1/2", "earlier/previous/last post", "remember", "as in the": only the eyebrow "Post 02" (this post's own label) and the generic "village market". audio-script.md line 116 says "the previous chapter" (an earlier chapter of this audio, so own post). One non-reader-visible note: index.html line 1276 carries a code comment "Generated from post 01 app.js"; it is in the page source, not in any sentence, so it is not counted.
- **Ours labelled:** five jobs, why five, run-time vs design-time, the society definition, scope, every toy (Ashby table, lemon, six-asset, N_eff, CDO, six banks, two-bank derivation, trend rule, broker), machine-acceptance arguments, the short answer ("our reading, not a finding"; "who gains and who bears (ours)"; "our verdict"). Unlabelled exceptions: m1 (§4 sentence), m5, m15, and the M1 gloss.
- **Own claims that are fine as labelled:** "contest … by withdrawing acceptance (our reading)", "designed consequences for deployers (ours)", "Only then is there an executable strategy (our gloss)".

---

## Checked and found correct

- **Kirilenko et al. 2017 (manuscript pp. 2, 3, 7):** $4.1 billion, "as a hedge to an existing equity position", "chose to execute this sell program via an automated execution algorithm", 9% of volume "without regard to price or time", "less than 1% of buy-side market depth" at 2:45:28, five-second pause, "automated pre-trade safeguard procedure" (fn. 1), "prices stabilized" after 2:45:33, "back to nearly their pre-drop level" by 3:08 (about 22–23 minutes after the pause), "fully electronic" and "no market maker obligations" (p. 7). The paper does not test the pause's effect.
- **IMF 2024 (printed pages):** p. 78 "most participants view having a ‘human in the loop’", "liability", "remain mostly speculative"; p. 82 "evidence is mixed", "there is evidence that sophisticated AI has not yet been implemented widely…", "may ultimately make the trading decision", "participants expect greater integration of sophisticated AI in investment and trading decisions"; p. 83 "all participants … expected a ‘human in the loop’ approach to persist in the near term (three to five years), especially for large capital allocation decisions", SupTech, "models will continue to operate within predefined rules"; p. 86 "about 70 percent of equities trading and more than half of futures trading"; p. 89 "lower flash-crash risk", "highly uncertain"; p. 92 "appear contained"; p. 93 "may herd…", "institutions are responsible for AI systems they deploy"; p. 101 definition. (p. 88 is no longer used.)
- **Harari:** all timestamps within 3 s of the transcripts. medium.en confirms "we’ll need to keep humans in the loop" (BIS [23:03]), "I think we’ll see AI creativity also in this field coming up with new types of financial devices that no human being would ever imagine creating" ([30:20–30:30]), "At the present moment, we still think better" (WEF [30:55]), "when AIs create a new financial system that they understand and we don’t understand" ([31:11–31:23]), "AIs can therefore function as persons" ([16:43]). Guardian 2023, Guardian 2024, Ynet, Poole quotes verbatim. Firmness groups, hedges and the "Unfortunately" turn are kept. Strongest unhedged lines present in the hook and fold-out.
- **Ashby 1956:** p. 207 law quote, p. 209 "owes nothing to experiment", p. 246 "ways that may make regulation possible", "somewhat trivial solution", p. 247 "the discovery of a constraint may convert ‘regulation impossible’ to ‘regulation possible’" and "only hope". Table rule direction (columns = checks). Cover and Thomas Thm 2.6.5 is on p. 27 of the 1991 library copy.
- **Lupia and McCubbins:** p. 85 knowledge and incentive conditions, Theorem 5.1, "the worst that can happen … is the retention of the status quo"; p. 92 Theorem 5.1′ (K, "either condition … fails"). Broker toy 110 / 100 / 90 follows the theorem's three cases.
- **Arora et al.:** CACM p. 101 "even in industry-standard models, the pricing problem can be as difficult as solving the planted dense subgraph problem"; p. 102 "unrigged", "computationally intractable", the conjecture sentence; ICS p. 52 formula and "all possible ways", p. 55 "under computational assumptions, the lemon cost for polynomial time buyers can be much larger than n", p. 61 Theorem 9, p. 62 "currently does not exist", p. 63 "clearly only a first step", "raise the hope". Lemon car example pp. 50–51.
- **Haldane and May:** p. 351 "major differences", "sharp transition", mα² > 1 with m and α as defined; p. 353 "all the banks doing the same thing … minimize risk for each individual bank, but maximize the probability of the entire system collapsing", N^N ε^N/N! ("obviously also the probability for all N of these banks to fail"), "liquidity shocks amplify as more banks fail" (gloss: M1); p. 355 "systemic diversity objective should probably be given much greater prominence", "Modular configurations prevent contagion…". The authors give no derivation.
- **Searle (printed pages):** 14, 24, 28, 32–33 (bill and type), 37, 41, 45 (two), 69, 70, 142 verbatim; pp. 140–141 (von Neumann vs connectionist) confirmed. Danielsson and Uthemann: abstract "amplifies existing financial system vulnerabilities", "faster and more severe", "develop their own AI systems"; §3, p. 10 "human experts cannot effectively oversee AI operating at machine speeds", "lose traction when the agent is an optimisation algorithm that cares only about its objective function". Danielsson et al. 2022 p. 7 "will likely be unintelligible to humans".
- **Others:** FSB p. 21 "as if it were a single institution", p. 2 "more work may be needed"; Gensler and Bailey pp. 2, 13, 17, 21, 22, 25; Scheurer p. 1; Luo abstract; Mik; Cointelegraph (handler "only approving its X posts", $50,000, 11 July); Decrypt ("semi-autonomous", "neither the bot nor its handler created the token"); FCIC p. 28 and p. 149 (text layer + page offset); N&K ("incoherent as usually conceptualized", "primarily in the hands of people and organizations", "median outcome").

## Numbers rerun

- `node site/ai4read/components/check.mjs posts/2026-10-ai-finance/src/content.html`: 15/15 widget configs OK; readouts match the prose (N_eff 2.703/1.099, six banks 6 of 6 in 3 rounds, 2,756 times, 0.64, herding 0.04 / −1.00 / 0.000, 0.370%). `scripts/wordcount.py`: 7,402 main-text words (cap 7,500), fold-outs 2,689.
- Python (scratchpad nums.py, nums2.py): Ashby 16 plans give a minimum of 2 outcomes (4/2 rule); V_D 13.29, 9.29, 6.64; H(D) = 1.75; lemon toy 12 placements give 7/4, 3 give 3/2, E[F] = 9/4, Δ(2) = 3/4; tree needs 4 flips (all 512 inputs) and 2^k for 27 and 81; N_eff 10.0, 2.703, 1.099, 1.0, 3.257, ceiling 3.33, N = 2, ρ = 0.5 gives 1.333; Bayes 0.5, 0.8, 0.941, 0.985, 0.996, 1,048,576, 0.999999; CDO q = 0.37%, w = 0.5 gives 5.185%, w = 1 gives 10% (27.0×), p = 0.02 gives 2.000% against 0.003152% (634.5×); Haldane–May N^N/N! = 64.8 (N = 6), 2,755.7 (N = 10), 4.31e7 (N = 20), N = 3 pyramid (3c)³/6 = 4.5c³, Stirling within 1% at N = 10; May 0.64 / 1.28 / 0.72, at most 6 links at α = 0.4.
- Six banks: 3 X failures give 6 of 6 in 3 rounds (Y1 loses 12 ≥ 10; Y2 4 + 8 = 12 ≥ 9; Y3 4 + 8 = 12 ≥ 11); capital ×1.5 gives 3; Play answers (1) none at 0.8, only Y1 (3 of 6) at 1.0; (2) any two X give 2 at 0.8 and 5 at 1.0; (3) ×1.2 gives 5, ×1.21 and ×1.25 give 3.
- Herding: m = 0.2 gives −0.9, −0.51, −0.189; m = 0.9 gives −2.30, −3.94; characteristic-root sizes 0.548, 1.002, 1.162 (complex in all three); first unstable m on a 0.001 grid is 0.667; real roots below m ≈ 0.067 (0.42, 0.18 at m = 0.05) and above m ≈ 0.933 (1.32, 1.08 at m = 0.95), as the fold-out says.
- Notebook files ex1–ex3 run clean (N_eff 10.06 / 2.71 / 1.10 / 1.00; failures 1, 2, 6, 3; root sizes 0.548 / 1.002 / 1.162).
