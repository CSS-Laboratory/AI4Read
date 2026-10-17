---
id: 2026-10-ai-finance/review/s2-check
stage: S2 (independent fact-check of source-brief.md)
checked: 2026-10-17
output: ../source-brief.verified.md
method: Each unit was re-read in the saved source (sources/), in Kunhao's library copy (AI4Read/library/), or in page images rendered at S2. Audio was re-transcribed per quote (±20 s) with faster-whisper small.en and medium.en (int8, CPU), and a tight medium.en pass with word probabilities was run for 3 disputed spots. All numbers were rerun in Python (scratchpad nums.py).
---

# S2 fact-check: source brief, post 02

Severity follows rubric §A, applied to the brief: a finding is rated by what the writer would have printed if they had trusted the unit.

## One line per unit
Format: **unit — verdict** — evidence — what changed (severity).

- **A1 — FIXED** — BIS mp3, segments [2:32–3:43], [4:54–5:40], [8:55–11:35], [12:22–13:02] and [29:47–31:40], re-transcribed with small.en and medium.en, plus a tight medium.en pass at [30:15–30:34].
  - The [30:07–30:28] quote "new types of financial security" was a base.en error. The audio has "new types of financial devices that no human being would ever imagine creating" (**major**).
  - Careful (iii), "not 'AI takes over'", is contradicted by [3:30]: "It could lead to power shifting from humans to algorithms, to alien forms of intelligence" (**major**).
  - "nobody at a central bank" → "nobody in the central bank" (minor).
  - [0:00–0:54] is a podcast teaser, not Harari's opening; it is now cited by the in-talk timestamps [8:41] and [16:21] (minor).
- **A2 — FIXED** — guardian-2023 .txt, paragraphs 3, 8–11. The CDO-cause sentence is the reporter's paraphrase ("adding that"), not "he says" (minor). Added: the "ideal field for AI because it's only data" quote.
- **A3 — FIXED** — WEF mp3, segments [1:40–3:18], [14:26–20:00] and [30:47–32:41], re-transcribed with small.en and medium.en, plus a tight pass at [31:50–32:10].
  - "USAI" → "U.S. AI" (minor).
  - The talk starts at ~[1:40], not 0:00 (minor).
  - The Q&A money lines lacked their frame, "at the present moment, we still think better ... prepare to the moment when this is no longer the case" (minor).
  - Added: [2:01] "not just another tool. It is an agent", and [19:11] a third "ten years" line.
  - All four quotes are confirmed. "dominated by AIs" has low confidence (p = 0.54).
- **A4 — FIXED** — nexus-penguin-sample.pdf pdf 23 and 33 (re-rendered); guardian-2024-nexus-extract .txt, lines 51–67 and the footer.
  - The existential line does not "close" the extract (minor).
  - p. xxxii is a question about how politicians can make financial decisions, not a general "what happens if" (minor).
  - All quotes are verbatim and the word counts are correct.
- **A5 — FIXED** — ynet .txt, paragraphs 1–4 and the last. "culture is made of words" dropped "almost" (minor). The quote and the 90% figure are confirmed.
- **A6 — DROP** — no saved copies exist. The items cannot be cited under charter §9; they are kept as leads only.
- **B1 — FIXED** — fcic pdf 25, 26, 57, 74, 157, 161 and 178 (images).
  - **CRITICAL:** S1's note that "Harari's 'almost nobody understood' is his gloss; the FCIC text ... does not use that phrase" is contradicted by p. 28: "the complexity bubble also burst: the securities almost no one understood". It is also contradicted by p. 45 (Reinhart: regulators "failed to appreciate the complexity").
  - Moody's deal counts are "Including all types of CDOs" (minor).
  - "often retained" (minor).
  - All the numbers ($673tn, $79bn, $73bn, 3,400/610, 220/363/749/717, $90/162/337/326bn, 2–3×) are confirmed from images.
- **B2 — FIXED** — kirilenko .txt, pdf 1, 3, 4, 6 and 7.
  - The $4.1bn is quoted on KKST p. 5, so it is SEEN, not UNSEEN (minor).
  - The "did not cause ... but contributed" quote is in the abstract (minor).
  - The "cure" is the authors' recommendation, not the regulators' (minor).
  - 36 minutes, 2:32 pm, 75,000, the five-second pause and "probably have little impact" are confirmed.
- **B3 — FIXED** — calvano .txt, pdf 1, 2, 11, 22, 28 and 30; running heads confirm p = 3266 + pdf.
  - The financial-markets section is p. 3294 only (minor).
  - The legal note is located at p. 3268 (minor).
  - Added: "even a modest price effect" (p. 3294) and the "same class" remark (p. 3296).
  - 70–90% and 85/64/56% are confirmed.
- **B4 — FIXED** — lopezlira .txt, pp. 1–6.
  - "generally increases with model size" (minor).
  - The correlation reading of the falling Sharpe ratio is ours, not the authors' "improved price efficiency" (minor).
  - 90%, 93.3/88.8%, 34 bps, 4,123 stocks and Sharpe 6.54/3.68/2.33/1.22 are confirmed.
- **B5 — FIXED** — scheurer .txt, pp. 1, 4, 5 and 8.
  - p. 8: strongly discouraging prompts give "nearly (but not exactly) 0%" misaligned behaviour; S1's "did not eliminate" dropped this (**major**).
  - "disapproved of by company management" (minor).
  - The 24-word existence-proof quote, 300 completions and 94% on 120 samples are confirmed.
- **B6 — FIXED** — fsb-2024-report .txt, pdf 5, 6, 24, 25, 29, 32 and 33 (p = pdf − 4).
  - The p. 28 sentence continues on p. 29 with "could change this in the future"; S1 used the first half alone (**major**).
  - The FSB names four drivers of correlation, not three (minor).
  - Added: "as if it were a single institution" (p. 21) and the Gensler and Bailey citations (p. 20, fn. 70 and 74).
- **B7 — DROP** — imf.org and the eLibrary returned 403 to curl on 2026-10-17. A second WebFetch summary is not verbatim; it agrees with S1 on 3 phrases and differs on the page of "mostly speculative" (78 vs 79). S1 had already marked the unit UNSEEN, so there is no severity.
- **B8 — FIXED** — cointelegraph .txt and decrypt .txt, full. Cointelegraph says both "just over" and "just under" $150m (minor). The $50k, 7,000%/8,000%, $214m and "neither the bot nor its handler" are confirmed.
- **B9 — FIXED** — arxiv-2603.16434 p. 1; 2506.01063 p. 1; 2602.09384 p. 1; duetting pp. 1, 3 and 6; buehler p. 1.
  - MIK: "may turn out to be contracts in form only" — the hedge was dropped (**major**).
  - DFNPR: RegretNet "will generally only find mechanisms that are approximately incentive compatible" (p. 3); S1 implied an exact check (**major**).
  - The MIK quote is in the abstract, not the introduction (minor).
- **C1 — FIXED** — shannon .txt pp. 1, 13 and 14. The 2^{HN} statement is Shannon's "for most purposes" gloss after Theorem 4, not the theorem (minor).
- **C2 — FIXED (status)** — library cover-2006-elements.pdf (it is the 1991 1st edition): Thm 7.2.4 and eq. (7.10) are on p. 150 (pdf 172); machine dependence p. 151; non-computability p. 163. Status CHECK-AT-SOURCE → SEEN. No content error.
- **C3 — FIXED** — arora-2011 pdf 1–8 and 12; Table 1 read from a rendered image.
  - Poly-time binary CDO: the table gives ~n√(N/M) ≫ n, not "about as large as n or larger" (minor).
  - "with significant probability" was dropped (minor).
  - "in our setting" was dropped from the tranching claim (minor).
  - Added: the "plain view yet cannot be understood" quote and the authors' caveat on the strength of their assumption.
  - 7019 × 5683, $1000/$800/$200 and n/2 are confirmed.
- **C4 — FIXED** — arora pdf 12–13.
  - The tree of majorities is on p. 12, not p. 11 (minor).
  - The concession "and this analysis is probably correct" about "faulty models" was dropped (minor).
- **C5 — FIXED (status)** — library hayek-1945-knowledge.html; every phrase is located by section (I, III, IV, V, VI). The quote is verbatim. Status → SEEN. Added: the "less perfectly as prices grow more rigid" hedge. No content error.
- **C6 — FIXED** — library akerlof pdf 2–5 and 13–14 (p = pdf + 486).
  - "nonatomistic ... concentrations of power" is on p. 488, not pp. 499–500 (minor).
  - "bad drives out good" was in quote marks but is not verbatim; the source has "The 'bad' cars tend to drive out the good" (minor).
- **C7 — FIXED** — library grossman pdf 1, 7, 9 and 12 (p = pdf + 392); (19b) was read from the p. 399 image. The digest toy's λ = 0.8 cannot be derived from a = 1, n = 5, e^{2ac} = 2 (minor). ρ² = 0.8 is confirmed.
- **D1 — FIXED** — ashby sheets 110 and 111 (pp. 206–209), rendered at 220 dpi.
  - S.11/8 starts on p. 207 (minor).
  - The printed signs are ≥ (underlined); they are not strict (minor).
  - The reprint's H_D(E) is a misprint for H_D(R), and S1 copied it into the brief (minor).
- **D2 — FIXED** — ashby sheet 131 (pp. 246–247). The "only hope" quote was given without its printed condition, "if R's capacity is not easily increased and the other methods are not possible" (**major**).
- **E1 — FIXED** — danielsson .txt pdf 3, 5, 9, 12 and 13.
  - The intelligibility clause dropped its hedge, "we might come to the point where", and S1 also dropped "This might not necessarily be the case" (**major**).
  - The "overestimate" note on the 42 years was dropped (minor).
- **E2 — FIXED** — arxiv-danielsson-uthemann pdf 1–2. "Later paper is more cautious" is not supported: the introduction says frameworks "cannot effectively prevent and resolve" AI-induced crises (minor).
- **E3 — UNSEEN-KEEP-AS-SECONDARY** — mitsloan .txt and .html metadata.
  - The "handful of foundational AI models ... herding" point is Gensler to the NYT, not the paper, but S1 listed it under the paper's claims (**major**).
  - The article is from 2023 (Vereckey), not 2020 (minor).
- **E4 — FIXED** — library keynes-1936-general.html, ch. 12. The convention passage is § IV in standard numbering; S1 put it in § III, and the HTML has no IV heading (minor). The "six prettiest", "third degree" and "fail conventionally" passages are confirmed in § V.
- **E5 — FIXED** — library morris pdf 2, 6, 8, 9 and 10. The welfare condition (19)–(20) is on p. 1529 (minor). Eq. (13), the toy numbers and the p. 1530 claim are confirmed.
- **E6 — FIXED** — library granovetter pdf 1, 5, 6, 8 and 9. The quoted "Two crowds that look nearly identical" is not verbatim; the source has "the two crowds are essentially identical" (p. 1425) (minor). The 12.2 threshold, "about six" and the limit of 50 are confirmed.
- **E7 — FIXED** — minsky .txt pdf 8–9.
  - "under monetary tightening" dropped "in an inflationary state" (minor).
  - The commercial-paper instance clashes with the printed text, which calls such issuers "typically hedge units" (minor).
- **E8 — OK** — our arithmetic; all values rerun (see below). Added: the FSB p. 21 anchor.
- **F1 — OK** — sep .txt; § 4.2.3, § 5.6 and § 5.2 are confirmed by position.
- **F2 — FIXED** — library keynes ch. 17, §§ II, III and V. The equilibrium equality includes expected appreciation (a₁ + q₁ = a₂ − c₂ = l₃) (minor).
- **F3 — FIXED** — library dennett, OCR of sheets 12–23. The thermostat passage starts on p. 29 (minor). p. 24 and pp. 16–17 are confirmed.
- **F4 — OK** — library lupia pdf 97–108 and 221–223 (p = pdf − 16). All pages and claims are confirmed. Added: Theorem 5.1′ (p. 92).
- **F5 — FIXED** — WEF audio [14:38–19:23]. It now has the audio-checked wording and drops its dependence on A6. No new error.
- **G1 — OK** — poole .txt, paragraph 26; datePublished 2024-09-11.
- **G2 — OK** — fox .txt, line 50; datePublished 2024-09-10.
- **G3 — OK** — narayanan .txt. All quotes are confirmed. Added: the "thought to have played a part" hedge and "rejects ... AI itself as an agent".
- **G4 — FIXED** — BIS audio [6:53–8:20], plus a tight pass at [7:13–7:32] and [29:47–31:40]. The [7:18] wording is confirmed; one medium.en run inserted "at least" and three passes omit it. Added: Harari's "your example with the airplane is perfect" [9:12]. No error.
- **G5 — FIXED** — derived. Row (b) listed B1 only as "against" ("CDOs failed on correlation, not mystery"), which carries the B1 error into the tension map (**major**). B7 was removed.

## Counts (rubric §A, applied to the brief)
- **Critical: 1** — B1 (the FCIC does use "almost no one understood", p. 28).
- **Major: 10**:
  - A1 ×2 (the misquote "financial security"; the "not AI takes over" note, contradicted by [3:30]);
  - B5 (nearly 0%);
  - B6 (the p. 29 continuation);
  - B9 ×2 (MIK "may"; DFNPR approximate incentive compatibility);
  - D2 (the "only hope" condition);
  - E1 ("might" dropped);
  - E3 (the NYT remark attributed to the paper);
  - G5 (the B1 error carried into the map).
- **Minor: 44** — listed per unit above.

Verdicts across the 42 units:
- 6 OK (E8, F1, F4, G1, G2, G3);
- 33 FIXED (including C2 and C5, where only the status changed);
- 2 DROP (A6, B7);
- 1 UNSEEN-KEEP-AS-SECONDARY (E3).

All 10 CHECK-AT-SOURCE units were verified at the page in the library: C2, C5, C6, C7, E4, E5, E6, F2, F3 and F4. Dennett is a scanned PDF and was read by OCR (tesseract), so print its quotes with a final glance at the page image.

## Numbers rerun (Python, scratchpad nums.py)
- **C2:** log₂ 10^4 = 13.2877; 2^10 − 1 = 1023 (10.23%); 2^6 − 1 = 63 (0.63%); Σ_{i<10} 2^i = 1023. ✔
- **C1/W1:** H = 1.75 bits. ✔
- **C3:** 7019 × 5683 = 39,888,977 ✔; 0.8 × 1000 = 800, lemon cost 200 ✔; C(100,10) = 17,310,309,456,440 ≈ 1.731e13 ✔; n/2 = 5 ✔.
- **C7:** 1 − ρ² = (2 − 1)/5 = 0.2, so ρ² = 0.8 ✔; m = 0.25 and 1/(1+m) = 0.8 ✔ (consistent with eqs. 17 and 19a); λ = 0.8 is **not derivable** ✘.
- **D1:** V_O ≥ 2 − 1 = 1 bit ✔; the entropy form with H(D) = 1.75 and H(R) = 1 gives H(E) ≥ 0.75 ✔.
- **D2:** log₂ 10^4 − log₂ 10^2 = 6.644 ✔.
- **E5:** public weight 1/11 = 0.0909 ✔; Bayesian 1/101 = 0.0099 ✔; W(1) = −0.01653 ✔; W(2) = −0.02083 ✔; W(0) = −0.0100 ✔; threshold β/α ≤ 12.5.
- **E6:**
  - uniform → 100 ✔; perturbed → 1 ✔;
  - normal with mean 25, by standard deviation: 12.0 → 4.0; 12.2 → 5.5; 12.3 → 100 (the jump between 12.2 and 12.3 ✔; "about six" ✔); 50 → 90.5; 1000 → 51 (limit 50 ✔).
- **E7:** at 5%, interest 5 and payment due 25: income 30 → hedge, 10 → speculative, 3 → Ponzi ✔; at 10%, income 8 < interest 10 → Ponzi ✔.
- **E8:**
  - N_eff = 10, 2.703, 1.099, 1 ✔; 0.01^10 = 1e−20 ✔;
  - 4^n/(4^n + 1) = 0.5, 0.8, 0.9412, 0.9846, 0.9961 ✔;
  - iterate toy (A = 1.5, G = 0.5, shock −1 at t = 3): m = 0.2 decays ✔; m = 0.67 oscillates across zero with slowly growing amplitude (|z|² = A·m = 1.005; peaks 2.53, 2.54, …, 2.7 by t = 40) ✔; m = 0.9 diverges (|p| ≈ 1,346 by t = 40) ✔.
- **B1:** deals 220 + 363 + 749 + 717 = 2,049; value $915bn in total; 2006 / 2004 = 3.4×. These are context only, not used in the brief.
- **B4, B8:** source figures copied; nothing to compute.
- **Word counts:** every quote in the verified brief was recounted and is ≤ 25 words.

## Audio check (every Harari or Skingsley quote used)
Comparison against small.en and medium.en (and a tight medium.en pass where marked):
- **BIS [0:00–0:22]** "unfathomable ... regulate it": both models agree. It is a teaser clip; in the talk it is at [8:41–8:59]. ✔
- **BIS [3:00]** "maybe 1% of the population really understands how the financial system works": both agree. ✔
- **BIS [3:13]** base.en "nobody's / nobody is a central bank" → both newer models give "nobody in the central bank". FIXED.
- **BIS [3:30]** "power shifting from humans to algorithms, to alien forms of intelligence": both agree. Added.
- **BIS [5:13]** "the first tool that we created that can actually understand finance better than us": both agree. ✔
- **BIS [9:54]** "AIs create a new financial device which is orders of magnitude more complicated than CDOs": both agree. "AI's" → "AIs". ✔
- **BIS [10:08]** "trillions of data points": both agree. ✔
- **BIS [10:27]** "and then something goes wrong and nobody knows why": both agree. ✔
- **BIS [12:42]** "humans are extremely adaptable": both agree. ✔
- **BIS [30:20–30:33]** base.en had "new types of financial security. What types of financial devices that no human being would ever imagine creating?" small.en, medium.en and the tight medium.en pass all give "coming up with new types of financial devices that no human being would ever imagine [creating]" as one Harari sentence. **FIXED (major).**
- **BIS [7:18], Skingsley** "most of us happily step into an airplane, having very vague understanding of how that works": base.en, small.en and the tight medium.en pass agree. The long medium.en run alone inserts "at least". Kept without it; flagged.
- **BIS [7:43–7:48], Skingsley** "no further AI without further trust": both agree. ✔
- **BIS [31:00], Skingsley** "But I am more optimistic than you": both agree. ✔
- **WEF [2:46]** knife and money line: verbatim in both. ✔
- **WEF [16:28]** "They will soon be able to make the decisions necessary to manage a bank account": both agree. ✔
- **WEF [17:29]** "Suppose some U.S. AI persons invent ... don't know how to regulate": both agree. "USAI" → "U.S. AI". ✔
- **WEF [17:05]** base.en "deregulating AIs" vs "deregulating AI" in both newer models: minor; shown as "AI[s]".
- **WEF [31:11]** "when AIs create a new financial system that they understand and we don't understand": both agree. ✔
- **WEF [32:00]** "Maybe nobody in the room, no human in the room, understands the financial system anymore, because it's dominated by AIs":
  - "Maybe" is in base.en, the long medium.en run and the tight medium.en pass (p = 0.99), but small.en drops it. Kept.
  - Final word: "AI" (p = 0.54) or "AIs". Flagged.

## The writer must not use
1. Anything from the IMF GFSR ch. 3 (B7), including "remain mostly speculative", "70%", "three to five years" and "may herd".
2. The A6 Harari items (Big Think, OfficeChai, the FT op-ed via Infobae, IMF Café, El Economista), and the WEF podcast page, Smith-Ruiu and Konch.
3. "new types of financial security" (BIS); "AI's"; "USAI"; "nobody is / at a central bank".
4. Any statement that the FCIC does not say the CDOs were poorly understood, or that the 2008 failure was "correlation, not mystery".
5. FSB p. 28 "not widely observed at present" without "could change this in the future" (pp. 28–29).
6. Scheurer's "the prompt did not eliminate the behaviour" without "nearly (but not exactly) 0%"; any misalignment or deception percentage read from their figures.
7. Danielsson et al.'s "will be intelligible" clause without "we might come to the point where"; "Minsky moment" without "This might not necessarily be the case".
8. Ashby's "only hope" without its condition; a strict inequality sign in the entropy form; "H_D(E)" as printed.
9. MIK's "contracts in form only" without "may turn out to be"; DFNPR as an *exact* incentive-compatibility check.
10. "As much as n or larger" for Arora's poly-time binary CDO (use "much larger than n", ~n√(N/M)); any Arora formula beyond Table 1 as read; Arora "proves" (use "shows, under a conjectured assumption").
11. The NYT "handful of foundational AI models" and Bloomberg "crisis of 2032 or 2028" remarks as Gensler and Bailey's paper; the MIT Sloan text as the paper's text; the MIT Sloan article as 2020.
12. The Grossman–Stiglitz toy's λ = 0.8.
13. "A firm that rolls over commercial paper" as Minsky's own speculative example.
14. "Two crowds that look nearly identical" (Granovetter) and "bad drives out good" (Akerlof) as quotations.
15. Hayek or Keynes page numbers (cite sections only); "Economist, 28 Apr 2023" as the origin of the Ynet essay.
16. Cover and Thomas pages as second-edition pages.
17. A single GOAT market-cap figure from Cointelegraph (it is internally inconsistent).
18. Lopez-Lira and Tang's 90% as a trading return, or their falling Sharpe ratio as a "correlation" finding of the authors.
19. BIS [0:00–0:54] as Harari's "opening" (it is a podcast teaser).
