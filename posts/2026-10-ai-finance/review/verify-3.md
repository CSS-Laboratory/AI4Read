---
id: 2026-10-ai-finance/review/verify-3
stage: S5, round 3 (independent fact-check of the round-3 draft, checker A)
checked: 2026-10-18
draft: src/content.html (all visible text, 15 widget configs incl. diagram step texts and node labels, captions, fold-outs, exercise answers, Sources with URLs), audio-script.md, english-gloss.json; post.json and numbers.md as bookkeeping
round-2 inputs checked against the text: review/verify-2.md, review/verify-2b.md, review/round2-merged.md (binding), review/response-2.md (claims re-checked in the text, not trusted)
not read: self-review.md, critic files
method: >
  Harari audio re-transcribed with faster-whisper small.en (int8; WAV cut with ffmpeg -ac 1 -ar 16000, loaded with `wave` into float32 numpy):
  BIS [2:55-3:40], [5:08-5:35], [7:10-7:30], [8:55-9:32], [9:50-10:35], [16:15-16:58], [29:55-30:40] (the [30:24] line that round 2 had only from base.en);
  WEF [1:58-2:15], [2:40-3:00], [5:44-6:15], [8:03-8:20], [10:30-10:45], [11:35-11:55], [15:08-15:22], [16:12-16:58], [17:26-17:48], [19:05-19:30], [26:00-26:40], [30:50-32:20].
  Both base.en transcripts re-read in full for the balance check, and the Guardian 2023, Guardian 2024 extract, Ynet, Poole and Fox texts read in full.
  Text sources re-opened: D&U abstract and introduction; Danielsson et al. 2022 p. 7 (running heads counted); Scheurer pp. 1, 8; Luo abstract; Mik introduction; Cointelegraph and Decrypt (text and page metadata); FSB pp. 1, 20, 21, 28-29 (page footers located in the text layer) and press release; MIT Sloan (author, date); N&K intro and Part I; KKST abstract and p. 1; Dütting p. 3; Shannon p. 1; Arora WP pp. 1, 2, 4, 5, 11-12; Ashby pp. 207, 209, 246-247; FCIC pp. 28, 128 (page image), 149; library copies of Cover and Thomas (1st ed., p. 150), Keynes ch. 12, Lupia and McCubbins pp. 85-86 and p. 207, Granovetter pp. 1424-1425, Akerlof; SEP §§ 4.2.3, 5.6.
  Numbers: check.mjs (15/15 OK; every preset, every prose value, every cascade seed set at lgd 0.8 and 1.0, capital ×1.2/1.25/1.5), the three notebooks, scratchpad v3/nums.py (incl. the new 6-asset, 3-product toy over all 15 junk placements).
  URLs: all 25 URLs in Sources fetched (24 return 200; weforum.org returns 403 to curl but the page exists: WebFetch shows "An Honest Conversation on AI and Humanity", 17 Mar 2026, Harari and Tracey); the three DOIs resolve (302 to publisher).
---

# S5 fact-check, round 3: post 02

Severity follows rubric §A. Source quotes are at most 25 words. Section names are the `id`s in `src/content.html`. Timestamps: base.en and small.en differ by up to ~5 s; I treat that as correct.

## (a) Round-2 fix verification

### Binding list §A: the four-group Harari classification
Every Harari line on the page and in the audio, checked against the re-transcribed audio or the saved text.

| Line (as printed) | Where | Group on page / audio | Source check | Verdict |
|---|---|---|---|---|
| WEF [2:00] "not just another tool. It is an agent" | box-harari | 1 | small.en [2:04-2:09] verbatim | correct |
| WEF [2:47] knife line, "new kinds of music, medicine and money" | box-harari | 1 | verbatim | correct |
| WEF [5:48]-[5:57] "AI already thinks better than many of us" … "anything made of words will be taken over by AI" | `home` table, box, Lens 4, audio `home`, `lens-social` | 1, premise kept | small.en [5:44-6:00] verbatim | correct |
| WEF [10:36] "Everything made of words…" | box | 1 | verbatim | correct |
| BIS [5:14] "can actually understand finance better than us"; [5:27] "It's only data, it's only information" | table, box, audio | 1 | small.en [5:13-5:28] verbatim; no "already" anywhere | correct |
| BIS [16:21] "make decisions by itself and can create new ideas by itself" | box | 1 | small.en [16:15] verbatim | correct |
| BIS [25:14] "already very creative", AlphaGo; extension [27:04], [30:07] | `home`, box | 1 | base.en verbatim; [27:04] "science, in art"; [30:07] "a sort of art" | correct |
| Guardian 2023 "ideal field for AI because it's only data" | box | 1 | verbatim | correct |
| Ynet "What gives money value is the stories…"; BIS [23:15] "money is really trust" | box, Lens 4 | 1 | verbatim | correct |
| BIS [30:24] "I think we'll see AI creativity also in this field coming up with new types of financial devices" | table, box, chain H3, audio | 2 | **small.en [30:20-30:32]: "So I think we'll see AI creativity also in this field, coming up with new types of financial devices that no human being would ever imagine creating."** Confirms the wording (base.en had "financial security") | correct |
| WEF [31:11] "We need to prepare for the moment … when AIs create a new financial system that they understand and we don't understand" | box, chain H3 | 2 | small.en [31:06-31:22] verbatim | correct (see n2 for H4) |
| WEF [16:28] "will soon be able to make the decisions necessary to manage a bank account" (… "and even to operate a corporation"); [16:36] "can therefore function as persons" | table, box, Lens 4, recall, audio | 2; [16:47] "Do we want to allow that?" = policy question | small.en [16:28-16:51] verbatim | correct |
| WEF [19:11]-[19:23] "Ten years from now, it will be too late…"; "Somebody else will already have decided it for you" | box, trap (3), Lens 4 | 2 | small.en [19:05-19:26]; quote truncated (n6) | correct group |
| WEF [26:29]-[26:35] "AI will beat me. I don't know how long it will take…" | box | 2, "timing explicitly unknown" | small.en [26:29-26:37] verbatim | correct |
| BIS [9:54] "Now imagine a situation maybe in 10 years…"; [10:19]; [10:27] | table, box, chain H4, audio, recall | 3 | small.en [9:53-10:31] verbatim | correct |
| WEF [17:29] "Suppose some … AI persons invent super efficient and super complex financial devices…" | box | 3 | small.en [17:29-17:43] verbatim | correct |
| WEF [31:54]/[31:59] "Maybe nobody in the room…" | box, trap (2), chain H4 | 3 | small.en [31:52-32:13] verbatim | correct |
| BIS [3:00] "maybe 1%…"; [3:30] "It could lead to power shifting…" | hook, box | 3 | small.en verbatim | group slightly loose (n7) |
| Guardian 2023 "What happens if…"; Guardian 2024 Broomstick | box | 3 | verbatim | correct |
| WEF [8:07], [11:39]; BIS [12:42], [20:46], [21:37], [22:57] | table, box, Lens 4, audio | 4 | small.en/base.en verbatim | correct |
| Guardian 2023 "catastrophic … by itself I wouldn't describe it as existential"; "indirectly" | box | 4 | verbatim, scoped to the financial crisis | correct |
| Guardian 2024 "Computers are not yet powerful enough…"; **"As long as humanity stands united, we can build institutions that will regulate AI"** | box | 4 | the next sentences are "Unfortunately, humanity has never been united" and "The rise of AI poses an existential danger to humankind" | **new M1** |

- **Verbatim summary sentence**: identical to round2-merged §A in `answer` (short answer box). Audio `answer` splits it into three spoken sentences with the same content. post.json summary uses the same three verbs. **fixed**.
- **Banned phrasings** ("his timelines are hedged", "forecasts are conditionals", "a policy question, not a forecast"): none in content.html, audio-script.md or post.json (grep). One stale label remains in numbers.md (n10).
- **Personhood both forecast and policy question**: `lens-social` "The capability claim is a forecast; the recognition question is policy, with a deadline he adds at [19:11]"; box group 2 entry says the same. **fixed**.

### Binding list §B
| id | Verdict | Evidence |
|---|---|---|
| B1 classification | **fixed** | table above; one new balance problem in group 4 (M1). |
| B2 Danielsson and Uthemann | **fixed** | Lens 2 lever 2: "amplifies existing financial system vulnerabilities", "faster and more severe" (abstract, verbatim); "cannot effectively prevent and resolve" (introduction, verbatim); "both stabilise and destabilise … depending on the severity of the shocks it faces and how prepared the financial authorities are" (introduction; page paraphrases the condition correctly); proposal (abstract). No longer under Counterweights. Audio `lens-control` matches. |
| B3 chain diagram | **fixed, with two label issues** | Title "Our compression of Harari's chain: his status, our evidence"; nodes H1-H4 only Harari; evidence tags as specified (H1 contested; H2 partly; H3 not yet evidenced, FSB p. 1 and pp. 28-29; H4 2008 only, FCIC pp. 28, 149; with AI none); our branch dashed, "Our additions, not his", tagged "Ours; FSB 'could' … toys use ordinary lenders" and "Ours; Scheurer: one red-team test, no likelihood estimate"; no "shown in toys" for hidden reasons or invented instruments; five-step reveal. Remaining: edge labels put his status on links he does not make (n1); H4's "nobody understands" half is also group 2 (n2). |

### Binding list §C (key minors) and the two round-2 checker files
| Item | Verdict | Evidence |
|---|---|---|
| A-M1 personhood | fixed | see §A. |
| A-M2 / B-m6 D&U | fixed | see B2. |
| A-M3 chain | fixed (n1, n2 residual) | see B3. |
| A-n1 / B-18 CDO "mostly" | fixed | "pools of financial assets, such as the riskier tranches of mortgage-backed securities" = FCIC p. 128 (page image). Audio same. |
| A-n2 / B-M2 [26:33] hedge | fixed | full sentence with "I don't know how long it will take". |
| A-n3 / B-m7 Scheurer | fixed | "Prompts that strongly discourage insider trading bring the trading to 'nearly (but not exactly) 0%', yet … 'remains high under all prompts'" = p. 8. |
| A-n4 "already" | fixed | only inside the WEF [5:51] quote. |
| A-n5 correlation range, variance | fixed | "runs from −1 to 1; we use 0 to 1"; variance "average squared distance from their mean"; covariance ρσ² defined. |
| A-n6 6.64 | fixed | "13.29 to 6.64 bits, a drop of exactly half (6.64 bits)"; log₂10⁴ = 13.2877, half = 6.6439. |
| A-n7 short answer Lupia, "could not foresee" | fixed | Lupia pattern stated correctly (Theorem 5.1, pp. 85-86); "may not be able to … or foresee". But (iv) in the same box says "verify and penalise" (n4). |
| A-n8 OQL "Trade" | fixed | node "Executable strategy"; step 4 "(our gloss)"; "proposed; the checker decided" gone. |
| A-n9 / B-m2 handler | fixed | "only approves its X posts and decides whom it interacts with" (Cointelegraph). |
| A-n10 / B-m5 source list | fixed | all entries titled; all URLs complete and resolve (see header); post.json `cites` has no Calvano, Lopez-Lira, Nexus or Mridul. |
| A-n11 N&K | fixed, slight residue | "a notion they view as incoherent"; the source adds "as usually conceptualized" (n8). |
| A-n12 plane | fixed | "(ours: a plane, where regulators supply the knowledge)". |
| A-n13 WEF [17:29] | fixed | box group 3, verbatim. |
| B-M1 [30:24], [31:11] as forecasts | fixed | group 2 in table, box, chain. |
| B-m1 Truth Terminal "both say" | fixed | Decrypt "neither the bot nor its handler created the token"; Cointelegraph "did not launch". $122M dated 14 Oct (Cointelegraph, "down from its $150 million peak on Oct. 14"); $214M dated 16 Oct (Decrypt, "according to CoinGecko"). |
| B-m3 Mik | fixed | "introduction" (txt lines 37-40). |
| B-m4 Decrypt date | fixed | 16 Oct 2024 (page metadata datePublished 2024-10-16T02:22:40). |
| B-m8 Poole pairing | fixed | "On the claim that chatbots create new ideas, Poole answers …". |
| B-m9 AlphaGo extension | fixed | [27:04], [30:07]. |
| B-m10 limits | fixed | "Our reading: that is a limit on the words thesis." |
| B-m11 [5:57] premise | fixed | [5:48] premise quoted in table, box, Lens 4, audio. |
| B-m12 "LLMs now translate" | fixed | "A research pipeline improves LLM translation …" (Luo abstract: "significantly improves execution accuracy"). |
| B-m13 audio "neural networks … approximately IC" | fixed | sentence removed from page and audio; Dütting now only "search for auction rules" (p. 3). |
| B-m14 Fox | fixed | verbatim. |
| B-m15, m16 "(ours)" | fixed | Lens 4 intro "Our framing (ours)"; section 12 "(ours, to test)" twice; audio same. |
| B-m17 Keynes | fixed | "worldly wisdom teaches that …" (§ V) and "we have tacitly agreed …" (§ IV), verbatim in the library HTML. |

### Writer's claims in response-2.md
All checked in the text. True: RegretNet/"approximately incentive compatible" removed from page and audio; OQL gloss removed; 30 entries with full titles and URLs (books without URL); four-group table and fold-out; verbatim sentence; [16:47] as policy question; D&U restored and out of Counterweights; dg-chain rebuilt as described; CDO "such as"; [26:33] full; Scheurer wording; correlation range; 6.64; Lupia pattern; Truth Terminal dates/outlets; Mik introduction; Decrypt 16 Oct; Poole; AlphaGo; Fox; Keynes; "(ours)" labels; tiny toy totals 1/4 vs 1/2 recorded in numbers.md; "intractable" glossed as a conjecture; C(100,10) removed from page and diagram; option example with numbers; link types on every "Lens N picks this up"; covariance; "1:1, 4:1, 16:1"; m = 0.67 check (Am = 1.005); word count 6,942 main / 1,853 fold-outs (rerun: same). I did not re-measure formula clipping (render test, not a fact check). No claim in response-2.md was found false.

## (b) New findings

### Major (1)

**M1. Balance: a Harari sentence that he immediately negates is listed as one of his "remedies"; his unhedged "existential danger" claim from the same paragraph is absent** — `home`, box-harari, group 4 ("Concedes, proposes: his limits and remedies")
- Post: "“Computers are not yet powerful enough to completely escape our control” and “As long as humanity stands united, we can build institutions that will regulate AI” [Guardian 2024]".
- Source (Guardian 2024 *Nexus* extract, same paragraph, next sentences): "Unfortunately, humanity has never been united." … "The rise of AI poses an existential danger to humankind, not because of the malevolence of computers, but because of our own shortcomings."
- What is wrong: the quoted conditional ("as long as … united") is the setup for his point that the condition has never held; filing it as a remedy, without the next sentence, reverses its force. The paragraph's central unhedged claim ("an existential danger to humankind") appears nowhere, while the page does print the Guardian 2023 line "by itself I wouldn't describe it as existential" (about the financial crisis only). Together these make Harari look more reassured about control than he is. (The Guardian 2023 article also has him saying the many AI scenarios "taken together … constitutes an existential threat to the survival of human civilisation".) The balance rule counts this direction as major too.
- Severity: **major** (balance rule: a central unhedged claim omitted and a sentence's force reversed by truncation).
- Fix: Replace the bullet with: "“Computers are not yet powerful enough to completely escape our control”; “As long as humanity stands united, we can build institutions that will regulate AI … Unfortunately, humanity has never been united” [Guardian 2024]", and add to group 1: "“The rise of AI poses an existential danger to humankind, not because of the malevolence of computers, but because of our own shortcomings” [Guardian 2024]". Keep the 2023 "by itself … not existential" line, which is correctly scoped to the financial crisis.

### Minor (10)

**n1. Chain diagram: edge labels give "his status" to links he does not make** — `answer`, `dg-chain` edges e1-e3; audio `answer`. Post: edge H1→H2 labelled "asserted", H2→H3 "predicted"; step 2: "He does not link H1 to H2 in our sources; the order is our compression"; audio: "Each link carries his status: asserted, predicted or imagined." Source: Lens 4 of the post itself ("he does not connect these steps in our sources"); the transcripts contain no such links. The labels are the status of the *target node*, but on an arrow they read as the status of the inference, and the audio says so explicitly. Mitigated by the title and step texts, so minor (label slip), but it is the same pattern as round-2 M3 (ii). Fix: put the status in the node ("H2 · asserted (group 1)") and label every edge "our order"; audio: "Each step carries his status."

**n2. H4 "Nobody understands" is also part of a group-2 forecast** — `dg-chain` H4 and step 4; `lens-social` "nobody understands finance, and crises have no explanation (group 3)". WEF [31:11]-[31:39] (small.en): "when AIs create a new financial system that they understand and we don't understand. How do you train economists … in a world in which humans really can no longer understand how finance functions". The *crisis nobody can explain* is imagined ([9:54], Broomstick), but *humans no longer understanding finance* is in his unhedged [31:11] forecast (the page itself files [31:11] under group 2). Fix: H4 step text "the loss of understanding is part of the [31:11] forecast (group 2); the crisis nobody can explain is imagined (group 3)", or split H4.

**n3. Lens 1 tiny toy points the opposite way to Arora's mechanism** — `lens-info` Ladder 2 "Tiny toy", `dg-seller`, audio `lens-info`. Post: AND products; "If the junk sits in two different products … total 1/4. If both junk assets share a product … total 1/2"; then "Scale it up … a seller can hide a few skewed placements" (Arora pp. 3-4). Arora WP p. 4: the seller's optimum is to make "the lemon assets … overrepresented in their pools … just enough to skew the probability of default". In Arora, concentrating junk *lowers* the value; in the toy, concentrating junk *raises* it (1/2 > 1/4), so the reader who maps "skewed" onto "Concentrated" learns the wrong direction. Arithmetic is right (Python over all 15 placements: 12 spread give 1/4, 3 concentrated give 1/2; E[F] = 3/4, Δ(2) = 1/2), and the toy is labelled ours, so minor (toy whose meaning is ambiguous). Fix: use senior-tranche-like products, "a product pays 1 unless both its assets default": healthy 3/4; spread total 1/2 + 1/2 + 3/4 = 7/4; concentrated 0 + 3/4 + 3/4 = 3/2; E[F] = 9/4, Δ(2) = 3/4 (checked by hand; rerun in numbers.md). Then concentration is the harmful placement, as in Arora. Or keep AND products and say "here spreading is the harmful placement; in Arora's CDOs it is concentration".

**n4. Short answer (iv) contradicts the Lupia pattern two sentences later** — `answer` short-answer box; audio `answer`. Post: "(iv) accountability needs someone who can verify and penalise (Lens 4)". Lupia and McCubbins pp. 85-86: "If only one of the two conditions is satisfied, then the worst that can happen … is the retention of the status quo"; p. 207 "verification or a penalty for lying". Labelled "ours, conjectured", but "and" makes both necessary. Fix: "accountability needs someone who can verify the agent, or a penalty that gives it reason to be honest (Lens 4)".

**n5. Personhood: corporations line mis-cited and its scope dropped** — `lens-social` Personhood; audio. Post: "asks whether your country will recognise them as legal persons, as corporations already are [16:47]". WEF [15:14] (small.en): "In many countries, corporations are considered legal persons"; [16:47]-[16:51] is the question. Fix: "…as corporations already are in many countries [15:14]".

**n6. [19:11] quotation truncated to finance without an ellipsis** — box-harari group 2. Post: "“Ten years from now, it will be too late for you to decide whether AIs should function as persons in the financial markets”". WEF [19:05-19:26]: "… as persons in the financial markets, in the courts, in the churches." Fix: add "…" or the full list.

**n7. Group 3 holds a hedged estimate, not a thought experiment; the actual what-if is missing** — box-harari group 3. Post: "“maybe 1% of the population really understands how the financial system works” [3:00]; “It could lead to power shifting…” [3:30]" under "thought experiments, hedged". BIS [3:00-3:36] (small.en): the 1% line is his estimate of the present; the thought experiment is "What happens if this number goes down to zero? … because AI has made it too complicated." Fix: quote [3:09] "What happens if this number goes down to zero?" as the group-3 line and keep [3:00] as its premise.

**n8. Narayanan and Kapoor: a qualifier dropped** — `lens-control` Counterweights; box-layers critics; audio. Post: "advanced but not “superintelligent” AI (a notion they view as incoherent)". Source (intro): "'superintelligent' AI, which we view as incoherent as usually conceptualized". Fix: add "as usually conceptualized".

**n9. "agents hold wallets" generalises from one case** — `answer` short answer (a); audio. The only case in the post (and in the saved sources) is Truth Terminal; the manifest lists other agent wallets as unverified leads. Fix: "an agent (Truth Terminal) held a wallet".

**n10. numbers.md keeps a label that the binding list removed** — numbers.md §C: "“Ten years from now, it will be too late” (a decision deadline, not a forecast)". Not on the page or in the audio, but it contradicts round2-merged §A ([19:11] is group 2). Fix: "(group 2: forecast with a decision deadline)".

### Balance check (summary)
- Harari, unhedged side: every central unhedged finance line found in both full transcripts is on the page in the right group (BIS [5:14], [16:21], [30:20]; WEF [2:47], [5:57], [10:36], [16:28], [19:11], [31:11]; Guardian 2023 "ideal field"; Ynet "stories"). WEF [31:24]-[32:13] (humans "can no longer understand how finance functions"; AIs' devices "mathematically beyond the human capacity") is the continuation of [31:11] and its [31:59] "Maybe" scenario; adequately represented once n2 is fixed.
- Harari, hedges: all kept ("maybe in 10 years", "a couple of years", "Suppose", "Maybe nobody", "at least for now", "I don't know how long it will take", "by itself … not existential", "indirectly").
- Harari, other direction: M1 (Guardian 2024 remedy truncated; "existential danger" absent).
- Danielsson and Uthemann: main result and concession now both present. FSB, Scheurer, Arora (simple model, conjecture, "probably correct"), Skingsley, Poole, Fox: at strength. N&K: n8 only.

## (c) Counts
- **Critical: 0**
- **Major: 1** (M1 Guardian 2024 truncation / balance)
- **Minor: 10** (n1-n10)

Round-2 items: binding §A and §B fixed (B3 with label residue n1, n2); all §C minors fixed; all 3 majors and 13 minors of verify-2 and both majors and 17 minors of verify-2b fixed (A-n11 with residue n8). No writer claim in response-2.md was false.

## (d) Checked and found correct

**Numbers (all rerun).**
- check.mjs: 15/15 configs OK. cfg-cdo presets 0.370% / 5.185% (14.0×) / 10.000% (27.0×) / p = 0.02: 2.000% vs 0.0032% (634.5×). cfg-count k = 6: 63 (0.0063); k = 10: 1,023 (0.102); k = 14: 16,383 (fraction 1); two days k = 20: 10¹⁶ contracts, 1.05e-10. cfg-ashby 9.29 / 2.64 / 4.29, and 0.00 at V_R = 14. cfg-neff 10.000 / 2.703 / 1.099 / 1.000; N = 100, ρ = 0.3: 3.257; N = 2, ρ = 0.5: 1.333. cfg-bayes2 0.5 / 0.8 / 0.941 / 0.985 / 0.996; n = 10 odds 1,048,576, P = 0.999999. cs-w5: default 6 of 6 in 3 rounds; every single seed 1 of 6 at lgd 0.8; at lgd 1.0 Y1 alone 3 of 6, other singles 1 of 6; every X pair 2 of 6 (0.8) and 5 of 6 (1.0); all three X 6 of 6; capital ×1.2: 5 of 6, ×1.25: 3 of 6, ×1.5: 3 of 6. it-herding m = 0.2: 0.04 / −1.00 / 0.000; m = 0.67: 2.68 / −2.70 / −0.505; m = 0.9: 1345.97 / −50.21; breaker 3: ±3.00, final −2.505.
- Python: Contract A 1/6/9 cells, (8 + 6 × 4)/16 = 2; 2¹⁰⁰ = 1.268e30; q = 0.0037, 0.1/0.0037 = 27.0; 0.02/0.00003152 = 634.5; log₂10⁴ = 13.2877, log₂100 = 6.6439 (exactly half); 2⁶ − 1 = 63; Ashby toy minimum 2 outcomes over all 16 plans; H = 1.75, bound 0.75; N_eff derivation and values; 1/0.3 = 3.33; odds ladder; m = 0.2 steps −0.9, −0.51, −0.189; m = 0.9 steps −2.30, −3.94; Am = 1.005 at 0.67; root sizes 0.548 / 1.002 / 1.162, complex at all three m; tree of majorities minimum 4 flips over 512 inputs; Granovetter 100 → 1; cascade 12 ≥ 10, 4 + 8 = 12 ≥ 9, 12 ≥ 11, 12 < 15. New tiny toy: 15 placements, 12 spread → 1/4, 3 concentrated → 1/2; E[F] = 3/4; Δ(2) = 1/2 (box-lemon correct).
- Notebooks: ex1 (10.061, 2.712, 1.099, 1.000), ex2 (1, 2, 6, 3), ex3 (0.548, 1.002, 1.162; first m above 1: 0.67). Match page and numbers.md.
- Playground answers (1)-(3), Exercise 4 solution, recall cards: correct.
- Word count (scripts/wordcount.py): main 6,942, fold-outs 1,853.

**Harari and Skingsley wording** (small.en this round): hook [3:00], [7:18] ("most of us happily step into an airplane having very vague understanding of how that works"), [8:59]-[9:28]; every line in the §A table above. Guardian 2023, Guardian 2024 (Broomstick, "imagine the following scenario", "bigger even than 1929 or 2008", "not yet powerful enough"), Ynet ("stories", "better than the average human at telling stories"), Poole ("No one has yet seen a chatbot create new ideas"), Fox ("capitalism is hardly mentioned at all"). Harari never says "LLM" in either talk (grep; the one "ChatGPT" is Tracey).

**Home field and LLM section.** FCIC p. 128 (image: "purchase and pool financial assets such as the riskier tranches of various mortgage-backed securities"; waterfall), p. 149 ("two key mistakes"; "weren't that different to begin with"), p. 28 ("almost no one understood … first dominoes"); KKST abstract quote and "about 36 minutes" (p. 1, "collapsed and rebounded"); N&K Part I circuit breakers; Luo abstract; Mik introduction; Cointelegraph (14 Oct, Mitchelhill; July 11 donation "to the bot's wallet"; handler role; $122M from $150M peak; bot did not launch); Decrypt (16 Oct; "semi-autonomous AI agent"; "neither the bot nor its handler created the token"; >$214M per CoinGecko); FSB p. 1 (correlation quote; "not widely observed at present"), p. 20 (four drivers incl. herding, lack of transparency), p. 21 ("as if it were a single institution"), pp. 28-29 ("could change this in the future"), press release; MIT Sloan (Vereckey, 30 Aug 2023; "lockstep"; "mask who's at fault"); Scheurer abstract ("consistently hides the genuine reasons"), p. 1 ("existence proof"; no conclusions about likelihood), p. 8; Dütting p. 3; Buehler abstract.

**Lenses.** Shannon p. 1; Cover and Thomas Theorem 7.2.4, p. 150 ("can produce only one possible output sequence"), library copy is the 1991 first edition; Arora WP abstract, p. 1 ("may be computationally intractable"), p. 2 ($1,000 / 20% / $800 / $200), p. 4 ("hidden dense subgraph … believe to be intractable"; unbounded buyer can enumerate), p. 5 (Δ(n), "position"), p. 11-12 (tree of majorities "perhaps more plausible"; "probably correct"; "only a first step"); Akerlof "bad cars tend to drive out the good"; Ashby p. 207 (table rule, "variety can destroy variety"), p. 209, pp. 246-247 ("ways that may make regulation possible", "somewhat trivial", "only hope" with its condition); Danielsson et al. 2022 p. 7 ("will likely be unintelligible to humans"); D&U abstract and introduction (note: "cannot effectively prevent and resolve" is a premise in their introduction; "find" is a fair paraphrase, not counted); N&K intro ("primarily in the hands of people and organizations"; "median outcome"); Keynes ch. 12 §§ IV, V verbatim; Granovetter pp. 1424-1425 ("essentially identical"); SEP § 4.2.3 (stones, Bureau of Engraving and Printing, deontic powers, X counts as Y in C), § 5.6 (Menger); Lupia and McCubbins Theorem 5.1 pp. 85-86 (table cells match), p. 207 n. 2.

**Sources list.** All 30 entries have full titles; all 25 URLs complete and live (WEF via WebFetch); DOIs 10.2307/1879431, 10.1086/226707, 10.1016/j.jbankfin.2021.106290 resolve. Dates match page metadata (Guardian 9 Nov 2023, 24 Aug 2024, Poole 11 Sep, Fox 10 Sep, Cointelegraph 14 Oct, Decrypt 16 Oct, MIT Sloan 30 Aug 2023). cite-map bare timestamps map to the right talk.

**Audio script.** Every chapter compared with the page: numbers and quotes match, the verbatim summary is spoken, "AI4Read from CSS Lab" intro present; audio-specific issues only n1, n4, n5, n8, n9. The lede's "warns that AI could make financial devices no person can understand" is a fair one-line summary of the hedged scenarios plus [31:11]; not counted.

**english-gloss.json.** Definitions and wrong/right pairs: no factual claims beyond the post; the reporting-verbs entry matches the four-group scheme.
