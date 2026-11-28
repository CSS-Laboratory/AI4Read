---
name: post04-numbers
description: Every number in the text of post 04 and where it came from (check.mjs readout, a python rerun, the notebook run recorded in notebook/results.md, or a brief unit). Revised at S5 round 2 (28 November 2026). "Brief unit" numbers are quoted from the verified brief and were not recomputed here unless a row says so.
---
# Numbers, post 04

**How these were produced.** Widget readouts: `node site/ai4read/components/check.mjs posts/2026-12-surprise/src/content.html` (9 of 9 configs OK, with the new `card-lab`; the `switch` is skipped by the checker and is covered by `test.mjs`). Toy arithmetic was rerun in plain Python (`math.log2`, `heapq`). Notebook numbers are copied from `notebook/results.md`; the notebook was executed again after the round-2 revision with nbclient (Python 3.12.12, numpy 2.5.5, matplotlib 3.11.2, seed 20261207); every number matched the earlier runs except the 1,050 random share vectors of exercise 7, which are redrawn with seed offset +7 (gap EQ - H now 0.0033 to 0.8361; the page states no gap range). Numbers from the sources are listed with their brief unit and page.

## Widget readouts (check.mjs)

| Number | Where | Value | Origin |
|---|---|---|---|
| Village entropy and script average | step 3, `village-lab` default (weights 4, 2, 1, 1) | H = 1.750; script 1.750; labels 2.000; bars (share × surprisal) 0.500, 0.500, 0.375, 0.375, which add to 1.750 | check.mjs `village-lab` |
| All equal | step 3 | H = 2.000; script 2.250; bars 0.500 each | check.mjs `village-lab --values {1,1,1,1}` |
| Only rain | step 3 | H = 0.000; script 1.000; all bars 0 | check.mjs, `{1,0,0,0}` |
| Reversed | step 3 | H = 1.750; script 2.625 (the 2.625 is not quoted in the text) | check.mjs, `{1,1,2,4}` |
| Reversed village | step 3 check yourself | village script 2.625; H = 1.750; shares 1/8, 1/8, 1/4, 1/2 | check.mjs `village-lab --values {1,1,2,4}`; by hand 1/8 + 2/8 + 3/4 + 3/2 = 2.625 |
| Build the card, village day | step 6, `card-lab` preset 0 with `auto` | tickets 1, 2, 3, 3; average 1.750; best 1.750; H 1.750; worths 1, 2, 3, 3 | check.mjs `card-lab --values {"preset":0,"auto":true}` |
| Build the card, a bad chain card on the village day | step 6 | join the first two groups each time: tickets 3, 3, 2, 1; average 2.625 | check.mjs `card-lab --values {"joins":[[0,1],[0,1],[0,1]]}` |
| Build the card, the 0.7 day | step 6, preset 1 with `auto` | H = 1.357; tickets 1, 3, 3, 2 (the widget's tie-break; the page says which 0.1 word gets 2 is a tie); average 1.500; best 1.500; gap 0.143; worths 0.51, 3.32, 3.32, 3.32 | check.mjs `card-lab --values {"preset":1,"auto":true}` |
| Build the card, the equal day | step 6, preset 2 with `auto` | tickets 2, 2, 2, 2; average 2.000; H 2.000 | check.mjs `card-lab --values {"preset":2,"auto":true}` |
| Surprisal plot at p = 0.1 | step 2 | 3.3 questions | check.mjs `surprisal-plot` |
| Surprisal plot at 0.001, 0.01, 0.2, 0.5, 1 | step 2 (the text now names 0.001, 0.1 and 0.5; the others are on the slider) | 10.0; 6.6; 2.3; 1.0; 0.0 | check.mjs with `--values`; equal to MacKay 2003, p. 67 (brief unit 7) at his digits. The second curve (average over event and non-event) was removed at round 1. |
| First weighing, k = 1 to 6 | step 3 fold-out, `weigh-lab` (bars now max 1; readout says "remain on average") | 0.817, 1.252, 1.500, 1.585, 1.483, 1.000 bits; chances for 4 v 4: 0.333 each; for 6 v 6: 0.500, 0.500, 0.000; bits still unknown on average at 4 v 4: 3.000, at 1 v 1: 3.768 | check.mjs `weigh-lab --values {"k":n}`; python `log2` |
| Two forecasters | layer 4(c), boundary 4 | Ana 1/8: 3.00; Ben 1/2: 1.00; gap 2.00; sliders now min 0.005, step 0.005, so 0.125, 0.25 and 0.5 are on the grid (checked in headless Chromium: the slider reads 0.125) | check.mjs `forecast-lab`; Playwright |
| Submarine, hit on shot t | step 4, `sub-lab` | t = 1: misses 0, hit 6.0000; t = 2: misses 0.0227, hit 5.9773; t = 6: five misses 0.1174, last miss 0.0242, hit 5.8826; t = 33: misses 1.0000, hit 5.0000; t = 49: misses 2.0000 (last 0.0875), hit 4.0000; t = 64: misses 6.0000, hit 0.0000; total 6.0000 each time | check.mjs `sub-lab --values {"t":n}`; replaces the stepper table of the first draft |

## Toy arithmetic (ours, rerun in Python)

| Number | Where | Value | Origin |
|---|---|---|---|
| 14 answers for 8 customers, 1.75 each | layer 2; step 3 | 4·1 + 2·2 + 1·3 + 1·3 = 14; 14/8 = 1.75 | arithmetic; check.mjs 1.750 |
| Old way, two questions each | layer 2 | 2.000 | arithmetic (two halvings of four) |
| Village script on a uniform village | layer 2 answer (b); step 3 (as a pointer to section 2's check); boundary 2 | ¼(1+2+3+3) = 2.25 | check.mjs "all equal" (2.250); notebook exercise 3 simulated 2.2470 on 100,000 days |
| Eight values, three times the speed of two | Nyquist fold-out | log₂ 8 / log₂ 2 = 3 | brief unit 1 (ours, checked at S2); Pierce p. 38 says "four times", an apparent slip |
| Three values, 58.5% | Nyquist fold-out | log₂ 3 = 1.585 | brief unit 1; Pierce p. 38 says "60 per cent" |
| 2⁵ = 32, 2⁶ = 64, 2⁴ = 16, log₂ 32 = 5, log₂ 64 = 6 | step 1 | | arithmetic; Cover & Thomas 1991, p. 5 (H = log 32 = 5) |
| Rain 1, sun 2, wind 3, snow 3; strings 0, 10, 110, 111 | step 2 | | Shannon 1948, p. 18; Cover & Thomas 1991, p. 15 (brief unit 6) |
| Rain then snow: 1/2 × 1/8 = 1/16; log₂ 16 = 4; 1 + 3 = 4 | step 2 | | arithmetic (brief unit 3 toy idea, ours) |
| A share of 0.3 costs 1.74 | step 2 | log₂(1/0.3) = 1.7370 | python |
| Powers of one half (1/2, 1/4, 1/8, 1/16, …) cost whole numbers of questions | step 2 | | arithmetic (ours); replaces the false "only halves, quarters and eighths" |
| Share 1/16 costs 4 | recall | log₂ 16 | arithmetic |
| Grouping rule: 1 + ½ × 1.5 = 1.75; group entropy ½·1 + ¼·2 + ¼·2 = 1.5 | step 3 fold-out | | Shannon 1948, p. 10, Fig. 6; entropy 1.5 of (1/2, 1/4, 1/4) is MacKay 2003, p. 33 eq. 2.41 (brief unit 8); recomputed |
| 24 hypotheses; 3² = 9; 3³ = 27 | step 3 fold-out | | MacKay 2003, p. 68 (brief unit 5) |
| 4 v 4 split 8 : 8 : 8; 6 v 6 split 12 : 12 : 0 | step 3 fold-out | | 8 : 8 : 8 by hand and notebook exercise 7; 12 : 12 : 0 is our count (MacKay p. 68 says only "can never balance") |
| 1.585, 1.000, 4.585 bits | step 3 fold-out | log₂ 3; 1.000; log₂ 24 | brief unit 5 (ours, rerun at S2); python; notebook exercise 7 |
| 4 squares: 0.415, 0.585, 1.000; sum 2.000 | step 4 | log₂(4/3), log₂(3/2), log₂ 2 | python |
| Five misses: 0.0227, 0.0231, 0.0235, 0.0238, 0.0242; together log₂(64/59) = 0.1174 | step 4 check | | python; the fifth miss is the "last one" of `sub-lab` at t = 6 |
| MacKay prints 0.0230 for the second miss | step 4 check, notebook | 0.02308 truncated | brief unit 9 (truncation, confirmed on the page image at S2) |
| 0.0227, 6 (hit on first shot), 32 misses = 1, 48 = 2, hit on shot 49 (16 squares) = 4, total 6 | step 4 | | MacKay 2003, pp. 70–72 (brief unit 9); `sub-lab`; notebook exercise 3 |
| Wenglish: 2¹⁵ = 32,768 words; 15 bits a word; 3 per letter; a (0.0625) about 4 bits; z (0.001) about 10 | step 4 fold-out | | MacKay 2003, pp. 72–73 (brief unit 10) |
| Café string 1 1 0 (no, no, yes); toy TEA → 2 1 3 → TEA | step 5 | | by hand (ours) |
| 0.7 village: H = 1.357; lengths 1, 2, 3, 3; EQ* = 1.5; H + 1 = 2.357; gap 0.143; log₂(1/0.7) = 0.515; log₂ 10 = 3.32 | step 6 | | python; check.mjs `card-lab`; notebook exercise 7 (results.md, cell 16, Huffman trace) |
| MacKay's Example 5.18: even top-down split 2.53; Huffman 1.97 | step 6 "where it holds", lens 4 | | brief unit 24 (MacKay 2003, p. 100); reproduced by the fact-checker in round 2; not rerun here |
| Cover & Thomas Example 5.6.1 (2.3) and MacKay 5.15 (2.30, H 2.2855) | not on the page | | brief unit 24, listed so nobody adds them |
| Box of four cells: 0 (all in one) and 2 (equal) | lens 1 (toy removed at round 2; no longer on the page) | | arithmetic (brief unit 13 toy idea, ours) |
| Village 1.75 becomes 2 when its shares are made equal | layer 4(a) | | check.mjs "all equal" |
| Market stall: lengths 1, 2, 3, 4, 4; EQ 1.875 = H; after the change: old script 2.5, H 2.25, best lengths 2, 2, 2, 3, 3 cost 2.25 | layer 6 | | python; notebook exercise 7 |
| 200 messages in an inbox; 30 million listeners | layer 5 | | invented illustrations (ours), no data |
| H = 0 (always rain) and H = 2.000 (four equal words) | layer 5, move 2 | | check.mjs "only rain", "all equal" |

## Notebook numbers (notebook/results.md, second run, seed 20261207)

| Number | Where | Value | Frame |
|---|---|---|---|
| Estimation: mean plug-in entropy for n = 10, 30, 100, 1,000 | layer 4(c), boundary 5 | 1.504, 1.675, 1.725, 1.747 (results.md prints 1.5036, 1.6753, 1.7253, 1.7469) | 2,000 repeats of n village days; true entropy 1.75 |
| Gaps from 1.75 | boundary 5 | −0.246, −0.075, −0.025, −0.003 | absolute, in bits, against the true entropy 1.75; not relative |
| Village script average on 100,000 simulated days; labels; uniform | notebook only (not in the page text) | 1.7499; 2.0000; 2.2470 | sample means; expected 1.75, 2, 2.25 |
| Sample-text letter entropy | notebook only | 4.012 bits per symbol | one 480-symbol paragraph written for the notebook; biased low (exercise 5) |
| Bound on random share vectors | exercise 7 | holds for all 1,050; gap 0.0033 to 0.8361 (seed offset +7) | absolute |
| EQ - H on shares that are powers of 1/2; on the 0.7 village | exercise 7 | 0.0000, 0.0000, 0.0000; 0.1432 | absolute |

## Numbers quoted from sources (not recomputed here)

| Number | Where | Source |
|---|---|---|
| 1920s; 1928 (Hartley) in layer 1; 1924 (Nyquist) and "60 per cent" in the step 1 fold-out | layer 1; step 1 | Pierce 1961, pp. 35–40; Shannon 1948, p. 1 (brief units 1–2) |
| Huffman's rule: pp. 92–93, 94, 96–97, 101 (Cover & Thomas 1991); Algorithm 5.4, pp. 99–101 (MacKay 2003); Theorem 5.3.1 equality iff powers of 1/2, p. 86 | step 6, lens 4, recall | brief unit 24 |
| MacKay's table: 0.001 → 10.0; 0.01 → 6.6; 0.1 → 3.3; 0.2 → 2.3; 0.5 → 1.0 | step 2 | MacKay 2003, p. 67 (brief unit 7) |
| 1.75 expected number of questions | step 3 | Cover & Thomas 1991, p. 15 (brief unit 6) |
| Mills: city of 100,000; nation of 50 million employees; 15 million men; "30 millions" | layer 5 | Mills 1959, pp. 9, 215 (brief units 18, 21); hypothetical, not data; the brief says state no rate |
| Mills: pages 4–9, 73, 212–215; seven items | layer 5 | brief units 16–21 and the balance note |
| Gibson et al.: [104,105] (cited, not named in the text) | lens 2, recall | Gibson 2019, p. 11, p. 18 (brief unit 15) |

## Numbers the post does not state (so that nobody adds them)
Pierce's "15 per cent" for Morse (not used), Shannon's 69% and 77% from 1951 (not used, brief unit 14), MacKay's 4.11 and Shannon's 4.03 (dropped from notebook exercise 5 at round 2), any unemployment rate from Mills' example (the brief says not to state one), and Pierce's ten-versus-a-million sentence with its 3.32 and 19.93 bits (not used).

## Round-3 polish additions
| Number | Where | Value | Source |
|---|---|---|---|
| Step 6 table: village button 1, 2, 3, 3 → 1.750 (H 1.750); first two joined each time 3, 3, 2, 1 → 2.625; 0.7 day 1, 2, 3, 3 → 1.500 (H 1.357); equal day 2, 2, 2, 2 → 2.000 | step 6 table | as listed | check.mjs `card-lab` (`{"auto":true}`, `{"joins":[[0,1],[0,1],[0,1]]}`, preset 1 and 2 with `auto`); the 0.7 tie is the page's "which 0.1 word gets 2 is a tie" |
| Rain's ticket against its worth on the 0.7 day: 1 − 0.515 = 0.485 | step 6 | 0.485 | python: 1 − log2(1/0.7) = 0.4854 |
| The day's gap, EQ − H = 1.500 − 1.357 | step 6 | 0.143 | python: 1.5 − 1.35678 = 0.1432 (replaces the old "gap, 0.143" after rain's worth) |
| Recall card 4: shares 0.3, 0.3, 0.2, 0.2 | recall 4 | Huffman lengths 2, 2, 2, 2; EQ* = 2.000; H = 1.971 | python (heapq Huffman; H = sum p log2(1/p) = 1.97095) |
| Nyquist 1924 page | fold-out box-nyquist | Pierce 1961, pp. 35–36 (date on p. 35, formula on p. 36) | Pierce; verify-3 V3-06 |
