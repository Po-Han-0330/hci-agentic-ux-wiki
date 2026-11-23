# 文獻清單（raw/ 的來源）

主題：**AI-Native 介面與 Agentic UX 設計趨勢**（HCI）

挑選原則：
- 優先收 CHI / UIST 等 HCI 頂會論文，以及 Microsoft Research、Google Research、UW 等研究機構的報告
- 涵蓋「經典理論 → 生成式 AI 介面 → Agent 介面」三層，讓 wiki 能做跨時代比較
- 全部可公開下載（arXiv 或作者官網）

執行 `python scripts/fetch_papers.py` 會把下面的 PDF 下載到 `raw/`。

| ID | 論文 | 發表處 | 角色 |
|---|---|---|---|
| horvitz1999-mixed-initiative | Horvitz. *Principles of Mixed-Initiative User Interfaces* | CHI 1999 | 經典：自動化 vs. 直接操作 |
| amershi2019-guidelines | Amershi et al. *Guidelines for Human-AI Interaction* | CHI 2019（Honorable Mention） | 經典：18 條人機 AI 設計準則 |
| park2023-generative-agents | Park et al. *Generative Agents: Interactive Simulacra of Human Behavior* | UIST 2023 | LLM agent 架構與互動 |
| subramonyam2024-gulf-of-envisioning | Subramonyam et al. *Bridging the Gulf of Envisioning* | CHI 2024 | AI-native：prompt 介面的認知鴻溝 |
| tankelevitch2024-metacognitive-demands | Tankelevitch et al. *The Metacognitive Demands and Opportunities of Generative AI* | CHI 2024 | AI-native：使用者的後設認知負擔 |
| masson2024-directgpt | Masson et al. *DirectGPT: A Direct Manipulation Interface to Interact with LLMs* | CHI 2024 | AI-native：直接操作取代純對話 |
| bansal2024-human-agent-communication | Bansal et al. *Challenges in Human-Agent Communication* | MSR-TR-2024-53 | Agentic UX：12 個溝通挑戰 |
| feng2025-levels-of-autonomy | Feng, McDonald & Zhang. *Levels of Autonomy for AI Agents* | Knight 1st Amendment Institute / arXiv 2025 | Agentic UX：五級自主性 |
| mozannar2025-magentic-ui | Mozannar et al. *Magentic-UI: Towards Human-in-the-loop Agentic Systems* | MSR-TR-2025-40 | Agentic UX：co-planning、action guards |
| leviathan2026-generative-ui | Leviathan et al. *Generative UI: LLMs are Effective UI Generators* | Google Research / arXiv 2026 | AI-native：模型直接生成介面 |

作業要求至少 ingest 5 篇。建議的順序（可以邊做邊比較）：
1. amershi2019-guidelines（打底）
2. subramonyam2024-gulf-of-envisioning
3. bansal2024-human-agent-communication
4. feng2025-levels-of-autonomy
5. mozannar2025-magentic-ui
6. 其餘 5 篇有空再加
