"""節點 4 關卡：python scripts/check_drafts.py <slug>

每頁 drafts/slide-XX.md：
- frontmatter 有 slide、title、layout、sources；slide 編號和檔名一致
- sources 裡每個頁面都存在於 wiki（標題頁可以沒有）
- 內文的數字（含 %）要能在引用的 wiki 頁面裡找到 → 防止 AI 亂編數字
- 字數限制：每點 ≤ 70 寬度單位（中文字算 2），最多 6 點，整頁 ≤ 360
- 頁數 8–15，且跟 outline.md 一致
"""
from __future__ import annotations

import re
import sys

from common import WIKI, Result, parse_frontmatter, read, topic_dir, visual_len, wiki_page_exists

LAYOUTS = {"title", "bullets", "compare", "quote"}
MAX_BULLET = 70
MAX_BULLETS = 6
MAX_TOTAL = 360
NUM_RE = re.compile(r"\d+(?:\.\d+)?\s*%|\b\d{2,}(?:\.\d+)?\b")


def visible_lines(body: str) -> list[str]:
    return [l for l in body.splitlines() if l.strip() and not l.strip().startswith("> notes:")]


def main(slug: str) -> int:
    r = Result("check_drafts（逐頁稿）")
    d = topic_dir(slug)
    files = sorted((d / "drafts").glob("slide-*.md")) if (d / "drafts").is_dir() else []
    if not files:
        r.err("drafts/ 底下沒有 slide-XX.md")
        return r.finish()

    outline = read(d / "outline.md") if (d / "outline.md").exists() else ""
    n_outline = len(re.findall(r"^## slide \d+:", outline, re.M))
    if n_outline and n_outline != len(files):
        r.err(f"逐頁稿有 {len(files)} 頁，大綱有 {n_outline} 頁")

    for i, f in enumerate(files, 1):
        meta, body = parse_frontmatter(read(f))
        tag = f.stem
        if f.stem != f"slide-{i:02d}":
            r.err(f"{f.name}: 檔名應為 slide-{i:02d}.md")
        for k in ("slide", "title", "layout"):
            if not meta.get(k):
                r.err(f"{tag}: frontmatter 缺 {k}")
        if meta.get("slide") and meta["slide"] != str(i):
            r.err(f"{tag}: slide 欄位是 {meta['slide']}，應為 {i}")
        layout = meta.get("layout", "")
        if layout and layout not in LAYOUTS:
            r.err(f"{tag}: layout「{layout}」不認得（可用 {', '.join(sorted(LAYOUTS))}）")

        sources = [s.strip() for s in meta.get("sources", "").split(",") if s.strip()]
        if layout != "title" and not sources:
            r.err(f"{tag}: 沒有出處（sources）")
        for s in sources:
            if not wiki_page_exists(s):
                r.err(f"{tag}: 出處 {s} 不存在於 wiki")

        lines = visible_lines(body)
        bullets = [l for l in lines if l.lstrip().startswith(("- ", "* "))]
        if len(bullets) > MAX_BULLETS:
            r.err(f"{tag}: {len(bullets)} 個重點（最多 {MAX_BULLETS}）→ 字太多，請縮短或拆頁")
        for b in bullets:
            if visual_len(b.strip()[2:]) > MAX_BULLET:
                r.err(f"{tag}: 這點太長 → {b.strip()[2:22]}…")
        total = sum(visual_len(l) for l in lines)
        if total > MAX_TOTAL:
            r.err(f"{tag}: 整頁太長（{total} > {MAX_TOTAL}）")

        # 數字要能在引用頁面找到
        src_text = "".join(read(WIKI / f"{s}.md") for s in sources if wiki_page_exists(s))
        src_norm = src_text.replace(" ", "")
        for num in set(NUM_RE.findall("\n".join(lines))):
            if num.replace(" ", "") not in src_norm:
                r.err(f"{tag}: 數字「{num}」在引用的 wiki 頁面裡找不到")

    if not 8 <= len(files) <= 15:
        r.err(f"共 {len(files)} 頁（要 8–15 頁）")
    print(f"逐頁稿 {len(files)} 頁")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
