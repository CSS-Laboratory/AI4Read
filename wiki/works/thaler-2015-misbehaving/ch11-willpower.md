---
id: thaler-2015-misbehaving/ch11-willpower
work: thaler-2015-misbehaving
unit: "11. Willpower? No Problem"
pages: 53-65
fields: [economics-finance]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Willpower? No Problem

## L0 — One line
Early economists treated self-control problems as real, but after Samuelson's constant-rate discounting model, theories of saving and consumption assumed ever smarter Econs with perfect willpower, and Thaler argues we must return to modeling Humans.

## L1 — The gist (≤ 120 words)
Why did economics lose sight of self-control? Thaler traces the history from Adam Smith and Irving Fisher, who wrote about myopic, impatient people, to Samuelson's 1937 discounted utility model. Samuelson's model assumes a constant discount rate and so rules out present bias and time inconsistency, though he himself noted its limits. Later consumption theories (Keynes, Friedman, Modigliani, Barro) look further ahead and need more willpower and cleverness. Thaler judges that Keynes, adjusted toward Friedman, predicts temporary-income responses best of the three, yet Modigliani's cleverer model became standard. He proposes the behavioral life-cycle hypothesis, which adds mental accounts. The point: models of consumption and saving should describe Humans, not Econs with PhDs.

**Prerequisites:** percentages and discounting (present value = value × discount factor); idea of utility; basic notion of consumption vs saving.

## L2 — Key ideas (5–10 bullets)
- Smith, Jevons, Pigou and Fisher wrote about myopia, impatience, and failures of willpower or imagination, so early economics had Humans "in plain sight" (pp. 54–56).
- Samuelson's discounted utility model made future value fall at a steady rate, with no passions and no faulty telescope. He still listed its "serious limitations" (pp. 55–56).
- A constant (exponential) discounter is time-consistent. A present-biased discounter such as Matthew reverses his plan as time passes (pp. 56–59).
- Samuelson mentioned precommitment (removing the cashews, whole life insurance), but the profession adopted the model and forgot the warnings. Kahneman calls this theory-induced blindness (pp. 59–61).
- From Keynes to Friedman to Modigliani to Barro, the modeled agent looks further ahead and needs more skill and willpower. Predicted spending from a $1,000 windfall falls from $950 (Keynes, middle-class family saving 5%) to $317 (Friedman, year one) to $25 per year (Modigliani) to $0 (Barro, for a bond-financed tax cut) (pp. 61–64).
- Thaler thinks Keynes, adjusted toward Friedman, predicts best for temporary income changes. He suggests that, perhaps through a "cleverer is better" heuristic, models were chosen on cleverness instead, and Modigliani's became standard (p. 63).
- The life-cycle hypothesis also assumes fungible wealth. The behavioral life-cycle hypothesis relaxes this using mental accounts (pp. 64–65).

## L3 — Walkthrough

### Adam Smith and early economists (pp. 53–55)
- Thaler's claim: for about two centuries, economists "knew their Humans" (p. 53).
- Smith's *Wealth of Nations* (1776) uses the "invisible hand" only once. The next sentence reads "Nor is it always the worse for the society…", which Thaler says is hardly the same as an assertion that things will turn out for the best (p. 53). 
- Smith's self-control ideas are in *Theory of Moral Sentiments* (1759): a struggle between "passions" and an "impartial spectator." Passions are myopic (shortsighted) (p. 54).
- Smith saw that willpower is needed against myopia. Loewenstein documents that other early work on intertemporal choice (choice about timing of consumption) also stressed willpower (p. 54).
- Jevons (1871): the preference for present over future consumption diminishes over time. Ice cream today vs tomorrow matters a lot. The same choice a year ahead matters little (p. 54).
- Some early economists saw any discounting as a failure of willpower or of imagination. Pigou (1921): our "telescopic faculty is defective" (p. 54).
- Fisher (1930) used indifference curves to model choice between two dates at a market interest rate. This was a normative theory (what a rational person should do). Fisher said it was not a satisfactory descriptive model (pp. 54–55).
- Fisher believed the poor are more impatient, and partly irrationally so. His examples were the farmer who never mends his leaky roof and workers lured to the saloon on payday (p. 55).

> **Intuition note:** Some early economists treated discounting of the future as a human failing (of willpower or imagination). Samuelson's model had only steady discounting, with no passions or faulty telescope.

### Samuelson's discounted utility model (pp. 55–56)
- Samuelson, aged 22, wrote the seven-page "A Note on the Measurement of Utility" (1937). It formulated the standard discounted utility model: future consumption is worth less, discounted at some rate (p. 55).
- Example: a dinner a year away valued at 90% of one now means an annual discount rate of about 10% (pp. 55–56).
- The model has no passions or faulty telescopes, only steady discounting. Its last two pages discuss "serious limitations." One is that if discount rates vary over time, people may change their minds. The worry is the case of greatest impatience for immediate rewards (p. 56).

### Ted and Matthew: exponential vs present-biased discounting (pp. 56–59)
- A Wimbledon match tonight is worth 100 utils (arbitrary units of happiness) (p. 56).
- **Ted** discounts at a constant 10% per year: 100, 90, 81, 72… This is exponential discounting (p. 56).
- **Matthew** values it at 100 today, 70 in a year, then 63 in year three or later. He discounts 30% for the first year, 10% for the next, then 0% (p. 56).
- He looks through Pigou's faulty telescope. The *New Yorker* "View of the World from 9th Avenue" cover is the analogy. Matthew finds waiting most painful at the beginning (p. 56).
- This pattern is called quasi-hyperbolic discounting. Thaler prefers the term **present-biased** (p. 58).
- Three tickets: A, first round tomorrow (100 utils if all were this year); B, quarterfinal next year (150); C, final in two years (180) (p. 58).
- **Ted, today:** present values are A = 100, B = 135 (90% of 150), C = 146 (81% of 180). He chooses C (p. 58).
- **Ted, a year later:** C is worth 162 (90% of 180), still above B. He sticks to his plan, so he is **time-consistent** (p. 58).
- **Matthew, today:** A = 100, B = 105 (70% of 150), C = 113 (63% of 180). He chooses C (p. 58).
- **Matthew, a year later:** C falls to 126, below B's 150, so he switches to B. He is **time-inconsistent** (pp. 58–59; Figure 5, p. 60).

> **Intuition note:** An exponential discounter applies the same trade-off between "now vs next year" and "next year vs the year after." A present-biased person weighs "now" much more heavily. His plan to wait therefore breaks when "later" becomes "now."

### Why the model won; theory-induced blindness (pp. 59–61)
- Samuelson was aware of time inconsistency. He mentions steps like removing the bowl of cashews and buying whole life insurance as compulsory saving. Then the profession moved on with exponential discounting as its workhorse (p. 59).
- Thaler says it may be unfair to blame this one paper, since economists were already moving away from folk psychology, led by Pareto (p. 60).
- Kahneman's term **theory-induced blindness**: most economists forgot earlier behavioral writing, even Fisher's of seven years before, and Samuelson's warnings (p. 60).
- Thaler says exponential discounting "just had to be" the right model once economists studied only Econs, who would not keep changing their minds. He says this blindness strikes nearly everyone with an economics PhD: the training gives insight into Econs but loses intuition about Humans (p. 61).

### Consumption function: Keynes → Friedman → Modigliani → Barro (pp. 61–64)
- The consumption function says how household spending varies with income. Test case: a one-time $1,000 tax cut per person in a recession (p. 61).
- Thaler's thesis: as models became more sophisticated, Econs became smarter and cured all self-control problems (p. 61).
- **Keynes:** a household consumes a fixed share of extra income, the marginal propensity to consume (MPC). MPC is highest (nearly 100%) for the poor and near zero for the rich. A middle-class family saving 5% would spend $950 of $1,000 (pp. 61–62).
- **Friedman** (1957), permanent income hypothesis: households smooth consumption, using a three-year horizon. Spending is spread evenly, about $950/3 ≈ $317 in year one. This implies a 33% annual discount rate (p. 62). Footnote: interest and inflation are assumed zero (p. 65).
- **Modigliani and Brumberg**, life-cycle hypothesis: plan consumption over total lifetime wealth, including retirement and possibly bequests. For someone who knows he will live exactly 40 more years and plans to leave no bequests, the windfall is spread evenly and spending is $1000/40 = $25 per year (pp. 62–63).
- Across these models the agents think further ahead and are implicitly assumed to have enough willpower to delay consumption, in Modigliani's case for decades (p. 63).
- Thaler's judgment: if models are judged by predictive accuracy (Friedman's standard), Keynes wins for temporary income changes, modified toward Friedman for smoothing. Modigliani won on cleverness, perhaps through a "cleverer is better" heuristic (p. 63). For retirement saving, Thaler would move "a bit further" toward Modigliani (footnote ‡, p. 65).
- **Barro:** parents care about their descendants, so the horizon is effectively forever. A casino windfall gives Modigliani's prediction. A tax cut financed by government bonds is not spent. The recipient raises bequests by exactly the tax cut, because heirs will pay taxes later (p. 63).
- Thaler: this requires Econs as smart as Barro. A "closet Keynesian" agent who expects the tax cut to pay for itself through growth would not change bequests. The agent would then need to know the relevant theory and the empirical tests (pp. 63–64).
- Thaler's conclusion: there must be limits to the knowledge and willpower assumed of agents (p. 64).
- Thaler reports that when he described Modigliani's theory in a Cornell psychology talk, the audience reaction suggested they found it hilarious. Bob Frank assured them he had not made anything up (p. 64).

> **Intuition note:** Each step in the sequence gives the agent a longer horizon and more calculation. Predicted spending from the same windfall drops from almost all of it to none. Thaler suggests that models were then chosen for cleverness rather than for predictive accuracy.

### Fungibility and the behavioral life-cycle hypothesis (pp. 64–65)
- The life-cycle hypothesis assumes smart planning (with rational expectations), willpower, and **fungibility**: wealth is wealth, whether in cash, home equity, a retirement plan or an heirloom (p. 64). Mental accounting makes that assumption doubtful (pp. 64–65).
- Shefrin and Thaler's **behavioral life-cycle hypothesis**: consumption depends on lifetime wealth and on the mental accounts in which wealth is held. MPC from a lottery win is likely much higher than from a rise in retirement holdings (p. 65).
- One study found the MPC from rising retirement wealth can even be negative: investors with high returns raised saving rates, most likely because they extrapolate the success (p. 65).
- Thaler's closing claim: we need a model of Humans, who have "passions, faulty telescopes," separate wealth pots, and respond to short-run returns (p. 65).

## Toy example (ours, not from the text)
A person can take Small = 60 utils (at year 1) or Large = 100 utils (at year 2).

**Exponential, 20% per year (factor 0.8 per year):**
- Today: Small = 0.8 × 60 = 48; Large = 0.8² × 100 = 64. Choose Large.
- One year later: Small is available now, 60; Large is one year away, 0.8 × 100 = 80. Still Large. Consistent.

**Present-biased (factor 0.5 for any wait, as in Matthew's pattern):**
- Today: Small = 0.5 × 60 = 30; Large = 0.5 × 100 = 50. Choose Large.
- One year later: Small = 60 now; Large = 0.5 × 100 = 50. Switches to Small. Time-inconsistent.

## Concepts
- [[exponential-discounting]] (new) — value falls by a constant percentage per period; time-consistent (p. 56)
- [[discounted-utility-model]] (new) — Samuelson's 1937 standard model of intertemporal choice (p. 55)
- [[present-bias]] (new) — high discounting of near delays, lower later (quasi-hyperbolic) (p. 58)
- [[time-inconsistency]] (new) — plans made earlier are reversed later without new information (pp. 56, 58–59)
- [[theory-induced-blindness]] (new) — Kahneman's term: a model's acceptance makes people ignore its flaws and earlier insights (p. 60)
- [[marginal-propensity-to-consume]] (new) — share of extra income consumed (p. 62)
- [[permanent-income-and-life-cycle-hypotheses]] (new) — Friedman and Modigliani smoothing models of consumption (pp. 62–63)
- [[behavioral-life-cycle-hypothesis]] (new) — life-cycle model where mental accounts affect consumption (p. 65)
- [[mental accounting, endowment effect, loss aversion]] — wealth is not fungible across accounts (pp. 64–65)
- [[rational expectations]] — mentioned as assumed in life-cycle planning (p. 64)
- [[bounded rationality / heuristics]] — Thaler suggests economists perhaps adopted a "cleverer is better" heuristic (p. 63)

## Canonical instances
- [[ted-matthew-wimbledon]] — time-consistent vs time-inconsistent discounters choosing tickets (p. 58)
- [[leaky-roof-farmer]] — Fisher's example of partly irrational impatience (p. 55)
- [[thousand-dollar-tax-cut]] — one windfall, four theories, different predicted spending (pp. 61–64)

## Bridges (candidates)
- [structural-analogy] Present bias and precommitment (cashews, whole life insurance) ↔ self-control problems: dividing planner and doer, with commitment devices (pp. 59, 54).
- [structural-analogy] Barro's forward-looking agent ↔ rational expectations: agent must know the true model (pp. 63–64).
- [metaphor] Faulty telescope / 9th Avenue map ↔ perception of distance: far events look equally far.

## Questions this raises
- What model of Humans does Thaler offer next (the next chapter)?
- How could present bias be measured in real saving or spending data?
- Does a temporary tax cut really lead to more spending than a retirement-account gain of the same size?
- When models are chosen for cleverness over accuracy, how could the choice be corrected?

## Reading notes
- Printed = pdf − 41. Printed page 57 has no text in the text layer, and no page image was supplied for it. Printed page 58 begins with the Figure 4 caption, followed by body text; the New Yorker cover image itself is not visible on p. 58.
- The text on p. 59 says Matthew "discounts the value of C by 70% to 126." The numbers (126 = 70% of 180, and Figure 5) imply a discount factor of 0.7, not a 70% cut. I followed the figure.
- In the text layer of p. 60 only the label "FIGURE 5" appears; the valuation tables are readable in the image. It gives full tables of valuations for Ted and Matthew.
- Ted's present value of C is 145.8, rounded to 146 in the text.
