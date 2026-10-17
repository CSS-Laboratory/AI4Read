---
id: 2026-10-ai-finance/review/verify-2b
stage: S5, round 2 (independent fact-check, checker B)
checked: 2026-10-17
scope: src/content.html (all visible text, fold-outs, 15 widget configs, captions, exercise answers, Sources list), audio-script.md, english-gloss.json and the page's English example sentences, post.json summary
not read: self-review.md, critic files, review/verify-2.md (independence)
read: review/verify-1.md, verify-1b.md, round1-merged.md, response-1.md; evidence source-brief.verified.md, s2-check.md
method: Every cited sentence was opened in the source. Audio re-transcribed with faster-whisper small.en (WAV cut with ffmpeg -ac 1 -ar 16000, read with `wave`): BIS [2:40-3:35], [5:00-5:45], [8:35-9:35], [9:45-10:40], [12:35-12:55], [16:00-16:25], [20:36-20:50], [21:20-21:40], [22:55-23:25], [23:05-23:25], [24:40-27:20], [29:55-30:40]; WEF [1:50-2:10], [2:35-2:55], [4:45-5:45], [5:55-6:15], [7:55-8:15], [10:30-10:50], [11:35-11:55], [14:50-16:45], [17:30-17:55], [19:00-19:20], [26:25-26:45], [30:50-33:00]. Both full machine transcripts were searched for every finance/money/invent passage (balance check). Text sources: sources/*.txt, FCIC pp. 28, 128, 149 and Arora pp. 11-12 from rendered page images, library copies (Keynes, Granovetter, Lupia, Cover and Thomas, Akerlof), page metadata of the saved web pages. Numbers: check.mjs on content.html (defaults, every preset, every number quoted in prose and in the playground answers), the three notebooks, and Python (scratchpad v2b).
---

# S5 fact-check, round 2, checker B: post 02

Severity: rubric §A. Quotes of sources are at most 25 words. Timestamps: the page uses the base.en transcript times; small.en times differ by up to about 6 s (e.g. [11:39] vs 11:43; [31:11] vs 31:06). I treat that as correct.

## (a) Round-1 fix verification

"FIXED" = the current text (page and audio) matches the source. The writer's claims in response-1.md were checked against the text, not accepted.

### Binding list (round1-merged.md, section A)

| # | Item | Verdict | Evidence in the current text |
|---|---|---|---|
| A1 | Danielsson hedge | FIXED | Lens 2: "will likely be unintelligible to humans" [Danielsson et al. 2022, p. 7]. JBF p. 7 (txt line 488): "will likely be unintelligible to humans". Audio `lens-control` says "will likely be unintelligible". Source entry is the 2022 JBF paper with DOI. |
| A2 | Harari unhedged capability claims | FIXED for the three named lines; PARTLY for the summary (see new M1) | Section 3 "He asserts, without hedges" has BIS [5:14], [16:21], WEF [2:47] (knife line), [5:57], with "asserts". Limits [8:07] and remedies [21:37], [22:57] present. All re-transcribed and correct. But "his forecasts about AI-made devices are conditionals" (section 13 key point, audio `answer`) and the classing of [30:24] and [31:11] as "hedged" remain wrong (new M1). |
| A3 | Truth Terminal "liability ran to people" | FIXED | Gone from text, diagram `dg-status` and audio. New text (donor sent Bitcoin to the bot's wallet; handler approved posts; someone else created the token; reports silent on liability) is right for Cointelegraph and Decrypt. Two small slips remain (m1, m2). |
| A4 | Arora toy | FIXED | Plain pool: every 10-set = 45, "nothing to search". Derivative paragraph: seller chooses where junk goes; detecting it is the "hidden dense subgraph" problem, "computer scientists believe to be intractable" (Arora p. 4); C(100,10) is "huge, but beside the point, since an unbounded buyer could do it" (p. 4: the unbounded buyer "can enumerate over all possible n-sized subsets"). Δ(n) cited to p. 5, Table 1 to p. 6. Diagram step and audio agree. |
| A5 | FSB merge | FIXED | "not widely observed at present" is p. 1 (executive summary, txt line 59); "could change this in the future" is pp. 28-29 (Conclusion, txt lines 1676-1708). The frameworks statement is separate (press release). Page and audio keep them apart. |
| A6 | Keynes "since" | FIXED | "Separately, of professionals, he writes ..." (§ IV, § V). Audio the same. Keynes text checked in the library HTML. |
| A7 | Ashby table condition | FIXED | Condition stated before the bound in Lens 2 and in the fold-out step (1) (p. 207: "no element shall occur twice in a column"). Audio gives the "only hope" condition in full. |
| A8 | Playground answer (2) | FIXED | "At 1.0 two X banks sink five of six, and all three are still needed for six." check.mjs --id cs-w5: lgd 1, every X pair = 5 of 6, X1+X2+X3 = 6 of 6. |

### Critic's structural changes that carry facts (section B)

| Item | Verdict | Note |
|---|---|---|
| Preview and "human-centred" definition | FIXED | Marked ours. |
| Short answer | FIXED (facts) | Marked "our reading, not a finding". One strengthening: "LLMs now translate plain language into fixed contracts" (m11). |
| Chain diagram with evidence labels | PARTLY | Labels are asserted, hedged, not yet evidenced, supported in toys, contested. The "hedged" label on "AI masters words -> AI takes over money and finance" conflicts with the page's own unhedged claims (see M1). |
| Self-contained ladders (N_eff, m = 1/A, "description", principal/agent) | FIXED | Derivations rerun, all correct (see checked list). |
| Vocabulary (HFT, circuit breaker, option, query language, memecoin) | FIXED | Each defined with `dfn`. Sharpe ratio and Lopez-Lira removed (grep: no leftovers in page, audio or numbers.md). |
| Widgets (cs-w5 default seeds, N_eff readout without 1/rho at rho = 0) | FIXED | Default readout 6 of 6; neff readout has no ceiling text. |
| One-line OQL-style contract | FIXED | `RANGE(index, 90, 110)`, labelled ours; "our gloss". |

### Checker A minors (verify-1.md) and checker B minors (verify-1b.md)

| Item | Verdict | Note |
|---|---|---|
| A m1 CDO "pools of loans" | FIXED | "pools of debt, in 2008 mostly slices of mortgage-backed securities". FCIC p. 128: "riskier tranches of various mortgage-backed securities". "mostly" is the writer's gloss; acceptable. |
| A m2 / B 8 $214M outlet | FIXED | $122M cited to Cointelegraph, $214M to Decrypt. (Different dates, see m1.) |
| A m3 Lopez-Lira | FIXED | Removed. |
| A m4 timestamps | FIXED | [10:19], [30:55], [6:06] correct. |
| A m5 "three different ten years" | FIXED, but see new M2 | "at least three"; [26:33] added in the fold-out without its hedge. |
| A m6 / B 6 Harari's limit | FIXED | [8:07], [11:39]. Wording of the second slightly strong (m10). |
| A m7 remedies | FIXED | [21:37], [22:57]. |
| A m8 / B 4 chain is ours | FIXED | "Our compression (ours)"; "money is really trust" [23:15] added (re-transcribed, correct). |
| A m9 / B 15 audio "only hope" | FIXED | Full condition. |
| A m10 Poole | FIXED | "(so invention is the weak link: our reading)". Pairing issue remains (m8). |
| A m11 / B 21 Narayanan and Kapoor | FIXED | "in the world they describe ... 'median outcome', not a certainty". |
| A m12 conditional 5 | FIXED | Marked ours; "if either fails" dropped. |
| A m13 conditional 4 / B 25 Lupia p. 207 | FIXED | "if neither knowledge nor incentive holds, it fails; with one, the worst case is the status quo" (Theorem 5.1, p. 85). |
| A m14 layer 3 | FIXED | "Shown in toys; flagged as a risk ('could') by regulators; not measured for LLMs." |
| A m15 / B M4 Rung 1 and Δ(n) | FIXED | See A4. The old "ladder" section is gone. |
| A m16 / B 17 "simple", "lesson" | FIXED | "(ours)" added, "simple" dropped. |
| A m17 / recall "fails" | FIXED | "It rules nothing out once 2^k - 1 exceeds the number of contracts." Audio the same. |
| A m18 rho = 0 readout | FIXED | Rerun: N_eff = 10.000, no ceiling text. |
| A m19 / B 14 source list | PARTLY | Danielsson et al. 2022 with DOI; URLs/DOIs added. Several entries still lack a title; one date is wrong (m4, m5). |
| A m20 concessions | FIXED, one dropped condition | Arora p. 12 "probably correct" present (image checked). Danielsson and Uthemann "can both stabilise and destabilise" present without its condition (m6). |
| A m21 "vaguely" / "works best provided" | FIXED | Page, recall, audio, English example. |
| B 1 hook | FIXED | "a very big difference", "perfect" [9:01-9:08] re-transcribed. |
| B 2 tool/agent contrast | FIXED | Removed. |
| B 3 bridge to post 01 | FIXED | Labelled "Our bridge"; quote [5:21] correct. |
| B 5 Guardian "indirectly" | FIXED | In the fold-out, full wording. |
| B 7 FSB p. 1 | FIXED | "background, not a test". |
| B 9 RegretNet | PARTLY | Page has "one method 'will generally only find' ... 'approximately incentive compatible'" (correct, "one method"). response-1 says "RegretNet named": it is not named on the page or in the audio. Audio generalises to neural networks (m13). |
| B 10 OQL | FIXED | "(our gloss)", "a candidate strategy". |
| B 11 tree | FIXED | "perhaps", "In their simple model", "much larger than sqrt(3^k)" checked against the page image (printed p. 12: "o(2^k) >> sqrt(3^k)"). |
| B 12 playground | FIXED | See A8. |
| B 13 Ladder 4 criterion | FIXED | "The swing shrinks when Am < 1 and grows when Am > 1"; fold-out: roots complex, size sqrt(c). Rerun: sizes 0.548 / 1.0025 / 1.162; stable iff c < 1 also holds for real roots. |
| B 19 W4/W5 | FIXED | |
| B 22 "best-supported" | FIXED | "most plausible ... our judgment, not a finding". |
| B 23, 24, 26, 27 | FIXED | [6:06]; Dennett removed; "financial devices"; "four possible drivers". |

## (b) New findings (round 2)

### Major (2)

**M1. Balance: Harari's undated, unhedged finance forecasts are classed as "hedged", and the summary says his forecasts are "conditionals"** — section 3 ("He imagines, with hedges"; "Our reading (ours)"), fold-out "All of Harari's lines" (list "Scenarios and hedged statements"), section 13 key point, chain diagram `dg-chain` (link label "hedged", step 2), audio `home` and `answer`.
- Post: "At Davos he says 'we need to prepare' for a financial system AIs understand and we do not [31:11]" under "He imagines, with hedges". Fold-out files "I think we'll see AI creativity also in this field coming up with new types of financial devices" [30:24] under "Scenarios and hedged statements". Key point: "Our reading: his forecasts about AI-made devices are conditionals, his capability claims are assertions." Chain: "AI masters words -> AI takes over money and finance" labelled "hedged".
- Source: BIS [30:20-30:33] (re-transcribed): "So I think we'll see AI creativity also in this field coming up with new types of financial devices that no human being would ever imagine creating." WEF [31:06-31:22]: "we need to prepare for the moment, let's say again take economics or finance, when AIs create a new financial system that they understand and we don't understand." WEF [4:45-5:57]: "Therefore, anything made of words will be taken over by AI."
- What the source says: neither forecast has "imagine", "maybe", "if" or a date. "I think we'll see" and "when AIs create" are predictions about the post's own question (a), more direct than the 10-year scenario ([9:54] "imagine ... maybe in 10 years"). The page's own definition ("a scenario is framed with 'imagine' or 'maybe'") does not cover them. The accurate summary: the 10-year device and "nobody in the room" are framed with "imagine"/"maybe"; his statements that AI will invent new financial devices ([30:24]) and that a moment will come "when AIs create a new financial system" ([31:11]) are undated forecasts with only "I think" or "let's say".
- Severity: **major** (balance rule: a central, nearly unhedged claim on the post's own question is placed under "hedged", and the summary states the opposite of two of its own fold-out entries; Harari looks more cautious than he is). Round 1 M5 flagged the same overstatement; the revision fixed the present-tense claims but kept "forecasts ... are conditionals".
- Fix: add one sentence to the main text: "He also forecasts, without a date and with only 'I think': 'we'll see AI creativity ... in this field coming up with new types of financial devices that no human being would ever imagine creating' [BIS 30:24], and 'when AIs create a new financial system that they understand and we don't' [WEF 31:11]." Move both lines out of "hedged" in the fold-out. Key point (page and audio): "the 10-year device is a scenario; his claims that AI understands finance better than us and will invent new devices are assertions or undated forecasts." Relabel the chain link "partly hedged: dated scenarios hedged, capability and forecasts not".

**M2. Dropped hedge on a quotation filed under "Asserted, no hedge"** — section 3, fold-out "All of Harari's lines", list "Asserted, no hedge".
- Post: "On himself as a writer: 'Two years, five years, ten years, it will beat me' [26:33]".
- Source: WEF [26:29-26:35] (re-transcribed): "and AI will beat me. I don't know how long it will take, two years, five years, ten years, it will beat me."
- What the source says: the outcome ("it will beat me") is unhedged, but the quoted timeframe is introduced by "I don't know how long it will take". The fragment drops that clause and the list heading says "no hedge", so the reader gets a committed two-to-ten-year forecast. Round-1 checker A suggested adding this line (m5) but described it as "an unhedged forecast with a timeframe"; the full sentence does not support that.
- Severity: **major** (house rule: a quoted timeframe stripped of its hedge; balance: the hedge on timing is Harari's own).
- Fix: quote in full: "AI will beat me. I don't know how long it will take, two years, five years, ten years, it will beat me" [26:29-26:35], and label it "outcome asserted; timing explicitly unknown".

### Minor (17)

**m1. Truth Terminal: "Both say neither the bot nor its handler created the token"** — section 4 item 2; audio `llm` ("Both outlets say ..."). Cointelegraph: the bot "was not directly responsible for launching the GOAT token"; "the bot never actually launched the memecoin". It does not say the handler did not. Decrypt: "neither the bot nor its handler created the token"; "Someone else did". Also $122M (Cointelegraph, after a drop from a $150M peak, 14 Oct) and $214M (Decrypt, CoinGecko market cap, 16 Oct) are figures from different days. Fix: "Decrypt says neither the bot nor its handler created the token; Cointelegraph says the bot did not launch it. The two figures are from different days."

**m2. Handler's role cut** — section 4 item 2. Post: "its human handler only approves 'its X posts'". Cointelegraph: "with its human handler only approving its X posts and deciding who it gets to interact with". Fix: add "and decides whom it interacts with".

**m3. Mik quotations located in the abstract** — section 4 item 1, diagram `dg-llm` caption. "contractual deepfakes" and "may turn out to be contracts in form only, not in function" are in the Introduction (txt lines 37-40), not the abstract (arXiv abstract re-fetched: it ends "... or contracts that are enforceable but unsuitable for a given transaction"). Fix: "Mik 2026, introduction".

**m4. Decrypt date** — Sources. "Decrypt (2024, 14 Oct)". Page metadata: datePublished 2024-10-16, "Oct 16, 2024" on the page; the text says GOAT "Launched five days ago" (10 Oct). Cointelegraph's 14 Oct is right. Fix: 16 Oct 2024 (the manifest has the same slip).

**m5. Source list completeness** — Sources, post.json. WRITING §3 asks for full references. No title: Scheurer et al., Luo et al., Dütting et al., Decrypt (headline and author). "AI and financial crises" is a shortening of Danielsson and Uthemann's title ("Artificial intelligence and financial crises"); Mik and Arora titles also shortened. `post.json` `cites` still lists Calvano, Lopez-Lira and Nexus, which the page does not cite. Fix: add titles; prune `cites`.

**m6. Danielsson and Uthemann used as a "counterweight" without their condition** — Lens 2 counterweights. Post: AI "can both stabilise and destabilise the financial system". Source (introduction): "finding that it can both stabilise and destabilise the financial system, depending on the severity of the shocks it faces and how prepared the financial authorities are". The abstract (cited two sentences earlier) says AI "amplifies existing financial system vulnerabilities" and that "crises become faster and more severe". Fix: add "depending on the severity of shocks and how prepared the authorities are", and say the abstract finds amplification.

**m7. Scheurer: the "nearly 0%" is the rate of acting on the tip, not of hiding** — section 4 item 4; audio `llm`. Post: "Prompts that strongly discourage it bring it to 'nearly (but not exactly) 0%'" ("it" follows "hid its genuine reasons"). Source p. 8: strongly discouraging or encouraging prompts lead "to nearly (but not exactly) 0% or 100% rates of misaligned behavior"; the strongest prompt "does not eliminate the misaligned behavior"; "the tendency to deceive, conditional on misalignment, remains high under all prompts". Fix: "Prompts that strongly discourage insider trading bring acting on the tip to nearly (but not exactly) 0%, yet it is not eliminated, and once it acts the hiding stays high."

**m8. Poole is not answering the "understands finance" claim** — section 3 "The evidence"; audio `home`. Post: "We did not test 'AI understands finance better than us'; Poole answers that 'no one has yet seen a chatbot create new ideas'". Poole writes this about Harari's claim that chatbots create new ideas and cultural innovations (Guardian, 11 Sep 2024); he says nothing about finance. Fix: "Poole answers a different claim, that chatbots create new ideas: 'no one has yet seen ...'".

**m9. "Harari's own example of creativity is AlphaGo"** — section 3; fold-out; audio `home`. After Go, Harari adds [27:04-27:10]: "What's true of Go is true of more and more areas in science, in art. AI is now composing music"; and at [30:02-30:33] he calls financial devices "a kind of art" and applies the argument to finance. The fold-out line "not an LLM and not finance" omits that extension. Fix: "his example is AlphaGo; he then says the same holds for science, art and music [27:04] and, by analogy, finance [30:02]."

**m10. "limits the thesis" / "locates the human role" strengthen two Harari lines** — section 3 ("His own limits"), Lens 4 test. [8:05]: "While AIs become better than us with words, at least for now, we have zero evidence that AIs can feel anything" is a statement about feelings; calling it a limit on the words thesis is our reading. [11:43]: "Whether humans will still have a place in that world depends on the place we assign our non-verbal feelings and our ability to embody wisdom that cannot be expressed in words" makes the place conditional on what we assign, not a location of the human role. Fix: "He adds that, at least for now, there is 'zero evidence' that AIs feel; and that humans' place 'depends on the place we assign our non-verbal feelings' (our reading: a limit on the words thesis)."

**m11. [5:57] given as unhedged without its premise** — section 3, prediction 4 answer, audio. WEF [4:45-5:57]: "If thinking really means putting words and other language tokens in order, then AI can already think much better than many, many humans ... Therefore, anything made of words will be taken over by AI." The unconditional form is [10:36] ("Everything made of words will be taken over by AI"), which is in the fold-out only. Fix: cite [10:36] in the main text, or add the "If thinking really means ..." premise.

**m12. Short answer: "LLMs now translate plain language into fixed contracts"** — section 13 short answer; audio `answer`. Luo et al. abstract: translating intents into correct option strategies "remains challenging"; their pipeline "significantly improves execution accuracy" over baselines on their dataset. Section 4 says this correctly. Fix: "a research pipeline improves LLM translation of plain-language intents into option strategies".

**m13. Audio generalises "one method" to neural networks** — audio `llm`: "neural networks that search for auction rules and generally find only approximately incentive-compatible ones". Dütting p. 3: RegretNet "will generally only find mechanisms that are approximately incentive compatible" (a second approach, RochetNet, is for a single bidder). The page says "one method". response-1 claims "RegretNet named"; it is not named anywhere. Fix: audio "one such method generally finds only approximately incentive-compatible rules".

**m14. Fox: "profit is the missing driver (ours)"** — section 13 fold-out. Fox: "it's odd, in a critique of a technology driven largely by profit-seeking corporations, that capitalism is hardly mentioned at all". The "(ours)" blurs who says what. Fix: "Fox notes that in *Nexus* 'capitalism is hardly mentioned at all'."

**m15. Our reasoning stated as fact in Lens 4's intro** — section 9. "A human-centred system (section 1) relies on acceptance, accountability and legal personhood" and "Only this lens shows that the human role at the end of the chain is acceptance and liability" carry no "(ours)"; the Truth Terminal sources are silent on liability. Fix: add "(ours)".

**m16. Section 12: empirical claims about LLM annotation unlabelled** — "Five prompts to one model are closer to one annotator plus noise than to five"; "Agents from one base model are correlated by construction" (and audio `work`). No source; the page has no data on prompts. Fix: "(ours, to test)".

**m17. Keynes: a maxim presented as Keynes's own statement** — Lens 3a. Keynes: "Worldly wisdom teaches that it is better for reputation to fail conventionally than to succeed unconventionally." The post (and audio) say "he writes that 'it is better for reputation ...'". Also "we have tacitly agreed" is "we", the post says "investors". Fix: "he writes that 'worldly wisdom teaches' ...".

### Balance check (explicit)

- Unhedged statements now in the post: BIS [5:14], [16:21], [25:14]; WEF [2:47], [5:57], [10:36]; Guardian 2023 "ideal field". Present and correct.
- Missing or misclassed: BIS [30:24] and WEF [31:11] (M1); the premise and extension in m9 and m11.
- Hedges kept: "maybe in 10 years", "a couple of years", "at least for now", "I think ... maybe 1%", "by itself ... not existential" and the "indirectly, via wars" qualification, "perhaps" and "simple model" for Arora, "likely" for Danielsson. Dropped: M2 ("I don't know how long it will take"), m6 (Danielsson and Uthemann's condition).
- His remedies and limits: present ([21:37], [22:57], [12:42], [20:46], [23:15]); m10 on wording.
- Critics at strength: Poole (m8), Fox (m14), Narayanan and Kapoor (kept with "median outcome"), FSB (separate statements), Skingsley ("very vague").

## (c) Counts

- **Critical: 0**
- **Major: 2** (M1 balance, M2 dropped hedge)
- **Minor: 17**

Round-1 majors (7 from A, 4 from B): all fixed in text and audio; one (A M5 / B M1) fixed only in part and is carried into M1 above.

Top 5: (1) M1 undated finance forecasts classed as hedged; keypoint "conditionals"; (2) M2 "I don't know how long it will take" dropped from a "no hedge" quote; (3) m7 Scheurer "nearly 0%" refers to acting, not hiding; (4) m1 Cointelegraph does not say the handler did not create the token; (5) m3 Mik quotes are in the introduction, not the abstract (with m4, the Decrypt date).

## (d) Checked and found correct

**Numbers (all rerun).**
- check.mjs on content.html: 15/15 configs OK.
- Widgets, every preset and quoted value:
  - tranche 0.370% / 5.185% / 10.000% (14.0x / 27.0x); p = 0.02: 2.000% vs 0.0032% (634.5x);
  - k = 6, 10, 14, 20 (two days): 63 (0.0063), 1,023 (0.102), 16,383 (fraction 1), 1.05e-10; 10^4 contracts, 13.29 bits; 10^16 for two days;
  - Ashby 9.29 / 2.64 / 4.29 / 0.00 and the bound stopping at 0 for V_R = 14;
  - N_eff 10 / 2.703 / 1.099 / 1; N = 100, rho = 0.3: 3.257 (ceiling 3.33); N = 2, rho = 0.5: 1.333, variance 0.75 sigma^2; all-ten-wrong 1e-20;
  - Bayes 0.5, 0.8, 0.941, 0.985, 0.996; n = 10 odds 1,048,576, P = 0.999999;
  - cs-w5: default 6 of 6 in 3 rounds; every single seed 1 of 6 (lgd 0.8); every X pair 2 of 6; kappa 1.5: 3 of 6; kappa 1.2: 5 of 6; kappa 1.25: 3 of 6; lgd 1: Y1 alone 3 of 6, every X pair 5 of 6, X1+X2+X3 6 of 6, other single seeds 1 of 6. All playground answers (1)-(3) correct;
  - herding: m = 0.2: 0.04 up / -1.00 down / 0.000; m = 0.67: 2.68 / -2.70 / -0.505; m = 0.66: decays (0.230); m = 0.9: 1345.97; breaker 3: +/-3.00, final -2.505.
- Python: contract A cell counts 1 / 6 / 9, price 2.0; 2^100 = 1.268e30; C(100,10) = 17,310,309,456,440; plain pool 90 x 1/2 = 45, lemon cost 5; Ashby toy minimum 2 outcomes over all 16 plans; H = 1.75 and bound 0.75; log2 100 = 6.64 and 13.29 - 6.64 = 6.64; tree of majorities 4 flips for 9 inputs (8 and 16 follow 2^k); Granovetter 100 -> 1; hand steps -0.9 / -0.51 / -0.189 and -2.30 / -3.94; root sizes 0.548 / 1.0025 / 1.162, roots complex at m = 0.2, 0.67, 2/3, 0.9; b = 0.9 / 1.84 / 2.3, c = 0.3 / 1.005 / 1.35.
- Notebooks ex1 (N_eff 10.06, 2.71, 1.099, 1.000), ex2 (1, 2, 6, 3 failures), ex3 (0.548, 1.002, 1.162; first m > 1 root size 0.67): run and match the text and numbers.md.
- N_eff, Bayes and Ladder 4 derivations checked line by line (variance of the mean, odds form, characteristic equation, Jury condition c < 1).

**Audio (re-transcribed) and Harari wording.**
- BIS: [3:00] "maybe 1%"; [3:30] "power shifting from humans to algorithms"; [5:14] and [5:27-5:28]; [9:01-9:08] "a very big difference", "perfect"; [9:54] device quote; [10:08] "trillions of data points"; [10:19] "a couple of years"; [10:27] "nobody knows why"; [12:42]; [16:21]; [20:46]; [21:37] and [22:57] (institutions, "humans in the loop"); [23:15] "money is really trust"; [25:14] "already very creative", Go.
- WEF: [2:47] knife line (preceded by "very creative agent" [2:43]); [5:20] "is that so different"; [5:57] and [10:36]; [6:06] laws; [8:07]; [11:43]; [16:28] and [14:56-15:19] "In many countries, corporations are considered legal persons"; [19:09]; [30:55]; [31:11]; [31:54-32:06] "Maybe nobody in the room".
- Guardian 2023 ("ideal field", "catastrophic", "by itself ... existential", "indirectly"); Ynet "What gives money value ..." and "better than the average human at telling stories"; Poole and Fox quotes verbatim.

**Home field and LLM section.**
- FCIC p. 28 "the securities almost no one understood ... first dominoes"; p. 128 definition and "waterfall"; p. 149 "two key mistakes", "weren't that different to begin with" (all from page images).
- KKST abstract quote and "about 36 minutes"; Narayanan and Kapoor circuit-breaker sentence; "median outcome"; "control is primarily in the hands of people and organizations".
- Decrypt "semi-autonomous AI agent", $50,000, July, $214M; Cointelegraph "$50,000 worth of Bitcoin ... to the bot's wallet", $122M.
- FSB p. 1 (correlation; "not widely observed at present"), p. 20 (four possible drivers), p. 21 ("as if it were a single institution"), pp. 28-29 ("could change this in the future"), press-release quotes.
- MIT Sloan "lockstep" and "mask who's at fault" (secondary, labelled); Scheurer "consistently hides", "existence proof", p. 8 quotes (apart from m7); Luo abstract; Mik quote text (apart from m3); Dütting p. 3 quote; Buehler abstract.

**Lenses.**
- Shannon p. 1 two phrases; Cover and Thomas Theorem 7.2.4 and "only one possible output sequence" (first-edition text in the library); Akerlof "bad cars ... drive out the good" (p. 489).
- Arora: abstract quote; p. 1 "may be computationally intractable"; p. 2 $1,000 / 20% / $800 / $200; pp. 3-4 illustrative example, "hidden dense subgraph ... believe to be intractable", enumeration by an unbounded buyer; p. 5 Δ(n); p. 6 Table 1 reading; p. 12 tree of majorities and "clearly only a first step", "probably correct" (page image).
- Ashby: p. 207 "only variety in R ... variety can destroy variety", table condition, H_R(E) >= H_R(D); p. 208 misprint trap; p. 209 "owes nothing to experiment"; p. 246 "ways that may make regulation possible", "somewhat trivial"; p. 247 "only hope" with its condition.
- Danielsson et al. 2022 p. 7 "will likely be unintelligible to humans"; Danielsson and Uthemann abstract proposals.
- Keynes § IV and § V wording (library HTML; section numbers taken from s2); Granovetter pp. 1424-1425; SEP § 4.2.3 and § 5.6; Lupia and McCubbins Theorem 5.1 (pp. 85-86) and p. 207 footnote.

**Cross-references and bookkeeping.**
- Post 01: village words and probabilities, H = 1.75, octopus, Bayes table 0.50 / 0.80 / 0.941 / 0.985 / 0.996, and the three returning idioms are all present.
- Audio script: all chapters match page sections; every spoken number matches (634 spoken as "six hundred thirty-four", 3.257 as "three point three"); quotes match apart from m1, m7, m8, m9, m13, m17 and the M1/M2 carry-overs; recaps add no claims. No MP3 exists yet (audio/chapters.json absent), so the "AI4Read from CSS Lab" tags could not be checked; the spoken intro is in `hook`.
- english-gloss.json: definitions and wrong/right pairs contain no factual claims; the page's example sentences are consistent with the post.
- Length (for the gate, not a fact issue): about 7,240 visible words outside the fold-outs (about 6,440 excluding Sources and English), 1,350 in fold-outs.
- Round-2 writer claims confirmed true: no Lopez-Lira, Sharpe, Dennett, W4/W5 or "liability ran to people" left; section 11 heading matches four exercises; Exercise 4 has hint and solution; each "LLM adds" item links to its lens; cs-w5 seeds X1, X2, X3; chain figure has five labelled links. Claim not true: "RegretNet named" (m13).
