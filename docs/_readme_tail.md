## Legend

| Mark | Meaning |
|---|---|
| ⚠️ next to a title | link not yet resolved by `scripts/resolve.py` |
| ⏳ next to a title | accepted at a venue, not yet indexed anywhere |
| 📄 next to a title | preprint with no version of record |
| `` `block-design` `` and similar | this paper's evaluation is subject to a documented pitfall — see [pitfalls.md](docs/pitfalls.md) |
| ⛔️ next to a dataset | known to be unsuitable for new work; kept for historical reference |
| ✅ / ⚠️ in Verified | whether a human has checked these numbers against the source |

## Preprints

Preprints stay in. On a 60-paper sample of the candidate pool, 100% of 2023 entries could
be verified as published against 8% of 2026 entries -- publication lag in this field runs
9 to 18 months, so a published-only rule removes the newest work, not the weakest. It also
removes true positives: Duala is a CVPR 2026 paper that neither Crossref nor DBLP had
indexed when this list first added it.

Status is therefore a derived field and a [separate view](docs/published-only.md), never a
filter on what the list may contain.

## Scope

In scope: non-invasive recordings (fMRI, EEG, MEG, and fNIRS where it appears) used to
decode visual or linguistic content — reconstruction, retrieval, captioning, continuous
language and speech decoding, plus the representation, evaluation and critique papers
needed to read those results.

Out of scope, deliberately: invasive BCI (ECoG, Utah arrays), motor imagery and P300
spellers, clinical diagnosis, emotion recognition. Each has a good list already; see
[Related lists](#related-lists).

## Automation

`.github/workflows/daily-arxiv.yml` runs `scripts/fetch_arxiv.py` every day, queries arXiv
for the topic keywords, filters out anything already in `data/papers.yaml`, and opens a
single issue with the candidates. Nothing enters the list without a human deciding it
belongs. `.github/workflows/build.yml` regenerates every table on push and fails the build
if a paper references an unknown dataset or pitfall id.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Short version: edit `data/*.yaml`, never the
generated markdown; write only the title by hand and let `resolve.py` fetch the link; and
if you are adding a benchmark number, you must also record its split, pool size and
per-subject budget, or it will not be accepted.

## Related lists

- [NeuSpeech/awesome-brain-decoding](https://github.com/NeuSpeech/awesome-brain-decoding) — broader brain decoding including music and audio
- [willxxy/awesome-mmps](https://github.com/willxxy/awesome-mmps) — multimodal physiological signals, actively maintained
- [MichaelMaiii/AIGC-Brain](https://github.com/MichaelMaiii/AIGC-Brain) — brain-conditional synthesis survey and taxonomy
- [subbareddy248/Awesome-Brain-Encoding--Decoding](https://github.com/subbareddy248/Awesome-Brain-Encoding--Decoding) — language encoding models
- [jackwyaya/Awesome-iBCIs](https://github.com/jackwyaya/Awesome-iBCIs) — invasive BCI, the complement to this list
- [braindecode](https://github.com/braindecode/braindecode) — a toolbox rather than a list, but the standard entry point for EEG/MEG deep learning

## License

[CC0-1.0](LICENSE). Paper metadata is factual; each linked work remains under its own terms.
