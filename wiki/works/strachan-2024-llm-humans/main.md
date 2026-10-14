---
id: strachan-2024-llm-humans/main
work: strachan-2024-llm-humans
unit: paper
pages: "(pdf 1–?) — HTML source, no printed pages; cited by section heading"
fields: [theory-of-mind]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Testing theory of mind in large language models and humans (Strachan et al., 2024)

## L0 — One line
On a battery of theory-of-mind tests, GPT-4 matches or beats humans on most tasks, and follow-up variants of the faux pas test suggest that its failure there reflects over-cautious non-commitment rather than failed inference, while LLaMA2's apparent success may reflect a bias.

## L1 — The gist (≤ 120 words)
Can large language models (LLMs) match humans on theory-of-mind tests? The authors gave GPT-4, GPT-3.5 and LLaMA2-70B five tests (false belief, irony, faux pas, hinting, strange stories), 15 independent sessions each, and compared them with 250 humans. GPT-4 matched or beat humans on most tests but fell short on faux pas. LLaMA2-70B beat humans only on faux pas. Follow-up variants suggest GPT's failure reflects over-cautious refusal to commit, not failed inference, and LLaMA2's success may reflect a bias towards attributing ignorance ("didn't know"). The authors argue that a single test or single run would have hidden these deviations, and they stress the importance of systematic testing with human benchmarks.

**Prerequisites:** the false-belief task idea; what a chat session with an LLM is; basic statistics (non-parametric test, p-value, effect size, chi-square test on counts).

## L2 — Key ideas (5–10 bullets)
- Method: a battery of five tests, repeated sessions, and a large human benchmark gives a fairer comparison than one test run once (§ "Main"; § "Discussion").
- False belief: humans and all LLMs were at ceiling. LLM success may have lower-level explanations, and humans also failed half of the perturbed versions (§ "False belief").
- On irony, hinting and strange stories, GPT-4 scored above humans on all three. GPT-3.5 did not differ significantly from humans on hinting and strange stories, and LLaMA2-70B was below humans on all three (§ "Irony", "Hinting", "Strange stories").
- Faux pas was the one test where GPT-4 fell below humans and LLaMA2-70B beat them. The GPT errors were mostly "not enough information" answers (§ "Understanding faux pas").
- Three hypotheses were tested: failure of inference, Buridan's ass, hyperconservatism. Rewording the question as a likelihood question gave GPT-4 perfect scores, which supports hyperconservatism (§ "Understanding faux pas").
- The belief likelihood test shows GPT models tracked story information. LLaMA2-70B did not separate "neutral" from "knowledge implied", so its faux pas success may be illusory (§ "Testing information integration").
- The authors propose a competence–performance dissociation: GPT may compute mentalistic inferences yet not commit to them under uncertainty. They suggest that this may reflect cautionary mitigation measures and disembodiment (§ "Discussion").
- Novel-item controls were designed to check for memorisation of published items, and the authors report no pattern pointing to it. They say these controls are of limited strength against Clever-Hans heuristics for false belief and faux pas (§ "Methods: Novel items").

## L3 — Walkthrough

### Main (introduction)
- Theory of mind (ToM) = the ability to track other people's mental states. The authors' example: a friend remarks that it is a bit hot in the room and you infer she wants the window opened (§ "Main").
- ToM is not one unitary construct. It is an interconnected set of notions used to explain, predict and justify behaviour. Many tasks exist: reaction-time and looking measures, reading eyes, false-belief and pragmatic-language tasks. They are proposed to test early, efficient but inflexible implicit processes and later, flexible but demanding explicit abilities (§ "Main").
- Earlier LLM work: LLMs solve some tasks used to test human ToM. But success is mixed, and small prompt changes (for example, changing characters' perceptual access) break it. This raises the worry that LLMs use shallow heuristics (§ "Main").
- The authors follow a "machine psychology" approach: diverse measures, multiple repetitions per test, and a clear human benchmark. They test GPT-4 and GPT-3.5, plus open-weight LLaMA2-Chat for reproducibility. Total human N = 1,907 (§ "Main").

### Results — Theory of mind battery
- Tests: hinting, false belief, faux pas, strange stories, plus an irony test adapted from an earlier study (§ "Theory of mind battery").
- Each test was given to GPT-4, GPT-3.5 and LLaMA2-70B-Chat across 15 chats. Chats are independent, so each counts as one observation. Humans: 250 participants. Items were presented in written form for a "species-fair" comparison (§ "Theory of mind battery").
- All tests except irony are public. To check for training-set memorisation, the authors wrote **novel items** with the same logic but different content (§ "Performance across theory of mind tests").
- Statistics: Holm-corrected two-sided Wilcoxon tests of LLM scores against human scores (§ "Performance…", Fig. 1 caption).

**Per-test results** (Fig. 1 compares scores to humans)
- **False belief.** Humans and all LLMs were at ceiling. All LLMs said that an agent who left would look where they remembered the object. On novel items, 5 of 51 humans made one error, typically by naming only one location (§ "False belief").
  - The authors note that LLM success may be explained by lower-level mechanisms than belief tracking. Earlier work found LLMs fail on small perturbations (transparent containers; asking about the character who moved the object) (§ "False belief").
  - In a control study they replicated GPT's poor performance on these perturbations. Humans (N = 757) also failed half of them. Because the perturbations also change physical properties, the authors say it is hard to tell why LLMs and humans failed (§ "False belief").
- **Irony.** GPT-4 was significantly better than humans ($P = 0.040$, $r = 0.32$). GPT-3.5 ($P = 2.37\times10^{-6}$, $r = 0.64$) and LLaMA2-70B ($P = 2.39\times10^{-7}$, $r = 0.70$) were below humans (§ "Irony").
  - GPT-3.5 was perfect on non-ironic controls but erred on ironic items. It also made more errors on earlier trials than later ones. LLaMA2-70B erred on both types, suggesting poor discrimination of irony (§ "Irony").
- **Faux pas.** GPT-4 was notably below humans ($P = 5.42\times10^{-5}$, $r = 0.55$). GPT-3.5 was near floor on all items except one ($r = 0.72$). LLaMA2-70B outperformed humans ($P = 0.002$, $r = 0.44$), with 100% accuracy in all but one run (§ "Faux Pas").
  - Novel-item pattern was qualitatively similar. Novel items were slightly easier for humans and harder for GPT-3.5. There was no difference for GPT-4 and LLaMA2-70B ($P > 0.462$; BF10 0.77 and 0.43). GPT-3.5's worse score on novel items is not explained by familiarity with the originals, since it did poorly on the originals (§ "Faux Pas").
- **Hinting.** GPT-4 was better than humans ($P = 0.040$, $r = 0.32$). GPT-3.5 did not differ from humans ($P = 0.626$, BF10 0.33). LLaMA2-70B was below humans ($P = 5.42\times10^{-5}$, $r = 0.57$) (§ "Hinting").
  - Novel items were easier for humans and LLaMA2-70B, not different for the GPT models. Because easier novel items are the opposite of what a familiarity explanation predicts, the authors infer item difficulty explains the LLaMA2 difference (§ "Hinting").
- **Strange stories.** GPT-4 significantly outperformed humans ($P = 1.04\times10^{-5}$, $r = 0.60$). GPT-3.5 did not differ ($P = 0.110$, BF10 0.47). LLaMA2-70B was lower ($P = 0.005$, $r = 0.41$). No model differed between original and novel items (all $P > 0.085$) (§ "Strange stories").

*Intuition note:* GPT-4 matched or beat humans on four of the five tests, and the faux pas test is the exception. LLaMA2-70B shows the opposite profile there, which is why the authors look closely at this test.

### Results — Understanding faux pas
- A faux pas story has a speaker who says something they should not have said, not knowing or realising it. Understanding it requires two mental states: the speaker does not know, and the hearer would feel hurt (§ "Understanding faux pas").
- Example (curtains story): Lisa calls Jill's newly bought curtains horrible. Four questions follow. The key fourth question asks whether Lisa knew that the curtains were new, and the correct answer is always "no" (§ "Understanding faux pas").
- Both GPT models correctly saw that the victim would be hurt. But on the speaker-knowledge question, the overwhelming majority of errors said there was not enough information. Only 2 of 349 responses said the speaker did know (§ "Understanding faux pas").
- **Three hypotheses** for GPT's failure (§ "Understanding faux pas"):
  1. *Failure of inference:* the models cannot infer the speaker's mental state, because this needs information outside the story, such as social norms.
  2. *Buridan's ass:* the models can generate the right answer as one option but cannot rank alternatives. Partial support: responses sometimes list "may not know" among alternatives.
  3. *Hyperconservatism:* the models can infer and rank "didn't know" as likeliest, but refrain from committing, out of excess caution. The authors say it is possible that inhibitory mitigation processes in GPT could lead to such an overly conservative stance.
- **Faux pas likelihood test:** ask whether it is more likely that the speaker knew or did not know. If unsure or wrong, prompt for the most likely explanation. Predictions: hyperconservatism gives correct "didn't know"; Buridan's ass gives several equal alternatives; failure of inference gives no right answer at all (§ "Understanding faux pas").
- Result: GPT-4 was perfect, always unprompted. GPT-3.5 improved but needed prompting in about 3% of items and missed the faux pas in about 9% (§ "Understanding faux pas").
- Conclusion (author): this supports hyperconservatism. The failure on the original question reflects an overly conservative approach, not failed inference or indecision among equally plausible options (§ "Understanding faux pas").

*Intuition note:* The models could say what was likeliest when asked a likelihood question. They declined when asked a flat yes/no question about the speaker's knowledge. The gap was in committing, not in being able to infer.

### Results — Testing information integration
- Confound (author's): every faux pas item has the answer "didn't know". A model biased to say "didn't know" would score perfectly without using the story. This could explain LLaMA2-70B's original result and GPT's likelihood-test result (§ "Testing information integration").
- **Belief likelihood test:** for each of six stories, three variants differ only in the final utterance: *faux pas* (speaker seems not to know), *neutral* (no hint either way), *knowledge-implied* (speaker seems to know). All items were new. Each item was given separately: LLMs 15 times per item, humans N = 900 in total (§ "Testing information integration"; Methods).
- Prediction: with real discrimination, "didn't know" should predominate for faux pas and "knew" for knowledge-implied, relative to neutral. If not, the responses are probably driven by a bias or heuristic unrelated to the story (§ "Testing information integration").
- Coding: $-1$ didn't know, $0$ unsure, $+1$ knew; the average is the "direction score" (§ "Testing information integration"; Fig. 2 caption).
- Results (§ "Testing information integration"):
  - *Humans:* both contrasts significant (faux pas vs neutral $\chi^2(2) = 56.20$; knowledge-implied vs neutral $\chi^2(2) = 143$). Uncertainty was higher in neutral (28/303) than faux pas (11/303) or knowledge-implied (0/298).
  - *GPT-4:* both contrasts significant ($\chi^2(2) = 109$; $\chi^2(2) = 18.10$, $P = 3.57\times10^{-4}$). It reported uncertainty most in neutral (42/90, versus 6 and 17 in the other variants).
  - *GPT-3.5:* both contrasts significant ($\chi^2(1) = 8.44$; $\chi^2(1) = 21.50$). It never reported uncertainty.
  - *LLaMA2-70B:* faux pas vs neutral significant ($\chi^2(1) = 20.20$), but no neutral vs knowledge-implied difference ($\chi^2(1) = 1.80$, $P = 0.180$, BF10 0.56). It never reported uncertainty.
- Apparent response bias (LLaMA2-70B and, to a lesser extent, GPT-3.5) on question 1 (whether somebody said something they should not have said): all LLMs said yes in the faux pas condition (humans 83.61%). GPT-3.5 said yes more often than humans in the neutral (71.11%) and knowledge-implied (87.78%) conditions. LLaMA2-70B always said yes. Only GPT-4 gave proportions similar to humans in these two conditions (GPT-4: 15.47% and 27.78%; humans: 19.27% and 30.10%; the source's wording for these figures is ambiguous, see Reading notes) (§ "Testing information integration").

*Intuition note:* A fair test must include cases where the answer is not always "didn't know". Humans, GPT-4 and GPT-3.5 shifted their answers when the story changed. LLaMA2-70B did not shift between neutral and knowledge-implied, so it may just lean towards "didn't know".

### Discussion
- The multi-test, multi-session, fair-comparison design exposed deviations from human behaviour that a single test or single run would have hidden (§ "Discussion").
- GPT-4 exceeded humans on irony, hinting and strange stories. Both GPT models failed only on faux pas, whereas LLaMA2-70B, otherwise the weakest, beat humans there (§ "Discussion").
- The likelihood and belief-likelihood experiments, in the authors' reading, show GPT models can identify unintentional offence as most likely but do not commit to it by default. They note this is consistent with evidence that GPT models have become more reluctant to answer opinion questions over time (§ "Discussion").
- **Possible explanations (hedged by the authors):**
  - The pattern may be the result of GPT's mitigation measures (against hallucination and overreliance). Faux pas requires committing to an explanation lacking full evidence. Hinting allows open-ended speculation, which LLMs suit (§ "Discussion").
  - Humans generally find social uncertainty aversive, and ToM helps them reduce it. GPT models respond conservatively despite having tools to reduce uncertainty. This echoes evidence that LLMs reason well about beliefs but struggle to turn this into decisions and actions (§ "Discussion").
  - Competence vs performance: GPT may be competent at mentalistic inferences yet not compute them spontaneously to reduce uncertainty. Quantitative scoring can miss this (§ "Discussion").
  - Being designed to imitate human outputs does not imply human-like cognition. Humans and GPT may trade off uncertainty cost against deliberation cost differently. LLMs do not operate in an environment, so the authors say they may gain little from narrowing future predictions (§ "Discussion").
  - Speculation: dis-embodied cognition "could explain" faux pas failure, and might also underlie false-belief success, since an agent without its own self-perspective may find tracking a story character's belief less challenging (§ "Discussion").
- Future work: effects of such behaviour on real-time human–machine interaction. Open models allow targeted probing of social reasoning (§ "Discussion").

### Methods
- **Models and sessions:** GPT-3.5 (default at testing) and GPT-4. Each test was run in a separate chat, which is a blank slate. LLaMA2-Chat used fixed settings: a system prompt calling it a helpful AI assistant, temperature 0.7, 512 new tokens, repetition penalty 1.1, top-P 0.9, with LangChain memory within a session (§ "Experimental model details").
  - Uncodable LLaMA2 responses were regenerated. They were rare for 70B but common for 13B and 7B, so only 70B is reported in the main text (§ "Experimental model details").
  - 15 sessions per LLM per test (Table 1: 75 per model for the battery). Humans: Prolific, native English speakers aged 18–70, no psychiatric history or dyslexia, about 50 per test. 13 were excluded as apparent LLM-users or non-answerers. Final N = 1,907 (§ "Experimental model details").
- **Battery** (§ "Theory of mind battery"):
  - *False belief:* A hides an item, leaves, B moves it, A returns. Where will A look? A true-belief control moves a different item, to rule out a recency effect. Four sandbox-task scenarios plus three novel items.
  - *Irony:* 12 items adapted from an eye-tracking study, scored 1/0. Internally contradictory answers (a "yes" followed by an explanation saying they did not believe it) were coded by whether the explanation showed appreciation of irony.
  - *Faux pas:* 10 original plus 5 novel items. Original scoring needs all four questions right. The authors coded only the last question (correct = "no"), because several humans seemed to fail question 1 from an apparent unwillingness to blame.
  - *Hinting:* 10 original plus 6 novel items. Binary coding with no additional prompting, which the authors say gives more conservative estimates than earlier studies.
  - *Strange stories:* 8 original plus 4 novel stories, 0–2 points each (maximum 24), converted to proportions.
- **Protocol:** original items first, novel items last, same preamble. Humans typed free-text answers (§ "Testing protocol").
- **Faux pas likelihood test:** the question was reworded, e.g. asking whether Richard more likely remembered or did not remember the fact. A follow-up prompt was added for unclear wrong answers. Scoring: 2 points unprompted correct, 1 after a prompt, 0 otherwise, rescaled to proportions (§ "Faux pas likelihood test").
- **Belief likelihood example:** Michael's reunion story. Amanda either says she hopes an awkward, poetry-writing classmate is not there tonight (faux pas), asks where the bar is (neutral), or asks whether he still writes poetry (knowledge implied). Items were kept independent across variants (§ "Belief likelihood test").
- **Coding:** five experimenters coded; 20% double-coded. Initial agreement was over 95% (lowest, above 88%, for strange stories in humans and GPT-3.5); disagreements were settled by group review. Ambiguous human belief-likelihood answers (~2.5%) were coded "knew" if affirmative, "didn't know" if negative (§ "Response coding").
- **Statistics:** scores were scaled to proportions per session. Wilcoxon effect size is $r = Z/\sqrt{N}$, with bootstrapped 95% CIs (1,000 iterations). Non-significant results got Bayes factors (BF10, Cauchy prior $r = 0.707$, JASP). False belief was not tested inferentially because of ceiling. Belief likelihood used chi-square tests (8, Holm-corrected) on response-type counts (§ "Statistical analysis").
- **Limit of the novel-item control (author's):** poorer scores on novel items would indicate training-set inclusion. It is convincing for open-ended hinting and strange stories but of limited strength for false belief and faux pas, whose regular structure allows heuristic ("Clever Hans") solutions (§ "Novel items").

## Toy example (ours, not from the text)
Aim: show why the belief likelihood test unmasks a bias. Imagine 10 responses per variant from two hypothetical models, coded $-1$ (didn't know), $0$ (unsure), $+1$ (knew).

**Model A (tracks the story).**
- Faux pas: 8 × (−1), 1 × 0, 1 × (+1). Direction score $=(-8+0+1)/10=-0.7$.
- Neutral: 4 × (−1), 3 × 0, 3 × (+1). Score $=(-4+0+3)/10=-0.1$.
- Knowledge-implied: 1 × (−1), 0 × 0, 9 × (+1). Score $=(-1+0+9)/10=+0.8$.
- Scores run from negative to positive across the three variants, so Model A discriminates.

**Model B (always answers "didn't know").**
- All three variants: 10 × (−1). Score $=-10/10=-1.0$ in each.
- It would score 100% on the original faux pas test (the correct answer is always "no"). But it shows no difference between neutral and knowledge-implied, as LLaMA2-70B did.

Lesson: perfect performance on a one-answer test cannot separate Model A from Model B. Varying the story can.

## Concepts
- [[theory of mind / mentalizing / mindreading]] — ability to track others' mental states; here treated as a set of interconnected notions, not one construct (§ "Main")
- [[first-order false belief]] — predicting that an agent acts on a belief that differs from reality (§ "False belief")
- [[unexpected transfer task]] — the false-belief format used: item moved while the protagonist is away (§ "False belief", Methods)
- [[implicit vs explicit ToM]] — early, efficient but inflexible implicit processes vs later, flexible, demanding explicit abilities (§ "Main")
- [[recursive mindreading / orders of intentionality]] — strange stories include second- or higher-order states (one character's knowledge of another's belief) (§ "Strange stories" in Methods)
- [[clever-hans-effect]] — heuristic solutions possible in tests with regular structure, such as false belief and faux pas (§ "Novel items")
- [[data contamination]] — novel items written to control for test items being in training data (§ "Performance across theory of mind tests")
- [[construct validity in LLM evaluation]] — here: systematic, multi-test, human-benchmarked comparison to make a non-superficial claim (§ "Main")
- [[machine theory of mind]] — LLM performance on ToM tasks; the authors speak of an artificial theory of mind (§ "Main")
- [[faux-pas-recognition]] (new) — recognising that a speaker unknowingly said something hurtful; needs two mental states (§ "Understanding faux pas")
- [[hyperconservatism-hypothesis]] (new) — models can infer the likeliest mental state but refuse to commit to it (§ "Understanding faux pas")
- [[belief-likelihood-test]] (new) — faux pas / neutral / knowledge-implied variants testing whether answers follow the story (§ "Testing information integration")
- [[competence-vs-performance]] (new) — the capacity to compute inferences vs. whether it is used spontaneously (§ "Discussion")
- [[species-fair-comparison]] (new) — presenting tests to LLMs and humans in matched written format (§ "Theory of mind battery")

## Canonical instances
- [[curtains-faux-pas-story]] — Lisa and Jill's curtains; the key question "Did Lisa know…?" (§ "Understanding faux pas")
- [[sandbox-false-belief-task]] — A hides item, leaves; B moves it; where will A look? (Methods: False belief)
- [[buridans-ass]] — rational agent between two equal hay bales; used as a hypothesis name (§ "Understanding faux pas")
- [[michael-reunion-story]] — three-variant belief likelihood item (Methods: Belief likelihood test)
- [[false-belief-perturbations]] — transparent containers etc.; humans failed half (§ "False belief")

## Bridges (candidates)
- [structural-analogy] Hyperconservatism ↔ speed–accuracy / decision-threshold trade-offs: refusing to commit despite knowing the likeliest option resembles a very high commitment threshold; the paper itself frames it as cost of uncertainty vs cost of deliberation.
- [structural-analogy] Belief likelihood test's manipulation of evidence ↔ cue-manipulation controls in psychophysics: shift the input, check the response shifts.
- [metaphor] Competence vs performance ↔ capacity vs use of a skill in linguistics-style debates.
- [structural-analogy] Novel-item control ↔ held-out test set in machine learning, meant to detect memorisation.

## Questions this raises
- Does the likelihood framing itself make the question easier in a way humans would also benefit from, and how would humans do on the original yes/no versus likelihood wording?
- If hyperconservatism comes from mitigation measures, would a model without such training commit to answers (the authors suggest open models allow such tests)?
- Why did LLaMA2-70B always say that someone had said something they should not have said, and how general is that response bias?
- How would human participants react in live interaction to an agent that declines to commit (the authors raise this as open)?

## Reading notes
- Source is the PMC HTML version (Nature Human Behaviour 8(7):1285–1295, 2024; published online 20 May 2024). It has no printed page numbers, so citations use section headings. The source was said to be about 12,777 words. Figures were not available as images; only captions and text were used.
- The reported "Z" values (e.g. $Z=0.00$ with $r=0.32$ for GPT-4 on irony and hinting) cannot be the $Z$ used in $r=Z/\sqrt N$ described in Methods, since $Z=0$ would give $r=0$. The source does not explain this. I report $P$ and $r$ and omit $Z$.
- Irony and hinting GPT-4 results share identical $Z$ and $P$ but different CIs. This may be coincidence; I could not check.
- Fig. 1b caption gives 49 humans for false belief; the text mentions 51 (5 of 51 with errors). The source does not explain the difference.
- Methods says the LLaMA2 models were trained on sets of different sizes: 70, 13 and 7 billion tokens. The numbers presumably refer to model parameters, but I report only what the source says.
- In the last paragraph of "Testing information integration", the wording for GPT-4 (15.47% and 27.78%) says that GPT-4 reliably reported no offensive statement. The numbers look like the proportions reporting an offensive remark (matching humans' 19.27% and 30.10%, and contrasting GPT-3.5's 71.11% and 87.78%). I report them as given and flag the ambiguity.
- The sentence saying GPT-4 was more likely to report uncertainty in the neutral condition than responding randomly is unclear in the source; I report only the counts.
- Many results (novel-item analyses for false belief, LLaMA2 7B/13B, order effects, qualitative analyses) are in the Supplementary Information, which was not provided.
