# HANDOFF — resume point for the VP ≠ VNP tutorial

**Read this file first in each new session.** The project has no `CLAUDE.md`.
This file is public: GitHub Pages serves it. Do not add personal data, local paths or session links.

## Current state (verified 2026-11-26)

- **Done.** One-page tutorial `index.html` with 4 tabs:
  - A. Background
  - B. Anthropic proof
  - C. OpenAI proof
  - D. Comparison
  - Sections B12 and C11 link each AHA item to its section.
- **Commits.**
  - `5a30f6f` added the tutorial.
  - `69d1e0c` changed the README links after the repo rename.
- **Repo.** https://github.com/az9713/openai-anthropic-vp-vnp-tutorial (public, branch `main`).
  - The repo was renamed from `openai-anthropic-vp-vnp`. GitHub forwards the old repo address.
- **Live page.** https://az9713.github.io/openai-anthropic-vp-vnp-tutorial/
  - On 2026-11-26 it returned HTTP 200, with Pages status "built".
  - The old Pages address returns 404.
- **Git state at the time of writing.** The working tree was clean, and local HEAD and `origin/main` were both `69d1e0c`.
  - This file is committed after that commit.
  - Use `git log` for the current HEAD.
- **Local-only files.** `.gitignore` keeps them out of the repo. Only the original working folder has them; a clone does not.
  - `sources/anthropic/paper.pdf` and `paper.txt`: the paper and its text extraction.
  - `sources/openai/paper.pdf`, `Paper.tex` and `README.md`: the paper, its LaTeX source and the preprint README.
  - `transcripts/`: the cleaned YouTube automatic captions.
  - Download them again from the 3 links in `README.txt`.

## Next task

- **No task is open.** All requested work is done and pushed.
- **Open items, from the user's choice only:**
  1. **Browser test.** Nobody has tested the tabs in a browser by a click on a tab and on a link between tabs.
     - Open the live page.
     - Click each tab.
     - Click one link in C11 and one link in the Contents list that goes to a different part.
  2. **License.** The repo has no `LICENSE` for the tutorial text itself.
  3. **OpenAI successor papers.** The two OpenAI papers of 24 November were not read. Part C10 only summarizes their READMEs.
  4. **`Pstar` and `f_n`.** Nobody has determined if the Lean `Pstar` (in `lean/OAI/Computability/VPVNP/QuantitativeSeparation.lean` of `openai/math`) is the paper's polynomial `f_n`. Part C10 and Part D4 say "not determined".

## Where to read things

- `README.md`: the sources, the file table and the license notes for the 3 copied `.lean` files (Apache-2.0).
- `index.html` › "Sources and method" (end of tab D): which source files were read, and what was not done.
- `hub_shift_check.py`: a numeric check of section B7.
  - Run `python hub_shift_check.py`.
  - The table in B7 shows its output.

## Workflow provenance

- **Skills used:**
  - `rigorous-explainer`: the HTML scaffold and these check scripts: `checktex`, `checklt`, `check_links`, `check_svg`, `verify_dom`, `check_frame`, `escape_math_lt`, `shoot`.
  - `handoff-after-clear`: this file.
- **Reviewer.** An advisor reviewer read the draft two times. Its corrections are in the commits:
  - Lean coverage.
  - The hub-shift scaling.
  - The determinantal-complexity credit.
- **Last checks, 2026-11-25, on `index.html`:**
  - 0 math errors.
  - 60 internal links, 0 broken.
  - 0 clipped figures.
- **Lean.** Neither Lean build was run. The tutorial reports the build status that each repository states.

## Session-transient scratch

- The PDF pages were rendered with PyMuPDF (`fitz`) into a temporary folder, which was then deleted. The committed `index.html` holds the result.
- The tabs are built in the page itself. A script at the end of `index.html` (`initTabs`) wraps each `<h2 id="parta|partb|partc|partd">` and the content after it in a panel, after MathJax finishes.

## How to work

- **Writing style.** Edit the text in `index.html` directly. Keep the style rules: ASD-STE100 sentences, precise numbers, and a dashed `.mine` box for each judgment of your own.
- **Checks.** After each edit, run the `rigorous-explainer` checks on `index.html`.
- **Personal data.**
  - Commit with the no-reply author identity, which is set in the repo `.git/config`.
  - Before a push, search the files for personal data.
