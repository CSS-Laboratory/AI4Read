---
id: pearl-2018-bookofwhy/ch06-paradoxes
work: pearl-2018-bookofwhy
unit: "Chapter 6 — Paradoxes Galore!"
pages: "pdf 177–202 (printed page numbers not visible)"
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 7
---
# Paradoxes Galore! (Monty Hall, Berkson, Simpson, Lord)

## L0 — One line
Pearl argues that many famous paradoxes come from a tension between causal intuition and the logic of proportions in data, and that a causal diagram of how the data were generated settles them.

## L1 — The gist (≤ 120 words)
Why do the Monty Hall, Berkson, Simpson and Lord puzzles baffle even experts? Pearl's answer: our minds expect causal structure, but the data alone do not carry it. Monty Hall and Berkson are collider cases: conditioning on a common effect creates a correlation with no cause. Simpson's reversal is only arithmetic. The real paradox is the clash with the conviction that no drug can be bad for men, bad for women and good for people; the causal diagram tells us which claim to believe. In his examples, confounders mean stratify; mediators mean pool. Lord's paradox is resolved the same way. Identical data can demand opposite conclusions under different causal stories, so the story, not the table alone, decides.

**Prerequisites:** fractions and percentages; conditional probability; the earlier-chapter ideas of causal diagram, confounder, collider, mediator and back-door path.

## L2 — Key ideas
- Paradoxes arise when rules from the realm of proportions are applied to causal intuitions, or the reverse. Studying them shows how the brain reasons (pdf 177).
- Monty Hall: the host's rules, not just what he opened, determine the answer. Switching wins with probability 2/3 under the real rules and 1/2 if the host picks at random (pdf 179–182).
- "Door Opened" is a collider. Conditioning on a collider creates a dependence between its parents that has no cause (pdf 181).
- Berkson's paradox, the two-coin experiment and the dating example are all collider bias from selecting which cases enter the data. Pearl says Reichenbach's common cause principle (a correlation needs one variable to cause the other, or a common cause) is too strong, because of such selection (pdf 183–186).
- Simpson's reversal is a numerical fact about fractions, and Pearl does not call it a paradox by itself. The paradox is the clash with the intuition that a drug cannot be bad for men, bad for women and good for people (pdf 188–189).
- Savage's sure-thing principle (if an action looks good whichever way an event C turns out, take it) needs, in Pearl's corrected version, a causal condition: the action must not change the probability of C. With that condition, Pearl says, no BBG drug (bad for men, bad for women, good for people overall) can exist (pdf 190–191).
- Whether to pool or stratify depends on the causal diagram, not on the data. In his examples, a confounder (Gender) means stratify and a mediator (Blood Pressure) means pool. Time order is a rule that works in many cases but is not foolproof (pdf 191–194).
- Lord's paradox is a cousin of Simpson's paradox. The data alone cannot say which of the two statisticians to believe. Pearl says the diagram shows which adjustment answers the question asked (pdf 196–200).

## L3 — Walkthrough

### Opening (pdf 177)
Pearl says the birth-weight paradox from Chapter 5 belongs to a large class of paradoxes about the tension between causation and association. The two sit on different rungs of the Ladder of Causation (the book's hierarchy of levels of reasoning, introduced earlier). Intuition runs on causal logic, while data obey probabilities and proportions. Paradoxes appear when we apply the rules of one realm to the other. Like optical illusions, they also reveal how the brain works. Pearl adds that, to the extent statisticians have struggled with these (he says they "whiffed rather badly"), this signals that looking at the world without causal thinking may be flawed.

### The Perplexing Monty Hall Problem (pdf 178–183)
**The puzzle.** Marilyn vos Savant's 1990 column asked: you pick Door 1 of three (one car, two goats). The host, who knows what is behind the doors, opens Door 3 (a goat) and offers a switch to Door 2. Should you switch? (pdf 178)
- **Vos Savant's answer:** switch. Staying wins with probability 1/3, switching with 2/3 (pdf 178).
- **Critics (many claiming PhDs):** only two doors remain and your pick was random, so the probability is 1/2 either way (pdf 178). She received over 10,000 letters, most disagreeing.

**Her table (Table 6.1, pdf 179).** Assume you picked Door 1. The three equally likely arrangements and the outcomes are:

| Door 1 | Door 2 | Door 3 | Switch | Stay |
|---|---|---|---|---|
| Auto | Goat | Goat | Lose | Win |
| Goat | Auto | Goat | Win | Lose |
| Goat | Goat | Auto | Win | Lose |

Switching wins in 2 of 3 cases. The opened door is implicit. In row 2 the host must open Door 3 (pdf 179); in row 3 he must open Door 2 (added step).

**Why it feels wrong.** Pearl's candidate reason is that it seems to imply mental telepathy: the car would be more likely to sit behind the door you did not choose (pdf 179).

**Resolution, part 1: the rules of the game.** We must take into account not only the data (which door the host opened) but also the data-generating process (the rules of the game), which tells us something about data that could have occurred but did not. Pearl says statisticians are used to R. A. Fisher's "reduction of data" and to ignoring this process (pdf 179).

**Let's Fake a Deal (Table 6.2, pdf 180).** The host opens one of the two doors you did not pick, completely at random, so he may reveal the car. There are two independent random events (car location, 3 options; host's door, 2 options), so six equally likely rows. If you chose Door 1 and the host opens Door 3 showing a goat, only rows 2 and 4 remain: (car 1, open 3) and (car 2, open 3). Stay and switch then each win with probability 1/2. Pearl concludes that in this game all of vos Savant's critics would be right, though the data are the same as in the real game. The lesson: how we obtain information matters as much as the information (pdf 180).

**Causal diagrams (Figures 6.1 and 6.2, pdf 180–182).**
- *Let's Make a Deal:* Your Door → Door Opened ← Location of Car. There is no arrow between Your Door and Location of Car, so mind-reading is ruled out. The host must avoid both your door and the car, so Door Opened has two arrows pointing into it (pdf 180–181).
- Door Opened is a **collider**. Conditioning on a collider creates a spurious dependence between its parents. If you chose Door 1, the car is twice as likely behind Door 2 as behind Door 1. If you chose Door 2, it is twice as likely behind Door 1 (pdf 181).
- Pearl calls this a dependence with no cause and no physical communication, a purely Bayesian artifact in which information moves without causality. We resist it because we link correlation to causation from infancy (pdf 181).
- *Let's Fake a Deal:* only Your Door → Door Opened remains. The arrow from Location of Car is deleted because the host ignores the car. Conditioning on Door Opened does nothing, so the parents stay independent (pdf 182).

**Resolution, part 2: Bayesian reasoning.**
- Why does belief in Door 2 rise from 1/3 to 2/3 even though the host's goat was inevitable? He could not open Door 1, but he could have opened Door 2. His not doing so makes it more likely that he was forced to open Door 3 (pdf 181).
- General theme of Bayesian analysis: a hypothesis that has survived a test that threatens its validity becomes more likely, and the greater the threat, the more likely it becomes (pdf 182). Door 2 was vulnerable, Door 1 was not, so Door 1 stays at 1/3.
- In Let's Fake a Deal, Door 1 is also vulnerable (the host could have revealed the car), so both doors stay equal (pdf 182).
- Belief propagation (Chapter 3; passing probability updates along the links of a network) gives P(Door 2) = 2/3 for Let's Make a Deal and 1/2 for Let's Fake a Deal (pdf 182).

**Why we see a paradox.** Pearl wants a resolution to explain the paradox as well as dissolve it. Paul Erdos did not believe the answer until a simulation convinced him (pdf 183). Pearl cites Persi Diaconis, who said our brains are not wired to do probability problems very well. Pearl adds that brains are wired for causal problems, and this wiring produces systematic probabilistic errors. Because there is no direct or common cause linking the two, we find the association incomprehensible; our brains are not prepared to accept correlations without cause, so special training is needed to spot where they arise. Once we learn to recognize colliders, the paradox stops confusing us (pdf 183).

*Intuition note.* The host's rule (he never opens your door and never opens the car) makes his choice depend on both your pick and the car. Seeing his choice therefore links your pick and the car, even though no signal passes between them.

### More Collider Bias: Berkson's Paradox (pdf 183–186)
- **Berkson (1946):** in hospital studies, two diseases unrelated in the general population can appear associated among patients (pdf 183).
- **Diagram (Figure 6.3):** Disease 1 → Hospitalization ← Disease 2. A hospital-based study controls for Hospitalization, a collider. The induced association is positive here because both diseases must be present for hospitalization (in the extreme case imagined). In many earlier examples it was negative, through the explain-away effect (once one cause is known, the other becomes less likely) (pdf 183–184).
- **Sackett (1979) data (Table 6.3, pdf 184).**

| | General population: bone disease yes / no (% yes) | Hospitalized in last six months: yes / no (% yes) |
|---|---|---|
| Respiratory yes | 17 / 207 (7.6) | 5 / 15 (25.0) |
| Respiratory no (control) | 184 / 2,376 (7.2) | 18 / 219 (7.6) |

For a long time epidemiologists refused to believe in this bias, even in 1979, when Sackett gave strong evidence for it. Among hospitalized people with respiratory disease, bone disease jumps to 25 percent. Sackett called it "admission rate bias" or "Berkson bias." He admits that confounding could also contribute. The debate is, to some extent, ongoing, and has moved on to how large the bias can be (pdf 184).
- Pearl lists earlier collider-induced correlations: Pigou (1911), Burks (1926), Simon (1954) (pdf 184).

**Two-coin experiment (pdf 185).** Flip two coins 100 times and record only trials where at least one is heads (about 75 entries). In the record the coins look dependent: whenever Coin 1 is tails, Coin 2 is heads. You conditioned on a collider by censoring the tails-tails outcomes.

**Reichenbach's common cause principle (pdf 185).** Reichenbach (*The Direction of Time*, 1956) proposed "No correlation without causation." A correlation between X and Y arises only if one causes the other or a third variable causes both. Pearl says the coin experiment shows this is too strong, because it ignores how observations are selected. Pearl says we live as if the principle were true and crave explanations in terms of stable mechanisms. Colliders are "too ethereal" to satisfy us. Selection is often not conscious: the host opens the door for us, and a researcher may study hospital patients for convenience (pdf 185–186).

**Dating example (Ellenberg, pdf 186).** You date people who are attractive or nice (or both), but not people who are both mean and unattractive. Among the people you date, this creates a spurious negative correlation between attractiveness and personality.

### Simpson's Paradox (pdf 186–195)
**Story (pdf 186–187).** Dr. Simpson sees that Drug D raises heart-attack risk in men and in women, yet seems to lower it in the whole population (a "bad/bad/good," BBG, drug). Edward Simpson found this paradox in 1951. Melvin Novick (1983) wrote that the apparent conclusion is ridiculous: do not use the treatment if gender is known, but use it if gender is unknown. Pearl agrees it is ridiculous, so one of the three assertions must be wrong (pdf 187).

**Data (Table 6.4, pdf 187).** Observational study, 60 men and 60 women. Patients chose whether to take the drug.

| | Control: heart attack / none | Treatment: heart attack / none |
|---|---|---|
| Female | 1 / 19 | 3 / 37 |
| Male | 12 / 28 | 8 / 12 |
| Total | 13 / 47 | 11 / 49 |

Women: 5% (control) vs 7.5% (drug). Men: 30% vs 40%. Total: 22% (control) vs 18% (drug) (pdf 187).

**Pearl's thesis and criteria (pdf 187–188).** The confusion comes from applying causal principles to statistical proportions incorrectly. Simpson's paradox is a puzzle about confounding. Pearl says a resolution of a paradox should meet four criteria: (1) explain why it is surprising; (2) identify the scenarios where it can occur; (3) identify scenarios, if any, where it cannot occur; (4) say which of two plausible contradictory statements is correct when it does occur (pdf 188).

**Reversal vs. paradox (pdf 188–189).**
- *Simpson's reversal* is a purely numerical fact: a frequency comparison flips on merging samples. Here 3/40 > 1/20 and 8/20 > 12/40, but $(3+8)/(40+20) < (1+12)/(20+40)$. The folk rule "if A/B > a/b and C/D > c/d then (A+C)/(B+D) > (a+c)/(b+d)" is wrong (pdf 188).
- *Baseball (Table 6.5, pdf 189).* Justice's average beat Jeter's in 1995 (.253 vs .250), 1996 (.321 vs .314) and 1997 (.329 vs .291). Over all three years, Jeter led: 385/1,284 = .300 vs Justice's 312/1,046 = .298. At-bats differ across years. Jeter had few at-bats in 1995, so his low average that year barely counted. Justice had many at-bats in his weakest year. "Better hitter" is a weighted average (pdf 188–189).
- Pearl does not call the reversal a paradox. In his view, a paradox should involve a conflict between two deeply held convictions (pdf 189).
- Intuition says no drug can cause and prevent the same heart attacks. Pearl says this intuition is right, that a BBG drug cannot exist, and that this can be proved mathematically (pdf 189).

**Savage's sure-thing principle (pdf 190–191).**
- *Savage (1954):* a businessman would buy a property if the Democrat won and would buy if the Republican won, so he should buy. Pearl notes Savage called it "extra-logical" and says that, when properly interpreted, it rests on causal, not classical, logic (pdf 190).
- Pearl's mapping: Property A vs B. If the Democrat wins, 5% vs 8% chance of $1. If the Republican wins, 30% vs 40%. Pearl says these quantities are the same as in the Simpson story (the text prints 8% here, while Table 6.4 gives 7.5%) (pdf 190).
- *Flaw:* if the businessman's decision could change the election outcome, buying A might be better. Savage left unstated the causal assumption that the decision does not affect the election (pdf 190–191).
- **Corrected principle (Pearl):** an action that increases the probability of an outcome given C and given not-C also increases it when C is unknown, provided the action does not change the probability of C. In particular, there is no BBG drug. This does not follow from classical logic. Its proof needs the do-operator calculus (rules for reasoning about interventions, written $do(X)$) (pdf 191).

*Intuition note.* In Pearl's corrected principle, an action that is good in every subgroup is good overall, provided the action does not change the probability of the subgroup. Drug D does not change a patient's gender, so no BBG drug can exist causally. The totals in Table 6.4 mislead because gender also shapes who takes the drug (confounding).

- Three statements cannot all hold: (i) Drug D increases heart-attack probability in men and in women; (ii) it decreases it in the population; (iii) it does not change the number of men and women. Since a drug changing sex is implausible, one of (i) and (ii) is false. Table 6.4 cannot say which; we need the data-generating process (pdf 191).

**Causal resolution: Drug D (Figure 6.4, pdf 191–192).** Gender → Drug, Gender → Heart Attack, Drug → Heart Attack. Gender is unaffected by the drug, men are at greater risk, and women preferred the drug. So Gender is a confounder and we must adjust. Pearl averages the gender-specific rates, since men and women are equally frequent in the population:
- Without Drug D: $(5+30)/2 = 17.5\%$.
- With Drug D: $(7.5+40)/2 = 23.75\%$.

Drug D is therefore BBB: bad for women, bad for men and bad for people (pdf 192; the book prints "bad for women" twice, see Reading notes).

**When pooling is right: Drug B (Table 6.6, Figure 6.5, pdf 192–193).** Same numbers as Table 6.4, but the rows are Low and High blood pressure measured after treatment. Drug B lowers blood pressure (a possible cause of heart attack). Among those who took it, 40 of 60 had low blood pressure, versus 20 of 60 in controls. Blood Pressure is a **mediator** (a variable on the path between cause and effect), not a confounder. Diagram: Drug → Blood Pressure → Heart Attack, plus Drug → Heart Attack. There is no back-door path, so stratifying is unnecessary. Conditioning on Blood Pressure would block one causal path, maybe the main one. Drug B works, and the aggregate data show it (pdf 193). Pearl stresses that aggregating is not always wrong and partitioning is not always right; it depends on the data-generating process (pdf 192).

**History (pdf 193–194).**
- Simpson (1951) gave two stories with the same data. In one, aggregating was "the sensible interpretation." In the other, partitioning was. So he saw a paradox, but offered only common sense (pdf 193).
- Lindley and Novick (1981) considered using the language of causation but chose not to, because they said the concept does not seem well defined (pdf 193–194). Pearl says Lindley told him in 2009 he would not have written this had Pearl's book existed in 1981 (pdf 194).
- **Objection (some readers):** use temporal order: stratify on variables measured before treatment (gender), aggregate over those measured after (blood pressure). **Pearl replies:** this works in many cases but is not foolproof. In M-bias (Game 4, Chapter 4; a pre-treatment variable that is a collider on a back-door path), B can precede A, yet conditioning on B would violate the back-door criterion. We should consult the causal structure (pdf 194).

**Real cases (pdf 194–195).**
- *Kidney stones (1996, observational):* open surgery beat endoscopic surgery for small stones and for large stones, but had a lower success rate overall. Larger stones led more often to open surgery and had a worse prognosis (pdf 194).
- *Thyroid disease (1995):* smokers had higher 20-year survival (76% vs 69%). Nonsmokers did better in six of seven age groups, with minimal difference in the seventh. Age was a confounder of Smoking and Survival (smokers were on average younger). Stratifying by age, Pearl concludes that smoking has a negative impact on survival (pdf 194–195).

**How to treat the paradox (pdf 195).** Some statisticians avoid the symptom (reversal) and ignore the disease (confounding). Simpson's paradox signals that at least one of the trends (aggregated, partitioned or both) cannot represent causal effects. Another warning sign: the aggregated estimate of the causal effect could be larger than the estimate in each stratum, which should not happen if confounders are properly controlled. A reversal is harder to ignore because it changes the sign.

*Intuition note.* The same table can mean opposite things. In these two examples, the story tells you whether the third variable is a common cause of treatment and outcome (adjust) or lies on the path from treatment to outcome (do not adjust). Time order alone is not foolproof (M-bias).

### Simpson's Paradox in Pictures (pdf 195–200)
**Continuous version (Figure 6.6, pdf 195–196).** In each age group, more exercise goes with lower cholesterol (a downward trend). Pooled across ages, the trend is upward. Older people exercise more, and Age is more likely to cause Exercise than the reverse. Age may affect Cholesterol, so Age may be a confounder. We should control for age and conclude that exercise is beneficial regardless of age (pdf 196).

**Lord's paradox (Lord, 1967; pdf 196–198).** A school measures students' weight in September ($W_I$) and June ($W_F$), to study the diet's effect on girls and boys. Figure 6.7 shows two ellipses as scatter plots of the data.
- **Statistician 1:** average weight in June equals September for girls and for boys (symmetry around $W_F = W_I$). Average gain is zero for both, so the diet has no differential effect on the sexes (pdf 197).
- **Statistician 2:** final weight depends strongly on initial weight, so stratify by initial weight. At a given $W_0$, boys' final weight is higher on average. Lord reports that this statistician concludes that boys gained significantly more weight than girls once differences in initial weight are allowed for (pdf 197).
- **Lord's view:** each conclusion is "visibly correct," and the usual study of this type tries to answer a question that cannot be answered rigorously on the basis of available data. This view fed a pessimistic literature on baseline differences (pdf 197–198). Pearl says this pessimism is unjustified: the dietitian's question can be answered rigorously, starting from a causal diagram (pdf 198).
- **Why the overall gain is not the average of stratum gains (pdf 198).** The sure-thing principle holds only when the proportion of each subpopulation does not change between groups. Here the "treatment" (gender) strongly affects the share of students in each weight class.

**Pearl's diagram (Figure 6.8, pdf 198–199).** Arrows: S (Sex) → $W_I$, S → $W_F$, $W_I \to W_F$. Gain is $Y = W_F - W_I$, a deterministic relation. The diagram marks coefficients $-1$ on $W_I \to Y$ and $+1$ on $W_F \to Y$.
- Statistician 1: no back doors between S and Y need blocking, so the aggregate answer "no effect" is correct for the question asked (pdf 199).
- Statistician 2: $W_I$ is not a confounder of S and Y. It is a mediator if Sex is the treatment. Controlling for it does not give the usual causal effect. At best it estimates a "direct effect" (Chapter 9; the effect not passing through the mediator). Pearl suspects he adjusted "out of habit" (pdf 199).
- Pearl notes that Lord never mentions a control diet, so we cannot even say anything about the diet's effect (pdf 199).

**Wainer and Brown (2006) version (Figure 6.9, pdf 199–201).** The treatment is diet. Students eat in dining hall A or B, which serve different diets. Heavier students tend to go to B. Statistician 1 claims switching from A to B has no effect on gain ($W_F - W_I$ has the same distribution in both ellipses). Statistician 2 finds that students at $W_0$ gain more on B (pdf 199–200). Two changes in the diagram: the treatment is now D (diet), and the arrow reverses to $W_I \to D$. Now $W_I$ is a confounder of D and $W_F$ (and of D and Y). Pearl says Statistician 2 is unambiguously correct in this version, and Statistician 1 would be wrong because he measures only statistical association, not causal effects. Wainer and Brown conclude that the data alone cannot say whom to believe (pdf 200).

**Conclusion (pdf 200).** Lord's paradox is no more a paradox than Simpson's. In one the association reverses, in the other it disappears. The diagram tells us which procedure to use. For "model-blind" statisticians it is paradoxical that the correct conclusion differs while the data look the same. The chapter closes by announcing that the next chapter begins rung two, intervention (pdf 201).

## Toy example (ours, not from the text)
Monty Hall under the two rule sets. You pick Door 1, and the host opens Door 3 showing a goat. Prior: each door holds the car with probability 1/3.

*Let's Make a Deal (host never opens your door or the car).* Likelihood $P(\text{opens }3\mid\text{car})$:
- Car at 1: host may open 2 or 3, so 1/2.
- Car at 2: host must open 3, so 1.
- Car at 3: host cannot open 3, so 0.

Joint probabilities: $\tfrac13\cdot\tfrac12=\tfrac16$ (car 1); $\tfrac13\cdot 1=\tfrac13$ (car 2); $0$ (car 3). Their sum is $\tfrac16+\tfrac13=\tfrac12$. Posterior: car 1 is $\tfrac16/\tfrac12=\tfrac13$, and car 2 is $\tfrac13/\tfrac12=\tfrac23$. Switching wins with probability 2/3.

*Let's Fake a Deal (host picks randomly between Doors 2 and 3).* Now $P(\text{opens }3\mid\text{car at }k)=\tfrac12$ for every $k$. We saw a goat behind Door 3, so car at 3 is excluded. Joint: car 1 is $\tfrac13\cdot\tfrac12=\tfrac16$, and car 2 is $\tfrac16$. The sum is $\tfrac13$. Posterior: $\tfrac12$ each. The observation is the same, but the rule that generated it differs, and so does the answer.

## Concepts
- [[simpsons-paradox]] — a trend in each subgroup that reverses in the pooled data, and so seems to contradict a causal belief; Pearl argues the causal diagram resolves it (pdf 186–189)
- [[simpsons-reversal]] (new) — the purely numerical flip of a comparison of proportions on merging groups; not paradoxical by itself (pdf 188)
- [[fork-chain-collider]] — a collider is a variable with two arrows into it; conditioning on it creates a spurious dependence between its parents (pdf 181)
- [[confounding-vs-selection-bias]] — confounder: common cause, adjust for it. Collider conditioning (selection): creates bias (pdf 181, 184–186, 191)
- [[causal-dag]] — a diagram encoding how data were generated; it decides what to adjust for (pdf 180, 191)
- [[back-door-front-door-criterion]] — no back-door path means no adjustment is needed; conditioning wrongly can violate the criterion (pdf 193–194)
- [[do-operator]] — the corrected sure-thing principle needs a causal calculus using it (pdf 191)
- [[bayes-theorem]] — belief rises for a hypothesis that survived a test that threatened it (pdf 182)
- [[ladder-of-causation]] — association and causation sit on different rungs, which is where Pearl says the tension behind these paradoxes starts (pdf 177)
- [[data-generating-process]] (new) — the rules that produced the data, which can change conclusions even when the data are the same (pdf 179–180)
- [[sure-thing-principle]] (new) — Savage's rule; valid only if the action does not change the probability of the conditioning event C (pdf 190–191)
- [[mediator]] (new) — a variable on the causal path from treatment to outcome; conditioning on it blocks that path (pdf 193)
- [[common-cause-principle]] (new) — Reichenbach's "no correlation without causation"; Pearl says it is too strong (pdf 185)
- [[lords-paradox]] (new) — two valid-looking analyses of group weight gain disagree; Pearl says the causal diagram resolves it (pdf 197–200)

## Canonical instances
- [[monty-hall-problem]] — the host's rules create a collider (pdf 178–183)
- [[lets-fake-a-deal]] — the same observation under a random host gives 1/2 (pdf 180)
- [[berkson-sackett-bone-respiratory]] — 25% vs 7.6% bone disease among hospitalized patients (pdf 184)
- [[two-coin-censoring]] — dropping tails-tails creates dependence (pdf 185)
- [[dating-attractive-jerks]] — selection of dates creates a spurious negative correlation (pdf 186)
- [[drug-d-simpson]] — BBG numbers; Gender confounds; the drug is BBB (pdf 187, 191–192)
- [[drug-b-blood-pressure]] — same numbers; mediator; pool the data (pdf 192–193)
- [[justice-jeter-batting]] — real-data Simpson's reversal (pdf 188–189)
- [[kidney-stone-study]] and [[thyroid-smoking-study]] — documented real cases (pdf 194–195)
- [[exercise-cholesterol-age]] — continuous Simpson's paradox (pdf 195–196)
- [[lord-diet-paradox]] and [[wainer-brown-dining-halls]] — mediator case and confounder case (pdf 197–200)

## Bridges (candidates)
- [structural-analogy] Collider conditioning ↔ Bayesian explaining-away: both create dependence between independent causes once their common effect is observed (pdf 181, 184).
- [same-math] Monty Hall posterior via likelihood × prior ↔ Bayes' theorem: the host's rule supplies the likelihood term (pdf 182).
- [structural-analogy] Censored coin flips and hospital samples ↔ selection on the outcome or a collider in sampling design: any selection that depends on two variables can link them.
- [metaphor] "Survived a test that threatened it" ↔ Bayesian updating as falsification: a hypothesis exposed to refutation gains more from surviving (pdf 182).

## Questions this raises
- If Simpson's reversal signals that at least one trend cannot represent causal effects, can we find the correct causal diagram from data, or must it come from outside knowledge?
- When variables could be both a mediator and a confounder in different parts of a diagram, how do we adjust?
- How large can collider bias be in diagrams with many variables (the question the Berkson debate now asks)? (pdf 184)
- What changes in Lord's paradox if we want the direct effect of sex on weight gain, as the second statistician might? (Chapter 9, pdf 199)

## Reading notes
- No printed page numbers are visible in the pages given, so all references use pdf numbers (pdf 177–202). Page 202 holds only a cartoon caption (Scaling "Mount Intervention") about methods for estimating intervention effects (back-door adjustment, instrumental variables, front-door adjustment, do-calculus); it is not digested here.
- Misprint, pdf 192: the text says "bad for women, bad for women, and bad for people" where "bad for men" is clearly meant.
- Misprint, pdf 181: "different both from both Your Door and Location of Car."
- Table 6.6 has its caption at the foot of pdf 192 and its body on pdf 193. Figure 6.6 is first mentioned on pdf 195 but printed on pdf 196.
- The Monty Hall posterior calculation is only in the Toy example, labeled as ours. The text itself states only the results 2/3 and 1/2 and refers to belief propagation.
- The main text says "17.5 percent" and "23.75 percent" are the adjusted rates; the arithmetic is consistent with Table 6.4.
