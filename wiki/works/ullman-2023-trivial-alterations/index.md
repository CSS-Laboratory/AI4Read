---
id: ullman-2023-trivial-alterations/index
work: ullman-2023-trivial-alterations
type: work-map
units: [ullman-2023-trivial-alterations/main]
generated: deterministic
---

# Ullman, T. (2023). Large language models fail on trivial alterations to theory-of-mind tasks. arXiv:2302.08399 [cs.AI].

## One digest
This work has a single digest, which is also its work-level summary: [[ullman-2023-trivial-alterations/main]].

## In one line
GPT-3.5 passes classic false-belief vignettes, but small changes that leave the logic of Theory-of-Mind intact make it fail, so Ullman argues for a skeptical default and for treating outlying failures as more informative than average success.

## The gist
Kosinski (1) reported that current LLMs (GPT-3.5 did best) succeed on classic Theory-of-Mind (ToM) tasks at a level comparable to 9-year-old children. Ullman asks whether this survives small perturbations that should not matter to an entity with ToM. He alters the "unexpected contents" and "unexpected transfer" vignettes (transparent containers, an illiterate reader, trusted testimony, a different person queried). GPT-3.5 then gives the wrong answer, mostly with high probability. He concludes that LLMs probably have not spontaneously developed ToM. He also argues that even a future model that passes such tests need not be credited with ToM, because, he argues, inferences about minds can also take into account the likely algorithms behind behaviour, not only input–output behaviour.

**Prerequisites:** false-belief tasks (unexpected contents, unexpected transfer); that an LLM assigns probabilities to next-word completions.
