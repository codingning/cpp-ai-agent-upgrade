# 今日任务 · 2026-09-29（周二）W4D2

> 🏆 **09-28 是开训以来最好的一天**：280min（前高 205min）、排的全做完、一条未顺延、
> 还自己加做了一个计时实验、Chromium 升到 L2。今天不要泄力 —— **本周只剩今天和明天，
> 10-01 起停训 7 天**，节前最后两天的密度决定假期后回来接得上什么。
>
> ⚠️ **昨天唯一的欠账是「产出」不是「知识」**：三仓零 commit。今天第一件事就是清它。

---

## 0. 开工前 5 分钟 · 清昨天的产出欠账（🔴 最高优先，不清不许开始新内容）

昨天你写了三份代码，**一份都没进版本库**。教练实查（09-28 23:00）：

| 仓 | 状态 | 要做什么 |
|---|---|---|
| `F:\code\cpp-practice` | `week-03/continer_timer.cpp`、`week-04/string_view_probe.cpp` 以及 09-23 两个探针全是 `??` 未跟踪 | `git add` + commit |
| `F:\code\vite_react\vite-project` | 🔴 **根本不是 git 仓库**（`git log` 报 `fatal: not a git repository`）。09-23 写的 `main.cjs` / `electron-smoke.cjs` **无版本记录已挂 5 天**，昨天的 `App.tsx` 同样裸着 | **先 `git init`**，加 `.gitignore`（至少 `node_modules/`、`dist/`），再首次 commit |
| `F:\code\new_npm` | 非仓库（一次性练习，可不入库） | 自己定，入库就顺手 init |

`.gitignore` 怎么写不用问我 —— `vite` 脚手架自带一份，你看一眼就知道要挡哪些目录。

---

## 一、上午 10:30-11:10（C++ 40min）

### A. 先清 Chromium 那条闭卷（10min，昨天顺延来的）

出处昨天就实抓给你了（`docs/debt-map.md` 第 139-158 行，两段原文可核，
commit `3e6893d`）。**只给出处不给答案**，闭卷答两问：

1. Renderer 和 Utility 都在沙箱里、都碰不到文件系统 —— **区别到底在哪一层？**
   （提示方向：这两种进程里跑的**代码是谁写的**）
2. network service 既然能进 Utility，**为什么不干脆放进 Renderer？**（线索是「Rule of Two」）

> **它是什么 · Rule of 2**（这条我直接给你，不让你猜）：Chromium 的安全硬规矩 ——
> 「处理不可信输入」「用不安全语言（C/C++）写」「不在沙箱里」三件事
> **最多只能同时满足两件**，三件全中就必须拆进程或换语言。

这条已经是**第六次**出现在计划里（前五次是我的账，09-24 已结清；这次是你的账）。今天必须落地。

### B. `std::optional`（20min · 本周原排）

> **它是什么**（新知识点，按 09-28 你立的规矩，我先讲清再让你写）：
> `std::optional<T>` 是 C++17 的「可能有值、也可能没有」的容器，最多装一个 `T`。
> 头文件 `<optional>`。三个要点：
> - 构造：`std::optional<int> a;`（空）／`std::optional<int> b = 42;`（有值）／`return std::nullopt;`（显式返回空）
> - 判空：`if (a)` 或 `a.has_value()`
> - 取值：`*a` 或 `a.value()` —— **区别是 `.value()` 空的时候抛异常，`*a` 空的时候是 UB**
> - `a.value_or(0)`：有值就给值，空就给 0

**你写的练习**（我不给实现）：一个函数，在 `std::vector<int>` 里找第一个大于 N 的数，返回 `std::optional<int>`；
`main` 里测两种情况：找得到 / 找不到。

**然后回答三问**（闭卷，不许翻代码）：

1. 以前你在 C/C++ 里表达「没找到」有哪几种写法？（想想 `find` 返回什么、指针返回什么、
   `bool` 返回值 + 出参那一套）每一种各有什么坑？
2. `*a` 和 `a.value()` 在空的时候行为不一样 —— 按我们 W1 学的分类，
   **哪一个更接近 `= delete` 那种「宁愿早死」的思路**？为什么标准库要同时留这两个？
3. 🔴 **接昨天那条自主实验的思路**：`std::optional<int>` 的 `sizeof` 是多少？
   **先写一句你的推理**（提示：它要同时存「值」和「有没有值」这个标志），**然后跑**。
   跑之前就写，不许看到数再编理由 —— 这是元规则第九次，昨天那次不记你账，今天这次记。

### C. STL 算法 + Lambda + 词频题（10min 起步，做不完顺延不扣）

这条是中秋从 W3D5 顺延来的，**内容一条不切**。

> **它是什么**（新知识点，先给）：
> - **Lambda（匿名函数）**：`[](int x) { return x > 5; }` —— 方括号是捕获列表、
>   圆括号是参数、花括号是函数体。`[&]` 表示按引用捕获外面所有变量，`[=]` 按值捕获。
>   **昨天你在 JS 里写的箭头函数 `({ text }) => (...)` 就是同一个东西的 JS 版**，
>   C++ 的写法多了一个捕获列表。
> - `<algorithm>` 里的 `std::count_if(begin, end, 谓词)`、`std::sort(begin, end, 比较器)` ——
>   「谓词」就是一个返回 `bool` 的可调用东西，Lambda 正好用来当它。

**练习**：给一段英文短句（自己编，10-20 个词），统计词频，输出按出现次数从高到低排前 3。
用 `std::unordered_map<std::string, int>` 计数（昨天刚闭的那个容器，正好复用）+ Lambda 做比较器。

**做完答一问**：排序时你把 `unordered_map` 的内容倒进了别的容器（`vector` 之类）才排的吧？
**为什么不能直接 `std::sort` 一个 `unordered_map`？**（这一问和昨天「迭代器承诺了什么」是一条线）

---

## 二、下午 17:00-17:50（前端/Electron 45min）

### A. `useState`（25min · 09-28 唯一保留的顺延项）

**这是你在 `frontend-prereq.md` 里自评「不会」的第 3 项。按昨天立的铁律，我先把知识点讲完，
你再写、再跑验证 —— 不让你猜。**

> **知识点 1 · 数组解构**：昨天你写的 `({ text })` 是**对象**解构（按名字取）。
> 数组解构是**按位置**取：`const [a, b] = [10, 20]` → `a` 是 10、`b` 是 20。
> 名字随便起，**位置决定拿到谁**。这和对象解构必须同名，是两套规则。
>
> **知识点 2 · `useState` 是什么**：React 的「状态钩子」。一个组件里写
> `const [count, setCount] = useState(0)`，这一行同时发生三件事：
> - `useState(0)` 告诉 React：这个组件要记一个值，初始是 0
> - 它返回一个**两元素数组**：`[当前值, 改这个值的函数]`
> - 你用数组解构把这两个接出来，习惯上命名成 `x` 和 `setX`
>
> **知识点 3 · 为什么不能直接改**：`count = count + 1` 不行，必须 `setCount(count + 1)`。
> 因为 React 是靠「你调了 set 函数」这个动作才知道要重新渲染的；直接赋值它不知道，界面不会变。
> 引入 `useState` 后，**组件函数会被重新执行一次**（不是改 DOM，是整个函数重跑）——
> 这一点是 React 和你熟的 DuiLib/Win32「直接改控件属性」最根本的区别。
>
> **知识点 4 · 不可变更新（数组/对象状态）**：`arr.push(x)` 改的是原数组，
> React 认不出来。要 `setArr([...arr, x])` —— `...` 是展开运算符，造一个**新数组**。
> 同理对象用 `{...obj, key: v}`。

**你写的练习**（我不给代码）：在 `vite-project/src/App.tsx` 里，
基于你昨天写的 `MessageItem`，做一个最小消息列表：
- 一个输入框 + 一个「发送」按钮
- 点发送，把输入框的内容加进消息数组，列表下面多出一条 `MessageItem`
- 发完清空输入框

会用到两个 `useState`（一个存输入框的字、一个存消息数组）。
输入框怎么受控（`value` + `onChange`）你查一下 React 官方 `State: A Component's Memory` 那一节，
**只看这一节，不要往后翻**（你有一口气看完整本教程的毛病，W1D1 犯过）。

**做完跑两个验证**：
1. `npx tsc --noEmit -p tsconfig.app.json` 零报错（昨天这条你已经会了）
2. 故意把一处 `setMsgs([...msgs, t])` 改成 `msgs.push(t)` + `setMsgs(msgs)`，
   看界面是不是不更新了 —— **这是「不可变更新」这条规则的分辨力实验**：
   如果改法不对界面照样更新，那说明我讲的知识点是错的，你直接抓我。

### B. preload / contextBridge（20min · 本周原排，但**我实查后要改题**）

⚠️ **教练 09-28 23:00 实查 `F:\code\ai-desktop-assistant\preload.js`，本周原排的
「添加 preload.js + 用 contextBridge 暴露一个测试 API」你在 W1D3 就做完了**，现在文件里已有：

```js
const { contextBridge, ipcRenderer } = require('electron/renderer')
contextBridge.exposeInMainWorld('electronAPI', {
  openFile: () => ipcRenderer.invoke('file:pick'),
  getCurrentData: () => ipcRenderer.invoke('getCurrentData'),
  helloName : (nameString) => ipcRenderer.invoke('helloName', nameString)
})
```

原题对你已经没有分辨力了。**按不缩水的规矩，题目升级不是删掉**，改成对着这 7 行做**安全审计**
（正好接你昨天刚升 L2 的三层链，也正好是你部门的活）：

1. 这三个 API 里，`helloName(nameString)` 接收渲染进程传来的字符串。
   **如果渲染进程被 XSS 了，攻击者能用这个接口做什么？** 取决于主进程那边 `helloName` 怎么实现的 ——
   自己去 `main.js` 看那个 `ipcMain.handle('helloName', ...)`，然后回答。
2. 假如我把这行加进去：`nodeRequire: (m) => require(m)` —— 三层链的哪一层被废掉了？为什么？
   （这一问是你昨天整链口述里第三层「contextBridge 写错了」的具体实例）
3. `exposeInMainWorld` 暴露的是**函数**而不是 `ipcRenderer` 本身。
   **如果直接 `exposeInMainWorld('ipc', ipcRenderer)` 会怎样？** 官方安全文档明确禁止这么写，
   自己找出禁止的理由。

---

## 三、段末 15min · q-framework 对照轨（第二格）

昨天第一格「为什么用 GN 不用 CMake」你自己看出来了（「因为 base 是直接用 Chromium 的 base」）。
今天第二格：**双后端全景**。

只读 `E:\code\q-framework\webview\webview.h`（约 70 行，纯虚基类），画出接口全貌，然后说清两件事：

1. `Create()` 为什么是 `static`？（这一问是 C++ 的，不是架构的 —— 想想调用它的时候
   还有没有对象存在）
2. `Delegate` 那一套是干什么的？它解决的问题，Electron 里对应的是什么机制？

---

## 四、记录（15min）

`daily/history/2026-09-29.md`，五栏：完成、掌握（闭卷自答·你自己的话）、
未掌握/卡壳、证据、明日计划。

🔴 **昨天的记录文件是我 23:00 替你补的，这是 09-16 之后第五次。**
自答栏我只能摘你会话里的原话，摘得再准也不是你回头写的那一遍 —— 那一遍才是复习。今天自己写。

---

## 五、明天（09-30 周三）预告 · 🔴 节前最后一天有硬任务

**「假期后第一件事」清单必须写出来** —— 09-24 那次已经落空过一回。
10-01~10-07 停训 7 天，10-08 回来时你会忘掉相当一部分。清单要具体到
「打开哪个文件、跑哪条命令、答哪三问」，不是「复习一下 C++」这种废话。

另：10-08 回来第一个上午整段用于间隔复习（`docs/calendar-holidays.md` 4.2 已定），
**C++ 的 7 天复测也在那天**（原定 10-05 撞停训）。
