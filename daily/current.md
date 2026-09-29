# 今日任务 · 2026-09-30（周三）W4D3 · 🔴 国庆前最后一个训练日

> **10-01 起停训 7 天，下一个训练日是 10-08（周四）。**
> 今天做不完的东西，不是"顺延一天"，是**顺延八天**。中间隔一个长假，
> 昨天 16:54 我讲的那四个 `useState` 知识点会掉得差不多干净。
>
> 昨天 185min，上午和下午前半段都扎实（`optional` 通式自推、两个主动提问挖出 `observer_list.h`），
> **但 17:35 之后停住了**。`App.tsx` 我 23:00 读了全文：只 `import` 了 `useState`，
> 一处调用都没有，`<input />` 没 `value` 没 `onChange`，`<button>` 没 `onClick`。
> 21:33 我问你是被工作打断还是卡在受控输入框，你没回。**今天第一句话先回这个。**

---

## 0. 开工先回三个问题（2 分钟，不回不许往下做）

1. 昨天下午 17:35 之后，是被部门任务打断，还是卡在受控输入框（`value` + `onChange`）上？
   —— 打断我就重排，卡住我就补讲，**不说我就没法判断**。
2. 词频题你写的是 `std::unordered_map<char, int>` + `for (auto word : str)`，
   拿到的是**字符**不是**词**。是有意改的，还是没注意到题目要按空格切词？
3. `sizeof(std::optional<int>)` 你答"我觉得是 8，跑完真的是 8" ——
   **那句"我觉得是 8"是跑之前写下来的，还是跑完回头说的？**
   元规则「先写预测再跑」已经第十次了，`current.md` 昨天白纸黑字写了"今天这次记你账"。

---

## 一、🔴 最高优先 · `useState` 练习本体做完（约 30min）

**这是今天唯一一件"不做完就会因为跨假期而作废"的事。** 排在最前，别的都往后靠。

知识点昨天 16:54 已经讲完了，不重复。只补两条你昨天问到但没落地的：

> **它是什么 · 受控输入框（controlled input）**（新概念，我直接给，不让你猜）：
> `<input />` 默认自己记着用户敲的字，React 不知道。「受控」是指**让 React 的 state 当唯一真相**：
> - `value={text}` — 输入框显示什么，由 state 决定（不是由用户敲了什么决定）
> - `onChange={e => setText(e.target.value)}` — 用户每敲一个键，React 收到事件，
>   把新值写回 state，state 变了组件重跑，`value` 跟着变，界面才动
>
> 所以「敲字 → 界面变」这条链在 React 里是**绕了一圈**的：
> 敲字 → onChange → setState → 组件重跑 → value 更新 → 界面变。
> 少写 `onChange` 的话，`value` 被钉死在初始值上，**输入框会变成敲不进字的**。
> 这一点正好可以当今天的验证实验。
>
> **它是什么 · `e.target.value`**：`e` 是事件对象，`e.target` 是触发事件的那个 DOM 元素
> （这里就是 `<input>`），`.value` 是它当前的内容。

**你写的练习**（我不给实现）：在 `vite-project/src/App.tsx` 里做最小消息列表。

- 两个 `useState`：一个存输入框里的字，一个存消息数组
- 点「发送」→ 把输入框内容加进消息数组 → 下面多出一条 `MessageItem`（复用 09-28 写的那个）
- 发完清空输入框
- 数组要怎么渲染成多条：`{msgs.map(...)}`，`map` 就是你 C++ 里 `std::transform` 那个意思 ——
  一个数组变成另一个数组。**每一项要带 `key` 属性**，不带 React 会在控制台警告，
  为什么要带你自己去官方那一节找。

**做完跑三个验证**：

1. `npx tsc --noEmit -p tsconfig.app.json` 零报错
2. **不可变更新的分辨力实验**：把 `setMsgs([...msgs, t])` 改成 `msgs.push(t); setMsgs(msgs);`，
   看界面是不是不更新了。—— 如果改完界面照样更新，**说明我昨天讲的知识点是错的，直接抓我**。
3. **受控实验**：把 `onChange` 删掉，只留 `value={text}`，看输入框是不是敲不进字。

---

## 二、🔴 硬任务 · 「假期后第一件事」清单（15min，09-24 已落空一回）

写进 `daily/history/2026-09-30.md` 的独立一节，标题就叫「10-08 回来第一件事」。

**不许写「复习一下 C++」这种废话。** 每一条必须具体到三件事：
**打开哪个文件 / 跑哪条命令 / 答哪几问**。

我给你格式（内容你自己填，我不替你想）：

```
1. 打开 F:\code\cpp-practice\week-04\____.cpp，跑 ____，
   先不看代码答：____？
2. 打开 ____，……
```

至少 5 条，覆盖：C++ 侧（`optional` / `string_view` / 容器）、
前端侧（`useState` / props / npm）、Chromium 侧（三层链 / Rule of 2）、
q-framework 对照轨、以及你自己觉得最容易忘的那一条。

**这份清单 10-08 我会当作当天上午的复习提纲用**（`calendar-holidays.md` 4.2 定的：
节后第一个上午整段间隔复习，不排新内容）。你写得糊，10-08 就复习得糊。

---

## 三、preload / contextBridge 安全审计三问（20min，昨天顺延来的）

题目不变，照抄昨天的（`F:\code\ai-desktop-assistant\preload.js` 现有 7 行）：

```js
const { contextBridge, ipcRenderer } = require('electron/renderer')
contextBridge.exposeInMainWorld('electronAPI', {
  openFile: () => ipcRenderer.invoke('file:pick'),
  getCurrentData: () => ipcRenderer.invoke('getCurrentData'),
  helloName : (nameString) => ipcRenderer.invoke('helloName', nameString)
})
```

1. `helloName(nameString)` 接收渲染进程传来的字符串。**渲染进程被 XSS 了，攻击者能用这个接口做什么？**
   取决于主进程那边怎么实现 —— 自己去 `main.js` 看 `ipcMain.handle('helloName', ...)` 再答。
2. 假如加一行 `nodeRequire: (m) => require(m)` —— **三层链的哪一层被废掉了？为什么？**
   （这是你 09-28 整链口述里第三层「contextBridge 写错了」的具体实例）
3. 直接 `exposeInMainWorld('ipc', ipcRenderer)` 会怎样？官方安全文档明确禁止，**自己找出禁止的理由**。

> **它是什么 · XSS（跨站脚本）**（避免又出现「我去搜了」的情况，我直接给）：
> 攻击者想办法让**他写的 JS** 在你的页面里跑起来（比如页面把用户输入当 HTML 插进 DOM）。
> 一旦跑起来，他的代码和你自己的页面代码**同权限**——你的页面能调 `window.electronAPI.xxx`，
> 他也能调。所以 preload 暴露出去的每一个函数，都要按「**攻击者会直接调用它**」来设计。

---

## 四、q-framework 对照轨第二格（若时间不够，**顺延 10-08，不算欠**）

只读 `E:\code\q-framework\webview\webview.h`（约 70 行纯虚基类），说清两件事：

1. `Create()` 为什么是 `static`？（这一问是 C++ 的不是架构的 —— 想想调用它的时候还有没有对象存在）
2. `Delegate` 那一套是干什么的？它解决的问题，Electron 里对应的是什么机制？

---

## 五、记录（15min）· 今天自己写

`daily/history/2026-09-30.md`，五栏：完成、掌握（闭卷自答·**你自己的话**）、未掌握/卡壳、证据、明日计划。
外加第二节那个「10-08 回来第一件事」清单。

🔴 **昨天的记录又是我 23:00 补的，这是 09-16 之后第六次。**
我只能摘你会话里的原话，摘得再准也不是你回头写的那一遍 —— **那一遍才是复习**。
今天是假期前最后一天，这一遍尤其值钱。

---

## 六、假期安排（10-01 ~ 10-07）

**不留作业、不设「有空看看」、不做任何变相排课。** 这是你 09-23 自己提的，我照办。
cron 推送这 7 天只会输出一行「假期停训」。

**10-08（周四）回来**：上午整段间隔复习（按你写的那份清单 + C++ 7 天复测），
下午另有真活儿 —— 扫 `base/` 顶层 108 个 `.h` 文件名，挑 5 个咱们团队重复造过的轮子，
这个产出简历上可以写。
