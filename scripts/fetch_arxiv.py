#!/usr/bin/env python3
"""Sweep arXiv for new candidate papers and write a review queue.

Candidates are never appended to data/papers.yaml automatically. The daily workflow opens
one issue with everything new; a human decides what belongs. That is the whole point of a
curated list.
"""
import argparse, json, re, sys, time, urllib.parse, urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CFG = yaml.safe_load((ROOT / "data" / "config.yaml").read_text())
API = "http://export.arxiv.org/api/query?"


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def query(q, start, end, max_results=200):
    params = {
        "search_query": f"({q}) AND submittedDate:[{start} TO {end}]",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    for attempt in range(4):
        try:
            with urllib.request.urlopen(API + urllib.parse.urlencode(params), timeout=60) as r:
                body = r.read().decode()
            break
        except Exception:
            time.sleep(5 * (attempt + 1))
    else:
        return []
    out = []
    for e in re.findall(r"<entry>(.*?)</entry>", body, re.S):
        def grab(tag):
            m = re.search(rf"<{tag}>(.*?)</{tag}>", e, re.S)
            return " ".join(m.group(1).split()) if m else ""
        out.append({
            "title": grab("title"),
            "url": grab("id"),
            "published": grab("published")[:10],
            "summary": grab("summary")[:400],
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=2, help="lookback window")
    ap.add_argument("--out", default="pending.md")
    args = ap.parse_args()

    end = datetime.now(timezone.utc)
    start = end - timedelta(days=args.days)
    fmt = "%Y%m%d%H%M"

    known = {norm(p["title"]) for p in yaml.safe_load((ROOT / "data" / "papers.yaml").read_text())
             if isinstance(p, dict) and "title" in p}
    seen_path = ROOT / "data" / "seen_arxiv.json"
    seen = set(json.loads(seen_path.read_text())) if seen_path.exists() else set()

    found, hits = {}, 0
    for q in CFG["arxiv_queries"]:
        for e in query(q, start.strftime(fmt), end.strftime(fmt)):
            hits += 1
            if e["url"] in seen or norm(e["title"]) in known:
                continue
            blob = e["title"] + " " + e["summary"]
            # strong_signal states what the paper does; must_not_match is only a heuristic,
            # so an unambiguous task phrase overrides every exclusion rule.
            if not any(re.search(p, blob, re.I) for p in CFG.get("strong_signal", [])):
                if any(re.search(p, blob, re.I) for p in CFG.get("must_not_match", [])):
                    continue
                if not any(re.search(p, blob, re.I) for p in CFG["must_match"]):
                    continue
            found[e["url"]] = e
        time.sleep(3)

    lines = [f"Swept {hits} arXiv results over the last {args.days} day(s).",
             f"{len(found)} candidates not already in the list.", ""]
    for e in sorted(found.values(), key=lambda x: x["published"], reverse=True):
        lines += [f"- [ ] **{e['title']}** ({e['published']})", f"  {e['url']}", ""]
    Path(args.out).write_text("\n".join(lines))

    seen_path.write_text(json.dumps(sorted(seen | set(found)), indent=0))
    print(f"{len(found)} candidates -> {args.out}")
    # exit 1 when there is nothing to review, so the workflow can skip opening an issue
    return 0 if found else 1


if __name__ == "__main__":
    sys.exit(main())
