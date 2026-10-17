---
id: 2026-10-ai-finance/review/verify-2
stage: S5, round 2 (independent fact-check of the revised draft, checker A)
checked: 2026-10-17
draft: src/content.html (all visible text, 15 widget configs, diagram step texts, captions, fold-outs, Sources), audio-script.md, english-gloss.json (factual content of examples)
round-1 inputs checked against the text: review/verify-1.md, review/verify-1b.md, review/round1-merged.md, review/response-1.md (writer's claims re-checked in the text, not trusted)
not read: self-review.md, critic files (independence)
method: Every cited sentence re-opened at the source. Danielsson et al. 2022 read in the published JBF PDF (p. 7 = pdf 8, running head checked). Arora WP pp. 2-5, 12; FSB report pp. 1, 20-21, 28-29 and press release; Scheurer pp. 1, 8; Luo, Mik, Cointelegraph, Decrypt, MIT Sloan, Poole, Ynet, Guardian 2023, N&K, D&U, SEP §§ 4.2.3 and 5.6 in the saved copies; FCIC p. 128 page image; Keynes ch. 12 and Lupia pp. 85-86, 207 and Akerlof pp. 489-490 in the library copies. Audio: re-transcribed with faster-whisper small.en (int8; WAV cut with ffmpeg -ac 1 -ar 16000, loaded with `wave`): BIS [5:08-5:42], [12:36-12:55], [16:05-16:30], [20:30-21:00], [21:30-22:10], [22:48-23:32], [25:05-26:12]; WEF [2:38-3:00], [5:44-6:12], [7:58-8:20], [16:10-16:52], [17:25-17:50], [25:50-26:42], [30:50-31:30], [31:50-32:16]. Both base.en transcripts re-read in full for the balance check. Numbers: check.mjs (15/15 configs OK; every preset, seed set and quoted value rerun with --id/--values/--seeds), the three notebooks, and scratchpad v2/nums.py.
---

# S5 fact-check, round 2: post 02

Severity follows rubric §A. Source quotes are at most 25 words. Section names are the `id`s in `src/content.html`.

## (a) Round-1 fix verification

### Binding list (round1-merged.md, A)
| id | Verdict | Evidence |
|---|---|---|
| A1 Danielsson hedge | **fixed** | `lens-control` lever 2 quotes "will likely be unintelligible to humans", cited Danielsson et al. 2022, p. 7. Published PDF: the sentence is on journal p. 7 (pdf 8; running head "Journal of Banking and Finance 140 (2022) 106290"). Audio `lens-control` matches. Source entry is the 2022 JBF paper with DOI. |
| A2 Harari's unhedged capability claims | **fixed** (but see new M1) | `home` "He asserts, without hedges": BIS [5:14], [16:21], WEF [2:47], [5:57], with the verb "asserts". Re-transcribed: all four verbatim. Limits and remedies present ([8:07]; [21:37]; [22:57]). Summary sentence present. New M1 shows the summary is not true of his personhood timelines. |
| A3 Truth Terminal liability | **fixed** | Text, `dg-status` step 4 and node, audio `lens-social`: "the reports say nothing about who would be liable". Cointelegraph: Bitcoin sent "to the bot's wallet"; Decrypt: "neither the bot nor its handler created the token". Brief F5 corrected. |
| A4 Arora toy | **fixed** | `lens-info` Ladder 2 now matches WP p. 4: seller over-represents junk "just enough to skew the probability of default"; detection is "the so-called hidden dense subgraph problem, which computer scientists believe to be intractable". C(100,10) only as brute force. Δ(n) cited p. 5 (verified, incl. the "position" quote), Table 1 p. 6. |
| A5 FSB merge | **fixed** | `llm` "Not found" and `box-layers` critics keep "not widely observed" (p. 1) and "could change this" (pp. 28-29) apart from the frameworks statement (press release). |
| A6 Keynes merge | **fixed** | `lens-decision`: § IV and § V joined by "Separately"; both quotes verbatim in the library text. Audio matches. |
| A7 Ashby condition | **fixed** | `lens-control` states the column rule (p. 207) before the bound; `box-ashby` derivation is correct (given R, D and E are in one-to-one correspondence, so H(D|R) ≤ H(E|R)). Audio `lens-control` gives "only hope" with its full condition. |
| A8 Playground answer (2) | **fixed** | check.mjs `cs-w5`, lgd 1: X1+X2, X1+X3, X2+X3 each 5/6; X1+X2+X3 6/6. Page text matches. |

### Checker A (verify-1.md)
| id | Verdict | Evidence |
|---|---|---|
| M1-M3, M6, M7 | fixed | as A1, A5, A6, A3, A7 above |
| M4 knife line | fixed | `home` [2:47]; re-transcribed: "AI is a knife that can invent new kinds of knives, as well as new kinds of music, medicine, and money." |
| M5 present-tense finance assertions | fixed | [5:14] in `home`, `g4` answer, `answer` keypoint; "It's only data, it's only information" [5:27] in `box-harari` (audio [5:28]). |
| m1 CDOs | **partly** | "pools of loans" is gone, but the new wording adds "in 2008 mostly", which p. 128 does not say (new n1). |
| m2 $214M outlet | fixed | $122M cited to Cointelegraph, $214M to Decrypt. |
| m3 Lopez-Lira | fixed | removed from page, sources, numbers.md. |
| m4 timestamps | fixed | [10:19], [30:55], [6:06] (all re-transcribed). |
| m5 "three ten years" | fixed; side issue | "at least three". [26:33] added to `box-harari`, but without his "I don't know how long it will take" (new n2). |
| m6 Harari's own limit | fixed | `home` [8:07]; `lens-social` [8:07], [11:39]. |
| m7 Harari's remedies | fixed | `home` and `box-layers` ("Harari's own remedy"). |
| m8 chain is ours | **partly** | `lens-social` text says "Our compression (ours) … The last step is ours". But the new `dg-chain` is titled "Harari's chain" and labels links that are not his (new M3). |
| m9 audio "only hope" | fixed | |
| m10 Poole | fixed | "(so invention is the weak link: our reading)". |
| m11 N&K hedge | fixed | "their 'median outcome', not a certainty". |
| m12 Conditional 5 | fixed | labelled ours; liability split off. |
| m13 Conditional 4 | fixed | matches Lupia Theorem 5.1 (pp. 85-86, re-read). |
| m14 Layer 3 "could" | fixed | |
| m15 Δ(n) page, "hard part" | fixed | |
| m16 2010 lesson | fixed | "Our reading (ours)"; "simple" dropped. |
| m17 "says nothing" | fixed | recall card 2 and audio. |
| m18 ρ = 0 readout | fixed | readout template has no ceiling; prose gives 1/ρ only for ρ > 0. |
| m19 source list | **partly** | Danielsson entry fixed. Several URLs are truncated and do not resolve; three arXiv entries have no title (new n10). |
| m20 concessions | fixed, but over-corrected | Arora p. 12 "probably correct" added. D&U now appear *only* with their concession; their central finding was removed (new M2). |
| m21 Skingsley, "works best" | fixed | page, audio, gloss example. |

### Checker B (verify-1b.md)
| id | Verdict | Evidence |
|---|---|---|
| M1-M4 | fixed | as A2, A1, A3, A4 |
| 1 hook | fixed | BIS [8:59]-[9:12] re-read: "a very big difference … your example with the airplane is perfect". |
| 2 tool vs agent | fixed | contrast dropped. |
| 3 bridge to post 01 | fixed | "Our bridge … he asks whether …" [5:20]. |
| 4 words vs stories, "money is trust" | fixed in text | "stories" (Ynet) and "money is really trust" [23:15] (re-transcribed) kept apart. Diagram: see M3. |
| 5 "indirectly, via wars" | fixed | `box-harari`, verbatim from Guardian 2023. |
| 6 limits and remedies | fixed | [20:46] "History is never deterministic" (re-transcribed), [12:42], [21:37], [22:57]. |
| 7 FSB p. 1 as background | fixed | |
| 8 $214M outlet | fixed | |
| 9 RegretNet | fixed | "will generally only find … approximately incentive compatible" (p. 3). Audio fixed (16). |
| 10 OQL gloss | **partly** | "(our gloss)" and "a candidate strategy" added. `dg-llm` step 4 still says "The LLM proposed; the checker decided (our gloss)"; response-1 says this was removed (new n8). |
| 11 tree of majorities | fixed | "perhaps", "in their simple model", o(2^k) vs √(3^k) all match p. 12. |
| 12 playground | fixed | as A8. |
| 13 Am > 1 | fixed | `box-gain`; also verified that Am < 1 ⇔ the swing shrinks holds for every m in [0, 1] in this toy (real roots for m < 0.067 and m > 0.933 included). |
| 14 sources entry | fixed | |
| 15, 16 audio | fixed | |
| 17 "simple" / lesson | fixed | |
| 18 CDO | partly | see m1 / n1. |
| 19 W4/W5 labels | fixed | no "W4", "W5" or "world W" anywhere in page, audio or gloss. |
| 20 Ashby condition | fixed | |
| 21 N&K "in this world" | fixed, wording imperfect | see n11. |
| 22 "best-supported" | fixed | "most plausible … our judgment, not a finding". |
| 23 [6:06] | fixed | |
| 24 Dennett | moot | quotation removed. |
| 25 Lupia p. 207 | fixed | "in their example, candidates supervised by a party leadership 'may be subject to verification or a penalty for lying'" (p. 207, n. 2, library copy). |
| 26 lede | fixed | "financial devices". |
| 27 FSB drivers | fixed | "four *possible* drivers"; FSB p. 20 "could be driven by several factors, including". |

Writer's claims in response-1.md that are **not** borne out by the text: (i) B-10 "'the LLM proposed, the checker decided' removed" (still in `cfg-llm` step 4); (ii) m19 "URLs or DOIs added to the entries" (several are truncated host paths, see n10). Everything else claimed in response-1.md was found in the text.

## (b) New findings

### Major (3)

**M1. Balance and labels: Harari's unhedged personhood forecasts are presented as "a policy question, not a forecast"** — `lens-social` (Personhood), `box-harari` (heading "Questions, limits and remedies"), audio `lens-social` and `home` trap; also the summary sentence in `home`
- Post: "AIs 'will soon be able to make the decisions necessary to manage a bank account' [WEF 2026 [16:28]]. A policy question, not a forecast." The fold-out lists [16:28] under "Questions". Audio trap: "That one is a deadline for a decision, not a forecast." Summary: "his timelines and finance scenarios are hedged."
- Source (WEF, re-transcribed [16:17-16:48]): "Unlike rivers and gods, AIs can actually make decisions by themselves. They will soon be able to … manage a bank account, to file a lawsuit and even to operate a corporation" … "AIs can therefore function as persons." [19:11]: "10 years from now, it will be too late for you to decide … Somebody else will already have decided it for you."
- What is wrong: the quoted sentence is an unhedged forecast with a timeframe ("will soon"); only the follow-up "Do we want to allow that?" is a question. [19:11]-[19:23] is also an unhedged forecast. Labelling them "not a forecast" and filing them under "Questions" makes Harari look more cautious than he is, and makes the summary "his timelines … are hedged" false for these two lines (the hedged timelines are the finance-device ones: BIS [9:54], WEF [31:54]).
- Severity: **major** (balance rule; speech act mislabelled in the direction the rule warns about).
- Fix: Write "He forecasts, without a hedge, that AIs 'will soon be able to … manage a bank account' [16:28], and asks whether your country will recognise them as legal persons; the recognition question is policy, the capability claim is a forecast." Move [16:28] (and [16:19] "AIs can actually make decisions by themselves") to "Asserted, no hedge"; narrow the summary to "his finance-device timelines are hedged"; in the audio trap say "a deadline for a decision" without "not a forecast".

**M2. Balance: Danielsson and Uthemann appear only as a reassuring counterweight; their central finding was removed** — `lens-control` ("Counterweights"); audio `lens-control`
- Post: "Counterweights. … Danielsson and Uthemann: AI 'can both stabilise and destabilise the financial system' [introduction]." Lever 2 cites them only for proposing that authorities build their own AI. (Round 1 also had their "cannot effectively prevent and resolve"; it is gone.)
- Source (arXiv 2407.17048v3, abstract): AI "amplifies existing financial system vulnerabilities … The consequence is crises become faster and more severe". Introduction, next sentence after the post's quote: "current regulatory frameworks cannot effectively prevent and resolve such AI-induced crises".
- What is wrong: the post keeps the authors' concession and drops their unhedged main result, then files them under "Counterweights" next to the FSB's "frameworks address many vulnerabilities". Readers get the opposite of the paper's conclusion. (This is the over-correction of round-1 m20, which asked to *add* the concession, not to replace the finding.)
- Severity: **major** (balance rule: a central unhedged claim omitted, so the authors look more reassuring than they are).
- Fix: In lever 2: "Danielsson and Uthemann find that AI 'amplifies existing financial system vulnerabilities' and that current frameworks 'cannot effectively prevent and resolve' AI-induced crises; they propose that authorities build their own AI." Keep "can both stabilise and destabilise" as their qualification, and move them out of "Counterweights" (or say "partly a counterweight"). Same in the audio.

**M3. The chain diagram mislabels its evidence and calls our chain Harari's** — `answer`, `dg-chain` (title, edge labels e2 and e4, steps 2 and 4); audio `answer` ("a figure shows his chain")
- Post: title "Harari's chain, with an evidence label on each link". Edge e2 (AI masters words → AI takes over money and finance) is labelled "hedged", while step 2 says "Our compression (ours)" and cites the unhedged [5:14]. Edge e4 (AI invents instruments → "Shared, opaque, hard to check") is labelled "supported in toys"; step 4: "Shared models make failures arrive together and hide reasons. Shown in toys (Lens 3)".
- Sources: Lens 4 of the post itself: "The last step is ours; he does not state it in these sources." The toys (`cs-w5`, `it-herding`, `lab-neff`) model correlated failures among *ordinary* lenders/traders; none involves hidden reasons or AI-invented instruments. Hidden reasons come from Scheurer et al., whose authors "do not aim to draw conclusions about the likelihood of this behavior occurring in practice" (p. 1). "Shared models" is the FSB's and ours, not a step Harari states.
- What is wrong: (i) nodes c5-c6 and links e2, e4 are not Harari's, yet the title says his chain; (ii) e2's label "hedged" describes a link he never states (its honest label is "ours, not stated"); (iii) e4 attributes "hide reasons" and the invention → shared-model step to toy evidence that does not test them.
- Severity: **major** (our inference presented as the author's chain, and evidence labels that overstate support, in the post's synthesis figure).
- Fix: Title "Our compression of Harari's chain, with an evidence label on each link"; e2 label "ours (he does not state it)"; e4 label "shared-model correlation: toys + FSB 'could'; hidden reasons: one red-team existence proof", and drop "hide reasons" from "Shown in toys". Make the audio sentence say "our compression of his chain".

### Minor (13)

**n1. CDO composition: an unsupported quantifier** — `home` (2008); audio `home`. Post: "pools of debt, in 2008 mostly slices of mortgage-backed securities … [FCIC 2011, p. 128]". FCIC p. 128 (page image): CDOs "purchase and pool financial assets such as the riskier tranches of various mortgage-backed securities". Neither "mostly" nor "in 2008" is on the page (CDO issuance peaked before 2008). Fix: "pools of debt securities, such as the riskier tranches of mortgage-backed securities".

**n2. Harari's own hedge on his writing timeline is dropped** — `box-harari` ("Asserted, no hedge"). Post: "On himself as a writer: 'Two years, five years, ten years, it will beat me' [26:33]". WEF [26:09-26:33] (re-transcribed): "something is going to be better than us in thinking, if thinking means putting words in order … AI will beat me. I don't know how long it will take." Fix: add "I don't know how long it will take" (and his "if thinking means putting words in order"), or move the timeframe to the hedged list.

**n3. Scheurer: the "nearly 0%" attaches to the wrong behaviour** — `llm` item 4; audio `llm`. Post: "… then 'consistently' hid its genuine reasons from its manager. … Prompts that strongly discourage it bring it to 'nearly (but not exactly) 0%'". After that sentence "it" reads as the hiding. Scheurer p. 8: the ~0% is the rate of "misaligned behavior" (acting on the tip); "the tendency to deceive, conditional on misalignment, remains high under all prompts". Fix: "Prompts that strongly discourage insider trading bring the trading to 'nearly (but not exactly) 0%'; when it does trade, it still tends to hide it."

**n4. "already" added to a quoted claim** — `answer` keypoint; audio `answer`. Post: "Harari asserts that AI can already understand finance better than us". BIS [5:13-5:17]: "AI is the first tool that we created that can actually understand finance better than us." "already" is his word only for words at WEF [5:51] ("AI already thinks better than many of us"). Fix: "can actually understand finance better than us".

**n5. Term box: correlation range and variance** — `lens-decision` term box; audio `lens-decision`. "The correlation ρ of two forecasters, from 0 to 1" — correlation runs from −1 to 1; and variance is the average squared distance from the mean (the box's "average squared size" is right only for errors with mean 0). Fix: "from −1 to 1; here we only use 0 to 1"; "its average squared distance from its mean (for unbiased errors, its average squared size)".

**n6. Displayed arithmetic does not add up** — `lens-control` lever 3; audio. "lowers V_D by 13.29 − 6.64 = 6.64 bits": as printed, 13.29 − 6.64 = 6.65 (exactly, log₂10⁴ − log₂10² = 6.644). Fix: "by 6.64 bits, exactly half of 13.29".

**n7. Short answer, our reading stated more strongly than its own sources** — `answer` "Short answer"; audio. (i) "People stay accountable only if someone can verify what the AI did *and* be penalised" — Lupia and McCubbins (pp. 85-86): with one condition met "the worst that can happen … is the retention of the status quo"; accountability is lost "when neither condition is satisfied" (the post's own Lens 4 table says so). (ii) Supervisors "could not … foresee a shared model's failures" is an unhedged claim with no source. Fix: "People keep control only if they can verify what the AI did or the agent has reason to be honest; an agent that hides its reasons removes the first"; "they may not foresee …".

**n8. OQL diagram gloss kept although response-1 says it was removed** — `dg-llm` step 4: "Only then can a trade follow. The LLM proposed; the checker decided (our gloss)." Luo et al. abstract: OQL queries are "validated and executed deterministically by an engine to instantiate executable strategies". It is labelled ours, so this is minor, but the node "Trade" and the step overstate what the paper's pipeline outputs. Fix: node "Executable strategy"; "Only then is there an executable strategy (our gloss)".

**n9. Truth Terminal: the handler's role is cut short** — `llm` item 2; audio. "its human handler only approves 'its X posts'". Cointelegraph: "with its human handler only approving its X posts and deciding who it gets to interact with." Fix: add "and decides who it interacts with".

**n10. Source list: truncated URLs and missing titles** (round-1 m19, partly fixed) — `sources`. Truncated paths that do not resolve: WEF "weforum.org/podcasts", Guardian 2023 "…/2023/nov/09", FCIC "govinfo.gov/content/pkg/GPO-FCIC", Kirilenko "cftc.gov/oce_flashcrash0314.pdf", MIT Sloan "mitsloan.mit.edu/ideas-made-to-matter", Poole "…/2024/sep/11", Fox "…/2024/sep/10". No title: Scheurer, Luo, Dütting. Full URLs and titles are in `sources/MANIFEST.md`. Fix: copy them in.

**n11. Narayanan and Kapoor's scope** — `lens-control` counterweights; audio. "Narayanan and Kapoor, for AI short of superintelligence". Source (intro): "a world with advanced AI (but not 'superintelligent' AI, which we view as incoherent as usually conceptualized)". "Short of" implies they treat superintelligence as a coherent higher level. Fix: "in a world with advanced AI (they reject 'superintelligence' as incoherent)".

**n12. "works (a plane)" in the Lupia table is an unlabelled mapping** — `lens-social` table. Skingsley's point is that passengers fly with "very vague understanding" [7:18], i.e. low personal knowledge; placing "a plane" in the "knowledge yes" cell only works if knowledge comes from regulators and experts, which the post does not say. Fix: "(ours: a plane, where regulators supply the knowledge)" or drop the example.

**n13. The Davos talk's own finance-device scenario is missing from "All of Harari's lines"** — `box-harari`. WEF [17:29-17:46] (re-transcribed): "Suppose some U.S. AI persons invent super efficient and super complex financial devices that humans cannot fully understand and therefore don't know how to regulate." It is the talk's only device scenario and is hedged ("Suppose"), so it supports the post's reading; the critic asked for the full list. Fix: add it under "Scenarios and hedged statements".

### Balance check (summary)
- Harari: the strongest unhedged lines on the post's question are now in the main text (BIS [5:14], [16:21]; WEF [2:47], [5:57]), and his limits and remedies are kept. Remaining problems: M1 (personhood forecasts labelled as questions) and n2 (a hedge dropped in the other direction). I searched both full transcripts; no other central unhedged finance claim is missing. WEF [2:00] ("not just another tool. It is an agent") and [5:51] ("AI already thinks better than many of us", about words) are absent from the page; they are not about finance and the words thesis they support is printed, so I do not count them.
- Danielsson and Uthemann: M2.
- Narayanan and Kapoor, FSB, Skingsley, Poole, Arora: hedges and concessions kept; n11 is wording only.

## (c) Counts
- **Critical: 0**
- **Major: 3** (M1 personhood forecasts mislabelled / balance; M2 D&U balance; M3 chain diagram labels)
- **Minor: 13** (n1-n13)

Round-1 items: 8/8 binding items fixed; of checker A's 28 and checker B's 31 items, all are fixed except A-m1/B-18 (partly, n1), A-m8 (partly, M3), A-m19 (partly, n10) and B-10 (partly, n8); A-m20 is fixed but over-corrected (M2).

Note outside the rubric: a crude count of visible main-text words (fold-outs excluded, Sources and English section included, TeX tokens counted) gives about 7,800. The meta-manager may want a precise count against the 7,500 cap.

## (d) Checked and found correct

**Numbers (all rerun).**
- check.mjs: 15/15 configs OK. Presets and quoted values: tranche 0.370% / 5.185% (14.0×) / 10.000% (27.0×); p = 0.02: 2.000% vs 0.0032% (634.5×); counting 63 (0.0063), 1,023 (0.102), 16,383 (fraction 1), two days k = 20: 1.05e-10; Ashby 9.29 / 2.64 / 4.29, and 0.00 at V_R = 14; N_eff 10 / 2.703 / 1.099 / 1, N = 100: 3.257, N = 2, ρ = 0.5: 1.333; Bayes 0.5 / 0.8 / 0.941 / 0.985 / 0.996, n = 10: 1,048,576 and 0.999999; cascade: every single seed 1/6, every X pair 2/6, X1+X2+X3 6/6 in 3 rounds, ×1.5 3/6, ×1.2 5/6, ×1.25 3/6; lgd 1: Y1 alone 3/6, every X pair 5/6, all three X 6/6, other single seeds 1/6; herding m = 0.2: 0.04 / −1.00 / 0.000, m = 0.66 still decays (final 0.230), m = 0.67 2.68 / −2.70, breaker 3: ±3.00.
- Python: (8 + 6 × 4)/16 = 2; 2¹⁰⁰ = 1.268e30; C(100,10) = 17,310,309,456,440; 4·0.1³·0.9 = 0.0036, 0.1⁴ = 0.0001; log₂10⁴ = 13.29, log₂100 = 6.64; 63/10⁴ = 0.63%, 1,023/10⁴ = 10.2%; Ashby table minimum = 2 outcomes over all 16 plans; H = 1.75, bound 0.75; N_eff derivation and the N = 2 check (0.75σ²); hand steps −0.9, −0.51, −0.189 and −2.30, −3.94; push/pull factors 0.3/0.4 and 1.35/0.05; root sizes 0.548 / 1.002 / 1.162, complex at m = 0.2, 0.67, 0.9; tipping 2/3; tree of majorities 4 flips for 9 inputs (all 512 inputs); Granovetter 100 → 1; cascade hand table (12/10, 4+8 = 12 ≥ 9, 4+8 = 12 ≥ 11; ×1.5: 12 < 15).
- Notebooks: ex1 (10.061, 2.712, 1.099, 1.000), ex2 (1, 2, 6, 3), ex3 (0.548, 1.002, 1.162; first m above 1 is 0.67) run and match the text and numbers.md.
- Playground answers (1)-(3) and Exercise 4 solution are correct.

**Harari (audio re-transcribed this round).**
- BIS [5:13-5:28] "first tool that we created that can actually understand finance better than us … It's only data. It's only information."
- BIS [16:21] "first tool in history that can make decisions by itself and can create new ideas by itself" (preceded by "potentially orders of magnitude more powerful", a separate sentence).
- BIS [12:42] "humans are extremely adaptable"; [20:46] "History is never deterministic"; [21:37] institutions ("the only thing that can really protect us"); [23:03] "we'll need to keep humans in the loop"; [23:17] "money is really trust"; [25:16] "it is already very creative", AlphaGo [25:57].
- WEF [2:47] knife line; [5:51]-[6:10] "anything made of words … If laws are made of words …"; [8:08] "at least for now, we have zero evidence that AIs can feel anything"; [16:28] (see M1); [30:55]-[31:19] "At the present moment we still think better … We need to prepare for the moment … when AIs create a new financial system that they understand and we don't understand"; [31:55]-[32:14] paraphrase is fair.
- From round 1 and the brief, re-read in the transcripts: BIS [3:00], [3:30], [7:18], [8:59]-[9:28], [9:54], [10:08], [10:19], [10:27], [30:24]; WEF [5:20], [10:36], [11:39], [19:11].
- Guardian 2023: "ideal field for AI because it's only data"; "It could, indirectly, if it triggers certain kinds of wars or conflicts. It's a catastrophic risk … by itself I wouldn't describe it as existential."
- Ynet: "What gives money value is the stories …" and the question about AI "better than the average human at telling stories".
- g4 answer "Partly" is correct.

**Home field and LLM section.**
- FCIC p. 128 waterfall (image), p. 149 "two key mistakes", p. 28 "almost no one understood" (round-1 image checks); KKST abstract quote, 6 May 2010, "about 36 minutes"; N&K Part I circuit-breaker sentence.
- Luo et al. abstract ("translating natural-language trading intents into correct option strategies remains challenging"; "validated and executed deterministically by an engine"); RANGE line labelled ours; Mik abstract ("contractual deepfakes"; "may turn out to be contracts in form only, not in function").
- Cointelegraph: July 11 donation "to the bot's wallet", $122 million; Decrypt: "semi-autonomous AI agent", "more than $214 million", "neither the bot nor its handler created the token"; the bot endorsed after the token launched.
- FSB p. 1 correlation quote and "not widely observed at present"; pp. 28-29 "could change this in the future"; p. 20 four possible drivers incl. herding and lack of transparency; p. 21 "as if it were a single institution"; press release "address many … more work may be needed".
- MIT Sloan "highly correlated predictions that proceed in lockstep" and "can easily mask who's at fault" (secondary, dated 2023).
- Scheurer abstract "consistently hides the genuine reasons", "existence proof" (p. 1), "nearly (but not exactly) 0%" (p. 8) as a number (see n3 for its referent).
- Dütting p. 3; Buehler abstract.

**Lenses.**
- Shannon p. 1; Cover and Thomas pp. 150, 151, 163.
- Arora WP: p. 2 lemon example, pp. 3-4 hardness and "computer scientists believe to be intractable", p. 5 Δ(n) and "position", p. 6 Table 1 reading, p. 12 tree of majorities, "probably correct", "clearly only a first step"; abstract "amplify the costs …"; p. 1 "may be computationally intractable". Akerlof "bad cars tend to drive out the good" (pp. 489-490).
- Ashby pp. 207, 208 (misprint trap), 209, 246, 247.
- Danielsson et al. 2022 p. 7; D&U abstract proposal and introduction "can both stabilise and destabilise"; N&K "control is primarily in the hands of people and organizations", "median outcome".
- Keynes § IV and § V verbatim (library text); Granovetter pp. 1424-1425.
- SEP § 4.2.3 (stones, Bureau of Engraving and Printing, deontic powers, "X counts as Y in C"), § 5.6 (Menger, non-intentional emergence); Lupia Theorem 5.1 (pp. 85-86) and the principal-agent instance, which matches it cell by cell; p. 207 n. 2.

**Audio script.** Every chapter compared with the page. Numbers match ("six hundred thirty-four", "seventeen trillion" for 1.73e13, "three point three" for 3.257 and for 1/0.3). Audio-specific issues are only those listed under M1, M2, M3, n1, n3, n4, n5, n9, n11. The playground chapter gives no answers.

**english-gloss.json.** Definitions and register labels checked; no factual claims beyond the post's own (the "provided that" example matches the corrected page).
