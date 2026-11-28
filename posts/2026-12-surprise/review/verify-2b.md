---
post: 2026-12-surprise
stage: S5 round 2 (independent fact check of the revised draft), checker B
checker: fresh fact-checker (Sonnet); did not read self-review.md, numbers.md or review/verify-2.md; no network
checked: src/content.html (all, incl. fold-outs, quizzes, recall, widget configs and readouts, Sources), audio-script.md, post.json, notebook/01_surprise_entropy.ipynb (re-executed with nbenv python) and notebook/results.md
against: sources/*.pdf and *.txt (page text split per page with pdftotext; page images read for Gibson p. 1), source-brief.verified.md
date: 2026-11-28
---

# Verify 2B: post 04 "How much is a surprise worth?"

**Counts: 0 critical · 3 major · 13 minor**

Release gate (rubric §A): not met while the 3 majors stand. With more than 5 minors, criterion 1 would score 3 even after the majors are fixed; most minors are one-phrase fixes.

Layer 2 (§1a, `#cafe`): scanned text, diagrams, parts list and check-yourself for formulas, symbols, abbreviations and unexplained terms. None found ("script" and "string" are defined in the sentence that introduces them). No layer-2 finding.

Note on S2c: no "Addendum S2c" (Huffman) was in `source-brief.verified.md` when step 6 was checked. V2B-01 below is checked against Cover & Thomas §5.6 directly; if a Huffman unit lands, merge it with V2B-01.

## Round-1 majors: resolved?

| Finding | Page | Audio | Verdict |
|---|---|---|---|
| V1-01 (Pierce p. 24 hedge and scope) | `#village` term box now reads: confusion about how communication theory relates to physics "is sometimes aggravated when more than one meaning of information creeps into a discussion". Verbatim, p. 24. | `village` chapter says the same sentence. | **Resolved** |
| V1-02 (Gibson "language processing effort ... predictability") | Quoted only as "Since language processing effort is associated with predictability [104,105]" (lens 2, p. 11 checked on the page text); check (iii), recall card 8, Sources note, move 3 all keep predictability and "associated with". Residual wording issue in move 3: V2B-13 (minor). | `lenses`, `fails`, `recall`, `imagination` all match the page. | **Resolved** (one minor residue) |
| V1B-01 ("Only halves, quarters and eighths ...") | Now "Only shares that are powers of one half (1/2, 1/4, 1/8, 1/16, …) cost a whole number of questions (ours)". True (log2(1/p) is a whole number only for p = 2^-k). Boundary 6 no longer has the false sentence. | `surprisal` chapter matches, labelled "That is ours". | **Resolved** |
| V1B-02 (reading effort) | Same fix as V1-02. Check (iii) now "Language processing effort is associated with predictability.", answer "An empirical claim by others, hedged ..." | `fails` and `recall` match. | **Resolved** (response said "partly"; the remaining difference is only that "Since" is dropped, which is fine) |
| V1B-03 (audio added "Equal to H only when every share is a power of one half") | The page says nothing about an equality condition (except the "ours" line in step 2, which is a different statement). | Sentence deleted; `nothalves` recap now reads "at least H and less than H plus one ... Join the two rarest, repeat." Searched the whole audio script: no "equal to H only when". | **Resolved** |
| V1B-04 (audio added "Gibson ... use surprisal for colour words, word length and ... processing") | Page lens 2 keeps the three statements apart. | `lenses`, lens two now matches the page: colour surprisal, one premise "since language processing effort is associated with predictability", "their word is predictability, not surprisal". | **Resolved** |

**Audio lines quoted in `response-1.md`:** I extracted every quoted audio line (59 segments, ellipsis-split) and searched `audio-script.md` after normalising quotes and spaces: all 59 are present. The single non-match was a page quote (V1B-13's "sense of proportion"), not an audio line; it is on the page, in the fold-out `box-mills-counting`.

## Major findings

### V2B-01 (major) "A rule, ours and not from our sources": the rule is Huffman's, and Cover & Thomas give it
- **Location:** `#nothalves`, "The 0.7 village": "A rule, ours and not from our sources (notebook exercise 8 does it in code): repeatedly join the two rarest outcomes into one group, and every outcome inside the group gets one more question." Audio `nothalves`: "A rule, ours and not from our sources, which the notebook does in code: repeatedly join the two rarest outcomes ...". Notebook exercise 8 intro says the opposite half: "This is the Huffman method; the post labels the rule as ours, not from its sources."
- **Source and page:** Cover & Thomas 1991, §5.6, pp. 92–93 (pdf 114–115). Example 5.6.1 on p. 93: "combining the two least likely symbols into one symbol, until we are finally left with only one symbol". p. 92: "An optimal ... prefix code ... can be constructed by a simple algorithm discovered by Huffman [138]". Also p. 95: "Since the Huffman code is the best source code for a random variable, the optimal series of questions is that determined by the Huffman code."
- **What the source says:** the procedure the post describes is the Huffman algorithm, stated and proved optimal in a source the post already cites (pp. 94–95, eq. 5.61).
- **Severity:** major. "Not from our sources" is a false negative claim about the sources (WRITING §9: search all sources before writing "none"), and our own label hides a named, sourced result. The brief's own note (unit on Cover p. 95, "a Huffman tree gives lengths 1, 2, 3, 3") also calls it Huffman.
- **Fix:** in page and audio write "This is Huffman's rule (Cover & Thomas 1991, §5.6, pp. 92–93, who prove it gives the shortest average); the worked 0.7 case is ours, run in code." Keep the notebook text, which already says Huffman.

### V2B-02 (major) "uniquely decipherable" is glossed with the wrong definition
- **Location:** `#answer`, (a) What it really is: "(“uniquely decipherable” means no string is the start of another, so a run of answers can be cut into words in only one way)". Audio `answer`: "Uniquely decipherable means no string is the start of another, so a run of answers can be cut into words in only one way."
- **Source and page:** Gibson et al. 2019, p. 4 (Box 2) uses the term and does not define it. Cover & Thomas 1991, p. 92 separates the two classes: "the class of uniquely decodable codes does not offer any further choices for the set of codeword lengths than the class of prefix codes".
- **What the source says:** "no string is the start of another" is the **prefix** (instantaneous) condition. Every prefix code is uniquely decodable, but not the reverse (for example {0, 01} is uniquely decodable and 0 is the start of 01). The step 2 gloss ("rows of answers can be cut back into words in only one way") is correct; the 4(a) gloss defines a different, stronger property.
- **Severity:** major (new gloss that is false as a definition; WRITING §9 "new glosses are new claims"). It also sits in the abstract layer where the reader takes the definition at face value.
- **Fix:** keep only "a run of answers can be cut into words in only one way", and if the prefix property is wanted add "(the simplest way to guarantee this is that no string is the start of another, which is the case for our card)". Same change in the audio.

### V2B-03 (major) Audio recap of `imagination` adds "only when" and states our hypothesis as a conclusion
- **Location:** audio `imagination`, Recap: "Trouble becomes issue only when the cause lies in an arrangement, here whoever owns the model."
- **Source and page:** page `#imagination`, move 1 (Mills 1959, pp. 8–9, and our labelled reading); no equivalent sentence on the page.
- **What the source says:** Mills distinguishes trouble and issue; the page adds "So (our reading) an issue is not a trouble multiplied", and for the ranking case says "that it does so is a hypothesis, not a finding" and offers a test (ours). Nowhere does the page say a trouble becomes an issue "only when" the cause is an arrangement, nor that the arrangement here is "whoever owns the model".
- **Severity:** major (audio strengthens: a new "only", and our hypothesis presented as established; V1B-03 was rated major for the same kind of addition).
- **Fix:** replace with a recap that matches the page: "In Mills' terms, trouble and issue differ by where the cause lies. Our hypothesis, not a finding: for a ranking that prices messages under its own model, part of the cause may lie in whose model prices them. Extremes and scale, and other disciplines' eyes, point to the same question: whose model prices a surprise?"

## Minor findings

### V2B-04 (minor) Audio recap of `submarine`: "A hit is worth six"
- **Location:** audio `submarine`, Recap: "A hit is worth six, a first miss about two hundredths, and the total for finding the target is always six."
- **Source:** MacKay 2003, pp. 71–72; page step 4: "A hit on the first shot would be worth six"; a hit on shot 49 is worth 4, on shot 64 worth 0.
- **Issue:** the recap drops "on the first shot"; looped alone it says every hit is worth six, which contradicts the chapter's point.
- **Fix:** "A hit on the first shot is worth six, a first miss about two hundredths, and the total for finding the target is always six."

### V2B-05 (minor) "ergodic" used without a definition
- **Location:** `#fails` boundary 2: Pierce says the chances "must not change with time if the source is to be ergodic"; audio `fails` repeats it.
- **Source:** Pierce 1961, p. 81 (quote verified); Pierce defines ergodic on p. 59 (a stationary source whose ensemble averages equal its time averages).
- **Issue:** technical term not defined at first use (WRITING §3).
- **Fix:** add "(ergodic: a source whose averages over a long run settle to fixed values)" or quote only "must not change with time".

### V2B-06 (minor) Mills's "information" glossed as "facts and news" without a label
- **Location:** `#imagination` intro: "His “information” (p. 5) means facts and news, not Shannon’s sense". Audio: "His word information means facts and news, not Shannon's sense."
- **Source:** Mills 1959, p. 5: "It is not only information that they need—in this Age of Fact, information often dominates their attention".
- **What it says:** the context supports "facts"; "news" is not there.
- **Fix:** "His “information” (p. 5) means, in our reading, facts (he calls his time the Age of Fact), not Shannon’s sense."

### V2B-07 (minor) "MacKay cuts digits off" is our inference stated as fact
- **Location:** `#submarine` check: "MacKay cuts digits off and prints 0.0230 for the second; we round". Audio: "MacKay cuts digits off and prints zero point zero two three zero for the second."
- **Source:** MacKay 2003, p. 71, Fig. 4.3: 0.0227, 0.0230, 0.0443, 0.0874. True values are 0.02272, 0.02308, 0.04439, 0.08746; all four printed values equal the truncation.
- **Issue:** MacKay does not say he truncates; this is an inference from four numbers.
- **Fix:** "MacKay prints 0.0230 for the second, which matches cutting off the digits (our reading); we round."

### V2B-08 (minor) Submarine "In the café" line: "Whichever path ... the total ... is the same"
- **Location:** `#submarine`, In the café: "A no on the ticket costs 0.0227 of a question; a yes costs six. Whichever path the customer takes, the total worth of finding her drink is the same: the cost of that drink." Audio matches.
- **Issue:** read plainly, "the same" says the two paths (yes: six; no then more answers) have the same total, but different drinks have different costs. What is true (ours): for one given drink, the answers' worths add to that drink's cost whatever order the questions come in. The matcha-at-1/64 toy also leaves the other three shares unstated.
- **Fix:** "For any one customer, the worths of her answers add up to the cost of her drink, whatever order the card asks in."

### V2B-09 (minor) Boundary 5 gives two reasons that are one
- **Location:** `#fails` boundary 5: "Biased low for small samples, partly because a rare word that never appears gets share 0, and partly because noisy observed shares lower the entropy on average (ours)." Audio and notebook exercise 6 hint repeat the two-part reason.
- **Issue:** the numbers are right (reference run: gaps −0.2464, −0.0747, −0.0247, −0.0031, reproduced). But a word never seen is the extreme case of noisy shares, not a separate cause; "partly ... partly" implies two independent parts we did not measure.
- **Fix:** "Biased low for small samples because noisy observed shares lower the entropy on average (ours); the extreme case is a rare word that never appears and gets share 0."

### V2B-10 (minor) Hook: Hartley's remark loses its condition and its object
- **Location:** `#hook`: "Hartley saw that some letters are chosen more often than others, E more than Z, and that this should govern the lengths of signals".
- **Source:** Pierce 1961, p. 40: "restrictions on the selection of symbols (the fact that E is selected more often than Z) should govern the lengths of the secondary symbols (Morse code representations) if we are to transmit messages most swiftly".
- **Fix:** "...and that this should govern the lengths of the code symbols, if messages are to be sent most swiftly." Audio the same.

### V2B-11 (minor) Sources: "corrected proof"
- **Location:** `#sources`, Gibson: "Our copy is the corrected proof (article in press)".
- **Source:** the PDF's first page (image) shows "ARTICLE IN PRESS", "TICS 1894 No. of Pages 19", "Month Year, Vol. xx, No. yy"; nothing on it says "corrected".
- **Fix:** "Our copy is an article-in-press proof (TICS 1894, 19 pages)".

### V2B-12 (minor) `weigh-lab` bars are clipped at the configured maximum
- **Location:** `#entropy` fold-out `box-weighing`, config `"bars":{...,"max":0.5}`.
- **Check:** the balance chance is 20/24 = 0.833 at k = 1 and 16/24 = 0.667 at k = 2; the component clamps bar width at 100 %, so those bars look equal to 0.5 while the readout prints 0.833 and 0.667. The numbers in the readout and caption are right (rerun: 0.817, 1.252, 1.500, 1.585, 1.483, 1.000).
- **Fix:** set `"max":1`.

### V2B-13 (minor) Move 3 narrows Gibson's sentence to "a listener" and "the word"
- **Location:** `#imagination`, move 3: "A psycholinguist asks whether a listener’s processing effort tracks how predictable the word is, an association Gibson and colleagues state". Audio matches.
- **Source:** Gibson et al. 2019, p. 11: "Since language processing effort is associated with predictability [104,105], an element that makes nouns more predictable in context would make them easier to produce and comprehend."
- **Issue:** the source speaks of language processing effort in general (production and comprehension) and of elements in context, not of a listener and a word; "tracks" is a little stronger than "is associated with".
- **Fix:** "...whether language processing effort is associated with how predictable an element is in context, a link Gibson and colleagues state (p. 11)."

### V2B-14 (minor) Audio drops a sentence of the page's "What it means" (step 3)
- **Location:** page: "It predicts the cost of the best script when the shares are powers of one half. It does not say what a word means ..."; audio `entropy` What it means omits the first of these.
- **Issue:** nothing is strengthened, but the audio no longer says the same as the page (the brief asks for nothing dropped).
- **Fix:** add "It predicts the cost of the best script when the shares are powers of one half." to the audio.

### V2B-15 (minor) Notebook exercise 3 hint uses "telescopes"
- **Location:** notebook cell for exercise 3, hint: "The product of the miss chances telescopes".
- **Issue:** the page removed the word (V1-12) and says what cancels; the notebook still uses unexplained jargon.
- **Fix:** "Each numerator cancels the next denominator, so the product is one fraction."

### V2B-16 (minor) `post.json` tag "Bayesian & causal inference"
- **Location:** `post.json`, `tags`.
- **Issue:** the post has a Bayesian-belief lens but no causal content (the only mention is "Associated with is not caused by"); the tag promises more than the post covers.
- **Fix:** use a tag for Bayesian theory only, if the site's tag list allows it.

## Checked and correct

**Numbers (recomputed in Python and with `check.mjs`: 8/8 widget configs OK).** Village H = 1.75; surprisals 1, 2, 3, 3; 14 answers in 8 days; uniform village with the village script 2.25; plain labels 2.000; café 14 answers, 1.75 vs 2; 0.7 village H = 1.3568 (1.357), best lengths 1, 2, 3, 3, EQ* = 1.5, gap 0.143, bound 1.357 ≤ 1.5 < 2.357; −log2 0.7 = 0.515; MacKay table 10.0, 6.6, 3.3, 2.3, 1.0; submarine: 0.0227, 0.0231, 0.0235, 0.0238, 0.0242, five misses log2(64/59) = 0.1174, 32 misses 1, 48 misses 2, hit on 49 worth 4, shot 2 hit 5.9773, four-square check 0.415 + 0.585 + 1 = 2; weighing 0.817, 1.252, 1.500, 1.585, 1.483, 1.000, log2 24 = 4.585, 8:8:8 and 12:12:0; Ana 3, Ben 1, gap 2; stall H = 1.875 = EQ, old script 2.5, new H = best = 2.25; log2 3 = 1.585 (58.5 %), log2 8 = 3; Wenglish 2^15 = 32,768, 4 and 10 bits. Widget readouts (default values) match the text.

**Notebook.** Re-executed top to bottom with `nbenv` Python 3.12.12, numpy 2.5.5, matplotlib 3.11.2 (seed 20261207): every printed number equals `results.md` (including 100,000-day means 1.7499 and 2.2470, the estimation table, 1,050 random share vectors with gaps 0.0019 to 0.6301, 480 symbols with letter entropy 4.012; the text has no "j", so 26 distinct symbols). Cell numbers in `results.md` match the execution counts. README claims (eight exercises, each with hint and folded solution; 0.25 bits at n = 10; 12 of 24 left) are correct. Page and README hedge untested Python versions. Shannon 1951 p. 54 value 4.03 (27 letters, F1) and MacKay p. 32 value 4.11 are right.

**Quotes and pages.** All 70-odd verbatim quotes were matched by script to the source page text and then checked against the cited page numbers (offsets: MacKay printed = pdf − 12; Pierce − 16; Cover − 22; Shannon 1951 + 49; Mills − 7; Shannon 1948 and Gibson printed = pdf). All match, including Pierce p. 24 (hedge and scope), p. 38 ("by 60 per cent"; the "four times" slip), p. 40 (Hartley), p. 81 (ergodic), p. 267 (surprise); Shannon pp. 1, 2, 10, 11, 12, 14, 18; MacKay pp. 26, 32, 33, 66–74 (the "Intuitively" sentence, "we might conclude", "I think the submarine example"); Cover pp. 5, 13–15, 94–95 (eq. 5.61 is H ≤ EQ < H + 1); Gibson pp. 1, 3, 4, 6, 7, 11, 14, 15; Mills pp. 5, 6, 8, 9, 73, 212–215 (the list has seven items); Shannon 1951 pp. 54–55 (dash record, twin). Editions: Pierce is the 1961 Harper scan, Cover the 1991 first edition, MacKay version 7.2, Mills the 2000 paperback (copyright pages read).

**Hedges and "ours" labels.** "Our reading", "ours" and "(ours, run in code)" are present where the text goes beyond a source (hook "what was missing", rats framing, "guaranteed means in the worst case", four-rats statement, power-of-one-half sentence, grouping and weighing numbers, 12 : 12 : 0, bias, boundary 4 and 6, Mills move names and cases, research questions). MacKay's "Thus we might conclude", "I think", "Intuitively" are kept. Gibson's "associated with" is kept and the "bolder abstract" is shown beside the limits. "Never", "none", "only", "all" scan of the page: every use checked; the ones that matter hold (36 uses of "only"; "never sees" in the café is the café's own rule; "never balance" is MacKay p. 68; "with equality only when all are equally likely" is MacKay p. 33).

**Audio.** Same chapter ids and order as the page; all numbers equal the page (estimation table, weighing, quiz options, stall, 0.7 village); every hedge and "ours" marker I looked for is spoken. The differences are V2B-02, 03, 04, 06, 07, 10, 14 above.

**Transfer challenge and quizzes.** (a) 1, 2, 3, 4, 4; (b) 1.875 = H; (c) old script 2.5, new best 2, 2, 2, 3, 3 = 2.25 = H; quiz g1 (almost nothing, 0.0227), g2 (1.50), g3 (five), café checks (a) and (b), step 3 (2.25), step 4 (slightly more), roles check, layer-4 labels, and recall cards 1–8 are all correct.

## Suggested priority
Fix V2B-01 to V2B-03 (page and audio together), then the minors in a single pass. After that, re-run `check.mjs` and the audio-versus-page comparison for the changed chapters (`nothalves`, `answer`, `imagination`, `submarine`, `entropy`).
