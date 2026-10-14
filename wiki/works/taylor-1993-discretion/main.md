---
id: taylor-1993-discretion/main
work: taylor-1993-discretion
unit: paper
pages: 195–214
fields: [control-theory]
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
# Discretion versus policy rules in practice (Taylor, 1993)

## L0 — One line
A policy rule can still guide central banks even when it cannot be applied mechanically, if "rule" means systematic, credible, judgment-informed behaviour that follows a feedback response of interest rates to inflation and output.

## L1 — The gist (≤ 120 words)
Research favours interest-rate rules that react to the price level and real output. Real policymakers cannot follow an algebraic formula mechanically. Taylor asks how the rule concept can be kept in practice. He defines a rule broadly: systematic, contingency-plan behaviour, as opposed to pure discretion. He separates design, transition and operation of rules. He gives a simple rule (equation 1) that closely tracks Fed behaviour in 1987–1992. He suggests using the rule as one input, or using only its general features (signs of responses). Two 1990 case studies (oil shock, German unification) illustrate judgment in operating such a rule, which in the oil case departs from the literal formula.

**Prerequisites:** inflation, real GDP, interest rates; the idea of a feedback rule; basic expectations (rational expectations); no formal math beyond one linear equation.

## L2 — Key ideas (5–10 bullets)
- Taylor defines a policy rule broadly. It need not be a fixed instrument setting or a mechanical formula. Feedback rules (instrument settings that respond to conditions), automatic stabilizers (tax and transfer rules that respond automatically to unemployment) and adjustable exchange-rate pegs (exchange-rate systems fixed but adjustable) all count. Pure discretion does not count (p. 198).
- In the time-consistency literature (studies of dynamic optimization problems), rules ("optimal", "precommitted") beat discretion ("inconsistent", "shortsighted"), as cooperative beats noncooperative play in game theory (p. 198).
- Comparing nine models shows some consensus, but no agreed rule, that rules responding directly to price level and real output work better than exchange-rate or money-supply rules. In his own simulations a positive weight on both is preferable in most countries. Flexible exchange rates did better than fixed ones in his G-7 simulations (pp. 200–202).
- Equation (1), $r = p + .5y + .5(p-2) + 2$, is a simple representative rule. It fits actual Fed policy in 1987–1992 "remarkably well" (p. 202).
- Policy questions come in three kinds: design, transition to a new rule, and day-to-day operation. Taylor says certain apparently discretionary acts can be interpreted as transitions or as part of operating a rule (p. 199).
- Transitions need special care because expectations adjust only gradually and contracts are rigid. Rigidities suggest the transition should be gradual and announced publicly (p. 207).
- A rule can be made operational in two ways. One is to show the specific rule to policymakers. The other is to state only its general characteristics, such as the signs of the responses (pp. 208–209).
- In the 1990 oil shock, following the literal formula was judged inappropriate because the price rise was judged temporary. In the German-unification bond-market episode, judgment about whether real or inflation factors drove long rates guided whether policy needed adjusting (pp. 211–213).

## L3 — Walkthrough

### Introduction (pp. 195–197)
- **Topic.** The paper applies econometric research on monetary rules to practical policymaking. Good rules typically change the federal funds rate (the US overnight bank-lending rate) in response to the price level or real income (p. 195).
- **Motivations.** The author lists four: the Lucas critique of old policy evaluation; the point that rational expectations do not imply monetary policy is ineffective; the benefits of credibility; and the time-inconsistency result that rules beat discretion (p. 196).
- **Preferred rules.** These are not fixed instrument settings. They change the money supply, monetary base or short-term interest rate in response to price level or real income. Exact coefficients differ across studies. There are signs of a consensus on functional forms and signs (p. 196).
- **Practice.** Policymakers do not follow rules mechanically (p. 196).
  - A quarter is probably too short to average out price blips, such as temporary commodity-price changes.
  - A quarter is too long to hold the rate fixed. In a recession, sharp and rapid declines are appropriate.
  - Moving averages or a monthly model could help in principle, but they would make the rule more complex (p. 196).
- **Encompassing problem.** Judging whether a price rise is temporary needs several price measures: CPI, PPI, the employment cost index. Expectations from futures markets, the term structure and surveys also help. Potential output depends on forecasts of productivity, labor force and the natural unemployment rate. Special episodes, such as the Fed's liquidity provision after the 19 October 1987 crash, need more than a simple rule (p. 197).
- **Taylor's own question:** does all this mean giving up rules for discretion? He notes that arguments like these sound like those of advocates of discretion, and that even some past advocates of rules seem to have concluded that discretion is the only answer. Laidler (1991) is cited as concluding that "We are left, then, with relying on discretionary policy" (p. 197).
- **Taylor's reply.** Modern macroeconomics is clear, with substantial consensus, that rules have major advantages over discretion. So the rule concept should be preserved where mechanical following is impossible (p. 197).
- **Plan.** Section 1 covers semantics. Section 2 covers design. Sections 3 and 4 cover use in practice. A hypothetical but representative rule and two case studies are used (p. 197).

### 1. Semantic issues (pp. 198–199)
- **Broad definition.** A rule need not fix instrument settings. Feedback rules count: the money supply responds to unemployment or inflation. So do automatic stabilizers, and fixed or adjustable exchange-rate systems (p. 198).
- **Not necessarily mechanical.** The author says more economists disagree here. Policymakers may operate a rule informally. They know the general instrument responses behind it and use judgment. A nominal-income rule is included. Pure discretion is not (p. 198).
- **Pure discretion** means instruments are set from scratch each period with no reasonably well-defined contingency plan (p. 198).
- **Time consistency.** Kydland–Prescott, Barro–Gordon and Blanchard–Fischer call the rule solution "optimal", "rules" and "precommitted". They call discretion "inconsistent", "cheating" and "shortsighted". The advantage of rules is like that of a cooperative over a noncooperative solution in game theory (p. 198).
- **Terminology.** Policymakers usually hear "rule" as a fixed setting or simplistic procedure. Taylor says an alternative terminology would help; he points to "systematic" policy, as in the 1990 *Economic Report of the President*. The adjective is defined as "methodical, according to a plan, and not casually or at random" (p. 199).
- **Durability.** Technically speaking, a rule is a contingency plan lasting forever unless there is an explicit cancellation clause. No rule literally lasts forever, but to have any meaning it must last a reasonably long time: several business cycles suffice, and several years would do for many purposes. Commitment is needed for credibility. Econometric evaluation is of little use if the rule keeps changing (p. 199).
- **Three issues.** (1) design, (2) transition to a new rule, (3) day-to-day operation (p. 199).

> **Intuition note.** A rule need not be a formula; it is a plan to respond systematically to conditions, and policymakers must commit to it for it to be credible. What separates a rule from discretion is a plan that outlasts the current period. The formula itself is not what separates them.

### 2. Policy design: the search for a good monetary policy rule (pp. 199–203)
- **Scope.** Design discussion is limited to monetary policy. Fiscal rules, such as automatic stabilizers, could use the same approach. But they respond to goals beyond stabilization, for example tax progressivity (pp. 199–200).
- **Bryant–Hooper–Mann comparison.** It uses nine multicountry models, seven of them rational-expectations models. All rules tested are interest-rate rules responding to one of three things (p. 200):
  1. deviations of the money supply from a target;
  2. deviations of the exchange rate from a target;
  3. weighted deviations of inflation (or price level) and real output from targets.
- **Consensus.** Models differ and no particular rule is agreed. But exchange-rate or money-supply focused rules do not perform as well (in output and price variability) as rules focused directly on the price level and real output. How much to change the rate is uncertain (p. 200).
- **Taylor's own simulations (G-7, rational-expectations model).** Rules were ranked by price and output stability. The model endogenizes expectations as Lucas did, and it includes his three examples: consumption, price determination, investment. The approach uses an empirically estimated distribution of shocks (p. 200).
- **Theory.** In a standard non-rational-expectations model, fixed exchange rates work better when country-specific liquidity-preference shocks have large variance. Flexible rates work better when consumption or investment shocks have large variance. Going further needs estimates of shock sizes (pp. 200–201).
- **Setup.** Under flexible rates, each central bank sets its own interest-rate target in response to its price level and real output. Under fixed rates, one common "world" short-term rate target must be chosen. It rises if the world price level rises above target (p. 201).
- **Results (p. 201).**
  - Real-output fluctuations are much larger under fixed rates in the US, France, Germany, Italy, Japan and the UK.
  - The standard deviation of output nearly doubles in Germany and Japan.
  - Canada has slightly smaller output fluctuations under fixed rates but worse price stability. A change in the Canadian domestic rule under flexible rates could easily match the output stability with more price stability.
  - Taylor concludes that, in this sense, the flexible system dominates for all countries considered.
  - Price volatility is greater under fixed rates in all countries. For Japan and Germany it is more than twice as large.
- **Weights.** Placing positive weight on both price level and real output is preferable in most countries. It is unclear whether the output weight should be larger or smaller than the price weight. Some weight on output is likely better than a pure price rule (pp. 201–202).

**Equation (1), the representative rule (p. 202):**
$$r = p + .5y + .5(p-2) + 2 \tag{1}$$
- $r$ is the federal funds rate. $p$ is inflation over the previous four quarters. $y = 100(Y - Y^*)/Y^*$ is the percent deviation of real GDP from target. $Y$ is real GDP. $Y^*$ is trend real GDP, which grows 2.2 percent per year from 1984.1 through 1992.3 (p. 202).
- The rate rises if inflation exceeds a 2 percent target or if real GDP exceeds trend. With both on target, $r = 4$ percent, which is 2 percent in real terms. Lagged inflation proxies expected inflation. The 2 percent "equilibrium" real rate is close to the assumed 2.2 percent steady-state growth. The coefficient is the same on the output deviation and the inflation deviation (p. 202).
- Algebraic rearrangement (added step): $r = 1.5p + .5y + 1$. Check at $p=2$, $y=0$: $3 + 0 + 1 = 4$.
- **Fit to history.** Figure 1 compares the actual funds rate with the rule's path in 1987–1992. It shows a significant deviation in 1987, when the Fed eased after the stock-market crash. Otherwise the rule fits "remarkably well". Fed policy was thus conducted as if following such a rule (pp. 202–203).
- **Figures 2–3.** By this rule, the economy was above trend in the late 1980s and below trend in the 1990–91 recession. The gap has narrowed only slightly since. Inflation and GDP changes appear to have influenced the funds-rate path (p. 203).

> **Intuition note.** Equation (1) is a thermostat for the interest rate with two dials: how far inflation is above 2 percent, and how far output is above trend. The rate goes up when either is too high and down when either is too low. It also works as a description of what the Fed did.

### 3. Discretion versus transitions between policy rules (pp. 203–208)
- Research has focused on design. Transitions have had relatively little attention, as in trade policy and in moves to market economies. There is therefore less formal framework (p. 203).
- **Examples.** Moving from a 5 percent to a 2 percent inflation target changes only the intercept in the rule. This is the disinflation problem. Fiscal analogues are balancing the deficit at full employment (the intercept) and raising the response of automatic stabilizers (the response coefficient). The latter might change the unemployment compensation system (pp. 203, 207).
- **Reason 1: expectations.** Rational-expectations rule design makes sense once a policy has run a long time. Right after a new rule starts, people may not know it or believe it will be kept. They may learn in a Bayesian way from past policy or from policymakers' records. The impact may differ from rational-expectations projections (p. 207).
  - Taylor (1975) worked out learning in a very simple model of a change in the inflation target. If initial inflation is above the long-run rate, it is optimal to make the new policy as credible as possible: announce and start using it.
  - If initial inflation is lower than optimal (an unusual case), a welfare function including inflation and unemployment can be increased only by gradually informing the public. The information to release each period can be computed with optimal control theory (p. 207).
- **Reason 2: rigidities.** People have committed to projects, plans or contracts under the old policy and may assume others have too. Examples are long-term wage-setting, investment projects and loan contracts. Such rigidities suggest the transition should be gradual and announced publicly, which gives people a chance to unravel commitments without significant losses (p. 207).
- **In practice** there is little distinction between transition problems and apparent pure discretion. Taylor (1993) examines two transitions: to a zero-inflation target, and to a balanced full-employment government budget (pp. 207–208).

> **Intuition note.** How a new rule works depends partly on whether people know it and believe it will be kept. If they have not learned it yet, the economy may respond differently from what a rational-expectations analysis projects. Announcement and, given rigidities, gradual pacing are then policy questions.

### 4. Discretion in the operation of policy rules (pp. 208–213)
Mechanical following of equation 1 is not practical. Two ways to use research results are offered: use the specific rule as an input, or list its general principles and leave policy-setting to policymakers. A mix is possible (p. 208).

**Using a specific rule (p. 208).**
- FOMC members already use many inputs: leading indicators, the yield curve, staff forecasts. The Fed staff could add information on how recent decisions compare with the rule. Forecasts of the funds rate implied by the rule could be included. Variants could cover different coefficients, or the growth rate of GDP instead of its level, with bands for the rate path (p. 208).
- At minimum this draws attention to the rule concept. "Learning by doing" would probably improve the rule and format. If the rule comes so close to describing recent Fed behaviour and FOMC members believe that performance was good and should be repeated, the rule could provide some guide to future decisions, particularly when membership changes (pp. 208–209).

**Using general characteristics (pp. 209–210).**
- Patent laws are the analogy: they set a principle and leave details to officials and courts. Where fundamentals end and details begin depends on many things (p. 209).
- The 1990 *Economic Report* states the Fed generally raises rates when inflationary pressures rise and lowers them when they abate and recession seems more of a threat. How much requires judgment, and appropriate settings vary with the interest sensitivity of aggregate demand (p. 209).
- Taylor notes this gives only the signs of the coefficients. The magnitudes are tied to demand's interest sensitivity. It is not specific about targets for inflation or output. More would be needed to convey the rule's fundamentals (p. 209).
- Monetary targets can state inflation targets. If velocity is stable, a money target plus estimated potential output growth implies a price-level target. Velocity is unstable in the short run, but the long-run stability of some measures allows this. With 2½ percent real growth and steady velocity, the Fed's 1992 money growth range of 2½ to 6½ percent implies a price-level target growing 0 to 4 percent a year. Given index-number biases, the implicit 2 percent is probably very close to price stability (pp. 209–210).

**Case study one: the oil-price shock of 1990 (pp. 210–212).**
- **Context.** Growth was slow after the 1988–89 monetary tightening. By equation 1, the tightening fits strong growth and rising inflation in 1987–88. The Fed was also disinflating gradually, a transition: the mean target range for M2 fell from 7 percent in 1987 to 5 in 1990, then to 4½ in 1991 (p. 210).
- **The shock.** Iraq invaded Kuwait on 2 August 1990. The two countries produced 4.3 million barrels a day, and Saudi supply was threatened. Oil rose from $21 a barrel (end July) to $28 (6 August) and a $46 peak in mid-October. The monthly average rose from $17 (July) to $36 (October). The Council of Economic Advisers estimated that a temporary one-year 50 percent oil rise could raise the GDP deflator by about 1 percent for a time and, with a longer lag, cut real output by about the same amount (pp. 210–211).
- **Literal rule vs judgment.** Taken literally, equation 1 calls for a higher rate, since prices would rise more than output falls in the short run. This would be inappropriate if the rise were temporary (p. 211). A longer moving average or expected inflation might be better, but the aim is to keep the rule simple (p. 211).
- **Evidence it was temporary.** Spot oil doubled by mid-October, but the December 1991 futures price rose only about $4 against $25 for spot. Oil supply analyses suggested that increased production elsewhere could eventually make up most of the lost Iraqi and Kuwaiti production if the embargo continued. The main uncertainty, whether more facilities would be destroyed, was resolved with the start of Desert Storm in mid-January 1991 (p. 211).
- **Conclusion.** A rate rise would be inappropriate despite the literal reading of equation 1. Not adjusting means deviating from the rule (p. 211). In most countries the rise was not viewed as requiring short-term monetary policy changes, best read as: interest rates should follow the path they would have taken without the shock. There was a broad consensus that credibility built in the 1980s should be maintained (p. 211).
- **Fiscal side.** Automatic stabilizers were meant to work. Some international officials raised overriding them by raising taxes or cutting spending; others strongly opposed this. There was less consensus on keeping fiscal policy "systematic" than monetary (pp. 211–212). The Gramm–Rudman–Hollings law did not allow automatic stabilizers: deficit increases, even from stabilizers, were against the law, and deficit targets would not change if conditions worsened. The weeks-later revisions required budget targets to be adjusted for the economy (p. 212).

**Case study two: bond market, inflation and German unification (pp. 212–213).**
- **Problem.** A rise in long-term rates might signal expected inflation, which would make policymakers less willing to keep short rates steady. It might also reflect investment demand or saving shifts (p. 212).
- **Facts.** After falling in late 1989, ten-year Treasury yields rose 75 basis points in early 1990. Germany had even larger increases, suggesting the possibility that real factors were behind them, and an integrated world capital market could transmit German rates to the US. Unification was anticipated to raise German capital demand and the budget deficit. West Germany's 1989 budget surplus of .2 percent of GDP became a 3 percent deficit in 1990, so the timing was consistent (pp. 212–213).
- **Decision without hindsight.** Policy could not wait until 1991. Forward-looking model simulations suggested a rise of about one percentage point in interest rates was consistent with plausible capital-demand increases. So rising expected inflation was not needed to explain long rates. This gave some guidance that interest-rate policy need not be adjusted (p. 213).

### Concluding remarks (p. 213)
Simple algebraic rules cannot and should not be followed mechanically. Starting from the assumption that systematic, credible rule-like behaviour improves performance, the paper considered ways to incorporate it. It distinguished design, transition and operation, and it considered using specific rules or general features in decisions. Two case studies and a hypothetical rule illustrated this (p. 213).

## Toy example (ours, not from the text)
Use $r = 1.5p + .5y + 1$ (the rearranged equation 1). Assume output is on trend ($y=0$), and annualized quarterly inflation is 2 percent for several quarters. A temporary one-quarter blip then pushes one quarter to 6 percent.

- Baseline: $p = 2$, so $r = 1.5(2) + 0 + 1 = 4.0$.
- Blip, using the four-quarter average (equation 1's definition). $p = (2+2+2+6)/4 = 12/4 = 3$. So $r = 1.5(3) + 1 = 5.5$, which is 1.5 points above the baseline. This lasts four quarters, until the blip leaves the window.
- Longer moving average (the kind of modification suggested on p. 196). Eight quarters: $p = (2\cdot 7 + 6)/8 = 20/8 = 2.5$. So $r = 1.5(2.5) + 1 = 4.75$, only 0.75 above the baseline.
- Lesson: a short averaging window passes a temporary price blip into the interest rate. A longer window damps it. A policymaker who judges the blip temporary may hold at 4.0, which is the oil-shock judgment (p. 211).

## Concepts
- [[feedback]] — author's "feedback rules": instrument settings respond to measured inflation, unemployment or output (p. 198)
- [[negative (balancing) feedback]] — the rate rises when inflation or output is above target and falls when below (canon link; not named by the author) (p. 202)
- [[reference (set point)]] — the 2 percent inflation target and the output trend $Y^*$ in the rule (p. 202)
- [[error signal]] — the deviations $y$ and $p-2$ in equation (1) (canon link; not named by the author) (p. 202)
- [[time inconsistency]] — rules ("precommitted") do better than discretion ("shortsighted") in the time-consistency literature, as cooperative beats noncooperative play (p. 198)
- [[policy-rule]] (new) — systematic contingency plan lasting a reasonably long time. It is not necessarily a fixed setting or a mechanical formula (pp. 198–199)
- [[discretion]] (new) — instrument settings determined from scratch each period, with no reasonably well-defined contingency plan (p. 198)
- [[systematic-policy]] (new) — alternative term (used in the 1990 *Economic Report of the President*) for rule-like behaviour: methodical and according to a plan (p. 199)
- [[policy-transition]] (new) — the move from one rule to a new one. Learning and rigidities make it differ from steady-state rule design (pp. 199, 207)
- [[credibility]] (new) — the public's belief that policymakers will keep to the rule. Commitment is needed to gain its benefits (pp. 199, 207)

## Canonical instances
- [[taylor-rule-eq1]] — $r = p + .5y + .5(p-2) + 2$ tracks the 1987–1992 funds rate (pp. 202–203)
- [[oil-shock-1990]] — a literal rule says tighten, but a judged temporary price rise says hold (pp. 210–212)
- [[german-unification-1990]] — a rise in long-term rates judged explainable by plausible real capital-demand increases, without needing higher expected inflation (pp. 212–213)
- [[stock-crash-1987]] — Fed easing as a deviation from the rule (pp. 197, 202)

## Bridges (candidates)
- [structural-analogy] Equation (1) ↔ control-theory: proportional feedback on two error terms (inflation gap, output gap) — a linear law of measured deviations, with no closed-loop dynamics given here.
- [structural-analogy] Moving averages of inflation to avoid reacting to blips ↔ control-theory: low-pass filtering of a noisy measurement — longer windows damp noise but slow the response (pp. 196, 211).
- [structural-analogy] Rules beating discretion (time inconsistency) ↔ game theory: cooperative vs noncooperative solutions — the author draws this comparison himself (p. 198).
- [structural-analogy] Gradual release of information in a transition, computed by optimal control ↔ control-theory: optimal control with a learning state (p. 207).

## Questions this raises
- If a rule may be overridden for special factors, as in 1987 and 1990, how can outsiders tell a legitimate exception from discretion and judge credibility?
- How should the rule be modified (averaging window, expected inflation) so that exceptions like the oil shock become part of the rule itself?
- How are the weights on output and inflation to be chosen, given that the paper says it is unclear whether the output weight should be larger or smaller (p. 202)?
- How can a transition be designed in practice, when the formal framework is thin (p. 203)?

## Reading notes
- The task metadata says printed pages are unknown. The page images, however, show printed numbers 196–214 (the first page shows no number, but its running head gives pp. 195–214), so printed = pdf + 194. Citations use the printed numbers.
- The text layer was blank; everything was read from the page images. Figures 1–3 are simple line charts; Figure 3 has faint show-through from the reverse page. Values were not read off the figures; claims about the fit rely on the author's text.
- References on p. 214 are listed but not digested. Laidler (1991) is listed with a 1993 publication note, as printed.
- The paper contains one numbered equation (1) and the unnumbered definition of $y$, no exercises, and no derivations.
