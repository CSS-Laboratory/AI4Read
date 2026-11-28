---
post: 2026-12-surprise
stage: S5 round 1 (fact check of the draft)
checker: independent fact-checker (fresh agent; did not write the post; read self-review.md: no; numbers.md: only after the own pass, to locate provenance)
checked: src/content.html (all, incl. fold-outs, quizzes, recall, widget configs and readouts, Sources), audio-script.md, post.json, notebook/01_surprise_entropy.ipynb (re-executed), notebook/results.md
against: sources/*.pdf / *.txt (page text; offsets from the brief, confirmed by quote hits), source-brief.verified.md incl. Addendum S2b
date: 2026-11-28
---

# Verify 1: post 04 "How much is a surprise worth?"

**Counts: 0 critical · 2 major · 24 minor**

Release gate (rubric §A): not met while the 2 majors stand. With more than 5 minors, criterion 1 would score 3 even after the majors are fixed. Most minors are one-word fixes.

Layer 2 (§1a): no formula, symbol, abbreviation or unexplained term found in the café section (text, diagrams, check-yourself). No major finding there.

---

## Major

### V1-01 · Pierce's warning loses its hedge and its scope (term box, layer 1; audio "hook")
- **Post:** "Pierce warns that the everyday sense, knowledge, creeps in and confuses the discussion" (#hook, term box). Audio: same sentence.
- **Source:** Pierce 1961, p. 24 (pdf 40).
- **Source says:** "The confusion is sometimes aggravated when more than one meaning of information creeps into a discussion." The confusion is about how communication theory relates to physics ("This is still a confused and confusing matter").
- **Why it matters:** The post drops a hedge ("sometimes"), turns "aggravated" into "confuses", and drops the scope (the physics debate). The S2 check fixed this exact point as unit 11, change (c), and unit 13, trap.
- **Severity:** major (dropped hedge; WRITING §9).
- **Fix:** Write "Pierce warns that confusion about information and physics 'is sometimes aggravated' when the everyday sense, knowledge, creeps in", and make the same change in the audio.

### V1-02 · Gibson's "language processing effort ... predictability" becomes "reading effort follows surprisal" (#fails check, #recall card 8, Sources note, #imagination move 3; audio)
- **Post:**
  - Layer-4 check (iii): "'Reading effort follows surprisal.'" The answer calls it "An empirical claim by others, hedged as 'is associated with'".
  - Recall card 8: "Which claim about reading effort is empirical, and who makes it? That effort 'is associated with predictability': Gibson and colleagues, citing Hale (2001) and Levy (2008)".
  - Sources note: "the reading-time studies behind Gibson and colleagues' sentence on predictability".
  - Move 3: "A psycholinguist asks whether listeners track surprisal, an association claimed in the literature".
- **Source:** Gibson et al. 2019, p. 11 (with p. 9, p. 3 and the reference list on p. 18).
- **Source says:** "Since language processing effort is associated with predictability [104,105], an element that makes nouns more predictable in context would make them easier to produce and comprehend."
  - [104] is Hale (2001), "A probabilistic Earley parser as a psycholinguistic model".
  - [105] is Levy (2008), "Expectation-based syntactic comprehension".
  - The only reading-time title is [107], Smith & Levy (2013). Gibson cites it only in the glossary entry on information locality (p. 3).
- **Why it matters:**
  - Scope: Gibson writes about *processing effort* in production and comprehension, not *reading* effort.
  - Quantity: Gibson writes *predictability*, not *surprisal*; a logarithmic link is the title of the unseen [107].
  - Source: none of our sources calls Hale (2001) or Levy (2008) a "reading-time study".
  - Brief: unit 15 and UNSEEN item 3 forbid "surprisal predicts reading time" on Gibson's authority. The recall card attributes this narrowed, strengthened claim to Gibson.
- **Severity:** major (wrong scope; the claim is changed and attributed to the author).
- **Fix:**
  - Recall card 8 and check (iii) should use Gibson's terms ("language processing effort is associated with predictability"), in the post and the audio.
  - The Sources note should say "the processing studies [104, 105] behind Gibson and colleagues' sentence".
  - Move 3 should say "whether processing effort tracks predictability".

---

## Minor

### V1-03 · Quote not verbatim at Shannon p. 18 (#village intro)
- **Post:** "Shannon assumes symbols “are chosen independently”" (cited to Shannon 1948, p. 18).
- **Source:** Shannon 1948, p. 18.
- **Source says:** "successive symbols being chosen independently".
- **Severity:** minor.
- **Fix:** Quote "successive symbols being chosen independently", or drop the quotation marks.

### V1-04 · "the basis" for "A basis" (#hook; audio)
- **Post:** "Shannon names both papers as the basis for a general theory".
- **Source:** Shannon 1948, p. 1.
- **Source says:** "A basis for such a theory is contained in the important papers of Nyquist and Hartley".
- **Severity:** minor (slightly strengthened).
- **Fix:** "names their papers as a basis for a general theory".

### V1-05 · Pierce's book called a "history" (#hook; audio "history of the field")
- **Post:** "Pierce, in his 1961 history, reports Nyquist's answer". The audio says "his nineteen sixty-one history of the field".
- **Source:** Pierce 1961, title page (pdf 7) and ch. II, "The Origins of Information Theory".
- **Source says:** The book is *Symbols, Signals and Noise: The Nature and Process of Communication*, a general introduction. Only ch. II is historical.
- **Severity:** minor.
- **Fix:** "Pierce, in the history chapter of his 1961 introduction, reports ...".

### V1-06 · Hartley's measure is the logarithm of the count, not the count (#hook)
- **Post:** "a message is measured by how many different messages the sender could have picked ... Pierce says the count fits only if ...".
- **Source:** Pierce 1961, pp. 39–40.
- **Source says:** Hartley "defined H, the information of the message, as the logarithm of the number of possible sequences". The next paragraph says "This is acceptable ... only if successive symbols are chosen independently".
- **Severity:** minor. Layer 1 avoids logarithms, and the fold-out gives H = n log s, but "the count fits" is not what Pierce says.
- **Fix:** "a message is measured by the number of messages the sender could have picked (in fact by its logarithm; see the fold-out in step 1) ... Pierce says this measure fits only if ...".

### V1-07 · Unlabelled historical verdict (#hook)
- **Post:** "What was missing was a number that weighs each message by how likely it is."
- **Source:** Pierce 1961, p. 40, gives no such verdict. He says Hartley "stated the matter in a way which encouraged mathematical attack and inspired further work".
- **Severity:** minor (our reasoning, not labelled).
- **Fix:** Add "(our reading)".

### V1-08 · Nyquist fold-out: citation, the "seven values" remark, and "slip" in the audio (#box-nyquist; audio "village")
- **Post:** "Eight values give log₂ 8 = 3 times (ours; Pierce's “four times” is an apparent slip, and his list of values shows only seven)". The next citation in the text is "Pierce 1961, p. 40". The audio says "which is a slip".
- **Source:** Pierce 1961, p. 38.
- **Source says:** Eight values "(0, 1, 2, 3, 4, 6, 7, or +7, +5, +3, +1, −1, −3, −5, −7) should enable us to send four times as fast". Pierce gives two lists: the first has seven values, the second has eight.
- **Severity:** minor.
- **Fix:**
  - Cite "Pierce 1961, p. 38" for "four times".
  - Write "his first list of values shows only seven".
  - Keep "apparent slip" in the audio.

### V1-09 · E1 drops the power-of-two condition (#village, step 1)
- **Post:** "For N equally likely options, the number of questions k satisfies N = 2^k, so k = log₂ N."
- **Source:** MacKay 2003, pp. 73–74.
- **Source says:** "the length of each name would be log₂ |A_X| bits, if |A_X| happened to be a power of 2".
- **Severity:** minor. Step 2 mentions whole numbers later, but for N = 12 or N = 3 the formula as written is false.
- **Fix:** "For N equally likely options, where N is a power of two, ...". Add one clause saying that otherwise log₂ N is a lower bound (ours).

### V1-10 · "she would learn almost nothing" overstates (#cafe, "Three checks"; audio)
- **Post:** "If she asked “Matcha?” first, almost every answer would be a shake and she would learn almost nothing".
- **Source:** Our own toy. With matcha at 1 in 8, the question is worth 0.544 bits on average, and a shake is worth log₂(8/7) = 0.193 bits (Python).
- **Severity:** minor (the toy's number points the right way, but "almost nothing" is about half of a fair question).
- **Fix:** "she would usually learn little: a shake rules out only one customer in eight".

### V1-11 · Wrong page for "can never balance" (#weighing)
- **Post:** "With six on each pan the pans can never balance, and the split is 12 : 12 : 0" (cited to MacKay 2003, p. 70).
- **Source:** MacKay 2003, p. 68.
- **Source says:** "these two sets of balls can never balance, so the only possible outcomes are ‘left heavy’ and ‘right heavy’". Page 70 has only the 8 : 8 : 8 and 3 : 3 : 2 splits.
- **Severity:** minor.
- **Fix:** Cite "MacKay 2003, pp. 68, 70".

### V1-12 · Wrong page for the telescoping product (#submarine)
- **Post:** "This is MacKay's telescoping product" (cited to MacKay 2003, p. 71).
- **Source:** MacKay 2003, p. 72, eq. 4.14.
- **Source says:** "= log₂ 64/1 = 6 bits" (eq. 4.14, p. 72). Page 71 ends at eq. 4.11.
- **Severity:** minor.
- **Fix:** Cite "MacKay 2003, p. 72".

### V1-13 · Exercise 4.9: "the second group" has no first group; the audio misparaphrases it (#weighing; audio "weighing")
- **Post:** "MacKay reports that some say it “conveys no information at all”, and asks the reader to “Explain to the second group why they are both right and wrong”". The audio says "asks the reader to explain why both groups are right and wrong".
- **Source:** MacKay 2003, p. 84.
- **Source says:** "While some people ... think that weighing six balls against six balls is a good first weighing, others say ‘no, weighing six against six conveys no information at all’. Explain to the second group why they are both right and wrong."
- **Severity:** minor. On the page the first group is missing. In the audio, "both" moves from "right and wrong" to "groups", which changes the meaning.
- **Fix:** Name both groups ("some think 6 v 6 a good first weighing; others say it 'conveys no information at all'"). In the audio, say "explain to the second group why they are both right and wrong".

### V1-14 · EQ means two things (#entropy E9 vs #nothalves E6)
- **Post:** E9 defines EQ = Σ P(x) L(x) for *any* script. E6 then states "H ≤ EQ < H + 1" for "the best average".
- **Source:** Cover & Thomas 1991, p. 95.
- **Source says:** "The expected number of questions EQ in this optimal scheme satisfies H(X) ≤ EQ < H(X) + 1" (eq. 5.61).
- **Severity:** minor. With E9's meaning, E6 is false for a bad script.
- **Fix:** In E6 write "EQ of the best script" (or EQ*), as Cover does.

### V1-15 · Village widget shows surprisal 0 for a word with share 0 (#entropy, `village-lab`)
- **Post:** `"hr":"if(pr>0,log2(1/pr),0)"` etc. With the "only rain" preset, the bars for sun, wind and snow read 0.00, and the caption says the bars are "each word's surprisal".
- **Source:** MacKay 2003, p. 32.
- **Source says:** The convention is "0 × log 1/0 ≡ 0", for the *contribution* to H. The surprisal itself is unbounded; notebook exercise 7 prints "inf".
- **Severity:** minor (a widget readout that teaches the wrong edge case).
- **Fix:** Show "—" or "no value (never happens)" for a share of 0, or label the bars "share × surprisal".

### V1-16 · Bias explained by one cause only (#fails, boundary 5; audio)
- **Post:** "Biased low for small samples, because a rare word that never appears gets share 0."
- **Source:** Our notebook, exercise 6 (results.md, cell 14). At n = 1,000 every word appears in essentially every sample, and the gap is still −0.0031. The plug-in estimate is biased low because entropy is a concave function of the shares, not only because words are unseen (ours).
- **Severity:** minor (our mechanism, stated as the whole cause).
- **Fix:** "Biased low for small samples, partly because a rare word that never appears gets share 0 (ours); the bias shrinks as n grows".

### V1-17 · Recall card 4: the best script averages 2 for more than equal shares (#recall)
- **Post:** "when would the best script average exactly 2? ... For four equally likely words."
- **Source:** Our computation. Shares 0.3, 0.3, 0.2, 0.2 have Huffman lengths 2, 2, 2, 2, so the best script also averages exactly 2.000 (Python).
- **Severity:** minor (the answer reads as the only case).
- **Fix:** "For example, for four equally likely words (then H = 2 as well)".

### V1-18 · Lens 2 framing: "tested against behaviour" and "unproven" are unsourced and pull against each other (#lenses, lens 2; #answer short answer; audio)
- **Post:** Lens 2 says "the only lens where the number is tested against behaviour". The short answer says "lens 2: one such claim, unproven". The audio says "still unproven".
- **Source:** Gibson et al. 2019, p. 11.
- **Source says:** "Since language processing effort is associated with predictability [104,105]". We hold neither study (brief unit 15, UNSEEN 3).
- **Severity:** minor. "Unproven" judges evidence we have not read, and "tested against behaviour" asserts what those studies did.
- **Fix:** In the short answer, write "lens 2: one such claim, whose evidence we have not checked". In lens 2, write "the only lens whose claim is about behaviour (ours)".

### V1-19 · Pierce's condition loses its "if" (#fails, boundary 2)
- **Post:** "In Pierce's simplest case the chances “must not change with time”".
- **Source:** Pierce 1961, p. 81.
- **Source says:** "The probabilities p0 and p1 must not change with time if the source is to be ergodic."
- **Severity:** minor (a dropped condition).
- **Fix:** Add "if the source is to be ergodic (his model of a source)", or say "for his model of the source".

### V1-20 · Mills Move 1: our gloss attached to Mills' quote, his reason left out, and our test called "Mills' sense" (#imagination, Move 1; audio). Writer's flag, judged.
- **Post:**
  - "An issue is not a trouble multiplied: it is “unlike even widespread trouble” and often involves “a crisis in institutional arrangements”".
  - In the next paragraph: "A test: if changing the ranking changes what many readers miss, and individual effort does not, it is an issue in Mills' sense".
- **Source:** Mills 1959, pp. 8–9 (pages of the 2000 Oxford edition).
- **Source says:**
  - "it is the very nature of an issue, unlike even widespread trouble, that it cannot very well be defined in terms of the immediate and everyday environments".
  - On p. 9: "The very structure of opportunities has collapsed."
  - On p. 8: "An issue is a public matter: some value cherished by publics is felt to be threatened."
- **Judgement:** The paraphrase is fair in substance, and its placement after the hypothetical example is right. But:
  - (a) "not a trouble multiplied" is our wording, and the colon makes it read as Mills';
  - (b) the quote leaves out what the issue is "unlike widespread trouble" *in*;
  - (c) Mills' own reason in the example ("The very structure of opportunities has collapsed") is missing, so his counts look like the whole story;
  - (d) the test is ours, but "in Mills' sense" claims fidelity, and Mills' definition also needs publics who feel a value threatened.
- **Severity:** minor.
- **Fix:**
  - Write "An issue, Mills says, 'unlike even widespread trouble', cannot be defined within everyday milieux: in his example 'The very structure of opportunities has collapsed' (p. 9). So (our reading) an issue is not a trouble multiplied."
  - Write "A test (ours, in the spirit of Mills' distinction): ...".

### V1-21 · Pierce p. 267 is about art and felt surprise (#imagination, Move 1)
- **Post:** "Pierce's one sourced anchor: “We can be surprised repeatedly only by contrast with that which is familiar” (Pierce 1961, p. 267). Whose idea of the familiar prices the message?"
- **Source:** Pierce 1961, p. 267 (art chapter).
- **Source says:** "to be appreciated art must be in a language familiar to the audience ... We can be surprised repeatedly only by contrast with that which is familiar, not by chaos."
- **Severity:** minor. The referent is audiences of art, and the sense is the felt one, which the post's own term box excludes ("not a feeling"). Brief unit 11, trap (c), says Pierce uses "surprising" loosely here.
- **Fix:** Add "writing about art and its audiences, in the everyday sense of surprise", and label the link to model-priced surprisal as our metaphor.

### V1-22 · Mills' "Nowadays at least" dropped (#box-mills-counting)
- **Post:** "He also says he would never count or measure anything before he had played with its elements in an imagined world “in which I control the scale of everything”".
- **Source:** Mills 1959, p. 215.
- **Source says:** "Nowadays at least, I should never think of actually counting or measuring anything, before I had played with each of its elements and conditions and consequences".
- **Severity:** minor (a dropped qualifier).
- **Fix:** "He says that, 'Nowadays at least', he would never count ...".

### V1-23 · Gibson Sources entry: "pre-proof" and the volume and page data (#sources). Writer's flag, judged.
- **Post:** "Trends in Cognitive Sciences, 23(5), 389–407. Pages cited are those of the journal pre-proof (pp. 1–19)".
- **Source:** gibson-2019-efficiency.pdf. PDF metadata: "Trends in Cognitive Sciences, Corrected proof. doi:10.1016/j.tics.2019.02.003". Every footer reads "Trends in Cognitive Sciences, Month Year, Vol. xx, No. yy". The p. 1 footer has "https://doi.org/10.1016/j.tics.2019.02.003".
- **Source says:** The file is a *corrected proof* (article in press), not a "journal pre-proof". The volume, issue and pages (23(5), 389–407) appear nowhere in the file, so they are **unverifiable** from our sources.
- **Severity:** minor.
- **Fix:** Write "corrected proof (article in press), doi:10.1016/j.tics.2019.02.003; pages cited are those of this proof (pp. 1–19)". Check 23(5), 389–407 against the published version, or drop it.
- **Shannon 1951, for comparison (verified):** vol. 30, pp. 50–64 is correct. The running heads read "THE BELL SYSTEM TECHNICAL JOURNAL, JANUARY 1951" on pp. 52–64, the PDF runs pp. 50–64, and Cover & Thomas 1991, p. 517 bibliography (pdf 541), ref. [42], gives "Bell Sys. Tech. Journal, 30: 50–64, 1951".
- **Shannon 1948 (verified):** "Vol. 27, pp. 379–423, 623–656" is in the reprint's own header (p. 1).

### V1-24 · Unexplained terms outside layer 2 (layer 1, steps 2 and 5, layer 4(a), boundary 5, layer 5)
- **Post:**
  - "quadruplex telegraph" (#hook);
  - "shortest uniquely decipherable script" (#surprisal, #answer);
  - "telescoping product" (#submarine);
  - "plug-in entropy with bias correction and bootstrap intervals", "regression with topic fixed effects" and "LLM surrogate labelling" (an abbreviation; #imagination).
- **Source:** WRITING §3 (define at first use) and CHARTER §6. Pierce p. 38 explains quadruplex only as "he sent two messages instead of one".
- **Severity:** minor. These are not in layer 2, so they are not major.
- **Fix:** Add a short gloss at first use for each, e.g. "the quadruplex telegraph (Edison's, which sent two messages at once)", "uniquely decipherable (a string of answers that can be cut back into drinks in only one way)", "large language model (LLM)".

### V1-25 · MacKay's hedges dropped in two paraphrases (#lenses, lens 5; audio "village")
- **Post:** Lens 5 says "The designer's view: to find something fast, choose the experiment with the most equal outcomes" (cited to MacKay 2003, p. 70). Audio: "MacKay writes that the best questions successively divide the sixty-four possibilities into equal sized sets".
- **Source:** MacKay 2003, p. 70.
- **Source says:** "Thus we might conclude: the outcome of a random experiment is guaranteed to be most informative if ...", and "Intuitively, the best questions successively divide the 64 possibilities".
- **Severity:** minor. Step 4 keeps the first hedge and the page quote keeps "Intuitively"; only these two paraphrases drop them.
- **Fix:** Lens 5: "MacKay's tentative conclusion ('we might conclude'): ...". Audio: "MacKay writes that, intuitively, the best questions ...".

### V1-26 · "The record of his guesses" is loose for Shannon's first version (#roles; audio)
- **Post:** "he knows it only up to the current point, guesses the next letter, and is told whether he was right. The record of his guesses is the reduced text."
- **Source:** Shannon 1951, pp. 54–55.
- **Source says:** "the second line contains a dash for each letter correctly guessed. In the case of incorrect guesses the correct letter is copied in the second line."
- **Severity:** minor. The reduced text holds no wrong guesses: it holds dashes and correct letters (or, in the second version, guess numbers, p. 56).
- **Fix:** "The record — a dash for each right guess and the correct letter for each wrong one — is the reduced text".

---

## Checked and found correct

**Quotes.** Every quotation from a source in the page was matched by script against the page text of the cited source, with quotes, dashes and hyphenation normalised. The doubtful ones were read in context: MacKay p. 72 "I think ..." (line-wrapped), Gibson pp. 1, 3 and 14 (two-column layout), Pierce p. 81, Mills pp. 8–9 (page break) and Pierce p. 267 (OCR "constrast"). Apart from V1-03, all are verbatim and at most 25 words. None is cut before a turn, including Mills p. 214 "sense of proportion" and the Shannon p. 11 "in no way necessary"/"real justification" pair.

**Pages.** Every citation's page supports its sentence except V1-11 and V1-12. In detail:
- Shannon 1948: pp. 1, 2, 10, 11, 12, 14, 18.
- Shannon 1951: p. 54 (the passage is unfamiliar to the predictor) and p. 55 (twin, reduced text as an encoded form, Fig. 2). The writer's flagged roles are correct.
- MacKay: pp. 26, 32, 33, 66, 67, 68, 70, 71, 72, 73, 74, 84.
- Cover & Thomas 1991: pp. 5, 13, 14–15, 94–95.
- Pierce 1961: pp. 23–24, 24, 35–40, 80, 81, 264, 267.
- Gibson: pp. 1, 3, 4, 6, 7, 11, 14, 15.
- Mills: pp. 4–6, 5, 6, 7, 8, 8–9, 9, 73, 212, 213, 214, 215.

**Editions (writer's flags).**
- Cover & Thomas = 1st ed., Wiley 1991, ISBN 0-471-06259-6 (copyright page). The file name "cover-2006" is wrong, but the post's citation is right.
- Pierce = Harper & Brothers, 1961, "FIRST EDITION" (copyright page, pdf 8).
- Mills = Oxford, "Copyright © 1959, 2000", afterword by Gitlin; the post states that its pages are those of the 2000 printing.
- Gibson: see V1-23. Shannon 1948 and 1951: verified (see V1-23).
- MacKay's file is "Version 7.2 (fourth printing) March 28, 2005" of the on-screen edition. Its pages match the post's. Naming the version in Sources would be more precise (optional).

**Hedges and voice.**
- Mills is reported as argument and advice ("argued", "defines", "suggests", "His advice is not findings", "I believe" kept).
- The hypothetical status of the unemployment numbers is stated, and no rate is given.
- Gibson's "is associated with" is kept in lens 2. The "likely reflects" and "approximates" hedges are kept.
- The bolder abstract sentence is given beside the p. 14–15 limits (balance kept).
- MacKay's "Thus we might conclude" and "I think" are kept in step 4 and step 5.
- MacKay's Bayesian sentence is attributed to the Bayesian view ("As MacKay puts that view").
- Shannon's "irrelevant to the engineering problem" is scoped, and his "final destination" sentence is added.

**"Ours" labels.**
- Correctly labelled: the cups-and-rats framing; the Hartley–raw bit content pairing (MacKay never names Hartley: whole-text search, 0 hits); "Shannon 1948 uses neither word" (whole-text search for "surprisal" and "information content": 0 hits); the eight-values ×3; the four-square check; the TEA walk-through; the 0.7 village; the bias table; the forecasters; the move names; the inbox case; both research questions.
- The 6-v-6 claim (ours; writer's flag) is correct and correctly labelled. After "left heavier" each ball keeps exactly one of its two hypotheses, so the posterior over balls is still uniform over 12 (0 bits), while the 24 ball-and-direction hypotheses halve (1 bit). The notebook prints 0.000 and 1.000.

**Numbers, recomputed in Python (all match the page and the audio).**
- Café 14/8 = 1.75; old way 2.
- Village surprisals 1, 2, 3, 3; H = 1.750; uniform H = 2.000; only rain H = 0; script on uniform 2.25; script on only rain 1.000; reversed H = 1.750.
- Grouping 1 + ½·1.5 = 1.75; E3 1 + 3 = 4.
- 0.3 → 1.737 (1.74); 0.7 → 0.5146 (0.515).
- MacKay p. 67 table: 10.0, 6.6, 3.3, 2.3, 1.0, and H₂ 0.011, 0.081, 0.469 (printed 0.47), 0.722, 1.0.
- log₂ 3 = 1.585 (58.5 %); log₂ 8 = 3.
- Weighing 0.817, 1.252, 1.500, 1.585, 1.483, 1.000; log₂ 24 = 4.585; remaining 3.000 at 4 v 4.
- Submarine 0.02272, 0.02308 (MacKay truncates to 0.0230; the post rounds, as stated), 0.0458, 30 misses 0.9542, 16 misses 1.0000, totals 1, 2, 6.
- Five misses 0.0227, 0.0231, 0.0235, 0.0238 (0.023847), 0.0242; log₂(64/59) = 0.1174.
- Four squares 0.415, 0.585, 1.000, sum 2.
- Wenglish 32,768, 15, 3, 4.00, 9.97.
- 0.7 village H = 1.357, Huffman 1, 2, 3, 3, EQ 1.5, gap 0.143, H + 1 = 2.357.
- Stall 1.875 = 1.875; after the change, old script 2.5, H 2.25, best 2, 2, 2, 3, 3 at 2.25.
- Ana and Ben 3, 1, gap 2.

**Widgets.** `node site/ai4read/components/check.mjs` reports 8/8 configs OK. The default readouts match the text (village 1.750/1.750/2.000; weighing 1.585, 3.000 remain; plot 3.3/0.469; forecasters 3.00/1.00/2.00). The presets were recomputed by hand: all equal 2.000/2.250; only rain 0/1.000; reversed 1.750/2.625; 6 v 6 1.000, with 3.585 remaining. The stepper rows were recomputed and match. The weighing caption's six values match.

**Notebook.** Re-executed top to bottom with nbclient in the provided environment. Every printed output is identical to the saved outputs and to results.md; the only difference is how one cell's stream output is split into chunks, and the text is the same.
- Bias table: 1.5036, 1.6753, 1.7253, 1.7469 and gaps −0.2464 … −0.0031, rounded in the post to 1.504, 1.675, 1.725, 1.747 and −0.246, −0.075, −0.025, −0.003.
- 1,050 share vectors; the bound holds; gaps 0.0019–0.6301.
- Exercise 5 text has no "j" (26 distinct symbols, confirmed).
- Shannon 1951's 4.03 for 27 letters (p. 54 table) and MacKay's 4.11 (p. 32) are correctly cited in exercise 5.

**Answers to checks and recall.** All are correct except V1-17 and the scope issue in V1-02: café (a) and (b), the step 3 check (2.25), the step 4 check (0 bits), the step 5 check, the roles check, the layer-4 labels (i), (ii) and (iv), recall cards 1–3 and 5–7, and the transfer challenge.

**post.json.** The summary matches the post. The cite keys match the Sources ids.

**Audio.** It says the same things as the page, apart from the audio-specific items in V1-01, V1-02, V1-05, V1-08, V1-13, V1-18 and V1-25. Its numbers match the page.
