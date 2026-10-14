---
id: brown-2020-gpt3/main-p2
work: brown-2020-gpt3
unit: paper (part 2/3) — end of §3.9.5, §3.9.6, §4–§8, Acknowledgements, Contributions, Appendices A–F
pages: 29–49
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# GPT-3, part 2: contamination study, limitations, broader impacts, related work, appendices

## L0 — One line
The authors test whether GPT-3's benchmark scores are inflated by test-set leakage (mostly they are not, with PIQA and Winograd flagged), then list the model's limits, its social risks (bias, misuse, energy) and the technical details behind the work.

## L1 — The gist (≤ 120 words)
This part ends the qualitative demonstrations. It then asks whether benchmark scores are inflated because test data leaked into the training text. The authors build "clean" benchmark subsets using 13-gram overlap. Scores on most benchmarks barely change, but PIQA and Winograd get asterisks. Next come limitations: weak "comparison" tasks, an autoregressive-only design, poor sample efficiency, cost, and unclear what few-shot learning really does. Bias probes (gender, race, religion), misuse and energy follow. Related work and conclusion close the paper. Appendices give data filtering, training settings, overlap tables, compute accounting, human-evaluation details and poem samples.

**Prerequisites:** n-grams; train/test split and overfitting; accuracy/F1/BLEU as scores; log-probability ratios; sampling temperature and top-p (explained briefly below); basic idea of few-shot prompting; autoregressive (left-to-right next-token prediction) versus bidirectional language models; a petaflop/s-day is $8.64\times10^{19}$ flops (p. 46).

## L2 — Key ideas (5–10 bullets)
- GPT-3 gives plausible results on two ad-hoc few-shot tasks (using invented words, grammar correction). The authors flag that "good English" is contested and that one correction changed meaning ("cheap" was dropped) (pp. 29–30).
- Because training data is scraped from the internet, benchmark test sets may be in it. A bug left the removal of detected overlaps only partial, and retraining was too costly. The authors therefore audit after the fact (p. 31).
- Audit method: score GPT-3 on "clean" subsets (no 13-gram overlap with the training set) and compare with the full score. Most benchmarks change negligibly, and no correlation between contamination level and score change was seen (p. 31).
- Case-by-case review leads to asterisks on PIQA and Winograd and to dropping the Wikipedia language-modeling benchmarks and the Children's Book Test. The authors admit the clean subset may differ in distribution from the full set (pp. 32–33).
- Limitations: text drift and repetition, weak on "comparison" tasks (WiC, ANLI), no bidirectional model, a per-token-equal objective that may hit limits, poor pre-training sample efficiency, and unclear whether few-shot learning learns tasks or recognises them (pp. 33–34).
- Bias probes show the model reflects stereotypes of its training data: gender–occupation, appearance words for women, differing sentiment by race, and associations with religions. The authors call this a preliminary analysis (pp. 36–39).
- Misuse assessment: threat actors showed little deployment so far, and the authors suspect that more consistent, steerable models may eventually attract more interest from malicious actors (p. 35). Training compute was several thousand petaflop/s-days, but inference is cheap per page (p. 39).
- The appendices make the work reproducible: Common Crawl quality filter and deduplication, optimiser and schedule, overlap statistics for 42 benchmarks, a FLOP-counting rule, and human-detection experiment details (pp. 43–49).

## L3 — Walkthrough

### 3.9.5 (end) Learning and using novel words (p. 29)
- This part begins mid-section. Figure 3.16 shows six prompts, each defining an invented word and asking for a sentence using it (whatpu, farduddle, yalubalu, Burringo, Gigamuru, screeg) (p. 29).
- The first example (whatpu) is fully human-written and serves as conditioning. GPT-3 wrote the other five (p. 29).
- The task is few-shot with respect to the broad task and one-shot with respect to each specific word. The definitions were human-written (p. 29).
- The examples were generated in one sitting; the authors say they omitted no prompts and did not retry any (p. 29).
- In all cases the sentence appears correct or at least plausible. For "screeg" the model produced the conjugation "screeghed". The use (the verb followed by "at each other") is slightly awkward but plausible, for example as a toy sword fight (p. 29).
- Conclusion: the authors say GPT-3 appears to be at least proficient at using novel words in a sentence (p. 29).

### 3.9.6 Correcting English grammar (pp. 29–30)
- Prompt format: `Poor English Input: <sentence>\n Good English Output: <sentence>`. The text says one human-written correction was given and 5 more were requested, with no omissions or repeats (p. 29). Figure 3.17 shows more pairs than that (see Reading notes) (p. 30).
- Examples include *I eated the purple berries* → *I ate the purple berries* (human-written), *The patient was died* → *The patient died*, and *Janet broke Bill on the finger* → *Janet broke Bill's finger* (p. 30).
- Caveat in the caption: the line between "poor" and "good" English is, in the authors' words, complex, contextual and contested. In the Mary/St. Louis sentence (about John renting a house cheap) the model also deleted the word "cheap", which alters the meaning. The authors attribute this to the model's assumptions about what "good" is (p. 30).

### 4 Measuring and preventing memorization of benchmarks (pp. 29–33)
**Motivation.**
- The training data comes from the internet, so some benchmark test sets may be in it. The authors describe detecting this at internet scale as a new research area with no established best practices (p. 29).
- Earlier work also met this problem. One of the first papers to train an LM on Common Crawl [TL18] detected and removed a training document overlapping one of its evaluation sets. GPT-2 did post-hoc overlap analysis and found models did moderately better on overlapping data. The effect was not significant because the contaminated fraction was small, often only a few percent (pp. 29, 31).
- GPT-3 is in a different regime (p. 31):
  - Data and model are about two orders of magnitude larger than GPT-2's, with much Common Crawl. This raises the chance of contamination and memorization.
  - Even GPT-3 175B does not overfit its training set by much, measured against a held-out validation split that was deduplicated against it (Figure 4.1).
  - The authors therefore expect contamination to be frequent, but its effects may be smaller than feared.
- Figure 4.1 (training curves, cross-entropy in nats/token versus tokens elapsed up to 300B, for models from $10^8$ to about $10^{11}$ parameters): the train–validation gap grows only minimally with model size and training time. This suggests the gap mostly reflects a difference in difficulty, not overfitting (p. 31).

**What went wrong and what was done.**
- The authors first tried to find and remove overlap with the dev/test sets of all benchmarks. A bug meant only partial removal. Retraining was infeasible because of cost, so they study the effect of the remaining overlap (p. 31).
- For each benchmark they build a "clean" version. They drop every example that has a 13-gram overlap with anything in the pretraining set, or, if the example is shorter than 13 grams, that overlaps as a whole. This is deliberately conservative. Exact procedure: Appendix C (p. 31).
- Interpretation rule (author's): if the clean-subset score is similar to the full score, this suggests that contamination, even if present, does not have a significant effect on reported results. If the clean score is lower, contamination may be inflating results (p. 31).
- Result (Figure 4.2): potential contamination is often high (a quarter of benchmarks score over 50%), but in most cases performance changes only negligibly. No evidence was found that contamination level and performance difference are correlated. Conclusion: either the conservative method overestimated contamination substantially, or contamination has little effect (p. 31).
- Axes of Figure 4.2: x is the percentage of data verified clean (a conservative lower bound), y is the percent change in performance when evaluating only on the clean subset (p. 32).

**Flagged groups** (Word Scrambling, Reading Comprehension, PIQA, Winograd, language modeling, German→English translation). Because the method is very conservative, false positives are expected (pp. 31–32).
- *Reading comprehension (QuAC, SQuAD2, DROP):* over 90% of examples were flagged. For every overlap inspected, in all 3 datasets, the source text was in the training data but the question/answer pairs were not. The model gains only background information (p. 32).
- *German→English (WMT16):* 25% of examples were flagged, with an associated total effect of 1–2 BLEU. None of the flagged examples contained paired sentences resembling machine-translation training data. The collisions were monolingual snippets, mostly of news events (p. 32).
- *Reversed words and anagrams* (tasks like "alaok = koala"): 2-grams were used for filtering because the tasks are short. The flagged overlaps were mostly palindromes or trivial unscramblings (e.g. "kayak = kayak"), not real reversals. Removing the trivial items made the task harder, giving a spurious signal. Symbol insertion shows high overlap but no performance effect, because the task removes non-letter characters and the overlap analysis ignores them (p. 32).
- *PIQA:* 29% flagged, with a 3 percentage point absolute (4% relative) decrease on the clean subset (p. 32).
  - The test set was released after the training set was created and its labels are hidden. Some web pages used by the crowdsourcing workers are in the training set.
  - A 25× smaller model showed a similar decrease. The authors suspect statistical bias rather than memorization (workers' copied examples may be easier), but "cannot rigorously prove" it. PIQA results carry an asterisk.
- *Winograd:* 45% flagged, with a 2.6% decrease on the clean subset. Manual inspection found 132 Winograd schemas in the training set, in a different format from the one presented to the model. Results are asterisked despite the small decrease (p. 32).
- *Language modeling (p. 33):* the 4 Wikipedia LM benchmarks used in GPT-2 and the Children's Book Test are almost entirely in the training data. No clean subset could be extracted, so the authors do not report them, although they had intended to. Penn Tree Bank, unaffected because of its age, became the chief LM benchmark.
- *LAMBADA (p. 33):*
  - Contamination appears substantial, but the clean subset scores within 0.5% of the full set.
  - Strictly speaking, the fill-in-the-blank format precludes the simplest form of memorization.
  - The results section still notes the potential contamination, because the gains on LAMBADA were very large.
- Other high-contamination datasets with near-zero impact often turned out to be false positives. They had no contamination, or contamination that did not reveal the answer (p. 33).

**Stated limitation.** The clean subset may not come from the same distribution as the original set. Memorization could inflate results while a bias making the clean subset easier cancels it exactly. The authors judge this unlikely because many shifts are close to zero and small models, unlikely to memorize, show no noticeable difference in shifts (p. 33). They call this a "best effort" and say much work remains for benchmark design and model training (p. 33).

*Intuition note.* The test asks: does the score drop when we remove every example the model could possibly have seen? If not, this suggests leakage has little effect on the score, although a clean subset that happens to be easier could hide an effect (p. 33). Where the score does drop (PIQA, Winograd), the authors found some evidence of contamination and mark those results with an asterisk. For PIQA they suspect statistical bias (an easier clean subset) rather than memorization but cannot rigorously prove it; for Winograd they found 132 schemas in the training set, and the decrease was small (p. 32).

### 5 Limitations (pp. 33–34)
- **Text quality (author's report):** samples sometimes repeat themselves semantically at document level, lose coherence over long passages, contradict themselves, and contain non-sequiturs. The authors will release 500 uncurated unconditional samples (p. 33).
- **Common-sense physics:** informally, GPT-3 seems to struggle with questions like "If I put cheese into the fridge, will it melt?", despite doing well on PIQA (p. 33).
- **Comparison tasks:** in-context performance has notable gaps. On WiC (same word sense in two sentences?) and ANLI (does one sentence imply another?) and some reading-comprehension tasks it does little better than chance, one-shot or few-shot, (p. 33).
- **Design choice and its cost:** the work used only autoregressive models, which are easy to sample from and to compute likelihoods for, so there are no bidirectional or denoising models. The authors say this comes at the cost of potentially worse performance on tasks that benefit from bidirectionality: fill-in-the-blank, comparing two pieces of content, and re-reading a long passage before a short answer (p. 33).
  - The authors say this *could be* a possible explanation for the lag on WiC, ANLI, QuAC and RACE.
  - They also *conjecture*, from past literature, that a large bidirectional model would be stronger at fine-tuning.
  - A large bidirectional model, or bidirectional models that work few/zero-shot, could give the "best of both worlds".
- **Objective limits:** scaling any LM-like model may eventually run into, or could already be running into, the limits of the pretraining objective (pp. 33–34).
  - The objective weights every token equally and has no notion of which tokens matter most.
  - Task specification forces tasks into prediction, while useful systems (e.g. virtual assistants) might be better seen as taking goal-directed actions.
  - Models are not grounded in other domains of experience such as video or physical interaction.
  - Conclusion: the authors say scaling pure self-supervised prediction is likely to hit limits, and that augmentation with a different approach is likely to be necessary. Directions named: learning the objective from humans, fine-tuning with reinforcement learning, adding modalities such as images (p. 34).
- **Sample efficiency:** pre-training sees much more text than a human sees in a lifetime. Test-time (one/zero-shot) efficiency is closer to humans'. Grounding or algorithmic improvements might help (p. 34).
- **What few-shot learning does is unclear:** it may learn tasks "from scratch" at inference or merely recognise tasks learned in training. This is a spectrum, from identical-distribution demonstrations in training, to the same task in a different format, to adapting to a style of a general task, to learning a skill de novo. Where GPT-3 sits may vary by task. Synthetic tasks (word scrambling, nonsense words) seem especially likely to be learned de novo. The authors say translation clearly must be learned during pretraining. Understanding how few-shot learning works is an open direction (p. 34).
- **Cost:** models this size are expensive and inconvenient for inference. Distillation is suggested, since the model holds many skills not needed for one task. It has not been tried at hundreds of billions of parameters (p. 34).
- **Common deep-learning issues:** poor interpretability, not necessarily well calibrated on novel inputs (indicated by much higher variance than humans on standard benchmarks), and it keeps data biases (p. 34).

### 6 Broader impacts (pp. 34–39)
- Beneficial uses: code and writing auto-completion, grammar assistance, game narrative, better search responses, question answering. GPT-3 also makes synthetic text harder to tell from human text, so it may advance harmful uses as well. The authors focus on harms not because they believe the harms are necessarily greater, but to stimulate work on studying and mitigating them (p. 34).

#### 6.1 Misuse (p. 35)
- Method: use security risk-assessment ideas (identify threats and impacts, assess likelihood, risk as a combination of likelihood and impact). Three factors are discussed (p. 35).
- **6.1.1 Applications:** any harmful activity that relies on text could be augmented: misinformation, spam, phishing, abuse of legal and governmental processes, fraudulent essays, social-engineering pretexting. Many of these are bottlenecked by human writing, and better text could lower barriers. GPT-3's ability to generate several paragraphs of synthetic content that people find difficult to distinguish from human-written text (§3.9.4, not in this part) is called a concerning milestone by the authors (p. 35).
- **6.1.2 Threat actors:**
  - *Low/mid-skill actors:* the authors monitored forums. After the GPT-2 release they found significant discussion, but fewer experiments and no successful deployments since. Misuse discussion correlated with media coverage. Assessment: the threat from these actors is "not immediate", but significant reliability gains could change this.
  - *APTs* (highly skilled, well-resourced, e.g. state-sponsored): the authors consulted professional threat analysts and saw no discernible difference in operations since GPT-2. The assessment was that LMs may not be worth significant investment, because there is no convincing demonstration that they beat current methods and content "targeting" or "controlling" is at an early stage (p. 35).
- **6.1.3 Incentives:** tactics are shaped by cost and ease of use (phishing is popular because it is low-cost and high-yield). LM outputs are stochastic. Developers can constrain them (e.g. top-k truncation) but they are not consistent without human feedback. If a bot is coherent 99% of the time, a human is still needed to filter the other 1%, which limits scalability. The authors suspect that AI researchers will eventually develop models consistent and steerable enough to be of greater interest to malicious actors (p. 35).

#### 6.2 Fairness, bias and representation (pp. 36–39)
- Scope: gender, race, religion, chosen subjectively as a starting point. The analysis is "preliminary" and not exhaustive. Probes were run on the 175B model and on smaller models. Headline: the authors' analysis indicates broadly that internet-trained models have internet-scale biases, i.e. tend to reflect stereotypes in their training data (p. 36).
- **6.2.1 Gender (pp. 36–37)**
  - *Occupation probe.* Context "The {occupation} was a" (Neutral Variant). The authors read off the probability of male-indicating words (man, male…) versus female-indicating words (woman, female…). 83% of 388 occupations were more likely followed by a male identifier.
  - Male-leaning examples: legislator, banker, professor emeritus, mason, millwright, sheriff. Female-leaning: midwife, nurse, receptionist, housekeeper.
  - *Variants.* "The competent {occupation} was a" (Competent) and "The incompetent {occupation} was a" (Incompetent). With "competent", the majority of occupations had an even higher probability of male identifiers than in the neutral case. With "incompetent", most still leaned male, with a probability similar to the neutral case.
  - *Metric.* Average occupation bias:
  $$\frac{1}{n_{\text{jobs}}}\sum_{\text{jobs}} \log\!\left(\frac{P(\text{female}\mid\text{Context})}{P(\text{male}\mid\text{Context})}\right)$$
  Values: $-1.11$ (Neutral), $-2.14$ (Competent), $-1.15$ (Incompetent). Negative values mean the male identifier is more probable (added step: the ratio female/male is below 1); the author's text reports the occupations as male leaning. The log ratio gives one number per occupation, averaged over $n_{\text{jobs}}$ occupations.
  - *Winogender pronoun resolution.* Example context: *The advisor met with the advisee because she wanted to get advice about job applications. 'She' refers to the ...* The model's two options are the Occupation option (advisor) and the Participant option (advisee). GPT-3 175B had the highest accuracy of all models (64.17%). It was the only model with higher accuracy for female than male pronouns on Occupation sentences (81.7% vs 76.7%). All other models were higher for male, except GPT-3 13B, which was equal (60%). The authors read this as "preliminary evidence" that larger models are more robust where bias can cause errors.
  - *Co-occurrence test.* For each prompt ("He was very", "She was very", "He would be described as", "She would be described as") 800 outputs of length 50 were generated, with temperature 1 and top-$p$ 0.9. (Temperature controls randomness. Top-$p$ samples only from the most probable words whose probabilities add up to $p$.) Adjectives and adverbs among the top 100 most favored words were extracted with an off-the-shelf POS tagger. Women were more often described with appearance-oriented words ("beautiful", "gorgeous"), men with adjectives spanning a greater spectrum. Footnote 9: only male/female pronouns were used, a simplification, and other forms of gender bias are likely present.
  - *Table 6.1* (175B; raw co-occurrence counts, averages 17.5 male and 23.9 female). Male: Large (16), Mostly (15), Lazy (14), Fantastic (13), Eccentric (13), Protect (10), Jolly (10), Stable (9), Personable (22), Survive (7). Female: Optimistic (12), Bubbly (12), Naughty (12), Easy-going (12), Petite (10), Tight (10), Pregnant (10), Gorgeous (28), Sucked (8), Beautiful (158). "Most favored" means words that co-occur at a higher rate with one category than the other.
- **6.2.2 Race (p. 37)**
  - Prompts: "The {race} man was very", "The {race} woman was very", "People would describe the {race} person as". 800 samples per prompt. Sentiment was measured with SentiWordNet for words co-occurring disproportionately with each race, on a scale from 100 to −100. Examples: wonderfulness 100, amicable 87.5, wretched −87.5, horrid −87.5.
  - Caveats: the models were explicitly prompted to talk about race, so, the authors say, the results do not show how the models talk about race outside an experimental setup. Because sentiment is measured by word co-occurrence, it can reflect socio-historical factors (e.g. text on slavery is often negative).
  - Result (Figure 6.1, 7 models from 350M to 175B): "Asian" ranked 1st in 3 of 7 models. "Black" ranked lowest in 5 of 7. Differences narrowed marginally on larger models. The authors say this highlights the need for more sophisticated analysis (p. 37).
- **6.2.3 Religion (p. 38)**
  - Prompts "{Religion practitioners} are" for Atheism, Buddhism, Christianity, Hinduism, Islam, Judaism. 800 outputs of about 50 tokens each, temperature 1, top-$p$ 0.9. Table 6.2 lists the ten most favored words per religion.
  - Findings: as with race, the associations indicate some propensity to reflect how these terms are sometimes presented in the world. For Islam, "ramadan", "prophet", "mosque" co-occurred at a higher rate than for other religions. "violent", "terrorism", "terrorist" co-occurred at a greater rate with Islam than with other religions and were in the top 40 most favored words for Islam (p. 38).
- **6.2.4 Future challenges (p. 39)**
  - The authors call the section "subjective signposting" and cite Model Cards as inspiration.
  - They say it is important to intervene, not only to characterise bias. This needs a common vocabulary tying together normative, technical and empirical challenges, plus engagement with literature outside NLP and with affected communities.
  - Mitigation should not be a purely metric-driven attempt to "remove" bias, a goal the authors say has been shown to have blind spots; it should be holistic.

*Intuition note.* The bias probes mostly count which words follow which prompts, so they show what the generated text associates with a group. The authors note that sentiment measured by co-occurrence can reflect socio-historical factors, and they call the analysis preliminary (pp. 36–37).

#### 6.3 Energy usage (p. 39)
- Training GPT-3 175B used several thousand petaflop/s-days, against tens for a 1.5B GPT-2 (Figure 2.2) (p. 39).
- The authors argue costs should be seen as amortised over the model's lifetime and many uses. Generating 100 pages of content from the trained 175B model can cost on the order of 0.4 kW-hr, or only a few cents in energy costs. Distillation and algorithmic progress may lower costs further (p. 39).

### 7 Related work (pp. 39–40)
- *Scale of LMs:* three lines of work (p. 39).
  - (a) Scale parameters and FLOPs per token roughly together. Model sizes grew from 213M (original Transformer) to 300M, 1.5B, 8B, 11B and 17B.
  - (b) Increase parameters but not computation, via conditional computation and mixture-of-experts. Models of 100B+ parameters were built, but only a small fraction of parameters is used per forward pass.
  - (c) Increase computation without parameters (adaptive computation time, universal transformer).
  - This work takes (a) and goes 10× beyond previous models that use it.
- *Scaling-law studies* find a smooth power-law trend in loss. This work suggests the trend largely continues, although a slight bending of the curve can perhaps be detected in Figure 3.1. Downstream tasks improve relatively smoothly (many though not all) over 3 orders of magnitude (p. 39).
- *Small models and distillation* (ALBERT etc.) are potentially complementary (pp. 39–40).
- *Harder benchmarks:* as fine-tuned models near human performance, harder, more open-ended or adversarial tasks have been built, and this work tests on many (p. 40).
- *QA:* other work fine-tuned an 11B model or attended over a large corpus at test time. This work differs in focusing on in-context learning, though it could be combined with them (p. 40).
- *Meta-learning:* in-context learning has an inner-loop/outer-loop structure like meta-learning in general (matching networks, RL2, MAML etc.). Stuffing the context with examples is most structurally similar to RL2: the inner loop adapts through computation in activations without weight updates, and the outer loop (LM pre-training) updates the weights and "implicitly learns" to adapt to or recognise tasks defined at inference time (p. 40).
- *Other few-shot approaches:* combining pre-trained LMs with gradient descent, and semi-supervised learning such as UDA (p. 40).
- *Instructions and multitask:* natural-language task instructions were formalised in supervised settings and used for some tasks by GPT-2. The text-to-text transformer used task text for multi-task fine-tuning, not in-context learning. Multi-task learning is limited by the need to curate datasets and curricula. By contrast, large-scale pre-training appears to offer a natural broad distribution of tasks implicit in predicting the text itself (p. 40).
- *Algorithmic innovations* (denoising bidirectionality, prefixLM, encoder-decoder, permutation training, etc.) are many. This work stays with pure autoregressive LMs to focus on in-context learning and to reduce implementation complexity. The authors say it is "very likely" that adding these would improve GPT-3, especially for fine-tuning (p. 40).

### 8 Conclusion (pp. 40–41)
- A 175B model shows strong performance on many NLP tasks in zero-, one- and few-shot settings, in some cases nearly matching fine-tuned state of the art. It generates high-quality samples and shows scaling trends that are "roughly predictable" without fine-tuning. Despite limitations, the results suggest very large LMs may be an important ingredient in adaptable, general language systems (pp. 40–41).

### Acknowledgements and Contributions (pp. 41–42)
- Thanks to reviewers, colleagues, the infrastructure teams, and the millions of people who created the content used in training (p. 41).
- The contribution list assigns roles (model implementation, data collection and overlap analysis, downstream tasks, scaling analysis, fairness analysis, human evaluations, threat analysis, writing). One line credits Alec Radford with originally demonstrating few-shot learning in LMs (p. 42).

### Appendix A: Common Crawl filtering (p. 43)
1. **Quality classifier.** WebText served as a proxy for high-quality documents. A logistic regression classifier (features: Spark's standard tokenizer and HashingTF) was trained with positives from curated datasets (WebText, Wikipedia, the web books corpus) and negatives from unfiltered Common Crawl. Each Common Crawl document is kept iff
$$\texttt{np.random.pareto}(\alpha) > 1 - \texttt{document\_score}$$
with $\alpha = 9$, chosen to take mostly highly scored documents but still include some out-of-distribution ones, and to match the score distribution on WebText. This re-weighting increased quality as measured by loss on out-of-distribution generative text samples.
2. **Fuzzy deduplication** within each dataset (Spark MinHashLSH, 10 hashes, same features), plus fuzzy removal of WebText from Common Crawl. This decreased dataset size by an average of 10%.
- Benchmark text was then partially removed (Appendix C) (p. 43).

*Intuition note (added reasoning).* A higher classifier score lowers the threshold $1-\text{document\_score}$, so the random draw is more likely to exceed it and the document more likely to be kept. A lower score does not mean certain removal, since the draw can still be large.

### Appendix B: Model training (p. 43)
- Optimiser: Adam with $\beta_1=0.9$, $\beta_2=0.95$, $\epsilon=10^{-8}$. Global gradient norm clipped at 1.0.
- Learning rate: cosine decay to 10% of its value over 260B tokens, then training continues at 10%. Linear warmup over the first 375M tokens.
- Batch size increases linearly from a small value (32k tokens) to full size over the first 4–12B tokens, depending on model size.
- Data are sampled without replacement (until an epoch boundary) to minimise overfitting. Weight decay is 0.1.
- Sequences always fill the $n_{\text{ctx}}=2048$ context window, packing multiple documents when short. There is no special masking. Documents are separated by an end-of-text token, from which the model can infer that context across it is unrelated (p. 43).

### Appendix C: Test-set contamination details (pp. 43–45)
- **Initial filter (pp. 43–44):**
  - It searched for 13-gram overlaps between all dev/test sets and the training data. A "gram" is a lowercase, whitespace-delimited word with no punctuation.
  - The colliding 13-gram plus a 200-character window around it was removed, splitting the document. Pieces under 200 characters were discarded. Documents split into more than 10 pieces were removed entirely.
  - Whole-document removal on a single collision was dropped because it over-penalised long documents (books) for false positives. 13-grams that matched more than 10 training documents were ignored (mostly cultural phrases, legal boilerplate).
- **Overlap methodology (p. 44):**
  - $N$ is the 5th-percentile example length in words (ignoring punctuation, whitespace, case), with a minimum of 8 on non-synthetic tasks (spurious collisions below it) and a maximum of 13 for performance.
  - Exact collisions were computed with Apache Spark (unlike GPT-2's bloom filters), against the full training corpus, though only 40% of filtered Common Crawl documents were used in training.
  - A "dirty" example has any $N$-gram overlap with any training document. A "clean" example has none.
  - Test and validation splits had similar contamination levels. The bug meant filtering failed on long documents such as books, hence the almost-complete overlap for several LM benchmarks and the Children's Book Test.
- **Overlap results (p. 44):** the clean-only score is compared with the original as a relative percent change. The author's wording: a clean score more than 1% or 2% worse suggests overfitting to seen examples. A significantly better clean score suggests the filter marked easier examples as dirty. The relative difference is
$$\text{Relative Difference} = \frac{\text{score}_{\text{clean}}-\text{score}_{\text{all}}}{\text{score}_{\text{all}}}\times 100\% \quad\text{(added step: the quantity in the last column of Table C.1, which recomputes only approximately from the rounded printed scores)}$$
  - False positives are common for datasets with web background information but no answers (SQuAD), and for examples under 8 words (ignored, except wordscrambling).
  - DROP is the case where the method fails: 94% of examples are dirty. The passage is provided to the model anyway, and every matching training document contained only the source passage, none of the questions and answers. The authors' likelier explanation for the drop is that the remaining 6% come from a slightly different distribution.
  - Figure 4.2: as contamination rises, the variance of clean/all rises, but there is no apparent bias toward better or worse performance. This suggests GPT-3 is relatively insensitive to contamination.
- **Table C.1** (p. 45; 42 benchmarks sorted from dirtiest to cleanest; scores come from a different random seed for in-context examples, so they differ slightly from the main paper). Selected rows (All score; clean %; relative difference):

| Dataset | $N$ | All | Clean % | Rel. diff. |
|---|---|---|---|---|
| QuAC (f1) | 13 | 44.3 | 1% | 20% |
| DROP (f1) | 13 | 36.5 | 7% | −21% |
| PIQA (acc) | 8 | 82.3 | 71% | −4% |
| Winograd (acc) | 9 | 88.6 | 40% | −3% |
| LAMBADA (acc) | 13 | 86.4 | 57% | 0% |
| De→En 16 (BLEU) | 12 | 43.0 | 75% | −5% |
| Anagrams 2 | 2 | 40.2 | 93% | −7% |
| Reversed Words | 2 | 0.4 | 93% | −26% |
| Winogrande | 13 | 77.7 | 100% | 0% |

  Winogrande has 0 dirty examples, so its dirty-score cell is shown as "-".

### Appendix D: Total compute (p. 46)
- Simplification: attention is ignored because it typically uses less than 10% of compute for these models (p. 46).
- Table D.1 chain (from the caption): training tokens; for T5 (encoder-decoder) only half of parameters are active per token; each active parameter in a forward pass costs one addition and one multiply (2 flops); a factor 3 for the backward pass, because computing both $\partial \text{loss}/\partial \text{params}$ and $\partial \text{loss}/\partial \text{acts}$ costs about as much as the forward pass; then multiply by total tokens and total parameters. One petaflop/s-day is $8.64\times10^{19}$ flops (p. 46).
$$\text{Total flops} = \text{params}\times\text{tokens}\times(\text{flops per param per token}),\qquad \text{flops per param per token} = (\text{fwd flops per active param per token})\times 3$$
- Table values: fwd flops per active param per token = 2 for BERT/RoBERTa/GPT-3 (active fraction 1.0) and 1 for T5 (active fraction 0.5, so 2 × 0.5 — added step), giving 6 and 3 flops per param per token. GPT-3 175B: 174,600M params, 300B tokens, $3.14\times10^{23}$ flops, $3.64\times10^{3}$ PF-days (p. 46).
- Check (added step): $6\times1.746\times10^{11}\times3\times10^{11}=3.1428\times10^{23}$ and $3.1428\times10^{23}/8.64\times10^{19}\approx3637.5$, consistent with the table.
- Other table rows: T5-11B $3.82\times10^2$ PF-days, RoBERTa-Large $4.93\times10^1$, BERT-Large $6.16$ (p. 46).

### Appendix E: Human quality assessment of synthetic news (pp. 46–48)
- *Participants (p. 46):* 718 recruited for 6 experiments, 97 excluded for failing an internet check question, 621 left (343 male, 271 female, 7 other), mean age about 38. Recruited through Positly (US-based). Paid \$12 for an estimated 60 minutes. No repeat participation.
- *Procedure (pp. 46–47):*
  - 25 articles from newser.com (early 2020). Titles and subtitles were used to prompt models from 125M to 13.0B and "200B (GPT-3)" (as printed).
  - Five outputs per question were generated per model, and the one with word count closest to the human article was chosen automatically.
  - Half of the participants took quiz A and half quiz B. Each quiz had 25 articles, 12–13 human and 12–13 model-generated, with the assignment swapped between quizzes. Question order was shuffled.
  - Participants were asked whether they had seen the articles and whether they had looked anything up.
- *Table E.1* (p. 47): participants recruited/excluded and word counts per model. Human article length averages 216 words. Model outputs average 188 words (Small) to 216 (175B).
- *Statistics (p. 47):* two-sample independent t-test of each model against the control (`scipy.stats.ttest_ind`). The accuracy-vs-size regression is a power law $ax^{-b}$. 95% confidence intervals use the t-distribution of the sample mean.
- *Duration (pp. 47–48):* time spent per question set rises with model size (Figure E.1, linear fit on a log scale; the control model is the dashed line at 105 seconds). Lower accuracy despite more time supports the finding that larger models generate harder-to-distinguish articles.
- *~500-word articles (p. 48):* 160 participants (Table E.2: control 79 recruited/17 excluded; GPT-3 175B 81/19). Twelve Reuters world news articles (late 2019). The context for GPT-3 175B was a single Reuters article outside the 12. Titles and Reuters locations generated the completions. The control is a "160M" model. Comprehension questions were added and articles were shown in 3 stages at 30-second intervals. Average lengths 569 (human) vs 464 (control) vs 498 (175B).

### Appendix F: Additional samples (pp. 48–49)
- Figure F.1: four uncurated poems titled "Shadows on the Way" in the style of Wallace Stevens. The context contained a Cavafy poem and an Ashbery poem (text omitted in the figure) and then the title and author. The authors first tried a few prompts, then generated four samples with no editing or selection (temperature 1, nucleus sampling $P=0.9$). Completions were truncated when the model began a new title/author heading or broke into prose commentary (pp. 48–49).

## Toy example (ours, not from the paper)
**Goal:** apply the clean-vs-all test of §4 and App. C by hand.

A test set has 10 examples. Overlap search flags 4 as dirty and 6 as clean. The model is correct on all 4 dirty ones and on 5 of the 6 clean ones.
1. Full accuracy = (4 + 5)/10 = 9/10 = 90%.
2. Clean accuracy = 5/6 ≈ 83.3%.
3. Relative difference = (83.3 − 90)/90 = −6.67/90 ≈ −7.4%.
4. Reading by the author's rule: a clean score 1–2% or more below the full score suggests possible inflation. Here −7.4% would be flagged. The explanation might be memorization of dirty items or an easier dirty subset (as for PIQA, where a smaller model showed a similar drop).
5. Cross-check on a real row (Table C.1, PIQA): (79.3 − 82.3)/82.3 = −3.0/82.3 ≈ −3.6%, listed as −4%.

With 4/4 on dirty items replaced by 3/4, clean accuracy stays 5/6 and the full accuracy becomes 8/10 = 80%. Relative difference = (83.3 − 80)/80 ≈ +4.2%. A positive difference means the clean subset looks easier, as the authors say can happen.

## Concepts
- [[benchmark-contamination]] (new) — benchmark test examples (or their answers) appearing in the pretraining data, possibly inflating scores (p. 29)
- [[n-gram-overlap-decontamination]] (new) — flag an example as dirty if it shares an $N$-gram (8–13 words) with any training document; evaluate on the clean remainder (pp. 31, 44)
- [[language model]] — here, autoregressive models only; the authors avoid bidirectional or denoising models (p. 33)
- [[encoder-only / decoder-only]] — the authors' contrast of autoregressive with bidirectional architectures and their effect on comparison/re-reading tasks (p. 33)
- [[in-context learning]] — learning a task from prompt examples without weight updates; structurally like RL2's inner loop, with LM pre-training as the outer loop (p. 40)
- [[zero-shot / few-shot prompting]] — demonstrated by the novel-word and grammar prompts (pp. 29–30)
- [[pretraining / fine-tuning]] — pretraining objective limits; multi-task fine-tuning contrasted with in-context use (pp. 33–34, 40)
- [[scaling law]] — smooth power-law loss trend with scale; this work finds it largely continues (p. 39)
- [[symbol grounding]] — in this unit, only the claim that LMs are not grounded in video or physical interaction and so lack world context; no formal theory (p. 34)
- [[nucleus-sampling-temperature]] (new) — sampling with temperature 1 and top-$p$ 0.9, used for bias probes and poems (pp. 36, 48)
- [[co-occurrence-bias-probe]] (new) — generate many completions from templated prompts and compare words by group (pp. 36–38)
- [[distillation]] (new) — compressing a large model into a smaller one, proposed to cut inference cost (p. 34)
- [[fuzzy-deduplication]] (new) — removing near-duplicate documents (MinHashLSH) to reduce overfitting (p. 43)
- [[quality-filter-classifier]] (new) — logistic regression separating WebText-like documents from raw Common Crawl, used to re-sample (p. 43)
- [[training-compute-pf-days]] (new) — total flops = params × tokens × 6 (models with all parameters active, e.g. GPT-3 and BERT; 3 for T5), in units of $8.64\times10^{19}$ flops (p. 46)

## Canonical instances
- [[novel-word-task]] (new) — GPT-3 uses invented words (whatpu, screeg…) correctly or plausibly after one definition (p. 29)
- [[grammar-correction-task]] (new) — few-shot correction; "cheap" deleted, showing assumptions about "good" English (p. 30)
- [[piqa-contamination]] (new) — 29% flagged, −4% relative on clean set, asterisked (p. 32)
- [[winograd-contamination]] (new) — 132 schemas found in training, asterisked (p. 32)
- [[drop-reading-comprehension-contamination]] (new) — 94% dirty, but only source passages overlapped, not Q&A (pp. 32, 44)
- [[occupation-gender-probe]] (new) — 83% of 388 occupations male-leaning; average log ratio −1.11 (p. 36)
- [[winogender]] — pronoun resolution; GPT-3 175B 64.17% (p. 36)
- [[racial-sentiment-probe]] (new) — SentiWordNet scores; "Asian" consistently high (1st in 3 of 7 models), "Black" lowest in 5 of 7 (p. 37)
- [[human-detection-of-synthetic-news]] (new) — accuracy falls and time spent rises with model size (pp. 46–48)

## Bridges (candidates)
- [structural-analogy] Clean-vs-all benchmark test ↔ ML evaluation: train/test leakage audit — the same idea as comparing performance on leak-free versus original data.
- [structural-analogy] Co-occurrence bias probe ↔ computational social science: templated audit studies — vary one attribute in a standard prompt and compare outcomes across groups.
- [structural-analogy] Inner loop (prompt) / outer loop (pretraining) ↔ meta-learning (RL2, MAML): adaptation happens through activations versus through weight updates.
- [same-math] Compute accounting (2 flops × 3 for backward = 6 per parameter per token) ↔ llm: compute-optimal training — the same per-token flop count is used to budget compute versus data.
- [metaphor] "Internet-scale biases" ↔ social science: a corpus as a mirror of society — the unit says models reflect stereotypes in their training data, but the measured quantity is only word co-occurrence.

## Questions this raises
- If the clean subset is not distributed like the full set, how could one separate memorization from difficulty differences? (The PIQA smaller-model comparison is one attempt.)
- Would a bidirectional or denoising model at GPT-3 scale close the gap on WiC, ANLI and QuAC, as the authors conjecture?
- Does few-shot prompting teach a task, or select one the model already knows, and how could an experiment tell the two apart?
- Do co-occurrence and sentiment probes measure harm, or only the statistics of the corpus, and what would an intervention-oriented test look like?

## Reading notes
- **Unit boundaries:** this part starts mid-§3.9.5 (the end of the novel-words task, p. 29) and ends at the end of Appendix F (Figure F.1, p. 49). It contains the end of §3, then §4–§8, Acknowledgements, Contributions and Appendices A–F. Printed page = pdf page (no offset). §6.1.1 refers to §3.9.4, which is not included here; Appendix E refers to "the main text" for the control model and the accuracy result.
- **No exercises** in this unit.
- **Misprints/inconsistencies seen in the pages:**
  - Text on p. 29 says "Table 3.16"; the item is Figure 3.16.
  - On p. 29 the text says one human correction plus 5 requested corrections. Figure 3.17 shows three human-written pairs and eight bold GPT-3 completions, and the caption speaks of the first few examples (not a count of one) as human-written.
  - Winograd: the §4 text says 45% flagged (p. 32). Table C.1 gives 40% clean ($N=9$), i.e. 60% dirty (p. 45). DROP: text says 94% dirty/6% clean (p. 44), Table C.1 shows 7% clean (p. 45). Table C.1 notes that its scores come from a different seed. The last column does not recompute exactly from the rounded scores for every row (e.g. QuAC: 54.1 vs 44.3 gives about +22%, printed 20%; DROP: 29.5 vs 36.5 gives about −19%, printed −21%) (p. 45).
  - The text says 1–2 BLEU for De→En; Table C.1 shows 43.0 (all) vs 40.8 (clean), a gap of 2.2 (pp. 32, 45).
  - Winogender: the text says the model chose the option with the lowest probability (p. 36); the page does not say whether this wording is intended.
  - Appendix E: text says 718 recruited and 6 experiments; Table E.1 has 9 rows summing to 713 recruited (excluded sums to 97). Rows for GPT-3 Medium, Large, 6.7B and 13.0B all show 46:28:2, which does not match recruited minus excluded for several of them (e.g. Large 81 − 24 = 57 vs 76). The text says "200B (GPT-3)" where Table E.1 and the rest of the paper use 175B. The control model is "160M" in the ~500-word experiment (p. 48).
  - Appendix A: "Wikiedia" is a typo. Poem 3 in Figure F.1 contains "gonne" as printed.
- Table 6.1 entries are printed unsorted by count (e.g. "Personable (22)", "Beautiful (158)").
- No equations were unreadable.
