---
id: bai-2022-constitutional/main
work: bai-2022-constitutional
unit: paper
pages: 1-34
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Constitutional AI: Harmlessness from AI Feedback

## L0 — One line
A helpful language model can be trained to be relatively harmless, with a short written list of principles as the only human harmlessness supervision, by letting a model critique, revise and rank its own outputs instead of using human harmlessness labels.

## L1 — The gist (≤ 120 words)
Can an AI assistant be made harmless without human labels that mark harmful outputs? The authors use a short list of written principles (a "constitution"). In a supervised stage, a helpful model critiques and revises its own harmful answers, then is fine-tuned on the revisions. In an RL stage, a model chooses the more harmless of two responses according to a principle; these AI labels train a preference model, which is the reward for RL (RLAIF). Crowdworkers judge the resulting models more harmless than RLHF models at similar helpfulness, and the authors find them virtually never evasive. It matters as a test of using AI to help supervise AI.

**Prerequisites:** RLHF basics (preference model as reward, policy trained by RL); few-shot and chain-of-thought prompting; Elo scores from pairwise comparisons; the idea of "red teaming" (writing prompts that bait a model into harm).

## L2 — Key ideas (5–10 bullets)
- **Two-stage method.** A supervised stage (critique → revision → fine-tune, "SL-CAI") is followed by an RL stage with AI-made harmlessness labels ("RL-CAI", i.e. RLAIF). For harmlessness, human supervision is only the principles plus a few few-shot examples; helpfulness labels are still human (pp. 2, 5, 15).
- **Models can already judge harm.** On 438 binary HHH comparisons, larger models do better and chain-of-thought helps. The Figure 4 caption says the trends suggest models larger than 52B will be competitive with human-feedback preference models (pp. 5–7).
- **Revisions reduce harm.** Repeated critique-and-revision raises harmlessness PM scores (with a caveat about PM calibration) while pure helpfulness PM scores fall (pp. 8–9).
- **Critiques help mainly small models.** Critiqued revisions beat direct revisions for small models and are about equal for large ones; the authors keep critiques partly for transparency (p. 10).
- **AI labels become PM training data.** The feedback model's normalized log-probabilities over "(A)/(B)" become soft targets. With chain-of-thought, targets are clamped to 40–60% (pp. 10–13).
- **Better harmlessness–helpfulness trade-off, less evasion.** RL-CAI models sit above the RLHF trade-off curve in crowdworker Elo and are virtually never evasive. Over-training can cause Goodharting-style boilerplate (pp. 3, 12–13).
- **Caveats stated by the authors.** Principles were chosen ad hoc; absolute harmfulness scores may be poorly calibrated; the method is dual-use and may reduce human testing (pp. 2, 14–16).

## L3 — Walkthrough

### Abstract, Figure 1 and §1 Introduction (pp. 1–5)

**Aim.** The authors want AI that stays helpful, honest and harmless even if some capabilities reach human level. They therefore want techniques that do not need humans to supervise every aspect of behaviour (p. 2). They train a non-evasive and relatively harmless assistant without any human feedback labels for harms (p. 2). They say the method improves upon, and partially replaces, RLHF (p. 2). The word "constitutional" means that a short list of principles drives training. It also signals that any deployed AI must be governed by some principles, even if hidden or implicit (p. 2).

**Figure 1 (p. 2).** Top row (SL stage): a helpful RLHF model answers red-teaming prompts, then Response → Critique → Revision, giving the fine-tuned SL-CAI model. Bottom row (RL stage): SL-CAI generates response pairs. Constitutional AI feedback produces a preference model (PM). RLAIF training with PM + SL-CAI gives the final RL-CAI model. The caption says the SL stage improves the initial model and gives some control over initial behaviour, addressing potential exploration problems (p. 2).

**1.1 Motivations (pp. 2–4).** Four motivations: (1) study using AI to help supervise AI ("scaling supervision"); (2) remove evasive responses and reduce the helpfulness–harmlessness tension; (3) make governing principles more transparent; (4) save iteration time, since changing the objective needs no new human labels (p. 2).
- Footnote 1 defines the tension: helpfulness tends to raise harmfulness, because models obey pernicious requests. Harmless-trained models tend to be evasive. Harmfulness includes harm to the user and help given for harmful aims (p. 2).
- *Scaling supervision* means using AI to help humans supervise AI more efficiently. The authors say it may work **if** the supervisor's capability scales with the actor's **and** the supervisor stays aligned. They also warn that it could further automate, and possibly obscure, decision making. Chain-of-thought is used to make decisions more legible (p. 3).
- RLHF typically needs tens of thousands of human preference labels. Here human input is reduced "to an extreme" to about ten simple natural-language principles (p. 3). Footnote 2: the principles were chosen ad hoc and iteratively, and in future should be refined by a larger set of stakeholders (p. 3).
- *Non-evasive assistant.* In the prior work, evasiveness was rewarded by crowdworkers, so the assistant refused controversial questions and could stay evasive for the rest of a conversation (p. 4). The goal here is an assistant that always engages and explains why it refuses unethical requests. This should make scaled-up automated red teaming easier (p. 4).
- *Simplicity and transparency.* Encode goals as a list of natural-language principles, use chain-of-thought during training, and train assistants that explain refusals (p. 4).

**Figures 2–3 (pp. 3–4).** Crowdworker Elo scores (higher is better; only differences are meaningful) for helpfulness and harmlessness. Helpful-only and HH RLHF models show a trade-off. The RL-CAI models are less harmful at a given level of helpfulness, which the figure labels a "Pareto improvement" (p. 3). In Figure 3, models are compared across sizes (p. 4). The caption of Figure 2 notes that crowdworkers were told to prefer less evasive responses when both were equally harmless. This is why the HH and helpful RLHF models differ less in harmlessness Elo (p. 3).

**1.2 The CAI approach (p. 5).** Human supervision comes "entirely" from the principles plus a small number of few-shot examples (p. 5).
- *Supervised stage.* A helpful-only assistant answers harmfulness prompts. The authors expect these initial responses to be quite harmful and toxic. The model critiques the response using a principle, then revises it. This repeats, drawing a random principle each step. A pretrained model is then fine-tuned on the final revisions. The purpose is to shift the response distribution easily and cut exploration and training length in the RL stage (p. 5).
- *RL stage.* The SL model generates a pair of responses per harmful prompt. Each prompt-pair is turned into a multiple-choice question asking which response is best under a constitutional principle. This yields an AI-made harmlessness preference dataset, mixed with human helpfulness data. A PM is trained on it, and the SL model is fine-tuned by RL against the PM. The PM is a "hybrid" human/AI PM: human labels for helpfulness, AI labels for harmlessness (p. 5, with footnote 5).

**1.3 Contributions (p. 5).** (a) AI identification of harms improves with capability, and chain-of-thought improves it, giving evaluations "becoming competitive" with human-feedback PMs (Fig. 4). (b) Critique-revision can be repeated to progressively reduce harmfulness (Fig. 5). Critiques improve harmlessness compared to direct revisions (Fig. 7). (c) RL with self-supervised preference labels improves crowdworker-judged behaviour, "equaling or exceeding" human-feedback harmlessness (Figs. 2–3). A repository with prompts and principles is provided (p. 5).

**1.4 Models and data (p. 6).** Pretrained LMs follow earlier work. The initial helpful models are RLHF models trained only on helpfulness data. Human data from earlier work: crowdworkers pick the more helpful or more harmless of two responses, collected separately. For harmlessness they red-team the model. "HH" models are RLHF models trained on both kinds of data (p. 6). The authors also trained new HH PMs and HH RLHF policies as comparison points (p. 6).

### §2 Evaluating the potential for AI supervision of HHH (pp. 6–7)
- *Test set.* Earlier work provides 221 binary comparisons ranked for helpfulness, honesty and harmlessness. The authors say models now exceed 90% accuracy on these (Figure 11, appendix), so they wrote 217 harder ones, mainly subtle harmlessness cases, including cases where an evasive reply is disfavoured against a harmless, helpful one. Figure 4 uses 438 questions (p. 6).
- *Two formulations.* (i) A PM trained on several hundred thousand human preference labels scores the better response higher. (ii) A pretrained LM or helpful RLHF policy answers a binary multiple-choice question (format in §4.1) (pp. 6–7).
- *Result.* Chain-of-thought improves larger models significantly. Sampling five CoT samples and averaging the probabilities for each answer gives a further small boost (p. 7). In Figure 4 the human-feedback PM is best at every size. At 52B the plain pretrained LM is about 0.68 accurate, CoT about 0.72 and ensembled CoT about 0.73, against about 0.78 for the PM (values read from the figure; approximate). The caption says trends suggest models larger than 52B will be competitive with human-feedback PMs (p. 6).
- Appendix B adds harm-identification results. The authors say these results suggest that increasingly capable LMs should be able to help humans supervise other AIs (p. 7).

> **Intuition note.** The method rests on a measured fact: bigger models, especially when they reason step by step, get better at saying which of two replies is less harmful. In Figure 4, small pretrained models are near chance when judging this way, and the gains appear at larger sizes.

### §3 Constitutional AI: critiques, revisions and supervised learning (pp. 7–11)

**3.1 Method (pp. 7–8).** Steps, shown on the wifi-hacking example (p. 7):
1. Show the helpful RLHF model a red-team prompt. Prompts come from earlier red-teaming work (p. 7).
2. Sample a response (the example's harmful advice is "fabricated", p. 7).
3. Append a pre-written *Critique Request*, asking the model to identify specific ways its last response is harmful, unethical, racist, sexist, toxic, dangerous or illegal, and sample a critique (p. 7).
4. Append a *Revision Request*, asking the model to rewrite its response to remove any and all harmful content, and sample a revision (p. 7).
5. Join the prompt with the revised response. In the example, the revision says hacking invades privacy, advises against it and warns of legal trouble (p. 7).

Because the prompt-revision pair has the same format as a prompt-response pair, the loop can be applied repeatedly. A critique + revision instruction pair together form one "principle" (p. 7).
- There are 16 principles related to harmlessness. Some are general, some target specific areas. One is sampled randomly at each revision step of each prompt (p. 8). Footnote 7: they were selected ad hoc.
- The model sometimes confuses its role (e.g. writes a critique where a revision is expected). This was fixed by few-shot examples in a uniform format (App. E, p. 8).
- Qualitatively: the original response often contains harmful content. The first revision "almost always" removed most harm. Later revisions sometimes helped further, but this was less clear by inspection. Revisions were rarely evasive (p. 8).
- The pretrained model is fine-tuned on revisions from all revision steps. To retain helpfulness, responses from the helpful RLHF model on helpfulness prompts are added. The result is "SL-CAI" (p. 8).

**3.2 Datasets and training (p. 8).**
- Red-team prompts: 42,496 human-written plus 140,335 generated by few-shot prompting a pretrained model, a total of 182,831. Check: $42{,}496 + 140{,}335 = 182{,}831$ (added step).
- Per red-team prompt, 4 critique-revision pairs were sampled, giving 4 revisions per prompt.
- Helpfulness prompts: 135,296 human-written, none model-generated, with 2 responses sampled per prompt from a helpful RLHF model.
- Temperature $T=1$ throughout. SL-CAI is trained for one epoch with a constant learning rate of 0.5 relative to the pretraining rate and batch size 1024 sequences (p. 8).

**3.3 Main results (pp. 8–9).** Elo scores come from crowdworker comparison tests, following earlier work (p. 8). Each conversation is written by the crowdworker. At each step two responses from two models get a preference label. A total of 10,274 helpfulness and 8,135 [word missing in source; presumably harmlessness] comparisons were collected across 24 snapshots (p. 8).
- The helpful RLHF model is more helpful but more harmful than HH RLHF. SL-CAI is less helpful than both RL models, more harmless than helpful RLHF and more harmful than HH RLHF (p. 8).
- SL-CAI is both more helpful and more harmless than pretrained models (p. 9).
- Footnote 8: harmlessness Elo scores of the RLHF models are closer together than in earlier work. The authors suspect this is because crowdworkers were told to prefer thoughtfully harmless over evasively harmless responses (p. 8).

**3.4 Scaling trends (p. 9).**
- *Number of principles* ($N = 1, 2, 4, 8, 16$; Fig. 6). More principles do not appear to change the harmlessness PM score. The authors expect more principles to give more diverse behaviours, which helps RL exploration, but did not study this quantitatively (p. 9).
- *Number of revisions* (Fig. 5; PMs trained only on human feedback, 52B). Harmlessness and HH scores rise monotonically with revisions (revision 0 is the initial response). Pure helpfulness scores fall. PM scores are less calibrated at high values, so the authors say the results should be treated with caution (p. 9).
- SL-CAI-$n$ is fine-tuned on revisions up to and including the $n$-th, for $n = 1,\dots,4$ (p. 9).

**3.5 Are critiques necessary? (p. 10).** Compare critiqued revisions with direct revisions (Fig. 7, same 52B harmlessness PM).
- Critiqued revisions score better for small models. For large models there is no noticeable difference (the caption adds that critiques are "always slightly better").
- Inspection of 52B samples: critiques were sometimes reasonable but often inaccurate or overstated. Revisions were still generally more harmless than the originals.
- Critiques are used anyway, since they may give more transparency into the model's reasoning and may help uncover subtle harms (p. 10).

> **Intuition note.** The SL stage works as a data-generation trick: the model rewrites its own bad answers under a rule, and then we train on the rewrites. For big models the PM scores barely differ with or without critiques, but the authors keep critiques because they may give more transparency.

### §4 Constitutional AI: RL from AI feedback (pp. 10–14)

**4.1 Method (pp. 10–11).** Human harmlessness labels are replaced by labels from a "feedback model" (typically a pretrained LM). The rest of the pipeline (PM training, RL) is exactly the same as in RLHF (p. 10).
- The assistant generates a pair of responses. The feedback model sees the conversation, a principle, and options (A) and (B), ending with "The answer is:" (p. 10).
- The log probabilities of "(A)" and "(B)" are computed, and the normalized probabilities become the PM comparison targets. The authors expect these to be fairly well calibrated for multiple-choice answers (p. 10). In symbols (added step, my formalisation): with log probabilities $\ell_A,\ell_B$, the soft target is $p_A = e^{\ell_A}/(e^{\ell_A}+e^{\ell_B})$, $p_B = 1-p_A$.
- Pretrained models are the feedback model in this section's main experiments (p. 11).
- 16 principles are written for this stage (App. C.2). One is sampled at random per comparison. Qualitatively, ensembling over principles gave more robust PM behaviour than one fixed principle. Few-shot labelled examples are prepended, each with an independently sampled principle (p. 11).
- SL-CAI generates the response pairs and is the RL initial snapshot. The authors suspect this gives better results, since the policy's responses resemble the PM's training distribution, at least early in RL. The PM is trained on human helpfulness labels mixed with AI harmlessness labels (p. 11).
- *Chain-of-thought variant.* The helpful RLHF model is used as feedback model, because the authors say it typically writes higher quality chain-of-thought. Prompts use Human:/Assistant: format and the phrase "Let's think step-by-step", plus hand-written few-shot examples (p. 11; App. E.2).
- CoT samples usually state which option wins, so probability targets are near 0 or 1 and not well calibrated. Clamping the CoT probabilities to the 40–60% range gave better, more robust behaviour. Without clamping, RL-CAI models learned to output more extreme responses (p. 11).

**4.2 Datasets and training (p. 11).** RL hyperparameters follow earlier work. Differences: current RLHF models are fine-tuned directly from pretrained models (no context distillation), and the pretrained LMs are improved. PM data: 135,296 human helpfulness comparisons and 182,831 constitutionally generated harmlessness comparisons (one per SL-CAI prompt). All RL runs use the same prompts: those used for SL-CAI plus 491,142 extra model-generated red-team prompts and 474,300 extra helpfulness prompts (p. 11).

**4.3 Main results (pp. 12–13).**
- RL-CAI models are "significantly more harmless" than RLHF and SL-CAI models (Figs. 3, 8). RL-CAI with CoT seems slightly less helpful but slightly more harmless than RL-CAI without CoT (p. 12).
- Figure 2 shows a rough outline of a Pareto frontier for each model. Figure 9 shows the feedback model's log-probabilities are reasonably well calibrated on the new HHH eval (p. 12).
- *Over-training.* RL-CAI can be over-trained, giving Goodharting behaviour: responses overly harsh, or boilerplate such as "you are valid, valued, and cared for". Two sample outputs are shown, on racial superiority and terrorism (p. 13).
- *Strategies that qualitatively gave more diverse, higher-quality responses* (p. 13): rewriting principles to avoid over-reactive or accusatory choices; ensembling over 16 principles; and soft labels. For RL-CAI without CoT, soft labels (normalized log-probabilities) gave "much better results" than hard 0/1 labels. The authors suspect this is because soft labels are fairly well calibrated. With CoT, soft labels could not be extracted directly without sampling multiple CoTs per label. Clamping at 20–80% slightly improved results and 40–60% improved more, so 40–60 is used for the main results (p. 13).

> **Intuition note.** A label of "0.73 for A" carries the feedback model's uncertainty, which a hard "A wins" throws away. A written chain of thought makes the model commit, so its probabilities are near 0 or 1 and poorly calibrated; clamping them to 40–60% worked better in the authors' tests.

**4.4 Harmlessness vs. evasiveness (pp. 13–14).**
- Earlier HH RLHF models were often evasive, giving canned refusals. The authors want transparency and expect non-evasive answers to fit better with helpfulness. They find RL-CAI "virtually never evasive" (p. 13). Appendix D gives samples.
- In Figure 8 (right), the helpful and HH RLHF harmlessness Elos decline late in training. For helpful RLHF this is likely because the model becomes more willing to help with dangerous tasks. For HH RLHF the authors *suspect* growing evasiveness, which crowdworkers were told to rank below nuanced, transparent responses when both are similarly harmless (p. 13).
- In earlier work workers simply chose the more harmless response, probably producing data favouring evasiveness. The HH PM data used here come from that period and likely reward evasiveness (p. 13, footnote 9 adds a second possible cause).
- The new instructions apply only to the comparison tests behind this paper's Elos (p. 14). This may explain why the helpful-vs-HH harmlessness gap is much smaller than in earlier work. Also, earlier work mostly used Upwork and MTurk. Here the PM data come from that period, but the tests used Surge AI workers (p. 14).

**4.5 Absolute harmfulness score (p. 14).** In earlier red-teaming data, a worker chats with a single model and finally rates their "success" at eliciting harm on an integer scale 0–4. The authors fine-tuned an LM to predict this score from the full conversation using an L2 loss, as an extra metric. Evaluation: 64 hand-picked held-out red-team prompts, 256 responses per prompt (Fig. 10). Helpful RLHF becomes more harmful during training. HH RLHF, RL-CAI and RL-CAI with CoT become progressively less harmful. Caveat: absolute scores may be poorly calibrated, since workers have personal biases on the 0–4 scale (p. 14).

### §5 Related work (pp. 14–15)
CAI is presented as an extension of RLHF and similar to LaMDA, InstructGPT and Sparrow in using human data to align LMs. Prior self-critique and natural-language-feedback work uses methods the authors call very similar to their supervised constitutional step. Sparrow's decomposition of harmlessness into areas resembles using principles. The paper also builds on chain-of-thought, red-teaming work, and the finding that LMs make well-calibrated choices. Scaling supervision has been proposed for alignment (e.g. debate, amplification) (pp. 14–15).

### §6 Discussion (pp. 15–16)
- Two methods were established: (1) CAI bootstraps a helpful RLHF model's instruction-following to critique and revise itself; (2) RL with model-generated harmlessness labels. They give harmless, non-evasive models, "partially resolving" an earlier issue (p. 15).
- Helpfulness labels are still human. The authors *expect* helpfulness could be obtained without human feedback from a pretrained LM and extensive prompting, but leave it to future work. The ultimate goal is to make human supervision more efficient, transparent and targeted, not to remove it (p. 15).
- *Future directions* (6.1): the methods may steer style, tone, personality, or responses to specific question categories. Cheaper labels could allow feedback along dozens of behavioural axes, to study how PMs trained on them correlate. Robustness to red-team attacks is a major motivation. Iterated "online" training with AI feedback could be fully automated (pp. 15–16).
- *Broader impacts* (6.2): dual use. The methods lower the barrier to training systems that behave as their creators intend, including pernicious ones. The SL methods may be especially accessible since they need no efficient RL implementation. Less human feedback may also let developers deploy insufficiently tested systems. A stated benefit is less need for human red teamers doing "unsavory work" (p. 16).
- §7 (Contribution Statement) and Acknowledgments, pp. 16–17, list roles and thanks; not summarised.

### Appendices (pp. 18–34)
- **A. Sample critiques/revisions (pp. 18–19).** All from the 52B helpful RLHF model, which gives inaccurate critiques often. The first revision often removes most harm and later ones make minor improvements. Example (grocery-store theft): the initial answer gives practical theft tips. The 1st critique flags it as harmful and the 1st revision refuses and points to assistance programs and food banks. The 2nd critique calls the response "perfect" and the revision barely changes it. The 3rd critique asks for stronger discouragement and the 3rd revision adds a plain request not to commit a crime The 4th critique worries that discussing illegality may be too intense for young children, and the 4th revision drops the legal talk (p. 19).
- **B. Identifying and classifying harm (pp. 19–20).** From Ganguli et al. red-team data. Task 1: a balanced set of 254 conversations in which both the crowdworker and an independent reviewer gave the minimum or maximum harmfulness score (1–5 scale); models say whether the assistant's behaviour was harmful or ethical. The human was typically harmful (red teaming), which may make the task harder for small models or zero-shot use. Chain-of-thought and few-shot evaluation significantly improve on zero-shot (Fig. 12 left). Task 2: 9-way classification of harm type, using the nine most frequent crowdworker labels, 287 examples (Fig. 12 right). Both suggest AI evaluation of harm will become more tractable as models improve (p. 20).
- **C. Principles (pp. 20–23).** C.1: 16 critique/revision request pairs for SL-CAI. They cover general harm, social bias, criminal advice, age-appropriateness, gender bias, and responding as a thoughtful, empathetic friend or therapist would. C.2: 16 single-sentence choice principles for RL-CAI. Several warn against preachy, over-reactive or condescending answers. One asks for the response a peaceful, ethical and wise person might give, naming Martin Luther King Jr. and Mahatma Gandhi (pp. 22–23).
- **D. Many more samples (pp. 23–29).** Side-by-side 52B HH RLHF vs RL-CAI CoT on PALMS sensitive questions, LaMDA prompts and InstructGPT prompts. HH RLHF often gives a short refusal, while RL-CAI CoT engages and explains. The authors find RL-CAI CoT similarly harmless but significantly less evasive than both versions of HH RLHF. They warn that some InstructGPT samples were likely cherry-picked for poor behaviour, so comparisons may be unfair (p. 23, 27).
- **E. Few-shot prompts (pp. 29–34).** E.1: five SL-CAI examples with critique and revision; the source says most are about harmlessness and one is an additional helpfulness example (the general-relativity one, whose critique request asks about truthfulness and confidence) (pp. 29–31). E.2: six chain-of-thought labelling examples, each with a `[[PRINCIPLE]]` slot and step-by-step reasoning ending in a chosen option (pp. 31–34).

## Toy example (ours, not from the paper)
**Goal:** turn one AI judgment into a PM training target, with and without CoT.

*Soft label (no CoT).* Suppose the feedback model gives log probabilities $\ell_A=-0.5$ for "(A)" and $\ell_B=-1.5$ for "(B)".
- $e^{-0.5}\approx 0.6065$ and $e^{-1.5}\approx 0.2231$; the sum is $0.8296$.
- $p_A = 0.6065/0.8296 \approx 0.731$, $p_B = 0.2231/0.8296 \approx 0.269$. The target for the PM is (0.731, 0.269): "A is probably better, not certainly".

*CoT label.* The feedback model writes reasoning ending "option (B) is best", and its probabilities become $p_B=0.97$, $p_A=0.03$.
- Clamp to [0.4, 0.6]: $p_B = \min(\max(0.97, 0.4), 0.6) = 0.6$ and $p_A = \max(0.03, 0.4) = 0.4$. The target is (0.4, 0.6).
- With the 20–80 clamp instead, the target would be (0.2, 0.8).
- A label already inside the band, such as 0.55, is unchanged.

Result: clamping keeps the direction of the judgment but limits how confident the PM target can be, which is the effect the authors report as more robust (p. 11, p. 13).

## Concepts
- [[constitutional-ai-rlaif]] — training with written principles, using model critiques/revisions (SL) and model-made preference labels (RL) in place of human harmlessness labels (p. 2).
- [[rlhf]] — RL against a PM trained on human preference labels; here it is the baseline and the source of the helpful model (p. 3).
- [[reward-model]] — the preference model (PM) scoring responses, trained on human helpfulness plus AI harmlessness comparisons (p. 5).
- [[supervised-fine-tuning]] — SL-CAI: fine-tuning a pretrained model on revised responses plus helpful RLHF samples (p. 8).
- [[chain-of-thought]] — "Let's think step-by-step" reasoning used for AI labelling; improves accuracy and transparency (p. 7, p. 11).
- [[zero-shot-few-shot-prompting]] — few-shot examples fix the critique, revision and labelling formats (p. 8, p. 11).
- [[critique-revision]] (new) — loop in which a model critiques its response under a principle, then rewrites it; repeatable (p. 7).
- [[constitution-principle]] (new) — a natural-language rule; for SL, a critique request plus a revision request; for RL, a choice instruction (p. 7, p. 11).
- [[scaling-supervision]] (new) — using AI to help humans supervise AI; may work if supervisor capability scales and stays aligned (p. 2–3).
- [[evasiveness]] (new) — refusing to engage with a sensitive request; harmless but unhelpful and not transparent (p. 4, p. 13).
- [[soft-vs-clamped-preference-label]] (new) — normalized feedback-model probabilities as PM targets; clamped to 40–60% with CoT (p. 10–13).
- [[elo-score]] (new) — rating from crowdworker pairwise preferences; only differences are meaningful (p. 3).
- [[red-teaming]] (new) — writing prompts to bait a model into harmful output (p. 6–7).
- [[goodharting]] (new) — over-training RL-CAI can yield overly harsh or boilerplate responses (p. 12).

## Canonical instances
- [[wifi-hacking-critique-revision]] — worked example of the critique and revision loop on a harmful answer (p. 7).
- [[grocery-theft-four-revisions]] — four sequential critiques and revisions; critiques are sometimes inaccurate (p. 19).
- [[hhh-binary-comparison-eval]] — 438 binary comparisons; LM accuracy grows with size and CoT (p. 6).
- [[pareto-helpful-harmless-plot]] — Fig. 2: RL-CAI vs RLHF trade-off (p. 3).
- [[rl-cai-boilerplate-goodharting]] — two examples of boilerplate reassurance after over-training (p. 13).
- [[palms-hh-vs-rl-cai-samples]] — evasive HH RLHF refusals vs RL-CAI CoT explanations (pp. 23–25).

## Bridges (candidates)
- [structural-analogy] soft AI preference labels distilled into a PM ↔ knowledge distillation: a teacher's probabilities used as training targets (the paper itself says it "distils" LM interpretations of principles into a PM, p. 5).
- [structural-analogy] Goodharting of the PM in RL-CAI ↔ reward over-optimization (cited as Gao et al., p. 12): optimizing a proxy reward too far reduces true quality.
- [structural-analogy] critique-then-revise loop ↔ chain-of-thought as inference-time reasoning: both write intermediate text before the final output, and here the text is also training data.
- [metaphor] constitution as principles ↔ political constitution: the authors use the word partly to stress that any deployed AI is governed by *some* principles (p. 2).
- [structural-analogy] human labellers vs a few written principles ↔ computational social science codebooks for LLM annotation: a short instruction text steers many labels.

## Questions this raises
- The paper says number of principles does not change harmlessness PM score but may raise diversity. How would one measure diversity and its effect on RL exploration?
- Harmlessness PM scores for revisions come from PMs trained on human feedback that likely reward evasiveness (p. 13), and PMs are less calibrated at high scores (p. 9). How reliable is Fig. 5?
- Whose values go into the principles? Footnote 2 says stakeholders should refine them. How would this be done?
- If critiques are often inaccurate yet revisions still improve (p. 10), what exactly does the critique step contribute for large models?

## Reading notes
- Printed page numbers equal pdf page numbers (offset 0). The paper is arXiv:2212.08073v1, 15 Dec 2022, Anthropic.
- No numbered equations. The formulas in L3 and the toy example are marked as added.
- **Possible source misprints/inconsistencies:**
  - §3.3 gives the counts 10,274 helpfulness and 8,135 [unlabelled] comparisons; "harmlessness" appears to be missing before the second count.
  - §2 says models exceed "well over 90%" on the original 221 comparisons, but Figure 11 (p. 20) shows maximum accuracies of roughly 0.8–0.87.
  - §3.4 uses "constitutions" where "principles" is meant.
  - App. E.1 (p. 29) critique says arson is dangerous and illegal and "should be condoned"; "not" appears to be missing.
  - App. E.1 (p. 31) revision request says the assistant is "unstable" to access other sources; "unable" appears intended.
  - Footnote 7 has a stray bracket after "Appendix C".
- The SL-CAI-$n$ results (§3.4) are described but not shown in these pages. Figure 4 values quoted in L3 are read from the image and approximate.
- Appendix E.1 contains flawed assistant text (e.g. the incorrect physics claims in the general-relativity example), used as few-shot material for critique, not as endorsed content.
