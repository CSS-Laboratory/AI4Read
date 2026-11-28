---
post: 2026-12-surprise
stage: S5 round 3 (last review round), fact check of the revised draft
checker: independent fact-checker (fresh agent; did not write the post or earlier checks; did not read self-review.md or numbers.md)
checked: src/content.html (all, incl. fold-outs, quizzes, recall answers, widget labels, readouts, presets and captions, Sources), audio-script.md, post.json, notebook/01_surprise_entropy.ipynb (re-executed), notebook/results.md, notebook/README.md, the built index.html (Playwright)
against: sources/*.pdf (pdftotext per page; page images rendered for Pierce p. 38 and Gibson p. 1) and source-brief.verified.md units 1–24 (unit 18 as corrected by the meta-manager; unit 24 Huffman)
also read: review/response-2.md, review/verify-2.md, review/verify-2b.md, review/critic-2.md
date: 2026-11-28
---

# Verify 3: post 04 "How much is a surprise worth?"

**Counts: 0 critical · 0 major · 7 minor**

Release gate (rubric §A, factual part): met. No critical or major finding. The seven minors are one-line fixes; V3-01, V3-03, V3-04 and V3-05 also touch the audio.

**Layer 2 (§1a).** The café section (prose, both diagrams, parts list, "Three checks", "Check yourself") was scanned by script and read: no formula, symbol, abbreviation or unexplained term. "Script" and "string" are defined where they appear; "ticket's length" and "order's worth" are defined in the parts list. No major.

---

## Round-2 majors: resolved?

| Round-2 major | Claimed fix (response-2) | Verdict | Evidence |
|---|---|---|---|
| V2-01 lens 5 "to find something fast" | lens 4 now "For one experiment … most informative when its outcomes are equally likely"; whole search differs (MacKay p. 100; Cover p. 97); step 6's rule is (Cover p. 101) | **Resolved** | #lenses lens 4 and audio `lenses` match. MacKay p. 70 "Thus we might conclude: the outcome of a random experiment is guaranteed to be most informative if … uniform"; p. 100 "It is not the case, however, that optimal codes can always be constructed by a greedy top-down method"; Cover p. 97 Fano "though not optimal in general". Step 6 gives Example 5.18, 2.53 vs 1.97 (recomputed: greedy lengths 3,3,3,3,2,3,3 → 2.53; Huffman 6,2,4,3,1,6,5 → 1.97). |
| V2-02 / V2B-02 "uniquely decipherable" = prefix | "a run of answers can be cut into words in only one way; scripts in which no string is the start of another … are one kind of these (Cover pp. 80–81)" | **Resolved** | #answer (a) and audio `answer`. Cover p. 80 (uniquely decodable: extension non-singular), p. 81 (prefix/instantaneous definition), p. 92 ("Since every instantaneous code is uniquely decodable"). Step 2 gloss is consistent. |
| V2-03 Mills hedge and scope | "“cannot very well be defined” … in his unemployment example, “The very structure of opportunities has collapsed” (pp. 8–9)" | **Resolved** | #imagination Move 2 and audio. Mills pp. 8–9 (pdf 15–16): "it cannot very well be defined in terms of the immediate and everyday environments"; the collapse sentence is in the 15-million example (p. 9). Brief unit 18 carries the meta-manager's correction. |
| V2B-01 Huffman "ours, not from our sources" | credited in step 6, lens 4, recall 8, notebook ex. 7 | **Resolved** | "not from our sources" is gone from page, audio and notebook. Citations checked: Cover p. 92 ("simple algorithm discovered by Huffman"), p. 93 (Example 5.6.1), p. 94 ("the optimal series of questions is that determined by the Huffman code"), p. 101 ("Huffman coding is optimal"); MacKay p. 99 Algorithm 5.4. Two small paraphrase slips in "Where it holds": V3-02. |
| V2B-03 audio recap "only when …" | recap rewritten as hypothesis | **Resolved** | Audio `imagination` recap now reads "Our hypothesis, not a finding: … part of the cause may lie in whose model prices them"; matches page Move 2 ("that it does so is a hypothesis, not a finding"). |
| C2-01 predict-first already answered | new predict-first on "reversed" (2.625, H 1.750) | **Resolved** | 2.625 appears nowhere above the exercise (first appears later in step 6). Widget `village-lab` preset "reversed" shows 2.625 and 1.750 in Playwright and check.mjs; Python 1/8·1 + 1/8·2 + 1/4·3 + 1/2·3 = 2.625. |
| C2-02 step 6 ladder (factual part) | Huffman credited with conditions and trap | **Resolved** | See V2B-01; conditions from unit 24 are on the page. |
| C2-03 ticket length vs worth | parts list, E2 and E4 café lines | **Resolved** | E2 café line: equal "only for shares 1/2, 1/4, 1/8, …" (true: log2(1/p) is an integer iff p = 2^−k). E4 café line: H equals the best script's average ticket length only for halves; Cover p. 86 Theorem 5.3.1 ("equality iff" D-adic). Submarine café line uses "worth" for 0.0227. |
| C2-04 hook (factual part) | Hartley paragraph cut; independence quote moved to the fold-out | **Resolved, minor residue** | Pierce p. 40 quotes verified. Residue: the main text and audio now give only one of Pierce's two conditions (V3-01). |
| C2-05 no widget builds a card | `cardlab` | **Resolved** | All numbers in the step-6 prose reproduce in check.mjs and in the built page (see Numbers). |

**Audio lines quoted in response-2.md.** Checked by script (`normalise → substring of audio-script.md`): 43 fragments, all present except three that are *meant* to be absent or are not audio quotes: the C2-11 sentence "A last button sets shares zero point seven …; keep it for step six" (deleted, correctly absent) and the widget-preset label "0.7, 0.1, 0.1, 0.1" quoted under C2-01 (a page item, not an audio line). V2-05's "Ana says one eighth, Ben one half. Ana is surprised by three, Ben by one. The gap is two." is present.

---

## Findings (all minor)

### V3-01 · Pierce's condition for Hartley's count loses its first half in the main text and audio (#hook; audio `hook`)
- **Post:** "Pierce says this count is acceptable only if each symbol “is equally likely to be selected” (Pierce 1961, p. 40)." Audio: "Pierce says this count is acceptable only if each symbol is equally likely to be selected." Audio recap: "Old measures counted possible messages, and they fit only equally likely choices."
- **Source:** Pierce 1961, p. 40 (pdf 56).
- **What the source says:** "acceptable in the light of our present knowledge of information theory only if successive symbols are chosen independently and if any of the s symbols is equally likely to be selected."
- **Why minor:** "only if X" stays true when the source says "only if X and Y", and the full condition is in the fold-out (#box-nyquist), in step 1 (Shannon's independence) and in boundary 3. But the main text reads as if equal likelihood were Pierce's whole condition.
- **Fix:** Write "acceptable only if successive symbols are chosen independently and each “is equally likely to be selected”", or add "(he also requires independent choices; section 4)"; same in the audio.

### V3-02 · Step 6 "Where it holds": two paraphrases drift from the cited pages (#nothalves; audio `nothalves`)
- **Post:** "It needs shares that are known and fixed (Cover & Thomas 1991, p. 94) … the best card is not unique, since swapping yes and no on a question gives another (Cover & Thomas 1991, pp. 96–97)."
- **Source:** Cover & Thomas 1991 p. 94 (pdf 116), p. 97 (pdf 119); MacKay 2003 pp. 100–101 (pdf 112–113).
- **What the source says:** Cover p. 94: "Assuming we know the probability distribution on the objects" (known, not "fixed"; "fixed/unchanging" is MacKay's "one unchanging ensemble", pp. 100–101). Cover p. 97: "inverting all the bits or exchanging two codewords of the same length will give another optimal code."
- **Why minor:** both statements are true (swapping yes and no at one question keeps every ticket length), but "fixed" is not on p. 94, and the single-question swap is our extension of Cover's "inverting all the bits".
- **Fix:** "shares that are known (Cover p. 94) and do not change (MacKay pp. 100–101)"; "since inverting every answer, or swapping two tickets of the same length, gives another (Cover p. 97)". Same in the audio.

### V3-03 · "the gap, 0.143" sits after rain's worth and reads as rain's gap (#nothalves; audio `nothalves`)
- **Post:** "Rain is worth 0.515 questions, but its ticket cannot be shorter than one; the gap, 0.143, is the price of whole questions."
- **Evidence (ours, Python):** rain's own ticket minus worth is 1 − 0.515 = 0.485; 0.143 is the day's gap EQ* − H = 1.500 − 1.357 = 0.1432. A reader who checks against the sentence just before gets 0.485.
- **Fix:** "… cannot be shorter than one. Over the day, the gap between the card and H, 1.500 − 1.357 = 0.143, is the price of whole questions." Same in the audio.

### V3-04 · Recall card 4 implies the best script averages exactly 2 only for equal shares (#recall card 4; audio `recall` Four)
- **Post:** "Why is 1.75 lower than 2, and when would the best script average exactly 2?" Answer: "The shares are uneven, so common words get short strings. With four equally likely words, H = 2."
- **Source:** Cover & Thomas 1991, p. 96 (pdf 118), Example 5.7.3: shares (1/3, 1/3, 1/4, 1/12) give Huffman lengths "(2,2,2,2) or (1,2,3,3)", both with the same expected length (= 2).
- **Evidence (ours, Python):** shares 0.3, 0.3, 0.2, 0.2 also give best lengths 2, 2, 2, 2 and EQ* = 2, with H = 1.971; Cover's example has H = 1.855.
- **Why minor:** the answer is a correct sufficient case, but it answers with H = 2, and step 6 has just taught that EQ* and H differ when shares are not powers of one half. A reader can take "equal shares" as the only case.
- **Fix:** "For example with four equally likely words (then H = 2 too). Uneven shares such as 0.3, 0.3, 0.2, 0.2 also need 2 on the best card, though H is below 2 (ours)." Same in the audio.

### V3-05 · Audio adds a Shannon claim that the page does not make (audio `entropy`)
- **Audio:** "Try only rain: the entropy is zero, and Shannon writes that no channel is required."
- **Page:** "“Only rain”: \(H = 0.000\) (Shannon 1948, p. 18)", with no "no channel" sentence.
- **Source:** Shannon 1948, p. 18: "If a source can produce only one particular message its entropy is zero, and no channel is required."
- **Why minor:** the claim is correct and on the cited page, but the audio must say what the page says.
- **Fix:** add "and, Shannon writes, “no channel is required”" to the page, or drop the clause from the audio.

### V3-06 · Nyquist's year cited to the wrong page (#box-nyquist, fold-out)
- **Post:** "As Pierce reports it, Nyquist’s result of 1924 relates the speed \(W\) … (Pierce 1961, p. 36)."
- **Source:** Pierce 1961, p. 35 (pdf 51): "In 1924, he published his results in an important paper"; the relation \(W = K\log m\) is on p. 36 (pdf 52).
- **Fix:** cite "Pierce 1961, pp. 35–36".

### V3-07 · The mathematical reading of Mills' "extremes" is not labelled ours (#imagination, Move 1; audio `imagination`)
- **Post:** "“Often you get the best insights by considering extremes” (Mills 1959, p. 213). A village where it always rains has \(H = 0\); four equal words give \(H = 2.000\)."
- **Source:** Mills 1959, p. 213 (pdf 220): "by considering extremes—by thinking of the opposite of that with which you are directly concerned" (despair and elation, the miser and the spendthrift). Brief unit 20, trap (b): Mills' extremes are opposite types, not a parameter pushed to its limits; "say so".
- **Why minor:** the section says "The names of the moves are ours", and the next sentence's 30 million listeners is labelled "(ours)", but the H = 0 / H = 2 pair directly after the quote reads as Mills' own application.
- **Fix:** "In our reading, the two extremes of the village are a village where it always rains (\(H = 0\)) and four equal words (\(H = 2.000\))." Same in the audio.

---

## What was checked and found correct

**Quotes.** Every quotation on the page (≈ 75) was matched by script against the pdftotext page text and its page number re-derived from the printed header (offsets: MacKay −12, Cover −22, Pierce −16, Mills −7, Shannon 1951 +49). Six needed a manual look because of line breaks or OCR and are verbatim: MacKay p. 72 ("I think the submarine example makes quite a convincing case"), Gibson p. 1 ("show how a pervasive pressure for efficiency guides the forms of natural language"), p. 3 (uniform information density), p. 14 ("it is difficult to get reliable estimates …"), Pierce p. 81 ("must not change with time if the source is to be ergodic"), Mills pp. 8–9 ("unlike even widespread trouble", across the page break). Mills appendix pages 212, 213, 214, 215 and p. 73 confirmed on the pdf pages. Shannon 1951 twin quotes are on printed p. 55, the "unfamiliar" quote and the dash record on p. 54. Gibson p. 1 image shows "ARTICLE IN PRESS" and "TICS 1894 No. of Pages 19" (Sources entry correct). Pierce p. 38 image confirms the first list of "eight current values" shows seven (0, 1, 2, 3, 4, 6, 7) and "four times".

**New round-2 text.**
- Step 6 ladder: village day joins (wind+snow → 1/4 → sun → rain), "first two" joins → 2.625, 0.7 day joins and tie, equal day; Huffman credit (Cover pp. 92–94, 101; MacKay p. 99); "shortest average length among scripts in which no string is the start of another" (Cover Lemma 5.8.1 and Theorem 5.8.1 compare instantaneous codes); E9 (Cover p. 15, eq. 5.61 p. 95); "\(\mathrm{EQ}^{*}\) equals \(H\) exactly when every share is a power of one half" (Cover p. 86); Example 5.18 (MacKay p. 100).
- "Ticket length" vs "worth": parts list, step 2 ("a ticket's length is whole, and a worth need not be"), E2/E4/E9 café lines, submarine café line (the per-customer sum of answer worths telescopes to log2 1/P(drink) for any card: ours, true).
- Predict-first 2.625 and answer text (rain and sun now rare, snow half the days).
- Recall cards 7 and 8 (8: Huffman pp. 92–94; 1.500 and 1.357).
- Lens 4 MacKay sentence and "Does not explain".
- Boundaries 1–7: Shannon p. 1, p. 10, p. 18; Pierce p. 81 with the gloss labelled ours; Gibson p. 14; Cover p. 94 for boundary 6 ("Any question depends only on the answers to the questions before it").
- Layer 5 opening: Mills pp. 4–6, p. 212 ("I believe"), p. 5 ("this Age of Fact"), Pierce p. 24.
- Notebook exercise 7: text, citations, hint, solution, printed answer to its prediction.

**Numbers (Python and check.mjs).** 14/8 = 1.75; clever card on equal day 2.25; log2 32 = 5, log2 64 = 6, 2^4 = 16; log2 3 = 1.585 (58.5 %); MacKay p. 67 values 9.97 → 10.0, 3.32 → 3.3, 1.0; share 0.3 → 1.737 → 1.74; 1/2 × 1/8 = 1/16 → 4; E6 1 + ½ × 1.5 = 1.75; weighing k = 1…6: 0.817, 1.252, 1.500, 1.585, 1.483, 1.000, log2 24 = 4.585, remaining 3.768 (1 v 1), 3.000 (4 v 4), 3.585 (6 v 6); submarine 0.415, 0.585, 1.000; 0.0227; 5.9773; misses 0.0227, 0.0231, 0.0235, 0.0238, 0.0242 (truncated: 0.0227, 0.0230, …, MacKay's 0.0230 matches truncation); log2(64/59) = 0.1174; Wenglish 2^15 = 32,768, a ≈ 4, z ≈ 9.97; 0.7 day H = 1.3568, log2(1/0.7) = 0.5146, EQ* = 1.5, gap 0.1432, H + 1 = 2.357; market stall 1.875 = 1.875, old script 2.5, best 2.25 = H; reversed 2.625; Example 5.18 2.53 vs 1.97.

**check.mjs** (9/9 configs OK): `surprisal-plot` 3.3; `village-lab` default 1.750/1.750/2.000, "all equal" 2.000/2.250, "only rain" 0.000/1.000, "reversed" 1.750/2.625; `weigh-lab` 1.585, 3.000 remain; `sub-lab` shot 49: 2.0000 + 4.0000 = 6.0000; `forecast-lab` 3.00, 1.00, gap 2.00; `card-lab` `{"auto":true}` 1.750 = best = H; `{"preset":1,"auto":true}` 1.500, best 1.500, H 1.357 (lengths rain 1, sun 3, wind 3, snow 2); `{"preset":2,"auto":true}` 2.000; `{"joins":[[0,1],[0,1],[0,1]]}` 2.625, best 1.750.

**Playwright** (built `index.html`, 390 px, network blocked; the only console errors are the blocked font/CDN requests). Every preset clicked: `village-lab` (4 presets), `weigh-lab` (4 v 4, 6 v 6), `sub-lab` (shots 1, 2, 33, 49, 64, all totals 6.0000; slider to 6 gives last miss 0.0242 and 0.1174 in all), `forecast-lab` (sliders read 0.125 and 0.5; "same belief" 2.00/2.00/0.00), `surprisal-plot` (0.001 → 10.0, 0.5 → 1.0, 1 → 0.0), `card-lab` (each preset with the rule pressed to the end, then "first two" joins three times). The page agrees with check.mjs and with the prose everywhere. On the village day the merged chip is placed first, so "always join the first two groups" really gives 2.625 on the page. On the 0.7 day the rule gives tickets rain 1, sun 3, wind 3, snow 2 in table order; the prose's "1, 2, 3, 3 (which 0.1 word gets 2 is a tie)" covers this. Every non-math sentence of `src/content.html` is present in the built page.

**Notebook.** Re-executed with nbclient in the given environment (Python 3.12.12, numpy 2.5.5, matplotlib 3.11.2): 0 errors; every printed line is identical to the saved outputs and to `results.md`; the execution counts match the `[cell n]` labels in `results.md`. The page's table (1.504, 1.675, 1.725, 1.747; gaps −0.246, −0.075, −0.025, −0.003) is the rounded output of exercise 6.

**Audio vs page.** All chapters read against the page. Apart from V3-01, V3-03, V3-04, V3-05 and V3-07, the audio says what the page says, keeps its hedges and "ours" labels, and adds nothing.

**post.json.** Title, date (7 December 2026, matching the eyebrow), num 4, tags ("Information theory", "Communication theory"), summary (true to the page) and the eight cite keys are consistent with the page and Sources.

**Sources.** Editions and page systems are stated correctly (Cover 1991 1st ed.; Pierce 1961 Harper; Shannon reprint; Gibson pre-proof; MacKay on-screen version 7.2; Mills 2000 Oxford printing, seven numbered items on pp. 212–216). Main text 7,044 words by `scripts/wordcount.py` (cap 7,500).
