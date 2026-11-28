---
post: 2026-12-surprise
stage: S4 revision after S5 round 2
author: writer (fresh agent)
answers: review/verify-2.md (V2-01 to V2-16), review/verify-2b.md (V2B-01 to V2B-16), review/critic-2.md (C2-01 to C2-18)
date: 2026-11-28
---

# Response to round 2

**Totals.** 49 findings answered (V2: 15, V2-15 being only a note; V2B: 16; C2: 18): **48 changed, 1 partly (C2-13), 0 not changed.** Main text is now **7,044 words** (cap 7,500; it was 6,844). The new step 6 with the `cardlab` widget costs about 260 words net; we cut the hook history, lens 1's toy, the old lens 3, the layer-5 caveat, a separate Move 4 and several quotes, but we did not reach the ideal of "below 6,844" (see the self-review).

**What moved.** Step numbers are as in round 1. Lenses are now four (the old lens 3, communication theory, is folded into step 5, where the café roles are mapped onto Shannon's diagram), so the old lens 4 and 5 are now lens 3 and 4. Boundaries are now seven (the old 6 is split into 6 and 7). Layer 5 now starts with extremes (Move 1), then trouble and issue (Move 2), then another discipline's eyes (Move 3); comparison stays inside research question 2. In the notebook the exercises were reordered: 1 surprisal and entropy, 2 whose model, 3 the village script (simulation), 4 the submarine, 5 your own text, 6 estimation bias, 7 the best script (Huffman), 8 the weighing (optional). Section ids in locations: hook, cafe, village (step 1), surprisal (2), entropy (3), submarine (4), roles (5), nothalves (6), answer, lenses, fails, imagination, turn, recall, sources.

**Audio.** Every audio change is quoted in its entry. A script check confirmed that each quoted audio line is present in `audio-script.md`.

---

## verify-2.md (Opus)

**V2-01 · changed.** lenses, lens 4 (was lens 5): “For one experiment, MacKay’s tentative conclusion (“we might conclude”) is that it is most informative when its outcomes are equally likely (p. 70). A whole search differs: splitting every group as evenly as possible is not always the fastest script (MacKay p. 100; Cover & Thomas p. 97), and step 6’s rule is (Cover & Thomas p. 101).” “Does not explain” now begins “a whole search built by even splits (step 6)”. Step 6 states the trap with MacKay’s numbers (Example 5.18, 2.53 against 1.97, p. 100) and says “Equal chances are the right aim for one question (MacKay p. 70), not for a whole card.” *Audio (lenses):* “For one experiment, MacKay's tentative conclusion, we might conclude, is that it is most informative when its outcomes are equally likely. A whole search differs. Splitting every group as evenly as possible is not always the fastest script, and step six's rule is.” *Audio (nothalves):* “The rule builds from the rarest up. Splitting the words into two nearly equal groups, again and again, is not always best. In MacKay's seven-outcome example five point eighteen, it gives two point five three, against one point nine seven for the best card.”

**V2-02 · changed.** answer, (a): ““Uniquely decipherable” means a run of answers can be cut into words in only one way; scripts in which no string is the start of another, like our card, are one kind of these (Cover & Thomas 1991, pp. 80–81).” Step 2 keeps its own, consistent gloss. Step 6 says Huffman's result is "among scripts in which no string is the start of another". *Audio (answer):* “Uniquely decipherable means a run of answers can be cut into words in only one way. Scripts in which no string is the start of another, like our card, are one kind of these.”

**V2-03 · changed.** imagination, Move 2: “An issue, he says, “unlike even widespread trouble”, “cannot very well be defined” within everyday surroundings; in his unemployment example, “The very structure of opportunities has collapsed” (pp. 8–9).” The collapse sentence is now tied to the example. Unit 18 in the brief was already corrected by the meta-manager; we did not edit the brief. *Audio (imagination):* “An issue, he says, unlike even widespread trouble, cannot very well be defined within everyday surroundings. In his unemployment example, he writes, the very structure of opportunities has collapsed.”

**V2-04 · changed.** The rule is credited to Huffman in step 6 (“The rule is Huffman’s … Cover and Thomas give this simple algorithm (pp. 92–93), prove that it gives the shortest average length among scripts in which no string is the start of another, as on our card: “Huffman coding is optimal” (p. 101), and say the best series of questions is the one the Huffman code gives (p. 94). MacKay states it as his Algorithm 5.4 (p. 99). Only the worked 0.7 day is ours.”), in lens 4, and in recall card 8. The conditions of unit 24 are on the page: shares known and fixed, one word at a time, “best” means shortest average, not unique, and the top-down trap. Notebook exercise 7 now says: “This is Huffman's rule (Cover & Thomas 1991, pp. 92-94 and 101; MacKay 2003, p. 99); only the worked 0.7 village is ours.” *Audio (nothalves):* “The rule is Huffman's. Join the two rarest outcomes, adding their shares, give everything in the group one more question, and repeat until one group is left. Cover and Thomas give this simple algorithm. They prove that it gives the shortest average length among scripts in which no string is the start of another, as on our card: Huffman coding is optimal.” and “Only the worked zero point seven day is ours.”

**V2-05 · changed.** `forecast-lab`: `min` 0.005, `step` 0.005 (0.125, 0.25 and 0.5 are on the grid), bar `max` 8 (the new minimum is worth 7.64). Checked with the real `widgets.js` in headless Chromium at 390 px: the slider reads 0.125, and the preset “Ana 1/8, Ben 1/2” gives 3.00, 1.00, gap 2.00 (`test.mjs` passes). The meta-manager's earlier fix of the presets is kept. No audio change needed: *Audio (fails)* still reads “Ana says one eighth, Ben one half. Ana is surprised by three, Ben by one. The gap is two.”

**V2-06 · changed.** fails, boundary 6: “a real barista can update the shares as the day goes on, ask a question that is on no card, or ask what the customer meant. With the shares known, choosing the next question from the last answer is already what a written card does (Cover & Thomas p. 94).” The “stops at the first yes” aside is gone. *Audio (fails):* “The café breaks: a real barista can update the shares as the day goes on, ask a question that is on no card, or ask what the customer meant. With the shares known, choosing the next question from the last answer is already what a written card does.”

**V2-07 · changed.** cafe: the general description no longer says “stops at the first yes”; it stays only on the new card. *Audio (cafe):* “The customer answers them on the ticket, one after another, and every answer costs one second of the queue's time.”

**V2-08 · changed.** Step 2 café line: the order's worth is not the ticket length except for shares 1/2, 1/4, 1/8, … (ours). Step 3 café line: “H: the day’s average worth. Where the shares are halves it is also the day’s average ticket length under the best script; step 6 shows the general case.” *Audio (entropy):* “H is the day's average worth. Where the shares are halves it is also the day's average ticket length under the best script. Step six shows the general case.”

**V2-09 · changed.** submarine café line: “A no on the ticket is worth 0.0227 of a question, a yes six. For any one customer, the worths of her answers add up to the worth of her drink, whatever order the card asks in (ours; the same chain of fractions as E8).” *Audio (submarine):* “A no on the ticket is worth zero point zero two two seven of a question. A yes is worth six. For any one customer, the worths of her answers add up to the worth of her drink, whatever order the card asks in. That is ours: the same chain of fractions as equation eight.”

**V2-10 · changed.** Step 3 “What it means” cites it: “For the best script of whole questions, the average equals H exactly when every share is a power of one half (Cover & Thomas 1991, p. 86); step 6 gives the general case.” Step 6 states and cites it again, next to E9. The g2 answer now says “no card of whole questions can reach it here”, which rests on that cited condition (shares 0.7, 0.1 are not powers of one half). *Audio (entropy):* “For the best script of whole questions, the average equals H exactly when every share is a power of one half. Step six gives the general case.”

**V2-11 · changed.** *Audio (cafe):* “If all four drinks sold equally, the clever card would save nothing, and a card built for the old shares would do worse than the plain board.”

**V2-12 · changed.** `weigh-lab` readout: “Of the 4.585 bits needed, {left} remain on average.” (3.768 remain on average for 1 v 1.) The bar `max` is 1 (V2B-12).

**V2-13 · changed.** turn: “(Python 3.9 or later should work; we did not test it)”.

**V2-14 · changed.** The card now hangs “by the counter” (not “by the cash register”, so “till” and a second “cash register” are both gone; the owner's “cash register’s record” stays as the source of the shares). *Audio (cafe):* “The same card hangs on the wall by the counter and on the wall in the back room: a list of yes or no questions in a fixed order.”

**V2-15 · not a finding.** The checker listed it only to say the Mills scope slip is counted under V2-03.

**V2-16 · changed.** Notebook exercise 4 (the submarine, was 3), hint: “Each numerator cancels the next denominator (the post's E8), so the product of the miss ratios is one fraction and you can also check with a single `math.log2`.” Exercise 7 (the best script, was 8): the solution now prints “EQ = H exactly when every share is a power of 1/2 (Cover & Thomas 1991, p. 86)” and the gaps (0.0000 for the three dyadic examples, 0.1432 for the 0.7 village). The notebook was re-executed with nbclient (0 errors) and `results.md` regenerated from that run only.

## verify-2b.md (Sonnet)

**V2B-01 · changed.** As V2-04. The page no longer says “ours and not from our sources”.

**V2B-02 · changed.** As V2-02.

**V2B-03 · changed.** *Audio (imagination), recap:* “In Mills' terms, trouble and issue differ by where the cause lies. Our hypothesis, not a finding: for a ranking that prices messages under its own model, part of the cause may lie in whose model prices them. Extremes and scale, and other disciplines' eyes, point to the same question: whose model prices a surprise?” “Only when” is gone and the hypothesis is stated as a hypothesis.

**V2B-04 · changed.** *Audio (submarine), recap:* “A hit on the first shot is worth six, a first miss about two hundredths, and the total for finding the target is always six.”

**V2B-05 · changed.** fails, boundary 2: Pierce's chances “must not change with time if the source is to be ergodic” (p. 81) “(ergodic, our gloss: its long-run averages do not depend on which run you watch)”. We did not cite Pierce p. 59 because the 1961 and Dover pagination differ. *Audio (fails):* “Ergodic, in our gloss, means its long-run averages do not depend on which run you watch.”

**V2B-06 · changed.** imagination intro: “His “information” (p. 5) means, in our reading, facts (“this Age of Fact”), not Shannon’s sense (Pierce p. 24).” *Audio (imagination):* “His word information means, in our reading, facts. He calls his time this Age of Fact. It is not Shannon's sense.”

**V2B-07 · changed.** submarine check: “MacKay prints 0.0230 for the second, which matches cutting the digits off (our reading); we round.” *Audio (submarine):* “MacKay prints zero point zero two three zero for the second, which matches cutting the digits off, in our reading. We round.” The same wording is in `results.md`.

**V2B-08 · changed.** As V2-09.

**V2B-09 · changed.** fails, boundary 5: “Biased low for small samples, because noisy observed shares lower the entropy on average (ours); the extreme case is a rare word that never appears and gets share 0.” The notebook exercise 6 hint now says “Noisy observed shares lower the entropy on average; the extreme case is a rare word you never saw, which gets share 0.” *Audio (fails):* “The estimate is biased low for small samples, because noisy observed shares lower the entropy on average. That is ours. The extreme case is a rare word that never appears and gets share zero.”

**V2B-10 · changed.** hook: Hartley saw that E is chosen more often than Z, “and that this should govern the lengths of Morse signals, if messages are to be sent most swiftly” (Pierce p. 40). *Audio (hook):* “Hartley himself saw that E is chosen more often than Z, and that this should govern the lengths of Morse signals, if messages are to be sent most swiftly.”

**V2B-11 · changed.** Sources: “Our copy is an article-in-press proof (marked “ARTICLE IN PRESS”, TICS 1894, 19 pages)”. `requests.md` item 1 follows.

**V2B-12 · changed.** `weigh-lab` bars `max` 1.

**V2B-13 · changed.** imagination, Move 3: “A psycholinguist asks whether language processing effort is associated with how predictable an element is in context, a link Gibson and colleagues state (p. 11).” *Audio (imagination):* “A psycholinguist asks whether language processing effort is associated with how predictable an element is in context, a link Gibson and colleagues state.”

**V2B-14 · changed.** As V2-10 (the entropy “What it means” line is now in the audio).

**V2B-15 · changed.** As V2-16 (exercise 4 hint).

**V2B-16 · changed.** `post.json` tags are now “Information theory” and “Communication theory”. The post has one Bayesian lens but no causal content, so “Bayesian & causal inference” is dropped; we did not invent a tag that the site's list may not have.

## critic-2.md

**C2-01 · changed.** Step 3: the 2.25 sentence is removed from the E5 paragraph (it points to “the equal-shares day of section 2’s check”). The predict-first exercise is new and not answered above it: with shares reversed (rain and sun 1/8, wind 1/4, snow 1/2), what does the village script cost and what is H? Answer 2.625 and 1.750 (check.mjs `village-lab` “reversed”). *Audio (entropy):* “Check yourself. Predict first, then press reversed in the widget: rain and sun are now an eighth of the days each, wind a quarter, snow a half. What does the village script cost a day now, and what is H? Why is the script not at H?” The widget preset “0.7, 0.1, 0.1, 0.1” is also removed (C2-11).

**C2-02 · changed.** Step 6 is rebuilt as a ladder: guess; the instance with the `cardlab` widget (village day, 0.7 day, equal day), what happens in each, the rule with its Huffman citation and its conditions and trap, then E9 and the check on the three days, then the guess answer and the café line. The reason joining the rarest is best is Cover and Thomas's proof (§5.8), which we say we do not reproduce; our picture, “a long ticket costs least where few customers go”, was cut for length.

**C2-03 · changed.** Layer 2's parts list now has “A ticket’s length: how many answers are on it. Always a whole number.” and “An order’s worth: how much news the order carries, counted in questions … For the four drinks above, worth and ticket length agree; section 3 shows when they do not.” Step 2 names the worth (E2) and says it matches the ticket length only for shares 1/2, 1/4, 1/8, …; a sentence before the plot says why 3.3 is not a ticket. E4 and E9 café lines use worth and ticket length. *Audio (cafe):* “a ticket's length, how many answers are on it, always a whole number; an order's worth, how much news the order carries, counted in questions, so that a rare order is worth more than a common one; for the four drinks above, worth and ticket length agree, and the next section shows when they do not;” *Audio (surprisal):* “h of x is the order's worth, in questions. A ticket's length is whole, so it can equal the worth only for shares one half, one quarter, one eighth and so on. That is ours.”

**C2-04 · changed.** hook: the Nyquist and Hartley paragraph is cut from about 190 to 132 words with one history sentence on Nyquist moved to the fold-out; the independence quote moved to the fold-out; the forward pointer is now “(a logarithm of that number; step 1 explains)”; g1's options each carry a “because” clause (also C2-15); “fair” is no longer in the guess. *Audio (hook):* “In nineteen twenty-eight Hartley measured a message by how many different messages the sender could have picked. In fact he used a logarithm of that number, which step one explains.”

**C2-05 · changed.** The `cardlab` widget (step 6) lets the reader do the mechanism: join two groups, see the ticket and worth columns, press “Join the two rarest”, try a bad join (2.625 on the village day). `check.mjs`: village day 1.750 = H; bad chain 2.625; 0.7 day 1.500 against H 1.357; equal day 2.000. `test.mjs` checks the tap and the rule. *Audio (nothalves):* “On the page, a widget lets you tap two groups to put them under one question. Every word in the two groups gets one more question on its ticket.”

**C2-06 · changed.** E3: “a log turns a product into a sum, because \(2^a\times 2^b = 2^{a+b}\): multiplying the crowds adds the halvings.” *Audio (surprisal):* “because two to the a times two to the b is two to the a plus b: multiplying the crowds adds the halvings.”

**C2-07 · changed.** E4 café line: “Σ: go through the drinks, each weighted by its share.” *Audio (entropy):* “The sigma means go through the drinks, each weighted by its share.”

**C2-08 · changed.** As V2-02: one gloss in layer 3 and a consistent, weaker one in layer 4(a).

**C2-09 · changed.** Ergodic glossed (V2B-05). E9 café line: “EQ*: the day’s average under the best card the owner could write; H is the day’s average worth.” *Audio (nothalves):* “E Q star is the day's average under the best card the owner could write. H is the day's average worth.”

**C2-10 · changed.** The old lens 3 (communication theory) is folded into step 5 (“Mapped onto Shannon’s diagram (our mapping, a structural analogy): the customer is the transmitter, …”), lens 1 loses its toy and keeps two sentences, and a one-paragraph “Compared (ours)” sets lens 2, 3 and 4 side by side. Four lenses remain. *Audio (lenses):* “Compared, in our reading. Lens two is a claim to test. Lens three says a share belongs to a believer. Lens four takes the shares as fixed and the average as the thing to minimise.” *Audio (roles):* “Shannon's diagram has the same roles, in our mapping, a structural analogy. The customer is the transmitter, the ticket the signal, and the barista the receiver.”

**C2-11 · changed.** The preset “0.7, 0.1, 0.1, 0.1” is removed from `village-lab`; the 0.7 day is now the `cardlab` preset in step 6, after the guess. *Audio (entropy):* the sentence “A last button sets shares zero point seven …; keep it for step six.” is deleted.

**C2-12 · changed.** Fold-out “Shannon’s twin game”: “The encoding side is the predictor together with whoever holds the original text: the predictor guesses, the holder says right or wrong, and the record is written.” (fold-out; the audio only names it).

**C2-13 · partly.** Changed: the section now opens with the 30-million extreme (Move 1), then trouble and issue (Move 2) with the link “which is E2 with a single model”; the Pierce art quote is gone; the edition caveat moved to the Sources entry for Mills; “comparable cases” (Mills p. 215) is named in research question 2. Not changed: comparison is not a separate move (we tried a Move 4 and cut it for length), and research question 1 still says “We have not checked the prior work”, because that is true and the question is offered as an invitation. *Audio (imagination):* “Move one: extremes and inverted scale. … Now invert the scale. Mills asks: what would pre-literate villages look like with populations of thirty millions?” and “Our case, ours. One reader misses an important message among her two hundred, and blames herself: a trouble.”

**C2-14 · changed.** Notebook: exercise 2 is now “whose model” (the easiest after 1), the optional weighing is last (8), “unigram” is defined in the task, the MacKay 4.11 and Shannon 4.03 numbers are dropped, exercise 7 (the best script) hints at `rng.dirichlet(np.ones(n))` for the random share vectors and credits Huffman. Seed offset for exercise 7 is +7; its random gap range is now 0.0033 to 0.8361. README, cell 0, “Where to go next” and `results.md` follow.

**C2-15 · changed.** g1 option 1 is “Almost nothing, because one miss rules out only one square of 64”; all four options now carry a “because” clause. *Audio (hook):* “Option one: almost nothing, because one miss rules out only one square of sixty-four.”

**C2-16 · changed.** “Move the slider to choose which shot hits, and read the readout.” The café claim is stated for any one customer, with “(ours; the same chain of fractions as E8)”.

**C2-17 · changed.** Step 1 café line: “The rats are a ticket filled in all at once: five rats, five answers (ours).” The “guaranteed means in the worst case” gloss now comes before the MacKay quote. *Audio (village):* “The rats are a ticket filled in all at once: five rats, five answers. That is ours.” and “For other N, think of the worst case, the most questions you could ever need. That is ours.”

**C2-18 · changed.** Recall card 7 is now the two-forecaster card (boundary 4), card 8 is “How do you build the best card for any shares, and what does it cost?”; the Gibson-citation card and the plain assumptions card are dropped (the forecaster card tests an assumption). *Audio (recall):* “Seven. Two forecasters see the same snow. Why do they get different numbers, and which assumption of the village breaks?” and “Eight. How do you build the best card for any shares, and what does it cost?”
