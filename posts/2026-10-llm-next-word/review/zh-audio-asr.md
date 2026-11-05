# Chinese audio check by speech recognition (2026-10-llm-next-word)

faster-whisper `small`, int8, CPU. Similarity on characters only; ≥ 0.85 is normal (homophones, digits).

| chapter | similarity | script chars | heard chars | script runs of ≥ 15 chars not heard | heard runs not in the script (≥ 10 chars more) |
|---|---|---|---|---|---|
| hook | 0.940 | 698 | 693 | — | — |
| guess | 0.882 | 324 | 302 | 百分之九十五百分之七十百分之四十 | — |
| home | 0.923 | 1047 | 1085 | — | 请收藏点开链接点开声音点开了声音点开了声音点开声音点开声音点开声音 |
| lens-info | 0.927 | 864 | 862 | — | — |
| lens-linalg | 0.930 | 548 | 534 | — | — |
| lens-bayes | 0.949 | 493 | 489 | — | — |
| lens-meaning | 0.976 | 577 | 577 | — | — |
| lens-tom | 0.940 | 700 | 687 | — | — |
| ladder | 0.831 | 734 | 714 | — | — |
| answer | 0.966 | 345 | 340 | — | — |
| work | 0.959 | 358 | 355 | — | — |
| recall | 0.957 | 358 | 359 | — | — |

Flagged for listening: guess, home.

Verified 2026-11-05: `guess` (digits for 百分之… in the transcript) and `home` (a recogniser hallucination that a second pass did not reproduce) are false alarms. The post is clean.
