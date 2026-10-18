# Pedagogy critic, post 02 v2, round 1 (stage S5)

Read as Kunhao would: phone, B2-C1, every step wanted. Criterion 1 is not judged here. Scores are 1-5 for criteria **2** ladder, **3** clarity and English, **4** insight and lenses, **5** illustrations and interactives, **6** concision. "-" means there is nothing to score.

**Method.** I read the critic prompt, rubric, WRITING.md v0.5, charter and learner state, then all of `src/content.html` (every fold-out and widget config). I did not open earlier critic or verify files. I hand-checked the arithmetic of every worked example (Ashby table, lemon toy, N_eff, Bayes odds, tranche, six-bank cascade and its play answers, trend-follower table, Haldane-May ratio, May threshold, majority tree). All agree with the text. Word count: main text 6,584 (cap 7,500).

**Tooling note, not a post defect.** The standalone build (`build-post.mjs posts/2026-10-ai-finance`) inlines the component library as a 389-character stub. Presumably a `String.replace` is swallowing a `$` sequence. `node --check` reports a SyntaxError, no widget mounts, and `scrollWidth` is 455 at 390 px. I therefore judged the widgets from their JSON configs and the prose, not from a live render. Please re-run the render test on the `--site` build, which is the gate.

## Scores

| Section | 2 Ladder | 3 Clarity | 4 Insight | 5 Illustr. | 6 Concision |
|---|---|---|---|---|---|
| 1 Hook | 4 | 3 | 4 | 4 | 4 |
| 2 Guess first | - | 4 | 4 | - | 5 |
| 3 Five jobs | 4 | 4 | 4 | 4 | 4 |
| 4 What AI agents add | 4 | 4 | 3 | 4 | 4 |
| 5 Lens 1 Check (Ashby, lemons) | 4 | 3 | 4 | 5 | 3 |
| 6 Lens 2a Decide (N_eff, tranche) | 5 | 4 | 4 | 5 | 4 |
| 7 Lens 2b Cascades | 3 | 3 | 4 | 5 | 3 |
| 8 Lens 3 Declare (Searle) | 4 | 4 | 4 | 4 | 5 |
| 9 Lens 4 Answer (Lupia-McCubbins) | 3 | 4 | 3 | 4 | 4 |
| 10-12 Play, exercises, 3C | 4 | 4 | 4 | - | 4 |
| 13 Synthesis | - | 4 | 3 | 4 | 3 |

**Post level (minimum): 2 = 3, 3 = 3, 4 = 3, 5 = 4, 6 = 3.** The gate (at least 4 everywhere) is not met.

Evidence for the minima:
- **Ladder, 3.** Ladder 4 gives its formula with no derivation: "plan B fails with chance \(N^N\varepsilon^N/N!\) (as given by Haldane and May)". In Lens 4 the Lupia-McCubbins ladder has an instance and a table but no numbers or check.
- **Clarity, 3.** "Instance. Six banks (toy, ours). X1, X2, X3 run one model; Y1, Y2, Y3 do not. Capital … 10 each for X; 10, 9, 11 …" runs to about 15 numbers in one paragraph.
- **Insight, 3.** Lens 4 does not explain the job it is named for (finding 5). The three-part question is only half answered (findings 1 and 2).
- **Concision, 3.** The same point (correlation makes failures joint) is made four times in Ladders 2, 3, 4 and 5. About 15% of the main text could go.

## The three changes that would raise the post most

1. Answer "possible" and "meaning" with arguments, not status reports (findings 1-2).
2. Rebalance: move the Arora lemon section to a fold-out, merge Ladders 3-5 into two, and spend the freed 500-700 words on what automation does to people and on the Declare and Answer jobs (findings 3, 8).
3. Fix the ladder and number-density breaks (findings 4, 6, 7).

## Findings

Severity: **critical** = the post fails its stated question; **major** = fails a rubric criterion for a section; **minor** = polish.

### F1 (major, criterion 4) Possibility is answered as "where finance stands today", not as "could it be"

Short answer (a) says: "Partly. In markets, *running* is largely automated already … Nothing we read shows that the other jobs could be automated, or that they could not." That is a status report plus an honest shrug. It does not separate three senses of "possible":
- capable (can AI do the task?),
- stable (does the system hold together without people?),
- legitimate or accepted (does anyone treat the output as binding?).

Specific gaps:
- **Design time versus run time is never decided.** The definition is "no person needed at any step". The hook then says of the 2010 Stop Logic "Nobody pressed a button: people had set the rule and its limits in advance". Under the post's own definition that Check already ran with nobody at the step. The table still says "Partly automatic", and Declare is marked "Human" with no argument. Everything the post concludes depends on whether a rule written by people beforehand counts as intervention, and the post never says. The user's phrase is "without any necessity of human intervention", so this is the heart of the question. **Fix:** after the five-jobs list, add one paragraph with a term box, "Intervention at run time vs at design time". State which one the post tests. Then re-label the table rows with it, for example "automated at run time, designed by people".
- **"Run" is only financial matching.** A society's running also includes energy, food, logistics and repair, which are physical. The post never says it is leaving them out, so "society" quietly means "financial system". **Fix:** one sentence in §3 saying the physical economy is out of scope, and why.
- **The five jobs are asserted ("Our framework (ours)").** Nothing says why five. Two candidates are missing: *goal-setting* (who chooses what the system is for) and *enforcement* (who makes a declared rule bite). Lens 3 half-admits the second ("a law is not in force until it is accepted and enforced"). **Fix:** two sentences in §3: why these five, and where goals and enforcement fall, probably under Decide and Declare.

### F2 (major, criterion 4) The "meaning" half is deferred rather than answered

- The lede asks "would the result still be a society?". The word *society* is never defined. WRITING §0 requires defining a key term from the question at first use. The Term box defines only "AI-automated society".
- Short answer (c) ends: "Whether that would still be a society is the question behind Harari's 'Do we want to allow that?'". That hands the question back instead of answering it.
- The preview says "Declaring and answering are the jobs that decide whether the result is still a society". This is asserted before any lens has argued it, and the argument is circular.
- Lenses 3 and 4 carry all the meaning. They are the shortest (671 and 401 words), have no toy, and have no worked numbers.

**Fix:**
1. In §3 give a one-sentence working definition, for example "a group whose members can rely on shared rules they can contest, and on someone being answerable". Mark it "ours" and say what it excludes.
2. In (c) say plainly: "On this definition, a world where AIs also declare and answer is either a society with hidden humans, or not a society in this sense, a machine system we live next to."
3. Mark that last step as the post's own verdict and say what evidence would change it.

### F3 (major, criterion 4 and 6) The impact half is one channel, and the weight sits on finance mechanics

- Short answer (b) is almost entirely "correlated failure". The only sentence about people is "The losses would fall on those exposed: buyers, lenders, and whoever bails them out". It is unsupported and uncited.
- Harari's "power shifting from humans to algorithms" appears only in the fold-out. What happens to who holds power, to losers and winners, and to speed and benefits is not discussed.
- Word budget by lens (main text): Check 992, Decide 631, Cascades 897, which is **2,520 words on finance fragility**. Declare plus Answer plus Synthesis total about 1,440.
- Ladders 2, 3, 4 and 5 all teach "sameness makes failure joint". They differ only in representation (tranche, network, assets, trend). A reader finishes with that one idea four times and with little on what it means for a society.

**Fix:**
- Make the Arora lemon passage (about 450 main words) a fold-out. It rests on a conjecture and serves only one sentence of the answer.
- Merge Ladder 3 (cascade) and Ladder 5 (trend-followers) into short "Look inside" pieces, or cut Ladder 2 (tranche) to the single 10% versus 0.37% contrast.
- Add a short "Who gains, who bears" paragraph to (b), with sources or marked "ours".

### F4 (major, criterion 2) Ladder 4: the key formula is quoted, not climbed

The reader gets the instance, the mechanism ("each bank is much safer, but the banks are identical, so when one fails they all fail"), then \(N^N\varepsilon^N/N!\) "as given by Haldane and May". Nothing shows where \(N^N/N!\) comes from, or what failure threshold makes a bank's own chance 2.76e-17. A strong 17-year-old cannot reproduce 2.76e-17 from the mechanism. WRITING §1 says "no 'it can be shown'". The check ("10^10 × 10^-20 / 3,628,800") only re-plugs the formula.

**Fix:** either derive it in four lines in the main text or in a fold-out for \(N=3\), or state the bank-failure rule Haldane and May use and compute \(N=3\) by hand. If the derivation is too long, say so honestly: "we quote the formula; the ratio's size is the point" and move the number to the fold-out.

### F5 (major, criterion 4) Lens 4 does not explain the job it is named for

- The **Answer** job is "bear losses and be held responsible". Lupia and McCubbins is about when a principal can *trust an agent's advice* (knowledge and incentive). That is the Decide or Check question, not who pays.
- The post's real Answer content is the IMF line "institutions are responsible for AI systems they deploy" and the personhood paragraph. Both are cited sources outside the lens.
- The "fill-in (ours)" that bridges the two ("an AI cannot be fined, jailed or shamed … so the incentive condition must run through whoever deploys it") is the useful insight. It is hidden at the end of a paragraph.
- There is no worked number and no check.

**Fix:**
- State the mismatch openly in the link-type line: "same shape for trust in delegation; liability is a separate question this lens only touches".
- Move the "cannot be fined, jailed or shamed" step up and give it its own sentence.
- Add a three-row toy, for example the broker who is paid only on profit, so the two-by-two earns its place.

### F6 (major, criterion 3) Number-dense paragraphs and an undefined-term hook

WRITING §5 caps a paragraph at about five numbers. Examples over the cap:
- Hook, first paragraph: date, time, 75,000, $4.1 billion, 9%, 13 minutes, 1,050, and 1%, about eight numbers in one paragraph.
- Ladder 3 instance paragraph, about 15 numbers (above).
- Ashby "Table rule" paragraph, about eight (plans, kinds, bits, outcomes).
- Ladder 4 worked numbers, seven.
- Lens 2a "For N=10: ρ=0 gives 10; ρ=0.3 gives 2.703; ρ=0.9 gives 1.099; ρ=1 gives 1".

**Fix:** put the six-bank setup in a small table of lender, borrower and amount, and the capitals in a one-line list, or let the widget carry it. Split the Ashby paragraph into Question, Mechanism, Numbers and Formula lines. Trim the hook to four numbers.

**First sentence where a high-school reader gets lost:** the hook, paragraph 1, "to sell 75,000 futures contracts on the US stock index … to protect its existing stock holdings". *Futures contract* and *hedging* are never explained. "buy orders were left waiting in the market" assumes an order book. The same paragraph then adds an "execution algorithm" and a "9% of volume" rule. **Fix:** one plain sentence first ("A futures contract is a promise to buy or sell at a set price on a later date; the fund sold them to cover itself if stocks fell"), then fewer numbers.

**First lost inside a lens:** §5, "The *variety* of a set is the base-2 log of its number of states, in bits." This is the definition first, before the instance (it breaks the ladder). It is also followed by "The books end in state a, b, c or d", where the states are never interpreted. **Fix:** give the instance first, and say what a and c mean, for example "a = books balanced, c = a small loss shown".

### F7 (major, criterion 2) Ladder 5's tipping condition is asserted in the main text

The text says "The swing shrinks when \(Am<1\) and grows when \(Am>1\)" with the intuition "each step the chasers add \(Am\) times the last move". That is not a full account, because the pull-back term also acts. The fold-out gives the real reason (complex roots of modulus \(\sqrt{c}\), valid only while \(b^2<4c\)). The reader is told to trust the claim and "the fold-out shows why". WRITING §4 says the argument the post needs belongs in the main text. A numeric check also helps: at \(m=0.95\) the roots are real (\(b^2=5.76>4c=5.70\)), so the "complex" condition does not hold for every \(m\) near 1. **Fix:** say in the main text that the condition was found by checking the toy numerically, and show the \(m=0.5\) versus \(m=0.8\) steps by hand. Keep the root argument in the fold-out.

### F8 (minor, criterion 4) The cross-lens tension is hidden in a fold-out

"Ashby's third lever says: impose a constraint … Haldane and May say: when everyone holds the same thing, the system grows fragile. A standard menu makes checking easier and firms more alike." This comparison is the best insight in the post (the lenses *disagree* on one policy). It sits in the closing fold-out. **Fix:** move it into §13 as a short paragraph, or into the end of Lens 2b.

### F9 (minor) Lens labels and link types

- The meta list calls Lens 2 "Complex systems and decision theory". Lens 2a is statistics and portfolio diversification.
- Its link type "same-math: effective number of opinions; odds form of Bayes" names a link to Bayes that appears only in a fold-out. **Fix:** state which field shares the math (variance of an average, portfolio theory) in the link-type line.
- Lens 3's link type uses the "analogy" colour for "conceptual analysis". Choose a type from the charter list or add one.

### F10 (minor, criterion 2) Ladder 1 jumps between two meanings of "failure"

The instance asks "how often are all ten wrong on the same day", which is an event probability. The next question is "how steady is the average", which is variance. Nothing says how the two relate. **Fix:** one bridging sentence: "Both ask how much ten banks' errors overlap."

### F11 (minor, criterion 2) Lens 3 terms

- "Constitutive" is undefined (the type-versus-token subtlety is the most compressed passage in the post).
- *Institutional fact* is used in the link-type line before it is explained.
- **Fix:** gloss both in a short term box, with the lost-bill example restated plainly.

### F12 (minor, criterion 3) Density and "(ours)" saturation

- The Ashby lever-2 list item is about 170 words with six quoted fragments from three papers. Split it into three sentences.
- The "(ours)" marker appears about a hundred times. It is honest and the fact-check needs it, but it breaks reading aloud. Use it where the status of a claim is unclear. Where the section already says "toy, ours", do not repeat it.

### F13 (minor, criterion 6) Repetition across the closing sections

The five-job verdict appears in the preview, short answer (a), the table in §13, the four-layers fold-out and the five-conditionals fold-out. The lens-sum lines say it again. **Fix:** drop the "Five conditionals" fold-out (it restates the lens-sums) or the §13 table, whichever the reader finds less useful.

### F14 (minor, criterion 4) Guess-first answers are guessable by form

In all four predictions the correct option is the longest, most specific and most hedged one. A test-wise reader can pick it without thinking. **Fix:** shorten the right options or lengthen two of the wrong ones. Replace "Nothing: the figure is about bonds", which is not a serious distractor.

### F15 (minor, criterion 4) Toys that bake in their conclusion

The six-bank cascade opens with X1-X3 "failing together" and capitals chosen (10, 9, 11) so that the cascade just completes. It shows the *threshold* well. It does not show that a shared model *causes* joint failure, which is assumed. The caption says "toy numbers, ours", which is honest. **Fix:** add one sentence in "What it means": "The toy starts after the shared failure; Lens 2a estimated how likely that is."

## Checks the prompt asked for

**Does the post answer all three parts?** Findable: yes, in the short answer. In substance: (a) partly (F1), (b) partly (F3), (c) the part that most needs an argument is deferred (F2).

**Five-jobs frame.** Used consistently in the §3 table, the lens headings and the §13 table. The transfer challenge and the "Signs to watch" list also follow it (the signs map to decide, decide, check, declare, answer, but are not labelled). Gaps: Run gets no lens, Lens 2b is not tied to a job, and §4 has a bold run-in "How far has invention got?" that is not a job. **Fix:** label each lens in its link-type line with its job, and say in one line that Run is shown by data, not by a lens.

**Does each lens earn its place?**
- *Lens 1 Check:* yes, with fold-outs. The lemon section is the weakest part (F3).
- *Lens 2a:* yes, the best-built ladder (full ladder plus check).
- *Lens 2b:* partly. Ladders 3-5 repeat the sameness point.
- *Lens 3:* yes. It gives the strongest "does not explain" line, and the for/against arguments are labelled ours.
- *Lens 4:* weakest (F5).

**Lens sections:** every one has an "Adds" and "Does not explain" line, which is good. Link types are present everywhere. The 3C section links to Kunhao's research well (N_eff for LLM annotators and simulated agents, "who checks the checker").

**Widgets (from configs).**

| Widget | Lets reader do the mechanism? | Edge case that teaches | Prose quotes readout correctly |
|---|---|---|---|
| Ashby stepper and lab | Yes, sliders for contract types and V_R | "standard menu 10^2", "AI supervisor +5 bits" | Yes: 13.29, 9.29, 6.64 |
| Seller diagram | Stepper only | Same rule, different price | Yes: 7/4 and 3/2 |
| N_eff lab | Yes | "huge crowd, 0.3" gives 3.257 | Yes |
| Bayes lab (fold-out) | Yes | 10 copies give 0.999999 | Yes |
| Waterfall diagram and tranche lab | Yes | "safe loans, p = 0.02": 634.5 times | Yes: 0.37%, 5.185%, 10%, 0.0032% |
| Six-bank stepper and cascade | Yes, tap to fail | capital ×1.5; lgd 1 | Yes (play answers verified by hand) |
| Haldane-May lab | Yes | N slider | Yes: 2,756 |
| Trend iterate | Yes | breaker clamps but does not stop feedback | Yes: 0.04, -1.00, ±3.00 |
| Status and LLM diagrams | Stepper only | Ghost nodes for the AI case | n/a |

The main gap is not a widget but the lack of one for the spine: no figure maps the five jobs to their status today and to the lens that treats each (F-note in §3, criterion 5). The herd-toy breaker is a clamp on the gap, not a pause and resume like the 2010 Stop Logic. The caption says "caps the gap", which is honest, but the text links it to the 2010 pause, so one sentence should say the toy breaker is a simplification.

**Standalone?** No references to other posts or to earlier toys. The eyebrow "Post 02" is only a label. The English toolkit's repeated phrases do not name earlier posts.

**Length well spent?** Under the cap at 6,584 words, but misallocated (F3). Fold-outs total 2,186 words and are used appropriately (Harari lines, Ashby entropy, lemon formula, tree, May, gain, Bayes, layers).

## What is good (keep)

- The firmness sort of Harari's lines and the "four different ten years" trap give a balanced, standalone treatment of the person, well kept in a fold-out.
- Lens 2a is a model ladder: instance, question, derivation, check (N=2, ρ=0.5), preset-quoted edge case.
- "Does not explain" lines are specific. The honesty marks are consistent: "toy, ours", "conjecture", "a hypothesis, not a finding".
- The edge-case design (N_eff ceiling, p = 0.02 tranche, capital ×1.5, breaker) really teaches.
- Section 12 ties to 3C with testable "ours, to test" claims, and Exercise 4 (Granovetter) is the right size for a fold-out hint and solution.
