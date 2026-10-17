# Pedagogy critic, round 2: post 02 (AI, finance, social system)

Read as Kunhao would: phone, B2-C1, every step wanted. Criterion 1 is not judged here. Scores 1-5 for criteria 2-6: **2** ladder, **3** clarity/English, **4** insight and lenses, **5** illustrations/interactives, **6** concision. "-" means the section has no such content to score.

I scored blind from `src/content.html`, the widget numbers (`check.mjs`, 15/15 configs OK, plus `--id lab-... --values` runs for every preset the prose quotes), the 390-px screenshot (contact sheets, plus native crops of the LLM section and the closing chain figure) and the audio script. I re-ran the six-bank cascade in Python for every number in the prose and the playground answers. I read `critic-1.md` only after scoring, for the status section at the end. I did not read self-review.md, response-1.md or the verify files.

## (a) Does the post now answer BOTH halves of Kunhao's question?

Kunhao asked: "can LLMs create a new type of finance, and what would that mean for our current social system?"

**Yes, both halves are now stated in one findable place, with one gap in half (b).**

- The hook defines "human-centred system" and splits the question into (a) and (b) in a term box. A one-line preview follows: "(a) Not yet evidenced. (b) The nearer risk is shared, opaque use of ordinary tools." That orients the reader in the first screen.
- Section 13 opens with a boxed short answer. (a): "Not yet evidenced... we found no traded instrument that an AI invented. Nothing shows it is impossible." (b): shared models mean losses "arrive together and fall on whoever lent to or holds the failed firms", people stay accountable "only if someone can verify what the AI did and be penalised when it fails", and supervisors "could not check what nobody can state in a page".
- Gap in (b): Kunhao's literal conditional is "if LLMs create a new type of finance, then what?" The short answer answers a nearby question (what happens with ordinary instruments on shared models). The literal case, an instrument nobody can state in a page, is covered only in the last clause plus Lens 1, 2 and 4, which the reader has to assemble. "Current social system" is also read narrowly as "who can check and answer for the rules that move money". That is defended in the hook, but law, the state and bail-outs get one clause each ("our toys do not model bailouts"). The concrete consequence for people (who pays, who can still verify) is one sentence.
- Where it sits: the short answer is still section 13 of 16, about 40 minutes in. The hook preview mitigates this.
- Fix: add two sentences to the short answer box that answer the literal case: "If an AI did invent an instrument nobody can state in a page, then by Ashby the supervisor's checks cannot match its variety, and by Lupia and McCubbins the principal loses the knowledge condition; only a standard menu or a verifier brings it back."

## Per-section scores

| Section | C2 Ladder | C3 Clarity | C4 Lenses | C5 Illus. | C6 Concision |
|---|---|---|---|---|---|
| 1 Hook | 5 | 5 | - | 5 | 5 |
| 2 Guess first | - | 5 | - | - | 5 |
| 3 Home field | 5 | 4 | 4 | 5 | **3** |
| 4 LLM agents add | 4 | 4 | 4 | 5 | 4 |
| 5 Lens 1 Information | **3** | **3** | 4 | 4 | 4 |
| 6 Lens 2 Control | 5 | 4 | 5 | 5 | 4 |
| 7 Lens 3a Correlation, Bayes | 4 | 4 | 4 | 5 | 5 |
| 8 Lens 3b Cascades | 4 | 4 | 5 | 5 | 4 |
| 9 Lens 4 Social reality | 4 | 4 | 5 | 5 | 4 |
| 10 What to try | - | 5 | - | - | 5 |
| 11 Your turn | - | 5 | - | - | 5 |
| 12 Where in your work | - | 5 | 5 | - | 5 |
| 13 Synthesis | - | 4 | 4 | 4 | 4 |
| 14 Recall | 5 | 5 | - | - | 5 |
| 15 English | - | 5 | - | - | 4 |

### Section evidence and fixes (every score below 5)

**1 Hook (5, 5, -, 5, 5).** C2: Contract A is priced by hand, "(8 + 6 × 4)/16 = 2 coins", and the one-sentence versus 16-numbers contrast is the whole idea. C3: "Which can you explain in one sentence?" is a short sentence. C5: the Contract A/B switch lets the reader see the table. No fix.

**3 Home field (5, 4, 4, 5, 3).**
- C2 is 5: the CDO ladder is complete (instance, question, mechanism, numbers "4×0.1³×0.9=0.0036", formula, check "w=0.5 gives 5.185%"). The widget gives 5.185% at w=0.5.
- C3 is 4: the "He asserts, without hedges" and "He imagines, with hedges" paragraphs carry up to 6 bracketed cites each. Phone readers and the audio meet "[5:14]", "[16:21]". Fix: in the body keep three quotes (one asserted, one imagined, one limit) with a cite each. The fold-out already holds the rest.
- C4 is 4: the home field has no link back to post 01 except one parenthesis: "(Our bridge to post 01: he asks whether next-word prediction is 'so different...')". Fix: one sentence naming the link type for 2008 and Lens 3 ("same-math: correlated errors; the junior and senior tranches are a threshold").
- C6 is 3: the assert/imagine point is made five times in one section (body paragraphs, the "three ten years" trap, the fold-out, the Prediction 4 answer, "Our reading (ours)") and again in sections 9 and 13. Fix: delete the Prediction 4 restatement of quotes (keep "Partly") and fold the trap into the fold-out. That is about 15-20% of this section.

**4 LLM agents add (4, 4, 4, 5, 4).**
- C2: "An option is a contract that pays if a price ends above or below a set level" has no number. The query line `RANGE(index, 90, 110)` helps, but a one-line payoff example is missing. Fix: add "if the index ends at 95, the payout is 1; at 120, 0".
- C3: first loss for a high-school reader in the whole post: "Neural networks that search for auction rules (who wins, who pays): one method 'will generally only find' rules that are 'approximately incentive compatible'. Deep hedging, which is risk management..." "Incentive compatible" and "deep hedging" are never defined. Fix: cut the Dütting and Buehler clauses to "Found: LLMs translating intent into a fixed vocabulary, and neural nets that tune auction rules (not invent instruments)".
- C4: "Lens 3 picks this up" gives no link type. Fix: add "(link: structural analogy)" etc.
- C6: the $122M vs $214M valuation detail can go.

**5 Lens 1 (3, 3, 4, 4, 4).**
- C2 (3): Ladder 1 is a full ladder: "10^4 = 10,000 contracts... log₂ = 13.29 bits... k=6: 63 (0.63%)". Ladder 2 is where the post's claim "a short rule can still be hard to price" rests. It gets an instance, a numerical lemon cost (45, 5) and then the key step with no instance or numbers: "Over-representing the junk in a few products, just enough to skew their default chance, can look like random pooling to a buyer with limited computing. Detecting it is the 'hidden dense subgraph' problem". "Hidden dense subgraph" is never explained, and the only number offered (C(100,10)) is disclaimed as "beside the point". Fix: add a toy in three sentences. Example: 6 assets, 3 products each over 3 assets. A plain pool gives each product the same default chance. The seller puts 2 junk assets into one product so that product defaults more often. Show how, with 100 assets and thousands of products, a few skewed ones hide among the rest, and say why trying all junk sets is too slow. State "intractable" in a clause: "no known fast method (conjectured)". The current fold-out holds only the formula.
- C3 (3): Ladder 1 packs instance, question, mechanism, counting and formula into one 160-word paragraph. Ladder 2's "Now put a derivative on top" paragraph has 7 sentences, one with "(impossible to solve in realistic time)" inserted. Fix: set Instance / Question / Mechanism / Formula / Check as five short lines (a list, as the ladder in WRITING §2). Define "derivative" at first use. The sentence "It cannot tell a fair price from an inflated one" is where the fix goes.
- C4 (4): the tag "metaphor: a price as a short message hiding a long story" is never used again, and the Arora step is computational complexity, not information theory. Fix: delete the metaphor tag, and say in "Adds" that ladder 2 borrows a complexity lens.
- C5 (4): the seller diagram shows who knows what, not how hidden junk skews products. Fix: show the toy above as a tiny diagram (6 assets, 3 products, one skewed).
- C6 (4): cut "Testing every junk set means C(100,10)... huge, but beside the point" (about 40 words) from the paragraph and from the diagram step.

**6 Lens 2 (5, 4, 5, 5, 4).**
- C3 (4): "The table condition" sentence block mixes the table rule, the failing case and the mechanism in one paragraph: "Ashby requires that in each column... Without it the bound below can fail (if every cell gave the same outcome, there would be nothing to regulate)." Fix: make "table rule" its own two-line paragraph before "Question".
- C6 (4): the three levers plus "Counterweights" quote five authors in one run; cut Danielsson/Uthemann's "stabilise and destabilise" since the box repeats it later.

**7 Lens 3a (4, 4, 4, 5, 5).**
- C2 (4): the N_eff derivation is full, with a check ("N=2, ρ=0.5: 2/1.5=1.33 ✓"). But "N(N−1) ordered pairs, each with covariance ρσ²" uses "covariance", which is not defined (the term box defines variance and correlation only). The Bayes ladder is reduced to a main-text paragraph with the instance and numbers in a fold-out, so the main text says "Counted once, 80% confidence; counted ten times, 99.9999%" without showing why. Fix: add "covariance = ρσ², the part of two errors that move together" to the term box, and one line in the main text: "each independent 'safe' multiplies the odds by 4: 1:1, 4:1, 16:1".
- C3 (4): the instance sentence is fine; the derivation is dense. See fix above.
- C4 (4): the lens is labelled "Decision, game theory and Bayes" in the header, but game theory is a Keynes quote only. Fix: rename the meta line to "Correlation, Bayes and conventions".

**8 Lens 3b (4, 4, 5, 5, 4).**
- C2 (4): Ladder 3 is complete, with a by-hand stepper and the widget. Ladder 4 gives the tipping point as "Intuition: each step the chasers add Am times the last move. The swing shrinks when Am<1" and leaves the proof to the fold-out (complex roots). A high-school reader cannot check the claim "tipping point m=1/A" from the main text. Fix: add one numeric check in the main text: m=0.67, Am=1.005: the last-move factor is just above 1, so the swing grows slowly (the readout shows 2.68/-2.70).
- C3 (4): "Worked numbers" paragraphs run 5-6 numbers in one line. Fix: a three-row table (m, push, pull, outcome).
- C6 (4): "What to try" (section 10) repeats the toy tasks and sits far from the toys. Optional fix: move "(1) Switch off X2 and X3" into the paragraph after the widget.

**9 Lens 4 (4, 4, 5, 5, 4).**
- C2 (4): acceptance and accountability have an instance, a mechanism and a table. Personhood has no ladder (by design: "we have no legal sources"). Lupia's theorem is given as the table only; the "check" is missing. Fix: add one sentence plugging the broker example back into the table cell: "knowledge no, incentive no: you buy whatever he sells".
- C3 (4): "Our test (ours)" runs six sentences with "(ours)" three times, then "our two supports are a different limit". Fix: cut to "Test: acceptance and enforcement. A story is not money until a community counts it; a contract is not honoured until someone enforces it." Mark "(ours)" once.
- C6 (4): "The strongest version" repeats the same point as the keypoint in section 13. Cut one.

**13 Synthesis (-, 4, 4, 4, 4).**
- C3 (4): the short answer is one 170-word paragraph with semicolons. Fix: split it into (a) and (b) in two paragraphs, one idea per sentence.
- C4 (4): the chain diagram labels the edge "AI invents new financial instruments → Shared, opaque, hard to check" as "supported in toys". But the toys show correlation among ordinary instruments, and the post's own (b) says no invention is needed. Fix: route "Shared models" off the "AI takes over finance" node, not the "invents" node, or relabel the edge "toys: no invention needed".
- C5 (4): same figure; also all five edge labels are visible at once, so the steps only add text. Fix: reveal the edges per step (edges have `steps.show`).
- C6 (4): the short answer, the keypoint, "Our reading" and the fold-out (layers, conditionals) all repeat the same four points. Fix: cut the keypoint paragraph (it restates sections 3 and 9).

**15 English (-, 5, -, -, 4).** C6: eight topic phrases plus eight evidence phrases plus patterns plus fixes is still a lot; three phrases are marked as repeats from post 01, which is good. Fix: cut "Small fixes" to two lines or fold it.

## First place a high-school reader gets lost

1. First loss, section 4, the "Found" bullet: **"Neural networks that search for auction rules (who wins, who pays): one method 'will generally only find' rules that are 'approximately incentive compatible'."** "Incentive compatible" is undefined and "deep hedging" in the next sentence is name-dropped.
2. The first real conceptual loss is in section 5, Ladder 2: **"Detecting it is the 'hidden dense subgraph' problem, which computer scientists believe to be intractable."** The reader has not been shown what is hidden, in what, or why a short public rule does not reveal it.

## Widget checks (does the reader do the mechanism? edge case? prose quotes readout?)

- **sw-contracts (switch):** works, and the point (one sentence vs 16 numbers) is visible. Prose "1 cell pays 8, 6 pay 4, 9 pay 0" matches the table. OK.
- **dg-waterfall + lab-cdo:** the reader can drag p and w, and the preset "safe loans, p = 0.02" is a real edge case. Readouts: w=0 gives 0.370%, w=0.5 gives 5.185%, w=1 gives 10.000%. Preset p=0.02, w=1: "2.000%... 0.0032%... 634.5 times". All quoted correctly. Note: the default readout says "your mix is 1.0 times that", which is fine.
- **dg-llm:** the steps work and the edge case "no checker?" teaches the Mik hedge. OK.
- **lab-count:** presets "k = 14" (readout: 16,383, fraction 1) and "two days, k = 20" (1.05e-10) match the prose. Teaches the bound saying nothing. OK. The "days in the contract" slider is hidden under the "k" slider, but the preset labels explain it.
- **dg-seller:** it shows the knowledge asymmetry but not the placement trick (see section 5 fix). Weak for the claim it supports.
- **dg-tree (fold-out):** steps work. "Fewer than 4 flips" and 9/27/81 inputs needing 4/8/16 flips are consistent with the code check.
- **st-ashby + lab-ashby:** the stepper walks the table. Preset "free market" gives V_O ≥ 9.29, "standard menu" gives 2.64 (13.29 - 4 → 6.64 - 4). Prose quotes 9.29 and 13.29-6.64=6.64. The edge case (V_R past V_D gives 0) is stated. OK.
- **lab-neff:** "huge crowd, 0.3" gives N_eff = 3.257 (the prose quotes 3.257). Default readout 1.099 at ρ=0.9. OK. The "all wrong together" line in the readout and N_eff are different quantities on one widget. The prose says so ("A second question").
- **lab-bayes2 (fold-out):** n=10 gives odds 1,048,576, P = 0.999999. Matches. OK.
- **st-w5-hand + cs-w5:** hand table ends "Y3 12 / 11, all six fail"; the widget gives 6 of 6 in 3 rounds. Seeded with X1, X2, X3 as the prose says. capMult 1.5 gives 3 of 6. Playground answers verified by Python: single failures at 0.8 spread nowhere; at 1.0 only Y1 spreads (3 of 6); any two X banks at 1.0 sink 5 of 6; ×1.2 gives 5 of 6, ×1.25 gives 3. All correct.
- **it-herding:** m=0.2: swing 0.04 up, -1.00 down, final 0.000, matches. m=0.9 with breaker 3: ±3.00 as stated. m=0.67 shows no decay in 40 steps (swing 2.68/-2.70), consistent with "tipping". Roots (0.548, 1.002, 1.162) checked against the formula.
- **dg-status:** steps work; the final step is long. OK.
- **dg-chain:** see section 13 notes (edge label, steps only change text).
- **Screenshot at 390 px:** no horizontal page scroll. Long formulas (the Lens 1 count, the N_eff variance, the herding rule) are clipped inside scroll containers; they work, but the reader has to swipe to read the key formula of ladder 1. Fix: break the three formulas into two lines each.

## Lens checks

| Lens | Says what it adds | Link type | Says what it does NOT explain | Verdict |
|---|---|---|---|---|
| 1 Information | Yes: "explainable novelty is rare among possible contracts, and a short rule does not make a price easy" | same-math, analogy, metaphor (the last is unused) | Yes: "whether an AI would pick opaque contracts" | Good; drop the unused metaphor, flag that ladder 2 is a complexity lens |
| 2 Control | Yes: "control needs variety, and there are three ways to get it" | same-math, analogy | Yes: Ashby's disturbance is passive; plus an "Across lenses" note | Strong |
| 3a Correlation, Bayes | Yes: independent opinions depend on correlation, not headcount | same-math, analogy | Yes: "how much correlation real LLM-based desks have; ρ is assumed" | Strong; header over-promises game theory |
| 3b Cascades | Yes: "failure needs no mistake, only correlation, then a threshold or a feedback gain" | same-math, analogy | Yes: "how many firms really share a model" | Strong |
| 4 Social reality | Yes: "taking over money" splits into writing contracts and giving status | structural analogy only | Yes: "how any of it works in law" | Good; honest about the missing legal sources |

Links to post 01: Lens 1 (Shannon, counting texts), Lens 3a (Bayes with LR 4), Lens 4 (the octopus), and the hook village. Links to Kunhao's 3C work: section 12 is concrete (N_eff for LLM labeling, social simulation, cross-lingual safety). Good.

## Audio listenability

The script follows the page and speaks formulas in words. Recaps end each chapter. Weak spots: the "home" chapter reads the three-layer frame twice and runs long; "range, index, ninety, one hundred ten" is hard to follow without the screen; the Lens 4 chain test has "(ours)" repeated. Nothing blocks.

## Suspicious facts (for the fact-checker; one line each)

- Akerlof 1970: the "bad cars tend to drive out the good" line is quoted at pp. 489-490; check the page.
- Cover and Thomas 1991, Theorem 7.2.4, p. 150: check the theorem number and that "can produce only one possible output sequence" is there in the 1st edition.
- SEP Social Ontology: "§ 4.2.3" for the stones/Bureau of Engraving example and "§ 5.6" for Menger; check the section numbers.
- Keynes 1936, ch. 12 "§ IV (standard numbering)": confirm § IV and § V for the two quotes.
- Flash Crash "about 36 minutes": the Kirilenko et al. abstract's duration; the post attributes it to a fold-out with a cite only on the HFT quote.
- Truth Terminal: "$50,000 worth of Bitcoin (BTC)" and the 122M/214M valuations from two outlets that may have been dated differently.
- Arora et al. 2009: "clearly only a first step" and "is probably correct" at p. 12; Table 1 in words (p. 6) in the lemon-cost fold-out.
- Arora's tree of majorities: "o(2^k)" and "much larger than √(3^k)" need page 12 confirmation.
- Granovetter 1978, pp. 1424-1425: the "two crowds are essentially identical" line.
- Danielsson et al. 2022, p. 7: "will likely be unintelligible to humans".
- Harari BIS [16:21], [22:57], [23:15] and WEF [26:33]: timestamps are from "our transcript"; confirm against the audio.

## Post-level scores (minimum over sections)

| Criterion | Score | Lowest section(s) |
|---|---|---|
| 2 Ladder | **3** | Lens 1 (ladder 2, the hardness step) |
| 3 Clarity and English | **3** | Lens 1 (dense ladder paragraphs, "hidden dense subgraph") |
| 4 Insight and lenses | **4** | Home field, LLM agents, Lens 1, Lens 3a, Synthesis (each 4) |
| 5 Illustrations | **4** | Lens 1 (seller diagram), Synthesis (chain diagram) |
| 6 Concision | **3** | Home field (assert/imagine repeated five times) |

The release gate (at least 4 on every criterion) is **not met** on criteria 2, 3 and 6. Every other section is at 4 or 5. One section (Lens 1) and the repeated Harari framing in section 3 hold the post back.

## Top three changes

1. **Climb the hardness step in Lens 1, ladder 2, and split the dense paragraphs.**
   - Add a three-sentence toy (6 assets, 3 products, 2 junk assets placed in one product) showing how a seller can skew a product while the public rule stays short. State "intractable" as "no known fast method (conjectured)", and define "derivative" at first use.
   - Break Ladder 1 and Ladder 2 into short Instance / Question / Mechanism / Formula / Check lines.
   - Cut the C(100,10) aside, and the unused metaphor tag.
   - Redraw the seller diagram to show the skew.
   - This lifts criteria 2, 3, 5 and 6 for Lens 1, the lowest section on both.
2. **Say the Harari assert/imagine split once in section 3, and clear the jargon in sections 3-4.**
   - Keep three quotes with cites in the body, and fold the trap and the Prediction 4 restatement into the fold-out or the answer reveal.
   - Cut or define "approximately incentive compatible" and "deep hedging", add a number to the option example, and give the "Lens N picks this up" notes a link type.
   - This lifts criteria 6 and 3 in section 3 and removes the first place a high-school reader gets lost.
3. **Sharpen half (b) and the dense closing blocks.**
   - Add the literal conditional to the short answer ("if an AI did invent an instrument nobody can state in a page...") and split the box into (a) and (b) paragraphs.
   - Fix the chain figure (the "supported in toys" edge points at the wrong node) and reveal edges stepwise.
   - Define covariance in the term box and add the odds line (1:1, 4:1, 16:1) to the Lens 3a main text.
   - Split the "worked numbers" lines in Ladder 4 and the "Our test (ours)" paragraph.
   - This lifts criteria 3, 4 and 5 in sections 7, 9 and 13.

## Status of round-1 top changes

| Round-1 change | Status | Evidence |
|---|---|---|
| 1. Findable short answer, finish the "social system" half, define "human-centred", cut §13, add chain figure, state consequences | **Mostly addressed** | Hook defines the term and previews (a)/(b); §13 opens with a boxed short answer; the layers, conditionals and critics moved into a fold-out; the chain figure exists. Still open: the literal "if invented, then" case, the one-sentence consequence for people, and a mislabeled chain edge. |
| 2. Ladders stand alone; N_eff and tipping inside the lenses; define description; show why hidden junk stops the buyer; principal/agent instance; define variance/correlation; widgets next to ladders; shorten Bayes ladder; fix playground answer (2) and seed cs-w5 | **Mostly addressed, one open** | N_eff derivation and variance/correlation term box are in Lens 3a. "Description" is defined. Principal/agent instance and the 2x2 are added. Widgets sit beside Ladders 3 and 4. Bayes is a paragraph plus fold-out. The playground answers check out in Python and cs-w5 is seeded. Open: the hidden-junk step has still no instance (Lens 1 ladder 2), and "covariance" is undefined. |
| 3. Cut and explain finance vocabulary in §3-4; keep about 4 Harari quotes; show the one-line contract; link each addition to its lens; fix §11 heading; Exercise 4 hint and solution | **Partly addressed** | HFT, circuit breaker, option, query language and memecoin are now defined, `RANGE(index, 90, 110)` is shown, each addition ends "Lens N picks this up", Exercise 4 has a hint and a solution, and the §11 heading is fixed. Still open: Harari quotes are ~12 in the body (not 4) and the point is repeated; "incentive compatible" and "deep hedging" are new undefined terms in §4. |
