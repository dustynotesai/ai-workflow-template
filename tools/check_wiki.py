#!/usr/bin/env python3
"""知識庫健檢（只檢查格式，不改檔）。AI 做完會跑；你不用自己跑。

檢查：
1. knowledge/wiki/ 的每一頁都列在 index.md，index.md 列的每一頁都在，而且「更新」日期一樣。
2. knowledge/ 裡每一個相對連結都找得到檔案。
3. 每一頁第一行是「# 標題」、有「> 更新：」；教訓另外要有「> 階段：」（試用中／保留／淘汰）跟「> 量法：」。
4. .claude/agents/ 的角色、.claude/skills/ 的 skill 開頭都有 name 跟 description。

用法：python tools/check_wiki.py .
有問題會列出來，結束碼是 1。只用 Python 內建的東西。
"""

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
INDEX_ROW_RE = re.compile(r"^\|\s*\[[^\]]*\]\(([^)]+)\)\s*\|.*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*$")
META_RE = re.compile(r"^>\s*([^：:]+)[：:]\s*(.*)$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
STAGES = {"試用中", "保留", "淘汰"}
SPECIAL = {"index.md", "log.md"}


def metadata(text):
    meta = {}
    for line in text.splitlines()[1:15]:
        m = META_RE.match(line)
        if m:
            meta[m.group(1).strip()] = m.group(2).strip()
    return meta


def links(text):
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = re.sub(r"`[^`]*`", "", line)
        for target in LINK_RE.findall(line):
            if not re.match(r"^[a-z]+:", target) and not target.startswith("#"):
                yield target.split("#")[0]


def frontmatter_ok(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    head = text.split("---", 2)[1] if text.count("---") >= 2 else ""
    return bool(re.search(r"^name:\s*\S", head, re.M)) and bool(re.search(r"^description:\s*\S", head, re.M))


def main(root):
    knowledge = root / "knowledge"
    wiki = knowledge / "wiki"
    errors = []
    pages = sorted(p for p in wiki.rglob("*.md") if p.name not in SPECIAL)

    indexed = {}
    for line in (wiki / "index.md").read_text(encoding="utf-8").splitlines():
        m = INDEX_ROW_RE.match(line)
        if m:
            indexed[(wiki / m.group(1)).resolve()] = m.group(2)

    for path in pages:
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        meta = metadata(text)
        if not text.startswith("# "):
            errors.append(f"{rel}：第一行要是「# 標題」")
        if not meta.get("更新"):
            errors.append(f"{rel}：少了「> 更新：」那一行")
        if path.parent.name == "lessons":
            if meta.get("階段") not in STAGES:
                errors.append(f"{rel}：「> 階段：」要是試用中、保留或淘汰")
            if not meta.get("量法"):
                errors.append(f"{rel}：教訓要有「> 量法：」那一行")
        if path.resolve() not in indexed:
            errors.append(f"{rel}：index.md 沒有列這一頁")
        elif meta.get("更新") and indexed[path.resolve()] != meta["更新"]:
            errors.append(f"{rel}：index.md 寫更新 {indexed[path.resolve()]}，這一頁寫 {meta['更新']}")

    for target in indexed:
        if not target.exists():
            errors.append(f"knowledge/wiki/index.md：列了一頁，但檔案不在：{target.name}")

    for path in sorted(knowledge.rglob("*.md")):
        for target in links(path.read_text(encoding="utf-8")):
            if target and not (path.parent / target).exists():
                errors.append(f"{path.relative_to(root).as_posix()}：連結壞了 {target}")

    for path in sorted((root / ".claude" / "agents").glob("*.md")):
        if not frontmatter_ok(path):
            errors.append(f"{path.relative_to(root).as_posix()}：開頭要有 name 跟 description")
    for path in sorted((root / ".claude" / "skills").glob("*/SKILL.md")):
        if not frontmatter_ok(path):
            errors.append(f"{path.relative_to(root).as_posix()}：開頭要有 name 跟 description")

    if errors:
        print(f"check_wiki：{len(errors)} 個問題")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"check_wiki：沒問題（{len(pages)} 頁、index 列了 {len(indexed)} 頁）")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()))
