# Pedagogy critic, round 1 (blind), post 04 "How much is a surprise worth?"

Read: `src/content.html` (all), `check.mjs` readouts (8/8 widgets OK), the notebook (all cells), `audio-script.md` (chapters hook, cafe, village, answer, lenses, fails read in full; others skimmed), the built page at 390 px (no horizontal scroll, scrollWidth 390; the page is about 43 phone screens tall). Not read: self-review, numbers, outline, verify-*. Criterion 1 is not scored. The weighing caption values (0.817, 1.252, 1.500, 1.585, 1.483, 1.000) and the stepper rows I recomputed by hand: correct.

Verdict: **0 critical, 12 major, 13 minor.** The post is strong where it matters most (a café that really is isomorphic to the mechanism, a clean ladder for E1–E4, honest layer 4 with "The café breaks" in every boundary, serious open questions). It fails the release gate on: a structural flaw in the café roles (C1-01), layer 1 breaking its own rule (C1-02), phone-hostile mapping by part number (C1-03), several skipped steps (C1-04, C1-09), too many scenes and about 1,300 cuttable words (C1-07, C1-08, C1-05, C1-12).

## 1. Section scores (criteria 2–7; "–" = criterion does not apply)

| Section | 2 Layers+ladder | 3 Clarity | 4 Insight | 5 Illustr. | 6 Concision | 7 CSS |
|---|---|---|---|---|---|---|
| 1 Motivation (hook) | 3 | 3 | – | – | 3 | – |
| 2 Café (layer 2) | 4 | 4 | – | 4 | 4 | – |
| 3.1 Equal chances | 3 | 3 | – | 3 | 3 | – |
| 3.2 Surprisal | 4 | 4 | – | 3 | 4 | – |
| 3.3 Entropy | 4 | 3 | – | 4 | 3 | – |
| 3.4 Weighing | 3 | 3 | – | 4 | 3 | – |
| 3.5 Submarine | 4 | 4 | – | 4 | 4 | – |
| 3.6 Who encodes | 3 | 3 | – | 4 | 3 | – |
| 3.7 Not halves | 4 | 4 | – | – | 5 | – |
| 4a What it is | 4 | 3 | 4 | – | 4 | – |
| 4b Lenses | 4 | 4 | 4 | – | 3 | – |
| 4c Where it fails | 4 | 4 | 4 | 4 | 4 | – |
| 5 CSS imagination | – | 4 | – | – | 3 | 4 |
| 6 Your turn / notebook | 4 | 4 | – | – | 4 | – |
| 7 Recall | 5 | 5 | – | – | 5 | – |

Evidence, one sentence per score, and a fix for each score below 5.

**1 Motivation.** C2 3: the term box defines "Worth … Surprise … Information" and "a model of the source", which are new concepts in a layer that must have none; fix in C1-02. C3 3: "In words (our reading): each time the number of values doubles, the speed grows by the same step." is abstract, and "by 60 per cent" has no reason given; fix: say what a "current value" is (a signal level on the wire) and drop the 60 per cent. C6 3: two paragraphs of dated, page-cited history (Nyquist, Hartley, Morse) come before the pain, which only arrives in the third paragraph ("The pain (ours). A count gives one number…"); fix in C1-02.

**2 Café.** C2 4: it has no formula or symbol, and the old way / error / changed rule are all present; but the scene lets the decoder ask questions live, so the shared script is not really needed (C1-01). C3 4: "the till" and forward pointers ("section 3 gives the numbers") add small friction (C1-15, C1-24). C5 4: the switch with two trees is good; no widget lets the reader do the questions. C6 4: "Three checks" paragraph is dense but earns its place.

**3.1 Equal chances.** C2 3: "Number the cups 0 to 31 in five binary digits; rat 1 drinks from every cup whose first digit is 1" uses "binary digits" without explaining them (C1-07). C3 3: the step has three scenes (rats, MacKay's 64 objects, object 35 = 100011) before the formula. C5 3: the rat labelling scheme is a mechanism told only in words (WRITING §5). C6 3: Nyquist fold-out is fine, but the MacKay 64 paragraph repeats the rat lesson.

**3.2 Surprisal.** C2 4: E2 and E3 have instance, pattern, check and café mapping; the "queue" wording ("halve the whole queue to arrive at that share") is unclear (C1-24). C3 4: fine. C5 3: the plot's second curve ("average of event and non-event") is not defined anywhere (C1-06). C6 4: MacKay's table is a good check; the "neither word in Shannon" aside costs 25 words for no learning.

**3.3 Entropy.** C2 4: E4 climbs well ("14 questions in 8 days: 1.75"), but E5 skips its steps (C1-04) and the abbreviation EQ is never spelled out (C1-14). C3 3: the "In the café" line maps by part numbers (C1-03). C5 4: the village lab is good: presets "all equal / only rain / reversed" teach three real edge cases, and the prose quotes 1.750, 2.000, 0.000 and 2.25 as the readout shows. C6 3: E9, E5, "Three settings", "What it means" and a fold-out are all in one section.

**3.4 Weighing.** C2 3: "about which ball it tells you 0 bits … about which ball and heavy or light 1 bit" is a new idea (information about part of the hypothesis) with no ladder (C1-08). C3 3: 24 hypotheses, three outcomes, and a "shrug" invented for the café. C5 4: slider and presets work, and the 6v6 edge case teaches. C6 3: about 500 words for a lesson ("split evenly") that the café's "Three checks" already gave.

**3.5 Submarine.** C2 4: the four-square check is excellent; E8 has unlabelled factors (C1-09). C3 4. C5 4: the stepper is correct, but it is a table you page through, not something you do (C1-17). C6 4.

**3.6 Who encodes.** C2 3: the twin game hides who encodes (C1-05). C3 3: see C1-01 and C1-05. C5 4: the stepped diagram is clear. C6 3: the twin game and the toy rank list are about 230 words of a second mechanism.

**3.7 Not halves.** C2 4: E6 is quoted, not proved, and says so (allowed by WRITING §2). C3 4. C6 5.

**4a.** C2 4: it grows out of E2 and E4. C3 3: the last sentences are dense: "Mixing the shares toward equality raises it, except a mere swap between outcomes." and "the shortest uniquely decipherable script" are undefined in the text. C4 4: "without the café" is the right idea. C6 4.

**4b.** C2 4. C3 4. C4 4: each lens has a link type, "Adds" and "Does not explain"; lenses 2 and 4 are mostly quotation (C1-19). C6 3: five lenses plus a fold-out of hedges; many sentences describe the sources, not the idea.

**4c.** C2 4: every boundary has "Assumption" and "The café breaks", and each points to an equation; the roles break is missing (C1-01). C3 4. C4 4. C5 4: the forecast widget teaches its edge ("same belief" gives gap 0). C6 4.

**5.** C3 4. C6 3: 804 words, the longest section; the paragraph about Mills' wording, edition and "men" is 100 words of protocol. C7 4: Moves 1 and 4 are reasoning; Moves 2 and 3 are thin (C1-20); both questions have data and method and are labelled ours.

**6.** C2 4, C3 4, C6 4: see C1-11 (notebook).

**7.** All 5: only this post's content, mixed forms, scope-not-denial card, and the one-line "Who encodes" card is correct.

## 2. Layer checks (the binding ones)

- **Layer 1 introduces no new concept: FAILS** (C1-02). The term box and "a model of the source" are new concepts.
- **Layer 2 formula, symbol, abbreviation or unexplained term: none found.** I searched the café section for symbols, numerals as variables, "bit", "log", "entropy", "P(x)": nothing. "script", "string" and "shares" are defined in the sentence where they appear ("We call the agreed list the *script*"). The scene has no major finding of this kind. Small friction: "the till" (C1-24), two forward pointers (C1-15).
- **Layer 3 equations with an "In the café" line: all present** (E1, E2/E3, E4/E5/E9, E7, E8, E6). Every term maps, but by part number only (C1-03), and the weighing line breaks the scheme by adding a "shrug" (C1-08). E5 and E8 are not fully laddered (C1-04, C1-09).
- **Layer 4:** all three parts present. "Where it fails" grows out of layer 3 (each boundary cites E2, E3, E9, step 3 or notebook ex. 6) and says where the café breaks, except the most important break: the café lets the decoder ask, a real channel does not (C1-01). Each lens states a link type, what it adds and what it does not explain. Lens 1's "same-math in form only" and lens 3's "metaphor" are not in the charter vocabulary / overclaim (C1-19).
- **Layer 5:** four moves present; Move 1 includes a real test ("if changing the ranking changes what many readers miss, and individual effort does not, it is an issue"). Two research questions with data and method, labelled ours. Claims about society are labelled ours or sourced to Mills.

## 3. First sentence where a high-school reader gets lost

Section 1, paragraph 1: **"In words (our reading): each time the number of values doubles, the speed grows by the same step."** Before it, the reader has met "how many different current values it can send", "quadruplex telegraph" and "rises by 60 per cent" with no explanation of what a current value is or why three values give 60 per cent. Then "the same step" quietly replaces "doubles" with "adds". (The earliest friction is the phrase "different current values", which nobody has defined.) In the main body, the first real stall is "Number the cups 0 to 31 in five binary digits" (3.1).

## 4. Findings

### Major

**C1-01 · major · The café lets the decoder ask live, so "who encodes, who decodes" is still muddled.** In section 2 the barista speaks each question and the customer nods. Then "Both must hold the same list before the day starts, or a nod means nothing" is false inside the scene: the nod answers a question the barista just spoke. The customer needs no script, and the "string" is never sent anywhere; the barista already knows every answer as it arrives. In step 6 the diagram says "The customer knows the drink and the script" and "The barista has only the answers", which contradicts the scene she was shown. This is the very confusion Kunhao had. Fix: make the scene match the channel. Example: the grinder is so loud that the customer cannot hear questions at all; a card on the wall lists the questions in order (the script); the customer ticks yes/no boxes on a paper ticket and hands it through the hatch to the barista in the back, who has the same card and has never seen the customer. Then: customer = encoder (drink + card → ticket), ticket = string, barista = decoder (ticket + card → drink). Rewrite "Who does what", the diagram steps (the customer holds the card and ticks, the barista holds the card and reads) and step 6 around this. Add to boundary 6 or a new boundary: "The café breaks: in the real café the barista can ask live and adapt; a transmitter cannot hear the receiver (a fixed script)". Also note that in the live version she asks adaptive questions, which is the 20 questions game; the fixed tree is the code.

**C1-02 · major · Layer 1 introduces new concepts, and the pain comes last.** The term box ("Worth … Surprise … a list of how likely each message is … Information … Shannon's engineering sense") and the sentences "We need one number for 'how much did this message tell me'" define the post's new vocabulary in the motivation layer, which is meant to have none. Two of the three paragraphs before the pain are history with page cites. Fix: open with the pain in plain terms (a telegraph clerk pays per symbol; "it rained today" and "it snowed in July" cost the same on a count), give Nyquist's 60 per cent in one sentence at most, and move the term box to the start of layer 2 or the first paragraph of 3.1. Keep the guess-first but phrase it without "worth" ("how much did that miss tell you?") or define worth in one clause inside the prompt.

**C1-03 · major · "In the café" lines point by part number, and the parts are 1,500 words above.** Example: "N is the number of drinks on the menu board when all sell equally (parts 1 and 10). k is … (part 3)." and "Log of one over the share: how often the queue is halved (parts 3, 4)." A reader on a phone must scroll back to a list and count to the tenth item. Fix: write the part's name instead of its number ("the four drinks", "one question", "the script"), keep the numbers in brackets only if you want. Optionally repeat a compact legend in step 1.

**C1-04 · major · E5 skips the steps.** "the rest, whose shares are sun 1/2, wind 1/4, snow 1/4, with entropy 1.5" gives shares that silently change (sun is 1/4 of all days, 1/2 of the non-rain days), and the 1.5 is never computed. "With chance one half we are in that group, so H = 1 + ½ × 1.5" does not say that 1 is the cost of the first question (rain vs the rest, a fair coin) or why the weight is ½. "Shannon's decomposition rule" is a label, not an explanation. Fix: three lines: (i) first question: rain or not, shares ½, ½, worth 1 question; (ii) on the ½ of days that are not rain, the shares inside that group are sun ½, wind ¼, snow ¼, and its entropy is ½·1+¼·2+¼·2 = 1.5; (iii) so H = 1 + ½ × 1.5 = 1.75. Or cut E5 to a fold-out (the tree already gives 1.75).

**C1-05 · major · The twin game (step 6) re-muddles the roles.** "he knows it only up to the current point, guesses the next letter, and is told whether he was right … The record of his guesses is the reduced text … Had the first person held the whole text in advance…". Who encodes: the guesser, the experimenter who says "right", or both? The answer card says "the side with the original text and a predictor encodes" which is neither person. The toy list-of-ranks code ("T 2nd, E 1st, A 3rd") is a third coding scheme, unrelated to yes/no. This is where Kunhao's earlier confusion is most likely to return. Fix: move the twin game to a fold-out ("Look inside: Shannon's twin game"), with one sentence in the main text that the same two roles exist there; keep the main step 6 on the repaired café (C1-01). About 230 words saved.

**C1-06 · major · The plot widget draws a second, undefined curve.** "average of event and non-event" and the readout "the average over event and non-event is 0.469" appear in step 2, before entropy exists; the caption promises "step 3 explains it" but step 3 only has a four-word village and never says "event vs non-event". The prose never uses the curve. Fix: delete the curve and point and the `H2` derived value from the step 2 widget (keep surprisal only). Move the two-outcome curve (peak 1.000 at p = 0.5, 0 at p = 0 and 1) into step 3 or the weighing fold-out as its own small widget, or drop it. Keep the p = 1 edge case: add one sentence "at p = 1 the worth is 0: a sure thing tells you nothing".

**C1-07 · major · The rat mechanism has an undefined term, no picture, and adds a second scene.** "Number the cups 0 to 31 in five binary digits; rat 1 drinks from every cup whose first digit is 1, rat 2 from every cup whose second digit is 1" requires binary numbers (not defined; "binary" first appears here) and has no figure (WRITING §5). Together with MacKay's 64 objects and "object 35 gives 100011" the reader gets three scenes before E1. Fix: keep the café and the rats only as the guess (answer five, with the argument "five yes/no answers give 2^5 = 32 labels"), cut the binary-digit recipe and the 64-object quote (about 150 words), or show an 8-cup table (3 rats) in a `stepper`. State "bit" and "binary" only after the café has produced them.

**C1-08 · major · The weighing step introduces new ideas for little gain and breaks the café mapping.** 500 words: 12 balls, 24 hypotheses, three-way outcomes, E7 (the same sum again), "Does 6 against 6 tell you nothing?" with "information about which ball" (conditional information, never defined), and an "In the café" line that invents a shrug. The lesson (a question is best when its answers are about equally likely) is already in the café's "Three checks" ("a question helps most when both answers are likely"). Fix: demote step 4 to a "Look inside" fold-out with the lab widget in it, or cut to about 150 words in the main text (a three-way weighing, 8:8:8 against 12:12:0, the widget). Remove "information about which ball" from the main text and from notebook ex. 4(b) (see C1-11).

**C1-09 · major · E8's chain does not say what its factors are.** "In general the chances multiply, and the fractions cancel in a chain: log₂(64/63 × 63/62 × … × (n+1)/n × n/1)". The reader cannot see that each ratio is "one over the chance of a miss", that the last factor, n/1, is the hit (1 over a chance of 1/n), or why the factors cancel. "the chances multiply" is not what the formula shows. Fix: one sentence: "A miss with s squares left has chance (s−1)/s, so its worth is log₂ of s/(s−1). The hit with n squares left has chance 1/n, so its worth is log₂ n. Write the product with the factor for the hit last: each numerator cancels the next denominator." Label the last factor with an underbrace in words ("this is the hit").

**C1-10 · major · The guess-first on entropy (g2) is already answered by layer 2.** The café says "fourteen questions. One and three quarters for each customer, against two for the old way", with the same four shares ½, ¼, ⅛, ⅛ as the village. The guess "1.25 / 1.50 / 1.75 / 2.00" is then a lookup: the correct card is 1.75 for anyone who read three screens up. Fix: make the guess about something not yet seen: e.g. "What does the best script cost on a village with shares 0.7, 0.1, 0.1, 0.1?" (options 1.0, 1.36, 1.5, 2.0), or ask "which of these two villages is harder to predict?". Keep the other two guesses (g1 and g3 are genuine predictions; their distractors are serious and similar in length, and the right answer is not the longest, although g1's right option is the only one with a quantity, "a few hundredths").

**C1-11 · major · The notebook's difficulty does not climb, and exercises 4 and 8 need ideas the post never teaches.** Order of difficulty by my reading: ex1 easy, ex2 medium (prefix decode), ex3 easy-medium, **ex4 hard** (conditional entropy: "H(O) − H(O | X)" appears only in the hint), ex5 medium, ex6 medium-hard (multinomial), **ex7 trivial**, **ex8 hardest** (Huffman with a heap, "repeatedly join the two smallest shares", not explained in the post; the post never says how to build the best script when shares are not halves). So the trivial exercise sits second-last and the hardest at the end without scaffolding, and ex4(b) teaches a concept (mutual information) outside this post (WRITING §0: recall tests only this post). Good: "Predict first" in every exercise, folded solutions, hints that do not give the answer, fixed seeds, ex6 linking to boundary 5. Fix: reorder to 1, 2, 3, 7, 5, 6, 4a, 8; drop ex4(b) or replace by a one-line count ("how many of the 24 hypotheses does '6 v 6 left down' leave?"); give ex8 a ladder (a): build the village tree by hand with `heapq` for 3 symbols, (b) 4 symbols, (c) random shares; and add one sentence in the post (step 7 or a fold-out) saying "join the two rarest, repeat" is how to build the best script.

**C1-12 · major (criterion 6) · About 1,300 words, 17 per cent, can go.** The post is 7,459 words (cap 7,500) and 43 phone screens; at "about 45 min" this is long. Suggested cuts in order of value: (1) Step 4 weighing to a fold-out or 150 words (−350); (2) twin game to a fold-out (−230); (3) hook: Nyquist/Hartley/Morse to about 120 words (−200); (4) step 1: drop the MacKay 64-object paragraph and the binary recipe (−150); (5) source-process asides that do not teach: "(our search of the whole text)", "MacKay prints 0.0230 because he cuts digits off", "Pierce's 'four times' is an apparent slip", "This is a review that points to studies we have not seen" (about −150; move to `sources` or the fold-outs); (6) lens 2 and 4 quotation blocks (−120); (7) layer 5's paragraph on Mills' wording, edition and "men" (−100). The same point repeated: scope-not-denial for meaning appears in the lede-term box, the short answer, lens 3, boundary 1 and the recall card.

### Minor

**C1-13 · minor** Equation labels run E1, E2, E3, E4, E5, E9 (step 3), E7, E8, E6. Renumber in reading order (E6 → E9, etc.) and fix the references ("E9 and boundary 2", "(E9)").

**C1-14 · minor** "EQ" is used as a symbol ("\mathrm{EQ}") and never spelled out. Say "EQ, short for the expected number of questions" at E9.

**C1-15 · minor** Layer 2 points forward ("section 3 gives the numbers"; "Section 3 gives the number, 2.25") and labels itself "Check yourself · layer 2". The reader should not need a later section; give 2.25 only after step 3, or compute it in the answer (¼·(1+2+3+3) = 2.25 is one line). Drop the word "layer" from the box titles.

**C1-16 · minor** Units drift: "questions" in the café and village, "bits" in step 4 ("This weighing is worth 1.585 bits") and in section 4. State once, at the formula, "one question's worth = one bit", then use one word per section.

**C1-17 · minor (widget)** The submarine stepper is a table that advances; the reader cannot choose when the hit comes, though that is the mechanism ("the total is the same whenever the hit comes"). Replace or add a `lab` with a slider "the hit comes on shot t" (1–64) showing misses so far, the hit, and the total 6.000. The notebook has this (ex. 3c); the page should.

**C1-18 · minor (widget)** `village-lab` cannot show the best script for new shares, so "a script is right only for its own shares" is seen only one way. Add a preset "0.7, 0.1, 0.1, 0.1" (weights 7, 1, 1, 1: H 1.357, village script 1.500), which connects step 3 to step 7 and the fold-out. The readout line "Equal-size labels (2 each): 2.000" already works well.

**C1-19 · minor** Layer 4b. Lens 2 is one hedged sentence ("is associated with predictability"); a high-school reader gets no example of what "processing effort" means. Add one concrete case from Gibson et al. (e.g. the colour-word chip game that is already in the fold-out) and cut the sentence about references [104,105]. Lens 4 uses three consecutive quotations of MacKay on belief, including "people with the same assumptions and data will draw identical conclusions", which does not bear on surprisal; keep only "beliefs can be probabilities" and the Ana/Ben point. Lens 3 is labelled "metaphor" but says "Our café roles are Shannon's transmitter, signal and receiver" (structural analogy at least). Lens 1 "same-math in form only" is outside the charter's link-type list: use "same-math (form) / metaphor (meaning)" or state the single type chosen. Layer 4a's last paragraph needs "uniquely decipherable" explained ("no string is the start of another string, so a run of answers can be cut into words without gaps") and "mixing the shares toward equality" shown with one number.

**C1-20 · minor (criterion 7)** Moves 2 and 3 assert more than they reason. Move 2: "Give the weather village 30 million listeners (ours). Each listener's surprisal for snow is the same. What changes is who writes the forecast, and who pays when it is wrong." There is no reasoning for why scale changes authorship; add one concrete mechanism (one forecast model prices every listener's surprise; a single error is made 30 million times: correlated surprise) or cut. Move 3 lists five professions in one clause each; develop two (journalist vs psycholinguist) and cut the rest. Move 1 jumps from surprisal to "a ranking system whose model, not hers, prices every message", which nothing in the post establishes; add one sentence that a ranker that orders by predicted surprisal/engagement is a hypothesis (ours) and name the observable. Research question 1 needs: how a post-level number is made from token probabilities (sum or per-token mean; length is a confound), and a pointer to the existing literature on novelty and spreading (Vosoughi et al. 2018 is the obvious one, but only add it if the fact-checker can verify it; otherwise say "we have not checked the prior work"). Question 2 is good.

**C1-21 · minor** "Check yourself · layer 4" item (iv) ("The surprisal of two independent events adds") has no label among the five offered; "theorem" fits and the answer says "a property that follows from the definition". Say "a theorem (a consequence of the definition and independence)". Boundary 5 explains the low bias as "a rare word that never appears gets share 0", which is only part of the cause: the plug-in estimate is biased low on average even when every word appears (the log is concave). Say "partly because".

**C1-22 · minor (audio)** The script runs 8,407 words (about 56 minutes at a listener's pace), 13 per cent longer than the page, and is close to a reading of it. Not good listening: the "In the café" lines are spoken with part numbers ("parts one and ten"), page numbers are read in cites ("Pierce's page thirty-eight"), the answers to "Check yourself" follow the question with no pause marker, and the lens chapter is a run of quotations. Fix after the text is cut: speak the part names, drop page numbers, add "Pause." before each answer, say each equation once with the café mapping, and aim for 35–40 minutes.

**C1-23 · minor** Placement. g1 (submarine) is asked in section 1 and answered in section 3.5: four sections later, so the guess is forgotten. Move g1 to the start of step 5 or add "(answered in step 5)" to the prompt (it has `data-answer-in`, which the reader may not see). The short answer says "two forecasters … (widget below)" but the widget is in boundary 4, two screens and a lens section away; say "(boundary 4)".

**C1-24 · minor** Small wording friction for a B2–C1 reader. "the till" (use "cash register" once, then "the sales record"); "halve the whole queue to arrive at that share" (E2 pattern paragraph) is unclear (say "how many times you must cut the customers in half to be left with a group the size of that share"); "In the café. … Σ: go through the day's customers" is the first time the reader sees "Σ" explained; add "Σ means add up" in the Read-aloud sentence; "≡" in the zero-share convention needs "means by definition".

**C1-25 · minor** Level line says "(counting, fractions, powers of two)" but the post needs logarithms; say so ("and one new function, the logarithm, explained in step 1") so a reader is not surprised, and "about 45 min" is an underestimate for 43 screens plus eight widgets; say 60–70 minutes or cut the length (C1-12).

## 5. Widget review (reader can do it / edge case teaches / prose quotes the readout)

| Widget | Do it? | Edge case | Prose = readout? |
|---|---|---|---|
| two trees (switch) | look only; fine for an illustration | – | caption: 14 questions ✓ |
| surprisal-plot | slide p, read worth | p = 1 never mentioned; extra curve undefined (C1-06) | 3.3, 6.6, 10.0 etc. ✓ (MacKay table) |
| village-lab | yes, four weights | "all equal", "only rain", "reversed" all teach | 1.750 / 2.000 / 0.000 / script 2.25 and 1.000 ✓ |
| weigh-lab | yes, one slider | 6 v 6 (balance impossible) teaches | caption list 0.817…1.000 ✓ (recomputed) |
| sub-table (stepper) | pages through rows; cannot choose the hit | 1st shot hit = 6.0000 in note | 0.0227, 0.0231, 1.0000, 2.0000, 6.0000 ✓ |
| roles-diagram | steps through | – | but contradicts the café (C1-01) |
| forecast-lab | yes, two sliders | "same belief" gives gap 0 | readout 3.00 / 1.00 / 2.00; prose in boundary 4 does not quote the numbers but the audio does ✓ |

All the numbers I checked match `check.mjs`. 390 px: no horizontal scroll.

## 6. Quizzes

- **Guess-first:** g1 and g3 are real predictions with serious, similar-length distractors; the right answer is not the longest or most hedged (g1's is the only one with a stated quantity; make option 2 also say "about one" and option 4 "about six" as now, and give option 1 no unit advantage by saying "far less than one question"). g2 is pre-answered (C1-10). Reveal placement: g3 and g2 are answered in their own sections, g1 four sections later (C1-23).
- **Check-yourself:** after the café (good), E4 (good: "predict first, then use the widget"), weighing (good), submarine (good), roles (good, but its answer rests on the twin game, C1-05), layer 4 (good, C1-21). None sits in step 2 or step 7; both are fine without one.
- **Recall:** eight cards, all answerable from this post alone; four marked as returning. Card 4 ("Why is 1.75 lower than 2, and when would the best script average exactly 2?") answers its second part in four words ("For four equally likely words."), which is too thin for a recall card: add "no script of whole questions can do better than 2 there".

## 7. Notebook as practice (see C1-11)

Good: each exercise has "Predict first", a hint that does not give the answer away (except ex. 3's "a hit on shot t is worth log2(65−t)", which is acceptable), an empty "your attempt" cell, a folded solution that later cells reuse, fixed seeds, outputs recorded in `results.md`, ex. 5 on the reader's own text and ex. 6 and 7 tie directly to boundaries 5 and 4. Weaknesses: the difficulty order; ex. 4(b) and ex. 8 need unseen ideas; ex. 2 asks for three things (round trip, comparison, uniform village) in one cell without a step-by-step; ex. 1 never asks the reader to explain why `p = 0` is skipped, though the markdown says it. A short "if you are stuck" ladder in ex. 8 and a final transfer cell ("write `best_script(shares)` and test it on the market stall") would turn the notebook into a closing of the loop with section 6.

## 8. Audio as listening material (see C1-22)

Good: opens with the source mark and the one-line answer; each chapter ends with a recap; widgets are described, not read; the café chapter works well by ear. Weak: length, part numbers spoken aloud, page numbers read, the lens and fails chapters are quotation chains, and no pauses for the checks.

## 9. Who encodes, who decodes: verdict

Not yet crystal clear. The sentences are right ("The customer encodes; the barista decodes"), the diagram is clear, and the Shannon quote "Our questioning strategy defines a way of encoding…" is handled well. But the scene underneath is wrong (the barista asks live; the customer needs no script), so a careful reader sees a contradiction between "the barista holds only the string" and "she asks each question and sees each nod". Fix C1-01 first; then step 6 can be two paragraphs and a diagram, and the twin game moves to a fold-out (C1-05).

## 10. Post-level scores (minimum over the sections that the criterion applies to)

| Criterion | Score | Why the minimum |
|---|---|---|
| 2 Four Layers and ladder | **3** | layer 1 new concepts (C1-02); E5, E8 skipped steps; weighing and twin game unladdered |
| 3 Clarity and English | **3** | part-number mapping (C1-03); hook; binary digits; dense 4a |
| 4 Insight and connections | **4** | lens 2 and 4 are quotation-led; the roles break is missing in layer 4 |
| 5 Illustrations and interactives | **3** | rat scheme has no picture; plot's second curve; stepper is passive |
| 6 Concision | **3** | about 17 per cent can be cut (C1-12) |
| 7 CSS imagination | **4** | moves 2 and 3 thin; question 1 lacks the post-level measure |

The release gate (every criterion at least 4, no major findings) is not met: criteria 2, 3, 5, 6 are 3 and there are 12 major findings.

## 11. The three changes that would raise the post most

1. **Repair the café's roles, then rebuild step 6 on it (C1-01, C1-05).** Customer ticks a paper ticket from a wall card; barista in the back reads it with the same card. Redraw the diagram, add the "live asking vs fixed script" break to layer 4, and move the twin game to a fold-out. This also settles Kunhao's earlier confusion.
2. **Cut about 1,300 words and add the missing steps (C1-12, C1-08, C1-07, C1-04, C1-09, C1-10).** Weighing and twin game to fold-outs, shorter history, no binary-digit recipe, no source-process asides; spend about 150 of the saved words on E5, E8 and a fresh g2. This brings the page to about 6,200 words and fixes concision, ladder and the phone length at once.
3. **Make layer 1 and the mapping phone-proof (C1-02, C1-03, C1-06).** Open with the pain and no new terms (move the term box to layer 2), write the part names in every "In the café" line, and remove the undefined second curve from the surprisal plot. Then reorder and scaffold the notebook (C1-11) and develop layer 5's moves 2 and 3 (C1-20).
