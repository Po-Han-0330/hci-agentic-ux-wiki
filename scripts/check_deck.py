"""節點 5 關卡：python scripts/check_deck.py <slug>

- deck.html 的頁數 = 逐頁稿頁數
- 每一頁（標題頁除外）都有出處列
- deck.html 比逐頁稿還新（改了稿就要重新渲染）
- 有安裝 Playwright 的話，會真的開瀏覽器檢查每頁有沒有溢出：
      pip install playwright && playwright install chromium
"""
from __future__ import annotations

import re
import sys

from common import Result, parse_frontmatter, read, topic_dir


def overflow_check(deck_path, r: Result) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        r.warn("沒有安裝 Playwright，略過真實溢出檢查（只靠 check_drafts 的字數限制）")
        return
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page(viewport={"width": 1280, "height": 720})
        page.goto(deck_path.resolve().as_uri())
        bad = page.evaluate(
            """() => [...document.querySelectorAll('.slide')].map((s, k) => {
                 s.classList.add('active');
                 const inner = s.querySelector('.inner');
                 const cite = s.querySelector('.cite');
                 const limit = cite ? cite.getBoundingClientRect().top : s.getBoundingClientRect().bottom - 60;
                 const over = inner.scrollHeight > inner.clientHeight + 2 || inner.getBoundingClientRect().bottom > limit + 2
                   || [...inner.querySelectorAll('*')].some(el => el.getBoundingClientRect().bottom > limit + 2);
                 s.classList.remove('active');
                 return over ? k + 1 : null;
               }).filter(x => x)"""
        )
        b.close()
    for n in bad:
        r.err(f"slide-{n:02d}: 渲染後內容溢出或壓到出處列 → 退回逐頁稿縮短")


def main(slug: str) -> int:
    r = Result("check_deck（渲染後簡報）")
    d = topic_dir(slug)
    deck = d / "deck.html"
    drafts = sorted((d / "drafts").glob("slide-*.md"))
    if not deck.exists():
        r.err("沒有 deck.html，請先跑 render_deck.py")
        return r.finish()
    html = read(deck)
    sections = re.findall(r'<section class="slide layout-(\w+)".*?</section>', html, re.S)
    blocks = re.findall(r'(<section class="slide.*?</section>)', html, re.S)
    if len(blocks) != len(drafts):
        r.err(f"deck.html 有 {len(blocks)} 頁，逐頁稿有 {len(drafts)} 頁 → 重新渲染")
    for k, (layout, block) in enumerate(zip(sections, blocks), 1):
        if layout != "title" and 'class="cite"' not in block:
            r.err(f"slide-{k:02d}: 沒有出處列")
    newest = max((f.stat().st_mtime for f in drafts), default=0)
    if deck.stat().st_mtime < newest:
        r.err("逐頁稿比 deck.html 新 → 重新跑 render_deck.py")
    for f in drafts:
        meta, _ = parse_frontmatter(read(f))
        if meta.get("title") and meta["title"].replace("**", "") not in re.sub(r"<[^>]+>", "", html):
            r.err(f"{f.stem}: 標題沒有出現在 deck.html（渲染時被改動？）")
    overflow_check(deck, r)
    print(f"deck.html {len(blocks)} 頁")
    return r.finish()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
