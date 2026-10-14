---
id: kahneman-2011-thinking/ch29-fourfold
work: kahneman-2011-thinking
unit: 29 The Fourfold Pattern
pages: pdf 302–313 (printed page numbers unknown)
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# The Fourfold Pattern

## L0 — One line
People weight outcomes by "decision weights" that are not their probabilities (small chances are overweighted, near-certainty is underweighted), and combined with gain/loss thinking this produces four typical attitudes to risk.

## L1 — The gist (≤ 120 words)
Rational-choice theory says an outcome's weight should equal its probability. Kahneman shows that people do not do this. Unlikely outcomes get too much weight (the possibility effect). Near-certain outcomes get too little (the certainty effect). Allais's paradox shows the effect in choices. Together with valuing gains and losses, this gives the fourfold pattern: risk aversion for likely gains and unlikely losses, risk seeking for unlikely gains and likely losses. It explains lotteries, insurance, desperate gambles and legal settlements. Over many repeated decisions, such deviations from expected value are likely to be costly.

**Prerequisites:** expected value (probability-weighted average); the idea of a utility/value of money; gains vs. losses.

## L2 — Key ideas (5–10 bullets)
- Expectation principle: weight each outcome by its probability. Kahneman calls it poor psychology (pdf 302–304).
- The possibility effect overweights very unlikely outcomes. The certainty effect underweights near-certain ones relative to sure things (pdf 303).
- Allais's paradox: most people prefer the 61%/$520,000 gamble in problem A but the sure $500,000 in problem B. This is inconsistent with utility theory (pdf 304–305).
- Prospect theory keeps utility theory as the logic of rational choice but describes real choices, with decision weights that differ from probabilities. Table 4 measures them (pdf 306).
- Fourfold pattern: gains likely → risk averse; gains unlikely → risk seeking; losses unlikely → risk averse; losses likely → risk seeking. The last cell was the surprise (pdf 309–310).
- Legal bargaining follows the pattern: a defendant with a weak case is likely to be risk seeking, and against a risk-averse plaintiff with a strong case the defendant holds the stronger hand. A plaintiff with a frivolous claim is likely to get more than the statistics justify (pdf 311–312).
- Over many similar cases, deviating from expected value is likely to be costly. The New York example shows this (pdf 312).

## L3 — Walkthrough

**Opening: weights in global evaluations (pdf 302).** Any global judgment of a complex object assigns weights to its characteristics. This is done by System 1, with or without awareness. For uncertain prospects, the weights are correlated with probabilities.

**Changing Chances (pdf 302–304).**
- The expected value of a gamble is the average of its outcomes, each weighted by its probability. Example: "20% chance to win $1,000 and 75% chance to win $100" has expected value $275 (pdf 302). (Added step: $0.20\times1000+0.75\times100=200+75=275$.)
- Bernoulli kept this weighting (the *expectation principle*) but applied it to the psychological value of outcomes. A gamble's utility is the probability-weighted average of the utilities of its outcomes (pdf 302).
- Test: chances of winning $1 million improve by 5 points in four cases: 0→5%, 5→10%, 60→65%, 95→100%. The principle says each adds exactly 5% of the utility of $1 million. Kahneman says this does not match experience (pdf 303).
- 0→5% and 95→100% feel more impressive. 0→5% creates a possibility, a hope: the *possibility effect*. Highly unlikely outcomes are weighted more than they "deserve." Lottery buyers pay much more than expected value (pdf 303).
- 95→100% is the *certainty effect*: almost-certain outcomes get less weight than their probability justifies (pdf 303).
- Example: you have a 95% chance to win a $1 million inheritance case, and expected value is $950,000. A company offers $910,000 now, $40,000 below expected value. Kahneman asks whether you are quite sure you would reject it. "Structured settlements" exploit this (pdf 303).
- In losses: a 5% risk of amputation is much worse than half of a 10% risk. People tend to overweight small risks and are willing to pay far more than expected value to eliminate them. The difference between a 95% risk and the certainty of disaster appears to be even greater, because the "sliver of hope" looms very large (pdf 303).
- Conclusion: decision weights are not identical to probabilities. Improbable outcomes are overweighted, and almost-certain ones are underweighted relative to actual certainty (pdf 304).
- Von Neumann and Morgenstern (1944) derived the expectation principle from axioms of rational choice. The text says they proved that any weighting not strictly proportional to probability leads to inconsistencies (pdf 304).

*Intuition note:* There is a tension. The theory of rational choice says to weight by probability, but real feelings do not. The next section shows a case where this causes an actual logical inconsistency.

**Allais's Paradox (pdf 304–306).**
- At a 1952 Paris meeting, Allais presented questions to leading economists. He wanted to show that they were susceptible to the certainty effect and so violated expected utility theory (pdf 304).
- Simplified version (pdf 304):
  - A: 61% to win $520,000 **or** 63% to win $500,000.
  - B: 98% to win $520,000 **or** 100% to win $500,000.
- Most people prefer the left option in A and the right (sure) option in B. Kahneman calls this a violation of rational choice (pdf 305).
- Urn argument: picture a 100-marble urn where red wins. B's urns are A's urns with 37 white marbles replaced by red in each (added step: $61+37=98$, $63+37=100$). Each added red marble is worth $520,000 on the left and only $500,000 on the right. So the left urn improved more, yet people switch to the right (pdf 305).
- Psychological explanation: the 2-point gap between 100% and 98% is much more impressive than the same gap between 63% and 61%. Kahneman calls this the certainty effect (pdf 305).
- The participants did not notice the inconsistency until Allais pointed it out at the end. Economists who were not decision theorists mostly ignored it as an anomaly. Decision theorists took it seriously (pdf 305–306).
- Most theorists, including Allais, tried to make the Allais pattern "rational" (Amos's name for them: "lawyers for the misguided"). Kahneman and Tversky kept utility theory as the logic of rational choice and built a psychological theory of actual choices, prospect theory (pdf 306).

**Decision Weights (pdf 306–308).**
- Table 4 (gains; probability % → decision weight): 0→0, 1→5.5, 2→8.1, 5→13.2, 10→18.6, 20→26.1, 50→42.1, 80→60.1, 90→71.2, 95→79.3, 98→87.1, 99→91.2, 100→100 (pdf 306, image).
- Weights equal probabilities at 0 and 100. Near those points they depart sharply. A 2% chance gets weight 8.1 instead of 2, overweighted by a factor of 4. A 2% risk of *not* winning cuts the gamble's utility from 100 to 87.1, i.e. by 13% (pdf 306).
- The certainty effect is called "even more striking." Anxiety over a 1% chance of losing a nearly sure $1 million seems more salient than hope from a 1% chance of winning. The same holds for surgery (pdf 307).
- From 5% to 95%, weights range only from 13.2 to 79.3, which the author says is about two-thirds of the range rationally expected. So people are insensitive to intermediate probabilities. Brain regions respond to probability in a way similar to the estimated weights (pdf 307).
- Below 1% or above 99% is a special case. Very rare events may be ignored (weight 0) or, if attended to, overweighted. People are almost insensitive to differences among tiny risks: 0.001% versus 0.00001% would mean 3,000 versus 30 cancers in the US (pdf 307).
- Worry is not proportional to probability. To remove the worry, the risk must reach zero (pdf 307).
- Insect-spray survey of parents: risks (15 inhalation and 15 child poisonings per 10,000 bottles) cut to 5. Parents would pay $2.38 extra for the reduction, and $8.09 (more than three times as much) to eliminate the risk. This is a "certainty premium," compatible with the psychology of worry but not with the rational model (pdf 307–308).

*Intuition note:* A decision weight is how much a possible outcome counts in your head. Near 0% and 100% it is distorted most. The middle of the scale is flattened.

**The Fourfold Pattern (pdf 308–310).**
- Prospect theory's two conclusions: people attach values to gains and losses rather than to wealth, and decision weights differ from probabilities. In combination they explain the *fourfold pattern* (pdf 308).
- Figure 13 rows: illustrative prospect; focal emotion; behaviour when choosing between a gamble and a sure amount equal to its expected value (risk averse if the sure thing is preferred, risk seeking if the gamble); attitudes of defendant and plaintiff in settlement (pdf 309).
- The cells, as described in the text (pdf 309):
  - Top left (substantial chance of a large gain): risk averse; people accept less than expected value to lock in the gain.
  - Bottom left (very small chance of a large gain): lotteries; the possibility effect. A ticket buys "the right to dream pleasantly of winning."
  - Bottom right (small chance of a disaster): insurance, bought for more than expected value; it buys peace of mind.
  - Top right (high chance of a large loss): the new, unexpected cell. People are risk seeking here (pdf 309–310).
- Two reasons for risk seeking over losses (pdf 310):
  1. Diminishing sensitivity: a $900 loss feels more than 90% as bad as a $1,000 loss, so the sure loss is very aversive.
  2. The weight for 90% probability is only about 71, so the gamble's bad outcome is underweighted.
- The same two factors favour the sure thing for gains. In the bottom row they oppose each other. Diminishing sensitivity favours risk aversion for gains and risk seeking for losses. The overweighting of low probabilities overcomes this, giving gambling for gains and caution for losses (pdf 310).
- Top-right examples: desperate gambles, firms losing to a superior technology, and the losing side in wars fighting on. These often turn manageable failures into disasters (pdf 310).

*Intuition note:* Two forces work at once: how much each outcome matters (value of gains and losses), and how much the chance counts (decision weight). For common events they point the same way. For rare events they conflict, and the weight wins.

**Gambling in the Shadow of the Law (pdf 311–312).** (Chris Guthrie's application.)
- Strong plaintiff (95% to win; offered 90% of the claim): top left. Sure gain plus fear of disappointment and regret typically leads to cautious behaviour; the plaintiff with a strong case is likely to be risk averse (pdf 311).
- Weak defendant (must pay 90% of the claim in settlement, or hope to win): top right. A defendant with a weak case is likely to be risk seeking, prepared to gamble (pdf 311).
- Facing a risk-averse plaintiff, the defendant holds the stronger hand; the prediction is that the plaintiff settles for less than the statistically expected outcome. Experiments with law students and judges, and analyses of actual negotiations, confirmed this (pdf 311).
- Frivolous suit: bottom row. The plaintiff holds a lottery ticket and is aggressive. The defendant, overweighting a small chance of a large loss, treats settlement as insurance. Plaintiffs with frivolous claims likely get more than the statistics justify (pdf 311–312).
- These attitudes are "not obviously unreasonable," but in the long run deviations from expected value are likely to be costly. Example: New York faces 200 frivolous suits a year, each with a 5% chance to cost $1 million, or can settle for $100,000 each (legal costs ignored). Litigating loses 10 cases, $10 million. Settling all costs $20 million (pdf 312).
- The rule applies to all cells and to both risk aversion and risk seeking. Consistent overweighting of improbable outcomes eventually leads to inferior outcomes (pdf 312).

**Speaking of the Fourfold Pattern (pdf 313).** Four sample remarks. Settling a frivolous claim out of fear of a freak loss is overweighting of small probabilities, and someone facing many similar problems would be better off not yielding. Paying for certainty on vacations is a certainty premium. Refusing to cut losses while there is a chance of breaking even is risk seeking in losses. Wanting a tiny gas-explosion risk mitigated is a possibility effect and a wish for peace of mind.

## Toy example (ours)
Use Table 4 weights and, for simplicity, treat money value as linear (an added simplification; the text says diminishing sensitivity also matters). Table 4 is estimated for gains; reusing it for losses follows the text's use of "about 71" for 90% in the loss discussion (pdf 310).
- Gain, likely: 98% chance of $1,000 versus $950 sure. Expected value 980 > 950. Weighted: $0.871\times1000=871 < 950$, so the sure thing wins (risk averse, top left).
- Gain, unlikely: 2% chance of $1,000 versus $20 sure. Expected value 20. Weighted: $0.081\times1000=81 > 20$, so the gamble wins (lottery, bottom left).
- Loss, likely: 90% chance of losing $1,000 versus a sure loss of $900. Expected value of the gamble: $-900$. Weighted: $0.712\times(-1000)=-712 > -900$, so the gamble feels better (risk seeking, top right).
- Loss, unlikely: 2% chance of losing $1,000 versus a sure loss of $20 (insurance). Weighted: $0.081\times(-1000)=-81 < -20$, so the sure loss is preferred (bottom right).

## Concepts
- [[expected utility]] — a gamble's utility is the probability-weighted average of its outcomes' utilities (the "expectation principle") (pdf 302)
- [[probability weighting]] — decision weights differ from probabilities: small ones overweighted, near-certain ones underweighted (pdf 304, 306)
- [[decision-weight]] (new) — the weight an outcome gets in the evaluation of a prospect; measured in Table 4 (pdf 306)
- [[possibility-effect]] (new) — highly unlikely outcomes get more weight than they deserve (pdf 303)
- [[certainty-effect]] (new) — almost-certain outcomes get less weight than their probability justifies (pdf 303)
- [[fourfold-pattern]] (new) — risk averse for likely gains and unlikely losses, risk seeking for unlikely gains and likely losses (pdf 308–310)
- [[risk aversion]] — preferring a sure amount to a gamble of equal expected value, as used in Figure 13 (pdf 309)
- [[reference dependence]] — people attach values to gains and losses rather than to wealth (pdf 308)
- [[independence axiom]] — canon link; not named in this unit. The unit speaks only of "axioms of rational choice" that Allais's problem violates (pdf 304–305)

## Canonical instances
- [[allais-paradox]] — A/B choices inconsistent with the expectation principle; shows the certainty effect (pdf 304–305)
- [[lottery-and-insurance]] — the possibility effect explains lotteries and insurance (pdf 309)
- [[structured-settlements]] — industry exploiting the certainty effect (pdf 303)
- [[insect-spray-survey]] — $2.38 vs $8.09: a certainty premium (pdf 308)
- [[guthrie-litigation]] — strong, weak and frivolous civil cases in the fourfold pattern (pdf 311–312)
- [[nyc-frivolous-suits]] — $10M vs $20M: long-run cost of overweighting (pdf 312)

## Bridges (candidates)
- [structural-analogy] Decision weights ↔ behavioural finance/insurance pricing: paying above expected value for peace of mind — both price a premium for removing small risks.
- [structural-analogy] Defendant's risk seeking in losses ↔ escalation of commitment in losing wars or firms (pdf 310).

## Questions this raises
- Is the pattern the same when stakes are large or when probabilities are described versus learned from experience?
- Table 4 comes from "modest monetary stakes." How well does it carry over to health or other non-monetary risks?
- When is paying a certainty premium sensible, for example if the worry itself has a real cost?
- Can a rare event that gets zero weight (below 1%) be predicted from what captures attention?

## Reading notes
- Printed page numbers are not given; all references use pdf numbers (302–313).
- The Figure 13 grid itself is not visible in the page images (pdf 309 shows only the caption and text). The cell contents above come from the text's descriptions.
- On pdf 310 the text refers to "table 13" where the figure is called Figure 13.
- Some OCR garbling appears ("Bima…" fragments); the sense was recoverable from context.
- The text says the 5%–95% weight range is "about two-thirds" of the rational range. From Table 4, the weight range is 79.3 − 13.2 = 66.1, against 90 for probabilities, which is about 0.73 (added check).
- The text says 2% risk lowers utility "by 13%"; 100 − 87.1 = 12.9.
