"""節點 1 關卡：python scripts/check_coverage.py <slug>

sources.md 至少要列 3 個存在的 wiki 頁面，其中至少 3 篇不同論文。
不通過 → 整個 graph 停下，不要硬做。
"""
from __future__ import annotations

import sys

from common import LINK_RE, Result, read, topic_dir, wiki_page_exists

MIN_PAGES = 3
MIN_PAPERS = 3


def main(slug: str) -> int:
    r = Result("check_coverage（覆蓋率關卡）")
    f = topic_dir(slug) / "sources.md"
    if not f.exists():
        r.err("沒有 sources.md")
        return r.finish()
    links = sorted({l.strip() for l in LINK_RE.findall(read(f))})
    missing = [l for l in links if not wiki_page_exists(l)]
    for l in missing:
        r.err(f"sources.md 引用不存在的頁面 [[{l}]]")
    ok = [l for l in links if l not in missing]
    papers = [l for l in ok if l.startswith("papers/")]
    if len(ok) < MIN_PAGES:
        r.err(f"相關頁面只有 {len(ok)} 個（至少 {MIN_PAGES}）→ 停下，先補 ingest")
    if len(papers) < MIN_PAPERS:
        r.err(f"相關論文只有 {len(papers)} 篇（至少 {MIN_PAPERS}）→ 停下，先補 ingest")
    if "## 子題" not in read(f):
        r.warn("sources.md 沒有列子題")
    print(f"相關頁面 {len(ok)}，論文 {len(papers)}")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
