---
id: interference
type: concept
fields: [control-theory, llm]
n_sources: 2
tiers: [core, deep]
grounding: digests
sources: [ashby-1956-cybernetics/ch08-transmission, elhage-2022-superposition/main-p1]
generated_by: build_kg.py
---

# interference

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch08-transmission]] (p. 158–159): whether two messages sharing a channel destroy each other. They need not, if no variety is lost and the mechanism is determinate [new]

### llm

- [[elhage-2022-superposition/main-p1]] (§ "The Superposition Hypothesis"): a feature's activity appearing as small activity in others because directions are non-orthogonal [new]

## Instances that use it

- [[call-tomasello-low-inhibition-task]] — non-verbal false belief task with reduced self-interference, not easier for children — from [[apperly-2011-mindreaders/ch02-evidence]]
- [[samson-avatar-dots-task]] — altercentric interference from an avatar who sees fewer dots — from [[apperly-2011-mindreaders/ch07-elaborating]]
- [[surtees-level-2-digit-task]] — 6/9 digits give egocentric but no altercentric interference — from [[apperly-2011-mindreaders/ch07-elaborating]]
- [[adversarial-vulnerability-from-interference]] — $\epsilon$ off-diagonal terms exploited by attacks — from [[elhage-2022-superposition/main-p1]]

## Candidate bridges

- [structural-analogy] altercentric and egocentric interference ↔ cognitive psychology: congruency effects — both slow responses when irrelevant information conflicts with the target. — from [[apperly-2011-mindreaders/ch05-evidence]] (theory-of-mind → other)
- [structural-analogy] Gaussian broadcast successive decoding ↔ interference cancellation in the Gaussian interference channel — both decode a codeword, subtract it, then decode the rest. — from [[cover-2006-elements/ch14-network-p1]] (information-theory → unspecified)
- [same-math] Linear-model interference $\sum_{i\ne j}|W_i\cdot W_j|^2$ ↔ compressed sensing: coherence $\max_{i\ne j}|W_i\cdot W_j|$ — the $L^2$ and $L^\infty$ norms of the same off-diagonal vector. — from [[elhage-2022-superposition/main-p1]] (llm → other)
- [metaphor] Mental shotgun ↔ interference effects in cognitive tasks: an irrelevant dimension slows a main task. — from [[kahneman-2011-thinking/ch08-judgments]] (decision-game-theory → other)
