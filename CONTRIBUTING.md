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
