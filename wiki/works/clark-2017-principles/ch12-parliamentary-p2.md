---
id: clark-2017-principles/ch12-parliamentary-p2
work: clark-2017-principles
unit: "12 Parliamentary, Presidential, and Semi-Presidential Democracies: Making and Breaking Governments (part 2/3)"
pages: 483–505
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Minority and surplus-majority governments, government duration, and presidential cabinets

## L0 — One line
Because politicians care about policy and not only office, "too small" and "too large" cabinets are common and understandable, and presidential cabinets tend to differ from parliamentary ones because presidents need no legislative majority to stay in office.

## L1 — The gist (≤ 120 words)
Why do parliamentary democracies so often produce minority cabinets (too small) and surplus-majority cabinets (too large)? The authors review theories that stress policy, test four minority-government hypotheses on West European data, and find support for opposition strength, corporatism and the absence of an investiture vote, but not for "strong party". They then cover government formation time, government duration, and why governments end. The unit closes with presidential systems. There, the president is always formateur and no legislative responsibility exists. So presidential systems tend to have more minority cabinets, fewer coalitions, more nonpartisan ministers and less proportional cabinets.

**Prerequisites:** what a cabinet, formateur, minimal winning coalition, caretaker government and vote of no confidence are; how to read a regression table (coefficient, standard error, stars).

## L2 — Key ideas
- If politicians cared only about office, minority and surplus-majority governments would be puzzling. Their frequent occurrence signals that policy matters (pp. 483, 488).
- Minority governments are more likely where the opposition can shape policy (strong committees; corporatism) and less likely where an investiture vote is required. "Strong party" gets no compelling empirical support (pp. 484–488).
- Surplus-majority governments have several explanations: national unity, supermajority rules, protection against blackmail by a small party, weak party discipline, policy-sequencing, and preelectoral pledges (pp. 489–490).
- Preelectoral coalitions can change who wins and give voters a clearer link to the government (pp. 490–492).
- Formation takes 29.9 days on average but varies widely. Delays have real consequences, including effects on markets (pp. 492–494).
- Cabinet duration varies by cabinet type and country. Governments end for technical or discretionary reasons (pp. 494–495). Early elections may be explained by signaling (pp. 497–498).
- Cabinet instability does not automatically imply ministerial instability, and cabinet duration is not the same as ministers' experience (pp. 498–499).
- In presidential systems the president is always formateur and the reversion point is the president's party ruling alone. Presidential democracies therefore tend to have more minority cabinets and fewer coalitions, and their cabinets tend to be less partisan and less proportional (pp. 500–505).

## L3 — Walkthrough

*Part begins mid-sentence in the subsection on minority governments (p. 483) and ends mid-sentence in the presidential-cabinet composition discussion (p. 505).*

### Minority governments in parliamentary democracies (pp. 483–488)

**Support parties and ad hoc majorities.** The Dutch example: the extreme-right PVV publicly agreed to support a minority VVD–CDA coalition (p. 483). Elsewhere governments build majorities ad hoc, bill by bill. It is then unclear who keeps the government in power, so voters find it hard to assign responsibility (p. 483).

**Frequency.** Strøm (1990) challenged the older view that minority governments are undemocratic and short-lived (p. 483).
- 38.7% of governments in West European parliamentary democracies in 1945–1998 were minority governments (p. 483).
- Minority governments were the norm in Denmark (82%), Sweden (81%) and Norway (65%) (p. 483).
- They held office for 30.6% of the postwar period and lasted 539 days on average (p. 483).

**Why they exist.** Pure office-seekers would not stay out of a cabinet they could force their way into. The theories therefore all rely on policy (p. 483).

**Strøm's argument.** Where committees spread policy influence to opposition parties, opposition parties have less incentive to join the cabinet (pp. 483–484).
- *Opposition strength hypothesis:* minority governments are more likely when opposition influence is strong (p. 484).
- Reasons to prefer opposition to cabinet, mostly about future elections (p. 484):
  - Governing parties are blamed for failures. Powell (2000) finds incumbents lose about 2% of their vote on average (20 democracies, 25 years).
  - A party may have pledged not to govern with certain parties.
  - Opposition parties have more flexible campaign strategies because they have no record in office.
- Footnote 12: committees are influential in Belgium, Denmark, Germany, the Netherlands, Norway and Sweden, with chairs allocated proportionally. They are weak in France, Greece and the UK (p. 484).

**Luebbert's argument.** Opposition influence depends on interest-group relations (p. 485).
- *Pluralist:* groups compete outside formal policymaking.
- *Corporatist:* key social and economic actors have a formal role in making policy, via national, specialized, hierarchical, monopolistic peak organizations. Norwegian and Swedish ministries must consult affected groups.
- Corporatism "allows, indeed guarantees, access to policymaking by a variety of groups" (Luebbert 1984, p. 235; this book p. 485). Opposition parties then have less incentive to enter the cabinet.
- *Corporatist hypothesis:* minority governments are more likely in corporatist countries (p. 485).

**Investiture.** Strøm argues a formal investiture vote raises the hurdle, because the opposition must support a minority government openly. Bergman (1993) calls such rules "positive": the government must show it is supported. Under "negative" rules the parliament must show the government is not tolerated (p. 485).
- *Investiture hypothesis:* minority governments are less likely with a formal investiture vote (p. 485).

**Strong party.** A minority government can survive if the opposition cannot agree on a replacement (pp. 485–486).
- Examples given: Congress Party in India, the Swedish Social Democrats, the Italian Christian Democrats. The latter two were large, centrally placed parties with opponents on both sides.
- Laver and Shepsle (1996) hypothesize: minority governments are more likely when there is a "strong" party (p. 486).

**Test (Table 12.7).** Probit models (for a yes/no outcome) of whether a minority government formed (p. 486).
- Sample: all governments in eleven West European parliamentary democracies, 1945–1998. Nonpartisan governments and cases with a majority party are omitted (p. 486).
- Variables (p. 486):
  - Opposition strength: 1–9, from a country-expert survey (Laver and Hunt 1992).
  - Corporatism: 0–5, high when there are few unions but high unionization (Garrett 1998).
  - Investiture: whether a formal vote exists.
  - Strong party: indicator from Martin and Stevenson (2001).

Coefficients (standard errors) (p. 487):

| | M1 | M2 | M3 | M4 | M5 |
|---|---|---|---|---|---|
| Opposition strength | 0.31*** (0.06) | | | | 0.34*** (0.10) |
| Corporatism | | 0.78*** (0.25) | | | 0.93*** (0.34) |
| Investiture vote | | | −0.89*** (0.18) | | −1.08*** (0.36) |
| Strong party | | | | −0.54** (0.22) | −0.23 (0.33) |
| Observations | 219 | 101 | 219 | 142 | 81 |

- Reading the table: a positive coefficient means the variable makes a minority government more likely, and a negative one less likely. A smaller standard error relative to the coefficient means more confidence. The table note reads *, **, *** as greater than 90, 95, 99 percent significant (p. 487).
- Results (p. 488):
  - Opposition strength and corporatism: always positive and significant.
  - Investiture: always negative and significant.
  - Strong party: always negative, which is the opposite of the Laver–Shepsle prediction. The authors say "if anything" strong parties reduce the likelihood of minority governments, and there is "no systematic evidence, as yet" for the hypothesis.
- Conclusion: minority governments are more likely where (a) the opposition can strongly influence policy, (b) interest-group relations are corporatist, and (c) there is no formal investiture vote requirement (p. 488).

*Intuition note:* A party outside the cabinet can often achieve some of its policy aims while being blamed less when things go wrong, so staying out can make sense for future elections even though opposition influence is never stronger than the government's. Where the opposition has real influence, the incentive to join is lower and minority cabinets are more likely. Requiring a public vote makes tacit toleration harder.

### Surplus majority governments (pp. 488–490)

- *Definition:* the cabinet has more parties than needed for a legislative majority, so it could drop a party and keep its majority (p. 488).
- Frequency: 18.8% of West European governments in 1945–1998, almost half in Italy (46%) and the Netherlands (45%) (p. 488). They held office 13.9% of the postwar period and lasted 505 days on average (p. 488).
- Pure office-seekers would not give up office they do not need to, so their existence signals that policy matters (p. 488).

**Explanations**
1. *National unity governments* form in crises (e.g. after WWII in Belgium, Germany, Italy, Luxembourg and the Netherlands, in post-1989 Eastern Europe, and in Iraq after 2006). The aim is to include the whole ideological spectrum. They are often popular but tend to be short-lived, because parties not needed for a majority are pushed into opposition by the desire for office and influence (p. 489).
2. *Supermajority needs.* Constitutional amendments may need more than a majority. The authors say one might call such a cabinet "oversized" in name only: in practice it is no different from a minimal winning coalition, given its policy objectives. Belgian laws on language-group relations need two-thirds of legislators and a majority of each language group (p. 489).
3. *Blackmail.* In a minimal winning coalition any party can topple the government by resigning, so a small party can extract concessions out of proportion to its size (Luebbert 1984). Larger parties may add partners to avoid this (p. 489).
4. *Weak party discipline.* A party unsure of its own legislators' votes may share office for the support it needs (pp. 489–490).
5. *Policy sequencing* (Carrubba and Volden 2000). Once a party has obtained the policies it wants, it may defect if it dislikes the remaining ones. A surplus partner means one defection does not stop the remaining policies (p. 490).
6. *Preelectoral pledges.* Parties that announced a coalition before the election may keep it even if one partner is unnecessary (p. 490).

*Intuition note:* A "spare" party acts like insurance. In a surplus-majority cabinet one party's resignation does not automatically bring the government down, and one defector cannot stop the remaining policies from being implemented.

### Box 12.3: Preelectoral coalitions (pp. 490–492)

- A preelectoral coalition is a set of parties that do not compete independently at election time. A government coalition forms after the election (p. 490).
- Political scientists have mostly studied post-election coalitions. S. Golder (2006), covering 23 democracies, shows that preelectoral coalitions are common and affect election outcomes and government formation (p. 490).
- Forming one requires bargaining over a joint strategy, who steps down in which district, and who becomes prime minister. The main motive is electoral advantage, especially under disproportional systems that punish small parties (pp. 490–491).
- *Simple example (authors').* Two blocs in single-member districts, the left with more support. If the right forms a coalition with common candidates and the left runs divided, the left most likely loses. A majority of voters then get a government they did not choose (p. 491).
- *French presidential election 2002.* The left vote split among many candidates, and Socialist PM Jospin came third behind Le Pen. Chirac easily won the runoff. The authors say the "earthquake" owed as much to the left's lack of a preelectoral coalition as to the extreme right's strength. Polls suggested Jospin may well have beaten Chirac head to head (p. 491).
- *Normative implications.* Under proportional rules, elections often serve "primarily as devices for electing representative agents in postelection bargaining" (Huber 1996, p. 492). Preelectoral coalitions can help voters identify and support government alternatives (Powell 2000), and arguably give coalitions as much of a mandate as single parties (p. 492).

### Duration of governments: formation and survival (pp. 492–499)

**Formation time (Table 12.8).** Days from election to inauguration, 1945–1998 (pp. 492–493).
- Average over all 156 cases: 29.9 days. By country: Norway 2.5, Sweden 5.7, Greece 7.5, UK 8.7, Denmark 9.4, Spain 28.6, Luxembourg 31.2, Germany 36.4, Italy 47.3, Belgium 59.7, Netherlands 85.7.
- Maximum: Netherlands 208 days. Belgium after June 2010 took until December 2011, over 500 days (p. 493).
- A single majority party means the cabinet is obvious, hence the UK's 8.7 days. Many parties mean longer bargaining over combinations, portfolios and policy (p. 492).
- Footnote 15: holidays can lengthen formation (p. 492).

**Costs of delay.** Caretaker governments do not generally make major policy initiatives (p. 493). Uncertainty about policy affects actors' behavior. In the Czech Republic, seven months followed the June 2006 election. The *Prague Post* reported stalled reforms and a cost to taxpayers of up to 3 million Kč a day (p. 494). Studies find effects on exchange rates (Leblang 2002), stock volatility (Leblang and Mukherjee 2006) and asset choices (Bernhard and Leblang 2006) (p. 494).

**Survival.**
- Fewer than a quarter of governments served their maximum permitted term. On average they lasted 60% of their permitted time, from 84% in the Netherlands to 33% in Italy (p. 494).
- By type (Figure 12.7): single-party majority 910 days, minimal winning coalition 893 days, both considerably longer (about a year in all) than minority or surplus-majority cabinets (p. 494).
- By country (Figure 12.8): longest in Luxembourg (1,170 days), UK (981) and Spain (957). Shortest in Italy (354) and Belgium (520) (p. 494).

**Why governments end (Table 12.9).**
- *Technical* reasons are beyond the government's control (death or illness of the PM, a constitutionally mandated election). *Discretionary* reasons are political acts (early election, no-confidence defeat, coalition conflict). Of 255 endings, 39% were technical and 61% discretionary (pp. 494–495).
- Counts (categories are not mutually exclusive): technical: mandated election 73, other constitutional reason 21, death of PM 6. Discretionary: early election 64, enlargement of government 13, parliamentary defeat 31, intercoalition conflict over policy 53, intercoalition conflict not over policy 16, intraparty conflict 39 (p. 496).
- A quarter of cabinets ended through early elections called by the government. Only 31 ended in parliamentary defeat, but governments often resign to avoid defeat, so this number should not be over-read (p. 495).

**Box 12.4: Endogenous election timing** (when the government chooses the election date within a window, as in the UK). All three stories assume that politicians want to win and that voters hold governments accountable for the economy (p. 497).
1. *Political surfing:* the government waits for an economic high, without manipulating it (Kayser 2005).
2. *Political business cycle:* the government engineers a short-term high, then calls an election, and decline follows (Clark 2003).
3. *Signaling:* the government knows more about future performance and calls elections before an expected decline. The early call itself signals bad times, so governments may hold back unless voters are naive or the opposition is unprepared (A. Smith 2003).

| Prediction | Surfing | Business cycle | Signaling |
|---|---|---|---|
| Elections called when economy is good | yes | yes | no (current conditions should not matter) |
| Decline follows an early call | no prediction | yes | yes |
| Government poll support falls after early call | silent | silent | yes |
| Earlier call means bigger coming decline | silent | silent | yes |

All as stated on p. 497. Smith (2004), using UK data, finds strongest support for signaling (p. 498). Findings: when elections are called early relative to expectations, government support, post-election outcomes and stock indexes decline and campaigns are short. Especially early elections are followed by particularly bad economic performance. Current economic performance had little evidence of affecting early calls (p. 498).

**Does duration matter?** Cabinet instability does not automatically mean ministerial instability (pp. 498–499).
- Allum (1973) found that a set of Italian politicians held office almost continuously for over 20 years.
- Huber and Martinez-Gallardo (2004), 19 democracies, 1945–1999, measured duration, portfolio experience (average days in the specific portfolio held) and political experience (average days in any significant portfolio) (p. 498).
- Per the text, cabinets in the UK, Canada and the Netherlands last long but have low experience because of frequent reshuffles. Those in Germany, Sweden and Belgium are short-lived but have relatively high experience, because the same people return, often to their former ministries (p. 498).
- Huber and Martinez-Gallardo's analysis suggests, in the authors' words, that we should perhaps be less concerned about what affects duration and more interested in what influences experience; political scientists are only now beginning to look at this (Dowding and Dumont 2009) (p. 499).

*Intuition note:* How long a cabinet lasts and how experienced its ministers are are two different things. Changing governments can keep the same people, and stable governments can reshuffle them often.

### Making and breaking governments: presidential democracies (pp. 499–505)

Less is known than for parliamentary systems, partly for lack of data, but new data are enabling research (p. 499).

**Formation process (p. 500)**
- The government is the president plus the cabinet. The president is political chief executive and head of state (p. 500).
- Four differences from parliamentary systems (p. 500):
  1. No legislative responsibility, so governments need no majority legislative support to stay in office.
  2. The president is always formateur, so there is no uncertainty about who forms the government. The president appoints and dismisses ministers at will (footnote 17: US Senate consent rarely prevents the president getting his own cabinet).
  3. The president's party must be in every cabinet, whatever its size, though other parties may join too.
  4. The reversion point (what happens if a minority formateur fails to get support) differs. In parliamentary systems it is an early election, a new bargaining round, or a caretaker government. In presidential systems, if a minority president fails to win the support of opposition parties, the president's party simply rules alone; elections occur at fixed intervals and the president cannot dissolve the legislature at will.
- Legislators of government parties can often vote against cabinet bills without fear of causing new elections. A *portfolio coalition* (legislators of cabinet parties) therefore does not imply a *legislative coalition* (a voting bloc supporting a bill) to the degree it does in parliamentary systems (p. 500).

**Size of cabinets (pp. 501–504)**
- Presidents form majority cabinets whenever their party holds a majority. Otherwise they are free to form minority cabinets, either with implicit legislative majority support (as in parliamentary systems) or without it, which parliamentary systems rule out. So, all things being equal, minority governments should be more frequent in presidential systems (p. 501).
- Evidence (p. 501):
  - About a third of parliamentary governments are minority governments (Strøm 1990).
  - Amorim Neto (2006): 46% (49) of Latin American presidential governments (late 1970s–2000) were minority governments.
  - Cheibub et al. (2004), in minority situations 1946–1999: 65% led to minority governments in presidential democracies versus 35% in parliamentary ones.
- Table 12.10 (13 countries, 106 governments): single-party majority 11, majority coalition 46, single-party minority 18, minority coalition 31 (p. 502). Ecuador has 15 minority coalitions out of 20 governments (p. 502).
- **Linz's prediction (1994):** coalitions in presidential democracies will be "exceptional" (p. 501). The authors disagree if actors care about policy. The incentive to form coalitions depends on the president's legislative powers (p. 501).
  - A decree is a presidential order with the force of law, and its scope varies. US executive orders only allow the president to regulate and interpret existing statutes and to give orders to the public administration; the president cannot enact new laws. Elsewhere presidents may issue "decree-laws" even against a hostile legislature (p. 502).
  - Presidents with weak decree power and no majority party need others' support, so they have an incentive to form coalitions (p. 502).
  - Evidence: 73% (77) of governments in Table 12.10 were coalitions (p. 503).
- **Cheibub and Limongi's view (2002):** "it is not true that incentives for coalition formation are any different in presidential than in parliamentary democracies." The authors call this conclusion "probably premature" (p. 503). Their reasons (p. 503):
  - The reversion point gives the president the last word over policy (Samuels 2007). He need not concede ministries as a prime minister may.
  - Policy promises to partners are less credible, since the president can dismiss them without losing office. Presidential preelectoral agreements are also less binding (Kellam 2011).
  - Benefits of joining are therefore lower for opposition parties, but costs are also lower, since coalition legislators can vote against bills without toppling the government.
  - Hence presidents may not always find willing partners, and partners are likely to be less reliable.
- Two implications. First, coalitions should be less common than in parliamentary systems. Cheibub et al. (2004), for minority situations 1946–1999, find coalitions formed 78% of the time in parliamentary versus 54% in presidential democracies (p. 503). Second, presidential coalitions may be less stable, or last as long but govern less effectively, because a portfolio coalition can outlive its legislative coalition. The authors say these two have not, to their knowledge, been tested (pp. 503–504).

**Composition of cabinets (pp. 504–505)**
- Presidents appoint more nonpartisan ministers (people not from the legislature, such as technocrats, cronies or interest-group representatives) and allocate portfolios less proportionally (Amorim Neto and Samuels 2006) (p. 504).
- Table 12.11 (30 parliamentary, 13 presidential democracies, 1980–2000): nonpartisan ministers 2.12% versus 29.17%. Proportionality (0–1, 1 = perfect) 0.90 versus 0.65 (p. 504).
- Why: prime ministers need a legislative majority, so they appoint partisan ministers and allocate seats in proportion to what each party contributes (Gamson's law). Presidents need not negotiate with parties to the same extent, so they can vary partisanship and proportionality (p. 504).
- Table 12.12 shows wide variation across presidential countries. Examples: Ecuador 65.3% nonpartisan with proportionality 0.27; Costa Rica 1.8% with 0.98; US 0% with 0.91; Brazil 46.9% with 0.50 (p. 505).
- Presidential cabinets are likely to look more parliamentary (more partisan ministers, more proportional) when the president has weak decree power, a small legislative party and low party discipline, because he must win opposition support (p. 505).

*Intuition note:* A prime minister must buy support with cabinet seats. A president can, at least in part, govern without it, so presidents have more freedom over who sits in the cabinet.

## Toy example (ours, not from the text)
*Blackmail and the surplus partner.* A 100-seat legislature needs 51 seats for a majority. Party A has 46 seats, B has 6, C has 10.
- Minimal winning coalition A+B: 46 + 6 = 52 ≥ 51. If B resigns, 52 − 6 = 46 < 51, so the government falls. B is pivotal and could demand concessions out of proportion to its 6 seats.
- Surplus coalition A+B+C: 46 + 6 + 10 = 62.
  - If B resigns: 62 − 6 = 56 ≥ 51, still a majority.
  - If C resigns: 62 − 10 = 52 ≥ 51, still a majority.
- Neither small party can now topple the government alone, so blackmail threats lose force (p. 489 logic). A is still pivotal (62 − 46 = 16 < 51), but it is the large coalition leader.

## Concepts
- [[minority-government]] (new) — cabinet whose parties lack a legislative majority. It can rule with support parties or ad hoc majorities (pp. 483–484).
- [[surplus-majority-government]] (new) — cabinet containing more parties than needed for a majority (p. 488).
- [[opposition-strength]] (new) — opposition's influence over policy, e.g. via committees. Linked by Strøm to more minority governments (p. 484).
- [[corporatism]] (new) — key social and economic actors have a formal role in making policy (p. 485).
- [[investiture-vote]] (new) — formal vote to approve a new government. Bergman's "positive" rule (p. 485).
- [[strong-party]] (new) — large, centrally located party whose opponents cannot agree on a replacement (p. 486).
- [[preelectoral-coalition]] (new) — parties that do not compete independently at election time (p. 490).
- [[endogenous-election-timing]] (new) — government chooses election date. Three stories: surfing, political business cycle, signaling (p. 497).
- [[technical-vs-discretionary-termination]] (new) — government ends by events beyond its control versus political acts (p. 494).
- [[cabinet-duration-vs-ministerial-experience]] (new) — cabinet survival and ministers' portfolio or political experience are distinct (p. 498).
- [[formateur-and-reversion-point]] (new) — the actor who forms the government, and the outcome if formation fails. In presidential systems the president is always formateur, and failure leaves his party ruling alone (p. 500).
- [[portfolio-vs-legislative-coalition]] (new) — cabinet-party legislators versus voting bloc backing a bill (p. 500).
- [[presidential-decree]] (new) — presidential order with the force of law, whose scope varies by country (p. 502).
- [[nonpartisan-minister]] (new) — cabinet member not from the legislature (p. 504).

## Canonical instances
- [[dutch-pvv-support]] — support party sustaining a minority VVD–CDA coalition (p. 483).
- [[nordic-minority-governments]] — Denmark 82%, Sweden 81%, Norway 65% minority (p. 483).
- [[belgian-language-supermajority]] — two-thirds rule produces surplus majorities (p. 489).
- [[france-2002-split-left]] — Jospin finishes third in first round after the left splits (p. 491).
- [[belgium-2010-formation-delay]] — over 500 days to form a government (p. 493).
- [[czech-2006-formation-delay]] — seven months under a caretaker government (p. 494).
- [[smith-uk-election-timing]] — UK evidence favoring the signaling story (p. 498).
- [[latin-american-presidential-cabinets]] — Tables 12.10 and 12.12 (pp. 502, 505).

## Bridges (candidates)
- [structural-analogy] Pivotal small party in a minimal winning coalition ↔ veto player: a single actor whose agreement is needed holds leverage — the text does not use the term (p. 489).
- [structural-analogy] Presidential partners' unreliable promises (president can dismiss them freely) ↔ commitment problem: promises not credible when the promiser keeps the exit option (p. 503).
- [structural-analogy] Early-election call as signal ↔ signaling games: the act itself reveals the informed party's private information (p. 497).
- [metaphor] Voters facing postelection coalition bargaining ↔ principal–agent problem: voters pick agents without knowing the eventual policy (p. 492).

## Questions this raises
- How could the authors' two untested hypotheses be tested, i.e. whether presidential coalitions are less stable, or less effective (p. 504)?
- What explains variation in ministers' political and portfolio experience across countries (p. 499)?
- Is a government with a preelectoral coalition really more "mandated" than one built after the election (p. 492)?
- Why might strong parties not produce minority governments, despite the plausible logic (p. 488)?

## Reading notes
- Printed page = pdf − 37 (pdf 520 = p. 483). This part runs from p. 483 (mid-sentence) to p. 505 (mid-sentence: "Cabinets tend to be…").
- Source is the 2nd edition (CQ Press, 2013), not the 3rd edition of the citation. Running header: "Principles of Comparative Politics".
- The text describes the Table 12.7 stars as confidence levels, while the table note calls them "significant"; both wordings are reported as printed.
- The parenthetical "(about a year in all)" (p. 494) is unclear next to the 910 and 893 days quoted just before; I kept the author's wording and reported the numbers.
- In Figure 12.9, the Netherlands, Canada and UK political-experience bars are above their duration bars. The text's "low experience" seems to be meant relative to Germany, Sweden and Belgium.
- The Cheibub et al. percentages (p. 501: 65% versus 35% minority governments; p. 503: 54% versus 78% coalitions) compare presidential with parliamentary democracies; the text gives no underlying counts.
- Presidential nonpartisan averages differ slightly between Table 12.11 (29.17; 0.65) and Table 12.12 (29.2; 0.64), which cite different sources and periods (1980–2000 versus late 1970s–2000); the text does not explain the difference.
- Figure 12.7 has no printed values; only the values quoted in the text are used.
