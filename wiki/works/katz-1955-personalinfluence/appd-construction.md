---
id: katz-1955-personalinfluence/appd-construction
work: katz-1955-personalinfluence
unit: Appendix D. On the Construction of Indices (Including a Substantive Addendum on an Index of Popular-Fiction Consumption)
pages: 369-380
fields: [communication-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# On the Construction of Indices

## L0 — One line
The authors list their indices, explain how four of them were built (latent structure, a correlation-type "importance" index, a three-question leadership index), and report that popular-fiction exposure rises with lower gregariousness and with anxiety.

## L1 — The gist (≤ 120 words)
How were the study's summary measures built, and can they be trusted? The authors list eleven indices. They explain that gregariousness and status were chosen after a latent structure analysis, which checks that items sit on one dimension. They give a formula for an "importance" index, whose values are to be used for comparison only. They describe how self-designated opinion leadership is built from three questions and report how the answers intercorrelate. A final addendum applies the gregariousness index to a new index of popular-fiction exposure. Less gregarious, more anxious and lower-status women report more exposure. The authors say the content seems to serve needs (their "uses and gratifications" approach).

**Prerequisites:** percentages and cross-tabulations; 2×2 tables; the idea of a correlation coefficient.

## L2 — Key ideas
- Eleven indices appear in the text; many combine a few questionnaire items (pp. 369–370).
- Several items can be reduced to two for grouping, but only after a latent structure analysis shows they measure one underlying dimension (pp. 371–372).
- The Importance index extends the four-fold-table correlation to tables with three or four classes. It runs from 0 to 1 but has small values, so it serves only for comparison (p. 373).
- Self-designated leadership uses two advice-giving reports and one self-rating. Agreement between the two reports is modest (about 40 per cent repeat), and the authors say advice-giving is not so continuous an activity that high consistency can be expected (p. 374).
- Self-rating differs clearly between two-time, one-time and non-advisers. The six response patterns were then collapsed into Leader and Non-Leader after the authors examined the ambiguous types 3 and 4 (pp. 376–377).
- Marketing shows somewhat lower intercorrelations than the other areas (p. 377).
- Popular-fiction exposure varies inversely with gregariousness, even with education or status held constant (pp. 378–380).
- Popular-fiction exposure varies directly with anxiety, independently of gregariousness; the authors link this to "uses and gratifications" (pp. 379–380).

## L3 — Walkthrough

### 1. Inventory of indices (pp. 369–370)
The text itself (or a footnote) explains how each index was formed, where the index is first introduced; this section simply lists them and alludes briefly to their items (p. 369). The list:
1. **Opinion Leadership (self-designated).** Either (a) an advice-giving instance in an area (marketing, fashion, public affairs, movies), reported in both June and August, or (b) one such instance plus a self-rating as "more likely" than others to be asked for advice (p. 369).
2. **Index of Effectiveness.** Ratio of "effective exposures" to a medium over its total exposures (p. 369).
3. **Life-Cycle.** Age, marital status, number of children (p. 369).
4. **Social and Economic Status.** Three alternatives: (a) rent and education; (b) breadwinner's occupation; (c) interviewer's intuitive rating (pp. 369–370).
5. **Gregariousness.** Number of friends; number of organizations (p. 370).
6. **Fashion Interest.** Views on being in style, a recent change, new dresses bought or made in the previous 3 months (p. 370).
7. **"Export" index.** Estimates out-group leadership by the deviation of a group's leadership-to-interest ratio from the whole-sample ratio (p. 370).
8. **Public Affairs Information.** Correct answers on a local highway scheme and the British elections (p. 370).
9. **Formulated Opinions.** Having an opinion, whatever its content, on 10 public-affairs questions (p. 370).
10. **"Local" and "Cosmopolitan" media behaviour.** Taking an out-of-town newspaper and reading national magazines (p. 370).
11. **Importance.** Rates the relative importance of factors for opinion leadership (p. 370).

The rent-and-education index is used most often. Where those data were missing in follow-up interviews, occupation or interviewer rating substituted (p. 370, n. 4). Interviewers rated A (best sections, top 5–10%), B (next 20%), C (moderately skilled and lower-paid white-collar) and D (poorest quarter to third) (pp. 370–371, n. 4).

### 2. Four indices discussed

**Gregariousness and social status (pp. 371–372).** The final gregariousness index used friends and organizations. The questionnaire had more indicators, such as attending afternoon social affairs and enjoying new people (p. 371). All were put through **latent structure analysis**, a procedure that tests whether the indicators express one underlying one-dimensional order (p. 371). The question is whether women who qualify on five or six indicators really may be assumed more gregarious than those who qualify on one or two (p. 371). The items did form a one-dimensional test, "similar, for example, to the traditional IQ tests" (p. 371). Once this is known, not all items are needed. Two sufficed for three groups: high (both items), low (neither), middle (the rest) (p. 371).

Status works the same way. Rent and education were kept; other items, such as a telephone, were also examined (pp. 371–372). Status can show up in many ways, and the authors compare this to a doctor who is surer of a diagnosis the more tests point to it (p. 372). Rent and education were chosen mainly because common sense links them to prestige. The *right* to treat them as indicators of one characteristic comes from the latent structure analysis, not from common sense (p. 372).

> *Intuition note.* Many signs of one hidden trait can be replaced by two signs (here, for a three-way grouping), but only after checking that all signs point to the same trait. The check, not intuition, justifies the shortcut.

**Index of Importance (pp. 372–373).** The aim is to measure how strongly characteristics (gregariousness, status, life-cycle) relate to opinion leadership (p. 372). For a four-fold table with rows $a_1,a_2$ / $b_1,b_2$, row totals $A,B$, column totals $S_1,S_2$ and grand total $N$, the usual measure is (p. 372; formula reconstructed from a garbled text layer, see Reading notes):

$$r^2=\frac{(a_1b_2-a_2b_1)^2}{A\,B\,S_1S_2}$$

"Very simple algebra" gives the same index as (p. 373):

$$r^2 = 1-\frac{\dfrac{a_1b_1}{S_1}+\dfrac{a_2b_2}{S_2}}{\dfrac{AB}{N}}$$

This form extends to leadership (absent/present) against a characteristic with three or four classes (high/middle/low, or girls/small-family wives/large-family wives/matrons). The tables then have six or eight cells (p. 373). For three classes, with $a_i$ and $b_i$ the counts of absent and present leaders in class $i$, the extension (by Mosteller) is:

$$1-\frac{\dfrac{a_1b_1}{S_1}+\dfrac{a_2b_2}{S_2}+\dfrac{a_3b_3}{S_3}}{\dfrac{AB}{N}}$$

The value is 1 if leadership is completely determined by the characteristic. It is 0 if the characteristic has no bearing (p. 373). Values are necessarily small. Equal-sized groups with leadership rates .60, .40, .20 give only .334. Small "corner" groups lower the value further. The figures should be used for comparison only (p. 373).

> *Intuition note.* The index asks how far leaders and non-leaders are spread across classes the same way. Because the values are necessarily small, the authors advise using the figures for comparison only.

**Index of (self-designated) Opinion Leadership (pp. 374–377).** Three items (the first is asked twice, giving two specific reports plus one general self-rating): (1) "Have you recently been asked your advice about…?" in June and again in August; (2) "Compared with other women in your circle… more or less likely… to be asked your advice?" (p. 374). The authors report how the replies intercorrelate. Consistency across two advice-giving reports is not like retesting a fact such as date of birth, because advice-giving is not continuous (p. 374).

Cross-tabulations (p. 375):
- Fashion: of 174 June advisers, 76 were also August advisers; 182 in August; 106 + 98 reported only one episode.
- Public affairs: 22 of 65 June advisers were also August advisers; 117 in August.
- The text says that in both areas only about 40 per cent of June influentials were influential in August (p. 374). Footnote 7 gives the public-affairs figure as 34 per cent (22 of 65) and adds that only 19 per cent of August influentials had been June influentials; public-affairs influentials almost doubled (65 to 117), while fashion stayed near 174/182 (p. 374, n. 7).
- In public affairs the August wording was changed to "asked your views on national, international or local affairs." Affirmative replies rose from 9 to 18 per cent. The authors believe both wordings pick out the same type of leader, because the self-rating correlation is as high with either (p. 375, n. 7).
- The authors do not expect high consistency in specific episodes. They say they perhaps have a right to expect women with two reports to differ from those with one, and those from women with none, in "potentiality" for influence (pp. 375–376).

Table D2 (p. 376) shows the proportion rating themselves "more likely":

| | 2-time adviser | 1-time adviser | None |
|---|---|---|---|
| Fashion | 72% (n=76) | 42% (n=204) | 17% (n=434) |
| Public affairs | 64% (n=22) | 44% (n=138) | 15% (n=555) |

The one-time advisers clearly stand in between (p. 376).

Cross-tabulating the three questions gives six types (Table D3, p. 376): (1) 2-time, "more likely"; (2) 2-time, "less likely"; (3) 1-time, more; (4) 1-time, less; (5) none, more; (6) none, less. Women who volunteered "same" were grouped with "more likely" (p. 376, n. 8). Types 1 and 6 are unambiguous. Type 2 is "modest" and joins 1. Type 5 is "boastful" and joins 6 (p. 377). Checking social and other characteristics, type 3 resembled 1 and 2, and type 4 resembled 5 and 6. So **Leader = 1, 2, 3; Non-Leader = 4, 5, 6** (p. 377).

Intercorrelations are about as high for movies. They are somewhat lower for marketing. The authors suggest that advice-giving there may be "somewhat more random," so a woman may report an episode yet not see herself as "more likely," and vice versa (p. 377).

### 3. Addendum: gregariousness, anxiety and popular fiction (pp. 377–380)
Leo Srole proposed this index and analysis (p. 377, n. 9). Items: reads "true story" magazines; reads movie magazines; listens to daytime radio serials. Score 2 for two or three, 1 for one, 0 for none (p. 377).

**Gregariousness (Table D4, p. 378).** With education held constant, less gregarious women report more exposure. For example, the share scoring 2 is 7%, 15%, 20% (high, medium, low gregariousness) at low education, and 3%, 7%, 12% at high education. Holding status (interviewers' A–D ratings) constant gives the same direction: the differences are "not spectacular but… completely consistent." Among high-status women, 36 per cent of the most gregarious versus 50 per cent of the least reported at least one item (p. 378). Education and status do not explain the inverse relation. This supports the obvious, though rarely documented, view that popular fiction media serve partly as a substitute for socializing. "Escapist" is the theorists' label (p. 378).

**Anxiety (pp. 378–380).** The authors do not know what makes women differ in gregariousness at equal status; perhaps personality does (p. 378). The anxiety items are independent of gregariousness (p. 379, n. 11).
- Table D5: women who think they worry "more" or "the same" score 2 in 13% of cases, versus 6% for "less"; score 0 in 45% versus 55% (n = 507 vs 202). The authors call this a "slight relationship" (p. 379).
- Table D6: "Are you ever blue or depressed?" Within each gregariousness level, "yes" women show more exposure (scores 2–1: 44/58/67% versus 34/44/47% for "no", from high to low gregariousness). So gregariousness and anxiety are each independently related (p. 379). The text then cites "Table D8", apparently a numbering slip for this table (p. 380).

**Summary (p. 380).**
1. Popular-fiction consumption is related to social and economic status: the authors say it "might be said" to be a majority characteristic of lower status groups and a minority pattern among upper-status people (p. 380).
2. It varies inversely with gregariousness with status held constant. The authors say this is more marked among upper-status groups, though not all data are shown.
3. It varies directly with an anxiety component, independently of gregariousness.

The content seems to serve needs tied to lower-status subculture, lower social activity and anxiety. The authors call this approach "uses and gratifications" (p. 380, n. 12).

> *Intuition note.* Fiction use is not just a matter of schooling or class. Within the same education or status, women with fewer social ties use it more; and within the same level of gregariousness, women who are sometimes blue or depressed use it more. The authors call both relations independent.

## Toy example (ours)
Three classes of 100 women each (S = 100, 100, 100; N = 300). Leaders present: 50, 30, 10, so B = 90. Absent: 50, 70, 90, so A = 210.
- Σ aᵢbᵢ/Sᵢ = 50·50/100 + 70·30/100 + 90·10/100 = 25 + 21 + 9 = 55.
- AB/N = 210·90/300 = 63.
- Ratio = 55/63 ≈ .873, so the index (1 − ratio) = 8/63 ≈ .127.

Check against the limits (added step): if leadership were the same in each class (30 each), every aᵢbᵢ/Sᵢ = 70·30/100 = 21, the sum = 63, and the index = 0. If one class contained only leaders and the other classes none, the index would be 1. The result .127 is small, as the author warns, and useful only for comparison with other characteristics.

## Concepts
- [[latent-structure-analysis]] (new) — test that several items express one underlying one-dimensional order; justifies using fewer items (p. 371)
- [[index-of-importance]] (new) — Mosteller's extension of the four-fold-table correlation to 3–4 class characteristics; 0 = no bearing, 1 = full determination, comparison only (p. 373)
- [[opinion-leader]] — here, a woman with two reported advice episodes, or one episode plus a "more likely" self-rating, in an area (p. 369)
- [[self-designated-leadership-index]] (new) — Leader = response types 1–3, built from two episode reports and one self-rating (p. 377)
- [[popular-fiction-index]] (new) — 0–2 score from true-story magazines, movie magazines, daytime serials (p. 377)
- [[uses-and-gratifications]] — audiences use media for needs; here popular fiction as, to some extent, a substitute for socializing and as linked to lower social activity and to anxiety (pp. 378, 380)

## Canonical instances
- [[fashion-advice-crosstab]] (new) — only ~40% of June fashion advisers repeat in August; self-rating separates 2-, 1- and 0-time advisers (pp. 375–376)
- [[popular-fiction-escapism]] (new) — fiction exposure rises as gregariousness falls and anxiety rises (pp. 378–380)

## Bridges (candidates)
- [structural-analogy] latent structure analysis ↔ psychometrics: items as indicators of one trait (the text compares it to IQ tests) — a one-dimensionality check before dropping items
- [same-math] Index of Importance (2×2 case only) ↔ statistics: squared phi coefficient (the text's four-fold-table formula); the 3–4 class extension is a different statistic
- [structural-analogy] popular fiction as escape ↔ uses-and-gratifications research: media consumption driven by needs

## Questions this raises
- Does the .334-style index have a sampling distribution, or is "comparison only" the whole guidance?
- Is the lower marketing intercorrelation because advice-giving there is random, or because the questions fit that area poorly?
- If anxiety and gregariousness are independent yet both raise fiction use, what personality or situation factors lie behind each?
- Is the status-versus-gregariousness difference by status level (stronger in upper status) robust?

## Reading notes
- Printed page = pdf − 26 (pdf 395 = printed 369).
- The text layer garbles the formulas on pp. 372–373. The 2×2 forms are reconstructed from the layout and checked against the stated limits (1 when fully determined, 0 when no bearing). The three-class form on p. 373 is the straightforward extension.
- Check of the p. 373 example: equal groups with leadership .60/.40/.20 give 1 − ratio = 1/9 ≈ .111. Its square root is ≈ .333, which matches the printed ".334". So the printed value may be the square root. The text layer reads "r =" for the three-class formula but "r² =" for the 2×2 forms, so the printed formula may be $r$ rather than $r^2$. I could not verify which.
- Item 10 in the inventory (p. 370) has a missing word in the text layer ("reading ___ of news in national magazines").
- Table D2 (p. 376): "Less likely" for the third fashion column is partly garbled ("Ch"); it is read as 77 by the other cell entries summing to 100. Percentages in some columns sum to 101 (rounding).
- p. 380 refers to "Table D8", but no Table D7 or D8 appears in this unit; probably D6, since the sentence concerns gregariousness and anxiety.
