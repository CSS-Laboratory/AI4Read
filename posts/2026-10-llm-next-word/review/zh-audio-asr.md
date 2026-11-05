# Chinese audio check by speech recognition (2026-10-llm-next-word)

faster-whisper `small`, int8, CPU. Similarity on characters only; ≥ 0.85 is normal (homophones, digits).

| chapter | similarity | script chars | heard chars | script runs of ≥ 15 chars not heard |
|---|---|---|---|---|
| hook | 0.940 | 698 | 693 | — |
| guess | 0.882 | 324 | 302 | 百分之九十五百分之七十百分之四十 |
| home | 0.938 | 1047 | 1052 | — |
| lens-info | 0.927 | 864 | 862 | — |
| lens-linalg | 0.930 | 548 | 534 | — |
| lens-bayes | 0.949 | 493 | 489 | — |
| lens-meaning | 0.976 | 577 | 577 | — |
| lens-tom | 0.940 | 700 | 687 | — |
| ladder | 0.831 | 734 | 714 | — |
| answer | 0.966 | 345 | 340 | — |
| work | 0.959 | 358 | 355 | — |
| recall | 0.957 | 358 | 359 | — |

Flagged for listening: guess.
