# Fact check, S5 round 1 (independent checker B): "How much is a surprise worth?"

Checked: `src/content.html` (all sections, fold-outs, quizzes, recall cards, widget labels and readouts, Sources), `audio-script.md`, `post.json`, `notebook/01_surprise_entropy.ipynb`, `notebook/results.md`, `notebook/README.md`.
Against: `sources/` (pdftotext pages, page images for doubtful lines) and `source-brief.verified.md` (with Addendum S2b). Not read: `self-review.md`, `numbers.md`, `review/verify-1.md`.

## Counts

| Severity | Count |
|---|---|
| Critical | 0 |
| Major | 4 |
| Minor | 25 |

Layer 2 (section `cafe`, 691 words): scanned for formulas, symbols, abbreviations, "bit", "log", "entropy", "surprisal". None found. No layer-2 finding.

## Major findings

### V1B-01 (major) "Only halves, quarters and eighths cost a whole number of questions"
- Location: section `surprisal`, paragraph "What it does not say": "Only halves, quarters and eighths cost a whole number of questions." Repeated in `fails`, boundary 6: "whole numbers of questions only for halves (step 7)". The audio script repeats the sentence.
- Source and page: our own reasoning (E2 and Cover & Thomas 1991, p. 15, with MacKay 2003, p. 33 for equality).
- What the source says: E2 gives a whole number for every share that is a power of 1/2. The post's own market stall (section `turn`) has two shares of 1/16 that cost exactly 4 questions.
- Severity: major (false universal "only", contradicted inside the post).
- Fix: write "Only shares that are powers of one half (1/2, 1/4, 1/8, 1/16, ...) cost a whole number of questions", in the page, boundary 6 and the audio.

### V1B-02 (major) "Reading effort" for Gibson's "language processing effort"
- Location: section `fails`, exercise "Check yourself · layer 4", statement (iii) "Reading effort follows surprisal." with the answer "hedged as 'is associated with'"; section `recall`, card 8: "Which claim about reading effort is empirical, and who makes it?"; the audio script repeats both (chapters `fails` and `recall`).
- Source and page: Gibson et al. 2019, p. 11 (pdf 11); Brief S2 unit on Gibson, trap (b) and open item 3.
- What the source says: "Since language processing effort is associated with predictability [104,105]". It is one premise in a paragraph about redundant gender marking.
- Severity: major (scope changed from "language processing" to "reading", and "predictability" to "surprisal" with "follows"; the brief and the post's own fold-out say we never write that surprisal predicts reading time on this review).
- Fix: say "language processing effort ... is associated with predictability" in the recall card and in statement (iii) (for example "Processing effort is associated with predictability"), in page and audio.

### V1B-03 (major) Audio adds a claim the page does not make
- Location: audio chapter `nothalves`, recap: "Equal to H only when every share is a power of one half."
- Source and page: not on the page (page step 7 says only "Do not take that as a rule"); the fact would be Cover & Thomas 1991 ch. 5, not read by the post.
- What the source says: Cover & Thomas p. 15 and eq. (5.61): the best average "lies between H(X) and H(X) + 1". No source page the post cites states an equality condition.
- Severity: major (audio says something extra, with an "only", unsourced and not labelled ours).
- Fix: delete the sentence, or add it to the page with a citation or an "ours" label and then keep both versions equal.

### V1B-04 (major) Audio adds an attribution to Gibson and colleagues
- Location: audio chapter `lenses`, lens two: "Gibson and colleagues use surprisal for colour words, word length and, through other work, processing."
- Source and page: Gibson et al. 2019, p. 6 (word length), p. 7 (colour), p. 11 (processing).
- What the source says: p. 6, word length depends on "a word's probability in context"; p. 11, "language processing effort is associated with predictability". Only p. 7 uses the word surprisal, for the colour score.
- Severity: major (extra in the audio, and stronger than the page, whose lens-2 text and fold-out keep the three statements apart and hedged).
- Fix: delete the sentence, or say what the page says: colour difficulty is a surprisal, word length follows predictability in context, effort "is associated with predictability".

## Minor findings

### V1B-05 (minor) Audio drops "apparent" about Pierce's "four times"
- Location: audio chapter `village`: "Pierce's page thirty-eight says eight values give four times the speed, which is a slip."
- Source: Pierce 1961, p. 38 (checked on the page image). The page fold-out says "an apparent slip".
- Fix: say "an apparent slip" in the audio.

### V1B-06 (minor) "his list of values shows only seven"
- Location: `village`, fold-out `box-nyquist`: "Pierce's 'four times' is an apparent slip, and his list of values shows only seven".
- Source: Pierce 1961, p. 38 (page image): the first list is "0, 1, 2, 3, 4, 6, 7" (seven); the second list ("+7, +5, +3, +1, -1, -3, -5, -7") has eight.
- Fix: write "his first list of values shows only seven (the second has eight)".

### V1B-07 (minor) Audio drops "Intuitively" in MacKay's sentence
- Location: audio chapter `village`: "MacKay writes that the best questions successively divide the sixty-four possibilities into equal sized sets, and six questions suffice."
- Source: MacKay 2003, p. 70: "Intuitively, the best questions successively divide the 64 possibilities into equal sized sets. Six questions suffice." (the page keeps "Intuitively").
- Fix: add "Intuitively," to the audio.

### V1B-08 (minor) Wrong page for the telescoping product
- Location: `submarine`: "This is MacKay's telescoping product (MacKay 2003, p. 71)".
- Source: MacKay 2003, eq. (4.14) is on p. 72 (pdf 84), not p. 71.
- Fix: cite p. 72 (or pp. 71-72).

### V1B-09 (minor) "Never balance" and 12 : 12 : 0 cited to p. 70
- Location: `weighing`: "With six on each pan the pans can never balance, and the split is 12 : 12 : 0 (MacKay 2003, p. 70)".
- Source: MacKay 2003, p. 68: "these two sets of balls can never balance". The 12 : 12 : 0 split is our count, not on p. 70.
- Fix: cite p. 68 for "never balance" and mark 12 : 12 : 0 as ours.

### V1B-10 (minor) "so" joins two passages in Shannon 1951
- Location: `roles`: the twin "will 'respond in the same way when faced with the same problem', so 'the reduced text can be considered to be an encoded form of the original'" (p. 55).
- Source: Shannon 1951, p. 55: the second sentence begins "To put this another way" and follows the paragraph that replaces the twin with a table of N-gram predictions.
- Fix: write "Shannon then adds" instead of "so".

### V1B-11 (minor) "are chosen independently" is not Shannon's wording on p. 18
- Location: `village` intro: "Shannon assumes symbols 'are chosen independently'" (no page); audio: "Shannon assumes successive symbols are chosen independently".
- Source: Shannon 1948, p. 18: "successive symbols being chosen independently" (boundary 3 quotes "chosen independently", which is right). The words "are chosen independently" are Pierce's (p. 40).
- Fix: quote "being chosen independently" with "Shannon 1948, p. 18".

### V1B-12 (minor) Mills p. 215: "Nowadays at least" dropped
- Location: `box-mills-counting`: "He also says he would never count or measure anything before he had played with its elements in an imagined world".
- Source: Mills 1959, p. 215: "Nowadays at least, I should never think of actually counting or measuring anything, before I had played with each of its elements".
- Fix: add "nowadays at least" (and the audio is silent on this fold-out, so no change there).

### V1B-13 (minor) Audio: Mills "he still strives"
- Location: audio chapter `imagination`: "He adds that he still strives to gain and to maintain a sense of proportion."
- Source: Mills 1959, p. 214: "you will strive to gain and to maintain a sense of proportion" (advice to the reader, not a report of his own habit). The page says "while still striving".
- Fix: say "He adds that you should still strive".

### V1B-14 (minor) Lens 2: "the only lens where the number is tested against behaviour"
- Location: `lenses`, lens 2, "Adds"; the audio repeats it.
- Source: Gibson et al. 2019, p. 11 says processing effort "is associated with predictability", as a premise in an argument about gender marking; the studies are unseen (the post says so).
- Severity reason: the "only" claim rests on unseen studies, and the page cites no test of surprisal itself.
- Fix: write "the one lens where the post cites a reported link to behaviour (unseen studies)".

### V1B-15 (minor) Gibson p. 7: the "average" is the average colour score
- Location: fold-out `box-lens-limits`: "compute a listener's difficulty as 'the surprisal of the color, given the word', and the average is 'the optimal number of yes-no guesses ...'".
- Source: Gibson et al. 2019, p. 7: the colour score is a product of a production factor and a comprehension factor (the surprisal); "The resulting average color score is the optimal number of yes-no guesses".
- Fix: add that the score also weighs how likely the speaker is to use the word (the production factor).

### V1B-16 (minor) "A script is right only for the shares it was built for"
- Location: `entropy`: "A script is right only for the shares it was built for."; widget caption (village-lab); audio.
- Source: our reasoning; Cover & Thomas p. 15.
- What the numbers say: lengths 1, 2, 3, 3 are also the best whole-question script for shares 0.4, 0.3, 0.2, 0.1 (Huffman, rerun in Python); its average equals H only for the exact shares 1/2, 1/4, 1/8, 1/8.
- Fix: write "its average equals H only for its own shares, and it can cost more on others".

### V1B-17 (minor) Bias explanation
- Location: `fails`, boundary 5: "Biased low for small samples, because a rare word that never appears gets share 0."
- Source: our computation (notebook exercise 6, rerun: mean 1.5036, 1.6753, 1.7253, 1.7469).
- Why: the table is right, but the cause is incomplete. The estimate is also low at n = 1,000 (-0.003), when every word appears; plug-in entropy is biased low for all n because the observed shares are noisier than the true ones and entropy is concave.
- Fix: write "mainly because a rare word that never appears gets share 0, and because noisy shares lower the entropy on average (ours)".

### V1B-18 (minor) Recall card 7 and boundary list: independence "needed before an entropy means anything"
- Location: `recall`, card 7: "Name two assumptions needed before an entropy means anything. Any two of: known shares; stable shares; independent days; enough data".
- Source: our reasoning; Shannon 1948, p. 18 uses independence for the example source; E4 itself needs only the shares.
- Fix: ask "Name two assumptions the village model makes".

### V1B-19 (minor) Recall card 4: "when would the best script average exactly 2?"
- Location: `recall`, card 4 (and audio): "For four equally likely words."
- Source: our reasoning, rerun in Python: shares 0.3, 0.3, 0.2, 0.2 also give a best script of lengths 2, 2, 2, 2, average exactly 2.
- Fix: answer "For example, for four equally likely words."

### V1B-20 (minor) Sources list: bibliographic data not in the files
- Location: `sources`.
- (a) Gibson et al., "23(5), 389-407": the file is a pre-proof ("Vol. xx, No. yy"); it shows only the DOI 10.1016/j.tics.2019.02.003. The volume and pages cannot be checked in `sources/` (they are correct to my knowledge).
- (b) Shannon 1951: "Pages cited are the printed pages 54-56", but only pp. 54 and 55 are cited.
- Fix: add the DOI for Gibson and say "(volume and pages from the publisher, not checked in our copy)"; change 54-56 to 54-55.

### V1B-21 (minor) Pierce "history"; Hartley without the logarithm
- Location: `hook`: "Pierce, in his 1961 history" (audio also); "a message is measured by how many different messages the sender could have picked".
- Source: Pierce 1961 is "Symbols, Signals and Noise: The Nature and Process of Communication", a general introduction (ch. II is the history). Pierce, p. 40 (page image): Hartley defined H "as the logarithm of the number of possible sequences".
- Fix: write "in his 1961 book"; and say Hartley's measure is a function (the logarithm) of the number of possible messages, in one plain clause.

### V1B-22 (minor) MacKay's game: "64 objects", "object 35 of 64"
- Location: `village`, step 1: "one of 64 objects is chosen" and "MacKay's object 35 of 64 gives 100011".
- Source: MacKay 2003, p. 70, Example 4.3: "an integer x between 0 and 63"; "35 => 100011".
- Fix: say "one of the 64 integers 0 to 63" and "the number 35".

### V1B-23 (minor) Equation labels out of order
- Location: `entropy`, `weighing`, `submarine`, `nothalves`: labels appear as E4, E5, E9, E7, E8, E6.
- Fix: renumber in reading order, or note that numbers follow the outline.

### V1B-24 (minor) "Fair yes/no question" is never defined
- Location: lede, term box "Worth", step 1 ("One answer of a fair yes/no question is one bit"), widget `weigh-lab`; audio.
- Source: MacKay, p. 70: each answer "has Shannon information content log2(1/0.5) = 1 bit" (a question whose answers are equally likely).
- Fix: one sentence at first use: "fair means that yes and no are equally likely".

### V1B-25 (minor) Unlabelled gloss on "guaranteed"
- Location: `village`, after E1: "'Guaranteed' means in the worst case, not on average."
- Source: MacKay 2003, p. 74 gives the quote but no gloss; the gloss is reasonable but ours.
- Fix: add "(ours)".

### V1B-26 (minor) MacKay p. 26: referent of "this"
- Location: `lenses`, lens 4: "He warns that 'this is not yet a globally held view'".
- Source: MacKay 2003, p. 26: "the reader is warned that this is not yet a globally held view": "this" is "a Bayesian approach makes sense", while the page's preceding quote ("you cannot do inference without making assumptions") is the Bayesian advocates' view.
- Fix: write "He warns that the view that a Bayesian approach makes sense 'is not yet a globally held view'" (the 25-word limit is met).

### V1B-27 (minor) Pierce p. 24 and p. 81: context and condition
- Location: term box (`hook`): "Pierce warns that the everyday sense, knowledge, creeps in and confuses the discussion"; `fails` 2: "In Pierce's simplest case the chances 'must not change with time'".
- Source: Pierce 1961, p. 24: the confusion is "aggravated when more than one meaning of information creeps into a discussion" of physics and communication theory. P. 81: "must not change with time if the source is to be ergodic".
- Fix: add "in the debate with physics" to the first; add "if the source is to be ergodic" to the second.

### V1B-28 (minor) Notebook README and cell 1: untested claims
- Location: `notebook/README.md`: "Other versions should give the same numbers, because every random draw is seeded"; "Python 3.9 or later" (README, notebook cell 1 and page section `turn`).
- Source: `results.md` says "on the same versions"; the reference run is Python 3.12.12, numpy 2.5.5 only. numpy does not guarantee that `Generator` streams are the same across versions.
- Fix: say "the reference run used ...; other versions may differ in the last digits", and "Python 3.9 or later (untested; the run used 3.12)".

### V1B-29 (minor) Pierce quote on art used as an anchor for messages
- Location: `imagination`, Move 1: "Pierce's one sourced anchor: 'We can be surprised repeatedly only by contrast with that which is familiar'" (p. 267).
- Source: Pierce 1961, p. 267 is in ch. XIII (information theory and art), about audiences and artists ("to be appreciated art must be in a language familiar to the audience"). The quote is verbatim (page image checked: the OCR "constrast" is a text-layer error).
- Fix: add "writing about art" before the quote.

## Numbers rerun (all correct, no finding)

Text numbers recomputed in Python and compared: 1.75 (14/8); 2.000; 2.25; 1.74 and 0.515 (share 0.3 and 0.7); log2 3 = 1.585, 58.5 per cent, log2 8 = 3; 4.585, 3.000 left, 1.585, 1.000; 8 : 8 : 8 and 12 : 12 : 0; weighing k = 1..6 = 0.817, 1.252, 1.500, 1.585, 1.483, 1.000; submarine rows 0.0227, 0.0231, 0.0458, 0.9542, 1.0000, 2.0000, 4.0000, 6.0000; four-square check 0.415, 0.585, 1.000; five misses 0.0227, 0.0231, 0.0235, 0.0238, 0.0242 and log2(64/59) = 0.1174; 0.7 village H = 1.357, EQ = 1.5, gap 0.143, bound 2.357; stall 1.875, 2.5, 2.25; MacKay table values (p. 67) 10.0, 6.6, 3.3, 2.3, 1.0; 2^15 = 32,768, 3 bits a letter, 4 and 10 bits for a and z; quiz answers g1, g2, g3.
Widgets (`check.mjs`, 8 of 8 OK): p = 0.100 gives 3.3 and 0.469 (MacKay 0.47); village 1.750 / 1.750 / 2.000; weighing 4 v 4 gives 1.585 and 3.000 remaining; Ana 3.00, Ben 1.00, gap 2.00. Preset values (all equal, only rain) agree with the text.
Notebook: re-executed top to bottom with the stated environment; every printed number equals `results.md` (including 1.7499, 2.2470, estimation table, 1,050 vectors, gap 0.0019 to 0.6301, 4.012 bits, 26 distinct symbols because only "j" is missing). Estimation table in the page equals the notebook.

## Checked and found correct (selection)

- Every verbatim quote in the page was matched by script against the source text (whitespace, dashes and hyphenation normalised) and, where the layout was doubtful, on the page image: Pierce pp. 23-24, 24, 38, 40, 80, 81, 264, 267; Shannon 1948 pp. 1, 2, 10, 11, 12, 14, 18; Shannon 1951 pp. 54-55; MacKay pp. 26, 32, 33, 66-74, 84; Cover & Thomas pp. 5, 13-15, 94-95; Gibson pp. 1, 3, 4, 6, 7, 11, 14, 15; Mills pp. 5-9, 73, 212-215. Printed page numbers agree with the offsets in the brief (Mills printed = pdf - 7). All quotes are at most 25 words (the longest, Mills p. 8, is exactly 25).
- Hedges kept on the page: Mills "advice, not findings", "I believe", "Perhaps the most fruitful"; MacKay "Thus we might conclude", "I think"; Gibson "is associated with", "approximates", "likely reflects"; Shannon "no way necessary" and the Theorem 2 justification.
- "Ours" labels: cups-and-rats, Hartley pairing, "Guess first" frames, 6 v 6 about which ball, toy walk-through, extremes and numbers in Mills' moves, research questions, bias table.
- Mills used as a dated source, "men" in quotes, seven items and four move names ours, hypothetical unemployment example, "information" not Shannon's sense.
- Shannon 1948 uses neither "surprisal" nor "information content" (whole-text search, confirmed); MacKay never mentions Hartley (whole-text search, confirmed).
- Sources list: titles, authors, publisher, edition and pagination notes agree with the files (Cover & Thomas 1991, Pierce 1961 first edition, Mills 2000 Oxford printing with Gitlin afterword, Shannon reprint pp. 1-55, Gibson pre-proof pp. 1-19), apart from V1B-20.
- `post.json` summary and tags agree with the page; `date` 2026-12-07 matches the eyebrow.
- Audio script: same chapter ids and order as the page, numbers equal the page (estimation table, weighing values, quiz options, stall), apart from V1B-03, 04, 05, 07, 11, 13, 14.
- "Never", "none", "only", "all" scan of the page: all other uses checked and acceptable (the "never" in the fold-out about reading time is the post's own sentence and holds only if V1B-02 is fixed).
