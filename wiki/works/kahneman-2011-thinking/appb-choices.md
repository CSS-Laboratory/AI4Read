---
id: kahneman-2011-thinking/appb-choices
work: kahneman-2011-thinking
unit: Appendix B — Choices, Values, and Frames
pages: printed numbers not visible; pdf 431–452 (text pdf 431–450, references pdf 450–452)
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
# Choices, Values, and Frames (Kahneman & Tversky)

## L0 — One line
People value gains and losses from a reference point and give probabilities nonlinear weights, so the way a problem is framed can change their choice, which breaks the rational-choice rule of invariance.

## L1 — The gist (≤ 120 words)
The paper asks why people's choices under risk break the rules a rational decision maker should follow. Kahneman and Tversky argue that value attaches to gains and losses from a reference point, and that probabilities receive nonlinear decision weights. The result is risk aversion for gains, risk seeking for losses, and overweighting of sure things and of small chances. Because the same problem can be framed in different ways, preferences violate invariance, and sometimes dominance. Mental accounting and the cost–loss difference explain further anomalies in consumer choice. The authors also note that decision value and experienced value can differ, and that confidence in a choice does not ensure it survives reframing.

**Prerequisites:** expected value (probability-weighted average); the idea of a concave vs convex curve; percentages and simple probability multiplication. Terms used above: invariance = a rational chooser's preference should not change with how the same options are described; dominance = if A is at least as good as B in every respect and better in one, prefer A; decision weight = the weight a stated probability gets in choice; mental accounting = how people organize the outcomes of transactions; cost–loss difference = the same money is more aversive as an uncompensated loss than as a cost; decision value vs experienced value = how much an anticipated outcome counts in choosing vs the pleasure or pain actually felt.

## L2 — Key ideas
- Following Bernoulli, subjective value is a concave function of gains (each extra dollar adds less). This entails a preference for a sure gain over a gamble with the same expectation, and most people also prefer a sure $800 to an 85% chance of $1,000. Preferring a sure outcome to a gamble of higher or equal expectation is called risk aversion. (pdf 432–433)
- The value function is S-shaped and defined on gains and losses, not wealth. It is steeper for losses (loss aversion) and convex for losses, which gives risk seeking in losses. (pdf 433–434)
- Invariance and dominance are accepted by all analyses of rational choice, yet framing can violate both (dominance only in concurrent decisions such as Problem 4). The "lives saved" and "lives lost" problems show this. (pdf 435–437)
- Decision weights are regressive: they underweight moderate and high probabilities, overweight low ones, and change disproportionately near 0 and 1 (the category-boundary effect). Regressive means that, away from the endpoints, weights rise less than the probabilities do. These features help account for lottery tickets, insurance, the pseudo-certainty effect (an uncertain event weighted as if certain) and aversion to probabilistic insurance. (pdf 438–441)
- Subjects tend to adopt the frame given in a problem's wording, so a change of wording can shift preference. A physician could influence a patient this way, and credit-card lobbyists deliberately pushed one label over another. (pdf 442)
- Mental accounting (minimal, topical, comprehensive accounts) is the authors' account of why more people say they would travel to save $5 on a $15 item (68%) than on a $125 item (29%), and why a lost ticket is treated differently from lost cash. (pdf 443–445)
- Losses loom larger than gains, which biases people toward the status quo and underlies the endowment effect (reluctance to give up owned assets). Losses are also more aversive than costs (the cost–loss discrepancy). The authors think loss aversion and the endowment effect are unlikely to matter much in routine exchanges. (pdf 446–449)
- Decision value and experience value can differ. In some cases the frame can probably also affect the experience itself. Decision value is the weight an anticipated outcome has in choice; experience value is the pleasure or pain actually felt. (pdf 449–450)

## L3 — Walkthrough
The paper has no numbered sections, so I follow its headings. All page references are pdf numbers (no printed numbers are visible).

### Introduction and abstract (pdf 431)
- Normative analysis asks about rationality and the logic of decisions. Descriptive analysis asks about beliefs and preferences as they are. The tension between them runs through the study of judgment and choice (pdf 431).
- Decision analysis commonly separates risky from riskless choice. The intro text is cut off by an OCR fault right after this point (pdf 431).

### Risky Choice (pdf 431–435)
- A risky choice is treated as acceptance of a gamble with outcomes of various probabilities. Research therefore studies simple monetary gambles with stated probabilities (pdf 431–432).
- **Bernoulli's analysis (1738).** He tried to explain why people are generally risk averse and why risk aversion falls as wealth rises (pdf 432).
- **Example.** Option 1 is an 85% chance of $1,000 (15% chance of nothing). Option 2 is $800 for sure. The expectation of Option 1 is $.85 \times 1000 + .15 \times 0 = \$850$, above $800. A large majority still prefers the sure $800 (pdf 432).
- **Definitions.** Expectation is the probability-weighted average of outcomes. Risk averse means preferring a sure outcome to a gamble with higher or equal expectation. Risk seeking means rejecting a sure thing for a gamble of lower or equal expectation (pdf 432).
- **Bernoulli's proposal.** People weight the subjective value (utility) of outcomes, not the money. Utility is a concave function of money: $u(\$200)-u(\$100) > u(\$1200)-u(\$1100)$. So the value of $800 is more than 80% of the value of $1,000, and concavity entails a risk-averse preference for a sure $800 over an 80% chance of $1,000, which has the same expectation (pdf 432).
- **Reference point instead of wealth.** Decision analysis usually codes outcomes as total wealth, for example $W$ versus an even chance of $W+\$20$ or $W-\$20$. The authors call this psychologically unrealistic. They propose that the carriers of value are changes (gains, losses, neutral status quo), an assumption central to prospect theory (pdf 432–433).
- Introspection and psychophysical measurements suggest that value is concave in the size of a gain, and the same generalization applies to losses. The authors say a loss of $200 vs $100 appears to differ in value by more than a loss of $1,200 vs $1,100 (pdf 433).
- **Figure 1 (value function), three properties.** It is (a) defined on gains and losses, (b) concave for gains and convex for losses, and (c) considerably steeper for losses than for gains. Property (c) is **loss aversion**: a loss of $X$ is more aversive than a gain of $X$ is attractive (pdf 433–434).
- **Evidence.** Most respondents in a sample of undergraduates refused to stake $10 on a coin toss if they stood to win less than $30 (pdf 434).
- **Risk seeking in losses.** Concavity for gains implies risk aversion, and convexity for losses implies risk seeking. Choice: 85% chance to lose $1,000 vs a sure loss of $800. A large majority takes the gamble, even though its expectation (−$850) is worse. The authors call this a robust effect, particularly when the probabilities of loss are substantial. It is also seen with hours of pain and lives lost (pdf 434).
- The authors say these preferences conform to compelling intuitions about value, and the presumption is that people should be entitled to their own values. However, they say they will show that an S-shaped value function has normatively unacceptable implications (pdf 434).
- **Axioms.** Von Neumann and Morgenstern's axioms include transitivity (A≻B and B≻C imply A≻C) and substitution (if A≻B, an even chance of A or C is preferred to an even chance of B or C). People do not always obey substitution, and its normative merit is disputed (pdf 434).
- **Two principles that all analyses of rational choice incorporate.**
  - *Dominance*: if A is at least as good as B in every respect and better in at least one, prefer A.
  - *Invariance*: the preference order should not depend on how prospects are described. Two versions recognized as equivalent when shown together should draw the same preference when shown separately (pdf 434–435).

*Intuition note.* If extra money matters less and less, a sure amount is preferred to a gamble with the same average. If losses are also felt with diminishing sensitivity, then in the loss domain people tend to prefer the gamble. The same person can thus be cautious about gains and willing to gamble about losses.

### Framing of Outcomes (pdf 435–438)
- The same option can be framed as gains and losses relative to the status quo, or as asset positions. Invariance says this should not matter (pdf 435).
- **Problem 1 (N = 152).** 600 people are expected to die. Program A: 200 saved for sure (72%). Program B: 1/3 chance 600 saved, 2/3 chance none saved (28%). The frame treats the 600 deaths as the reference point and the outcomes as gains, so preferences are risk averse (pdf 435).
- **Problem 2 (N = 155).** Program C: 400 will die (22%). Program D: 1/3 chance nobody dies, 2/3 chance 600 die (78%). C and D are the same in real terms as A and B. The reference state is now "no one dies", the outcomes are losses, and the majority is risk seeking. There is more risk seeking here than risk aversion in Problem 1 (pdf 436).
- The failure is pervasive and robust. It occurs among sophisticated and naive respondents and is not removed by answering both within minutes. Respondents confronted with their conflicting answers are typically puzzled and, even after rereading, still wish for all three: risk aversion for saved, risk seeking for lost, and consistency. The authors say framing effects "resemble perceptual illusions more than computational errors" (pdf 436).
- **Problem 3 (N = 86).** E: 25% win $240, 75% lose $760 (0% chose). F: 25% win $250, 75% lose $750 (100% chose). F dominates E (pdf 436).
- **Problem 4 (N = 150).** Two concurrent decisions.
  - (i) A: sure gain $240 (84%) vs B: 25% chance of $1,000, 75% nothing (16%).
  - (ii) C: sure loss $750 (13%) vs D: 75% chance to lose $1,000, 25% nothing (87%).
  - 73% chose A and D. Only 3% chose B and C. The same pattern appeared in a reduced-stakes version in which undergraduates chose gambles they would actually play (pdf 437).
  - A + D: 25% chance (D's "lose nothing" branch) of +$240, 75% chance of $240 − $1,000 = −$760. This is exactly E.
  - B + C: 25% chance of $1,000 − $750 = +$250, 75% chance of 0 − $750 = −$750. This is exactly F.
  - So the preferred conjunction is dominated by the rejected one. Framing plus the S-shaped value function violates dominance in concurrent decisions (pdf 437).
- **The moral, in the authors' words:** invariance is "normatively essential, intuitively compelling, and psychologically unfeasible" (pdf 437).
- **Two ways to guarantee invariance, both limited.**
  1. A canonical representation, such as total assets. The advice is easier to give than follow. Except where ruin is possible, gains and losses are more natural. Compounding concurrent decisions exceeds intuitive computation. In health and safety, the right canonical frame is unclear (pdf 437–438).
  2. An actuarial criterion. It has some appeal for human lives but is inadequate for financial choices (known since Bernoulli) and inapplicable to outcomes without an objective metric (pdf 438).
- **Conclusion.** Frame invariance cannot be expected to hold. Confidence in a choice does not ensure the same choice in another frame. It is good practice to test robustness by framing a problem in more than one way (pdf 438).

*Intuition note.* In the lives problems, respondents still want risk aversion for saved, risk seeking for lost, and consistency, though their answers conflict. Each choice in Problem 4 looks natural by itself, yet together they pick a package that is dominated by the rejected one.

### The Psychophysics of Chances (pdf 438–442)
- **Setup.** The Bernoullian expectation rule says the value of a prospect is the sum of outcome utilities weighted by probability. To test it, set the status quo at 0 and give a $300 cash gift the value 1. A lottery ticket for $300 then has a value between 0 and 1, barring utility for gambling (pdf 438).
- Intuition says the ticket's value is not linear in probability. An increase from 0% to 5% seems to matter more than 30% to 35%, which seems smaller than 95% to 100% (pdf 438–439).
- This is a **category-boundary effect**: a change from impossible to possible, or from possible to certain, has more impact than a comparable change mid-scale (pdf 439).
- **Figure 2 (weighting function).** Decision weights are regressive relative to stated probabilities. Except near the endpoints, a .05 rise in probability raises the value by less than 5% of the prize (pdf 439).
- **Consequences of the weights.**
  - Moderate and high probabilities are underweighted relative to sure things. This adds to risk aversion in gains (positive gambles look less attractive) and to risk seeking in losses (negative gambles look less aversive) (pdf 439).
  - Low probabilities are overweighted, and very low ones are either grossly overweighted or neglected, so weights there are highly unstable. This enhances long shots and amplifies the aversiveness of a small chance of severe loss. People are therefore often risk seeking for improbable gains and risk averse for unlikely losses. This contributes to the attractiveness of both lottery tickets and insurance (pdf 439–440).
- **Problem 5 (N = 85), two-stage game.** Stage 1: 75% chance the game ends with nothing, 25% chance to reach stage 2. The choice is made before stage 1. A: sure $30 (74%). B: 80% chance of $45 (26%) (pdf 440).
- **Problem 6 (N = 81).** C: 25% chance of $30 (42%). D: 20% chance of $45 (58%) (pdf 440).
- Problems 5 and 6 are identical in probabilities and outcomes: A gives $.25$ of $30, and B gives $.25 \times .80 = .20$ of $45. Yet the majority prefers the higher chance of the smaller prize in Problem 5 and the opposite in Problem 6. This held with real and hypothetical money (these results used real money), with lives, and with a nonsequential presentation of the chance process (pdf 440).
- **Explanation.** The authors attribute it to framing of probabilities interacting with nonlinear weights. They propose that in Problem 5 people ignore the first phase (same outcome whatever they choose) and focus their attention on stage 2. Choices were practically identical to those between a sure $30 and an 85% chance of $45. A sure thing is overweighted relative to moderate or high probabilities, so A looks better. This is the **pseudo-certainty effect**: an uncertain event is weighted as if it were certain (pdf 440–441).
- **Probabilistic insurance.** A hypothetical agent offers half the premium for cover only if the quake falls on an odd day. Most people find this distinctly unattractive. Figure 2 suggests why: in the low-probability region, a drop from $p$ to $p/2$ reduces the weight less than a drop from $p/2$ to 0. So halving the risk is not worth half the premium (pdf 441).
- **Why it matters (three reasons).**
  1. It undermines the classical explanation of insurance by concave utility. According to expected utility theory, probabilistic insurance should be preferred to normal insurance when the latter is just acceptable.
  2. It represents protective actions that reduce a hazard without removing it (checkups, new tires, burglar alarms).
  3. Insurance acceptability can be manipulated by framing. A fire-only policy can be seen as full protection against a specific risk or as a reduction in overall loss probability, and Figure 2 suggests people greatly undervalue a reduction of a hazard compared with its complete elimination, so insurance should appear more attractive framed as eliminating risk than as reducing it (pdf 441).
- **Evidence (Slovic et al.).** A vaccine cutting disease risk from 20% to 10% is less attractive described as "effective in half of the cases" than as "fully effective against one of two equally probable virus strains" (pdf 441–442).

*Intuition note.* Going from "maybe" to "certain" feels bigger than a comparable change in the middle of the scale, such as 30% to 35%. So a sure thing is overweighted, and the step from zero chance to a tiny chance also looms large. This can help make both insurance and lottery tickets attractive.

### Formulation Effects (pdf 442–443)
- In the public health problem, changing "saved" to "lost" shifted preference from risk aversion to risk seeking. Subjects seem to have taken the description as given and coded outcomes as gains or losses (pdf 442).
- McNeil et al. found that physicians' and patients' preferences between lung cancer therapies varied with mortality vs survival wording. Surgery carries a risk of death during treatment, and was relatively less attractive in mortality terms (pdf 442).
- A physician or advisor could influence a decision, without distorting information, by framing. Effects may arise fortuitously or be exploited deliberately. Thaler noted that credit card lobbyists insisted on "cash discount", not "credit card surcharge". Because "losses loom larger than gains", consumers are less likely to accept a surcharge than to forgo a discount (pdf 442).
- The two sources of susceptibility are the nonlinear value function and the tendency to use the reference point suggested by the statement (pdf 442–443).
- In language comprehension, people quickly recode equivalent messages (active/passive; said/implied) into one abstract form. This silent machinery is not adequate for recoding the two public health versions or mortality/survival statistics (pdf 443).

### Transactions and Trades (pdf 443–446)
- **Mental account.** To evaluate a multiattribute option, a person sets up a mental account of its advantages and disadvantages relative to a multiattribute reference state. The option is acceptable if the value of its advantages exceeds that of its disadvantages. This assumes psychological, not physical, separability, with concavity and loss aversion imposed on the measures. The authors credit Thaler (pdf 443).
- **Problem 7.** You are buying a jacket for $125 and a calculator for $15. The calculator is $10 at another branch, 20 minutes away. Will you go? (pdf 443)
- **Three account types.** A *minimal* account includes only the differences (gain of $5). A *topical* account uses a reference level set by the decision's topic (price cut from $15 to $10, jacket excluded). A *comprehensive* account relates the saving to something wider, such as monthly expenses (pdf 444).
- The authors suggest people spontaneously use topical accounts, which play a role analogous to "good forms" in perception and basic-level categories in cognition. With concave value, willingness to travel for a $5 saving should then be inversely related to the calculator's price and independent of the jacket's price (pdf 444).
- **Test.** Prices were swapped (calculator $125 vs $120; jacket $15). 68% of 88 respondents would drive to save $5 on a $15 calculator, but only 29% of 93 would to save $5 on a $125 calculator. The two versions are identical under minimal and comprehensive accounts (pdf 444).
- Supporting observation: the standard deviation of prices quoted by different stores for the same product is roughly proportional to its average price (Pratt, Wise, Zeckhauser). This suggests consumers hardly exert more effort to save $15 on $150 than $5 on $50 (pdf 444).
- Topical accounts make people evaluate gains and losses in relative terms, so the rate at which money is exchanged for effort varies widely. This runs counter to standard theory, which assumes invariance (pdf 444–445).
- **Problem 8 (N = 200).** You paid $10 for a play ticket and lose it. Buy another? Yes 46%, No 54%. **Problem 9 (N = 183).** You lose a $10 bill before buying a $10 ticket. Still buy? Yes 88%, No 12% (pdf 445).
- **Explanation.** Going to the play is a transaction exchanging ticket cost for the experience. A second ticket raises the account's cost to a level many find unacceptable. Lost cash is not posted to the play's account and only makes one feel slightly less affluent (pdf 445).
- When the same subjects saw both, willingness to replace the lost ticket rose after the lost-cash version. Willingness to buy after losing cash was unaffected by prior exposure to the other problem. Subjects apparently saw that a lost ticket can be thought of as lost cash, not vice versa (pdf 445–446).
- **Normative status is questionable.** The calculator and ticket versions may differ in substance as well as form: saving $5 on $15 may be more pleasurable, and paying twice for a ticket more annoying. Regret, frustration and self-satisfaction can depend on framing. If such secondary consequences are legitimate, invariance is not violated. They may change on reflection, though. The authors do not recommend resolving every pair with the same primary consequences the same way. They propose that examining alternative framings is a reflective device for assessing the values of primary and secondary consequences (pdf 446).

### Losses and Costs (pdf 446–449)
- If the status quo is the reference level for all attributes, an alternative's advantages are gains and its disadvantages are losses. Because losses loom larger, the decision maker is biased toward the status quo (pdf 446).
- **Endowment effect** (Thaler): reluctance to part with assets one owns. When giving up an asset hurts more than obtaining it pleases, buying prices are lower than selling prices. Several studies found large gaps, in hypothetical and real transactions. Standard theory has them coincide except for transaction costs and wealth effects (pdf 446–447).
- **Job study.** Respondents imagined holding position (S₁, T₁), with weekly salary S and workplace temperature T, and were offered (S₂, T₂), better in one respect and worse in another. Most assigned to either position did not want to move to the other. The same difference looms larger as a disadvantage than as an advantage (pdf 447).
- **Twins.** Two hedonically identical twins find two environments equally attractive and are separated into them. Once each adopts the new state as reference point, both prefer to stay. Instability of preferences produces a preference for stability. Adaptation plus loss aversion also give limited protection against regret and envy (pdf 447).
- **Limits of loss aversion.** It is unlikely to matter much in routine exchanges. A merchant adds costs and revenues and evaluates the balance. Consumers' payments are viewed as alternative purchases ("a new camera or a new tent"), not as losses (pdf 447).
- **Cost vs loss.** Insurance can be framed as a sure loss against a risk of a greater loss. Choice: sure loss of $50 vs 25% chance of losing $200. 80% of Slovic et al.'s subjects preferred the gamble. But only 35% refused to pay $50 for insurance against a 25% risk of losing $200. The authors suggest the same money was an uncompensated loss in the first problem and a cost of protection in the second. The modal preference reversed because losses are more aversive than costs (pdf 447–448).
- **Problems 10 and 11.** P10: accept a gamble with 10% chance to win $95 and 90% chance to lose $5? P11: pay $5 to join a lottery with 10% chance to win $100 and 90% chance to win nothing? 132 undergraduates answered both, separated by a filler problem (order reversed for half). 55 gave different answers across versions. 42 of those rejected the gamble in P10 and accepted the lottery in P11. Thinking of $5 as a payment makes the venture more acceptable than thinking of it as a loss (pdf 448).
- **Dead-loss effect.** Thaler's example: a man develops tennis elbow soon after paying a club fee and keeps playing in agony. The authors suggest that playing keeps the fee evaluated as a cost. Stopping would force him to see it as a dead loss, which may be more aversive than playing in pain (pdf 448–449).

### Concluding Remarks (pdf 449–450)
- **Two senses of value.** *Experience value* is the pleasure or pain actually felt. *Decision value* is the contribution of an anticipated outcome to an option's attractiveness. Theory tacitly assumes they coincide, which describes an idealized decision maker who predicts experience perfectly. For ordinary people the match is far from perfect: some factors affecting experience are hard to anticipate, and some affecting decisions do not affect experience equally (pdf 449).
- Little systematic work exists on the psychophysics linking hedonic experience to objective states. The basic problem is fixing the level of adaptation or aspiration that separates positive from negative outcomes. The hedonic reference point is largely set by the objective status quo but also by expectations and social comparison. Example: a smaller raise than everyone else's can feel like a loss. Brickman and Campbell's hedonic treadmill suggests the radical hypothesis that rapid adaptation will make the effects of any objective improvement short-lived. Example: ordering a big meal when ravenously hungry (pdf 449).
- Framing often creates decision values with no counterpart in experience (mortality vs survival framing is unlikely to affect experience). In other cases, such as a loss vs the price of insurance, the framing can probably affect the experience, so evaluation both anticipates and molds experience (pdf 450).

## Toy example (ours, not from the text)
Take a value function of the S-shaped kind with made-up numbers: $v(x)=\sqrt{x}$ for gains and $v(-x)=-2\sqrt{x}$ for losses. This is concave for gains and convex for losses, with losses steeper. Ignore probability weighting.

**Gain frame.** You get $100 for sure, or a 50% chance of $200.
- Sure: $v(100)=\sqrt{100}=10$.
- Gamble: $0.5\times\sqrt{200}=0.5\times14.142=7.07$.
- 10 > 7.07, so you take the sure gain (risk averse).

**Loss frame.** You lose $100 for sure, or have a 50% chance of losing $200.
- Sure: $-2\sqrt{100}=-20$.
- Gamble: $0.5\times(-2\sqrt{200})=0.5\times(-28.28)=-14.14$.
- $-14.14 > -20$, so you take the gamble (risk seeking).

Both problems describe the same final positions: start at $1,000 in the first and $1,200 in the second. The first gives $1,100 for sure vs $1,000 or $1,200 at even odds. The second gives $1,100 for sure vs $1,200 or $1,000 at even odds. So the choice reverses with the frame, although the final-wealth prospects are identical.

## Concepts
- [[risk aversion]] — preferring a sure outcome to a gamble of higher or equal expectation; here explained by concave value of gains (pdf 432)
- [[utility function]] — Bernoulli's subjective value of money, concave; the authors prefer value defined on gains and losses (pdf 432–433)
- [[expected utility]] — probability-weighted sum of outcome utilities (Bernoullian rule); the authors question it via nonlinear weights (pdf 438)
- [[reference dependence]] — value attaches to changes from a reference point, not to total wealth (pdf 433)
- [[loss aversion]] — value function steeper for losses than for gains (pdf 433–434)
- [[probability weighting]] — decision weights regressive: low probabilities overweighted, moderate and high underweighted, with category-boundary effects (pdf 439)
- [[framing effect]] — equivalent descriptions give different preferences (pdf 435)
- [[independence axiom]] — appears as the "substitution" axiom; people do not always obey it and its normative merit is disputed (pdf 434)
- [[invariance]] (new) — preference order should not depend on how prospects are described (pdf 434–435)
- [[dominance-principle]] (new) — if A is at least as good in every respect and better in one, prefer A (pdf 434–435)
- [[mental-accounting]] (new) — evaluating options through accounts of advantages and disadvantages, minimal, topical or comprehensive (pdf 443–444)
- [[endowment-effect]] (new) — reluctance to give up owned assets; buying price below selling price (pdf 446)
- [[pseudo-certainty-effect]] (new) — an uncertain event weighted as if certain (pdf 441)
- [[cost-loss-discrepancy]] (new) — the same money is more aversive as an uncompensated loss than as a cost (pdf 448)
- [[experience-vs-decision-value]] (new) — felt pleasure or pain vs the weight an anticipated outcome has in choice (pdf 449)

## Canonical instances
- [[asian-disease-problem]] — "lives saved" vs "lives lost" reverses preference (Problems 1–2) (pdf 435–436)
- [[concurrent-decisions-dominance]] — choosing A+D over B+C violates dominance (Problems 3–4) (pdf 436–437)
- [[two-stage-game-pseudo-certainty]] — Problems 5 and 6 are probabilistically identical but get different majorities (pdf 440)
- [[probabilistic-insurance]] — half-premium, half-coverage insurance is unattractive (pdf 441)
- [[calculator-jacket]] — 68% vs 29% would travel to save $5 (Problem 7) (pdf 444)
- [[lost-ticket-vs-lost-cash]] — 46% vs 88% would still buy a ticket (Problems 8–9) (pdf 445)
- [[cash-discount-vs-credit-surcharge]] — a label frames a price difference as gain or loss (pdf 442)
- [[insurance-vs-gamble-cost-loss]] — 80% prefer the gamble; only 35% refuse to pay for insurance (pdf 448)
- [[tennis-elbow-dead-loss]] — the authors suggest playing in pain keeps a fee evaluated as a cost (pdf 448–449)

## Bridges (candidates)
- [same-math] concave value for gains ↔ decision-game-theory: concave utility gives risk aversion — the same curve-shape argument, here applied to gains and losses separately.
- [structural-analogy] invariance failure under reframing ↔ survey methodology: answers changing with question wording — equivalent descriptions get different responses.
- [structural-analogy] regressive decision weights ↔ regression to the mean: stated probabilities map to weights that are pulled toward the middle, but this is a psychological curve, not a statistical effect.

## Questions this raises
- If the value function is an S-shape with a reference point, what fixes the reference point in real decisions, beyond the wording of a problem?
- How can a canonical representation be built for health or safety policy, where the right total (all deaths, disease deaths, or one disease) is unclear?
- When are secondary consequences (regret, annoyance) legitimate enough to make different frames of the same primary outcomes acceptable?
- How strongly do the framing effects here carry over to real, high-stakes choices?

## Reading notes
- **Page numbers.** No printed page numbers are given in the labels or visible in the images I was shown, so all references are pdf numbers (pdf 431–452).
- **OCR damage in the text layer.**
  - The introduction cuts off mid-sentence at "decision un ^v>" (pdf 431).
  - Garbled fragments occur at pdf 433 ("Wn indispan>"), 434, 437, 438, 440, 442, 443, 444, 445, 447, 448, 450 and 451.
  - The two page images I could inspect (pdf 433 and 439) confirm the text layer there, including the garbled "Wh indispan> – $20" on pdf 433, which is presumably meant as "W − $20".
  - I did not have images for the other pages. Where fragments are garbled I used only the surrounding intact sentences, and no numbers were affected as far as I could tell.
- **Edition.** The unit is Appendix B of the 2011 book named in the unit metadata. No separate title page for the original paper is shown, and the text is signed Daniel Kahneman and Amos Tversky.
- **Exercises.** None are in the unit.
- **References.** pdf 450–452; the work "Erakar" at pdf 450 appears to be the same as "Eraker" cited at pdf 434.
