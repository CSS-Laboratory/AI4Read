# Verify 3c: light fact-check of the round-3 polish diff (post 04)

Scope: `git diff a1b7d3d 19bdc29 -- src/content.html audio-script.md`, read with `review/response-3.md`. Only changed or new sentences checked. Checker: fresh agent, did not write or review the post before. No network; sources read from `sources/*.txt` (page split on form feeds; printed page headers read in the text; MacKay printed = pdf − 12, Cover printed = pdf − 22, Pierce printed = pdf − 16).

**Counts: critical 0 · major 0 · minor 6**

---

## Findings

### V3C-01 · minor · step 6 table, row "0.7 day" (and its audio line)
- **Post:** table row "0.7 day | 1, 2, 3, 3 | 1.500 | 1.357", under the column head "tickets: rain, sun, wind, snow". Audio: "On the zero point seven day the tickets are one, two, three, three".
- **Source:** our widget (`check.mjs --id card-lab --values '{"preset":1,"auto":true}'`): `len1 1, len2 3, len3 3, len4 2`, so the button gives rain 1, **sun 3, wind 3, snow 2**.
- **What it says:** The tie is real (the prose says "Which 0.1 word gets 2 is a tie"), and the average 1.500 is right either way. But the new column head makes the row a claim per word, and a reader who presses the button sees 1, 3, 3, 2, not 1, 2, 3, 3. Before the polish, the prose said only "Tickets 1, 2, 3, 3", with no word order.
- **Fix:** Change the row to "1, 3, 3, 2" (what the button gives), or write "1, then 2, 3, 3 in some order (a tie)", and make the audio match.

### V3C-02 · minor · audio, step 6, the table paragraph
- **Post (audio):** "the average is one point five, and H is one point three six." Three paragraphs later the same chapter says "One point three five seven is at most one point five zero zero".
- **Source:** Python: H(0.7, 0.1, 0.1, 0.1) = 1.35678. The page has 1.357 in both places.
- **What it says:** The number is right, but the audio uses two roundings of the same value in one chapter, and only the first differs from the page.
- **Fix:** Say "one point three five seven" in the table paragraph too.

### V3C-03 · minor · #nothalves, "Why the two rarest?" (page and audio)
- **Post:** "They sit deepest on the card, with the longest tickets, so an extra question there falls on the fewest customers and costs the least in total (ours)."
- **Source:** Brief unit 24, trap (c): Cover p. 101 calls the rule "greedy". He says it "coalesces the two least likely symbols at each stage", and that the proof shows "this local optimality ensures a global optimality of the final code".
- **What it says:** The reasoning is correct for one join: that join is the cheapest one possible. But "costs the least in total" can be read as "so the whole card is cheapest", and that is the theorem, not something one step shows. The label "ours" covers the reasoning, but not a reading of it as a proof.
- **Fix:** Write "…falls on the fewest customers, so this join costs the least of any join at this step (ours); that the finished card is then the best is Cover and Thomas's theorem".

### V3C-04 · minor · #imagination, Move 3, new closing sentence (page and audio)
- **Post:** "The two questions predict different things (ours; neither is a finding): under one model, the same snow should cost every reader the same effort; the journalist expects attention to follow what the news changes for each reader, whatever its surprisal."
- **Source:** Gibson et al. 2019, p. 11 (the page the post cites just before): "language processing effort is associated with predictability".
- **What it says:** Gibson states an association, and the post's sentence before this one keeps it ("associated with"). The new prediction, "should cost every reader the same effort", treats effort as set by surprisal alone. It is labelled ours and not a finding, so this is not a misattribution. But it strengthens the link that the psycholinguist's question rests on.
- **Fix:** Write "under one model, if effort tracks surprisal, the same snow should cost every reader about the same effort".

### V3C-05 · minor · #answer 4(a), new parenthesis "(Cover and Thomas write 'uniquely decodable')"
- **Post:** "'Uniquely decipherable' is theirs too (Cover and Thomas write 'uniquely decodable'); it means a run of answers can be cut into words in only one way … <Cover & Thomas 1991, pp. 80–81>".
- **Source:** Cover & Thomas 1991, p. 80 (pdf 102): "A code is called uniquely decodable if its extension is non-singular." p. 81: the definition of a prefix (instantaneous) code. Gibson p. 4: "…the shortest uniquely decipherable code…" (brief unit 5). Both are verbatim and on the printed pages.
- **What it says:** The quote and the cite are correct. But Cover pp. 80–81 is **not in `source-brief.verified.md`**: no unit lists p. 80 or p. 81 of Cover, and the brief has "uniquely decodable" only as a paraphrase of p. 92. The cite itself was already on the page before this round; the new quote rests on it.
- **Fix:** Add Cover pp. 80–81 (pdf 102–103) to brief unit 24, condition 3, with the definition quoted above. The post text needs no change.

### V3C-06 · minor · #entropy, "on the equal-shares day of section 2's check it cost 2.25" (page and audio, unchanged sentence; the target changed)
- **Post:** The cross-reference is unchanged. Its target changed: section 2's "Three checks" paragraph is now "**A check.**", which is only about the "Matcha?" opening and no longer mentions the equal day. The 2.25 appears only in "Check yourself", answer (b).
- **Source:** Our own text (#cafe).
- **What it says:** A reader who looks for "section 2's check" now finds the paragraph headed "A check.", which does not have the number.
- **Fix:** Write "on the equal-shares day of section 2's Check yourself (b) it cost 2.25" (and the same in the audio).

---

## Checked and found correct

**New or changed citations (all verbatim checks are at most 25 words, on the printed page, and in the brief unless noted):**
- MacKay p. 99 (pdf 111), Algorithm 5.4: "These two symbols will be given the longest codewords, which will have equal length, and differ only in the last digit." This supports "Those two tickets have equal length and differ only in the last answer". It is brief unit 24. "The card's last question separates exactly those two" is labelled our reading.
- Cover p. 97 (pdf 119), §5.8: "inverting all the bits or exchanging two codewords of the same length will give another optimal code". This supports "inverting every answer, or swapping two tickets of the same length, gives another". It is brief unit 24, condition 4. The page narrowing from pp. 96–97 to p. 97 is correct.
- Cover p. 94 (pdf 116), §5.7 item 1: "Assuming we know the probability distribution on the objects". This supports "known". It is brief unit 24, condition 1.
- MacKay pp. 100–101 (pdf 112–113): "one unchanging ensemble"; Huffman codes "do not handle changing ensemble probabilities with any elegance"; "They are optimal symbol codes". This supports "do not change" and "one word at a time". It is brief unit 24, conditions 1–2.
- Pierce pp. 35–36 (pdf 51–52): Nyquist's 1924 paper (p. 35); "W = K log m" and "K is a constant whose value depends on how many successive current values are sent each second" (p. 36). It is brief unit 1 [S2].
- Pierce p. 40 (pdf 56): "only if successive symbols are chosen independently and if any of the s symbols is equally likely to be selected". The hook now keeps both conditions, and the quoted fragment "is equally likely to be selected" is verbatim. It is brief unit 2.
- Gibson p. 4: "uniquely decipherable" is verbatim (brief unit 5). Removing the step-2 Gibson sentence leaves no dangling reference: "Step 6 returns to this" still points to whole questions against fractional worths.
- Removed cites (Pierce p. 24 in the term box, MacKay p. 68 additivity, MacKay p. 72 "convincing case", Cover p. 86 in E5, Cover p. 94 in boundary 6, the Mills p. 5 gloss moved to the fold-out): nothing that remains depends on them. E9 still carries Cover p. 86.

**New numbers (recomputed in Python and with `check.mjs`):**
- Step 6 table:
  - village with the button: 1, 2, 3, 3, average 1.750, H 1.750;
  - first two joined each time: 3, 3, 2, 1, average 2.625 (joins [[0,1],[0,1],[0,1]] in `check.mjs`: 2.625);
  - 0.7 day: average 1.500, H 1.35678 → 1.357 (for its word order, see V3C-01);
  - equal day: 2, 2, 2, 2, average 2.000, H 2.000.
- Gaps: rain 1 − log2(1/0.7) = 0.4854 → 0.485; the day's gap 1.5 − 1.35678 = 0.1432 → 0.143. The widget gives gap 0.14322.
- Recall card 4: the Huffman lengths for 0.3, 0.3, 0.2, 0.2 are 2, 2, 2, 2 and EQ* = 2.000. A brute-force search over all lengths that satisfy the Kraft inequality confirms 2.000 is the minimum (1, 2, 3, 3 gives 2.1). H = 1.97095 → 1.971. It is labelled "ours, run in code".
- The submarine misses 0.0227, 0.0231, 0.0235, 0.0238, 0.0242 and the total log2(64/59) = 0.1174 are unchanged and correct.

**Hedges and labels:**
- "(our reading)" was added at the hook ("The count itself gives every possible message the same weight"), in #roles, and on both new Huffman "why" answers; "(ours)" was added on Move 1's third extreme and on Move 3's predictions.
- "What was missing…" lost its own "(our reading)", but it sits in the paragraph headed "The pain (ours)", and it agrees with brief unit 2, trap (c).
- No source is strengthened. Huffman optimality is still attributed to Cover p. 101, and the proof is still not reproduced.

**Mills:**
- Dropping "and he hedges it" keeps the hedge, because the quote still contains "I believe" (p. 212).
- Move 1's "two extremes" is now labelled our reading. The Mills quotes (pp. 213, 215) are unchanged.
- The new audio recap, "In our reading of Mills, an issue is not a trouble multiplied: unlike even widespread trouble, it cannot very well be defined within everyday surroundings", matches the page's Move 2. Mills pp. 8–9: "unlike even widespread trouble, that it cannot very well be defined in terms of the immediate and everyday environments".
- No Mills overreach.

**Audio against the page:** every change in the page diff has its audio twin.
- Hook: the reorder, both Pierce conditions, and "independent," in the recap.
- Café: the three checks become one; "Who does what" is trimmed.
- Village: independence is defined at first use; the rats line is cut; Pierce "aggravated" is cut.
- Surprisal: the fraction sentence is added; the MacKay additivity and Gibson sentences are cut.
- Entropy: "Let E Q stand for…" is added; Cover p. 86 is cut; "no channel" is cut (V3-05).
- Submarine: the asides are cut.
- Roles: "That is our reading." is added.
- Step 6: the table, the gaps, the two "why" answers, and "Where it holds".
- Answer 4(a): "uniquely decodable".
- Boundary 6: the Cover sentence is cut.
- Imagination: Move 1, Move 3, the fold-out mention, and the recap.
- Turn: the Python 3.9 aside is cut.
- Recall 4.

No claim appears only in the audio. Audio boundary 6 keeps "as the day goes on" where the page now says "during the day"; that is the same claim.

**Layer 2 (`#cafe`):** a scan of the page section, with widget JSON stripped, and of the audio `cafe` chapter found:
- no TeX, `=`, `+`, `^` or Σ;
- no word of two or more capitals;
- none of H, EQ, bit, log, entropy, surprisal, independent, code, encode, decode, probability or Huffman;
- only one numeral, the "2 questions" in the diagram labels, and that was already there.

"Script" and "string" are still defined in the same sentence that introduces them.

**Checks:**
- `node site/ai4read/components/check.mjs posts/2026-12-surprise/src/content.html`: 9/9 widget configs OK.
- `card-lab` with `auto`, the first-two joins, and presets 1 and 2 reproduces the table (except the word order in V3C-01).
- `node site/ai4read/components/test.mjs posts/2026-12-surprise/index.html --inline`: PASS. There are 0 console errors, no overflow at 390 px, the readouts are reproducible, and the card-lab tap, join and rule all work.
- `index.html` carries the new text.
