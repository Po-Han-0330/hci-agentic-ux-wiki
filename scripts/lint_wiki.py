"""Wiki 健檢：python scripts/lint_wiki.py

檢查：
1. [[連結]] 指到的頁面存在
2. papers/ 頁面有必填欄位、必要段落，且 id 與檔名一致、對得上 raw/SOURCES.md
3. concepts/ 和 debates/ 頁面至少引用一篇論文
4. 每個頁面都列在 index.md
5. 孤兒頁（沒有任何頁面連到它）→ 警告
7.（2026-11-23 新增，把人工檢查前移）trends/ 段落沒出處、concept 缺新手定義、百分比沒附頁碼 → 警告
6. log.md 每篇已 ingest 的論文都有紀錄
"""
from __future__ import annotations

import re
import sys

from common import LINK_RE, ROOT, WIKI, Result, parse_frontmatter, read

PAPER_FIELDS = ["id", "title", "authors", "venue", "year", "type"]
PAPER_SECTIONS = ["## 一句話", "## 主要發現", "## 設計啟示", "## 相關概念"]


def main() -> int:
    r = Result("lint_wiki")
    index_text = read(WIKI / "index.md")
    log_text = read(WIKI / "log.md")
    sources_text = read(ROOT / "raw" / "SOURCES.md")
    known_ids = set(re.findall(r"^\|\s*([a-z0-9]+[a-z0-9-]*)\s*\|", sources_text, re.M)) - {"id"}

    pages = sorted(p for p in WIKI.rglob("*.md") if p.name not in {"index.md", "log.md"})
    inbound: dict[str, int] = {p.relative_to(WIKI).with_suffix("").as_posix(): 0 for p in pages}

    for p in [WIKI / "index.md", *pages]:
        rel = p.relative_to(WIKI).with_suffix("").as_posix()
        text = read(p)
        for link in LINK_RE.findall(text):
            link = link.strip().removesuffix(".md")
            if link not in inbound:
                r.err(f"{rel}: 斷掉的連結 [[{link}]]")
            elif link != rel and p.name != "index.md":
                inbound[link] += 1

    for p in pages:
        rel = p.relative_to(WIKI).with_suffix("").as_posix()
        meta, body = parse_frontmatter(read(p))
        if f"[[{rel}]]" not in index_text:
            r.err(f"{rel}: 沒有列在 index.md")

        if rel.startswith("papers/"):
            for f in PAPER_FIELDS:
                if not meta.get(f):
                    r.err(f"{rel}: frontmatter 缺 {f}")
            if meta.get("id") and meta["id"] != p.stem:
                r.err(f"{rel}: id ({meta['id']}) 跟檔名不一致")
            if known_ids and p.stem not in known_ids:
                r.err(f"{rel}: 不在 raw/SOURCES.md 的論文清單裡")
            for s in PAPER_SECTIONS:
                if s not in body:
                    r.err(f"{rel}: 缺少段落「{s}」")
            if len(re.findall(r"\[\[concepts/", body)) < 2:
                r.warn(f"{rel}: 相關概念少於 2 個")
            if not re.search(r"\(p\.\s*\d+|§\s*\d", body):
                r.err(f"{rel}: 主要發現沒有任何頁碼或章節標記")
            if f"| {p.stem}" not in log_text and f"|{p.stem}" not in log_text:
                r.err(f"{rel}: log.md 沒有這篇的 ingest 紀錄")
        if rel.startswith("concepts/") and "**一句話定義（給新手）**" not in body:
            r.warn(f"{rel}: 缺少給新手的「一句話定義」")
        for line in body.splitlines():
            if re.search(r"\d+(?:\.\d+)?\s*%", line) and not re.search(r"p\.\s*\d|§\s*\d", line):
                r.warn(f"{rel}: 百分比沒有附頁碼 → {line.strip()[:30]}…")
        if rel.startswith(("concepts/", "debates/", "trends/")):
            if not re.search(r"\[\[papers/", body):
                r.err(f"{rel}: 沒有引用任何論文")
            # 有內容但沒出處的段落
            for para in re.split(r"\n\s*\n", body):
                line = para.strip()
                if (
                    line
                    and not line.startswith("#")
                    and len(line) > 40
                    and "[[papers/" not in line
                    and "待查" not in line
                    and "[[concepts/" not in line
                    and "[[debates/" not in line
                ):
                    r.warn(f"{rel}: 這段沒有出處 → {line[:30]}…")

    for rel, n in inbound.items():
        if n == 0:
            r.warn(f"{rel}: 孤兒頁（沒有其他頁面連到它）")

    n_papers = sum(1 for p in pages if p.parent.name == "papers")
    print(f"共 {len(pages)} 頁（論文 {n_papers} 篇）")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main())
