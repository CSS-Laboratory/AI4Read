---
id: zaller-1992-massopinion/ch07-basic
work: zaller-1992-massopinion
unit: "7 Basic processes of 'attitude change'"
pages: 118-150
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Basic processes of "attitude change"

## L0 — One line
In the RAS model, attitude change is a two-step process, reception then acceptance, and a logistic version of that product is estimated on survey data and agrees with the predicted patterns: aware people receive more but resist more, so change can rise or peak in the middle with awareness.

## L1 — The gist (≤ 120 words)
Within the RAS model there are no fixed attitudes, only response probabilities. So "attitude change" must mean a lasting shift in the balance of considerations. Zaller asks how this change is distributed across people. His answer is Prob(Change) = Prob(Reception) × Prob(Acceptance | Reception). Reception rises with political awareness. Acceptance falls with awareness, and falls faster for people far from the message in values. The product can rise or be nonmonotonic (peaking at middle awareness), depending on message intensity and the group's values. He tests this on NES data on defense spending (1980–82) and Central America (1986–87). He then builds a logistic, maximum-likelihood version of the model.

**Prerequisites:** probability products; the logistic function and regression coefficients (slope, intercept, interaction); maximum likelihood; the RAS axioms of earlier chapters (reception, acceptance, awareness).

## L2 — Key ideas
- In RAS, "attitude change" is a permanent change in long-term response probabilities, caused by acquiring new considerations. Salience shifts that persist may be called "mood changes"; they involve no change in feelings and are not attitude change (p. 118–119).
- Change in response probability is the change in the share of considerations favouring the dominant message (Eq. 7.1). Resistance can be partisan, inertial or countervalent, and each is likely to grow with awareness (p. 120–122).
- Core model: Prob(Change) = Prob(Reception) × Prob(Acceptance | Reception) (Eq. 7.2). Reception increases with awareness. Acceptance decreases with awareness and with value distance from the message (p. 122–123).
- The model generates families of curves. Change can be positive, negative or nonmonotonic in awareness, depending on how message difficulty and resistance interact (McGuire's hard- and easy-learning cases; value groups) (p. 124–127).
- Defense-spending data conform well to the predicted patterns; Central America data fit fairly well but not perfectly. The main departure is among highly aware doves, which Zaller calls more apparent than real because the cells are small (p. 130–132).
- Statistical version: logistic reception function with a floor parameter, logistic acceptance function with predispositions. Variables inside the acceptance logistic interact automatically, and a baseline-plus-change model (Eq. 7.7) handles two-way change in cross-section data (p. 134–141).
- The model predicts conversion rates among the not-yet-converted, not absolute changes. Iran-Contra polarized hawks and doves, and net support for involvement rose (p. 146–147).
- Limits: a one-message simplification, wide standard errors, and untested claims about considerations themselves (p. 147–149).

## L3 — Walkthrough

### Opening (p. 118)
- In RAS, "attitudes" in the conventional sense do not exist; people give "survey responses" from momentarily salient considerations. Attitude change therefore cannot be a conversion from one crystallized opinion to another (p. 118).
- It must be a change in the balance of positive and negative considerations. Its RAS equivalent is a permanent alteration of long-term response probabilities. Zaller keeps the phrase "attitude change" for convenience (p. 118).
- Dynamic data let the analyst observe the shaping process directly. In Chapter 6 it had to be inferred from static distributions. This permits a more demanding test of the claim that opposing information flows shape mass attitudes (p. 118).
- Deductions in this chapter are no longer numbered (p. 118).

### Modeling attitude change (p. 118–122)
**Two routes.** If opinion has changed, the relative salience of liberal and conservative considerations must differ, and this can come about by one of only two routes (p. 119).
1. *Salience effects.* New events raise the salience of existing considerations. They involve no change in feelings about the issue, so they do not count as attitude change. Persistent ones may be called "mood changes" (p. 119).
   - Mood is hard to separate from attitude change outside a laboratory.
   - Zaller **conjectures** that presidential "rally-round-the-flag" effects may be *partially* due to mood shifts: more stress on leadership in crises.
   - Brody (1991) shows rally timing and size depend on elite support for the president, so mood is at most a partial explanation. Zaller says nothing more about mood (p. 119).
2. *New considerations.* People receive persuasive communications and accept them as considerations. This fits the definition. It is a two-step process: reception, then acceptance of some messages (p. 119).

New liberal and new conservative considerations may both form. If opinion moves conservative, all that is required is that the relative prevalence of conservative considerations has risen. Normally, if the initial balance of considerations reflects the balance of competing messages in the preceding period, this prevalence will rise if the relative intensity of the conservative message has risen (p. 119).

**Example (p. 120).** Media run 9 liberal and 1 conservative story per week, equal in prominence and credibility. They then run 8 liberal and 2 conservative. That is a gain in relative conservative intensity and moves opinion conservative (p. 120).

**Dominant vs countervailing.** The message that is more intense in the change period is *dominant*; the other is *countervailing*. Opinion may move toward the countervailing message if it gained relative intensity while staying less intense. Most often, Zaller says, change probably runs toward the dominant message (p. 120).

**Eq. 7.1.** The probability of supporting the dominant position at time 1 is $D_1/(C_1+D_1)$, where $C_1$ and $D_1$ count initial countervalent and dominant considerations. Zaller's assumptions: the person answers from the first consideration that comes to mind, and some consideration always comes to mind (p. 120, n. 1).
- Example: 3 dominant and 2 countervalent considerations give $3/(3+2)=.6$ (p. 120).
- New considerations are $D_2$ and $C_2$. Change in long-term response probability is the time-2 proportion favouring the dominant position minus the time-1 proportion (p. 120):

$$\text{Change}=\frac{D_1+D_2}{(C_1+C_2)+(D_1+D_2)}-\frac{D_1}{C_1+D_1}\tag{7.1}$$

(Layout garbled in the source; rebuilt from the author's verbal definition and the visible denominator, p. 120.)

> **Intuition note.** Attitude change here is just a change in the mix of reasons in someone's head. Adding many considerations on the same side moves the share only a little if the person already holds many.

**Three forms of resistance** to a dominant message (p. 121):
- *Partisan resistance:* people reject new dominant messages they recognize as inconsistent with their predispositions. Recognition needs contextual information from a cueing message (axioms A1–A3). This keeps $D_2$ small or zero.
- *Inertial resistance:* large stores of $C_1$ and $D_1$ swamp the effect of any internalized $D_2$.
- *Countervalent resistance:* people internalize countervalent considerations $C_2$, which offset new $D_2$.

Each is expected to rise with awareness (p. 121–122). The argument runs through liberals facing a conservative dominant message.
- More aware liberals are more likely to have the contextual information to spot and reject it (Reception Axiom), so they show more partisan resistance.
- They have the largest stock of liberal considerations from earlier exposure, so more inertial resistance.
- They are most exposed to the countervailing liberal message and likely to accept it, so more countervalent resistance (p. 121–122).

"Resistance" means resistance in *long-term response probabilities*. Highly aware people may accept some conservative messages and still not change, because of countervalent or inertial considerations (p. 122). Each form should make an independent contribution; Chapters 8–10 give the evidence (p. 122).

This chapter instead builds a **one-message model** that refers to no resistance mechanism and no countervalent message. It also serves as a "reduced form" when data on the separate mechanisms are lacking (p. 122).

### A reception-acceptance model (p. 122–124)
$$\text{Prob(Change)}=\text{Prob(Reception)}\times\text{Prob(Acceptance}\mid\text{Reception)}\tag{7.2}$$
Reception means exposure plus comprehension. Example: .5 reception × .5 acceptance = .25 (p. 122–123).

The equation drops considerations and countervalent messages, but can be filled out to accommodate them implicitly. Reception increases with awareness. Acceptance falls as awareness and ideological distance from the message jointly increase. Awareness stands in for three hard-to-observe resistance mechanisms (p. 123).

**Hypothetical table (p. 123).**

| | Low | Middle | High |
|---|---|---|---|
| Prob(Reception) | .10 | .50 | .90 |
| Prob(Accept∣Reception) | .90 | .50 | .10 |
| Change | .09 | .25 | .09 |

Hence the awareness–change relation *may* be nonmonotonic. Zaller says such patterns recur in opinion data, but that nonmonotonic change is only one special case among many (p. 124).

> **Intuition note.** Low-awareness people rarely hear the message. High-awareness people hear it but argue back. People in the middle both hear it and lack the defences, so they move most.

### Patterns of attitude change (p. 124–128)
**McGuire (1968, 1969)** first proposed a reception-acceptance model of this form. He noted that self-esteem, intelligence and freedom from anxiety show nonmonotonic relations to persuasion in laboratory studies. He suggested these traits relate positively to reception but negatively to acceptance ("yielding") (p. 124–125). The relation to change can then be positive, negative or nonmonotonic.

- **Hard learning** (message difficult to receive, e.g., a physics lecture). Acceptance is 1.0 for all; reception rises with intelligence (.10, .20, .30), so change = .10, .20, .30. Some political messages are so weak or hard that only the most aware receive them; then the most aware change most (p. 125).
- **Easy learning** (message so simple everyone receives it, e.g., "Your head is moving back and forth"). Reception is 1.0 for all; acceptance falls with intelligence (.90, .50, .10), so change = .90, .50, .10 (p. 125–126).

A trait positively tied to reception and negatively to uncritical acceptance can therefore relate to change positively, negatively or nonmonotonically. Which it is depends on whether the situation stresses reception capacity, willingness to accept, or both (p. 126). Awareness behaves like such a trait. Message intensity varies continuously, so *families* of curves arise (p. 126). Zaller adds a factor McGuire did not consider: the fit between the audience's partisanship and the source's (p. 126).

**Liberal message, three ideological groups (p. 127).** Reception is the same in all groups: .10, .50, .90 at low, middle and high awareness.

| | Low | Middle | High |
|---|---|---|---|
| Liberals: acceptance | .90 | .85 | .80 |
| Liberals: change | .09 | .425 | .72 |
| Centrists: acceptance | .90 | .55 | .20 |
| Centrists: change | .09 | .275 | .18 |
| Conservatives: acceptance | .90 | .46 | .02 |
| Conservatives: change | .09 | .23 | .018 |

Change rises with awareness among liberals. It is nonmonotonic among centrists and conservatives (p. 127). Zaller's account:
- Low-awareness centrists and conservatives rarely receive the message (10 percent).
- High-awareness ones receive it (90 percent) but accept rarely (2 and 20 percent).
- Moderately aware ones pay enough attention to be likely to receive it but are not aware enough to be able to reject it as inconsistent with their values (p. 127).

**Does awareness reduce acceptance even of congenial messages?** Zaller's answer is empirical. When the model allows for it, there turns out always to be a negative awareness–acceptance relation, even if slight; Zaller adds that it "seems always" to be negative (p. 127–128).
- This suggests, "perhaps for reasons of inertial resistance", that more aware people are always somewhat more resistant, given reception.
- There is no tendency for awareness to interact with ideology so as to give a positive slope for one group and a negative one for the other. Except in Tables 7.3 and 9.1, he does not report these tests (p. 128, n. 4).

### Initial tests (p. 128–132)
**Defense spending, 1980 and 1982 NES.**
- The question was a seven-point scale from greatly reduced to greatly increased spending. Positions 1–3 are collapsed into "favour cuts" (p. 128–129, n. 8).
- Newsweek coverage (Chapter 2) favoured cuts over increases by about 2 to 1. Support for cuts rose from 10 to 28 percent (p. 128).

**Central America, fall 1986 and June 1987.**
- Iran-Contra broke as the 1986 survey went into the field, and the Senate hearings were under way at the June reinterview. It increased publicity for Reagan's Central America policy.
- Support for greater involvement (positions 5–7) rose from 28 to 38 percent (p. 128–129).
- The analysis uses the 360 of 457 June reinterviewees who also agreed to an August interview, which carried the Hurwitz–Peffley militarism items (p. 129, n. 7).

**Predicted patterns (p. 129).**
- For a liberal message (defense): liberals show a positive awareness–change relation; conservatives are nonmonotonic.
- For a conservative message (Central America): the expectations reverse, with a positive relation among conservatives and a nonmonotonic one among liberals.
- Awareness is measured by neutral political knowledge. Values are measured by party attachment (defense) and by the Hurwitz–Peffley items (Central America) (p. 129).

**Change rate** $=(\text{Opinion}_{82}-\text{Opinion}_{80})/(100-\text{Opinion}_{80})$, the share of those not initially favouring cuts who switched. Example: highly aware Democrats, $(57-20)/(100-20)=46\%$ (p. 130).

**Table 7.1 (percent favouring cuts; awareness low → high; p. 130).**

| | 1980 | 1982 | Change rate |
|---|---|---|---|
| Democrats | 12, 11, 12, 20 | 16, 36, 41, 57 | 4, 28, 33, 46 |
| Republicans | 8, 12, 3, 4 | 10, 23, 29, 14 | 2, 13, 27, 10 |

Democrats show a rising pattern. Republicans show a nonmonotonic one (2, 13, 27, then 10), "as expected". The results "conform well to theory" (p. 130–131).

**Table 7.2 (percent favouring more involvement; p. 131).**

| | 1986 | 1987 | Change rate | N |
|---|---|---|---|---|
| Hawks | 22, 30, 43, 60 | 33, 48, 50, 80 | 14, 26, 12, 50 | 18, 40, 44, 15 |
| Centrists | 17, 8, 18, 21 | 23, 30, 38, 21 | 7, 24, 24, 0 | 30, 37, 40, 14 |
| Doves | 20, 10, 8, 8 | 20, 10, 18, 19 | 0, 0, 11, 12 | 15, 31, 50, 26 |

Zaller reads hawks as a positive relation and centrists as sharply nonmonotonic (p. 131). Doves were much less responsive. But the few doves who moved were very highly aware, not moderately aware (p. 132). Zaller calls this deviation "more apparent than real" (p. 132):
- Small cells: two different responses in the high-awareness doves cell would drop the rate to .04.
- One predispositional variable only; other predispositions may need controlling.
- Footnote: for p = .20 and n = 25, the standard error of a difference of means is 0.11 (p. 132, n. 9).

Tables cannot supply controls or tests, so a statistical model is needed (p. 132).

### A statistical model of attitude change (p. 132–147)
**Why functional form matters (p. 132–134).** Knowing that two variables are positively related is not enough. Figure 7.1 shows the chance of answering "square root of 4" correctly against years of school under three forms: linear, exponential and logistic. Because square roots are taught in grades 3–8, the logistic form is the plausible one (p. 133–134).

**Reception function.** Reception is a probability, and a logistic stays between 0 and 1. Diffusion studies often find logistic fits (Price, 1961; Neuman, 1990). By analogy with test theory (normal ogive ≈ logistic), reception of a message is a "test" passed more by the highly aware (p. 134, n. 10).

$$\text{Prob(Reception)}_i=1-\left[\frac{1}{1+f+e^{(a_0+a_1\text{Awareness}_i)}}\right]\tag{7.3}$$
equivalently $1-[1+f+\exp(a_0+a_1\text{Awareness}_i)]^{-1}$ (7.3′, p. 135). Here $a_0$ is message intensity, $a_1$ is the strength of the awareness–reception link, and $f$ is a floor parameter (p. 134).

*Parameters (p. 135–137).*
- $a_1$ is the analogue of a regression slope. Figure 7.2a plots $a_1=.5, 1.0, 2.0$. Awareness is in standard units, and about 96 percent of people fall within ±2 (Zaller's figure). With $a_1=1.0$ and $a_0$ near zero, reception rises from about 10 to 90 percent across the range.
- $a_0$ is the analogue of an intercept: message "loudness". Higher $a_0$ means higher reception at any awareness level (Fig. 7.2b). Coefficients can be compared across models "if appropriate care is taken".
- $f>0$ sets a minimum reception regardless of awareness (Fig. 7.2c, $f=.30$). It handles guessers, who answer without receiving anything. It is a "nuisance term", matters only at low awareness, and has no substantive significance (p. 135–137). (added step: as awareness becomes very low, $e^{a_0+a_1\text{Awareness}}\to0$ and reception tends to $f/(1+f)$.)

**Acceptance function.**
$$\text{Prob(Accept}\mid\text{Reception)}_i=[1+\exp(-b_0-b_1\text{Awareness}_i-b_2\text{Predispositions}_i\ldots)]^{-1}\tag{7.4}$$
- $b_0$ is the difficulty or credibility of the message. $b_1$ is the awareness effect on resistance, and $b_2$ is the predispositions effect (p. 137).
- The signs are arranged so that the awareness coefficient is negative when awareness lowers acceptance. Earlier work used the opposite sign convention (p. 137, n. 14).
- Variables in a logistic interact automatically, so the effect of awareness depends on predispositions. The interaction must be allowed for because RAS holds that predispositions have no effect unless the person is aware enough to hold the contextual information (p. 137).
- Evidence for the interaction: unaware Democrats and Republicans differed little (4 and 2 percent less favourable to defense spending), while aware ones differed a lot (46 and 10 percent). The same happened for hawks and doves (p. 138).
- **Fig. 7.3** uses $b_0=2$, $b_1=-1$, $b_2=-1$, party scored −2 for Republicans and +2 for Democrats. Acceptance falls with awareness for both, but much more steeply for Democrats. Zaller says this interaction would occur only when the change-inducing message is conservative; for a liberal message the sign of $b_2$ would reverse, so awareness would affect Republicans' acceptance more (p. 138).
- No explicit Awareness × Predispositions term is entered. Such terms usually add little fit and much multicollinearity, and Eq. 7.4 normally picks up the interaction (Table 7.3). One case in Chapter 9 did use them (p. 138).
- Readers are encouraged to replicate Figures 7.2–7.3 on a spreadsheet (p. 139).

**Combined model (Eq. 7.5, p. 139).**
$$\text{Prob(Change)}=\Big(1-\big(1+f+\exp[a_0+a_1\text{Awareness}]\big)^{-1}\Big)\times\Big(1+\exp[-b_0-b_1\text{Awareness}-b_2\text{Predispositions}\ldots]\Big)^{-1}\tag{7.5}$$
The first factor increases with awareness and the second decreases with awareness and value distance (p. 139).

> **Intuition note.** Two S-shaped curves are multiplied: one going up with awareness (hearing it) and one going down (believing it). Their product can peak in the middle. Values only enter the second curve.

**No selective reception.** Predispositions appear only in acceptance, so reception is assumed independent of them. This is inappropriate if people practised "selective reception" (early opinion research). More recent research has been "unkind" to that notion (p. 139). To the extent selective exposure occurs at all, it appears to do so under special conditions that do not typically arise in mass persuasion (p. 139). Zaller's reasons (p. 139–140):
- Most people use many outlets that are common carriers of a national flow (Key, 1961).
- Selective reception requires more vigilance than apathetic citizens give.
- Major continuing stories (Vietnam, Iran-Contra) are hard to miss for anyone paying some attention.

Selective reception "cannot be entirely false" (liberals and *National Review*). Evidence does not suggest it is broad enough to affect the diffusion of major ideas (p. 140).
- n. 15: the one rigorous nonlaboratory case (Cotton, 1985) is new-car buyers reading ads. Price and Zaller (1990) found small-to-nonexistent effects, but large ones in two minor stories (p. 139).
- n. 16: predispositions cannot be put in both functions to test this, because Eq. 7.5 would not be identified (complete collinearity) (p. 140).

**Three limits of Eq. 7.5 (p. 140).**
1. The defense data are separate cross-sections, not the same people, so individual-level change rates cannot be computed.
2. It permits change only toward the dominant message. In Central America, 22 percent moved in the hawkish direction and 12 percent in the dovish, a net 10 points (28 to 38 percent). This reflects random response variability (Table 2.1). Eq. 7.5 would imply 10 percent changed and 90 percent stayed.
3. Modelling only change rates throws away the baseline and final opinion distributions.

**Baseline-plus-change model (p. 141).**
$$\text{Prob(Opinion}_2)=\text{Prob(Baseline Opinion)}+\text{Prob(Change)}\,(1-\text{Baseline Opinion})\tag{7.6}$$
Opinion at time 2 is baseline opinion plus conversion of those not already holding the opinion. Baseline and change are each reception-acceptance models of the form of Eq. 7.5, estimated together on stacked data:
$$\text{Prob(Opinion)}_t=\text{Prob(Baseline)}+\text{Dum}_t\cdot\text{Prob(Change)}\,(1-\text{Baseline})\tag{7.7}$$
Here $\text{Dum}_t=0$ at time 1 and 1 at time 2. The floor $f$ is only in the baseline reception function, since guessing is absorbed there (p. 141).
- The dependent variable is 0–1 (supports cuts vs all others including no opinion). This throws away scale information. But dropping no-opinion respondents would bias the estimated awareness effect on reception, and 0–1 keeps the "percent supporting" metric (p. 141, n. 17).

**Defense results (Table 7.3, p. 142; Time 1 N = 1602, Time 2 N = 1402; maximum-likelihood estimates, standard errors in parentheses).**

| Coefficient | No constraints | One constraint |
|---|---|---|
| Baseline reception: $a_0$ | −4.18 | −3.51 |
| Baseline reception: awareness | 1.24 (.82) | 0.96 (.66) |
| Baseline reception: $f$ | 0.10 (.03) | 0.10 (.03) |
| Baseline acceptance: $b_0$ | 6.56 | 1.96 |
| Baseline acceptance: awareness | −0.59 (.49) | −0.41 (.40) |
| Baseline acceptance: party | 6.12 (6.96) | 2.03 (.46) |
| Change reception: $a_0$ | −1.07 | −1.16 |
| Change reception: awareness | 1.03 (.19) | 0.91 (.14) |
| Change acceptance: $b_0$ | 2.37 | 3.70 |
| Change acceptance: awareness | −1.39 (0.53) | −1.65 (.64) |
| Change acceptance: party | 1.23 (.37) | 2.03 (.46) |
| Residual sum of squares | 538.23 | 538.97 |

A third column adds Party × Awareness terms (baseline −1.65, SE 2.52; change −0.52, SE 0.57). These did not significantly improve fit (p. 142–143).
- Magnitudes and signs are as expected. The baseline acceptance coefficients are imprecise because there is little variance in 1980 support.
- Constraining the party coefficient (the most unstable) to be equal in baseline and change reduced fit significantly, $F(1,2993)=4.12$, $p<.05$. It left the qualitative fit to Table 7.1 unaffected (p. 143).

**Fig. 7.4 (unconstrained estimates; z-scores for awareness from −1.86 to +1.96, about the 1st to 98th percentile).**
- Reception rises with awareness (p. 144, n. 18).
- Acceptance falls strongly with awareness for Republicans and "barely" for Democrats.
- For a hypothetical Republican and Democrat somewhat above median awareness, reception is .52 for both. Acceptance is .30 for the Republican and .94 for the Democrat. The Republican's change rate is $.52\times.30=.15$. The Democrat's is labelled .49 (p. 143–144).
- These estimates agree well with Table 7.1 (p. 144).

**Central America (Table 7.4, p. 145; N = 360 at each time).** Sample size is smaller, so estimates are less precise: of six substantive coefficients, only two are significant. The awareness coefficients are constrained to be equal across baseline and change models. This brings them to $p<.05$ without a significant fit loss, $F(2,707)=.43$, n.s. (p. 144).

| Coefficient | No constraints | Two constraints |
|---|---|---|
| Baseline reception: $a_0$ | −1.15 | −1.27 |
| Baseline reception: awareness | 2.52 (1.69) | 2.13 (1.20) |
| Baseline reception: $f$ | 0.37 (.17) | 0.35 (.16) |
| Baseline acceptance: $b_0$ | −0.33 | −0.19 |
| Baseline acceptance: awareness | −0.76 (.42) | −0.80 (.37) |
| Baseline acceptance: hawk-dove | −1.38 (.43) | −1.42 (.46) |
| Baseline acceptance: Reagan disapproval | −0.30 (.19) | −0.33 (.20) |
| Change reception: $a_0$ | −1.40 | −0.60 |
| Change reception: awareness | 1.17 (1.16) | 2.13 (1.20) |
| Change acceptance: $b_0$ | 1.50 | −0.10 |
| Change acceptance: awareness | −1.39 (1.56) | −0.80 (.37) |
| Change acceptance: hawk-dove | −0.66 (.93) | −0.52 (.47) |
| Change acceptance: Reagan disapproval | −0.29 (.47) | −0.14 (.28) |
| Residual sum of squares | 155.99 | 156.18 |

Hawk-dove (standardized) and Reagan disapproval (−2 to +2) have about the same range. Hawk-dove looks about four times as important as Reagan approval. So it was people with hawkish values, not Reagan supporters per se, who rallied (p. 145–146). Hawk-dove remains dominant if party replaces Reagan approval (p. 145, n. 19).

**Fig. 7.5 (change rates, unconstrained).** The patterns are highly similar to the defense case. Hawks rise with awareness, and centrists and doves are low and flatter. Here the left-wing group resists. In the defense case the right-wing group resisted more. The model works when opinion swings right as well as left (p. 146).

**Fig. 7.6 (levels of support before and after).**
- Most aware hawks go from .79 to .89, a 10-point rise, which is a conversion rate $10/(100-79)=10/21=48\%$.
- Hawks just below median awareness go from .35 to .46, an 11-point rise, which is $11/(100-35)=17\%$ (p. 146–147).
- The model deals in conversion *rates among the unconverted*, not absolute change within subgroups (p. 147).
- Iran-Contra polarized hawks and doves. Net support for involvement rose because the public began so one-sidedly opposed that polarization meant gains for the pro-involvement side (p. 147).

**Caveat.** Wide confidence intervals worry Zaller (taken up in Chapter 11). He gives two reasons: multicollinearity, since awareness enters four times, and dependence of some coefficients on a small group of highly aware, predisposed-to-resist respondents. He says neither is a problem with the model itself (p. 147).

### Concluding remarks (p. 148–149)
- Main point: attitude change is a two-step process of reception and acceptance. Reception rises with awareness. Acceptance is lower for the aware, especially when value distance is great. For Democrats facing the anti-defense message, awareness has little effect on resistance; for Republicans it has a strong effect (p. 148).
- Still to come: effects of message intensity (saturating versus reaching only the aware); issue familiarity (many existing considerations mean more inertial resistance and altered patterns); direct evidence at the level of considerations; and two-sided information flows (p. 148–149).
- The one-sided assumption is "entirely implausible" for Central America amid Iran-Contra. It is less extreme for defense, where the Reagan administration still supplied countervalent information (p. 148–149).

### Appendix: maximum-likelihood estimation (p. 149–150)
Eq. 7.7 is $\text{Prob}(y=1)=f(X,\beta)$, with $y$ a 0–1 variable. With $D1=1$ if $y=1$ and $D2=1$ if $y=0$ (p. 149):
$$L=\prod D1\cdot f(X,\beta)\times\prod D2\cdot(1-f(X,\beta))$$
$$\text{Log}(L)=\sum D1\cdot\log f(X,\beta)+\sum D2\cdot\log[1-f(X,\beta)]$$
Since $0<f<1$, each log is negative, so
$$-\text{Log}(L)=\Big(\sqrt{-\textstyle\sum D1\log f-\sum D2\log(1-f)}\Big)^2.$$
Nonlinear regression minimizes squared residuals, so estimating
$$0=\sqrt{-D1\cdot\log[f(X,\beta)]-D2\cdot\log[1-f(X,\beta)]}\tag{7.8}$$
minimizes $-\text{Log}(L)$, which maximizes $\text{Log}(L)$. Zaller credits this unpublished algorithm to Doug Rivers (p. 149).
- Data from both periods are stacked with a 0–1 year dummy. A SAS PROC NLIN program (for the defense data) defines T1 and T2 (the baseline and change products), $P1=T1+\text{YEAR}\cdot T2\cdot(1-T1)$, and the model above (p. 149–150).
- The simpler "MODEL DEFSPN = P1" gives unbiased, consistent but inefficient estimates, with wrong standard errors because of heteroskedasticity from the 0–1 variable (p. 150).
- n. 21 (starting values, p. 150):
  1. Confirm clear nonmonotonicities in a Table 7.1-style layout.
  2. Keep only the essential variables.
  3. Fix awareness in reception, and awareness plus one predisposition in acceptance, at plausible values (+1, −1, −.4 for standardized variables).
  4. Estimate the baseline first, then loosen constraints.
- A spreadsheet fit is an alternative. Zaller suspects many researchers will need to learn to manipulate the model on a spreadsheet first (p. 150).

## Toy example (ours, not from the text)
Take Eq. 7.3 with $f=0$, $a_0=0$, $a_1=1$. Take Eq. 7.4 with $b_0=0$, $b_1=-1$ and no predispositions. Use awareness $A=-2,0,+2$.

- Reception $=e^{A}/(1+e^{A})$:
  - $A=-2$: $e^{-2}=.1353$, so $.1353/1.1353=.119$.
  - $A=0$: $1/2=.500$.
  - $A=+2$: $e^{2}=7.389$, so $7.389/8.389=.881$.
- Acceptance $=1/(1+e^{A})$ (because $b_1=-1$ gives $-b_1A=+A$, so $\exp(-b_0-b_1A)=\exp(A)$):
  - $A=-2$: $1/1.1353=.881$.
  - $A=0$: $.500$.
  - $A=+2$: $1/8.389=.119$.
- Change = reception × acceptance:
  - $A=-2$: $.119\times.881=.105$.
  - $A=0$: $.5\times.5=.250$.
  - $A=+2$: $.881\times.119=.105$.

Change peaks in the middle at .25, a nonmonotonic pattern.

Using Eq. 7.6 for the middle group: if baseline support is .10 and Prob(Change) = .25, then Opinion$_2=.10+.25\times(1-.10)=.10+.225=.325$.

## Concepts
- [[receive-accept-sample-ras-model]] — opinion as sample of received and accepted considerations. Here, attitude change means a permanent change in response probabilities (p. 118)
- [[reception-acceptance-model]] (new) — Prob(Change) = Prob(Reception) × Prob(Acceptance∣Reception), the model of attitude change first proposed by McGuire (p. 122, 124)
- [[political-awareness-sophistication]] — raises reception and lowers acceptance of uncongenial messages (p. 123)
- [[mood-change]] (new) — persisting salience shift with no change in feelings, not counted as attitude change (p. 119)
- [[dominant-countervailing-messages]] (new) — the more vs less intense message in the change period (p. 120)
- [[partisan-resistance]] (new) — rejecting messages seen as inconsistent with predispositions (p. 121)
- [[inertial-resistance]] (new) — new considerations swamped by a large store of old ones (p. 121)
- [[countervalent-resistance]] (new) — new countervalent considerations offsetting dominant ones (p. 121)
- [[nonmonotonic-attitude-change]] (new) — change peaking at middle awareness, which the model implies can arise when reception rises and acceptance falls with awareness (p. 124)
- [[hard-vs-easy-learning]] (new) — McGuire's cases where reception, or acceptance, is the bottleneck (p. 125–126)
- [[logistic-reception-function]] (new) — Eq. 7.3 with intensity $a_0$, slope $a_1$ and floor $f$ (p. 134–135)
- [[conversion-rate]] (new) — change among those not already holding the opinion (p. 130, 147)
- [[selective-exposure-media-choice]] — Zaller's "selective reception". He judges that, on the available evidence, it apparently does not occur broadly enough to affect the diffusion of major ideas (p. 139–140)
- [[heuristics-cues]] — contextual information from cueing messages enables resisting uncongenial messages (p. 121)

## Canonical instances
- [[defense-spending-1980-82]] — liberal-direction change (10→28% favouring cuts); Table 7.1 (p. 128, 130)
- [[central-america-iran-contra-1986-87]] — conservative-direction change (28→38%); polarization of hawks and doves (p. 128–129, 147)
- [[mcguire-hard-easy-learning]] — physics lecture and "head moving" examples (p. 125–126)
- [[rally-round-the-flag]] — conjectured partly mood effect (p. 119)

## Bridges (candidates)
- [structural-analogy] reception × acceptance with a rising and a falling logistic ↔ epidemiology/diffusion: exposure × susceptibility giving a middle-heavy infection pattern — the product of an increasing and a decreasing function peaks in the middle.
- [same-math] logistic reception function with floor $f$ ↔ psychometrics: item-response curves with a guessing parameter (Lord & Novick, cited p. 134, 135, n. 12) — the same functional family.
- [same-math] stacked-data maximum likelihood via nonlinear regression (Eq. 7.8) ↔ statistics: Bernoulli log-likelihood estimation — the same likelihood function.
- [structural-analogy] conversion rates among the unconverted ↔ survival or hazard analysis: change defined among those still "at risk".

## Questions this raises
- If acceptance always falls somewhat with awareness even for congenial messages, how large is that effect when countervalent messages are modelled explicitly?
- How could one separate partisan, inertial and countervalent resistance empirically? (The text promises this in Chapters 8–10.)
- With wide standard errors from four awareness terms, which parameters are really identified?
- What changes when the dominant message is not the only one, as Zaller concedes in the Central America case?

## Reading notes
- Printed page = pdf − 16. Page images were available only for pdf 145–166 (printed 129–150). For pdf 134–144 (printed 118–128) I worked from the text layer only.
- Eq. 7.1 (p. 120) is garbled in the text layer and has no image. I rebuilt it from the author's verbal definition and the visible denominator. The garbled layer also gives the time-1 probability only as "C₁ + D₁", but the example 3/(3+2) fixes the numerator.
- The text gives the natural-log base as "2.7214" (p. 134); this is a misprint for 2.71828….
- The text says Eq. 7.3's $f$ sets the floor. By my added step the floor is $f/(1+f)$.
- The SAS code (p. 150) uses LOG10, while the text equations use "log". A trailing "*" after the T2 line looks like a misprint. The text layer prints "PROC NUN"; the image shows NLIN.
- The text says $b_0$ is "+2" in Fig. 7.3's discussion; the caption also gives $b_0=2$. They agree.
- The Table 7.1 and 7.2 column headers show only "Low … High"; the four columns are low, two middle categories, high.
- The text's hawks claim ("positive relationship") is made although the hawk change rates 14, 26, 12, 50 dip in the third category.
- The text reads "Tables 7.1. and 7.2" and "Reagan fall disapproval" in Table 7.4; these are the author's wording as printed.
