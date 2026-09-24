# 今日任务 · 2026-09-24（周四）· W3D4 · 1.5h 保底

> 🔴 **本周最后一个训练日。** 明天 09-25 是中秋假期第一天，停三天（09-25~09-27）。
> 依据 `docs/calendar-holidays.md`（国办发明电〔2025〕7 号，教练 09-23 实查）。
>
> 昨天 160 分钟，三项欠账全清：三层链重考**两问独立答对**、构建时/运行时**三问全对**、
> `loadFile` 白屏挂了一整天的实验**结清**。
> **Chromium/Electron 今天口述一次整链就提级 L2。**

---

## 元规则（第 10 次要求，昨天未见书面执行）

动手前先写一句：**「我认为 X 由 ___ 决定」**。写不出来说明该查文档，不是该跑实验 —— 不罚。

昨天你在 `loadFile` 那条上栽了一次：说「无 base 会白屏」的时候**没看控制台**。
CORS 和 404 都能产生白屏 —— 那句结论当时是猜的，去看了控制台才变成证据。
**这是第五次同类。** 今天 npm 和 React 两段里都有「跑完看什么」的环节，别再跳。

---

## 上午 10:30-11:10（40min）· C++ 清欠

### A. 🔴 三问闭卷（20min）· 昨天 21:31 布置未答

这三问是你上午那两个探针**本来要回答的问题**，探针跑完了、问题还空着。**闭卷，不许翻记录。**

1. `map` 慢，什么场景你会**故意**选它？
   ——「有序」这个答案不够。**要说出 q-framework 里哪一种数据非有序不可**，
   或者哪一种 key 根本进不了 `unordered_map`。（昨天你说「一时想不起来，
   可能还需要翻代码查找」——**今天允许翻代码，不允许答不出**。）
2. `unordered_map` 触发 rehash 之后，**迭代器**和**元素地址**是不是同一回事？
   昨天探针里 `bucket_count 8 → 512` 真 rehash 了，但 `key=2` 的地址没变。
   **这说明节点搬了没搬？那失效的到底是什么东西？**
3. vector 扩容让迭代器失效，标准为什么写「**可能**」而不是「**一定**」？

### B. 🟡 `lower_bound` 闭卷复述（10min）

昨天我给了定义，你**没复述过**。按 09-20 你自己立的规矩：
**记录里没标明你已掌握的，一律按没掌握处理。** 用自己的话说一遍，两问：

- `lower_bound(k)` 和 `upper_bound(k)` 分别返回什么？`k` 不存在时呢？
- 「遍历有序」和「动态范围查询」为什么是两件不同的事？（各举一个只需要其中一个的场景）

### C. ⚠️ 顺带一条订正（10min）

昨天 `key_probe.cpp` 默认编译打出 `__cplusplus = 199711` —— 那是 **MSVC 不加
`/Zc:__cplusplus` 时的假值**，不代表在用 C++98（加开关后是 201402）。
**如果你据那个 199711 推过任何结论，作废重推。**

> **它是什么**：`/Zc:__cplusplus` 是 MSVC 的一个编译开关。不加时 `__cplusplus` 这个宏
> 永远返回 `199711L`（C++98 的值），这是 MSVC 为了兼容老代码留的历史包袱。
> **含义**：以后凡是想靠 `__cplusplus` 判断标准版本，在 MSVC 上都要先确认这个开关。

---

## 下午 17:00-17:50（50min）· 前端断层第一课

> 这两段是昨天你填完 `docs/frontend-prereq.md` 28 项后重排出来的，
> 前提是「**你会 JS、缺的是 React**」被你自己推翻了 —— JS 四项语法你自评全「不会」。
> 关键那句是你说的：「Electron 主进程是我从教程里拷贝的，所以并不是全部了解」
> → **用过 ≠ 会写。**

### A. 🔴 npm 工具链亲手跑一遍（15min）· 断层 D

三项全是你自评「只知道是什么，没跑过」。**这一段的目的是亲手跑，不是理解。**

1. 在 `F:\code\` 下新建一个空目录，`npm init -y`
2. 打开生成的 `package.json`，**逐行看里面有什么**
3. 手动加一条 script：`"hello": "node -e \"console.log(1+1)\""`
4. 跑 `npm run hello`

**闭卷答**：`npm run hello` 的时候，npm 到底做了什么？它**怎么知道** `hello` 是什么？

> **它是什么**：`package.json` = 这个 JS 项目的说明书（依赖列表 + 可执行命令列表）。
> `npm run X` = 去 `scripts` 字段里找名为 X 的那条命令并执行它。
> `npm init -y` = 生成一份默认的 `package.json`，`-y` 是全部问题都答「是」。

### B. 🔴 React 组件 + props（30min）· 断层 C，寄生补两条 JS 语法

在昨天那个 `F:\code\vite_react\vite-project` 里动手（已经能跑起来了，别新建工程）。

**目标**：写一个 `MessageItem` 组件，接收一个 `text` 参数并显示出来；
在 `App.tsx` 里用**三次**，传三个不同的字符串。

**两版都要写**（这是红线内的骨架，不是实现 —— 函数体你自己填）：

```
function MessageItem(props) { ... }         // 第一版：用 props.text
const MessageItem = ({ text }) => ( ... )   // 第二版：箭头函数 + 解构
```

第二版就是你自评「不会」的那两条语法的**第一次实战**。

> **它是什么**：
> **组件** = 一个返回 JSX 的函数，**函数名首字母必须大写**（小写会被当成 HTML 标签）。
> **props** = 父组件传给子组件的参数，在子组件里是一个**对象**，**只读，不能改**。
> **箭头函数** `const f = (x) => y` 大致等价于 `function f(x) { return y; }`。
> **解构** `({ text })` = 从传进来的那个对象里直接把 `text` 字段取出来当参数名用。

**先写预测再跑**：我认为 props 改成 `({ text })` 之后，函数体里要写 ___ 而不是 ___。

---

## 🔴 收工前必做三件（今天不做就跨中秋三天）

### 1. Chromium/Electron 提级判定 —— 整链口述一次

昨天两问都独立答对了，但 L2 的口径是「**能自己讲清三层链**」。
**今天从头到尾讲一遍**（sandbox → contextIsolation → contextBridge，
每层「掉了会怎样」+「为什么开关独立但防护串联」），过了就 L1+ → **L2**。

### 2. 三仓代码全部推完

- `F:\code\cpp-practice` —— `week-03/iter_probe.cpp`、`key_probe.cpp` 未提交
  ⚠️ **这两个是我写的探针，不是你的练习代码**，commit message 里要标明来源，别混进你的产出
- `F:\code\vite_react\vite-project` —— **这个目录根本不是 git 仓库**
  （我昨天查过：`git log` 报 `fatal: not a git repository`）。
  昨天你写的 `main.cjs`、`scripts/electron-smoke.cjs` **全无版本记录**。
  今天先 `git init`，注意 `.gitignore` 要挡掉 `node_modules/` 和 `dist/`
- `F:\code\ai-desktop-assistant` —— 今天动了就推

### 3. 「假期后第一件事」清单

写进今天的 `daily/history/2026-09-24.md` 最后一栏。停三天后你会掉的是**只学过一次的东西**
（组件/props、npm、`lower_bound`），不是练了三遍的（Rule of 5、placement new）。
**清单只写「回来第一个小时干什么」，不要写成一份复习计划。**

---

## 不做（写明，不是切掉）

- **`useState`** —— 原排 09-25（周五），中秋停训 → **顺延 09-28（周一）**，不作废
- **周六 4h 深度档**（含 LRU 门禁）—— 中秋 → **顺延 10-17**
- **周日 2h 复盘** —— 中秋 → **顺延 09-30（周三）**
- **q-framework D1（IOCP 异步 IPC）** —— 已正式排到 **W4D1（09-28）起**，有完整四层深挖链
- **扩展项**（有余力才上，做了必须写进记录）：
  ①元素级计数 vs 类级打印为何后者无分辨力
  ②`push_back` 用 swap 改造
  ③手动 try/catch 回滚 vs RAII 守卫

---

## 📌 我欠你的一件事（今天不给就是我欠着）

**Utility vs Renderer 的区别 —— 连续第五次落地。**

这条一直没布置给你，不是你没做，是**我欠你一次文档实读**。
我 09-23 承诺「本周内给出处」，**09-24 09:2x 已实抓，账结了**。

⚠️ 09-19 我曾在这条上翻车（给了 `mojo_and_services.md`，那里根本没这内容）。
这次的出处是我真抓到原文、并把句子抄在下面的，**两处都可核**：

**出处 1 · `chromium.org` 设计文档 `Multi-process Architecture` → 末节 `Additional Process Types`**
> 原文：`Chromium has split out a number of other components into separate processes as well,`
> `sometimes in platform-specific ways. For example, it now has a separate GPU process,`
> `network service, and storage service. Sandboxed utility processes can also be used for`
> `small or risky tasks, as one way to satisfy the Rule of Two for security.`

**出处 2 · Chromium 仓库 `docs/servicification.md` → `Hooking Up the Service Implementation`**
> 原文：`For out-of-process service launching, Content uses its "utility" process type.`
> 注册点：`//content/utility/services.cc`、`//chrome/utility/services.cc`；
> 拉起方式：`ServiceProcessHost::Launch`。

**我只给出处，不给答案。** 这两段 + 你 09-19 已画的四进程图，够你自己读出区别了。
闭卷两问（今天不做就顺延 09-28，不作废）：
1. Renderer 和 Utility 都在沙箱里、都不可能随便碰文件系统 —— 那**区别到底在哪一层**？
   （提示方向：这两种进程里跑的**代码是谁写的**？不用回答提示，回答问题。）
2. 网络栈（network service）既然可以进 Utility，**为什么不干脆放进 Renderer**？
   出处 1 里「Rule of Two」那半句是线索，它是什么你可以问我。

> **它是什么 · Rule of 2**：Chromium 的安全硬规矩——「处理不可信输入」「用不安全语言（C/C++）写」
> 「不在沙箱里」三件事，**最多只能同时满足两件**。三件全中就必须拆进程或换语言。
> 这条我只给定义，它和上面两问的关系你自己接。

---

## 收工（15min 记录）

`daily/history/2026-09-24.md`，五栏照旧：完成 / 掌握（闭卷自答）/ 未掌握卡壳 / 证据 / 明日计划。
**第四栏「明日计划」今天换成「假期后第一件事」清单。**

昨天那份记录是我 23:00 补写的（09-16 后第三次）。今天你自己写。
