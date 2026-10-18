# Pedagogy critic, post 02 v2, round 3 (stage S5, final)

Read as Kunhao would: phone, B2-C1, every step wanted. Criterion 1 is not judged here. Scores are 1-5 for criteria **2** ladder, **3** clarity and English, **4** insight and lenses, **5** illustrations and interactives, **6** concision. "-" means nothing to score. Scored blind on the current draft; rounds 1-2 and the response were read only afterwards.

**Method.** I read the critic prompt, rubric, WRITING.md v0.6, charter, learner state, then all of `src/content.html` (main text, every fold-out, every widget config), then v2-critic-2 and v2-response-2. I re-ran by hand or in code: N_eff (2.703, 1.099, 3.257; N=2 check 1.33), tranche (0.370%, 5.185%, 10%, 634.5x, 0.0032%), the six-bank cascade (hand table rounds 0-3; capital x1.2 loses five, x1.25 loses three), the two-bank triangle (2 eps^2), N=10 ratio (2,756), trend-follower steps (-0.9, -0.51, -0.189; -2.30, -3.94), real-root range (m < 0.067 and m > 0.933), Ashby (V_O = 1; H(D) = 1.75), Granovetter swap (riot stops at 1). All agree with the text. Word count: main text **7,433** (cap 7,500), fold-outs 2,689. Build and render test: PASS (0 console errors, no overflow at 390 px, all eight readouts reproduce, 151 cites mapped, 0 unmapped).

## Scores

| Section | 2 Ladder | 3 Clarity | 4 Insight | 5 Illustr. | 6 Concision |
|---|---|---|---|---|---|
| 1 Hook | 4 | 4 | 4 | 4 | 4 |
| 2 Guess first | - | 4 | 4 | - | 5 |
| 3 Five jobs | 4 | 4 | 4 | 4 | 4 |
| 4 What AI agents add | 4 | 4 | 4 | 4 | 4 |
| 5 Lens 1 Check (Ashby; resist checking) | 4 | 4 | 4 | 5 | 4 |
| 6 Lens 2a Decide (N_eff; tranche) | 5 | 4 | 4 | 5 | 4 |
| 7 Lens 2b Cascades (Ladders 3-5) | 4 | **3** | 5 | 4 | **3** |
| 8 Lens 3 Declare (Searle) | 4 | 4 | 5 | 5 | 4 |
| 9 Lens 4 Answer (broker toy) | 5 | 4 | 4 | 4 | 4 |
| 10-12 Play, exercises, 3C | 4 | 4 | 4 | - | 4 |
| 13 Synthesis | - | 4 | 4 | - | 4 |

**Post level (minimum): 2 = 4, 3 = 3, 4 = 4, 5 = 4, 6 = 3.** The gate (at least 4 on every criterion) is **not met**, still on clarity and concision, and now both in one section (Lens 2b). Ladder, insight and illustrations pass. Two of round 2's three number-dense paragraphs are fixed (Ladders 2 and 5 now use tables and a fold-out); the repetition fixes were real but were paid for by new words elsewhere, so the main text grew from 7,325 to 7,433 words instead of shrinking by about 400.

## The three changes that would raise the post most

1. **Make Lens 2b readable and shorter (clarity and concision, one section).** Draw the square-and-triangle (one small diagram, 3 steps), then split the Ladder 4 "Formula" paragraph into three short lines; shorten Ladder 3's "What it means"; cut about 250 words from the section (G1, G2). This lifts both minima to 4.
2. **Make the possibility argument in short answer (a) say only what the lenses prove (G3).** The regress argument shows that the chain of checkers ends *somewhere*, not that it ends in a human-written rule. Say "today it ends in people's rules; Lens 1 shows why the end point matters; whether an AI-written rule could stand there is open".
3. **Finish the two small ladders that still skip a step:** Ashby's counting step (G4) and the "rough reason" for the tipping point in Ladder 5 (G6). Both are one sentence.

## Did it answer the reader's question?

**Possibility: mostly, with one weak inference.** The three senses are defined in section 3 and carried to (a) as run time, design time, stable and accepted. The run-time part is well supported (IMF, Check row). The design-time part says "two lenses give reasons to doubt it". Lens 1's reason is the regress, but Lens 1's own sentence says the chain "in today's markets ends in human institutions"; (a) drops "today's" and turns a description into an in-principle reason (G3). Lens 3's reason is Searle's criteria, but Lens 3 itself gives the strongest case *for* machine acceptance and calls the question open; (a) cites only the "against" side. The third sense ("stable and accepted: see (b) and (c)") is a pointer, not a verdict.

**Impact: yes, argued.** (b) has three mechanisms (coinciding failures, safer firms in a fragile system, checkers that need checkers), each tied to a lens and a toy, and a "who gains and who bears" sentence marked ours with a cited counter-scenario ("lower flash-crash risk"). "Power would tend to move to whoever writes the models and the rules" is still asserted; Ashby's variety gives a one-clause step that was suggested in round 2 and is not in the text (G5). Impact on ordinary people outside finance stays thin; acceptable for a finance worked case.

**Meaning: yes, honest about its stipulation.** (c) now states the logic in one line (some person is in those jobs, or nobody is and by our definition it is not a society) and names two defeaters. The logic is true by definition, and the text says so ("it rests on our definition"). Searle and Lupia-McCubbins are named before "The logic is then short" but the logic uses neither; "contest", a third clause of the definition, is used only in a defeater (G7).

**Consistency of (a)-(c) with the lenses.** (a) matches the Check and Run rows and Lenses 1 and 3. (b) matches Lenses 1-2 and uses "may/could" as the lenses do. (c) matches Lenses 3-4. One mismatch: the hook preview says "Declaring needs people who accept", which prejudges what Lens 3 and Prediction 3 call open (G8).

## Findings

Severity: **major** = fails a gate criterion for a section; **minor** = polish or a one-step fix.

### G1 (major, criterion 3) Lens 2b: three dense blocks, the geometry has no figure
- **Ladder 4 "Formula" paragraph** (about 90 words, 15 numeric tokens): "the triangle becomes a corner of an N-dimensional cube, with volume (Nc)^N/N!, and each unit of volume has chance (eps/c)^N ... For N = 3 the corner is a pyramid ... Check. N = 2 ... For N = 10 ..." It carries the generalisation, the N = 3 step, the check and the N = 10 number in one block.
- **Ladder 4 "Plan B" bullet**: square, line, triangle, area and chance in one sentence chain, with no drawing. On a phone the reader must build the picture alone. This is the post's only geometric argument without a figure, and round 2 already asked for one (F7).
- **Ladder 3 "What it means"** (about 100 words): the threshold, "the toy starts after the shared failure", Granovetter, and the Haldane-May liquidity caution with a quote and a gloss.
- **Fix:** (a) add a small `diagram` (square of side 2c, diagonal, shaded triangle; steps: the square, the line V1+V2 = 2c, the triangle with area 2c^2); (b) split the Formula paragraph into three lines: *N = 3 pyramid*, *general rule*, *Check at N = 2 and N = 10*; (c) cut the Ladder 3 Granovetter sentence (Exercise 4 carries it, and the forward reference "(Exercise 4)" sends the reader away from the section) and move the liquidity caution into one short clause. This gives clarity 4.

### G2 (major, criterion 6) Main text still full; round 2's -400 words did not happen
- Main text 7,433 (round 2: 7,325; target about 6,900). Lens 2b is the largest section at about 1,100 words (15% of the post).
- Remaining repeats: "each bank safer, the system more fragile" appears in the g4 question, the Ladder 4 mechanism, the Prediction 4 answer, "What it means", the Lens 2b sum, (b) and a recall card. The five-job verdict is in the preview, the section 3 table, (a), two Signs to watch and the layers fold-out.
- **Fix (about -250 words, no loss):** (1) shorten the Prediction 4 answer to the quote plus "No"; drop the second quote from p. 355 (it is in the Lens 2b sum idea anyway); (2) drop the IMF "de-risk" quote from Ladder 5 "What it means" (not used again) or move it to the fold-out; (3) in section 4, drop the Truth Terminal "who answers" sentence that restates Lens 4 and shorten the query-language paragraph (the diagram it feeds teaches only a minor point); (4) Signs to watch: keep three of five (those that are not already the verdict of (a)). This gives concision 4 and leaves about 300 words under the cap.

### G3 (minor, high priority, criterion 4) Short answer (a): design-time "no" rests on a description and on half of Lens 3
- (a) "Every automated checker needs a checker, so the chain ends in rules someone wrote (Lens 1)". The regress shows only that some last checker is unchecked; Lens 1's sentence says that "in today's markets it ends in human institutions that set the rules". Nothing says an AI-written rule could not stand at the end. If AI writes the end rule, design-time intervention is removed by definition.
- "declaring needs a 'we' that accepts (Lens 3)": Lens 3 gives the "for" case (language-like systems, dispositions) and says whether machines can join the "we" is open; Prediction 3's answer says "open".
- **Fix:** "Without people at design time: not shown, and not ruled out. Today the last checker is a rule people wrote (Lens 1), and a declared status needs a community that keeps accepting it; whether a network of AIs could be that community is open (Lens 3)." This keeps the verdict, labelled ours, and what would change it (an AI-written end rule that stays accepted).
- Also make the third sense a verdict in one line, e.g. "Stable and accepted: not without people, if (b) and (c) hold".

### G4 (minor, criterion 2) Ashby's law: the counting step is missing
- The ladder goes toy table, rule, "best plan leaves two end states", then "Formula (Ashby's law)". The step that makes the formula follow is not said: because no state appears twice in a column, each end state can come from at most one contract type per check, so with 2 checks at most 2 of the 4 types share an end state, so at least 4 / 2 = 2 end states; the base-2 logarithm turns "divide" into "subtract". WRITING §2: "a quoted formula still needs its climb". One sentence closes it, and it makes the 16-plans code check a confirmation rather than the evidence.
- **This is also the first sentence where a high-school reader could stall in sections 5-6:** "Ashby measures a set by its variety: the base-2 logarithm of its number of states". The reader has not been told why a logarithm appears. Add "(four states need 2 yes/no questions to name, so 2 bits)".

### G5 (minor, criterion 4) "Who gains" still has no step
- (b) "power would tend to move to whoever writes the models and the rules" is marked ours but has no argument. **Fix:** one clause: "(Lens 1: the side with more variety in its responses sets the terms for the rest)". Also mark "users may gain speed and lower costs" as ours without a source, or drop it.

### G6 (minor, criterion 2) Ladder 5: the reason for the tipping point is in the fold-out
- Main text gives the instance, mechanism, widget, table of next gaps and "Running the toy for many values of m shows the switch at m = 2/3". The reason is one sentence in the fold-out: "a swing keeps its size when Am = 1, at m = 1/A = 2/3". The argument needs it, so it belongs in the main text (WRITING §4), with one check: at m = 2/3 the push is 1.5 x 2/3 = 1, the full last move.
- Neighbouring point: the toy is trend-following; the text says shared models do not imply it. Good. Add why the lens still matters ("the question is how big m is, and whether a shared model raises it", ours).

### G7 (minor, criterion 4) Society definition: "contest" is used only as a defeater
- The definition has three clauses (rely on shared rules, contest them, find someone answerable); (c)'s logic uses two. Either add a clause ("and if people cannot contest the rules, the machines are declaring for them, and the 'we' in Lens 3 has become a machine") or reduce the definition to two clauses plus "contest" as an extra the second defeater adds.
- Searle and Lupia-McCubbins are named in (c) but the logic does not use them. Move the names into the logic: "declaring (Searle) and answering (Lupia and McCubbins) both need someone who can be affected by the result".

### G8 (minor) Preview over-asserts, quiz options, small items
- Hook preview: "Declaring needs people who accept" -> "Declaring needs a community that accepts; whether AIs could be one is open."
- Guess-first: the correct option is the longest in g1 (44 characters against 35, 36, 39), g3 (42 against 32, 38, 39) and g4 (39 against 14, 15, 35). Round 2 called them balanced; they are not (WRITING §5). Shorten the correct answers or lengthen two distractors per question. Correct answer is "b" in both g1 and g2.
- Section 3 "Decide" row packs three IMF quotes and two horizons into 100 words. Split: one line on trading, one on expectations.
- Lens 4 "Applied to AI": about 170 words, six citations and three ideas (knowledge, incentive routes, deployer liability). Split after "outside pressure on whoever deploys it" into a new paragraph.
- Ladder 1: the "Check" shares a paragraph with the worked numbers (25 numeric tokens: 10/(1+9x0.3) = 10/3.7 = 2.703 ... 2/1.5 = 1.33 ... 0.75 sigma^2). Put the check on its own line. The sentence "Both questions ask how much ten banks' errors overlap; the second measures it in a way we can count" is vague; say "Prediction 2 asked about the rare extreme. We now ask about the average forecast."
- "(ours)" count is 57. Where a whole paragraph is ours (the personhood paragraph; the "For" case), one label at the head is enough.
- The Arora paragraph in Lens 1 ("planted dense subgraph problem ... no tractable algorithm") is the first place a high-school reader is lost on terms: "tractable" and "conjecture" are not glossed. Add "(no one knows a fast method)".

## Per-criterion detail for scores below 5

- **Ladder (4):** Lens 1 (G4); Lens 2b (G6; the general-N volume step is asserted, though N = 2 and N = 3 are derived and the text says so); Lens 3 has no numbers (acceptable, its diagram applies the formula to the bill and then to the AI token as a check); Hook, sections 3-4 and 10-12 introduce no formula.
- **Clarity (4 or 3):** G1 for Lens 2b; G8 for sections 3, 6 and 9. Short sentences, defined terms (futures, tranche, CDO, option, capital, variety, SupTech, liquidity shocks, disturbance, IMF and BIS expansions) are now in place before use. No internal jargon.
- **Insight (4):** Lens 1 has the regress claim that (a) over-reads (G3); Lens 2a and 2b both make "sameness" points (N_eff and Haldane-May), which the 2b sum partly acknowledges ("three routes: thresholds, sameness and feedback"). Say in the 2a sum that 2a is *how many* independent views and 2b is *what happens when they fail together*; Lens 4 has a good counter-case but the premise "an AI cannot be jailed or shamed" remains ours and unexamined beyond the deployer remedies.
- **Illustrations (4):** Lens 2b lacks the square-and-triangle (G1); Lens 4 and the Hook are text and tables (adequate); the Lens 4 toy is a three-row table with no interactive, which is enough for a decision table.
- **Concision (4 or 3):** G2.

## Checks the prompt asked for

**Number density.** Over the five-number guideline: Ladder 1 "For ten banks" paragraph (25 numeric tokens), Ladder 4 Formula paragraph (15), Ladder 4 Plan B bullet (15, partly symbols), and the Play answers (12; acceptable in a fold-out). Ladder 2 and Ladder 5 are fixed (table plus separate meaning). Hook paragraphs now have 4-5 numbers each. Lens 1 is at the limit and fine.

**Repetition.** Partly fixed: the section 13 job table, the Mercer paragraph and the main-text Granovetter detail are gone. Not fixed: the "safer banks, fragile system" point (7 places), the "human in the loop" point (6 mentions), the five-job verdict (G2). Net main text +108 words.

**Short answer: argued, consistent.** (b) and (c) are argued; (a) is argued for run time and weak for design time (G3). Consistency with lenses is good apart from the preview (G8).

**Do all ladders climb?**

| Ladder | Instance | Question | Mechanism | Worked numbers | Formula | Check | Meaning / limit |
|---|---|---|---|---|---|---|---|
| Ashby (Lens 1) | yes | yes | yes, but no counting step | yes | yes | yes (2-1 = 1; 13.29 / 9.29) | yes |
| Ladder 1 N_eff | yes | yes | yes | yes | derived | yes (N=2, rho=0.5) | yes (cap 1/rho) |
| Ladder 2 tranche | yes (fold-out) | yes | yes | table | yes | yes (0.370 / 5.185 / 10.000) | yes (634.5x) |
| Ladder 3 six banks | yes | yes | yes | hand table | threshold rule | yes ("6 of 6 in 3 rounds") | yes (capital x1.5, lgd 1) |
| Ladder 4 Haldane-May | yes | yes | yes | two banks, derived | N^N eps^N / N! | yes (N=2, N=10) | yes (extreme by design) |
| Ladder 5 trend | yes | yes | yes | table | in fold-out | in fold-out | yes (breaker; trend-following only) |
| Lens 4 broker | yes | yes | yes | 3-row table | theorem in words | yes (take away the incentive) | yes (success vs strict success) |

Every ladder climbs. Weak rungs: Ashby counting step (G4), Ladder 5 reason and check in the fold-out (G6).

**Standalone.** Yes. "Post 02" is only a label; no reference to another post or toy; the English section repeats no earlier phrase by name.

**Widgets.**

| Widget | Reader can do the mechanism? | Edge case that teaches | Prose quotes readout correctly |
|---|---|---|---|
| Ashby stepper and lab | Yes | standard menu 10^2; AI supervisor +5 bits | Yes (13.29, 9.29, 6.64) |
| Seller diagram, tree diagram (fold-outs) | Stepper only | same rule, different price (7/4 vs 3/2) | Yes |
| N_eff lab | Yes | huge crowd 0.3: 3.257 | Yes |
| Bayes lab (fold-out) | Yes | 10 copies: 0.999999 | Yes |
| Waterfall diagram, tranche lab (fold-out) | Yes | safe loans p = 0.02: 634.5 | Yes (0.0032%, 2.000%) |
| Six-bank hand table and cascade | Yes, tap to fail | capital x1.5; lgd 1 | Yes; Play answers verified |
| Haldane-May lab | Yes (N = 2 gives 2) | N = 20 | Yes (2,756) |
| Trend iterate | Yes | breaker clamps, feedback stays | Yes (-0.9, -0.51, -0.189; -2.30, -3.94) |
| May lab (fold-out) | Yes | m = 8, alpha = 0.3 | Yes |
| Status, LLM diagrams | Stepper only | ghost nodes for the AI case | n/a |
| (missing) two-bank square | - | - | - |

**Lens sections.** All five lenses give "Adds", "Does not explain" (Lens 1 and 2b with "ours" limits), a link type and a job label. Link types are honest (Lens 1 same-math plus analogy; Lens 2a same-math; Lens 4 admits the theory is touched only through incentives). The §13 tension (Lens 1 against Lens 2b, standardise the form only) is the post's best cross-lens insight. 3C links in section 12 are concrete (N_eff for LLM annotators and simulated agents, "who checks the checker", Searle for crisis trust); the Collaboration card is a question only.

## Round-2 findings: status

| Round 2 | Status |
|---|---|
| F1 number density (Ladders 2, 5, 1) | Ladders 2 and 5 fixed; Ladder 1 check still in one block; Ladder 4 now the densest (G1, G8) |
| F2 undefined terms | Fixed (disturbance, SupTech, liquidity shocks, IMF, BIS, success in the toy) |
| F3 repetition, -400 words | Partly: jobs table, Mercer, Granovetter cut; net +108 words (G2) |
| F4 possibility rests on status | Met for run time; design-time argument over-reads Lens 1 and 3 (G3) |
| F5 society chain, "contest", preview | Chain stated in (c); preview still over-asserts; "contest" half-treated (G7, G8) |
| F6 who gains, Lens 4 premise | Counter-case added; Ashby clause not added (G5) |
| F7 two-bank derivation | Derivation and N = 3 step added; figure not added (G1) |
| F8 broker check | Fixed (tests the toy) |
| F9 first stalling sentence (Ashby table rule) | Fixed (plain gloss); next stall is G4 |
| F10-F11 | Met |

## What is good (keep)

- The hook is now short, with few numbers and a careful "the paper does not test it".
- The run-time and design-time term box turns the reader's phrase into a testable claim and the Check row shows it.
- Ladder 3 (do it by hand, then let the widget agree) and the two-bank Haldane-May derivation with its stated assumption.
- The §13 "Where the lenses disagree" with its link type, and the (c) verdict with its defeaters.
- Lens 4's check now tests the toy ("take away the incentive").
