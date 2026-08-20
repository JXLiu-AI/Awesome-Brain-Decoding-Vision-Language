# Awesome Brain Decoding: Vision & Language

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Build](https://github.com/JXLiu-AI/Awesome-Brain-Decoding-Vision-Language/actions/workflows/build.yml/badge.svg)](../../actions/workflows/build.yml)
[![Last commit](https://img.shields.io/github/last-commit/JXLiu-AI/Awesome-Brain-Decoding-Vision-Language)](../../commits/main)

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

**45 papers · 18 datasets · 5 documented evaluation pitfalls**  
Coverage: fMRI 31 · EEG 13 · MEG 5

| | |
|---|---|
| [Datasets](docs/datasets.md) | what each corpus actually contains, and the per-subject budget it gives you |
| [Pitfalls](docs/pitfalls.md) | the confounds that make published numbers incomparable, with a test for each |
| [Benchmarks](docs/benchmarks.md) | metrics, reported only with split, pool size and data budget attached |
| [Reproducibility](docs/reproducibility.md) | which released code has actually been run by someone |

---


## Papers

### Image reconstruction  <sub>(19)</sub>

| Year | Paper | Modality | Venue | Data | Code |
|---|---|---|---|---|---|
| 2025 | [MindAligner: Explicit Brain Functional Alignment for Cross-Subject Visual Decoding from Limited fMRI Data](https://arxiv.org/abs/2502.05034v1)  | fMRI | — | Natural Scenes Dataset | [code](https://github.com/Da1yuqin/MindAligner) |
| 2024 | [Brain decoding: toward real-time reconstruction of visual perception](https://arxiv.org/abs/2310.19812v3)  | MEG | — | THINGS-MEG | — |
| 2024 | [DREAM: Visual Decoding from Reversing Human Visual System](https://doi.org/10.1109/wacv57701.2024.00804)  | fMRI | WACV 2024 | Natural Scenes Dataset | [code](https://github.com/weihaox/DREAM) |
| 2024 | [MindBridge: A Cross-Subject Brain Decoding Framework](https://doi.org/10.1109/cvpr52733.2024.01077)  | fMRI | CVPR 2024 | Natural Scenes Dataset | [code](https://github.com/littlepure2333/MindBridge) |
| 2024 | [MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://arxiv.org/abs/2403.11207v2)  | fMRI | — | Natural Scenes Dataset | [code](https://github.com/MedARC-AI/MindEyeV2) |
| 2024 | [NeuroPictor: Refining fMRI-to-Image Reconstruction via Multi-individual Pretraining and Multi-level Modulation](https://doi.org/10.1007/978-3-031-72983-6_4)  | fMRI | ECCV 2024 | Natural Scenes Dataset | — |
| 2024 | [UMBRAE: Unified Multimodal Brain Decoding](https://doi.org/10.1007/978-3-031-72667-5_14)  | fMRI | ECCV 2024 | Natural Scenes Dataset | [code](https://github.com/weihaox/UMBRAE) |
| 2024 | [UniBrain: Unify Image Reconstruction and Captioning All in One Diffusion Model from Human Brain Activity](https://arxiv.org/abs/2308.07428v1)  | fMRI | — | Natural Scenes Dataset | — |
| 2024 | [Visual Decoding and Reconstruction via EEG Embeddings with Guided Diffusion](https://doi.org/10.52202/079017-3266)  | EEG | NeurIPS 2024 | THINGS-EEG2 | [code](https://github.com/dongyangli-del/EEG_Image_decode) |
| 2023 | [DreamDiffusion: Generating High-Quality Images from Brain EEG Signals](https://arxiv.org/abs/2306.16934v2)  | EEG | — | — | [code](https://github.com/bbaaii/DreamDiffusion) |
| 2023 | [High-resolution image reconstruction with latent diffusion models from human brain activity](https://doi.org/10.1109/cvpr52729.2023.01389)  | fMRI | CVPR 2023 | Natural Scenes Dataset | — |
| 2023 | [MindDiffuser: Controlled Image Reconstruction from Human Brain Activity with Semantic and Structural Diffusion](https://doi.org/10.1145/3581783.3613832)  | fMRI | ACM MM 2023 | Natural Scenes Dataset | — |
| 2023 | [Natural scene reconstruction from fMRI signals using generative latent diffusion](https://doi.org/10.1038/s41598-023-42891-8)  | fMRI | Sci Rep | Natural Scenes Dataset | [code](https://github.com/ozcelikfu/brain-diffuser) |
| 2023 | [Reconstructing the Mind's Eye: fMRI-to-Image with Contrastive Learning and Diffusion Priors](https://doi.org/10.52202/075280-1073)  | fMRI | NeurIPS 2023 | Natural Scenes Dataset | [code](https://github.com/MedARC-AI/fMRI-reconstruction-NSD) |
| 2023 | [Seeing Beyond the Brain: Conditional Diffusion Model with Sparse Masked Modeling for Vision Decoding](https://doi.org/10.1109/cvpr52729.2023.02175)  | fMRI | CVPR 2023 | Generic Object Decoding, BOLD5000 | [code](https://github.com/zjc062/mind-vis) |
| 2022 | [Mind Reader: Reconstructing complex images from brain activities](https://doi.org/10.52202/068431-2148)  | fMRI | NeurIPS 2022 | Natural Scenes Dataset | — |
| 2022 | [Self-supervised natural image reconstruction and large-scale semantic classification from brain activity](https://doi.org/10.1016/j.neuroimage.2022.119121)  | fMRI | NeuroImage | Generic Object Decoding | — |
| 2019 | [Deep image reconstruction from human brain activity](https://doi.org/10.1371/journal.pcbi.1006633)  | fMRI | PLoS Comput Biol | Deep Image Reconstruction | [code](https://github.com/KamitaniLab/DeepImageReconstruction) |
| 2019 | [From voxels to pixels and back: Self-supervision in natural-image reconstruction from fMRI](https://arxiv.org/abs/1907.02431v1)  | fMRI | — | Generic Object Decoding | — |

### Video reconstruction  <sub>(3)</sub>

| Year | Paper | Modality | Venue | Data | Code |
|---|---|---|---|---|---|
| 2024 | [NeuroClips: Towards High-fidelity and Smooth fMRI-to-Video Reconstruction](https://doi.org/10.52202/079017-1636)  | fMRI | NeurIPS 2024 | — | [code](https://github.com/gongzix/NeuroClips) |
| 2023 | [Cinematic Mindscapes: High-quality Video Reconstruction from Brain Activity](https://doi.org/10.52202/075280-1079)  | fMRI | NeurIPS 2023 | — | [code](https://github.com/jqin4749/MindVideo) |
| 2018 | [Neural Encoding and Decoding with Deep Learning for Dynamic Natural Vision](https://doi.org/10.1093/cercor/bhx268)  | fMRI | Cerebral Cortex | — | — |

### Image retrieval / identification  <sub>(5)</sub>

| Year | Paper | Modality | Venue | Data | Code |
|---|---|---|---|---|---|
| 2024 | [Brain decoding: toward real-time reconstruction of visual perception](https://arxiv.org/abs/2310.19812v3)  | MEG | — | THINGS-MEG | — |
| 2024 | [Decoding Natural Images from EEG for Object Recognition](https://arxiv.org/abs/2308.13234v3)  | EEG | — | THINGS-EEG2 | — |
| 2024 | [Lite-Mind: Towards Efficient and Robust Brain Representation Learning](https://doi.org/10.1145/3664647.3681229)  | fMRI | ACM MM 2024 | Natural Scenes Dataset | [code](https://github.com/gongzix/Lite-Mind) |
| 2024 | [Visual Decoding and Reconstruction via EEG Embeddings with Guided Diffusion](https://doi.org/10.52202/079017-3266)  | EEG | NeurIPS 2024 | THINGS-EEG2 | [code](https://github.com/dongyangli-del/EEG_Image_decode) |
| 2023 | [Reconstructing the Mind's Eye: fMRI-to-Image with Contrastive Learning and Diffusion Priors](https://doi.org/10.52202/075280-1073)  | fMRI | NeurIPS 2023 | Natural Scenes Dataset | [code](https://github.com/MedARC-AI/fMRI-reconstruction-NSD) |

### Brain captioning  <sub>(4)</sub>

| Year | Paper | Modality | Venue | Data | Code |
|---|---|---|---|---|---|
| 2025 | [Learning Interpretable Representations Leads to Semantically Faithful EEG-to-Text Generation](https://arxiv.org/abs/2505.17099v1)  | fMRI | — | — | [code](https://github.com/justin-xzliu/GLIM) |
| 2024 | [UMBRAE: Unified Multimodal Brain Decoding](https://doi.org/10.1007/978-3-031-72667-5_14)  | fMRI | ECCV 2024 | Natural Scenes Dataset | [code](https://github.com/weihaox/UMBRAE) |
| 2024 | [UniBrain: Unify Image Reconstruction and Captioning All in One Diffusion Model from Human Brain Activity](https://arxiv.org/abs/2308.07428v1)  | fMRI | — | Natural Scenes Dataset | — |
| 2023 | [Brain Captioning: Decoding human brain activity into images and text](https://arxiv.org/abs/2305.11560v1)  | fMRI | — | Natural Scenes Dataset | — |

### Continuous language reconstruction  <sub>(3)</sub>

| Year | Paper | Modality | Venue | Data | Code |
|---|---|---|---|---|---|
| 2023 | [Semantic reconstruction of continuous language from MEG signals](https://doi.org/10.1109/icassp48485.2024.10448281)  | MEG | ICASSP 2024 - 2024 IEEE Interna… | — | — |
| 2023 | [Semantic reconstruction of continuous language from non-invasive brain recordings](https://doi.org/10.1038/s41593-023-01304-9)  | fMRI | Nat Neurosci | Natural language fMRI dataset | [code](https://github.com/HuthLab/semantic-decoding) |
| 2018 | [Toward a universal decoder of linguistic meaning from brain activation](https://doi.org/10.1038/s41467-018-03068-4)  | fMRI | Nat Commun | Pereira et al. 2018 sentence fMRI | — |

### Speech decoding  <sub>(1)</sub>

| Year | Paper | Modality | Venue | Data | Code |
|---|---|---|---|---|---|
| 2023 | [Decoding speech perception from non-invasive brain recordings](https://doi.org/10.1038/s42256-023-00714-5)  | MEG/EEG | Nat Mach Intell | MEG-MASC, Natural Speech, Brennan and Hale "Alice" EEG, MOUS | [code](https://github.com/facebookresearch/brainmagick) |

### Brain-to-text  <sub>(3)</sub>

| Year | Paper | Modality | Venue | Data | Code |
|---|---|---|---|---|---|
| 2025 | [Brain-to-Text Decoding: A Non-invasive Approach via Typing](https://arxiv.org/abs/2502.17480v1)  | MEG/EEG | — | — | [code](https://github.com/facebookresearch/brain2qwerty) |
| 2023 | [DeWave: Discrete Encoding of EEG Waves for EEG to Text Translation](https://doi.org/10.52202/075280-0432) `teacher-forcing` | EEG | NeurIPS 2023 | ZuCo 1.0 / 2.0 | — |
| 2022 | [Open Vocabulary Electroencephalography-To-Text Decoding and Zero-shot Sentiment Classification](https://doi.org/10.1609/aaai.v36i5.20472) `teacher-forcing` | EEG | AAAI 2022 | ZuCo 1.0 / 2.0 | — |

### Representation / encoding analyses  <sub>(7)</sub>

| Year | Paper | Modality | Venue | Data | Code |
|---|---|---|---|---|---|
| 2023 | [Scaling laws for language encoding models in fMRI](https://doi.org/10.52202/075280-0958)  | fMRI | NeurIPS 2023 | Natural language fMRI dataset | — |
| 2022 | [A large and rich EEG dataset for modeling human visual object recognition](https://doi.org/10.32470/ccn.2022.1029-0)  | EEG | 2022 Conference on Cognitive Co… | THINGS-EEG2 | — |
| 2022 | [Brains and algorithms partially converge in natural language processing](https://doi.org/10.1038/s42003-022-03036-1)  | fMRI | Communications Biology | — | — |
| 2021 | [The neural architecture of language: Integrative modeling converges on predictive processing](https://doi.org/10.1073/pnas.2105646118)  | fMRI | PNAS | — | — |
| 2017 | [Deep Learning Human Mind for Automated Visual Classification](https://doi.org/10.1109/cvpr.2017.479) `block-design` | EEG | CVPR 2017 | EEG-ImageNet | — |
| 2017 | [Generic decoding of seen and imagined objects using hierarchical visual features](https://doi.org/10.1038/ncomms15037)  | fMRI | Nat Commun | Generic Object Decoding | [code](https://github.com/KamitaniLab/GenericObjectDecoding) |
| 2016 | [Natural speech reveals the semantic maps that tile human cerebral cortex](https://doi.org/10.1038/nature17637)  | fMRI | Nature | — | — |

### Evaluation, replication and critique  <sub>(4)</sub>

| Year | Paper | Modality | Venue | Data | Code |
|---|---|---|---|---|---|
| 2026 | [Multigranular Evaluation for Brain Visual Decoding](https://doi.org/10.1609/aaai.v40i21.38845)  | fMRI | AAAI 2026 | Natural Scenes Dataset | [code](https://github.com/weihaox/BASIC) |
| 2024 | [Are EEG-to-Text Models Working?](https://doi.org/10.2139/ssrn.4882932)  | EEG | — | ZuCo 1.0 / 2.0 | — |
| 2024 | [Rethinking Cross-Subject Data Splitting for Brain-to-Text Decoding](https://doi.org/10.18653/v1/2025.emnlp-main.289)  | EEG | EMNLP 2024 | ZuCo 1.0 / 2.0 | — |
| 2021 | [The Perils and Pitfalls of Block Design for EEG Classification Experiments](https://doi.org/10.1109/tpami.2020.2973153)  | EEG | IEEE Transactions on Pattern An… | EEG-ImageNet | — |

### Surveys and taxonomies  <sub>(1)</sub>

| Year | Paper | Modality | Venue | Data | Code |
|---|---|---|---|---|---|
| 2025 | [Brain-Conditional Multimodal Synthesis: A Survey and Taxonomy](https://doi.org/10.1109/tai.2024.3516698)  | fMRI/EEG/MEG | IEEE Transactions on Artificial… | — | [code](https://github.com/MichaelMaiii/AIGC-Brain) |

---

## Legend

| Mark | Meaning |
|---|---|
| ⚠️ next to a title | link not yet resolved by `scripts/resolve.py` |
| `` `block-design` `` and similar | this paper's evaluation is subject to a documented pitfall — see [pitfalls.md](docs/pitfalls.md) |
| ⛔️ next to a dataset | known to be unsuitable for new work; kept for historical reference |
| ✅ / ⚠️ in Verified | whether a human has checked these numbers against the source |

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
