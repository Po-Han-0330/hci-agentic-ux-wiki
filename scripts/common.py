"""檢查腳本共用的小工具（只用標準函式庫）。"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
OUT = ROOT / "out"

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
SOURCE_TAG_RE = re.compile(r"\[來源:\s*([^\]\s]+)([^\]]*)\]")


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """解析 --- 包起來的簡單 key: value frontmatter。"""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("\n")
    meta: dict[str, str] = {}
    for i, line in enumerate(parts[1:], start=1):
        if line.strip() == "---":
            return meta, "\n".join(parts[i + 1 :])
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.split("#", 1)[0].strip() if k.strip() == "layout" else v.strip()
    return meta, text


def wiki_page_exists(link: str) -> bool:
    link = link.strip().removesuffix(".md")
    return (WIKI / f"{link}.md").is_file()


def visual_len(s: str) -> int:
    """估計顯示寬度：中日韓全形字算 2，其他算 1。"""
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)


def topic_dir(slug: str) -> Path:
    d = OUT / slug
    if not d.is_dir():
        raise SystemExit(f"找不到 {d}，請先建立 out/{slug}/")
    return d


class Result:
    """收集錯誤，最後印出並決定 exit code。"""

    def __init__(self, name: str):
        self.name = name
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def finish(self) -> int:
        status = "PASS" if not self.errors else "FAIL"
        print(f"[{status}] {self.name}")
        for e in self.errors:
            print(f"  ✗ {e}")
        for w in self.warnings:
            print(f"  ! {w}")
        return 0 if not self.errors else 1
