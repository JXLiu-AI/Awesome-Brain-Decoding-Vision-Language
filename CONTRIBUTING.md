# Contributing

The markdown in this repository is **generated**. Editing `README.md` or anything under
`docs/` (except `_readme_head.md` / `_readme_tail.md`) will be overwritten on the next
build. Edit the YAML under `data/`.

```bash
pip install pyyaml
python scripts/resolve.py     # fill links/venues/citations for new entries
python scripts/build.py       # regenerate README.md and docs/
```

## Adding a paper

Add an entry to `data/papers.yaml` with **only** the hand-written fields:

```yaml
- key: scotti2024mindeye2          # firstauthor + year + short name
  title: "MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data"
  year: 2024
  modality: [fMRI]                 # fMRI | EEG | MEG
  task: [image-recon]              # see the task list at the top of papers.yaml
  datasets: [nsd]                  # ids from datasets.yaml -- the build fails on unknown ids
  code: https://github.com/MedARC-AI/MindEyeV2
```

Do not write `paper:`, `doi:`, `arxiv:`, `venue:` or `citations:` by hand. `resolve.py`
fetches them, requiring a 0.90 title similarity before it accepts a match. This is the rule
that keeps the list free of plausible-looking wrong links.

**Coverage policy** (`data/config.yaml`): everything in scope from 2024-01-01 onward gets an
entry. Before 2024 the list is deliberately selective — milestones only. A pre-2024 addition
needs a sentence in the PR saying why it is still load-bearing.

## Adding a benchmark number

This is the part that makes the list worth more than a link dump, so it has the strictest
rule. A metric is only accepted with all four of:

```yaml
  metrics:
    - dataset: nsd
      split: "shared-982, subj01"
      repeats: averaged-3        # or single-trial
      pool: 982                  # retrieval pool size; null for non-retrieval metrics
      hours_target_subject: 30   # per-subject training data the model consumed
      values: {pixcorr: 0.322, clip: 0.947}
      source: "Table 1"
      verified_by: "@your-handle"
```

Missing any of `split`, `repeats`, `pool`, `hours_target_subject`? Then the number is not
comparable to the numbers next to it, and it will be rejected. Leaving a cell empty is the
intended outcome, not a failure.

## Flagging a pitfall

If a paper's evaluation is subject to a documented confound, add its id to that paper's
`flags:`. To document a new one, add an entry to `data/pitfalls.yaml` — it must name the
published work that established it and give a check a reader can run. "I think this is
probably wrong" is not enough; the whole file has to stay defensible.

## Reproducibility status

`repro: ran-ok` and `repro: ran-mismatch` may only be set by someone who actually ran the
code. Say so in the PR: which commit, which GPU, which numbers you got. `claimed` is the
default for any repo with released code that nobody here has run.

## Out of scope

Invasive BCI, motor imagery, P300 spellers, seizure and sleep staging, emotion recognition.
Good lists exist for those and are linked from the README.

## Marking what changed between updates

Every paper carries an `added:` date. `data/config.yaml` holds a `releases:` list, and
anything added after the newest release date renders as new: a one-line banner at the top
of the README saying how many and since when, plus an in-place highlight on the rows
themselves, so you can see where each addition lands rather than only that it exists.

The banner deliberately does not list the new entries. An earlier version did, and it meant
every new paper appeared twice on the same page -- once in a summary table and once
highlighted below it. The highlight already answers "which ones"; the banner only needs to
answer "how many, since when".

```bash
python scripts/release.py v0.2 --note "first bulk import"   # roll the window forward
python scripts/build.py
```

`highlight.style` in `data/config.yaml` picks how the in-place mark is drawn:

| Style | What you get | Trade-off |
|---|---|---|
| `mark` (default) | `<mark>` — a real background highlight | GitHub's theme picks the colour (light yellow); CSS is stripped from READMEs so it cannot be set to pink |
| `badge` | a light-pink shields.io pill in the Year column | exact colour, but a badge beside the row rather than a background behind it |
| `both` | both | noisier |
| `none` | nothing | the What's new table still appears |

**Open question:** a genuine pink row background needs real CSS, which means publishing a
GitHub Pages build alongside the README. Worth doing once the list is large enough that
readers scroll rather than search.
