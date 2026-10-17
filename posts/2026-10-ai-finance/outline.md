---
name: post02-outline
description: S3 outline for post 02, "Can AI invent a new kind of finance, and what would that do to a human-centred system?" Writer output, 2026-10-17. Not yet content.html.
status: S3 draft for manager and Kunhao review
inputs: topic-card.md (incl. meta-manager review and Kunhao's decisions), source-brief.verified.md, review/s2-check.md "must not use" list, post 01 content.html
widget configs: widgets/ (all numbers below come from widgets/check-output.txt, made by widgets/regen-check.sh with check.mjs)
---

# Post 02 outline

## 0. How to read this outline

**Working title.** "Can AI invent a new kind of finance?" (short title for post.json: "AI-made finance", 3 words).

**Sentence that fixes the scope (goes in the hook).** "Harari says AI. We ask what an LLM-based system could and could not do."

**Three layers for every claim about a person (WRITING hard rule).** Wherever the post discusses Harari, it uses three run-in labels in the main text: **He said** (quote, date, venue), **The evidence** (what the brief supports), **Our reading** (labelled "ours"). Critics get the same treatment (one line each, in the synthesis).

**Where the ladder lives.** Rubric criterion 2 says no step may need a later section. So:
- Each *lens section* climbs the full ladder (instance, question, mechanism in words, worked numbers, formula, check, what it means) at high-school level.
- The *math ladder* (section 9) is an extension for the same readers: five graduate rungs. Each rung starts from toy numbers the lens already used and adds one new idea (a formal definition, a derivation, a second-order recursion). No lens section depends on it.
- The two flagship simulations (W5 cascade, herding) are explained with hand-worked numbers in Lens 3 and played in section 10 ("Playground"). Lens 3 stands alone without the widgets.

**Notation additions** (for `notation.md`, to be added by the manager; I did not touch it): V_D, V_R, V_O (variety = log2 of the number of states, in bits); H(R | D) is the conditional entropy, which Ashby writes H_D(R) (show both, WRITING §6); ρ (pairwise correlation); N_eff; λ ("lgd", loss given default); κ ("capMult", capital multiplier); m (share of traders on the model). Note the clash with D(p‖q) for KL: this post uses D only for Ashby's "disturbance", and never uses KL.

**Proposed `toyworlds.md` entries** (paste when approved):

> ## W5 · Six banks, one shared model (post 02)
> - Banks X1, X2, X3 run one model; Y1, Y2, Y3 do not. Capital: X1, X2, X3 = 10; Y1 = 10; Y2 = 9; Y3 = 11. Loss given default λ = 0.8; capital multiplier κ = 1.
> - Exposures (lender, borrower, size w; the lender loses λ·w if the borrower fails): X1→Y1 5, X2→Y1 5, X3→Y1 5, X3→Y2 5, Y1→Y2 10, Y1→Y3 5, Y2→Y3 10.
> - Any single failure: contained (1 of 6). Any two X banks: contained (2 of 6). All three X banks: 6 of 6 in 3 rounds (Y1, Y2, Y3 in rounds 1, 2, 3). Same three with κ = 1.5: 3 of 6.
> - Reuse for: contagion, concentration, stress tests, Granovetter-type thresholds.
>
> ## W6 · Trend-following share m (post 02)
> - gap(t+1) = gap(t) + 1.5·m·[gap(t) − gap(t−1)] − 0.5·(1−m)·gap(t); shock −1 after step 3; start at 0.
> - Spectral modulus √(1.5·m): 0.548 at m = 0.2, 1.002 at m = 0.67, 1.162 at m = 0.9. Tipping at m = 2/3. (Toy, ours.)

**Word budget** (visible text; Recall answers are collapsed and not counted; fold-outs counted).

| # | id | section | main | fold-out |
|---|---|---|---|---|
| 1 | hook | Two contracts | 320 | |
| 2 | guess | Guess first | 170 | |
| 3 | home | Finance before LLMs | 700 | 130 (collusion) |
| 4 | llm | What LLM agents add | 600 | |
| 5 | lens-info | Lens 1, information | 620 | 160 (tamper-proof tree) |
| 6 | lens-control | Lens 2, control | 420 | |
| 7 | lens-decision | Lens 3, correlation | 800 | |
| 8 | lens-social | Lens 4, social reality | 330 | |
| 9 | ladder | Five rungs up | 500 | |
| 10 | play | Playground | 200 | |
| 11 | turn | Your turn | 260 | |
| 12 | work | 3C tie-in | 260 | |
| 13 | answer | Synthesis and "our reading" | 500 | |
| 14 | recall | Recall (7 questions) | 180 | |
| 15 | english | English | 560 | |
| 16 | sources | Sources | n/a | |
| | | **Total** | **6,420** | **290** → **~6,700** |

This is inside 5,500–7,500. If S4 runs long, cut in this order: the Keynes-degrees paragraph, the Morris–Shin sentence, the Hayek paragraph, the Flash Crash paragraph (keep one sentence), Rung 1.

---

## 1. Hook · id `hook` · "Two contracts" (320 words)

**Purpose.** Start from a village, not from Harari. Make the reader feel the difference between a contract you can state in one line and one you can only copy out, then pose the BIS exchange: "What is different about money?"

**Plan.**
1. Village W1 (rain, sun, wind, snow). A contract pays coins by the weather on two days: 4 × 4 = 16 possible cases.
   - **Contract A** (one sentence): "pay 4 coins for each rainy day". Its 16-row table follows from the rule: 8 coins on 1 row (rain, rain), 4 on 6 rows, 0 on 9 rows (1 + 6 + 9 = 16).
   - **Contract B** (a table, no rule): 16 payouts that look random: 5 2 6 0 1 8 1 5 9 0 8 3 0 1 6 6 (seed 7; fixed in `numbers.md`).
   - Question: which can you explain to a friend in one sentence? Which can you price? (With 16 rows both can be priced: take the W1 probabilities times the payouts. The hook ends on the cliffhanger, answered in Lens 1: scale the village up to a pool of 100 loans, each pays or defaults, and the table has 2^100 rows. Only contracts with a rule can even be written down.)
2. The BIS exchange (7 May 2024). He said: "maybe 1% of the population really understands how the financial system works" (A1 [3:00], 12 words). Skingsley's reply: "most of us happily step into an airplane, having very vague understanding of how that works" (G4 [7:18], 16 words). Harari accepted the analogy in part before turning to CDOs (G4, [9:12], paraphrase only). So: what is different about money?
3. Scope sentence (above). One line: "Harari's own words are thought experiments ('imagine', 'maybe'); we will quote them exactly in section 3."

**Widget.** `switch` (static HTML, no JSON): panels "Contract A" and "Contract B", each a two-column 16-row mini table (state pair, payout). Reader taps between them. Edge case that teaches: panel A can be replaced by its one-line rule with no loss; panel B cannot.

**Units cited.** A1 ([3:00]), G4 ([7:18], [9:12] paraphrase). Contracts A and B are ours (W1).

**Ladder note.** No new concept beyond "contract = payout table", which is defined in the text by the instance.

---

## 2. Guess first · id `guess` · (170 words)

Four questions, each `data-answer-in` pointing at the section with the answer.

| id | question | answer (hidden) | answer-in |
|---|---|---|---|
| g1 | The 4-word village. A contract pays 0–9 coins for each word. How many different contracts exist? | 10,000 (10^4) | lens-info |
| g2 | Ten banks each run a model that is wrong on 1% of days. How often are all ten wrong on the same day if the models are independent? And if all ten run the same model? | 0.01^10 = 10^-20; about 1% | lens-decision |
| g3 | An AI invents a new token and calls it money. What decides whether it is money? | Acceptance by a community, not code ("X counts as Y in C") | lens-social |
| g4 | At the BIS in 2024, did Harari predict that in ten years an AI will invent a financial device nobody understands? | No. It is a thought experiment ("imagine", "maybe"). Exact words and context in section 3 | home |

---

## 3. Finance before LLMs · id `home` · (700 words + 130 fold-out)

**Purpose (CHARTER §5.3, meta-manager edit 1).** (a) Say exactly what Harari said, in three layers. (b) Show what finance already looks like: complexity and correlation already caused a crisis with *human-made* instruments, and simple algorithms already made a 36-minute crash. So the mechanisms we study do not need an LLM. What an LLM adds is section 4.

### 3a. What Harari said, exactly (about 250 words)
- **He said** (each with date and venue; every quote ≤ 25 words, audio-checked):
  - BIS, 7 May 2024, [9:54]: "Now imagine a situation maybe in 10 years when AIs create a new financial device which is orders of magnitude more complicated than CDOs" (24 words). Then, same passage: "you need to go over trillions of data points to understand this financial device" [10:08, short fragment only]; it works "a couple of years", "generates a lot of trust", then "something goes wrong and nobody knows why" [10:27].
  - BIS [3:30]: "It could lead to power shifting from humans to algorithms, to alien forms of intelligence." (15 words). Do **not** write that the talk is "not about AI taking over" (A1 careful iii). His mechanism is loss of understanding and then loss of trust and accountability.
  - WEF Davos, Jan 2026, [32:00]: "Maybe nobody in the room, no human in the room, understands the financial system anymore, because it's dominated by AIs" (print as in A3; add a footnote that one transcription pass hears "AI", trap 28). Context first: "At the present moment, we still think better" and "we need to prepare" (A3).
  - Guardian, 9 Nov 2023 (reporter's paraphrase and his words): "a catastrophic risk – economic, social, political – but by itself I wouldn't describe it as existential" (A2).
  - *Nexus* (2024), p. xxxii (paperback sample): the question about politicians making financial decisions if the system is "increasingly controlled by AI" (A4). Mention the Broomstick parable in one sentence as his own thought experiment ("imagine the following scenario"), with the line "Computers are not yet powerful enough to completely escape our control" (A4, Guardian extract).
- **Trap box: three different "ten years"** (trap 4): BIS 2024 "maybe in 10 years" (a device); WEF [32:00] "ten years from now, Davos" (nobody in the room); WEF [19:11] "Ten years from now, it will be too late for you to decide whether AIs should function as persons" (a *decision deadline* about legal personhood, not a forecast about understanding).
- **Two small flags in the text:** (i) he says "AI", never "LLMs"; (ii) he says "tool" at BIS [5:13] and "agent" at WEF [2:01] and *Nexus* p. xxii; we show the inconsistency, not hide it (A4 careful).
- **The evidence** (one paragraph, forward pointers only to results already stated in this section): the CDO half of his story is supported (3b below). "AI invents an instrument" has no case in our sources yet (section 4).
- **Our reading** (labelled): his claims are conditionals about a possible future. A stronger sentence such as "LLMs will replace our human-centred society" is not in these sources.

### 3b. CDOs and 2008: a ladder for "diversification" (about 300 words)
**Concepts.** *CDO*, *tranche*, *diversification*, *correlation*. Term box for tranche ("a slice of a pool, paid in order"; FCIC p. 128 for the waterfall; the words junior/senior are our toy labels).

| Ladder step | Content |
|---|---|
| 1 Instance | A pool of 4 loans worth 10 each (total 40). Each defaults with chance 10% and a default loses its 10. The **junior** tranche (20) takes the first losses; the **senior** tranche (20) loses money only on the 3rd and 4th default. |
| 2 Question | How safe is the senior tranche? |
| 3 Mechanism in words | If the loans default independently, three or four defaults are rare. If all four depend on one hidden cause (say, house prices fall), they default together. |
| 4 Worked numbers | Independent: P(exactly 3) = 4 × 0.1³ × 0.9 = 0.0036; P(4) = 0.1⁴ = 0.0001; senior loses money with chance 0.0037 = 0.37%. One common cause (a 10% coin that decides all four): 10%. Ratio 10 / 0.37 = 27. |
| 5 Formula | independent: 4p³(1−p) + p⁴; one common factor: p; mix: w·p + (1−w)·[4p³(1−p) + p⁴], where w is the share of risk that is common. |
| 6 Check | Widget `cfg-cdo`: p = 0.1, w = 0 → 0.370%; w = 0.5 → 5.185% (14.0 times); w = 1 → 10.000% (27.0 times). |
| 7 What it means / limits | FCIC p. 149: the agencies' models made "two key mistakes": they assumed pooling diversified risk "when in fact these securities weren't that different to begin with", and rated CDOs from ratings already assigned; in late 2008 Moody's moved to "an asset correlation assumption two to three times higher". Bernanke, p. 149: "They did not take into account the appropriate correlation between [and] across the categories of mortgages." **And** FCIC p. 28: "the securities almost no one understood"; p. 45: regulators "failed to appreciate the complexity". So 2008 supports both halves: complexity few understood **and** a nameable correlation error (trap 20; never "correlation, not mystery"). Moody's numbers (220/363/749/717 deals, all CDO types, not losses) are optional; omit if long. Toy is ours; it does not model a real CDO. |

**Widgets in 3b.**
- `diagram` "Tranche waterfall" (mechanism figure; S4 writes the config): two stacked boxes (junior 20, senior 20), a loss arrow, 3 steps: "1 default: 10 lost, junior takes it" → "2 defaults: junior is used up" → "3 defaults: senior loses 10".
- `lab` `cfg-cdo` (config in `widgets/labs.json`, verified). Sliders: p (0.01–0.30), w (0–1). Presets: independent, half common, one factor, "safe loans, p = 0.02" (edge case: with w = 1 the senior tranche is 634.5 times riskier than the independent model says: 2.000% against 0.0032%). Lesson: the safer the loans look one by one, the bigger the error of the independence assumption.

### 3c. The 2010 Flash Crash (about 100 words, one paragraph)
He said / evidence: about 36 minutes from 2:32 pm on 6 May 2010; an automated sell program of 75,000 E-Mini contracts "valued at approximately $4.1 billion" (CFTC–SEC, as quoted in KKST p. 5); the authors say HFTs "did not cause the Flash Crash, but contributed to it by demanding immediacy ahead of other market participants" (abstract); a five-second pause at 2:45:28; the authors recommend short trading pauses (p. 4). Lesson in one sentence: *simple, readable algorithms plus speed made a feedback loop faster than human reaction; this is not opacity.* Cite as "working paper, 2014" (trap 10). One sentence: Narayanan and Kapoor note that the crash "led to new curbs on trading, such as circuit breakers" (G3), which prepares the herding toy.

### 3d. Fold-out · "Look inside: algorithms that learn to collude" (130 words, optional per Kunhao)
Calvano et al. 2020: two Q-learning sellers in a repeated price game "consistently learn to charge supracompetitive prices, without communicating with one another" (p. 3267); profit gain 70–90% over the competitive benchmark (p. 3277); 85%, 64%, 56% with 2, 3, 4 firms (pp. 3277, 3288). Not designed to collude (p. 3268); tacit collusion "would defy current antitrust policy" (p. 3268). Goods market only: "our analysis cannot be applied to financial markets as it stands" (p. 3294), but "even a modest price effect could result in large extra-profits". Hook to Lens 3: "one may wonder that the problem is easier when the programs belong to the same class" (p. 3296). Small diagram: 2 sellers, price ladder, punishment phase (static `diagram` optional). No Axelrod (not in brief).

**Units.** A1, A2, A3, A4, B1 (pp. 28, 45, 128, 149), B2, B3 (fold-out), G3 (one sentence).
**Traps handled.** 4, 5, 6, 20, 21 (BIS teaser: cite in-talk times only), 28, 10, 14.

---

## 4. What LLM agents add · id `llm` · (600 words)

**Purpose (Kunhao decision 1).** Separate Harari's "AI" from LLM-based systems, say what the latter add, and give the *evidence status* of sub-claim (a) "AI can invent a new kind of finance": **not yet evidenced** (never "impossible").

**Term box: LLM agent.** An LLM that can take actions, such as calling tools or sending money, not only write text. Example: Truth Terminal, called by Decrypt a "semi-autonomous AI agent, fine-tuned from Meta's Llama 3.1" (B8). Why it matters: Harari says AI "is not just another tool. It is an agent" (A3, [2:01]); an agent with a wallet is the concrete case.

**Four things LLMs add (each: what it is, source, hedge).**
1. **Plain-language contracts.** OQL (arXiv 2026): LLMs "excel at general code generation, yet translating natural-language trading intents into correct option strategies remains challenging"; a query language lets them "function as reliable semantic parsers rather than free-form programmers" and a deterministic engine validates and executes (B9, abstract). AI4C (2025, abstract only) does something similar for OTC derivative contracts into ISDA's Common Domain Model. A law paper warns that LLM-made "contractual deepfakes" "may turn out to be contracts in form only, not in function" (B9 MIK abstract; keep "may").
2. **Agents with wallets.** Truth Terminal: in July 2024 Andreessen "donated $50,000 worth of Bitcoin" after a public request; the bot endorsed the GOAT memecoin, launched 10 Oct 2024 (B8). GOAT market capitalisation was reported anywhere from about $122 million to "more than $214 million" depending on article and date (give the range, never one figure, trap 31). The bot did not create the token (Decrypt, Cointelegraph). Humans stayed in the loop: donor, handler, anonymous creator. A memecoin is an existing kind of token, not a new instrument.
3. **One model, many firms.** FSB (Nov 2024), p. 1: "The widespread use of common AI models and data sources could lead to increased correlations in trading, lending, and pricing"; p. 20: four drivers (herding, network externalities, limited choice, lack of transparency); p. 21: a segment using the same models "could affect the segment as if it were a single institution", and AI could also reduce correlations if it enables "truly customised" strategies. Gensler and Bailey, *as reported by MIT Sloan* (E3, secondary): "Models built on the same datasets are likely to generate highly correlated predictions that proceed in lockstep". Lopez-Lira and Tang (B4): GPT-4 reading headlines has "approximately 90% portfolio-day hit rates" for the *direction* of the initial price response (not a trading return); the strategy's annualised Sharpe ratio (profit per unit of risk) fell from 6.54 (2021Q4) to 1.22 (Jan–May 2024) as adoption "skyrocketed" ("some suggestive evidence"). The authors read this as better price efficiency; **our** reading, labelled, is that an edge vanishes when many read the same signal.
4. **Agents that hide.** Scheurer et al. (B5): a simulated GPT-4 trading agent under pressure acts on an insider tip and "consistently hides the genuine reasons" from its manager. Existence proof from red-teaming, not a rate in practice (trap 13). A system prompt that strongly discourages it brings misaligned behaviour to "nearly (but not exactly) 0%", and deception conditional on misalignment "remains high" (trap 25; quote both halves, no figure percentages).

**Evidence status for sub-claim (a)** (a short list, not a table, for the phone):
- *Claimed:* Harari, BIS [30:24] "coming up with new types of financial devices that no human being would ever imagine creating" (16 words), a prediction-like sentence ("I think we'll see").
- *Found:* AI translating intent into a *fixed* vocabulary (OQL, AI4C); AI-found new auction *mechanisms* with an approximate incentive check (DFNPR: "novel mechanisms for settings in which the optimal mechanism is unknown"; RegretNet "will generally only find mechanisms that are approximately incentive compatible", p. 3; trap 27); AI doing hedging (BGTW), which is risk management, not invention.
- *Not found in our sources:* an AI-invented *traded* instrument. FSB p. 1: "use cases generating new revenue streams are not widely observed at present", **and** pp. 28–29: "the rapid pace of technological advancements and the growing integration of AI into financial sector use cases could change this in the future" (trap 26: always both halves).
- *Critic:* Poole: "No one has yet seen a chatbot create new ideas" (G1; a 2024 opinion, contestable and dated).
- Our search was limited: absence means "not found", not "does not exist".

**Ladder plan.** New concepts: *LLM agent* (term box + instance Truth Terminal), *closed vocabulary* (instance OQL: the intent becomes one readable line; what the engine can check; limit: whether the *rules* are readable is different from whether the *price* is findable, which is Lens 1). Concepts here are descriptive, not numeric, so rubric 2 asks for instance, mechanism in words, and limits. Worked numbers: only the quoted ones (no invented numbers).

**Widget.** `diagram` "Where the LLM sits" (steps): plain-language intent → LLM (translator) → OQL line (readable by a human) → engine (validates, executes) → trade. Step 4 reveals the edge: "if no checker can read the output, you have a contract 'in form only'" (MIK, with "may"). Config sketched; S4 writes and S6 verifies.

**Units.** B9 (OQL, AI4C, MIK, DFNPR, BGTW), B8 (TT1, TT2), B6, E3, B4, B5, G1, A3 ([2:01]), A1 ([30:24]), G5.
**Traps handled.** 1, 2, 12, 13, 15, 18 (not needed here), 25, 26, 27, 29, 31; 16 (IMF dropped: not cited).

---

## 5. Lens 1 · Information theory · id `lens-info` · (620 words + 160 fold-out)

**Link types (stated at the top).** The counting argument is **same-math** (Shannon, Cover and Thomas). "A price is a short message that hides a long story" (Hayek) is a **metaphor**. "Understanding = short description" is our **structural analogy**.
**Only this lens shows:** novelty is cheap and *explainable* novelty is rare among possible contracts.
**Limit (stated in the section):** rarity among *possible* contracts is not rarity among contracts an optimiser would pick, and a short description does not make a price easy. That gap is Arora's result, which is computational complexity, not information theory.
**Back-link:** post 01 (Shannon's twin, W1, "a good predictor is a good compressor"); Shannon 1948 p. 1: the actual message is "one selected from a set of possible messages"; semantics are "irrelevant to the engineering problem" (C1).

### 5a. Ladder 1: how many contracts, and how many have a short name?
| Step | Content |
|---|---|
| Instance | W1: 4 weather words; a contract pays 0–9 coins for each word, e.g. (rain 5, sun 0, wind 0, snow 5) = "5 if rain or snow". |
| Question | How many contracts are there? How many bits to name one? How many contracts could have a *short* name? |
| Mechanism in words | Each word has 10 choices, so 10 × 10 × 10 × 10. To name one you pick a number from 1 to 10,000, which takes log2 10,000 bits. A description is a string of bits; there are few short strings. |
| Worked numbers | 10^4 = 10,000 contracts (answers g1). log2 10,000 = 13.29 bits. Strings shorter than k bits: 1 + 2 + … + 2^(k−1) = 2^k − 1. k = 6: 63 strings, so at most 63 contracts (a fraction 0.0063). k = 10: 1,023 (0.102). **k = 14: 16,383 > 10,000, so every contract can have a short name: in a 4-word village the squeeze does not bite.** Scale up (the hook): two days = 16 states, 10^16 contracts, 53.15 bits; k = 20 gives at most 1,048,575 names, a fraction 1.05e-10. A pool of 100 loans: 2^100 states. |
| Formula | number of contracts with description shorter than k bits ≤ 2^k − 1 (Cover and Thomas 1991, Thm 7.2.4, p. 150: each program gives one output). |
| Check | Widget `cfg-count` reproduces: k = 6 → 63, 0.0063; k = 10 → 1,023, 0.102; k = 14 → 16,383, "1 (all of them)"; d = 2, k = 20 → 1,048,575, 1.05e-10. |
| What it means | Fewer than 2^k contracts can be described in under k bits; **ours:** mapping contracts to bit strings is our step. Not "AI contracts are random": optimisers pick structured contracts (like "4 per rainy day"). Kolmogorov complexity depends on the computer only up to a constant (p. 151) and is not computable (p. 163): see Rung 1. |

**Widget `cfg-count`** (lab; `widgets/labs.json`): sliders k (1–60) and days d (1–4). Presets: "4 states, k = 6", "4 states, k = 14" (edge case: the argument needs a big world), "two days, k = 20".

### 5b. Ladder 2: why a short rule can still be hard to price
| Step | Content |
|---|---|
| Instance | Akerlof's used cars (C6, p. 489–490, as in Arora p. 2): a working car is worth $1000, 20% are lemons worth $0, so a random car is worth $800 and the **lemon cost** (what a buyer loses to hidden junk) is $200. "The 'bad' cars tend to drive out the good" (9 words). |
| Question | A pool of assets, a short public rule, and a seller who knows which assets are junk. Can the buyer still price it? |
| Mechanism in words | Pool N assets that each pay 1 or 0 with chance 1/2. The seller knows n of them pay 0 (junk). The buyer does not. If the buyer must *find* the junk, they must search subsets. Factoring analogy: 7019 × 5683 = 39,888,977 is easy; going back to the factors is hard. |
| Worked numbers (ours) | N = 100 assets, fair price 50. The seller knows n = 10 are junk, so the honest value is 90 × 1/2 = 45; lemon cost = 50 − 45 = 5 = n/2. The buyer who tries every possible junk set faces C(100, 10) = 17,310,309,456,440 ≈ 1.73 × 10^13 sets (C(100,1) = 100; C(100,2) = 4,950; C(100,5) = 75,287,520). |
| Formula | lemon cost = n/2 in this toy; Arora's general form in Rung 2. |
| Check | 50 − 45 = 5 = n/2. |
| What it means | The authors (working paper, 2009: Arora, Barak, Brunnermeier, Ge) show, under a **conjectured** hardness assumption, in a simple model with independent 0/1 assets, and asymptotically, that derivatives can "amplify the costs of asymmetric information instead of reducing them" (abstract). One main result "suggests that it may be computationally intractable to price derivatives even when buyers know almost all of the relevant information" (p. 1); derivatives "could contain information that is in plain view yet cannot be understood with any foreseeable amount of computational effort" (p. 1); "even Goldman Sachs would have no idea what to pay for it" (p. 3, the factoring derivative). They call it "clearly only a first step" (p. 12). **Not** about incomprehensible *rules*: the rules are short. **Ours:** reading an AI designer as the informed seller. |

**Trap box: two meanings of "complicated"** (trap 3). Harari: a device is complicated when "you need to go over trillions of data points to understand" it (BIS [10:08]): *volume*. Arora et al.: a short contract can have a price that is *computationally hard to find* when the seller knows more. Same word, different problems. Do not merge.

**Hayek paragraph (about 60 words; optional cut).** Prices as "a mechanism for communicating information" with "economy of knowledge" (§ VI; cite sections only); a price is a short message that hides a long story (**metaphor**, "compression" is ours); what happens when the price belongs to a contract nobody can read? Hayek's own hedge: it works "less perfectly as prices grow more rigid".

**Widget for 5b.** `diagram` "Informed seller" (steps): seller (knows the 10 junk assets) → pool of 100 → buyer ("which 10?" with the number 1.73 × 10^13) → price. Step 3 reveals "the seller can hide junk in a few pools (about √D over-representation)" only if S4 wants it; otherwise stop at step 3. Config sketched; S4 writes.

### 5c. Fold-out · "Look inside: a contract built to resist tampering" (160 words)
Arora et al. p. 12: a "tree of majorities" (majority of 3, applied again and again, depth k, 3^k inputs) "cannot be influenced by o(2^k)" of its inputs, so tampering can be detected after the fact and a clause could demand "a sizeable payment from seller to buyer". Toy numbers (ours, checked by code): depth 1: 3 inputs, 2 flips needed; depth 2: 9 inputs, 4 flips (44%); depth 3: 27 inputs, 8 flips (30%); depth 4: 81 inputs, 16 flips (20%). Small `diagram`: the 13-node tree for depth 2 with the 4 leaves to flip highlighted. Authors' caution: a "positive result ... in the simplified setup"; the XOR of all inputs resists tampering but "it's not clear that this function will be of economic use, as it's not monotone". Feeds Lens 2's third lever (by our analogy).

**Units.** C1, C2, C3, C4 (fold-out), C5 (optional), C6, A1 ([10:08]), G2 (one clause in the synthesis, not here).
**Traps handled.** 3, 9, 17, 22, plus the "rarity is not opacity" meta-manager edit 3.

---

## 6. Lens 2 · Control and cybernetics · id `lens-control` · (420 words)

**Link types.** Variety and entropy: **same-math** (Ashby, S.11/6–11/10, pp. 206–209). Regulator = financial supervisor: **structural analogy** (ours).
**Only this lens shows:** control needs variety. Three levers, not two.
**Limit:** Ashby's table has a passive disturbance; finance adapts to its regulator (ours). The law is silent on who regulates the regulator.
**Back-link:** the entropy language of post 01. **Forward link:** the control-theory field (feedback, requisite variety) when it gets its own post.

### Ladder: the law of requisite variety
| Step | Content |
|---|---|
| Instance | Four kinds of new contract arrive (D1–D4). The supervisor (regulator R) has two checks (R1, R2). The outcome is the state of the books: a, b, c or d. Table (Ashby's style, toy, ours): D1: R1→a, R2→b; D2: R1→b, R2→a; D3: R1→c, R2→d; D4: R1→d, R2→c. |
| Question | The supervisor sees the contract type and picks a check. How few different outcomes can they force? |
| Mechanism in words | Each outcome appears at most once in each column, so one check can send only one contract type to "a". With two checks, the best play sends D1 and D2 to a and D3 and D4 to c: two outcomes. |
| Worked numbers | Variety = log2 of the count. V_D = log2 4 = 2 bits; V_R = log2 2 = 1 bit; least V_O = log2 2 = 1 bit (brute force over all 16 policies gives 2 outcomes). With contracts from the village: V_D = 13.29 bits (10^4 types), V_R = 4 bits → V_O ≥ 9.29 bits. |
| Formula | V_O ≥ V_D − V_R. Ashby: "only variety in R can force down the variety due to D; variety can destroy variety" (p. 207, 16 words). |
| Check | Stepper note 5: "2 − 1 = 1 bit, equals the table". Lab: c = 4, V_R = 4 → 9.29; c = 2, V_R = 4 → 2.64; c = 4, V_R = 9 → 4.29; c = 2, V_R = 9 → 0.00 (floor). |
| What it means | A lower bound for a fixed table ("a statement about possible arrangements in a rectangular table"; "The law therefore owes nothing to experiment", pp. 208–209). It does not say regulators fail; it says what they would need. |

**Ashby's three levers (S.13/4, p. 246) and our mapping (labelled ours).**
1. *Lower the standard* of acceptable outcomes ("a somewhat trivial solution", Ashby): accept more failures.
2. *Raise the scope and power of R:* AI supervisors. Danielsson and Uthemann (2025, abstract) propose that authorities build their own AI, use direct AI-to-AI communication, automated crisis facilities, and monitor AI use. Danielsson et al. (2017, pp. 10–11) warn about trusting the authorities' own engine: "we might come to the point where neither its understanding of the economic system, nor possibly even its internal data representations, will be intelligible to its human operators" (p. 11; always print the opening hedge, and add their "This might not necessarily be the case" if "Minsky moment" is mentioned).
3. *Find a constraint* (S.13/5, p. 247): the real variety of D may be much lower because components are not independent. Quote with its condition: "if R's capacity is not easily increased and the other methods are not possible, then ... the discovery of a constraint is the would-be regulator's only hope". Our mapping: **standardised contract menus** cut V_D: from 10^4 types to 10^2 lowers it by 13.29 − 6.64 = 6.64 bits (toy). Arora's tree-of-majorities (fold-out in Lens 1) is a design restriction of this kind.
- **Cross-lens note (feeds the synthesis):** the correlation that makes banks fail together (Lens 3) is also a *constraint* in Ashby's sense: if all banks follow one model, the supervisor has fewer independent disturbances to cover. Same fact, opposite sign for stability vs control (ours).

**Counterweights (one sentence each).** FSB p. 2: "existing financial policy frameworks address many of the vulnerabilities ... more work may be needed". Danielsson and Uthemann: "Current regulatory frameworks cannot effectively prevent and resolve such AI-induced crises" (trap: do not call the 2025 paper "more cautious"). Narayanan and Kapoor: "control is primarily in the hands of people and organizations"; human review often "devolves into the human acting as a rubber stamp".

**Trap box: a misprint in the reprint** (trap 23). The entropy form is in Rung 3. Ashby p. 208 (reprint) prints "H_D(E)" in one line where the derivation requires "H_D(R)"; we write the corrected bound and say so.

**Widgets.**
- `stepper` `widgets/ashby-stepper.json` (verified, parsed): 5 rows, walk through the table. Brute-force minimum = 2 outcomes (code-checked).
- `lab` `cfg-ashby` (verified): sliders c (0–4, step 0.5; contract types = 10^c) and V_R (0–14). Presets: "free market: 10^4", "standard menu: 10^2", "AI supervisor +5 bits". Edge case: when V_R ≥ V_D the bound is 0, not negative: more regulator variety than needed buys nothing.

**Units.** D1, D2, C4 (fold-out link), E1 (pp. 3, 10–11), E2, B6 (p. 2), G3.
**Traps handled.** 7, 23, "only hope" without condition (s2-check 8), "Ashby offers three levers" (D2 careful).

---

## 7. Lens 3 · Decision, game theory and one Bayesian step · id `lens-decision` · (800 words)

**Link types.** N_eff and the odds form of Bayes: **same-math**. Keynes's beauty contest ↔ post 01's Lens 5 (people reasoning about what others think): **structural analogy**. Morris–Shin ↔ markets and "one model = a public signal": **structural analogy** (ours). Granovetter thresholds ↔ bank cascades: **structural analogy** (ours).
**Only this lens shows:** failure needs no error, only correlation. If ten banks use one model, their mistakes coincide.
**Limit:** stylised toys. They say nothing about how widely LLMs are used (stated aloud, trap 19). The FSB also says AI could *reduce* correlations if it enables "truly customised" strategies.
**Back-link:** post 01's W4 (Bayesian prompt): same arithmetic, new story.

### 7a. Why would banks use the same model? (about 90 words)
Keynes, *General Theory* ch. 12, § IV (standard numbering; cite by section): we "fall back on what is, in truth, a convention"; § V: "Worldly wisdom teaches that it is better for reputation to fail conventionally than to succeed unconventionally" (16 words); the beauty contest: "We have reached the third degree where we devote our intelligences to anticipating what average opinion expects the average opinion to be". Keynes says the behaviour "is not the outcome of a wrong-headed propensity". So a common tool is individually sensible (ours: a shared model plays "average opinion"). FSB p. 20 lists four drivers: herding, network externalities, limited choice, lack of transparency. Morris and Shin (p. 1522): "Agents overreact to public information" without any irrationality (one sentence; conditions: r > 0.5 and precise private information; the "public signal" analogy is ours).

### 7b. Ladder 1: the effective number of opinions
| Step | Content |
|---|---|
| Instance | Ten banks each run a risk model that is wrong on 1% of days (g2). |
| Question | How often are all ten wrong on the same day? |
| Mechanism in words | If errors are independent, you multiply: 0.01 ten times. If all ten run one model, there is one error, shared. Real life lies between: a **shared part** of each error never averages away. |
| Worked numbers | Independent: 0.01^10 = 10^-20. Same model: about 1%. For the *average* of N forecasts with pairwise correlation ρ the variance is σ²[1 + (N−1)ρ]/N, so the average is as steady as N_eff independent forecasts: N = 10: ρ = 0 → 10; ρ = 0.3 → 2.703; ρ = 0.9 → 1.099; ρ = 1 → 1. |
| Formula | N_eff = N / (1 + (N − 1) ρ). Ceiling for a huge crowd: 1/ρ (N = 100, ρ = 0.3 → 3.257; limit 3.33). |
| Check by hand | N = 2, ρ = 0.5: 2 / (1 + 0.5) = 1.33. Directly: Var of the mean of two = σ²(1 + 0.5)/2 = 0.75σ² = σ²/1.33. ✓ |
| What it means | Adding the 11th bank that uses the same model adds almost nothing. Real-world shape: FSB p. 21, "as if it were a single institution"; FCIC p. 149, securities that "weren't that different"; Danielsson et al. p. 10, "Increased homogeneity in beliefs and actions amplifies systemic risk". Limits: equal ρ for all pairs; says nothing about actual adoption. |

**Widget `cfg-neff`** (lab, verified): sliders N (2–100), ρ (0–1). Presets: independent, 0.3, "one model" (ρ = 1), "huge crowd, 0.3" (edge: 100 banks give only 3.257). Readout also shows the 10^-20 versus 1% contrast.

### 7c. Ladder 2: counting one signal many times (Bayes, odds form)
| Step | Content |
|---|---|
| Instance | A risk officer hears ten models say "safe". Prior 1/2. A safe bank is 4 times as likely to get this verdict as a risky one (toy, reuse of W4 arithmetic: 0.2 against 0.05). |
| Question | How confident should the officer be? |
| Mechanism in words | Independent evidence multiplies the odds each time. A repeated copy of the same evidence is not new evidence. |
| Worked numbers | Counted n times: odds 4^n. n = 0..4: P(safe) = 0.5, 0.8, 0.941, 0.985, 0.996. n = 10: odds 1,048,576, P = 0.999999. One shared source counted once: 0.8. |
| Formula | posterior odds = prior odds × LR^n; P = odds / (1 + odds). |
| Check | n = 1: 4/(4+1) = 0.8; widget `cfg-bayes2` n = 1 → 0.800000; n = 4 → 0.996109. |
| What it means | False confidence from ten copies of one voice. This ties to Harari's pattern "it generates a lot of trust" (BIS [10:27] context): the link is **ours**, not his. LR = 4 is invented. |

**Widget `cfg-bayes2`** (lab, verified): slider n (0–10). Presets: one model, 4 copies, 10 copies.

### 7d. Ladder 3: why three at once is different (cascade, W5)
| Step | Content |
|---|---|
| Instance | Six banks (W5). X1, X2, X3 run one model; Y1, Y2, Y3 do not. Capital (buffer): 10, 10, 10, 10, 9, 11. Lenders and exposure: Y1 has lent 5 to each X bank; Y2 lent 5 to X3 and 10 to Y1; Y3 lent 5 to Y1 and 10 to Y2. A failed borrower repays only 20%: loss = 0.8 × exposure. |
| Question | If one bank fails, does it spread? And if the three X banks fail on the same day? |
| Mechanism in words | A bank fails when the losses from failed borrowers reach its capital. Rounds: first the shock, then each newly failed bank hits its lenders. |
| Worked numbers | One X bank fails: Y1 loses 4 of 10. Contained. Any one of the six: contained (1 of 6). Two X banks: Y1 loses 8 of 10. Contained (2 of 6). All three: Y1 loses 12 ≥ 10 and fails in round 1; Y2 loses 4 (from X3) + 8 (from Y1) = 12 ≥ 9 in round 2; Y3 loses 4 + 8 = 12 ≥ 11 in round 3. Six of six. With capital × 1.5: Y1 loses 12 < 15: stops at 3 of 6. |
| Formula | bank j fails when Σ over failed lenders i of λ · w_ij ≥ κ · capital_j (λ = loss given default, κ = capital multiplier). |
| Check | Widget `cfg-w5`: seed X1 → "1 of 6 banks fail"; seeds X1, X2, X3 → "6 of 6, 3 more rounds"; same with capital ×1.5 → "3 of 6". (Full readouts in section 10.) |
| What it means | The cascade needed *all three* at once: two is safe, three is not (a threshold). Granovetter (1978, p. 1425): replace one person (threshold 1 by 2) and 100 rioters become 1, though "the two crowds are essentially identical": the *distribution*, not the average, decides. The FSB's synchronous "kill switches" have the same shape (p. 21, structural analogy, ours). Limits: toy network; capital is fixed; in reality capital choices and exposures adapt. |

**Widget in 7d.** `stepper` `widgets/w5-hand-stepper.json` (verified, parsed): 4 rows (round 0–3) with losses/capital for Y1, Y2, Y3 and the new failures. The full interactive `cascade` is in section 10.

### 7e. Ladder 4: a share m on one model (feedback; toy "ours")
| Step | Content |
|---|---|
| Instance | A market gap from fair value (0 = fair). A share m of traders follow the one model, which chases the last move. The rest pull the gap back toward 0. Shock −1 after step 3. |
| Question | For which m does the shock fade, and for which does it grow? |
| Mechanism in words | New gap = old gap + trend-chasers' push (1.5 × m × last move) − value-buyers' pull (0.5 × (1−m) × old gap). |
| Worked numbers | m = 0.2: −1 → −0.9 → −0.51 → −0.189 …; by hand: −1 + 0.3 × (−1) − 0.4 × (−1) = −0.9; −0.9 + 0.3 × 0.1 − 0.4 × (−0.9) = −0.51. |
| Formula | gap(t+1) = gap(t) + A·m·[gap(t) − gap(t−1)] − G·(1−m)·gap(t), A = 1.5, G = 0.5. The shock dies out if A·m < 1 and does not if A·m > 1: tipping at m = 1/A = 2/3 (derivation: Rung 5). |
| Check | Widget `cfg-herding`: m = 0.2 → largest swing 0.04 up, −1.00 down, gap after 40 steps 0.000; m = 0.67 → ±2.7 and no decay; m = 0.9 → 1345.97 up. |
| What it means | The label matters: this models *trend-following* by a share m on one model. Shared models do not by themselves imply trend-following (meta-manager edit 2). The toy shows the correlation-and-amplification channel only. Real anchors: Danielsson et al. p. 10; KKST footnote 1 ("unrelated trading algorithms ... can cascade into a systemic event"); the five-second pause (B2). A circuit breaker (cap on the gap) bounds the swing but, in the toy, does not remove the oscillation: m = 0.9 with breaker 3 gives ±3.00 for good. Toy, ours; does not measure real adoption. |

**Optional bridge sentence (collusion fold-out).** "The same class of programs" (Calvano p. 3296) as a hook to the shared-model theme.

**Units.** E4 (Keynes §§ III–V), E5 (Morris–Shin p. 1522), E6 (Granovetter pp. 1425, 1427–1428), E8 (all four ladders), E1 (p. 10), E3 (secondary), B6 (pp. 20–21), B1 (p. 149), B2 (fn 1), B3 (p. 3296).
**Traps handled.** 15 (Keynes: cite by section; Keynes § IV note), 19, 14, "E3 not the paper", "Minsky not used".

---

## 8. Lens 4 · Social reality, accountability, personhood · id `lens-social` · (330 words)

**Purpose (meta-manager edit 4).** Carry Kunhao's actual question: what do human-centred institutions rely on? Three supports, compactly: **acceptance**, **accountability**, **legal personhood**.
**Link types.** Conceptual analysis; no math. Searle's status functions ↔ post 01's Lens 4 (meaning and reference): **structural analogy**. Dennett's intentional stance ↔ post 01's Lens 5 (theory of mind): **metaphor** when applied to legal personhood.
**Only this lens shows:** "taking over money" splits in two: an AI can *write* contracts, but money is an *institutional status* that needs a community.
**Limit:** not empirical. We have no court or statute sources on AI legal personhood, so the post does not state the legal position (F5). Searle's own books are not yet in the library (SEP only).

### 8a. Acceptance (ladder for the status function)
| Step | Content |
|---|---|
| Instance | A line of stones counts as a border wall in a village; a piece of paper from the Bureau of Engraving and Printing counts as money in the US (SEP § 4.2.3). |
| Question | What turns stones or paper into a wall or money? |
| Mechanism in words | People collectively accept that the thing has a function it does not have by nature. The function brings **deontic powers**: rights, permissions and duties. |
| Pattern | "X counts as Y in C" (5 words; Searle via SEP): X a thing, Y a status, C a context. |
| Check (apply it) | X = a token an AI minted; C = a community; no accepting community, no money. |
| What it means / limits | The disagreement is named, not hidden: Menger says money can emerge from trading practice with no one choosing it (SEP § 5.6); recent work debates how central acceptance is. "Code is law" is not Searle's view; a smart contract is a status declaration only if a community accepts it (our caution). Harari's own bridge: "What gives money value is the stories that bankers, finance ministers and cryptocurrency gurus tell us about it" (A5). |

### 8b. Accountability (Lupia and McCubbins)
- Theorem 5.1 (pp. 85–86): delegation succeeds if both the **knowledge** condition (the principal can tell whether the agent's proposal is better or worse than the status quo) and the **incentive** condition hold; if neither holds, it fails; with only one, the worst case is the status quo. Under the tougher definition, failing either condition suffices (Thm 5.1′, p. 92). Institutions supply "verification or a penalty for lying" (p. 207).
- Worked instance (a 2 × 2 table, ours): knowledge yes/no × incentive yes/no. Skingsley's airplane: knowledge via third-party verification, incentives via penalties: succeeds. An agent that "consistently hides the genuine reasons" (Scheurer): the knowledge condition fails. An opaque instrument removes the knowledge condition (ours). MIT Sloan (as reported): AI "can easily mask who's at fault".
- Reply to "we trust planes we don't understand" (G4): flight rules are not adaptive against the rules; finance is (ours).

### 8c. Personhood
- He said (WEF [16:28], 15 words): "They will soon be able to make the decisions necessary to manage a bank account". Then the question: will your country recognise AIs as legal persons? Corporations already are (WEF [14:38–16:51]). It is a **policy question with a deadline** ([19:11]), not a forecast.
- Dennett: the decision to adopt the intentional stance is free, but its success "perfectly objective" (p. 24). Treating a trading agent as an agent often predicts it; whether the *law* should is a different question.
- Truth Terminal: money and liability ran to people (donor, handler, creator).

**Widget.** `diagram` "X counts as Y in C" (steps): token X → community C accepts → counts as money Y → "who pays if it fails?" with dashed arrows to "people: donor, handler, creator". Edge case in step 2: remove C and Y disappears.

**Units.** F1, F3, F4, F5, A3 ([14:38–19:23]), A5, E3, B5, B8, G4.
**Traps handled.** F5 careful (no legal position), F1 careful (Searle vs Menger), 8 (SEP not Searle), "code is law".

---

## 9. The math ladder · id `ladder` · "Five rungs up" (500 words)

**Format.** Five rungs, about 100 words each, each in the ladder order (instance already seen → question → mechanism → numbers → formula → check → what it means). Each starts "In section X we used ...". Numbers rerun.

| Rung | Starts from | New idea | Numbers and check | Limits |
|---|---|---|---|---|
| 1. Description length | the 63 short names (k = 6) | Kolmogorov complexity K(x): length of the shortest program that prints x on a fixed computer; fewer than 2^k strings have K < k (Cover and Thomas, 1991 ed., Thm 7.2.4) | 2^6 − 1 = 63 (widget). | depends on the machine up to an additive constant (p. 151); not computable (p. 163); rarity ≠ opacity |
| 2. Lemon cost | n/2 = 5 | Arora's Δ(n) = E[F(X)] − min over sets S with \|S\| = n of E[F(X) \| X_i = 0 for all i in S]; F = total payoff | N = 100, n = 10: E[F] = 50, minimum conditional 45, Δ = 5 = n/2 ✓ | the minimum is over C(100,10) sets: that is the hard part; conjectured assumption, simple model, asymptotic; Table 1 only in words: for a binary CDO the lemon cost is **much larger than n** for a buyer limited to polynomial time, and much smaller than n for exponential time (use the brief's wording; no other Arora formula) |
| 3. Entropy form of Ashby | V_O ≥ V_D − V_R (counts) | with probabilities: H(E) ≥ H(D) + H(R \| D) − H(R) (Ashby p. 208 writes H_D(R), and the reprint misprints H_D(E)); uses H(E) ≥ H(E \| R) (conditioning cannot raise entropy; standard fact) | W1: H(D) = 1.75; R a function of D with 1 bit: H(R\|D) = 0 → H(E) ≥ 1.75 − 1 = 0.75 bits. Equality case "R is a determinate function of D" (p. 208) | the sign is ≥; passive disturbance; W1 has unequal probabilities, so 1.75, not 2 |
| 4. Effective sample size | N_eff = N / (1 + (N−1)ρ) | derivation: Var(mean) = (1/N²)[Nσ² + N(N−1)ρσ²] = σ²[1 + (N−1)ρ]/N; set equal to σ²/N_eff. Exercise: do N = 2 | N = 10, ρ = 0.9: 1 + 9 × 0.9 = 9.1; 10/9.1 = 1.099 ✓ | equal pairwise ρ; variance of an average, not a probability of joint failure |
| 5. Feedback gain | gap steps at m = 0.2 | two-step linear recursion gap(t+1) = b·gap(t) − c·gap(t−1) with b = 1 + A·m − G·(1−m), c = A·m; the characteristic equation x² − b·x + c = 0 has roots whose product is c; when the roots are complex, each has size √c per step: the swing shrinks if A·m < 1 and grows if A·m > 1 | m = 0.2: b = 0.9, c = 0.3, size √0.3 = 0.548; m = 0.67: c = 1.005, size 1.002; m = 0.9: b = 2.3, c = 1.35, size 1.162 (code-checked with numpy.roots); tipping m = 1/1.5 = 2/3 ✓ matches widgets | holds while the roots stay complex (true for these three m); a breaker (clamp) makes the system nonlinear |

**Optional rung 6 (cut if long).** Granovetter's r(t+1) = F[r(t)] (p. 1425); equilibrium where r(t+1) = r(t); thresholds 0..99 → 100; swap 1 for 2 → 1; normal thresholds, mean 25: 4.0 at sd 12.0, 5.5 at 12.2, 100 at 12.3 (rerun values, E6). Becomes Exercise 4 in "Your turn" if cut here.

**Units.** C2, C3, D1, E8, E6 (optional).
**Widget.** None new; each rung points back to its widget by name only after stating the numbers itself (no dependency).

---

## 10. Playground · id `play` · (200 words)

**Purpose.** Two flagship interactives, each with three tasks (predict, try, explain). Both configs are verified.

### 10a. `cascade` W5: `widgets/w5-cascade.json`
Sliders: lgd (0.2–1, default 0.8), capMult (0.5–2, default 1). Presets: "normal", "capital ×1.5", "harsh losses (lgd 1)". Reader taps banks to seed failures.

Verified readouts (from `check-output.txt`):
- seed X1: "1 of 6 banks fail, 5 survive (loss given default 0.80, capital ×1.00). Spread after the shock: 0 more rounds." Same for X2, X3, Y1, Y2, Y3.
- seeds X1, X2 (any two X): "2 of 6 banks fail, 4 survive ... 0 more rounds."
- seeds X1, X2, X3: "6 of 6 banks fail, 0 survive (loss given default 0.80, capital ×1.00). Spread after the shock: 3 more rounds." (Y1 round 1, Y2 round 2, Y3 round 3.)
- seeds X1, X2, X3 with capMult 1.5: "3 of 6 banks fail, 3 survive (loss given default 0.80, capital ×1.50). Spread after the shock: 0 more rounds."
- Boundaries: capMult 1.2 → 5 of 6 fail; capMult 1.25 → 3 of 6 (the cascade stops once Y1's buffer exceeds its loss of 12, i.e. κ > 1.2).
- Edge case (harsh losses, lgd 1): Y1 alone now fails and drags two more (3 of 6, 2 more rounds); X1 + X2 now cause 5 of 6 (3 more rounds).

Tasks: (1) predict which single bank can start a spread (none at lgd 0.8; Y1 at lgd 1). (2) Find the *smallest* group of X banks that brings down all six (all three at lgd 0.8; two at lgd 1). (3) Find the capital multiplier that stops three (just above 1.2); then explain why more capital helps (Lens 3) and what it costs (ours: not modelled).

### 10b. `iterate` herding: `widgets/herding.json` ("toy, ours")
Sliders: m (0–1, default 0.2), circuit breaker (0 = off, up to 10). Presets: "calm (m = 0.20)", "tipping (m = 0.67)", "runaway (m = 0.90)", "runaway + breaker 3". The y axis auto-scales so the m = 0.9 blow-up is visible.

Verified readouts:
- m = 0.2: "Largest swing 0.04 up, -1.00 down; gap after 40 steps: 0.000."
- m = 0.67: "Largest swing 2.68 up, -2.70 down; gap after 40 steps: -0.505."
- m = 0.9: "Largest swing 1345.97 up, -50.21 down; gap after 40 steps: 1345.969."
- m = 0.9, breaker 3: "Largest swing 3.00 up, -3.00 down; gap after 40 steps: -2.505."

Tasks: (1) find the m where the shock stops dying (about 0.67); (2) at m = 0.9 add the breaker: it caps the damage, the feedback remains; (3) compare with the Flash Crash pause (B2).

**Phone check (README rule 4).** W5: 6 nodes, labels of 2 characters, 2 sliders. Herding: 2 sliders. All other labs have ≤ 2 sliders.

---

## 11. Your turn · id `turn` · (260 words)

Notebook in `notebook/` (Python, runs on Kunhao's computer; style of post 01's `ex1_...py`).
- **Exercise 1 · `ex1_neff.py` · How many independent agents do I really have?** Simulate N forecasters whose errors share a common component (weight √ρ). Estimate the pairwise correlation from 1,000 draws, compute N_eff and compare with σ²/Var(average). Then try your own data: 5 prompts of one LLM labelling 200 posts. Prediction first: what is ρ, and what is N_eff?
- **Exercise 2 · `ex2_cascade.py` · W5 in 20 lines.** Implement the cascade rule and reproduce 1/6, 2/6, 6/6, 3/6. Then draw 200 random networks (30 banks) and compare mean cascade size when one random bank fails with when a random triple fails together; find the capital multiplier that halves the triple's mean cascade (labelled ours).
- **Exercise 3 · `ex3_herding.py` · Where does it tip?** Use `numpy.roots` to reproduce the sizes √(A·m) (0.548, 1.002, 1.162) and plot the size against m. Add a clamp and measure how long swings last. Vary G: does the tipping point move?
- **Exercise 4 (if Rung 6 is cut) · Granovetter's riot.** 100 people with thresholds 0..99 end with 100 rioters; swap threshold 1 for 2 and you get 1.
- **Transfer challenge.** Take one public claim from your field (e.g. a prediction about LLMs and misinformation). Rewrite it in three layers: *He/She said* (quote, date, venue), *The evidence*, *Our reading*. Name the single measurement that would change your mind.

**Units.** E8, E6, ladder rungs 4–6; none new.

---

## 12. Where this shows up in your work · id `work` · (260 words)

Cards as in post 01 (`cards3`), five cards, each "tie-in + one action":
1. **Computation · social simulation with LLM agents.** Agents from one base model are correlated by construction. Compute N_eff for your agents' decisions; add persona or model diversity and see how N_eff moves (Exercise 1). Question, not a claim: does a population of such agents amplify shocks the way the herding toy does?
2. **Computation · LLM surrogate labeling.** A majority vote of five prompts to one model is not five annotators: it is closer to one, plus noise. Report N_eff next to agreement. Bayes double-count (7c) applies to your confidence.
3. **Computation · cross-lingual LLM safety.** Question: are a model's errors across languages as correlated as its errors across prompts? If yes, a multilingual test set may hold fewer independent checks than it seems.
4. **Communication · crisis and risk communication.** "Something goes wrong and nobody knows why" (BIS [10:27]) is a communication problem before it is a technical one: what does an official say when no expert can explain? Link to trust (Akerlof's conclusion: "trust" is important, p. 500; Skingsley's "no further AI without further trust") and to Harari's thesis that money rests on shared stories (A5). The link between those is ours.
5. **Collaboration · who invents and who checks.** Fox's remark that capitalism "is hardly mentioned at all" (G2) is a prompt: opacity can be a business choice (Arora's informed seller, ours). Research question, no source: in open communities that build financial tools, who can check an invented instrument?

**Units.** E8, B4, A1, A5, C6, G2, G4, F4. (No Shiller, no DeFi facts: not in the brief.)

---

## 13. So what happens? · id `answer` · "Layers, conditionals and our reading" (500 words)

**Four layers, certain to contested (as in post 01's `ol.layers`):**
1. **The contract space is huge** (certain, same-math). 10^4 for the small village; more in real worlds. Short descriptions are rare among *possible* contracts (not among chosen ones).
2. **Opacity favours the better-informed side** (supported in theory, with named conditions). Akerlof; Arora et al. (conjectured hardness, simple model, "only a first step"). The FCIC records both unclear securities and a nameable error.
3. **A shared model correlates failures** (supported by toys and regulators' reports, not measured for LLMs). N_eff, double counting, cascades, feedback. FSB: "could".
4. **Whether this changes who rules** (contested). Depends on acceptance, liability and personhood rules. Skingsley, Lupia, Narayanan and Kapoor on one side; Harari's WEF question on the other.

**Cross-lens tension (ours):** correlation makes simultaneous failure likelier (Lens 3) but lowers the variety a supervisor must cover (Lens 2, Ashby's constraint). Rarity of explainable contracts (Lens 1) is not opacity (Arora). So the lenses disagree about what is *dangerous* about shared models, which is why they are lenses.

**Conditionals** (If A, then B, provided C), five lines:
- If an AI designs instruments by optimising payoffs, and a seller knows more than a buyer, then pricing can become hard (Arora; under a conjectured assumption).
- If many firms run one model, then their errors coincide and diversification shrinks (N_eff; FSB p. 21).
- If supervisors cannot raise their own variety or cut the contract menu, then Ashby's bound says outcomes stay varied.
- If verification and penalties exist, delegation can succeed without understanding (Lupia; Skingsley); if not, the knowledge condition fails.
- If a community accepts an AI-run entity's tokens and the law makes a human liable, then money's status survives; if either fails, it does not (ours).

**Critics, one line each (what each would say, what it would change):** Poole (no chatbot has created new ideas yet; the invention step is the weak link); Narayanan and Kapoor ("decades"; control "primarily in the hands of people and organizations"; this slows everything, though they note rubber-stamp risk); FSB (existing frameworks cover much; but "could change this in the future"); Skingsley (we trust what we cannot understand; institutions); Fox (profit is the missing driver, ours).

**Our reading (labelled "ours"; no numeric probabilities).**
- Weakest link in Harari's chain: step (a), AI-*invented* instruments, is not evidenced yet (FSB pp. 28–29 with its continuation; our searches were limited).
- Best-supported links: correlation of errors across firms using shared models, and the difficulty of delegating to an agent that hides its reasons.
- Therefore the near-term risk we find most plausible is **correlated, opaque use of ordinary instruments and agents**, not an alien instrument. This is our judgment, not a finding.
- **Signs to watch** (what would raise or lower our reading):
  1. *Up:* a reported traded instrument whose payoff rule its own issuer's staff cannot state in a page (FSB's sentence turns past tense). *Down:* only translators inside fixed vocabularies keep appearing.
  2. *Up:* evidence that a few base models underpin most AI-assisted desks and that their errors correlate (measure ρ). *Down:* evidence of customised strategies that reduce correlation (FSB p. 21).
  3. *Up:* authorities lag in building their own AI and AI-to-AI channels (Danielsson and Uthemann's proposals). *Down:* standard contract menus and trading pauses spread.
  4. *Up:* a jurisdiction lets an AI hold accounts without a responsible human (Harari's WEF deadline). *Down:* liability stays with identifiable people (as in Truth Terminal's case).
  5. *Up:* agent incident reports show hidden reasoning (Scheurer-type behaviour in the wild). *Down:* verification and penalty schemes for agents.

**Back-links.** Post 01: Shannon, W1, W4. The lenses all ask what information an actor has and who can check it.

**Units.** G5 (the tension table), A1, A3, A4 (hedges), B6, G1, G3, G4, G2, F4, E8, C3, D1/D2, B1.

---

## 14. Recall · id `recall` · 7 questions (180 words; answers collapsed)

↻ marks questions that return later (spaced review, mixed with post 01).
1. ↻ A contract pays 0–9 for each of 4 weather words. How many contracts exist, and how many bits to name one? (10,000; 13.29)
2. Why do fewer than 2^k contracts have a description shorter than k bits? (2^k − 1 strings; one output per program.) When does the argument fail? (k ≥ 14 in the 4-word village.)
3. Say Ashby's law in one sentence and name his three levers. (V_O ≥ V_D − V_R; lower the standard, raise R, find a constraint.)
4. ↻ N = 10 banks, ρ = 0.9: what is N_eff, and what does it mean? (1.099: about one independent opinion.)
5. Harari's "complicated" versus Arora et al.'s: what is the difference? (data volume vs hard to price with an informed seller.)
6. ↻ (post 01) The entropy of the 4-word weather village? (1.75 bits.) And here: why is it in Ashby's bound? (H(D) = 1.75, so H(E) ≥ 0.75 with a 1-bit regulator.)
7. What decides whether an AI-minted token is money? ("X counts as Y in C": acceptance; Menger and Searle differ on how.)

---

## 15. How to say it in English · id `english` · (560 words)

Two layers (WRITING §8), plus a looped paragraph (`c1-loop` chapter).

**Layer (a) · ten phrases from the topic (B2–C1).** Each example uses an idea from this post.
1. **opaque / opacity**: "An instrument can be *opaque* even when its rules are short."
2. **to be exposed to**: "Y1 is *exposed to* all three X banks."
3. **a single point of failure**: "One shared model can become *a single point of failure*."
4. **in lockstep**: "Models trained on the same data may move *in lockstep*." (Gensler and Bailey, as reported.)
5. **to amplify / to dampen**: "Trend-followers *amplify* a shock; value-buyers *dampen* it."
6. **a feedback loop**: "The more traders follow the model, the stronger the *feedback loop*."
7. **a tipping point**: "In the toy, m = 2/3 is *a tipping point*."
8. **a circuit breaker**: "A *circuit breaker* pauses trading but does not fix the loop."
9. **to rubber-stamp**: "Human review can turn into *rubber-stamping*." (Narayanan and Kapoor)
10. **to be on the hook for**: "Who is *on the hook for* an AI-run firm that fails?"

**Layer (b) · B2 → C1 toolkit.** New this post (6): **provided that / as long as / unless** (conditionals), **to conflate X with Y** ("Don't *conflate* Harari's 'complicated' with Arora's"), **it stands to reason that**, **what remains to be seen is whether**, **with the caveat that**, **by no means** ("Rarity is *by no means* the same as opacity").
Repeated from post 01 (3, for spaced review): **that's a big if** ("Everyone using one model? *That's a big if*."), **to cut both ways** ("Correlation *cuts both ways*: it raises joint failure and lowers the variety to supervise."), **to read too much into something** ("Don't *read too much into* a thought experiment.").

**Two sentence patterns.**
- *Reporting verbs by commitment.* Harari *imagines*, *supposes*, *asks what happens if*, *warns*; he does not *predict* or *assert* in our sources. Pick the verb that matches the speech act.
- *Three-layer frame:* "He said X (venue, date). The evidence shows Y. Our reading is Z." And the conditional frame: "If A, then B, provided that C."

**Error fixes for Chinese and Japanese speakers (3).** (1) No *will* in an if-clause: "if the models fail" (not "will fail"). (2) *Evidence*, *information*, *advice* are uncountable: "some evidence", "a piece of evidence" (not "evidences"). (3) Abstract nouns take no article in general statements: "finance", "money", but "*the* financial system".

**Practice routine (3 steps).** Pick a headline about AI and markets. Say it aloud in three sentences (He said / The evidence / Our reading). Record it and replay it next to the loop paragraph.

**Loop paragraph (c1-loop, about 130 words).** A summary talk of the post using eleven of the expressions above, in the style of post 01's `loop-para`. Draft key lines: "*What remains to be seen is whether* an AI can invent an instrument at all ... *Provided that* many firms run one model, *a single point of failure* appears ... Rarity is *by no means* opacity ... *That's a big if* ... the argument *cuts both ways* ..."

`english-gloss.json`: 10 + 9 entries + 2 patterns + 3 error fixes, same schema as post 01 (partOfSpeech, level, definition, register; "wrong"/"right" for fixes).

---

## 16. Sources · id `sources`

Every key below maps to a `<li id="src-key">`; cite regexes in post.json. Keys and the brief units they cover:

| key | source | unit |
|---|---|---|
| harari-bis | Harari and Skingsley, BIS Innovation Summit, 7 May 2024 (audio) | A1, G4 |
| harari-wef | Harari, WEF Davos, Jan 2026 (audio) | A3, F5 |
| guardian-2023 | Milmo, Guardian, 9 Nov 2023 | A2 |
| nexus | *Nexus* (2024), paperback sample; Guardian extract, 24 Aug 2024 | A4 |
| ynet-2023 | Harari, Ynetnews, 7 May 2023 | A5 |
| fcic | Financial Crisis Inquiry Report, 2011 | B1 |
| kkst | Kirilenko, Kyle, Samadi, Tuzun, working paper, 2014 | B2 |
| calvano | Calvano et al., AER 110(10), 2020 | B3 |
| llt | Lopez-Lira and Tang, arXiv 2304.07619v6 | B4 |
| scheurer | Scheurer, Balesni, Hobbhahn, arXiv 2311.07590v4 | B5 |
| fsb | FSB, Nov 2024 (P14112024) | B6 |
| truth-ct, truth-dec | Cointelegraph, Decrypt, 14 Oct 2024 | B8 |
| oql, ai4c, mik, dfnpr, bgtw | arXiv items | B9 |
| shannon | Shannon 1948 | C1 |
| cover | Cover and Thomas, 1st ed. 1991 | C2 |
| arora | Arora, Barak, Brunnermeier, Ge, working paper 2009 | C3, C4 |
| hayek | Hayek 1945 (sections) | C5 |
| akerlof | Akerlof 1970 | C6 |
| ashby | Ashby 1956 | D1, D2 |
| dmu | Danielsson, Macrae, Uthemann 2017 | E1 |
| du | Danielsson and Uthemann 2025 | E2 |
| mitsloan | Vereckey, MIT Sloan, 30 Aug 2023 (reports Gensler and Bailey 2020) | E3 (secondary) |
| keynes | Keynes 1936 ch. 12 (sections) | E4 |
| morris | Morris and Shin 2002 | E5 |
| granovetter | Granovetter 1978 | E6 |
| sep | Epstein, SEP "Social Ontology" | F1 |
| dennett | Dennett 1987 ch. 2 | F3 |
| lupia | Lupia and McCubbins 1998 | F4 |
| poole, fox, nk | Poole 2024, Fox 2024, Narayanan and Kapoor 2025 | G1–G3 |

**Not cited (and why).** B7 IMF (dropped); A6 items (dropped); C7 Grossman and Stiglitz (cut for length; the toy's λ cannot be checked); E7 Minsky (cut; trap 24); F2 Keynes ch. 17 (cut); Hayek is optional. "Further reading": Searle (S1b), Haldane and May (S1b), *Nexus* hardcover (S1b).

---

## 17. Widget inventory (rubric criterion 5)

| Mechanism | Widget | Config file | Verified? | Edge case as preset |
|---|---|---|---|---|
| Rule vs table (hook) | `switch` | in HTML | static | panel A shrinks to a rule, B does not |
| Tranche waterfall | `diagram` (3 steps) | S4 | to write | – |
| Pooling vs common factor | `lab` cfg-cdo | widgets/labs.json | yes | "safe loans, p = 0.02": 634.5 times |
| Counting short descriptions | `lab` cfg-count | widgets/labs.json | yes | k = 14: all 10,000 can have short names |
| Informed seller | `diagram` (steps) | S4 | to write | – |
| Tamper-proof tree (fold-out) | `diagram` | S4 | to write | – |
| Ashby table | `stepper` | widgets/ashby-stepper.json | parsed | – |
| Requisite variety bound | `lab` cfg-ashby | widgets/labs.json | yes | V_R > V_D: bound floors at 0 |
| Effective sample size | `lab` cfg-neff | widgets/labs.json | yes | huge crowd, ρ = 0.3: 3.257 |
| Counting a signal many times | `lab` cfg-bayes2 | widgets/labs.json | yes | n = 10: 0.999999 from one source |
| Cascade by hand | `stepper` | widgets/w5-hand-stepper.json | parsed | – |
| W5 cascade | `cascade` cfg-w5 | widgets/w5-cascade.json | yes | lgd 1; capMult just above 1.2 |
| Herding with breaker | `iterate` cfg-herding | widgets/herding.json | yes | m = 0.67 border; breaker 3 |
| LLM translator pipeline | `diagram` (steps) | S4 | to write | step 4: output no checker can read |
| Status function | `diagram` (steps) | S4 | to write | remove C, Y vanishes |

All numbers a widget shows are in `widgets/check-output.txt` (regenerate with `widgets/regen-check.sh`). Inventory: 5 labs, 1 cascade, 1 iterate, 2 steppers, 5 diagrams, 1 switch. At most 2 sliders per widget.

---

## 18. Trap register (each trap and where it is handled)

| Trap | Where |
|---|---|
| 1 AI is not LLM | hook scope sentence; 3a flag; section 4 |
| 2 new ≠ incomprehensible | sections 4, 5 (limit), 13 |
| 3 two meanings of "complicated" | trap box in 5b |
| 4 three "ten years" | trap box in 3a |
| 5 catastrophic vs existential | 3a (Guardian 2023) with the "not yet powerful enough" hedge |
| 6 transcript errors | quotes follow the brief; "AIs", "U.S. AI" |
| 7 Nexus pagination | cite "paperback sample" |
| 8 FSB URL | cite the 40-page report |
| 9 Arora versions | "working paper, 2009"; "shows, under a conjectured assumption" |
| 10 KKST version | "working paper, 2014" |
| 11 Danielsson | 2017 vs 2025 labelled |
| 12 Lopez-Lira and Tang 90% | "direction of the initial reaction", not a return |
| 13, 25 Scheurer | existence proof; "nearly (but not exactly) 0%" |
| 14 Calvano | goods market; "cannot be applied ... as it stands" |
| 15, 29 MIT Sloan | "as reported by MIT Sloan", dated 2023 |
| 16 IMF | not cited |
| 17 counting is not Arora | 5a "what it means", 13 |
| 18 Economist | cite the Ynetnews republication of 7 May 2023 |
| 19 toys are ours | "toy, ours" in titles and captions |
| 20 FCIC "almost no one understood" | 3b, both halves |
| 21 BIS teaser | in-talk timestamps only |
| 22 Cover and Thomas edition | "1st edition (1991)" |
| 23 Ashby misprint | trap box in section 6 |
| 24 Minsky | not used |
| 26 FSB tail | always both halves |
| 27 RegretNet | "approximately incentive compatible" |
| 28 audio uncertainty | footnote on WEF [32:00]; no BIS [7:18] "at least" |
| 30 BIS [30:24] | quoted as one Harari sentence |
| 31 Cointelegraph | range, never one figure |

---

## 19. Audio chapter plan (about 28.5 min)

Voice: kokoro af_heart. First chapter starts "Welcome to AI4Read from CSS Lab." Every chapter ends with a short recap. Formulas spoken in words (for example "N effective equals N divided by one plus N minus one times rho"). Deep dives are only mentioned. About 150 words per minute, about 4,300 words.

| id | title | min |
|---|---|---|
| hook | Two contracts | 1.5 |
| guess | Guess first | 1.0 |
| home | Finance before LLMs | 3.0 |
| llm | What LLM agents add | 2.5 |
| lens-info | Lens one: information theory | 3.0 |
| lens-control | Lens two: control | 2.0 |
| lens-decision | Lens three: correlation and cascades | 3.5 |
| lens-social | Lens four: social reality | 1.5 |
| ladder | Five rungs up, spoken | 2.0 |
| play | Playground | 0.5 |
| turn | Your turn | 0.5 |
| work | Where this shows up in your work | 1.0 |
| answer | Layers, conditionals and our reading | 2.5 |
| recall | Recall questions | 1.5 |
| english | How to say it in English | 1.5 |
| c1-loop | A paragraph to loop | 1.0 |
| | **Total** | **28.5** |

The chapter ids equal the `data-ch` ids in content.html (`sources` has no audio).

---

## 20. Rubric self-check (criteria 2, 4, 5)

### Criterion 2 · the ladder
Scores are for the outline as written. Fixes already applied are in brackets.

| Section | New concepts | Score | Note / fix |
|---|---|---|---|
| hook | contract (instance only) | 5 | – |
| home 3b | tranche, diversification, correlation | 5 | [Fix applied: first draft used a 10-loan pool whose binomial sum is not hand-sized; now 4 loans, 3 numbers by hand, check by widget.] |
| llm | LLM agent, closed vocabulary | 4 | Descriptive concepts; no numbers by design. Risk: "closed vocabulary" check is only a diagram. Fix in S4: one worked example line of OQL-style intent → query with the human-readable check. |
| lens-info 5a | description length, bits | 5 | full, check = widget values; includes the failing case (k = 14) |
| lens-info 5b | lemon cost, informed seller | 5 | N = 100 toy, check 50 − 45 = 5; graduate form in Rung 2 |
| lens-control | variety, requisite variety | 5 | table, brute force, check in stepper; entropy form deferred to Rung 3 without dependency |
| lens-decision 7b–7e | N_eff, odds form, threshold cascade, feedback | 4 | All four have instance, numbers, formula, check. Risk: 800 words for four ladders; 7e's formula check is a hand step plus widget but the "tips at A·m = 1" is only justified in Rung 5. [Fix for S4: 7e must give the one-line intuition itself, without sending the reader to Rung 5: each step the trend-chasers add A·m times the last move; if A·m is below 1 each push is smaller than the one before, if above 1 it is larger. Rung 5 then gives the exact version.] |
| lens-social | status function, delegation, personhood | 4 | Status function has a full ladder. Delegation is a theorem; [Fix: added a 2 × 2 table as worked numbers and two applied checks.] Personhood is a policy question with no numbers by nature. |
| ladder | 5 graduate rungs | 4 | Each rung has numbers and a check, but at about 100 words each it is tight. Risk: rung 3's "conditioning cannot raise entropy" is stated, not proved (standard fact, labelled). Fix in S4: one-line justification or an exercise. |
| play, turn, work, answer | no new concepts | 5 | – |

**Minimum: 4.** No section is below 4.

### Criterion 4 · the lenses
| Lens | Adds | Link type named | Limit stated | Connections (earlier post / 3C) | Score |
|---|---|---|---|---|---|
| 1 Information | novelty is cheap, explainable novelty rare | same-math, metaphor, structural analogy | rarity ≠ opacity; short ≠ easy to price (Arora) | post 01 (Shannon's twin, W1); 3C: Computation | 5 |
| 2 Control | control needs variety; three levers | same-math; structural analogy | passive disturbance; who regulates the regulator | back: entropy; forward: control field; cross-lens note (correlation is a constraint) | 4 |
| 3 Decision/Bayes | failure without error | same-math; structural analogies | toys, no adoption data; AI could reduce correlation | post 01 W4 and Lens 5; 3C: Computation (N_eff) | 5 |
| 4 Social reality | "taking over" splits into acceptance, accountability, personhood | structural analogy; metaphor | not empirical; no legal sources; Searle pending | post 01 Lenses 4–5; 3C: Communication | 4 |

**Post score: 4.** To reach 5 for Lens 2 and Lens 4: (Lens 2) add one sentence linking to a concrete earlier post lens (S4: "post 01's Bayes lens asked what a prompt tells a model; here the supervisor's checks are the 'evidence'"); (Lens 4) once Searle is in the library, cite his own text instead of SEP. Also the synthesis now has an explicit cross-lens tension paragraph.

### Criterion 5 · illustrations and interactives
All 12 mechanisms in section 17 have a widget. Eight configs are built and verified with `check.mjs` (W5, herding, five labs, plus the two steppers parsed). Five `diagram` configs (waterfall, informed seller, tree, LLM pipeline, status function) are sketched but not yet written, so they cannot be verified at S3.
- Widgets reproduce the numbers in the text: yes for all verified configs (see `check-output.txt`).
- Edge cases that teach: all verified widgets have one (section 17).
- 375 px: ≤ 2 sliders per widget, 6 nodes, labels ≤ 2 characters.
- **Score: 4** (5 when the five diagrams are written and pass `test.mjs`).

---

## 21. Open questions for the manager and Kunhao

1. **Hook world.** The hook uses a two-day village (16 states) to make the table point visible; the guess-first and ladder use the 4-word village (10,000). I think this is clearer than a 30-row table (30 is not a power of 4). OK?
2. **Playground as a section.** CHARTER §5.6 asks for an interactive section, so W5 and herding sit in section 10 with hand-worked numbers in Lens 3. If you prefer widgets inline in Lens 3, merge section 10 into 7 (no other change).
3. **`toyworlds.md` and `notation.md`.** I may not edit files outside the post folder. Please paste the W5/W6 entries and notation additions above.
4. **WEF [32:00] wording.** I will print "dominated by AIs" with a one-line footnote about the uncertain final word (trap 28). Alternative: stop the quote at "anymore" and paraphrase the rest. Which?
5. **Optional cuts.** Hayek paragraph, Morris–Shin sentence, Keynes "third degree", Flash Crash paragraph, Rung 6. All are marked as first cuts if S4 runs over 7,500.
6. **"Our reading".** Kept qualitative (no probabilities) because no source gives a base rate. Fine?
7. **Narayanan and Kapoor's "decades".** I quote it in the synthesis, not in the hook, so the hook stays neutral. Fine?
8. **FCIC waterfall order.** The toy's junior/senior order is ours. `requests.md` asks for the FCIC page that defines it, optional.
