# Pedagogy critic, round 3: post 02 (AI, finance, social system)

Read as Kunhao would: phone, B2-C1, every step wanted. Criterion 1 is not judged here. Scores 1-5 for criteria 2-6: **2** ladder, **3** clarity/English, **4** insight and lenses, **5** illustrations/interactives, **6** concision. "-" means no such content to score.

**Method and one disclosure.** I read the role prompt, `learner/state.md`, `topic-card.md` (decisions), the full `src/content.html`, the `check.mjs` output (15/15 configs OK) and the word count (main text 6,942 words, cap 7,500; fold-outs 1,853). I also ran `check.mjs --id ... --values` for every preset the prose quotes, and looked at contact sheets of `shot-390.png` at native resolution. I skimmed `audio-script.md`. I did not read self-review.md, response files or verify files. **Disclosure:** I opened `critic-2.md` in the same tool batch as the audio script, after I had read the whole post but before I wrote any score. The scores below come from the current text, but I am not strictly blind to round 2. All scores are from the draft as it now stands.

## (a) Does the post clearly answer both halves of Kunhao's question?

Kunhao's question: can LLMs create a new type of finance, and what would that mean for our current social system?

**Yes, both halves are answered in a findable place, and the round-2 gap is closed. One weakness remains in half (b).**

- **Findable.** The hook defines "human-centred system" and splits the question into (a) and (b). It previews: "(a) Not yet evidenced. (b) The nearer risk is shared, opaque use of ordinary tools. Section 13 has the short answer." The contents list links to it. Section 13 opens with a boxed short answer.
- **Half (a).** "Not yet evidenced. A research pipeline improves LLM translation of plain-language intents into option strategies, and agents hold wallets, but we found no traded instrument that an AI invented. Nothing shows it is impossible." Section 4 supports this with Found / Not found bullets and the FSB's own scope caveat. This is honest and clear.
- **Half (b), literal case.** Fixed since round 2: "If an AI did invent an instrument nobody can state in a page, then (each step ours, conjectured): (i) the seller-side information gap grows (Lens 1); (ii) supervisors lose variety (Lens 2); (iii) if many firms use it, failures arrive together (Lens 3); (iv) accountability needs someone who can verify and penalise (Lens 4)." Each step points to a lens.
- **Remaining weakness.** "Current social system" is still read narrowly, as who can check and answer for money's rules. The consequence for people is thin. Step (iv) says what accountability *needs*, not what happens to people if nobody can verify. The next paragraph supplies "buyers and lenders" and "delegation fails", but only for the ordinary-instrument case. The state, bail-outs and democratic control (Harari's own worry: "power shifting from humans to algorithms") get one parenthesis ("our toys do not model bailouts") and a "contested" tag in the chain figure.
- **Distance.** The short answer is section 13 of 16, about 40 minutes in. The hook preview and contents link mitigate this.
- **Fix.** Add one plain sentence to (b): "If nobody can verify, the people who hold the contracts cannot tell a fair price from an unfair one, supervisors cannot match its variety, and nobody can be held to account. That is the sense in which the system stops being human-centred." Then trim the third paragraph (see section 13 below).

## Per-section scores

| Section | C2 Ladder | C3 Clarity | C4 Lenses | C5 Illus. | C6 Concision |
|---|---|---|---|---|---|
| 1 Hook | 5 | 5 | - | 5 | 5 |
| 2 Guess first | - | 5 | - | - | 5 |
| 3 Home field | 4 | 4 | 4 | 5 | 4 |
| 4 LLM agents add | 4 | 4 | 5 | 5 | 4 |
| 5 Lens 1 Information | 4 | 4 | 5 | 5 | 4 |
| 6 Lens 2 Control | 5 | 4 | 5 | 5 | 4 |
| 7 Lens 3a Correlation, Bayes | 4 | 4 | 5 | 5 | 5 |
| 8 Lens 3b Cascades, feedback | 4 | **3** | 5 | 5 | 4 |
| 9 Lens 4 Social reality | 4 | 4 | 5 | 5 | **3** |
| 10 What to try | - | 5 | - | - | 5 |
| 11 Your turn | - | 5 | - | - | 5 |
| 12 Where in your work | - | 5 | 5 | - | 5 |
| 13 Synthesis | - | 4 | 4 | 4 | **3** |
| 14 Recall | - | 5 | - | - | 5 |
| 15 English | - | 5 | - | - | 4 |

## Section evidence and fixes (every score below 5)

**1 Hook (5, 5, -, 5, 5).** C2: "Contract A is worth (8 + 6 × 4)/16 = 2 coins" is priced by hand. C3: "Which can you explain in one sentence?" C5: the A/B switch shows the table. No fix.

**3 Home field (4, 4, 4, 5, 4).**
- C2 (4): the CDO ladder is complete ("4×0.1³×0.9=0.0036 ... 0.37%", check "w=0.5 gives 5.185%"). Two small gaps. The definition is circular: "CDOs ... pools of financial assets, such as the riskier tranches of mortgage-backed securities, sliced into *tranches* in a cash-flow 'waterfall'". The reason for the formula "P = w·p + (1−w)·q" (with chance w one common coin decides, otherwise independent) appears only in the widget caption. Fix: replace the definition with "a CDO pools many loans and cuts the pool into slices called tranches; the slice paid last is safest". Add one sentence before the formula: "With chance w one common coin decides all four loans (the senior tranche loses with chance p); otherwise they are independent (chance q)."
- C3 (4): the four-row table still carries nine bracketed cites on a phone ("[5:48]–[5:57]", "[10:19], [10:27]"). Fix: keep one cite per row and move the rest to the fold-out, which already lists them.
- C4 (4): the 2008 block names its link type ("same-math with Lens 3a ... and Lens 3b") but nothing links the home field back to post 01. Fix: one sentence: "Post 01 asked whether a model that predicts words can understand; Harari's group 1 claims assume it can."
- C6 (4): the table, "Our reading (ours)", the Prediction 4 answer and the fold-out all sort Harari's lines into the same four groups. Fix: cut the first two sentences of "Our reading" (they restate the table row by row). Keep "The fold-out lists every line we use."

**4 LLM agents add (4, 4, 5, 5, 4).**
- C2 (4): the option now has a number ("an index ending at 95 pays 1, one ending at 120 pays 0"). Items 2-4 are reported findings, not concepts to climb, which is fine. The query language is explained as "like the boxes on a form". The line is "(our gloss)", labelled honestly. No fix beyond C3/C6.
- C3 (4): item 2 (Truth Terminal) is nine sentences of attribution: "Decrypt says neither the bot nor its handler created the token; Cointelegraph says the bot did not launch it. On 14 October Cointelegraph put GOAT at about $122 million ... on 16 October Decrypt reported over $214 million". Fix: "Reports differ on who created the token; neither discusses liability." Cut both valuations.
- C6 (4): the same valuation detail (about 45 words) is the cut.

**5 Lens 1 (4, 4, 5, 5, 4).**
- C2 (4): Ladder 1 is a full ladder: "10⁴ = 10,000 ... 13.29 bits ... k=6: 63 (0.63%) ... k=10: 1,023 (10.2%)", with an edge case at k=14. Ladder 2 now has a toy: "If the junk sits in two different products, only one product is worth anything: total ¼. If both junk assets share a product, two are: total ½." That fixes round 2. The hardness step is still only asserted: "Spotting them is the 'hidden dense subgraph' problem. Computer scientists believe it is intractable (a conjecture)". What the "graph" is (assets as points, products as groups) is not said. The honesty is fine; the picture is missing. Fix: one sentence: "Think of assets as dots and each product as a group of dots; the seller hides a few groups packed with junk among thousands of ordinary groups, and finding them means searching all ways to pick groups."
- C3 (4): the ladders are now short labelled lines. "What is claimed" is a dense paragraph of five cites ("amplify the costs ... pricing 'may be computationally intractable' ... 'clearly only a first step' ... 'is probably correct'"). Fix: split into "claimed" and "how far it goes" paragraphs (the bold labels exist; add a break).
- C6 (4): the plain-pool paragraph (45, lemon cost 5) is needed as a contrast, but the sentence "Every choice of 10 junk assets gives the same 45, so there is nothing to search" repeats the point the toy makes. Cut it.

**6 Lens 2 (5, 4, 5, 5, 4).**
- C3 (4): the "Table rule" paragraph is still one block (rule, failing case, mechanism). Fix: set the rule in two lines before "Question". Lever 2 packs eight sentences from three papers into one list item (Danielsson and Uthemann twice, plus Danielsson, Macrae and Uthemann).
- C6 (4): cut the "stabilise and destabilise" sentence from lever 2; keep the "amplifies" quote and the "build their own AI" proposal.

**7 Lens 3a (4, 4, 5, 5, 5).**
- C2 (4): covariance is now defined in the term box and the odds are in the main text ("1:1 ... 4:1 ... 16:1"). The N_eff derivation says "N terms of variance σ² and N(N−1) ordered pairs, each with covariance ρσ²" but never states the rule behind it: the variance of a sum is all the variances plus all the pair covariances. A high-school reader must take this on trust. The check ("the mean of two has variance 0.75σ²") is asserted, not computed. Fix: add "Rule: the variance of a sum is the sum of all variances and all pair covariances" and show the N=2, ρ=0.5 check in one line: (σ²+σ²+2·0.5σ²)/4 = 0.75σ².
- C3 (4): the derivation is two aligned lines plus one dense paragraph; acceptable. Fix is the same as above.

**8 Lens 3b (4, 3, 5, 5, 4).**
- C2 (4): Ladder 3 is complete (hand stepper, then widget, "6 of 6 ... 12 ≥ 10"). Ladder 4's tipping claim rests on intuition in the main text ("The swing shrinks when Am<1"), with the proof in the fold-out. The numeric check at m=0.67 helps ("Am=1.005 ... 2.68 up and −2.70 down"). Fine for a main text that stands alone; fix not required, but see C3.
- C3 (**3**): two dense paragraphs. Ladder 3 "Instance" is one 110-word paragraph with nine numbers and seven loan facts: "Y1 lent 5 to each X bank; Y2 lent 5 to X3 and 10 to Y1; Y3 lent 5 to Y1 and 10 to Y2." The reader has to hold the network in the head, and the figure comes after the worked numbers. Ladder 4's "Worked numbers, m = 0.2" paragraph runs about 15 numbers across two scenarios, then the intuition, then the tipping point. Round 2 asked for a table; it was not done. Fix: (1) a small loan table (borrower | lender | amount | capital) before the mechanism. (2) A three-row table: m | push Am | pull G(1−m) | gaps over three steps (0.2: 0.3, 0.4, −0.9, −0.51, −0.189; 0.9: 1.35, 0.05, −2.30, −3.94). Then put "Intuition" and the tipping point in their own paragraph.
- C6 (4): "What to try" (section 10) repeats the toy tasks far from the toys. Optional: move the three tasks under each widget.

**9 Lens 4 (4, 4, 5, 5, 3).**
- C2 (4): acceptance and accountability have instances, mechanism and a table check ("knowledge no, incentive no is the broker who sells you whatever he likes"). Personhood has no ladder, honestly flagged ("We have no legal sources and state no legal position"). No fix.
- C3 (4): "Testing Harari's chain" runs five paragraphs, each with two to four cites and repeated "(ours)" tags ("Our compression ... (ours ...)", "Our test (ours)", "The strongest version (ours)", "Our reading"). Fix: mark "(ours)" once per paragraph.
- C6 (**3**): the chain (money is stories → words → new devices → nobody understands) is stated here in prose with the group labels, then again in the section 13 figure with the same labels, and its quotes were already given in section 3 and the fold-out. Fix: keep the two-line test (acceptance and enforcement) plus the "strongest version", and cut the two "He asserts" paragraphs to the figure caption; the figure in section 13 already carries them. That saves about 200 words.

**13 Synthesis (-, 4, 4, 4, 3).**
- C3 (4): the box is now split into (a) and (b) paragraphs, which is better. The third paragraph is about 130 words of semicolon-chained clauses: "The nearer risk ... Losses would arrive together ...; with neither verification nor a reason ..., delegation fails; with one of the two, the worst case is the status quo (Lupia and McCubbins). An agent that hides its reasons removes the first. Supervisors and auditors can still verify ...". Fix: split into three short paragraphs (the nearer risk; delegation; what supervisors can still do).
- C4 (4): see (a) above: add the plain consequence for people. The chain figure's evidence tags are good ("2008 only ... with AI: none").
- C5 (4): the chain is clear and its dashed "ours" branch is now separate, so the round-2 mislabel is fixed. In the 390-px screenshot only step 1 shows, in a canvas about 500 px tall that is mostly empty (one box and one tag at the top, then blank until the text readout). A reader scrolling sees a big blank. The same happens, less severely, in dg-status and dg-llm. Fix: set the diagram height from the visible step, or show all nodes faded (`ghost`) from the start.
- C6 (**3**): the nearer-risk message appears four times (hook preview, short-answer paragraph 2, "Our reading (ours, qualitative)", and the Lens 3b "Adds"). The "Harari asserts ... predicts ... imagines" paragraph at the end of the box repeats section 3 for the third time. The fold-out repeats the four layers and the conditionals that the lens summaries have already given. Fix: delete the last box paragraph and the first two sentences of "Our reading"; keep the "Signs to watch" list, which is new.

**15 English (-, 5, -, -, 4).** C6: eight topic phrases, eight evidence phrases, four patterns and three fixes. Fix: fold "Small fixes" (already folded) and cut one of the two repeated expressions the paragraph-to-loop uses twice.

## First place a high-school reader gets lost

1. **First loss, section 3, "2008: complexity and a shared mistake":** "Harari's template is the 2007–08 crisis and its CDOs (collateralised debt obligations): pools of financial assets, such as the riskier tranches of mortgage-backed securities, sliced into tranches in a cash-flow 'waterfall'." "Mortgage-backed securities" is undefined, and "tranches" is used in its own definition. The toy right after rescues the reader, so this is a soft loss.
2. **First real conceptual loss, section 7, Lens 3a Ladder 1:** "The average has N terms of variance σ² and N(N−1) ordered pairs, each with covariance ρσ²." The rule that a variance of a sum includes every pair covariance is never given.
3. Third, section 5: "Spotting them is the 'hidden dense subgraph' problem." The graph is never drawn.

## Widget checks (does the reader do the mechanism? edge case? prose quotes the readout?)

All 15 configs parse. I reran every preset the prose quotes.

- **sw-contracts:** works. "1 cell pays 8, 6 pay 4, 9 pay 0" matches the table.
- **dg-waterfall + lab-cdo:** the reader drags p and w. The edge case "safe loans, p = 0.02" gives 2.000%, 0.0032% and 634.5 times: all quoted correctly. The default readout "1.0 times" and the w=0.5 readout "5.185% ... 14.0 times" match. The ratio "27 times" (10/0.37) is right. The screenshot shows the slider at 0.30 and 8.370%, which is just where the capture left the slider; the page default is 0.10.
- **dg-llm:** the steps work. The edge case ("Output nobody can check") teaches the Mik hedge ("may"). The canvas is tall for its content at step 1.
- **lab-count:** "k = 14" gives 16,383 > 10,000, so every contract could have a short name. "two days, k = 20" gives fraction 1.05e-10. Both match the prose. The "days" slider is hidden behind the preset labels, as noted in round 2.
- **dg-seller:** now shows the toy in the text (spread ¼ vs concentrated ½). Good. It shows placement, not hardness; the hardness is a conjecture.
- **dg-tree (fold-out):** consistent with the code check (9 / 27 / 81 inputs need 4 / 8 / 16 flips).
- **st-ashby + lab-ashby:** "free market" gives 9.29; "standard menu" gives V_D 6.64, V_O ≥ 2.64 (prose: 13.29 to 6.64, exactly half). The edge case (V_R past V_D gives 0) is in the prose. OK.
- **lab-neff:** "huge crowd, 0.3" gives N_eff = 3.257, as quoted. The readout mixes two quantities (N_eff, and "all wrong together"); the prose separates them ("A second question"). Acceptable. The 1.00e-200 at N=100 is a harmless oddity.
- **lab-bayes2 (fold-out):** n=10 gives odds 1,048,576 and P = 0.999999. Matches.
- **st-w5-hand + cs-w5:** the hand table ends "Y3 12 / 11, all six fail" and the widget reads "6 of 6 ... 3 rounds". capMult 1.5 gives 3 of 6, 0 more rounds, as in the prose. Seeded with X1, X2, X3. The playground answers were verified in round 2.
- **it-herding:** m=0.67 gives 2.68 up, −2.70 down, as quoted. m=0.9 with breaker 3 gives ±3.00, as quoted. m=0.2 is as quoted. The hand numbers (−0.9, −0.51, −0.189; −2.30, −3.94) are correct.
- **dg-status, dg-chain:** the steps work; see section 13 C5 about blank canvas.
- **Screenshot (390 px):** no horizontal page scroll. The three long formulas are now broken across two lines (aligned blocks), which fixes the round-2 note. The Lens 3b "bank j fails when Σ ..." formula still sits partly clipped and needs a swipe.

## Lens checks

| Lens | Says what it adds | Link type | Says what it does NOT explain | Verdict |
|---|---|---|---|---|
| 1 Information | Yes: "explainable novelty is rare among possible contracts ... a short rule does not make a price easy (Ladder 2, which borrows a complexity lens)" | same-math, structural analogy; the unused metaphor tag is gone | Yes: "whether an AI would pick opaque contracts" | Strong; links back to post 01 ("Shannon's counting") |
| 2 Control | Yes: "control needs variety, and there are three ways to get it" | same-math, structural analogy | Yes: "Ashby's disturbance is passive; finance adapts to its regulator" | Strong; "Across lenses" note ties to Lens 3 |
| 3a Correlation, Bayes | Yes: independent opinions depend on correlation, not headcount | same-math, structural analogy | Yes: "how much correlation real LLM-based desks have; ρ is assumed" | Strong; the meta line no longer promises game theory; links to post 01's likelihood ratio |
| 3b Cascades | Yes: "failure needs no mistake, only correlation, then a threshold or a feedback gain" | same-math, structural analogy | Yes: "how many firms really share a model" | Strong; the toy is labelled as trend-following, not a claim about LLMs |
| 4 Social reality | Yes: "'taking over money' splits into writing contracts (words) and giving them status" | structural analogy | Yes: "how any of it works in law" | Good; honest about the missing legal sources; links to post 01's octopus |

Link to Kunhao's research: section 12 is concrete (N_eff for LLM labelling and social-simulation agents, cross-lingual safety, who checks an online community's builds). Exercise 1 supplies the computation. Good. The "Lens N picks this up" notes in section 4 now carry link types.

## Audio listenability

The script follows the page and speaks formulas in words. Recaps end each chapter. About 5,700 words, roughly 28 minutes. Weak spots: the "home" chapter is long and sets out the four groups with six quotes by ear. The variance derivation in the "lens-decision" chapter ("sigma squared times one plus N minus one times rho, over N") is hard to hold without the screen, though it is spoken in words. "Range, index, ninety, one hundred ten" works only because the next sentence says what it means. The opening says "Welcome to AI4Read from CSS Lab." Nothing blocks.

## Post-level scores (minimum over sections)

| Criterion | Score | Lowest section(s) |
|---|---|---|
| 2 Ladder | **4** | Home field, LLM, Lens 1, Lens 3a, Lens 3b, Lens 4 (each 4) |
| 3 Clarity and English | **3** | Lens 3b (two dense numeric paragraphs) |
| 4 Insight and lenses | **4** | Home field (no link to post 01), Synthesis (consequence for people thin) |
| 5 Illustrations | **4** | Synthesis (mostly blank canvas at step 1) |
| 6 Concision | **3** | Lens 4 and Synthesis (the same chain and the same near-term-risk message repeated) |

**Gate (every criterion at least 4): not met on criteria 3 and 6.** Everything else is at 4 or 5. Both failures are cheap to fix, and neither needs new content. Round 2 had three criteria below 4 (2, 3, 6); criterion 2 is now at 4.

## Top three changes

1. **Turn the two dense number paragraphs in Lens 3b into tables, and state the variance-of-a-sum rule in Lens 3a.**
   - Add a loan table (borrower, lender, amount, capital) before the Ladder 3 mechanism. Add a three-row table for Ladder 4 (m, push, pull, the next gaps). Put "Intuition" and the tipping point in their own paragraph.
   - Add one rule sentence and a one-line N=2 check to the N_eff derivation.
   - Replace the circular CDO definition with one plain sentence.
   - This lifts C3 for Lens 3b from 3 to 4, and C2 for Lens 3a and the home field.
2. **Say each repeated message once.**
   - Cut Lens 4's two "He asserts" paragraphs to the section 13 figure. Cut the closing paragraph of the short-answer box. Cut the first two sentences of "Our reading" in section 3. Cut the Truth Terminal valuations and the "stabilise and destabilise" sentence. Cut the "nothing to search" sentence in Lens 1.
   - This removes about 400 words (under 6%) and the three-fold repetition of the Harari classification and the near-term-risk message. It lifts C6 for sections 9 and 13 from 3 to 4.
3. **Sharpen half (b) and fix the figure space.**
   - Add the plain consequence for people to (b) ("if nobody can verify, ... nobody can be held to account"). Split the third paragraph of the box into three short paragraphs.
   - Make the chain figure (and dg-status, dg-llm) show all nodes faded from step 1, or size the canvas to the revealed step, so a phone reader does not scroll past 500 px of blank.
   - Add one sentence in the Lens 1 Ladder 2 scale-up saying what the graph is (dots and groups of dots).
   - This lifts C3, C4 and C5 for section 13.

## (b) Status of round-2 top changes

| Round-2 change | Status | Evidence |
|---|---|---|
| 1. Climb the hardness step in Lens 1 Ladder 2; split dense paragraphs; cut C(100,10) and the unused metaphor tag; redraw the seller diagram | **Mostly addressed** | The six-asset toy (¼ vs ½) is in the text and in `dg-seller`. "Derivative" is defined at first use and "intractable" is glossed ("no fast method is known, and none is expected (a conjecture)"). Ladders 1-2 are short labelled lines. The C(100,10) aside and the metaphor tag are gone. "Adds" now says Ladder 2 "borrows a complexity lens". Still open: what the "graph" in "hidden dense subgraph" is. |
| 2. Say the Harari split once; clear jargon in sections 3-4; add a number to the option; give "Lens N picks this up" a link type | **Partly addressed** | "Incentive compatible" and "deep hedging" are gone ("search for auction rules (who wins, who pays) or for hedging strategies"). The option example has numbers. Each "picks this up" now has a link type. The trap moved into the fold-out and the Prediction 4 answer is short. Still open: the body table carries nine cites, and the classification still appears in section 3 (table plus "Our reading"), section 9, section 13 (box and figure), the recall cards and the English patterns. The Truth Terminal valuations are still there. |
| 3. Sharpen half (b); split the answer box; fix the chain figure and reveal its edges per step; define covariance; add the odds line; split the worked-numbers lines and the "Our test" paragraph | **Mostly addressed** | The literal conditional is in the box, split into (a)/(b). The chain's dashed "ours" branch is separate and its edges now appear step by step. Covariance is in the term box. The odds line (1:1, 4:1, 16:1) is in the main text. The Lens 3a meta line is renamed. Formulas are broken into two lines. Still open: Ladder 4's worked-numbers table, the "Our test (ours)" paragraph, the plain consequence for people in (b), and the blank canvas under the chain figure on a phone. |
