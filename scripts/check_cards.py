"""節點 2 關卡：python scripts/check_cards.py <slug>

每張證據卡：
- frontmatter 的 paper 要存在於 wiki/papers/
- 3–8 條主張，每條都有 [來源: papers/<同一篇> p.X 或 §X]
- 不能混入其他論文（一張卡只能有一篇）
- sources.md 列到的每篇論文都要有卡片
"""
from __future__ import annotations

import re
import sys

from common import LINK_RE, SOURCE_TAG_RE, Result, parse_frontmatter, read, topic_dir, wiki_page_exists


def main(slug: str) -> int:
    r = Result("check_cards（證據卡）")
    d = topic_dir(slug)
    cards_dir = d / "cards"
    cards = sorted(cards_dir.glob("*.md")) if cards_dir.is_dir() else []
    if not cards:
        r.err("cards/ 底下沒有卡片")
        return r.finish()

    have = set()
    for c in cards:
        meta, body = parse_frontmatter(read(c))
        paper = meta.get("paper", "")
        have.add(paper)
        name = c.name
        if paper != c.stem:
            r.err(f"{name}: frontmatter paper ({paper}) 跟檔名不一致")
        if not wiki_page_exists(f"papers/{paper}"):
            r.err(f"{name}: wiki/papers/{paper}.md 不存在")
        claims = [l for l in body.splitlines() if l.strip().startswith("- ")]
        if not 3 <= len(claims) <= 8:
            r.err(f"{name}: 主張有 {len(claims)} 條（要 3–8 條）")
        for i, line in enumerate(claims, 1):
            tags = SOURCE_TAG_RE.findall(line)
            if not tags:
                r.err(f"{name} 第 {i} 條：沒有 [來源: ...]")
                continue
            for src, loc in tags:
                if src != f"papers/{paper}":
                    r.err(f"{name} 第 {i} 條：引用了別篇 {src}（一張卡只能有一篇）")
                if not re.search(r"p\.\s*\d+|§\s*\d", loc):
                    r.err(f"{name} 第 {i} 條：來源沒有頁碼或章節")

    wanted = {l.strip().removeprefix("papers/") for l in LINK_RE.findall(read(d / "sources.md")) if l.startswith("papers/")}
    for p in sorted(wanted - have):
        r.err(f"sources.md 列了 {p}，但沒有對應卡片")
    print(f"卡片 {len(cards)} 張")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
