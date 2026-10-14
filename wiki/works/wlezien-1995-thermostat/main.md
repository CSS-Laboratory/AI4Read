---
id: wlezien-1995-thermostat/main
work: wlezien-1995-thermostat
unit: paper
pages: 981-1000
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# The Public as Thermostat: Dynamics of Preferences for Spending

## L0 — One line
US public demand for "more" or "less" spending falls when appropriations rise and rises when they fall, so the public acts like a thermostat with negative feedback, clearly for defense and only weakly for social programs.

## L1 — The gist (≤ 120 words)
Does the public adjust its wish for "more" or "less" policy in response to what policymakers actually do? Wlezien builds a thermostatic model: public preference R is the gap between the preferred level of policy (P*) and actual policy (P). He tests it with annual US survey data on spending (1973–91) and with appropriations (money formally set aside in the budget). For defense, net support for more spending (% “too little” minus % “too much”) changes negatively with appropriations changes (b = −2.70). For social programs, the public does not reliably respond to appropriations for single categories, but does respond reliably to total social appropriations (b = −.18). Preferred levels also change over time. This matters because accountability needs an informed public.

**Prerequisites:** linear regression and first differences; the idea of negative feedback; "median voter".

## L2 — Key ideas (5–10 bullets)
- Thermostat model: the public's relative preference R is the gap between preferred policy P* and actual policy P, so ΔR = ΔP* − ΔP (p. 986).
- Tested hypothesis: preferences for more policy respond negatively to policy changes, in domains where policy is clear and salient (p. 981; p. 987).
- Defense: net support for more spending responds strongly and negatively to defense appropriations, with b = −2.70. The pattern is robust to exclusions (pp. 990–992).
- Social programs: no reliable response to appropriations in each category (welfare is the exception). There is a reliable response to total social appropriations, b = −.18, much weaker than for defense (pp. 993–994).
- The public responds to appropriations (decisions), not to outlays. This implies that the information the public gets about the domains studied is fairly accurate on balance, whether from the media or other channels (p. 998).
- The preferred level of spending also moves, proxied by net dislike of the USSR (defense) and business expectations (social) (pp. 988–989).
- Guns–butter trade-off runs one way: a higher preferred defense level lowers net support for social spending, not the reverse (p. 995).
- Policy only partly reflects public preferences: if policymakers were solely responsive to them, we would not see such pronounced cyclicality in preferences (pp. 998–999).

## L3 — Walkthrough

### Introduction and theory (pp. 981–984)
- Democratic accountability needs a public that notices policy and adjusts its "more/less" preferences accordingly (p. 982).
- Public = individuals along a preference dimension; public preference is the median, implying an "ideal" level. The author does not claim individuals hold specific levels in mind (p. 982).
- If actual policy differs from the preferred level, the public wants a change. If policymakers respond, the wish for more shrinks. If they overshoot, the public favors less. Once policy is adjusted enough, "the signal stops" (p. 982).
- The author places this in the tradition of Easton and Deutsch. He says it asks more of the public than Page and Shapiro's "rational public" does (p. 982).
- Stimson's "policy sentiment" shows that preferences across domains tend to move together in the same liberal or conservative direction. Duff's analysis gives some suggestion that this movement is thermostatic, but the author says this does not follow from the research. Whether the public adjusts to policy is not known (p. 983).
- Test domain: the US federal budget. It has clear annual policy and annual opinion surveys on spending categories since 1973 (p. 983).
- Responsiveness may differ by domain, depending on how available information is. Whether and how the public responds is an empirical question (pp. 983–984).

### Measuring Public Preferences for Spending (pp. 984–985)
- Survey item: spending "too much," "too little," or "about the right amount." Answers are anchored to the status quo (p. 984).
- Categories: big cities, education, environment, health, defense, welfare. The GSS asked from 1973 to 1991, except 1979 and 1981, where Roper data fill in (p. 984).
- Between 25% and 50% answer "about right." So the author uses **net support** = % "too little" − % "too much" (p. 985).
- Social categories move together (Figure 1). Defense moves inversely to them and varies far more (p. 985).
- Average social net support correlates r = .97 with Stimson's policy sentiment (p. 985, n. 5).

*Intuition note:* The survey asks only about relative preference: more or less than current policy, not a level (p. 984). The model works with changes in net support because influences on R carry over into future values (p. 989).

### A Model of Public Preferences for Spending (pp. 985–989)
Public preference R is the difference between P* and P, so R is "integrated": influences on R are carried into future values (p. 986).

$$\Delta R_t = \Delta P^*_t - \Delta P_t \tag{1}$$

For each spending category $i$:

$$\Delta R_{it} = \tau_{1i}\,\Delta P^*_{it} + \tau_{2i}\,\Delta P_{it} + e_{it} \tag{2}$$

- In theory $\tau_1 = 1$ and $\tau_2 = -1$. That needs a common metric and equal parameters across categories. The metrics are not common and $P^*$ is unobserved. So only $\tau_{1i} > 0$ and $\tau_{2i} < 0$ is hypothesized (pp. 986–987).
- Policy is measured by appropriations (budget authority), not outlays. Appropriations are measured as percentage change in real (1982) dollars (pp. 987–988). Data run from 1976, so the analysis covers 1977–1991 (p. 987).
- Simultaneity: any positive feedback from appropriations to net support biases against finding thermostatic behavior (p. 988).
- Instruments for P*: defense uses net dislike of the USSR (% dislike − % like). Social programs use long-term business expectations (Michigan Index of Consumer Sentiment, first quarter) (pp. 988–989).
- Figure 1's parallel movement across social categories implies that their preferred levels and/or policies move together. The inverse movement of defense and social preferences implies that their preferred levels and/or policies are inversely related (a possible guns–butter trade-off). The author says the analysis must account explicitly for any such parallelism and interdependence, which can be assessed empirically (p. 989).

### An Analysis of Public Preferences for Spending (pp. 989–995)
Dependent variables are differenced, as influences on preferences are integrated into future values (p. 989). Estimates are given in Tables 1–3.

**Defense (Table 1, OLS, N = 15, p. 990).**

| Term | Coefficient (s.e.) |
|---|---|
| Intercept | 11.53 (2.40) |
| Δ net dislike, t | .66 (.12) |
| Δ net dislike, t−1 | .60 (.13) |
| Defense appropriations, t | −2.70 (.41) |

$R^2 = .84$. The appropriations coefficient is negative and reliable (p. 992).
- Robustness: without the net-dislike variables, r = −.56 (p = .03). Without 1981–82, b = −2.46 (s.e. .67) (p. 992).
- Hartley and Russett found no feedback. The author says they used fiscal-year-mismatched timing and averaged opinion over the year, which masks feedback (p. 992, n. 13).

**Social, pooled five categories (Table 2, GLS-ARMA, N = 75, p. 991).**
- Business expectations: current .12 (.03), lagged −.08 (.03). The effect is largely short-lived (p. 992).
- Own-category appropriations: −.03 (.02). The sign is right but too unreliable to credit (pp. 992–993).
- With separate coefficients, only welfare is reliable (−.14, s.e. .06). The public generally does not respond to appropriations for particular social programs (p. 993).

**Total social appropriations (Table 3, p. 994).**
- Conjecture: the public learns only general facts, such as "Reagan cut social programs" (p. 993).
- Coefficient on total social appropriations: −.18 (.04), p < .01. It does not differ across categories (F₄,₆₇ = .34). $R^2 = .36$ (pp. 993–994).
- So the public responds to social appropriations more generally than to defense appropriations (p. 994).
- The response is much smaller than for defense (−.18 versus −2.70). This fits the more stable social preferences in Figure 1 (pp. 994–995).
- Footnote 18 reports that responsiveness to social appropriations varies by education (p. 995).

*Intuition note:* A 1% rise in defense appropriations lowers net support for more defense by about 2.7 points. The same rise in total social appropriations lowers net support for more social spending by about .18 points. The public reacts much more to defense appropriations; the author's conjecture is that information about particular social programs is less available (p. 994).

### A Guns-Butter Trade-Off? (pp. 995–997)
- Table 4 adds to each model the other domain's "predicted difference in the preferred level" (p. 995).
- Defense model: coefficient on predicted social difference is −.10 (.86), not significant.
- Social model: coefficient on predicted defense difference is −.10 (.03), significant. It holds across categories (F₄,₆₆ = .43) (pp. 995–996).
- Result: the trade-off is unidirectional, from guns to butter. The author reads this as national defense being primary in public evaluations (p. 997).
- Intercepts are positive (Tables 1 and 4). Combined with the appropriations coefficients, they imply the public wants real appropriations to rise by about 4–8% a year. Defense is 11.53/2.70 = 4.3%. Social is 1.38/.17 = 8.1% (p. 997, n. 21).
- The author notes this exceeds average real GNP growth (p. 997).

### Discussion (pp. 997–999)
- The thermostatic model "works quite well." There is negative feedback of spending decisions on relative preferences. It is not claimed that preferences reflect only policy shifts, since preferred levels also change (p. 998).
- The public responds to appropriations, not to the more tangible outlays. The information the public receives about certain policy domains is quite accurate, on balance; otherwise the public could not behave like a thermostat (p. 998).
- Policymakers may not follow the signals closely. Preferences drifted conservative in the 1970s and liberal in the 1980s. If policymakers were solely responsive, preferences would equilibrate quickly (pp. 998–999).
- The model works less well for crime, foreign aid and space. For crime, b = −.09 (s.e. .08) (p. 998, n. 23).

## Toy example
*(Ours, not from the text.)*
Idealized case with $\tau_1 = 1$, $\tau_2 = -1$, and $P^* = P = 100$ at the start, so $R = 0$.
- Year 1: $P^*$ rises to 110, $P$ unchanged. $\Delta R = 10 - 0 = +10$, so $R = 10$.
- Year 2: policy rises by 8. $\Delta R = 0 - 8 = -8$, so $R = 2$.
- Year 3: policy rises by 6 more (overshoot). $\Delta R = -6$, so $R = -4$. Check: $110 - 114 = -4$. The public now favors less.

Using Table 1: suppose net dislike of the USSR has been unchanged over the last three years, so both differenced-dislike terms are 0. A 5% rise in defense appropriations predicts $\Delta R = 11.53 + (-2.70)(5) = 11.53 - 13.5 = -1.97$. The break-even rise is $11.53/2.70 \approx 4.27\%$.

## Concepts
- [[feedback]] — policy outputs "feed back" on public inputs (Easton's model) (p. 981).
- [[negative-feedback]] — a rise in appropriations lowers the public's wish for more spending, and vice versa (p. 998).
- [[reference-set-point]] — the public's preferred level of policy, $P^*$, which itself can change and is unobserved (p. 982; p. 987).
- [[error-signal]] — the public's relative preference $R = P^* - P$ is the "signal" sent to policymakers (pp. 982, 986, 998).
- [[net-support]] (new) — % "too little" minus % "too much" on spending (p. 985).
- [[appropriations-vs-outlays]] (new) — the public responds to budget authority (decisions), not to money actually spent (pp. 987, 998).
- [[instrument-for-preferred-level]] (new) — net dislike of the USSR and business expectations stand in for unobserved $P^*$ (pp. 988–989).
- [[differenced-dependent-variable]] (new) — model changes in $R$ because $R$ is integrated (pp. 986, 989).

## Canonical instances
- [[us-defense-spending-preferences]] — net support for defense follows Soviet net dislike and responds negatively to appropriations (p. 992).
- [[total-social-appropriations-response]] — public responds to total social appropriations but generally not to category appropriations (welfare aside) (pp. 993–994).
- [[guns-butter-tradeoff]] — preferred defense level lowers social net support, not the reverse (p. 995).
- [[public-as-thermostat]] — the central analogy (p. 982).

## Bridges (candidates)
- [structural-analogy] $R = P^* - P$ as public signal ↔ control theory: error signal = reference − output — same sign logic, but $P^*$ is unobserved here.
- [structural-analogy] Policymakers as the plant, the public as the sensor and comparator ↔ closed-loop control — the author notes policymakers may not follow the signal (p. 998).
- [metaphor] "Signal stops once adjusted" ↔ steady-state error going to zero (integral action) — the text does not model integral action.

## Questions this raises
- How long are the delays between appropriations decisions and the public's response?
- Does the sharp asymmetry between defense and social programs persist if information availability is measured directly?
- If policymakers only partly follow the signal, what explains the cyclicality of preferences?
- Does the 4–8% "wanted growth" reflect income effects, which the author says he did not consider (p. 997, n. 21)?

## Reading notes
- Printed pages 982–1000; the unnumbered abstract page (pdf 2) is taken as p. 981 from the citation line. Printed = pdf + 979 for later pages.
- The text layer has missing spaces and garbled words; tables were read from the images.
- Table 4 column heading reads "Net Suport" (misprint). Its note reads "Uniont" for "Union_t".
- Table 2's second model has adjusted $R^2 = .16$, lower than the first model's .17, despite higher $R^2$.
- The author does not write out the estimated equations as formulas. Only (1) and (2) are given.
