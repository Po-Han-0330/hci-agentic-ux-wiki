---
description: 把 raw/ 的一篇論文編進 wiki
---
Ingest 這篇論文：$ARGUMENTS
（如果沒給 ID，先列出 raw/ 裡還沒 ingest 的 PDF 讓我選，一次只做一篇。）

嚴格照 AGENTS.md 的「Ingest 流程」七個步驟做。
完成的定義：`python scripts/lint_wiki.py` 顯示 PASS。沒過就修，最多 3 輪；
第 3 輪還沒過，把剩下的問題列出來後停下。
最後告訴我新增和修改了哪些頁面，並提醒我 commit。
