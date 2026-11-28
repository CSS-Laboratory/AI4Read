---
post: 2026-12-surprise
stage: S5 round 2 (fact check of the revised draft)
checker: independent fact-checker (fresh agent; did not write the post or the earlier checks; did not read self-review.md or numbers.md)
checked: src/content.html (all, incl. fold-outs, quizzes, recall, widget labels, readouts and presets, Sources), audio-script.md, post.json, notebook/01_surprise_entropy.ipynb (re-executed), notebook/results.md, notebook/README.md
against: sources/*.pdf and *.txt (page text; page images rendered with pdftoppm for Cover pp. 86, 92, 93, 96, 97, 101 and MacKay pp. 99, 100), source-brief.verified.md units 1–23 and the new unit 24 (Addendum S2c, written in this round)
also read: review/response-1.md, review/verify-1.md, review/verify-1b.md, review/critic-1.md
date: 2026-11-28
---

# Verify 2: post 04 "How much is a surprise worth?"

**Counts: 0 critical · 3 major · 12 minor**

Release gate (rubric §A): not met while the 3 majors stand. Each major is a one-sentence fix on the page and the same fix in the audio.

**Layer 2 (§1a).** The café section, its two diagrams and its "Check yourself" have no formula, symbol, abbreviation or unexplained term. No major finding there. One internal inconsistency in the scene's rule is a minor (V2-07). "Till" is still there (V2-14).

**Task A.** New brief unit **24** (Addendum S2c, `source-brief.verified.md`): Huffman's procedure, from Cover & Thomas 1991 pp. 86, 92–97, 101 and MacKay 2003 pp. 98–102, 105. It is VERIFIED on page images. It answers `requests.md` item 5 and is the source for V2-01, V2-04 and V2-10.

---

## Round-1 majors: resolved?

| Round-1 major | Claimed fix (response-1) | Verdict | Evidence |
|---|---|---|---|
| V1-01 Pierce hedge and scope | term box quotes "is sometimes aggravated …", scoped to physics | **Resolved** | #village term box; Pierce p. 24 (pdf 40) matches; audio `village` has the same sentence. |
| V1-02 Gibson "reading effort follows surprisal" | "language processing effort is associated with predictability" everywhere | **Resolved** | Lens 2, fails (iii), recall 8, move 3 and the Sources note all match Gibson p. 11. No "reading", "Hale" or "Levy" is left on the page or in the audio, except the bibliography line and one sentence that says we do *not* claim reading time. |
| V1B-01 "Only halves, quarters and eighths" | "powers of one half (1/2, 1/4, 1/8, 1/16, …)", labelled ours | **Resolved** | #surprisal; audio `surprisal`. The claim is true: surprisal is a whole number exactly when p = 2^−k. |
| V1B-02 "reading effort" (second checker) | same as V1-02 | **Resolved** | Same places as V1-02. |
| V1B-03 audio adds "equal to H only when every share is a power of one half" | sentence deleted | **Resolved** | The sentence is not in `audio-script.md`, and the recap now matches the page. (The page now says the *if* direction in #entropy, "It predicts the cost of the best script when the shares are powers of one half". That is true but uncited; see V2-10.) |
| V1B-04 audio lens 2 adds attribution | audio now reads the page's lens-2 text | **Resolved** | Audio `lenses` matches the page word for word, apart from the citations. |
| C1-01 café roles (live asking) | hatch, ticket, two cards; roles step rebuilt; boundary 6 | **Resolved**, with two minor residues | The roles now match Shannon's transmitter → signal → receiver (pp. 1–2). Residues: V2-07 (the "stops at the first yes" rule does not fit the old card) and V2-06 (the live-asking boundary says more than the model allows). |
| C1-04 E5 grouping skips steps | fold-out E6 with steps (i)–(iii) | **Resolved** | 1 + ½ × 1.5 = 1.75 (Python); MacKay p. 33 (1/2, 1/4, 1/4 → 1.5); Shannon p. 10 rule. |
| C1-06 undefined second curve | plot has one curve; p = 1 edge case | **Resolved** | `surprisal-plot` config has one curve; check.mjs readout "p = 0.100: … 3.3 questions"; MacKay p. 67 values 10.0, 6.6, 3.3, 2.3, 1.0 match (Python: 9.97, 6.64, 3.32, 2.32, 1.00). |
| C1-07 binary recipe for rats | cut | **Resolved** | No binary-digit recipe or "35 → 100011" is left. "One of 64 integers" matches MacKay p. 70 ("an integer x between 0 and 63"). |
| C1-08 weighing, conditional information | fold-out; "information about which ball" removed | **Resolved**, one minor residue | The 12 : 12 : 0 split is labelled "our count", and "never balance" is cited to p. 68. Residue: the widget readout "… {left} remain" brings the removed quantity back as an average (V2-12). |
| C1-09 E8 factors | s, s−1, hit, cancellation, braces | **Resolved** | Algebra checked; the four-square check 0.415 + 0.585 + 1.000 = 2.000 (Python). |
| C1-10 g2 already answered | new g2 on the 0.7 village; answer 1.50 | **Resolved** (factually) | H = 1.3568, Huffman lengths 1, 2, 3, 3, EQ = 1.5 (notebook and Python). The right option is not the longest. Pedagogy note for the critic: the village widget's "0.7, 0.1, 0.1, 0.1" preset in step 3 already shows "1.500" before the guess. |
| C1-11 notebook ladder, ex. 4(b) | reordered; ladder in ex. 8; 4(b) gone | **Resolved** | Re-executed: 0 errors; every printed number equals `results.md`. Residues: V2-04 (ex. 8 still calls the rule unsourced) and V2-16. |
| C1-05 twin game re-muddles roles | fold-out | **Resolved** | Shannon 1951 p. 54 (dash record), p. 55 (twin, "encoded form"). The toy walk-through uses guess ranks, as in Shannon's second version (p. 56), and is labelled ours. |

The audio lines quoted in `response-1.md` were checked by script against `audio-script.md`: **every quoted audio line is present** (punctuation normalised). One line quoted under V1B-13 is a page quote, not an audio quote, and it is on the page. One claimed fix is not made: C1-24 says "the till" became "cash register", but "by the till" is still in the café paragraph, on the page and in the audio (V2-14).

---

## Major

### V2-01 · Lens 5 turns "most informative" into a search rule and leaves out MacKay's own limit (#lenses, lens 5; audio `lenses`)
- **Post:** "The designer’s view, in MacKay’s tentative conclusion (“we might conclude”): to find something fast, choose the experiment whose outcomes are most nearly equally likely" (MacKay 2003, p. 70). Audio: "In MacKay's tentative conclusion, we might conclude that to find something fast, you choose the experiment whose outcomes are most nearly equally likely."
- **Source:** MacKay 2003, p. 70 (pdf 82), and p. 68; MacKay p. 100 (pdf 112) and p. 98; Cover & Thomas 1991, p. 97 (pdf 119). Brief units 5 and 24.
- **What the source says:**
  - MacKay p. 70 concludes about a single experiment: "the outcome of a random experiment is guaranteed to be most informative if the probability distribution over outcomes is uniform". On p. 68 the equiprobable rule is stated for each step of the weighing procedure.
  - For a whole search, he warns on p. 100: "It is not the case, however, that optimal codes can always be constructed by a greedy top-down method" that splits into near-equiprobable subsets. In Example 5.18 the greedy method gives 2.53 against Huffman's 1.97 (rerun in Python).
  - Cover p. 97, on Fano's equal-split procedure: "This scheme, though not optimal in general, achieves L(C) ≤ H(X) + 2."
- **Why it matters:**
  - "To find something fast" is a claim about the expected number of questions in a whole search, and it is attributed to MacKay.
  - His own book says that the even-split rule, applied step by step, does not always give the fastest search.
  - It also contradicts the post's step 6, which builds the best script bottom-up ("join the two rarest") and says nothing about the clash. A reader who applies lens 5 to MacKay's seven-outcome example gets a script about 28% longer.
- **Severity:** major (our generalisation presented as the author's; a condition the reader needs is dropped; rubric §A).
- **Fix:** Write "for one experiment, MacKay's tentative conclusion (“we might conclude”) is that it is most informative when its outcomes are equally likely (p. 70)". Add to **Does not explain**: "a whole search: splitting every group as evenly as possible is not always the fastest script (MacKay 2003, p. 100; Cover & Thomas 1991, p. 97); step 6's rule is." Make the same change in the audio.

### V2-02 · "Uniquely decipherable" is defined as "no string is the start of another" (#answer, section 4(a); audio `answer`)
- **Post:** "(“approximates” is the authors’ word; “uniquely decipherable” means no string is the start of another, so a run of answers can be cut into words in only one way)". Audio: "Uniquely decipherable means no string is the start of another, so a run of answers can be cut into words in only one way."
- **Source:** Cover & Thomas 1991, pp. 80–81 (pdf 102–103), definitions and Table 5.1; p. 92 (pdf 114).
- **What the source says:**
  - p. 80: "A code is called uniquely decodable if its extension is non-singular": any encoded string has only one source string.
  - p. 81 gives a separate definition: "A code is called a prefix code or an instantaneous code if no codeword is a prefix of any other codeword."
  - p. 81 also says "The uniquely decodable code is not prefix free and is hence not instantaneous", about the example code in Table 5.1.
- **Why it matters:**
  - The gloss gives the definition of a *prefix* code as the meaning of *uniquely decipherable*. Prefix-free implies uniquely decipherable, but the converse is false (Cover's own example).
  - It is a new gloss, so it is a new claim (WRITING §9). It also contradicts the post's own correct gloss in step 2 ("a script whose rows of answers can be cut back into words in only one way").
- **Severity:** major (a false definition of a technical term, attached to a quoted source's word).
- **Fix:** Write "“uniquely decipherable” means a run of answers can be cut into words in only one way; scripts in which no string is the start of another, like the café card, are one kind (Cover & Thomas 1991, pp. 80–81)". Or reuse the step-2 gloss and drop the prefix clause. Make the same change in the audio.

### V2-03 · Mills' "cannot very well be defined" loses its hedge, and an example sentence becomes a general one (#imagination, move 1; audio `imagination`)
- **Post:** "An issue, he says, “unlike even widespread trouble”, cannot be defined within everyday surroundings; there “The very structure of opportunities has collapsed” (Mills 1959, pp. 8–9)." Audio: "An issue, he says, unlike even widespread trouble, cannot be defined within everyday surroundings. There, he writes, the very structure of opportunities has collapsed."
- **Source:** Mills 1959, pp. 8–9 (pdf 15–16); text layer checked, and the page-break line read on pdf 16.
- **What the source says:**
  - "it is the very nature of an issue, unlike even widespread trouble, that it cannot very well be defined in terms of the immediate and everyday environments of ordinary men" (pp. 8–9).
  - "The very structure of opportunities has collapsed" is said only of the example of 15 million men out of work, after "we may not hope to find its solution within the range of opportunities open to any one individual" (p. 9).
- **Why it matters:**
  - "cannot very well be defined" becomes "cannot be defined", a dropped hedge, and the words are attributed with "he says".
  - "there" makes the collapse sentence look like Mills' general account of issues rather than his unemployment example.
  - Brief unit 18 has the same unhedged paraphrase ("cannot be defined in terms of everyday environments"), so the error starts in the brief (WRITING §9: fix the brief too).
- **Severity:** major (dropped hedge, rubric §A), with a minor scope slip inside it.
- **Fix:** Write "An issue, he says, “unlike even widespread trouble”, “cannot very well be defined” within everyday surroundings; in his unemployment example, “The very structure of opportunities has collapsed” (pp. 8–9)." Make the same change in the audio, and correct the unit 18 claim in `source-brief.verified.md`.

---

## Minor

### V2-04 · The Huffman rule is still labelled "ours, not from our sources" (#nothalves; audio `nothalves`; notebook ex. 8)
- **Post:** "A rule, ours and not from our sources (notebook exercise 8 does it in code): repeatedly join the two rarest outcomes into one group …". Notebook ex. 8: "This is the Huffman method; the post labels the rule as ours, not from its sources."
- **Source:** brief unit 24.
  - Cover & Thomas 1991, p. 93: "combining the two least likely symbols into one symbol, until we are finally left with only one symbol".
  - Cover, p. 101: Theorem 5.8.1, "Huffman coding is optimal".
  - Cover, p. 94: "the optimal series of questions is that determined by the Huffman code".
  - MacKay 2003, p. 99, Algorithm 5.4: "Take the two least probable symbols … Combine these two symbols into a single symbol, and repeat."
- **Severity:** minor (attribution; the rule and the lengths are correct).
- **Fix:** Cite it: "This rule is Huffman's (Cover & Thomas 1991, pp. 92–94, 101; MacKay 2003, p. 99)". Keep the conditions from unit 24: shares known and fixed, one outcome at a time, the result shortest on average but not unique. Change the audio and notebook ex. 8 to match, and add the Cover pages to the Sources note if wanted.

### V2-05 · The forecaster widget cannot show 1/8: its slider rounds 0.125 to 0.13 (#fails, `forecast-lab`; audio `fails`)
- **Post:** the config has `"min":0.01,"step":0.01,"value":0.125`, and the preset "Ana 1/8, Ben 1/2" sets `a: 0.125`. The audio says "Ana says one eighth … Ana is surprised by three, Ben by one. The gap is two."
- **Evidence (ours):** the real `widgets.js` was loaded in headless Chromium (Playwright).
  - On load the slider reads **0.130** while the readout says "3.00 … Gap: 2.00", because the readout uses the raw config value.
  - After the preset "Ana 1/8, Ben 1/2" is clicked, the readout is "Ana is surprised by **2.94** … Gap: **1.94**": the browser snaps a range input to its step grid (0.01 + k × 0.01).
  - `check.mjs` reports 3.00 only because it does not use a range input.
- **Severity:** minor for the facts. It fails the render rule "every widget's displayed numbers equal the numbers in the text" (rubric §C).
- **Fix:** Use `"min":0.005,"step":0.005` for both sliders (0.125, 0.25 and 0.5 are then on the grid), and rerun a browser check.

### V2-06 · The live-asking boundary credits the live barista with something the fixed tree already does (#fails, boundary 6; audio `fails`)
- **Post:** "a real barista at the counter can ask live, change her next question after a surprising answer, or ask what the customer meant. Our card is fixed in advance (it stops at the first yes, but the whole tree is written down) …"
- **Source:** Cover & Thomas 1991, pp. 94–95 (unit 24).
  - "Any question depends only on the answers to the questions before it". The whole series is a code, and with known shares "the optimal series of questions is that determined by the Huffman code".
  - Cover adds that "we need not wait for the answer to the first question to ask the second" (p. 95).
- **Why it matters:** with shares known in advance, changing the next question after an answer is already part of a written tree, so it is not where the model breaks. The model breaks where the barista changes her *shares* (learns), asks a question outside the tree, or asks about meaning (boundaries 1 and 2).
- **Severity:** minor (our reasoning, imprecise).
- **Fix:** Write "a real barista can update her idea of the shares as the day goes on, ask a question that is not on any card, or ask what the customer meant; with known shares, choosing the next question from the last answer is already what a written tree does (Cover & Thomas 1991, p. 94)". Make the same change in the audio.

### V2-07 · The café's general rule "stops at the first yes" does not fit the old card (#cafe, first paragraph; audio `cafe`)
- **Post:** "The customer answers the card’s questions on the ticket, one after another, and stops at the first yes." Then the old card asks "Is your drink on the left side of the board?" and "Is it the top one?", and "Every ticket has two answers".
- **Why it matters:** under the stated rule, a flat-white customer would stop after "yes" to the first question, and the barista could not name the drink. The two-answer count for the old way only holds if she answers both questions.
- **Severity:** minor (internal inconsistency in the layer-2 scene; the numbers are right once the rule is scoped).
- **Fix:** Move "and stops at the first yes" to the new card ("The card now says … and the customer stops at her first yes", which is already in the next paragraph), and drop it from the general description. Make the same change in the audio.

### V2-08 · Two "In the café" lines equate surprisal and entropy with the best script's cost in general (#surprisal and #entropy mappings; audio)
- **Post:** step 2: "\(h(x)\) is the drink’s cost: the answers on its ticket under the best script." Step 3: "\(H\): the day’s average under the best script." Audio: "H is the day's average under the best script."
- **Source:** the post's own step 6 (0.7 village: H = 1.357, best script 1.5); Cover & Thomas 1991, p. 86, Theorem 5.3.1: expected length ≥ H, "with equality iff" every share is a power of 1/2 (unit 24, condition 5).
- **Severity:** minor (true for the village, false in general, and the post says so later).
- **Fix:** Add "(here, where the shares are halves; step 6 shows the general case)" to both lines.

### V2-09 · The submarine's "In the café" line uses "cost" for "worth" (#submarine; audio `submarine`)
- **Post:** "A no on the ticket costs 0.0227 of a question; a yes costs six. Whichever path the customer takes, the total worth of finding her drink is the same: the cost of that drink."
- **Why it matters:** the café defines a drink's cost as "the answers on its ticket". Under a script that begins "Matcha?", a "no" costs one whole answer but is worth 0.0227. For a drink whose share is not a power of 1/2 (or under a poor script), the number of answers on its ticket is not its total worth. What is the same on every path is the sum of the worths, the drink's surprisal (E2, E8).
- **Severity:** minor (label slip that teaches a wrong identity).
- **Fix:** "A no on the ticket is worth 0.0227 of a question, a yes six. Whichever path the customer takes, the worths along it add to the drink’s surprisal, log₂ of one over its share (ours)."

### V2-10 · "It predicts the cost of the best script when the shares are powers of one half" is uncited and unlabelled (#entropy, "What it means"; also the g2 answer "no script of whole questions can reach it here")
- **Source:** Cover & Thomas 1991, p. 86, Theorem 5.3.1: expected length ≥ H, "with equality iff" every share is \(D^{-l}\); "Thus we have equality in the theorem if and only if the distribution of X is D-adic" (unit 24).
- **Severity:** minor (correct, but neither cited nor labelled ours).
- **Fix:** Cite Cover & Thomas 1991, p. 86 for both sentences, or label them ours.

### V2-11 · The audio's "Three checks" gives two (audio `cafe`)
- **Post (page):** three checks. The third is "a card built for the old shares would do worse than the plain board".
- **Audio:** "Three checks. If the card began with matcha … A question helps most when both answers are likely. If all four drinks sold equally, the clever card would save nothing." The third check is missing.
- **Severity:** minor (audio does not match the page).
- **Fix:** Add "and a card built for the old shares would do worse than the plain board" to the audio.

### V2-12 · The weighing readout says how many bits "remain", an average the post does not explain (#entropy, `weigh-lab`)
- **Post:** readout "Of the 4.585 bits needed, {left} remain." For 1 v 1 this reads "3.768 remain".
- **Why it matters:** for uneven splits (k = 1, 2, 3, 5) the hypotheses left differ by outcome (2, 2 or 20 for 1 v 1). 3.768 is the average of log₂(hypotheses left) over outcomes, the conditional quantity that round 1 asked to remove (C1-08). It is exact only for 4 v 4 (8 left) and 6 v 6 (12 left).
- **Severity:** minor.
- **Fix:** Write "… remain on average" or drop the clause. Alternatively show "hypotheses left: 8 / 8 / 8", which the notebook already computes.

### V2-13 · "3.9 or later" reads as a matplotlib version (#turn)
- **Post:** "The reference run used Python 3.12 with numpy and matplotlib (3.9 or later should work; we did not test it)". The audio and README say "Python 3.9 or later".
- **Severity:** minor (ambiguous; matplotlib 3.9 exists).
- **Fix:** "(Python 3.9 or later should work; we did not test it)".

### V2-14 · "The till" is still in the café, though response-1 says it was replaced (#cafe; audio `cafe`)
- **Post:** "The same card hangs on the wall by the till and on the wall in the back room". The response for C1-24 says "“the till” → “cash register” (first use)".
- **Severity:** minor (a claimed fix not made; an everyday British word, but the critic flagged it).
- **Fix:** "by the cash register", on the page and in the audio.

### V2-15 · The Mills "there" scope slip is listed under V2-03, so it is not counted again.
(Not counted.)

### V2-16 · Notebook leftovers
- Ex. 3 hint: "The product of the miss chances telescopes". *Telescopes* is not defined. The post dropped the word in round 1 (V1-12), and the post's product is of miss *ratios* (64/63 …), not chances. Fix: "each numerator cancels the next denominator (the post's E8)".
- Ex. 8: "Predict first: for which shares is EQ exactly H?" The solution never answers it. Fix: one printed line, "EQ = H exactly when every share is a power of 1/2 (Cover & Thomas 1991, p. 86)", or drop the question.
- **Severity:** minor (counted as one).

---

## Checked and found correct

**Numbers (Python, check.mjs, re-executed notebook).**
- Village surprisals 1, 2, 3, 3; H = 1.75; uniform 2.000; one word 0.000; reversed 1.750.
- Village script on a uniform village 2.25 (simulated 2.2470); on "only rain" 1.000.
- 0.7 village: H = 1.3568 → 1.357; best lengths 1, 2, 3, 3; EQ = 1.5; gap 0.1432 → 0.143; H + 1 = 2.357; log₂(1/0.7) = 0.5146 → 0.515.
- Share 0.3: 1.737 → 1.74. Pierce three values: log₂ 3 = 1.585 (+58.5%); eight values: 3×.
- Weighing k = 1…6: 0.817, 1.252, 1.500, 1.585, 1.483, 1.000; log₂ 24 = 4.585.
- Submarine:
  - four-square check: 0.415, 0.585, 1.000, sum 2.000;
  - misses 0.02272, 0.02308, 0.02346, 0.02385, 0.02425, rounded 0.0227, 0.0231, 0.0235, 0.0238, 0.0242; log₂(64/59) = 0.1174;
  - shot 2: 0.0227 + 5.9773; shot 33: 1 + 5; shot 49: 2 + 4 (last miss 0.0875); shot 64: 6 + 0.
- Wenglish 4.00 and 9.97; 26^5 = 11,881,376.
- Market stall: 1.875 and 1.875; after the change, old script 2.5, best 2.25, H 2.25.
- Estimation table: 1.5036, 1.6753, 1.7253, 1.7469 (gaps −0.2464, −0.0747, −0.0247, −0.0031), rounded as on the page.
- Unit 24 examples: 2.3 and 2.2855; 2.53 against 1.97.

**Widgets.**
- `check.mjs`: 8/8 configs OK.
- In Chromium (real `widgets.js`), every preset of `village-lab`, `weigh-lab` and `sub-lab` gives the numbers the text and captions state. The exception is `forecast-lab` (V2-05).

**Notebook.**
- Re-executed with nbclient in the specified environment (Python 3.12.12, numpy 2.5.5, matplotlib 3.11.2): 0 errors. Every printed line equals `results.md`.
- The execution counts match the cell numbers in `results.md`. The sample text has no "j" (26 distinct symbols, as stated).

**Citations, pages and quotes.**
- Every quotation on the page that is followed by a citation was matched by script against the pdftotext text of the cited page (±1 page). All were found except OCR-damaged lines in Pierce (pp. 81, 267), which earlier rounds checked on the page image, and Mills p. 213, which only fails because of a line-break dash and matches. Checked by hand:
  - Shannon 1951: p. 54 (dash record, "unfamiliar"), p. 55 (twin, "encoded form"); the twin also appears in the second version on p. 56.
  - Shannon 1948: p. 14 ("relative entropy" as H/Hmax).
  - Cover & Thomas 1991: p. 15 ("lies between H(X) and H(X) + 1"), pp. 94–95 (equivalence quote, eq. 5.61).
  - MacKay 2003: p. 26 ("not yet a globally held view"), p. 68 (3² < 24, 3³ = 27, "never balance"), p. 70 ("an integer x between 0 and 63"), p. 71 (eqs. 4.9–4.10), p. 74 (raw bit content).
  - Gibson et al. 2019: p. 7 (colour score is a product with a production factor, which supports "also weighs how likely a speaker is to use the word"), p. 11 (gender paragraph).
  - Pierce 1961: p. 24 ("can be fully useful …", "similar mathematical terms", "aggravated"), p. 38 ("60 per cent", "four times"), p. 40 (Hartley's conditions; E more often than Z "should govern the lengths of the secondary symbols").
  - Mills 1959/2000: p. 73 (both sides), p. 214 ("sense of proportion"), p. 215 ("Nowadays at least", "in which I control the scale of everything", villages of 30 millions).
  - Shannon 1951, p. 54: F1 table, 4.03 for 27 letters (notebook ex. 5).

**Hedges and labels.**
- "Ours" labels are present where the post reasons on its own: the pain paragraph, our reading in the hook, rats, the four-square check, E5 numbers, the 12 : 12 : 0 split, the toy walk-through, the bias explanation, the layer-5 cases and the research questions.
- MacKay's "Thus we might conclude", "I think" and "Intuitively" are kept.
- Gibson's "approximates", "is associated with", "likely reflects" and "currently unclear" are kept.
- Mills' "Perhaps", "I believe", "Often" and "Nowadays at least" are kept. "cannot very well" is not (V2-03).

**Other files.**
- Sources entries: editions and page notes match the brief's "Editions"; MacKay version 7.2, fourth printing, 28 March 2005 matches the PDF's title page.
- `post.json`: the summary matches the post; the cite keys match the Sources ids; the date matches the eyebrow.
- Audio: it matches the page apart from V2-01, V2-02, V2-03, V2-04, V2-06, V2-07, V2-08, V2-09, V2-11 and V2-14. Its numbers match the page.
- Word count 6,844 (cap 7,500).
