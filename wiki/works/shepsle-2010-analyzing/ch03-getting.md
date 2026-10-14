---
id: shepsle-2010-analyzing/ch03-getting
work: shepsle-2010-analyzing
unit: "3 Getting Started with Group Choice Analysis"
pages: 41-52
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Getting Started with Group Choice Analysis

## L0 — One line
Even when every member has a complete, transitive preference ordering and votes sincerely, majority voting can give a cycling group preference, so the voting procedure (for example who sets the agenda) can decide the outcome.

## L1 — The gist (≤ 120 words)
How can a group of people with different preferences reach a choice? Shepsle uses three friends choosing an afternoon outing. With one set of preferences, a round-robin majority tournament (every option is voted against every other) gives a clear winner. After one friend changes his ranking, the group's majority preference becomes intransitive (it cycles). Then the result depends on institutions: with an agenda procedure, the agenda setter can obtain his favourite outcome. The chapter also shows that "the majority" is ambiguous, because there are many majorities, and that voters may vote sincerely (honestly) or strategically. It prepares the next chapters on majority rule, the spatial model, manipulation and other voting methods.

**Prerequisites:** Chapter 2's preference ordering (completeness, transitivity); counting simple majorities; factorials.

## L2 — Key ideas (5–10 bullets)
- In the example, preference diversity means the friends share no common first preference, so neither unanimity nor first-preference majority rule settles the choice, and they need another way to decide (p. 42, p. 46).
- A round-robin tournament pits each alternative against every other. An alternative that beats all others wins (p. 42–43).
- A group has many majorities, and different majorities may support the winner in different pairings. "The" majority is therefore ambiguous (p. 43).
- Voters may reveal preferences sincerely or strategically. To judge whether strategic voting is worthwhile, the author checks both feasibility (can my vote change the result?) and desirability (do I like the change?) (p. 43–44).
- Individuals with transitive preferences can form a group whose majority preference cycles (p. 47).
- An agenda procedure (pairwise votes in an order set by an agenda setter) gave Andrew great power in the example, where the group cycled. Other setters would have chosen other agendas and reached different outcomes (p. 48–49).
- Institutions matter: procedure can dramatically affect the group choice (p. 46, p. 50).

## L3 — Walkthrough

### Warm-up exercise (pp. 41–46)
Andrew, Bonnie and Chuck want to spend an afternoon together. Alternatives: Museum of Fine Arts (MFA), Walden Pond rally (WP), Red Sox game (RS) (p. 41). Individual rankings (Display 3.1, p. 42):

| A | B | C |
|---|---|---|
| MFA | WP | RS |
| WP | RS | WP |
| RS | MFA | MFA |

Each has complete, transitive preferences (p. 41). The group is *heterogeneous* in its preferences; this is "preference diversity" (p. 42).

- **Unanimity** and **first-preference majority rule** (each votes for the top choice) both fail, because the three first preferences differ (pp. 42, 45–46).
- **Round-robin tournament:** each alternative faces every other. If one beats all, it is the group choice. Otherwise "back to the drawing board" (pp. 42–43). Result (Display 3.2, p. 43):
  - MFA vs WP: WP wins 2–1 {B, C}
  - MFA vs RS: RS wins 2–1 {B, C}
  - WP vs RS: WP wins 2–1 {A, B}

  WP beats both others, so WP wins (p. 43).
- **Multiple majorities:** {A,B}, {A,C}, {B,C} and {A,B,C} are all majorities. Bonnie is the only common member of the coalitions behind WP (p. 43).
- **Sincere revelation:** each voted for the alternative he or she ranked higher. **Strategic (sophisticated) revelation:** voting against one's preference to do better overall (p. 43).

**Strategic incentives here (pp. 44–45).** Two questions: (1) feasibility, can someone shift the outcome by changing a vote? (2) desirability, would the shifted outcome be better for her or him? (p. 44)
- Feasibility holds: each pairing was decided by one vote (p. 44).
- Bonnie's first choice wins, so she has no reason to switch (p. 44).
- Andrew is pivotal only in WP vs RS. Switching would make RS the winner, his worst outcome, so he does not switch (p. 44).
- Chuck could change MFA vs RS, but this would not change the overall result. Changing both of the first two ballots would make MFA the winner, his worst outcome (p. 44 and note 2).
- If Chuck voted for MFA against WP in the first pairing, the tournament would have no winner. Whether this is rational depends on the rule for "no winner", which the author left unspecified. This is deferred to a later chapter (pp. 44–45). Conclusion: one friend *may* have an incentive to act strategically (p. 45).

Three lessons: multiple majorities; multiple forms of preference revelation; multiple ways to decide by voting (p. 45). The preferences lend themselves to round-robin voting at least as long as everyone votes sincerely; the author calls it fortunate that there were only three friends and three alternatives, so that, given their preferences, the tournament was easy to run and decisive (p. 46). With more people, alternatives or diversity it may not suit the group, and institutional features can be essential in determining the winner (p. 46).

*Intuition note:* "Take a vote" hides choices: which procedure, which majority, honest or not. Different choices may give different answers (the agenda example shows this for procedure).

### A revised example (pp. 46–49)
Claim: "Institutions matter"; the procedure affects the group choice dramatically (p. 46). The author adds a stage of debate and deliberation, which may look like window dressing but may sometimes change someone's preferences (p. 46). Suppose Chuck becomes convinced that a museum trip might be brief and that he might still catch the last innings of the game on TV, while the rally would go on all afternoon; he raises MFA above WP (pp. 46–47). New profile (Display 3.3, p. 47):

| A | B | C |
|---|---|---|
| MFA | WP | RS |
| WP | RS | MFA |
| RS | MFA | WP |

Round-robin (Display 3.4, p. 48): MFA beats WP {A,C}; WP beats RS {A,B}; RS beats MFA {B,C}. Each alternative loses to another: the group majority relation $P_G$ gives $RS\,P_G\,MFA\,P_G\,WP\,P_G\,RS$ (p. 47). This is not an ordering, since RS is at the top and bottom at once (note 4, p. 47). Individuals are transitive but the group is **intransitive**: its preferences *cycle*, with a different majority coalition in each pairing (p. 47).

*Intuition note:* Each pairwise contest has a majority winner, yet the results chase each other in a circle. No option can claim to be "the" majority choice.

**Agenda procedure** (p. 47–48; note 5 says the procedure is also used in sports under the name single-elimination tournament):
- An agenda setter (individual or subcommittee) assembles a voting order. In some organizations an especially powerful setter also proposes the items (p. 48).
- The first two items are voted on by majority rule. The loser is eliminated and the winner meets the next item. This repeats, and the survivor is the group choice (p. 48).
- For $k$ items there are $k\times(k-1)\times\cdots\times2\times1$ orderings. For $k=3$ that is $3\times2\times1=6$, but only three are substantively distinct. What matters is which alternative goes last, since the order within the first pair does not matter (p. 48, note 6).

Agendas (Display 3.5, p. 49): I = MFA, WP, RS; II = RS, MFA, WP; III = WP, RS, MFA.

Andrew (the oldest, so he sets the agenda) knows the others' preferences and assumes sincere voting. Using Display 3.4 (p. 49):
- Agenda I: MFA beats WP, then RS beats MFA, so the outcome is RS.
- Agenda II: RS beats MFA, then WP beats RS, so the outcome is WP.
- Agenda III: WP beats RS, then MFA beats WP, so the outcome is MFA.

Andrew picks III and gets his favourite, MFA (p. 49). If the tallest (Chuck) or the lightest (Bonnie) chose the agenda, then agenda I or II respectively would be chosen, with different group choices (p. 49).

*Intuition note:* When the majority relation cycles, the order of votes decides who survives. Whoever controls the order controls the result.

### Summary (pp. 49–50)
Even with honest revelation, the group can be "badly behaved" (intransitive) while its members are not. Shepsle cites Barry and Hardin's phrase "rational man and irrational society" (p. 50). What is best for the group, or even what a majority thinks best, is therefore not evident. Procedures are critical (p. 50). Roadmap: Ch. 4 majority rule and intransitivity; Ch. 5 spatial model; Ch. 6 manipulation (misrepresented preferences, agenda stratagems); Ch. 7 other ways to choose (p. 50).

## Toy example (ours)
Three voters, alternatives X, Y, Z. Voter 1: X>Y>Z; voter 2: Y>Z>X; voter 3: Z>X>Y.
- X vs Y: voters 1 and 3 prefer X, so X wins 2–1.
- Y vs Z: voters 1 and 2 prefer Y, so Y wins 2–1.
- Z vs X: voters 2 and 3 prefer Z, so Z wins 2–1.

So X beats Y, Y beats Z, Z beats X: a cycle, and no round-robin winner.

Agendas (sincere voting):
- (X, Y), then Z: X beats Y, then Z beats X, so Z wins.
- (Y, Z), then X: Y beats Z, then X beats Y, so X wins.
- (Z, X), then Y: Z beats X, then Y beats Z (voters 1, 2), so Y wins.

Each alternative wins under some agenda. Voter 1, who prefers X, would choose the agenda (Y, Z), then X.

## Concepts
- [[cycling-intransitivity]] — group majority preference that loops although each individual's is transitive (p. 47)
- [[agenda-control-agenda-setter]] — the agenda setter assembles the order of pairwise votes. The unit introduces it for the case where the round-robin has no winner (p. 47–49)
- [[strategic-sophisticated-voting]] — voting against one's preference to get a better outcome. Whether it pays is assessed by feasibility and desirability (p. 43–44)
- [[institutions]] — procedure for voting (round-robin, agenda procedure, who sets the agenda) — the author says "Institutions matter" (p. 46)
- [[condorcet-winner]] — an alternative that beats all others pairwise. The unit calls it the round-robin winner and does not use the term (p. 43)
- [[round-robin-tournament]] (new) — every alternative is paired against every other. A majority winner over all others is the group choice (p. 42–43)
- [[sincere-preference-revelation]] (new) — voting for the alternative one ranks higher in each pairing (p. 43)
- [[preference-diversity]] (new) — group members' differing rankings, the affliction that makes group choice difficult (p. 41–42)
- [[multiple-majorities]] (new) — a group contains many majority coalitions, so "the majority" is ambiguous (p. 43)

## Canonical instances
- [[boston-outing-warm-up]] — three friends, MFA/WP/RS: a clear round-robin winner (p. 41–43)
- [[boston-outing-cycle]] — Chuck's changed ranking creates a majority cycle (p. 46–48)
- [[agenda-power-andrew]] — Andrew's choice of agenda III yields MFA (p. 49)
- [[rational-man-irrational-society]] — Barry and Hardin's phrase (p. 50)

## Bridges (candidates)
- [structural-analogy] Majority cycle ↔ rock–paper–scissors: each option beats one and loses to another, so no option dominates.
- [structural-analogy] Agenda setter ↔ seeding in a single-elimination sports tournament: the bracket order shapes who wins (the text notes the sports analogy, p. 47).

## Questions this raises
- How common are majority cycles as the number of voters and alternatives grows? (Chapter 4 next, p. 50)
- If a cycle exists, are there agendas that let any alternative win, including ones a majority dislikes? (cf. Problem 3, p. 51)
- What should a tournament do when there is no winner, and how does that change incentives to vote strategically? (p. 45)
- Which preference restrictions rule out cycles? (spatial model, Chapter 5, p. 50)

## Exercises worth doing
- Ex. 1 (p. 50–51) — plurality vs round-robin with four plans, then with one plan removed — difficulty: easy
- Ex. 2 (p. 51) — find cycles, then see how one voter's changed mind creates or removes them — difficulty: medium
- Ex. 3 (p. 51) — design agendas for each voter's top choice, and ask whether a majority-favoured alternative can be defeated — difficulty: medium
- Ex. 4 (p. 51–52, starred) — strategic misrepresentation under a given agenda — difficulty: hard
- Ex. 5 (p. 52) — why transitivity matters for individuals versus groups — difficulty: easy

## Reading notes
- Printed page = pdf − 13 (pdf 54–65 are printed 41–52).
- OCR garbles some words (e.g. "Museum of F ine Arts", "round-r obin"). Display 3.4 is labelled "DISPLAY 8.4" in the OCR text; context shows it is 3.4.
- In the text layer of Problem 2 (p. 51), the preference orderings of i, j, k are missing, and the new ordering for k appears as ("tPksPkrPkq"), which reads $t\,P_k\,s\,P_k\,r\,P_k\,q$. The three original orderings are blank in the text layer, so Ex. 2–4 cannot be set up from the text layer alone (the page image should be consulted).
- Display 3.1 gives C's column as RS, WP, MFA (p. 42); this is consistent with the pairwise results in Display 3.2 (p. 43).
- Footnote 3 (p. 45) is a long aside on baseball rules; skipped.
