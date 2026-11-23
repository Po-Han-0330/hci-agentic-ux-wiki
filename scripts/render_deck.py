"""節點 5：把通過檢查的逐頁稿「原封不動」渲染成 HTML 簡報。

    python scripts/render_deck.py <slug>             # 產生 out/<slug>/deck.html
    python scripts/render_deck.py <slug> --publish   # 另外複製到 docs/<slug>.html 並更新 docs/index.html

渲染由腳本做、不經過 AI，所以不可能「排版時順手改句子」。
操作：← → 或空白鍵換頁，N 顯示講者備註，F 全螢幕。
"""
from __future__ import annotations

import html
import re
import shutil
import sys
from pathlib import Path

from common import ROOT, parse_frontmatter, read, topic_dir

LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def inline(s: str) -> str:
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    s = LINK_RE.sub(lambda m: f'<span class="ref">{html.escape(m.group(2) or m.group(1).split("/")[-1])}</span>', s)
    return s


def render_list(lines: list[str]) -> str:
    out, in_ul = [], False
    for l in lines:
        t = l.strip()
        if t.startswith(("- ", "* ")):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline(t[2:])}</li>")
        else:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if t.startswith("> "):
                out.append(f"<blockquote>{inline(t[2:])}</blockquote>")
            elif t.startswith("#"):
                out.append(f"<h3>{inline(t.lstrip('#').strip())}</h3>")
            elif t:
                out.append(f"<p>{inline(t)}</p>")
    if in_ul:
        out.append("</ul>")
    return "\n".join(out)


def short_source(s: str) -> str:
    kind, _, name = s.partition("/")
    return name if kind == "papers" else f"{kind[:-1]}: {name}"


def render_slide(meta: dict[str, str], body: str, idx: int, total: int) -> str:
    notes = [l.strip()[len("> notes:"):].strip() for l in body.splitlines() if l.strip().startswith("> notes:")]
    lines = [l for l in body.splitlines() if not l.strip().startswith("> notes:")]
    layout = meta.get("layout", "bullets")
    title = inline(meta.get("title", ""))
    sources = [s.strip() for s in meta.get("sources", "").split(",") if s.strip()]

    if layout == "title":
        inner = f'<div class="title-wrap"><p class="kicker">HCI · AI-Native 介面與 Agentic UX</p><h1>{title}</h1>{render_list(lines)}</div>'
    elif layout == "compare":
        cols, cur = [], None
        for l in lines:
            if l.strip().startswith("### "):
                cur = [l.strip()[4:], []]
                cols.append(cur)
            elif cur is not None:
                cur[1].append(l)
        col_html = "".join(f'<div class="col"><h3>{inline(h)}</h3>{render_list(b)}</div>' for h, b in cols)
        inner = f'<h2>{title}</h2><div class="compare">{col_html}</div>'
    elif layout == "quote":
        inner = f'<h2>{title}</h2><div class="quote">{render_list(lines)}</div>'
    else:
        inner = f"<h2>{title}</h2><div class=\"body\">{render_list(lines)}</div>"

    cite = ""
    if sources:
        cite = '<footer class="cite">出處：' + "、".join(html.escape(short_source(s)) for s in sources) + "</footer>"
    note_html = f'<aside class="notes">{"<br>".join(html.escape(n) for n in notes)}</aside>' if notes else ""
    return (
        f'<section class="slide layout-{layout}" data-slide="{idx}">'
        f'<div class="inner">{inner}</div>{cite}'
        f'<div class="pageno">{idx} / {total}</div>{note_html}</section>'
    )


CSS = """
:root{--bg:#f6f3ee;--ink:#1d1d1f;--muted:#6b6660;--accent:#c2410c;--accent2:#0f766e;--card:#fffdf9;--line:#e4ddd3}
*{box-sizing:border-box}html,body{margin:0;height:100%;background:#2a2723;font-family:"Noto Sans TC","PingFang TC","Microsoft JhengHei",system-ui,sans-serif;color:var(--ink)}
.stage{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}
.slide{position:absolute;width:1280px;height:720px;background:var(--bg);padding:64px 80px 72px;display:none;overflow:hidden;transform-origin:center}
.slide.active{display:block}
.slide h1{font-size:56px;line-height:1.25;margin:0 0 24px;letter-spacing:.01em}
.slide h2{font-size:40px;margin:0 0 32px;padding-bottom:16px;border-bottom:3px solid var(--accent);display:inline-block}
.slide h3{font-size:26px;color:var(--accent2);margin:0 0 12px}
.slide ul{margin:0;padding-left:1.1em}.slide li{font-size:28px;line-height:1.55;margin:0 0 14px}
.slide li::marker{color:var(--accent)}
.slide p{font-size:26px;line-height:1.6;margin:0 0 12px;color:var(--muted)}
.slide strong{color:var(--accent)}.slide code{font-size:.85em;background:#ece6dc;padding:2px 6px;border-radius:4px}
.ref{color:var(--accent2);font-weight:600}
.title-wrap{height:100%;display:flex;flex-direction:column;justify-content:center}
.kicker{font-size:22px!important;letter-spacing:.12em;color:var(--accent)!important;text-transform:uppercase;font-weight:700}
.compare{display:grid;grid-template-columns:1fr 1fr;gap:32px}
.col{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:24px 28px}
.col li{font-size:24px}
.quote blockquote{font-size:34px;line-height:1.5;border-left:6px solid var(--accent);margin:0 0 20px;padding:8px 0 8px 28px}
blockquote{font-size:26px;border-left:4px solid var(--accent2);margin:12px 0;padding-left:20px;color:var(--muted)}
.cite{position:absolute;left:80px;right:180px;bottom:28px;font-size:16px;color:var(--muted);border-top:1px solid var(--line);padding-top:10px}
.pageno{position:absolute;right:40px;bottom:28px;font-size:16px;color:var(--muted)}
.notes{display:none;position:absolute;left:0;right:0;bottom:0;background:#1d1d1fee;color:#f6f3ee;font-size:18px;line-height:1.6;padding:18px 80px}
body.show-notes .notes{display:block}
.progress{position:fixed;left:0;bottom:0;height:4px;background:var(--accent);transition:width .2s}
@media print{body{background:none}.stage{position:static;display:block}.slide{position:relative;display:block!important;transform:none!important;page-break-after:always}.progress{display:none}}
"""

JS = """
const slides=[...document.querySelectorAll('.slide')];let i=0;
function fit(){const s=Math.min(innerWidth/1280,innerHeight/720)*0.96;slides.forEach(el=>el.style.transform=`scale(${s})`)}
function show(n){i=Math.max(0,Math.min(slides.length-1,n));slides.forEach((s,k)=>s.classList.toggle('active',k===i));
document.querySelector('.progress').style.width=((i+1)/slides.length*100)+'%';history.replaceState(null,'','#'+(i+1))}
addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' '].includes(e.key))show(i+1);else if(['ArrowLeft','PageUp'].includes(e.key))show(i-1);
else if(e.key==='n'||e.key==='N')document.body.classList.toggle('show-notes');else if(e.key==='f'||e.key==='F')document.documentElement.requestFullscreen?.()});
addEventListener('click',e=>{if(e.clientX>innerWidth/2)show(i+1);else show(i-1)});
addEventListener('resize',fit);fit();show((parseInt(location.hash.slice(1))||1)-1);
"""


def build(slug: str) -> Path:
    d = topic_dir(slug)
    files = sorted((d / "drafts").glob("slide-*.md"))
    if not files:
        raise SystemExit("drafts/ 底下沒有逐頁稿")
    parsed = [parse_frontmatter(read(f)) for f in files]
    deck_title = parsed[0][0].get("title", slug)
    sections = "\n".join(render_slide(m, b, k, len(parsed)) for k, (m, b) in enumerate(parsed, 1))
    page = (
        "<!DOCTYPE html>\n<html lang=\"zh-Hant\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        f"<title>{html.escape(deck_title)}</title><style>{CSS}</style></head>"
        f"<body><div class=\"stage\">{sections}</div><div class=\"progress\"></div>"
        f"<script>{JS}</script></body></html>\n"
    )
    out = d / "deck.html"
    out.write_text(page, encoding="utf-8")
    print(f"[ok] {out.relative_to(ROOT)}（{len(parsed)} 頁）")
    return out


def publish(slug: str, deck: Path) -> None:
    site = ROOT / "docs"
    site.mkdir(exist_ok=True)
    shutil.copy(deck, site / f"{slug}.html")
    items = []
    for p in sorted(site.glob("*.html")):
        if p.name == "index.html":
            continue
        t = re.search(r"<title>(.*?)</title>", p.read_text(encoding="utf-8"))
        items.append(f'<li><a href="{p.name}">{t.group(1) if t else p.stem}</a></li>')
    (site / "index.html").write_text(
        "<!DOCTYPE html><html lang=\"zh-Hant\"><head><meta charset=\"utf-8\"><title>HCI LLM Wiki 簡報</title>"
        "<style>body{font-family:system-ui,'Noto Sans TC',sans-serif;max-width:720px;margin:64px auto;padding:0 24px;line-height:1.7}"
        "a{color:#c2410c}</style></head><body><h1>AI-Native 介面與 Agentic UX：主題簡報</h1>"
        f"<p>由 LLM Wiki 自動產生，每頁都附出處。</p><ul>{''.join(items)}</ul></body></html>\n",
        encoding="utf-8",
    )
    print(f"[ok] 已發布到 docs/{slug}.html，並更新 docs/index.html")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    deck = build(sys.argv[1])
    if "--publish" in sys.argv:
        publish(sys.argv[1], deck)
