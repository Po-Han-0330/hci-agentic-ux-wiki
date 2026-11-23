# HCI LLM Wiki：AI-Native 介面與 Agentic UX

TAICA《生成式 AI》第 10 週作業：用「先討論、後生成」建立 LLM Wiki（至少 ingest 5 篇），再用 Graph workflow 從 wiki 產生 HTML 簡報。

```
├── AGENTS.md               給 AI 的員工手冊（Copilot、Codex、Antigravity 都會讀）
├── CLAUDE.md               只有一行 @AGENTS.md（給 Claude Code 用）
├── raw/                    原始論文 PDF + SOURCES.md（10 篇 HCI 文獻）
├── wiki/                   AI 維護的知識庫：index、log、papers、concepts、debates
├── workflows/topic-slides.md   簡報 Graph：節點、關卡、退回路線
├── scripts/                可以執行的檢查（「做完了」是腳本說了算）
├── out/<slug>/             每個簡報主題的中間產物與成品
├── docs/                   GitHub Pages 發布用（render_deck.py --publish 會放進來）
├── guide/                  訪談 prompt、反思模板
├── .github/prompts/        VS Code Copilot 的 /ingest /lint /topic-slides
└── .claude/commands/       Claude Code 的同一組指令
```

---

## 0. 準備（約 5 分鐘）

需要：VS Code、Python 3.10 以上、git，加上一個 coding agent，下面兩種都可以：
- **GitHub Copilot**（VS Code 內建 Chat，切到 **Agent** 模式）：會自動讀 `AGENTS.md`，指令打 `/ingest`
- **Claude Code**（VS Code 擴充套件，或在終端機打 `claude`）：會讀 `CLAUDE.md`，指令打 `/ingest`

在 VS Code 打開這個資料夾，開終端機（`` Ctrl+` ``）：

```bash
git init
git add -A && git commit -m "project skeleton"
python scripts/fetch_papers.py        # 下載 10 篇論文到 raw/
```

下載失敗的論文，腳本會告訴你網址，手動下載後存成 `raw/<id>.pdf` 就好。

## 1. 先討論，再生成 AGENTS.md（作業重點）

照 `guide/01-interview-prompt.md` 做：先把 `AGENTS.md` 改名成 `AGENTS.reference.md`，再把開場 prompt 貼給 agent，讓它一題一題訪談你。那份文件也附了參考答案。

訪談完記得：
- 把對話存成 `guide/interview-log.md`
- 比較 AI 生成的 `AGENTS.md` 和 `AGENTS.reference.md`
- `git commit -m "AGENTS.md from interview"`

## 2. Ingest 至少 5 篇（一次一篇）

在 agent 對話框輸入：

```
/ingest amershi2019-guidelines
```

每篇做完：
```bash
python scripts/lint_wiki.py           # 要看到 [PASS]
git add -A && git commit -m "ingest amershi2019-guidelines"
```

建議順序：`amershi2019-guidelines` → `subramonyam2024-gulf-of-envisioning` → `bansal2024-human-agent-communication` → `feng2025-levels-of-autonomy` → `mozannar2025-magentic-ui`

想看圖譜的話，可以用 Obsidian 打開 `wiki/` 資料夾。

## 3. 用 Graph 產生 HTML 簡報

```
/topic-slides 主題：Agent 介面的自主性該怎麼設計，slug：agent-autonomy
```

Agent 會走 6 個節點（流程圖見 `workflows/topic-slides.md`）：
檢索 → 覆蓋率關卡 → 證據卡 → 大綱（**停下等你確認**）→ 逐頁稿 → 腳本渲染 → 交件

**AI 審查**：逐頁稿完成後，開一個**新的**對話，貼上 `workflows/topic-slides.md` 裡的審查 prompt。審查者不能審自己的作品。

隨時可以自己跑檢查：
```bash
python scripts/run_checks.py agent-autonomy     # 依序跑全部關卡，寫出 out/agent-autonomy/report.md
python scripts/render_deck.py agent-autonomy    # 重新渲染
```

想要真的開瀏覽器檢查文字有沒有溢出（選用）：
```bash
pip install playwright && playwright install chromium
```

其他主題可以試試：
- 「從 Chat 到 Generative UI：AI-native 介面的下一步」
- 「人類該在 agent 流程的哪一關介入？」

## 4. 發布到 GitHub Pages

```bash
python scripts/render_deck.py agent-autonomy --publish   # 複製到 docs/ 並更新 docs/index.html
git add -A && git commit -m "slides: agent-autonomy"
git remote add origin https://github.com/<你的帳號>/<repo>.git
git push -u origin main
```

接著到 GitHub repo 的 **Settings → Pages**，Source 選 `main` 分支的 `/docs` 資料夾。

## 5. 反思

用 `guide/reflection-template.md`，回答作業的三個問題。

---

## 檢查腳本一覽

| 腳本 | 檢查什麼 |
|---|---|
| `lint_wiki.py` | 斷連結、孤兒頁、papers 必填欄位與段落、沒出處的段落、index/log 是否同步 |
| `check_coverage.py` | 主題相關頁面 ≥ 3、論文 ≥ 3，不足就停 |
| `check_cards.py` | 每張證據卡只來自一篇論文、每條主張都有頁碼 |
| `check_outline.py` | 8–15 頁、每頁對應卡片、每張卡都被用到 |
| `check_drafts.py` | 每頁有出處、出處存在、數字能在 wiki 找到、字數上限 |
| `check_deck.py` | 頁數一致、出處列、稿件改了要重渲染、（選用）真實溢出 |
| `run_checks.py` | 依 graph 順序跑全部，寫出 report.md |

所有腳本只用 Python 標準函式庫，不用另外 `pip install`。
