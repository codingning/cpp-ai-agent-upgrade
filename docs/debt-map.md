# W1-W2 欠账清单
## 说明
### 本文件是教练批改产出，非宁鑫洋自己的知识索引
- 清掉一条就从这里删掉，搬进 cpp-concept-map.md
- 更新日：2026-09-22
## 🔴 方法论（最高优先级，比任何知识点都重要）
### 动手前先写「我认为 X 由 ___ 决定」
- 09-20 起替代原「运行前先写预测」（原版 6 次未执行）
- 改版理由（本人 09-20 提出）：不是不会设计实验，是知识不足以判断
  「这个实验能不能验证我的要求」。写不出这句 = 该查文档，不是该跑实验，不罚
- ✅ 09-20 首次执行：day7_debt_clear.cpp 第 2 行写了预测，且实验推翻预测后回头改了第 3 行
### 实验要有分辨力
- 09-18 连犯两次，09-19 再犯一次
- 判据：如果两种假设都能产生你看到的结果，这个实验就是白做
- ✅ 09-20 本人自行绕过一次：发现 static_assert 对「=default 是否抑制移动」无分辨力
  （两侧都为真，因 const& 能绑右值），改用带打印的实例化才分开
- ✅ **09-22 本人第二次自行绕过**：教练问「搜到 `createElement` 能否证明 JSX 被转译成它」，
  本人答**「不能证明，我也不确定」**。实测佐证：`createElement` 29 次里绝大部分是 React 库
  内部自用，与是否写 JSX 无关；另有 `jsxs` 18 次才是真产物 → 两种假设都会「搜得到」，无分辨力
- **09-22 新增第二问（同日教练翻车衍生）**：不只问「两种假设会否产生同样结果」，
  还要问**「我这条命令/探针测的到底是什么量」**。
  当日实例：同一问题 `grep -c` 得 3（匹配**行数**）、`grep -o|wc -l` 得 29（**出现次数**），
  两者都对但回答的是不同问题；教练出题给 `-c`、自验用 `-o`，再拿自己的数字判本人错
### 不许拖延可即时完成的小项（教练 09-20 被本人当面指出）
- 教练对一个 3 分钟的实验说「挂到 W3」，与 Vector<T> 拖两周同一个动作
- 规矩：能当场做完的不许排进下周
- ✅ 09-21 本人再次执行此规矩：提出 MyVector 三刀合并为一天做完，教练核对后采纳
### 排计划前必须核 debt-map / history，不许照过期文件和记忆说话（09-21 教练第 5 次犯）
- 09-21 教练依 `week-03.md` 第 138 行过期条目断言「noexcept→扩容退化实验尚未做」，
  实际 09-20 day7 实验4 已完成并写在本文件第 57 行；同时主张「Rule of 5 要隔一天写」，
  但 09-20 day7 已把整张表逐条实验过，间隔检索价值已用掉
- 两处均由本人当场指出。连带发现 `week-03.md`「W2 遗留欠账」6 条里 4 条早已清却一直挂着
- 规矩：**本文件是欠账唯一权威源**。计划文件与本文件冲突时以本文件为准，并当场改计划文件
## C++ 概念欠账
### 🔴 MyVector 隐含要求 T 默认可构造 → placement new（09-22 新增 · 本人自答暴露）
- ✅ **09-22 下午已清**：本人自行搜索 placement new 后改完三处构造 + 异常安全回滚，教练实跑全通过
- `new T[4]` 会调 T 的默认构造 → 本人 MyVector 装不了无默认构造的类型；std::vector 不要求
- 改造内容：`::operator new` 只要内存 + `::new (addr) T(...)` 就地构造 + 析构显式 `~T()` 再 `::operator delete`
- **本人自建 `NO_PLACEMENT_NEW` 编译期对照实验**（D11 加 `std::string str` 成员并在 `operator=` 打印它）：
  - 开 placement new：`D11 constructor → copy constructor → destructor`，全程无 copy assignment，退出码 0
  - 关（走赋值）：打印 str 吐乱码 → **段错误，退出码 139**，崩前把整个进程环境变量吐到 stdout
  - **分辨力来自 `std::string` 成员**：两种假设输出完全不同。手法本人自想
- 扩容异常安全（教练追问后本人独立改对）：`count` 提到 try 外、catch 只清 `[0,count)`、
  `throw;` 原样重抛、销毁旧元素与改 `data_/cap_` 全挪到 try 之后、`move_if_noexcept` 加回
  - 教练 Boom 探针实跑（第 3 次拷贝构造抛）：`size/cap 4→4 未变`、`存活对象 4→4 无泄漏`、
    `异常后继续 push 成功 size=5 cap=8` → **强异常保证成立**
### ⚪ 新挂（09-22，不急）
- 手动 try/catch 回滚 vs RAII 守卫（昨天用 unique_ptr 做过同一件事，零 catch）：
  同为异常安全，两种写法差在哪，为什么标准库基本都选后者
### ⚪ 09-21 本人自评超纲、明日续做（2 项）
- 元素级计数 vs 类级打印，为什么后者无分辨力
- `push_back` 用 swap 改造
### 🟡 依赖间接包含（09-21）
- 用 `std::unique_ptr` 未 `#include <memory>`，靠 `<iostream>` 间接带入。已提醒，**是否补上待核**
### 🎉 W1-W2 遗留 C++ 欠账已全部清空（2026-09-20，零 ❓）
- 知识图 `cpp-concept-map.md` 上 5 个 ❓ 全部拿到自有实验证据
- 上列 09-21 新增各条为当日新产生，非历史遗留
## Electron / Chromium 欠账
### 🔴 前端技术栈前置断层（09-21 本人提出，教练核实成立 —— 计划缺陷非本人问题）
- week-01 第 78 行、week-02 第 133 行均写「不要 React」，week-03 第 34-36 行直接要求「用 React 重写」，**中间零节课**
- 同时 week-01 第 50 行「初始化 Electron + TypeScript 项目结构」从未落地（实查 `package.json` 无 TS，全 `.js`），一路挂着未标作废
- 违反本人 09-20 立的硬规矩：记录里没标掌握的一律按没掌握处理，出题不许假设附带知识
- 处置：09-21 下午改为概念课（React 解决什么问题 / JSX 是什么 / 为何需构建工具 / Electron 里引 React 的三点不同），**已完成**
- 本人立场（09-21）：不急于让 Chat UI 像产品，要的是掌握框架与概念；AI 时代手写基础 HTML 无意义
- ✅ **09-22 已建 `docs/frontend-prereq.md`**（结构教练起 / 内容本人填）。6 节 28 项 + 附表。
  「计划假设你会」列教练已从 week-01~04 原文实抓填完；**「你实际会」列全空待本人填**
  （四档：独立能做 / 看文档能做 / 听过不会用 / 没听过）；每节末一个自问待本人写字作答
### ~~🟡 React / JSX / Vite 概念课闭卷未答~~ ✅ 09-22 已出已批（概念课标准，不挂 L 级）
- 五问结果：Q1 对、**Q3 独立答对**（Vite 不打包直接喂模块 vs 传统全打 bundle 再启动，答得比题目准）、
  Q2 大意对缺细节、**Q4 答不出**、Q5 结论对但理由不成立
- 出处已实抓：Vite 官方中文文档 `cn.vitejs.dev/guide/why.html`
### 🔴 沙箱掉了之后攻击者站在哪个进程（09-22 复测答错，重新挂账）
- 本人答「拿到主进程的权限」。**错**：拿到的是**渲染进程那个 OS 进程**的权限
- 渲染进程与主进程是两个独立 OS 进程，打穿一个不等于拿到另一个；想让主进程干活仍须发 IPC
- 09-20 本人自核文档时这条答对过 → 今天记成了「掉了很严重」，丢了「严重在哪个进程上」
### 🟡 contextIsolation 掉了：共享 window 的主动攻击面（09-22 答对但不完整）
- 本人只答「拿到 preload 的权限」（被动）
- 缺：两者共享同一个 `window`，攻击者可改 `Array.prototype.push` 等内置方法，
  **等高权限代码来调用他** —— 这句 09-20 本人自己写过，今天没写出来
### 🟡 「开关独立」与「防护串联」为何同时成立（09-22 提示后答对，非独立）
- 本人两次尝试均为同义反复（「不同层级/共同防护」「防护的两件不同的事」）
- 正解：二者描述**同一套防护的两个不同视角**——「独立」看**配置**（两开关状态互不影响），
  「串联」看**攻击路径**（门的顺序）。`nodeIntegration:true` 时门还立着，但不在攻击者路上
- ⚠️ 本人在教练的场景题里其实已把三点全答中（能 require / 它拦的是 preload 权限 / 攻击者不需要它），
  **缺的只是收成结论那一步**，不是缺理解
### 🔴 构建时 vs 运行时的分界（09-22 Q5 理由不成立，新挂）
- 本人答「React 只是一个库，不能自己把 JSX 转成 JS」——**是不是库与能否转译无关**
- 正解：JSX 转译是**构建时**的事（`vite build` 那一刻，在开发机上）；
  React 是**运行时**的库，它拿到的已是转译完的产物，压根没机会看到 JSX
### 🔴 `vite build` 产物如何进 Electron（09-22 Q4 答不出，教练所给）
- 链条：JSX → Vite 转译+打包 → `dist/` 里普通 HTML + 普通 JS → 渲染进程像加载任何网页一样加载它
- **渲染进程完全不知道 React 和 JSX 存在**
- ⏳ `win.loadFile('dist/index.html')` 这条本人未实跑验证
### 🔴 `file://` + `type="module"` → CORS 拦截（09-22 本人实验发现，**教练完全不知道的一层**）
- 本人实测两版对照（改 `base` 前后各双击一次 `dist/index.html`）：**两版都白屏**
- 真主因：script 带 `type="module"`，**ES 模块受 CORS 约束**，而 `file://` 不在浏览器
  协议白名单（chrome / chrome-extension / chrome-untrusted / data / http / https / isolated-app）
- 原始报错：`Access to script at 'file:///...' from origin 'null' has been blocked by CORS policy`
- **路径问题与 CORS 问题是两个独立的坑**，教练原断言只覆盖了第一个
- ⏳ 待查：Electron `loadFile` 是否走同一条路？教练判断「不能证明」但明确标注为**推测**
  （Electron 对 `file://` 是否特殊处理，双方均不知）→ 必须在 Electron 里实跑才能结账
### ~~🔴 Vite `base: './'` 与 Electron `loadFile`~~ ⚠️ 09-22 本人实测：教练对一半
- 实测 `dist/index.html` 里是 `<script type="module" crossorigin src="/assets/index-BRDr3nmD.js">`
  —— 开头 `/` 是**绝对路径**（本人误认为相对路径，观察失误；其下半问推理链本身无错）
- ✅ **路径部分成立**：`/assets/` 确被解析成磁盘根 `F:/assets/`（`GET file:///F:/favicon.svg
  net::ERR_FILE_NOT_FOUND` 是干净佐证）；加 `base: './'` 后 src 变 `./assets/index-DBszTkjK.js`，
  请求路径修正为 `file:///F:/code/vite_react/vite-project/dist/assets/...`
- ❌ **「加了 base 就不白屏」不成立**，两版都白屏 → 见上一条 CORS
- 本人自行完成配置修改（教练只给定位「base 是 defineConfig 顶层属性，跟 plugins 平级」，未给代码）
### Utility 和 Renderer 的区别
- 09-19 记录里空缺，09-20 块 2 题 7 仍空——连续两次落地
- ⚠️ 教练 09-19 曾在此翻车（给了一篇不含答案的 mojo_and_services.md）
- 已确认覆盖的一句（Electron tutorial/sandbox）：除主进程外多数进程都在沙箱内，
  包括 renderer，也包括 utility（audio/GPU/network service 属此类）
  —— 这句能说明 Utility 装什么，回答不了「区别是什么」
- 状态：❌ 出处待教练实读 process_model_and_site_isolation.md / sandbox.md 后确认
### ~~A4 sandbox → contextIsolation → preload 三层链~~ ✅ 09-20 结账
- 本人自核 Electron 官方 `tutorial/sandbox` + `tutorial/context-isolation` + `tutorial/security` 后重答通过
- 三层递进（不开这层攻击者能多拿到什么）：
  1. 沙箱掉 → 拿到渲染进程那个 OS 进程的全部权限（沙箱内只能自由用 CPU 和内存，其余靠 IPC 委托）
  2. 沙箱在、contextIsolation 掉 → 拿不到 OS，但拿到 **preload 那一层的权限**；
     且两者共享同一个 window，攻击者可改 `Array.prototype.push` 等内置方法，**等高权限代码来调用他**
  3. 两层都在、contextBridge 写错 → 仍漏。官方反例 `exposeInMainWorld('myAPI',{send: ipcRenderer.send})`
     等于让任意网站发任意 IPC；正确做法是一个 IPC 消息包一个方法
- **Q11/Q12 矛盾解法**：两句都对，不矛盾。开关是独立的（nodeIntegration 不影响 contextIsolation），
  但防护是**串联**的——第一层塌了后两层拦不住从第一层进来的人。
  官方原话：关 Node 集成可防止 XSS 升级成 RCE；开着时页面脚本直接有 `require('child_process')`，
  攻击者根本不需要偷 preload 的 API
## 🔴 前端前置断层（09-23 新增，主线必补非扩展项）

> 来源：`docs/frontend-prereq.md` 本人 09-23 亲填 28 项 + 教练当日写结论区 6.1/6.2。
> **这是整个 Electron/React 主线的地基**，不补则后续每节课都会卡在语法而非卡在概念。

### ❌ JS 四项语法（本人自评「不会」）
- 箭头函数 `() => {}`、解构赋值 `const {a,b}=obj`、展开运算符 `...`、`async/await`+Promise
- **本人 09-23 原话（关键证据）**：「用过箭头函数、解构、async/await，
  **但是 Electron 主进程是我从教程里拷贝的，所以并不是全部了解**」
- **教练 09-22 出错**：据「他代码里出现过这些语法」推断「他会」→ 推断作废。
  教训定名：**用过 ≠ 会写**，拷贝来的代码里出现某语法不构成掌握证据
- 补法：**不单独开语法课**，寄生在 React 课里（箭头函数+解构挂组件/props，
  数组解构+展开挂 useState，async/await 挂 W4 的 IPC 异步）
- 排期：W3D4（09-24）起，见 `plan/weekly/week-03.md` 周四/周五重排段

### ❌ React 四件套（全零基础，本人点名前三「连大概想干什么都说不出」）
- 组件/props → W3D4 ｜ useState → W3D5 ｜ useEffect → W3 周六 ｜ 构建时vs运行时 → 09-23 下午段 B
- 状态：`useReducer` **顺延 W6**（原排 W4 周四，比 useState 更抽象，已改为 useState）

### ❌ npm 工具链（三项均「只知道是什么，没跑过」）
- `npm init` / `package.json` / `npm run X` —— 排 W3D4 15min，必须亲手跑
- 验收：闭卷答「`npm run hello` 时 npm 做了什么，它怎么知道 hello 是什么」

### 🚫 已正式作废（非顺延）
- **TypeScript**：week-01 第 50 行排过，09-21 已核实从未落地（`package.json` 无 TS 依赖）。
  **09-23 正式标 W1-W6 作废**，理由：JS 本体四项都没过关，加 TS 是负担不是助力。W7 后视情况重排
- **原生 DOM / `addEventListener` / HTML+`<script>`**：本人三项全「不会」，
  但**不在 React 主线路径上**（React 用 `onClick`，不需要先会 `addEventListener`），
  且本人 09-21 立场「AI 时代手写 DOM 无意义」成立。**不排补课**，
  只在 React 事件课上标一行「原生对应物是什么」

### ✅ 已确认不是断层（有本人闭卷证据，不重复排课）
- Vite 的作用、什么是打包（09-22 Q1/Q3 独立答对）
- 开发者工具会看（工作中与前端对接用过）｜ CSS 基本布局（DuiLib XML 经验可迁移）
- 「React 组件不能直接 `require('fs')`」（09-23 本人答对，理由「渲染进程沙箱化」成立）

## 产出欠账
### 🆕 q-framework 吃透（09-21 本人提出，教练采纳）—— 简历主项目
- 详见 `docs/q-framework-map.md`。本人真实职责：主 UI / 照片压缩 / Shell 扩展，Lynx UI 少量
- 提交实查：1172 commits，本人 `ningxinyang` 56 次；核心开发者三四人，模块划分清晰
- **教练当日出错**：曾以「没写过就讲不清」为由反对本人吃透全项目，本人以
  「项目不大、三四人做、水平相当、只是模块不同」驳回，**教练核 git log 后收回**
- 唯一硬规矩：**「我写的」和「我吃透的」要能分开说**，不限制吃透范围与简历写法
- ⚠️ 待查：`Cheng Zhao`（Electron 创造者）在本仓库有 202 次提交 —— 若 `webview/` 与 Electron
  `BrowserWindow` 同源，则对照学习升级为**同源对照**
### 博客第 1 篇正文
- 大纲 09-19 建、09-20 改到及格；正文计划第 6 周发布
- 状态：⚠️ 大纲完成，正文未开始
### W1 周复盘三处空白
- 2026-09-13-weekly.md 第 13-14 行（达成率/缺口原因）、第 191 行（下周调整整节）
- 状态：❌ 仍空
## 已清（保留 7 天作为对照，之后删）
### ✅ Q3 均摊推导（09-22 闭卷独立答对）
- 本人自推：S=4+8+...+2^(k-1)=2^k-4；最后一次扩容触发条件 cap/2+1<=n → cap<=2n-2 → cap<2n
- 教练实跑补边界（n=1..100 探针）：n=1、n=2 时 cap 恒为初始 4，一次未扩，cap<=2n-2 不成立；
  n>=3 全成立，n=5 时 cap=8 与 2n-2=8 相等 → 该界是紧的。**答案须写明「至少扩容过一次」前提**
### ✅ Q8 move_if_noexcept 判据（09-22 闭卷独立答对，本人答「没得选」）
- 完整判据：移动构造 noexcept **或** 类型不可拷贝 → 移动；否则拷贝
### ✅ Q9 copy-and-swap 异常安全（09-22 提示后答对，一个反问即通）
- 本人原话：手写拷贝赋值先 delete 再 new，new 抛 bad_alloc 时旧资源已毁；
  copy-and-swap 的拷贝/移动构造发生在进函数体之前，失败时 `*this` 未被动过
- 定名：**强异常保证**（可能抛的动作全部发生在碰 `*this` 之前，非「出错能回滚」）
- 另两问本人 09-21 已对：swap 三个成员是 T* 与 size_t，基本类型赋值不抛；
  noexcept 函数真抛 → std::terminate，栈展开前终止，外层 try/catch 接不住
### ✅ Q10 按值传参一函数两用（09-22 本人自建 test4 实验，独立答对，「ai说」已划掉）
- **教练当日出错**：09-21/09-22 两次引用「证据 9 路径 2/4」当 Q10 证据，但本人 my_vector.cpp 的 test3 里
  `MyVector<D11> e = a;` 与 `d = std::move(a);` 是**初始化走构造**，真赋值只有 `c=std::move(b)` 一条，
  单条无分辨力。**本人当场指出，教练核后收回**（引用了不在本人文件里的实验）
- 本人自补 test4（b=a; b=std::move(a);），教练实跑确认输出：
  `b = a` → MyVector copy constructor + copy assignment；
  `b = std::move(a)` → MyVector move constructor + copy assignment
- 结论：形参 other 在**调用点**被构造，源是左值用拷贝构造填、右值用移动构造填，函数体内部不知情
### ✅ 左值/右值值类别（09-20 day7_value_category.cpp：五条重载探针实测，有名字的右值引用是左值，预测命中）
### ✅ 析构 protected 的「为什么」（**本条系教练误标**：09-17 history 第 55-57 行本人已答对，
  09-18 debt-map 未核原始记录照抄为「未补」，09-20 本人指出后销账。教练第 4 次「不核来源照记忆排」）
### ✅ `= default` vs 什么都不写（09-20 day7 实验1：D1 走拷贝 / D2 走移动，证明 =default 算用户声明）
### ✅ 拷贝赋值是否随拷贝构造一起 delete（09-20 day7 实验2：D10 成员逼出真实调用链，未跟着死）
### ✅ move 退化三条的最小例子（09-20 day7 实验3：D5 const / D6 无移动构造）
### ✅ noexcept → vector 扩容退化（09-20 day7 实验4：D7 走拷贝 / D8 走移动，本人自有实验证据）
### ✅ 移动构造反向抑制拷贝（09-20 day7 test3 #ifdef 对照：exit 0 vs exit 2，两条 C2280 + 编译器 note）
### ✅ Chromium 进程模型图（09-19 drawio，09-20 cell48/49 重填）
### ✅ Chat UI v0（09-19 index.html）
### ✅ 博客大纲 + blog-drafts/（09-19 建，09-20 改到及格）
### ✅ W2 周复盘 + 口头复述自评栏（09-20 完成，九题自答）
### ✅ Rule of 0/3/5 索引缺失（09-17 闭卷重答通过）
### ✅ 异常路径 RAII（day4_exception_raii.cpp）
### ✅ MyUniquePtr 单元测试（day4_uniqueptr_test.cpp）
### ✅ move-from 状态 + SSO 原因
### ✅ preload + contextIsolation（基础层，A4 整链仍欠）
### ✅ 语境转换（09-18 讲解 + 自己画进图里）
### ✅ Menu 接线 + 菜单份数（09-18 实验验证）
