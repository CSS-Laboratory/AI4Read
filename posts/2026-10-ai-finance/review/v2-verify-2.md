---
id: 2026-10-ai-finance/review/v2-verify-2
stage: S5, round 2 of post 02 version 2 (independent fact-check, Opus)
checked: 2026-10-18
draft: src/content.html (632 lines, modified 18:11): all visible text, every fold-out, all 15 widget JSON configs incl. diagram step texts, notes and captions, quiz options and reveals, Play answers, exercises, recall cards, English section, Sources
round-1 inputs: review/v2-verify-1.md (Opus 0/1/21), review/v2-verify-1b.md (Sonnet 0/2/32), review/v2-critic-1.md, review/v2-response-1.md
briefs: source-brief-v2.verified.md, source-brief.verified.md (used only as maps; every claim below was checked at the source)
method:
- Quotes matched against the source text, page by page: Kirilenko et al. 2017 manuscript pp. 2–3; IMF 2024 per printed page (PDF + 76) pp. 78, 82, 83, 86, 88, 89, 92, 93, 101; FSB printed pp. 1, 2, 21 (page footers); Gensler and Bailey pp. 2, 13, 17, 21, 22, 25 (page footers); Danielsson and Uthemann abstract, introduction, §3 (p. 10); Arora CACM pp. 101–102, ICS 2010 printed pp. 61–63 (PDF + 48); Haldane and May pp. 351, 353, 355 (page footers); Searle OCR printed pp. 14, 24, 28, 32, 33, 37, 41, 45, 69, 70, 142 (OCR − 9 to p. 57, then − 8); Lupia and McCubbins library copy pp. 11, 85–86, 91–92, 207; Granovetter library copy p. 1425; Cover and Thomas library copy (1991, 1st ed.; Thm 2.6.5 confirmed by number); Scheurer p. 1; Luo, Mik, Cointelegraph, Decrypt, Guardian 2023, Guardian 2024 extract, Ynet, Poole, Narayanan and Kapoor.
- Harari and Skingsley: every timestamp in the post checked against both whisper transcripts with the surrounding lines. (No new audio re-transcription this round; "we'll need" at BIS [22:56] rests on the round-1 medium.en re-runs.)
- Numbers: `node site/ai4read/components/check.mjs posts/2026-10-ai-finance/src/content.html` (15/15 OK) plus `--id/--values/--seeds` for every preset and every Play answer; Python for the Haldane–May two-bank derivation (Monte Carlo, N = 2 and 3), N^N/N! and Stirling, herding gaps and characteristic roots (incl. the real-root ranges), CDO, N_eff, Ashby, Bayes.
- No Nexus file used other than the Penguin sample (not needed this round).
---

# S5 fact-check, post 02 v2, round 2

Severity follows rubric §A. Source quotes are at most 25 words.

## Critical (0)

None.

## Major (2)

**M1. The short answer says AI runs and checks, where the sources say algorithms and pre-set rules do** — `answer`, box (a) and the §13 table.
- Post: "<i>Capable:</i> AI already runs much of the work, can increasingly decide, and checks at run time." Table: "Run | Yes, and in some markets largely does."
- Source: IMF 2024, p. 101: algorithmic trading is where "an algorithm independently executes trading decisions", "in its simplest guise" "basic trading rules"; p. 82: "evidence that sophisticated AI has not yet been implemented widely". The only run-time check in the post is the 2010 Stop Logic, "an automated pre-trade safeguard procedure" (Kirilenko et al. 2017, p. 2, fn 1), a fixed rule; supervisors "use AI-driven SupTech tools" (IMF p. 83) to help people monitor, not to check on their own.
- Why major: wrong scope at the place the reader looks. It is the exact conflation the post warns against in Prediction 1, the recall card ("Why is '70% algorithmic' not '70% AI'?") and §4 ("Most market algorithms are fixed rules").
- Fix: "<i>Capable:</i> software, mostly rule-based algorithms, already runs much of the work and checks at run time on pre-set rules; AI is beginning to help decide"; in the table, "Run | Yes; in some markets algorithms (many simple rules) largely do."

**M2. Lens 4 says an unpunishable agent leaves only knowledge, but Lupia and McCubbins' incentive condition can be met by common interests** — `lens-answer`, "Applied to AI (ours)" and the lens summary.
- Post: "And since an AI cannot be punished, the incentive condition must run through whoever deploys it." Lens summary (unlabelled): "delegating to an agent that cannot be punished leaves only knowledge to protect you."
- Source: Lupia and McCubbins 1998, p. 85: the incentive condition "is satisfied either if the agent and principal have common interests or if external forces motivate the agent". P. 11: it "is satisfied when the agent and the principal have at least some goals in common."
- Why major: a dropped condition the argument rests on, and the summary presents it as what the lens adds. The post's own toy shows the other route ("he is paid only if you profit" is a common-interest device, not a punishment). Short answer (c) leans on the same step ("AIs that can be held responsible in a way that changes their behaviour").
- Fix: "Punishment is one route to the incentive condition; the other is shared goals. An AI cannot be fined or jailed, so its incentive must come from its objective (how it was built) or from whoever deploys it, and today's capital-market rule takes the second route." Danielsson and Uthemann give a citable version of the first half: incentives "such as rewards and punishments, lose traction when the agent is an optimisation algorithm that cares only about its objective function" (2025, §3, p. 10). Change the summary to match.

## Minor (17)

**n1. Ashby's third lever: "impose" and "becomes possible"** — `answer`, "Where the lenses disagree".
- Post: "Ashby’s third lever says: impose a constraint, such as a standard menu of contracts, and checking becomes possible."
- Source: Ashby 1956, p. 247: "the discovery of a constraint may convert 'regulation impossible' to 'regulation possible'"; the constraints are those "in the disturbances". Lens 1 labels imposing a menu as "Our mapping"; this sentence, newly moved into §13, gives our mapping to Ashby and drops "may".
- Fix: "Ashby’s third lever says: find a constraint, and regulation may become possible; imposing one, such as a standard menu, is our mapping."

**n2. "Who gains and who bears": no hedge, and only one side** — `answer`, box (b).
- Post: "<i>Who gains and who bears (ours):</i> power moves to whoever writes the models and the rules, and losses fall on whoever is exposed when shared models fail together."
- Source: the ours label is there, but the sentence is an unconditional forecast inside a conditional box. The sources name gains to other parties: IMF p. 89 (Table 3.1, positive column) "lower flash-crash risk"; Gensler and Bailey p. 2 "increased efficiency, greater financial inclusion … better risk management".
- Fix: "In that case (ours), power would tend to move to whoever writes the models and rules, users may gain efficiency, and losses would fall on whoever is exposed when shared models fail together."

**n3. Harari's [3:30] line loses its condition and its end** — `answer`, box (b).
- Post: "Harari puts the extreme case as a possibility: it “could lead to power shifting from humans to algorithms”".
- Source: BIS [3:09]–[3:30]: "What happens if this number goes down to zero? … It could lead to power shifting from humans to algorithms to alien forms of intelligence."
- "It" has no antecedent in the post. Harari's condition is that no human understands finance any more. His line is about power moving away from humans, the opposite direction to the post's "whoever writes the models".
- Fix: "Harari's extreme case: if nobody understands finance any more, it “could lead to power shifting from humans to algorithms to alien forms of intelligence” (BIS [3:09], [3:30])."

**n4. Danielsson and Uthemann: wrong locator for the machine-speed quote** — `lens-control`, "What it means".
- Post: "“human experts cannot effectively oversee AI operating at machine speeds” <cite>Danielsson and Uthemann 2025, introduction</cite>".
- Source: the sentence is in §3, "Channels of AI Impact on Financial Crises" (malicious-use channel), p. 10, not in the introduction.
- Fix: cite "§3, p. 10".

**n5. Searle p. 142: "consciously" weakens his claim** — `lens-social`, "For".
- Post: "Searle argues that money users neither know nor consciously apply the rules".
- Source: Searle 1995, p. 142: "they do not apply them consciously or unconsciously; rather, they have developed a set of dispositions".
- The dropped "or unconsciously" is the part the "For" argument needs.
- Fix: "neither know the rules nor apply them, consciously or unconsciously".

**n6. Skingsley's "deep trouble" line is her restatement of Harari** — `box-layers`, critics.
- Post: "<b>Skingsley</b> …: we already trust what we only vaguely understand, such as airplanes, though if the last 1% … “goes down to zero, then we are all in deep trouble”".
- Source: BIS [7:35]: "But it sounds from what I hear you saying that this last percent, if that goes down to zero, then we are all in deep trouble."
- Fix: "… though, restating his point, she grants that if the last 1% “goes down to zero, then we are all in deep trouble”".

**n7. Narayanan and Kapoor: "incoherent" without its qualifier** — `box-layers`, critics.
- Post: "a notion they view as incoherent".
- Source: Part II intro: "‘superintelligent’ AI, which we view as incoherent as usually conceptualized".
- Fix: add "as usually conceptualized".

**n8. Broker toy: "neither" row softer than the theorem** — `lens-answer`, table.
- Post: "neither | whatever he sells, possibly 90".
- Source: Lupia and McCubbins p. 85: "If neither condition is satisfied, then delegation fails"; "fails" is defined on p. 79 as "when an agent’s actions reduce a principal’s welfare". The prose ("fails if neither does") and the Check ("worst cases, 110, 100 and 90") are right; only the table cell hedges.
- Fix: "you end up worse than your cash: 90". The other two rows and the Check match Theorem 5.1 (pp. 85–86) and the stricter Theorem 5.1′ (p. 92).

**n9. "Democracy" heading on an organisational claim** — `lens-answer`, "Democracy".
- Post: "<b>Democracy.</b> When decisions cannot be explained, “Human agency and traditional intervention approaches may be lost”".
- Source: Gensler and Bailey 2020, p. 13: the challenge is "at various levels within organizations and regulatory bodies". They do not discuss democracy.
- Fix: retitle "Accountability" or mark the step to democracy "(ours)".

**n10. "Most participants" grows into "most market participants" and "most firms"** — `lens-answer`, the English section, Signs to watch 1.
- Post: "most market participants want a human in the loop partly for “liability” reasons"; English: "Most firms still want a human in the loop …" (phrase and loop paragraph); Signs: "the IMF’s “human in the loop” holds past five years".
- Source: IMF 2024, p. 78: "most market participants that responded to IMF outreach"; p. 83: "all participants in the IMF’s outreach expected …".
- Fix: "most participants in the IMF’s outreach"; English: "Most firms the IMF asked …"; Signs: "the outreach participants’ expected “human in the loop” …".

**n11. An unattributed quotation in the term box** — `home`, run-time/design-time term box.
- Post: "a system whose rules people still write is not running “without any necessity of human intervention”."
- Source: none. The phrase appears nowhere else in the post or in any source; it is the reader's question. In quotation marks with no attribution it reads as a source quote.
- Fix: drop the quotation marks, or write "not running, in our question’s words, without any necessity of human intervention".

**n12. "Most automated corner of society" is unsourced** — masthead meta and `home`, Scope.
- Post: "Economics and finance, the most automated corner of society today"; "finance is where automation has gone furthest".
- Source: no source in the post compares automation across sectors.
- Fix: "one of the most automated corners …" and "(our judgement)".

**n13. "A pre-set rule paused the 2010 crash"** — `home`, table, Check row.
- Source: Kirilenko et al. 2017, p. 2: "trading on the E-mini was paused for five seconds". The hook is careful not to claim the pause stopped the fall; "paused the crash" undoes that.
- Fix: "A pre-set rule paused trading during the 2010 crash."

**n14. The hook speaks for a report we did not read** — `hook`, paragraph 2 (round-1 M1 follow-up).
- Post: "the regulators report that prices stabilised after the pause …; neither they nor the paper test whether the pause caused it."
- Source: the CFTC–SEC report is known only through the passage Kirilenko et al. quote (MANIFEST: sec.gov returned 403). The quoted passage gives only purpose and sequence; whether the full report tests causation is unseen. The rest of the M1 fix is correct.
- Fix: "the quoted report passage does not say the pause caused it, and the paper does not test it."

**n15. Two-bank derivation: "under the diagonal" points to the wrong line** — `lens-cascade`, Ladder 4.
- Post: "Draw both values on a square of side \(2c\): that region is the triangle under the diagonal, with area \(\tfrac12(2c)^2=2c^2\)."
- The region \(V_1+V_2<2c\) lies below the anti-diagonal, the line from \((0,2c)\) to \((2c,0)\). A reader who shades below the main diagonal \(V_1=V_2\) gets the same area by coincidence but the wrong event. The general step also needs \(N\varepsilon\le1\) for "\(\varepsilon x/c\) up to \(Nc\)" to be a probability (true for every slider setting: max \(20\times0.05=1\)).
- Fix: "the triangle below the line \(V_1+V_2=2c\), from the top-left corner to the bottom-right"; optionally add "(this needs \(N\varepsilon\le1\))".

**n16. IMF balance: participants also expect more AI in decisions** — `home`, Decide row, and short answer (a).
- Post: only the human-in-the-loop expectation (p. 83) is given.
- Source: IMF 2024, p. 82: "Within a three- to five-year horizon, participants expect greater integration of sophisticated AI in investment and trading decisions."
- Fix: add it next to the p. 83 line: "they also expect more AI in investment and trading decisions over the same horizon (p. 82)".

**n17. Build and records lag the draft (round-1 n21 only partly fixed)** — `index.html`, `numbers.md`.
- index.html (18:05) is older than content.html (18:11).
- The embedded tutor brief has no cross-post lines now (n21 fix). But it still carries stale v1 units that contradict the post: B7 "IMF … [DROP]"; E3 Gensler and Bailey "[UNSEEN-KEEP-AS-SECONDARY]"; "Cite it as 'working paper, 2014'" for Kirilenko. The v2 brief adds "The CACM 2011 text (V4) is UNSEEN", yet the post cites CACM p. 101 from `arora-2011-cacm-published`.
- numbers.md has no rows for the new two-bank numbers (0.0002, 2ε²), the broker toy (110/100/90) or Haldane–May 2,756, and its section labels are stale ("Lens 3a/3b").
- Fix: rebuild; drop the superseded v1 units from the tutor brief and mark V4 as seen; update numbers.md.

## Counts

critical 0 / major 2 / minor 17

## Round-1 findings: verification

- **Fixed correctly:**
  - Majors: Opus M1 (pause purpose vs effect; residual n14); Sonnet M1 (Goldman quote removed, CACM p. 101 only); Sonnet M2 (Harari remedy split into BIS [21:37], [22:56] and Guardian 2024, "three months later" ≈ 7 May → 24 Aug).
  - Opus n1–n20: all fixed. n6 is moot, because the D&U "cannot effectively prevent" quote is gone; the new D&U quote has its own locator slip (n4). n10 is moot, because the fold-out was dropped.
  - Sonnet m1–m18, m20–m32: all fixed. m1 is moot, because the hook gives no clock time. On m32, the optional p. 22 balance line was not added, which is acceptable.
  - The brief's V1 note was also corrected (source-brief-v2.verified.md line 111).
- **Partly fixed:** Opus n21 (n17 here); Sonnet m19 ("consciously" added, n5); Sonnet m24 (second half added, attribution nuance n6); Opus n2 residue in Signs to watch and the English section (n10).
- **Critic items with factual content:** F4 derivation correct (below); F5 broker toy matches Theorem 5.1 except n8 and M2; F8 tension moved to §13 (introduces n1); F1 term box and society definition labelled ours; F3 "who gains" (n2, n3).

## Checked and found correct

- **Haldane–May two-bank derivation.**
  - The maths is right. With \(P(V<x)=\varepsilon x/c\) on \([0,2c]\) (density \(\varepsilon/c\)), independent assets, and a bank failing when \(V_1+V_2<2c\), the chance is \(2c^2\cdot(\varepsilon/c)^2=2\varepsilon^2\).
  - The general simplex volume \((Nc)^N/N!\times(\varepsilon/c)^N=N^N\varepsilon^N/N!\) reproduces the formula exactly. Haldane and May print it on p. 353: "the probability for any one bank to fail can now be calculated as N^N ε^N/N!".
  - Monte Carlo (4M draws): N = 2, ε = 0.1 gives 0.02006 (formula 0.0200); N = 3, ε = 0.1 gives 0.00452 (0.0045).
  - At ε = 0.01: per bank 0.01 → 0.0002, system 0.0001 → 0.0002, "twice as likely".
  - The assumption is stated. "Haldane and May give no derivation; this one is ours" is true: their text gives the toy and the result only, crediting N. Beale and colleagues. The ratio is 2,755.7 for N = 10. The check \(4\varepsilon^2/2=2\varepsilon^2\) is right.
- **Haldane and May, other:** "major differences" (p. 351); mα² > 1 with m, α as defined (p. 351); "liquidity shocks amplify as more banks fail" and "high connectivity distributes, and thereby attenuates risk" (both p. 353); the reveal quote "minimize risk … maximize the probability" (p. 353); "systemic diversity objective should probably be given much greater prominence" and "Modular configurations prevent contagion …" (p. 355). The citation "pp. 353–354" is acceptable, because the passage runs on to p. 354.
- **Broker toy vs Lupia and McCubbins:**
  - Definitions: principal, agent, status quo. The knowledge condition (p. 85: "can correctly infer whether the agent’s proposal is better or worse for her than the status quo") matches "you can tell a good bond from a bad one".
  - Theorem 5.1 (p. 85) is stated correctly, including "the worst that can happen … is the retention of the status quo" (pp. 85–86).
  - "With knowledge, you refuse a bad bond. With the incentive, he never offers one" follows the authors' two cases (pp. 85–86).
  - Theorem 5.1′ (p. 92): "If either condition is not satisfied, then delegation fails."
  - The p. 207 footnote: "may be subject to verification or a penalty for lying".
  - The recall card is correct. Exceptions: n8 and M2.
- **Short answer (c):** "trust in an agent needs knowledge or a working incentive" is correct as a necessary condition (neither → fails). Searle does treat money, contracts and corporations as institutional facts (pp. 35–36, 79, 97). The verdict and what would change it are labelled ours.
- **Hook (new wording):**
  - Kirilenko p. 2: "a mutual fund complex", 75,000 contracts, "approximately $4.1 billion", "as a hedge"; "chose to execute this sell program via an automated execution algorithm"; "target an execution rate set to 9% … without regard to price or time" ("set to sell a fixed share" is fair).
  - Buy-side depth "less than 1%" of start-of-day at 2:45:28, about 13 minutes after 2:32; five-second pause; "automated pre-trade safeguard procedure" (fn 1); "prices stabilized" (p. 2); 3:08 "back to nearly their pre-drop level" (p. 3), "about twenty minutes later" (≈ 23 min).
  - The futures definition is common knowledge.
- **Harari:**
  - Every timestamp matches the transcripts within 3 s: WEF [2:00], [2:47], [2:58], [3:26], [5:48]–[5:52], [5:57], [6:06], [8:07], [10:36], [11:39], [15:14], [16:27]–[16:47], [17:29] ("USAI" correctly elided), [19:11], [19:23], [26:26]–[26:33], [30:55], [31:07]–[31:11], [31:54], [31:59]; BIS [3:00], [3:09], [3:30], [5:14], [5:28], [8:41], [8:53], [9:21], [9:54], [10:16]–[10:24], [12:42], [16:21], [20:46], [21:37], [22:56], [23:15], [25:14]–[25:57], [27:04], [30:07], [30:17]–[30:28].
  - The quotes are verbatim in Guardian 2023, Guardian 2024 (incl. the full "not yet powerful enough … by themselves" clause and the "Unfortunately" turn), Ynet and Poole.
  - The firmness groups are consistent: "I think" flagged, the [30:55] concession present, the [8:41] condition present. The four "ten years" are kept apart.
  - The strongest unhedged lines are present in the hook and fold-out. No passages are joined, apart from same-passage adjacent lines.
- **IMF:**
  - p. 78 "quite uncomfortable", "liability", "remain mostly speculative" (GenAI "revolutionary" uses); p. 82 "evidence is mixed", "there is evidence that sophisticated AI has not yet been implemented widely", "a human trader may ultimately make the trading decision".
  - p. 83 "in the near term (three to five years), especially for large capital allocation decisions", "use AI-driven SupTech tools", Mercer survey 59% / 11% (round-1 image check stands); p. 86 "about 70 percent of equities trading and more than half of futures trading".
  - p. 88 "de-risk or even shut down", "under certain conditions"; p. 89 "On balance … highly uncertain" (now scoped to the future impact); p. 92 "currently … appear contained" (the use of AI in capital markets "still relatively nascent"); p. 93 "may herd …" and "institutions are responsible for AI systems they deploy"; p. 101 definition.
- **FSB:** p. 1 "could lead to increased correlations in trading, lending, and pricing"; p. 21 "as if it were a single institution" (segment using the same models); p. 2 "more work may be needed" (page footers checked).
- **Gensler and Bailey:** p. 2 "a more mature stage of broad adoption" (hypothesis); pp. 13, 17, 21, 22, 25 verbatim; hedges kept.
- **Danielsson and Uthemann:** abstract "game-theoretic model", "amplifies existing financial system vulnerabilities", "faster and more severe", own AI systems; introduction "both stabilise and destabilise … depending on the severity of the shocks … and how prepared the financial authorities are". Danielsson et al. 2022 p. 7 unchanged.
- **Arora et al.:**
  - CACM p. 101 "in industry-standard models, the pricing problem can be as difficult as solving the planted dense subgraph problem". "Cannot tell a fair price from an inflated one" matches p. 102 ("distinguishing it from a normal ('unrigged') higher yield derivative is computationally intractable").
  - ICS pp. 50–51 lemon cost as the gap for trade; p. 52 formula and "position"; p. 55 bottom line with the seller-pooling condition; p. 61 Theorem 9.
  - Theorem 10 conditions are right: D = inputs per product, M = products, "If D ≫ log³ M", ex-post detectable; p. 62 "a level of transparency that currently does not exist". p. 63 "clearly only a first step" and the full "raise the hope … tampering problem with better design".
  - The six-asset toy moves in the source's direction (concentration does more damage: 7/4 vs 3/2; 12 and 3 of 15; Δ(2) = 3/4).
- **Searle:** pp. 14, 24, 28, 32–33 (bill and type), 37, 41, 45 (×2), 69, 70, 142 at the stated printed pages; "most, perhaps all" kept; the machine application labelled ours throughout.
- **Ashby:** p. 207 "Only variety in R can force down the variety due to D; variety can destroy variety"; p. 209 "owes nothing to experiment"; p. 246 "ways that may make regulation possible", "somewhat trivial solution"; p. 247 the "only hope" condition, correctly paraphrased in Lens 1 ("If the regulator’s capacity cannot easily grow and the other ways fail"). The 16-plan toy, 13.29 / 9.29 / 6.64, and entropy 1.75 / 0.75 are right. Cover and Thomas 1991 Thm 2.6.5 is confirmed in the library copy (1st ed.).
- **Others:** Scheurer p. 1 "consistently hides the genuine reasons", "existence proof"; Truth Terminal (handler approves posts, $50,000 BTC "to the bot’s wallet", "semi-autonomous", "neither the bot nor its handler created the token"); Luo "translating natural-language trading intents into correct option strategies remains challenging", engine "validated and executed"; Mik "may turn out to be contracts in form only, not in function"; FCIC "two key mistakes" (p. 149); Granovetter "the two crowds are essentially identical" (p. 1425); N&K "primarily in the hands of people and organizations", "median outcome", impacts "slow (on the timescale of decades)"; Poole verbatim.
- **Numbers (all rerun):**
  - check.mjs 15/15. Herding: m = 0.2 gives 0.04 / −1.00 / 0.000, m = 0.9 grows, breaker ±3.00; gaps −0.9, −0.51, −0.189 and −2.30, −3.94; root sizes 0.548, 1.002, 1.162. Real roots exist only for m < 0.067 (both inside the unit circle) and m > 0.933 (larger root > 1), so "near m = 1 the roots become real, but … the larger root already exceeds 1" holds.
  - Haldane–May presets 64.8 (N = 6), 2,756 (N = 10), 43,099,804 (N = 20), ratio independent of ε, e^N/√(2πN) close. CDO 0.37%, 5.185%, 10%, 27×, 2.000% vs 0.0032%, 634.5×. N_eff 2.703, 1.099, 3.257, ceiling 3.33, check 1.33. Bayes 0.8 … 0.996, 1,048,576, 0.999999. May 0.64 / 1.28 / 0.72, max 6 links. Ashby presets 6.64 / 2.64 and 4.29.
  - Six banks: hand table rounds 1–3 (12/10, 12/9, 12/11); every Play answer (single seeds: none at 0.8, Y1 → 3 of 6 at 1.0; two X → 2 at 0.8 and 5 at 1.0; ×1.2 → 5, ×1.21 and ×1.25 → 3; ×1.5 → 3; lgd 1 → 6). Granovetter 100 → 1.
- **Standalone (WRITING §0):** no sentence refers to another AI4Read post (grep for post numbers, "earlier/previous/last post", "remember", earlier toys). The eyebrow "Post 02" is a label; "a village market" is a generic example.
- **Word count:** main text 7,325 (cap 7,500).
- **Sources list:** entries match the files used. Gensler and Bailey link is now abstract=3766555. cite-map not rechecked for new cites beyond the visible ones (all new cites point to listed sources).
