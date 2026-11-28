# Critic 2 (S5 round 2): blind pedagogy review

Post: `posts/2026-12-surprise` (information theory, week 1). Reader model: Kunhao, phone, B2-C1, high-school level outside his field.
Read: `src/content.html` (all), built `index.html` at 390 px (no horizontal scroll, 0 console errors), `check.mjs` readouts, notebook, `audio-script.md`. Main text 6,844 words (ceiling 7,500).
Written before reading `critic-1.md` and `response-1.md`.

## A. Section scores (criteria 2-7; "-" = not applicable to the section)

C2 = Four Layers and ladder; C3 = clarity and English; C4 = layer 4 insight; C5 = illustrations; C6 = concision; C7 = CSS imagination.

| Section | C2 | C3 | C4 | C5 | C6 | C7 |
|---|---|---|---|---|---|---|
| 1 hook (layer 1) | 4 | 3 | - | 4 | 3 | - |
| 2 cafe (layer 2) | 5 | 5 | - | 5 | 5 | - |
| 3.1 equal chances | 4 | 4 | - | 4 | 4 | - |
| 3.2 surprisal | 4 | 4 | - | 5 | 4 | - |
| 3.3 entropy | 3 | 4 | - | 4 | 4 | - |
| 3.4 submarine | 4 | 4 | - | 5 | 4 | - |
| 3.5 roles | 5 | 5 | - | 5 | 5 | - |
| 3.6 not halves | 3 | 4 | - | 4 | 5 | - |
| 4 answer + (a) what it is | 4 | 3 | 4 | - | 4 | - |
| 4(b) lenses | 4 | 4 | 4 | - | 4 | - |
| 4(c) fails | 5 | 4 | 5 | 5 | 4 | - |
| 5 imagination | - | 3 | - | - | 4 | 4 |
| 6 turn + notebook | 4 | 4 | - | - | 5 | - |
| 7 recall | 4 | 4 | - | - | 5 | - |

### Evidence and fixes, section by section

**1 Hook (C2 4, C3 3, C5 4, C6 3).**
- C3 evidence: "Pierce says this is acceptable only if successive symbols 'are chosen independently' and each 'is equally likely to be selected'". Layer 1 has not said what a symbol is or what "independently" means, and this sentence stacks two quotes on one citation. The whole second paragraph is about 190 words and carries seven citations.
- C2 evidence: layer 1 should introduce no new concept, but the guess-first uses "worth" and "fair yes/no questions", and its first option ("a few hundredths of one question") already tells the reader that fractions of a question exist. "(in fact by a function of that number, which step 1 explains)" is a forward pointer to an unnamed idea.
- Fix: cut the Nyquist and Hartley paragraph to about 90 words. Keep "counting messages gives 'it rained' and 'it snowed in July' the same score" and "Hartley noticed E is commoner than Z". Move the independence quote to the Look-inside box "Nyquist and Hartley". Replace the forward pointer with "(a logarithm of that number; step 1 explains)".
- C5 evidence: guess g1 is well built (four serious options, no earlier leak), but the correct option is the only one with no "because" clause; this is a format tell. Fix: give option 1 a reason ("because one miss rules out only one square in 64").

**2 Café (C2 5, C3 5, C5 5, C6 5).**
- Layer 2 passes. No formula, symbol or abbreviation, and every term is explained in the sentence: "We call the card the script, and the row of answers on a ticket its string."
- The café makes the shared script necessary: "'no, no, yes' means mocha only under this card, so the same card must hang on both walls before the day starts", and the grinder and back room remove any live talk.
- The scene is told with old way, break point and changed rule, and ends with a parts list.
- The two diagrams, in a switch, do the old-versus-new comparison. 1.75 against 2 is checked by hand.
- Nothing to fix. One caution carried to step 2: the parts list defines "a drink's cost" as "the answers on its ticket" (whole numbers) and says "one question ... one second". See C2-03.

**3.1 Equal chances (C2 4, C3 4, C5 4, C6 4).**
- Ladder: instance (rats), steps (32, 16, 8, 4, 2, 1), pattern, E1, check (log2 32 = 5; "four rats cannot decide 32 cups"), and a café line. Complete.
- C2 gap: the rats are a third scene beside café and village, and the guess is a parallel test ("all the rats drink at the same time"), not the sequential card of layer 2. Nothing says how the rats map to the café; the "In the café" line maps N, k and 2 but not the rats.
- C3: the MacKay sentence "a lower bound for the number of binary questions that are always guaranteed to identify an outcome" is hard at B2, and the gloss "guaranteed means in the worst case" comes after it.
- Fix: one sentence after the answer: "Five rats at once is the same as five questions on a ticket, filled in together." Put the gloss before the MacKay quote or drop the quote.
- Guess g3: distractors are serious and of similar length (58-71 characters), and the answer is not the longest. Nothing earlier leaks it.

**3.2 Surprisal (C2 4, C3 4, C5 5, C6 4).**
- Ladder: instance (0, 10, 110, 111), pattern (halve the crowd), E2, check (snow log2 8 = 3; MacKay's table by slider), and a limit ("Only shares that are powers of one half cost a whole number").
- The plot readout is quoted correctly ("p = 0.100 ... 3.3 questions"; the table values 10.0, 6.6, 3.3, 2.3, 1.0 match log2). The edge case at p = 1 is stated.
- C2 evidence (skipped step): "a log turns a product into a sum". The reason (2^a x 2^b = 2^(a+b), so exponents add) is never given. The 16 = 2 x 8 example shows it for one case only, and recall card 1 depends on it.
- C2 evidence (café map): "h(x) is the drink's cost: the answers on its ticket under the best script". That is true only for shares that are powers of one half; for share 0.1 it is 3.3 against a ticket of 3 or 4. The hedge sits in a paragraph above the café line, not in it. See C2-03.
- Fix: add one sentence to E3 ("because 2^a x 2^b = 2^(a+b): multiplying the crowds adds the halvings"); make the café line say "equal to the ticket length only for shares 1/2, 1/4, 1/8 ...".

**3.3 Entropy (C2 3, C3 4, C5 4, C6 4).**
- Ladder is complete otherwise: instance (eight days, 14 questions, 1.75), words, E4 with sign read aloud, before and after (2.000 to 1.750), "what it means".
- C2 major evidence: the exercise "Predict first, then use the widget: what does the village script cost on a day when all four words are equally likely?" is answered in the paragraph just above it ("On a village where all four words have share 1/4, the same script ... averages 2.25"), and again in section 2's check (b). The prediction is void. See C2-01.
- C2 map slip: "In the café. Σ: go through the day's customers". The sum runs over the drinks, each weighted by its share, not over customers. The audio script repeats it.
- C5: the lab sets the shares but hard-wires the script lengths (1, 2, 3, 3). The reader never builds or reorders a card, which is the layer-2 mechanism. See C2-05. Edge cases (all equal, only rain, reversed, 0.7) are well chosen and quoted correctly: the readout shows 1.750, 2.000 and 2.250 for the cases the prose names.
- Fix: delete "On a village where all four words ... 2.25 ..." from the main text (keep it in the exercise answer), or turn it into the exercise.

**3.4 Submarine (C2 4, C3 4, C5 5, C6 4).**
- Ladder: instance, plain words, a hand check on four squares (0.415 + 0.585 + 1.000 = 2.000), E8 with the telescoping product, slider. Quoted numbers match the readouts: shot 2 gives 0.0227 and 5.9773; shot 33 gives exactly 1 and 5; shot 49 gives 2 and 4; shot 64 gives 6 and 0.
- The widget is a real "do the mechanism" widget: choose when the hit comes and watch the total stay at 6.
- C2 evidence: the café line says "A no on the ticket costs 0.0227 of a question". Layer 2 said every answer costs one question. The reader has no word for "one answer of the ticket" against "the news that answer carries". See C2-03.
- C3: "Move the slider ... and check the rows" refers to rows that do not exist (the widget shows a readout). Say "read the readout".
- The café line's claim "Whichever path the customer takes, the total worth ... is the same: the cost of that drink" is proved only for equal shares (the grid). Add "(for unequal shares the same chain of fractions holds; ours)" or say it only for the grid.

**3.5 Who encodes, who decodes (C2 5, C3 5, C5 5, C6 5).**
- Crystal clear. Roles are defined once ("The encoder holds the original ... and the agreed script ... The decoder holds only the string and the same script"), walked through one example (110 for mocha), drawn in the stepped diagram, and mapped in the café line. The MacKay "asker encodes" confusion is named and resolved.
- Exercise (different card order) tests exactly the shared-script point, and its answer is not given earlier.
- Minor, in the fold-out "Shannon's twin game": "The side with the original text and a predictor encodes". The guesser, who has not seen the text, is the predictor; the one who knows the text only says right or wrong. State that the encoding side is the guesser plus the person who knows the text. Fold-out, so minor (C2-12).

**3.6 When shares are not halves (C2 3, C3 4, C5 4, C6 5).**
- C2 evidence: the ladder runs backwards. After the guess, the section opens with the formula E9 ("H <= EQ* < H + 1"), then the 0.7 instance. WRITING §2: "Do not start a concept at step 4."
- C2 major evidence: the construction of the best script is one sentence, "repeatedly join the two rarest outcomes into one group, and every outcome inside the group gets one more question", introduced as "A rule, ours". The café rule is "split the customers", top-down; this rule is bottom-up, and the post never says why joining the rarest is right or why the result is "best". The check "1.357 <= 1.5 < 2.357" does not show 1.5 is the best. The reader meets 1.5 without the means to find it. See C2-02.
- C5: no figure for the new mechanism; the join steps are prose.
- The answer to g2 (1.50) is not given earlier in the prose, but the step-3 preset "0.7, 0.1, 0.1, 0.1" shows "Village script ... 1.500", the answer, to a reader who clicks it (C2-11). Distractors (1.00, 1.36, 1.50, 2.00) are the same length, and 1.36 is a serious trap (the entropy).
- Fix: put the instance first. Show the 0.7 village with its three "naive" scripts (halve the crowd as evenly as possible). Then give the join rule as a four-line table (step, group, new lengths), say why the two rarest go deepest (the card spends questions where customers are), and say "best" is shown by the notebook search, not here. Then state E9. Add the 0.515 against 1 whole question line to the table.

**4 Short answer and (a) What it really is (C2 4, C3 3, C4 4, C6 4).**
- Short answer: verdict given, labelled ours, with what would change it. Good. The last sentence, "evidence that the number predicts something beyond improbability (lens 2: one such claim, whose evidence we have not checked)", is hard to parse.
- (a) is one 190-word paragraph with nine claims in a row and six citations. Evidence: "(approximates is the authors' word; 'uniquely decipherable' means no string is the start of another, so a run of answers can be cut into words in only one way)". Step 2 defined the same term differently ("rows of answers can be cut back into words in only one way"). "No string is the start of another" is the prefix property, which is stronger than unique decipherability (C2-08).
- Fix: split (a) into three short paragraphs (surprisal; entropy and its bounds; surprisal and code length). Use one gloss, "no ticket is the beginning of another, so the barista can cut a long run of answers into drinks".
- The fold-out on Shannon's three properties is fine.

**4(b) The same idea elsewhere (C2 4, C3 4, C4 4, C6 4).**
- Each lens gives a link type, Adds and Does not explain. The hedges are kept ("Read the hedge ... their word is predictability, not surprisal"). No link to another post.
- C4 (4 not 5): five lenses (WRITING §1a says 2-4). Lens 1 (statistical mechanics, "a box of four cells") and lens 3 (communication theory, "Adds: the roles") add little the reader can use, and the lenses are not compared with one another.
- Fix: fold lens 3 into step 5 (it is the café's role map) and shorten lens 1 to two sentences. Add one line that says which lens changes how Kunhao reads a result, for example lens 4 (surprisal belongs to a believer) against lens 2 (an empirical claim).

**4(c) Where it fails (C2 5, C3 4, C4 5, C5 5, C6 4).**
- This is the best section. Each of the six boundaries names the assumption in section 3 and then says "The café breaks:" ("the cash register's record gets old, and the village script costs 2.25 on a uniform day"; "a real barista ... can ask live"). Boundary 4 has a two-forecaster widget with an edge case ("same belief"). Boundary 5 has a table of numbers from the notebook (1.504, 1.675, 1.725, 1.747), which match `notebook/results.md`.
- C3: "must not change with time if the source is to be ergodic" uses "ergodic" with no gloss (C2-09). Boundary 6 packs four ideas (fixed script, whole questions, no noise, no feedback) into one paragraph.
- Fix: gloss ergodic in six words ("keeps the same long-run shares") or drop the clause. Split boundary 6 into "fixed in advance" and "no noise".

**5 CSS imagination (C3 3, C6 4, C7 4).**
- Moves used as reasoning: extremes and inverted scale ("Give the weather village 30 million listeners ... one forecast now prices all of them ... their surprise is correlated (ours). What changes is who writes the forecast, and who pays when it is wrong"); trouble and issue with a test ("if changing the ranking changes what many readers miss, and individual effort does not, the cause lies in an arrangement"); another discipline's eyes (psycholinguist, journalist). Comparison appears only inside research question 2. Mills is quoted with hedges.
- Two open questions, each with data, method and a 3C tie. Both are labelled ours.
- Why not 5: (1) Move 1's trouble is not tied to an entropy mechanism: how does a "ranking that orders messages by how surprising they are" follow from E2? The Pierce quote about art is about surprise in another sense. (2) Move 3's claim "a rumour and a budget can carry the same surprisal" is ours and unillustrated. (3) Research question 1 admits "We have not checked the prior work on novelty and spreading", which weakens an invitation to start a project. (4) Comparison (a second society, period or platform) is not used on its own.
- C3: the first paragraph is Mills quotes plus caveats about editions and move names (about 130 words before any reasoning); "milieu" is used raw.
- Fix: open with the 30-million extreme (the post's own idea), then trouble and issue. Move the edition caveat to Sources. In Move 1, give the one-line link ("a ranker that favours the improbable decides, for every reader, what counts as news; that is E2 with a single model"). Name one real comparison (two platforms, or the same platform before and after a dated event) as move 4 before research question 2.

**6 Your turn and notebook (C2 4, C3 4, C6 5).**
- Transfer challenge: hint and solution given; its numbers check (1.875 = H; old script costs 2.5 on the new shares; H = 2.25).
- Notebook: eight exercises with predict-first prompts, hints and folded solutions. It needs nothing the post does not teach, with these exceptions. Exercise 5 uses "unigram" (explained only in the hint) and compares with MacKay's 4.11 and Shannon's 4.03, numbers the post never gives. Exercise 8 (c) asks for 1,050 random share vectors with no hint for how to draw them (the solution uses a Dirichlet draw). Exercise 8 calls the join rule "the Huffman method", while the post calls it "ours".
- Difficulty climb: ex 1 (easy), 2 (simulate and decode), 3 (loop), 4 (easiest, two lines), 5, 6 (multinomial, standard error), 7 (optional extension), 8 (heap). Exercise 4 is a dip after 2 and 3, and the optional 7 sits between 6 and 8. Fix: swap 4 to follow 1, put 7 last, give a hint for random shares, drop the MacKay and Shannon numbers or give them in the post.

**7 Recall (C2 4, C3 4, C6 5).**
- Eight cards, all answerable from this post; the "outside idea" trap is avoided (the Gibson card names a claim the post itself quotes). Card 4 and card 7 are good.
- Fix: card 8 tests a citation detail ("Which statement of Gibson and colleagues is an empirical claim") rather than an idea; replace it with "Two forecasters, same snow: why do they get different numbers?" (boundary 4). Add a card for the best-script rule once step 6 is repaired.

## B. Layer checks

- **Layer 2 formulas, symbols, abbreviations, unexplained terms:** none found in section 2 (read word by word, including captions and diagram labels). Count: 0.
- **Layer 3 "In the café" lines:** present for E1, E2/E3, E4/E5, E6, E7, E8, step 5, step 6. Mapping slips: the sum sign over "customers" (3.3); "cost = ticket answers" for non-dyadic shares (3.2); E9's EQ* and H are named only in prose. The post's own sentence for E9 ("Here EQ* is the EQ of the best script") is not mapped to a café part (C2-09).
- **Layer 4:** all three parts present; "Where it fails" grows from layer 3 ("Each boundary is an assumption you can find in section 3, with the place where the café breaks") and shows where the analogy breaks six times. Each lens states link type, adds, does not explain. Five lenses (guideline 2-4).
- **Layer 5:** moves 1-3 are reasoning; move 4 appears inside RQ2; two open questions with data and method; society claims are labelled "ours" or sourced.
- **Who encodes and who decodes:** crystal clear in section 2, step 5, the diagram and recall card 6. The only blur is the twin fold-out (C2-12).

## C. The first sentence where a high-school reader gets lost

Section 1, second paragraph: "Pierce says this is acceptable only if successive symbols 'are chosen independently' and each 'is equally likely to be selected'." Layer 1 has not said what a symbol is, what independent choice means, or why equal likelihood matters. The paragraph asks the reader to hold three quotes and a 1920s history before anything has been built. The first sentence in the mathematics where a strong 17-year-old stalls is the one in step 2: "a log turns a product into a sum" (no reason given).

## D. Findings

Severity: major = a reader cannot follow or a house rule breaks; minor = a fix helps, the post still works.

| ID | Sev | Where | Finding | Fix |
|---|---|---|---|---|
| C2-01 | major | 3.3 exercise | The predict-first exercise's answer (2.25) is stated in the paragraph above it and in section 2's check (b). | Remove the 2.25 sentence from the main text; keep it as the exercise answer. |
| C2-02 | major | 3.6 | The best-script rule is one sentence, "ours", with no reason and no proof of "best"; the ladder starts at the formula (E9); no picture. | Instance first; a four-row join table; say why the rare words go deepest; then E9; say "best" is shown in the notebook. |
| C2-03 | major | 2 parts list, 3.2 café line, 3.4 café line | "Cost" means whole answers on the ticket (layer 2, "one second") and also fractional worth (3.2, 0.3 gives 1.74; 3.4, "0.0227 of a question"). The E2 café line is false for non-dyadic shares. | Name two things: the ticket's length (whole answers) and the worth (can be fractional). Say in the E2 café line that they match only for shares 1/2, 1/4, 1/8. Say once, before the plot, why 3.3 questions is not a ticket. |
| C2-04 | major | 1 hook | "Successive symbols are chosen independently ... equally likely" with no definitions; 190 words and seven citations in one paragraph; forward pointer to "a function of that number". | See section 1 fix. |
| C2-05 | major | widgets 3.3 and 2 | No widget lets the reader build or reorder a card: the lab hard-wires lengths 1, 2, 3, 3; the trees are static. The layer-2 mechanism (split the customers, put the likely question first) is read, not done. | Add a small `lab`: choose the first question's group (flat white only, flat white and latte, matcha only) and read the average questions per customer against 1.75 and 2. Preset "matcha first" gives the second check of section 2. |
| C2-06 | minor | 3.2 | "a log turns a product into a sum" is asserted. | Add 2^a x 2^b = 2^(a+b) in one line. |
| C2-07 | minor | 3.3 | In the café: "Σ: go through the day's customers". Σ runs over drinks weighted by share. Audio script repeats it. | "Σ: go through the drinks, each weighted by its share." |
| C2-08 | minor | 4(a) vs 3.2 | Two glosses of "uniquely decipherable"; the 4(a) one is the prefix property, which is stronger. Send to the fact-checker. | Use one gloss: "no ticket is the beginning of another". |
| C2-09 | minor | 4(c) 2; E9 | "ergodic" unexplained; E9's EQ* and H not mapped to café parts. | Gloss or cut; add "EQ*: the day's average under the best card the owner could write". |
| C2-10 | minor | 4(b) | Five lenses (guideline 2-4); lens 1 and lens 3 add little; no comparison between lenses. | Fold lens 3 into step 5; cut lens 1 to two sentences; add a comparison line. |
| C2-11 | minor | 3.3 preset | The preset "0.7, 0.1, 0.1, 0.1" shows "Village script ... 1.500", which is the answer to the step-6 guess. | Either accept this (the preset is advertised in step 6) or hide the script row for that preset. |
| C2-12 | minor | 3.5 fold-out | "The side with the original text and a predictor encodes" blurs the guesser who has not seen the text. | One sentence naming the encoding side as the guesser plus the one who knows the text. |
| C2-13 | minor | 5 | Move 1's trouble is not tied to E2; Pierce's art quote is off-target; comparison appears only in RQ2; RQ1 says prior work unchecked; a 130-word caveat opens the section. | See section 5 fix. |
| C2-14 | minor | notebook | Exercise 4 dip; optional 7 before 8; "unigram"; MacKay 4.11 and Shannon 4.03 not in the post; no hint for random shares in 8(c). | See section 6 fix. |
| C2-15 | minor | 1 quiz g1 | The correct option is the only one with no "because" clause. | Give it one. |
| C2-16 | minor | 3.4 | "check the rows": no rows. Café claim "the total ... is the same: the cost of that drink" is proved only for the equal-shares grid. | "read the readout"; add the limit. |
| C2-17 | minor | 3.1 | Rats and a parallel test are a third scene not mapped to the café. | One mapping sentence. |
| C2-18 | minor | 7 recall | Card 8 tests a citation, not an idea. | Replace with the two-forecaster card. |

Counts: critical 0, major 5, minor 13.

## E. Post-level scores (minimum over sections)

| Criterion | Score | Limiting section |
|---|---|---|
| 2 Four Layers and ladder | 3 | 3.3 (answer given away) and 3.6 (ladder runs backwards, join rule asserted) |
| 3 Clarity and English | 3 | 1 hook, 4(a), 5 (dense, citation-heavy paragraphs) |
| 4 Insight and connections | 4 | 4(a), 4(b) (five lenses, thin lenses 1 and 3) |
| 5 Illustrations and interactives | 4 | 1 (g1 format), 3.1, 3.3, 3.6 (no widget to build a card; step 6 text only) |
| 6 Concision | 3 | 1 hook (about 25% could go) |
| 7 CSS imagination | 4 | 5 |

Gate (0 critical, 0 major, every criterion at least 4) is not met: five majors; criteria 2, 3 and 6 are at 3.

## F. The three changes that would raise the post most

1. **Rebuild step 6 as a ladder and give the reader the card to build.** Instance first (0.7 village), the join rule as a short table with its reason, then E9. Add the "choose the first question" lab to step 3 so the reader does the layer-2 mechanism. This clears C2-02 and C2-05 and raises criteria 2 and 5.
2. **Separate "ticket length" from "worth" in layers 2 and 3.** Two named things, one sentence in section 2's parts list, one line before the plot in step 2, and corrected café lines in steps 2 and 4. This clears C2-03 and the cleanest source of confusion for the phone reader. Also remove the repeated 2.25 (C2-01).
3. **Trim and open the hook, (a), and layer 5.** Cut the Nyquist and Hartley paragraph to about 90 words, split 4(a) into three short paragraphs, move the Mills caveats to Sources, and start layer 5 with the 30-million extreme. This clears C2-04 and the density behind the criterion 3 and 6 scores, with a net saving of roughly 400 words.

## G. Round-1 critic majors: resolved?

Checked against the revised `src/content.html`, notebook and audio script (I read `critic-1.md` and `response-1.md` only after section A to F were written).

| ID | Status | Evidence in the revised draft |
|---|---|---|
| C1-01 (café lets the decoder ask live) | Resolved | The hatch café: "The barista never sees the customer: she sees only the ticket, and she holds the same card ... 'no, no, yes' means mocha only under this card." Step 5, the diagram and the new check (different card order) all follow it. Boundary 6 names the live-asking break. Only the twin fold-out still blurs a role (C2-12, minor). |
| C1-02 (layer 1 has new concepts) | Mostly resolved | The term box moved to step 1, and the hook opens with the pain ("It rained today" and "It snowed in July"). Residual: "worth" and "fair yes/no questions" are defined inside the guess, and the Pierce sentence on "successive symbols" is still too early (C2-04). |
| C1-03 (mapping by part number) | Resolved | Every "In the café" line now names parts in bold words ("the drinks", "the ticket", "the script"). Two slips remain in what is mapped (Σ over customers; cost = ticket answers), not in the format (C2-03, C2-07). |
| C1-04 (E5 skipped steps) | Resolved | Now fold-out E6: "first question 'rain or not?' ... shares inside that group ... entropy 1.5 ... H = 1 + 1/2 x 1.5 = 1.75", checked against the tree. |
| C1-05 (twin game muddles roles) | Mostly resolved | Moved to a fold-out; main step 5 is clean. The fold-out's sentence "The side with the original text and a predictor encodes" still blurs the guesser (C2-12, minor). |
| C1-06 (undefined second curve) | Resolved | One curve only; the p = 1 edge case is in the text and caption. |
| C1-07 (rats: binary digits, no picture, extra scene) | Resolved | The recipe and the 64-object paragraph are gone; the rats are only the guess and its one-line argument. A mapping sentence to the café is still missing (C2-17, minor). |
| C1-08 (weighing step) | Resolved | A fold-out with its widget, laddered (instance, question and pattern, E7 with numbers), and the shrug is gone. The widget caption values (0.817 ... 1.000) are right. |
| C1-09 (E8 factors unlabelled) | Resolved | "With s squares left ... a miss ... is worth log2 s/(s-1). A hit ... is worth log2 s", the telescoping product with braces "all the misses" and "the hit", a hand check on four squares, and a slider whose readouts the caption quotes correctly. |
| C1-10 (g2 pre-answered) | Resolved, with a repeat | g2 now asks about the 0.7 village, which nothing earlier states. One small leak: the preset "0.7, 0.1, 0.1, 0.1" in the step-3 widget shows the village script at 1.500 (C2-11). The same fault now appears in a different place: the step-3 "Check yourself" is answered by the paragraph above it (C2-01). |
| C1-11 (notebook difficulty; ex 4 and 8) | Mostly resolved | Conditional information is removed; exercise 8 has a ladder (by hand with a trace, 0.7 village, 1,050 random vectors, market stall transfer); exercise 7 is marked optional. Residual: exercise 4 is easier than 2 and 3, exercise 7 sits before the hardest exercise, "unigram" and MacKay's 4.11 are not taught, and 8(c) has no hint for drawing random shares (C2-14). The post's own one-sentence "join the two rarest" rule is still too thin to support exercise 8 (C2-02). |
| C1-12 (concision, about 1,300 words) | Partly resolved | 6,844 words, 615 fewer; the weighing and twin game are fold-outs. By my reading about 10 per cent could still go: the hook's history (about 100 words), lens 1 and 3, the Mills caveat at the start of layer 5, and one of the sixth-boundary ideas. |

Net: of the twelve round-1 majors, eight are resolved, three are mostly resolved and one is partly resolved. Round 2 finds five new or surviving majors (C2-01 to C2-05), none of them a layer-2 violation.
