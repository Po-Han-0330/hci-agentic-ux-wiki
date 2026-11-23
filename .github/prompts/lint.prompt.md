---
description: Wiki 健檢
---
執行 `python scripts/lint_wiki.py`。
把每個錯誤分成「你可以直接修」和「需要我決定」兩類列出。
先修第一類，重跑腳本直到 PASS（最多 3 輪）；第二類列給我，不要自己決定。
在 wiki/log.md 記一筆 `## [日期] lint | 結果`。
