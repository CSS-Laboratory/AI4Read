---
id: bai-2022-constitutional/index
work: bai-2022-constitutional
type: work-map
units: [bai-2022-constitutional/main]
generated: deterministic
---

# Bai, Y., Kadavath, S., Kundu, S., Askell, A., et al. (2022). *Constitutional AI: Harmlessness from AI Feedback*. arXiv:2212.08073.

## One digest
This work has a single digest, which is also its work-level summary: [[bai-2022-constitutional/main]].

## In one line
A helpful language model can be trained to be relatively harmless, with a short written list of principles as the only human harmlessness supervision, by letting a model critique, revise and rank its own outputs instead of using human harmlessness labels.

## The gist
Can an AI assistant be made harmless without human labels that mark harmful outputs? The authors use a short list of written principles (a "constitution"). In a supervised stage, a helpful model critiques and revises its own harmful answers, then is fine-tuned on the revisions. In an RL stage, a model chooses the more harmless of two responses according to a principle; these AI labels train a preference model, which is the reward for RL (RLAIF). Crowdworkers judge the resulting models more harmless than RLHF models at similar helpfulness, and the authors find them virtually never evasive. It matters as a test of using AI to help supervise AI.

**Prerequisites:** RLHF basics (preference model as reward, policy trained by RL); few-shot and chain-of-thought prompting; Elo scores from pairwise comparisons; the idea of "red teaming" (writing prompts that bait a model into harm).
