---
id: axelrod-1984-cooperation/ch03-chronology
work: axelrod-1984-cooperation
unit: Chapter 3 — The Chronology of Cooperation
pages: 55–69
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# The Chronology of Cooperation

## L0 — One line
Cooperation based on reciprocity can start in a world of unconditional defectors if cooperators arrive in small clusters, and once established it can be stable if the future matters enough and the rule is "nice" (never the first to defect) but provocable (it retaliates).

## L1 — The gist (≤ 120 words)
Chapter 2 showed TIT FOR TAT (cooperate first, then copy) winning tournaments. This chapter asks what happens once nearly everyone uses one strategy: can a rare newcomer strategy "invade"? It defines collective stability (no strategy can invade). It shows TIT FOR TAT is collectively stable if and only if the future weight w is large enough. Any strategy that may cooperate first needs a large enough w, and a nice (never first to defect) stable strategy must retaliate. ALL D (always defect) is always stable against single invaders, but a small cluster of TIT FOR TAT players can invade it. A nice strategy that resists single invaders also resists clusters. Cooperation can therefore emerge without central control.

**Prerequisites:** the iterated Prisoner's Dilemma with payoffs T, R, P, S; discount parameter w (probability or weight of meeting again); sums of geometric series; weighted averages.

## L2 — Key ideas (5–10 bullets)
- **Invasion and collective stability.** A rare newcomer strategy invades if it scores higher against natives than natives score against each other. A strategy is collectively stable if nothing can invade it. (p. 56)
- **Prop. 2.** TIT FOR TAT (cooperate first, then copy the other's previous move) is collectively stable if and only if w (the weight of the future) is large enough. The critical value depends on T, R, P, S. With T=5, R=3, P=1, S=0, the threshold is w = 2/3. (pp. 58–59)
- **Prop. 3 and 4.** Any strategy that may cooperate first is collectively stable only for large enough w. A nice strategy (one that is never the first to defect) must be provoked by the very first defection, meaning it must have some chance to defect in response on a later move, to be stable. (pp. 61–62)
- **Prop. 5.** ALL D (the rule that always defects) is always collectively stable against single invaders, whatever w, T, R, P, S. A lone cooperator finds nobody to reciprocate. (p. 63)
- **Clusters.** A small cluster of TIT FOR TAT players can invade ALL D if they meet each other often enough. In the example (w = .9) about 5% of their interactions suffice. (pp. 64–65)
- **Prop. 6.** Maximally discriminating strategies (they eventually cooperate, never again with ALL D once they have cooperated, and always with their own kind), such as TIT FOR TAT, invade ALL D with the smallest cluster. (p. 66)
- **Prop. 7.** If a nice strategy cannot be invaded by a single individual, it cannot be invaded by any cluster. This is an asymmetry between nice rules and ALL D. (p. 67)
- **Chronology.** Cooperation can begin in clusters, then resist invasion, and so emerge without central control. (pp. 68–69)

## L3 — Walkthrough

### Setting up the question (pp. 55–57)
Chapter 2 suggested TIT FOR TAT might eventually be used by virtually everyone. The question: would anyone then want to switch? (p. 55)

**Invasion (Maynard Smith's approach, as used by Axelrod).** Imagine a whole population using one "native" strategy and a single mutant using another. The mutant meets only natives, and natives almost surely meet natives. So the new strategy **invades** if the newcomer scores higher with a native than a native scores with another native. This is the same as the mutant beating the population average. (p. 56)

**Collectively stable:** no strategy can invade it. (p. 56)

Why it matters:
- *Biology:* payoffs are read as fitness, and all mutations are possible. So only a collectively stable strategy is expected to be maintained by everyone in the long run (p. 56).
- *People:* a better strategy may be found by deliberation, trial and error, or luck. So only a strategy that cannot be invaded can be maintained by everyone (p. 57).
- *Warning:* the definition assumes that those trying novel strategies do not interact much with one another. If they interact in clusters, "new and very important developments are possible" (p. 57).

Finding all collectively stable strategies is hard. The author says a full characterization exists in Appendix B. Here he only tests particular strategies (p. 57).

*Intuition note:* "Stable" means "no single outsider can do better by deviating." It is a test against every possible rare deviator.

### Proposition 2: when TIT FOR TAT is stable (pp. 57–60)
TIT FOR TAT cooperates first, then copies the other player's previous move. A population of TIT FOR TAT players gets R per move. An invader must get more than R in expectation (pp. 57–58).

Argument:
1. An invader must defect at some point, since otherwise it gets only R. Its first defection earns T, the highest payoff, but TIT FOR TAT then retaliates (p. 58).
2. TIT FOR TAT remembers only one move. So the best challenger repeats some sequence, and a sequence of at most two moves is enough. The candidates are alternating D and C, or DD (which is ALL D) (p. 58).
3. Both challengers beat R on the first move and do worse than R on the second. They benefit from settings where the future matters little. If neither can invade, no strategy can (p. 58).

**Proposition 2.** TIT FOR TAT is collectively stable if and only if w is large enough. The critical value is a function of T, R, P and S. The proof is in Appendix B, which is not part of this unit (p. 59).

**Example (author's).** With T=5, R=3, P=1, S=0, TIT FOR TAT is collectively stable if the next move is at least 2/3 as important as the current one. Below that value, defecting on alternate moves pays against TIT FOR TAT. If w < 1/2, always defecting pays (p. 59).

*Intuition note:* A defection earns T at once, but TIT FOR TAT then retaliates. If the future is weighted heavily enough, the losses from retaliation outweigh the gain.

**Illustrations of "the future matters" (author's examples, p. 59–60):**
- Caesar on Pompey's allies: they saw his prospects as hopeless, and friends became enemies in adversity (p. 59).
- A failing business sells its receivables to a factor at a steep discount. Mayer says the "continuing relationship" is the enforcer of commercial morality, and it is lost when a firm is failing (p. 60).
- A member of Congress seen as likely to lose the next election may find legislative trust harder (p. 60).
- Reciprocity is easier in a stable small town or ethnic neighborhood. A visiting professor is likely to be treated worse than regular colleagues (p. 60).
- **World War I trenches.** The "live-and-let-live system": between large battles each side avoided harming the other, provided the other reciprocated. Sometimes the rule was not TIT FOR TAT but two for one. A British officer reports a French code: fire two shots for every one received, but never fire first (pp. 60–61). The whole next chapter is devoted to this.

### Propositions 3 and 4: strategies that may cooperate, and nice strategies (pp. 61–62)
**Proposition 3.** Any strategy which may be the first to cooperate can be collectively stable only when w is sufficiently large (p. 61).

Reason, in key steps (formal proof in Appendix B):
- ALL D is one possible challenger.
- If the native strategy ever cooperates, ALL D gets T on that move.
- The native average can be at most R per move.
- So the interaction must last long enough for the temptation gain to be cancelled over later moves (pp. 61–62).

A **nice** rule is one that is never the first to defect. TIT FOR TAT and two-for-one are both nice. Nice rules get the highest score possible in a single-strategy population: R each move (p. 62).

**Proposition 4.** For a nice strategy to be collectively stable, it must be provoked by the very first defection of the other player. This means that on some later move it must have a finite chance of defecting in response. Reason: if a nice strategy were not provoked by a defection on move n, a rule that defected only on move n could invade it (p. 62).

*Intuition note:* A nice rule can be collectively stable only if it can retaliate: if it ignored a defection on move n, a rule that defected only on move n could invade it.

### Proposition 5: ALL D (p. 63)
**Proposition 5.** ALL D is always collectively stable, whatever w and T, R, P, S (p. 63).

Reason: if the others surely defect, a cooperative choice yields only S, with no later compensation. ALL D players get P per move, and no one can do better. So a world of "meanies" resists invaders who arrive one at a time. A lone newcomer has nobody to reciprocate. Newcomers arriving in small clusters, however, can get cooperation started (p. 63).

### Invasion by clusters (pp. 63–66)
**Author's numerical example** (T=5, R=3, P=1, S=0, w=.9; p. 63–64):

| Pairing | Per-move payoffs | Cumulative score |
|---|---|---|
| ALL D vs ALL D | P each turn | 10 |
| TIT FOR TAT vs ALL D (TFT's score) | 0 on move 1, then 1 | 9 |
| TIT FOR TAT vs TIT FOR TAT | 3 each move | 30 |

If a TIT FOR TAT player has proportion p of its interactions with other TIT FOR TAT players, its average score is
$$30p + 9(1-p).$$
It pays to use TIT FOR TAT if this exceeds 10, since ALL D natives meet almost only each other and get 10. The author says this holds even if only 5 percent of interactions are with other TIT FOR TAT players (p. 64).

*(added step)* $30p + 9 - 9p > 10 \iff 21p > 1 \iff p > 1/21 \approx 4.8\%$.

*Intuition note:* Against a meanie TIT FOR TAT scores 9, one point less than the 10 meanies get with each other. Against a twin it scores 30, which is 20 more. So enough meetings with twins can make up for the small loss against meanies.

**Illustration (p. 65).** If a business school taught students to start cooperating and to reciprocate, and they did not disperse too widely, their lessons would pay off. A firm needs only 5% of its interactions with another such firm in the example.

**Longer games need less clustering (p. 65):**
- Median game length 200 moves (w = .99654): one interaction in a thousand with a like-minded TIT FOR TAT player is enough.
- Median length 2 moves (w = .5): anything over a fifth is enough.

**General definition of cluster invasion (pp. 65–66).** A new strategy is used by a small group. Let p be the proportion of a newcomer's interactions that are with other newcomers.
- Newcomer's average score = p·(score with a newcomer) + (1−p)·(score with a native).
- Native's average score ≈ score of a native with a native, since newcomers are rare.
- The cluster invades if newcomers do well with each other and meet each other often enough (p. 66).

This assumes pairing is not random. With random pairing a newcomer would rarely meet another newcomer (p. 66).

**Maximally discriminating strategy:** it eventually cooperates even if the other has never cooperated yet. Once it cooperates, it never cooperates again with ALL D. It always cooperates with another player using the same strategy (p. 66).

**Proposition 6.** The strategies that can invade ALL D in a cluster with the smallest p are the maximally discriminating ones, such as TIT FOR TAT (p. 66).

TIT FOR TAT qualifies: it cooperates on the first move, never cooperates again with ALL D after that, and cooperates without a break with another TIT FOR TAT (pp. 66–67).

### Proposition 7: an asymmetry (pp. 67–68)
**Proposition 7.** If a nice strategy cannot be invaded by a single individual, it cannot be invaded by any cluster either (p. 67).

Reason: a clustered strategy's score is a weighted average of (a) its score with its own kind and (b) its score with the predominant strategy. Both are ≤ the score of the predominant nice strategy, which gets R against its own kind, the highest possible. Hence if single invaders fail, so do clusters (p. 67).

So ALL D can be invaded by clusters, but a nice rule that resists single nice invaders resists clusters of any size. "Nice rules can protect themselves in a way that meanies cannot" (p. 68).

*Intuition note:* Nice rules can protect themselves against clusters because they get R per move with their own kind, the highest score possible. ALL D has no such protection: clusters can invade it.

### The chronological picture (pp. 68–69)
- **Senate illustration (author's, tentative):** without clustering or a comparable mechanism, early "treachery" could not have been overcome (Prop. 5). The author says "perhaps" the early clusters were boardinghouse groups (Young 1966), or "perhaps" state and party delegations (Bogue and Marlaire 1975). Once reciprocity is established, Prop. 7 says it survives a cluster of newcomers who ignore it. Props. 2 and 3 say it is collectively stable as long as the biennial turnover rate is not too great (p. 68).
- **Summary:** cooperation can emerge in a world of unconditional defection if tried by small clusters of discriminating individuals with at least a small share of interactions among themselves. Scattered individuals fail. Once nice strategies are adopted by virtually everyone, they can protect themselves against clusters of any other strategy, but to be stable they must be provocable (pp. 68–69).
- Mutual cooperation can emerge among egoists without central control, starting from a cluster relying on reciprocity. The next chapters test this on wartime trenches and on biology (p. 69).

## Toy example
*(Ours; same payoffs T=5, R=3, P=1, S=0, but w = .5.)*

A move's value is weighted by w^(move number − 1), so a payoff stream x per move for ever is worth x/(1−w) = 2x here.
- ALL D vs ALL D: P=1 forever → 1×2 = 2.
- TFT vs ALL D: 0 on move 1, then 1 forever → 0 + 0.5×1/(1−0.5) = 1.
- TFT vs TFT: 3 forever → 3×2 = 6.

A cluster member with proportion p of encounters with twins averages 6p + 1(1−p) = 1 + 5p. The ALL D natives get 2. Invasion succeeds if 1 + 5p > 2, i.e. p > 1/5. This matches the text's "over a fifth" at w = .5 (p. 65).

Check of Prop. 2 at w = .6 (threshold 2/3): TFT vs TFT = 3/(0.4) = 7.5. ALL D against TFT = 5 + 0.6×1/0.4 = 6.5 < 7.5, so ALL D fails. Alternating D, C against TFT earns 5 + 0w per two moves → 5/(1−0.36) = 7.81 > 7.5, so it invades. This is below 2/3, so TFT is not collectively stable, and only alternating invades.

## Concepts
- [[evolutionarily stable strategy]] — closest canon term; here the author's own term is "collectively stable": no strategy can invade it (p. 56). The text does not use the word "ESS". See [[collective-stability]] (new).
- [[collective-stability]] (new) — a strategy that no newcomer strategy can invade, tested against single mutants (p. 56).
- [[invasion]] (new) — a rare newcomer scores higher with natives than natives score with each other (p. 56).
- [[shadow of the future]] — the weight w on future moves; stability of reciprocity needs it large enough (p. 59).
- [[nice-strategy]] (new) — a strategy that is never the first to defect (p. 62).
- [[provocability]] (new) — a nice strategy that must respond to the first defection with a defection on some later move (p. 62).
- [[cluster-invasion]] (new) — newcomers invade when a proportion p of their interactions is with each other (pp. 65–66).
- [[maximally-discriminating-strategy]] (new) — cooperates eventually, never again with ALL D after cooperating, always with its own kind (p. 66).
- [[repeated game & folk theorem]] — the setting is the iterated Prisoner's Dilemma. The text states no folk theorem (p. 57).

## Canonical instances
- [[tit-for-tat]] — cooperate first, then copy; stable for large w (pp. 57–59).
- [[all-d]] — always defect; always collectively stable but invadable by clusters (pp. 63–66).
- [[wwi-live-and-let-live]] — trench cooperation, e.g. "two for one" (pp. 60–61).
- [[factor-and-failing-business]] — customers stop paying when future dealings vanish (p. 60).
- [[pompey-allies]] — allies defect once prospects look hopeless (p. 59).
- [[us-senate-reciprocity]] — cooperation among legislators via clusters, tentatively (p. 68).

## Bridges (candidates)
- [structural-analogy] collective stability (no single invader succeeds) ↔ evolutionary game theory: evolutionarily stable strategy — similar resistance-to-mutants idea; the text does not claim identity.
- [metaphor] cluster invasion of ALL D ↔ network reciprocity: cooperators who meet each other locally thrive.
- [structural-analogy] provocability of nice strategies ↔ credible commitment: a threat to retaliate must be real to deter exploitation.

## Questions this raises
- How does the critical w depend on T, R, P, S in general (Appendix B)?
- If pairing is non-random in real populations, what makes clusters form?
- Which other strategies are collectively stable besides TIT FOR TAT and ALL D?
- Does the two-for-one rule, or a rule that only responds sometimes, need a larger w than TIT FOR TAT?

## Reading notes
- Printed page = pdf − 8.
- Proofs of Propositions 2 and 3 are referred to Appendix B (pp. 59, 62), which is not in these pages. For Propositions 4–7 only the author's informal reasons are given here. The endnotes (marked 1–9 in the text) are also not in these pages.
- Typos in the source: "each will each get" (p. 63); "(or. some comparable mechanism)" (p. 68). The text prints "alternative moves" (p. 59), apparently where "alternate moves" is meant.
- Payoffs T, R, P, S (temptation, reward, punishment, sucker's) are named on p. 63; the payoff matrix, figure 1, is referenced on pp. 59 and 63 ("on page 8") but is not in this unit.
- The author's "5 percent" (p. 64) is consistent with the break-even value 1/21 ≈ 4.8% computed in the added step.
