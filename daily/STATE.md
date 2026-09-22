# 训练续接状态

这是新会话和新环境恢复训练时的首要入口。任何代理开始工作前依次读取：

1. `README.md`
2. `plan/STRATEGY-2026-09-07.md`（战略说明，理解方向）
3. `plan/roadmap-24-weeks.md`（总路线）
4. `plan/weekly/week-01.md`（当周详细计划）
5. `plan/baseline.md`（能力基线）
6. `plan/learning-loop.md`（学习方法论）
7. `plan/competency-matrix.md`（能力矩阵）
8. `daily/STATE.md`（本文件）
9. `daily/current.md`（当日任务）
10. 最近 3 份 `daily/history/*.md`

## 学习时段（工作日固定）

- **上午 10:30-11:10（40min）**
- **下午 17:00-17:50（50min）**
- 合计工作日 1.5h/天，周六 4h 深度，周日 2h 复盘
- **前提**：部门 AI 探索任务有等待 AI 输出的空档，学习时段是结构性摸鱼窗口（不是压榨下班时间），这是 24 周计划可持续的核心假设——如果这个前提变化（换任务/被调岗），整个计划要重排

## 当前状态

- **战略版本**：2026-09-07 版（Electron/Chromium + AI 集成方向，替代原 C++ AI 推理基础设施方向）
- **当前阶段**：阶段一 · 基础重建 · **Week 03 进行中**
- **Week 03 起止**：2026-09-21（周一）~ 2026-09-27（周日）
- **本周主题**：STL 容器（vector 均摊/迭代器失效）+ MyVector 实现 + 前端技术栈补课
- **当前日期**：2026-09-22（周二）= **W3D2 · 七天复测日**
- **今日状态（09-22，上午段完成）**：**C++ L2 复测通过**。上午 10:33-11:0x 闭卷四题，
  **Q3 / Q8 / Q10 独立答对，Q9 提示后答对（只给一个反问即通）**，四道里三道独立。
  ①**Q3 均摊推导**本人自推（S=2^k-4；cap_/2+1<=n → cap_<=2n-2 < 2n），推翻 09-21「抄答案」判定。
  教练实跑 n=1..100 探针补边界：n=1、n=2 时一次未扩容，cap<=2n-2 不成立 → 结论须写明
  「至少扩容过一次」前提；n=5 时 cap=8 与 2n-2=8 取等，界是紧的。
  ②**Q8** 本人答「没得选」，即命中 09-21 漏掉的那条（类型不可拷贝时仍移动）。
  ③**Q9 异常安全**本人原话：手写拷贝赋值先 delete 再 new，new 抛时旧资源已毁；
  copy-and-swap 的构造发生在进函数体之前，失败时 `*this` 未动 → **强异常保证**已定名。
  另两问 09-21 已对（swap 换 T*/size_t 不抛；noexcept 真抛 → std::terminate，栈展开前终止）。
  ④**Q10 本人自建 test4 实验独立答对，「ai说」已划掉**——且当场指出教练引用错误（见下）。
  ⑤**本人自答暴露新缺口并自己答对三小问**：`new T[4]` 会调 T 默认构造 → 本人 MyVector
  要求 T 默认可构造、std::vector 不要求；所以 `data_[size_]=v` 只能是赋值。
  → 新增欠账「申请内存 ≠ 构造对象 / placement new」，标**主线必补**非扩展。
- **📌 教练 09-22 出错 1 次**（本人当场指出，教练核后收回）：
  **Q10 证据引用错**——09-21 与 09-22 两次拿「证据 9 路径 2/4」当 Q10 的证据，
  但本人 `my_vector.cpp` 的 test3 里 `MyVector<D11> e = a;` 与 `d = std::move(a);`
  是**初始化走构造**，真正的赋值只有 `c = std::move(b)` 一条，单条无分辨力。
  本人原话：「Q10不对吧，路径2和路径4是构造啊，看不出来到底是走的移动operator= 还是拷贝operator=」。
  **根因：引用了不在本人当前文件里的实验**（同类老毛病：不核当前来源照记忆说话）。
- **能力等级**：C++ **L2 候选 → ✅ L2 达成**（09-22 七天复测通过：四题三独立一提示后答对，
  均有自有实验或自有推导证据）。Chromium/Electron **L2 候选**——下午 17:00 段复测后定。
- **C++ 侧欠账**：09-21 新增 6 条中 **Q3 / Q8 / Q9 / Q10 四条已于 09-22 上午全清**；
  剩 2 条扩展项（元素级计数为何无分辨力 / push_back 用 swap 改造）+ 🔴 新增 1 条
  （placement new，主线必补）。见 `docs/debt-map.md`
- **今日状态（09-21）**：W3D1 **200 分钟**（10:10-11:30 / 14:10-15:30 / 16:30-17:10），远超 1.5h 保底。
  ①**W3 门禁项 `MyVector<T>` 达成**（拖两周的欠账一次清完）——本人当日主动提出
  「三刀合并为一天做完，不要切三刀」，教练核 debt-map 后采纳。四项齐：可编译可运行 +
  Rule of 5 + 真扩容 + assert 测试。9 组实跑证据见 `daily/history/2026-09-21.md` 第四节。
  ②三个**计划外扩展**全部本人自主完成：`move_if_noexcept`（本人自行搜索补入）、
  RAII 守卫异常安全（强异常保证实测：异常后 size/cap 三成员一个没动，析构 8 次无泄漏）、
  copy-and-swap 三版演进（本人连改三版自己改对，版本三路径2 只 1 次 copy、路径4 走 move）。
  ③**下午 Electron 原任务作废**——本人指出「不知道 React 和 JSX 是什么，npm 只会简单命令，
  根本无法推进」。教练实查确认是**计划缺陷**：week-01 第 78 行、week-02 第 133 行都写
  「不要 React」，week-03 第 34-36 行直接要求 React 重写，中间零节课；且 week-01 第 50 行
  TypeScript 化从未落地（实查 `package.json` 全 `.js`）却一直挂着。改为概念课并完成：
  React 解决什么问题 / JSX 是什么 / 为何需构建工具 / Electron 里引 React 三点不同，
  加本人追问的 Vite 是什么（已实抓 `cn.vitejs.dev/guide/why.html`）、JSX 算不算一门语言。
  ④**本人立场（记录在案）**：不急于让 Chat UI 像产品，要的是掌握框架与概念；
  AI 时代手写基础 HTML 无意义。教练原提的「降级用原生 JS 做交互」方案被本人否决，**否决成立**。
  ⑤**新增简历主项目 `q-framework`**（见下「关键决策」）。
  ⑥记录本人自填，教练批改 **7/10**（扣：Q3 抄答案 -2、Q8 漏一种情况 -0.5、两处状态填错 -0.5；
  亮点：Q7 用自己的话讲透模板为何不能放 .cpp、**Q10 主动标注「ai说，未验证」**）。
  **教练当日自身出错 5 次**，全部记入 history 第五节 + 下方。
- **🆕 关键决策（09-21）· q-framework 作为简历主项目**：
  本人提出把前部门真实项目 `E:\code\q-framework`（Windows 桌面「全能压缩 OmniZip」，
  纯 C++17 + GN/Ninja + Chromium base，**当前可访问可构建**）吃透并写进简历。
  教练最初以「没写过的模块讲不清、会在面试被戳穿」反对，**本人驳回**：
  「项目不大，三四个人做的，他们水平和我差不多，只是分配的模块不同，
  没写过的高含量模块现在吃透，不也变相等于会了吗」。
  教练实查 `git log`（1172 commits：lanshichao 359 / **Cheng Zhao 202** / liyun 130 /
  litao8 92 / xuhuazhi 72 / **ningxinyang 56**）后**收回反对**——核心开发者三四人、
  模块划分清晰，「没写过=讲不清」对这种规模不成立。
  **保留唯一硬规矩：「我写的」和「我吃透的」要能分开说。** 不限制吃透范围与简历写法。
  计划已落 `docs/q-framework-map.md`。⚠️ 重大待查线索：**Cheng Zhao 是 Electron 的创造者**，
  在本仓库有 202 次提交 —— 若 `webview/` 抽象层与 Electron `BrowserWindow` 同源，
  则「Electron ↔ q-framework 对照学习」不是类比而是**同源对照**。
  另已查明：q-framework **不是 Electron**（主 UI 是 DuiLib DirectUI）；
  `ui/lynx_ui/` 的 **Lynx 不是 React**（字节开源的 C++ 跨平台 UI 框架），
  但上层 ReactLynx 用 React 语法；其 `external.AppCmd` ↔ C++ `HandleAppCmd`
  **就是 IPC**，与 Electron `ipcRenderer.invoke`/`ipcMain.handle` 同一模式
  （`lynx_window.h` 第 32-39 行注释自述「镜像 QFrameWork::WebView 接口」）。
- **能力等级**：C++ **L2-** → **L2 候选**（7 天复测 **09-22 明日**定）——09-21 独立完成
  Rule of 5 完整实现 + 三个计划外扩展 + 连改三版自己改对，但 Q3 推导抄答案、
  Q8 漏一种情况，复测时这两处必问。
  Chromium/Electron **L1+ → L2 候选**（09-22 定）——A4 三层链已结账，
  Utility vs Renderer 仍空；新发现前端技术栈（React/JSX/构建链）为零起点。
- **C++ 侧欠账**：W1-W2 遗留**已全清**（09-20，知识图零 ❓）；
  09-21 **新增 6 条**（Q3 推导重推 🔴 / Q8 判据 / Q9 异常安全 / Q10 连实验 /
  元素级计数 vs 类级打印 / push_back 用 swap 改造），见 `docs/debt-map.md`
- **Chromium/Electron 侧欠账（3 条）**：
  ①**前端技术栈前置断层** 🔴（09-21 新增，计划缺陷已处置，待建 `docs/frontend-prereq.md`）
  ②React/JSX/Vite 概念课**闭卷题未出**（09-21 讲完，题欠）
  ③**Utility vs Renderer 区别**——09-19 空、09-20 仍空，连续两次落地。
  ⚠️ 教练 09-19 曾在此翻车（给了不含答案的 `mojo_and_services.md`），**出处待教练实读
  `process_model_and_site_isolation.md` / `sandbox.md` 确认后再布置**
- **下一步（09-22 周二 W3D2）**：①**七天复测日**（C++ L2 / Electron L2 定级）；
  ②清 09-21 新增 6 条 C++ 欠账（Q3 闭卷只答「为什么 cap_ < 2n」，推不出写推不出来不罚）；
  ③**排 q-framework 吃透的具体打法**（大活，单独设计，不许顺手带过）；
  ④React 概念课闭卷题 + 建 `docs/frontend-prereq.md`
- **📌 教练 09-21 出错 5 次**（供周复盘核对计划可靠性）：
  ①排计划前不核 debt-map 照过期文件说话（**第 5 次同类**，本人当场指出）；
  ②全天报了三个编造时钟点（**第 2 次同类**，memory 里已有「说时间先查工具」的规则仍犯）；
  ③用「今天不做」切知识点三处（本人批评后立规：只分「主线必补」与「扩展有余力再上」，
  扩展项必须写进当日记录）；
  ④**越线替本人完成 Q3 推导**（红线延伸，本人当场质疑。已立规：本人说卡住时先问
  「卡在哪」，只给最小单位——一个公式/一个定义/一个反问，绝不给成链推理）；
  ⑤**拿岗位当知识**——讲 React 时说「Chromium 里 Blink 渲染流程你天天看」，
  本人指出「我的 Chromium 知识很匮乏，不比 Electron 多」。已立规：
  **Chromium 相关概念（DOM 树、渲染流程、Blink、进程模型细节）一律按未掌握处理，
  出现即标一行「它是什么」。**
- **今日状态（09-20 归档）**：W2D7（09-20）**W2 周复盘完成 + C++ 侧欠账全清**。
  ①周复盘 `daily/history/2026-09-20-weekly.md` 四块全填：投入统计（本人复核 735min=12.25h，累计 17.75h，
  `STATE.md` 原「18.6h」作废）、口头复述自评九题闭卷自答（5 对 / 3 错已纠 / 1 空）、门禁逐条验收、下周调整。
  ②教练驳回本人对 **A4 的「已掌握」自判**——条件是自核官方文档而非听教练结论，已实抓 Electron
  `tutorial/sandbox` 原文证明三者是**递进三层**非并列（`nodeIntegration:true` 直接掀掉第一层）。
  ③`day7_debt_clear.cpp` 一个文件清四条 C++ 欠账 + 额外清一条（commit `89a15e9` / `1d579e0`）：
  `=default` 算用户声明（D1 走拷贝 / D2 走移动）、拷贝构造 delete 不连坐拷贝赋值（D10 成员逼出调用链）、
  move 退化两缺例（D5 const / D6 无移动构造）、noexcept→vector 扩容（D7 拷贝 / D8 移动）、
  移动构造反向抑制拷贝（`#ifdef` 编译期对照，关=exit 0 / 开=exit 2 两条 C2280 + 编译器 note 原话）。
  ④`day7_value_category.cpp` 清左值/右值（commit `ccf4aac`）：五条重载探针实测，
  **`test2(int&& x)` 里 `probe(x)` 打印「左值」，本人动手前预测命中**。
  ⑤进程图 cell48/49 按订正口径重填、博客大纲四处改完（commit `60a50b0`）。
  **三大方法论进步**：Ⓐ「我认为 X 由 ___ 决定」首次执行，且实验推翻预测后**回头改了结论行**；
  Ⓑ 本人自行发现 `static_assert` 对「=default 是否抑制移动」**无分辨力**（两侧都为真），
  改用带打印实例化才分开——这正是连犯三次的那个坑，今天自己绕过去了；
  Ⓒ 本人当面指出教练「3 分钟的实验说挂到 W3」＝ Vector 拖两周的同一个动作，已立规矩：能当场做完的不许排下周。
  **教练当日自身出错 2 次**：出题诱导（「BrowserWindow 对应谁」诱向进程对象）、
  把析构 protected 误标为未补（09-17 history 第 55-57 行本人早已答对，**第 4 次「不核来源照记忆排」**）。
  ⑥**【23:00 补记 · 17:16】**`day7_value_category.cpp` test3 补测「左值可取地址」（commit `bf9f125`）：
  正面 `&a` = `000000E217CFFB50`；反面 `#ifdef` 三条一次放一行——`&10` → **C2101**（字面量是纯右值，
  没有对象也没有存储位置）、`&(a+1)` → **C2102**、`&std::move(a)` → **C2102**。
  字面量与表达式报的是**不同错误码**。→ `docs/cpp-concept-map.md` **零 ❓**。
  ⑦**【23:00 补记 · 17:28】A4 三层链结账**（commit `45ff2f4`）：本人自核官方 `tutorial/sandbox` +
  `tutorial/context-isolation` + `tutorial/security` 三篇后重答通过，已写入 `docs/debt-map.md`——
  沙箱掉 → 拿整个渲染进程的 OS 权限；contextIsolation 掉 → 拿 preload 层权限且共享同一 `window`，
  可改 `Array.prototype.push` 等**高权限代码来调用他**；contextBridge 写错（整个暴露 `ipcRenderer.send`）仍漏。
  **Q11/Q12 矛盾解法：开关独立、防护串联，两句都对。**
  ⑧日流水记录 `daily/history/2026-09-20.md` 由教练 23:00 补建（周复盘正文仍在 `-weekly.md`）。
- **能力等级**：C++ **L2-** → **L2 候选**（7 天复测 09-22 定）——今天五条欠账全部拿到**自有实验证据**，
  知识图上 ❓ 从 5 个**降到 0 个**（17:16 test3 清掉最后一个）；且首次出现「自己发现实验无分辨力并改进设计」。
  Chromium/Electron **L1+ → L2 候选**（7 天复测 09-22 定）——A4 三层链 17:28 已自核官方文档结账，
  仅 Utility vs Renderer 仍空。
- **C++ 侧欠账：✅ 全清**（「左值可取地址」半条已于 17:16 `day7_value_category.cpp` test3 补测完，
  正反两面证据齐全，**知识图零 ❓**）
- **Chromium/Electron 侧欠账（1 条，W3 清）**：
  ~~①**A4 三层链**~~ **✅ 09-20 17:28 结账**（本人自核官方 sandbox / context-isolation / security 三篇，
  commit `45ff2f4`，答案写在 `docs/debt-map.md`）
  ①**Utility vs Renderer 区别**——09-19 空、09-20 块 2 题 7 仍空，连续两次落地。
  ⚠️ 教练 09-19 曾在此翻车（给了不含答案的 `mojo_and_services.md`），**出处待教练实读
  `process_model_and_site_isolation.md` / `sandbox.md` 确认后再布置**
- **下一步**：**09-21（周一）W3D1 启动**，见 `plan/weekly/week-03.md`。
  原有 C++ 30min（`std::vector` 均摊 O(1) + 迭代器失效）+ Electron 45min（React 引入）**不动**，
  另加 🟣 **MyVector 追加档 75min**（三刀合一：骨架+assert / 真扩容 / Rule of 5 + 五路径测试）。
  **09-21 变更**：原排「周一/二/四各 25min 三刀」，**本人当日提出合并、教练核对 debt-map 后采纳**，
  周二/周四追加档撤销。教练在此处出错两次：①拿 week-03.md 第 138 行过期条目当依据，
  断言「noexcept→扩容退化实验要等 MyVector 能扩容后做」，而该实验 09-20 已由 day7 实验4 完成；
  ②主张「Rule of 5 要隔一天写才算索引挂钩」，但 09-20 day7 已把整张表逐条实验过，
  间隔检索价值已用掉。**根因同第 5 次老毛病：排计划前不核 debt-map/history，照记忆和过期文件说话。**
  已连带修正：week-03.md「W2 遗留欠账」6 条中 4 条早已清却一直挂着未同步
- **周末环境**：ToDesk 已于 09-18 本人实测确认可用，周末训练不废
- **欠账总表**：`docs/debt-map.md`（**已更新**：C++ 6 条全清 → 仅剩 Electron 2 / 产出 2 / 方法论 3 条常驻纪律）
- **今日状态（09-19 归档）**：W2D6（09-19）**约 140min（13:50–16:09，按 mtime+commit 推算）**，**本周三个 🔴 门禁补课项全部落地**：①主任务 Chromium 四进程模型图 `docs/chromium-process-model.drawio`（四框 + 职责 + 沙箱标注 + MOJO 边，四句职责经教练读 XML 核对与官方资料一致，Utility「网络服务默认在这儿」出自 `services/network/README.md`）；②补 B2 Chat UI v0（`index.html` 三段式 flex + `overflow-y` 消息区 + 左右气泡，纯 HTML/CSS，commit `3ec8791`）；③补 B4 建 `blog-drafts/` + 第 1 篇三节标题（commit `bf8ab4e`）。**最大亮点**：13:50 本人自查发现教练漏排 week-02.md 周六的 B2/B4 两个门禁项并要求补回——自查质量高于教练初排（此为教练第二次犯「新排替代原计划」的错）。**遗留**：图上 cell48 填「RenderProcessHost 对应 ipcMain」是**错答且与同图黄框注释自相矛盾**（该对应关系第三次出错）、cell49 仍空；博客大纲四处未改；**元规则「运行前先写预测」第六次未见书面执行**（current.md 明确要求写两条猜测，仓库内找不到）；当日未自建记录文件（教练 23:00 补写，09-16 后第二次）；本日 **C++ 侧零产出**，`Vector<T>` 连续两周未动。**教练当日自身出错 4 次**（资料失效 2 次、Renderer↔GPU 断言错 1 次、要求做未训练过的 CSS 对照实验 1 次），已记入 history 供周复盘核对计划可靠性
- **今日状态（09-18 归档）**：W2D5（09-18）完成闭卷默写整张表（4 题，第 3/4 题经批改后重答通过）；Menu 接线 commit `240b09a` 并用「删 File 菜单项→所有窗口同时消失」验证菜单为**全局一份**（原猜每窗口一份，猜错）；概念图从 ProcessOn 迁到 **markmap** 并三轮重构定版 `docs/cpp-concept-map.md`——主干七步因果链（RAII→持有资源→拷贝要处理→6 个函数→Rule 0/3/5→抑制规则→退化陷阱）+ [C++98]/[C++11] 版本标记 + 抑制表两行 + 工具箱补入 `=delete`/`=default`，**可直接当 09-22 七天复测的复述提纲**；新增 `docs/debt-map.md`（13 条欠账四分类）与 `docs/roadmap-map.md`（24 周全景 + 里程碑时间轴）；**ToDesk 本人实测确认可用** → 周六不重排。**遗留**：实验设计缺分辨力当日连犯两次（第三次才对）；Rule of 0 定义再次答错（09-17 答对过，答表现不答条件）；`= default` vs 什么都不写仍未重答；析构 `protected` 的为什么仍未补；Q11/Q12 矛盾只听结论未自行核实官方文档；noexcept→vector 扩容退化无本人实验；**元规则「运行前先写预测」第五次未执行**；current.md 原定的 progress.jsonl 核对与本周门禁自测两项未做（下午时间全用于工具链改造）。**~~`ai-desktop-assistant` push 失败~~ → 23:00 教练实测更正：三仓远端均已同步（`git ls-remote` 实查 240b09a / 013c4c2 / e9d8ed7 全部与本地一致），当时那两次超时发生在推送生效之后，不是凭据失效。「超时=失败」是又一次缺分辨力的判断（本日第三次），分辨只需 `git ls-remote origin master` 对 hash**
- **能力等级**：C++ **L2-**（不变）——抑制关系表与 move 退化三条经重答后全对，但 Rule of 0 定义二次答错说明索引仍不牢；7 天复测日 **2026-09-22** 照常。Chromium/Electron **L1+**（不变）——Q11/Q12 矛盾仍未自行核实
- **今日状态（09-17 归档）**：W2D4（09-17）**基本完成，本周最扎实的一天**，约 200min（按 mtime 三段：10:30-11:03 / 14:00-14:21 / 17:35-18:12，另 21:34 重编一次）——**大幅超出 1.5h 保底**。09-16 欠账**全清**：Rule of 0/3/5 闭卷重答通过、C++98/C++11 分组纠正、Test3 传染机制说清、A3 两条结论补上。✅ A1 `week-02/day4_exception_raii.cpp` + ✅ B1 `week-02/day4_uniqueptr_test.cpp`（commit `ff3a0d1`）——**W2 门禁两项达成**。✅ 本日原定内容也动了手：`day4_noncopyable.cpp`，教练实跑 0 error / 1 条 C4189 / 退出码 0，`is_copy_constructible_v<Widget>`=0、`is_move_constructible_v<Widget>`=1 证明 mixin 生效；另自己用 `#ifdef USE_DELETE` 做出「`= delete` 禁某个重载被选中」的对照并抄回 C2280（这是 current.md 的提示项，做到了但没写进答案）。✅ A4 第二、三步（sandbox.md 两节 + 三句话 + 三问），并**自行补读** Electron 官方 sandbox / context-isolation 两篇（自己发现的缺口，值得记）。✅ 记录文件本人自写（09-16 是教练补的）。**遗留**：Menu 只写了 `menu.js` 未在 `main.js` require，菜单实际未生效；`= default` vs 什么都不写答成了生成规则、没答到「用户声明」；两处空白（move 翻车原因 / 析构 protected 的为什么）；Q11 与 Q12 自相矛盾（沙箱与 nodeIntegration 画等号）；`day4_noncopyable.cpp`、`menu.js` 未 commit；「今日一句话复述」连续第二天空缺；**元规则「运行前先写预测」第四次未执行**（代码注释只有事后抄回的报错，无事前预测——但 Menu 那题写了猜测，说明是只在被问到时才做）
- **能力等级**：C++ **L2-**（不变）——今天闭卷首次基本答对 Rule of 0/3/5 与 C++98/11 分组，索引缺失已补上；但「答非所问」（`= default` 那题）说明复述仍不稳定，等 09-22 七天复测再定。Chromium/Electron **L1+**（不变）——Q11/Q12 自相矛盾说明沙箱模型还没搭稳。7 天复测日 **2026-09-22**：闭卷说清 5 个特殊成员函数 + 生成规则方向性，过则提 L2
- **W1 欠账（9 条）→ 已清 7 条**：A 概念 4 条全清（异常路径 RAII ✅09-17 / 裸指针观察语义 ✅09-15 / move-from 状态 ✅09-17 / preload+contextIsolation ✅09-17）；B 产出 4 条清 1（MyUniquePtr 单元测试 ✅09-17；Chat UI v0、进程模型图+`docs/`、博客大纲+`blog-drafts/` → 周六）；C 索引缺失 1 条 ✅09-17 闭卷重答通过
- **本周门禁**：见 `plan/weekly/week-02.md` 末尾"本周门禁"。已达成：A1 异常路径 RAII ✅、B1 MyUniquePtr 单元测试 ✅、**B2 Chat UI v0 ✅（09-19）、B3 进程模型图 ✅（09-19，升级为四进程 drawio，但图上 RenderProcessHost 对应关系填错，判「产出达成、内容有错待改」）、B4 blog-drafts + 第 1 篇大纲 ⚠️（目录与标题已建，但大纲质量不达标，四处未改）**。09-20 周复盘逐条终判
- **W1 门禁验收结果（09-15 补做）**：1 MyUniquePtr ✅；2 GitHub ≥2 commit ✅；3 Electron 主/渲染口述 ✅（下午读完 Chromium 后重答通过）；4 记录齐全 ✅（09-12/09-13 已补建，周复盘已补写）
- **下一步**：**09-20（周日）W2 周复盘，约 1h**，见 `daily/current.md`。四块：投入统计（核对 progress.jsonl 全周数据，**注意累计投入总数与明细对不上，见下**）、**口头复述自评（标「自己想的/抄的」，最防自欺的一栏，09-18/09-19 都没做）**、W2 门禁逐条验收、下周调整（重点：`Vector<T>` 连续两周没动，W3 是 STL 容器周，怎么带进去）；另补 W1 周复盘空着的达成率/缺口原因/下周调整三处；另需改 09-19 遗留的三处（图 cell48 错答 + cell49 空 + 博客大纲四处）
- **周末环境**：**ToDesk 已于 09-18 本人实测确认可用**，周末训练不废。周六按 90min 保守排，拿到真实数据后下周再调
- **欠账总表**：`docs/debt-map.md`（13 条，四分类：方法论 2 / C++ 6 / Electron 2 / 产出 3）。方法论两条排最前——「运行前先写预测」已 **6 次**未执行（09-19 第六次）、「实验要有分辨力」09-18 连犯三次
- **累计投入（09-20 版，已被上方 09-21 版取代，保留备查）**：按明细加总 = 17.75 小时
- **周末方案变更**：09-12/09-13 断档根因为公司代理更新后家庭电脑无法直连办公机。**改用 ToDesk 远程**，09-19（周五）前确认可用性；周六时长先按 90min 保守排，拿到真实数据后再定，不按原计划 4h 排
- **累计投入**：**21.08 小时**（截至 09-21）。W1：330min = 5.5h（09-08 90 + 09-09 90 + 09-10 45 + 09-11 105，09-07/09-12/09-13 为 0）；W2：735min = 12.25h（09-14 105 + 09-15 180 + 09-16 110 + 09-17 200 + 09-18 未计 + 09-19 140 + 09-20 未单列）；**W3：09-21 200min**。小计 1265min = 21.08h。⚠️ **09-19 23:00 教练核账发现：此前长期写的「18.6 小时」与明细对不上，差 3.2h 来源不明。现一律按明细加总，18.6 作废。** 注：09-09~09-11 为 09-15 补记估算，09-16/09-17/09-19 按 mtime+commit 推算，09-18 无法切分故不计（真实总时长应略高于此数）
- **累计博客**：0 篇（目标 24 周 5 篇）
- **Side project（2 个）**：
  ①**`F:\code\ai-desktop-assistant`**（学习项目，GitHub: codingning/ai-desktop-assistant, private）——
  已完成 IPC 双向通信（openFile / getCurrentData / helloName）+ Chat UI v0（纯 HTML/CSS）。
  **TypeScript 化：week-01 第 50 行原定，从未落地，09-21 已在计划文件中划掉标作废。**
  React 化原定 09-21，因前置断层改期，待排。
  ②🆕 **`E:\code\q-framework`**（生产项目，简历主项目，09-21 新增）——
  详见 `docs/q-framework-map.md`。可访问可构建。吃透打法 09-22 单独设计。
- **简历状态**：无（Week 4 完成 v0 保底版）。**09-21 变更**：简历项目从 1 个改为 2 个——
  q-framework（生产，标注真实职责：主 UI / 照片压缩 / Shell 扩展）+ ai-desktop-assistant（学习，自研）

## 关键文件索引

| 用途 | 文件 |
|---|---|
| 为什么调整方向 | `plan/STRATEGY-2026-09-07.md` |
| 24 周总路线 | `plan/roadmap-24-weeks.md` |
| Week 1-6 详细日计划 | `plan/weekly/week-01.md` 至 `week-06.md` |
| Week 7-24 周纲要 | `plan/weekly/week-07-to-24-outline.md` |
| Side project 设计 | `plan/side-project-ai-desktop.md` |
| 求职工程轨 | `plan/job-hunt-track.md` |
| 归档旧路线 | `plan/archive/` |
| 🆕 q-framework 吃透计划 | `docs/q-framework-map.md` |
| 欠账唯一权威源 | `docs/debt-map.md` |
| C++ 知识图（markmap） | `docs/cpp-concept-map.md` |
| 24 周全景图（markmap） | `docs/roadmap-map.md` |

## 续训规则

- 先检查 `git status -sb`，保护用户已有未提交改动
- 只依据仓库中的记录判断已掌握内容；"看过"不等于"掌握"
- 每个单元遵循诊断 → 主资料 → 源码切片 → 实现 → 验证 → 复述
- 每日记录必须使用中文，包含：完成任务、训练内容、掌握部分、未掌握/阻塞、证据、下一日计划
- 无学习日也必须写记录，明确"今日未学习"，不新增虚构能力结论
- 每次记录后更新 `current.md` 和本文件的当前状态，再提交并推送
- 推送失败必须明确记录失败，不把本地提交当作远端成功
- 每周日晚上必须写周复盘，存 `daily/history/YYYY-MM-DD-weekly.md`
- 只有通过 7 天复测后才可以稳定提升能力等级；只有 L4 证据可以进入简历

## 阶段目标提示

- **阶段一（Week 1-6）**：基础重建。C++17 到 L2 + Electron 入门 + Chromium 概念地图 + 第 1 篇博客
- **阶段二（Week 7-12）**：Electron 深化 + Side project MVP + 第 2 篇博客
- **阶段三（Week 13-18）**：AI 集成 + Side project v1 + 简历 v1 + 第 3、4 篇博客
- **阶段四（Week 19-24）**：面试冲刺 + 拿 offer + 第 5 篇博客
