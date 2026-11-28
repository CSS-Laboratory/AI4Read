# Critic round 3 (S5, blind pedagogy review): "How much is a surprise worth?"

Read: `src/content.html` (all), built `index.html` at 390 px (Playwright; 0 console errors, no horizontal scroll, scrollWidth 390), `check.mjs` readouts (9/9 widgets OK), the notebook, `audio-script.md`. Main text 7,044 words (cap 7,500). I read `critic-2.md` and `response-2.md` only after scoring.

Widget runs, all at 390 px: card-lab village day, three presses of "Join the two rarest": 1.750 = H. Joining the first two groups each time: 2.625 against best 1.750. 0.7 day: 1.500 against H 1.357. Equal day: 2.000. Every number matches the prose. Chips, Undo and Start again work. Page readouts equal `check.mjs`.

## Section scores (criteria 2–7; n/a = nothing to judge)

| Section | 2 Layers+ladder | 3 Clarity | 4 Lenses | 5 Widgets | 6 Concision | 7 CSS imag. |
|---|---|---|---|---|---|---|
| 1 Hook (layer 1) | 4 | 4 | n/a | n/a | 4 | n/a |
| 2 Café (layer 2) | 5 | 5 | n/a | 4 | 4 | n/a |
| 3.1 Equal chances | 5 | 4 | n/a | 4 | 5 | n/a |
| 3.2 Surprisal | 4 | 4 | n/a | 5 | 4 | n/a |
| 3.3 Entropy | 5 | 4 | n/a | 5 | 4 | n/a |
| 3.4 Submarine | 5 | 4 | n/a | 5 | 5 | n/a |
| 3.5 Encode/decode | 5 | 5 | n/a | 5 | 5 | n/a |
| 3.6 Not halves | 4 | 4 | n/a | 4 | 4 | n/a |
| 4 Short answer + what it is | 5 | 4 | 5 | n/a | 5 | n/a |
| 4b Lenses | n/a | 4 | 4 | n/a | 4 | n/a |
| 4c Where it fails | 5 | 4 | 5 | 5 | 4 | n/a |
| 5 CSS imagination | n/a | 4 | n/a | n/a | 4 | 4 |
| 6 Turn + notebook | 4 | 4 | n/a | n/a | 5 | n/a |
| 7 Recall | 4 | 5 | n/a | n/a | 5 | n/a |

### Evidence and fixes for each score below 5

**1 Hook.**
- C2: the pain is the author's own example ("In a town where it rains most days…"). The real practice is one Hartley sentence, and the guess defines "worth" and "fair yes/no questions" before layer 2. This is acceptable, but thin and slightly new-concept-ish (C3-07).
- C3: "Hartley himself saw that E is chosen more often than Z, and that this should govern the lengths of Morse signals, if messages are to be sent most swiftly" is a heavy sentence, carrying one citation each.
- Fix: keep the Morse point, which is the real pain. Cut one Pierce citation and add one concrete number.

**2 Café.**
- C5 (4): the two trees are static. This is right for a scene, and the reader builds the card in step 6.
- C6 (4): the "parts" list and "Who does what" repeat each other, and step 5 repeats the roles again. Fix: cut "Who does what" to three sentences, since the parts list and step 5 carry the rest.
- Layer-2 audit: no formula, symbol, abbreviation or unexplained term. "script" and "string" are defined in the sentence (`dfn`); "share", "worth", "ticket's length" are in the parts list. The hatch and the loud grinder make the shared card necessary, and the text says so: "'no, no, yes' means mocha only under this card, so the same card must hang on both walls". Nothing found.
- One loose phrase: "a card built for the old shares would do worse than the plain board". "Old shares" has no referent. Fix: "a card built for the owner's shares".

**3.1 Step 1.**
- C3: "Shannon has 'successive symbols being chosen independently', and so do we" uses "independent" with no plain definition (C3-04).
- C5 (4): the halving and rats are text only. A small tap-halve widget is optional. The notebook and the table carry it, so this is not a finding.

**3.2 Step 2.**
- C2: the "pattern" is "how many times you must halve the whole crowd to be left with a group the size of its share". It is exact for halves only. At 0.3 the post says "worth 1.74", but a fractional number of halvings is not explained (C3-10). The ladder is complete (instance, tickets 0/10/110/111, E2, check, slider, break).
- C3: the Gibson sentence is the first place where a high-school reader gets lost (C3-05).
- C6: Gibson's naming and MacKay's naming are given in the main text. Fix: move one of them to a fold-out.

**3.3 Step 3.**
- C3: E5 uses "EQ" in the formula, and "short for the expected number of questions" comes after it. WRITING §3: define before use. Fix: write "Let EQ stand for the expected number of questions. For a script that spends L(x) questions on word x:" before the formula (C3-04).
- C6: three settings, EQ, "What it means" and "Check yourself" together are about 530 words. Acceptable. Fix: merge "Three settings" into the widget caption.

**3.4 Submarine.**
- C3: E8 has a product of eight-plus fractions, an underbrace and a one-line explanation of the cancellation. It is correct and the 4-square check precedes it, but it is dense. Fix: show the 4-square cancellation as "4/3 × 3/2 × 2/1 = 4" in one line before E8.

**3.6 Step 6 (the new ladder).**
- C2 (4): instance (card-lab, 4 groups), then what happens (three days), then the rule (Huffman), then E9, then the check ("1.357 ≤ 1.500 < 2.357") are all present, with the reader building the card. Two rungs are thin (C3-01): why the two *rarest* are joined, and why a join counts as one more question. The post only says Cover and Thomas prove it.
- C3 (4): the "What happens" paragraph carries about 25 numbers and a tie-break aside, against the house limit of about 5 (WRITING §5), and the "Where it holds" paragraph carries 6 citations. The ambiguous "gap, 0.143" is in it (C3-02).
- C5 (4): the widget works. The caption says "watch the average rise", but the average shows only when the card is complete (C3-08).
- C6: this section carries the post's densest density, but it is the post's new material, so about 5% could go.

**4b Lenses (C4 = 4).**
- Link types are named: same-math (the form of the sum only), structural analogy ×2, same-math. Each has "Adds" and "Does not explain", plus a comparison paragraph and 3C. Lens 1 is thin: "Adds: the sum is about distributions wherever shares exist" tells the reader little. Lens 2 is carefully hedged, but its "Adds" line ("the one lens whose claim is about behaviour (ours)") is a claim about the lens set, not about what the lens adds to understanding surprisal.
- Fix: for lens 1, add what thermodynamics adds that the others cannot (a physical reading of "number of arrangements"), or merge it into one line.

**4 Short answer, 4c Where it fails.**
- C3 (4): the short answer has dense but good sentences. The seven boundaries each name an assumption in section 3 and where the café breaks.
- C6: 4c is about 575 words, and boundaries 6 and 7 could be one paragraph each at 40 words.

**5 CSS imagination (C7 = 4).** Moves used as reasoning:
- Extremes and inverted scale: 30 million listeners, "who writes the forecast, and who pays when it is wrong".
- Trouble and issue: the 200-message reader, with a testable condition ("if changing the ranking changes what many readers miss, and individual effort does not…").
- Another discipline's eyes (psycholinguist, journalist).
- Comparison, in RQ 2.

Two open questions have data, method and a caveat. Society claims are labelled ours or hypothesis. Weak points:
- Move 1 states H = 0 and H = 2 and then reasons only from the 30 million. The extremes are decoration. The reasoning that "one forecast prices all of them" is simply the definition of a shared model.
- Move 3 ends with the unsupported assertion "Neither asks who owns the model."
- Fix: for move 1, push the share of snow to 0 in the forecaster widget (surprisal infinite, the forecast is *refuted by a single snowfall*), which is a real extreme the reader can try. For move 3, replace the last sentence with what the journalist's question predicts that the number cannot (C3-09).

**6 Your turn and notebook (C2 = 4).** Difficulty climbs mostly: ex 1 (functions), 2 (two forecasters), 3 (simulate and round-trip decode), 4 (submarine sums), 5 (own text), 6 (bias), 7 (Huffman, bound), 8 (optional weighing). Exercise 5 is easier than 3 and 4, and exercise 7 is the first one to need `heapq`. The hint gives the heap layout, so nothing is required that is not taught or hinted. Notes:
- Ex 2 asks what happens at share 0. The post defines the 0 convention for entropy only (not surprisal), so the exercise leaves a decision to the reader. The hint says so. Fine, not a finding.
- Fix: swap exercises 4 and 5, so the notebook does not dip in difficulty.

**7 Recall (C2 = 4).** All questions use only this post. Eight cards, no distractors. Card 4: "when would the best script average exactly 2?" has the answer "With four equally likely words, H = 2." Not unique: shares 1/2, 1/8, 1/8, 1/8, 1/8 also give 2.000 (C3-10).

## Layer checks (WRITING §1a, §1b)

- **Layer 1:** no new concept beyond the defined guess prompt (C3-07). It opens with the pain, names real practice (Hartley, Pierce, Morse), and ends with a guess.
- **Layer 2:** no formula, symbol, abbreviation or unexplained term found. 0 findings. The café needs the shared card (loud grinder, back room, tickets) and says so. The parts are listed.
- **Layer 3:** every equation (E1–E9) has an "In the café" line that maps each term in words. E6 and E7 sit in fold-outs and have lines. Ticket length (whole questions) and worth are kept distinct in the parts list, E2, E4 and E9 lines and the step-6 table. Step 6 is a ladder, using the card-building widget.
- **Layer 4:** (a) grows from E2 and E4 ("This is E2 and E4 without the café"); (b) four lenses, each with link type, adds and does-not-explain; (c) seven boundaries, each "Assumption" in section 3 and "The café breaks".
- **Layer 5:** three moves used as reasoning (a fourth, comparison, inside RQ 2) and two research questions with data and method; claims about society are labelled ours. Residual: C3-09.
- **Who encodes and who decodes:** crystal clear. Step 5 names the roles, walks "no, no, yes" through them, draws the three-step diagram, resolves MacKay's wording and ends with the mismatched-card exercise. The café settings make it hard to confuse.
- **Quizzes:** answers are not given before their reveal (g1 in step 4, g2 in step 6, g3 in step 1). No answer text appears earlier. Distractors are serious and similar in length, except g1's correct option, which is the longest and most specific (63 characters against 57–59; C3-06). Recall tests only this post.

## Findings

All are minor. Critical 0, major 0, minor 11.

| ID | Severity | Where | Finding | Fix |
|---|---|---|---|---|
| C3-01 | minor | 3.6 rule | The ladder is complete, but two rungs have no reason: why the two *rarest* join, and why a join counts as "one more question on every ticket". The picture was cut (response-2 C2-02). A strong 17-year-old will ask both. The post only says Cover and Thomas prove it. | Add two sentences: "The longest tickets belong to the rarest drinks, and the two longest differ only in their last answer: the card's last question separates exactly those two. So join them, then repeat." And: "A join is that last question; every word under it gets one more." |
| C3-02 | minor | 3.6 "What happens" | "Rain is worth 0.515 questions, but its ticket cannot be shorter than one; the gap, 0.143, is the price of whole questions." The nearest gap a reader computes is 1 − 0.515 = 0.485. The 0.143 is EQ − H = 1.500 − 1.357. A check on the page gives a different number (WRITING §5). | "Rain's ticket is 0.485 longer than its worth. Over all four words the average ticket is 1.500 − 1.357 = 0.143 longer than H." |
| C3-03 | minor | 3.6 "What happens", "Where it holds"; audio `nothalves` | About 25 numbers in one paragraph and 6 citations in the next (house rule: about 5 numbers). On a phone, and spoken in the audio, the 0.7 arithmetic loses the listener. | Put the three days in a 3-row table (days; tickets; EQ; H). In the audio say "average one point five, against H of one point three six" and leave the sum for the page. |
| C3-04 | minor | 3.1, 3.3 | "Independent" is used at first use (step 1 Shannon quote, step 2 "The days are independent") with no plain sentence; the only plain example comes in boundary 3 (a rainy morning makes hot drinks likelier). "EQ" appears in E5 before it is defined. | At first use: "Independent: one day's word does not change the chances of the next day's." Define EQ before the formula. |
| C3-05 | minor | 3.2 "What it does not say" (first place a high-school reader gets lost) | "…the shortest uniquely decipherable script (a script whose rows of answers can be cut back into words in only one way)". The café has one ticket per customer, so nothing is ever concatenated and "cut back into words" has no scene. The gloss is correct but sits outside the story. | Move the sentence to the 4(a) paragraph where it is repeated, or say "tickets stapled end to end". Keep step 2 on whole-versus-fractional. |
| C3-06 | minor | Guess g1 | Correct option A ("Almost nothing, because one miss rules out only one square of 64") is the longest and most specific (about 63 characters against 57–59). WRITING §5 says the right answer must not be longest or most specific. | Shorten A to "Almost nothing, because one miss rules out one square of 64", or lengthen the others by one clause. |
| C3-07 | minor | 1 Hook | The guess uses "news is worth the questions it saves you" before the café. The pain is the author's own constructed example; the real practice is one sentence. | Open with the real pain (Morse lengths from Pierce), then the town as an illustration. Keep the guess as it is. |
| C3-08 | minor | card-lab | Caption: "Try a bad join and watch the average rise." The average shows only when the card is complete, and "rise" is relative to the best (1.750). | Caption: "…finish a bad card and compare its average with the best." Or show the running average of the finished groups. |
| C3-09 | minor | 5, moves 1 and 3 | Move 1 states two extremes (H = 0, H = 2) and then drops them. The 30 million paragraph is a definition of a shared model. Move 3 ends on an unsupported assertion ("Neither asks who owns the model"). | Move 1: use the forecast widget at share 0 (a single snowfall gives infinite surprise), then 30 million. Move 3: say what the journalist's question predicts and the number cannot. |
| C3-10 | minor | 3.2 pattern; 7 recall card 4 | "How many times you must halve" is not whole for 0.3 (1.74), and the text never says what a fraction of a halving means. Recall card 4 "when exactly 2" has the answer "four equally likely words", which is not unique. | Add "(for other shares, read it as the same count with fractional halvings: the formula still gives the number)". Card 4: "…for example when all four words are equally likely." |
| C3-11 | minor | Whole post (concision) | About 8% could go without loss: the café "Who does what" paragraph (repeated in step 5), 41 "(ours)" tags (keep those on numbers and claims only), Gibson naming sentence in step 2, one of the two Mills hedges in layer 5, boundaries 6 and 7 as short paragraphs. | Cut about 500 words to about 6,550. |

## First sentence where a high-school reader gets lost

Step 2: "So Gibson and colleagues say the information content *approximates* the length of the shortest uniquely decipherable script (a script whose rows of answers can be cut back into words in only one way)." The scene has no concatenated tickets, and the sentence turns on citation hedging as well as on a new concept. Everything before it, including layer 2, steps 1, 4 and 5, a high-school reader can follow. (C3-05)

## Post-level scores (minimum over sections)

| Criterion | Score |
|---|---|
| 2 Four Layers and ladder | 4 |
| 3 Clarity and English | 4 |
| 4 Insight and connections (layer 4) | 4 |
| 5 Illustrations and interactives | 4 |
| 6 Concision | 4 |
| 7 CSS imagination | 4 |

Criterion 1 belongs to the fact-checker. Counts: critical 0, major 0, minor 11. Gate (every criterion at least 4, 0 majors) met from the pedagogy side.

## Round-2 critic majors: resolved?

| ID | Round-2 finding | Status | Evidence |
|---|---|---|---|
| C2-01 | Predict-first answer stated above it | Resolved | The exercise is now "reversed" (rain and sun 1/8, wind 1/4, snow 1/2). The answer 2.625 against H = 1.750 is not above it; the 2.25 sentence in E5 now points to section 2's check, and the widget preset that showed 1.500 was removed. I ran "reversed" and read 2.625. |
| C2-02 | Best-script rule thin, no ladder, no picture | Mostly resolved | A real ladder is there: guess, instance (card-lab), what happens (three days), the rule with citations, E9, the check on the three days, and "where it holds". Still no reason for "rarest first" or for join = question. Now minor (C3-01), not major, because the reader builds the card, sees the tickets and the bad-join cost, and the post says honestly that it cites the proof. |
| C2-03 | "Cost" means ticket length and worth | Resolved | The parts list has "A ticket's length… whole number" and "An order's worth… worth and ticket length agree [for the four drinks]; section 3 shows when they do not". The E2, E4 and E9 café lines use both words correctly. The step-2 sentence "no ticket has 3.3 answers" comes before the plot. Residual ambiguity in one number (C3-02). |
| C2-04 | Hook too dense; independence quote undefined | Resolved | The hook is 304 words with one history paragraph; the independence quote moved to a fold-out. "Independent" is still undefined later (C3-04, minor). |
| C2-05 | No widget lets the reader build a card | Resolved | `cardlab` runs at 390 px: tap two groups, join, undo, preset days, "Join the two rarest". Numbers match the prose and `check.mjs` (1.750, 2.625, 1.500, 2.000). Residual caption wording (C3-08). |

## Three changes that would raise the post most

1. **Step 6: give the two missing reasons and replace the number-heavy paragraph with a table.** The two rarest drinks get the longest tickets, and a join is the card's last question (C3-01). Put the three days in a table and fix the "gap" wording (C3-02, C3-03). This also helps the audio chapter.
2. **Define "independent" and "EQ" at first use, and move the Gibson "uniquely decipherable" sentence out of step 2** (C3-04, C3-05, C3-10). That removes the first lost-reader point and keeps steps 1–2 on one idea each.
3. **Trim about 500 words and sharpen layer 5** (C3-11, C3-09): use the share-0 extreme in move 1 and a real prediction in move 3. Rebalance g1's options (C3-06). Together these lift criteria 3, 6 and 7 toward 5.
