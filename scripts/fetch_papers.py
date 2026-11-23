"""下載 raw/SOURCES.md 列出的論文 PDF 到 raw/。

用法：
    python scripts/fetch_papers.py            # 下載全部
    python scripts/fetch_papers.py amershi2019-guidelines feng2025-levels-of-autonomy

已經下載過的檔案會略過。只用 Python 標準函式庫。
"""
from __future__ import annotations

import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"

PAPERS: dict[str, list[str]] = {
    "horvitz1999-mixed-initiative": [
        "https://www.erichorvitz.com/chi99horvitz.pdf",
    ],
    "amershi2019-guidelines": [
        "https://research.microsoft.com/~horvitz/Guidelines_Human_AI_Interaction.pdf",
        "https://www.microsoft.com/en-us/research/uploads/prod/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf",
    ],
    "park2023-generative-agents": ["https://arxiv.org/pdf/2304.03442"],
    "subramonyam2024-gulf-of-envisioning": ["https://arxiv.org/pdf/2309.14459"],
    "tankelevitch2024-metacognitive-demands": ["https://arxiv.org/pdf/2312.10893"],
    "masson2024-directgpt": ["https://arxiv.org/pdf/2310.03691"],
    "bansal2024-human-agent-communication": ["https://arxiv.org/pdf/2412.10380"],
    "feng2025-levels-of-autonomy": ["https://arxiv.org/pdf/2506.12469"],
    "mozannar2025-magentic-ui": ["https://arxiv.org/pdf/2507.22358"],
    "leviathan2026-generative-ui": ["https://arxiv.org/pdf/2604.09577"],
}


def download(paper_id: str, urls: list[str]) -> bool:
    dest = RAW / f"{paper_id}.pdf"
    if dest.exists() and dest.stat().st_size > 10_000:
        print(f"[skip] {dest.name} 已存在")
        return True
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (LLM-Wiki homework)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            if not data.startswith(b"%PDF"):
                print(f"[warn] {url} 回傳的不是 PDF，換下一個網址")
                continue
            dest.write_bytes(data)
            print(f"[ok]   {dest.name}  ({len(data) // 1024} KB)")
            return True
        except Exception as e:  # noqa: BLE001
            print(f"[warn] {url} 失敗：{e}")
    print(f"[fail] {paper_id}：請手動下載，存成 raw/{paper_id}.pdf")
    return False


def main() -> int:
    RAW.mkdir(exist_ok=True)
    wanted = sys.argv[1:] or list(PAPERS)
    unknown = [w for w in wanted if w not in PAPERS]
    if unknown:
        print("不認得的 ID：", ", ".join(unknown))
        return 2
    ok = 0
    for pid in wanted:
        ok += download(pid, PAPERS[pid])
        time.sleep(1)  # 對 arXiv 客氣一點
    print(f"\n完成 {ok}/{len(wanted)} 篇")
    return 0 if ok == len(wanted) else 1


if __name__ == "__main__":
    sys.exit(main())
