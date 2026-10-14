---
id: kahneman-2011-thinking/ch31-risk
work: kahneman-2011-thinking
unit: 31 Risk Policies
pages: pdf 326–333 (printed page numbers not shown)
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Risk Policies

## L0 — One line
Humans tend to decide each risky choice separately (narrow framing), which together with loss aversion is costly; a broad frame, such as a risk policy, is the remedy Kahneman proposes.

## L1 — The gist (≤ 120 words)
Kahneman asks what goes wrong when people judge risky choices one at a time (narrow framing). His example: most people pick the sure gain in one problem and the gamble in a paired loss problem. Together, they form a combination clearly worse than the one rejected. Loss aversion (losses hurt more than equal gains please) plus narrow framing can make people reject small, favorable gambles that they would accept in a bundle. The remedy is a broad frame: bundle similar decisions, think like a trader, check investments rarely, and keep a standing risk policy. Such a policy is the counterpart of the outside view (statistics of similar cases) in planning. It matters because limited minds cannot reach consistent preferences unaided.

**Prerequisites:** expected value (probability-weighted average); the idea of a gain/loss frame; the System 1 / System 2 distinction.

## L2 — Key ideas
- Most people prefer the sure gain (A) and the loss gamble (D). Together these give a dominated combination, and the dominating one (BC) was favored by only 3% (pdf 326–327).
- Any simple choice framed as gains and losses can be split into a combination of choices in many ways, and the resulting preferences are likely to be inconsistent (pdf 327).
- Narrow framing treats decisions one by one; broad framing treats them as one comprehensive decision. Broad framing is superior (or at least not inferior) whenever several decisions are contemplated together. A rational agent frames broadly, but humans are by nature narrow framers (pdf 327–328).
- Samuelson's friend would refuse one bet but accept 100 such bets. Kahneman's loss-averse "Sam" shows why: bundling lowers the chance of a net loss (pdf 328–329).
- Advice: treat small gambles as part of a bundle ("you win a few, you lose a few"), with three stated limits (pdf 330).
- Experienced traders shield themselves from the pain of losses by broad framing; in an experiment, students told to think like traders showed a blunted emotional reaction to losses. Checking investments only about once a quarter helps (pdf 331).
- A risk policy is a broad frame, the analogue of the outside view. The outside view and the risk policy remedy two opposing biases (optimism and loss aversion), though there is no guarantee that the biases cancel in every case (pdf 331–332).

## L3 — Walkthrough

### The paired decisions (pdf 326–327)
- **Decision (i):** A = sure gain $240; B = 25% chance of +$1,000, else nothing. **Decision (ii):** C = sure loss $750; D = 75% chance of −$1,000, else nothing (pdf 326).
- System 1 reacts automatically: attraction to a sure gain, aversion to a sure loss. This comes before any optional expected-value computation (gamble B: +$250, gamble D: −$750) (pdf 326).
- People tend to be risk averse for gains and risk seeking for losses when probabilities are moderate or high. In Kahneman and Tversky's experiment, 73% chose A and D; only 3% chose B and C (pdf 326).
- People did not compute the four combinations, since this takes paper and pencil (pdf 326).
- Combined options (added step: arithmetic checked):
  - AD: 25% → $240 + $0 = +$240; 75% → $240 − $1,000 = −$760.
  - BC: 25% → $1,000 − $750 = +$250; 75% → $0 − $750 = −$750.
- BC dominates AD, meaning it is unequivocally better. The 73% majority therefore chose the inferior one (pdf 327).
- **Intuition note:** Each choice felt reasonable alone. Added up, they cost money in every outcome. Gut preferences are not guaranteed to be consistent.

### Broad or narrow? (pdf 327–328)
- Kahneman's claims: consistency of human preferences is "a hopeless mirage". Risk aversion for gains plus risk seeking for losses costs money, because both premiums are paid from "the same pocket" (pdf 327).
- Every simple choice formulated in terms of gains and losses can be deconstructed in innumerable ways into a combination of choices, yielding preferences that are likely to be inconsistent (pdf 327).
- **Narrow framing:** a sequence of separate simple decisions. **Broad framing:** one comprehensive decision with all combined options (pdf 327).
- With 5 binary decisions, the broad frame has 32 options. The narrow sequence is just one of them, probably not the best (pdf 327–328).
- Kahneman's explanation: susceptibility to WYSIATI (an acronym defined earlier in the book; its expansion is not on these pages) and aversion to mental effort make us tend to decide as problems arise, even when specifically instructed to consider them jointly (pdf 328).

### Samuelson's problem (pdf 328–329)
- Samuelson's friend refused a single coin toss (lose $100 / win $200) but said he would take 100 such bets, because he would feel the $100 loss more than the $200 gain (pdf 328).
- Samuelson proved that, under some very specific conditions, a utility maximizer who rejects one gamble should reject many. The proof is valid, but its conclusion violates common sense (pdf 328).
- Rabin and Thaler's point: the 100-bet package has expected return $5,000, a 1/2,300 chance of losing any money, and a 1/62,000 chance of losing more than $1,000. If utility theory permits rejecting it, something is wrong with the theory as a model of rationality (pdf 328).
- Samuelson did not seem to mind that his valid proof led to a conclusion violating common sense; Kahneman says his willingness even to consider rejecting the package as possibly rational testifies to the powerful hold of the rational model (pdf 328).
- **Sam's model:** Sam multiplies losses by 2, then takes the expected value. One toss has expected value $50, since $0.5 \cdot 200 - 0.5 \cdot 100 = 50$ (added step). Doubled, the value is 0, so Sam refuses (pdf 328–329).
- **Two tosses:** the chance of losing falls to 25%. Extremes (lose 200, win 400) cancel after doubling. The middle outcome is positive, so the bundle is worth $50 (pdf 329).
- Added step (our reconstruction; the table is missing from the text layer): net outcomes $+400$ (25%), $+100$ (50%), $-200 \to -400$ (25%) give $0.25\cdot 400 + 0.5\cdot 100 - 0.25\cdot 400 = 50$.
- **Three tosses:** the third toss adds $62.50 (pdf 329). **Five tosses:** expected value $250, probability of losing anything 18.75%, cash equivalent $203.125 (pdf 329).
- Sam never changes his loss aversion; aggregation lowers the probability of loss, and so loss aversion matters less (pdf 329–330).
- **Intuition note:** Bundling many favorable bets makes an overall loss less likely. The pain of losing matters less because losing overall becomes unlikely.

### The advice: think like a trader (pdf 330–331)
- Kahneman's sermon asks a loss-averse person whether he is on his deathbed. Small favorable gambles will come repeatedly. See each as part of a bundle, and repeat "you win a few, you lose a few". The mantra's purpose is to control the emotional response to losses (pdf 330).
- **Qualifications:** it works when gambles are genuinely independent (it does not apply to several investments in the same industry); it works only when a loss does not worry you about total wealth; and it should not be applied to long shots (pdf 330).
- Experienced traders live by broad framing. In an experiment, students received narrow instructions ("make each decision as if it were the only one") or broad ones ("imagine yourself as a trader"). Physiological measures (including skin conductance) were used; as expected, broad framing blunted the emotional reaction to losses and increased willingness to take risks (pdf 331).
- Investors can get similar benefits by checking results less often. Once a quarter is enough and may be more than enough. Frequent checks mean frequent small losses, whose pain exceeds the pleasure of equally frequent small gains (pdf 331).
- Aggregated feedback gives less bad news, and the usual reaction to bad news is more loss aversion. A commitment not to change a position for several periods improves performance (pdf 331).

### Risk policies (pdf 331–332)
- A narrow framer constructs a preference each time. A **risk policy** is a routine rule, for example "always take the highest possible deductible" or "never buy extended warranties". It is a broad frame; the occasional loss is bearable because the policy should pay off over the long run (pdf 331–332).
- A risk policy is analogous to the outside view (focus on statistics of similar cases). The outside view remedies the planning fallacy (exaggerated optimism); the risk policy remedies exaggerated caution from loss aversion (pdf 332).
- The two biases oppose each other, but there is no guarantee that they cancel in every situation. An organization should aim at both remedies (pdf 332).
- Thaler's story: 25 division heads each refused a 50–50 bet of losing a large amount of capital or earning double. The CEO said he would like all of them to accept their risks. Kahneman says it was natural for the CEO to adopt a broad frame covering all 25 bets, relying on statistical aggregation (pdf 332).
- **Intuition note:** A rule applied in advance is a broad frame. One loss then looks like an expected part of a larger plan.

## Toy example (ours)
Decision 1: sure +$60 (A) vs 25% chance of +$300 (B). Decision 2: sure −$225 (C) vs 75% chance of −$300 (D).
- A + D: 25% → $60 + $0 = +$60; 75% → $60 − $300 = −$240.
- B + C: 25% → $300 − $225 = +$75; 75% → $0 − $225 = −$225.
- BC beats AD in both outcomes ($75 > $60 and −$225 > −$240). Choosing A and D is therefore dominated, as in the book's example.

## Concepts
- [[framing-effect]] — the same choice problem can yield different, even inconsistent, preferences depending on how it is split or bundled (pdf 327)
- [[narrow-framing]] (new) — treating each decision separately as it arises (pdf 327)
- [[broad-framing]] (new) — treating several decisions as one comprehensive choice (pdf 327)
- [[loss-aversion]] — losses weigh more than gains; Sam values a loss at twice a gain (pdf 328–329)
- [[risk-aversion]] — here, the preference for a sure gain; paired with risk seeking in the loss domain (pdf 326)
- [[expected-utility]] — the rational-model benchmark Samuelson used; Rabin and Thaler's point, reported by Kahneman, is that if it can be consistent with such a foolish rejection, something is wrong with it (pdf 328)
- [[risk-policy]] (new) — a routine rule that applies a broad frame to recurring risky choices (pdf 331–332)
- [[outside-view]] (new) — a broad frame for plans, based on statistics of similar cases (pdf 332)
- [[wysiati]] (new) — an acronym introduced earlier in the book (expansion not given on these pages); cited as one reason people decide problems as they arise (pdf 328)
- [[bounded-rationality]] — limited mind and effort prevent enforcing consistency (pdf 328)

## Canonical instances
- [[kt-sure-gain-sure-loss-pair]] — decisions i and ii, with 73% choosing A and D and only 3% choosing B and C (pdf 326–327)
- [[samuelson-100-bets]] — rejecting one bet while accepting many (pdf 328)
- [[sam-doubled-loss-table]] — loss aversion fades as favorable gambles are bundled (pdf 329)
- [[thaler-25-divisions]] — executives refuse risks that their CEO wants all to accept (pdf 332)

## Bridges (candidates)
- [same-math] Broad framing of repeated bets ↔ statistics: pooling independent bets reduces the chance of net loss, which is the aggregation effect Sam shows.
- [structural-analogy] Risk policy ↔ decision theory of commitment: a rule fixed in advance constrains later in-the-moment choices.
- [structural-analogy] Outside view and risk policy ↔ forecasting: both replace case-specific detail with reference-class statistics.

## Questions this raises
- When bets are not independent (for example, same-industry investments), how much of the bundling benefit remains?
- How should one decide whether a loss is small relative to wealth before applying the mantra?
- If optimism and loss aversion partly cancel, when is removing only one of them harmful?
- Is a rule such as "never buy extended warranties" always good, or only for certain risks?

## Reading notes
- Printed page numbers are not visible in the labels, so citations use pdf numbers (326–333).
- The table on pdf 329 (Sam's one-, two- and three-toss values) is missing from the text layer. I reconstructed the arithmetic myself, marked "added step", and matched it to the numbers in the prose ($0, $50, +$62.50 for the third toss).
- The text layer has garbled fragments (e.g., "Bght hecome oo", "Bght iciof 2"). I read around them.
- The book writes "Humans" (capital H) in contrast to the rational agent model (pdf 327–328).
- In the text layer of pdf 327, the sentences about AD and BC read as if AD were the dominant option and BC were preferred by 73%. This conflicts with pdf 326–327 (73% chose A and D; BC dominates AD). The digest follows the consistent reading.
