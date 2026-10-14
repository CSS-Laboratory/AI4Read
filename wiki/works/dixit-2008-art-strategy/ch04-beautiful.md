---
id: dixit-2008-art-strategy/ch04-beautiful
work: dixit-2008-art-strategy
unit: "4. A Beautiful Equilibrium (with Epilogue to Part I)"
pages: 106-138
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# A Beautiful Equilibrium (Chapter 4) and Epilogue to Part I

## L0 — One line
A Nash equilibrium is a set of choices in which each player's choice is a best response to correct beliefs about the others; it is the place to start analysing simultaneous-move games, but when there are several equilibria players also need a focal point or some other selection method, such as a convention, to reach one.

## L1 — The gist (≤ 120 words)
In simultaneous-move games each player must guess what the other will do, which leads to endless "I think that he thinks that I think…" reasoning. The chapter shows how Nash's equilibrium ends this circle. It shows how to find equilibria: by checking best responses, by successively eliminating dominated strategies, and by graphs when choices are continuous. Games with several equilibria (coordination, battle of the sexes, chicken) need extra devices such as focal points, commitment or convention. The authors judge the evidence for Nash equilibrium mixed but encouraging: start with Nash, then ask why outcomes may differ. The epilogue summarises Rules 1–4 for Part I.

**Prerequisites:** reading a payoff table; the idea of a dominant strategy (chapter 3); simple linear algebra (a line's intersection); halving a number repeatedly.

## L2 — Key ideas (5–10 bullets)
- A Nash equilibrium needs two conditions: each player best-responds to his beliefs, and the beliefs are correct. This squares the circle of "thinking about thinking" (pp. 110, 131–132).
- Best responses are formed against beliefs, not observed moves, since choices are simultaneous. Undercutting a rival is not always the best response (p. 109).
- Games can have several equilibria, and Nash theory alone does not choose one. A focal point is an equilibrium that is obvious ad infinitum, and it can depend on shared historical, cultural, linguistic or accidental experience (pp. 112–117).
- Battle of the sexes and chicken combine common and conflicting interests. Symmetric players can have asymmetric equilibria. Commitment, alternation or coin tosses can select among equilibria (pp. 118–121).
- Successive elimination of dominated or never-best-response strategies simplifies a game. If it leaves one outcome, that outcome is a Nash equilibrium (pp. 123–125).
- With continuous prices, equilibrium is where best-response lines cross. In the shirt game this is at $40 for each firm (pp. 126–127).
- Field and lab evidence is mixed. Allowing other-regarding preferences, learning from experience and focal points helps. The authors advise: start with Nash, then ask why outcomes may differ (pp. 127–131).
- In the "half" game, repeated best-responding-to-best-responses converges to 0. The authors' experience is that most people stop after two or three levels on a first go-around, but after a few plays players get very close to 0 (pp. 133–136).

## L3 — Walkthrough

### Big Game of Coordination (pp. 106–107)
- Fred and Barney can hunt rabbit alone, getting 1. If both hunt stag, or both hunt bison, a joint day's hunt yields six times a day's rabbit meat, so each hunter's share is 3 (p. 106). One alone on stag or bison cannot expect any success (p. 106); if the other goes to the other ground he gets nothing (p. 107).
- They forgot which big game they agreed on, and must choose simultaneously, in isolation (p. 106).
- Unlike the prisoners' dilemma, there is no dominant strategy. Each player's best choice depends on the other's (p. 107).
- Fred's reasoning is circular: he must guess what Barney thinks he, Fred, will do (p. 107).

### Squaring the Circle (pp. 107–112)
**Idea.** Nash's equilibrium looks for an outcome where each player's strategy is the best response to the other's. Then nobody wants to deviate alone (pp. 107–108).

**Pricing game, more prices.** Rainbow's End (RE) and B. B. Lean (BB) choose prices from $42 to $38 in $1 steps (p. 108).
- At $80 each sells 1,200 shirts. A one-dollar cut by one firm gains it 100 customers: 80 from the rival and 20 from elsewhere (p. 108).
- If both cut by $1, each gains 20 (p. 108).
- Both at $42: each gains $38 \times 20 = 760$, so sells 1,960. Profit is $22 \times 1{,}960 = 43{,}120$ (p. 108). (The text layer prints "(42 × 20)"; only $42-20=22$ gives 43,120.)

**Best responses (p. 109).**
- If RE believes BB charges $42, RE's best price is $41, with profit $43,260.
- RE's best response is $40 if it believes BB charges $41, $40 or $39, and $39 if BB charges $38.
- "Best response" here means best reply to a belief, not to an observed move, because choices are simultaneous.
- Undercutting is not always best. Cutting raises quantity but lowers the margin per shirt. If BB prices at cost ($20), matching it gives RE zero profit (p. 109).

**Nash equilibrium (p. 110).**
- One cell, both at $40, has both numbers as best responses; each firm earns $40,000.
- Each action is best given the belief about the other, and each belief is confirmed by the outcome. The authors say this "is just a definition of Nash equilibrium" (p. 110).
- The game is still a prisoners' dilemma. A credible, enforceable collusion at $80 gives $72,000 each instead of $40,000 (p. 110).
- With asymmetric costs the equilibrium prices can differ (Trip to the Gym 3: RE's cost falls to $11.60, BB's stays $20; p. 111).

**General remarks (p. 111).**
- Every game essentially has a Nash equilibrium if mixing of moves is allowed (Nash's theorem; mixing comes in chapter 5).
- Nash is a "guarded yes" as a solution concept.
- Equilibria are not always unique.

*Intuition note.* An equilibrium is a resting point of thinking: if both players were told the truth about the other's choice, neither would change. This is why it ends the circle.

**Which equilibrium? (pp. 111–112).**
- In the hunting game a player's best response is to make the same choice he believes the other makes. So there are three equilibria: Stag-Stag, Bison-Bison and Rabbit-Rabbit (pp. 111–112).
- Nash alone does not say which will occur. Something "prominent" is needed, such as a stag party or a farewell ritual such as "Be safe", which would favour rabbit (p. 112).
- Prominence must be multilevel: it must be obvious to Fred that it is obvious to Barney that it is obvious to Fred… If so, it is a **focal point** (Schelling) (p. 112).

**Focal-point examples (pp. 113–118).**
- *Meeting in New York* with no instructions about place or time: noon is the obvious time. Landmarks narrow the place. For Schelling's Boston/New Haven subjects, Grand Central's clock was focal (p. 113).
- In Nalebuff's TV experiment, six pairs of strangers chose noon. Three went to the Empire State Building and three to Times Square. All met, with some ingenuity (pp. 113–114).
- What matters is that the place is obvious to each that it is obvious to the others. If one team thought Times Square obvious and the other the Empire State Building, they would fail (p. 114).
- *Kreps's city-division game:* one student has Boston, the other San Francisco, and they divide nine other cities. A complete, non-overlapping split pays both; otherwise both get nothing (p. 114).
  - Every split is a Nash equilibrium, since any change by one creates an omission or an overlap: $2^9 = 512$ equilibria (p. 114). (The text layer prints "29".)
  - Americans or long-term U.S. residents split east/west of the Mississippi over 80 percent of the time. This was much less likely when a player was non-U.S. resident. Alphabetical splits had no clear dividing point, and nine cities cannot be split equally (p. 115).
  - Failure to find a focal point is a distinct possibility (p. 115).
- *Choose a positive integer:* both win if they match. The most frequent choice is 1, for mathematical reasons (p. 115).
- *Lost and Found* (linguistic reason). Germany and Switzerland deliberately build *Treffpunkt* meeting points (p. 115).
- *Keynes's beauty contest* is a metaphor for the stock market. The task is to pick the face most others will pick, not the most beautiful. Anything distinctive can become focal: red hair, a gap in the teeth, a mole (pp. 115–116).
  - The hot stock is the one that everyone thinks everyone else thinks is hot. Round numbers like 10,000 for the Dow are focal only because expectations can converge more easily on round numbers (p. 116).
  - So equilibrium can be set by whim or fad. High forecast earnings are one of many necessary but by no means sufficient conditions to anchor it (p. 116).
- The authors disagree with the many mathematical game theorists who want solutions fixed by abstract structure alone. They think it appropriate that outcomes depend on social and psychological aspects (p. 117).
- *Bargaining:* both sides want to avoid disagreement. A focal point, often 50:50 because it is simple and appears fair, lets expectations converge (p. 117).
- *CEO pay:* the "meeting place" is being above average. Every firm pays its CEO above last year's average, so everyone can think theirs is above average, and pay escalates. A new focal point is needed, but changing it "won't be easy" (p. 117).
- *Fairness:* the Millennium Development Goals and Sachs's book stress giving 1 percent of GDP. A percentage of income is focal, so richer countries owe more. Whether funds materialise "remains to be seen" (pp. 117–118).

*Intuition note.* A focal point works only if it is obvious to each player that it is obvious to the other, and so on. Shared culture, language or history can supply the hints that make one equilibrium stand out.

### Battles and Chickens (pp. 118–121)
**Battle of the sexes (pp. 118–120).**
- Original story: a husband wants the action film 300, a wife wants Pride & Prejudice. Each prefers either film in company to any film alone (p. 118).
- Hunting version: drop Rabbit. Fred gets 4 (instead of 3) from a joint stag hunt and Barney has the opposite preference (p. 118).
- Two Nash equilibria (Stag-Stag, Bison-Bison). Both prefer either to hunting alone, but they disagree on which is better (p. 119).
- If Fred can convey that he is credibly and unyieldingly determined to choose Stag, then Barney must make the best of it by complying. Two problems: Fred needs one-way communication, and it is hard to make unyielding determination credible, because Barney can test it. Chapter 7 returns to commitment (p. 119).
- With two-way communication it becomes a negotiation. In repeated play they can alternate. In a single play they can toss a coin to pick an equilibrium (pp. 119–120).

**Chicken (pp. 120–121).**
- Original story: two teenagers drive at each other, and the first to swerve is the "chicken". Both going straight is worst (p. 120).
- Hunting version: South is large but sparse (1 each if both go). North is plentiful but small: alone it gives 2, but if both go, both get 0 from fighting. A hunter going South while the other goes North gets only 1/2 because of envy (p. 120).
- Two equilibria, one North and one South. The one going South is the chicken (p. 120).
- Both games mix common and conflicting interests, and the conflict is sharper in chicken. If each tries to get his preferred equilibrium, both end up in their worst outcome (p. 121).
- Selection methods are as before: credible commitment (chapters 6–7), alternation in repeated play, or a coin toss (p. 121).
- Players symmetric in strategies and payoffs can have asymmetric equilibria (p. 121).

### A Little History (pp. 121–122)
- The hunters' meeting game is the **assurance game**, introduced by Rousseau. Fred best-responds to Barney's action, whereas in a prisoners' dilemma each has a dominant strategy. Fred would hunt stag if assured that Barney would (pp. 121–122).
- Rousseau's wording (Cranston's translation, a deer) can be read as saying each hunter's dominant strategy is the hare, making it a prisoners' dilemma. The game is more commonly read as an assurance game (p. 122).
- Chicken (from *Rebel Without a Cause*) was used for nuclear brinkmanship by Bertrand Russell and others, and analysed by Schelling (chapter 6). Battle of the sexes appears in Luce and Raiffa's *Games and Decisions* (p. 122).

### Finding Nash Equilibria (pp. 122–125)
- Worst case: inspect cells. A cell where both payoffs are best responses is a Nash equilibrium. Software can do this for big tables (p. 122).

**Successive elimination, using the shirt game (pp. 123–125).**
- BB will never choose $42 or $38 for two reasons (p. 123):
  1. **Dominated:** A is dominated by B if A is uniformly worse than B. BB's $42 profits are below its $41 profits for each of RE's five choices: 43,120 < 43,260; 41,360 < 41,580; 39,600 < 39,900; 37,840 < 38,220; 36,080 < 36,540. Likewise $38 versus $39 (pp. 123–124).
  2. **Never a best response:** $42 is never BB's best response to any RE price in the range (p. 124).
- Anything dominated is a never best response, but the converse fails. BB's $39 is a best response only to RE's $38. Since $38 is eliminated, $39 is never a best response to anything RE will play. So never-best-response eliminates strategies that are not dominated (p. 124).
- The same applies to RE. This leaves a 3-by-3 table (p. 124).
- In the 3-by-3 game $40 is dominant for each firm. In the original game it was not dominant: against BB's $42, RE's $41 gives $43,260 and $40 gives $43,200 (p. 125). So elimination can open the way to a second round (p. 125).
- If successive elimination leads to a unique outcome, that outcome is a Nash equilibrium. Otherwise it may only narrow the range (p. 125).

**RULE 3:** Eliminate dominated strategies and never-best-responses, and go on doing so successively (p. 125).
**RULE 4:** If that does not finish, search the cells for a pair of mutual best responses, which is a Nash equilibrium (p. 125).

*Intuition note.* Rule 3 rests on the belief that a rival will not play a dominated or never-best-response strategy. Each round of deletion uses the previous one.

### Games with Infinitely Many Strategies (pp. 125–127)
- If prices are continuous, plot RE's price on the X axis and BB's on the Y axis, and draw best-response lines (pp. 125–126).
- With $20 costs, the authors state (details omitted) that BB's best response is

$$\text{BB's best-response price} = 24 + 0.4 \times (\text{RE's price, or BB's belief about it}).$$

- Each $1 cut by RE leads BB to cut by only 40 cents, balancing lost customers against a lower margin. This is the flatter line (p. 126).
- RE's best response is the steeper curve. Where the two curves cross, each response is consistent with the other's beliefs. This is the Nash equilibrium at $40 for each (p. 126).
- (added step) Symmetry gives $p = 24 + 0.4p$, so $0.6p = 24$ and $p = 40$, matching the figure.
- The figure shows exactly one Nash equilibrium, so the unique equilibrium in the $1 table was not an artefact of discrete prices (p. 127).

### A Beautiful Equilibrium? (pp. 127–131)
**Argument for Nash (p. 127).**
- If an outcome is not a Nash equilibrium, some player is not best-responding and has a clear incentive to deviate. That destroys the proposed solution.
- With several equilibria one needs Nash plus something else. This does not contradict Nash.

**Testing theory (pp. 127–129).**
- Lab experiments give control over rules, costs and payment by profit. Their weaknesses are that subjects are usually students, many of them novices who must learn the game quickly, and the payments are usually small (pp. 127–128).
- Real-life data have experienced players and high stakes, but there are many uncontrolled factors and unknown costs and motives (p. 128). The authors conclude one should use both kinds of evidence (p. 128).
- Industrial organisation tests face many handicaps:
  - costs and demand must be estimated from the same data;
  - the form of demand is unknown;
  - competition has other dimensions, and managers' aims may not be pure profit maximisation;
  - there are dynamics, entry and exit, and randomness (p. 129).
- If the data fit poorly, one cannot conclude that Nash is wrong, since something else may be wrong. But one may rightly raise one's doubt about it (p. 129).
- Reiss and Wolak give a mixed verdict (the models are very complex, but attempts so far begin to define the issues). The authors read this as "more research is needed" (pp. 129–130).
- Auction estimation is already having considerable success; auctions come in chapter 10 (p. 130).

**Lab results (pp. 130–131).**
- Vernon Smith's markets gave surprisingly good results. Small numbers of traders, with no direct knowledge of others' costs or values, reached equilibrium exchanges quickly (p. 130).
- In ultimatum games offers were surprisingly generous. In prisoners' dilemmas good behaviour was more frequent than theory suggests. The authors read this as other-regarding preferences. With such preferences allowed, backward reasoning and Nash give generally good explanations (p. 130).
- With multiple equilibria, success depends on shared understanding. Otherwise disequilibrium may persist (pp. 130–131).
- Novices often converge to equilibrium with experience, but some uncertainty about the other remains. The quantal response equilibrium of McKelvey and Palfrey allows for this; the authors call it too technical for the book (p. 131).
- Holt and Roth: Nash equilibrium has become a required tool, and the basic analysis is the place to begin, and sometimes end, the analysis (p. 131). The authors agree. Begin with Nash, then think why the outcome may differ. They reject both "anything goes" and naïve adherence with added assumptions such as selfishness (p. 131).

### Case Study: Half Way (pp. 131–136)
**Two conditions (pp. 131–132).** A Nash equilibrium combines (i) each player best-responds to what he believes the others do, and (ii) beliefs are correct. Condition (i) is natural. The rub is (ii) (p. 132).

**Game.** Abe and Bea each pick a number from 0 to 100 inclusive. The player whose number is closest to half the other's wins $100. A tie splits the prize (p. 132).

**Reasoning (pp. 133–135).**
1. No best response exceeds 50. For example, 60 is a best response only if the other picks 120, which is impossible. So both pick in [0, 50] (p. 133).
2. Many novices stop there; the most common first response is 50. The authors call this "lame": it is best only if the other picks 100, which any lower number beats (p. 133).
3. Next, assume the other plays a best response. Then my best choice lies in [0, 25]. This is a best response to a best response (pp. 133–134). After 50, 25 is the most common guess (p. 134).
4. Next level: 12.5. The authors say most people do not think beyond two or three levels on a first go-around (p. 134).
5. Further levels: 6.25, 3.125, 1.5625, 0.78125 (pp. 134–135).
6. In general, if the other picks in [0, X], I pick in [0, X/2], and the other's best choice is in [0, X/4] (p. 135).

**Equilibrium.** The only way both can be right is both picking 0 (p. 135). If you pick 0 I want 0, and vice versa.
- If you pick X and I pick 0, I win, since 0 is closer to X/2 than X is to $0/2 = 0$ (p. 135).
- So here 0 beats any positive number the other picks (a tie if both pick 0), without knowing what the other does. This is an artefact of having two players (p. 135).

**Many players (pp. 135–136).**
- Now the winner is closest to half the average. 0 no longer always wins, but best responses still converge to 0. The levels are [0, 50], [0, 25], [0, 12.5], … (p. 135).
- Everyone picking 0 is the only profile where each best-responds and each is right about the others (p. 136).

**Evaluation (p. 136).**
- People rarely pick zero the first time. The authors call this convincing evidence against Nash's predictive power. After two or three plays they are very close to Nash, which they call convincing evidence in favor (p. 136).
- Authors' view: both are right. Best responses are straightforward, but correct beliefs are harder. Beliefs can be built by thinking or by playing, and learning drives convergence (p. 136).
- Experience is no guarantee with multiple equilibria. Example: after a dropped mobile call, both "you call, the other waits" and "you wait, the other calls" are equilibria. If both call, they get busy signals. People often turn to a convention, such as the original caller calling back, to resolve it (p. 136).

### Epilogue to Part I (pp. 137–138)
- A game is strategic interdependence among purposeful players. In zero-sum games, one's gain is always another's loss; more typically interests partly conflict and partly coincide (p. 137).
- Sequential games have a linear chain of reasoning and are studied with a game tree. **Rule 1:** look forward and reason backward (p. 137).
- Simultaneous games have a logical circle of reasoning that must be squared; the authors advise constructing a table of all combinations (p. 137).
  - **Rule 2:** if you have a dominant strategy, use it. If you have none but your rival does, count on his using it and best-respond (p. 137).
  - **Rule 3:** eliminate dominated strategies successively. If dominant strategies then emerge in the smaller game, choose them. This may give a unique solution or only shrink the game (p. 138).
  - **Rule 4:** look for an equilibrium of mutual best responses. A unique one has good arguments for being chosen. Many equilibria need a commonly understood rule or convention. If there is none, that usually means systematic behaviour can be exploited, which indicates the need to mix plays (chapter 5) (p. 138).
- Games with both sequential and simultaneous moves need a combination of techniques (p. 138).

## Toy example (ours, not from the text)
A 2×3 game. Payoffs are (Row, Column).

| | Left | Mid | Right |
|---|---|---|---|
| **Up** | (3, 3) | (1, 2) | (0, 0) |
| **Down** | (2, 1) | (0, 2) | (1, 0) |

1. Column's Right versus Left: Up row, 0 < 3; Down row, 0 < 1. So Right is dominated by Left. Delete it (Rule 3).
2. Row, now without Right: Up gives 3 and 1 against Left and Mid. Down gives 2 and 0. Up beats Down in each case, so Up is dominant in the smaller game. In the full game Up was not dominant, because against Right Up gives 0 and Down gives 1.
3. Column's best response to Up: Left 3, Mid 2, so Left.
4. The outcome (Up, Left) = (3, 3) is a Nash equilibrium. Up is Row's best response to Left (3 > 2), and Left is Column's best response to Up (3 > 2 > 0).
5. Check by cells (Rule 4). Each other cell has a profitable deviation:
   - (Up, Mid): Column prefers Left.
   - (Up, Right): Row prefers Down.
   - (Down, Left): Row prefers Up.
   - (Down, Mid): Row prefers Up.
   - (Down, Right): Column prefers Mid (2 > 0).

So (Up, Left) is the unique equilibrium. This is the chapter's point that elimination leading to a unique outcome gives a Nash equilibrium.

## Concepts
- [[best-response]] — the action that maximises your payoff given your belief about others' actions (pp. 109, 131) (new)
- [[nash-equilibrium]] — each player best-responds to beliefs about the others, and the beliefs are correct (pp. 110, 131–132)
- [[dominant-dominated-strategy]] — a strategy that is uniformly worse than another is dominated; it will never be used (p. 124)
- [[iterated-elimination-of-dominated-strategies]] — drop dominated and never-best-response strategies in successive rounds; a unique remainder is a Nash equilibrium (pp. 124–125)
- [[never-best-response]] — a strategy that is not a best response to anything the rival might choose; every dominated strategy is one, but not conversely (p. 124) (new)
- [[focal-point]] — an equilibrium that is obvious ad infinitum, so players' expectations converge on it (p. 112)
- [[convention]] — a commonly understood rule for choosing among equilibria, such as who calls back (pp. 136, 138)
- [[mutual-vs-common-knowledge]] — the "obvious that it is obvious that…" regress (p. 112)
- [[assurance-game]] — a game where each wants to do what the other does, if assured (pp. 121–122) (new)
- [[battle-of-the-sexes]] — two equilibria, with conflicting preferences between them (pp. 118–119) (new)
- [[chicken-game]] — two asymmetric equilibria; trying for one's preferred equilibrium leads to the worst outcome (pp. 120–121) (new)
- [[social-preferences]] — other-regarding preferences, used to explain ultimatum and dilemma experiments (p. 130)
- [[quantal-response-equilibrium]] — extension allowing uncertainty about the other's choice; only mentioned (p. 131)
- [[level-k-cognitive-hierarchy]] — most people, on a first go-around, stop after two or three levels of reasoning in the half game (pp. 134–135)
- [[mixed-strategy]] — mixing moves; needed for existence in general (pp. 111, 138)

## Canonical instances
- [[hunting-assurance-game]] — Fred and Barney's stag/bison/rabbit coordination (pp. 106–112)
- [[shirt-pricing-game]] — RE versus BB pricing: equilibrium $40, a prisoners' dilemma, elimination (pp. 108–110, 123–127)
- [[keynes-beauty-contest]] — a focal point as the stock-market metaphor (pp. 115–116)
- [[kreps-city-division]] — 512 equilibria; Mississippi split as focal point (pp. 114–115)
- [[new-york-meeting-game]] — noon, Grand Central, Empire State Building (pp. 113–114)
- [[half-way-number-game]] — halving iteration converging to 0 (pp. 132–136)
- [[dropped-call-game]] — wait versus call; a convention is often used to resolve it (p. 136)

## Bridges (candidates)
- [same-math] Rule 3 successive elimination ↔ decision-game-theory: iterated elimination of dominated strategies — the same procedure (p. 124).
- [same-math] Nash equilibrium as mutual best response ↔ decision-game-theory: Nash equilibrium — the same definition.
- [structural-analogy] Half-way game reasoning to 0 ↔ level-k / cognitive hierarchy: the authors say most people stop after two or three levels.
- [structural-analogy] Focal point of the beauty contest ↔ common knowledge: "obvious that it is obvious that…" has the same regress shape.
- [metaphor] Keynes's beauty contest ↔ stock-market behaviour: valuation by guessing others' guesses.

## Questions this raises
- What does mixing moves (chapter 5) change when no pure-strategy equilibrium exists?
- How can a player make a commitment credible so that his preferred equilibrium is chosen (chapters 6–7)?
- What explains the early, non-equilibrium play of novices, and how does quantal response model it?
- When do focal points exist, and could they be designed deliberately, as with *Treffpunkt* signs?

## Exercises worth doing
- Trip to the Gym no. 2 (p. 109) — build the shirt-game payoff table in a spreadsheet and see best responses — difficulty: easy.
- Trip to the Gym no. 3 (p. 111) — recompute with RE's cost at $11.60 and BB's at $20, then find the new equilibrium; the authors note equilibrium prices can differ across firms — difficulty: medium.
- Half-way game (pp. 132–133) — play the game, write down your number and compare to the iterated reasoning (the Case Discussion follows on p. 133) — difficulty: easy.

## Reading notes
- Printed page = pdf page (offset 0) throughout.
- Only the p. 123 image was supplied. Other payoff tables and graphs (pp. 106, 108, 111, 112, 118–120, 124–126) were not in the text layer, so payoffs for the hunting variants are drawn from the prose.
- The text layer shows "(42 × 20) × 1,960 = 43,120" on p. 108. The product only works as $(42-20)\times 1{,}960$, so the sign is probably a misprint or an extraction error; I could not check this against a page image.
- The text layer shows "29, or 512" on p. 114. It must be $2^9$.
- Footnote markers (*, †, numbers) appear in the text, but the footnote text is not in the supplied pages.
- In the shirt example, the 3-by-3 table and its dominance are described only in prose (pp. 124–125).
