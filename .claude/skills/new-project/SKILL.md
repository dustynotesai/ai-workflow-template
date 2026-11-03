---
name: new-project
description: 新增一個專案。主人說「我要開始一件新的事」「新增專案」「幫我開一個 X」的時候用。開資料夾、寫專案頁、登記進目錄跟 log，看哪些教訓跟筆記用得上。
---

# 新增一個專案

每件事一個資料夾 `projects/<專案短名>/`，一件事出錯不會弄亂另一件。資料跟教訓不放在專案裡，放在共用的 `knowledge/`。

## 先問清楚（主人沒講的才問，一次問完）

- 名字、一句話要做到什麼、截止日（沒有就寫「沒有」）。
- 放在哪：不講就放 `projects/<專案短名>/`；已經有資料夾或 repo 的，寫它在哪，主人沒說就只讀不改。
- 專案短名：英文小寫加連字號（例如 `new-fridge`）。主人沒給就你取，跟他說一聲。

## 步驟

1. **原始想法。** 主人講的目標、需求、討論，照 wiki skill「整理」第 1 步存進 `knowledge/raw/projects/<專案短名>.md`。
2. **資料夾。** 開 `projects/<專案短名>/`，放一份 `CLAUDE.md`：照 [project-claude-template.md](project-claude-template.md) 填。
3. **專案頁。** 照 [project-page-template.md](project-page-template.md) 寫 `knowledge/wiki/projects/<專案短名>.md`，日期寫今天。
4. **用得到的。** 看目錄 `knowledge/wiki/index.md`：別的專案整理過、這次用得到的筆記，連進「用到的筆記」，不要重查。看 `knowledge/wiki/lessons/`：哪幾條這個專案也適用，寫在回報裡。
5. **登記。** 目錄的「專案」那一區加一行，`knowledge/wiki/log.md` 加一行。

## 做好的樣子

- 電腦有 Python 的話，`python tools/check_wiki.py .` 沒有錯。
- 回報 3 行：建議的前 3 個下一步、用得到哪幾條教訓、主人應該先放哪些檔案進 `knowledge/raw/`。
