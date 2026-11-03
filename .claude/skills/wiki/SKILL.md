---
name: wiki
description: 知識庫（照 Karpathy 的 LLM Wiki 做法）。主人說「整理一下」「放進知識庫」「存起來」、問「資料裡有什麼」「我知道哪些關於 X 的」，或說「健檢」的時候用。收尾寫教訓時也用。
---

# 知識庫：整理、回答、健檢

`knowledge/raw/` 是原始資料，**存進去就不改**。`knowledge/wiki/` 是 AI 寫的筆記。`knowledge/wiki/index.md` 列出每一頁。`knowledge/wiki/log.md` 只往下加。為什麼這樣做：[這個資料夾怎麼運作](../../../knowledge/wiki/workspace/how-this-folder-works.md)。

## wiki 的四區（只有一層資料夾）

| 資料夾 | 放什麼 | 格式 |
|---|---|---|
| `knowledge/wiki/notes/` | 整理好的資料，一個主題一頁，所有專案共用 | [note-template.md](references/note-template.md) |
| `knowledge/wiki/projects/` | 專案頁，一個專案一頁 | `.claude/skills/new-project/project-page-template.md` |
| `knowledge/wiki/lessons/` | 教訓：不想再犯的錯，一條一頁 | [lesson-template.md](references/lesson-template.md) |
| `knowledge/wiki/workspace/` | 這個資料夾的做事方式，每個專案都適用的 | 跟筆記一樣 |

都不適合才開新的一區，並且加進這張表。

## 整理（放了新資料）

1. **存原始檔。** 先在 `knowledge/raw/` 找同一個主題的。**有就加在那份最下面**：新的一段 `## YYYY-MM-DD · 誰或從哪來`，上面的字一個都不改。沒有才開新的一份 `knowledge/raw/<種類>/<這是什麼>.md`，開頭照 [raw-template.md](references/raw-template.md)。主人自己丟進來的 PDF、Excel、照片原樣留著；要的話旁邊放一份同名的 `.md` 把重點打成字。
2. **先找有沒有同一頁。** 用關鍵字跟同義詞搜 `knowledge/wiki/`。**一個主題一頁**：已經有就更新那一頁，不要再開一頁。
3. **寫。** 照格式寫或更新。寫任何數字、日期、引句之前，先在原始檔找到一模一樣的字；找不到就不要寫。互相矛盾、沒寫清楚的，放進「需要人工確認」。
4. **連帶的也改。** 這份資料影響到別頁的，也一起更新。舊的說法不要偷偷改掉：在下面加一行 `> **已過時**（YYYY-MM-DD）：…` 或 `> **有爭議**：…`。
5. **登記。** `knowledge/wiki/index.md` 那一行的「更新」改成今天（新的一頁就加一行），`knowledge/wiki/log.md` 最下面加一行：`- YYYY-MM-DD · 誰 · 整理〈頁名〉（原始檔：raw/<種類>/<檔名>）`。

## 回答（主人問問題）

先讀 `knowledge/wiki/index.md`，再搜關鍵字跟同義詞，讀那幾頁，回答時附連結。要查證才打開原始檔。沒人叫你存就不寫檔；主人說要存，存成 `knowledge/wiki/notes/<這是什麼>.md`，來源寫「整理自〈頁名〉」，登記進目錄跟 log。

## 健檢（一個星期一次）

1. 電腦有 Python 就跑 `python tools/check_wiki.py .`，修它找到的：目錄沒列的頁、目錄列了卻不在的頁、壞掉的連結、教訓少了階段或量法、目錄的日期跟那頁對不上。
2. 再用看的，**列出來給主人，不要偷偷改**：
   - 數字、日期、引句在原始檔找不到的
   - 兩頁（或兩份原始檔）講同一件事的（建議合併）
   - 互相矛盾、可能過時的
   - 沒有任何一頁連過來的頁
   - 階段該換的教訓（套用 3 次以上還是試用中的）
   - 「更新」超過 14 天的專案頁、「下一步」沒寫日期的
3. log 加一行：`- YYYY-MM-DD · 誰 · 健檢：找到 N 個、修了 M 個`。

## 規則

- 連結照檔案位置寫。從 `knowledge/wiki/<區>/` 連到原始檔：`../../raw/<種類>/<檔名>.md`。
- 寫日期（2026-10-28），不寫「這週」。
- 一頁短短的就好。超過 80 行，拆成兩頁。
- log 只記知識庫的動作（整理、存答案、健檢、教訓），一件一行。專案的進度寫在專案頁。
