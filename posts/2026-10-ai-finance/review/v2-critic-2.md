# Pedagogy critic, post 02 v2, round 2 (stage S5)

Read as Kunhao would: phone, B2-C1, every step wanted. Criterion 1 is not judged here. Scores are 1-5 for criteria **2** ladder, **3** clarity and English, **4** insight and lenses, **5** illustrations and interactives, **6** concision. "-" means there is nothing to score. Scored on the current draft on its own merits; round 1 was read only afterwards, to check which findings were met.

**Method.** I read the critic prompt, rubric, WRITING.md v0.5, charter and learner state, then all of `src/content.html` (main text, fold-outs, every widget config), then v2-critic-1 and v2-response-1. I re-ran the numbers in code: Ashby (min 2 end states over all 16 plans), N_eff (2.703, 1.099, 3.257), tranche (0.37%, 5.185%, 634.5 times), the six-bank cascade (6 of 6 at x1, 3 of 6 at x1.25 and x1.5; the round table and all play answers), trend-follower roots (0.548, 1.002, 1.162; real roots at m = 0.95), Haldane-May (N = 10 ratio 2,755.7; the N = 2 triangle gives 2 eps^2). All agree with the text. Word count: main text **7,325** (cap 7,500), fold-outs 2,490. Build and render test: PASS (0 console errors, no overflow at 390 px, all eight readouts reproduce, cites 152 mapped). The tooling truncation noted in round 1 is fixed.

## Scores

| Section | 2 Ladder | 3 Clarity | 4 Insight | 5 Illustr. | 6 Concision |
|---|---|---|---|---|---|
| 1 Hook | 4 | 4 | 4 | 4 | 4 |
| 2 Guess first | - | 4 | 4 | - | 5 |
| 3 Five jobs | 4 | 4 | 4 | 4 | 4 |
| 4 What AI agents add | 4 | 4 | 4 | 4 | 4 |
| 5 Lens 1 Check (Ashby; resist checking) | 4 | 4 | 4 | 5 | 4 |
| 6 Lens 2a Decide (N_eff; tranche) | 5 | 3 | 4 | 5 | 4 |
| 7 Lens 2b Cascades (3 ladders) | 4 | 3 | 5 | 4 | 3 |
| 8 Lens 3 Declare (Searle) | 4 | 4 | 5 | 4 | 4 |
| 9 Lens 4 Answer (broker toy) | 4 | 4 | 4 | 4 | 4 |
| 10-12 Play, exercises, 3C | 4 | 4 | 4 | - | 4 |
| 13 Synthesis | - | 4 | 4 | 4 | 3 |

**Post level (minimum): 2 = 4, 3 = 3, 4 = 4, 5 = 4, 6 = 3.** The gate (at least 4 everywhere) is **not yet met**, on clarity (number density) and concision. Both are cheap to fix. Round 1 was 3/3/3/4/3, so ladder and insight now pass.

Evidence for the minima:
- **Clarity, 3** (Lens 2a, Lens 2b). Ladder 2 "Worked numbers" paragraph holds about 12 numbers: "exactly 3 defaults has chance \(4\times0.1^3\times0.9=0.0036\); 4 defaults, \(0.1^4=0.0001\) … 0.37% … 10%, 27 times more". Ladder 5 "Worked numbers" holds about 11: "−0.9, −0.51, −0.189 … −2.30, −3.94 … \(m=2/3\) … (±3.00 at \(m=0.9\))", and it also carries the meaning and an IMF quote. WRITING §5: at most about five numbers, else a small table.
- **Concision, 3** (Lens 2b, Synthesis). Main text grew from 6,584 to 7,325 words (+11%) although the lemon toy and the trend algebra moved to fold-outs. The five-job verdict is stated five times, and Granovetter's riot appears in Ladder 3 and again as Exercise 4.

## The three changes that would raise the post most

1. **Number density.** Move Ladder 2's and Ladder 5's worked numbers into small tables, and split Ladder 1's "second question" paragraph (findings F1-F2). This lifts clarity to 4.
2. **Cut about 400 words of repetition** (F3): the §13 job table, the Mercer paragraph, the main-text Granovetter sentence, and one of the preview and short-answer (a) restatements. This lifts concision to 4 and leaves headroom under the cap.
3. **Carry the in-principle argument into short answer (a)** and tighten the society chain in (c) (F4-F5). The post's only argument about what is possible in principle (every chain of automated checkers must end somewhere) sits in Lens 1's last line, not in the answer.

## Did it answer the reader's question?

**Possibility: mostly.** The run-time/design-time term box (§3) and the three senses of "possible" in (a) are real progress and are used consistently: hook ("Nobody pressed a button: people had set the rule"), the definition of "AI-automated society" ("neither while it runs nor in writing its rules"), the Check row ("Automatic at run time, designed by people") and (a). Two gaps. First, (a) says "Without any human intervention: no" and then "Removing design-time intervention too is not shown possible or impossible", which reads as a "no" and a shrug in one breath; the "no" rests on what current systems do, not on an argument (F4). Second, the one in-principle argument, the checker regress, is in Lens 1's lens-sum under "Ours" and never reaches (a).

**Impact: yes for one channel, thin for people.** (b) now states three argued mechanisms (shared models make failures coincide; safer firms and a fragile system; automated checkers need checkers), each backed by a toy, plus a "who gains and who bears" line marked ours with a hedged Harari quote. The "who gains" line is asserted, not argued (F6). It is acceptable at this length, but it is where a reader asking about impact on people will want one more step.

**Meaning: yes, with an argument and defeaters.** (c) gives a definition, a two-horn verdict ("a society with people hidden in those two jobs, or … not a society at all") and two things that would change it. The weak points are that the definition is stipulated and chosen "so that the question has teeth", and "contest" is not treated in any lens (F5).

## Section findings (per-section fixes for scores below 5)

Only items that cost a point. Severity: **major** = fails a gate criterion for a section; **minor** = polish or one-step fix.

### F1 (major, criterion 3) Number-dense paragraphs remain in Lens 2a and 2b
- **Ladder 2** (6): about 12 numbers in the "Worked numbers" paragraph, with the formula's symbol list. **Fix:** a 3-row table: "loans default alone / 3 default / 4 default" with chances 0.0036, 0.0001, total 0.37%; then one line "with one common coin: 10%, 27 times more".
- **Ladder 5** (7): about 11 numbers, mixed with the meaning and the IMF quote. **Fix:** a 2-row table (m = 0.2 and 0.9: next gaps, verdict, largest swing), then a separate "What it means" paragraph. The fold-out already has such a table; move it up and shorten the fold-out.
- **Ladder 1** (6): the "second question" paragraph packs a bridge, a rule, a two-error check and the start of a derivation into one block of about 90 words. **Fix:** give "One rule first" and "Derivation" their own lines.
- **Lens 1 check** (5): "With 10,000 kinds … 13.29 … 4 bits … 9.29" and lever 3 ("10^4 to 10^2 … 13.29 to 6.64") are at the limit. Fine as is; do not add more.

### F2 (minor, criterion 3) Small undefined terms and dense sentences
- "disturbance" and "regulator" appear in the stepper title and in Lens 1's lens-sum before Ashby's words are glossed (the instance says "kinds of new contract"). **Fix:** one clause: "(Ashby calls a new contract type a disturbance, and the supervisor's check a response)".
- "SupTech" (§3 table) and "liquidity shocks" (Ladder 3) are not explained. BIS and IMF are never expanded in the main text (the Sources list does). **Fix:** gloss each in three words or drop the quote.
- Ashby lever 2 is still about 120 words with five quoted fragments. Split into three sentences.
- Lens 4: "Under a stricter definition of success, losing either condition is enough to fail" appears with no definition of "success" in the toy. **Fix:** say in the mechanism line what success means in the toy (ending above 100), then what the stricter version needs, or cut the sentence.

### F3 (major, criterion 6) Growth and repetition
- Main text +741 words since round 1. Repeats: the five-job verdict (hook preview, §3 table, (a), §13 table, Signs to watch); Granovetter (Ladder 3 and Exercise 4); "each bank safer, system more fragile" (Ladder 4 text, prediction 4 answer, lens-sum, (b), layers fold-out).
- **Fix, about -400 words:** (1) delete the §13 job table (§3 table plus (a) already carry it) or fold it into the layers fold-out; (2) cut the "One more data point" Mercer paragraph (read from a chart, approximate, and used nowhere later); (3) keep Granovetter as Exercise 4 and reduce the Ladder 3 sentence to one clause; (4) in the hook, drop the preview's second sentence and rely on (a).

### F4 (minor, high priority, criterion 4) Possibility rests on status, not on the in-principle argument
- Short answer (a): "Without any human intervention: no. Every automated system in our sources runs on rules and limits people set in advance." That is evidence about today's systems. The question is whether a system *could* do without them. The post has the argument but it sits in Lens 1's lens-sum: "every chain of automated checkers has to end somewhere, and in today's markets it ends in human institutions that set the rules".
- Also: the §3 table says Decide is "Mostly not", while (a) says AI "can increasingly decide" and the §13 table says "Technically more and more". The IMF finds "evidence is mixed" and "not yet implemented widely". "Increasingly" has no source in the post. **Fix:** (a) in three lines: *Run-time:* not today (humans in the loop, IMF). *Design-time:* open, but Lens 1 gives a reason to doubt it (a checker needs a checker, so the chain ends in rules someone wrote) and Lens 3 gives another (declaring needs a "we"). Replace "can increasingly decide" with the IMF's own wording.
- The Run row ("Yes, and in some markets largely does") and the Declare and Answer rows do not carry the run/design label the Check row got. **Fix:** add "(rules written by people)" to Run, so the label is applied to every row or none.

### F5 (minor, high priority, criterion 4) The society chain: stipulated definition, "contest" untreated, preview over-promises
- The hook preview says "Lenses 3 and 4 argue that declaring and answering are what make a group of people a society". They do not. Lens 3 shows that institutional facts need acceptance; Lens 4 shows when delegation can be trusted. The link to "society" is made only by the stipulated definition in §3 (members "can rely on shared rules, can contest them, and can find someone answerable"), which the box says is "chosen so that the question has teeth". The verdict in (c) therefore follows from the definition plus the premise that an AI cannot be held responsible in a behaviour-changing way.
- "Contest" appears in the definition and in (c)'s second defeater but is argued in no lens (only the one-line Gensler "Human agency … may be lost").
- **Fix:** (1) rewrite the preview to say what the lenses do show: declaring needs acceptance, answering needs consequences; the definition, which is ours, then turns that into a claim about society. (2) In (c), state the logic in one line: "if AIs also declared and answered with no human anywhere, either some human is still in those jobs (then it is not full automation) or nobody is (then, by our definition, it is not a society)". (3) Either give "contest" one sentence of support in Lens 3 or 4 (it follows from Searle: a declared status can be withdrawn by the community that accepts it) or remove it from the defeaters.

### F6 (minor, criterion 4) "Who gains, who bears" is asserted; Lens 4's central premise is uncited and one-sided
- (b): "power moves to whoever writes the models and the rules, and losses fall on whoever is exposed" is marked ours but has no step. Ashby supplies one: whoever has more variety in R constrains the rest. Add a clause: "(Lens 1: the party with the larger regulator variety sets the terms for the rest)".
- Lens 4: "An AI cannot be fined, jailed or shamed the way a broker can" carries the Answer verdict. It is unsourced, and the personhood paragraph two lines later implies the opposite once an AI is a legal person with assets (Harari notes that corporations are legal persons, and corporations are fined, not jailed). Lens 3 gives a for and against; Lens 4 gives none. **Fix:** change to "cannot be jailed or shamed, and is not yet a legal person who can hold assets to be fined", then add one sentence of counter-case (a deployer's bond, insurance or shutdown as consequences) marked ours.

### F7 (minor, criterion 2 and 5) Ladder 4 derivation: good, with three small gaps
The two-bank derivation is a genuine ladder climb now: instance, question, mechanism, worked numbers (triangle of area \(2c^2\); 2 eps^2), formula, N = 2 check, N = 10 check (2,756; verified), meaning. The widget at N = 2 reproduces the factor 2. Gaps:
- The text never says *when a bank fails*: "so it fails when \(V_1+V_2\lt 2c\)" has to be inferred from "half of each asset". **Fix:** one clause before the bullets: "a bank fails when the value of what it holds falls below c".
- The jump from the triangle to "a corner of an \(N\)-dimensional cube, with volume \((Nc)^N/N!\)" is the one "it can be shown" step. **Fix:** one more rung: N = 3 gives a pyramid, \(\tfrac13\times\tfrac12(3c)^2\times3c=(3c)^3/6\), which matches \(x^N/N!\) at \(N=3\). Then say the pattern continues.
- The square and the triangle are described ("Draw both values on a square") but not drawn. This is the one mechanism in the post with a geometric argument and no figure. **Fix:** a small diagram widget (square of side 2c, diagonal, shaded triangle; 3 steps), and one sentence pointing the reader to set N = 2 in the lab.

### F8 (minor, criterion 2) Lens 4 toy check is weak
The broker toy works (110/100/90 and the "only one condition" middle row are right), and the link type now says openly that liability is only touched. But the "Check" says "The table's worst cases, 110, 100 and 90, follow the theorem's three cases". The "both" row (110) is a best case, not a worst case, so the sentence mislabels it, and the check restates the table rather than testing it. **Fix:** replace with a case that tests the toy: "Take away the incentive: the broker sells you the 90 bond, you spot it and refuse, and you keep 100".

### F9 (minor, criterion 2) Lens 1: "Some products resist checking" explains the result but not the mechanism
The paragraph gives the instance, the hardness claim and the hedges. Why the *placement* of junk changes the price is only in the fold-out toy (7/4 versus 3/2). The reader of the main text gets "a hard problem" without the mechanism. **Fix:** move the spread-versus-concentrated contrast (two lines) into the main paragraph; keep the six-asset detail in the fold-out. Also state that Ashby's table rule ("no state appears twice in a column") is an assumption of Ashby's model and the toy happens to satisfy it. **This is the first sentence where a high-school reader could get lost:** "Ashby's table rule: in each column (each check), no state appears twice". It is stated as a fact, with no reason.

### F10 (minor, criterion 4) Cross-lens tension is now in §13; keep it, and add its link type
"Where the lenses disagree" is the post's best insight and now sits where it belongs. Add its link type (tension) in one word, and one sentence on the third kind of answer: standardise the *form* only.

### F11 (minor) Small points
- "What to try on the toys" says "The toys are in sections 7 and 5"; the tasks use only section 7 toys. Say "section 7".
- Ladder 5 text says "a circuit breaker caps the swing (±3.00 at \(m=0.9\))" without saying the breaker is set to 3; tell the reader to press "runaway + breaker 3".
- Short answer (c) is one 160-word paragraph. Split after "a machine system that people live next to".
- Guess-first options are now balanced. Prediction 3's best answer ("Open: it depends on whether AIs can accept") is not the longest. Good.

## Checks the prompt asked for

**Is the run/design-time distinction and the definition of society used consistently to the short answer?** Run/design-time: yes in hook, term box, Check row and (a); the Run, Declare and Answer rows and the §13 table do not carry the label (F4). Definition of society: used in (c), and in the hook preview only as a promise the lenses do not keep (F5).

**Ladders.**
- *Ladder 1* (N_eff): instance, question, rule, derivation, formula, N = 2 check, edge (cap 1/rho = 3.33, 3.257 at N = 100). Full. Paragraph density only (F1).
- *Ladder 2* (tranche): full with check (0.370%, 5.185%, 10.000%) and edge (634.5 times at p = 0.02). Density (F1).
- *Ladder 3* (six banks): instance, table, threshold formula, hand table (rounds 0-3, every cell checks), widget, edge (capital x1.5 saves three; lgd 1). Full, with a check ("6 of 6 in 3 rounds").
- *Ladder 4* (Haldane-May): see F7. Full for N = 2, one asserted step for general N.
- *Ladder 5* (trend): the tipping condition is now honest in the main text ("Running the toy for many values of m shows the switch at m = 2/3"), and the fold-out gives the exact argument including the real-root case near m = 1 (m = 0.95 gives roots 1.32 and 1.08; checked). Density (F1).
- *Lens 4 broker toy*: instance, table, mechanism, theorem in words, weak check (F8).

**Number density** (target at most 5): over the cap in Ladder 2, Ladder 5, Ladder 1's second paragraph. Hook now has four to five numbers per paragraph (was eight). Ladder 3 is fixed (table). Ladder 4's worked numbers have about 5.

**Terms defined before use:** futures contract, tranche, CDO, option, query language, memecoin, capital, variance, correlation, covariance, variety, status quo, principal and agent: all before use. Gaps: SupTech, liquidity shock, "disturbance", BIS/IMF expansions (F2).

**Concision and repetition:** F3.

**Standalone:** yes. No reference to another post or earlier toy; "Post 02" is a label; the English section repeats no earlier phrase by name.

**Widgets.**

| Widget | Reader can do the mechanism? | Edge case that teaches | Prose quotes readout correctly |
|---|---|---|---|
| Ashby stepper and lab | Yes | standard menu 10^2; AI supervisor +5 bits | Yes (13.29, 9.29, 6.64) |
| Seller diagram (fold-out) | Stepper only | same rule, different price | Yes (7/4, 3/2) |
| N_eff lab | Yes | huge crowd 0.3: 3.257 | Yes |
| Bayes lab (fold-out) | Yes | 10 copies: 0.999999 | Yes |
| Waterfall diagram, tranche lab | Yes | safe loans p = 0.02: 634.5 | Yes |
| Six-bank hand table and cascade | Yes, tap to fail | capital x1.5; lgd 1 | Yes; play answers verified |
| Haldane-May lab | Yes (N = 2 gives 2) | N = 20 | Yes (2,756) |
| Trend iterate | Yes | breaker clamps, feedback stays | Yes (0.04, -1.00, +-3.00) |
| May lab (fold-out) | Yes | m = 8, alpha = 0.3 | Yes |
| Status, LLM and tree diagrams | Stepper only | ghost nodes for the AI case | n/a |

The only missing figure is the two-bank square (F7). The five-jobs spine is a table, which is adequate.

**Lens sections.** All five lenses give "Adds", "Does not explain", a link type and, new this round, a job label. Lens 1 and Lens 4 mix two link types. The "same-math" label on Lens 1 is honest (variety and entropy). Lens 2a's link type now names the shared mathematics (variance of an average, portfolio theory). Lens 3 has the best limits. Lens 4 states the mismatch with the theory, which is honest, but it lacks a counter-case (F6). Links to Kunhao's 3C research are concrete (N_eff for LLM annotators and simulated agents; "who checks the checker"; Searle and crisis communication).

## Round-1 findings: status

| Round 1 | Status |
|---|---|
| F1 possibility (run/design time, scope, why five) | Met, with the gap in F4 |
| F2 meaning (society definition, verdict) | Met; stipulation and "contest" remain (F5) |
| F3 impact and balance (lemon to fold-out, who gains) | Met in structure; length grew (F3 here); "who gains" thin (F6) |
| F4 Haldane-May formula | Met: derived for N = 2 (F7 for the rest) |
| F5 Lens 4 mismatch | Met: openly stated; toy added; check weak (F8) |
| F6 number density, hook | Hook met; Ladders 2, 5 and 1 not (F1 here) |
| F7 tipping condition | Met |
| F8-F15 minors | Met (tension moved, labels, quiz options, "toy starts after the shared failure"); "(ours)" count is now 19 parenthetical marks |

## What is good (keep)

- The hook now explains futures and the Stop Logic with few numbers and a careful "neither they nor the paper test whether the pause caused it".
- The run/design-time term box: it turns the user's phrase into a testable claim and the table shows it row by row.
- Ladder 3 is a model of "do it by hand, then let the widget agree" (hand table, then 6 of 6 in 3 rounds).
- The Haldane-May two-bank derivation, with its stated assumption and a widget that returns the same factor at N = 2.
- The (c) verdict names what would change it.
