# AI 總部起手包：一個資料夾管你所有的事，AI 越用越懂你

AI 不會自己變聰明。你上次說過「不要漸層」「報告先寫結論」，換一件事它又忘了；你不要的東西，它會一直做。

問題不在 AI，在它每次都從零開始。這個資料夾給它三樣東西：

1. **一張地圖**：你有哪些事在做、各放在哪、做到哪。
2. **一份共用的資料**：你的檔案、查過的資料，整理一次，每件事都去同一個地方拿。
3. **一本它學到的你**：你糾正過它的、教過它的，下次開工前先讀。

做什麼工作都能用：接案、開店、上班、讀書、家裡的事。不用會寫程式，也不用打開「終端機」那個黑色視窗。照下面做，大約 5 分鐘。

---

## 裡面有什麼

| 資料夾 | 放什麼 |
|---|---|
| `projects/` | 每件事一個資料夾，放做出來的東西（文件、計畫、清單）。每個資料夾可以有自己的 `CLAUDE.md`：只跟這件事有關的規則。 |
| `knowledge/raw/` | 原始資料：你的檔案、查來的資料、你糾正 AI 的原話。**放進來就不改**，新的加在最下面。 |
| `knowledge/wiki/` | AI 讀完原始資料寫的：目錄、每個專案一頁、教訓、筆記。每一句都連回原始檔。 |
| `AGENTS.md` | 家規：開工前讀什麼、做完做什麼、一定要照的規則。AI 每次先讀這份。 |
| `CLAUDE.md` | 讓 Claude Code 讀到 `AGENTS.md`。不用動它。 |
| `.claude/` | 給 Claude Code 的：四個角色、三個固定做法（Skill）、自動提醒收尾。 |
| `prompts/` | 叫 AI 做事的句子，複製貼上就能用。 |
| `tools/` | 一個健檢小程式，AI 做完會跑（要電腦有 Python，沒有就跳過）。 |
| `archive/` | 做完或不做了的專案。 |

```
AGENTS.md  CLAUDE.md  README.md
projects/                 每件事一個資料夾
knowledge/
  raw/                    原始資料（放了就不改）
    feedback/  how-tos/  lessons/  projects/  references/
  wiki/                   AI 整理的
    index.md  log.md      目錄、紀錄
    projects/             專案頁：做到哪、下一步、還沒決定的事
    lessons/              教訓：AI 學到的你
    notes/                筆記：一個主題一頁，所有專案共用
    workspace/            這個資料夾的做事方式
.claude/  agents/  skills/  rules/  hooks/
prompts/  tools/  archive/
```

資料照「種類」放，不照「事情」放：一份資料只放一次，每件事都去同一個地方拿。資料改了，每件事拿到的都是新的。

> `.claude` 開頭有一個點，Windows、Mac 可能預設看不到，不影響使用。

### 四個地方：AI 的記憶放哪

| 影片裡的說法 | 在這個資料夾 | 放什麼 |
|---|---|---|
| 家規 | `CLAUDE.md`（規則寫在 `AGENTS.md`） | 每次開工都要照的規則。裡面有一條：只要我糾正你，就把這次的教訓整理下來，放到對的地方 |
| 便利貼 | `knowledge/wiki/lessons/` | 教訓：你糾正過它的事，一條一份。不放在單一專案裡，換專案一樣先讀 |
| Skill（食譜） | `.claude/skills/` | 固定做法：收尾 `capture`、知識庫 `wiki`、新增專案 `new-project`，還有你教過 3 次的事 |
| 知識庫 | `knowledge/raw/`、`knowledge/wiki/` | 共用資料：你的檔案跟整理好的筆記，每個專案都去同一個地方拿 |

---

## 它怎麼學

```
1. 開工前     AI 先讀目錄、那件事的專案頁、你的教訓（knowledge/wiki/lessons/）
2. 你糾正它   「不要漸層」→ 它先改對，把你的原話存進 knowledge/raw/feedback/
3. 變成教訓   自己寫一條，階段：試用中
4. 下一件事   換一個專案，開工前一樣讀到這條，你沒講也照做，記在「套用紀錄」
5. 越用越準   照做 3 次都沒再被糾正 → 問你要不要升成「保留」
6. 教了 3 次   同一件事你教了 3 次 → 問你要不要寫成固定做法（Skill），之後一句話就好
```

**還沒決定的事，它先問你。** 每一頁專案頁有一區「還沒決定的事：問我，不要猜」。做到那一件，AI 停下來問你，不會自己猜一個；你回答了，它搬到「已決定」寫上日期，之後不再重新討論。

每次做完，AI 會問自己一句：**「下次還要重講嗎？」**（這叫收尾，`capture`）。要，就把最小的一份記在對的地方；不用，就什麼都不寫。

**教訓跟著你，不跟著專案。** 在一件事學到的，別的事也用得上。

### 四個角色：照工作分，不照專案分

| 角色 | 做什麼 |
|---|---|
| 組長 `lead` | 有好幾步的事先找它：拆工作、交給對的角色、更新專案頁；也回答「所有專案做到哪」 |
| 研究員 `researcher` | 把新放的資料整理成筆記、回答問題、上網查 |
| 製作 `maker` | 做出東西：文件、計畫、清單、貼文、表格 |
| 檢查員 `reviewer` | 交給你之前，照每一條教訓的「量法」對一遍 |

Claude Code 會自己挑角色，你也可以直接說「用 researcher 整理一下」。其他工具在開頭說「你現在是研究員」就好。同一種工作你講了 2–3 次、四個角色都不太對，AI 會建議加一個。

---

## 一個例子（範例，可以刪）

資料夾裡有一組很小的範例，檔名都是 `example-` 開頭，內容是虛構的。

1. 第一篇貼文沒交代風格，AI 自己做了紫色漸層、三種字體。你說：「不要漸層，只用深藍跟白。標題 10 個字以內。」AI 先改對（[第一篇](projects/example-social/first-post.md)），原話存進 [`knowledge/raw/feedback/`](knowledge/raw/feedback/example-post-style.md)，自己寫成一條教訓：[照品牌做](knowledge/wiki/lessons/example-follow-the-brand.md)。
2. 開新對話做第二篇，**沒提顏色**。AI 開工先讀教訓，第一版就對了（[第二篇](projects/example-social/second-post.md)）。
3. 換去做影片封面，**什麼都沒交代**。AI 開工先讀同一條教訓：深藍跟白、標題 5 個字（[封面](projects/example-social/cover.md)）。要你決定的「封面要不要放你的臉？」，它寫進[專案頁](knowledge/wiki/projects/example-social.md)先問你。

你開自己的專案時也一樣：教訓在 `knowledge/wiki/lessons/`，不在任何一個專案資料夾裡，每個專案開工前都先讀。

---

## 5 分鐘開始

### 1 · 下載（1 分鐘）

1. 在這一頁最上面，按綠色的 **Code** 按鈕 → **Download ZIP**。
2. 解壓縮：
   - Windows：在下載的檔案上按右鍵 → **全部解壓縮**。
   - Mac：點兩下那個檔案。
3. 把解壓出來的資料夾改名成 `my-hq`（或任何你喜歡的名字），放在你找得到的地方，例如「文件」裡面。

> 會用 git 的人：`git clone https://github.com/dustynotesai/ai-workflow-template.git my-hq`

### 2 · 把你的檔案放進 `knowledge/raw/`（2 分鐘）

先挑**一件你正在做的事**就好，不用一次全放。

| 你的檔案 | 放進 |
|---|---|
| 文件、表格、收據、合約、查到的價格跟規定、文章 | `knowledge/raw/references/` |
| 某件事的想法、需求、群組討論、會議紀錄 | `knowledge/raw/projects/` |
| 你已經知道的習慣（「報告先寫結論」） | `knowledge/raw/lessons/` |

用**複製**的，不要剪下：原本的檔案留在原本的地方，當作備份。`feedback/`、`how-tos/` 是 AI 記你的原話用的，你不用放。

### 3 · 用 AI 工具打開這個資料夾（1 分鐘）

三個選一個，打開以後選「打開資料夾」（Open Folder），選 `my-hq`：

- **Claude Code**：Claude 的桌面 app 裡就有，要 Claude 的付費方案。
- **Codex**：OpenAI 的，用 ChatGPT 帳號登入。
- **Cursor**：一個編輯器，裡面有 AI。

它們都會先讀 `AGENTS.md`（Claude Code 透過 `CLAUDE.md` 讀到同一份），所以一打開就知道這個資料夾的規則。

### 4 · 貼第一句話（1 分鐘）

打開 [`prompts/01-organize.md`](prompts/01-organize.md)，整段複製，貼給 AI。

它會讀你放進 `knowledge/raw/` 的檔案，在 `knowledge/wiki/` 寫筆記，最後告訴你它做了什麼。再用 [04 新增一個專案](prompts/04-new-project.md) 把你正在做的事加進來。這些工具第一次要寫檔案時通常會先問你，按「允許」就好。

### 範例要刪嗎？

看懂了就可以刪，刪了範本照樣能用：

1. 刪掉所有 `example-` 開頭的檔案跟資料夾：`projects/example-social/`、`knowledge/wiki/projects/example-social.md`、`knowledge/wiki/lessons/example-follow-the-brand.md`、`knowledge/raw/feedback/example-post-style.md`。
2. `knowledge/wiki/index.md`、`knowledge/wiki/log.md` 裡有「（範例）」的那幾行刪掉。
3. 這份 README 的「一個例子」那一節刪掉。

也可以直接跟 AI 說：「照 README 把範例刪掉。」它刪之前會先問你。

---

## 之後每天怎麼用

| 你想 | 用這句 |
|---|---|
| 放了新檔案進 `knowledge/raw/` | [01 整理](prompts/01-organize.md) |
| 問問題，例如「上個月花最多的是哪一類？」 | [02 問問題](prompts/02-ask.md) |
| 一個星期檢查一次：連結壞掉、太久沒更新的專案頁 | [03 健檢](prompts/03-health-check.md) |
| 開始一件新的事 | [04 新增一個專案](prompts/04-new-project.md) |
| 表格加總、分類 | [05 處理表格](prompts/05-work-with-a-table.md) |
| 做一份文件、一篇貼文、一張封面 | [06 幫我做一個東西](prompts/06-make-something.md) |
| 一次看所有事情的進度 | [07 我所有的專案現在做到哪？](prompts/07-all-projects-status.md) |
| 做完一段事 | [08 收尾](prompts/08-wrap-up.md) |
| AI 做出你不要的東西 | [09 這裡錯了](prompts/09-thats-wrong.md) |

全部的句子在 [`prompts/`](prompts/README.md)。

**自動提醒收尾**：用 Claude Code 的話，AI 停下來之前會自動被提醒一次「下次還要重講嗎？」。要電腦有 Python；沒有也不會壞，規則已經寫在 `AGENTS.md`。說明：[`.claude/hooks/README.md`](.claude/hooks/README.md)。

---

## 沒有這些工具？

一般的 ChatGPT 或 Claude 網頁版也能用一半：開一個新對話（或「專案」），先把 `AGENTS.md` 跟 `knowledge/wiki/lessons/` 的內容貼進去，再上傳你要它看的檔案。它不能自己在你的電腦裡寫筆記、改專案頁，要你自己存回去。

## 要注意的

- **工作的資料，先看公司准不准用這些 AI 工具。** 檔案在你自己的電腦上，但 AI 讀到的內容會送到那家公司的伺服器處理。
- 身分證字號、帳號、卡號、地址，放進 `knowledge/raw/` 之前想一下要不要先遮掉。
- 用 git 的人：這個資料夾放了你的檔案以後，**不要推到公開的 GitHub**，要推就開私人 repo。
- AI 會寫錯。所以每一句筆記都要連回原始檔：它講錯的時候，你點進去就查得到是哪一份寫的。教訓也一樣：每一條都連回你的原話。

---

## 這個做法是誰想的

資料的放法來自 Andrej Karpathy 的〈[LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)〉（2026 年 4 月 4 日發在 GitHub Gist）。他把它分成三層：原始檔（raw sources）、AI 寫的 wiki、告訴 AI 怎麼做的規則檔；`index.md` 當目錄，`log.md` 按時間記發生了什麼。他的一句話：

> "the wiki is a persistent, compounding artifact."

意思是：整理一次，之後一直更新、越積越多，不用每問一次就從頭找一次。

這個起手包照他的三層來放，另外多了幾樣：每個專案一頁的專案頁、`knowledge/wiki/lessons/`（AI 學到的你）、收尾的 `capture`、四個照工作分的 AI 角色、`prompts/`（複製貼上的話）。規則檔用 [AGENTS.md](https://agents.md/) 這個很多 AI 工具都認得的格式。

---

**你不需要 AI 什麼都記得，你需要它知道去哪裡找，而且記得你說過的話。**

---

微塵筆記 DustyNotes · YouTube [@DustyNotesAI](https://www.youtube.com/@DustyNotesAI)

## 授權

[MIT](LICENSE)：可以自由使用、修改、分享，包括商業用途，保留版權聲明就好。照現狀提供，不做任何擔保。
