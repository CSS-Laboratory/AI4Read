---
id: 2026-12-surprise/outline
type: outline
stage: S3
post: "How much is a surprise worth?"
series: information-theory, week 1
inputs: topic-card.md, source-brief.verified.md (the only citable facts), review/s2-check.md, learner/state.md
status: ready for the outline check
planned_main_text_words: 6,610 (ceiling 7,500)
---

# Outline: How much is a surprise worth?

**One-line preview (under the title).** A surprise is worth the number of fair yes/no questions it saves you. The rarer the news, the more questions it saves, and the average over all the news a source can send is called its entropy.

**Editions to cite (S2).** Cover & Thomas (1991, first edition). Pierce (1961, Harper, first edition). Shannon 1948 (Bell Labs reprint pages). Shannon 1951. MacKay 2003. Gibson et al. 2019 (pre-proof pages). Source keys for `post.json`: `shannon1948`, `shannon1951`, `mackay2003`, `cover1991`, `pierce1961`, `gibson2019`. Brief units are written U1–U15.

**Threshold words (WRITING §0), fixed in a term box at the end of layer 1 and carried to the Short answer.**
- *Worth* = the number of fair yes/no questions the outcome saves, in bits. Not usefulness or importance.
- *Surprise* = improbability under a stated model of the source. Not a feeling.
- *Information* = the engineering sense: one selection from a set of possible messages (Shannon p. 1, U11). Pierce p. 24 warns that the popular sense (knowledge) creeps in.

**Notation (notation.md).** Logs base 2. `h(x)` = surprisal (MacKay's "Shannon information content", Gibson's "surprisal"; say which source uses which name, U7 trap 1). `H` = entropy. Never use "relative entropy" (U8 trap a). `P(x)` = the share of the outcome x. New symbols for this post: `N` (number of options), `k` (number of questions), `EQ` (expected number of questions of a script), `L(x)` (number of questions the script spends on x).

---

## The café scene and its numbered parts (fixed here; layer 3 uses exactly these)

**Scene: the guessing barista.** A loud café. The grinder drowns speech, so a customer can only nod or shake their head, and each question costs the barista one second. The owner knows, from the till, how the regulars order: half want a flat white, a quarter a latte, an eighth a mocha, an eighth a matcha. The barista must find out each regular's drink with questions that can be answered by a nod or a shake.

**Numbered parts (layer 3 maps each term to one of these):**
1. **The four drinks** (the outcomes).
2. **The share of customers who want each drink**, as recorded in the owner's till (the probabilities; the model of the source; the till can be out of date).
3. **One question, answered by a nod or a shake** (one yes/no answer, one bit; each costs one second).
4. **The question script** agreed in advance, which both the barista and the till's notes hold (the code, a question tree).
5. **The customer**, who knows the drink and answers (holds the secret; the encoder side).
6. **The string of nods and shakes** for one customer (the message that travels).
7. **The barista**, who has only the string and the script and names the drink (the decoder side).
8. **The number of questions one drink costs** (surprisal).
9. **The day's average** over all customers (entropy).
10. **The menu board** (the old way: the options as a list, split in equal halves).

**Draft of the layer-2 scene (plain words; the S4 text may expand it, but must keep this content and these constraints: no formula, no symbol, no abbreviation, no unexplained term; no use of "bit", "code", "probability", "entropy", "model", "encode", "decode").**

> The café is loud. The grinder drowns every word, so the customers can only nod or shake their head. The owner knows what her regulars order from years of watching the till: out of every eight customers, four want a flat white, two a latte, one a mocha and one a matcha. The barista wants to find out each regular's drink with as few questions as possible, because each one costs a second.
>
> **The old way.** She looks at the menu board, a 2 by 2 grid. She asks, "Is it on the left half of the board?" Then, "Is it the top one?" Two questions, and she always knows. This seems fair, but it is wasteful. Half of the customers want the flat white, and she spends two questions on each of them. She spends exactly as many on the rare matcha. She split the *drinks* into equal halves, and she ignored how many *customers* sit behind each drink.
>
> **The rule that changes.** Split the *customers*, not the drinks. The first question is, "Flat white?" A nod settles four customers out of eight in one second. A shake leaves the other four, and she asks, "Latte?" A nod settles two more. A shake, and she asks, "Mocha?" and after that she knows. So the flat white costs one question, the latte two, and the mocha and the matcha three each. Over a day, the average falls from two questions to one and three quarters. The rare drinks cost more, and that is fair: when a matcha is ordered, she has learned something unusual, and it took her the most questions. The rarer the order, the bigger the surprise, and the more questions it is worth.
>
> **Two checks on the rule.** Suppose she asked "Matcha?" first. The answer would nearly always be a shake, and she would learn almost nothing from it. A question is useful when both answers are likely. Now suppose all four drinks sell equally: then no script beats two questions for everyone, and the script made for the old shares would do worse. And suppose everyone orders the same drink: then she need not ask anything.
>
> **Who does what.** The customer knows the drink. As the barista asks the agreed questions, the customer's nods and shakes turn the drink into a string. The barista has only the string and the same agreed script. She turns the string back into a drink. Both must hold the same script before the day starts. That agreement is what makes the nods mean anything.

(About 400 words in the draft; target 650 in the post with the widget and the check-yourself questions.)

---

## Section list, planned word counts, and per-section plans

| § | Section | Layer | Planned words |
|---|---|---|---|
| 0 | Title and preview | 0 | 60 |
| 1 | Motivation, with Guess first | 1 | 650 |
| 2 | Intuition: the guessing barista | 2 | 650 |
| 3 | Concrete: the weather village | 3 | 2,550 |
| 4 | Abstract: (Short answer) (a) what it is, (b) the same idea elsewhere, (c) where it fails | 4 | 1,370 |
| 5 | The CSS imagination | 5 | 750 |
| 6 | Your turn | 6 | 280 |
| 7 | Recall | 7 | 300 |
| 8 | Sources | 8 | (not counted) |
| | **Total main text** | | **6,610** |

Fold-outs ("Look inside"), the Sources list, and answers inside `.reveal` blocks are outside the count (WRITING §8a). Counting with `python3 scripts/wordcount.py` at S4.

---

### 0. Title and preview (60 words)
- **Title:** "How much is a surprise worth?" Preview line as above.
- No widget, no cites.

---

### 1. Motivation: why should we care? (650 words; layer 1, no new concepts)

**Purpose.** Show how engineers measured messages before Shannon, what hurt about it, and give the strange phenomenon that the idea explains. Introduce no new concept: no "bit", no "logarithm", no "probability" as a technical word, no "entropy". Plain words only ("how many choices", "how likely").

**Content (each claim sourced or labelled ours).**
- *Old practice 1, Nyquist.* In his 1924 paper, as Pierce reports it, Nyquist tied telegraph speed to the number of distinct current values the line can send. Going from two values (on, off) to four doubled the speed, as in the quadruplex telegraph; three values (+, 0, −) gave 60 per cent more. In words: each doubling of the number of values adds the same step of speed. (U1; Pierce 1961 pp. 35–38.) A small **trap box**: Pierce's printed "eight values give four times" is a slip; by the same rule eight values give three times the speed of two (ours; U1 S2). Say it in words only; the formula `W = K log m` sits in a layer-3 fold-out.
- *Old practice 2, Hartley.* In 1928 Hartley pictured a sender choosing symbols from a set and measured a message by how many different messages could have been sent. That measure, Pierce says, fits only "if successive symbols are chosen independently and if any of the s symbols is equally likely to be selected" (U2; Pierce p. 40, p. 39; Shannon p. 1). Note: Shannon credits Hartley with the right kind of measure. Hartley is not "the wrong measure" (U2 trap a, brief trap 4). Hartley also noticed that restrictions on selection, such as E being more frequent than Z, should govern code lengths, and Pierce says Morse understood this (U2 trap c; Pierce p. 40). What was missing was a number that weighs each message by how likely it is.
- *The pain (ours, labelled).* A counting measure gives the same number to "it rained today" and "it snowed in July". Both are one pick among the same set. Yet one told us nothing, and the other is news.
- *The strange phenomenon.* Presented as the Guess first block G1 (the submarine miss), not as a stated fact: one yes/no answer can be worth six questions, and another worth almost nothing.
- *The urgent problem.* One number for "how much did this message tell me" that works when the choices are not equally likely.
- *Pin down the question.* A term box "Words in the question" (worth / surprise / information, as above). It ends layer 1 and sets the scope; it adds no technique.

**Quiz.** **G1 Guess first** (`data-answer-in="section 3, step 5 (the submarine)"`). *A submarine hides in one of 64 squares, all equally likely. You fire at one square and miss. How much news is that miss worth, counted in fair yes/no questions?*
- A. About one question's worth, because a plain no is still an answer
- B. Almost nothing: a few hundredths of one question's worth ✔
- C. Exactly nothing, because you still do not know where it is
- D. About six questions' worth, the same as finally finding it

Reveal (short, at the point of the question): a miss is worth 0.0227 questions (MacKay p. 71), a hit on the first shot is worth 6; the reveal points to step 5 for the proof. Options are the same length and none is the longest, most hedged or most specific (WRITING §5). S4 places the correct option in a different position from G2 and G3.

**Widget.** None (the layer is words and a quiz).
**Cites.** U1, U2 (U3 not used here). Pierce 1961 pp. 35–40; Shannon 1948 p. 1; MacKay p. 71 (in the reveal).

---

### 2. Intuition: the café version (650 words; layer 2)

**Purpose.** One complete mental map in plain words. The scene above, told in full: the old way (split the menu), where it goes wrong (the same two questions for a flat white and a matcha), the rule that changes (split the customers), the two checks (a "Matcha?" first question; equal shares; one-drink day), and who does what (the customer, the string, the shared script, the barista). Ends with the numbered parts in a compact list (so the layer-3 mapping is visible), phrased in plain words.

**New concepts.** None named with a technical term. Every idea (share, question, script, cost of a drink, day's average) is in the numbered list; the technical names arrive in layer 3.

**Constraints (checked by grep at S4, major finding if broken).** No digits-with-symbols formulas, no Greek or math symbols, no abbreviations, no technical word that layer 2 does not explain on the spot. Words that must not appear: bit, entropy, probability, code, model, encode, decode, log, surprisal. Numbers are allowed (two, three, one and three quarters).

**Widget.** `diagram` + `switch` (two panels), "Two scripts" (see widget list, W1): the menu-split tree and the customer-split tree, each leaf labelled with its number of questions. The reader taps a drink and sees its path.
**Quiz.** Two **check-yourself** questions with folded answers, in plain words:
- (a) Which customers get the longest run of questions, and why? *Answer: mocha and matcha (three each), because each is one customer in eight and only three shakes in a row get to them; the barista spends her questions where the customers are.*
- (b) A day comes when all four drinks sell equally. Would the clever script still be best? *Answer: no. It would cost more than two questions on average. A script is built for the shares it was made for. (Layer 3 gives the number, 2.25.)*

**Cites.** None (all ours). The scene is our analogy; the owner's shares are the village's numbers (U6), which layer 3 introduces as the field's own setting.
**Link to later layers.** Part 2 (the till) feeds the failure boundaries in 4(c) (stable shares, who owns the model). Part 10 (menu board) is the equal-case rung in step 1.

---

### 3. Concrete: the weather village (2,550 words; layer 3)

**Purpose.** Leave the café. Re-introduce the four-word weather village from scratch (the radio sends one word a day: rain 1/2, sun 1/4, wind 1/8, snow 1/8; Shannon p. 18; Cover pp. 14–15, U6). Work it by hand with numbers, one concept per step, each on the WRITING §2 ladder, each equation followed by an "In the café" line that maps every term to a numbered part. A reader should be able to point to any symbol and say which part of the scene it is.

Opening paragraph (~110 words) says: same scene, the field's setting. The owner's till is now a radio station's log; the drinks are weather words; "question" is "fair yes/no question".

#### Step 1. Equal chances: questions = log₂ of the number of options (≈ 380 words; includes G3)
- **Instance.** 32 cups of water, one poisoned, one hour for the poison to show. G3 Guess first (below). Cover's version: 32 equally likely outcomes, 5-bit labels (Cover pp. 5–6, U4); MacKay's sixty-three game (p. 70, U4). The cups-and-rats framing is Kunhao's puzzle, not from a source: label "ours" (U4 trap).
- **Question.** How many fair yes/no questions are needed in the worst case?
- **Mechanism in words.** Each good question splits the options in equal halves (MacKay p. 70: "Intuitively, the best questions successively divide the 64 possibilities into equal sized sets"). 32 → 16 → 8 → 4 → 2 → 1: five halvings. The answers, read as 0 and 1, spell a number: 35 of 64 gives 100011 (MacKay p. 70). Rat version: five rats, each drinks from the cups whose label has a 1 in its place; the rats that die spell the label. All questions are asked at once; the 20-questions game asks in turn. With equal chances the count is the same (U4 trap).
- **Numbers.** 2⁵ = 32; 2⁶ = 64. Name the unit: one answer of a fair yes/no question is one **bit** (a word Shannon credits to J. W. Tukey, p. 1, U3). Term box: **Bit**. Warn: MacKay also uses "bit" for a 0/1 variable (U3 trap; MacKay p. 32).
- **Formula.** For N equally likely options, `k = log₂ N` questions, because `N = 2^k` (read aloud: "the number of times you must halve N to reach 1"). Hartley's measure `H = n log s` is this formula for n symbols from s kinds; the pairing with MacKay's "raw bit content" (p. 74, "a lower bound for the number of binary questions that are always guaranteed") is ours (U2 S2 change a). The conditions again: independent and equally likely (Pierce p. 40).
- **Check.** log₂ 32 = 5, log₂ 64 = 6; Cover's H = log 32 = 5 (p. 5).
- **Edge / what it does not say.** Four rats cannot decide 32 cups: 2⁴ = 16 < 32 (ours). MacKay's "guaranteed" is a worst-case count, not an average (U4 tension).
- **In the café.** `N` = the number of drinks on the menu board when all sell equally (parts 1, 10); `k` = the number of nod-or-shake questions (part 3); `2` = each answer has two possible replies (part 3); the equal split of the board is the old way (part 10).
- **Fold-out "Look inside: Nyquist and Hartley in symbols"** (not counted): Nyquist's `W = K log m` as Pierce reports it, with `K` kept (U1; Pierce p. 36); two values → four double the speed; three values +58.5% (log₂ 3 = 1.585; Pierce says "60 per cent"); eight values three times (ours; Pierce's "four times" is a slip, and its list shows only seven values). Hartley's `H = n log s` (U2). Shannon's three reasons for a logarithm, with his hedges: parameters "tend to vary linearly" with the log; "One feels, for example, that two punched cards should have twice the capacity of one" (U3).

**G3 Guess first** (`data-answer-in="section 3, step 1"`). *One of 32 cups of water is poisoned. A rat that drinks any poisoned cup dies within the hour, and you have one hour. All rats drink at the same time, each from any cups you choose. What is the smallest number of rats that is always enough?*
- A. Four, because each rat can clear half of the cups that are left
- B. Five, because five yes/no tests can tell 32 cups apart ✔
- C. Six, because the very last cup needs a test of its own
- D. Eight, because one rat can safely check four cups

(Equal-length options. The correct one is neither the longest nor the most specific.) Reveal ties it to the village: the 5 answers spell a label.

#### Step 2. Unequal chances: surprisal (≈ 420 words; widget W1 tree diagram reused here)
- **Instance.** The village. Best questions: "Rain?" (1 yes/no), "Sun?" (2), "Wind?" (3), and snow after "Not wind?" (3; no further question). Yes written as 0, no as 1, so the answers match the code 0, 10, 110, 111 (Shannon p. 18; Cover p. 15, U6). Say it plainly: Cover's "Is X = a?" splits the *probability* in half (Cover p. 15; only for this example, U6 trap d).
- **Question.** What rule gives the number of questions an outcome costs?
- **Mechanism in words.** A word that comes half of the time needs one halving of the queue; one in four needs two; one in eight needs three. The count is "how many times you halve to get from the whole queue to this share".
- **Numbers.** Shares 1/2, 1/4, 1/8, 1/8 give costs 1, 2, 3, 3.
- **Formula.** `h(x) = log₂ (1 / P(x))` (MacKay eq. 2.34; Gibson Box 2 eq. I, U7). Read aloud: "the surprisal of x is the log, base 2, of one over the share of x." Names: MacKay "Shannon information content"; Gibson "surprisal" and "information content" in the same sentence (p. 4); Shannon 1948 has neither word (U7 trap 1, S2 check). Say who coined "surprisal": we do not know (not in our sources); do not say.
- **Check.** P = 1/8: log₂ 8 = 3. Table: rain 1, sun 2, wind 3, snow 3; MacKay Fig. 4.1 values p = 0.001: 10.0; 0.01: 6.6; 0.1: 3.3; 0.2: 2.3; 0.5: 1.0 (p. 67), reproduced in the plot widget W3.
- **Additivity (second concept, short ladder).** *Instance:* rain today, snow tomorrow. *Mechanism:* two independent days, one string after the other, questions add. *Numbers:* 1 + 3 = 4 = log₂ 16, and there are 16 equally likely pairs of two days if each day is a quarter (ours check on W1 numbers; MacKay p. 68 eqs. 4.4–4.6 for the general rule). *Formula:* `h(x, y) = h(x) + h(y)` for independent x and y; so `log 1/(P(x)P(y)) = log 1/P(x) + log 1/P(y)`. *Check:* 1 + 3 = 4. *Limit:* only for independent events (the village assumes it, see 4c).
- **Edge.** Only for shares that are powers of 1/2 is the cost a whole number of questions; Gibson says the log "approximates" the length of the shortest uniquely decipherable code (Box 2, p. 4; U7 trap c). Step 7 returns to this.
- **In the café.** `x` = a drink (part 1); `P(x)` = its share in the till (part 2); `h(x)` = the questions that drink costs under the best script (part 8); "log₂ of 1/P" = how many times the queue must be halved (parts 3 and 4); additivity = two customers in a row, the two strings joined (parts 5, 6).
- **Widget W2 `lab` "Weather village"** appears at step 3 (see below).

#### Step 3. Average: entropy (≈ 520 words; G2, widgets W2 and W3)
- **G2 Guess first** (`data-answer-in="section 3, step 3"`). *With the best question script, how many questions does one day's word of the village radio cost on average?*
  - A. 1.25 questions
  - B. 1.50 questions
  - C. 1.75 questions ✔
  - D. 2.00 questions
- **Instance.** 8 days: 4 rain (1 question each), 2 sun (2 each), 1 wind (3), 1 snow (3): 4 + 4 + 3 + 3 = 14 questions in 8 days = 1.75 per day.
- **Question.** What single number describes the source?
- **Mechanism in words.** Weight each word's cost by how often it comes.
- **Formula.** `H = Σ P(x) log₂ (1/P(x))`, read: "the sum over all words of share times cost". Village: 1/2·1 + 1/4·2 + 1/8·3 + 1/8·3 = 1.75 (Shannon p. 18; Cover p. 15: "The resulting expected number of binary questions required is 1.75"). Convention 0 log 1/0 = 0 (MacKay p. 32).
- **Check.** Two ways. (i) The tree gives 1.75 questions. (ii) The grouping rule: first question splits rain (1/2) from the rest; then among the rest (sun 1/2, wind 1/4, snow 1/4) the entropy is 1.5, so `H = 1 + 1/2 × 1.5 = 1.75`. Equivalently 1 + 1/2·1 + 1/4·1 (Shannon p. 10, Fig. 6 and U8; MacKay p. 33). One check in a paragraph, the other in the widget.
- **Before and after (the crucial change).** Equal-size labels: 2.000 questions per day. Equal-share script: 1.750.
- **Extremes (ours; with sources).** The uniform village: H = 2.000, the largest possible for four words (MacKay p. 33: `H ≤ log |A_X|`; Shannon p. 11: H is largest when all are equally likely). A one-word village: H = 0, and "no channel is required" (Shannon p. 18, quote in 4c). The village script on the uniform village costs 2.25: a script is only right for the shares it was built for (ours, W2 readout).
- **Edge: names.** "Entropy" = the average surprisal (MacKay p. 32). "Uncertainty" in Shannon, Pierce, MacKay is a name for this number, not a feeling (U8 trap c). Entropy belongs to the distribution, not to one message (U8 trap b). Avoid "relative entropy" (U8 trap a). Cover p. 13: it depends only on the shares, not on what the outcomes are.
- **What it means (WRITING §7).** Measured: the average number of fair questions per word, on a source whose shares we assume known. It lets you predict: the cost of the best script per day (when shares are halves). It does not say what any word means, how long a real message is, or how good any script is for other shares.
- **In the café.** `Σ` = go through the day's customers (part 9); `P(x)` = how often that drink is ordered (part 2); `log₂ (1/P(x))` = the questions that drink costs (part 8); `H` = the day's average (part 9).
- **Widget W2 `lab` "Weather village"** (four sliders: weights of rain, sun, wind, snow). The reader sets the weights; the bars show each word's surprisal; the readout shows the shares, H, and the village script's average. Presets: "the village" (H = 1.750; script 1.750), "all equal" (H = 2.000; script 2.250), "only rain" (H = 0.000; script 1.000, the script still asks one question), "reversed" (H = 1.750; script 2.625). Edge cases taught: the script is only right for its own shares; entropy does not change when the shares are shuffled among the words.
- **Widget W3 `plot` "One event"** (slider p): the surprisal curve `log₂ (1/p)` and the average over "the event" and "not the event". Readouts at p = 0.001: 10.0 and 0.011; 0.01: 6.6 and 0.081; 0.1: 3.3 and 0.469; 0.2: 2.3 and 0.722; 0.5: 1.0 and 1.000; p = 1: 0 and 0. These match MacKay's p. 67 table (rounded to his digits). Edge: as p → 0 the surprisal grows without bound while the average falls back to 0.

#### Step 4. A question is an experiment: the best one splits the probability (≈ 330 words; widget W4)
- **Instance.** 12 balls, one is heavier or lighter, a balance with three outcomes (MacKay pp. 66, 68–70). 24 hypotheses (12 balls × heavy or light); 3² = 9 < 24 < 27 = 3³, so two weighings cannot do it and three might.
- **Question.** Which first weighing is best?
- **Mechanism in words.** The best experiment makes its outcomes as equally likely as possible. 4 against 4 splits the 24 hypotheses 8 : 8 : 8. 6 against 6 can never balance, so it splits them 12 : 12 : 0 (MacKay p. 68, p. 70; Fig. 4.2 p. 69 starts with 1 2 3 4 against 5 6 7 8).
- **Numbers (ours, rerun).** 4 v 4: 1.585 bits; 6 v 6: 1.000 bit; all 24 cases: log₂ 24 = 4.585 bits.
- **Formula.** The same `H`, now of the three outcomes of one weighing. MacKay concludes: "Thus we might conclude" an experiment's outcome is most informative if the distribution is uniform (p. 70; quote with the hedge; tied to `H ≤ log |A_X|`, not a theorem for every question, U5 trap).
- **Check.** 8/24 = 1/3 each: 3 × (1/3) log₂ 3 = log₂ 3 = 1.585.
- **Edge (MacKay's Exercise 4.9, p. 84).** Does 6 v 6 convey no information? About *which ball*, 0 bits (every ball is still possible); about *which ball and heavy or light*, 1 bit. Our answer, labelled ours (MacKay prints none, U5 trap); check-yourself question below.
- **In the café.** The weighing = a question with three possible replies (a nod, a shake, and a shrug); each reply's chance = its share of hypotheses (part 2 again); choosing the first weighing = choosing the first question of the script (part 4); the equal split of the *menu* (part 10) is the wrong split, the equal split of the *customers* (part 2) is the right one.
- **Widget W4 `lab` "First weighing"**: one slider, k balls per pan (1–6). Bars: the three outcome chances; readout: bits and the bits still unknown. Values: k = 1: 0.817; 2: 1.252; 3: 1.500; 4: 1.585; 5: 1.483; 6: 1.000. Preset "6 v 6" is the teaching edge case.
- **Check-yourself:** "Predict the worth of the 6 v 6 weighing before moving the slider. What does it tell you about *which ball*?" (Answer above.)

#### Step 5. The submarine: one answer can be worth six bits, a miss almost nothing (≈ 330 words; widget W5)
- **Instance.** An 8 × 8 grid, one hidden submarine (MacKay pp. 70–72, Fig. 4.3). First shot: a hit has chance 1/64.
- **Question.** What are one hit and one miss worth, and how do many misses add up?
- **Mechanism in words.** A hit identifies the square among 64: six halvings. A miss crosses off one square, so it takes away only a sliver of the options. After 32 misses, half the squares are gone: exactly one question's worth. The sum is the same however long it takes.
- **Numbers.** First hit: log₂ 64 = 6. First miss: log₂ (64/63) = 0.0227; second miss: log₂ (63/62) = 0.0231 by rounding (MacKay prints 0.0230 because he truncates; say so, U9). 32 misses: 1.0000 exactly; 48 misses: 2.0000; then a hit on the 49th shot, 16 squares left, is worth log₂ 16 = 4: total 6.0000 (MacKay p. 71).
- **Formula.** The product of the miss chances telescopes: `64/63 × 63/62 × … × (n+1)/n × n/1 = 64`, and the log of it is 6 whatever n (MacKay eq. 4.14). Do **not** quote eq. 4.11's last term 0.0430 (a misprint in this printing; U9).
- **Check.** 0.0227 + … sums to 1.0000 after 32 misses (rows computed by code).
- **What it means.** MacKay: "Now, it might seem a little strange that one binary outcome can convey six bits." (p. 71). His verdict, "I think the submarine example makes quite a convincing case for the claim that the Shannon information content is a sensible measure" (p. 72), keeps "I think" and is an argument, not a proof (U9 trap).
- **In the café.** The squares = the drinks still possible (parts 1, 2, updated as answers arrive); "Matcha?" asked first of a queue where matcha is one in 64 = a shot at one square (part 3): a "no" costs 0.0227 of a question, a "yes" costs six; total cost of finding the drink is the same on any path (part 8).
- **Widget W5 `stepper` "Submarine":** rows (computed by code first; per-row bits rounded, not truncated; note this in the first row's note):
  | shots | squares left | result | worth | total |
  |---|---|---|---|---|
  | 1 | 64 | miss | 0.0227 | 0.0227 |
  | 2 | 63 | miss | 0.0231 | 0.0458 |
  | 3–32 | 62 → 33 | 30 misses | 0.9542 | 1.0000 |
  | 33–48 | 32 → 17 | 16 misses | 1.0000 | 2.0000 |
  | 49 | 16 | hit | 4.0000 | 6.0000 |
  Notes per row; final note: "If the very first shot hits: 6.0000".
- **Check-yourself:** "A fifth of the grid is searched with five misses in a row. Is that worth more or less than the first miss? (Predict, then use the stepper.)" Answer: each later miss is worth slightly more than the one before (0.0227, 0.0231, 0.0235 …), because fewer squares are left.
- **Fold-out "Look inside: Wenglish"** (U10; not counted): in MacKay's made-up language, 5-letter words from 2¹⁵ = 32,768 equally likely words, so each word is 15 bits; a first letter `a` (chance about 0.0625) carries about 4 bits and `z` (about 0.001) about 10, but the five letters of a word always total 15 (MacKay pp. 72–73). Gibson's "uniform information density" is a hypothesis that information per unit time is roughly constant (glossary, p. 3), and Wenglish does not test it (U10 trap).

#### Step 6. Who encodes and who decodes (≈ 280 words; widget W6 diagram in steps)
- **Instance (the café).** The customer wants a mocha. The barista asks "Flat white?" (shake), "Latte?" (shake), "Mocha?" (nod). The string is shake, shake, nod, which is 1 1 0 (nod = yes = 0, shake = no = 1, Cover's convention for A = 0, B = 10 …).
- **Question.** Which side encodes and which decodes? (Kunhao's confusion, learner state 2026-10-15: he took Shannon's twin for the compressor.)
- **Mechanism in words (the roles, named).**
  - The **encoder** is the side that holds the original (here the customer's drink) and the agreed script, and turns the original into a string.
  - The **decoder** is the side that holds only the string and the same script, and turns the string back into the original. Shannon 1948 p. 2: the receiver "ordinarily performs the inverse operation of that done by the transmitter, reconstructing the message from the signal".
  - The script is the codebook both must hold before the day starts.
  - MacKay's wording (p. 70) says the questioning *strategy* defines the encoding; add the sentence that the strategy is shared in advance (U14 tension).
- **Shannon's twin (1951, correct roles, U14).** The subject has *not* seen the passage ("unfamiliar to the person who is to do the predicting", p. 54). He knows the text only up to the current point (pp. 54–55), guesses the next letter, and is told if he was right. The record of his guesses is the **reduced text**. In Fig. 2 (p. 55) the encoding side is ORIGINAL TEXT → COMPARISON with a PREDICTOR → REDUCED TEXT, and the decoding side is REDUCED TEXT → COMPARISON with an identical PREDICTOR → ORIGINAL TEXT. The twin, "mathematically, not just biologically identical", responds in the same way (p. 55). If the first person held the whole text in advance, every guess would be right and the record would carry nothing (U14 trap; our gloss).
- **A tiny walk-through (ours, labelled).** Predictor: a fixed ranked list of letters, E, T, A, … (a toy: Shannon's predictor uses the preceding text). Original "TEA". Encoder: T is the 2nd in the list; E the 1st; A the 3rd; the reduced text is 2 1 3. Decoder with the same list and only "2 1 3": 2nd = T, 1st = E, 3rd = A: "TEA". (We can also show the café's own version: string 110 + the script gives mocha.)
- **Do not** reuse Shannon's 69% and 77% as evidence for "1 bit per letter" (U14).
- **In the café.** Customer = part 5 (encodes); string = part 6; script = part 4 (both hold it); barista = part 7 (decodes).
- **Widget W6 `diagram` in 3 steps** ("customer → script → string → same script → barista"), config tested with `check.mjs` (parsed OK).
- **Check-yourself:** "In the café, who encodes? In Shannon's twin game, who decodes? What does each side need to hold?" Answers folded.

#### Step 7. When the shares are not halves (≈ 150 words; fold-out for the example)
- **Why.** The village is too nice: halves, quarters, eighths give whole numbers of questions, so the average equals H exactly (brief trap 2). Say it in the text so the reader does not think 1.75 is a rule.
- **The rule.** Cover p. 15 and §5.7 (pp. 94–95, eq. 5.61): the best expected number of questions lies between `H` and `H + 1`: `H(X) ≤ EQ < H(X) + 1` (quoted; the ladder is our small case in the fold-out). A sequence of questions is equivalent to a code, and the average number of questions to the average code length (Cover p. 94: "We now digress to show the equivalence of coding and the game of 20 questions").
- **Fold-out "Look inside: shares 0.7, 0.1, 0.1, 0.1" (ours, run in code).** H = 1.357 bits; the best whole-question tree has lengths 1, 2, 3, 3 and an average of 1.5; 1.357 ≤ 1.5 < 2.357. The first step of the tree is "Rain?" with a share of 0.7.
- **Check.** 0.7·1 + 0.1·2 + 0.1·3 + 0.1·3 = 1.5.
- **In the café.** Whole questions only: a customer cannot be asked half a question (part 3), so a share of 0.7 costs one whole question although 0.515 questions' worth of news arrives (log₂ (1/0.7) = 0.515). Extra cost is the gap between 1.5 and 1.357.
- **Equation E9 (script mismatch).** `EQ = Σ P(x) L(x)`, with `L(x)` = the questions the script spends on x. Village script on the uniform village: ¼(1+2+3+3) = 2.25. In the café: the owner's till is out of date (part 2) and the script (part 4) stays the same.

**Brief units cited in section 3.** U3, U4, U5, U6, U7, U8, U9, U14; U10 (fold-out). Pierce pp. 36–40, 80; MacKay pp. 26, 32–33, 66–73, 84; Cover pp. 5–6, 13–15, 94–95; Shannon 1948 pp. 1–2, 10–12, 18; Shannon 1951 pp. 54–56.

**Layer-3 equation table (each with an "In the café" line, as above).**
| Eq. | Statement | Café parts |
|---|---|---|
| E1 | `N = 2^k`, so `k = log₂ N` | 1, 3, 10 |
| E2 | `h(x) = log₂ (1/P(x))` | 1, 2, 3, 4, 8 |
| E3 | `h(x, y) = h(x) + h(y)` (independent) | 5, 6, 8 |
| E4 | `H = Σ P(x) h(x)` | 2, 8, 9 |
| E5 | grouping: `H = 1 + ½·H(½, ¼, ¼)` | 2, 3, 4 |
| E6 | `H ≤ EQ < H + 1`, with `EQ = Σ P(x) L(x)` | 2, 3, 4, 9 |
| E7 | outcome entropy of a weighing (three replies) | 2, 3, 4, 10 |
| E8 | telescoping `log₂ 64 = 6` | 1, 2, 3, 8 |
| E9 | script mismatch `EQ` on other shares (2.25) | 2, 4, 9 |

**The ladder per concept (WRITING §2; every step is in the text above).**
| Concept | Instance | Question | Mechanism | Numbers | Formula | Check | Limits |
|---|---|---|---|---|---|---|---|
| Bit (equal case) | 32 cups, 5 rats | how many tests? | halve | 5 | `k = log₂ N` | 2⁵ = 32; Cover H = 5 | 4 rats too few; worst case |
| Surprisal | village words | what does a word cost? | halve the queue | 1, 2, 3, 3 | `h = log₂ 1/P` | 1/8 → 3; MacKay table | whole only for halves |
| Additivity | rain then snow | cost of two days? | strings join | 1 + 3 = 4 | `h(x,y) = h(x) + h(y)` | log₂ 16 | independent only |
| Entropy | 8 days | the source's number? | weighted average | 1.75 | `H = Σ P h` | tree; grouping | assumes known shares; not meaning |
| Best question | 12 balls | which weighing? | equal outcomes | 1.585 vs 1.000 | `H` of outcomes | 3 × ⅓ log₂ 3 | MacKay's "might conclude" |
| One answer, many bits | submarine | what do hit and miss add to? | telescoping | 6, 0.0227, 1.0000 | `log₂ 64 = 6` | 32 misses → 1 | MacKay's "I think" |
| Roles | café and twin | who encodes? | original + script vs string + script | 110 → mocha; 213 → TEA | none (words) | round trip | toy predictor |
| Script cost, bound | 0.7 village | when shares are not halves? | whole questions | 1.357 ≤ 1.5 | `H ≤ EQ < H+1` | 0.7+0.2+0.3+0.3 | quoted; ours small case |

---

### 4. Abstract: the principle, its relatives and its limits (1,370 words; layer 4)

**Purpose.** Grow out of layer 3: strip the task away, name the relatives, and state the limits, each limit visible as an assumption in layer 3. Opens with the boxed **Short answer** (WRITING §0).

**Short answer (boxed, ≈ 150 words; verdict labelled ours).**
- *How much:* `log₂ (1/P)` questions for an outcome, under a stated model; the average is H. Check with the village: 1.75.
- *A surprise:* improbability under a model; it belongs to the model, not to the event (two forecasters give the same snow different numbers).
- *Worth:* questions saved, not importance, truth or meaning. Shannon (p. 1) sets meaning aside for "the engineering problem"; that is a scope decision, not a claim that meaning does not matter.
- Our verdict: the measure is a good price for improbability under a stated model, and a poor price for anything else. What would change our verdict: a source whose messages cannot be given a stable distribution; or evidence that the code-length reading ("approximates", Gibson p. 4) fails for the cases we use.

#### (a) What it really is (≈ 250 words)
- Surprisal re-codes a share into units that *add* for independent events (MacKay p. 68; log is the function that turns products into sums). H is its average, depends only on the distribution (Cover p. 13), is ≥ 0 with equality only when one outcome is certain, and is ≤ log |A| with equality only when all are equally likely (MacKay p. 33; Shannon p. 11). Information content approximates the length of the shortest uniquely decipherable code for the event (Gibson Box 2, p. 4; "approximates").
- Shannon's Theorem 2 (p. 11) says the only H with his three properties is `−K Σ p log p`. The text says that he calls the assumptions "in no way necessary for the present theory" and that "the real justification … will reside in their implications" (p. 11). We do not reproduce the proof.
- Averaging toward equality raises H, except for a permutation (Shannon p. 12, property 4; U8).
- Link back: this is E2 and E4 without the café.

#### (b) The same idea elsewhere (≈ 450 words; five lenses, each with link type, what it adds, what it does not explain)
| # | Lens | Link type | What it adds | What it does not explain |
|---|---|---|---|---|
| 1 | Statistical mechanics (Boltzmann's `S = k ln W`; Shannon p. 11; Pierce pp. 22–24; Cover p. 49) | **same-math in form only** | The sum `−Σ p log p` is about *distributions*, wherever the p are the shares of states, not about messages. Box of 4 cells: all molecules in one cell, 0; spread equally, 2 (the village numbers). | Identity of the two entropies. Pierce: the ideas are "quite different" and one can be fully useful without the other (pp. 23–24); both "can be described in terms of uncertainty, in similar mathematical terms" (p. 24); efforts to marry them "more interesting than fruitful" (p. 24); clear your mind of physics first (p. 80). The post stops at the form (U13). |
| 2 | Psycholinguistics (Gibson et al. 2019) | **structural analogy** (same quantity; its role is an empirical claim, not a theorem) | The number is also a hypothesis about minds: "language processing effort is associated with predictability" (p. 11, citing [104, 105] = Hale 2001, Levy 2008). Also used for colour-word difficulty (p. 7) and word length (p. 6, "likely reflects"). | Cause. Gibson et al. is a review; "associated with" is not "caused by". The papers behind the claim are UNSEEN. No baseline method (p. 14). Open limits such as taboo words (p. 15). We never write "surprisal predicts reading time". |
| 3 | Communication theory (Shannon's transmission diagram) | **metaphor** | The roles of sender, channel, receiver, and the narrow engineering scope (Shannon pp. 1–2). | Meaning, truth or effect, which is where the study of communication starts. Weaver's three levels are UNSEEN, so the post does not use them. |
| 4 | Bayesian probability | **structural analogy** | A one-off event has no frequency, but a person can hold a degree of belief; MacKay p. 26: the Bayesian view lets one-off propositions have probabilities. | That beliefs are right. In MacKay's Bayesian view "you cannot do inference without making assumptions" (p. 26), "not yet a globally held view"; same assumptions and same data give identical conclusions (p. 26). Our inference: different beliefs give different surprisal (labelled ours). |
| 5 | Search and decision (twenty questions, weighing) | **same-math** (a question tree *is* a code; Cover pp. 94–95) | The designer's view: choose the experiment with the most equal outcomes (MacKay p. 70). It turns a description into an action. | Cost of questions differing from one another, noisy answers, and questions that depend on earlier answers beyond the tree. |
- Closing comparison paragraph (≈ 80 words): the five lenses answer different questions: lens 1 *where else the sum appears*, lens 2 *whether minds use it*, lens 3 *what is left out*, lens 4 *where the shares come from*, lens 5 *what to do with it*.
- 3C tie: Computation (token log-probabilities and "novelty" scores are surprisals under a model), Communication (headline surprisal), Collaboration (a Shannon diversity index is the same formula on shares). Labelled as connection, not as findings.

#### (c) Where it fails (≈ 520 words; required)
Each boundary is tied to a layer-3 assumption and says where the café breaks.

| Boundary | Layer-3 assumption it comes from | Source | Where the café breaks |
|---|---|---|---|
| 1. **Meaning** | E2 has only `P(x)` in it, so two words with equal share get equal surprisal, understood or not | Shannon p. 1 ("irrelevant to the engineering problem"); Gibson p. 4 ("entirely agnostic to the form and content of messages"); Pierce p. 264 (a random pattern is "mathematically the most surprising" and "the dullest of all patterns"); p. 267 ("We can be surprised repeatedly only by contrast with that which is familiar, not by chaos"); Gibson p. 15 ("It is currently unclear whether such factors can be expressed as part of general communicative efficiency") | The barista cares which drink it is, whether the customer is allergic to milk, who is in a hurry. The script is blind to taste. |
| 2. **A known, stable distribution** | Step 2: the shares are given; step 3: "These probabilities are known but that is all we know" | Shannon p. 10; Pierce p. 81 (ergodic, for his simplest case: the shares "must not change with time") | The till's record gets old. The script built for the village costs 2.25 on a uniform day (E9), more than the plain 2 of the equal-size labels. |
| 3. **Independent days** | Step 2: Shannon p. 18 "successive symbols being chosen independently"; E3 | Shannon p. 18 | The regulars are not independent: a rainy morning makes hot drinks more likely; the same people come on the same days. |
| 4. **One-off events and whose model** | E2 needs `P(x)`; step 2 shares come from a record | Shannon p. 18 ("If a source can produce only one particular message its entropy is zero, and no channel is required": about transmission, not importance); MacKay p. 26 (beliefs as probabilities, with assumptions; same assumptions and same data give identical conclusions) | The till is a record of many days. A one-off event has no till. Two forecasters can write two shares for the same snow: widget W7 (Ana 3.00, Ben 1.00 for the snow). Ours. |
| 5. **Estimation** | The village shares are given. In practice they are estimated | Gibson p. 14 ("it is difficult to get reliable estimates … without very large datasets"); the size of the bias is our computation (notebook exercise 6) | The owner sees only a few days. Small table (ours, rerun at S4 with a fixed seed): mean plug-in H of sampled village days for n = 10, 30, 100, 1000 is about 1.50, 1.68, 1.73, 1.75 against the true 1.75: biased low for small n. |
| 6. **Whole questions, no noise** | Step 7: costs are whole numbers only for halves; step 6: the string always arrives intact | Cover p. 15 (H ≤ EQ < H + 1); Gibson Box 2 ("approximates") | Real shares are not halves, so a script has to round up (1.5 vs 1.357). Real nods can be misread. (Noise is outside this post.) |

- Add a closing "three kinds of statement" **check-yourself** (layer 4): label each as *theorem, definition, assumption or empirical claim*: (i) "The village's entropy is 1.75 bits" (a computation under the stated shares); (ii) "Probabilities must be known" (an assumption of the setup); (iii) "Reading effort follows surprisal" (an empirical claim, made by others, hedged "is associated with"); (iv) "Surprisal of two independent events adds" (a property that follows from the definition). Answers folded.
- **Widget W7 `lab` "Same snow, two forecasters"** (two sliders: Ana's chance of snow, Ben's). Default Ana 0.125, Ben 0.5: 3.00 vs 1.00, gap 2.00. Edge: equal beliefs give equal numbers (the number belongs to the model).
- **Brief units.** U7, U8, U11, U12, U13, U15 (and U6, U14 as backing).

---

### 5. The CSS imagination (750 words; layer 5, rubric 7)

**Purpose.** Turn the idea into questions about society with Mills' moves, as reasoning that stays within what the brief supports. All claims about society are labelled "ours" unless sourced. Four moves, each a paragraph of reasoning (~130 words) and a closing pair of research questions (~200 words). Mills' own pages are not in the brief (see requests); the text names the move and the terms only after the S2 supply or checks them; until then the layer uses them without a page cite.

- **Move 1. Trouble ↔ issue.** *Trouble (ours):* one reader cannot tell which of 200 messages in an inbox matters; she reads each by its surprise to her. *Issue at scale (ours):* a society's attention is allocated among messages whose surprisal is judged under models that readers do not see, and a platform's model is not a reader's model (layer 4(c), boundary 4: the number belongs to the model). The one sourced anchor: surprise works only against a familiar background (Pierce p. 267). Reasoning: what looks like a personal failure to cope (the trouble) is partly a structural fact about whose model sets the price.
- **Move 2. Extremes and inverted scale.** *Zero:* a village where it always rains needs no radio (H = 0; Shannon p. 18: "no channel is required"). *Infinity of equal options:* the village where every word is equally likely has the largest entropy and the least predictable day (H = 2.000 for four words). *Scale:* a country with one news channel and one with a million channels (ours): in the first, what the channel does not say has a huge price; in the second the same event has a different share at each channel. The question this raises: at what number of channels does a "known, stable distribution" (4c, boundary 2) stop being a sensible assumption?
- **Move 3. Another discipline's eyes.** A linguist (lens 2) asks whether comprehenders track surprisal, and finds an association claimed in the literature, not a theorem. A journalist asks what counts as news and answers with meaning and consequence (4c, boundary 1), which the number leaves out. A physicist sees the same sum as a count over states (lens 1) and stops, with Pierce, at the form. Each sees what the others miss, and none sees the model's owner.
- **Move 4. Comparison.** Compare the entropy of topic mixes across platforms or periods, or the surprisal of headlines across outlets, with the model held fixed. The comparison is only meaningful if the same model prices every case; otherwise differences in the numbers reflect differences in the models (4c, boundary 4).
- **Open research questions (ours, with data and method, tied to 3C).**
  1. *(Computation + Communication.)* Do posts with higher model-based surprisal spread further, after controlling for topic and emotion? **Data:** a post collection with share counts and a topic label; token probabilities from one fixed language model. **Method:** regression with topic fixed effects; report the sensitivity to the choice of model, since the number measures wording under that model, not the event. Ours; an invitation, not a finding.
  2. *(Collaboration + Communication.)* How does the entropy of a platform's daily topic mix change around a crisis? **Data:** posts labelled by topic (LLM surrogate labelling, Kunhao's own method). **Method:** plug-in entropy with bias correction and bootstrap intervals (4c, boundary 5), compared before and after a dated event. Ours.
- **Honesty line.** Where this section guesses, it says "ours" and says what evidence would test it.

**Widget.** None (reasoning section). **Quiz.** None here; transfer is in section 6.
**Cites.** U11 (Pierce pp. 264, 267; Shannon p. 1), U12 (MacKay p. 26; Shannon p. 18), U15 (Gibson pp. 11, 14), U7. Mills: pending (requests.md).

---

### 6. Your turn (280 words)

**Purpose.** Active practice: a Python notebook (run on Kunhao's Mac) and one transfer challenge.

**Transfer challenge (≈ 120 words, `.exercise`, hint and folded solution).** *A market stall sells five items with shares 1/2, 1/4, 1/8, 1/16, 1/16.* (a) Build the question script. (b) Compute the average number of questions and the entropy. (c) Change the shares to 1/4, 1/4, 1/4, 1/8, 1/8 and ask what the old script costs, and what the best script costs. Hint: halve the customers each time; the two rarest items get four questions. Solution (ours, run in code): script lengths 1, 2, 3, 4, 4; EQ = 1.875 = H. After the change: the old script costs 2.5; H = 2.25; the new best lengths are 2, 2, 2, 3, 3 and cost 2.25. The old script stops being best because it was built for the old shares (E9; 4c boundary 2).

**Notebook (≈ 160 words in the post: what it is, how to run, what to look for).** `posts/2026-12-surprise/notebook/01_surprise_entropy.ipynb`, plus `README.md` and `results.md` (post pattern). Python 3.9 or later, `numpy`, `matplotlib`, standard library; seeds fixed; the builder states the versions that were run and, for any relative error, its denominator (WRITING §7). Exercises, each with a hint and a folded solution (WRITING §6). The reader runs a cell, changes one line, and watches the number move.

| # | Exercise | What it computes | Expected output |
|---|---|---|---|
| 1 | `surprisal(p)`, `entropy(p)` with 0 log 0 = 0 | the village table | surprisal 1, 2, 3, 3; entropy 1.7500; uniform 2.0000; one word 0.0000; the stall of five 1.8750 |
| 2 | Simulate 100,000 village days; encode with the village script and with 2-bit labels; then run the village script on a uniform village | average string length | about 1.75 (script) vs 2.00 (labels); about 2.25 for the script on a uniform village (±0.01 with seed fixed; values recorded in `results.md`) |
| 3 | Submarine: sum the information of 32 misses; then a hit at a random shot | running totals | 32 misses sum to 1.0000; 48 to 2.0000; any hit shot gives total 6.0000; per-shot table prints rounded values (0.0231 for shot 2, MacKay prints 0.0230 by truncation) |
| 4 | Weighing: enumerate the 24 hypotheses, compute the outcome entropy for k against k (k = 1…6), and for 6 v 6 the information about *which ball* and about *which ball and direction* | outcome entropy table | k = 1…6: 0.817, 1.252, 1.500, 1.585, 1.483, 1.000; log₂ 24 = 4.585; 6 v 6: 0.000 bits about the ball, 1.000 bit about ball and direction |
| 5 | A text of your own (a methods section or a news article): letter surprisal table and entropy (27 symbols: a–z and space); optional word-level unigram surprisal | letter entropy; the three words that carry the most bits | for English, about 4 bits per letter (MacKay's table gives 4.11 for his texts, p. 32; Shannon 1951 p. 54 gives 4.03 for 27 symbols; do not mix them, U7); your number will differ from both: say why. Word-level: labelled "a model, not a mind" (U15) |
| 6 | Estimation bias: sample n = 10, 30, 100, 1000 village days, plug-in entropy, 2,000 repeats | mean estimate and its gap from 1.75 | about 1.50, 1.68, 1.73, 1.75 (gaps about 0.25, 0.07, 0.02, 0.00); our computation (Gibson p. 14 only says estimates need large datasets) |
| 7 | Whose model? Two beliefs about tomorrow's snow (1/8 and 1/2) | surprisal of the same event | 3.000 and 1.000 bits; gap 2.000 |
| 8 | Check the bound: a Huffman builder (`heapq`); for random shares on four to ten outcomes, compare `H`, the average length and `H + 1`; and the 0.7 village | the inequality `H ≤ EQ < H + 1` | 0.7 village: H = 1.357, EQ = 1.5; the inequality holds for all random draws |

**Quiz.** Transfer challenge; check-yourself in exercises (hints). **Cites.** MacKay p. 32; Shannon 1951 p. 54; Cover p. 15; Gibson p. 14.

---

### 7. Recall (300 words; 8 questions, each with a folded answer; all use only what this post teaches)

1. Why does the measure use a logarithm? *Two independent days add; log turns the product of shares into a sum (MacKay p. 68; U3).*
2. What is the surprisal of an outcome whose share is 1/16? *4 questions' worth (log₂ 16).*
3. What does 1.75 bits mean for the village? *The best script needs 1.75 yes/no questions per day on average, in this village.*
4. Why is 1.75 lower than 2, and when would the best script average exactly 2? *The shares are uneven; for four equally likely words.*
5. What does entropy not measure? *Meaning, value, truth, importance (Shannon p. 1; scope, not denial).*
6. Who encodes and who decodes? *The side with the original and the script encodes; the side with only the string and the same script decodes.*
7. Name two assumptions needed before an entropy means anything. *Known (and stable) shares; independent days (any two of the 4(c) list).*
8. Which claim about reading effort is empirical, and who makes it? *That effort is "associated with predictability"; Gibson et al., citing Hale 2001 and Levy 2008 (p. 11); not a theorem.*

Spaced review: questions 1–4 may reappear in a later post, without naming this one. The guess-first blocks G1–G3 have their reveals in section 3; recall asks different questions.

---

### 8. Sources (not counted)
Verified list, one `<li id="src-key">` per key: `shannon1948` (Bell Labs reprint pagination), `shannon1951`, `mackay2003`, `cover1991` (first edition, 1991), `pierce1961` (Harper first edition, 1961; scan provenance noted in S2 G2), `gibson2019` (pre-proof pages). Note the editions in the entries. If Mills is verified, add `mills1959`. Not used: Weaver, Hartley and Nyquist in their own words (UNSEEN), the reading-time papers (UNSEEN).

---

## Widget list (library: `site/ai4read/components`; all configs run in `check.mjs`; prototypes in the scratch directory, numbers pasted above)

| # | Where | Type | What the reader does | Numbers checked |
|---|---|---|---|---|
| W1 | §2 end; §3 step 2 | `diagram` ×2 in a `switch` (menu-split, customer-split); fallback: two stacked diagrams if a nested widget does not render | taps a panel; reads the questions per drink | trees parse OK in `check.mjs`; costs 2, 2, 2, 2 vs 1, 2, 3, 3 |
| W2 | §3 step 3 | `lab` "Weather village", 4 sliders | sets the weights of the four words; reads the shares, H, the village script's average | the village 1.750 / 1.750; all equal 2.000 / 2.250; only rain 0.000 / 1.000; reversed 1.750 / 2.625 |
| W3 | §3 step 3 | `plot` "One event" | slides p; watches the surprisal and the average | table above; at p = 0.1: 3.3 and 0.469 |
| W4 | §3 step 4 | `lab` "First weighing" | slides the balls per pan | 0.817, 1.252, 1.500, 1.585, 1.483, 1.000 |
| W5 | §3 step 5 | `stepper` "Submarine" | taps through rows | 0.0227; 0.0231; 1.0000; 2.0000; 6.0000 |
| W6 | §3 step 6 | `diagram` in 3 steps ("Who encodes, who decodes") | taps Next | no numbers; the string "no, no, yes" for mocha |
| W7 | §4(c) boundary 4 | `lab` "Same snow, two forecasters", 2 sliders | sets the two beliefs | 3.00 and 1.00; gap 2.00 |

Seven widgets, each with at most 4 sliders and 6–8 nodes, labelled "(toy, ours)" or with the source and page. The main number of every widget appears in the text above. A WIDGET-REQUEST (optional, not needed for release): a question game in which the reader plays the barista, picks a script, and sees a running average over many customers; `diagram` steps and the W2 lab approximate it, but cannot repeat.

## Quizzes at a glance
- **Guess first (3):** G1 submarine miss (end of layer 1); G2 village average (step 3); G3 cups and rats (step 1).
- **Check yourself (inside the layers):** layer 2 (2 questions: longest run; equal-share day); layer 3 (snow surprisal = 3; village script on a uniform village, predict 2.25 before moving the slider; 6 v 6 weighing; who encodes, who decodes; the stepper's "five misses"); layer 4 (four statements, label each theorem, definition, assumption or empirical claim).
- **Recall (8):** section 7. **Transfer challenge:** the market stall (section 6).
- Every question uses only what this post teaches and cites (WRITING §0).

## Self-score against the rubric (v1.1)

| Criterion | Score | Basis | Fixes made before handing over |
|---|---|---|---|
| **2. Four Layers and ladder** | **4** (aiming for 5 at S4) | All four layers present in order. Layer 1 introduces no concept (the logarithm, bit and probability appear first in layer 3; Nyquist's formula is held in a fold-out). Layer 2's draft has no formula, symbol or abbreviation and avoids the ten banned words. Every layer-3 equation E1–E9 has a café mapping to parts 1–10. Layer 4 has all three parts and the analogy-breaks column. Ladders are complete for bit, surprisal, additivity, entropy, best question, submarine, roles. The bound `H ≤ EQ < H + 1` is quoted from Cover with our small case and not derived in full, which caps the ladder for that concept at 4. | Added the table of the ladder per concept; added E9 for mismatch; moved Nyquist and Hartley formulas to a layer-3 fold-out so layer 1 stays concept-free; added the "Matcha?" first-question check to layer 2 so the submarine has a café footing. |
| **4. Insight and connections (layer 4)** | **4** | Layer 4 grows out of layer 3 (a→E2, E4; c→named assumptions). Each of five lenses names a link type, what it adds, and what it does not explain, and a comparison paragraph says how they differ. 3C link present. The post stands alone and names no other post. Weak spot: lens 3 (communication theory) is a metaphor with thin content because Weaver is UNSEEN. | Narrowed lens 1 to "same-math in form only" (Pierce); added the lens-2 limit "review, not result"; added the comparison paragraph. |
| **5. Illustrations and interactives** | **4** | Seven widgets covering each mechanism (two scripts, village, surprisal curve, weighing, submarine, roles, whose model) with edge cases as presets; every main number is checked with `check.mjs`. Two weaker spots: the bound and the estimation bias have no widget (a table from the notebook, ours); a `switch` with nested diagrams has not been tested in the render test. | Prototyped all configs; added W7; added the fallback for W1; recorded the render-test risk for S4. |
| **7. The CSS imagination** | **4** | Four of Mills' moves (trouble ↔ issue, extremes and inverted scale, another discipline's eyes, comparison), each as reasoning on this idea (whose model sets the price), two open questions with data and method, labelled ours, tied to 3C. Weak spots: all society claims are labelled conjecture because the brief contains no social-science source except Pierce p. 267; Mills' page cites wait for verification (requests.md), so the 5 is not reachable yet. | Anchored each move in a layer-4(c) boundary; added the sensitivity-to-model line to question 1; added the bias correction to question 2. |

Nothing is scored below 4. The criteria 1, 3, 6 are for the draft; planned length is 6,610 of 7,500 words, with no padding planned.

## Risks and checks for S4 (for the writer's own list)
1. Layer 2: grep for the banned words and any symbol before the first build.
2. Brief traps: cite Cover (1991) and Pierce (1961); say "eight values give three times, ours"; do not quote 0.0430 or "four times"; keep MacKay's "I think" and "Thus we might conclude"; use the corrected 1951 roles; "surprisal" is not in Shannon 1948; never write "relative entropy"; name the village's independence assumption.
3. Numbers: every widget number from `check.mjs` (prototypes above); the submarine rows rounded, not truncated, and flagged; notebook values from a fixed-seed run recorded in `numbers.md`.
4. Render: nested `switch` + `diagram` widgets at 390 px; W3's log axis ticks; W2's zero-weight guard.
5. Phone: at most five numbers per paragraph (the village paragraphs use small tables).
