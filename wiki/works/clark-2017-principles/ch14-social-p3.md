---
id: clark-2017-principles/ch14-social-p3
work: clark-2017-principles
unit: "14 Social Cleavages and Party Systems (part 3/3: Duverger's theory, evidence, conclusion, problems)"
pages: 641–672
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Number of Parties: Duverger's Theory of Social Cleavages and Electoral Institutions

## L0 — One line
The size of a party system depends on the interaction of social heterogeneity (the demand for parties) and the permissiveness of electoral rules (how much of that demand is allowed through).

## L1 — The gist (≤ 120 words)
Why do some countries have many parties and others few? Following Duverger, the chapter argues that social divisions create demand for parties, but electoral rules decide how much of that demand becomes parties that win votes and seats. Disproportional systems such as single-member district plurality (SMDP) penalise small parties in two ways: a mechanical effect (votes into seats) and a strategic effect (voters and politicians desert small parties). Expecting two parties nationally from Duverger's law requires the same two parties to dominate most districts. Data from 1980s democracies, and from 1946–2000 data using district magnitude (seats per district), fit the interaction: more ethnic groups raise party numbers under permissive rules but not under nonpermissive ones.

**Prerequisites:** SMDP vs PR electoral systems; effective number of parties (formula restated on pp. 668–669); sincere vs strategic voting; normal-form games and Nash equilibrium; reading simple scatterplots and regression slopes.

## L2 — Key ideas (5–10 bullets)
- The social "engine": the number of parties demanded depends on the number of *cross-cutting* cleavages, not the raw number of cleavages. Cross-cutting cleavages are ones where group memberships are uncorrelated. Reinforcing cleavages (correlated memberships) merge latent (not yet politicised) identity groups (pp. 642–643).
- Electoral rules act as a "brake" (Duverger's metaphor). Social heterogeneity matters less for party-system size when the system is nonproportional (p. 644).
- Mechanical effect: disproportional systems turn votes into seats at a worse rate for small parties. How badly depends on how geographically dispersed a party's support is (pp. 644–648).
- Strategic effect: voters (strategic voting) and elites (strategic entry, mergers) abandon small parties in disproportional systems. Small parties get fewer votes than their latent support, and may never form (pp. 648–652).
- Duverger's law (SMDP systems encourage two-party systems) works at the district level. A national two-party system needs the same two parties to win across districts ("nationalization"), which depends on centralisation, presidentialism and cleavage patterns (pp. 654–657).
- Interaction prediction: many parties arise only with high heterogeneity *and* a permissive system. Table 14.16 shows 3.88 effective legislative parties (a party count weighted by size) in that cell and 1.68–3.06 in the others (pp. 658–660).
- Mechanical distortion is larger under single-member districts (SMD; slope 0.61) than under multimember districts (0.92) (p. 661). More ethnic groups raise party numbers under permissive rules but not under nonpermissive ones (pp. 663–665).
- Using average district magnitude as a continuous measure, the effect of one more ethnic group grows with magnitude, from about zero at magnitude 1 to about 1.4 electoral parties at magnitudes 120–150 (pp. 665–666).
- The authors say we understand how many parties form much better than which types form (p. 667).

## L3 — Walkthrough

*Where this part begins:* it opens at the end of the section on politicized cleavages. Figure 14.1 shows latent cleavages being filtered by electoral institutions into politicized cleavages. The sentence that ends on p. 641 (its start lies before this unit) gives reasons for a change: the underlying latent cleavages change, the electoral rules change, or both (p. 641).

### Number of Parties: Duverger's Theory (p. 641)
The authors say we know more about *how many* parties form than about *which* parties form (p. 641).

#### Social Cleavages (pp. 641–643)
- **Duverger's claim:** the primary engine of party formation is social divisions. The more divisions, the greater the demand for parties. Cleavages in society tend to be represented in the party system (p. 641).
- It is not the number of cleavages per se, but how membership is *distributed across* them, that determines the pressure for distinctive representation (p. 641).
- **Hypothetical example (Latin America).** Countries A and B both have three attributes: income (rich/poor), place of origin (European/indigenous), religion (Catholic/Protestant). In both, exactly half are rich, half European, half Catholic (p. 642).
- **Country A (Table 14.11):** every one of the eight attribute combinations holds 12.5% of citizens (rich European Catholic, rich European Protestant, and so on). Cleavages are entirely cross-cutting, because there is no correlation between income, origin and religion (p. 642). Many identity categories are "equally distinctive and, presumably, equally likely to be activated." With policy preferences tied to these attributes, Duverger's "engine" pushes country A toward a large multiparty system (p. 642). (Electoral rules are deliberately ignored at this stage, fn. 12.)
- **Country B (Table 14.12):** half of the rich and half of the poor are European, but *all rich are Catholic and all poor are Protestant* (p. 642). Cells: rich Catholic European 25.0, rich Catholic indigenous 25.0, poor Protestant European 25.0, poor Protestant indigenous 25.0; all other cells 0.0 (p. 643).
  - Income × origin is cross-cutting: origin does not predict income. Income × religion is reinforcing: religion predicts income (p. 642).
  - There are now only four latent identity categories, even though B has the same three cleavages as A (pp. 642–643).
  - If origin were also perfectly correlated with income, only two latent groups would remain: rich Catholic Europeans and poor Protestant indigenous people (p. 643).
- **Conclusion:** the key social factor for the number of parties is the number of *cross-cutting* cleavages, not the total number of cleavages. Real cleavages are rarely perfectly cross-cutting or reinforcing. The same logic suggests that pressure for distinctive representation depends on the number of cleavages and increases with the degree to which they are cross-cutting rather than reinforcing (p. 643).

> *Intuition note.* Count the groups you would need to represent, not the dimensions on which people differ. If religion already tells you income, religion and income describe the same split. A country with many *independent* splits has many distinct groups.

#### Electoral Institutions (pp. 643–644)
- Duverger believed social divisions create the demand, but electoral institutions determine whether the latent demand produces new parties (p. 643).
- **Motivating puzzle:** a post-materialist cleavage emerged in Europe from the 1960s (Inglehart). If cleavages were the only factor, all European countries should have seen more parties. Kitschelt (1988) finds a significant rise only in the vote share of "left-libertarian parties" in *some* countries (p. 643).
- One possible explanation is that the value shift was stronger in some countries. Duverger instead points to electoral rules: nonproportional systems such as SMDP act as a "brake" on translating cleavages into parties (pp. 643–644).
- **Duverger's theory (as stated here):** increasing the number of social cleavages has less effect on party-system size if the electoral system is nonproportional than if it is proportional. There are two reasons, the mechanical and the strategic effects (p. 644).

#### The Mechanical Effect of Electoral Laws (pp. 644–648)
- **Definition:** the mechanical effect is the way votes are translated into seats. All electoral systems systematically punish small parties and reward large ones. The extent depends on proportionality, and small parties find it hardest in highly disproportional systems such as SMDP (p. 644).
- **Duvergerland (hypothetical).** The electorate was divided fairly evenly between a workers' party (Labor) and a business party. The 100-seat legislature is elected by SMDP. Then 20% of voters back a new Green Party, with the rest split in different ways between Business and Labor in each district (p. 644).
  - The Green share is 20% in every district, but one of the other parties always wins more than 20%. Result: no Green seat (p. 644, Fig. 14.2).
  - Seats (Fig. 14.3a): Labor and Business each get close to 50%. Three parties have voter support but only two reach the legislature (pp. 644–645).
  - Under PR in a single national district, the same votes give the Greens 20 seats (Fig. 14.3b). The difference is the mechanical effect of SMDP (p. 645).
- **United Kingdom, St. Ives, 1992 (Table 14.13):**

| Candidate | Votes | % |
|---|---|---|
| Harris (Conservative) | 24,528 | 42.9 |
| George (Liberal Democrat) | 22,883 | 40.1 |
| Warr (Labour) | 9,144 | 16.0 |
| Stevens (Liberal) | 577 | 1.0 |

  Harris wins by fewer than 2,000 votes (24,528 − 22,883 = 1,645, added step). George, with 40%, gets nothing (pp. 645–646).
- **National totals, UK 1992 (Table 14.14, %; p. 647):**

| Party | Votes | Seats |
|---|---|---|
| Conservative | 41.9 | 51.6 |
| Labour | 34.9 | 41.6 |
| Liberal Democrats | 17.8 | 3.1 |
| Others | 5.4 | 3.7 |

  - The two big parties won about 20 percent more seats than their vote shares suggest (the author's wording, p. 646). For the Conservatives this "electoral bonus" turned a plurality of votes into a seat majority (p. 647).
  - The Liberal Democrats got 3.1% of seats with 17.8% of votes (p. 647).
  - Footnote 13: SMDP is sometimes called "majoritarian," although only a plurality in a district is needed (p. 647).
- **Dispersion matters.** The punishment of small parties under SMDP depends on how their votes are distributed across districts (p. 648).
  - Greens in Duvergerland: evenly spread, so no seats.
  - The Liberal Democrats (about 20 seats, i.e. the 3.1%) had support that varied across districts, and some districts were big enough to win. Even so, with support broadly spread over many districts, the Liberal (Democratic) party has generally been penalised heavily (p. 648).
  - Small regional parties (Plaid Cymru, the Scottish National Party, Sinn Féin, the Ulster Unionists) have a much smaller national vote share but little disadvantage, because their support is concentrated in a few districts (p. 648).

> *Intuition note.* Under SMDP a district gives its seat to one party only. In Duvergerland a party with 20% in every district wins nowhere, because another party always beats it. A party with 20% nationally but concentrated in a few districts (like the UK regional parties) can win those districts. The same national vote share can produce zero or several seats.

#### The Strategic Effect of Electoral Laws (pp. 648–652)
- **Definition:** the strategic effect is how the translation of votes into seats influences the "strategic" behaviour of voters and political elites. Anticipating the mechanical effect, voters have an incentive to vote strategically and elites to enter strategically. Both help large parties further (p. 648).

**Strategic voting.**
- Strategic voting means voting for your most preferred candidate *who has a realistic chance of winning*. Sincere voting means voting for your most preferred candidate or party (pp. 648–649).
- **St. Ives example:** your ranking is Labour > Liberal Democrat > Conservative (L > LD > C). Polls show Labour trailing the other two by a wide margin. A sincere Labour vote is likely "wasted"; voting LD gives you a better chance to stop the Conservative, your least-preferred candidate (p. 649).
- The incentive grows as the electoral system becomes more disproportional. Small parties are therefore penalised twice: by the seat translation and by voters not voting for them in the first place. Large parties gain from the bonus and from strategic votes (p. 649).

**Strategic entry.**
- **Definition:** the decision by elites whether to enter under the label of their most preferred party, or under the label of their most preferred party *with a realistic chance of winning* (p. 649).
- An environmentalist entrepreneur in Duvergerland could run for the Greens, who would not win under SMDP given the distribution of support. Or the entrepreneur could work within a party that has a chance of commanding a legislative majority (pp. 649–650).
- Under PR the trade-off is less stark, because even small vote shares can win seats, and small-party leaders may become kingmakers or sought-after junior coalition partners (p. 650).
- **Comparison:** the Free Democratic Party (FDP) in Germany (proportional mixed system) was nearly constantly in cabinets. The UK Liberal Party (SMDP), with a similar ideological position, was long on the sidelines until very recently (p. 650).
- The authors infer that small parties in SMDP systems find it harder to attract and keep high-quality leaders and private funding, which in turn makes winning votes harder (p. 650).
- Before the Greens exist, the same logic discourages forming them at all. Disproportional systems mean small parties get lower vote shares *and* are less likely to exist (p. 650).

**The Strategic Entry Game (Fig. 14.5, p. 651).**
- *Setup (author's assumptions):* two left parties L1, L2 and one right party R.
  - If both left parties run, the left vote splits and R wins for sure. If only one left party runs, R is defeated (pp. 650–651).
  - Each left party's worst outcome is both running, with R winning. Its best is the other left party dropping out and itself winning (p. 651).
  - Payoffs are normalised (the authors note this loses no generality): worst = 0, best = 1. A parameter $\lambda$ is the value each left party places on its fellow left party running *instead of it*. It is better than R winning but worse than winning itself (p. 651).
  - The text prints the restriction as "0 > λ > 1", which is a misprint; the logic implies $0<\lambda<1$ (see Reading notes).
- *Normal form* (row = L1, column = L2; payoffs L1, L2):

| | L2 Run | L2 Don't run |
|---|---|---|
| **L1 Run** | 0, 0 | 1, $\lambda$ |
| **L1 Don't run** | $\lambda$, 1 | 0, 0 |

- *Result:* two pure-strategy Nash equilibria, (Run; Don't run) and (Don't run; Run). Each party has an incentive to drop out if the other does not (p. 651).
  - (Added step: with $0<\lambda<1$, if L2 does not run, L1 gets 1 from running and 0 from staying out; if L1 runs, L2 gets $\lambda>0$ from staying out and 0 from running. Neither (Run, Run) nor (Don't run, Don't run) is an equilibrium, since each party gains by switching.)
- This is a mixed-motive, "asymmetric coordination game" (fn. 14). The parties share a goal (defeat R) but disagree on who should carry it. They may know they should withdraw but fail to agree who does, and the one that stays in helps elect its most bitter rival (pp. 651–652).
- **Examples given:**
  - France, 2002 presidential election: the left vote was split among so many candidates that the Socialist leader Jospin came third behind the extreme-right Le Pen. The authors say this "political earthquake" had as much to do with the left's failure to solve its coordination problem as with extreme-right strength (p. 652).
  - US, 2000: Nader's presence split the left vote, particularly in Florida, so that Bush defeated Gore in the Electoral College (p. 652).
- **A solution: merger.** The Liberal Party and Social Democratic Party merged into the Liberal Democratic Party in 1988. The more disproportional the system, the greater the incentive for small parties to merge or form coalitions (p. 652). The incentive can also deter entry: a forward-looking entrepreneur may stay in an existing party rather than risk electing a less-desired party (p. 652).
  - Fn. 15: pre-electoral coalitions are an alternative. Fn. 16: fusion candidates (several parties nominating the same candidate) help parties keep separate identities; their ending contributed to the US two-party system outside New York. Two-round systems are also thought to encourage parties to stay separate (p. 652).

> *Intuition note.* Strategic voting and strategic entry both rest on one fact: in a winner-take-all contest a vote or candidacy for a hopeless party can help the rival you like least. So fewer people back or form small parties, which makes them weaker still.

#### Summarizing Duverger's Theory (p. 653; Fig. 14.6, p. 654)
- Party-system size depends on the interplay of social and institutional forces. Social structure drives party formation. Electoral institutions determine how much demand turns into **electoral parties** (win votes) and **legislative parties** (win seats) (p. 653).
- Disproportional systems give a smaller "input-output" ratio from votes to seats for small parties than for large ones. Proportional systems translate at a roughly constant rate (p. 653).
- Two routes to fewer new parties: (1) the mechanical effect leaves small parties with fewer seats than PR would give; (2) the strategic effect leaves them with fewer votes than their latent support suggests (p. 653).

### Evidence for Duverger's Theory (pp. 653–666)
- **Two testable statements** (the author calls them "observational implications"):
  - *Duverger's law:* SMDP systems encourage two-party systems.
  - *Duverger's hypothesis:* PR rules favour multiparty systems (p. 653).
- **Caveat:** the prediction of two-party systems under SMDP is a valid inference from the broader theory *only when some auxiliary assumptions are satisfied*. Duverger himself noted that the mechanical and strategic logic works at the district, not the national, level (pp. 653–654).
  - Example: if Labour has no chance in St. Ives, the strategic-voting benefit goes to the Conservatives and LDs *there*. In most UK districts the LDs are the "also ran," so Conservative and Labour benefit (p. 654).
  - A national two-party system is expected only to the extent that the same two parties are favoured across the "lion's share" of districts. If some parties are favoured in some regions and others elsewhere, the offsetting distortions may leave a multiparty system with national seat shares close to vote shares (p. 655).

**Box 14.4 — Nationalizing party systems (pp. 655–657).**
- A party system is *nationalized* if local and national party systems are of similar size. There can be more parties nationally than on average per district (p. 655).
- **Centralisation (Chhibber and Kollman):** nationalization is more likely when political and economic power is centralised in the national government. Parties with little chance at the national level, even if top-two locally, tend to be abandoned by voters and entrepreneurs (p. 655).
- **US data (Fig. 14.7, effective number of parties, 1790–1990, p. 656):**
  - The district-level average is about two throughout.
  - The national number varied considerably. Before the 1930s New Deal it was often much larger than two, because minor parties (Labor, Progressives, Socialists, Prohibitionists, Farmers) were locally dominant in some regions and periods.
  - Since the 1930s there has been little difference between local and national. Chhibber and Kollman explain this by centralisation: national spending as a share of total government spending more than doubled, and as a share of GNP rose almost tenfold (p. 656).
- **Hicken (2009):** if power is centralised and *not shared* across branches, national office is especially valuable. This creates stronger incentives to solve cross-district coordination problems like the Strategic Entry Game, giving Duvergerian dynamics at both levels (p. 657).
- **Presidential elections (M. Golder 2006):** a presidency attracts few viable candidates, so parties without a viable presidential candidate tend to be abandoned. Nationalization is more likely if the president's power is large relative to other actors and if presidential and legislative elections coincide (p. 657).
- **Cleavage pattern:** if the same cleavages dominate each region, the party system is likely to be national. If politicized cleavages vary by region, it is likely to be less nationalized. Whether regional cleavages become parties still depends on how permissive the electoral system is (p. 657).

**Why the cautions do little damage (p. 657).** Duverger's theory is more about how *changes* in social conditions or electoral laws change the number of parties, and considerable evidence fits his predictions there (citing Amorim Neto and Cox 1997; Brambor, Clark and Golder 2007; Clark, Gilligan and Golder 2006; Clark and Golder 2006; Cox 1997; Ordeshook and Shvetsova 1994) (p. 657).

**Metaphors (pp. 657–658).**
- *Car:* social structure is the engine, electoral laws the brake pedal (p. 657).
- *Dam:* social divisions create a storm of demands. Electoral laws moderate how they flow downstream into parties. SMDP is a closed dam, and PR an open dam. Hence PR is called *permissive* and nonproportional systems *nonpermissive* (p. 658).
- The effect of social structure depends on permissiveness, and the effect of the electoral system depends on social structure (p. 658). Table 14.15 (pp. 658–659) gives the four scenarios:

| | Low permissiveness (SMDP) | High permissiveness (PR) |
|---|---|---|
| **High heterogeneity** | Few parties | Many parties |
| **Low heterogeneity** | Few parties | Few parties |

  - High heterogeneity + open dam: demands flow through, so many parties. High heterogeneity + closed dam: some demands form a "reservoir" and are not translated into parties (p. 658).
  - Low heterogeneity is like a dry river: little reaches the dam whether open or closed, so few parties either way (pp. 658–659).
- **Implication:** there are two reasons for few parties (nonpermissive rules, or few social divisions) but only one route to many parties, a heterogeneous society *and* a permissive system, according to Duverger's theory (p. 659).

> *Intuition note.* In Duverger's theory the effect of each factor depends on the other, rather than the two simply adding up. With low heterogeneity, changing the electoral rule is expected to change little. With a nonpermissive rule, adding diversity is expected to change little. According to the theory, only the combination of the two produces many parties (pp. 658–659).

**Test 1: the 2×2 table (Table 14.16, p. 659).** Clark, Gilligan and Golder (2006); 54 democracies in the 1980s. Party-system size is the effective number of legislative parties. Permissiveness: single-member districts = low, multimember = high. Heterogeneity: effective number of ethnic groups above the sample median = high, below = low.

| | Low permissiveness | High permissiveness |
|---|---|---|
| High heterogeneity | 1.68 | 3.88 |
| Low heterogeneity | 2.52 | 3.06 |

- The highest average is with high heterogeneity and a permissive system (p. 659).
- With high heterogeneity, the gap 3.88 − 1.68 is what the authors call the reductive effect of nonpermissive laws when heterogeneity is high (p. 660).
- With low heterogeneity, 2.52 vs 3.06 is *not* statistically significantly different. This suggests closing the floodgates matters less when the river is low, as Duverger predicts (p. 660).

**Test 2: mechanical effect (Figs. 14.8–14.9, pp. 660–662).**
- Data: 52 democracies in the 1980s (fn. 18: two of the original 54 are dropped because they show slightly more legislative than electoral parties, which is not possible unless seats are reserved) (p. 660).
- Plotting legislative against electoral effective number of parties: with no distortion, a country lies on the 45-degree line (slope 1). Most countries lie below it, so the mechanical process reduces the number of parties. The vertical distance from the line measures the mechanical distortion (p. 660).
- Duverger's theory implies a smaller slope (more distortion) in nonpermissive systems. Fitted lines: **0.92** for multimember districts, **0.61** for single-member districts (p. 661).
  - One extra electoral party yields 0.92 legislative parties in permissive systems and 0.61 in nonpermissive ones (p. 661).
  - Distortion reduces the effective number of parties by $1-0.92 = 8\%$ (permissive) and $1-0.61 = 39\%$ (nonpermissive) (the arithmetic is added). The authors say that, on average, nonpermissive systems are almost five times as distortionary as permissive ones (p. 661; $39/8\approx 4.9$, added step).
- Fig. 14.9 note: Ecuador is a huge outlier and is excluded from the multimember-district line. Including it, the slope is 0.73, still significantly larger than the single-member slope (p. 662).

**Test 3: strategic effect with ethnic groups (Figs. 14.10–14.11, pp. 662–665).**
- *Measure:* the effective number of ethnic groups is built like the effective number of parties, but uses each group's population share (p. 662; values for 54 democracies are in Table 14.2, outside this unit).
- *Mechanism (Chandra 2004, "ethnic head count"):* under SMDP, ethnic groups check whether co-ethnics are numerous enough to win a constituency. If so, they form and vote for an ethnic party. If not, they vote for a nonethnic party or redefine group boundaries (pp. 662–663).
  - *Example:* in Gujarat, India, Kshatriya entrepreneurs (about 5% of the population) enlarged their group after independence in 1947. One admitted: "We have taken all the backward people who are martial by nature and called them Kshatriyas" (p. 663). (Fn. 19: Dominicans, Mexicans, Puerto Ricans and others are often mobilized as "Hispanics" or "Latinos" in the US.)
  - Plurality rule means a group must be bigger than any other group in the district. In permissive systems a party only has to pass the natural or legal threshold. So permissive systems should translate many ethnic groups into many parties, but nonpermissive ones need not (p. 663).
- *Fig. 14.10 (ethnic groups → electoral parties):* slope **+1.24** in permissive systems. In nonpermissive systems the slope is **−0.36**, not statistically significant. The authors conclude there is no relationship in nonpermissive systems (pp. 663–664). The slope difference reflects the strategic effect. A slope above one means each effective ethnic group is represented by more than one party, one interpretation being that parties also form around other cleavages (p. 664).
- *Fig. 14.11 (ethnic groups → legislative parties; total mechanical + strategic effect):* slope **0.84** (multimember) vs **−0.43** (single-member). An extra ethnic group gives close to a full effective legislative party in permissive systems but essentially zero in nonpermissive systems (pp. 664–665).

**Test 4: district magnitude as a continuous measure (Table 14.17, pp. 665–666).** Duverger identified district magnitude as the single most important way electoral systems differ (p. 665). Clark and Golder (2006) use all democracies, 1946–2000. Effect of one additional ethnic group:

| District magnitude | Sample countries | Electoral parties (labelled "Strategic effect") | Legislative parties (labelled "Mechanical effect") |
|---|---|---|---|
| 1 | Australia, Canada, US, UK | 0.11 | 0.07 |
| 2 to 5 | Chile, Thailand, Ireland | 0.29–0.54 | 0.20–0.39 |
| 5 to 10 | Greece, Argentina, Spain, Honduras | 0.54–0.72 | 0.39–0.55 |
| 10 to 20 | Portugal, Finland, Brazil, Luxembourg | 0.72–0.90 | 0.55–0.72 |
| 120 to 150 | Israel, Netherlands | 1.37–1.43 | 1.24–1.31 |

- Very large magnitude (Netherlands): about 1.5 electoral and 1.25 legislative parties per extra group. Moderately large (Greece, Spain, Argentina): about 0.6 and 0.5. Single-member districts: 0.11 and 0.07, neither statistically distinguishable from zero (p. 666).
- Conclusion of the evidence section: strong evidence that party-system size depends on the interaction of social and institutional forces as Duverger predicts (p. 666).

### Conclusion (p. 667)
- Party-system size is shaped by the interaction of social heterogeneity and electoral permissiveness. According to Duverger's theory, large multiparty systems occur only with both high heterogeneity and permissive rules (p. 667).
- With high district magnitude, social heterogeneity is translated into electoral and legislative parties with little distortion. Low magnitude produces systems much smaller than the number of cleavages suggests (p. 667).
- The amount of distortion under nonpermissive rules depends on geographic distribution. Evenly spread small-party support gives legislatures with many fewer parties than cleavages. Geographically concentrated support greatly curtails the reductive effect (p. 667).
- The chapter also argued that the *types* of parties arise from social and institutional forces. Cleavages give potential lines of conflict, and institutions affect which are politicized (p. 667). Scholars have made much greater progress on the number of parties than on their ideological or programmatic orientation (p. 667).

### Problems (pp. 668–672; the unit contains no printed solutions)
- **Effective number of parties** (restated, p. 668–669): for $P$ actual parties with vote shares $v_i$ or seat shares $s_i$,
$$\text{effective number of electoral parties} = \frac{1}{\sum_{i=1}^{P} v_i^2},\qquad \text{effective number of legislative parties} = \frac{1}{\sum_{i=1}^{P} s_i^2}.$$
- **Problem 1** (South Africa 2004, Table 14.18, p. 669): 19 parties won votes and 12 won seats, with the ANC at 69.70% of votes and 69.80% of seats. Parts a–d ask for the two effective numbers, a comparison with actual counts, a classification of the system, and whether the mechanical effect suggests a permissive system (pp. 669–670).
- **Problem 2** (India, SMDP, p. 670): nearly 40 parties won seats in 2004, with an effective number of legislative parties of 6.52. Parts a–c ask why there is no two-party system, why district-level numbers stay near two (Fig. 14.12), and why the national number varies, e.g. more nationalized in the 1970s (pp. 670–671).
- **Problem 3** (hypothetical Los Angeles community, Table 14.19, p. 671): language by race percentages (Latino 20 English / 31 Spanish; Asian 17 English / 14 Korean; Black 10 English; White 8 English). Parts a–c ask about cross-cutting vs reinforcing attributes, minimal winning coalitions at a 50% threshold, and who belongs to both coalitions (pp. 671–672).

## Toy example (ours, not from the text)
Aim: show that the same social "demand" gives different party counts under different rules and different geography, using the effective-number formula.

Five SMDP districts of equal size; national vote shares A = 45%, B = 35%, C = 20%.

1. **Electoral parties:** $\sum v_i^2 = 0.45^2+0.35^2+0.20^2 = 0.2025+0.1225+0.04 = 0.365$, so $N_{\text{elec}} = 1/0.365 \approx 2.74$.
2. **Evenly spread support:** in every district A = 45, B = 35, C = 20. A wins all 5 seats. Seat shares 1, 0, 0, so $N_{\text{leg}} = 1/1 = 1$.
3. **Concentrated support for C:** C's shares by district are 60, 10, 10, 10, 10 (average 20). In the other four districts A = 51.25 and B = 38.75. Check: A's average is $(20+4\times 51.25)/5 = 45$ and B's is $(20+4\times 38.75)/5 = 35$. C wins district 1 and A wins districts 2–5. Seat shares are A 0.8, C 0.2, B 0, so $\sum s_i^2 = 0.64+0.04 = 0.68$ and $N_{\text{leg}} = 1/0.68 \approx 1.47$.
4. **PR with 20 seats, shares proportional:** seats 9, 7, 4 give shares 0.45, 0.35, 0.20, so $N_{\text{leg}} = N_{\text{elec}} \approx 2.74$.

Reading: identical votes yield 1, 1.47 or 2.74 legislative parties depending on the rule and the geography. This is the mechanical effect only. Strategic voting and entry would additionally lower C's vote share under SMDP, but this toy does not model them.

## Concepts
- [[duverger-theory]] (new) — party-system size results from social demand filtered by electoral rules (p. 653).
- [[duverger-law]] (new) — SMDP systems encourage two-party systems (p. 653).
- [[duverger-hypothesis]] (new) — PR rules favour multiparty systems (p. 653).
- [[cross-cutting-cleavages]] (new) — attributes uncorrelated, so many distinct identity categories. Reinforcing attributes are correlated and merge categories (pp. 642–643).
- [[latent-vs-politicized-cleavage]] (new) — latent cleavages exist in society; electoral institutions filter which become politicized (p. 641, Fig. 14.1).
- [[mechanical-effect]] (new) — how votes translate into seats. In disproportional systems it penalises small parties and rewards large ones (p. 644).
- [[strategic-effect]] (new) — effect of the vote-seat translation on strategic behaviour of voters and elites (p. 648).
- [[strategic-voting]] — voting for the most preferred candidate with a realistic chance of winning, i.e. the canon's "strategic (sophisticated) voting" (pp. 648–649).
- [[strategic-entry]] (new) — elites' choice of party label: most preferred, or most preferred with a realistic chance (p. 649).
- [[electoral-permissiveness]] (new) — how far a system lets social demands become parties. PR is permissive, SMDP nonpermissive, with high district magnitude more permissive (pp. 658, 667).
- [[district-magnitude]] (new) — number of legislators elected per district. It is Duverger's most important dimension of electoral systems (p. 665).
- [[party-system-nationalization]] (new) — local and national party systems are of similar size (p. 655).
- [[effective-number-of-parties]] (new) — $1/\sum v_i^2$ (or seats), counting parties weighted by size (pp. 668–669).
- [[electoral-vs-legislative-parties]] (new) — parties that win votes vs parties that win seats (p. 653).
- [[ethnic-head-count]] (new) — Chandra's term for ethnic groups checking whether co-ethnics are numerous enough to win a constituency under SMDP (p. 662).
- [[observable-implications]] — Duverger's law and hypothesis are called "observational implications" of his theory (p. 653).

## Canonical instances
- [[latent-identity-countries-A-B]] — hypothetical countries showing how cross-cutting vs reinforcing cleavages change the number of latent groups (pp. 642–643).
- [[duvergerland]] — 20% Green vote yields 0 seats under SMDP but 20 under PR (pp. 644–646).
- [[uk-1992-election]] — St. Ives and national totals: large-party bonus, LD penalty, regional parties unpenalised (pp. 645–648).
- [[strategic-entry-game]] — two left parties, one right party; two pure-strategy Nash equilibria (p. 651).
- [[france-2002-presidential]] — split left vote puts Le Pen ahead of Jospin (p. 652).
- [[us-2000-nader]] — Nader splits left vote; Bush defeats Gore (p. 652).
- [[us-party-nationalization]] — district vs national effective number of parties, 1790–1990 (p. 656).
- [[kshatriya-gujarat]] — redefining ethnic boundaries to win under SMDP (p. 663).
- [[liberal-democrats-merger]] — Liberal and Social Democratic parties merge in 1988 (p. 652).

## Bridges (candidates)
- [same-math] effective number of parties $1/\sum v_i^2$ ↔ economics/industrial organisation: inverse of the Herfindahl concentration index — same formula, applied to market shares (our proposal; not stated in this unit).
- [structural-analogy] Strategic Entry Game (asymmetric coordination, two pure equilibria) ↔ game theory: anti-coordination games such as "chicken" — each prefers the other to yield; the text calls it an asymmetric coordination game (p. 651).
- [structural-analogy] Table 14.15 / 14.16 (effect of one factor depends on the other) ↔ statistics: interaction effects in regression — the unit's slope-by-group evidence has this structure, though it only reports separate slopes.
- [structural-analogy] strategic voting / wasted-vote logic ↔ the canon's strategic (sophisticated) voting and the paradox of voting — both turn on how likely a vote is to matter.
- [metaphor] engine and brake / open and closed dam ↔ filtering models of institutions as moderators, not causes, of social demands (pp. 657–658).

## Questions this raises
- Table 14.16 shows 1.68 legislative parties for high heterogeneity with SMD but 2.52 for low heterogeneity with SMD. The text says only "few parties" for both. Is there a reason why more diversity gives fewer parties there?
- If a system's cleavages are national but its electoral rule is permissive, what gives more parties — the cleavages or the rule? How would one separate them with data?
- Strategic entry presupposes elites who can estimate which parties are viable. How might this change when polls are poor or voters are loyal to a party?
- The authors say we know less about *which* parties form than about *how many*. What would a theory of party types need, beyond cleavages and electoral rules (p. 667)?

## Exercises worth doing
- Ex. 1a–d (pp. 668–670) — compute effective numbers for South Africa 2004 and judge actual vs effective counts and the mechanical distortion — difficulty: easy
- Ex. 1b–c (p. 670) — decide which measure better captures party-system size and classify the system — difficulty: medium
- Ex. 2a–c (p. 670) — explain India's district-vs-national gap with the mechanical and strategic effects and nationalization — difficulty: medium
- Ex. 3a (p. 672) — judge cross-cutting vs reinforcing attributes using Table 14.19 — difficulty: easy
- Ex. 3b–c (p. 672) — find minimal winning coalitions and the individuals who belong to both — difficulty: hard

## Reading notes
- **Part boundaries:** this unit (printed pp. 641–672) starts mid-section, with Fig. 14.1 and a sentence ending the discussion of politicized cleavages (earlier parts of Chapter 14 are not covered here). It ends with Problems 1–3 on p. 672. The Key Concepts list on p. 668 references pages across the whole chapter and is not digested.
- **Page offset:** printed = pdf − 37.
- **Edition:** the source notes state the PDF is the 2nd edition (CQ Press, 2013), although the work id suggests a 2017 3rd edition. No copyright line is visible in these pages.
- **Images:** page images were supplied for only some pages; the others (e.g. printed pp. 644, 648, 650) were read from the text layer. Equations and Fig. 14.5 were checked against the images (pp. 651, 669). The text-layer running heads on pp. 669–672 are garbled and reproduce stray head text.
- **Misprints found:** (1) p. 649 refers to the St. Ives results as "Table 14.12"; the St. Ives table is 14.13. (2) p. 651 prints "0 > λ > 1"; the page image shows the same, but the logic (λ between the worst and best payoffs) requires $0<\lambda<1$. (3) Not a misprint: the p. 642 sentence on Catholics in country A mentions only two subgroups (half of the rich Europeans and half of the poor indigenous people). This is consistent with Table 14.11 (all cells 12.5) but does not describe the whole table, so I used the table.
- **Table 14.17 labels:** the column headings say "Strategic effect: Electoral parties" and "Mechanical effect: Legislative parties." The text describes these as the effect of one extra ethnic group on electoral and legislative parties, so I report the column contents that way.
- **Percentages:** in Table 14.18 the votes and seats columns sum slightly above 100 (probably rounding); I did not correct them.
- **Wording:** The claim that the two UK big parties won about a fifth more seats than their vote shares suggest (p. 646) is the author's phrase. Table 14.14 shows Conservatives +9.7 and Labour +6.7 percentage points.
