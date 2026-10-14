---
id: bail-2018-opposingviews/main
work: bail-2018-opposingviews
unit: paper
pages: printed pages unknown (journal pages 9216–9221)
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
# Exposure to opposing views on social media can increase political polarization

## L0 — One line
In a month-long Twitter field experiment, paying frequent Twitter users to follow a bot retweeting opposing-party elites produced no evidence of reduced polarization: Republicans became substantially more conservative, and Democrats' small shift toward liberal views was not statistically significant.

## L1 — The gist (≤ 120 words)
Social media is often blamed for "echo chambers" that shield people from opposing views. The authors ask whether breaking that selective exposure changes political attitudes. They recruited Democrats and Republicans who use Twitter often, randomly offered some of them money to follow a bot retweeting opposing-side accounts for a month, and surveyed everyone before and after. Treated Republicans moved toward more conservative views; the effect grew with compliance. Treated Democrats moved slightly toward liberal views, but not significantly. The authors stress limits (self-identified partisans who use Twitter often, paid exposure, unknown mechanism). They conclude that broad exposure to opposing views may be ineffective or counterproductive for reducing polarization.

**Prerequisites:** random assignment and control groups; regression with a control for the pre-test score; p-values and confidence intervals; the idea of non-compliance in experiments.

## L2 — Key ideas (5–10 bullets)
- The "echo chamber" worry is hard to test observationally, because it is hard to establish whether social networks shape opinions or the reverse (§ "Introduction"). The authors respond with a randomized field experiment designed to disrupt selective exposure.
- Three preregistered hypotheses: disrupting selective exposure will decrease polarization through intergroup contact; exposure may backfire through motivated reasoning; backfire is more likely among conservatives than liberals (§ "Introduction").
- Design: pre-survey, random assignment, one month of bot-delivered opposing-party tweets, post-survey, with weekly compliance checks (§ "Research Design").
- Treated Republicans: ITT = 0.12 on a seven-point scale (p = 0.008), and larger for more compliant respondents (§ "Results").
- Treated Democrats: small, non-significant shifts toward liberal views (§ "Results").
- The authors could not identify the mechanism and could not rule out several alternative explanations (§ "Discussion and Conclusion").
- Scope is limited to party-identified, frequent Twitter users who were paid to follow the bot (§ "Discussion and Conclusion").
- Practical reading: efforts to expose people to opposing views on Twitter might be ineffective or counterproductive, especially if started by liberals (§ "Discussion and Conclusion").

## L3 — Walkthrough

### Introduction (untitled opening section)
- Polarization in the US is a central topic. Divisions on issues such as inequality, gun control and immigration increasingly align with partisan identity. Partisanship predicts policy preferences nearly three times as well as any other demographic factor, as the authors report citing Pew (§ "Introduction", para. 1).
- Echo chambers are patterns of information sharing that reinforce prior beliefs by limiting exposure to opposing views. Concern rose with social media, where **homophily** (tendency to form ties with similar people) may worsen the problem (para. 2).
- Methodological problem: it is hard to tell whether networks shape opinions or the reverse (para. 2).
- The authors report a field experiment that disrupts selective exposure among Twitter users. It is governed by three preregistered hypotheses (para. 3):
  1. **H1:** disrupting selective exposure will *decrease* polarization through intergroup contact effects. Earlier contact studies concern interpersonal contact. Here the contact is virtual, and anonymity might encourage incivility (para. 3).
  2. **H2:** exposure to opposing views may create **backfire effects**. People are prone to counterargue conflicting messages using motivated reasoning, which, the literature indicates, increases commitment to prior beliefs. Backfire findings from fact-correction survey experiments (e.g. Saddam Hussein and weapons of mass destruction) failed to replicate in two recent studies. This study does not test fact correction. It tests prolonged exposure to counterattitudinal messages (para. 4).
  3. **H3:** backfire is more likely among conservatives than liberals. The authors cite value differences (certainty and tradition vs change and diversity) and asymmetric polarization in roll-call voting. They know of no study of this asymmetry in the broader public or on social media (para. 5).

*Intuition note:* Contact could reduce prejudice, or it could trigger defensive reasoning. The experiment pits these two possibilities against each other.

### Research Design
- **Sample and survey.** A professional survey firm recruited self-identified Republicans and Democrats who visit Twitter at least three times a week. They took a 10-minute survey in mid-October 2017 and again 1.5 months later. The outcome is change in ideology on a 10-item, seven-point agree/disagree policy scale (α = .91). Twitter IDs were collected to mine behavioural data. IRBs at Duke and NYU approved the study, and respondents gave informed consent (§ "Research Design").
- **Randomization.** Separate experiments were run for each party. Within each, block randomization stratified respondents by party attachment and interest in current events, and also by Twitter-use frequency (which the authors reasoned would affect exposure).
- **Sample size.** There were 1,652 pre-survey responses (901 Democrats, 751 Republicans).
- **Treatment.** One week later, an "ostensibly unrelated" survey design was used. Treated respondents were offered $11 to follow a bot that would retweet 24 messages a day for 1 month. They were not told the content. Each experiment had a liberal and a conservative bot. The bots retweeted messages sampled at random from 4,176 political accounts (officials, opinion leaders, media, nonprofits). The accounts were found by network sampling, which assumes similar ideologies follow each other.
- **Compliance monitoring.** Respondents could earn up to $18 more for weekly surveys. These asked about tweet content and about an animal picture the bot tweeted twice a day and deleted just before each survey.
- **Compliance rates.** 64.9% of Democrats and 57.2% of Republicans accepted the invitation. About 62% of those who followed answered all substantive content questions, and 50.2% identified the animal picture.

### Results
- **Estimands.** ITT is the effect of *assignment* to treatment. CACE (Complier Average Causal Effect) accounts for differing compliance rates. Models predict the post-treatment scale score, controlling for the pre-treatment score (to mitigate period effects) and 12 other covariates. Positive = more conservative; negative = more liberal (§ "Results").
- **Compliance definitions.** *Minimal* means followed the bot throughout. *Partial* means answered at least one but not all weekly content questions. *Full* means answered all of them. The last two are mutually exclusive.
- **Analysis samples.** Democrats n = 697, Republicans n = 542 (Fig. 3 caption).

| Group | Democrats (est., p, n) | Republicans (est., p, n) |
|---|---|---|
| Assigned (ITT) | −0.02, p = 0.45, 416 | 0.12, p = 0.008, 316 |
| Minimally compliant (CACE) | −0.04, p = 0.45, 271 | 0.19, p < 0.007, 181 |
| Partially compliant (CACE) | −0.05, p = 0.45, 211 | 0.31, p < 0.007, 121 |
| Fully compliant (CACE) | −0.14, p = 0.46, 66 | 0.60, p < 0.01, 53 |

- Democrats: slightly more liberal after treatment, growing with compliance, but no estimate is statistically significant.
- Republicans: substantially more conservative, growing with compliance, and highly significant.
- The authors' most cautious estimate for Republicans is +0.12 points. The fully compliant estimate is +0.60. They say these correspond to increases of 0.11 to 0.59 standard deviations.

*Intuition note:* ITT is what happens when you merely *offer* the treatment. CACE asks what happens to those who actually took it, The paper says only that CACE accounts for differing compliance rates. In the table, the estimates grow as the compliance definition gets stricter.

### Discussion and Conclusion
- **Limits on generalizing.** The findings do not show that exposure raises polarization in all settings. They should not be generalized to all of the US, since most Americans do not use Twitter. Other countries, independents and infrequent users were not studied. Respondents were paid to read opposing messages, so unpaid users might ignore them. Perhaps the most important limitation is that the mechanism behind the Republican backfire was not identified.
- **Alternative explanations.** SI analyses give the authors confidence that the results are not driven by Hawthorne effects, partisan "learning", differing message extremity by party, or age differences in social media use. They cannot rule out other explanations:
  - more exposure to politics in general, rather than to opposing messages as such;
  - more exposure to women or minorities retweeted by the liberal bot;
  - a possible antielite bias that could exacerbate the backfire effect, since the bots showed only high-profile elites, whom previous studies find significantly more polarized than the general electorate.
- **Contributions.** The authors found no evidence that exposure to opposing views reduces polarization. They found significant partisan differences in backfire effects, under repeated contact over an extended period. They also claim a methodological advance for computational social science: combining surveys, bots and digital trace data, with compliance measurement and behavioural verification of survey answers.
- **Applied reading.** The authors say recent studies indicate that this population has an outsized influence on public discussion. Broad exposure to opposing views on a site like Twitter *might* be ineffective or counterproductive, particularly if initiated by liberals. Future work should learn which messages, tactics or issue positions cause backfire, and whether nonelites or offline settings work better.

*Intuition note:* The authors suggest that simple attempts to "show people the other side" might be ineffective or counterproductive. They do not claim to know why it happened.

## Toy example (ours, not from the text)
Assume 100 respondents are assigned to treatment and 100 to control, and the scale runs 1–7 with higher = more conservative. After adjusting for pre-scores, assume the treated group's mean post-score is 4.12 and the control group's is 4.00.
- ITT = 4.12 − 4.00 = 0.12.
- Suppose 60 of the 100 treated people actually followed the bot, so the compliance rate is 60/100 = 0.60.
- If we assume non-followers were not affected, the effect on followers is CACE = 0.12 / 0.60 = 0.20.

This shows why CACE (0.20) exceeds ITT (0.12) when compliance is partial. The division is the standard instrumental-variable logic, and the paper does not print this formula.

## Concepts
- [[selective-exposure-media-choice]] — people's choice of information that fits their views; the paper tries to *disrupt* it experimentally (§ "Introduction")
- [[echo-chamber]] (new) — information-sharing patterns that reinforce prior beliefs by limiting exposure to opposing views (§ "Introduction")
- [[homophily]] (new) — tendency to form network ties with similar others (§ "Introduction")
- [[intergroup-contact]] (new) — contact between rival groups, expected to reduce stereotypes (here, virtual contact) (§ "Introduction")
- [[backfire-effect]] (new) — people exposed to conflicting messages are prone to counterargue them, which may increase commitment to prior beliefs (§ "Introduction")
- [[motivated-reasoning-motivated-skepticism]] — the cited mechanism for backfire: counterarguing messages that conflict with one's own attitudes (§ "Introduction")
- [[intent-to-treat]] (new) — effect of being assigned to treatment, regardless of compliance (§ "Results")
- [[cace]] (new) — Complier Average Causal Effect: effect among compliers, adjusting for compliance rates (§ "Results")
- [[block-randomization]] (new) — random assignment within strata (party attachment, interest, Twitter use) (§ "Research Design")
- [[asymmetric-polarization]] (new) — Republicans becoming more conservative while Democrats change little, a pattern the authors cite from roll-call voting (§ "Introduction")

## Canonical instances
- [[bail-twitter-bot-experiment]] — month-long paid exposure to opposing-party bot retweets; Republicans shifted conservative (§ "Results")
- [[wmd-correction-backfire]] — fact-correction (Saddam Hussein/WMD) backfire findings, which failed to replicate in two recent studies (§ "Introduction")

## Bridges (candidates)
- [structural-analogy] Backfire after exposure ↔ political-science: motivated skepticism and identity-protective cognition — both say conflicting information can strengthen priors.
- [structural-analogy] Echo chambers via homophily ↔ sociology/networks: homophily and selection-versus-influence confounding.
- [same-math] ITT vs CACE ↔ causal inference: instrumental-variable estimation with random assignment as the instrument (the standard identity is not printed in this paper).

## Questions this raises
- What mechanism produced the Republican shift (counterarguing, reaction to elites, reaction to the identities of the retweeted people)?
- Would unpaid users show the same effects, or even see such messages at all?
- Why were Democrats' estimates small and not significant: a true asymmetry, or too little power?
- Would bots retweeting non-elite accounts, or offline contact, produce contact-like effects?

## Reading notes
- The source is an HTML copy from PMC (PNAS 2018, 115(37):9216–9221). No printed page numbers are visible, so citations use section headings.
- Fig. 1 and Fig. 2 are images and are not in the text; only their captions are visible. Fig. 3's caption text is the source of the numbers above.
- The text after the Fig. 3 caption repeats the same points twice with slightly different wording; the digest reports them once.
- Fig. 3 gives n = 697 and 542, but pre-survey responses were 901 and 751. The text does not explain the gap, and the SI Appendix was not provided.
- Odd as printed: the minimal and partial CACE for Republicans share t = 2.73 and p < 0.007. The reference list repeats Wood & Porter (refs 38 and 39). Refs "(34, 26)" are cited for cultural schemas.
- The Discussion says it found no evidence that exposure reduces polarization (bearing on H1) and reports significant partisan differences in backfire effects (bearing on H3). It does not explicitly label the hypotheses as confirmed or rejected.
- All methods, covariates and robustness checks are in the SI Appendix, which was not provided.
