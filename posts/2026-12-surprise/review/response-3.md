# Response to round 3 (S5 polish pass)

Main text: 7,044 → 7,033 words (about 250 words of fixes added, about the same cut). Notebook untouched (not re-run). Checks: `check.mjs` 9/9 OK; `build-post.mjs --public --owner` 0 math errors, 0 unmapped cites, no missing source entries; `test.mjs --inline` PASS; layer-2 scan (café section: formulas, symbols, H, EQ, bit, log, entropy, surprisal, independent) clean in page and audio.

## verify-3.md

| ID | Status | Where | Audio line (new) |
|---|---|---|---|
| V3-01 | changed | #hook: Pierce now gives both conditions ("chosen independently and each 'is equally likely to be selected'") | "Pierce says this count is acceptable only if successive symbols are chosen independently and each is equally likely to be selected." Recap: "Old measures counted possible messages, and they fit only independent, equally likely choices." |
| V3-02 | changed | #nothalves "Where it holds": "known" to Cover p. 94, "do not change" and "one word at a time" to MacKay pp. 100–101; "inverting every answer, or swapping two tickets of the same length" (Cover p. 97) | "It needs shares that are known and do not change, and one word at a time." / "The best card is not unique: inverting every answer, or swapping two tickets of the same length, gives another." |
| V3-03 | changed | #nothalves: "gap" is now the day's average minus H, 1.500 − 1.357 = 0.143; rain's own gap is 0.485 | "Rain is worth about half a question, but its ticket cannot be shorter than one, so its ticket is longer than its worth. Over the day, the card's average is above H by a small gap, about zero point one four: that gap is the price of whole questions." |
| V3-04 | changed | #recall card 4 ("For example … 0.3, 0.3, 0.2, 0.2 also need 2 … H is 1.971 (ours, run in code)"); numbers.md | "For example, with four equally likely words the best script averages two, and H is two too. Uneven shares such as zero point three, zero point three, zero point two and zero point two also need two on the best card, though H is one point nine seven one. That is ours, run in code." |
| V3-05 | changed (audio only) | #entropy audio | "Try only rain: the entropy is zero." (clause about Shannon and "no channel" removed) |
| V3-06 | changed | #box-nyquist: Pierce 1961, pp. 35–36 | none needed |
| V3-07 | changed | #imagination Move 1: "In our reading, the village has two extremes…" | "In our reading, the village has two extremes: a village where it always rains, with entropy zero, and four equal words, with entropy two." |

## verify-3b.md

| ID | Status | Where | Audio line (new) |
|---|---|---|---|
| V3B-01 | changed | same as V3-05 | "Try only rain: the entropy is zero." |
| V3B-02 | changed (audio recap) | #imagination recap now says only what Move 2 says | "In our reading of Mills, an issue is not a trouble multiplied: unlike even widespread trouble, it cannot very well be defined within everyday surroundings." |
| V3B-03 | changed | #roles: "(our reading)" after the strategy/script sentence | "The one who knows the secret, applying it, makes the string. That is our reading." |
| V3B-04 | changed | same as V3-06 | none |
| V3B-05 | changed | #answer 4(a): "'Uniquely decipherable' is theirs too (Cover and Thomas write 'uniquely decodable')" | "Uniquely decipherable is theirs too; Cover and Thomas write uniquely decodable. It means a run of answers can be cut into words in only one way." |
| V3B-06 | changed | same as V3-02 | same as V3-02 |
| V3B-07 | changed | same as V3-02 | same as V3-02 |
| V3B-08 | changed | #hook: the "engineers in the 1920s" sentence is gone; the paragraph starts "In 1928 Hartley measured…" | "In nineteen twenty-eight Hartley measured a message by how many different messages the sender could have picked." (opening of the chapter's second paragraph) |

## critic-3.md

| ID | Status | Where | Audio line (new) |
|---|---|---|---|
| C3-01 | changed | #nothalves "The rule is Huffman's": "Why the two rarest?" (they sit deepest with the longest tickets, so an extra question there falls on the fewest customers and costs least in total; the two longest tickets differ only in the last answer, MacKay p. 99) and "Why does a join add one question?" (a join is the question that separates the two groups; everyone in either group answers it). Both labelled ours | "Why the two rarest? They sit deepest on the card, with the longest tickets, so an extra question there falls on the fewest customers and costs the least in total. That is ours." and "Why does a join add one question to everyone under it? A join is the question that separates the two groups it merges, and every outcome in either group must answer it, so each gets one more. That is our reading too." |
| C3-02 | changed | same as V3-03 | same as V3-03 |
| C3-03 | changed | #nothalves: the 25-number paragraph is now a 4-row table (tickets, average, H) with short prose around it; "Where it holds" down from 6 to 4 citations | "On the page a small table lists the four days. On the village day the tickets are one, two, three, three, and the average is one point seven five, which is H. … On the zero point seven day … the average is one point five, and H is one point three six." (sum left to the page) |
| C3-04 | changed | #village: "independent: one day's word does not change the chances of the next day's" at first use; #entropy: "Let EQ stand for the expected number of questions" before E5 | "We take the days to be independent: one day's word does not change the chances of the next day's." / "Let E Q stand for the expected number of questions." |
| C3-05 | changed | #surprisal: Gibson "uniquely decipherable" sentence removed from step 2 (it stays in 4(a), where it is repeated) | "A share of zero point three is worth one point seven four. Step six returns to this." |
| C3-06 | changed | g1 option A now "Almost nothing, because a miss crosses off one square" (shortest of the four) | "Option one: almost nothing, because a miss crosses off one square." |
| C3-07 | changed | #hook: Hartley and Morse come first; the town is "The pain (ours)" afterwards | "In nineteen twenty-eight Hartley measured … Now the pain, and this is our own point." |
| C3-08 | changed | card-lab caption: "Finish a bad card and compare its average with the best." | none (widget) |
| C3-09 | changed | #imagination Move 1: share pushed toward 0, worth grows without bound, a forecast with share 0 is refuted by one snowfall (ours); Move 3: the closing assertion replaced by two different predictions (ours, not findings) | "A third extreme is a share pushed toward zero: the worth of that word grows without bound, and a forecast that gives snow share zero is refuted by one snowfall. That is ours." / "The two questions predict different things, ours, and neither is a finding. Under one model, the same snow should cost every reader the same effort. The journalist expects attention to follow what the news changes for each reader, whatever its surprisal." |
| C3-10 | changed | #surprisal: "For other shares the count of halvings is a fraction, and the formula below still gives it"; recall card 4 as V3-04 | "For other shares the count of halvings is a fraction, and the formula below still gives it." |
| C3-11 | partly | 7,033 words (not 6,800). Cut: "Who does what" to three sentences; the "Three checks" second half; the 4-rat sentence; the Pierce "aggravated" quote; MacKay additivity and "convincing case" sentences; MacKay 0.0230 aside; one Mills hedge; "information" gloss moved to the fold-out; Python 3.9 aside; the boundary-6 Cover sentence; the step-3 duplicate of the power-of-one-half result. The fixes above add about the same, and I did not cut any step. | The matching audio cuts, e.g. "A check. If the card began with matcha, most tickets would start with a no…" |

Also fixed (café loose phrase, critic note): "a card built for the old shares" is cut with the second check; the audio matches.
