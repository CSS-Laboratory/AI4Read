---
id: vosoughi-2018-spread/main
work: vosoughi-2018-spread
unit: paper
pages: 1146–1151
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
# The spread of true and false news online

## L0 — One line
On Twitter (2006–2017), fact-checked false news spread farther, faster, deeper and more broadly than true news, and the authors conclude that humans, not bots, are more likely to spread falsehood; spreader characteristics did not explain it, and novelty and emotional reactions are offered as possible contributors, not proven causes.

## L1 — The gist (≤ 120 words)
The paper asks how true and false news differ in their spread, and why. It uses about 126,000 rumor cascades on Twitter, verified by six fact-checking organizations. False news travelled farther, faster, deeper and more broadly than true news in all categories, most strongly in politics. Spreaders of falsehood had fewer followers and were less established, so network position does not explain the gap. False rumors were more novel, and replies to them showed more surprise and disgust. Bots accelerated true and false news roughly equally, so the authors conclude that human behavior contributes more to the difference. Their policy implication is to add behavioral interventions to bot-focused measures.

**Prerequisites:** distributions and the CCDF; logistic regression and odds ratios; probability distributions over topics (the idea of "distance" between them); the idea of a retweet tree.

## L2 — Key ideas (5–10 bullets)
- Terms are defined by verifiability, not source: "true"/"false" news, not "fake news"; no claims about intent (p. 1146).
- Unit of analysis is the rumor cascade, an unbroken retweet chain with one origin, measured by depth (retweet hops), size (users involved), max breadth (most users at one depth) and structural virality (how far spread is multi-generation rather than one broadcast) (pp. 1146–1147).
- Falsehood beat truth on every diffusion measure, in all categories; false political news was strongest (pp. 1147–1148).
- User and network traits go the "wrong" way: false-news spreaders had fewer followers and less tenure, yet falsehoods were about 70% more likely to be retweeted (p. 1149).
- Novelty hypothesis: false rumors were more novel than what users had recently seen, and reply emotions differed (more surprise and disgust for falsehood). The authors do not claim novelty is the only cause (pp. 1149–1150).
- Robustness checks: rumor-clustered errors, an independent student-verified sample, and bot removal or inclusion all left conclusions unchanged (p. 1150).
- Conclusion: humans, not robots, are more likely to spread falsehood, so containment should include behavioral interventions (p. 1150).

## L3 — Walkthrough
The paper has no numbered sections; headings below follow its order.

### Motivation and prior work (p. 1146)
- Theories of decision-making, cooperation, communication and markets treat truth or accuracy as central. Yet true and false information both spread rapidly online. Example: a false tweet that Barack Obama was injured in an explosion wiped out $130 billion in stock value (p. 1146).
- Existing studies are small and ad hoc. They ignore two questions: how do truth and falsity diffuse differently, and which human-judgment factors explain it (p. 1146).
- Earlier work studied single rumors (Higgs boson, Haiti earthquake), rumors from one event (Boston Marathon), models, detection, credibility, or interventions. Del Vicario et al. and Bessi et al. studied scientific and conspiracy stories but not veracity. Friggeri et al. (~4000 Facebook rumors) is the only prior study splitting by veracity (p. 1146).
- Note 22 (p. 1151): Friggeri et al. find little depth difference and more shares per rumor for true rumors. The authors call this not definitive: small sample, early timing (misses the post-2013 rise), and shares per rumor do not necessarily mean deeper, broader or faster spread.

### Terminology (p. 1146)
- The authors avoid "fake news". They think it is now "irredeemably polarized" because politicians label opposing sources fake, so it no longer tracks veracity (p. 1146).
- They make no claims about the intent of those who spread information, and they define news broadly: any asserted claim on Twitter counts, not only claims from institutional news sources (p. 1146).
- **News** = any story or claim with an assertion in it, whether shared or not. **Rumor** = the social phenomenon of news spreading through the Twitter network (p. 1146).
- **Cascade** = an instance of a rumor-spreading pattern with an unbroken retweet chain and one common origin. Size one means nobody retweeted (p. 1146).
- Number of cascades of a rumor = number of independent (non-retweet) tweets of it. Example A: tweeted separately by 10 people, never retweeted → 10 cascades of size one. Example B: tweeted independently by 2 people, each retweeted 100 times → two cascades of size 100 (p. 1146).

### Data and measures (pp. 1146–1147)
- Sources: snopes.com, politifact.com, factcheck.org, truthorfiction.com, hoax-slayer.com, urbanlegends.about.com. Their verdicts agreed 95–98% of the time (pp. 1146–1147).
- Procedure: parse title, body and verdict (true, false, mixed). Collect English replies (2006–2017) to tweets linking to these sites, with OCR for images. For each reply, extract the original tweet and all its retweets. Each retweet cascade is one verified rumor cascade (p. 1147).
- Result: ~126,000 cascades, ~3 million people, >4.5 million tweets (p. 1146).
- Four measures: **depth** (retweet hops from origin, a hop being a retweet by a new unique user); **size** (users involved); **maximum breadth** (most users at any single depth); **structural virality** (interpolates between one big broadcast and multi-generation spread, no single person responsible for much of it) (p. 1147).
- Descriptives (Fig. 1): a greater fraction of false rumors had 1–1000 cascades; a greater fraction of true rumors had more than 1000 (also for political rumors). False rumors peaked at the end of 2013, 2015 and 2016. False political rumors rose around the 2012 and 2016 elections. Mixed rumors spiked at the 2014 Crimea annexation. Politics was the largest category (~45,000 cascades), then urban legends, business, terrorism, science, entertainment, natural disasters (p. 1147).

### Result 1: falsehood diffuses more than truth (pp. 1147–1148)
- Falsehood was farther, faster, deeper and broader in all categories (K-S tests in tables S3–S10, not in these pages) (p. 1147).
- Depth: more false than true cascades passed depth 10. The top 0.01% of false cascades went eight hops deeper than the truth, beyond 19 hops (p. 1147–1148).
- Reach: the truth rarely reached more than 1000 people; the top 1% of false cascades routinely reached 1000–100,000. Falsehood reached more people at every depth, and its spread was aided by virality, meaning peer-to-peer branching, not simple broadcast (p. 1148).
- Speed: truth needed about six times as long as falsehood to reach 1500 people, and 20 times as long to reach depth 10. Since truth never passed depth 10, falsehood reached depth 19 nearly 10 times faster than truth reached depth 10 (p. 1148).
- Breadth: falsehood was broader and retweeted by more unique users at every depth (p. 1148).

*Intuition note:* Compare the same kind of tree for true and false claims. False trees are bigger, branch more, grow deeper and grow quicker. The difference appears at every level of the tree, not only in a few big cases.

### Result 2: false political news (p. 1148)
- False political news was deeper, broader, larger and more viral than any other false category. It reached 20,000+ people nearly three times faster than other false types reached 10,000 (p. 1148).
- Other false categories were slightly broader at shallow depths, but political news was broader at depths above 10. This suggests more-popular false political items have broader, more accelerated dynamics (pp. 1148–1149).
- Across all categories, politics, urban legends and science reached the most people. Politics and urban legends were fastest and most viral (fig. S11, not shown) (p. 1149).

### Do user or network traits explain it? (p. 1149)
- One might suspect spreaders of falsity had more followers, followed more people, tweeted more, were verified more often, or were on Twitter longer. The authors find "the opposite … in every case" (p. 1149).
- Users spreading false news had fewer followers (K-S 0.104), followed fewer people (0.136), were less active (0.054), were verified less often (0.004 in text; 0.005 in Fig. 4A) and had less time on Twitter (0.125); all P ≈ 0.0 except verification, P < 0.001 (p. 1149).
- Falsehood therefore spread "despite these differences, not because of them" (p. 1149).
- A logistic model of retweeting: falsehoods were 70% more likely to be retweeted (Wald chi-square, P ≈ 0.0), controlling for the original tweeter's account age, activity, followers, followees and verified status (p. 1149). Fig. 4B gives coefficient 0.5350 and odds ratio 1.707489. (added step) Check: $e^{0.5350}\approx 1.7074$ (equal to the table value up to rounding of the coefficient).

*Intuition note:* Sharers of falsehood were, on the measures shown, less well connected, yet falsehood still travelled more. So these sender and network traits do not explain the gap, and the authors look for other explanations such as novelty and people's greater likelihood to retweet falsity.

### Novelty hypothesis (pp. 1149–1150)
- Argument: novelty attracts attention, helps decision-making and encourages sharing, because it updates our understanding of the world. It has information-theoretic value (greatest aid to decisions) and social value (status of being "in the know"). The authors test whether falsity was more novel and whether novel information was more likely retweeted (p. 1149).
- Method: ~5000 randomly selected users who spread true and false rumors; a random sample of ~25,000 tweets that they were exposed to in the 60 days before retweeting. An LDA topic model (200 topics, trained on 10 million English tweets) gives each tweet a probability distribution over the 200 topics. Novelty = distance between the rumor tweet's topic distribution and that of the prior tweets (p. 1149).
- Three metrics: information uniqueness (K-S 0.457), Kullback–Leibler divergence (0.433), Bhattacharyya distance (0.415; similar to Hellinger distance). All P ≈ 0.0; false rumors were more novel on all three (pp. 1149–1150). Fig. 4E means (false vs true): IU 0.85 vs 0.78; KL 4.49 vs 4.15; BD 0.87 vs 0.84 (p. 1149).
- Perception: users may not have perceived the novelty. Reply emotions were scored with the NRC lexicon (~140,000 words, eight Plutchik emotions) plus ~32,000 hashtags. After removing stop words and URLs, each reply gets a vector of emotion weights summing to one (p. 1150).
- False rumors drew replies with more surprise (K-S 0.205) and disgust (0.102). True rumors drew more sadness (0.037), anticipation (0.038), joy (0.061) and trust (0.060). The surprise result corroborates the novelty hypothesis (p. 1150).
- Fig. 4F shows fear (D = 0.021, P ≈ 0.164) and anger (0.023, P ≈ 0.078) with no significant difference (p. 1149).
- Limit: "we cannot claim that novelty causes retweets" or that it is the only reason. The authors do find that false news is more novel and that novel information is more likely to be retweeted (p. 1150).

*Intuition note:* "Novel" here means unlike what a person recently saw in their own feed. Falsehood scored as more unusual by this measure. Surprise in replies fits that picture, but it is supporting evidence, not proof of cause.

### Robustness checks (p. 1150)
1. **Clustering:** cascades of one rumor have correlated errors, so all variances are clustered at rumor level. Comparing analyses with and without clustered errors, clustering reduced the precision of estimates as expected, but directions, magnitudes and significance did not change. Chi-square (P ≈ 0.0) and deviance goodness-of-fit tests ($d = 3.4649\times10^{-6}$, $P\approx1.0$) indicate well-specified models.
2. **Selection bias:** fact-checking may select particular rumors. A second sample, not checked by any organization, was labeled by three MIT and Wellesley undergraduates trained with the authors' rumor-detection algorithm (run on 3 million English tweets from 2016). Rumors already investigated by a checker were discarded. They agreed on 90% of 13,240 cascades (Fleiss' kappa 0.88). Results were nearly identical (fig. S17); false rumors had greater depth (K-S 0.139), size (0.131), max breadth (0.139), structural virality (0.066), speed and users per depth. Majority-rule labeling gave the same results.
3. **Bots:** with bots removed using a bot-detection algorithm, then added back, no main conclusion changed. Results held when removing all cascades started by bots (including human retweets), using a second algorithm, and varying sensitivity. Bots accelerated true and false news roughly equally.

### Discussion (p. 1150)
- Bot result: false news spreads farther, faster, deeper and more broadly "because humans, not robots, are more likely to spread it" (p. 1150).
- More research on behavior is needed, via interviews, surveys, lab experiments and neuroimaging (p. 1150).
- False news can drive misallocation of resources in attacks and disasters, misaligned investment and misinformed elections. The amount of false news is increasing (Fig. 1C, E) (p. 1150).
- The analysis "overturns conventional wisdom": network structure and spreader traits might be expected to favor falsehood, but the opposite holds. People's greater tendency to retweet falsity drives its spread despite factors favoring truth (p. 1150).
- Congressional testimony has focused on bots (note 36). The authors conclude human behavior contributes more to the differential spread. Containment should also use behavioral interventions (labeling, incentives), not only curtail bots (p. 1150).

## Toy example (ours, not from the text)
Two cascades of the same rumor, counted like Fig. 1A (origin user counts in size; origin is depth 0).
- Cascade X: O is retweeted by U1, U2, U3 (depth 1); U4 retweets U1 (depth 2); U5 retweets U4 (depth 3). Users at each depth: 1, 3, 1, 1. Size = 6, depth = 3, max breadth = 3.
- Cascade Y: O′→V1→V2→V3. Users per depth: 1, 1, 1, 1. Size = 4, depth = 3, max breadth = 1.
- Same depth, different shape: X has more branching than Y.
- CCDF (we define it as the share of cascades with size ≥ x): sizes 1, 1, 2, 4, 6 give 100% at x = 1, 60% at 2 (3 of 5), 40% at 4 (2 of 5), 20% at 6 (1 of 5). A curve that stays higher at large x means more large cascades, as for false news in Fig. 2B.
- Odds ratio: coefficient 0.5350 → $e^{0.5350}\approx1.7074$ (matches the table's 1.707489 up to rounding of the coefficient).

## Concepts
- [[structural-virality]] — metric between one broadcast and multi-generation spread; the paper uses it to show falsehood spreads peer to peer (pp. 1147–1148)
- [[rumor-cascade]] (new) — unbroken retweet chain with a single origin; a rumor can have many (p. 1146)
- [[differential-diffusion-of-falsehood]] (new) — falsehood spreads farther, faster, deeper, more broadly than truth (p. 1147)
- [[novelty-hypothesis]] (new) — hypothesis that novel content is more likely to be shared; false rumors scored more novel on topic-distance measures, but causation is not claimed (pp. 1149–1150)
- [[ccdf]] (new) — complementary cumulative distribution function; one way the paper compares cascade distributions (Figs. 1–3) (p. 1147)
- [[nrc-emotion-lexicon]] (new) — word-emotion list (eight emotions) used to score emotions in replies (p. 1150)
- [[cluster-robust-standard-errors]] (new) — errors clustered by rumor because cascades of one rumor are correlated (p. 1150)

## Canonical instances
- [[obama-explosion-false-tweet]] (new) — a false tweet claimed Obama was injured; $130 billion in stock value wiped out (p. 1146)
- [[crimea-annexation-mixed-rumor-spike]] (new) — spike in partly true, partly false rumors in 2014 (p. 1147)
- [[us-election-false-political-rumors]] (new) — increases in false political rumors during the 2012 and 2016 elections (p. 1147)

## Bridges (candidates)
- [structural-analogy] Novelty measured as KL or Bhattacharyya distance between topic distributions ↔ Information (Shannon): information as surprise relative to what the receiver expects — both tie value to departure from expectation.
- [structural-analogy] Peer-to-peer branching vs broadcast (structural virality) ↔ Two-step flow: influence passes through people, not directly from a source.
- [metaphor] Fact-checker verdicts as ground-truth labels ↔ Pseudo-environment: both concern the gap between what circulates and what is verifiably so.

## Questions this raises
- If novelty is only one factor, what other judgments (the paper mentions disgust) drive sharing, and can interviews or lab experiments separate them?
- Do these findings, from Twitter retweets of fact-checked rumors, generalize to other platforms or to unchecked rumors?
- Do reply emotions reflect what sharers felt, or only what repliers felt?
- Would labeling or incentive interventions change retweeting of falsehood?

## Reading notes
- Printed page = pdf + 1145 (pdf 1 = 1146). Printed 1152 (pdf 7) is the journal's cover/summary sheet, not article text. Supplementary materials (tables S3–S10, fig. S11, fig. S17, section S8.3) were not provided and are cited only as the authors cite them.
- The text gives the verified-users K-S as 0.004; Fig. 4A shows D = 0.005, p < 0.001.
- The abstract (p. 1146) lists fear among emotions in replies to false stories. The body text mentions only surprise and disgust, and Fig. 4F shows fear not significant (p ≈ 0.164).
- The text says "70% more likely" for retweeting; Fig. 4B shows an odds ratio of 1.707.
- "P ~ 0.0" is the authors' notation for a P-value near zero.
- Figures were checked in the page images; no unreadable equations (the paper has none).
