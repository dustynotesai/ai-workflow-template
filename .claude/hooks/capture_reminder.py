#!/usr/bin/env python3
"""收尾提醒（Claude Code 的 Stop hook，在 .claude/settings.json 打開）。說明：同一個資料夾的 README.md。

這次對話裡資料夾有檔案變了，AI 要停下來之前提醒它一次：跑 capture（下次還要重講嗎？）。
同一批變動只提醒一次，不會一直跳、不會繞圈。只用 Python 內建的東西，不用 git。

  python capture_reminder.py start   對話開始時記下現在的樣子（SessionStart）
  python capture_reminder.py         AI 要停下來時比對（Stop）
"""

import json
import os
import sys

SKIP_DIRS = {".git", "node_modules"}
MARKER = os.path.join(".claude", "hooks", ".capture-state")

REASON = (
    "收尾檢查（capture skill，.claude/skills/capture/SKILL.md）：這次做的事，下次主人還要重講嗎？"
    "主人糾正過你 → 存原話、寫一條教訓；主人教了怎麼做 → 記進 .claude/skills/capture/watchlist.md；"
    "做完一段 → 更新專案頁的「現在做到哪」「下一步」「更新」。都不用就說一句「不用記」再停。"
)


def state():
    newest, count = 0.0, 0
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            path = os.path.join(root, name)
            if os.path.normpath(path) == os.path.normpath(MARKER):
                continue
            try:
                newest = max(newest, os.path.getmtime(path))
                count += 1
            except OSError:
                pass
    return f"{count}:{newest:.0f}"


def save(value):
    try:
        with open(MARKER, "w", encoding="utf-8") as f:
            f.write(value)
    except OSError:
        pass


def main():
    os.chdir(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
    now = state()
    if len(sys.argv) > 1 and sys.argv[1] == "start":
        save(now)
        return
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    try:
        with open(MARKER, encoding="utf-8") as f:
            before = f.read().strip()
    except OSError:
        before = ""
    save(now)
    if data.get("stop_hook_active") or not before or before == now:
        return  # 已經提醒過、第一次跑、或什麼都沒變
    # ensure_ascii：中文寫成 \uXXXX，Windows 的命令列也印得出來
    print(json.dumps({"decision": "block", "reason": REASON}))


if __name__ == "__main__":
    main()
