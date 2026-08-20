#!/usr/bin/env python3
"""Fill in paper links, venues and citation counts from public APIs.

No URL in this repository is typed from memory. Titles are hand-written; this script
resolves them against arXiv and Crossref (neither needs an API key) and optionally
Semantic Scholar for citation counts, requiring a high title-similarity match before it
accepts anything. Entries it cannot resolve keep `resolved: false` so the build flags them
with a visible warning rather than shipping a plausible-looking wrong link.

Usage:
  python scripts/resolve.py            # resolve entries that are not yet resolved
  python scripts/resolve.py --force    # re-resolve everything
  python scripts/resolve.py --cite     # also try Semantic Scholar for citation counts
"""
import argparse, difflib, html, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "data" / "papers.yaml"
UA = {"User-Agent": "awesome-brain-decoding-vision-language/1.0 (github list builder)"}
THRESHOLD = 0.90


def norm(s):
    return re.sub(r"[^a-z0-9 ]+", " ", html.unescape(s).lower()).split()


def similar(a, b):
    return difflib.SequenceMatcher(None, " ".join(norm(a)), " ".join(norm(b))).ratio()


def get(url, timeout=45):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read().decode()


def from_arxiv(title):
    """arXiv title search. Returns (score, dict) or (0, None)."""
    q = urllib.parse.urlencode({"search_query": f'ti:"{title}"', "max_results": 5})
    try:
        body = get(f"http://export.arxiv.org/api/query?{q}")
    except Exception:
        return 0.0, None
    best, score = None, 0.0
    for e in re.findall(r"<entry>(.*?)</entry>", body, re.S):
        t = re.search(r"<title>(.*?)</title>", e, re.S)
        i = re.search(r"<id>(.*?)</id>", e)
        if not (t and i):
            continue
        cand = " ".join(t.group(1).split())
        s = similar(title, cand)
        if s > score:
            aid = i.group(1).rsplit("/", 1)[-1]
            score, best = s, {"arxiv": f"https://arxiv.org/abs/{aid}"}
    return score, best


# A preprint DOI is a worse citation than the version of record, so peer-reviewed
# record types win ties even when the preprint scores marginally higher on title match.
PREFERRED_TYPES = ("proceedings-article", "journal-article", "book-chapter")


def from_crossref(title):
    """Crossref title search -> DOI + published venue, preferring the version of record."""
    q = urllib.parse.urlencode({"query.bibliographic": title, "rows": 8,
                                "select": "title,DOI,container-title,issued,type"})
    try:
        items = json.loads(get(f"https://api.crossref.org/works?{q}"))["message"]["items"]
    except Exception:
        return 0.0, None
    cands = []
    for it in items:
        s = similar(title, (it.get("title") or [""])[0])
        if s < THRESHOLD:
            continue
        cands.append((0 if it.get("type") in PREFERRED_TYPES else 1, -s, {
            "doi": it["DOI"], "paper": f"https://doi.org/{it['DOI']}",
            "venue": (it.get("container-title") or [None])[0], "type": it.get("type")}))
    if not cands:
        return 0.0, None
    cands.sort(key=lambda c: (c[0], c[1]))
    rank, negs, best = cands[0]
    return -negs, best


def from_s2(title):
    q = urllib.parse.urlencode({"query": title, "limit": 3,
                                "fields": "title,venue,citationCount,externalIds"})
    try:
        data = json.loads(get(f"https://api.semanticscholar.org/graph/v1/paper/search?{q}")).get("data", [])
    except Exception:
        return 0.0, None
    best, score = None, 0.0
    for it in data:
        s = similar(title, it.get("title", ""))
        if s > score:
            score, best = s, {"citations": it.get("citationCount"), "venue": it.get("venue") or None}
    return score, best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--cite", action="store_true", help="also query Semantic Scholar for citation counts")
    args = ap.parse_args()

    papers = yaml.safe_load(PAPERS.read_text())
    todo = [p for p in papers if isinstance(p, dict) and "title" in p and (args.force or not p.get("resolved"))]
    print(f"resolving {len(todo)} of {len(papers)} entries\n")

    ok = 0
    for p in todo:
        title = p["title"]
        found = {}
        sa, a = from_arxiv(title)
        if sa >= THRESHOLD and a:
            found.update(a)
        time.sleep(1.0)
        sc, c = from_crossref(title)
        if sc >= THRESHOLD and c:
            # keep the arXiv link too, but a version-of-record DOI becomes the primary link
            if c.get("type") in PREFERRED_TYPES or "paper" not in found:
                found.update({k: v for k, v in c.items() if v and k != "type"})
        time.sleep(0.6)
        if args.cite:
            ss, s = from_s2(title)
            if ss >= THRESHOLD and s:
                found["citations"] = s.get("citations")
                found.setdefault("venue", s.get("venue"))
            time.sleep(1.5)

        if found.get("arxiv") and not found.get("paper"):
            found["paper"] = found["arxiv"]
        if found.get("paper"):
            p.update({k: v for k, v in found.items() if v is not None})
            p["resolved"] = True
            p["match_score"] = round(max(sa, sc), 3)
            ok += 1
            src = "arxiv+doi" if (found.get("arxiv") and found.get("doi")) else ("doi" if found.get("doi") else "arxiv")
            print(f"  ok   {max(sa, sc):.2f}  [{src:9s}] {title[:64]}")
        else:
            p["resolved"] = False
            print(f"  MISS       [{'':9s}] {title[:64]}")

    PAPERS.write_text(yaml.safe_dump(papers, allow_unicode=True, sort_keys=False, width=110))
    print(f"\nresolved {ok}/{len(todo)}; {sum(1 for p in papers if not p.get('paper'))} entries still unlinked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
