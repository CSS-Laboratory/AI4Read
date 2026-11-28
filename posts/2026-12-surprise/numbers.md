---
name: post04-numbers
description: Every number in the text of post 04 and where it came from (check.mjs readout, a python rerun on 2026-11-28, the notebook run recorded in notebook/results.md, or a brief unit). "Brief unit" numbers are quoted from the verified brief and were not recomputed here unless a row says so.
---
# Numbers, post 04

**How these were produced.** Widget readouts: `node site/ai4read/components/check.mjs posts/2026-12-surprise/src/content.html` (8 of 8 configs OK; the `switch` is skipped by the checker and was tested in the browser at 390 px). Toy arithmetic was rerun in plain Python (`math.log2`, `heapq`). Notebook numbers are copied from `notebook/results.md`; the notebook was executed once with nbclient (Python 3.12.12, numpy 2.5.5, matplotlib 3.11.2, seed 20261207). Numbers from the sources are listed with their brief unit and page.

## Widget readouts (check.mjs)

| Number | Where | Value | Origin |
|---|---|---|---|
| Village entropy and script average | step 3, `village-lab` default (weights 4, 2, 1, 1) | H = 1.750; script 1.750; labels 2.000; bars 1.00, 2.00, 3.00, 3.00 | check.mjs `village-lab` |
| All equal | step 3 | H = 2.000; script 2.250 | check.mjs `village-lab --values {1,1,1,1}` |
| Only rain | step 3 | H = 0.000; script 1.000 | check.mjs, `{1,0,0,0}` |
| Reversed | step 3 | H = 1.750; script 2.625 (the 2.625 is not quoted in the text) | check.mjs, `{1,1,2,4}` |
| Surprisal plot at p = 0.1 | step 2 | 3.3 questions; average over event and non-event 0.469 | check.mjs `surprisal-plot` |
| Surprisal plot at 0.001, 0.01, 0.2, 0.5, 1 | step 2 | 10.0 / 0.011; 6.6 / 0.081; 2.3 / 0.722; 1.0 / 1.000; 0.0 / 0.000 | check.mjs with `--values`; equal to MacKay 2003, p. 67 (brief unit 7) at his digits |
| First weighing, k = 1 to 6 | step 4, `weigh-lab` | 0.817, 1.252, 1.500, 1.585, 1.483, 1.000 bits; chances for 4 v 4: 0.333 each; for 6 v 6: 0.500, 0.500, 0.000; bits still unknown at 4 v 4: 3.000 | check.mjs `weigh-lab --values {"k":n}`; python `log2` |
| Two forecasters | layer 4(c), boundary 4 | Ana 1/8: 3.00; Ben 1/2: 1.00; gap 2.00 | check.mjs `forecast-lab` |
| Submarine stepper rows | step 5 | 0.0227; 0.0231 (total 0.0458); 30 misses 0.9542 (total 1.0000); 16 misses 1.0000 (total 2.0000); hit 4.0000 (total 6.0000) | python: sums of `log2((65-k)/(64-k))`, rounded to 4 decimals, not cut off; notebook exercise 3 prints the same (results.md, cell 12) |

## Toy arithmetic (ours, rerun in Python)

| Number | Where | Value | Origin |
|---|---|---|---|
| 14 questions in 8 days, 1.75 per day | layer 2; step 3 | 4·1 + 2·2 + 1·3 + 1·3 = 14; 14/8 = 1.75 | arithmetic; check.mjs 1.750 |
| Old way, two questions each | layer 2 | 2.000 | arithmetic (two halvings of four) |
| Village script on a uniform village | layer 2 answer (b); step 3; 4(c) | ¼(1+2+3+3) = 2.25 | check.mjs "all equal" (2.250); notebook exercise 2 simulated 2.2470 on 100,000 days |
| Eight values, three times the speed of two | Nyquist fold-out | log₂ 8 / log₂ 2 = 3 | brief unit 1 (ours, checked at S2); Pierce p. 38 says "four times", a slip |
| Three values, 58.5% | Nyquist fold-out | log₂ 3 = 1.585 | brief unit 1; Pierce p. 38 says "60 per cent" |
| 2⁵ = 32, 2⁶ = 64, 2⁴ = 16, log₂ 32 = 5, log₂ 64 = 6 | step 1 | | arithmetic; Cover & Thomas 1991, p. 5 (H = log 32 = 5) |
| Object 35 of 64 is 100011 | step 1 | | MacKay 2003, p. 70 (brief unit 4) |
| Rain 1, sun 2, wind 3, snow 3; strings 0, 10, 110, 111 | step 2 | | Shannon 1948, p. 18; Cover & Thomas 1991, p. 15 (brief unit 6) |
| Rain then snow: 1/2 × 1/8 = 1/16; log₂ 16 = 4; 1 + 3 = 4 | step 2 | | arithmetic (brief unit 3 toy idea, ours) |
| A share of 0.3 costs 1.74 | step 2 | log₂(1/0.3) = 1.7370 | python |
| Share 1/16 costs 4 | recall | log₂ 16 | arithmetic |
| Grouping rule: 1 + ½ × 1.5 = 1.75 | step 3 | | Shannon 1948, p. 10, Fig. 6; entropy 1.5 of (1/2, 1/4, 1/4) is MacKay 2003, p. 33 eq. 2.41 (brief unit 8); 1.5 recomputed |
| 24 hypotheses; 3² = 9; 3³ = 27 | step 4 | | MacKay 2003, p. 68 (brief unit 5) |
| 4 v 4 split 8 : 8 : 8; 6 v 6 split 12 : 12 : 0 | step 4 | | MacKay 2003, pp. 68, 70; counts by hand and by notebook exercise 4 |
| 1.585, 1.000, 4.585 bits | step 4 | log₂ 3; 1.000; log₂ 24 | brief unit 5 (ours, rerun at S2); python; notebook exercise 4 |
| 6 v 6: 0 bits about which ball; 1 bit about ball and direction | step 4 | | brief unit 5 (ours, checked at S2); notebook exercise 4 prints 0.000 and 1.000 |
| 4 squares: 0.415, 0.585, 1.000; sum 2.000 | step 5 | log₂(4/3), log₂(3/2), log₂ 2 | python |
| Five misses: 0.0227, 0.0231, 0.0235, 0.0238, 0.0242; together log₂(64/59) = 0.1174 | step 5 check | | python |
| MacKay prints 0.0230 for the second miss | step 5 | 0.02308 truncated | brief unit 9 (truncation, confirmed on the page image at S2) |
| 0.0227, 6 (hit on first shot), 32 misses = 1, 48 = 2, hit on shot 49 (16 squares) = 4, total 6 | step 5 | | MacKay 2003, pp. 70–72 (brief unit 9); python; notebook exercise 3 |
| Wenglish: 2¹⁵ = 32,768 words; 15 bits a word; 3 per letter; a (0.0625) about 4 bits; z (0.001) about 10 | step 5 fold-out | | MacKay 2003, pp. 72–73 (brief unit 10) |
| Café string 1 1 0; toy TEA → 2 1 3 → TEA | step 6 | | by hand (ours) |
| 0.7 village: H = 1.357; lengths 1, 2, 3, 3; EQ = 1.5; H + 1 = 2.357; gap 0.143; log₂(1/0.7) = 0.515 | step 7 fold-out; layer 4(c) | | python; notebook exercise 8 (results.md, cell 27) |
| Box of four cells: 0 (all in one) and 2 (equal) | lens 1 | | arithmetic (brief unit 13 toy idea, ours) |
| Market stall: lengths 1, 2, 3, 4, 4; EQ 1.875 = H; after the change: old script 2.5, H 2.25, best lengths 2, 2, 2, 3, 3 cost 2.25 | layer 6 | | python; notebook exercise 8 |
| 200 messages in an inbox | layer 5, move 1 | | invented illustration (ours), no data |
| H = 0 (always rain) and H = 2.000 (four equal words) | layer 5, move 2 | | check.mjs "only rain", "all equal" |

## Notebook numbers (notebook/results.md, one run, seed 20261207)

| Number | Where | Value | Frame |
|---|---|---|---|
| Estimation: mean plug-in entropy for n = 10, 30, 100, 1,000 | layer 4(c), boundary 5 | 1.504, 1.675, 1.725, 1.747 (results.md prints 1.5036, 1.6753, 1.7253, 1.7469) | 2,000 repeats of n village days; true entropy 1.75 |
| Gaps from 1.75 | boundary 5 | −0.246, −0.075, −0.025, −0.003 | absolute, in bits, against the true entropy 1.75; not relative |
| Village script average on 100,000 simulated days; labels; uniform | notebook only (not in the page text) | 1.7499; 2.0000; 2.2470 | sample means; expected 1.75, 2, 2.25 |
| Sample-text letter entropy | notebook only | 4.012 bits per symbol | one 480-symbol paragraph written for the notebook; biased low |
| Bound on random share vectors | exercise 8 | holds for all 1,050; gap 0.0019 to 0.6301 | absolute |

## Numbers quoted from sources (not recomputed here)

| Number | Where | Source |
|---|---|---|
| 1920s; 1924 (Nyquist); 1928 (Hartley); four values double the speed; three values "by 60 per cent" | layer 1 | Pierce 1961, pp. 35–40; Shannon 1948, p. 1 (brief units 1–2) |
| MacKay's table: 0.001 → 10.0; 0.01 → 6.6; 0.1 → 3.3; 0.2 → 2.3; 0.5 → 1.0 | step 2 | MacKay 2003, p. 67 (brief unit 7) |
| 1.75 expected number of questions | step 3 | Cover & Thomas 1991, p. 15 (brief unit 6) |
| Mills: city of 100,000; nation of 50 million employees; 15 million men; "30 millions" | layer 5 | Mills 1959, pp. 9, 215 (brief units 18, 21); hypothetical, not data; the brief says state no rate |
| Mills: pages 4–8, 73, 211–216; seven items | layer 5 | brief units 16–21 and the balance note |
| Gibson et al.: [104,105] = Hale (2001), Levy (2008) | lens 2 | Gibson 2019, p. 11, p. 18 (brief unit 15) |

## Numbers the post does not state (so that nobody adds them)
Pierce's "15 per cent" for Morse (not used), Shannon's 69% and 77% from 1951 (not used, brief unit 14), MacKay's 4.11 and Shannon's 4.03 (named only in the text of notebook exercise 5, as numbers from other texts), any unemployment rate from Mills' example (the brief says not to state one), and Pierce's ten-versus-a-million sentence with its 3.32 and 19.93 bits (not used).
