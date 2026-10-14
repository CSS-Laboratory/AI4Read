---
id: schelling-1960-conflict/ch07-randomization
work: schelling-1960-conflict
unit: "7 - Randomization of Promises and Threats"
pages: 202-216
fields: [decision-game-theory]
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
# Randomization of Promises and Threats

## L0 — One line
In games mixing conflict and common interest, randomization is not mainly about hiding one's strategy; its role is chiefly to make indivisible things divisible, which lets a threat or promise be "scaled down" when its full size would be too costly.

## L1 — The gist (≤ 120 words)
In zero-sum games (pure conflict), randomizing stops the opponent from predicting you. Schelling asks what randomizing does in mixed-motive games. His answer: it makes indivisible things, such as a too-large threat, divisible. A threat that is too harsh can be made fractional, carried out only with probability π. This lowers the cost of two risks: the threat failing, and the threat being fulfilled by accident. A commitment can also be randomized, and this can pay off. Schelling derives inequalities that bound π in his models. In his model, a certain threat can be not worth making while a fractional one is.

**Prerequisites:** expected value; probability; solving linear inequalities; reading a 2×2 payoff matrix.

## L2 — Key ideas (5–10 bullets)
- In zero-sum games randomization blocks the adversary's intelligence. In the traditional literature on mixed-motive games the main role is different: it is a device to make indivisible or incommensurate things divisible by lottery (pp. 202–203).
- A promise is costly when it succeeds; a threat is costly when it fails. So an oversized threat is often merely superfluous, while an oversized promise is a real loss (pp. 203–204).
- The risk that a threat fails gives a reason to scale it down by a lottery, since the punishment would then hurt both sides less often (pp. 205–206).
- In the Fig. 17 model, an effective fractional threat needs $\pi$ above $1/(1+X)$, and Row's gain falls as $\pi$ rises. So Row picks $\pi$ barely above that floor (pp. 207–208).
- Attaching probability π to the threat is, in this model, substantially equivalent to carrying out a fraction π of the penalty for certain. A difference is that lowering the probability cuts both players' expected losses proportionally, whereas a direct cut in size need not (pp. 210–211).
- Risk of inadvertent fulfillment gives a ceiling on π as well. Some threats, like the driver's, can only be made by starting to carry them out (pp. 211–213).
- A commitment can also be randomized, giving a fractional "first move". In the Fig. 18 example, a mixed commitment beats every pure one (pp. 213–216).

## L3 — Walkthrough

### Opening: the role of randomization (pp. 202–204)
- In zero-sum games, randomizing prevents the adversary from anticipating one's play and from exploiting regularities or inadvertent biases. In games mixing conflict and common interest it plays no such central role (p. 202).
- There, one is often more concerned that the other player anticipate one's mode of play correctly than with disguising it (p. 202).
- Zero-sum components can be embedded in a larger game. Examples are randomized aircraft sorties inside the limits of a limited war, and arms-control monitoring by sampling. Sampling lets each side learn enough to check compliance without learning so much that surprise attack becomes easier (pp. 202–203).
- The main traditional role is making indivisible objects divisible. Their expected values can be divided by lottery. Examples are coin flips, "double or nothing", and draft lotteries (p. 203).
- For promises, a lottery can scale down an oversized favor and so reduce its cost to the promiser (p. 203).
- **Promise vs threat:** a promise is costly when it succeeds; a threat is costly when it fails. A successful threat is one that is not carried out (pp. 203–204).
- Hence a threat that is "too big" is likely superfluous rather than costly. Tear-gas versus grenade: one could scale the grenade down by threatening a percentage chance of it going off. But the need is less clear than for a promise (p. 204).
- Size can matter if bigger threats cost more to equip, and the display of the weapon is needed. But for many threats the greatest cost is the risk of having to carry them out (p. 204).

*Intuition note:* A successful threat is one that is not carried out, so an oversized threat is likely superfluous rather than costly (though equipping may cost something). A successful promise is paid, so any excess is a loss. Oversizing is therefore clearly worse for promises, unless something might go wrong.

### The risk of failure (pp. 204–211)
- **Setup (Fig. 17):** Column moves first, then Row. Row may first commit to a threat. Without a threat, Column chooses II, expecting Row to choose i. Threatening row ii if Column chooses II makes II unattractive for both, so Column chooses I (p. 205). The Fig. 17 matrix is not visible in the pages I was given; its payoffs are inferred from the formulas on pp. 207–208:
  - Column gets 0 in I, 1 in (i, II) and $-X$ in (ii, II).
  - Row gets +1 if the threat succeeds, 0 in (i, II) and $-Y$ in (ii, II). Row gets 0 with no threat.
- **Why a threat may fail:** Row may have misjudged Column's payoffs, or Column may be a "deviant". The threat may not be communicated. Column may have committed to II first, or may be unable to choose I. Then the threat guarantees the worst outcome for both (pp. 205–206).
- With only pure threats, Row can merely wish the punishment were milder. If he can randomize (for example, a 50-50 chance between i and ii), he commits to row ii with probability $\pi$ if Column chooses II, and to row i with probability $1-\pi$. $P$ is the probability that the threat fails for any reason, taken as independent of Row's strategy (p. 206).
- **Effectiveness condition.** Column gets 0 from I. From II he gets a weighted average of 1 and $-X$, with weights $1-\pi$ and $\pi$. He is motivated to choose I if (p. 207):
$$0 > (1-\pi) - \pi X \iff \pi > \frac{1}{1+X}.$$
- **Row's expected value.** The threat succeeds with probability $1-P$, giving +1. It fails with probability $P$, giving a weighted average of 0 and $-Y$ (p. 207):
$$(1-P) + P(0-\pi Y) = 1 - P - P\pi Y .$$
- This is higher when $\pi$ is lower. So Row sets the lowest $\pi$ meeting the effectiveness condition (p. 207).
- **Worth making at all:** the value must exceed 0, which is Row's value with no threat (p. 208):
$$1-P-P\pi Y>0 \iff \frac{1-P}{P}\cdot\frac1Y > \pi .$$
- **Effective range** (p. 208):
$$\frac{1-P}{P}\cdot\frac1Y > \pi > \frac1{1+X}.$$
- **No threat worth making** if the range is empty, that is, if $\frac{1-P}{PY}<\frac1{1+X}$, or equivalently $\frac{P}{1-P} > \frac{X+1}{Y}$ (p. 208).
- **Only a fractional threat ($\pi<1$) is worth making** if $\frac{1-P}{PY}<1$ (p. 208). A further "or" form follows this on p. 209 but is not visible in the pages I was given [unreadable p. 209]. *(added step: this is equivalent to $PY > 1-P$.)*
- So the fractional threat can beat the certain threat, and the certain one may be not worth making at all (p. 209).
- **Caveat on $P$:** treating $P$ as independent of $\pi$ is "somewhat special". It implies a bimodal population: either payoffs as in the matrix, or payoffs so different that no threat up to $\pi=1$ deters. With a bell-shaped spread of adversary payoffs, success probability would rise with $\pi$. Burglars who steal for money versus for fun illustrate the two classes. Independence is more plausible if the failure is a communication breakdown (pp. 209–210).
- **Equivalence with scaling:** let $X$ be a maximum fine, number of lashes or days of prison that both parties suffer. Let $\pi$ be the fraction of it exacted for certain. The analysis and the conclusion are the same: $\pi$ as small as possible, with minimum $1/(1+X)$ (p. 210).
- Schelling says it seems fair to say that, in this case, randomization makes an otherwise too large, indivisible threat divisible. A caveat: a probability reduction cuts the expected outcome proportionately for both players, whereas a direct size reduction need not (pp. 210–211).

*Intuition note:* A smaller probability of punishment keeps the deterrent just strong enough for Column to comply, while limiting Row's loss in the cases where deterrence fails.

### The risk of inadvertent fulfillment (pp. 211–213)
- The threat may be carried out by accident even if the adversary complies. Examples are a gun going off early and a dog biting non-trespassers (p. 211).
- **Hitchhiker case:** the driver threatens to kill them both by speeding. The threat can only be made by starting to fulfil it, and some interval of risk is unavoidable. If the car were safe at all speeds below sixty but certain to skid off the road at exactly sixty, with no gradations between, the driver would have no incentive to risk a dangerous speed and the hitchhiker would not respond to a verbal threat. A "fractional threat" is what makes the threat possible (pp. 211–212).
- Suppose the risk of inadvertent fulfillment is $\alpha\pi$ (proportional to $\pi$), with the failure probability $P$ ignored. The minimum $\pi$ is unchanged. Row's expected value must exceed 0 (p. 212):
$$(1-\alpha\pi) - \alpha\pi Y>0 \iff \frac{1}{\alpha(1+Y)} > \pi > \frac1{1+X}.$$
- The optimal $\pi$ again barely exceeds the lower limit. The upper limit may be below 1. Whether a profitable $\pi$ exists depends on $X$, $Y$ and $\alpha$ (p. 213).

### Randomized commitments (pp. 213–216)
- A pure commitment gives the equivalent of first move. A randomized commitment is a "first move" fixed by a random device with odds chosen by the player. The other player knows the odds but not the move. To use it, Row must keep the right to move second and use only the right to commit in advance (p. 213).
- **Fig. 1 variant (pp. 213–214):** Row may commit before Column's choice but cannot make his choice depend on Column's. The matrix for Fig. 1 is not in the pages given. The figures below follow the text and assume Row gets 1 in the upper-left cell, 0 in the lower-left cell, and Column's payoffs are as in Fig. 17.
- A firm commitment to ii induces Column to choose I, but Row gets nothing in the lower-left cell. Row needs ii to induce I but needs i to profit from I (p. 214).
- **Coin-flip commitment:** Column chooses I if $X>1$, and Row's expected value is 0.5. Setting $\pi$ just above $1/(1+X)$ gives the largest expected value consistent with Column choosing I (p. 214).
- If Row's lower-left payoff were $-1$, no commitment with more than 50% on ii would serve. If it were $-X$ or worse, no mixture would work: any $\pi$ large enough to induce I would be too large to give Row a positive expected value (p. 214). *(added step: with payoff $-1$, Row's value is $(1-\pi)-\pi>0$ only if $\pi<0.5$.)*
- **Fig. 18** (Row's payoff first, then Column's; read from the image): (i,I) = 2, 4; (i,II) = 1, 1; (ii,I) = 3, 0; (ii,II) = 2, 2 (p. 215).
  - Every pure-strategy case gives Row 2. Commit to ii and Column chooses II. Commit to i and Column chooses I. No commitment leaves Column preferring II (pp. 214–215).
  - With a 50-50 mix, Column gets 2 in column I and 1.5 in column II, so he picks I. Row gets 2.5 (p. 215).
  - Row wants the largest $\pi$ (his probability of ii) that keeps Column in I (p. 215):
$$4(1-\pi) > (1-\pi)+2\pi \iff \tfrac35 > \pi .$$
  - This is a combination of a fractional threat (a high probability of i if II) with a fractional promise (the same probability of i if I) (p. 215).
- **Conditional probabilities:** if $\pi$ could depend on Column's choice, any probability up to 0.75 for ii after I would suffice. This assumes Row retaliates certainly with i after II (p. 216).
  - With one $\pi$ for both threat and promise: upper limit 0.6, Row gets 2.6 and Column 1.6.
  - With separate $\pi$ for the promise: upper limit 0.75, Row gets 2.75 and Column only 1.0 (p. 216).

*Intuition note:* Row cannot commit to "ii" (it wastes his gain) or to "i" (no inducement). Committing to a probability mix gets him between the two.

## Toy example (ours, not from the text)
Take the Fig. 17 structure with $X=3$, $Y=10$, $P=0.2$.
- Floor: $1/(1+X)=1/4=0.25$.
- Ceiling: $\frac{1-P}{PY}=\frac{0.8}{2}=0.4$. The range is $0.25<\pi<0.4$, and a fractional threat is worth making since $0.4<1$.
- Certain threat ($\pi=1$): $1-0.2-0.2\cdot1\cdot10=-1.2<0$, which is worse than no threat (0).
- Fractional threat, $\pi=0.3$: Column's value from II is $0.7\cdot1-0.3\cdot3=-0.2<0$, so he complies. Row gets $1-0.2-0.2\cdot0.3\cdot10=0.2>0$.
- $\pi=0.26$: Column's value from II is $0.74-0.78=-0.04<0$. Row gets $0.8-0.2\cdot0.26\cdot10=0.28$, which is better still.

## Concepts
- [[mixed-strategy]] — randomizing over actions; here the main role is making objects, promises and threats divisible, not mainly disguising play (p. 203)
- [[zero-sum-game-minimax]] — pure conflict, where randomization prevents the adversary's anticipation (p. 202)
- [[credible-commitment]] — binding oneself in advance. Here the commitment can be to a probability mixture (p. 213)
- [[expected-utility]] — the probability-weighted value used to compare threats (p. 207)
- [[fractional-threat]] (new) — a threat carried out only with probability $\pi<1$ (pp. 205–206)
- [[randomized-commitment]] (new) — a pre-announced lottery over one's later move (p. 213)
- [[risk-of-failure]] (new) — probability $P$ that a threat fails for any reason (p. 206)
- [[inadvertent-fulfillment]] (new) — risk, assumed proportional to $\pi$ and written $\alpha\pi$, that the threat is carried out by accident (p. 212)

## Canonical instances
- [[fig-17-threat-matrix]] — the model for the failure and inadvertent-fulfillment analysis (p. 205)
- [[fig-18-randomized-commitment]] — mixed commitment beats every pure one (p. 215)
- [[hitchhiker-driver-threat]] — a threat that can only be made by starting to fulfil it (p. 211)
- [[burglar-deterrence]] — a bimodal versus a bell-shaped population of adversaries (p. 209)
- [[draft-lottery]] — dividing the burden of citizenship by lottery (p. 203)

## Bridges (candidates)
- [structural-analogy] fractional threat probability $\pi$ ↔ mixed strategy: both are probability distributions over actions, but here the odds are meant to be learned by the other player.
- [metaphor] randomizing a threat to limit failure cost ↔ bias–variance trade-off: accepting a weaker, more moderate policy to reduce the cost of error.

## Questions this raises
- What if $P$ rises with $\pi$ (the bell-shaped case)? How would the optimal $\pi$ change?
- How can the other side verify that Row really commits to the odds $\pi$ and not to a pure move?
- Can a fractional threat be credible if carrying it out is costly for Row only after the threat has failed?
- When both players can randomize commitments, what happens to the "first move" advantage?

## Reading notes
- Printed page = pdf page − 1.
- The Fig. 17 and Fig. 1 matrices are not visible in the pages provided; their payoffs are inferred from the text's formulas. Fig. 18 was read from the image.
- The text layer writes "0" as "o". The curly-brace numbers (e.g. {97}) are endnote markers; the notes themselves are not in this unit.
- Printed p. 209 (pdf 210) had a text layer with blank formula slots and no image. The formulas on pp. 207–208, 212 and 215 were checked against their images.
