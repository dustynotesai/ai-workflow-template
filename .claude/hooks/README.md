# 選用：做完自動提醒 AI 收尾

**不用也可以。** `AGENTS.md` 已經寫了「做完跑收尾」，大部分時候 AI 會自己做；忘了的話，貼 [08 收尾](../../prompts/08-收尾.md) 就好。

想要每次都不會忘，Claude Code 可以在 AI 停下來之前自動提醒它一次（這叫 Stop hook）。只有 Claude Code 有，Codex、Cursor 沒有。

## 要先有什麼

- **Python**：Mac 打開「終端機」打 `python3 --version`，有出現版本號就有。Windows 多半沒有，要從 python.org 裝（免費）。沒有 Python 就跳過這一頁，不影響其他功能。

## 怎麼打開

在 `.claude/` 資料夾裡新增一個檔案 `settings.json`（已經有的話，把 `"hooks"` 那一段併進去），內容：

```json
{
  "hooks": {
    "SessionStart": [
      { "hooks": [ { "type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/capture_reminder.py\" start 2>/dev/null || python \"$CLAUDE_PROJECT_DIR/.claude/hooks/capture_reminder.py\" start" } ] }
    ],
    "Stop": [
      { "hooks": [ { "type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/capture_reminder.py\" 2>/dev/null || python \"$CLAUDE_PROJECT_DIR/.claude/hooks/capture_reminder.py\"" } ] }
    ]
  }
}
```

重開 Claude Code。之後只要這次對話裡有檔案變了，AI 停下來之前會收到一次提醒：「下次還要重講嗎？」同一批變動只提醒一次。什麼都沒改（只是問問題）就不會跳。

## 它做什麼

[`capture_reminder.py`](capture_reminder.py)：對話開始時記下資料夾裡有幾個檔案、最新改的是什麼時候；AI 要停的時候再看一次，不一樣就提醒。記錄存在 `.claude/hooks/.capture-state`，可以刪。不連網、不裝東西、不用 git。

不想要了：把 `settings.json` 裡 `"hooks"` 那一段刪掉。
