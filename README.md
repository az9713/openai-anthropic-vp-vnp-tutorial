# VP ≠ VNP: the two AI proofs, a guided walk

A tutorial on the two proofs of VP ≠ VNP that Anthropic and OpenAI published on 23 November 2026.

**Read it as a live page: https://az9713.github.io/openai-anthropic-vp-vnp-tutorial/**

The page has four tabs:

- **A. Background** — P versus NP, arithmetic circuits, VP and VNP, the permanent, and how VP versus VNP relates to P versus NP.
- **B. The Anthropic proof** — a step-by-step walk, with the AHA moments.
- **C. The OpenAI proof** — a step-by-step walk, with the AHA moments.
- **D. Comparison** — results, structure, machine checks, quality, complexity, elegance, readability.

It is written for a reader who took one complexity course and forgot most of it.

## Status of the claims

- Both papers say that an AI model found and wrote the proof. Neither paper claims a check by a human mathematician.
- Each proof comes with a Lean 4 formalization. The Lean builds were **not** run for this tutorial; the build status in the tutorial is what the two repositories state.
- The tutorial explains what the papers say. It is not an independent verification. It was written with an AI assistant.
- Neither result settles P versus NP.

## Sources

These are the sources listed in `README.txt`:

1. Video: "VP ≠ VNP: what the two AI proofs actually do", channel Dirac — https://www.youtube.com/watch?v=HgqnBtPGmww
2. Anthropic paper and Lean proof — https://github.com/anthropics/formal-math/tree/main/vp-vnp
3. OpenAI paper and Lean proof — https://github.com/openai/math/tree/main/preprints/VP-and-VNP-are-different-November-23-2026

The tutorial's last section, [Sources and method](https://az9713.github.io/openai-anthropic-vp-vnp-tutorial/#sources), lists which files of each source were read and what was not done.

## Files

| File | Content |
|---|---|
| `index.html` | The tutorial. One self-contained page; formulas load MathJax from a CDN. |
| `hub_shift_check.py` | Numeric check of the "shift the hub" step (tutorial section B7). Run `python hub_shift_check.py`; it needs only the Python standard library. |
| `README.txt` | The original list of source links. |
| `sources/anthropic/Statement.lean`, `sources/anthropic/Challenge.lean` | Unchanged copies of the Lean statement files from `anthropics/formal-math`, folder `vp-vnp`. Copyright Anthropic, PBC. Apache License 2.0. |
| `sources/openai/VPVNP.lean` | Unchanged copy of `lean/ComparatorChallenges/VPVNP.lean` from `openai/math`. Apache License 2.0. |

The papers themselves are not copied here. Use the links above.

## License of third-party files

The three `.lean` files are redistributed without change under the Apache License, Version 2.0: https://www.apache.org/licenses/LICENSE-2.0 . See the `LICENSE` and `NOTICE` files of the two source repositories.
