---
id: 2026-10-ai-finance/review/verify-1b
stage: S5 round 1 (independent fact-check, checker B)
checked: 2026-10-17
scope: src/content.html (all visible text, widget configs, captions), audio-script.md, example sentences in english-gloss.json
not read: self-review.md, review/verify-1.md, review/s3-meta-review.md, review/cite-map.tsv (independence)
evidence: source-brief.verified.md (incl. A3b), review/s2-check.md ("must not use" list), the sources themselves (sources/, library copies, page images, audio)
---

# Fact-check, round 1B: post 02

Method. Every cited sentence was opened in the source: PDF text, page images (FCIC pp. 28, 128, 149; Arora pp. 6 and 12; Dennett p. 24), saved web text, or audio. Audio was re-transcribed with faster-whisper small.en for WEF [4:50-6:35], [10:15-10:50], [1:45-2:15] and BIS [8:55-9:35], [29:45-30:40]. I also read both full machine transcripts for the strongest and the hedging statements (balance check). All numbers were rerun: `check.mjs` (14/14 configs OK), the three notebooks, and an independent script (`scratchpad/v1b/nums.py`). Quotes of sources are at most 25 words.

Severity: rubric §A.

## Major findings

### M1. Balance: Harari's unhedged claims on the post's own question are missing
- **Post (#home, "His assertion, without hedges" and "Our reading"; also #answer keypoint and audio chapters `home`, `answer`):** "His finance scenarios are conditionals; his thesis about words is an assertion, and a strong one." The only BIS use of [5:13] is "(He calls AI 'a tool' at the BIS [5:13]...)".
- **Sources:**
  - WEF [2:47], audio re-checked (A3 brief lists it): "AI is a knife that can invent new kinds of knives as well as new kinds of music, medicine and money."
  - BIS [5:14-5:44], and Guardian 2023, para 11: AI is "the first tool that we created that can actually understand finance better than us"; "it's only data". Guardian: "this is the ideal field for AI because it's only data."
  - BIS [25:14-27:04]: "it is already very creative", with AlphaGo (not an LLM, not finance) as his evidence.
- **What the post does:**
  - It prints the "words" thesis (good) and his hedged devices (good).
  - It omits the three unhedged capability claims that answer the post's own title question ("can AI invent?"). The [5:13] timestamp is used only for the word "tool".
  - So his finance position reads as purely conditional. It is not: the *timelines* are conditional ("imagine... maybe in 10 years"), but the capability claims are not.
  - Poole's critique ("no one has yet seen a chatbot create new ideas") is then set against hedged scenarios, not against his actual evidence (AlphaGo).
- **Severity:** major (balance check: a central unhedged claim omitted).
- **Fix:** add 2 sentences to the "assertion" paragraph: the knife line [2:47] and "can actually understand finance better than us ... it's only data" [5:14-5:28], plus "already very creative" with AlphaGo [25:14-26:05]. Change "his finance scenarios are conditionals" to "his finance timelines are conditionals; his capability claims are not."

### M2. Danielsson, Macrae and Uthemann: hedge dropped (on the s2 "must not use" list, item 7)
- **Post (#lens-control, lever 2):** "An earlier paper warns that eventually 'neither its understanding of the economic system, nor possibly even its internal data representations, will be intelligible to its human operators'" [Danielsson et al. 2017, p. 11].
- **Source (SP13, printed p. 11):** "Eventually, we might come to the point where neither its understanding ... nor possibly even its internal data representations, will be intelligible".
- **What the post does:** "warns that eventually" removes "we might come to the point where". The audio keeps "may not be intelligible", so page and audio disagree.
- **Severity:** major (dropped hedge).
- **Fix:** "warns that we might come to the point where ...". Optionally use the published version, JBF 140 (2022), pdf p. 8 (journal p. 7): "will likely be unintelligible to humans". That is the authors' later, still hedged, wording. Also fix the source-list title (see minor 14).

### M3. Lens 4 diagram: a claim about Truth Terminal that the sources do not make
- **Post (#lens-social, cfg-status, last step):** "In the one case we checked, Truth Terminal, the money and liability ran to people."
- **Sources:**
  - Cointelegraph: Andreessen "sent $50,000 worth of Bitcoin (BTC) to the bot's wallet".
  - Decrypt: "neither the bot nor its handler created the token. 'Someone else did.'"
  - Neither source discusses liability. The creator of the token is unknown.
- **What the post does:**
  - The donation went to the bot's wallet, not to a person (the post's own section 4 says Andreessen donated "to Truth Terminal").
  - "Liability" appears nowhere in the sources. The node "people: donor, handler, creator" is ours, but the step text states it as a finding about the one real case.
- **Severity:** major (unsupported claim about a real case, used as the evidence step of the Lens 4 test).
- **Fix:** "In the one case we checked, a donor sent bitcoin to the bot's wallet, a human handler approved its posts, and someone else created the token; the sources say nothing about who would be liable."

### M4. Arora et al. toy: the search over C(100,10) is not where the paper's hardness lies
- **Post:**
  - #lens-info Ladder 2: "A buyer hunting the junk must search possible junk sets: 17,310,309,456,440 of ten".
  - cfg-seller, last step: "A buyer who tries every possible junk set faces 17,310,309,456,440 sets".
  - #ladder Rung 1: "The minimum runs over C(100,10)≈1.73×10^13 sets: that search is the hard part."
- **Source (Arora et al. WP, printed pp. 3-4):**
  - The plain bundle has lemon cost n/2 and needs no search.
  - The hardness is in detecting whether a *derivative's pooling* over-represents some n-set: M products of D assets, junk placed "to swing the election".
  - p. 4: a computationally unbounded buyer "can enumerate over all possible n-sized subsets of [N] and verify that none are over-represented". That is the easy, infeasible brute force, not the hardness claim.
- **What the post does:**
  - The toy pool (100 assets, F = sum) has no derivative. Every 10-set gives the same expected value 45, so there is nothing to search.
  - The numbers (45, 5, C(100,10)) are correct; the story attached to them is not the paper's.
  - The paper's mechanism (seller chooses which assets go into which pools; poly-time buyer cannot tell) is absent, and the post then says "what is hard is the price".
- **Severity:** major (the toy misdescribes the source's mechanism; the Rung 1 sentence is not marked "ours").
- **Fix:** either add the pooling layer to the toy, or write: "C(100,10) is the size of the brute-force check an unbounded buyer would run on a pooled derivative; the paper's claim is that no poly-time check is known under the conjectured assumption." Drop "that search is the hard part" for the plain pool.

## Minor findings

1. **#hook.** "Harari accepted the comparison in part" [BIS [9:12]]. BIS [9:08-9:27]: "your example with the airplane is perfect ... it's the same with finance, we don't need everybody to understand everything." Fix: "accepted the comparison, then argued that 1% and 0% are very different." (Audio `hook` repeats it.)
2. **#home, last sentence of "The evidence".** "(He calls AI 'a tool' at the BIS ... and 'an agent' at Davos)". BIS [38:20]: "The difference is that AI has agency, unlike printing presses." Also [39:50] "entities with agency" and [16:21] "first tool in history that can make decisions by itself". The contrast overstates a change of view. Fix: drop it, or add the BIS "agency" lines.
3. **#home, "His assertion".** "This bridges to post 01: his answer to what a next-word predictor knows is enough ..." and #hook "his Davos 2026 argument is about machines that ... predict the next word". WEF [5:15-5:20]: "It barely predicts the next word in a sentence. But is that so different from what the human mind is doing?" He asks a question and states a condition ([4:47] "If thinking really means putting words ... in order"). He never says what a predictor "knows". Fix: mark the bridge "(ours)" and keep his condition.
4. **#lens-social, "Testing Harari's chain".** "Chain: money is words, so AI takes over money." Ynet: money's value comes from "the stories that bankers, finance ministers and cryptocurrency gurus tell us about it" (stories, not words). BIS [23:15-23:26]: "Money is trust between people." He never links the two statements. Fix: "The chain is ours, built from two of his sentences", and add his BIS "money is trust" line.
5. **#home.** "In 2023 he called an AI financial crisis 'a catastrophic risk' but not, 'by itself', 'existential'". Guardian 2023: "It could, indirectly, if it triggers certain kinds of wars or conflicts. It's a catastrophic risk ... but by itself I wouldn't describe it as existential." The "indirectly, via wars" qualification (the stronger half) is dropped. Fix: add it.
6. **#home / #answer (balance, hedges both ways).** Harari's own limits and remedies are absent. BIS [20:36]: "if it was doomed, there was no point in having this conversation". BIS [20:46]: "History is never deterministic". BIS [21:55]: "We need to build good institutions". WEF [11:39]: humans' place "depends on ... our non-verbal feelings". The post gives him the "present moment, we still think better" hedge only. Fix: one sentence each ("he says it is not inevitable and names institutions and humans in the loop as the remedy").
7. **#llm, "Not found".** "The FSB: 'use cases generating new revenue streams are not widely observed at present' [p. 1]" is offered as support for "no AI-invented traded instrument". FSB p. 1 is about AI use cases in finance generally; it does not discuss AI-invented instruments. Fix: "The FSB reports ...; it does not address AI-invented instruments, so this is background, not a test."
8. **#llm, "Agents with wallets".** "valued in reports at about $122 million to over $214 million [Cointelegraph 2024]". Cointelegraph gives $122m (now), $150m (peak, "just over" and "just under" in one article); the $214m ("more than $214 million, according to CoinGecko") is Decrypt. Fix: cite both.
9. **#llm, "Found".** "neural nets that find auction mechanisms, only 'approximately incentive compatible' [Dütting et al., p. 3]". Source p. 3: RegretNet "will generally only find mechanisms that are approximately incentive compatible"; RochetNet (single bidder) is the other approach. Fix: "RegretNet generally finds only approximately incentive-compatible mechanisms".
10. **#llm, cfg-llm.** "A person can read that line (Luo et al. 2026)"; "Only then is there a trade. The LLM proposed; the checker decided." Luo et al. abstract and p. 1-2: OQL is a high-level intermediate representation, "validated and executed deterministically by an engine to instantiate executable strategies". "Interpretability" is the authors' claim in the introduction; the system produces candidate strategies, not trades; "one line" is not stated. Fix: "(our gloss)" and "a candidate strategy".
11. **#lens-info "Look inside" (box-tree).** "What would help? A 'tree of majorities' ... so tampering could be detected afterwards." Source p. 12: "Another, perhaps more plausible candidate", "in our simple model", ex-post detection of a dense subgraph, and the bound is "o(2^k) ≫ √3^k". The hedges and the √ comparison are dropped. Fix: add "perhaps", "in their simple model", and "much more than √(3^k)".
12. **#play, answers.** "(2) all three at 0.8; two at 1." With loss 1.0 and X1+X2 seeded, 5 of 6 fail, not all six (numbers.md and my rerun agree; X3 has no borrowers' loss). Fix: "two at 1 sink five of six".
13. **#lens-decision, Ladder 4.** "each step feeds back Am times the last move; once Am>1 the push outgrows the pull". At m = 0.25 push (0.375) equals pull (0.375), yet the swing still decays until Am > 1. The criterion is the product of the roots, c = Am > 1, while the roots are complex (Rung 4 says so). Fix: "once Am>1 the swing grows each step".
14. **#sources.** "Danielsson, Macrae & Uthemann (2017). AI and systemic risk. LSE SRC Paper 13." The 2017 paper is "Artificial intelligence, financial risk management and systemic risk" (SP13); "AI and systemic risk" is the 2022 JBF title. Fix: correct the title, or cite the 2022 paper.
15. **Audio `lens-control`.** "Ashby says that when capacity cannot be raised, a constraint is the regulator's only hope." Ashby p. 247: "if R's capacity is not easily increased and the other methods are not possible". Dropping "easily" and "other methods" turns it false (lowering the standard is still possible). The page version is correct. Fix: "when capacity is not easily raised and the other ways are closed".
16. **Audio `llm`.** "auction mechanisms checked only approximately". Source: the networks *find* approximately incentive-compatible mechanisms. Fix: "auction mechanisms that are only approximately incentive compatible".
17. **#home, 2010 section.** "simple programs in a 36-minute crash" and "The lesson is speed and feedback, not opacity". KKST do not call the programs simple; the "lesson" is ours but unmarked. Fix: drop "simple"; "Our reading: ...".
18. **#home, 2008 section.** "CDOs ... pools of loans sliced into tranches". FCIC p. 128: CDOs "purchase and pool financial assets such as the riskier tranches of various mortgage-backed securities". Fix: "pools of loans or loan-backed securities".
19. **#lens-decision, Ladders 2-3, cfg-bayes2 caption.** "world W4 (likelihood ratio 4)" and "Six banks (W5, ...)". "W4" does not appear in post 01 (same numbers, no label); "W5" is a file label. Internal jargon. Fix: delete the labels.
20. **#ladder Rung 2.** "The step: H(E) ≥ H(E|R) (conditioning cannot raise entropy), then expand." The expansion needs H(E,R) = H(D,R), i.e. D is determined by (E,R): Ashby's "no repeated outcome in a column" condition. Without it the inequality is not justified. The result is correct. Fix: state the condition (p. 207).
21. **#lens-control, counterweights; #answer.** "Narayanan and Kapoor: 'control is primarily in the hands of people and organizations'". Source (intro): "In this world" (advanced but not superintelligent AI), and they also write "a tool that we can and should remain in control of" (prescription). Fix: add "in the world they describe, with AI short of superintelligence".
22. **#answer, "Our reading".** "The best-supported links are ... the difficulty of delegating to an agent that hides its reasons." Scheurer et al. p. 1: "we do not aim to draw conclusions about the likelihood of this behavior occurring in practice". Layer 3 of the same section says shared-model correlation is "not measured for LLMs". Fix: "most plausible to us" instead of "best-supported", or name the evidence's limit.
23. **#lens-social, "Testing Harari's chain".** "'if laws are made of words, then AI will take over the legal system' [WEF 2026 [5:57]]". That sentence starts at [6:06]. Fix: [6:06].
24. **#lens-social, Personhood.** "its success is 'perfectly objective' [Dennett p. 24]". Dennett p. 24: "the facts about the success or failure of the stance ... are perfectly objective". Fix: "the facts about its success or failure are 'perfectly objective'".
25. **#lens-social, Accountability.** "Institutions supply 'verification or a penalty for lying' [p. 207]". Lupia p. 207 n. 2 says candidates supervised by party leadership "may be subject to verification or a penalty for lying". Fix: "e.g. party supervision supplies ...".
26. **Lede.** "AI could make financial contracts no person can understand." Harari says "financial devices" and "the financial system" (BIS, WEF); "contracts" is our word. Fix: "financial devices".
27. **#lens-decision.** "The FSB lists four drivers of common AI models: herding, ... lack of transparency [p. 20]". FSB: "could be driven by several factors, including". Fix: "lists four possible drivers".

## Counts
- **Critical: 0**
- **Major: 4** (M1 balance, M2 Danielsson hedge, M3 Truth Terminal "liability", M4 Arora toy mechanism)
- **Minor: 27**

## Checked and found correct

**Harari audio and text** (small.en re-transcription, or machine transcript plus s2/A3b audio checks):
- WEF [5:10-5:20] (glorified autocomplete, "barely predicts the next word", "is that so different"), [5:48] ("thinks better than many of us"), [5:57] ("anything made of words will be taken over by AI"), [10:36] ("Everything made of words ..."), [2:01] ("not just another tool. It is an agent"), [16:28], [19:11], [31:54-32:12] (the "ten years from now, Davos" trap).
- BIS [3:00] ("maybe 1%..."), [3:30], [5:13], [7:18], [9:28], [9:54], [10:08], [10:27], [30:24].
- Guardian 2023 ("catastrophic", "by itself ... existential"; Milmo, 9 Nov 2023).
- Ynet 2023 money-and-stories quote. Fox "capitalism is hardly mentioned at all". Poole "No one has yet seen a chatbot create new ideas".
- "never 'LLM'" holds for both talks (BIS says "chatbot" once at [39:24]).
- None of the s2 "must not use" items 1-6, 8-9 and 11-19 occur in the page (checked by text); item 7 occurs (M2); item 8 is partly breached in the audio (minor 15).

**Home field:**
- FCIC p. 28 ("the securities almost no one understood ... first dominoes"), p. 128 (waterfall), p. 149 ("two key mistakes", "weren't that different to begin with", "two to three times higher"), all from images.
- KKST abstract quote and "about 36 minutes" (p. 1 of the paper). Narayanan-Kapoor Part I circuit-breaker sentence.
- Lopez-Lira and Tang: 90% (non-tradable initial reaction), Sharpe 6.54 → 3.68 → 2.33 → 1.22, "some suggestive evidence", p. 6.
- Scheurer: "consistently hides the genuine reasons", "existence proof", "nearly (but not exactly) 0%", "remains high under all prompts" (p. 8).
- FSB: p. 1 (two quotes), p. 20 (four items), p. 21 ("as if it were a single institution"), pp. 28-29 ("could change this in the future"), press-release bullets.
- MIT Sloan quotes (Vereckey, 30 Aug 2023; labelled "as reported"). Mik, Luo (quote), Buehler (risk management).
- Truth Terminal: "semi-autonomous AI agent", $50,000 in Bitcoin, "neither the bot nor its handler created the token".

**Theory sources:**
- Shannon p. 1 quotes. Cover and Thomas Theorem 7.2.4 (p. 150, 1st ed.; "can produce only one possible output sequence"), p. 151 (machine dependence), p. 163 (non-computability).
- Arora et al.: abstract quote, p. 1 "may be computationally intractable", p. 2 lemon cost ($1,000/$800/$200), Table 1 reading (p. 6: "much larger than n" poly-time, "much smaller" exp-time), p. 12 "clearly only a first step", tree of majorities on p. 12. Akerlof p. 489 ("bad cars tend to drive out the good").
- Ashby pp. 207, 208 (H_D(R) misprint), 209 ("owes nothing to experiment"), 246 (three possibilities), 247 (condition quoted correctly on the page). Danielsson and Uthemann abstract and introduction quotes.
- Keynes ch. 12 (convention; "fail conventionally"; section numbers by s2). Granovetter pp. 1424-1425 (verbatim "essentially identical"; 100 → 1). Lupia Theorem 5.1 (pp. 85-86). SEP § 4.2.3 and § 5.6 (Menger). Dennett p. 24 (OCR plus page image).

**Numbers:**
- `check.mjs`: 14/14 configs OK; notebooks reproduce 1 / 2 / 6 / 3 failures, root sizes 0.548 / 1.002 / 1.162 and N_eff 10 / 2.703 / 1.099 / 1.
- Independent rerun: 2^100 ≈ 1.27e30 (page "about 1.3e30" OK); contract A cell counts (1/6/9); senior-tranche chance 0.370% / 5.185% / 10.000% (14.0× and 27.0×); p = 0.02: 2.000% vs 0.0032% (634.5×); 10^4, 13.29 bits, 63 / 1,023 / 16,383, 10^16 and 1.05e-10; 45, 5, C(100,10) = 17,310,309,456,440; Ashby 2 / 1 / 13.29 / 9.29 / 6.64 and brute force over all 16 plans = 2 outcomes; H = 1.75, 0.75; N_eff incl. N = 100 → 3.257 and N = 2 check 1.33 / 0.75σ²; 1e-20; Bayes 0.5 / 0.8 / 0.941 / 0.985 / 0.996 / 0.999999.
- W5 cascade: 1, 2, 6 (3 rounds), κ = 1.2 → 5, κ = 1.25 → 3, ×1.5 → 3, loss rate 1 with Y1 alone → 3. Hand-step table matches. Herding: −0.9 / −0.51 / −0.189; −2.30 / −3.94; swings at m = 0.2, 0.67, 0.9 and the breaker ±3.00; tipping at 2/3.
- Tree of majorities: min 4 flips for 9 inputs (4, 8, 16 follow 2^k). Granovetter 100 → 1.
- Post 01 cross-references (weather probabilities, H = 1.75, Bayes table) match.

**Audio script:** all spoken numbers match the page; quotes match except minor 15-16; recaps do not introduce claims. **english-gloss.json:** no factual claims beyond grammar and register; every example sentence is consistent with the post.

## Not checked (outside the post's citations)
Hayek, Minsky, Morris-Shin, Grossman-Stiglitz, Calvano, IMF, the *Nexus* sources and the Guardian 24 Aug 2024 extract are not cited in the draft, so were not rechecked. Keynes section numbers (§ IV, § V) were taken from s2 (the library HTML has no § headings). Akerlof's page range "489-490" was confirmed only for p. 489.
