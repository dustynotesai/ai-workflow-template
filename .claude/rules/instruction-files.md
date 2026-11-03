---
paths:
  - "AGENTS.md"
  - "CLAUDE.md"
  - "**/CLAUDE.md"
  - ".claude/agents/*.md"
  - ".claude/skills/**/SKILL.md"
  - ".claude/rules/*.md"
---
# 你正在改給 AI 讀的說明檔

這些檔每次都會被讀進去，每一行都佔 AI 的注意力。

- **長度上限**（寫之前先數）：`AGENTS.md` 100 行；專案的 `CLAUDE.md` 60 行；角色 40 行；skill 100 行。滿了先刪一行過時的，或把一段搬進 skill，再加新的。
- **只寫看不出來的。** 資料夾裡有什麼看得到就不用寫；寫交給誰、不要碰什麼、為什麼。
- **同一件事只寫一個地方**，其他地方連過去。
- **只跟某些檔案有關的規則**，放 `.claude/rules/` 加 `paths:`，不要放 `AGENTS.md`。
- **專案的細節放那個專案的 `CLAUDE.md`**，不放 `AGENTS.md`。
- 寫成「做 X」，不寫成「X 是…」。原因不明顯的，附一句為什麼。
