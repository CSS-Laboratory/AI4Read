# Audit of Lens 2b and section 13 after round 3 (criteria 3 clarity, 6 concision)

Scope: `src/content.html`, `id="lens-cascade"` and `id="answer"`, against `v2-critic-3.md` (G1-G8), rubric criteria 3 and 6, WRITING v0.6. Not a full review; criteria 1, 2, 4, 5 not scored. Word counts from `scripts/wordcount.py`: main text 7,484 (cap 7,500; round 3 had 7,433), Lens 2b 1,075 words, section 13 670 words.

## Scores

| Section | 3 Clarity | 6 Concision |
|---|---|---|
| Lens 2b (Cascades) | **4** | **4** (low; see R2) |
| 13 Synthesis | **4** | **4** |

Both sections now reach the gate threshold. Lens 2b moved up from 3 and 3. The concision score is borderline: the section shrank by only about 25 words, and the post as a whole grew by 51 words.

## Were the requested fixes made?

| Round-3 fix | Status | Evidence |
|---|---|---|
| G1a Square-and-triangle figure | Done | `<figure class="illus">` after the Plan B bullets. Geometry checks: square side 2c, shaded triangle V1+V2<2c (area 2c^2), plan A square c x c. Caption states "twice the area, twice the chance". It is one static picture, not the 3-step diagram asked for; acceptable. |
| G1b Split the dense "Formula" paragraph | Mostly | "Formula" (2 sentences + display), the source-attribution line and a separate "Check" paragraph. The N = 3 pyramid is now only the parenthesis "(for three, a pyramid)". The general-N step is still asserted (see R1). |
| G1c Shorten Ladder 3 "What it means" | Done | Granovetter sentence and the "(Exercise 4)" forward reference are gone. The liquidity-shock caution stays (one sentence, with a gloss). |
| G2 Prediction 4 answer to one quote plus "No" | Done | Single p. 353 quote. |
| G2 Drop the IMF "de-risk" quote from Ladder 5 | Done | Not in the section. |
| G2 Signs to watch: five down to three | Done | Three items in section 13. |
| G2 Net -250 words, "leaves about 300 under the cap" | **Not met** | Post is 16 words under the cap, not 300. Lens 2b is about 25 words shorter. I did not check section 4, which G2 also named. |
| G3 Short answer (a), design-time claim | Done | Now "not shown, and not ruled out ... in today's markets it ends in rules people wrote (Lens 1) ... Whether machines could do the accepting that declaring needs is open (Lens 3)", plus what would show it. Keeps the verdict, labelled ours. |
| G3 Third sense as a verdict | **Not done** | Still "Stable and accepted: see (b) and (c)". |
| G5 "Who gains" step | Done | "since the regulator with more variety sets the terms for the rest (our extension of Ashby's law)". The step is thin (R4). |
| G6 Ladder 5 reason for m = 2/3 in main text | Mostly | Sentence "Roughly: each step the chasers repeat 1.5m times the last move ... keeps its size when 1.5m = 1" added. No numeric check (at m = 2/3 the push is 1.5 x 2/3 = 1). The same sentence still appears in the fold-out. |
| G7 "Contest", Searle and Lupia-McCubbins inside the logic | Done | (c) now uses Searle for contest-by-withdrawing-acceptance and Lupia-McCubbins for knowledge and incentive; the logic then uses both. |
| G8 Preview over-asserts | Done | "whether machines can supply either is the open part." |

## Remaining problems

| # | Severity | Where | Problem | Fix |
|---|---|---|---|---|
| R1 | moderate (criterion 3; holds the 4) | Ladder 3 formula | \(w_{ij}\) is never defined, and neither is the direction of the loan. WRITING §2 step 4 says every symbol is read aloud in words. The text says "loss rate" for \(\lambda\), the widget says "loss given default"/"lgd", and \(\kappa\) appears only in the formula. | One clause: "\(w_{ij}\) = what bank j lent to bank i"; use "loss rate" in the widget label or add "(loss given default)" once. |
| R2 | moderate (criterion 6) | Lens 2b | Still the largest section (1,075 words, 14% of the post). About 110-130 words are cuttable without loss: the liquidity-shock sentence (about 45), the "twice as likely" result stated four times (bullet, caption, paragraph, Check), the Ladder 5 table that duplicates the fold-out table, and the opening "compared banks to food webs, carefully" which sets up only the fold-out. The post total is 16 words under the cap, so any later addition breaks the 7,500 limit. | Cut those four items. |
| R3 | moderate (criterion 3) | Ladder 4 "Formula" | "a corner of an N-dimensional cube ... volume (Nc)^N/N!" is the hardest sentence in the post for a high-school reader, and the general-N step is only asserted. | Say "for three assets the same idea gives a pyramid with volume (3c)^3/6 and chance 4.5 eps^3", then "for N the pattern is (Nc)^N/N!". |
| R4 | minor | 13 (b) | "power would tend to move to whoever writes the models and the rules, since the regulator with more variety ..." jumps from model-writers to regulators; one sentence of about 80 words. | Split into two sentences and say who "the regulator" is in this case. |
| R5 | minor | 13 (a), (c) | (a) is about 170 words with three parentheses; (c) uses "delegation", "agent" and "incentive" without a gloss. | Split (a) at "Without people at design time"; gloss "agent" as "the one who acts for you". |
| R6 | minor | 13 (b) | The Harari sentence ("Harari's extreme case runs further ...", about 35 words) is the only person-centred line left (WRITING §0); it could move to the fold-out. | Cut or fold. |
| R7 | minor | Ladder 3 "What it means" | The liquidity-shock sentence is not linked to anything in the toy. | Cut (see R2) or tie to the "lgd 1" preset. |
| R8 | minor | Ladder 4 vs Lens 2a | Ladder 4's sameness point partly overlaps Lens 2a (WRITING §0 "one point, one ladder"). It does add the "each bank safer, system more fragile" turn, so keep it. | Say in the 2a sum that 2a is "how many independent views" and 2b "what happens when they fail together" (G-detail from round 3). |

## Remaining major issue

None. There is no major issue on criteria 3 or 6 for these two sections. R1 and R2 are the two to fix before the gate is called, because they are the likeliest reasons a judge would drop either score back to 3.
