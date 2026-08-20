# Awesome Brain Decoding: Vision & Language

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Build](https://github.com/OWNER/Awesome-Brain-Decoding-Vision-Language/actions/workflows/build.yml/badge.svg)](../../actions/workflows/build.yml)
[![Last commit](https://img.shields.io/github/last-commit/OWNER/Awesome-Brain-Decoding-Vision-Language)](../../commits/main)

Decoding **what a person is seeing and what a person is hearing or reading** from
**non-invasive** brain recordings — fMRI, EEG and MEG.

Most lists in this area are link dumps, and a link dump cannot tell you that two
state-of-the-art numbers were measured on different splits, with different retrieval pool
sizes, on different amounts of per-subject data. This one is built around that problem:

- **Every number carries its conditions.** A metric appears in [benchmarks.md](docs/benchmarks.md)
  only once its split, retrieval pool size and per-subject data budget are recorded with it.
  Otherwise the cell stays empty. An empty cell is more honest than an incomparable one.
- **Known confounds are first-class.** [pitfalls.md](docs/pitfalls.md) documents the
  block-design leak, evaluation-time teacher forcing and four others — each with the paper
  that established it and a test you can run yourself. Affected papers are flagged inline.
- **Nothing is typed from memory.** Titles are hand-written; every link, venue and citation
  count is resolved from the Semantic Scholar and arXiv APIs by `scripts/resolve.py`.
- **Datasets are compared on what limits you.** Not "8 subjects", but how many hours each
  of those subjects actually contributed. See [datasets.md](docs/datasets.md).

New arXiv preprints are swept daily and land in a review queue rather than straight into
the list — see [Automation](#automation).
