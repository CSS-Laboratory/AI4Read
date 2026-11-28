---
id: 2026-12-surprise/topic-card
type: topic-card
series: information-theory, week 1
title_question: "How much is a surprise worth?"
stage: S0
created: 2026-11-28
status: proposed (awaiting Kunhao's go)
sources_read: posts/2026-12-surprise/sources/ (Shannon 1948, MacKay 2003, Pierce 1980, Cover & Thomas 2006, Gibson et al. 2019, plus Shannon 1951 copied from the library for the guessing-game roles)
---

# Topic card: How much is a surprise worth?

**One-line preview (for under the title).** A surprise is worth the number of yes/no questions it saves you: the rarer the news, the more questions it is worth, and the average over all possible news is the *entropy*.

## 1. The question

- **High-school version.** Some news tells you a lot and some tells you almost nothing. Can we put a number on how much news is worth, and what is the right unit?
- **Sharper research version.** If a source emits outcomes with known probabilities, why is the log of the inverse probability (surprisal) the right per-outcome measure, why is its average (entropy) the right measure of the source, and which assumptions must hold before those numbers mean anything?
- **Threshold words (WRITING §0).** The post fixes three senses and carries them to the end:
  - *Worth* = the number of fair yes/no questions the outcome saves, measured in bits. It is not usefulness, value or importance.
  - *Surprise* = improbability under a stated model of the source. It is not a feeling of astonishment.
  - *Information* = the engineering sense, a selection from a set of possible messages (Shannon 1948, p. 1). Pierce p. 24 warns that the popular sense (knowledge) creeps into discussions and confuses them.

## 2. Why it matters for Kunhao's 3C research

- **Computation:** every LLM score a CSS researcher uses (token log-probability, perplexity, surprisal-based "novelty" or "atypicality" of a post) is a surprisal under a model. The post gives the base unit and shows that the number belongs to the model, not to the event.
- **Communication:** crisis and misinformation messages compete for attention. Entropy of a platform's topic mix, or surprisal of a headline, are measurable but they exclude meaning, which is exactly where communication theory starts.
- **Collaboration:** diversity and concentration of topics or ties (a Shannon diversity index) is the same entropy formula applied to shares.

## 3. What the post will and will not claim

**Will claim (each checked against a page in the source brief):**
1. Hartley and Nyquist already used a logarithmic measure. It counts possibilities and is correct only when all choices are equally likely and independent (Pierce p. 40). The missing piece was probability (Shannon p. 1; Pierce pp. 36–40).
2. The worth of one outcome is `h(x) = log2 (1/P(x))` bits (MacKay p. 32; Gibson Box 2, p. 4). Independent outcomes add (MacKay p. 68).
3. Entropy is the average surprisal (MacKay p. 32; Cover p. 13). It is 0 when the outcome is certain and largest when all outcomes are equally likely (Shannon p. 11; MacKay p. 33).
4. A good yes/no question splits the *probability* in half, not the list of options (MacKay pp. 68, 70). The expected number of questions lies between H and H + 1 (Cover pp. 15, 94–95). It equals H exactly for the weather village, whose probabilities are halves, quarters and eighths (Shannon p. 18).
5. One yes/no answer can be worth many bits (a lucky hit worth 6 bits) and a typical answer almost nothing (a miss worth 0.0227 bits), but the total for finding the target is always 6 bits (MacKay pp. 71–72).

**Will not claim:**
- That entropy measures meaning, value, truth or importance. Shannon (p. 1) sets the semantic aspect aside as "irrelevant to the engineering problem". The post says this is a scope decision, not a claim that meaning does not matter.
- That surprisal *causes* reading effort. Gibson et al. (p. 11) write only that "language processing effort is associated with predictability" and cite Hale 2001 and Levy 2008 for it. The strongest evidence they list, Smith & Levy 2013 (reference 107, title seen only), is not in our sources (gap 3). The post reports the association as an empirical claim from the linguistics literature with its hedge, never as a theorem.
- That thermodynamic entropy and Shannon entropy are the same thing. The formula has the same form (Shannon p. 11), but Pierce (pp. 23–24) calls attempts to marry the two "more interesting than fruitful".
- Anything from Weaver's three levels. Weaver's essay is not in our sources (gap 1); the post uses Shannon's own statement.

**A person's claim.** The only person's claim used as a hint is Shannon's scope statement (p. 1). Strongest unhedged form: "These semantic aspects of communication are irrelevant to the engineering problem." It is scoped to "the engineering problem". Hedges that matter: Shannon says the entropy axioms "are in no way necessary for the present theory" and that "the real justification ... will reside in their implications" (p. 11). The post tests the claim by showing what the number leaves out (layer 4c).

## 4. Lenses (layer 4b; each states a link type)

| # | Lens (field) | Canon and wiki nodes | Link type | What only this lens shows |
|---|---|---|---|---|
| 1 | Statistical mechanics / thermodynamics | `canon/information-theory.md` (shannon-1948, cover-2006 pp. 12–49, pierce-1980 ch. II and V); `wiki/concepts/entropy-thermodynamic.md`, `thermodynamic-entropy.md`, `entropy-communication-sense.md` | **same-math in form only**; the physical interpretation needs extra assumptions | The same sum `-Σ p log p` appears where `p` is the share of microstates, so the formula is about *distributions*, not about messages. Pierce (pp. 23–24) says the marriage has been more interesting than fruitful, so the post stops at the form. |
| 2 | Psycholinguistics / efficient communication | `canon/information-theory.md` (gibson-2019-efficiency); `wiki/works/gibson-2019-efficiency/main.md`, `wiki/concepts/surprisal.md`, `uniform-information-density.md` | **structural analogy** (same quantity, a role claimed empirically, not a theorem) | Human comprehenders may behave as if they computed surprisal, so the number is also a hypothesis about minds. The only lens where the number is tested against behaviour. |
| 3 | Communication theory (Shannon–Weaver) | `canon/information-theory.md` (shannon-1949-mathematical-theory, need-copy); Shannon 1948 p. 1; Gibson p. 4 | **metaphor** (the transmission diagram) | Where the engineering sense stops: the model excludes meaning, truth and effect, which is what the field of communication studies is about. Weaver's levels are UNSEEN, so the post uses Shannon's sentence and Gibson's "entirely agnostic". |
| 4 | Bayesian / subjective probability | `wiki/concepts/subjective-probability.md`, `probability-as-extended-logic.md`; MacKay p. 26 | **structural analogy** (surprisal is relative to a stated model, so beliefs can supply the model) | Answers the one-off-event objection: a single event has no frequency, but a person can have a degree of belief. The price is that the number then depends on the assumptions (MacKay p. 26: "you cannot do inference without making assumptions"). |
| 5 | Decision / search (twenty questions, weighing) | `wiki/instances/twenty-questions.md` (incomplete, see gaps), `wiki/instances/weighing-problem.md`, Cover §5.7 | **same-math** (a question tree *is* a code) | The designer's view: choose the experiment whose outcomes are as close as possible to equally likely (MacKay p. 68). This links entropy to doing something, not only describing something. |

## 5. The Four Layers plan

### Layer 1. Motivation (no new concepts)
- **Old practice, checked against the sources.** The series entry says engineers "measured messages by length or by the number of signal levels (Hartley, Nyquist)". This holds only in part, so the card changes it:
  - *Nyquist* (1924, 1928) tied telegraph speed to the logarithm of the number of distinct current values: `W = K log m` (Pierce pp. 36–38). Going from two current values to four doubled the speed, as in Edison's quadruplex telegraph (p. 38).
  - *Hartley* (1928) defined the information of a message as the logarithm of the number of possible sequences: `H = n log s` (Pierce pp. 39–40; Shannon p. 1 credits him with the logarithm).
  - So the old measure was **already logarithmic**. Its pain was that it counts possibilities and is right "only if successive symbols are chosen independently and ... equally likely" (Pierce p. 40). It gives the same number to "it rained" and "it snowed in July".
  - *Morse* (1838) gave E a single dot, and estimated letter frequencies by counting a printer's type box (Pierce p. 25). The idea that frequent things deserve short codes was old; a number for it was missing. Week 2 uses Morse as its main motivation, so week 1 may skip it.
- **Strange phenomenon.** One yes/no answer can be worth six bits, and another almost nothing (the submarine, MacKay p. 71). Pierce (p. 23): a message that is one of ten possible messages tells less than one that is one of a million.
- **Urgent problem.** Engineers (and today analysts of text) need one number for "how much did this message tell me" that works when messages are not equally likely.
- **Guess first (end of layer 1).** A submarine hides in one of 64 squares, all equally likely. You fire at one square and miss. How many fair yes/no questions' worth of news is that miss? Options (same length, serious): about one whole question / almost nothing, about one-fiftieth of a question / exactly nothing / about six questions. Answer: almost nothing (0.0227 bits); a *hit* would be worth six. (No bits or logs in layer 1: the unit is "a fair yes/no question's worth".)

### Layer 2. Intuition: the guessing barista (no formulas, no symbols, no abbreviations)
- **Scene.** A loud café where the grinder drowns speech, so a customer can only nod or shake their head. The owner knows from the till that half the customers want a flat white, a quarter a latte, an eighth a mocha, an eighth a matcha. The barista must find out a regular's drink with nods and shakes only, and each question costs a second.
- **Old way.** The barista splits the *menu* into equal halves, "is it on the left of the board?", then "is it the top one?" Two questions for everyone. Where it goes wrong: she spends two questions on flat white, which half the customers order, and asks as much for the rare matcha as for the common one.
- **The rule that changes.** Split the *customers*, not the menu: "flat white?" settles half the queue in one question; then "latte?"; then "mocha?". Common drinks cost one or two questions, the rarest cost three, and the average falls from two to one and three-quarters. A rare order costs more questions, so the rare order is the bigger surprise.
- **Two extremes, told in words.** If all four drinks sell equally, the clever script saves nothing and the board shape does not matter. If everyone orders the same drink, the barista need not ask anything.
- **Parts list for layer 3 to map:** the drinks (outcomes); the share of customers who want each (probabilities); one nod or shake (one yes/no answer, one bit); the question script agreed in advance and kept by both barista and till (the code, a tree); the customer, who knows the drink and answers (holds the secret); the string of nods and shakes (the message); the barista who reads the string and names the drink (decoder); how many questions one drink costs (surprisal); the average over a day's customers (entropy).
- **Roles (Kunhao's open confusion, learner state 2026-10-15).** The one who knows the secret turns it into a string of answers (encodes); whoever holds the same script and the string recovers the secret (decodes). Layer 2 says this in plain words ("the person who knows turns the drink into nods; the person who sees the nods turns them back into a drink"); layer 3 repeats it with the terms encode and decode and with Shannon's twin (below).
- **Check-yourself (no formulas):** (a) Who gets the longest run of questions, and why? (b) What would the barista do on a day when the regulars change their taste?

### Layer 3. Concrete: the weather village, in the field's own setting
Re-introduce the four-word weather village (toyworlds W1) from scratch: a village radio sends one word a day, rain 1/2, sun 1/4, wind 1/8, snow 1/8 (Shannon 1948, p. 18; Cover pp. 14–15). Ladder (WRITING §2), each step with an "In the café" line:
1. **Equal case first (Kunhao's 32 cups and 5 rats).** One poisoned cup among 32, five rats drink in parallel; or five fair yes/no questions. Five bits, because 2^5 = 32 (Cover p. 5; MacKay p. 70, "sixty-three" version; the cups-and-rats framing is Kunhao's puzzle, not from a source). *Edge:* with 4 rats, 2^4 = 16 < 32, so the puzzle cannot be solved (MacKay p. 74: the raw bit content is a lower bound on guaranteed questions). Note for the writer: the rat version asks all questions at once, the 20-questions version asks them in turn; with equal probabilities the count is the same, with unequal ones the adaptive tree is the one the entropy bound talks about.
2. **Unequal case: surprisal.** Best questions for the village: rain? (1), sun? (2), wind? (3), snow (3, no more questions after "not wind?"). Pattern: question count = log2 (1/p). Formula `h(x) = log2 (1/P(x))`, every symbol read aloud. Check: rain 1, sun 2, wind 3, snow 3 (MacKay p. 32 defines it; Gibson p. 4 names it surprisal). Additivity check: rain today and snow tomorrow = 1 + 3 = 4 bits = log2 16 (MacKay p. 68).
3. **Average: entropy.** Pattern: weight each cost by how often it happens. `H = Σ P(x) log2 (1/P(x))`; village: 1/2·1 + 1/4·2 + 1/8·3 + 1/8·3 = 1.75 bits (Shannon p. 18). Check by the tree (1.75 questions), and by the grouping rule: 1 + 1/2·1 + 1/4·1 = 1.75 (Shannon p. 10, Fig. 6; MacKay p. 33). Key before/after: equal-count script 2.000 → equal-probability script 1.750. Edge cases: uniform village 2.000 (largest), one-word village 0; the village script on a uniform village costs 2.25 (worse than 2.000, so a script is only good for the shares it was built for).
4. **A question is also an experiment (weighing).** 12 balls, one odd, three-outcome balance: 24 cases, 4.585 bits; one weighing gives at most 1.585 bits; 4 against 4 gives that, 6 against 6 gives 1.000 bit, because it can never balance (MacKay pp. 66, 68–70, Exercise 4.9 on p. 84).
5. **Submarine.** A miss on the first shot is worth 0.0227 bits, a hit 6 bits, and 32 misses add to exactly 1.000 bit (MacKay pp. 71–72). Total for finding the target is 6 bits whenever it is hit.
6. **Roles.** The answerer who holds the secret encodes; the person with the script and the string decodes. Shannon's twin game (1951, p. 55): the first person, who has the text, writes the guess numbers (encodes); the twin, who has only those numbers, uses the same guessing procedure to recover the text (decodes).
7. **Numbers for the write-up** come from `check.mjs` and the notebook, never by hand (WRITING §6).

The smallest non-powers-of-two example sits in a fold-out ("Look inside: when shares are not halves", ours): shares 0.7/0.1/0.1/0.1 give H = 1.357 bits and the best whole-question tree averages 1.5, inside Cover's bound H ≤ average < H + 1 (p. 15; the 1.5 is our Huffman computation).

### Layer 4. Abstract
- **(a) What it really is.** Surprisal is a re-coding of probability into units that *add* for independent events (MacKay p. 68); entropy is its average and depends only on the probabilities, not on what the outcomes are (Cover p. 13). Shannon's three-axiom derivation (Theorem 2, p. 11) pins the formula down but he calls the axioms "in no way necessary", and the post does not reproduce the uniqueness proof (Appendix 2 is beyond layer 3's scope). Gibson Box 2 (p. 4): information content *approximates* the length of the shortest uniquely decipherable code.
- **(b) The same idea elsewhere.** Lenses 1–4 in section 4, each with link type and what it does not explain.
- **(c) Where it fails (required).**
  - *Meaning:* the number is blind to what a message says (Shannon p. 1; Gibson p. 4). Pierce p. 264: a completely random pattern is "mathematically the most surprising" and also "the dullest". Pierce p. 267: surprise only works against a familiar background.
  - *Known, stable distribution:* Shannon p. 10 ("These probabilities are known but that is all we know"); Pierce p. 81 (probabilities must not change with time for an ergodic source). The weather village assumes independent days (Shannon p. 18, "successive symbols being chosen independently"), which real weather is not.
  - *One-off events:* a single message has no frequency (Shannon p. 18: a source that can produce only one message has zero entropy). The way out is probability as degree of belief (MacKay p. 26), and then the number depends on the believer's assumptions.
  - *Estimation:* the probabilities must be estimated from data, which is unreliable without very large datasets (Gibson p. 14). The notebook shows the plug-in entropy of a small sample is biased low (our computation).
  - *Where the café breaks:* real shares are not halves (so average questions sits between H and H + 1); the nods are noiseless; the script must be agreed in advance and the shares must stay put; customers do not order independently.

### Layer 5. The CSS imagination (Mills; WRITING §1b)
Uses four moves; all claims about society are labelled "our conjecture" unless sourced.
- **Trouble ↔ issue.** One reader cannot tell which of 200 notifications matters (trouble, ours). At platform scale the issue is how attention is allocated among messages whose "surprise" is judged by a model the reader does not see (ours). Pierce p. 267 gives the one sourced anchor: surprise needs a familiar background.
- **Extremes and inverted scale.** The village where it always rains needs no radio (Shannon p. 18); the village where every word is equally likely has the largest entropy and the least predictable day. Scale up: a country with one news channel vs a million channels (ours).
- **Another discipline's eyes.** A linguist (Gibson, lens 2) asks whether comprehenders track surprisal; a journalist asks what is "news"; a physicist sees the same formula as a count of microstates (Pierce's caution applies).
- **Comparison.** Compare the entropy of topic mixes across platforms or periods, or the surprisal of headlines across outlets, with the model held fixed.
- **Open research questions (ours, with data and method, tied to 3C):**
  1. *Computation + Communication.* Do posts with higher model-based surprisal spread further, after controlling for topic and emotion? Data: posts with share counts; token probabilities from one fixed language model; method: regression with topic fixed effects. Caveat built in: the number measures wording under the model, not the event.
  2. *Collaboration + Communication.* How does the entropy of a platform's daily topic mix change around a crisis? Data: posts labelled by topic (LLM surrogate labelling, Kunhao's own method); method: plug-in entropy with bias correction and bootstrap intervals (layer 4c estimation caveat).

## 6. Interactives, quizzes and notebook (Kunhao's request, 2026-11-28)

### 6a. Interactive widgets (component library `site/ai4read/components/`; checked with `check.mjs`)
Prototype configs for the two `lab` widgets ran in `check.mjs` (village: H = 1.750, tree = 1.750, uniform tree = 2.250; weighing: 4 v 4 gives 1.585, 6 v 6 gives 1.000). Phone-first limit: 4 sliders, 6–8 nodes. Priority order, so the meta-manager can cut from the bottom.

| # | Widget type | Where | What the reader does | Edge case as preset |
|---|---|---|---|---|
| 1 | `lab` "Weather village" | L3 steps 2–3 | Four sliders for the weights of rain, sun, wind, snow (probabilities are derived by dividing by the total). Bars show each word's surprisal; readout shows H, the average questions of the village script, and the 2-bit labels (2.000). | "village" (4,2,1,1: 1.750 = 1.750); "all equal" (script cost 2.250, entropy 2.000); "only rain" (H = 0; a zero weight uses `if(p>0,...)`, the 0 log 0 = 0 convention) |
| 2 | `diagram` with `switch` | L2 end, L3 step 3 | Steps through the question tree: the equal-halves-of-the-menu tree (two questions each) vs the equal-halves-of-the-customers tree (1, 2, 3, 3). Taps move one customer down the tree and count nods. | "rare drink" highlights the 3-question path |
| 3 | `plot` | L3 step 2 | Slide `p` and watch two curves: `log2(1/p)` and the binary entropy; marks reproduce MacKay Fig. 4.1 (p = 0.001: 10.0; 0.01: 6.6; 0.1: 3.3; 0.2: 2.3; 0.5: 1.0, entropy 0.011, 0.081, 0.47, 0.72, 1.0, p. 67). | p → 0 (surprisal grows without bound; entropy returns to 0) and p = 1 |
| 4 | `lab` "First weighing" | L3 step 4 | One slider, k balls per pan (1–6). Bars: P(left heavier), P(right heavier), P(balance); readout: outcome entropy and the 4.585 bits still unknown. | k = 6: balance impossible, entropy 1.000 |
| 5 | `stepper` "Submarine" | L3 step 5 | Walks through shots 1, 2, 3, ... 32 (rows computed by code first): chance of a miss, bits for the miss, running total; ends at 1.000 bit after 32 misses, then a hit worth 4 bits (shot 49) gives the total 6. | Shot 1 hit: 6 bits |

`<!-- WIDGET-REQUEST -->` for the meta-manager: a *question game* the reader plays (hidden drink, nod/shake with a chosen script, a counter of questions, a running average over many customers). `diagram` steps approximate it but cannot count or repeat. Not needed for release.

### 6b. Quizzes (all use only what this post teaches; WRITING §0)
- **Guess first (the `.quiz` / `.reveal` block):**
  - G1 (end of layer 1): the submarine miss (above).
  - G2 (start of layer 3, step 3): "With the best script, how many questions does the village radio's word cost on average? 1.25 / 1.50 / 1.75 / 2.00." Answer 1.75; the reveal shows the tree.
- **Check yourself (small questions inside the layers, answer folded):**
  - Layer 2: who gets the longest run of questions, and why; what changes if all drinks sell equally.
  - Layer 3: surprisal of snow (3 bits); the village script on a uniform village (2.25: predict before moving the slider); 6 v 6 first weighing (predict the entropy, then check; MacKay's "both right and wrong" about 6 v 6 turns on *which ball* (0 bits) vs *which ball and heavy or light* (1 bit)); who encodes and who decodes in the café and in Shannon's twin game (Kunhao's confusion).
  - Layer 4: label each of four statements as "theorem", "definition", "assumption" or "empirical claim" (e.g., entropy of the village = 1.75; probabilities must be known; reading effort follows surprisal; log is additive).
- **Recall questions (end of post, 5–8):** (1) Why a log? (two independent days add). (2) Surprisal of an outcome with probability 1/16. (3) Meaning of 1.75 bits for the village. (4) Why 1.75 < 2 and when is the best script's average exactly 2? (5) What does entropy not measure? (6) Who encodes and who decodes? (7) Name two assumptions needed before entropy means anything. (8) Which claim about reading effort is empirical, and who makes it? Items 1–4 can come back later in spaced form without naming this post.
- **Transfer challenge (layer 6):** a market stall sells five items with shares 1/2, 1/4, 1/8, 1/16, 1/16. Build the script, compute the average questions and the entropy (both 1.875), then change one share and say why the script stops being best.

### 6c. Python notebook (Kunhao runs it on his computer)
`posts/2026-12-surprise/notebook/01_surprise_entropy.ipynb` plus a `README.md` and `results.md` (post 03's pattern). Standard library plus numpy; seeds fixed. Builder states what was run (Python and numpy versions) and, for any relative error, its denominator (WRITING §7). Exercises, each with a hint and a folded solution (WRITING §6):
1. `surprisal(p)` and `entropy(p)` with 0 log 0 = 0; reproduce the village table (1, 2, 3, 3; 1.75).
2. Simulate 100,000 village days. Encode with the village script and with 2-bit labels; average length 1.75 vs 2. Then run the village script on a uniform village: 2.25.
3. Submarine: sum the information of 32 misses (1.000), then of a hit at a random shot (always 6.000).
4. Weighing: enumerate the 24 hypotheses, compute outcome entropy for k against k (k = 1..6), and the information about *which ball* vs *which ball and direction* for 6 v 6.
5. A text of your own (a methods section, a news article): letter surprisal table and entropy; compare with MacKay's English-letter value of about 4.11 bits per letter (p. 32), and say why yours differs. Optional word-level unigram surprisal: which three words carry the most bits, and what the number does not say about them.
6. Estimation bias: sample n = 10, 30, 100, 1000 village days, compute the plug-in entropy, repeat 2,000 times; the mean sits below 1.75 for small n (our computation; Gibson p. 14 only says estimates need large datasets).
7. Challenge: two people with different beliefs about tomorrow's weather assign different probabilities. Compute the same event's surprisal for each.

## 7. Sources, gaps and fixes to the series entry

**In the knowledge base (digests are maps, not truth).** The five canon works are in `wiki/works/` with `grounding: primary-text`; audited digests are `shannon-1948-mathematical/main-p1`, `mackay-2003-information/ch04-source`, `cover-2006-elements/ch02-entropy.pipeline` and `shannon-1951-prediction/main`. Gibson and Pierce digests are unaudited. The brief was built from the PDFs, not from the digests.

**Changes to the series entry (proposals that did not hold or needed a change):**
1. "Engineers measured messages by length or by the number of signal levels (Hartley, Nyquist)." Partly wrong: both used a logarithm. Changed to: counting possibilities is right only for equally likely, independent choices (Pierce p. 40).
2. "Same-math: thermodynamic entropy (with care)". Kept, but narrowed to "same-math in form only" because Pierce (pp. 23–24) says the interpretation has been confusing and not fruitful.
3. "Structural analogy: surprisal and reading effort (Gibson 2019)". Gibson 2019 does not report reading-time data. It defines surprisal (p. 4), uses it for colour-word difficulty (p. 7, a different role: how hard it is to pick the chip from the word) and says processing effort "is associated with predictability" citing others (p. 11). The post cites it for that sentence and for the definition only.
4. "Entropy ignores meaning (Weaver's semantic level)". Weaver's essay is not in the sources. The claim rests on Shannon p. 1 and Gibson p. 4; Weaver's levels are named only as a pointer in lens 3 if Kunhao supplies the book.
5. "Twenty questions (L2)". Kept, but the café scene has unequal shares from the start, because equal shares would not show the rule that changes (split probability, not options). The 32 cups / 5 rats puzzle moves to layer 3 as the equal-case rung.
6. Cover & Thomas dates Hartley "in the 1930s" (p. 49); Shannon (p. 1, footnote 2) and Pierce (p. 39) give 1928. The post uses 1928.
7. The wiki node `wiki/instances/twenty-questions.md` says Cover mentions twenty questions only in Problems 7 and 13. Cover §5.7 (pp. 94–95) states the equivalence of source coding and twenty questions, with `H(X) ≤ EQ < H(X) + 1`. The digest `cover-2006-elements/ch05-data-p1.md` has it right; the instance node should be fixed.

**Gaps (none blocks the post):**
1. *Weaver's introductory essay* (Shannon & Weaver 1949, the three levels). `shannon-1949-mathematical.pdf` in the library folder `communication-theory/` is the 1948 paper alone (checked: the extracted text is identical), not the book. Request to Kunhao: a copy of the 1949 book, or leave Weaver out. Never a shadow library.
2. *Hartley 1928, "Transmission of Information"* and *Nyquist 1924/1928*. Not in the library. The post relies on Pierce pp. 36–40 and Shannon p. 1. Hartley's own wording is UNSEEN. Free route to try later: Bell System Technical Journal 1928 scans (public domain status of the 1928 issue to be checked by Kunhao).
3. *Smith & Levy 2013*, "The effect of word predictability on reading time is logarithmic", Cognition 128, 302–319, and Levy 2008, Hale 2001: only titles seen through Gibson's reference list (p. 18). Fetch from the authors' pages or open-access repositories if the post is to say more than Gibson does; the network was not used at S0/S1.
4. *Wiki and canon:* `canon/information-theory.md` lists Pierce and Weaver as `need-copy`; Pierce's text we hold is the 1961 text reprinted by Dover in 1980, OCR with garbled layout in places. Quotes from it carry an OCR warning in the brief.
5. *Shannon 1951* is read only for the guessing-game roles (pp. 55–56); its numbers (about 1 bit per letter) are out of scope for this post.
