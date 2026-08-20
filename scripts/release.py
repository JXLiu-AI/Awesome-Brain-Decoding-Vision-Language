#!/usr/bin/env python3
"""Cut a release: roll the "what's new" window forward.

Everything with an `added:` date after the newest release is rendered as new in the
README. Cutting a release freezes that batch into CHANGELOG.md and starts an empty window.

  python scripts/release.py v0.2 --note "first bulk import"
"""
import argparse, datetime, sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CFG = ROOT / "data" / "config.yaml"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("version")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--note", default="")
    args = ap.parse_args()

    cfg = yaml.safe_load(CFG.read_text())
    releases = cfg.setdefault("releases", [])
    if any(r["version"] == args.version for r in releases):
        sys.exit(f"release {args.version} already exists")
    if releases and str(max(str(r["date"]) for r in releases)) >= args.date:
        sys.exit(f"date {args.date} is not after the newest release; pass --date explicitly")

    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text())
    last = max((str(r["date"]) for r in releases), default="0000-00-00")
    n = sum(1 for p in papers if isinstance(p, dict) and last < str(p.get("added", "")) <= args.date)

    releases.append({"version": args.version, "date": args.date, "note": args.note or f"{n} entries added"})
    CFG.write_text(yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False, width=110))
    print(f"cut {args.version} ({args.date}) covering {n} entries; run scripts/build.py")


if __name__ == "__main__":
    main()
