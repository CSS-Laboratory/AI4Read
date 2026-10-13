---
id: achen-2016-realists/ch05-blind
work: achen-2016-realists
unit: "Chapter 5 — Blind Retrospection: Electoral Responses to Droughts, Floods, and Shark Attacks"
pages: 116–145
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Blind Retrospection: Electoral Responses to Droughts, Floods, and Shark Attacks

## L0 — One line
Voters punish incumbents for bad times that no government could control (sharks, droughts, floods), so retrospective voting is natural but not clearly a reliable form of accountability.

## L1 — The gist (≤ 120 words)
The chapter asks whether voters punish incumbents only for what governments actually control. It tests this with New Jersey's 1916 shark attacks, a century of state-level droughts and floods (1900–2000), and the 2000 election. In all three, incumbents lost votes for events no government could prevent. The authors reject two defences of voter rationality (policy learning, judging disaster responses), citing short-lived, one-sided punishment; a third, narrower view fits. They argue blame often depends on socially constructed explanations; the unpunished 1918 flu illustrates this. They conclude that retrospective voting is natural but not obviously rational, and it supports weaker accountability than the conventional account assumes.

**Prerequisites:** Basic regression (coefficient, standard error, t-statistic, R²); vote share; the idea of retrospective voting (judging incumbents by past outcomes); the principal–agent idea from the book's chapter 4.

## L2 — Key ideas (5–10 bullets)
- **Blind retrospection:** the authors' claim is that when voters are in pain they tend to punish the government, whatever its actual responsibility, if some plausible story of blame is available (p. 118).
- **Sharks, 1916:** in New Jersey's four beach counties Wilson's 1916 vote was about 3 points lower than expected. In the shore townships the loss was about 10 points (pp. 122–127).
- **Droughts and floods:** across 26 presidential elections, higher absolute drought scores lower the incumbent party's state vote, by about 0.7 points in a typical state-year. Effects vary a lot by election (pp. 128–133).
- **2000 election:** climate distress cost the incumbent party (Gore) about 2.7 points nationally. The authors attribute this to 2.8 million votes and to seven states (p. 135).
- **Two rationality defences fail:** punishment is not tied to ideology, it fades quickly, and it is one-sided rather than balanced between rewards and punishments (pp. 135–137).
- **Narrow rationality only:** punishing whenever well-being falls below normal fits the data, and it may be "rational" in chapter 4's technical sense if voters cannot tell relevant from irrelevant sources of well-being. The authors say mechanically turning pain into punishment is "just what we mean by blind retrospection" (p. 138).
- **Blame is socially constructed:** voters punish when elites, entrepreneurs, and folk culture supply a story of government responsibility. The authors offer the 1874 Nebraska locusts and the 1918 flu as cases where, without such a story, there was little or no punishment (pp. 138–142).
- **Weak accountability:** blind retrospection gives incumbents less incentive to serve voters and sits badly with the folk theory of democracy (pp. 143–145).

## L3 — Walkthrough

### Introduction (pp. 116–118)
- Historical examples (Egypt's Nile floods, Kansas and Nebraska Populists, Hurricane Andrew in 1992, Krakatoa, the Black Death) show that rulers and rivals have long treated disasters as politically significant. The authors say this evidence is "impressively broad" but "uncomfortably thin" (pp. 116–117).
- They aim for more precise evidence from modern electoral politics, where data are detailed and reliable (p. 117).
- Their finding: electorates still hold rulers responsible for calamities clearly beyond their control (p. 118).
- Their wider claim: disasters are just illuminating cases of retrospective voting. Retrospections are "blind" in hardships of all kinds (p. 118).
- When in pain, voters are likely to "kick the government" if plausible cultural constructions allow it. Only if none is available, or no ambitious challengers voice one, do people blame other scapegoats or just suffer (p. 118).

### Shark attacks in New Jersey (pp. 118–128)
**The events.** Four deaths and one survivor between 1 and 12 July 1916 (pp. 118–119). The first two attacks were at Beach Haven (Vansant, July 1) and Spring Lake (Bruder, July 6). Two more occurred in Matawan creek, and a boy survived (pp. 118–119).
- No shark attack had ever been recorded in New Jersey, and prominent scientists doubted such attacks occurred (p. 119).
- Resorts lost heavily: $250,000 of reservations cancelled within a week, and perhaps $1 million over the season (p. 119).
- Federal officials were on the scene: the Treasury Secretary and Wilson's political aide had summer homes nearby. Wilson held a cabinet meeting, but the Bureau of Fisheries could recommend no certainly effective measure (p. 120).
- The authors' reasons to expect an effect on Wilson's vote (p. 120):
  1. deaths and economic distress;
  2. the election came a few months later;
  3. high federal officials were present from the start.
- They add that the fact that no government controls sharks "would, from our perspective, have been irrelevant to the voters" (p. 120).

**County analysis.** The outcome is Wilson's 1916 two-party vote share in New Jersey counties. The key factor is a "beach county" indicator (Monmouth, Ocean, Atlantic, Cape May), which captures where tourism-dependent economies were hit (p. 121).
- Control 1: Wilson's 1912 three-way vote share, as a measure of partisanship and candidate appeal. Earlier elections added nothing once 1912 was included (p. 121).
- Control 2: a "machine counties" indicator (at least 30,000 voters in 1916 and 60% or more "foreign" citizens in 1910). It covers Bergen, Hudson, Essex and Union, and captures Wilson's weaker control over the state party bosses after 1912 (pp. 121–122).
- Essex was excluded as an outlier. Wilson never controlled its machine, and its residual was 4.6 standard deviations. That leaves 20 counties (p. 122, fn. 9).

**Table 5.1 results** (OLS; standard errors in parentheses; dependent variable is Wilson's 1916 two-party %, p. 123):

| Variable | Estimate |
|---|---|
| Beach county | −3.2 (1.0) |
| Machine county | −5.7 (1.1) |
| Wilson 1912 vote (three-way fraction) | 0.95 (0.06) |
| Intercept | 4.5 (2.8) |

- Standard error of regression 1.7; adjusted $R^2 = .94$; $N = 20$ (p. 123).
- The text reports a correlation of .97 between actual and predicted vote shares (p. 122).
- The beach effect is "a little more than three percentage points", with a 95% confidence interval from 1.3 to 5.2 (p. 122).
- Figure 5.1 shows all beach counties lying below the non-beach line by roughly the same amount. This consistency tightens the standard errors (pp. 122–124).

**Robustness (pp. 124, fns. 10–12).**
- Other partisanship measures never did better than the 1912 vote. With 1912 included, the shark effect stayed between 2 and 4 points.
- Proportions German, Irish, and "foreign" showed no effects.
- Turnout weighting, or using the change in vote share as the dependent variable, never cut the effect by more than a tenth of a point. Turnout-weighted estimates were a few tenths larger.
- Roosevelt ran better along the shore than elsewhere, so the shark effect is "if anything, slightly underestimated" (fn. 12).
- Fear extended to the machine counties and to New York beaches. Some of the negative "machine county" effect may therefore also come from the sharks (fn. 10).

**Township analysis, first test (p. 125).** Beach Haven and Spring Lake were small, stable communities. Beach Haven cast 112 presidential votes in 1912 and 119 in 1916; Spring Lake cast 271 and 265 (fn. 14). Wilson's vote fell 11 points in Beach Haven and 9 in Spring Lake. The declines in their counties were modest, and New Jersey as a whole moved less than a point (pp. 122, 125, Fig. 5.2).

**Township analysis, second test (pp. 125–126).** To check that these two towns are typical, the authors compared Ocean County towns on the water with towns near the water.
- There were 8 beach and 11 near-beach communities. Townships whose vote totals changed by more than 25% between 1912 and 1916 were dropped, leaving 14 (4 beach, 10 near-beach).
- Wilson's 1912 shares were similar: 37.1% at the beach and 33.5% near the beach.
- From 1912 to 1916 the beach area lost 13.3 points and the near-beach area lost 0.5 (Fig. 5.3).
- A differences-in-differences regression (change in vote on a beach indicator, weighted by 1916 votes) gives −12.8 points (SE 4.4, t = 2.9). A second weighted regression gives −11.1 (SE 3.2, t = 3.5). Dropping two townships with fewer than 50 voters gives −8.4 and −8.8, both with t > 2.7 (fn. 17).
- The authors summarise this as a loss of "about 10 percentage points" in the directly affected areas (pp. 126–127, fn. 17).
- By US standards they call this "a near-earthquake". Hoover's New Jersey vote fell 12 points in the Depression, from 59.8% in 1928 to 47.6% in 1932 (p. 127).

**Why the retrospection was blind (pp. 127–128).** Shark attacks are random and have no governmental solution. The truth could not be covered up, and the vacationers could not be forced back. Yet "the voters punished anyway" (p. 127).
- **Objection (readers' suggestion):** voters blamed Wilson for not extending federal disaster assistance.
- **Authors' reply:** such programmes did not exist, could not be created quickly, and would not be expected after one local disaster. The objection is "historical presentism" (p. 128).

> *Intuition note.* The shark attacks are a nearly pure test, because no government can change sharks. The vote still fell about ten points where the economic damage was greatest. This is the authors' evidence that punishment can follow pain without any link to responsibility.

### A century of droughts and floods (pp. 128–135)
**Why go broader.** A single case can be dismissed as coincidence. The authors want to show that voters "consistently and systematically" punish incumbents for conditions beyond their control (p. 128).

**Data and index (pp. 128–129).**
- The data are monthly readings, 1897–2000, for 344 US climate divisions. The measure is the Palmer Hydrological Drought Index (PHDI), an index of long-term moisture supply. Zero is ideal, negative values mean drought, and positive values mean wet spells.
- The "drought index" is the absolute value of the sum of monthly PHDI readings, May–October each year. It therefore reflects both dry and wet spells.
- Division values are averaged within states. This assumes that equally severe droughts and wet spells are equally painful. Separate measures gave generally similar effects (fn. 22).
- The index runs from 0.04 to 49.08, with mean 11.03 and standard deviation 6.29. There are 4,992 state-years. Of these, 649 (13%) exceed 18, the equivalent of a year of "severe" drought or wetness. 203 (4%) exceed 24, the equivalent of "extreme" (p. 129).

**Design (pp. 129–131).**
- The analysis covers 26 presidential elections from 1900 to 2000, using state-level incumbent-party vote and weighting each state-year by votes cast (fn. 24).
- The authors rely on "the random occurrence of numerous droughts and floods" to separate their common effect from specific circumstances (p. 129).
- Controls are the incumbent party's vote in the same state in the previous two elections, percent rural, and a South indicator. The effects of all controls and the intercept vary by election. This adds 130 coefficients, and only the drought effect is held constant across elections (pp. 130–131).
- Observations are clustered by election year. This raises the standard errors by about 35% (fn. 25).

**Table 5.2 (OLS; incumbent vote %; $N = 1{,}233$; adjusted $R^2 = .88$; p. 130).**

| | (1) | (2) | (3) | (4) | (5) | (6) |
|---|---|---|---|---|---|---|
| Election-year index | −0.060 (0.031) | −0.052 (0.034) | — | −0.176 (0.083) | −0.140 (0.082) | — |
| Election−1 | — | −0.043 (0.029) | — | — | −0.116 (0.088) | — |
| Election−2 | — | 0.016 (0.036) | — | — | 0.023 (0.102) | — |
| Election−3 | — | −0.043 (0.040) | — | — | −0.024 (0.102) | — |
| Time-weighted | — | — | −0.104 (0.045) | — | — | −0.273 (0.122) |

Columns 1–3 use the drought index. Columns 4–6 use the rural drought index (the index times the rural population share).

**Reading the results (pp. 131–132).**
- Column 1: the t-statistic is −1.9. A typical state-year (index about 11) costs the incumbent party 0.7 points. "Extreme" conditions (24 or more) cost about 1.5 points. (Check, added step: $0.060 \times 11 \approx 0.66$ and $0.060 \times 24 \approx 1.44$.)
- Column 2: the election-year effect is similar. Drought in two of the three earlier years has additional, slightly smaller negative effects.
- Column 3: the time-weighted index doubles the weight for each year closer to the election, with weights .06667, .13333, .26667, .53333 (fn. 26). Its effect is −0.104 (t = −2.3), costing about 1.1 points in a typical state-year.
- Columns 4–6: the rural versions show a similar pattern. For example, column 4 implies a 0.6% loss in a typical state-year.
- The authors say the consistency of results "should leave little doubt" that droughts and wet spells reduced the president's party's support. They also tried separate dry/wet effects, nonlinear indices, secular trends, interactions with prior partisanship, and local–national interactions. None added significantly, though all showed drought effects (p. 132, fn. 27).

**Variation across elections (pp. 132–133).** Figure 5.4 gives election-specific estimates. Almost half are more than twice as large as the overall estimates, and a few are up to five times as large. The authors say that explaining this variation (e.g., ranchers versus farmers, per Barnhart) is beyond the scope of the chapter (p. 132).

**The 2000 election (pp. 133–135).**
- Average absolute PHDI was about 10% above the historical average. Drought was severe in parts of the South and West, and wetness was excessive in the Dakotas, New York and Vermont (p. 133).
- Table 5.3 (dependent variable: Democratic vote % by state; $N = 48$; controls: 1996 and 1992 Clinton vote, percent rural, South; p. 134):

| Index | Estimate (SE) |
|---|---|
| Election-year | −0.231 (0.073) |
| Rural | −0.546 (0.259) |
| Time-weighted | −0.310 (0.103) |

- Fit is very good: standard errors 1.94, 2.06 and 1.96; adjusted $R^2$ .92, .91 and .92 (p. 134).
- The t-statistics range from −2.1 to −3.2. The implied national loss for the Democrats is 1.6 to 3.6 points. The best-fitting model, with the simple election-year index, gives 2.7 points (p. 135).
- The authors say this means 2.8 million people voted against Gore because their states were too dry or too wet. Attributing the votes to states in proportion to their drought scores, the cost was seven states (Arizona, Louisiana, Nevada, Florida, New Hampshire, Tennessee, Missouri). That is almost three times as many electoral votes as Florida's "butterfly ballot" (p. 135).

> *Intuition note.* Because droughts and floods strike states at random times, comparing hit and unhit states in many elections gives a fairer test than one famous case. The average effect is modest but one-directional, and in a close election it can matter.

### Holding incumbents responsible: why so much punishment? (pp. 135–138)
The authors say many readers feel "a powerful urge" to defend voter rationality, so they address three defences (p. 135).

**Defence 1: voters blame government for worsening the damage, not for the disaster (pp. 135–136).**
- **Barnhart on 19th-century Nebraska:** farmers did not blame politicians for lack of rain, but politicians were held responsible for some of the conditions that the drought made worse. "They could not make it rain, but they thought they could lower railroad rates" (p. 136).
- **Authors' reply (p. 136):**
  - This reading has a strong policy component. If voters learned that more intervention is needed, droughts should push electorates left.
  - Instead droughts reduce support for incumbents regardless of ideology. In 1890s Nebraska the result was left-wing gains. Where left-wing governments were in power, as in the 1930s Dust Bowl, drought produced right-wing surges.
  - If New Jersey voters in 1916 wanted a stronger safety net, swinging to Wilson's Republican opponent was "politically quite illogical".
  - What voters learn has a very short half-life. In table 5.2, droughts in the first half of a term have no consistent influence. By 1920 the Ocean County beach areas were 8 points more favourable to Wilson's party than the near-beach, the reverse of 1916.
  - The authors conclude that short-term anti-incumbent voting without substantial policy content is "the only common pattern" (p. 136).

**Defence 2: voters punish insufficient responses (pp. 136–137).**
- **The defence:** voters monitor responses as they monitor other performance, to select competent leaders and give incentives. This fits the logic of chapter 4.
- **Authors' reply:**
  - A competent electorate must recognise that incumbents' responses are better than average about half the time. Punishing the better-than-average ones is counterproductive for both selection and incentives.
  - Rational electorates should therefore reward as often as they punish, and the average effect over all droughts and floods should be about zero.
  - Instead the table 5.2 effects are "preponderantly negative". Politicians can sometimes win credit or shift blame, but voters "are much more apt to punish their leaders than to reward them" (p. 137).
  - In human terms this is understandable. Voters see neighbours help at once, while bureaucracies with anti-fraud rules look heartless or slow. If money flows freely, citizens complain of waste. Either way the government looks inept (p. 137).

**Defence 3: the version more consistent with the evidence (pp. 137–138).**
- On this view voters punish any time their well-being is below "normal", whether incumbents performed well or badly.
- Disasters cause hardship even under competent responses, so this rule means frequent punishment after disasters, matching the evidence.
- It is "rational" in chapter 4's technical sense if voters cannot distinguish relevant from irrelevant sources of well-being. The authors say this "is just what we mean by blind retrospection" (p. 138).

> *Intuition note.* If voters judged government performance, good and bad responses to disasters should roughly cancel. The data show net punishment instead. The authors read this as evidence that voters respond to pain itself, not to performance.

### The social construction of blame (pp. 138–142)
- So far the text treated hardship as if it alone caused backlash. The authors now say that voters' attributions of blame are "often crucial". Even irrelevant events such as local football outcomes may affect votes through mood (Healy, Malhotra, and Mo), but substantial punishment is "likely to be grounded in a belief, however farfetched" that government is responsible (p. 138).
- Explanations are typically mass-produced. Political and ideological entrepreneurs have incentives to build self-serving explanations, and the media amplify them. In ordinary recessions the stories are familiar and the process goes unnoticed. Natural disasters create unfamiliar hardship, uncertainty, and fear, and "people are ready to listen" (p. 138).
- Popular blame often comes from trusted sources and appeals to broadly shared values in a clear, simple way. If a "nutty or dangerous" vision spreads, demagogues may ride it (p. 139, citing Cantril).
- Elite culture is "usually (though not always)" less susceptible, but popular culture is "never entirely under the control of the respectable" (p. 139).
- Examples of unconventional attributions (p. 139):
  - medieval towns blamed the plague on Jews, prostitutes, beggars, or foreign agents;
  - some New Jersey residents in 1916 thought German U-boats induced the sharks;
  - some Americans in 1918 feared Bayer aspirin contained plague germs.
- **Contested explanations can protect incumbents.** In the 1793 yellow fever epidemic, Republicans blamed sanitation and climate while Federalists blamed Haitian refugees. If interpretations are sufficiently contested and incumbents can exploit this, they may sometimes escape blame (p. 139).

**Blame can fail because of too few explanations: Nebraska 1874 (pp. 139–140).**
- Locusts devastated western Nebraska, and farmers faced starvation. The Army delayed distributing clothes until after the fall election and food until February.
- The incumbent Republicans still won, and repeated locust plagues in the mid-1870s did not notably dent their popularity.
- The authors' "simplest explanation is probably" the following: communication was poor and no shared interpretation emerged, self-reliance was a strong ethic, and "perhaps most important" the Populists were not organised until a decade later. When they ran a serious campaign in 1890, "punishment began" (p. 140).

**The 1918 flu as a test case (pp. 140–142).**
- The authors predict that if their interpretation is right, a disaster the government was plausibly responsible for should go unpunished when opponents never construct the case for responsibility (p. 140).
- The pandemic killed 20–40 million worldwide (some estimates up to 100 million) and about half a million Americans, more than US battle deaths in four wars combined (p. 140).
- They examined the 1918 midterm vote using mortality data from 16 states and 29 cities, and the 1920 presidential vote. They found no reliable statistical evidence that voters punished anyone. The results were imprecise, and some implausibly showed governors gaining votes in high-death cities (pp. 140–141, fns. 29–30).
- The exception: in New Mexico, Wilson attacked Republican Senate candidate Fall while Fall grieved his children's deaths. Fall won by fewer than 2,000 votes, and Crosby argues the attack backfired from sympathy (p. 141).
- The authors think a rational electorate could reasonably have held leaders partly accountable, since efforts to stem or track the contagion were "slow and disorganized" (p. 141).
- Their reasons for no retribution (pp. 141–142):
  1. the country was at war, so criticism seemed unpatriotic;
  2. government and press downplayed the risk;
  3. victims were scattered, and people could not tell "excess deaths" from usual ones;
  4. most important, no elite or popular discourse attributed responsibility to Wilson or other officials.
- In Deborah Stone's terms, voters saw the pandemic as part of the natural world ("fate and accident") rather than the social world ("control and intent"). The authors add that such understandings are subject to change; fn. 31 notes the Ford administration's aggressive response to the 1970s swine flu scare (p. 142).
- The authors' summary: while hundreds of thousands died, "no one thought to blame the pharaoh" (p. 142).

> *Intuition note.* The flu case reverses the usual pattern. The pain was enormous but unpunished, because nobody told a story linking it to the government. Sharks were punished because that story existed.

### Conclusion (pp. 142–145)
- In most recent accounts retrospective voting is natural and rational. The authors say it is natural but "not so obviously rational", and that blind retrospection challenges conventional accountability (p. 142).
- The century of droughts and floods "seems to us to rule out" the idea that voters were reacting to subpar handling. It is hard to see how presidents' handling could have been substantially worse than average over a century (p. 143).
- Voters may themselves contribute to poor preparedness by insisting on low taxes. Punishment is then self-defeating, because its randomness makes advance investment pointless for incumbents (p. 143, citing Healy and Malhotra 2009).
- **Fiorina's view as an objection:** perhaps voters should "only calculate the changes in their own welfare". Perhaps a few leaders suffer needlessly, but every incumbent gets a strong incentive to maximise welfare (p. 143).
- **Authors' reply:** in a narrow technical sense this is right when voters are utterly ignorant about whether leaders' actions affect them. But "Crazy beliefs can make crazy behavior 'rational'", and chapter 4's models show that ignorance is costly (p. 143).
- Their account strikes the common normative justification that voters can recognise good or bad performance. Real voters often have only a vague understanding of the link between incumbents' actions and their own welfare, and even professionals struggle (pp. 143–144).
- To translate conditions into political judgement, citizens must find and accept a valid cultural understanding of causation. Elite culture helps constrain scapegoating, but the folk culture of ordinary citizens matters as much or more. How a story becomes plausible is hard to trace, and "nothing very rational" governs it (p. 144).
- "Rough justice" from such voters is likely to be very rough. The rougher it is, the less reason incumbents have to serve voters. Such voters may therefore suffer more misguided tax policies and foreign wars (p. 144).
- This is hard to square with the folk theory of democracy. The authors close with the claim that "Blind retrospection afflicts us all". They attribute it to social complexity and human cognitive limits, and say it shows the conventional account underestimates the limits of democratic accountability (p. 145).

## Toy example (ours, not from the text)
**Setup A: differences-in-differences.** Town B is on the beach and town N is inland. The incumbent's vote share is:
- Town B: 1912 = 40%, 1916 = 30%.
- Town N: 1912 = 40%, 1916 = 39%.

Change in B = 30 − 40 = −10. Change in N = 39 − 40 = −1. Estimated disaster effect = −10 − (−1) = −9 points. This is the same logic as the Ocean County comparison (pp. 126–127).

**Setup B: rewards versus punishments.** Six districts suffer disasters. Each incumbent's response is better than average in 3 districts and worse in 3.
- *Performance-based voter:* gives +1 point for a better-than-average response and −1 for a worse one. Total = 3(+1) + 3(−1) = 0, so the average effect is 0/6 = 0.
- *Blind voter:* gives −1 whenever well-being is below normal. All six districts are hurt, so total = 6(−1) = −6 and the average is −6/6 = −1.

Table 5.2 shows a negative average, which fits the blind pattern better than the balanced one (p. 137).

## Concepts
- [[blind-retrospection]] (new) — voters punish incumbents for hardship whatever the government's actual responsibility, if a blame story is available (p. 118)
- [[retrospective-voting]] — judging incumbents by past outcomes. The authors call it natural but not obviously rational (p. 118, p. 142)
- [[social-construction-of-blame]] (new) — voters need a cultural story linking hardship to government before they punish it; elites, entrepreneurs, and folk culture supply it (p. 138)
- [[principal-agent-problem]] — used here for the argument that voters monitor responses to disasters to select and motivate leaders (p. 136)
- [[folk-theory-of-democracy]] — the view that citizens critically assess candidates and choose by their values. Blind retrospection is hard to square with it (p. 145)
- [[palmer-hydrological-drought-index]] (new) — an index of long-term moisture supply. Zero is ideal, negative means drought, positive means wet. Here the absolute value is summed May–October (pp. 128–129)
- [[difference-in-differences]] (new) — comparing vote change in affected and unaffected places, as in the Ocean County analysis (p. 126, fn. 17)

## Canonical instances
- [[nj-shark-attacks-1916]] — Wilson lost about 3 points in beach counties and about 10 in shore townships after random shark deaths (pp. 122–127)
- [[drought-flood-elections-1900-2000]] — incumbent-party state vote falls with absolute PHDI across 26 elections (pp. 129–132)
- [[drought-2000-election]] — climate distress cost Gore an estimated 2.7 points nationally, about 2.8 million votes and seven states (p. 135)
- [[nebraska-locusts-1874]] — heavy suffering, no punishment until Populists supplied an explanation in 1890 (pp. 139–140)
- [[influenza-1918]] — huge mortality with no detectable electoral retribution, because no blame story arose (pp. 140–142)

## Bridges (candidates)
- [structural-analogy] Blind retrospection (punish when well-being is below a fixed standard) ↔ political-science: retrospective voting as a principal–agent monitoring rule (book chapter 4) — the same voter rule, judged as sensible by one account and as weak accountability by the other.
- [structural-analogy] Differences-in-differences comparison of beach versus near-beach towns ↔ causal inference: natural experiments, where random events act as treatments.
- [structural-analogy] Need for a socially supplied blame story ↔ political-science: framing and elite cues (canon link; not stated in this unit).

## Questions this raises
- How would one distinguish voters who punish pain blindly from voters who judge competence, when both predict some punishment after disasters?
- What makes a blame story catch on in some disasters (sharks, 1890 Nebraska) and not in others (1918 flu)?
- If incumbents are punished randomly, how far do they reduce effort ex ante, as the authors argue?
- Do the findings from US presidential elections generalise to other countries and to modern media environments?

## Reading notes
- Page offset: printed = pdf − 19 (pdf 135 = printed 116). The pdf range 135–164 corresponds to printed 116–145.
- Page images were supplied only for pages 122, 123, 125, 127, 130, 133 and 134 (mostly table and figure pages; p. 122 is a text page).
- In the text layer (no image for p. 129), fn. 22 gives separate drought and wet-spell effects as ".067" and ".066" with no minus sign. Table 5.2 column 1 shows −0.060, so the signs may be missing from the text layer or the print (the source does not say).
- Fn. 21 (p. 128) lists PHDI "values less than 4" as extreme drought. The text layer shows no minus signs for the drought values (no image for that page), so the printed wording may be missing them.
- Table 5.2 reports $N = 1{,}233$; the text refers to 26 elections and 48 states without explaining the count (26 × 48 = 1,248; the difference is not explained in the unit).
- The text layer says the resort losses were "a sizable sum in 1918" (p. 119, no image for that page); the season in question is 1916.
- Text gives Beach Haven and Spring Lake drops as 11 and 9 points; figure 5.2 bars look slightly smaller (about −10.5 and −8.6).
- The authors cite "Brader n.d." (p. 137); the pages give no further detail on the work's date or status.
