"""節點 3 關卡：python scripts/check_outline.py <slug>

- 8–15 頁，編號連續
- 每頁（標題頁除外）都要對應到存在的卡片
- 每張卡片至少被用到一次（覆蓋率）
通過後還要「人工確認」才能往下走。
"""
from __future__ import annotations

import re
import sys

from common import Result, read, topic_dir

MIN_SLIDES, MAX_SLIDES = 8, 15


def main(slug: str) -> int:
    r = Result("check_outline（大綱）")
    d = topic_dir(slug)
    f = d / "outline.md"
    if not f.exists():
        r.err("沒有 outline.md")
        return r.finish()
    text = read(f)
    blocks = re.split(r"^## slide (\d+):", text, flags=re.M)[1:]
    slides = [(int(blocks[i]), blocks[i + 1]) for i in range(0, len(blocks), 2)]
    nums = [n for n, _ in slides]
    if not MIN_SLIDES <= len(slides) <= MAX_SLIDES:
        r.err(f"共 {len(slides)} 頁（要 {MIN_SLIDES}–{MAX_SLIDES} 頁）")
    if nums != list(range(1, len(nums) + 1)):
        r.err(f"頁碼不連續：{nums}")

    cards = {c.stem for c in (d / "cards").glob("*.md")}
    used: set[str] = set()
    for n, body in slides:
        m = re.search(r"^cards:\s*(.*)$", body, re.M)
        ids = [x.strip() for x in m.group(1).split(",") if x.strip()] if m else []
        if n != 1 and not ids:
            r.err(f"slide {n}: 沒有對應卡片（cards: 那行）")
        for i in ids:
            if i not in cards:
                r.err(f"slide {n}: 卡片 {i} 不存在")
            used.add(i)
        if "重點:" not in body:
            r.warn(f"slide {n}: 沒寫「重點:」")
    for c in sorted(cards - used):
        r.err(f"卡片 {c} 沒有被任何一頁用到（覆蓋率不足）")
    print(f"大綱 {len(slides)} 頁，用到卡片 {len(used & cards)}/{len(cards)}")
    rc = r.finish()
    if rc == 0:
        print("  → 腳本通過。請人工看過 outline.md，回覆「確認」或指出要退回哪裡。")
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
