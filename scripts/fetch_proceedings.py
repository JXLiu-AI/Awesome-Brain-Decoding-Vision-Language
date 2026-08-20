#!/usr/bin/env python3
"""Sweep conference proceedings listings for candidates arXiv cannot see.

Measured 2026-08-20: of the 19 brain-decoding papers in CVPR 2026, only 5 appeared in a
658-paper arXiv sweep of the same period. The other 14 -- including a new large-scale
audiovisual brain dataset -- were invisible to arXiv-based automation entirely, because
plenty of accepted papers are never posted to arXiv, are posted after the proceedings, or
use titles that share no keywords with the query.

CVF (CVPR/ICCV/WACV) publishes a complete listing per year, which is what this reads.
DBLP covers the venues CVF does not; see --venue dblp:<stream>.

  python scripts/fetch_proceedings.py --venue CVPR2026 --out pending_cvpr.md
"""
import argparse, html, json, re, sys, urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CFG = yaml.safe_load((ROOT / "data" / "config.yaml").read_text())
CVF = "https://openaccess.thecvf.com/{venue}?day=all"
UA = {"User-Agent": "awesome-brain-decoding-vision-language/1.0"}

# Title-only matching, so it has to be tighter than the abstract-level filter used for
# arXiv. "neural network" and "neural rendering" are the obvious false friends.
KEY = r"\b(fMRI|EEG|MEG|brain|neuroimag|BOLD|cortical|neural decoding)\b"
ANTI = r"\b(neural network|neural radiance|neural field|neural render|brainstorm)\b"
TOPIC = r"(decod|reconstruct|retriev|caption|align|represent|understand|semant|visual|language|text|video|image)"


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def cvf_titles(venue):
    req = urllib.request.Request(CVF.format(venue=venue), headers=UA)
    with urllib.request.urlopen(req, timeout=180) as r:
        body = r.read().decode("utf-8", "ignore")
    titles = re.findall(r'class="ptitle"><br><a href="([^"]*)">(.*?)</a>', body, re.S)
    return [(html.unescape(t).strip(), "https://openaccess.thecvf.com" + href) for href, t in titles]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--venue", required=True, help="CVF venue slug, e.g. CVPR2026, ICCV2025, WACV2026")
    ap.add_argument("--out", default="pending_proceedings.md")
    args = ap.parse_args()

    known = {norm(p["title"]) for p in yaml.safe_load((ROOT / "data" / "papers.yaml").read_text())
             if isinstance(p, dict) and "title" in p}

    all_titles = cvf_titles(args.venue)
    cands = [(t, u) for t, u in all_titles
             if re.search(KEY, t, re.I) and not re.search(ANTI, t, re.I) and re.search(TOPIC, t, re.I)]
    fresh = [(t, u) for t, u in cands if norm(t) not in known]

    pretty = args.venue[:-4].rstrip() + " " + args.venue[-4:] if args.venue[-4:].isdigit() else args.venue
    lines = [f"`{args.venue}` listing: {len(all_titles)} papers, {len(cands)} match the topic filter, "
             f"{len(fresh)} not already in the list.", "",
             f"Venue is known exactly here, so set `venue_short: {pretty}` on every entry you accept "
             f"-- that is metadata an arXiv sweep can never supply.", ""]
    for t, u in sorted(fresh):
        lines += [f"- [ ] **{t}**", f"  {u}", ""]
    Path(args.out).write_text("\n".join(lines))
    print(f"{len(all_titles)} papers -> {len(cands)} topical -> {len(fresh)} new; wrote {args.out}")
    return 0 if fresh else 1


if __name__ == "__main__":
    sys.exit(main())
