# Pedagogy critic, round 1: post 02 (AI, finance, social system)

Read as Kunhao would: phone, B2-C1, every step wanted. Criterion 1 is not judged here. Scores 1-5 for criteria 2-6: **2** ladder, **3** clarity/English, **4** insight and lenses, **5** illustrations/interactives, **6** concision. "-" means the section has no such content to score.

Widget numbers were run with `check.mjs` (14/14 configs OK). I also re-ran the six-bank cascade in Python for the values the prose quotes. I did not read self-review.md or review/ (only shot-390.png and the audio script).

## Does the post answer Kunhao's question?

Kunhao asked: "can LLMs create a new type of finance, and what would that mean for our current social system?"

**Half yes, half not clearly.**

- **"Can they?"** Answered well and honestly. Section 4 says "Verdict: 'not yet evidenced', not 'impossible'. Our search was limited." The closing "Our reading" says the near-term risk is "correlated, opaque use of ordinary instruments and agents, not an alien instrument."
- **"What would it mean for the social system?"** Never stated in one place. The reader has to assemble it from Lens 4 (acceptance, accountability, personhood), five conditionals, and five "up/down" signs. The only consequence spelled out is "money's status survives if a community accepts the tokens and the law makes a human liable."
- **Missing consequences:** who bears the loss, who bails out whom, and what happens to oversight if supervisors cannot follow instruments. These are the "social system" part. Lens 4 gives about 700 words to it, late in the post.
- **Undefined phrase:** "human-centred system" is in the title and in Lens 4's first sentence, but is never defined.
- **Where the answer sits:** the reader meets the synthesis only after about 40 minutes, and §13 holds six overlapping summaries (layers, keypoint, tension, five conditionals, critics, our reading, signs). There is no 3-sentence "short answer".

## Per-section scores

### 1 Hook (Two contracts)
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| 4 | 4 | 4 | 4 | 4 |

- **C2:** Instance first and good: "'Pay 4 coins for each rainy day.' ... 1 cell pays 8, 6 cells pay 4, 9 cells pay 0." But "With 16 cases you can price both: multiply each payout by the chance of its case and add" is a method with no numbers.
  - Fix: either give one worked price (for example, equal chances 1/16 each gives A = 2 coins) or cut the sentence and say "pricing comes later".
- **C3:** Short sentences. "What is different about money?" is a good hinge. Fix: move "A note on words" (AI vs LLM) to section 4, where it is used.
- **C4:** Links to post 01's village. It sets the question, not the lenses. Fix: add one sentence naming the two halves of the question (can AI invent; what changes) so the reader knows what to track.
- **C5:** The switch shows rule versus table clearly and its numbers are right. It has no edge case. Fix: add a third panel, "Contract C: 4 coins on rain, but only if day 2 is sun". That makes "a short rule can still be a table" visible.
- **C6:** The Harari/Skingsley paragraph and the 2^100 aside delay the hook. About 10% could go.

### 2 Guess first
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| - | 4 | - | 4 | 5 |

- **C3:** Option text is long. Q2: "1 day in 10^20 if independent; about 1 day in 100 if the same model". Fix: shorten the options to the numbers.
- **C5:** Four guess-first cards, each pointing to its answer section.
- **Fix, Q4:** It asks whether Harari's statement was "a firm forecast" before the reader has seen any quote. It is a coin-flip, not a prediction. Fix: put Q4 after the two Harari quotes, or turn it into "which of these sentences did he hedge?"

### 3 Home field (Finance before language models)
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| 4 | 3 | 4 | 5 | 3 |

- **C2 (4):** The CDO sub-ladder is complete. Instance (4 loans, 10 each), question, mechanism, numbers (0.0036 + 0.0001 = 0.37%), formula, check (0.370 / 5.185 / 10.000%), "What it means". The Flash Crash paragraph has no ladder; it is three sentences of quotation.
  - Fix: add one line saying why speed plus feedback matters, or point forward to the herding toy ("the toy in section 10 is this").
- **C3 (3):** The Harari catalogue is dense. It stacks about 12 quotes with time-stamps in five paragraphs. Undefined terms: "High-frequency traders ... 'demanding immediacy ahead of other market participants'", "circuit breakers". The aside "(transcripts disagree on the last word, so we paraphrase)" is noise for a reader.
  - Fix: define high-frequency trading and circuit breaker in one clause each. Keep 4 quotes (BIS device, Davos "made of words", BIS "believe", Davos "deadline") and move the rest to the Sources or a fold-out.
- **C4 (4):** Three-layer format (said / evidence / ours) is good, and the "Trap: three different ten years" is useful. Missing: what 2008 does not show (it was human-made, not AI-made). The text says it indirectly. Fix: add that sentence in "What it means".
- **C5 (5):** The waterfall diagram steps through 1, 2, 3 defaults. `lab-cdo` has an edge-case preset ("safe loans, p = 0.02"), and the prose quotes it correctly: 2.000%, 0.0032%, 634.5 times. No fix.
- **C6 (3):** About 20% could go. The Harari quote layer is the main weight. The "Two statements in between" paragraph and the "tool / agent" parenthetical could be cut with no loss. The Guardian 2023 line is not used later. Fix: cut as above.

### 4 What LLM agents add
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| 3 | 3 | 3 | 4 | 3 |

- **C2 (3):** All four items are quotation plus number, with no instance, mechanism or check.
  - Item 1 promises an example: "'the index stays between 90 and 110' becomes one short line a person can read." The line is never shown.
  - Fix: show the line (for example `RANGE(index, 90, 110)`, labelled "ours") and say in one sentence why a fixed vocabulary keeps it checkable.
- **C3 (3):** Undefined for the reader: "option strategies", "query language", "memecoin", "Sharpe ratio", "hit rates for the direction of the first price reaction". "Sharpe ratio fell from 6.54 to 1.22" is a bare number.
  - Fix: either define Sharpe ratio in one clause ("profit per unit of risk") or drop the figures and keep "the edge shrank as adoption grew".
- **C4 (3):** The section lists four additions but does not connect them to post 01 (why a next-word predictor can translate intent) or to the lenses that follow. Fix: for each item name the lens that picks it up ("shared model → Lens 3", "hides reasons → Lens 4"). This also gives the later lens-sums something to point back to.
- **C5 (4):** The "translator inside a fixed vocabulary" diagram is useful, and its edge case ("no checker?") is the point. Items 3 and 4 have no figure here (they get one later). No fix beyond the cross-references above.
- **C6 (3):** The GOAT price range ($122M to $214M), Dütting and Buehler lines, and the Sharpe numbers do not carry the argument. Fix: keep the "Found / Not found / Critic" list and cut the sub-numbers.

### 5 Lens 1 (Information theory)
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| 3 | 4 | 5 | 4 | 4 |

- **C2 (3):**
  - Ladder 1 is complete. 10^4, 13.29 bits, 2^k-1, check at k=6 (63) and k=10 (1,023).
  - Ladder 2 (lemon cost) skips the central step. The text shows lemon cost = 5 and a search space of 1.73e13, then says "a buyer hunting the junk must search". It never shows why an unsearchable junk set means the buyer cannot fix the price.
  - "Description" is never defined as "a short program or message from which the contract can be rebuilt". The jump from "description" to "bit string" to "program has one output" is where a high-school reader loses the thread.
  - Fix, ladder 1: add one sentence before the formula: "By a description we mean the shortest message that lets someone rebuild the whole table."
  - Fix, ladder 2: add one line to the pool toy. The buyer wants to price the pool without knowing which 10 are junk; each guess about the junk set changes the price by up to 5; checking all guesses is hopeless.
- **C3 (4):** "What the paper shows" packs four hedges into three sentences ("under a conjectured hardness assumption", "in a simple model", "may be computationally intractable", "clearly only a first step"). Fix: split into two paragraphs, "what is claimed" and "how far it goes".
- **C4 (5):** Link types are named, and it says what the lens adds and what it does not explain. It also names the trap (two meanings of "complicated") and links back to post 01. Fix: none. The used-car example needs checking for what comes from Arora p.2 and what is ours.
- **C5 (4):** `lab-count` has three presets, and the prose quotes its readouts exactly (63, 0.63%, 16,383, 1.05e-10). The seller diagram shows who hides what. But nothing lets the reader move the lemon-cost numbers: pool size, junk count and the search space are static.
  - Fix: add a small `lab` with sliders n (junk count) and pool size, showing lemon cost n/2 and C(pool, n).
- **C6 (4):** Two instances for lemon cost (used cars and the 100-asset pool) are one too many. Fix: cut the used-car arithmetic ($800, $200) to one sentence, since Akerlof is already quoted.

### 6 Lens 2 (Control and cybernetics)
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| 4 | 4 | 5 | 5 | 4 |

- **C2 (4):** Complete for the central law: instance (4 contracts, 2 checks), table, V_D=2, V_R=1, V_O≥1, check "2-1=1 bit, as in the table". "Each outcome appears once per column, so one check sends only one contract kind to 'a'" is the key step, but it depends on how the toy table was built, not on a general rule. The general pattern step ("what stays the same if we change the numbers") is only in the lab. The three levers have no numbers except the constraint one.
  - Fix: add one sentence after the check: "Change 4 kinds to 8 and 2 checks to 4 and the same count gives 3 - 2 = 1 bit."
- **C3 (4):** Terms D, R, E are named with roles. "Variety" is defined by a log. The "Counterweights" paragraph has three long quotes in a row. Fix: cut it to two.
- **C4 (5):** Link types are correct (same-math for variety/entropy, analogy for the supervisor). The limit is stated: "Ashby's disturbance is passive; finance adapts to its regulator (ours)". Cross-lens link is present.
- **C5 (5):** The stepper walks the table. `lab-ashby` has an edge-case preset ("AI supervisor +5 bits"), and the prose says "the bound stops at 0". Readouts quoted correctly (13.29, 9.29, 6.64).
- **C6 (4):** The "Counterweights" paragraph plus the two Danielsson quotes can lose about 10%.

### 7 Lens 3 (Correlation, Bayes and cascades)
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| 3 | 3 | 4 | 4 | 3 |

- **C2 (3):**
  - **Ladder 1:** the formula is given with the derivation sent elsewhere ("derived in Rung 3"). This is exactly the Test 0 "see rung 8" failure. Also, Prediction 2 (10^-20, probability that all ten are wrong) and N_eff (variance of the average of correlated forecasts) are two different quantities. The text slides from one to the other with no bridge.
  - **Ladder 4:** "Tipping point: m=1/A=2/3 (Rung 4)" and "Check. The section 10 widget at m=0.2" both send the reader elsewhere for the step.
  - **Ladder 2 and 3:** complete.
  - Fix, ladder 1: add a three-line derivation (Var of mean = [Nσ² + N(N-1)ρσ²]/N²) in the text or in a "Look inside" fold-out, and a sentence saying N_eff answers "how steady is the average", not "how often are all wrong". Keep Prediction 2 as a probability example.
  - Fix, ladder 4: move the "why 1/A" argument into the text. One line: each step multiplies the last move by A·m, so the move grows if A·m>1.
- **C3 (3):** Four ladders in one section is a lot. "Pairwise correlation ρ" and "variance σ²" are used without definition ("correlation: how often two forecasts err in the same direction, from 0 to 1"). "Likelihood ratio" is not named. Fix: add a term box for correlation and variance. Split the section into two subsections with a recap line at the end of each.
- **C4 (4):** Link types are listed. Granovetter is a clean analogy (same threshold shape), and the lens-sum has a cross-lens link. But "Does not explain: how widely LLMs are used in finance" is an evidence gap, not a limit of the lens. And "correlation ... cuts the variety a supervisor must cover in Lens 2" is asserted twice (here and in §13) with no argument. Fix: state the real limit of this lens (it takes the network and the shared-model share as given) and say in one sentence why fewer independent disturbances means less variety to cover, or drop the tension from §13.
- **C5 (4):** `lab-neff`, `lab-bayes2`, the W5 hand stepper and `cs-w5` / `it-herding` all work, and their edge-case presets teach. But the two widgets that carry Ladders 3 and 4 sit three sections later in the Playground. In the ladder the reader has only a static stepper for the cascade and no picture for the feedback loop. Fix: put `cs-w5` right after Ladder 3 and `it-herding` after Ladder 4, and leave the Playground questions as prompts.
- **C6 (3):** Lens 3 is about a quarter of the post. Ladder 2 (counting one voice ten times) repeats post 01's arithmetic and is not needed for the question. Fix: reduce it to a two-sentence paragraph or a fold-out. This cuts about 15%.

### 8 Lens 4 (Social reality, accountability, personhood)
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| 3 | 3 | 4 | 4 | 4 |

- **C2 (3):** Acceptance has a ladder: stones as wall, paper as money, "X counts as Y in C", then the diagram. Accountability starts with the theorem: "Lupia and McCubbins, Theorem 5.1: if the principal can tell whether the agent's proposal beats the status quo (knowledge) and the agent has a reason to be trustworthy (incentive), delegation succeeds". The instance is a table cell ("a plane"). Roles (principal, agent) are never named, which breaks WRITING §4. The "Testing Harari's chain" paragraph has no worked case.
  - Fix: before the theorem, give one instance with named roles. For example, you (principal) hire a broker (agent) to buy a bond. Case 1: you can read the bond and the broker is paid on your result. Case 2: you cannot read it. Walk the four cells with this case. Then state the theorem as a short name for it.
- **C3 (3):** Undefined or unclear: "deontic powers" (defined inline, but heavy), "principal", "agent", "status quo", "intentional stance" (never explained), "steelman" (idiom, not defined). The Dennett sentence ("adopting the intentional stance is free, but its success is 'perfectly objective'") is hard to parse for a reader who has not met the idea.
  - Fix: drop Dennett, or give a two-line instance. Replace "steelman" with "the strongest version of Harari's argument".
- **C4 (4):** This lens carries Kunhao's question, tests the Harari chain, and says "Does not explain: how any of it works in law". The link-type chip says Searle is a "structural analogy" to post 01's meaning lens, but the text never makes that comparison. It also does not say what this lens adds that the others cannot. Fix: add one sentence on the post 01 link (meaning as use ↔ money as accepted status) and one on what only this lens shows (the human role is acceptance and liability).
- **C5 (4):** The status diagram is clear, and step 4 is useful. The Lupia table is plain text. The chain test, the post's central argument, has no figure. The diagram's last step says "In the one case we checked, Truth Terminal, the money and liability ran to people", and "liability" is not supported anywhere above (suspicious, see below).
  - Fix: add a small 4-node diagram of the chain "Money is words → AI takes over words → AI takes over money", with acceptance and enforcement as the two gates between steps 2 and 3.
- **C6 (4):** The Personhood paragraph and the Dennett sentence add little. About 10% could go.

### 9 The math ladder (four rungs)
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| 3 | 3 | 4 | 3 | 3 |

- **C2 (3):** The opener says "nothing above depends on them", but Lens 3 says "derived in Rung 3" and "(Rung 4)". That is a contradiction in the post's own structure.
  - Several steps are announced, not shown. Rung 2: "The step: H(E)≥H(E|R) (conditioning cannot raise entropy), then expand." Rung 3: "Set this equal to σ²/N_eff and solve." Rung 4: "The roots of x²-bx+c=0 have product c; when complex, each has size √c" (the characteristic equation is never derived from the gap rule).
  - Numbers and checks are present (1.75, 0.75, 1.099, 0.548 / 1.002 / 1.162).
  - Fix: write each skipped line (2-3 lines each), or fold the rung into the Lens 3 text where it is needed. Delete "nothing above depends on them".
- **C3 (3):** Graduate density: "conditional entropy", "characteristic equation", "complex roots" without definition. Fix: one-clause glosses.
- **C4 (4):** Each rung says which section it comes from. Fix: add the link type (rung 2 same-math with Lens 2, rung 3 same-math with Lens 3).
- **C5 (3):** No figure at all. Rung 4 could reuse `it-herding`. Rung 2 could use the Ashby bars. Fix: embed or link the widgets next to the rung text.
- **C6 (3):** Rung 1 repeats the lemon-cost numbers from Lens 1 (100 assets, 10 junk, 45, 5, 1.73e13). Fix: fold Rung 1 into Lens 1, or cut it to the Δ(n) definition.

### 10 Playground
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| - | 3 | - | 4 | 5 |

- **C3 (3):** The answer line is hard to read: "(1) none; Y1. (2) all three at 0.8; two at 1. (3) just above 1.2: ×1.2 still loses five of six, ×1.25 only three."
  - **Error (my re-run):** (2) is wrong for "two at 1". With lgd=1 and X1, X2 seeded, five banks fail, not six. X3 never lends, so it fails only if seeded, so "sinks all six" needs all three X banks at any loss rate. The ×1.2 and ×1.25 numbers are correct.
  - (1) is ambiguous ("none; Y1" means: at 0.8 no single bank starts a spread; at 1.0, Y1 does).
  - Fix: rewrite the answers as three clear lines and correct (2) ("all three X banks, at any loss rate; two X banks sink 5 of 6 at lgd 1").
- **C5 (4):** `cs-w5` and `it-herding` work, and the iterate readout at m=0.2 matches the prose (0.04 up, -1.00 down, 0.000). The breaker at m=0.9 shows the cap (±3.00). But `cs-w5` opens with only X1 seeded, so the first thing the reader sees is "1 of 6 banks fail", which is the boring case. Fix: seed X1, X2, X3 by default, or say "tap X2 and X3 now" in the first line.
- **C6 (5):** Short and useful.

### 11 Your turn
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| - | 4 | - | - | 4 |

- **C3 (4):** The heading says "Three exercises and a transfer challenge", but four exercises follow. Exercise 4 (Granovetter) has no hint and no folded solution, which WRITING §6 asks for. Fix: fix the heading, and add a hint ("threshold k means the k-th person joins once k are already rioting") and a folded solution.
- **C6 (4):** Fine. Exercise 2's random 30-bank networks is optional and could be marked so.

### 12 Where this shows up in your work
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| - | 5 | 4 | - | 4 |

- **C4 (4):** Four of five cards give a real research handle: N_eff for agent populations, surrogate labels as one annotator plus noise, cross-lingual correlated errors, and crisis communication. The Collaboration card is weak. Fox's remark that "capitalism is hardly mentioned" in Nexus is a book-review point, not a network-science link. Missing: a link to Kunhao's climate-misinformation and conspiracy work. Fix: replace the Collaboration card with one on Kunhao's online-innovation work (who can inspect an artefact made by an open community?), and drop the Fox quote from here.
- **C6 (4):** Good. Five cards are about right.

### 13 So what happens? (Synthesis)
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| - | 3 | 4 | 3 | 2 |

- **C3 (3):** The section is long and mostly restates things already said in the lens-sums. A first-time reader cannot find the answer to their question quickly.
- **C4 (4):** The "tension between lenses" paragraph is the best insight in the post, but "The lenses disagree about what is dangerous in shared models" is asserted rather than argued. See the Lens 3 C4 fix.
- **C5 (3):** No figure. Fix: add a one-picture summary of Harari's chain (AI invents → opaque → correlated → who rules), with the evidence level on each link (not found / theory / toy / contested). The reader would then see the answer at a glance.
- **C6 (2):** The same point is made six times: layers, keypoint, tension, five conditionals, critics, our reading, plus five "up/down" signs. The five conditionals repeat the lens-sums almost word for word.
  - Fix: open with a boxed "Short answer" (3-5 sentences, two parts: can LLMs invent new finance; what would change for the social system). Then keep only "Our reading" and "Signs to watch". Cut the conditionals and critics paragraphs, or fold them into one `details`.

### 14 Recall questions
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| - | 4 | 4 | - | 4 |

- **C4 (4):** Seven cards, three marked ↻ for later reuse. Coverage is lopsided: three cards for Lens 1-2, one for Lens 3 (N_eff), one for Lens 4. Nothing asks for the cascade threshold, the tipping point, Lupia's four cells, or "assertion versus scenario". Fix: swap the Rung-2 entropy card for "Why does one failure not spread but three do?" and add "Name Harari's assertion and one scenario".
- **C6 (4):** Fine.

### 15 How to say it in English
| C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|
| - | 5 | - | - | 3 |

- **C3 (5):** Natural examples that use post ideas ("in lockstep", "a single point of failure"). The "paragraph to loop" is a good idea.
- **C6 (3):** 10 + 9 phrases + 4 patterns + 3 fixes is more than a phone reader will use. WRITING §8 also asks for 2-3 repeats from earlier posts, and none is marked. Fix: cut the "Small fixes" block and 4 of the 9 evidence phrases, and mark which 2-3 are repeats from post 01.

## First sentence where a high-school reader gets lost

In section 3, the Flash Crash paragraph: **"High-frequency traders 'did not cause the Flash Crash, but contributed to it by demanding immediacy ahead of other market participants'."** Neither "high-frequency trader" nor "demanding immediacy" is explained, and the paragraph's point (speed and feedback) cannot be seen without them.

The first real conceptual loss is in Lens 1 ladder 1: **"A description gives only one contract (a program has one output)".** The reader was never told that a "description" means a shortest program or message that rebuilds the table.

## Widget checks

| Widget | Reader can do the mechanism? | Edge case teaches? | Prose quotes readout correctly? |
|---|---|---|---|
| sw-contracts (switch) | Compare only | None | Yes (1/6/9 cells) |
| dg-waterfall | Step through | - | Yes |
| lab-cdo | Yes (p, w sliders) | Yes ("safe loans, p = 0.02") | Yes: 0.370%, 27x, 2.000%, 0.0032%, 634.5x; 5.185% verified |
| dg-llm | Step through | Yes ("no checker?") | n/a; the example line is promised but not shown |
| lab-count | Yes | Yes (k=14, two days k=20) | Yes: 63, 0.63%, 16,383, 1.05e-10 |
| dg-seller | Step through only; no sliders | - | 1.73e13 and C(100,10) correct |
| dg-tree (fold-out) | Step through | - | 4 / 8 / 16 flips as stated |
| st-ashby / lab-ashby | Yes | Yes ("AI supervisor +5 bits") | Yes: 13.29, 9.29, 6.64 |
| lab-neff | Yes | Yes ("huge crowd, 0.3") | Yes: 2.703, 1.099, 3.257 |
| lab-bayes2 | Yes (n slider) | Yes (10 copies) | Yes: 0.8, 0.941, 0.999999 |
| st-w5-hand | Step through | - | Matches my Python re-run |
| cs-w5 | Yes, but seeded with X1 only | Yes (capital ×1.5) | 6/6 and ×1.5 → 3 correct; ×1.2 → 5, ×1.25 → 3 correct; **Playground answer (2) wrong** |
| it-herding | Yes | Yes (breaker) | Yes: 0.04 / -1.00 / 0.000; ±3.00 at m=0.9 |
| dg-status | Step through | - | n/a |

Layout at 390 px (from the screenshot): no horizontal scroll. The diagram widget has a large empty area at step 1 of 5 (dg-llm), which looks unfinished until you tap Next.

## Lens checks

| Lens | Says what it adds | Link type | What it does not explain | Gap |
|---|---|---|---|---|
| 1 Information | Yes | same-math / analogy / metaphor | Yes | Mapping contracts → programs is labelled "ours". Good. |
| 2 Control | Yes | same-math / analogy | Yes (passive disturbance) | None |
| 3 Correlation | Yes | same-math / analogy | Weak: "how widely LLMs are used" is an evidence gap, not a limit of the lens | N_eff and Prediction 2 are different quantities, but both sit under "same-math" |
| 4 Social | Yes, but not "only this lens" | analogy / metaphor | Yes (law) | The Searle link to post 01 is named but not made |

Cross-lens links are good in the lens-sums, but the "tension" claim needs an argument or a cut.

## Audio listenability

- **Standalone chapters:** each chapter ends with a recap. Most can be looped alone.
- **Hook, guess, answer, recall:** work well.
- **Ladder (math) chapter:** very hard by ear. "The lemon cost is the expected payoff minus the minimum, over sets of n assets, of the expected payoff given those assets pay zero." And "a characteristic equation whose roots have product A m." Fix: shorten each rung to its idea and its number ("ten banks, correlation 0.9, about one opinion"), and say that the derivation is on the page.
- **Lens 3 chapter:** four ladders in one chapter is long for looping. Fix: split into two chapters (correlation, then cascade and feedback).
- **Letter names:** "V D", "V R", "V O" are easy to mishear. Fix: say "variety of disturbances", "variety of the regulator", "variety left in the outcome" at least the first time.
- **Playground chapter:** it cannot be done by ear (it says "tap banks" and answers are given without the setup). Fix: shorten to two sentences and say "do this on the page".
- **Home chapter:** the quotes are readable but long. Fix: after cutting section 3, cut here too.
- **Six-bank spoken description:** "One bank lent to all three; others lend to it" is ambiguous about direction. Fix: "Y1 lent five to each of the three X banks."
- **Formulas:** otherwise spoken clearly ("N divided by one plus N minus one times rho").

## Suspicious facts (for the fact-checker; one line each)

1. Playground answer (2): "two at 1" sinks five banks, not six, per my re-run.
2. Lens 1 ladder 2: the $1,000 / 20% lemons / $200 used-car numbers are cited to Arora et al. 2009, p.2; they may be ours (Akerlof-style), so check attribution.
3. Lopez-Lira and Tang: "about 90% hit rates" and "Sharpe ratio fell from 6.54 to 1.22", page 6.
4. Cover and Thomas 1991, "Theorem 7.2.4" and pages 150, 151, 163 (first-edition numbering).
5. dg-status step 4: "the money and liability ran to people" for Truth Terminal; the sources cited for Truth Terminal speak of donation and endorsement, not liability.
6. Truth Terminal "GOAT valued ... about $122 million to over $214 million".
7. Dennett 1987 p.24 "perfectly objective"; Arora Table 1 on p.6; Ashby pp.246-247.
8. Structure contradiction (not a fact error): §9 says "nothing above depends on them" while Lens 3 defers its derivations to Rung 3 and Rung 4.
9. Heading of §11 says three exercises; the section has four.

## Post-level scores (minimum over sections)

| Criterion | Score | Lowest section(s) |
|---|---|---|
| 2 Ladder | **3** | Lens 1 (ladder 2), Lens 3 (ladders 1 and 4), Lens 4, §4, §9 |
| 3 Clarity and English | **3** | §3, §4, Lens 3, Lens 4, §9, §10, §13 |
| 4 Insight and lenses | **3** | §4 (LLM agents) |
| 5 Illustrations | **3** | §9 (no figure), §13 (no figure) |
| 6 Concision | **2** | §13 (six repeated summaries) |

The release gate (at least 4 on every criterion) is not met.

## Top three changes

1. **Make the answer easy to find, and finish the "social system" half.**
   - Add a boxed 3-5 sentence "Short answer" at the start of §13 (and a one-line preview after the hook). Part 1: can LLMs create new finance (not yet evidenced; what they do add). Part 2: what would change (who accepts, who is liable, who can still check).
   - Define "human-centred system" once.
   - Cut §13 to Short answer, Our reading and Signs to watch. Fold the layers, conditionals and critics into one `details`.
   - Add the chain-with-evidence-levels figure.
   - Add one sentence on the concrete consequences the post currently omits: who bears the loss, who bails out, and what supervisors can do when they cannot follow an instrument.
   - This lifts criteria 6, 3 and 5 for §13.

2. **Make every ladder stand on its own page, and move the lens maths out of the appendix.**
   - Put the N_eff derivation and the "tip at m=1/A" argument inside Lens 3 (or a "Look inside" fold-out) and delete "nothing above depends on them".
   - Write the skipped lines in Rungs 2-4.
   - Add the missing steps in Lens 1 (define "description"; show why a hidden junk set stops the buyer fixing the price).
   - Add a worked instance with named roles (principal, agent) before Lupia's theorem.
   - Define variance and correlation.
   - Put `cs-w5` and `it-herding` next to Ladders 3 and 4.
   - Reduce Ladder 2 (counting one voice ten times) to a paragraph.
   - Fix Playground answer (2) and seed `cs-w5` with X1, X2, X3.
   - This lifts criteria 2, 3, 5 and 6 together.

3. **Cut and explain the finance vocabulary in §3-4.**
   - Define high-frequency trading, circuit breaker, option, query language, memecoin and Sharpe ratio in one clause each, or cut the figures that need them.
   - Keep about 4 Harari quotes with the three-layer frame and move the rest to Sources.
   - Show the one-line contract in the LLM section.
   - Link each of the four "additions" to the lens that picks it up and to post 01.
   - Fix §11's heading and give Exercise 4 a hint and a folded solution.
   - This lifts criteria 3, 4 and 6 in sections 3 and 4, which are where a high-school reader first gets lost.
