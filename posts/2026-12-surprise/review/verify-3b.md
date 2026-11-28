---
post: 2026-12-surprise
stage: S5 round 3, independent fact check (Sonnet)
checked: src/content.html, audio-script.md, post.json, notebook/01_surprise_entropy.ipynb, notebook/results.md
against: sources/ (text layers; Pierce p.38 and Gibson p.1 also read on the rendered page), source-brief.verified.md units 1-24
not read: self-review.md, numbers.md, review/verify-3.md
date: 2026-11-28
---

# Verify 3b

**Counts: critical 0, major 0, minor 8.**

**Layer 2 (the café section): no formula, symbol, abbreviation or unexplained term found.** "Script", "string", "ticket's length" and "order's worth" are all defined where they first appear.

**Round-2 majors: all six resolved** (page and audio). Details are in the next section.

## Round-2 majors: resolved?

| ID | Page | Audio | Verdict |
|---|---|---|---|
| V2-01 (lens 4 turned "most informative" into a search rule) | Lens 4: "For one experiment, MacKay's tentative conclusion ("we might conclude") is that it is most informative when its outcomes are equally likely (p. 70). A whole search differs: splitting every group as evenly as possible is not always the fastest script (MacKay p. 100; Cover & Thomas p. 97), and step 6's rule is." Step 6 gives the trap: Example 5.18, 2.53 against 1.97. | `lenses` and `nothalves` both contain the quoted lines. | **Resolved.** MacKay p.100 (pdf 112) and C&T p.97 (pdf 119) say this. I recomputed 1.97 by Huffman in Python. |
| V2-02 ("uniquely decipherable" glossed as the prefix property) | "means a run of answers can be cut into words in only one way; scripts in which no string is the start of another, like our card, are one kind of these (C&T pp. 80-81)". | `answer` has the same two sentences. | **Resolved.** C&T p.80 defines uniquely decodable; p.81 defines prefix codes. See V3B-05 for a small terminology point. |
| V2-03 (Mills: dropped hedge, example sentence made general) | "'unlike even widespread trouble', 'cannot very well be defined' within everyday surroundings; in his unemployment example, 'The very structure of opportunities has collapsed' (pp. 8-9)". | `imagination` has both sentences as quoted in the response. | **Resolved.** Mills pp.8-9 (pdf 15-16), read on the page text; the collapse sentence belongs to the unemployment example. Brief unit 18 is corrected. |
| V2B-01 ("ours, not from our sources" for the rule) | "The rule is Huffman's ... Cover and Thomas give this simple algorithm (pp. 92-93), prove that it gives the shortest average length among scripts in which no string is the start of another ... 'Huffman coding is optimal' (p. 101) ... Only the worked 0.7 day is ours." | `nothalves` has "The rule is Huffman's ..." and "Only the worked zero point seven day is ours". Recall card 8 and the notebook also credit Huffman. | **Resolved.** C&T p.92 (pdf 114), p.93, p.94, p.101 (pdf 123); MacKay Algorithm 5.4 on p.99 (pdf 111). All conditions of unit 24 are on the page. |
| V2B-02 (same gloss as V2-02) | as V2-02 | as V2-02 | **Resolved.** |
| V2B-03 (audio recap "only when ... whoever owns the model") | Move 2 keeps "that it does so is a hypothesis, not a finding". | `imagination` recap: "Our hypothesis, not a finding: ... part of the cause may lie in whose model prices them." | **Resolved.** "Only when" is gone. See V3B-02 for one residual sentence in the same recap. |

The quoted audio lines from `response-2.md` exist in `audio-script.md`. I checked every one that the response quotes for V2-01 to V2-14, V2B-03 to V2B-13 and C2-01 to C2-18.

## What I re-ran

**Widgets.** I ran `check.mjs` on all 9 widgets, with the card lab on the presets and on explicit joins, and on every preset of the other labs.
- Card lab, village day: auto-join gives lengths 1, 2, 3, 3, average 1.750 = H. Always joining the first two groups gives 2.625.
- Card lab, 0.7 day: average 1.500, H 1.3568, gap 0.1432. Rain's worth is 0.5146. One of the 0.1 words gets 2, so the tie remark is right.
- Card lab, equal day: 2.000.
- Village lab: 2.000 (equal), 0.000 (only rain), H 1.750 and script 2.625 (reversed), script 2.250 (equal shares).
- Weigh lab: 0.817, 1.252, 1.500, 1.585, 1.483, 1.000. "3.000 remain" for 4 v 4.
- Submarine lab: shots 1, 2, 6, 33, 49, 64 all total 6. The captions match, and the fifth miss reads 0.0242.
- Forecast lab: 3.00, 1.00, gap 2.00.
- Surprisal plot: 10.0, 3.3, 1.0, 0.0.

**Python.**
- H(village) = 1.75.
- 0.7 village: H 1.3568, EQ* 1.5, H+1 = 2.357.
- Transfer challenge: (a) 1, 2, 3, 4, 4; (b) 1.875 = H; (c) 2.5 old, 2.25 best = H.
- Fifth miss 0.02425; log2(64/59) = 0.1174.
- log2 3 = 1.585, which is 58.5 per cent. log2 8 = 3.
- MacKay Example 5.18 by Huffman gives 1.97.
- 0.3 gives 1.74; log2 24 = 4.585.
- The caption values for 1 v 1 to 6 v 6 are correct.

**Notebook.** I re-ran it with nbclient in a copy, using the scratchpad `nbenv`. There were 0 errors and every output is identical to `results.md`:
- 1.7499 and 2.2470 in exercise 3;
- the submarine table;
- the estimation table (1.5036, 1.6753, 1.7253, 1.7469);
- 1,050 vectors, gap 0.0033 to 0.8361;
- the stall (2.5, 2.25);
- the weighing.

The page's estimation table matches the rounded values.

**Quotes.** I matched all 114 quoted strings by script against the text layers, then read the unmatched ones by hand (line breaks, ligatures and hyphenation only). Every quote is verbatim at the cited printed page. That includes:
- Mills pp. 5, 8-9, 73, 212-215 (offset +7);
- Pierce pp. 24, 38, 40, 80, 81;
- MacKay pp. 26, 32, 33, 67, 68, 70-74, 99, 100;
- Shannon pp. 1, 2, 10-12, 14, 18;
- Shannon 1951 pp. 54-55;
- Gibson pp. 1, 3, 4, 6, 7, 11, 14, 15;
- C&T pp. 5, 13, 15, 80-81, 86, 92-97, 101.

**Other checks.**
- The "never", "none", "only", "always" and "cannot" sentences on the page were all checked. Each is either true by the arithmetic or supported by the cited page.
- `post.json` is consistent with the page (title, number 4, date 2026-12-07, series, tags, cites).

## Findings

### V3B-01 · Audio adds a sentence that the page does not have (`entropy`, audio)
- **Quote:** "Try only rain: the entropy is zero, and Shannon writes that no channel is required." The page says only: "'Only rain': H = 0.000 (Shannon 1948, p. 18)".
- **Source and page:** Shannon 1948, p. 18: "If a source can produce only one particular message its entropy is zero, and no channel is required."
- **What the source says:** The audio's claim is supported. The page does not make it.
- **Severity:** minor (the audio must say what the page says, nothing added; WRITING §8b).
- **Fix:** Delete "and Shannon writes that no channel is required" from the audio, or add the Shannon p.18 sentence to the page.

### V3B-02 · Audio recap states Mills's distinction in words that are not on the page (`imagination`, recap)
- **Quote:** "In Mills' terms, trouble and issue differ by where the cause lies."
- **Page:** Move 2 quotes the distinction and says an issue "is not a trouble multiplied (our reading)", but it never says it is about "where the cause lies".
- **Source and page:** Mills 1959, p. 8: troubles are matters where "the statement and the resolution ... properly lie within the individual"; issues "transcend" local environments. On p. 9 the war example speaks of "causes". The brief (unit 18, trap b) paraphrases this as "causes and solutions lie in institutions".
- **What the source says:** Mills places the statement and the resolution of a trouble within the individual's milieu. "Cause" is the brief's and the recap's paraphrase.
- **Severity:** minor (a loose attributed paraphrase that appears only in the audio).
- **Fix:** Reword the recap to "In Mills' terms, a trouble lies within a person's own milieu, and an issue lies in the institutions of the society", or put one such sentence on the page and keep the audio.

### V3B-03 · Our reading of MacKay is not labelled (`roles`, page and audio)
- **Quote:** "The strategy is the shared script; the one who knows the secret, applying it, makes the string."
- **Source and page:** MacKay 2003, p. 70: "Our questioning strategy defines a way of encoding the random variable x as a binary file".
- **What the source says:** MacKay does not say who encodes. The post's sentence is our resolution of an apparent ambiguity.
- **Severity:** minor (our own reasoning without an "ours" label; WRITING §9).
- **Fix:** Add "(our reading)" after the sentence, on the page and in the audio.

### V3B-04 · Page for Nyquist's date (fold-out `box-nyquist`)
- **Quote:** "Nyquist's result of 1924 relates the speed W of a telegraph line ... by W = K log m ... (Pierce 1961, p. 36)".
- **Source and page:** Pierce p. 35 (pdf 51): "In 1924, he published his results in an important paper". The formula is on p. 36.
- **What the source says:** The date is on p. 35, the formula on p. 36.
- **Severity:** minor.
- **Fix:** Cite "pp. 35-36".

### V3B-05 · "Uniquely decipherable" is cited to a book that says "decodable" (`answer`, 4(a))
- **Quote:** "'Uniquely decipherable' means a run of answers can be cut into words in only one way ... (Cover & Thomas 1991, pp. 80-81)".
- **Source and page:** C&T pp. 80-81 define "uniquely decodable" and "prefix code". "Decipherable" appears only in Gibson et al. p. 4. MacKay does not use it either.
- **What the source says:** The definition is the same idea, but the term in the cited pages is "decodable".
- **Severity:** minor.
- **Fix:** Add "(Cover and Thomas write 'uniquely decodable')". The audio needs no change, or the same short clause.

### V3B-06 · "Not unique" gloss is a variant of the source's (`nothalves`, Where it holds)
- **Quote:** "the best card is not unique, since swapping yes and no on a question gives another (Cover & Thomas 1991, pp. 96-97)".
- **Source and page:** C&T p. 97 (pdf 119): "there are many optimal codes: inverting all the bits or exchanging two codewords of the same length will give another optimal code." p. 96: Example 5.7.3, lengths (2,2,2,2) or (1,2,3,3).
- **What the source says:** The source swaps every bit (all questions at once) or two equal-length codewords. Swapping one question's answers is true (the lengths do not change), but it is our extension.
- **Severity:** minor.
- **Fix:** Write "swapping yes and no on every question, or two tickets of the same length, gives another (p. 97)". The audio has the same sentence.

### V3B-07 · "Known and fixed" is cited to a page that has only "known" (`nothalves`, Where it holds)
- **Quote:** "It needs shares that are known and fixed (Cover & Thomas 1991, p. 94), and one word at a time (MacKay 2003, pp. 100-101)".
- **Source and page:** C&T p. 94: "Assuming we know the probability distribution on the objects". "One unchanging ensemble" is MacKay p. 100; "fixed" appears on p. 101.
- **What the source says:** C&T p. 94 supports "known". "Fixed" belongs to MacKay pp. 100-101.
- **Severity:** minor.
- **Fix:** Cite "known" to C&T p. 94 and "fixed, one word at a time" to MacKay pp. 100-101. The brief's unit 24 condition 1 already splits them that way.

### V3B-08 · Hook generalises from Hartley to "engineers" (`hook`, page and audio)
- **Quote:** "Counting was how engineers measured messages in the 1920s."
- **Source and page:** Pierce pp. 35-40 (Nyquist 1924 and 1928; Hartley 1928); Shannon p. 1 ("Hartley ... the logarithmic function").
- **What the source says:** The sources describe the measures of Nyquist and Hartley. They do not say this was how engineers in general measured messages, and both used a logarithm of a count.
- **Severity:** minor (a scope word; "the pain (ours)" covers only the previous paragraph).
- **Fix:** Write "In 1928 Hartley measured ..." directly, or "In the 1920s Nyquist and Hartley measured ...", and drop the general sentence.

## Checked and found correct (no finding)

- **Citations and quotes:** every citation and verbatim quote listed under "Quotes" above; the Hartley and Nyquist passages, including the 7-versus-8 values remark (read on the Pierce p. 38 page image); the Gibson "ARTICLE IN PRESS" proof and page 1 abstract (read on the image); the edition notes in Sources (Mills 2000 printing with Gitlin afterword; MacKay v7.2, 28 March 2005; C&T 1991; Pierce 1961 Harper first edition).
- **Hedges and scope:** the Huffman paragraph and its conditions (unit 24); the lens-4 and step-6 even-split trap; the Gibson hedges; MacKay's "we might conclude"; the Mills hedges and "hypothetical, not data".
- **Ergodic gloss:** it is labelled ours.
- **Notebook text:** Huffman credited in exercise 7; hints; "Python 3.9 or later should work; we did not test it"; the README; results.md frames.
- **"Ours" labels:** the 0.7 village, the café tie-in claims, the research questions.
- **Audio against page, chapter by chapter:** hook, cafe, village, surprisal, entropy, submarine, roles, nothalves, answer, lenses, fails, imagination, turn and recall. Apart from V3B-01, V3B-02, V3B-03 and V3B-06 (audio repeats the page's sentence), nothing is added, dropped or strengthened.
