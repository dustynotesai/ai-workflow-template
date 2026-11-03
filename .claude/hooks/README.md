# 做完自動提醒 AI 收尾

只有 Claude Code 有這個功能（叫 Stop hook），Codex、Cursor 沒有；`AGENTS.md` 已經寫了「做完跑收尾」，所以沒有也沒關係。忘了的話，貼 [08 收尾](../../prompts/08-wrap-up.md) 就好。

## 它做什麼

[`capture_reminder.py`](capture_reminder.py)：對話開始時記下資料夾裡有幾個檔案、最新改的是什麼時候；AI 要停下來的時候再看一次，不一樣就提醒它一次：「下次還要重講嗎？」同一批變動只提醒一次，什麼都沒改（只是問問題）就不會跳。

記錄存在 `.claude/hooks/.capture-state`，可以刪。不連網、不裝東西、不用 git。

## 已經打開了

[`.claude/settings.json`](../settings.json) 已經寫好，用 Claude Code 打開這個資料夾就會生效。

- 要電腦有 **Python**：Mac 打開「終端機」打 `python3 --version`，有出現版本號就有。Windows 多半沒有，要從 python.org 裝（免費）。
- **沒有 Python 也不會壞**：提醒就安靜地不跳，其他功能照常。

不想要了：把 `settings.json` 裡 `"hooks"` 那一段刪掉，重開 Claude Code。
