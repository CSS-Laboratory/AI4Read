---
id: 2026-10-ai-finance/review/verify-1
stage: S5, round 1 (independent fact-check of the draft)
checked: 2026-10-17
draft: src/content.html (all visible text, 14 widget configs, captions), audio-script.md, english-gloss.json (factual claims only)
not read: self-review.md (independence)
method: Every cited sentence was checked at the source page, section or timestamp, not just against the brief. Sources: sources/*.txt and *.pdf; FCIC pp. 28, 128 and 149 and Dennett p. 24 read from rendered page images; Arora p. 12 read from a rendered image; Ashby, Cover and Thomas, Akerlof, Granovetter, Lupia, Keynes and SEP from the library or saved copies. Audio: BIS [10:00–10:40], [16:14–16:32], [21:33–22:10], [22:50–23:17] and WEF [2:45–2:59], [7:45–8:12], [11:36–11:52], [26:18–26:40] re-transcribed with faster-whisper small.en (int8; WAV cut with ffmpeg, read with `wave`). Both base.en transcripts were read in full for the balance check. Numbers: check.mjs on content.html (defaults and every preset/claimed value via --id/--values/--seeds), the three notebooks, and scratchpad nums.py.
---

# S5 fact-check, round 1: post 02

Severity follows rubric §A. Quotes from sources are at most 25 words. "Section" = the `id` of the post section.

## Major findings (7)

**M1. Danielsson et al.: dropped hedge, and the published version says something different** — section `lens-control` (lever 2); also audio `lens-control`
- Post: "An earlier paper warns that eventually “neither its understanding of the economic system, nor possibly even its internal data representations, will be intelligible to its human operators” [Danielsson et al. 2017, p. 11]."
- Source: SRC SP13 (2017), p. 11: "Eventually, we might come to the point where neither its understanding of the economic system, nor possibly even its internal data representations, will be intelligible". The hedge "we might come to the point where" is gone (s2 "must not use" item 7). The published paper, *J. Banking & Finance* 140 (2022) 106290, §5.2, p. 7, says: "The AI's knowledge of the financial system and internal data representations will likely be unintelligible to humans." (pp. 2 and 8, about leaving "a macro AI in charge": "will become unintelligible to humans".)
- Severity: **major** (dropped hedge on a quoted claim; cites the working paper when the published text exists).
- Fix: Quote and cite the published version, keeping its hedge: "the AI's knowledge … 'will likely be unintelligible to humans'" (Danielsson, Macrae and Uthemann 2022, *JBF* 140, 106290, p. 7, doi:10.1016/j.jbankfin.2021.106290). In the audio, say "will likely be unintelligible to humans", not "may not be intelligible". Update brief E1 and the source list entry (see m19).

**M2. FSB: two separate statements merged, so "this" points to the wrong thing** — section `answer` ("Critics, one line each"); audio `answer`
- Post: "FSB: existing frameworks cover much, but AI “could change this in the future”." Audio: "The FSB says AI could change this in the future."
- Source: FSB 2024, pp. 28–29: "Although use cases generating new revenue streams are not widely observed at present, the rapid pace of technological advancements … could change this in the future." Here "this" means that new-revenue use cases are rare. The "frameworks" sentence is a separate statement (p. 2 and the press release), and its own hedge is "more work may be needed".
- Severity: **major** (merges separate statements; "this" now seems to say that AI could overturn the frameworks).
- Fix: "FSB: frameworks address many vulnerabilities, but 'more work may be needed'; new-revenue uses are 'not widely observed at present', though advances 'could change this'." Make the same change in the audio.

**M3. Keynes: two passages joined by a "since" that Keynes does not write** — section `lens-decision` ("Why would banks use the same model?")
- Post: "Keynes: human investors “fall back on what is, in truth, a convention” [§ IV], since “it is better for reputation to fail conventionally than to succeed unconventionally” [§ V]."
- Source: § IV gives the convention as how daily revaluations "are … carried out in practice", resting on assuming "the existing state of affairs will continue indefinitely". The reputation line (§ V) is about the long-term investor who goes against "average opinion".
- Severity: **major** (house rule: merging separate statements; it gives Keynes a reason he does not give for the convention).
- Fix: "Keynes: investors 'fall back on … a convention' (§ IV); and, of professionals, 'it is better for reputation to fail conventionally …' (§ V)." Drop "since". The audio wording ("because it is better for reputation") needs the same fix.

**M4. Balance: Harari's one unhedged line about AI inventing money is left out** — section `home` ("What Harari said, exactly"), and `answer`
- Post: The "His assertion, without hedges" paragraph gives only the words thesis. Every finance line is presented under "His finance scenarios, with hedges".
- Source: WEF 2026 [2:45–2:59] (audio re-checked): "AI is a knife that can invent new kinds of knives as well as new kinds of music, medicine and money." The talk presents it as one of three things "to know about AI", without "imagine" or "maybe".
- Severity: **major** (balance rule: a central unhedged claim on the post's own question, "can AI invent a new kind of finance", is omitted, so Harari looks more cautious on finance than he is).
- Fix: Add one sentence to "His assertion": "He also states, as a fact to know about AI: 'AI is a knife that can invent new kinds of … money' [2:47] (a claim about what AI can do, with no date)." Mention it in prediction 4's answer and in the synthesis key point.

**M5. Balance: his unhedged present-tense finance assertions are missing, and "his finance scenarios are conditionals" overstates the hedging** — section `home` ("His finance scenarios, with hedges"; "Our reading (ours)"; the parenthesis "He calls AI 'a tool' at the BIS [5:13]"), `answer` key point; audio `home`, `answer`
- Post: BIS [5:13] is used only for the word "tool". "Our reading (ours). His finance scenarios are conditionals; his thesis about words is an assertion."
- Source: BIS [5:14–5:28]: "AI is the first tool that we created that can actually understand finance better than us … It's only data". BIS [16:14–16:30] (re-checked): AI "is the first tool in history that can make decisions by itself and can create new ideas by itself." Guardian 2023: finance is "the ideal field for AI because it's only data".
- Severity: **major** (balance rule: these are unhedged assertions about AI and finance now, not scenarios. Leaving them out lets the post class all his finance statements as hedged conditionals).
- Fix: Add: "He also asserts, in the present tense, that AI 'can actually understand finance better than us' because 'it's only data' [5:14]." Change "Our reading" (and the synthesis) to: "His forecasts about AI-made devices are conditionals; his claims that AI already understands finance better than us and that anything made of words will be taken over are assertions."

**M6. Truth Terminal: a factual claim about money and liability that the sources contradict or do not make** — section `lens-social`, diagram `dg-status`, step 4
- Post: "In the one case we checked, Truth Terminal, the money and liability ran to people."
- Source: Cointelegraph: Andreessen "sent $50,000 worth of Bitcoin (BTC) to the bot's wallet". Neither Cointelegraph nor Decrypt says anything about liability. (Cointelegraph does support humans in the loop: the handler approves "its X posts".)
- Severity: **major** (presented as what we found in a real case. The money half is contradicted and the liability half is unsupported. The Lens 4 "liability stays with people" signal leans on it.)
- Fix: "In Truth Terminal's case, a donor sent Bitcoin to the bot's wallet, a human approved its posts, and the reports say nothing about who would be liable. Whether an AI could be the liable party is a legal question we do not answer." Correct brief F5 "Instance" too (WRITING §9).

**M7. Ashby's entropy bound is derived without the condition it needs** — section `ladder`, Rung 2
- Post: "H(E) ≥ H(D) + H(R|D) − H(R). The step: H(E) ≥ H(E|R) (conditioning cannot raise entropy), then expand."
- Source: Ashby 1956, S.11/8, p. 207: "The condition introduced in S.11/5 (that no element shall occur twice in a column) here corresponds to … H_R(E) ≥ H_R(D)". This step is needed before "conditioning cannot raise entropy".
- Severity: **major** (dropped condition the reader needs: without it the bound is false. For example, if every cell gives the same outcome, H(E) = 0 while the right side can be 2).
- Fix: "Two steps. The table rule 'no outcome twice in a column' gives H(E|R) ≥ H(D|R). Then H(D) + H(R|D) = H(R) + H(D|R) ≤ H(R) + H(E|R) ≤ H(R) + H(E)."

## Minor findings (21)

**m1. CDOs are not "pools of loans"** — `home` ("2008: complexity…"); audio `home`. Post: "CDOs … pools of loans sliced into tranches … [FCIC 2011, p. 128]". FCIC p. 128 (image): CDOs "purchase and pool financial assets such as the riskier tranches of various mortgage-backed securities". Fix: "pools of debt securities (in 2008, mostly tranches of mortgage-backed securities), sliced into tranches"; keep the toy's "loans" as ours.

**m2. $214 million is cited to the wrong outlet** — `llm`, item 2. Post: "valued in reports at about $122 million to over $214 million [Cointelegraph 2024]". Cointelegraph gives $150 million (peak) and $122 million; "more than $214 million, according to CoinGecko" is Decrypt. Fix: cite "Cointelegraph 2024; Decrypt 2024".

**m3. Lopez-Lira and Tang: wrong page, and the 90% is not a strategy figure** — `llm`, item 3. Post: "GPT-4 headline strategy had about 90% hit rates for the direction of the first price reaction … [Lopez-Lira and Tang 2025, p. 6]". Source p. 1: "approximately 90% portfolio-day hit rates for the non-tradable initial reaction" (also pp. 2–3). The Sharpe ratios are on p. 6 and belong to "the ChatGPT-based strategy". Fix: "GPT-4 scores matched the direction of the non-tradable initial reaction about 90% of the time (pp. 1–3); the tradable strategy's Sharpe ratio fell … (p. 6)."

**m4. Timestamps** — `home`. "a couple of years" is at [10:19], not [10:27] (re-checked). "at the present moment, we still think better" is at [30:55], not [32:00]. "If laws are made of words…" (`lens-social`) is at [6:06], not [5:57]. Fix: give the timestamps for each quote ([10:19]; [30:55]–[32:00]; [6:06]).

**m5. "Three different 'ten years'" undercounts** — `home` trap. In the WEF talk Harari also says "10 years from now, living in a world in which AIs are in command of language" [24:13], and of his own writing: "AI will beat me … Two years, five years, 10 years. It will beat me" [26:29–26:35] (re-checked). The second is an unhedged forecast with a timeframe that belongs to the words thesis. Fix: "at least three"; add [26:33] to "His assertion" as the words thesis with his own timeframe.

**m6. Balance: Harari's own limit on the words thesis is left out** — `home`, `lens-social` (test and steelman). WEF [8:05–8:12]: "While AIs become better than us with words, at least for now, we have zero evidence that AIs can feel anything". [11:36–11:52]: humans' place "depends on … our non-verbal feelings and our ability to embody wisdom that cannot be expressed in words" (re-checked). Fix: one sentence in the Lens 4 test: "Harari himself limits the thesis to what is made of words and locates the human role in non-verbal feeling [8:05], [11:42]; our supports (acceptance, enforcement) are a different limit."

**m7. Balance: Harari's own remedies are presented only as his critics' counterpoint** — `answer` ("Skingsley: we already trust…"), `lens-control`. BIS [21:37–22:06] (re-checked): "The solutions that we again and again see in history is institutions … the only thing that can really protect us". [22:57–23:04]: "we'll need to keep humans in the loop"; [12:42]: "humans are extremely adaptable". Fix: add one line in `home` or `answer`: "His own remedy is institutions and 'humans in the loop' [21:37], [23:00]; Skingsley agrees on institutions."

**m8. The chain "money is words, so AI takes over money" is ours, not his** — `lens-social` ("Testing Harari's chain"). Harari's Ynet essay poses the step as a question: "What would happen once a non-human intelligence becomes better than the average human at telling stories…". He never says "AI takes over money" in our sources. Fix: "Our compression of his two assertions (his essay asks it as a question): money is stories, so AI …".

**m9. Ashby's "only hope": the audio keeps only half the condition** — audio `lens-control`. The audio says: "Ashby says that when capacity cannot be raised, a constraint is the regulator's only hope." Ashby p. 247: "if R's capacity is not easily increased and the other methods are not possible" (s2 item 8). Fix: "when capacity cannot easily be raised and no other method works".

**m10. Our framing attributed to Poole** — `answer` ("Critics"); audio `answer`. "Poole: the invention step is the weak link." Poole: "No one has yet seen a chatbot create new ideas, as Harari thinks they can". Poole says nothing about finance or a "step". Fix: "Poole: 'no one has yet seen a chatbot create new ideas' (so invention is the weak link, our reading)."

**m11. Narayanan and Kapoor's hedge dropped** — `answer` ("Critics"). "impacts will be slow and control stays with people". Source: "Of course, we cannot be certain of our predictions, but we aim to describe what we view as the median outcome." Fix: add "(their 'median outcome', not a certainty)".

**m12. Conditional 5 adds a condition no source states** — `answer` ("Five conditionals"); audio `answer`. "If a community accepts … and the law makes a human liable, money's status survives; if either fails, it does not." SEP § 4.2.3 (Searle) makes collective acceptance the condition; no source makes human liability necessary for money's status. Fix: label it "ours", and drop "if either fails, it does not" or limit it to acceptance.

**m13. Conditional 4 overstates Lupia and McCubbins** — `answer`. "If verification and penalties exist, delegation can work without understanding (Lupia); if not, it fails." Theorem 5.1 (pp. 85–86): with one condition met, "the worst that can happen … is the retention of the status quo". The incentive condition can also be met by "common interests". Fix: "…; if neither knowledge nor incentive holds, it fails."

**m14. Layer 3 hides the regulators' "could"** — `answer` ("Four layers"). "A shared model correlates failures. Supported by toys and regulators' reports". FSB p. 1: common models "could lead to increased correlations". The reports warn; they do not measure. Fix: "Shown in toys; flagged as a risk ('could') by regulators; not measured for LLMs."

**m15. Rung 1: definition page and "the hard part"** — `ladder`, Rung 1 (and the `lens-info` Ladder 2 toy). Δ(n) is defined on Arora p. 5, which is not cited. "The minimum runs over C(100,10) sets: that search is the hard part." In the plain pool every 10-set gives 45, so the minimum is trivial. In Arora, the hardness is finding a planted dense subgraph in CDO wiring, under a conjecture, not the size of the subset count. Fix: cite p. 5; write "with a derivative on top, the seller chooses where the junk goes, and finding that placement is the hard part, under the conjecture (a large count alone proves nothing)".

**m16. Our reading not labelled** — `home` (2010). "The lesson is speed and feedback, not opacity". Neither KKST nor N&K says this. Fix: add "(ours)".

**m17. "It fails" should be "it says nothing"** — `recall` card 2; audio `lens-info` ("the squeeze fails"). When 2^k − 1 exceeds the number of contracts, the bound is still true but no longer informative. Fix: "It stops ruling anything out once 2^k − 1 exceeds the number of contracts."

**m18. Widget readout at ρ = 0** — `lens-decision`, `lab-neff`. At ρ = 0 (the "independent" preset) the readout says "N_eff never exceeds 1/rho = 100.00". That 100 comes from the clamp max(ρ, 0.01); the true ceiling is infinite. Fix: show the ceiling sentence only when ρ > 0 (or say "no ceiling when rho = 0").

**m19. Source list** — `sources`. "Danielsson, Macrae & Uthemann (2017). AI and systemic risk. LSE SRC Paper 13." SP13's title is "Artificial intelligence, financial risk management and systemic risk"; "Artificial intelligence and systemic risk" is the 2022 *JBF* title. More generally, the entries carry no URL or DOI (charter §9; WRITING §3). Fix: "Danielsson, J., Macrae, R. & Uthemann, A. (2022). Artificial intelligence and systemic risk. *J. Banking & Finance* 140, 106290. doi:10.1016/j.jbankfin.2021.106290", and add a URL or DOI to every entry (MANIFEST has them).

**m20. Balance: the authors' own concessions are left out** — `lens-info` (Arora) and `lens-control` (Danielsson and Uthemann). Arora p. 12: blaming "faulty models" in pricing "is probably correct". Danielsson and Uthemann (intro): AI "can both stabilise and destabilise the financial system". Fix: add one clause each to "What it does not say" and to the counterweights.

**m21. Small strengthenings in summaries and example sentences** — `answer`: "Skingsley: we already trust what we cannot understand". She says "very vague understanding" [7:18]. Fix: "we already trust what we only vaguely understand." `english`/gloss: "Diversification works *provided that* errors are independent". By the post's own N_eff formula it works partly whenever ρ < 1. Fix: "works best provided that errors are independent."

## Counts
- **Critical: 0**
- **Major: 7** (M1 dropped hedge; M2 and M3 merged statements; M4 and M5 balance; M6 unsupported case claim; M7 dropped condition)
- **Minor: 21**

S2 "must not use" list, checked item by item: item 7 is violated (M1). Item 8 is half kept in the audio (m9). Items 1–6 and 9–19 are respected.

## Checked and found correct
**Numbers (all rerun).**
- check.mjs on content.html: 14/14 configs OK.
- Every preset and claimed value reproduces:
  - tranche 0.370% / 5.185% / 10.000% (27.0×); p = 0.02: 2.000% vs 0.0032% (634.5×);
  - 10⁴ contracts and 13.29 bits; 63, 1,023 and 16,383; two days, k = 20: 1.05×10⁻¹⁰;
  - Ashby 9.29 / 2.64 / 4.29, with the bound stopping at 0;
  - N_eff 10 / 2.703 / 1.099 / 1 and 3.257; N = 2, ρ = 0.5: 1.333;
  - Bayes 0.5, 0.8, 0.941, 0.985, 0.996; odds 1,048,576 and 0.999999;
  - W5: every single seed 1/6; every X pair 2/6; X1+X2+X3 6/6 in 3 rounds; capital ×1.5 3/6; κ = 1.2 5/6 and κ = 1.25 3/6; lgd 1: Y1 alone 3/6, X pairs 5/6. The playground answers are right.
  - Herding: m = 0.2 gives 0.04 / −1.00 / 0.000; m = 0.67 2.68 / −2.70; m = 0.9 1345.97; breaker ±3.00; m = 0.66 still decays.
- Python:
  - 2¹⁰⁰ = 1.268×10³⁰; C(100,10) = 17,310,309,456,440; lemon cost 50 − 45 = 5;
  - hand steps −0.9, −0.51, −0.189 and −2.30, −3.94;
  - root sizes 0.548 / 1.002 / 1.162; the roots are complex at m = 0.2, 0.67, 2/3 and 0.9; tipping at 2/3;
  - H = 1.75 and H(E) ≥ 0.75; log₂ 100 = 6.64;
  - Ashby table minimum is 2 outcomes over all 16 plans; tree of majorities: 4 flips for 9 inputs by brute force, then 8 and 16;
  - Contract A cell counts 1/6/9.
- Notebooks: ex1 (N_eff ≈ 10.06, 2.71, 1.099, 1.000), ex2 (1, 2, 6, 3 failures) and ex3 (0.548, 1.002, 1.162; first m above 1 is 0.67) all run and match the text. All match numbers.md.

**Harari, audio and wording.**
- BIS [3:00] "maybe 1% …"; [9:54] device quote; [10:08] "trillions of data points"; [10:27] "nobody knows why"; [30:24] "new types of financial devices…"; [3:30] "power shifting…"; [9:12] "your example with the airplane is perfect" (so "accepted … in part, then turned to" is fair).
- WEF [2:01] tool/agent; [5:10] autocomplete; [5:48] "putting words in order"; [5:57] and [10:36] "made of words"; [16:28] bank account; [19:11] "too late"; [31:54] "ten years from now, Davos"; the paraphrase of [32:00], with the low-confidence last word handled correctly.
- Skingsley [7:18], with no "at least".
- Guardian 2023 "catastrophic … by itself … existential"; Ynet "What gives money value…".
- The g4 answer "Partly" is correct.

**Home field.**
- FCIC p. 28 "the securities almost no one understood … first dominoes" (image).
- FCIC p. 149 "two key mistakes", "weren't that different to begin with", "two to three times higher" (image).
- KKST abstract quote; "about 36 minutes" (p. 1).
- N&K Part I "led to new curbs on trading, such as circuit breakers".

**LLM section.**
- OQL (first author Haochen Luo) abstract wording; Mik abstract "may turn out to be contracts in form only, not in function".
- Decrypt "semi-autonomous AI agent", "$50,000 worth of Bitcoin"; both outlets say the bot did not create GOAT.
- FSB p. 1 correlation quote and "not widely observed at present" (pdf 5); pp. 28–29 continuation (pdf 32–33).
- MIT Sloan "lockstep" quote, labelled secondary and dated 2023.
- Lopez-Lira and Tang p. 6: Sharpe 6.54 → 1.22, "some suggestive evidence".
- Scheurer p. 1: "consistently hides", "existence proof"; p. 8: "nearly (but not exactly) 0%", "remains high under all prompts".
- Dütting p. 3 "approximately incentive compatible"; Buehler abstract.

**Lens 1.**
- Shannon p. 1, both phrases.
- Cover and Thomas, 1st ed.: Thm 7.2.4 and "each program can produce only one possible output sequence" (p. 150); computer dependence (p. 151); not computable (p. 163).
- Arora:
  - abstract "amplify the costs of asymmetric information instead of reducing them";
  - p. 1 "may be computationally intractable";
  - p. 2: $1,000 / $800 / $200;
  - p. 6 Table 1 as described;
  - p. 12 "clearly only a first step" and "cannot be influenced by o(2^k)" (image).
- Akerlof p. 489 "The 'bad' cars tend to drive out the good".

**Lens 2.**
- Ashby p. 207 "only variety in R can force down … variety can destroy variety"; p. 209 "owes nothing to experiment"; p. 246 "ways that may make regulation possible" and "somewhat trivial"; p. 247 "only hope" with its full condition in the text.
- The H_D(E) misprint trap matches the reprint (p. 208 text layer).
- Danielsson and Uthemann abstract proposals and "cannot effectively prevent and resolve" (intro).
- FSB press release "address many … more work may be needed".

**Lens 3.**
- Keynes § IV and § V wording (each quote verbatim).
- FSB p. 20: four drivers; FSB p. 21: "as if it were a single institution".
- Granovetter pp. 1424–1425: threshold swap and "the two crowds are essentially identical".

**Lens 4.**
- SEP § 4.2.3: stones and Bureau of Engraving examples, deontic powers, "X counts as Y in C"; SEP § 5.6: Menger and the acceptance debate.
- Lupia and McCubbins Theorem 5.1 (pp. 85–86) and p. 207 "verification or a penalty for lying".
- Dennett p. 24 "free … perfectly objective" (page image).
- Scheurer abstract "consistently hides the genuine reasons"; MIT Sloan "can easily mask who's at fault".
- WEF [16:28] and [19:11].

**Critics and sources.**
- Poole "No one has yet seen a chatbot create new ideas"; Fox "capitalism is hardly mentioned at all".
- Source list dates, authors and versions, apart from m19.

**Audio script.** Every chapter was compared with the page. Its numbers match (634.5 is spoken as "six hundred thirty-four"; 3.257 as "three point three"). The only audio-specific problems are M1, M2, M3, m1, m9, m10 and m17.

**English gloss.** All definitions and example sentences checked; the only factual issue is m21.
