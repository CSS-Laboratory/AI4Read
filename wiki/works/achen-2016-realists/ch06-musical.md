---
id: achen-2016-realists/ch06-musical
work: achen-2016-realists
unit: "Chapter 6 — Musical Chairs: Economic Voting and the Specious Present"
pages: 146-176
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Musical Chairs: Economic Voting and the Specious Present

## L0 — One line
US presidential voters respond almost only to income growth in the last six months before the election, which gives little sign of competence-based selection, gives politicians a reason to manipulate election-year income, and makes the most important single factor in who wins essentially arbitrary from the standpoint of accountability.

## L1 — The gist (≤ 120 words)
Economic voting is usually read as evidence that voters hold incumbents accountable. The authors ask whether the time horizon of US presidential voters fits that reading. For the 1952–2012 elections, income growth in the last two quarters before Election Day predicts the incumbent party's vote margin far better than growth over the whole term, which voters seem to ignore. Quarterly growth is volatile and barely persistent, so short windows say little about competence. The authors find little trace of voters selecting competent managers. Short horizons also give incumbents a reason to manipulate election-year income. The authors conclude that the key factor in who wins is, for accountability, essentially arbitrary.

**Prerequisites:** OLS regression (coefficients, standard errors, adjusted R²); natural logs as percentage changes; correlation and lagged (autoregressive) relationships; the retrospective-voting idea from chapter 4.

## L2 — Key ideas
- On the authors' argument, retrospective voters seeking accountability should judge the whole term. Most studies of economic voting focus on the election year or less (pp. 148–149).
- Presidential vote margin is explained far better by growth in Q14–Q15 plus incumbent-party tenure (adjusted R² .81) than by growth in Q3–Q15 (.54). Earlier growth seems to add little or nothing (pp. 152–153).
- Hibbs's geometric-lag weighting adds little or nothing once short-term growth is included. Years 1 and 2 of a term look politically irrelevant (pp. 157–158).
- Quarterly income growth is volatile and almost uncorrelated across quarters. Six-month windows are therefore nearly useless for inferring competence, with selection only 8–9% better than chance (pp. 159–164).
- In these 16 cases post-election growth was lower under reelected incumbents, and it shows no positive link to their vote margin. The authors treat selection as speculation, not fact, while noting weak tests (pp. 165–168).
- Under the sanctioning rationale, voters should reward average growth over the term. Myopic voting instead rewards election-year growth and invites political business cycles (pp. 169–171).
- Election-year income growth is about a point higher than in other years. Incumbents running for reelection appear to gain about 1.5 vote-margin points from timing (pp. 172–173).
- Conclusion: myopic retrospection, like "duration neglect", makes the most important single factor in who wins essentially arbitrary for accountability. When races are in doubt, voters "usually, in effect" toss a coin (pp. 175–176).

## L3 — Walkthrough

### Introduction (pp. 146–147)
- Economic voting is the main application of the retrospective theory of democracy, in which voters judge incumbents by past results. The scholarly literature finds a real, substantial effect of economic conditions on elections. It is often read as a mark of voter rationality, though Tufte (1978) stresses myopic voters who can be fooled by pre-election stimulus (pp. 146–147).
- The authors ask whether this is "rational". Hard times may not be the president's fault, as with "killing the pharaoh when the Nile fails to flood" (p. 147). **Kohut (quoted):** ordinary people do not know what a president can do about the economy and hold him responsible anyway (p. 147).
- Deeper problem: voters may be biased even about national economic conditions. Economic voting may then be "little more than a high-stakes game of musical chairs" (p. 147). In musical chairs, the child who happens to be near a seat when the music stops wins (fn. 1, p. 147).

### The Specious Present (pp. 148–158)
**The time-horizon puzzle (pp. 148–149).**
- **Uchitelle (2004):** the incumbent is likely re-elected if the economy flourishes "when the music stops". The authors ask: "Is that really how we pick our presidents?" (rhetorical question, following their remark that Uchitelle's account has a "disturbingly arbitrary air") (p. 148).
- **Hibbs (2006):** voters rewarding real income performance should assess "the incumbent's entire term of office, with little or no backward time discounting" (p. 148). Yet "virtually all analyses" use election-year economic conditions or a fraction of that year (p. 148).
- **Kramer (1971):** the relevant variable is actual performance minus the performance voters expected. He assumed expectations for year $t$ rest on year $t-1$. He then tested only election-year income growth (p. 148).
- Others use only Q1–Q2 (Lewis-Beck and Tien 2001) or only Q2 (Campbell 2001) of the election year. Still others weight the whole term with recent performance heavier (Hibbs 1982; Erikson 1989; Bartels and Zaller 2001) (pp. 148–149).
- **Author's argument:** if voters forecast rationally and incumbent competence is constant, the best forecast is average past performance. All periods the incumbent is responsible for are then weighted equally (p. 149). Some evidence suggests this matches voters' own intentions (Healy and Lenz 2014) (p. 149).
- The authors suspect analysts gave up on equal weights "because it doesn't work". Hibbs (2006) is the exception, implying "modest (if any) discounting". The consensus is that recent performance matters much more (p. 149).

**Data and design (pp. 149–152).**
- Data: quarterly real disposable personal income per capita (RDI) from the BEA, 1947Q1–2013Q2. Real income beats GDP in explaining elections (Achen and Bartels 2004; Bartels 2008) (pp. 149–150).
- Quarter growth rate (fn. 4, p. 150):
$$\Delta RDI_t = 100\,[\ln(RDI_t) - \ln(RDI_{t-1})]$$
Logs make gains and losses comparable. For small changes, log differences approximate fractional changes. Cumulative growth over a period is the sum of quarterly rates (fn. 5, p. 150):
$$\Delta RDI{:}Q1\text{–}Q16 = \sum_{t=Q1,\dots,Q16}\Delta RDI_t$$
- Quarters are indexed by the election cycle. Q1 is the inauguration quarter and Q16 is the last quarter of the election year (p. 150).
- Two reasons the whole term may not, and should not, count. First, Q16 is only one-third complete by the election. Second, early months reflect the predecessor's policies (p. 150).
- "Grace period": responsibility runs from five months after inauguration (Q3) to five months after the next one (end of Q18). This maximizes variation across administrations. Alternatives, such as starting 11 months in, give similar results (p. 151).
- Table 6.1 covers elections since 1952 (N = 16). The 1948 election is excluded because quarterly data start in 1947 and the postwar transition distorts income growth (fn. 6, p. 151). The outcome is the incumbent party's popular-vote margin in percentage points. Would-be successors count as the same party (fns. 7–8, p. 151). Vote margins range twice as widely as vote shares, so coefficients scale accordingly (fn. 8, p. 151).
- Incumbent-party tenure is a control. The incumbent party's fortunes decline the longer it holds the White House. The authors presume this reflects exhausted agendas, turnover and scandals. Over four years it lowers the expected margin by 5–8 points (p. 152).

**Table 6.1 (p. 152).** Coefficients, with standard errors in parentheses. The outcome is the incumbent party's vote margin; N = 16.

| | Long-term | Short-term | Both |
|---|---|---|---|
| Growth Q3–Q15 | 1.35 (0.49) | — | — |
| Growth Q14–Q15 | — | 6.37 (1.06) | 7.62 (1.43) |
| Growth Q3–Q13 | — | — | −0.70 (0.55) |
| Tenure (years) | −1.68 (0.45) | −1.78 (0.29) | −1.79 (0.29) |
| Intercept | 6.20 (4.84) | 9.45 (2.55) | 12.33 (3.37) |
| Std. error of regression | 7.40 | 4.82 | 4.71 |
| Adjusted $R^2$ | .54 | .81 | .81 |

- Long-term model: each extra point of Q3–Q15 growth adds almost 1.5 points to the margin. Fit is mediocre, with an average error of 7.4 points (pp. 152–153).
- Short-term model: the average error falls by more than one-third and the effect is almost five times larger. Each point of Q14–Q15 growth adds more than 6 margin points (p. 153).
  - A one-term incumbent in a recession (Carter, 1980) might expect to lose by about 3 points.
  - A one-term incumbent in a boom (Johnson 1964, Nixon 1972, Reagan 1984) might expect to win by 18–23 points (p. 153).
  - In fact Johnson, Nixon and Reagan won by 18–23. Carter lost by 10, the second-largest residual; the authors suggest, "perhaps", foreign policy failures (fn. 9, p. 153).
  - Eisenhower 1956 has the largest residual in both models (9.4 and 9.8) (fn. 10, p. 153).
- Both-variables model: short-term growth matters even more, and earlier growth has a perversely negative coefficient too small to show any real long-term effect (p. 153).
- Fig. 6.1 plots the vote margin against Q14–Q15 growth adjusted for tenure. The adjustment subtracts $1.78/6.37 = .28$ points per tenure year beyond four years. Deviations exist, but the model gives "a powerful account" (pp. 154–155).

*Intuition note.* Voters seem to reward the last six months of income growth and almost nothing before. That is roughly what the musical-chairs image says. A model with two numbers (recent growth and tenure) fits 16 elections well.

**Robustness (pp. 155–158).**
- No horizon between 2 and 13 quarters fits better. The best, Q9–Q15, has a standard error about 6% larger; the others are 7%–54% larger (p. 155, fn. 12).
- Short-term coefficient: 5.5–6.7 when omitting each election in turn; 5.2 without the three boom years; 5.6 without the three negative-growth years; 6.7 without the three most recent elections (p. 155).
- Eight reelected presidents: 7.8. Six successor candidates: 3.7. The difference is too imprecisely estimated to be reliable (p. 155).
- **Table 6.2** (p. 156) tests Hibbs's geometric lag. Each quarter's weight is a fixed fraction $\lambda<1$ of the next quarter's weight (fn. 15, pp. 156–157).
  - Hibbs's estimates of $\lambda$ range from .80 to .954. Others find .82 down to .53. The authors' data give .76. They use .90 for illustration. With $\lambda=.90$, Q15 gets about 3.5 times the weight of Q3 (fn. 15, p. 157).
  - Column 1: geometrically weighted growth 5.83 (1.36), standard error 6.03, adjusted $R^2$ .70.
  - Column 2, adding Q14–Q15 growth: geometric −0.76 (2.76) and Q14–Q15 7.04 (2.69), standard error 5.00. The geometric term disappears (p. 157).
  - Column 3, separate year blocks: year 4 (Q13–Q16 block) 3.25 (0.92); Q9–Q12 2.45 (1.08); Q5–Q8 −0.02 (0.60); Q1–Q4 −1.11 (0.63); standard error 4.58, $R^2$ .83 (p. 156).
- The authors say it "would be a mistake to take these results too seriously". The year-by-year pattern suggests the geometric lag understates discounting in the first half of the term. Third-year growth "almost surely" matters a little. Second-year growth seems "utterly forgotten" (p. 157).
- Conclusion of the section: no analysis supports equal or near-equal weighting of the whole term (p. 158).

### Can Myopic Voters Select Competent Economic Managers? (pp. 158–168)
- Quoting Kramer, the authors say elections are "in substantial part responsive to objective changes" under the incumbent, but only for changes near Election Day. They ask "Is that good enough?" (a question they then pursue by testing selection and sanctioning separately) (p. 158).
- Two rationales for retrospective voting (from chapter 4) are tested separately. **Selection**: voters keep competent incumbents and replace incompetent ones. **Sanctioning**: voters reward success and punish failure so that leaders try hard, whatever their competence (p. 158).
- Selection needs real, persistent differences in economic competence between teams. The authors say this has never been systematically examined, as far as they know (p. 158).

**Dynamics of income growth (pp. 159–161).** Fig. 6.2 shows three features of postwar growth.
1. No striking trend (fn. 16: modest drift).
2. Large short-term volatility; quarterly annualized swings of 5 points or more are common.
3. Very little continuity. Regressing current growth on four lags gives coefficients .00, .06, −.00 and −.14, with adjusted $R^2 = .01$. A single lag gives −.03 and $R^2 = -.00$ (fn. 18). So current deviations hardly forecast future ones (p. 159).
- Volatility is probably not just measurement error. There is no strong negative correlation between successive quarters, which random error would produce (fn. 17, p. 159).
- Differences among administration averages are modest compared with quarter-to-quarter swings. The correlation between a quarter's growth and its administration's average is only .29, or .16 once the quarter's own contribution to the average is removed. The F-test cannot decisively reject equal averages across administrations (tail probability .12) (p. 160, fn. 20).
- The correlation between growth in any two quarters and the same president's whole-term growth is .41. So "more than 80%" of the variance in overall performance is unrelated to short-term outcomes. This is consistent with $1-.41^2\approx .83$ (added step) (p. 161).
- Direct testing is hard, because the unobserved comparison is future performance under the incumbent versus the challenger (p. 161).

**Test 1: how well can a six-month window reveal competence? (pp. 161–164).**
- Using the chapter 4 model, subjective well-being is competence plus random factors. Six-month income growth stands in for well-being (p. 161).
- **Table 6.3** regresses six-month growth on indicators for the ten presidencies, or for the two parties (N = 131 six-month windows). Competence is taken as deviation from average growth, assumed "with unrealistic optimism" to be perfectly measured by observed average growth (p. 162).
  - Presidencies: deviations from +1.38 (Kennedy–Johnson) to −1.26 (G. H. W. Bush). Standard error 2.98, adjusted $R^2 = -.000$, efficiency of selection 8.3% over chance (pp. 162–163).
  - Parties: +0.41 (Dem), −0.28 (Rep), so about +.7 and −.7 relative to each other. Standard error 2.98, adjusted $R^2 = .005$, efficiency 9.1% (pp. 162–163).
- The regression standard error implies a noise level $\sigma$ slightly under 3.0, "off the chart" of figure 4.1's 0–2 scale (fn. 23, p. 163).
- Translated into reelection probabilities, voters are under 60% likely to reelect a more competent party or candidate, and over 40% likely to reelect a less competent one (p. 164).
- The inefficiency reflects the difficulty of the task (simplified here by assuming luck cancels out) and, in significant part, myopia (p. 164).

*Intuition note.* If growth jumps around a lot from quarter to quarter and an administration's true level moves little, a six-month window is mostly noise. Voters then have great difficulty telling good managers from lucky ones.

**Test 2: what happens after the election (pp. 164–166).**
- Expectation under selection: reelected incumbents should deliver more growth, and less variable growth (the worst having been weeded out). Replacements are random draws (p. 164).
- **Table 6.4** (Q19–Q34; eight reelections and eight replacements; N = 16) (p. 165):

| | Retained | Replaced | Difference |
|---|---|---|---|
| Income growth, mean | 7.95 (1.73) | 9.17 (1.70) | −1.22 (2.43) |
| Income growth, SD | 4.89 | 4.82 | +0.06 |
| GDP growth, mean | 7.87 (2.50) | 8.46 (1.43) | −0.59 (2.88) |
| GDP growth, SD | 7.06 | 4.06 | +3.00 |

- Growth was lower under reelected incumbents, by 13% (income) and 7% (GDP). It was equally or more variable. With 16 cases this is "far from definitive". The authors read it as no support for retention based on competence (pp. 165–166). Going back to 1929 with annual data adds four observations and leaves the results essentially unchanged (fn. 25, pp. 165–166).

**Test 3: does future growth predict the incumbent's vote? (pp. 166–168).**
- If voters forecast competence, incumbents who turn out to be competent should get more support, other things equal (p. 166).
- The authors say the objection that this test is too stringent amounts to conceding that selection is too hard for voters (p. 166).
- **Table 6.5** uses only the eight reelections (new administrations are random draws under this logic) (fn. 26, p. 166). The outcome is the reelected party's vote margin (p. 167):
  - Income growth, no controls: post-election growth −0.11 (0.68), adjusted $R^2 = -.16$.
  - Income growth with short-term growth and tenure: post-election growth −0.51 (0.59), short-term growth 6.73 (2.69), tenure −1.72 (0.61), standard error 5.70, adjusted $R^2 = .50$.
  - GDP growth, no controls: 0.17 (0.46), $R^2 = -.14$.
  - GDP growth with controls: 0.11 (0.56), short-term income growth 4.92 (3.45), tenure −1.80 (0.67), standard error 6.17, $R^2 = .42$.
- Post-election income growth stays "perversely negative" and gets larger with controls. GDP results are similarly null (pp. 167–168).
- **Caveat (author):** these tests are indirect and low-powered, so they do not prove selection is impossible. But the efficacy of retrospective selection "must... be taken as a matter of theoretical speculation, not as a matter of fact" (p. 168).

### Can Myopic Voting Provide Incentives for Sustained Economic Growth? (pp. 168–175)
**Sanctioning logic (pp. 168–170).**
- A rational electorate may punish bad times regardless of cause or competence, to discipline future incumbents. Here election outcomes are not meant to change the economy. So the null results of tables 6.3–6.4 are "no embarrassment" to this model (p. 169).
- But the model works only if voters reward what they want future incumbents to do. Voters want to maximize the present discounted value of future income. Income gains tend to cumulate and persist. So average real income growth throughout the term indexes the voter's long-term gain and is what should be rewarded (p. 169). Footnotes 28–29 note that the exact form depends on the discount rate. More impatient voters should reward early growth more, which they do not do (pp. 169–170).
- Instead the literature finds voters focusing on election-year conditions. Earlier conditions are, "to a good approximation", electorally irrelevant, despite being at least as important as election-year conditions for voters' long-term welfare (pp. 169–170).
- **Consequence (author):** a president who shirks, or pursues his own ideological agenda, early in the term pays little at the polls. Short horizons magnify incentives to manipulate the economy near elections. **Erikson (1989, quoted):** "a rational incentive for the party in power to manipulate the business cycle" (p. 170).

**Political business cycle literature (pp. 170–171).**
- **Nordhaus (1975)** pointed out that short voter horizons might induce a "political business cycle". **Tufte (1978)** found cycles in transfers, income growth, unemployment and inflation. Nixon in 1972 was an energetic manipulator, from the money supply to the timing of Social Security changes (p. 170). Footnote 30 says Nixon's zeal partly came from 1960, when jobless rolls rose by 452,000 in October. He lost the official popular vote by fewer than 120,000 votes (p. 170).
- **Tufte's worry (reported):** costs from wasteful spending and "myopic policies for myopic voters" (pp. 170–171). Later research is mixed: **Schultz (1995)** calls the evidence "spotty at best" (p. 171).
- **Authors' view:** the spotty support may reflect low test power with few elections, a focus on unemployment and inflation instead of income growth, ignoring fixed versus variable election timing, and skepticism from rational-expectations theory. They note political business cycles can emerge even with fully rational voters and politicians (Rogoff and Sibert 1988; Rogoff 1990) (p. 171).

**Their own test (pp. 171–174).**
- **Fig. 6.3** shows average real GDP and income growth by year of the term, 1949–2012. The authors expect a stronger cycle in income than in GDP. Voters respond more to income, and income is easier to manipulate (transfers, tax cuts) (p. 171).
- Election-year income growth averages 2.9 versus 1.9 in non-election years (more than 50% higher; $t = 2.8$), and election-year income growth exceeds election-year GDP growth by 40% (2.9 versus 2.0) (p. 172, fn. 31).
- Compare Q14–Q15 income growth with the Q3–Q18 GDP growth average. Across 16 administrations the former is about 0.2 points higher (annualized). Using table 6.1's estimate, the authors suggest incumbents have routinely padded margins by about two-thirds of a point. The arithmetic is not shown (p. 173).
- Examples: Nixon 1972 gained 7–8 points; Reagan 1984 and Johnson 1964 "probably" 8–9. Carter in 1980 "probably" lost 10–11 points through the election-year recession (p. 173).
- In the ten elections with a reelection-seeking president, the gap averaged almost half a point, worth 1.5 margin points. In the six with retiring presidents, short-term growth was slightly lower, reducing successors' margins by about 0.7. Dropping 1968 reduces but does not eliminate this. Dropping Carter 1980 would nearly double the boost to 2.8 (p. 173, fn. 33).
- Footnote 32 reports outside election years GDP 1.94 versus income 1.77, and in election years income 3.03 versus GDP 2.04 (p. 173).
- Social cost is hard to assess. If incumbents merely shift gains, everyone gets one more electoral edge. If waste results, voters bear the cost (p. 174). Footnote 34 notes that Republicans typically gained about 2 points from unusually high short-term growth when in office, and about 1 point from unusually low growth under Democrats. The footnote also comments on the unfairness of such gains (p. 174).
- **Turkey:** inflation was 17% in the six months before the November 1987 election and 48% in the next six months. The pairs for October 1991 were 26% and 36%, and for December 1995 24% and 46%. A Treasury director said bureaucrats dislike early elections (Uras 2004) (p. 174).
- **Remedies debated (voices):** **Nordhaus (1975)** doubted that better voter information could work ("the classical political solution") and favored changing election frequency or giving policy to unelected central bankers and interest groups. **Tufte (1978)** hoped public scrutiny would let voters "repudiate corrupt economic policies" (p. 174).
- Authors: there is little sign public scrutiny increased. Election-year income growth was 1.2 points higher than in other years in 1949–1976 and 1.1 points higher since 1977 (both $t = 1.9$) (p. 175, fn. 35).

*Intuition note.* If voters reward only the final months, politicians profit from timing growth to arrive then. The evidence for such timing in figure 6.3 is strongest for income, the variable voters respond to.

### Conclusion (pp. 175–176)
- The authors agree that economic assessments substantially drive outcomes. They deny that retrospective voting ensures effective accountability (p. 175).
- Myopia is likened to "duration neglect". Colonoscopy patients recall mostly the last few minutes (Kahneman 2000; Redelmeier, Katz and Kahneman 2003) (p. 175).
- Lab subjects with modest incentives show similar biases: overweighting recent performance, being swayed by unrelated welfare shocks, and being swayed by rhetoric (Huber, Hill and Lenz 2012) (p. 175).
- Results are "in an important sense, random", but not chaotic. Fig. 6.1 shows they are highly structured. The key factor is "essentially arbitrary" for accountability, and, when electoral competition is vigorous enough for the outcome to be in doubt, "usually, in effect, the voters toss a coin" (p. 176).
- One possible rehabilitation: in national crises, voters might cast ideologically sophisticated votes (Sundquist 1983). The 1932–1936 period is the strongest candidate, taken up in chapter 7 (p. 176).

## Toy example (ours, not from the text)
Two presidents, each with 8 quarters of income growth (percent per quarter):
- A: 1, 1, 1, 1, 1, 1, 1, 1. Whole-term sum = 8; last two quarters = 2.
- B: 2, −2, 2, −2, 2, −2, 3, 3. Whole-term sum = 2−2+2−2+2−2+3+3 = 6; last two quarters = 6.

Say voters add 6 margin points per point of last-two-quarter growth (illustrative, near the 6.37 in table 6.1).
- Myopic rule: A gets 6×2 = 12, B gets 6×6 = 36. B wins by more, although B delivered less total growth (6 versus 8).
- A whole-term rule, say 1.5 points per unit of term growth: A gets 1.5×8 = 12, B gets 1.5×6 = 9. Now A is ahead.
- Note B's quarters swing between 2 and −2. Looking at one or two quarters tells little about B's term average of 0.75. A's average is 1.0.

## Concepts
- [[retrospective voting]] — judging incumbents by their past performance. Here the authors test it with economic data (p. 146).
- [[myopic retrospection]] (new) — voters respond almost only to the latest economic conditions, here Q14–Q15, and discount or ignore the rest of the term (pp. 148, 153).
- [[retrospective selection]] (new) — voters keep competent managers and replace incompetent ones. It requires persistent competence differences and a usable signal (p. 158).
- [[retrospective sanctioning]] (new) — voters reward success and punish failure to motivate future incumbents, regardless of competence (pp. 158, 168–169).
- [[economic grace period]] (new) — the first months of a term, treated as the predecessor's responsibility. Here responsibility is Q3–Q18 (p. 151).
- [[incumbent tenure effect]] (new) — the incumbent party's vote margin falls with years in office (about 5–8 points over four years) (p. 152).
- [[geometric lag discounting]] (new) — weights falling by a fixed factor $\lambda$ per quarter going backward (fn. 15, pp. 156–157).
- [[political business cycle]] (new) — election-timed economic manipulation by incumbents facing short-sighted voters (Nordhaus, Tufte) (p. 170).
- [[duration neglect]] (new) — judging an experience by its final moments and ignoring its length (colonoscopy analogy) (p. 175).
- [[observable implications]] — the authors test testable consequences of the selection model (post-election growth, variance, vote margin) (pp. 164–168).

## Canonical instances
- [[instance-nixon-1972-manipulation]] — Nixon's pre-election manipulation, with a 7–8 point margin gain (pp. 170, 173).
- [[instance-carter-1980-recession]] — an election-year recession is estimated to have cost Carter 10–11 points (p. 173).
- [[instance-table-6-1]] — long-term versus short-term income growth models of the vote margin, 1952–2012 (p. 152).
- [[instance-turkey-inflation-cycles]] — inflation rises sharply after the 1987, 1991 and 1995 elections (p. 174).
- [[instance-huber-hill-lenz-lab]] — an experiment showing recency bias with real incentives (p. 175).

## Bridges (candidates)
- [same-math] Geometric lag weights $\lambda^k$ ↔ time series: exponentially decaying weights, as in an exponential moving average — same weight form (pp. 156–157).
- [structural-analogy] Retrospective sanctioning ↔ principal–agent problem: voters motivate an agent whose actions they cannot observe (pp. 168–169).
- [structural-analogy] Low quarter-to-quarter persistence and noise $\sigma$ ↔ signal extraction: a noisy signal cannot reveal a fixed trait (pp. 159–164).
- [metaphor] Musical chairs and duration neglect ↔ behavioral psychology: judgment by final moments (pp. 147, 175).

## Questions this raises
- If competence differences are real but small relative to quarterly noise, what would a voter need to observe to detect them?
- Would equal-weight (whole-term) voting be better than recency weighting? Could voters do it if they wished?
- Do the 16-election results hold in other systems, with other timing of elections, or with other economic indicators?
- If political business cycles are hard to detect statistically, how could one measure their cost?

## Reading notes
- Printed page = PDF page − 19 (for example, PDF page 165 is printed p. 146).
- The text layer was consistent with the images. Table 6.2 has merged row labels in the image. I read the 3.25 (0.92) cell as covering the Q13–Q16 block (year 4), and 7.04 (2.69) in column 2 as the Q14–Q15 term.
- Numbers for election-year versus non-election income growth differ slightly. The text says 2.9 versus 1.9 (p. 172). Footnote 32 gives 3.03 for election years and 1.77 for other years (p. 173). Also GDP 2.0 (p. 172) versus 2.04 (p. 173).
- Table 6.4 title says "1948–2008", but table 6.5 N lists 1948, 1956, ..., 2004 for the eight reelection cases. This is consistent with the text.
- The "two-thirds of a point" padding estimate (p. 173) is stated without the arithmetic. I did not reconstruct it.
- The unit has no exercises.
