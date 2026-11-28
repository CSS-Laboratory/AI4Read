---
id: 2026-12-surprise/review/s2-check
stage: S2 (source-brief check)
checker: independent fact-checker (fresh agent; did not write the brief)
date: 2026-11-28
input: source-brief.md (15 units) → output: source-brief.verified.md
method: every quote re-matched by script against the pdftotext page (ligatures, quotes and hyphenation normalised), with every failed match read by hand. Printed page numbers were read from each page's header or footer. Page images were rendered for every doubtful page: Cover pp. 13, 49, 95; MacKay p. 71; Pierce pp. 22, 24, 35, 38, 81, 264, 267 and the front matter; Shannon 1951 p. 55. Every number was recomputed in Python. Network not used.
---

# S2 check: "How much is a surprise worth?"

## Summary
- **Units:** 15 checked, 0 unchecked. **3 VERIFIED** (4, 6, 8), **12 CORRECTED** (1, 2, 3, 5, 7, 9, 10, 11, 12, 13, 14, 15), **0 DROPPED**.
- **Findings:** **0 critical, 4 major, 24 minor.**
  - Major: G1 (the Cover edition), G2 (the Pierce edition), U1 (Nyquist's eight values, "four times"), U14 (the 1951 encoder and decoder roles).
- **UNSEEN items:** 3 resolved (MacKay Exercise 4.1 and 4.9 solutions; eq. 4.11 vs Fig. 4.3; Pierce p. 22). 3 stay UNSEEN (Weaver's essay; Hartley and Nyquist in their own words; the reading-time papers). New UNSEEN: whether the 2006 Cover and the Dover 1980 Pierce match our pages.
- **The planner's reported source errors:** all three confirmed.
  - Cover p. 49 "1930s": on the page image, and Cover's own bibliography says 1928.
  - MacKay eq. 4.11 "0.0430": on the page image; it is the truncated 31st term.
  - The `wiki/instances/twenty-questions.md` misstatement: confirmed, with a nuance.
  - One new source slip: Pierce p. 38, "four times" for eight current values (it should be 3).

## Global findings (apply to several units)

**G1. MAJOR (citation, wrong edition).** The brief cites "Cover & Thomas 2006". Every Cover page in the brief is from the 1991 first edition.
- Evidence: pdf 1, "Copyright 1991 John Wiley & Sons, Inc. Print ISBN 0-471-06259-6"; pdf 4, "Copyright 1991 by John Wiley & Sons, Inc."
- Why it matters: the 2006 pagination differs, so a 2006 citation with these pages points readers to the wrong pages. This affects units 2, 4, 5, 6, 8, 12 and 13, and trap 5.
- Fix: cite Cover & Thomas (1991) with these pages, or re-check every page against a 2006 copy.

**G2. MAJOR (citation, wrong edition).** The brief cites "Pierce 1980 (Dover)". The file is the 1961 Harper & Brothers first edition.
- Evidence: the title page (pdf 5) reads "Symbols, Signals and Noise: The Nature and Process of Communication"; the copyright page reads "COPYRIGHT 1961 BY JOHN R. PIERCE … HARPER & BROTHERS … FIRST EDITION". The file is a public-library scan.
- Affects units 1, 2, 3, 8, 11, 12 and 13.
- Fix: cite Pierce (1961), Harper, with these pages. Whether the Dover 1980 pagination matches is UNSEEN. (Kunhao may also want to confirm that this scan meets the Charter §9 source policy.)

**G3. Minor.** Shannon 1948 pages are those of the Bell Labs reprint, not the BSTJ issue.
- Evidence: pdf 1 header, "Reprinted with corrections from The Bell System Technical Journal, Vol. 27, pp. 379–423, 623–656".
- Fix: say "reprint pagination" in Sources.

**G4. Minor.** Gibson et al. pages are those of the pre-proof, pp. 1–19.
- Evidence: the page header reads "TICS 1894 No. of Pages 19"; the footer reads "Trends in Cognitive Sciences, Month Year, Vol. xx, No. yy".
- Fix: cite the pages as pre-proof pages, or re-check them against the published version (its pagination is UNSEEN).

**G5. Minor (trap 1).** Gibson uses both names, not only "surprisal".
- Evidence: Box 2, p. 4: "the information content of a discrete event x is given by its log inverse probability, or surprisal".
- Fix: done in the verified brief (trap 1).

Checked and correct at the top of the brief:
- trap 1: our search of the whole Shannon 1948 text finds neither "surprisal" nor "information content";
- trap 2: Cover p. 15, "lies between H(X) and H(X) + 1";
- trap 3: Shannon p. 18;
- trap 4: Shannon p. 1 and Pierce p. 40;
- the offsets, except that the Cover bibliography drifts (pdf 541 = p. 517).

## Per-unit entries

**U1. Nyquist. CORRECTED.**
- **Major.** The brief says "eight values should give four times the speed". By the unit's own `W = K log m`, log2 8 / log2 2 = 3, so the speed is 3 times; the brief's own toy ("each doubling adds one") also gives 3.
  - Source: Pierce p. 38 (pdf 54; page image): "the use of eight current values (0, 1, 2, 3, 4, 6, 7, …) should enable us to send four times as fast". This is a slip in the source; its list also shows seven values.
  - Fix: never write "four times"; give 3 and label the computation ours.
- **Minor.** The brief dates the relation to "1924 and 1928". Pierce p. 35 introduces the 1924 paper ("In 1924, he published his results … 'Certain Factors Affecting Telegraph Speed.'") and gives `W = K log m` from it (p. 36). The 1928 paper (p. 39) is about redundant high frequencies.
  - Fix: attribute the relation to the 1924 paper.
- Verified: the quote (p. 38); the three-value "60 per cent" (log2 3 = 1.585); the table on p. 37; the quadruplex (p. 38); Shannon p. 1, notes 1–2.

**U2. Hartley. CORRECTED.**
- **Minor.** "MacKay p. 74 for the modern name": MacKay defines the raw bit content (p. 74), but a search of the whole MacKay text finds no "Hartley", so the pairing is ours. Fix: label it ours.
- The tension is strengthened. Cover's bibliography p. 517 (pdf 541), ref. [133], reads "Bell Sys. Tech. Journal, 7: 535, 1928". The p. 49 page image reads "In the 1930s, Hartley introduced a logarithmic measure of information for communication." So the planner's reported error is confirmed as an error in the book itself.
- Verified: the Pierce p. 40 quote with both conditions; Pierce p. 39 (1928; "regarded the sender … as equipped with a set of symbols"); the Shannon p. 1 quote; the MacKay p. 74 quotes.

**U3. Why a logarithm. CORRECTED.**
- **Minor (dropped hedges).** Three hedges were missing:
  - Shannon p. 1: "tend to vary linearly with the logarithm of the number of possibilities";
  - Shannon p. 1: "One feels, for example, that two punched cards should have twice the capacity of one";
  - Pierce p. 80: "It also seems reasonable that we should be able to send 4 times as much information … If this is so".
  - Fix: restored in the verified brief.
- Verified: all three quotes; Tukey; "N such devices can store N bits"; log2 M = 3.32 log10 M (1/log10 2 = 3.3219); MacKay eqs. 4.4–4.6 (p. 68); "bit" with two meanings (p. 32); Theorem 2 and its disclaimer (p. 11).

**U4. Equal chances. VERIFIED.**
- MacKay p. 70: "Intuitively, the best questions successively divide the 64 possibilities into equal sized sets. Six questions suffice."
- Also verified: the six questions; 35 → 100011; the 1-bit answers rest on "If we assume that all values of x are equally likely" (kept in the claim).
- Cover Example 1.1.1 (p. 5), H = log 32 = 5; the horse-race code (p. 6), average 2 bits.
- MacKay p. 74: "always guaranteed".
- Rats: 2^4 = 16 < 32, labelled ours.

**U5. Weighing. CORRECTED.**
- **Minor (dropped hedge).** The brief's "Conclusion: …" drops MacKay's "Thus we might conclude" (p. 70). Fix: restored.
- UNSEEN resolved:
  - Exercise 4.1 is marked "[2, p.69]", so its printed solution is Fig. 4.2 (p. 69), "An optimal solution to the weighing problem".
  - Exercise 4.9 is marked "[1 ]", so no solution is printed. Preface p. xi: "Where a solution is provided, this is indicated by including its page number alongside the difficulty rating."
- Recomputed: 4 v 4 gives 1.585 bits; 6 v 6 gives 1.000; log2 24 = 4.585; 27 > 24 > 9.
- Our 6 v 6 answer (0 bits about which ball, 1 bit about ball and direction) was checked by listing the hypotheses.
- Verified: the quotes on p. 68 and p. 70; the 8:8:8 and 3:3:2 splits; Exercise 4.9's wording (p. 84); Cover p. 15, "An efficient first question".

**U6. Question tree. VERIFIED.**
- Cover p. 15: "The resulting expected number of binary questions required is 1.75."
- Eq. 5.61 on the page image (p. 95): "H(X) ≤ EQ < H(X) + 1".
- Shannon p. 18: the A–D source, H = 7/4, code 0, 10, 110, 111, relative entropy 7/8. Cover p. 94: the §5.7 quote.
- Huffman for 0.7/0.1/0.1/0.1 gives lengths {1, 2, 3, 3}, average 1.5, H = 1.357.
- The wiki claim is confirmed.
  - Cover names twenty questions on p. 6, p. 94, p. 95, p. 118 (Problem 7) and p. 120 (Problem 13); the index lists "twenty questions, 6, 94, 95".
  - Nuance: the wiki line comes from the digest `ch05-data-p2`, scoped "(pp. 118–120)". It is true for those pages and misleading on the instance page.
  - Fix: correct the wiki instance page and the digest line (WRITING §9). This was not done here; the fact-checker does not edit other files.

**U7. Surprisal definition. CORRECTED.**
- **Minor (dropped hedge).** The quote cut Shannon's "approximately".
  - Shannon p. 13: "H is thus approximately the logarithm of the reciprocal probability of a typical long sequence divided by the number of symbols in the sequence".
  - Fix: quote it from "H is thus approximately".
- **Minor (wrong explanation).** The brief says "Table 2.9 values come from rounded probabilities". It is the other way round. MacKay Table 2.9 (p. 32) prints z ".0007 10.4", but log2(1/.0007) = 10.48, which rounds to 10.5. The h column was therefore computed from unrounded probabilities; the other 26 rows match the printed p.
  - Fix: explained in the verified brief, with a widget warning.
- Verified: the Gibson glossary on p. 3, "Surprisal: the negative log probability of a discrete event." (two columns, matched across the layout); Gibson p. 4, eq. I; MacKay Fig. 4.1 (10.0/0.011, 6.6/0.081, 3.3/0.47, 2.3/0.72, 1.0/1.0); H from Table 2.9 = 4.109; Shannon 1951 p. 54, F1 = 4.14 / 4.03.

**U8. Entropy. VERIFIED.**
- MacKay p. 32: "Another name for the entropy of X is the uncertainty of X."
- Verified quotes: MacKay p. 32; Cover p. 13; Shannon p. 10 and p. 11 (both disclaimers).
- Recomputed: H(1/2,1/3,1/6) = 1.459 = 1 + ½ × 0.918; the MacKay eq. 2.41 example, 1.5; Pierce p. 83, .811.
- Pages: MacKay p. 33, properties; Shannon p. 14, "relative entropy" = H/Hmax; Pierce p. 81, "must decrease entropy".
- Note, not a finding: Shannon's property 4 (p. 12) excepts permutations ("except in the special case where this transformation amounts to no more than a permutation").

**U9. Submarine. CORRECTED.**
- **Minor (number frame).** The brief says Fig. 4.3 values "agree to rounding". MacKay truncates. Recomputed: 0.02272, 0.02308, 0.04439 and 0.08746 are printed as 0.0227, 0.0230, 0.0443 and 0.0874; rounding would give 0.0231, 0.0444 and 0.0875.
  - Fix: quote MacKay's printed values, and say so if a widget rounds.
- **Minor (hedge).** MacKay's verdict begins "I think the submarine example makes quite a convincing case" (p. 72). Fix: keep "I think".
- UNSEEN resolved. The page image of p. 71 shows eq. 4.11 ending "+ 0.0430 = 1.0 bits"; log2(34/33) = 0.04307 is the 31st term, and the 32nd is log2(33/32) = 0.04439. It is a misprint in this printing.
- Verified: eqs. 4.8–4.14; the p. 71 quote; the caption "hit on the 49th attempt"; the sums 1.000, 2.000 and 6.000.

**U10. Wenglish. CORRECTED.**
- MacKay verified: pp. 72–73; 2^15 = 32,768; 4.00 and 9.97 bits; 15 bits per word (p. 73); 2048 and 32 words; 26^5 = 11,881,376; the quote on p. 73.
- **Minor (gloss as fact).** The brief calls uniform information density "an empirical claim about speakers". Gibson p. 3 (glossary): "the hypothesis that the information content of an utterance per unit time should be roughly constant".
  - Fix: use Gibson's words.
- **Minor (scope).** Gibson p. 8: "Based on co-occurrence statistics for a small set of subjects, verbs, and objects". Fix: restored the "small set" scope.

**U11. Meaning set aside. CORRECTED.**
- **Minor (misquote).** The brief prints "constrast [sic]". The page image of p. 267 reads "We can be surprised repeatedly only by contrast with that which is familiar, not by chaos." It was an OCR error. Fix: "contrast", no [sic].
- **Minor (not verbatim).** The brief quotes Gibson p. 15 as "are currently unclear". The source reads "It is currently unclear whether such factors can be expressed as part of general communicative efficiency". Fix: use the exact sentence.
- **Minor (scope).** Pierce p. 24's confusion concerns communication theory and physics: "This is still a confused and confusing matter. The confusion is sometimes aggravated when more than one meaning of information creeps into a discussion." Fix: say "aggravated", and keep the context.
- Verified: Shannon p. 1 (both quotes, plus "since this is unknown at the time of design"); Gibson p. 4; Pierce p. 264 (page image, "A completely random visual pattern … is mathematically the most surprising"). Weaver: UNSEEN; see the end.

**U12. Known distribution. CORRECTED.**
- **Minor (voice).** "you cannot do inference without making assumptions" is introduced as the view of Bayesian advocates. MacKay p. 26: "Advocates of a Bayesian approach … do not view this subjectivity as a defect, since in their view,". He then warns "this is not yet a globally held view".
  - Fix: attribute it as MacKay's statement of the Bayesian view.
- **Minor (balance).** The brief left out MacKay's counterweight, p. 26: "if two people make the same assumptions and receive the same data then they will draw identical conclusions". Fix: added beside our "different people, different surprisal" inference.
- **Minor (omitted continuation and scope).** Shannon p. 18 goes on: "we can choose to ignore some or all of the statistical knowledge we have of the source". Pierce's ergodic sentence (p. 81, page image) is stated for his simplest two-symbol case. Fix: both added.
- Verified: Shannon p. 10 and p. 18; MacKay p. 26 ("some books…"); Gibson p. 14 (verbatim, hyphenated "information-theoretic").

**U13. Physics. CORRECTED.**
- **Minor (balance).** Pierce p. 24: "Nonetheless, both the entropy of statistical mechanics and that of communication theory can be described in terms of uncertainty, in similar mathematical terms." The brief gave only the "quite different" side, which is on p. 23, not p. 24. Fix: added, with the page corrected.
- **Minor (wording).** The brief wrote "gives the reason for confusion"; Pierce says the confusion "is sometimes aggravated" (p. 24). Fix: reworded.
- UNSEEN resolved. Pierce p. 22 on the page image reads: "an increase in entropy means a decrease in order", followed by "when we ask what order means, we must in some way equate it with knowledge."
- Verified: Shannon p. 11 and note 8; Pierce p. 80, "clear our minds"; p. 24, "more interesting than fruitful" (clean on the image); Cover p. 49, "S = k ln W inscribed as the epitaph on his gravestone"; Cover p. 49: "attempts have been made to compare these theorems with the fundamental laws of physics".

**U14. Encode and decode. CORRECTED.**
- **Major (wrong description of the experiment, on the learner's recorded confusion).** The brief says "the person who has the text guesses letters and writes the reduced text", and "the guesser who holds the text encodes". In fact:
  - Shannon 1951 p. 54: "Select a short passage unfamiliar to the person who is to do the predicting."
  - p. 55: "the subject knows the text up to the current point".
  - The reduced text is the second line of the record. Fig. 2 (p. 55, page image) shows "ORIGINAL TEXT → COMPARISON [PREDICTOR] → REDUCED TEXT → COMPARISON [PREDICTOR] → ORIGINAL TEXT".
  - So the encoder is the original compared with a predictor, and the decoder is the reduced text with an identical predictor. A guesser who held the text would always be right.
  - Fix: rewritten in the verified brief, consistent with `learner/state.md` ("the first person encodes (writes guess numbers)").
- **Minor.** "102 letters" should be "102 symbols" (p. 56: "Out of 102 symbols the subject guessed right on the first guess 79 times"). 77% is our computation and is not printed.
- Verified: Shannon 1948 p. 2 (receiver quote; "In telegraphy we have an encoding operation"); the 1951 p. 55 quotes (twin; "encoded form"); 89/129 = 69% (printed); the hedge "something of the order of one bit per letter" (p. 50); MacKay p. 70; Gibson p. 3, Fig. 1.

**U15. Gibson. CORRECTED.**
- **Minor (missing context).** The brief says ref. [107] (Smith & Levy 2013) is "p. 18, title only". Gibson's text does cite [107] once, in the glossary: "Information locality: the hypothesis that all words with high mutual information should be close, for processing efficiency [107]" (p. 3). It is never cited for reading time.
  - Fix: noted, which strengthens trap (a).
- Verified:
  - p. 11: "Since language processing effort is associated with predictability [104,105]" (hedged context: "may ease language processing effort");
  - p. 6: "This pattern likely reflects lexicalization…", and Figure 2's "3-gram";
  - p. 7: both colour quotes ("yes–no" with an en dash);
  - p. 9: "[104–106]";
  - p. 14: the baseline quote;
  - p. 15: taboo words and populations;
  - the p. 1 abstract (matched across columns);
  - refs 104 (Hale 2001), 105 (Levy 2008), 106 (Levy 2011) and 107 on p. 18.

## Outcome of the UNSEEN items
1. Weaver's essay: **still UNSEEN.** It appears only as bibliography entries (Cover; MacKay). Keep it marked, or obtain the essay.
2. Hartley 1928 and Nyquist 1924/1928 in their own words: **still UNSEEN.** Report them only through Pierce and Shannon.
3. Smith & Levy 2013, Hale 2001, Levy 2008 (and Levy 2011): **still UNSEEN** (titles only).
4. MacKay Exercises 4.1 and 4.9: **resolved.** 4.1 → Fig. 4.2, p. 69; 4.9 → no printed solution.
5. (a) eq. 4.11 vs Fig. 4.3: **resolved** (a misprint in eq. 4.11). (b) Pierce p. 22: **resolved** (exact wording quoted).

## Follow-ups outside this stage (not done by the checker)
- Fix `wiki/instances/twenty-questions.md` and the digest line in `wiki/works/cover-2006-elements/ch05-data-p2.md` (WRITING §9).
- Re-label the source files and the canon entries for Cover (1991) and Pierce (1961), or obtain the editions that the names claim.
