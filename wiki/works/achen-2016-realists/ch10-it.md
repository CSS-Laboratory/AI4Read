---
id: achen-2016-realists/ch10-it
work: achen-2016-realists
unit: "Chapter 10 — It Feels Like We're Thinking: The Rationalizing Voter"
pages: 267-296
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# It Feels Like We're Thinking: The Rationalizing Voter

## L0 — One line
Party identification often shapes what citizens think the parties stand for, what they believe are facts, and even their unrelated issue views; this consistency feels like thinking, and it is often strongest among the well-informed.

## L1 — The gist (≤ 120 words)
What comes first for voters: opinions or party loyalty? Achen and Bartels argue that party identification, the most important political identity, often produces the "reasons" citizens give. They show this three ways. Partisans misperceive where the parties stand on issues. Partisans give partisan answers even to factual questions, and political knowledge often fails to correct this. After the Watergate shock to partisanship, well-informed people also changed views on logically unrelated issues. Voters may be "rational" in a thin sense, but their beliefs rest on partisan surmise and folk wisdom. This matters because the folk theory of democracy (informed citizens translate their values into political preferences and action) assumes informed citizens pick policies and govern through elections.

**Prerequisites:** survey percentages and 7-point scales; reading a regression coefficient and its standard error; the idea of a weighted average (and, loosely, Bayesian updating from a prior).

## L2 — Key ideas
- Party identification (a voter's attachment to a party) is the broadest political identity. It organizes the thinking of its adherents, so many preferences and "facts" are consequences of loyalty, not its bases (pp. 267–269).
- On taxes and services, Republicans and Democrats at the same self-placement perceive different distances to the parties. This is the reverse of what the folk theory of democracy and the spatial model of voting (voters compare their own position with perceived party positions) assume (pp. 270–272).
- Two readings of such misperception exist: non-rational cognitive balancing (imagining one's party shares one's views, to ease dissonance) and rational partisan inference (using one's party to guess what one does not know). The authors call the choice between them "a distinction without a difference" for their argument. They doubt that the result is good for democracy (pp. 273–275).
- Perception errors are large and grow for unfamiliar candidates. For favored groups, own positions get about one-third the weight of the group's actual position (pp. 275–276).
- Factual beliefs are partisan too (inflation 1988, Iraq, the 1996 deficit), and more political knowledge often increases partisan bias (pp. 277–279).
- The Achen–Bartels model weights prior belief, party cues and facts by reliability. It predicts, and the data show, that moderately informed Republicans were the most wrong about the 1996 deficit (pp. 279–284).
- After Watergate, well-informed people shifted both perceived proximity and their own positions on unrelated issues. Less-informed people mostly did not (pp. 284–293).
- Conclusion: rationalization is often strongest among the engaged. Thin rationality is not competence, which also needs accuracy and openness to disconfirming evidence (pp. 294–296).

## L3 — Walkthrough

### Introduction (pp. 267–269)
- **Claim.** The primary sources of partisan loyalty and voting are social identities, group attachments and myopic retrospections, not policy preferences or ideological principles (p. 267). Chapter 9 showed that single identities (Catholic, white southerner, woman) can have large effects when made salient or threatened (p. 267).
- **Why party identification.** Unlike particular social identities, partisanship is relevant in nearly all elections. Each party gives its adherents a conceptual framework, spread by sympathetic media. It names friends and enemies and supplies talking points (p. 268).
- Footnote 1: the Michigan concept of party identification does not fit everywhere. In systems organized around a leader (de Gaulle, Perón) or with changing party names (South Korea), voters still find "their party", which suffices for the argument (pp. 267–268).
- **Inside the framework.** Candidate preferences, opinions and view of the facts "go together nicely". The other side's arguments seem dismissible. The voter does not see that the opinions propping up her loyalty are not really hers: "It will feel like she's thinking" (p. 268).
- Even among well-informed people, the preferences that look like bases of partisanship are often consequences of loyalties. More information often lets the voter bolster identity with rational-sounding reasons. Converse might call such a person an "ideologue", yet she may be as impervious to evidence as anyone (p. 268).
- **Psychology cited.** Rahn, Krosnick and Breuning (1994): people asked to explain preferences mention reasons that sound rational and systematic and overlook emotional ones. In short, "people rationalize their pre-existing preferences" (p. 269).
- **Plan.** Three aspects of partisan beliefs: perceptions of party positions, purely factual beliefs, and the "ricochet effect" on other issues when an exogenous shock moves partisanship (p. 269). The authors say the evidence is "overwhelming" (p. 269).

*Intuition note.* If loyalty comes first, then the reasons a voter gives can be after-the-fact. The voter cannot tell the difference from the inside.

### Partisan Perception and Misperception (pp. 269–276)

**The measure.** Cognitive dissonance (Festinger) is the unpleasant feeling that my party's candidates do not share my views. One relief is to adopt the party's position. A simpler one is to imagine the party's views match mine, which the authors call "cognitive balancing" (p. 269).

ANES taxes-vs-services question, asked since 1982: self-placement and party placements on a 7-point scale from "many more services" to "reduce spending a lot" (pp. 269–270).
- **Issue proximity** = (perceived distance to the Democrats) − (perceived distance to the Republicans). Example: GOP one unit away, Democrats four units away gives +3, favoring the Republicans (p. 270). (Added step, notation:) $\text{prox}_i = |x_i - \hat d_{i}| - |x_i - \hat r_{i}|$, where $x_i$ is the respondent's own placement and $\hat d_i,\hat r_i$ are her placements of the Democratic and Republican parties.
- **Test.** Without rationalization, a Democrat and a Republican who both place themselves at 2 and see the parties accurately have identical proximity, so partisanship should be irrelevant. With rationalization, Republicans' scores are pulled up and Democrats' scores pulled down (p. 270).
- **Nonresponse.** Of more than 22,000 respondents, about 15% would not place themselves and another 14% did not place one or both parties. So about 30% could not compute proximity as the spatial model of voting (chapter 2) takes for granted (p. 270).
- **Result (Fig. 10.1, 1982–2012).** Unbiased perceptions would make the Republican and Democratic curves overlap. They diverge markedly. At the scale midpoint ("the 24% of these respondents" in Fig. 10.1; 2,803 partisan identifiers per fn. 3), the groups differ by a full point. Republicans saw their party as more than half a point closer to the middle, and Democrats saw theirs as almost half a point closer. "Obviously, both could not be right" (p. 271). The t-statistic is 25.6, against the customary 1.96 (fn. 3, p. 271). Year-specific intercepts barely change this (fn. 4, p. 271).
- Liberal Democrats and conservative Republicans, sensibly, saw themselves as closer to their own party, increasingly so as they became more extreme (p. 272). But liberal Republicans and conservative Democrats were "entirely impervious" to the fact that their views were closer to the other party. Liberal Republicans saw the GOP as just as close as the Democrats, and conservative Democrats saw their party as just as close as the Republicans (p. 272).
- Footnote 5: 20% of Republican identifiers and 15% of Democratic identifiers took positions contrary to their party's usual one on this issue. Dissonance has been more common on most other ANES issues (p. 272).
- Footnote 6: abortion is an exception. Most pro-choice Republicans and (by a narrower margin) most pro-life Democrats saw themselves as closer to the other party. Most other issues look like the spending case, so "partisan misperception is the rule, not the exception" (p. 272).
- **Conclusion.** Party loyalty determines how many voters see party positions, the opposite of the folk theory and the spatial model. This may help explain why the electorate fails to pull polarized parties back to the centre (Sood and Iyengar 2014) (p. 272). Berelson, Lazarsfeld and McPhee (1954) were among the first to show partisan coloring of perceived candidate positions (p. 272).

*Intuition note.* Two people at the same spot on a scale should measure the same distance to the same party. They do not, and the gap tracks their party label.

**Two explanations.**
- **Non-rational (Brady and Sniderman 1985).** People want accuracy and also "a strain to consistency". Liked groups are seen as near, disliked groups as far. Perception is a weighted average of the group's actual and hoped-for position, with weights set by the relative importance of accuracy and consistency (p. 273).
- **Rational but poorly informed (Lowell; Feldman and Conover 1983).** **Lowell (1913):** following a trusted party blindly is "not wholly without justification" because it probably stands for opinions one would hold after study (p. 273). **Feldman and Conover:** apparent dissonance reduction can be rational inference under uncertainty. Assuming consistency "may be an efficient way of perceiving the world" (p. 273). Their cues include own issue positions and perceptions of parties and ideological groups (p. 273). Conover and Feldman (1989) found most people uncertain about Carter's positions in the 1976 primaries but shifting toward the Democratic Party's positions once he was nominee (p. 274).
- **The authors' response.** Perceptual bias may be "efficient" at minimizing psychological stress. Example: a Democrat who favors spending cuts can convince himself that Obama is just as committed to cutting spending. This may be a "reasonable response to ambiguity" for someone who ignored Obama's statements, actions and party platforms. But "we see no reason to suppose that it is conducive to effective electoral democracy" (p. 274).
- The same pattern fits cognitive balancing or partisan inference. For their argument "this is a distinction without a difference", and they do not want to get caught in debates about mechanisms (p. 274). They cite Lodge and Taber (2013) on affective and cognitive forces working outside awareness, and say subconscious dissonance minimization seems like "a pretty good bet" as the central force. They also note that similar patterns follow from stylized rational-choice assumptions (Achen and Bartels 2006; Lauderdale 2012) (pp. 274–275).

**How wrong are perceptions?**
- **Authors' complaint.** The cues literature expresses enthusiasm for "efficiency" and "rationality". **Feldman and Conover:** voters "do the best they can" and inference makes a positive contribution to vote choice (p. 275). **Brady and Sniderman:** affect efficiently encodes who and what one is for or against, and the mass public is "remarkably accurate" about strategic groups (p. 275). The authors say that claim seems to refer to the public's average, not to individuals, and that Brady and Sniderman said little about accuracy (p. 275).
- **Brady and Sniderman's own results.** In 34 analyses, perceptions of disliked groups were fairly accurate on average. Perceptions of favored groups were strongly biased toward the respondent. For a typical favored group, own position got about one-third the weight of the group's actual position (p. 275).
- Footnote 8: the model has a "false consensus" term (average estimate .185) and a differential projection term (.550). For a 25-point feeling-thermometer difference between favored and disfavored groups, the combined effect is +.05 for disfavored and +.31 for favored groups. The actual position is normalized to 1.0 (pp. 275–276).
- These are salient groups (liberals/conservatives, blacks/whites, Republicans/Democrats). The authors assume projection would be larger for less familiar groups or candidates and for less prominent issues (p. 276).
- **Primaries (Bartels 1988, 98–107).** In 1984, Democrats saw front-runner Mondale as about 20% closer to their own positions than he was. For little-known Hart the distortion was about 40% early, declining to about 20%. People giving Hart the warmest thermometer rating early saw him as almost 75% closer than he really was (p. 276).
- **Verdict.** Voters may "do the best they can" but still be "depressingly far" from realistic perceptions, which belies the "encouraging" conclusion (p. 276).
- Footnote 9: Rahn (1993) found that with both party stereotypes and particular policy information available, voters rely on the label, neglect the policy information and are less responsive to inconsistent information (p. 276). So partisan inference may crowd out real information.

### Our Own Facts (pp. 276–284)

- **Folk theory.** Facts transcend moral disagreement, so people with different values can agree on facts (e.g., whether raising the minimum wage increases unemployment), and agreement on facts helps agreement on policy. Citizens can learn what they need to know, and more engagement is the surest route to improvement (p. 277). Two problems: widespread ignorance (chapter 2), and how much people "know that ain't so" (Hochschild and Einstein 2015) (p. 277).
- **Inflation 1988.** Inflation fell from 13.5% (1980) to 4.1% (1988). 47% of "strong" Republicans said "much better" and 13% said worse. Fewer than 8% of "strong" Democrats said "much better", and more than half said worse (p. 277).
- **Iraq (Program on International Policy Attitudes 2006).** About 18 months after the 2003 invasion: 47% of Republicans vs 9% of Democrats believed Iraq had weapons of mass destruction (WMD); 71% vs 37% believed Iraq was directly involved in 9/11 or gave substantial support to al-Qaeda. 18 months later: 41% vs 7% (WMD), 63% vs 35% (al-Qaeda link) (pp. 277–278). Footnote 10: Jacobson (2008) cites even larger gaps in late 2004–early 2005 (around 80% of Republicans, fewer than 40% of Democrats, said WMD) (p. 278).
- **Interpretation.** Gaines et al. (2007) found that in repeated interviews with college students in 2003–2004 all partisan groups held reasonably accurate beliefs and updated them. They differed greatly in interpretation, and "effectively used interpretations to rationalize their existing opinions" (p. 278).
- **Why.** Dissonance reduction may lead people to adopt the party's view of whether crime is rising. Or people may do their best, since few consequential facts can be verified personally, and may reasonably guess that the party's view is what they would reach after study (the Lowell argument). Either way the result is partisan consistency, but the danger is more obvious for facts than for other perceptions (p. 278).
- **Knowledge does not cure bias.** Factual judgments are "cobbled together" from news, conversation, propaganda and folk wisdom. In some cases accurate information trumps partisanship, and some observers assume rationalization is greater for less-informed citizens (Aldrich et al. 1989) (p. 279). **Shani (2006):** political knowledge "enhances the bias" (p. 279). Footnote 11: of eight factual questions in ANES 2000, seven showed substantial, significant increases in partisan bias among the well-informed, largely unchanged by controls for values or demographics (p. 279).

**The model (Achen and Bartels 2006), described in words only, p. 279.**
- A fully rational citizen's opinion is a weighted average of three quantities:
  1. background opinion or prior belief;
  2. what she hears from party leaders and co-partisans, or infers from her own partisanship;
  3. actual factual knowledge.
- Weights depend on the reliability of her information on each, which depends on political information and experience (p. 279).
- Footnote 12: reliability weighting in Bayesian learning models yields complex nonlinear relations between information and judgments within each partisan group. So the model implies one should not generally expect linear relations between cues and judgments or between information and the extent of bias (p. 279).
- Citizens sure of the facts rely on facts. Those who know only talking points parrot the party or assume that when the other party is in office times are bad. Those who know neither use folk wisdom about "how things always are" or the zeitgeist (p. 280).

**Case: the 1996 budget deficit** (ANES 1996: did the yearly deficit increase, decrease or stay the same during Clinton's time as President?).
- **Why a clean test.** The question is factual. Republicans and Democrats would hardly differ on what "yearly budget deficit" means or on standards for "increased". So differences must come from rationalization or partisan inference, not values (p. 280).
- **The facts.** The deficit rose under Bush and was central to Perot's 1992 campaign, then fell from $255bn (FY1993) to $203bn (FY1994), $164bn (FY1995) and $107bn (FY1996). The correct answer was "decreased a lot" (p. 280). Footnote 14: the CBO's August 1996 update had already estimated $116bn for FY1996 (p. 280). Footnote 13: Perot's supporters' deficit concern was in large part itself a consequence of his campaign (p. 280).
- **Table 10.1 (by 1992 party identification).**

| Answer | Democrats % | Independents % | Republicans % | Total % |
|---|---|---|---|---|
| Increased a lot (−50) | 6.7 | 15.8 | 22.6 | 14.8 |
| Increased a little (−25) | 25.6 | 22.1 | 29.7 | 25.2 |
| Stayed about the same (0) | 28.5 | 29.7 | 23.5 | 27.7 |
| Decreased a little (+25) | 32.0 | 24.2 | 20.4 | 25.6 |
| Decreased a lot (+50) | 7.3 | 8.1 | 3.8 | 6.7 |
| N | 185 | 235 | 156 | 576 |

- Only about one-third of the public recognized a decrease and 40% said it increased. More than half of Republicans said increased and only one-fourth said decreased. Even most Democrats were wrong: fewer than 10% said "decreased a lot" (p. 281).
- Partisanship is taken from 1992, before Clinton took office, to rule out partisanship being an effect of the perceptions (fn. 15, p. 282).

**Fig. 10.2** (perceived improvement, −50 to +50, by political-information percentile; lowess curves using 30% of the data at each point, fn. 16, p. 282):
- *Least informed.* Neither reality nor partisanship structures answers. Both parties are slightly, and about equally, more likely to say the deficit increased. This may reflect murky memory of past rises or prejudice about profligate politicians (pp. 282–283).
- *Moderately informed (bottom two-thirds of information).* Partisan divergence arises entirely because moderately informed Republicans are less likely than the least informed to answer correctly. They knew a Democrat was in office and that Democrats do poorly by their standards. They inferred that Clinton was probably doing poorly on the deficit (p. 283). "A modicum of political information was enough for Republicans to figure out what ought to be true, but not to learn what was in fact true" (p. 283). Partisanship is likely to trump reality when an issue is "the least bit arcane or divorced from personal experience" (p. 283).
- *Best-informed Republicans.* Presumably they have as much stake in resisting the idea, but they are more likely to have met the objective information. There is an uptick in correct recognition, though they are still only slightly more likely to say decreased than increased (p. 283).
- *Democrats.* Well-informed Democrats, with no clash between reality and partisan hopes, were very likely to see some improvement. But "well-informed" means roughly the best-informed quarter. Democrats in the middle third were no more likely to say decreased than increased (p. 283).
- Footnote 17: on the economy-better-or-worse question, partisan biases were substantial but less dramatic than on the deficit (pp. 283–284).

**Reading the result.** The authors say the point is not that citizens are irrational. Their model gives rationality "every benefit of the doubt" and reproduces the nonlinear pattern in Fig. 10.2 very well. It predicts that moderately informed Republicans are the group most likely to be mistaken (p. 284). The problem is that most voters have little real information. Even if they "do the best they can", their beliefs are made up largely of folk wisdom and partisan supposition: "their own facts" (p. 284).

*Intuition note.* A little knowledge can make bias worse. It tells you which side a question favors, but not what the facts are. In this case, the best-informed Republicans showed an uptick toward the facts (p. 283).

### The Ramifications of a Partisan Shock: Reactions to Watergate (pp. 284–294)

- **Why a shock.** Snapshots of views at one time fit many dynamic processes. Experiments help; footnote 18 describes Gerber, Huber and Washington (2010), where a mailing to unaffiliated voters raised party identification and shifted candidate preferences, supporting "a change in partisan identity" as the cause (p. 284). Panels over months or years are limited because both partisanship and views are stable. Decades-long panels (as in chapter 9) are rare (p. 285).
- **Implication tested.** If loyalties change from an external shock, the ripples should include changes in preferences and beliefs "logically unrelated to the shock" (if Watergate was bad, "then the government should do more to help everyone get a job"). This need not be irrational: it is a logical implication of the Bayesian model, and ripples may be widest among the engaged and well-informed, who see many implications of altered loyalty (p. 285).
- **Why Watergate.** It was largely unrelated to issues of the day, and an ANES panel bracketed it: the 1972 election run-up, the 1974 aftermath of Nixon's resignation, and 1976 (p. 285).
- **Watergate scale.** Four 1974 items (pleased/displeased by the resignation; House Judiciary hearings fair/unfair; media coverage fair/unfair; resignation good/bad for the country) are added into a scale from −50 (most pro-Nixon on all four) to +50 (most anti-Nixon). Mean 20.1, SD 26.9, alpha .68 (pp. 285–286, fn. 23).
- **Variation within parties.** Strong Republicans in 1972, when the scandal was still murky, averaged 0.6 on the scale in 1974. Strong Democrats averaged 29.3. Almost one-third of 1972 strong Republicans scored below −20 and another third above +20. So scandal reactions can be separated from general partisan predispositions (p. 286).
- **Issues.** Five issues were measured in all three waves (liberal–conservative, government jobs, school busing, rights of accused, aid to minorities). Self- and party placements in all waves also let the authors estimate reliability (p. 287). Estimates come from errors-in-variables regressions using Wiley–Wiley reliabilities (fn. 29, p. 287).
- **Design.** The sample is split into the top one-third and bottom two-thirds by political information. The reasons are that fewer low-information respondents answered the issue items and more dropped out of the panel, so an even split leaves too few cases (fn. 30, p. 289).
- **Regression (added step; schematic, as the text states the three predictors).** For each issue and information group,
$$Y_{i,1976}=a+b\,W_i+c\,\mathrm{PID}_{i,1972}+d\,Y_{i,1972}+e_i ,$$
where $W_i$ is the Watergate attitude scale, $\mathrm{PID}_{i,1972}$ is 1972 party identification and $Y$ is the dependent variable. In Table 10.2, $Y$ is perceived issue proximity (−50 = closer to Democrats, +50 = closer to Republicans). In Table 10.3, $Y$ is the respondent's own issue position (p. 289; p. 290). High-information N per issue ranges from 268 to 356 (Tables 10.2–10.3, pp. 288, 292).

**Table 10.2 (perceived proximity), coefficient on Watergate attitudes (standard error), p. 288:**

| Group | Lib–cons | Gov. jobs | Busing | Rights of accused | Aid to minorities | Weighted average |
|---|---|---|---|---|---|---|
| High information | −0.153 (0.061) | −0.060 (0.079) | −0.174 (0.083) | −0.180 (0.064) | −0.080 (0.073) | −0.134 (0.070) |
| Low information | −0.032 (0.054) | −0.049 (0.057) | 0.131 (0.066) | −0.041 (0.050) | −0.004 (0.051) | −0.008 (0.055) |

- Weighted averages use precision (reciprocal of squared standard error) as weights (fn. 31, p. 289).
- **High information.** The effect is negative on every issue. Those reacting strongly to the scandal saw themselves further from the Republicans by 1976, other things equal. Nixon sympathizers saw themselves closer to them (p. 289). In three of five cases the effects are too large to be plausibly sampling error (p. 290).
- **Size.** A 35-point difference on the Watergate scale (roughly 25th to 75th percentile) implies a reduction in perceived distance from the Democrats of two to six points on each 100-point proximity scale. The average total shifts from 1972 to 1976, including measurement error, were 11–17 points (p. 290).
- **Low information.** Little evidence of change. Only busing is comparable in size, and it has the "wrong" sign. The average is almost zero (p. 290).
- Footnote 32: lagged 1972 party identification is included to allow earlier partisan predispositions to produce rationalization, though the model gives no strong reason to expect it (p. 289). Footnote 33 notes that a Watergate score of zero was relatively sympathetic to Nixon (only a fifth of respondents had negative values), which the authors cite in explaining the positive intercepts (pp. 289–290).

**Two processes (Brody and Page 1972).** Perceived proximity could change because new or more committed Democrats projected their existing preferences onto their party while viewing Republican positions more critically. Or they were persuaded to change their own positions. Table 10.3 targets the second (p. 290).

**Table 10.3 (own issue positions), coefficient on Watergate attitudes (standard error), p. 292:**

| Group | Lib–cons | Gov. jobs | Busing | Rights of accused | Aid to minorities | Weighted average |
|---|---|---|---|---|---|---|
| High information | −0.085 (0.063) | −0.228 (0.104) | −0.125 (0.064) | −0.161 (0.110) | −0.077 (0.101) | −0.122 (0.078) |
| Low information | 0.085 (0.061) | −0.040 (0.076) | −0.078 (0.055) | −0.076 (0.079) | −0.155 (0.077) | −0.044 (0.067) |

- **High information.** Those most critical of Nixon moved left on government jobs, rights of the accused and busing. Sympathizers moved right. A typical Watergate difference means two to six points in 1976 positions, against average total shifts of 12–25 points (p. 291). Footnote 34 attributes the lower stability of jobs positions to a change in the debate from McGovern's 1972 $1,000 grants to modest public-works talk in 1976 (p. 291).
- **Low information.** One sizable negative estimate (aid to minorities). The average effect is about one-third the high-information average and too imprecise to be reliable (p. 291). The authors attribute this to a lack of contextual knowledge to turn the scandal into positions on unrelated issues (p. 291).
- **Objection and check.** Reactions to Watergate correlated with education and region, which might change views for other reasons (p. 291). The analyses were rerun with age, education, income, race, region, gender, marital status, home ownership, union membership and church attendance. Results "generally confirmed" the earlier ones, somewhat less precisely (p. 293).
- **Caveat.** The data cannot rule out modest effects among the less informed (p. 293).
- **Summary.** The shock altered views on issues logically unrelated to the scandal, and the effects were concentrated in the top third by information. Those most negative on Watergate moved left and saw themselves closer to the Democrats on many issues by 1976 (p. 293). The authors suspect that if asked, these people would have offered rationalizations of the kind Rahn, Krosnick and Breuning describe (reasons that sound rational and systematic). The overlooked factor was "the essentially random partisan shock" of a Republican president's disgrace (pp. 293–294).

*Intuition note.* A scandal about a president should not change your view on school busing. It changed it for well-informed people, apparently because they link party, president and issues into one package. Less-informed people did not link them.

### Conclusion (pp. 294–296)
- Most of the time voting reaffirms identities. When voters consider new issues they often bolster commitments by constructing consistent beliefs. "They sound like they are thinking... We all do" (p. 294).
- **Proponents of the folk theory** blame such pseudo-thinking on ignorance. The authors reply that rationalization is often most powerful among the informed, whose commitments are most consistent and strongly held (p. 294).
- **Zaller (2004):** well-informed voters resist short-term forces. Less-informed voters respond more to the content of elections: they reward incumbents of strong economies, react to candidates' ideological moves and react to foreign-affairs success or failure. So sophistication dampens responsiveness to the very considerations the folk theory treats as proper bases (p. 294).
- **Lippmann (1922):** people live in a "pseudo-environment" only loosely connected to the real one. Contradiction comes only when pseudo-facts lead to action on things or people. For many, the discomfort never comes (pp. 294–295).
- Thin rationality is "a far cry" from the competence citizenry that Kuklinski and Quirk (2000) set out and criticized. Competence needs consistency and efficiency plus "some modicum of accuracy" and receptiveness to disconfirming evidence. One can be "a rational fool" (Sen 1977) (p. 295).
- **Hansen (1998), 1995 ANES pilot.** Questions were designed to allow logically inconsistent budget answers. He found very few and concluded the public has "well-formed and well-behaved preferences" and that democracy "does not want for the competence of its citizens". The authors ask how people unaware, a year later, that the deficit had more than halved could "make budget policy choices with reasonable discernment". They call Hansen's claim "hasty, if not wishful" (pp. 295–296).
- Citizens' deficit perception is mostly folk wisdom and partisan surmise with "a trace element of reality" (fn. 35 refers to Achen and Bartels 2006 for the weights) (p. 296). The authors say this psychology "may be interpreted as" remarkably efficient low-information rationality, but troubling for democracy's enthusiasts (p. 296).
- The picture "may seem shocking, cynical, implausible". It follows from the power of group loyalties, with Lowell (1913) on membership effects on judgment. In politics, the most salient groups are parties, and people adopt beliefs that rationalize partisan loyalties. Those loyalties, not beliefs, ideologies or policy commitments, are "fundamental" (p. 296).

## Toy example (ours, not from the text)
A stylized version of Brady and Sniderman's "weighted average of actual and hoped-for position" (p. 273), using the chapter's proximity measure (p. 270).

Setup: a 7-point scale. The Democratic Party's actual position is 3 and the Republican Party's is 6. Two voters both sit at 2.
- **Accurate perception.** Distance to Democrats = |2−3| = 1. Distance to Republicans = |2−6| = 4. Proximity = 1 − 4 = −3 for both voters.
- **Bias rule (our assumption).** A voter sees her own party at 0.5×actual + 0.5×own position. She sees the other party accurately.
- **Republican voter at 2.** She sees the GOP at 0.5×6 + 0.5×2 = 4, and the Democrats at 3. Proximity = |2−3| − |2−4| = 1 − 2 = −1.
- **Democratic voter at 2.** She sees the Democrats at 0.5×3 + 0.5×2 = 2.5, and the GOP at 6. Proximity = |2−2.5| − |2−6| = 0.5 − 4 = −3.5.
- **Gap.** −1 − (−3.5) = 2.5 points between two people at the same position. With no bias the gap would be 0, the test the authors use (p. 270).

## Concepts
- [[party-identification]] (new) — loyalty to a party as a political identity that organizes beliefs; here broader than the Michigan sense (pp. 267–268).
- [[partisan-perceptual-bias]] — partisans see issue positions and "objective" facts through party loyalty (pp. 272, 277–284).
- [[motivated-reasoning]] — here "rationalization": constructing reasons that bolster existing commitments (pp. 268–269, 293–294).
- [[cognitive-balancing]] (new) — reducing dissonance by assuming one's party shares one's views (p. 269).
- [[partisan-inference]] (new) — the rational reading: people use their party to guess what they do not know (p. 273).
- [[issue-proximity]] (new) — perceived distance to the Democrats minus distance to the Republicans on a 7-point issue scale (p. 270).
- [[projection-effect]] (new) — perceiving a liked group or candidate as closer to oneself than it is (pp. 275–276).
- [[folk-theory-of-democracy]] — the view that informed citizens form preferences and pick policies; the authors' target (pp. 272, 277).
- [[spatial-model-of-voting]] — voters compare their own position with perceived party positions; partisan perception undercuts it (pp. 270, 272).
- [[political-awareness]] — measured by factual knowledge; here it raises partisan bias in perceptions and ripples (pp. 279, 283, 293).
- [[heuristics-cues]] — party labels and similar shortcuts, which the authors do not take as a reason for comfort (pp. 273–276).
- [[partisan-shock]] (new) — an external event that moves partisanship and so ripples to logically unrelated views (p. 285).
- [[thin-rationality]] (new) — logical consistency and efficiency without accuracy or openness to evidence; "rational fool" (pp. 294–295).
- [[pseudo-environment]] (new) — Lippmann's term for a picture of the world loosely tied to the real one (pp. 294–295).

## Canonical instances
- [[anes-spending-services-proximity]] — Republicans and Democrats at the same position perceive different proximity (Fig. 10.1) (pp. 270–272).
- [[hart-mondale-1984-projection]] — larger projection for little-known Hart than for Mondale (p. 276).
- [[inflation-1988-beliefs]] — partisan gap in beliefs about inflation under Reagan (p. 277).
- [[iraq-wmd-beliefs]] — persistent partisan gaps in beliefs about WMD and al-Qaeda (pp. 277–278).
- [[budget-deficit-1996]] — partisan and information-dependent misperception of the deficit (Table 10.1, Fig. 10.2) (pp. 280–284).
- [[watergate-ricochet]] — Watergate attitudes shifting unrelated issue views among the well-informed (Tables 10.2–10.3) (pp. 284–293).
- [[hansen-1995-budget-preferences]] — the authors contrast consistent budget preferences with deficit ignorance (pp. 295–296).

## Bridges (candidates)
- [structural-analogy] Bayesian weighting of prior, party cue and fact by reliability ↔ canon `RAS` (Receive–Accept–Sample): opinion built from received considerations weighted by awareness and predispositions — both make awareness shape how cues are used.
- [structural-analogy] Rationalization raised by information ↔ canon `identity-protective cognition`: skill used to protect group standing — both predict more bias among the more skilled.
- [metaphor] Lippmann's pseudo-environment ↔ canon `preference falsification`: both involve gaps between professed and real bases of belief, though falsification is conscious and here it is not.

## Questions this raises
- If partisan inference is rational given uncertainty, what evidence could separate it from dissonance reduction? The authors say they do not need to separate them (p. 274).
- The Watergate result rests on a split at the top third by information (p. 289). How robust is it to other splits, given the attrition problem (fn. 30)?
- If knowledge raises bias, what could raise accuracy? Does accuracy require direct personal experience or exposure to disconfirming facts (pp. 283, 295)?
- How should the 1996 deficit result, from one question at one time, be generalized to other facts and other countries?

## Reading notes
- Page offset: the page labels give printed numbers; printed = pdf − 19.
- **Apparent inconsistency:** the text on p. 290 says own issue positions are coded −50 (most conservative) to +50 (most liberal). The Table 10.3 note (p. 292) says −50 = extreme liberal, +50 = extreme conservative. The table coding fits the text's finding that anti-Nixon respondents moved left (negative coefficients), so the text sentence appears reversed.
- On p. 271 the phrase "the 24% of these respondents" is ambiguous; I report it as the text says. The 2,803 figure is partisan identifiers at the midpoint (fn. 3).
- Fig. 10.1 and 10.2 are line graphs; I give only what the text says about them.
- Table 10.1's column headers say "1992" partisanship; the table title says 1996. The "one-third decreased / 40% increased" figures are my sums of the printed Total column (6.7 + 25.6 = 32.3; 14.8 + 25.2 = 40.0).
- In fn. 8 the .05 and .31 figures are as printed. I did not rederive them.
- Footnotes 1–35 are included only where they carry results; the chapter has no exercises.
- OCR: "fig ure" (p. 272, fn. 6), "Paul Q uirk" (p. 295), and "though" for "thought" in fn. 28 (p. 287) are visible typos.
