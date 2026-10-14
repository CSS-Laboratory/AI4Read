---
id: xie-2022-icl/main
work: xie-2022-icl
unit: paper
pages: 1-31
fields: [llm]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# An Explanation of In-context Learning as Implicit Bayesian Inference

## L0 — One line
If pretraining documents are generated from a latent document-level concept (a mixture of HMMs), a language model that fits this distribution can do in-context learning by implicitly inferring the shared concept of the prompt examples (Bayesian inference), provably so (asymptotically optimal error) under a distinguishability condition.

## L1 — The gist (≤ 120 words)
Large LMs can learn a task from a few input-output examples in the prompt, although they were never trained to do so and prompts look unlike natural text. The paper asks what makes this possible. Answer: if pretraining documents come from a mixture of HMMs with a latent concept, an LM that fits the pretraining distribution implicitly does Bayesian inference over that concept. Under a distinguishability condition, its error is asymptotically optimal despite the prompt/pretraining mismatch. In two further settings, error bounds still shrink with example length. A small synthetic dataset (GINC) shows Transformers and LSTMs reproducing several real-world phenomena. This is a first formal step toward explaining in-context learning.

**Prerequisites:** Bayes' rule and marginalization; Markov chains and hidden Markov models (HMMs); KL divergence; total-variation distance; Taylor expansion and Fisher information (for Theorem 2); matrix–vector notation.

## L2 — Key ideas (5–10 bullets)
- **Setting.** Pretraining documents are drawn from a latent concept θ (which sets an HMM's transitions). Prompts concatenate independent examples sharing one concept θ*, so prompts are low-probability sequences under pretraining (pp. 2–4).
- **Posterior predictive.** If the LM fits the pretraining distribution exactly, in-context prediction is a posterior predictive, p(output | prompt) = ∫ p(output | concept, prompt) p(concept | prompt) d(concept). If p(concept | prompt) concentrates on θ* as examples increase, the LM learns by "selecting" the prompt concept through marginalization (pp. 2–3).
- **Main theorem.** Under a distinguishability condition (the KL "signal" summed over k tokens exceeds start and delimiter error terms), the in-context predictor reaches the optimal 0-1 risk as the number of examples n→∞ (Thm 1, p. 7).
- **Longer examples help.** The signal grows with example length k, so information in inputs, not only in the input–output mapping, can be useful. When distinguishability fails, the bounds in Theorems 2 and 3 (under extra assumptions) shrink with k (pp. 7–9).
- **GINC.** Transformers and LSTMs pretrained on a synthetic mixture-of-HMMs dataset show in-context accuracy rising with n and k (p. 10).
- **Ablations.** Pretraining with one concept, or on random transitions, or testing on unseen concepts, makes in-context learning fail. A mixture of concepts matters; diverse token transitions alone are not enough (p. 10).
- **Beyond the theory.** In GINC, larger Transformers can gain in-context accuracy even when pretraining loss is the same (e.g. 12 vs 16 layers at vocab 50). Example order matters, and zero-shot can beat few-shot (pp. 10–11).
- **GPT-3 check.** On filtered LAMBADA, five long examples slightly beat five short ones, while duplicating short examples does not (pp. 30–31).

## L3 — Walkthrough

### Abstract and §1 Introduction (pp. 1–3)
- **In-context learning (ICL):** an LM "learns" a task by conditioning on a prompt of input-output pairs, with no weight updates. Example: p("Polish" | "Albert Einstein was German \n Mahatma Gandhi was Indian \n Marie Curie was") is largest for the correct output (p. 1).
- GPT-3 was not explicitly pretrained to learn from examples, and prompts (concatenated independent examples) differ from natural language. Understanding is limited because real data are messy and ICL has needed large models and data (p. 2).
- **Idea.** Draw a latent concept θ that parameterizes the transitions of an HMM, then sample tokens from that HMM (p. 2). To continue documents coherently, the LM must infer θ. At test time, ICL occurs when it also infers the shared prompt concept. The authors assume the LM fits the pretraining distribution $p$ exactly. The question then becomes the *posterior predictive* of completions given prompts from a different distribution $p_{\text{prompt}}$ (p. 2):
$$p(\text{output}\mid\text{prompt})=\int_{\text{concept}}p(\text{output}\mid\text{concept},\text{prompt})\,p(\text{concept}\mid\text{prompt})\,d(\text{concept}).\tag{1}$$
- If $p(\text{concept}\mid\text{prompt})$ concentrates on the prompt concept as examples increase, the LM "selects" it by marginalization. ICL is then implicit Bayesian inference (p. 3).
- **Challenge.** The Bernstein–von Mises theorem (posterior concentrates on the MLE under regularity conditions) usually assumes independent observations and/or data from the model's own distribution. Neither holds here (p. 3).
- **Claims** (p. 3): (i) asymptotic ICL error is optimal when the per-example signal about the concept exceeds the error from distribution mismatch; (ii) ICL error decreases with example length. The GINC dataset (Transformers and LSTMs) verifies these intuitions, and the latent concept structure is crucial in ablations.
- Open questions beyond the theory, which studies only the pretraining distribution: scaling parameters improves ICL at the same pretraining loss; order sensitivity and zero-shot > few-shot are mirrored in GINC (p. 3).

### §2 In-context learning setting (pp. 3–5)
- **Pretraining distribution.** Document of length $T$ over vocabulary $\mathcal O$ (p. 3):
$$p(o_1,\dots,o_T)=\int_{\theta\in\Theta}p(o_1,\dots,o_T\mid\theta)\,p(\theta)\,d\theta.\tag{2}$$
$p(o_1..o_T|\theta)$ is an HMM. θ determines the transition matrix of the hidden states $h_1..h_T\in\mathcal H$ (p. 3).
- **Prompt distribution** $p_{\text{prompt}}$: $n$ independent training examples plus one test input $x_{\text{test}}$, all conditioned on a shared prompt concept θ*. An example has input $x_i=O_i[1:k-1]$ and output token $y_i=O_i[k]$. The length $k$ is fixed for simplicity (pp. 3–4). Each example is generated by (1) drawing a start hidden state $h_i^{\text{start}}$ from a prompt start distribution, (2) drawing $O_i=[x_i,y_i]$ from $p(O_i\mid h_i^{\text{start}},\theta^*)$. A delimiter token $o^{\text{delim}}$ separates examples (p. 4):
$$[S_n,x_{\text{test}}]=[x_1,y_1,o^{\text{delim}},x_2,y_2,o^{\text{delim}},\dots,x_n,y_n,o^{\text{delim}},x_{\text{test}}]\sim p_{\text{prompt}}.\tag{3}$$
- **Mismatch.** Prompts are low-probability under pretraining. Example: wiki bios go name → nationality → occupation, but prompts go name → nationality → name, with unlikely transitions such as "German" → "Mahatma Gandhi". Delimiter choice is another source (p. 4).
- **Predictor and task.** The target is sampled from (p. 4)
$$y_{\text{test}}\sim p_{\text{prompt}}(y\mid x_{\text{test}})=\mathbb E_{h^{\text{start}}_{\text{test}}\sim p_{\text{prompt}}(h^{\text{start}}_{\text{test}}\mid x_{\text{test}})}\big[p(y\mid x_{\text{test}},h^{\text{start}}_{\text{test}},\theta^*)\big].\tag{4}$$
The analysed in-context predictor is $f_n(x_{\text{test}})=\arg\max_y p(y\mid S_n,x_{\text{test}})$, using the *pretraining* distribution conditioned on the prompt. Its error is $L_{0\text{-}1}(f_n)=\mathbb E_{x_{\text{test}},y_{\text{test}}\sim p_{\text{prompt}}}[\mathbf 1[f_n(x_{\text{test}})\neq y_{\text{test}}]]$ (p. 4).

**§2.1 Assumptions** (pp. 4–5)
- **A1 (delimiter states).** A subset $\mathcal D\subseteq\mathcal H$ emits $o^{\text{delim}}$ deterministically: $p(o^{\text{delim}}|h,\theta)=1$ for $h\in\mathcal D$, and $=0$ for $h\notin\mathcal D$. Seeing the delimiter reveals the state is in $\mathcal D$, not which one. No delimiter is assumed significantly more likely under one concept than another (p. 4).
- **A2 (delimiter transitions).** For $h^{\text{delim}}\in\mathcal D$ and any $h\in\mathcal H$: $p(h^{\text{delim}}|h,\theta)<c_2$ for $\theta\ne\theta^*$; $p(h^{\text{delim}}|h,\theta^*)>c_1>0$; and $p(h^{\text{delim}}|\theta)\in[c_3,c_4]$ for the start distribution (p. 5).
- **A3 (prompt start shift).** $\max_{h^{\text{delim}}\in\mathcal D}TV\big(p_{\text{prompt}}(h)\,\|\,p(h|h^{\text{delim}},\theta^*)\big)<\Delta/4$, where $\Delta=p_{\text{prompt}}(y_{\max}|x_{\text{test}})-\max_{y\ne y_{\max}}p_{\text{prompt}}(y|x_{\text{test}})$ is the margin between the top two labels. Even with TV = 0 there is still shift from concatenating independent examples (p. 5).
- **A4 (well-specification).** $\theta^*\in\Theta$ (p. 5).
- **A5 (regularity).** (1) $p(h|h',\theta^*)>c_5>0$ for all $h,h'$; (2) $p(h|\theta^*)\ge c_8>0$; (3) every token can be emitted: some $h$ has $p(o|h,\theta^*)>c_6>0$; (4) the prior $p(\theta)$ has support on all of Θ and is bounded above (p. 5). These mainly ensure the prompt has non-zero probability under θ*.

### §3 Theoretical analysis (pp. 5–9)
Summary stated by the authors: with infinite examples the error is optimal if a *distinguishability* condition holds (e.g. Θ discrete). Otherwise (e.g. Θ continuous) the expected error still decreases with example length (p. 5).

**§3.1 High-level approach** (pp. 5–6). Goal: $\arg\max_y p(y|S_n,x_{\text{test}})\to\arg\max_y p_{\text{prompt}}(y|x_{\text{test}})$, assuming $p(S_n,x_{\text{test}}|\theta^*)>0$. Expansion:
$$\begin{aligned}p(y|S_n,x_{\text{test}})&=\int_\theta p(y|S_n,x_{\text{test}},\theta)\,p(\theta|S_n,x_{\text{test}})\,d\theta\\&\propto\int_\theta p(y|S_n,x_{\text{test}},\theta)\,p(S_n,x_{\text{test}}|\theta)\,p(\theta)\,d\theta\quad\text{(Bayes; drop } 1/p(S_n,x_{\text{test}}))\\&=\int_\theta\sum_{h^{\text{start}}_{\text{test}}\in\mathcal H}p(y|x_{\text{test}},h^{\text{start}}_{\text{test}},\theta)\,p(h^{\text{start}}_{\text{test}}|S_n,x_{\text{test}},\theta)\,\frac{p(S_n,x_{\text{test}}|\theta)}{p(S_n,x_{\text{test}}|\theta^*)}\,p(\theta)\,d\theta\end{aligned}\tag{5}$$
(law of total probability, Markov property, division by the constant $p(S_n,x_{\text{test}}|\theta^*)$), and so
$$=\int_\theta\sum_{h^{\text{start}}_{\text{test}}}p(y|x_{\text{test}},h^{\text{start}}_{\text{test}},\theta)\,p(h^{\text{start}}_{\text{test}}|S_n,x_{\text{test}},\theta)\,\exp(n\cdot r_n(\theta))\,p(\theta)\,d\theta,\tag{6}$$
with $r_n(\theta)=\tfrac1n\log\frac{p(S_n,x_{\text{test}}|\theta)}{p(S_n,x_{\text{test}}|\theta^*)}$.
- Theorem 1 shows that under distinguishability $\exp(n\,r_n(\theta))\to0$ for every $\theta\ne\theta^*$, while $\exp(n\,r_n(\theta^*))=1$. Only θ* survives in the integral, so the prompt concept is "selected" (limit–integral exchange is justified by boundedness, dominated convergence; p. 6).
- Lemma 1 shows that, restricted to θ*, the argmax equals the most likely label under $p_{\text{prompt}}(y|x_{\text{test}})$ (using A3). Together:
$$\arg\max_y p(y|S_n,x_{\text{test}})\to\arg\max_y p_{\text{prompt}}(y|x_{\text{test}}).\tag{7}$$

*Intuition note.* The likelihood ratio between a wrong concept and the true one shrinks like $e^{-cn}$. After many examples only the true concept carries weight, and the LM's prediction is that concept's prediction.

**§3.2 Heuristic derivation** (pp. 6–7). The authors aim to show that $r_n(\theta)$ converges to a negative constant. Their approach is to approximately factorize the examples, which are dependent under $p$. Let $O_i^{\text{ex}}=[o^{\text{delim}}_{i-1},O_i]$ for $i>1$ and $O_1^{\text{ex}}=O_1$. The goal is
$$p(S_n,x_{\text{test}}|\theta)=p(x_{\text{test}}|S_n,\theta)\,p(S_n|\theta)\approx\prod_{i=1}^nO(1)\,p(O_i|\theta).\tag{8}$$
Chain rule plus A5 (to bound $p(x_{\text{test}}|S_n,\theta)$ by $O(1)$) give
$$p(x_{\text{test}}|S_n,\theta)\,p(S_n|\theta)\approx\prod_{i=1}^nO(1)\,p(O_i^{\text{ex}}|O^{\text{ex}}_{1:i-1},\theta).\tag{9}$$
Marginalizing over the delimiter hidden state $h^{\text{delim}}_{i-1}$, restricted to $\mathcal D$ by A1:
$$\prod_{i=1}^nO(1)\,p(O_i^{\text{ex}}|O^{\text{ex}}_{1:i-1},\theta)=\prod_{i=1}^nO(1)\sum_{h^{\text{delim}}_{i-1}\in\mathcal D}p(O_i|h^{\text{delim}}_{i-1},\theta)\,p(h^{\text{delim}}_{i-1}|O^{\text{ex}}_{1:i-1},\theta)\approx\prod_{i=1}^nO(1)\,p(O_i|\theta).\tag{10}$$
The first equality uses that $O^{\text{ex}}_{1:i-1}\to h^{\text{delim}}_{i-1}\to O_i^{\text{ex}}$ is a Markov chain and $p(o^{\text{delim}}|h^{\text{delim}})=1$. The second uses A2. Hence
$$r_n(\theta)\le\frac1n\Big(O(n)+\sum_{i=1}^n\log\frac{p(O_i|\theta)}{p(O_i|\theta^*)}\Big)\to O(1)+\mathbb E_{O\sim p_{\text{prompt}}}\Big[\log\frac{p(O|\theta)}{p(O|\theta^*)}\Big].\tag{11}$$
The expectation equals $KL(p_{\text{prompt}}(O)\|p(O|\theta^*))-KL(p_{\text{prompt}}(O)\|p(O|\theta))$. The first KL is bounded by a constant (A5). The second splits into $k$ per-token KL terms, against only $O(1)$ error terms from the mismatch. If the KL terms exceed the error terms, $r_n(\theta)$ has a negative limit (p. 7).

**§3.3.1 Distinguishability** (p. 7). Let $p^j_\theta(o)=p(O[j]=o|O[1:j-1],\theta)$ and $p^j_{\text{prompt}}(o)=p_{\text{prompt}}(O[j]=o|O[1:j-1])$.
$$KL_j(\theta^*\|\theta):=\mathbb E_{O[1:j-1]\sim p_{\text{prompt}}}\big[KL(p^j_{\text{prompt}}\|p^j_\theta)\big]\tag{12}$$
$$\epsilon^\theta_{\text{delim}}:=2(\log c_2-\log c_1)+\log c_4-\log c_3,\qquad\epsilon^\theta_{\text{start}}:=\log(1/c_8).\tag{13}$$
**Condition 1 (Distinguishability).** θ* is distinguishable if for all $\theta\in\Theta$, $\theta\neq\theta^*$,
$$\sum_{j=1}^kKL_j(\theta^*\|\theta)>\epsilon^\theta_{\text{start}}+\epsilon^\theta_{\text{delim}}.\tag{14}$$
The left side grows with example length $k$. Intuitively, longer examples put more of the prompt "in distribution", giving more evidence (p. 7; Fig. 2: signal comes from tokens in both inputs and input–output mapping, p. 8).

**Theorem 1.** Assume §2.1 holds. If Condition 1 holds, then as $n\to\infty$
$$\arg\max_yp(y|S_n,x_{\text{test}})\to\arg\max_yp_{\text{prompt}}(y|x_{\text{test}}),\tag{15}$$
so $f_n$ achieves optimal 0-1 risk: $\lim_{n\to\infty}L_{0\text{-}1}(f_n)=\inf_fL_{0\text{-}1}(f)$ (p. 7).

*Intuition note.* Each example gives about $k$ tokens of evidence for the true concept, but the awkward joins between examples cost a fixed amount. If the evidence per example beats that fixed cost, the evidence wins as $n$ grows.

**§3.3.2 Non-distinguishable case** (pp. 8–9). When Eq. 14 fails for some θ, that θ's output distributions are close to θ*'s in KL; this is used to bound error in two settings.

*Continuity.* **Theorem 2.** Let $B$ be the set of θ that violate Eq. 14. Assume the second-order expansion
$$\forall j>1,\quad KL_j(\theta^*\|\theta)=\tfrac12(\theta-\theta^*)^\top I_{j,\theta^*}(\theta-\theta^*)+O(\|\theta-\theta^*\|^3),\tag{16}$$
where $I_{j,\theta^*}$ is the Fisher information matrix of the $j$-th token distribution. Let $\gamma_{\theta^*}=\frac{\max_j\lambda_{\max}(I_{j,\theta^*})}{\min_j\lambda_{\min}(I_{j,\theta^*})}$. Then for $k\ge2$ and as $n\to\infty$,
$$\lim_{n\to\infty}L_{0\text{-}1}(f_n)\le\inf_fL_{0\text{-}1}(f)+g^{-1}\Big(O\Big(\frac{\gamma_{\theta^*}\sup_{\theta\in B}(\epsilon^\theta_{\text{start}}+\epsilon^\theta_{\text{delim}})}{k-1}\Big)\Big),\tag{17}$$
where $g(\delta)=\tfrac12((1-\delta)\log(1-\delta)+(1+\delta)\log(1+\delta))$ is a calibration function for multiclass logistic loss on $\delta\in[0,1)$, assuming the minimizers of the 0-1 risk and the multiclass logistic risk coincide (p. 8). Since $g^{-1}$ is roughly linear for $\epsilon\le0.7$, excess risk decreases roughly as $O(1/k)$. A smaller ("well-conditioned") $\gamma_{\theta^*}$ lowers the error: no direction of θ* exists along which the output distribution changes sharply (p. 8).

*Varying-length test examples.* **Theorem 3.** Let $|x_{\text{test}}|$ be uniform on $\{2,\dots,k\}$, $k\ge2$. Then for $k\ge2$ and $n\to\infty$,
$$\lim_{n\to\infty}L_{0\text{-}1}(f_n)\le\inf_fL_{0\text{-}1}(f)+g^{-1}\Big(O\Big(\frac{\sup_{\theta\in B}(\epsilon^\theta_{\text{start}}+\epsilon^\theta_{\text{delim}})}{k-1}\Big)\Big),\tag{18}$$
under the same minimizer assumption and without continuity. The error is averaged over the 2nd to $k$-th tokens. Bridging the mismatch between fixed-length training examples and random-length test examples is left to future work (p. 9).

*Intuition note.* Even if a wrong concept cannot be ruled out, it cannot differ much from the true one in its predictions, or the evidence would already separate them. So the leftover error is small and falls as examples get longer.

### §4 Simulations (pp. 9–11)
- **GINC dataset** (Appendix F.1): uniform mixture of HMMs over 5 concepts; 1000 pretraining documents, about 10M tokens. Prompts have 0–64 examples, $k\in\{3,5,8,10\}$, 2500 prompts per setting. $y_{\text{test}}$ is the most likely output $\arg\max_yp_{\text{prompt}}(y|x_{\text{test}})$, so intrinsic error is 0 (p. 10).
- **Main result.** GPT-2-based Transformers and LSTMs, vocabularies 50/100/150, averaged over 5 pretraining runs. In-context accuracy improves with $n$ and $k$ (Fig. 3, p. 9), "verifying our theory" (p. 10).
- **Ablations** (4-layer Transformer, Fig. 4): one concept only (no prior) gives flat curves; pretraining on random data containing all transitions also fails; prompts from 5 random unseen concepts fail. So the mixture-of-concepts structure matters, and diverse token transitions alone do not enable ICL (p. 10).
- **Model size and architecture** (Figs. 5–6, p. 11). Accuracy rises as Transformers grow from 4 to 12 to 16 layers. At vocab 50, 12- and 16-layer models both have validation loss 1.33, but in-context accuracy goes 81.2 → 84.7. So larger models may improve ICL beyond better pretraining loss (p. 10). The 4-layer model gets 60.2 ± 5.7 at validation loss 1.50, and the LSTM (28M parameters) gets 95.8 ± 1.11 at loss 1.35 (p. 11). LSTMs consistently beat Transformers despite fewer parameters, "perhaps" due to the similarity between HMMs and LSTMs. Scaling and architecture effects are left open (p. 10).
- **Order sensitivity** (Fig. 7 left): 10 sets of 4 examples, all 24 permutations each, one concept. Accuracy varies by 10–40% across permutations of the same set, as with GPT-3 (p. 10).
- **Zero-shot can beat few-shot** (Fig. 7 right): with lower-entropy transitions (temperature 0.01 instead of 0.1), 12 concepts, vocab 100, few-shot accuracy first dips below zero-shot, then recovers with more examples. The authors hypothesize the distracting prompt structure causes the dip (p. 11).

### §5 Discussion and related work (pp. 11–12)
- Bernstein–von Mises does not apply since prompt examples are not independent under pretraining. Gunst and Shcherbakova give a BvM-type result for HMM observations but not for data from a different distribution (pp. 11–12). A possible route to extrapolation: factorize the concept into semantics and syntax; the LM might generalize to unseen pairs if it learns operations such as copying or reordering (p. 12).
- Topic models (LDA) also have document-level latents but use algorithms such as EM or MCMC. Here, learning arises from Bayesian inference without an explicit algorithm. Wei et al. (2021a) analyse head/prompt tuning, not ICL (p. 12).
- Prior work is said to support the intuition that reducing prompt/pretraining mismatch helps: finetuning on prompt formats, prompt-template optimization, calibration (p. 12). Meta-learning models are trained to learn, whereas ICL emerges from LM pretraining (p. 12).
- GINC is small, so its data and models are relatively large compared with its distribution's complexity, which lets a large-scale phenomenon be studied at small scale with control over latent properties (p. 12).

### §6 Conclusion (p. 12)
ICL is cast as implicit Bayesian inference of a concept, and occurs when the pretraining distribution is a mixture of HMMs. The authors call this a first step.

### Appendix A: Framework details (p. 16)
Hidden segments $H_i=[h_{i,1},\dots,h_{i,k}]$ with
$$h_i^{\text{start}}=H_i[1]\sim p_{\text{prompt}},\qquad H_i^{\text{seg}}=H_i[2:k]\sim p(H_i^{\text{seg}}|h^{\text{start}},\theta^*),\tag{19–20}$$
delimiter states $h_i^{\text{delim}}\sim p^{\text{delim}}_{\text{prompt}}$ (21), tokens $O_i\sim p(O_i|H_i)$ (22), $o_i^{\text{delim}}\sim p(o^{\text{delim}}_i|h_i^{\text{delim}},\theta^*)$ (23). The prompt is $[O_1,o^{\text{delim}}_1,\dots,O_n,o_n^{\text{delim}},x_{\text{test}}]\sim p_{\text{prompt}}$ (24), with $x_{\text{test}}=O_{n+1}[1:k-1]$.

### Appendix B: Propositions (pp. 16–17)
- **Prop. 1.** For all $i$: $p(h_i^{\text{delim}}|O_1,o_1^{\text{delim}},\dots,O_i,\theta^*)>c_1$ and $p(h_i^{\text{delim}}|\dots,\theta)<c_2$. Proof: write $p(h^{\text{delim}}_i|\cdot)=\sum_{h_{i,k}}p(h_i^{\text{delim}}|h_{i,k})\,p(h_{i,k}|\cdot)$ and apply A2 to each term; the weights sum to 1 (Eqs. 25–28) (p. 16).
- **Prop. 2.** There is $c_7>0$ with $p(O_i|h_i^{\text{start}},h_{j,l},\theta^*)>c_7$ for all $i$ and future hidden states $h_{j,l}$ ($j>i$). Proof: by A5, $p(O_i|h^{\text{start}}_i,h_{j,l},\theta^*)=\sum_{H_i}p(O_i|H_i)\,p(H_i|h^{\text{start}}_i,h_{j,l},\theta^*)>(c_6)^k$ for some $H_i$ (29). By Bayes, $p(H_i|\cdot)=\frac{p(h_{j,l}|H,h_i^{\text{start}},\theta^*)\,p(H|h_i^{\text{start}},\theta^*)}{p(h_{j,l}|h^{\text{start}}_i,\theta^*)}>c_5^2$ (30), lower-bounding the numerator terms by $c_5$ and upper-bounding the denominator by 1. Set $c_7=(c_6)^kc_5^2$ (p. 17).

### Appendix C: Lemma 1 (pp. 17–18)
**Lemma 1.** Under A3, for given $S_n,x_{\text{test}}$:
$$\arg\max_y\sum_{h^{\text{start}}_{\text{test}}}p(y|x_{\text{test}},h^{\text{start}}_{\text{test}},\theta^*)\,p(h^{\text{start}}_{\text{test}}|S_n,x_{\text{test}},\theta^*)=\arg\max_yp_{\text{prompt}}(y|x_{\text{test}}).\tag{31}$$
Proof.
- By definition $p_{\text{prompt}}(y|x_{\text{test}})=\sum_{h}p(y|x_{\text{test}},h,\theta^*)\,p_{\text{prompt}}(h|x_{\text{test}})$ (32), with $p_{\text{prompt}}(h|x_{\text{test}})\propto p(x_{\text{test}}|h,\theta^*)\,p_{\text{prompt}}(h)$ (33). Also $p(h|S_n,x_{\text{test}},\theta^*)\propto p(x_{\text{test}}|h,\theta^*)\,p(h|S_n,\theta^*)$ (34). The two differ only in the last factor.
- Let $T\in\mathbb R^{|\mathcal H|\times|\mathcal D|}$ hold $p(h^{\text{start}}_{\text{test}}|h^{\text{delim}})$. Then $p(h^{\text{start}}_{\text{test}}|S_n,\theta^*)=\sum_{h^{\text{delim}}_n}p(h^{\text{start}}_{\text{test}}|h_n^{\text{delim}},\theta^*)\,p(h_n^{\text{delim}}|S_n,\theta^*)=Tv$ (35–36), with $v\in\mathbb R^{|\mathcal D|}$ the delimiter-state probabilities.
- Let $W\in\mathbb R^{|\mathcal Y|\times|\mathcal H|}$ have entries $p(y|x_{\text{test}},h,\theta^*)\,p(x_{\text{test}}|h,\theta^*)\ge0$, and $u\in\mathbb R^{|\mathcal H|}$ the prompt start distribution. Then the two sides are $WTv$ and $p_{\text{prompt}}(\cdot|x_{\text{test}})=Wu$ (37–38). (added step: $Tv,u\in\mathbb R^{|\mathcal H|}$, $WTv,Wu\in\mathbb R^{|\mathcal Y|}$; the normalizing constants are constants in $y$.)
- $\|WTv-Wu\|_\infty\le\|WTv-Wu\|_1=\sum_i|\sum_jW_{ij}(Tv-u)_j|\le\sum_i\sum_jW_{ij}|(Tv-u)_j|=\sum_j(\sum_iW_{ij})|(Tv-u)_j|=\|Tv-u\|_1$ (39–44; the last equality as written by the authors).
- $\|Tv-u\|_1=2\,TV\big(p_{\text{prompt}}\|\sum_iv_i\,p(\cdot|h^{\text{delim}}=i,\theta^*)\big)\le2\sum_iv_i\,TV(\cdot)\le2\max_{h^{\text{delim}}}TV(\cdot)<\Delta/2$ (45–47; convexity of TV, then A3).
- No output probability moves by more than $\Delta/2$, and the margin is $\Delta$, so the argmaxes agree. ∎

*Intuition note.* The prompt start distribution is close enough to the natural post-delimiter distribution that it cannot flip the top answer, because the top answer leads by a margin.

### Appendix D: Proof of Theorem 1 (pp. 19–22)
- **Reduction.** Eqs. 48–51 repeat the expansion of §3.1 with $r_n(\theta)=\frac1n\log\frac{p(S_n,x_{\text{test}}|\theta)}{p(S_n,x_{\text{test}}|\theta^*)}$ (52). The claim is that under distinguishability $r_n(\theta)$ converges to a negative constant, so $\exp(n\,r_n(\theta))\to0$ for $\theta\ne\theta^*$ (53), while the ratio is 1 at θ*.
- **From (53) to the theorem.** Let $\Delta'=\max_{h^{\text{delim}}}TV(p_{\text{prompt}}(\cdot)\|p(\cdot|h^{\text{delim}},\theta^*))<\Delta/2$ (54) and $\epsilon<(\Delta/2-\Delta')\,p(\theta^*)$. For $n$ large enough, the integral of (51) equals
$$\sum_{h}p(y|x_{\text{test}},h,\theta^*)\,p(h|S_n,x_{\text{test}},\theta^*)\,p(\theta^*)+\int_{\theta\ne\theta^*}\epsilon_\theta(y)\,p(\theta)\,d\theta\tag{56}$$
$$\propto\sum_hp(y|x_{\text{test}},h,\theta^*)\,p(h|S_n,x_{\text{test}},\theta^*)+\frac1{p(\theta^*)}\int_{\theta\ne\theta^*}\epsilon_\theta(y)\,p(\theta)\,d\theta\tag{57}$$
with $\epsilon_\theta(y)\le\epsilon/2$ (55–57). By Lemma 1 the first term's argmax is $\arg\max_yp_{\text{prompt}}(y|x_{\text{test}})$, with margin at least $\Delta/2-\Delta'$. The remainder is $\le\epsilon/(2p(\theta^*))<(\Delta/2-\Delta')/2$ (58), so the overall argmax is unchanged.
- **Factorization.** With $O_i^{\text{ex}}$ as in §3.2, Eqs. 59–65 write $p(S_n,x_{\text{test}}|\theta)=\sum_{h^{\text{start}}_{\text{test}}}p(x_{\text{test}}|h^{\text{start}}_{\text{test}},\theta)\,p(h^{\text{start}}_{\text{test}}|S_n,\theta)\prod_{i=1}^n\sum_{h^{\text{delim}}_{i-1}\in\mathcal D}p(O_i|h^{\text{delim}}_{i-1},\theta)\,p(h^{\text{delim}}_{i-1}|O^{\text{ex}}_{1:i-1},\theta)$, using that a delimiter token forces its hidden state into $\mathcal D$ and that $\sum_{h_n^{\text{delim}}}p(h_n^{\text{delim}}|O^{\text{ex}}_{1:n},\theta)=1$. Attention is restricted to θ with $p(S_n,x_{\text{test}}|\theta)>0$, since others do not affect prediction.
- **Bounding $r_n$.** Eqs. 66–69 split $r_n$ into a test-input term and a product over examples. Prop. 1 bounds the delimiter-state posterior ($c_2$ above, $c_1$ below). Prop. 2 bounds $p(x_{\text{test}}|\cdot)$ below by $c_7$:
$$r_n(\theta)\le\frac1n\Big(-\log c_7+n(\log c_2-\log c_1)+\sum_{i=1}^n\log\frac{\sum_{h^{\text{delim}}_{i-1}\in\mathcal D}p(O_i|h^{\text{delim}}_{i-1},\theta)}{\sum_{h^{\text{delim}}_{i-1}\in\mathcal D}p(O_i|h^{\text{delim}}_{i-1},\theta^*)}\Big).\tag{69}$$
- **Start-state step.** Eqs. 70–76: $\sum_{h^{\text{delim}}_{i-1}}p(O_i|h^{\text{delim}}_{i-1},\theta)=\sum_{h^{\text{start}}_i}p(O_i|h^{\text{start}}_i,\theta)\,p(h^{\text{start}}_i|\theta)\sum_{h^{\text{delim}}_{i-1}\in\mathcal D}\frac{p(h^{\text{delim}}_{i-1}|h_i^{\text{start}},\theta)}{p(h^{\text{delim}}_{i-1}|\theta)}$, by Bayes' rule. By A2, each ratio is at most $p(h^{\text{delim}}_{i-1}|h^{\text{start}}_i,\theta)/c_3$ and at least that value divided by $c_4$, giving $\sum\ldots\le1/c_3$ and $\ge1/c_4$ (73–76). Plugging in (as the authors state it):
$$r_n(\theta)\le\frac1n\Big(-\log c_7+2n(\log c_2-\log c_1)+n(\log c_4-\log c_3)+\sum_{i=1}^n\log\frac{p(O_i|\theta)}{p(O_i|\theta^*)}\Big)\xrightarrow{n\to\infty}\mathbb E_{O\sim p_{\text{prompt}}}\Big[\log\frac{p(O|\theta)}{p(O|\theta^*)}\Big]+\epsilon^\theta_{\text{delim}}\tag{77–79}$$
with $\epsilon^\theta_{\text{delim}}=2(\log c_2-\log c_1)+\log c_4-\log c_3$ (80).
- **To KL.** $\mathbb E_{p_{\text{prompt}}}[\log\frac{p(O|\theta)}{p(O|\theta^*)}]=KL(p_{\text{prompt}}\|p(\cdot|\theta^*))-KL(p_{\text{prompt}}\|p(\cdot|\theta))$ (81–82). The expansions of $p_{\text{prompt}}(O)$ and $p(O|\theta^*)$ (84–85) differ only in the hidden start distribution. By A5, $p_{\text{prompt}}(h)/p(h|\theta^*)\le1/c_8$, so $p_{\text{prompt}}(O)\le p(O|\theta^*)/c_8$ and $KL(p_{\text{prompt}}\|p(\cdot|\theta^*))\le-\log c_8$ (86–88; non-negative since $c_8\le1$).
- **Chain rule over tokens.** $-KL(p_{\text{prompt}}\|p(\cdot|\theta))=-\sum_{j=1}^k\mathbb E_{O[1:j-1]\sim p_{\text{prompt}}}[KL(p^j_{\text{prompt}}\|p^j_\theta)]$ (89–92). Hence
$$\lim_{n\to\infty}r_n(\theta)<-\sum_{j=1}^k\mathbb E_{O[1:j-1]\sim p_{\text{prompt}}}[KL(p^j_{\text{prompt}}\|p^j_\theta)]+\epsilon^\theta_{\text{start}}+\epsilon^\theta_{\text{delim}}\tag{93}$$
with $\epsilon^\theta_{\text{start}}=\log(1/c_8)$. The authors say the bound is negative when the sum of KL terms is larger in magnitude than the error terms, and call this condition equivalent to Condition 1. Then $\lim_n\frac{p(S_n,x_{\text{test}}|\theta)}{p(S_n,x_{\text{test}}|\theta^*)}=\lim_n\exp(n\,r_n(\theta))=0$ (94). ∎

*Skip path:* carry forward Eq. 93, whose negativity condition the authors call equivalent to Condition 1.

### Appendix E: Non-distinguishable case (pp. 23–25)
Challenge: when Condition 1 is unsatisfied, Eq. 14 gives an upper bound on the sum of KL divergences for next-token distributions given different-length histories, but the ICL task scores only the $k$-th token (p. 23).

**Lemma 2.** Let $B$ be the set of θ violating Condition 1. Assume $KL(p_{\text{prompt}}(y_{\text{test}}|x_{\text{test}})\|p(y_{\text{test}}|x_{\text{test}},\theta))$ is bounded above for all θ, and that θ* minimizes the multiclass logistic risk $L_{CE}(\theta)=-\mathbb E_{x_{\text{test}}\sim p_{\text{prompt}}}[p_{\text{prompt}}(y_{\text{test}}|x_{\text{test}})\log p(y_{\text{test}}|x_{\text{test}},\theta)]$ (as printed). If
$$\mathbb E_{x_{\text{test}}\sim p_{\text{prompt}}}[KL(p_{\text{prompt}}(y_{\text{test}}|x_{\text{test}})\|p(y_{\text{test}}|x_{\text{test}},\theta))]\le\epsilon_\theta\ \ \forall\theta\in B,\tag{95}$$
then $\lim_nL_{0\text{-}1}(f_n)\le\inf_fL_{0\text{-}1}(f)+g^{-1}(\sup_{\theta\in B}\epsilon_\theta)$ with $g$ as in Eq. 97, the same calibration function as Theorem 2 (p. 23).

*Proof sketch.*
- Dominated convergence moves the limit inside the 0-1 risk (98–100). The limiting predictor is an argmax of $\mathbb E_{\theta\sim q}[p(y|x_{\text{test}},\theta)]$ for some distribution $q$ over $B$ (101).
- Convexity of KL, then exchanging expectations, gives
$$\mathbb E_{x_{\text{test}}}\big[KL(p_{\text{prompt}}\|\mathbb E_{\theta\sim q}[p(\cdot|x_{\text{test}},\theta)])\big]\le\sup_{\theta\in B}\mathbb E_{x_{\text{test}}}[KL(p_{\text{prompt}}(y|x_{\text{test}})\|p(y|x_{\text{test}},\theta))]\tag{102–105}$$
- The expected KL equals $L_{CE}(\theta)-L_{CE}(\theta^*)\le\sup_B\epsilon_\theta$ (106). Theorems 2.2 and 5.11 of Ávila Pires and Szepesvári (2016) convert this to a 0-1 bound, with zero approximation error since $\theta^*\in\Theta$ (p. 24). $g^{-1}$ is roughly linear for $\epsilon<0.7$, where the bound is non-vacuous (p. 24).

**E.1 Proof of Theorem 2** (p. 24). For $\theta\in B$, Eq. 14 fails, so the KL sum is at most $\epsilon^\theta_{\text{start}}+\epsilon^\theta_{\text{delim}}$ (added step). Using (16) over $j=2..k$:
$$\sum_{j=2}^kKL_j(\theta^*\|\theta)\ge\tfrac12\sum_{j=2}^k(\theta-\theta^*)^\top I_{j,\theta^*}(\theta-\theta^*)+(k-1)O(\|\theta-\theta^*\|^3)\ge\tfrac12(k-1)\lambda_{\min}(I_{j,\theta^*})\|\theta-\theta^*\|^2\tag{107–108}$$
$$\Longrightarrow\ \|\theta-\theta^*\|^2\le\frac{\epsilon^\theta_{\text{start}}+\epsilon^\theta_{\text{delim}}}{\tfrac12(k-1)(\min_j\lambda_{\min}(I_{j,\theta^*}))}.\tag{109}$$
(The cubic term is absorbed without comment, and the minimum over $j$ appears in (109).) Then the last-token KL is
$$KL_k(\theta^*\|\theta)\le\tfrac12(\max_j\lambda_{\max}(I_{j,\theta^*}))\|\theta-\theta^*\|^2+O(\|\theta-\theta^*\|^2)\le\frac{(\epsilon^\theta_{\text{start}}+\epsilon^\theta_{\text{delim}})(\max_j\lambda_{\max}(I_{j,\theta^*})+O(1))}{(k-1)\min_j\lambda_{\min}(I_{j,\theta^*})}\tag{110–112}$$
which, since $KL_k=\mathbb E_{x_{\text{test}}}[KL(p_{\text{prompt}}(y_{\text{test}}|x_{\text{test}})\|p(y_{\text{test}}|x_{\text{test}},\theta))]$, is the bound (113) to plug into Lemma 2.

**E.2 Proof of Theorem 3** (pp. 24–25). Condition 1 bounds the sum of KL over all positions, so intermediate tokens are also bounded; the random-length test lets the predictor "take credit" for them. Averaging over positions $2..k$ and using the bound,
$$\mathbb E_{x_{\text{test}}}[KL(\cdot)]\le\frac1{k-1}\sum_{j=2}^k\mathbb E_{O[1:j-1]}KL(p_{\text{prompt}}(O[j]|O[1:j-1])\|p(O[j]|O[1:j-1],\theta))\le\frac{\sup_\theta(\epsilon^\theta_{\text{start}}+\epsilon^\theta_{\text{delim}})}{k-1}\tag{114–116}$$
then Lemma 2 applies.

### Appendix F: Experimental details (pp. 25–31)
**F.1 GINC dataset** (pp. 25–28).
- *Hidden state.* $h_t=[s_t,v_t]$: entity $v_t\in\{1..|\mathcal V|\}$ (e.g. Einstein) and property $s_t\in\{1..|\mathcal S|\}$ (e.g. nationality). They follow independent Markov chains (a factorial HMM). Tokens are deterministic: $p(o_t|h_t)=1$ if $o_t=M[v_t,s_t]$ for a memory matrix $M$ (so A1 holds). All transitions are nonzero and the prior over concepts is uniform (A2, A5) (p. 25).
- *Concept* θ = property transition matrix; the entity transition matrix is shared by all concepts (p. 26). Vocab sizes 50/100/150; the delimiter is token index 1, and sequences are tokenized by whitespace (p. 26).
- *Memory matrix:* 10 entities × 10 properties = 100 hidden states. The first column is the delimiter token; other entries are uniform draws from the vocabulary (p. 26).
- *Property transitions:* 5 matrices, each a convex combination of 100 random permutation matrices with weights $\text{softmax}((u-0.5)/t)$, $u\in[0,1]^{100}$ uniform, $t=0.1$ (117) (p. 26).
- *Entity transitions:* generated the same way, then final matrix $0.1T+0.9I$, so the same entity persists with probability at least 0.9. Without the identity component (Fig. 10), ICL is "still generally successful", though not as well for vocab 50 (p. 27).
- *Start distribution:* $\text{softmax}((u-0.5)/t)$ with $t=10$, sampled only at the beginning of a document (p. 27).
- *Prompts:* sample θ uniformly from Θ (A4). Start distribution uniform over entities with a randomly chosen fixed starting property per prompt. This may not satisfy A3 but works empirically (p. 27). Label $=\arg\max_yp_{\text{prompt}}(y|x_{\text{test}})$ (118), computed by conditioning the HMM on the generated prompt; this differs from the theory, which samples $y_{\text{test}}$ (pp. 27–28). Worked example (Fig. 8): start property 5, entity 3, tokens "l", then "aw", and so on (p. 28).
- *Data sizes:* 1000 training documents of 10240 tokens and 100 validation documents of 1024 tokens. Prompts: $n\in\{0,1,2,4,8,16,32,64\}$, $k\in\{3,5,8,10\}$, 2500 per pair (p. 28).

**F.2 Transformers.** GPT-2 architectures with 4, 12, 16 layers, 12 heads, 768-dim embeddings, dropout 0.1, context 1024; AdamW, batch 8, 5 epochs, peak learning rate 8e-4. Results use 5 seeds (p. 28). **F.3 LSTM.** 6 layers, embedding and hidden size 768, dropout 0.2, 10 epochs (p. 28).

**F.4 Vocabulary size** (pp. 29–30). To do well the model must infer both the concept and the last HMM hidden state. More symbols make hidden-state inference easier, even though the number of output classes increases. Accuracy generally improves with vocabulary size (Figs. 11–14).

**F.5 GPT-3 experiment** (pp. 30–31). Test set: LAMBADA test examples of 200–300 characters. Prompt pools: "train-short" (200–300 chars) and "train-long" (500–600 chars), each cut to 47 examples. 5-shot accuracy (Table 1, p. 30): short 69.8, long 70.7. With 10 examples: short duplicated 69.6, short independent 71.4. Longer examples improve accuracy by almost 1% despite the long/short mismatch, while duplicating short examples (same total length) does not. Five long examples close about 56% of the gap between five short and ten independent short examples, without adding examples (p. 31). The authors' reading: longer examples carry information not directly about the input–output mapping that helps infer the latent concept (p. 31).

## Toy example (ours; illustrative, not from the paper)
**Concept selection.** Two concepts, θ* and θ′, with uniform prior ½ each. Suppose each prompt example has probability 0.2 under θ* and 0.1 under θ′, ignoring mismatch. Then the likelihood ratio θ′/θ* after $n$ examples is $0.5^n$, so $r_n=\ln0.5=-0.693$ per example. Suppose the label "A" has probability 0.9 under θ* and 0.3 under θ′.
- $n=0$: $p(A)=0.5\cdot0.9+0.5\cdot0.3=0.60$.
- $n=3$: ratio $=0.125$; posterior of θ* $=1/(1+0.125)=8/9$. $p(A)=(8/9)(0.9)+(1/9)(0.3)=0.8+0.0333=0.833$.
- As $n\to\infty$, $p(A)\to0.9$, the θ* prediction.

**Condition 1 in miniature.** Suppose each token of an example is 0.8 times as likely under θ′ as under θ*, so a $k$-token example gives ratio $0.8^k$. Suppose the concatenation mismatch lets θ′ gain a fixed factor 1.5 per example (a stand-in for the ε terms). Per-example ratio θ′/θ* is $1.5\cdot0.8^k$.
- $k=1$: $1.5\cdot0.8=1.2>1$. θ′ wins; selection fails.
- $k=2$: $1.5\cdot0.64=0.96<1$. θ* wins slowly.
- $k=3$: $1.5\cdot0.512=0.768<1$.
In log terms the signal is $k\ln(1/0.8)=0.223k$ against an error of $\ln1.5=0.405$. The signal exceeds the error once $k\ge2$ ($0.446>0.405$). Longer examples therefore help, as in Condition 1.

## Concepts
- [[in-context-learning]] — the LM does a task by conditioning on a prompt of input-output examples, with no weight updates; here, implicit Bayesian inference of a shared latent concept (p. 1–3)
- [[zero-shot-few-shot-prompting]] — prompts with 0 or $n$ examples; in GINC zero-shot can beat few-shot early on (p. 11)
- [[latent-concept]] (new) — document-level latent θ that parameterizes an HMM's transitions and determines the task (pp. 2–3)
- [[hidden-markov-model]] (new) — sequence model with hidden states $h_t$ that emit observed tokens; the pretraining document model (p. 3)
- [[mixture-of-hmms-pretraining]] (new) — pretraining distribution $p(o_{1:T})=\int p(o_{1:T}|\theta)p(\theta)d\theta$ (p. 3)
- [[posterior-predictive]] (new) — $p(\text{output}|\text{prompt})$ with the latent concept marginalized out (p. 2)
- [[implicit-bayesian-inference]] (new) — the LM "selects" the prompt concept through marginalization as $p(\text{concept}|\text{prompt})$ concentrates (p. 3)
- [[distinguishability-condition]] (new) — summed per-token KL signal exceeds start and delimiter error terms (Eq. 14) (p. 7)
- [[distribution-mismatch-prompt-pretraining]] (new) — prompts concatenate independent examples and are low-probability under pretraining (p. 4)
- [[bernstein-von-mises]] (new) — under regularity conditions the posterior concentrates on the MLE; its usual assumptions fail here (p. 3)
- [[cross-entropy-log-loss]] — multiclass logistic risk $L_{CE}$ used with the calibration function $g$ to turn KL bounds into 0-1 bounds (p. 23)
- [[perplexity]] — pretraining (validation) loss; in GINC, same loss with different ICL accuracy (p. 10)
- [[pretraining-fine-tuning]] — here only the pretraining distribution is analysed, assumed fit exactly by the LM (p. 2)
- [[calibration-function]] (new) — $g(\delta)$ links excess logistic risk to excess 0-1 risk (p. 8)

## Canonical instances
- [[ginc-dataset]] — synthetic mixture-of-HMMs dataset (entity × property factorial HMM) where Transformers and LSTMs exhibit ICL (pp. 10, 25–28)
- [[names-to-nationalities-prompt]] — "Albert Einstein was German \n … Marie Curie was" illustrates concept inference and mismatch (pp. 1–2, 4)
- [[example-order-sensitivity]] — 10–40% accuracy spread across permutations of 4 examples (p. 10)
- [[zero-shot-beats-few-shot-ginc]] — few-shot accuracy initially below zero-shot at temperature 0.01 (p. 11)
- [[lambada-long-vs-short-examples]] — GPT-3: five long examples beat five short; duplication does not (pp. 30–31)

## Bridges (candidates)
- [structural-analogy] Concept selection by exponentially shrinking likelihood ratios $\exp(n\,r_n)$ ↔ Bayesian model comparison: the posterior concentrates on the best-fitting hypothesis as data accumulate.
- [structural-analogy] Latent document-level concept ↔ topic models (LDA): the paper itself notes this shared latent-variable structure (p. 2), but uses no explicit inference algorithm.
- [metaphor] A persona/backstory prompt selecting a subgroup distribution ↔ silicon sample / algorithmic fidelity (conditioning an LM selects a conditional distribution); the paper does not discuss this.
- [structural-analogy] Distinguishability (signal over $k$ tokens vs. fixed mismatch cost) ↔ signal-to-noise trade-offs, where longer evidence beats fixed bias.

## Questions this raises
- Real LMs are not exact fits to the pretraining distribution. How do approximation error and optimization enter, given that larger GINC models gain ICL accuracy at equal pretraining loss?
- Do real pretraining corpora behave like a mixture of HMMs with delimiter structure, and can "concepts" be identified in them?
- What happens under misspecification, when θ* is not in Θ (A4 relaxed), or for unseen concepts (e.g. semantics–syntax factorization)?
- Why do LSTMs beat Transformers on GINC, and why can zero-shot beat few-shot? Could a theory of the prompt format itself explain this?

## Reading notes
- Page offset: printed = pdf (pages 1–31). The first page shows arXiv:2111.02080v6 [cs.CL], 21 Jul 2022. No venue is printed in these pages.
- Section 4 refers to "Table 6", but the page shows it as Figure 6 (a table). The intro cites "Figure 9" for the HMM sampling process.
- At vocab 150 in Fig. 6, the 12-layer Transformer (98.4 ± 0.4) is slightly above the 16-layer (98.1 ± 0.5), so "steadily increases" holds clearly only at vocab 50 and 100.
- Appendix F.1: the "Transformation matrix for entities" paragraph has an unfinished sentence ("Letting T be … property transition matrix,") followed by a restated paragraph. Two consecutive paragraphs are both headed "Prompt distribution". Appendix D has a typo ("the sum can must be"). The $L_{CE}$ formula in Lemma 2 omits a sum over $y$ as printed. Theorem 2 gives $g$ on $[0,1)$ while Lemma 2 says $[0,1]$.
- Eq. 93 is stated with "<" although the preceding limit is an upper bound; reproduced as printed. The step from (107) to (109) silently absorbs the cubic term. The step "$\ge1/c_4$" in (76) is as printed and not discussed.
- Theorem 2's proof requires $\theta\in B$ to bound the KL sum by $\epsilon_{\text{start}}+\epsilon_{\text{delim}}$; I made that explicit with (added step).
- Pages 13–15 are the reference list, not digested.
