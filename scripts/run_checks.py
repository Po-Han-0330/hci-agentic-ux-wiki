"""一鍵跑所有關卡並寫出 report.md：python scripts/run_checks.py <slug>

依 graph 順序跑；前一關沒過，後面的關卡不跑（錯在哪關就回哪關）。
"""
from __future__ import annotations

import contextlib
import datetime as dt
import io
import sys

import check_cards
import check_coverage
import check_deck
import check_drafts
import check_outline
from common import ROOT, topic_dir

STAGES = [
    ("1 檢索 → 覆蓋率關卡", check_coverage.main, "停下，先 ingest 更多論文"),
    ("2 證據卡", check_cards.main, "退回節點 2，只重做有問題的卡片"),
    ("3 大綱", check_outline.main, "退回節點 3（缺子題就回節點 1）"),
    ("4 逐頁稿", check_drafts.main, "退回節點 4，只修有問題的那幾頁"),
    ("5 渲染", check_deck.main, "字太多／溢出 → 退回節點 4；稿比較新 → 重跑 render_deck.py"),
]


def main(slug: str) -> int:
    d = topic_dir(slug)
    lines = [f"# 檢查報告：{slug}", "", f"時間：{dt.datetime.now():%Y-%m-%d %H:%M}", ""]
    failed = None
    for name, fn, fix in STAGES:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = fn(slug)
        out = buf.getvalue().strip()
        print(out)
        lines += [f"## {name}：{'✅ 通過' if rc == 0 else '❌ 未通過'}", "", "```", out, "```", ""]
        if rc != 0:
            lines += [f"**下一步**：{fix}", ""]
            failed = name
            break
    review = d / "review.md"
    if review.exists():
        lines += ["## AI 審查（review.md）", "", review.read_text(encoding="utf-8").strip(), ""]
    else:
        lines += ["## AI 審查", "", "尚未執行：請開新對話跑 workflows/topic-slides.md 裡的審查 prompt。", ""]
    lines.append("## 結論：" + ("全部關卡通過，可以交件 🎉" if failed is None else f"卡在「{failed}」"))
    (d / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n報告已寫入 {(d / 'report.md').relative_to(ROOT)}")
    return 0 if failed is None else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
