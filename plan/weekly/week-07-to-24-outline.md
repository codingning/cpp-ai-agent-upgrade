# Week 07-24 纲要（阶段二/三/四简要周计划）

> # 🔴 2026-10-15 方向变更（本人指令，详见 `plan/STRATEGY-2026-10-15.md`）
>
> **Electron / 前端 / Side project 整条移出，新方向 = Chromium 内核 / C++ 基础设施。**
>
> 下方 **Week 07-12 原文（Electron 深化 + AI 桌面助手）整段作废**，
> 由本节顶部的「10-15 改写版 Week 07-12」替代；
> **Week 13-18（AI 集成）标🔴待定**，等本人在 A/B/C 三案里选一个再定稿；
> Week 19-24（面试冲刺）**结构不变，只改岗位口径与项目口径**。
>
> ⚠️ 原文全部保留在下方 `<details>` 里，**作废不等于删除**（他 09-21 立的规矩）。

---

## 🔴 Week 07-12（10-15 改写版，以此为准）：C++ 并发 + q-framework 深挖

> ⚠️ **10-15 晚补充（第二条主线）**：下午那格**不只有 q-framework**。
> 本人 16:49 指出简历是两个项目（360 安全浏览器 + q-framework），教练只训练了一个
> → 已建 **`docs/browser-track.md`**（浏览器四层深挖链）。
> **W7 起下午时段两条线并行**，具体日排法见 `docs/browser-track.md` 第六节，
> 要点：W7 浏览器第二层②③④ ／ W8 浏览器第三层③（`SequencedTaskRunner`，与上午 `mutex` 合流）
> ／ W9 浏览器第三层⑤（扩展 API 全链路，与 q-fw `ipc/` 同讲「JS 调 C++」）
> ／ W10 **Mojo**（他最大单点缺口）／ W11 GN+`gn args` ／ W12 minidump + 上游 merge。
> **下方本节的 q-fw 排法不变，浏览器线是并行增量不是替换。**

**节奏不变**：上午 10:30-11:10 C++ 40min ／ 下午 17:00-17:50 q-fw/Chromium 50min ／ 记录 15min。
**周六 4h 深度 ／ 周日 2h 复盘** 不变。

### Week 07：`std::thread` 起步 + CEF 两个进程的职责

**上午 C++**：`std::thread` 构造与启动 / `join` vs `detach` / 线程对象的生命周期（没 join 就析构 = `std::terminate`）/ 传参的拷贝语义（为什么要 `std::ref`）
**下午 q-fw**：第三层①——CEF 的 browser 进程和 renderer 进程，各自职责、谁先起、谁创建谁。
对照锚点：`webview/cef/browser/` 与 `webview/cef/render/` 的成对 handler（09-22 实查，38 个文件）
**周六 4h**：`base/` 顶层 108 个 `.h` 扫 5 个「重复造的轮子」收尾（这条从 W6 挂下来）+ 一个多线程小程序

#### 🔴 2026-10-18 补入 · W7 浏览器线（D 组）四项日排法

> **为什么补**：本文件 10-15 只在第 17-25 行写了「浏览器线并行，详见 `docs/browser-track.md` 第六节」，
> **没有落到周计划文件的日排里** → 教练账，10-18 结清（`daily/current.md` 第三节原排）。
> **两条线怎么共存一格**：下午 50min 不切两半。**周一/周三/周五给浏览器线，周二/周四给 q-fw 第三层。**
> 周六 4h 档里 q-fw 另有独立格，所以 q-fw 不吃亏。

| # | 内容 | 排到 | 时长 | 解锁/前提 |
|---|---|---|---|---|
| ① | **S 档第一课**：`SiteInstance` / `SiteInfo` / `RenderProcessHost` / `RenderFrameHostManager` / `ChildProcessSecurityPolicy` 五类各是什么 + Site Isolation 决策链 | **W7 周一下午（首项，不许后移）** | 40min | **这是简历行「参与 content/ 进程隔离决策链路排障」的解锁条件**（本人 10-17 主动指令，commit `745aebd`）。闭卷过关前不许写进简历 |
| ② | 他的功能落在哪层 —— 用他自己的提交当教材（`04fd0d1` 网页打不开 9 文件 / `8beac32` content 片 22 文件） | W7 周三下午 | 50min | 需 ① 的五类名字先立住 |
| ③ | omnibox 两处分层：`components/omnibox/browser/` 与 `chrome/browser/ui/views/omnibox/` 同一需求为何改两处（教材 `578c743`，20 文件） | W7 周五下午 | 50min | 需 B1-B4 五层分界（10-17 已过） |
| ④ | 360 自有代码与上游并存 —— `content/` 下 20 处违例 include 就是教材 | **W8 周一下午**（W7 装不下，写明去向不是砍） | 50min | 需 ② 先落地 |

**W7 浏览器线门禁（可验证形式）**：
- [ ] 五类闭卷各答一句「它是什么 + 它决定什么」，**不许复述教练措辞，要指到自己改过的文件**
- [ ] Site Isolation 决策链能说出「谁问谁、谁拍板建新进程」
- [ ] ①过关后方可解锁那条简历行；不过关则简历行继续冻结

**门禁**：
- [ ] `join`/`detach` 的差别能用自己跑的实验说明（不是背定义）
- [ ] 能画出 CEF 的进程树并说清每个进程里跑的是什么
- [ ] 5 个重复轮子清单落到 `docs/q-framework-map.md`
- [ ] 🆕 **W6 带病进来的 5 条清完**：W6-3（析构四类位置）／W6-4（`shared_ptr` 收尾两项）／W6-5（`explicit` 换实例）／W6-7（CEF/WebView2 两方对照表）／W6-8（Chromium 四进程口述 5min）

### Week 08：`mutex` + `HandleAppCmd` 全链路

**上午 C++**：`std::mutex` / `lock_guard` / `unique_lock` 的区别 / 死锁的四个必要条件 / 锁粒度
**下午 q-fw**：第三层②——`HandleAppCmd` 这条链走完：JS 调 `external.AppCmd` → `cef_render_appcmd_handler` → 跨进程 → `cef_browser_message_handler` → C++ 业务。**每一环实查文件，不许凭印象。**
**周六 4h**：09-29 挖出的那个真 bug（`pref_service` 全文无任何锁，两线程场景有数据竞争）——自己设计加锁方案并说清为什么这么加
**门禁**：
- [ ] 死锁四条件能举出自己写的例子
- [ ] `HandleAppCmd` 全链路能画出来，每一环指到具体文件和行

### Week 09：`condition_variable` + 手写 IPC 传输层

**上午 C++**：`condition_variable` / 生产者消费者 / spurious wakeup 为什么要用 `while` 不是 `if`
**下午 q-fw**：第三层③——`ipc/` 模块：Windows IOCP 命名管道、带长度前缀的消息序列化、16MB 上限、自动分片重组、多客户端会话管理（出处 `ipc/README.md`）
**周六 4h**：自己写 `ThreadSafeQueue<T>`（阻塞 pop + 优雅关闭）
**门禁**：
- [ ] 生产者消费者可运行、无 race、能优雅退出
- [ ] 能说清「为什么要长度前缀」和「分片重组解决的是什么问题」

### Week 10：线程池 + 异步回调在哪个线程

**上午 C++**：线程池设计（任务队列 + worker 组 + 优雅退出 + 任务返回值 `future`）
**下午 q-fw**：第三层④——`ExcuteJavaScript` 带 callback 是异步的，**那个 callback 在哪个线程被调用**？（这一问是第三层压轴）
**周六 4h**：线程池完整实现 + 压测
**门禁**：
- [ ] 线程池能跑、能收、不泄漏
- [ ] 能说清 q-fw 里跨线程回调的线程归属，并指出代码位置

### Week 11：`std::atomic` + 崩溃收集两套并存

**上午 C++**：`std::atomic` / 内存序入门（`relaxed` / `acquire-release` / `seq_cst` 三档的差别与代价）
**下午 q-fw**：第四层①——`crashpad/` 与 `breakpad/` **两套崩溃收集并存，为什么**（历史包袱？不同进程用不同套？）
**周六 4h**：实际抓一个崩溃 dump 并定位到函数
**门禁**：
- [ ] 三档内存序能讲清各自保证什么、代价差在哪
- [ ] 抓到一个真实 dump 并定位到函数名

### Week 12：阶段二验收

**上午 C++**：并发闭卷 + 线程池闭卷重写计时
**下午 q-fw**：第四层②——CEF 沙箱 vs Chromium 沙箱是不是同一套；WebView2 是进程外运行时，Edge 升级会不会把你的程序搞崩
**周六 4h**：q-framework 吃透笔记定稿（结构 = 四层深挖链，面试直接当讲稿）
**阶段二门禁**：
- [ ] C++ 并发达 L2（线程池闭卷能写出来）
- [ ] q-fw 面试深挖链**四层全部可答**
- [ ] 吃透笔记定稿
- [ ] 至少抓过一个真实崩溃 dump

---

## 🔴 Week 13-18 → **本人 2026-10-15 17:36 选定方案 B：AI 集成压成 2 周，放 W17-W18**

原排「AI 集成 + 简历工程」六周。三个选项中本人原话 **「那就选B 压成 2 周」**。

**生效安排**：
- **W13-W16（四周）**：还给 C++/Chromium 深水区 —— 两条线（q-framework / 360 浏览器）
  第四层收口 + Chromium 本体专题（Mojo、GN/`gn args`、minidump 深一层、上游 merge 工程化）。
  **具体排法见 `docs/browser-track.md` 第六节与 `docs/q-framework-track.md` 第四节。**
- **W17-W18（两周）**：AI 集成压缩版。保留的理由（教练给、本人认）：浏览器厂都在往客户端塞 AI，
  他本职部门就有 AI 探索任务，「能聊」是加分项不是主业。
  **压缩后保留什么由 10-18 周日复盘定稿**，原则：只保留「面试能答得上」那一层，不做产品。

原 AI 六周原文保留在下方 `<details>`，**标作废不删**。

---

## Week 19-24：结构不变，只改口径

- 投递岗位口径：~~Electron/Chromium 客户端~~ → **Chromium 内核 / C++ 基础设施**
- 项目讲解口径：~~AI 桌面助手 Side project~~ → **q-framework（主）+ 阶段三自写的 C++ 工具（辅）**
- 面试题库分类：~~C++/Electron/Chromium/AI~~ → **C++（语言+并发）/ Chromium 架构 / 构建与调试工程 /（AI 视 W13-18 决定）**
- 系统设计题模板三个：~~Electron 应用架构 / chatbot / 桌面应用性能优化~~
  → **多进程桌面应用架构 / 跨进程 IPC 传输层设计 / 崩溃收集与定位体系**

其余（投递数、面试轮次、复盘节奏、offer 门槛）**一条不改**。

---

<details>
<summary>～～以下为 09-07 原文，自 2026-10-15 起整段作废，保留备查～～</summary>

**说明**：前 6 周是详细每日计划（在 `week-01.md` 至 `week-06.md`），第 7 周开始只写周纲要 + 门禁。每周开始时（周日晚），你需要根据当周纲要自己拆解到每天，这样也是训练自己的学习设计能力。

---

## 阶段二：Electron 深化 + Side project 启动（Week 7-12）

### Week 07：Electron 主进程深度 + C++ 并发起步 + Side project 立项

**主线**：
- Electron 主进程完整 API 遍历：app / BrowserWindow / Menu / Tray / dialog / shell / net / session
- 每个 API 都要在 side project 里用一次（哪怕小功能）

**副线**：
- C++ 并发起步：`std::thread` 基础、joinable、detach
- 写代码：多线程打印 hello world（简单但要理解 join/detach 差异）

**Side project**：
- 立项文档：`ai-desktop-assistant/docs/PROJECT.md`
- 架构图 v1：主进程模块划分
- 技术选型 ADR-001：为什么用 Electron + TypeScript + React

**门禁**：
- [ ] 8 个主进程 API 都在 side project 里有使用
- [ ] 多线程 join/detach 示例代码可运行
- [ ] Side project 立项文档 + 架构图 + ADR-001 完成

### Week 08：Electron 渲染进程 + C++ mutex + Side project UI 骨架

**主线**：
- Electron 渲染进程 + Web API 融合（Notification / Clipboard / File System Access）
- 与传统 Web 开发的区别在哪

**副线**：
- C++ `std::mutex` / `std::lock_guard` / `std::unique_lock`
- 生产者消费者问题（用 mutex + condition_variable 的准备）

**Side project**：
- Chat UI 完整版：消息滚动、代码高亮预留（markdown 渲染）、输入区自动扩展
- 参考主流 AI 客户端 UI 细节

**门禁**：
- [ ] mutex + shared 数据的多线程示例可运行且无 race
- [ ] Chat UI 达到"能演示"标准

### Week 09：Electron IPC 深度 + C++ condition_variable + Side project IPC 完善

**主线**：
- Electron IPC 深度：MessageChannel、Transferable、Structured Clone
- 性能考量：大数据传输方案

**副线**：
- C++ `std::condition_variable`：生产者消费者的完整实现
- 陷阱：spurious wakeup、lock 的粒度

**Side project**：
- 完善 IPC 层：加入错误处理、超时、取消
- 消息发送状态：pending / success / error 三态显示

**门禁**：
- [ ] 生产者消费者 C++ 代码可运行且线程安全
- [ ] IPC 层有完整错误处理

### Week 10：Electron 原生模块（N-API 入门）+ C++ 移动语义实战 + llama.cpp 接入

**主线**：
- Electron 原生模块：Node N-API 概念、node-addon-api、prebuild-install
- 选择方案：child_process 调用 llama.cpp CLI vs N-API 直接集成
- **推荐初期用 child_process**（简单、快、够用）

**副线**：
- C++ 移动语义综合练习：写一个 `ThreadSafeQueue<T>` 类

**Side project**：
- 下载 llama.cpp Windows 编译版（或自己编）
- 下载一个 3B/7B 量化模型（Qwen 或 Llama 或 Phi）
- 主进程用 child_process 调用 llama.cpp CLI
- **第一次真实 LLM 对话**（这是 MVP 前的关键里程碑）

**门禁**：
- [ ] llama.cpp 在本机能用命令行跑起来
- [ ] Electron 应用能调用 llama.cpp 并返回真实回复（哪怕慢、格式乱）

### Week 11：Electron 打包 + V8 入门 + Side project MVP 集成

**主线**：
- Electron 打包：electron-builder 配置、Windows 安装包制作
- 图标、签名（不签也行，本地够用）

**副线**：
- Chromium V8 引擎入门：JavaScript 执行流程、isolate/context 概念
- 学习目的：面试可讲，非深入

**Side project**：
- 集成打磨：llama.cpp 调用稳定化、错误处理、超时处理
- 加载/发送态的 UI 反馈

**门禁**：
- [ ] Side project 能打包成 exe 安装包
- [ ] V8 isolate/context 能口述 3 分钟

### Week 12：阶段二验收 + 第 2 篇博客

**主线**：
- 阶段二验收：Electron 4 大机制（主/渲染/IPC/原生）能改代码不是只用
- Side project MVP 演示视频（3-5 分钟）录制

**副线**：
- 第 2 篇技术博客：《Electron 调用本地 LLM 的三种方案对比》
- 内容："创造学习"式——你亲自试的三种方案 + ADR 决策

**门禁**：
- [ ] Side project MVP 可演示、可打包、可分发
- [ ] 第 2 篇博客公开发布
- [ ] 累计博客 2 篇

---

## 阶段三：AI 集成 + 简历工程（Week 13-18）

### Week 13：Transformer 复习 + Side project 流式响应 + 简历 v0 起草

**主线**：尚硅谷 07/09 章节复习（DL + NLP 基础），重点 Transformer 结构
**副线**：Side project 加流式响应（主进程 spawn 流式读 → IPC 增量推送 → 渲染进程打字机效果）
**求职**：简历 v0（应急版第 4 周完成过）→ 起草 v0.5（融合 Side project 内容）
**门禁**：Side project 流式响应打通；简历 v0.5 完成

### Week 14：LangChain 核心 + Side project 会话记忆 + 简历同行 review

**主线**：LangChain.js 基础，理解 Chain / Prompt / Model / Parser / Memory 5 大概念
**副线**：Side project 加会话记忆（Buffer/Window/Summary 三种策略至少懂原理）
**求职**：简历 v0.5 找 2 位同行 review，收集反馈
**门禁**：LangChain 5 大概念能口述；Side project 有多轮对话记忆；简历收到 review 反馈

### Week 15：RAG 原理 + Side project 本地知识库 + 第 3 篇博客

**主线**：RAG 完整流程（load → split → embed → store → retrieve → generate）
**副线**：Side project 加本地文档 RAG（用 chroma 或 sqlite-vss 存向量）
**博客**：第 3 篇《本地 RAG 系统的 chunk 策略实验》——你亲自试不同 chunk 大小的效果
**门禁**：Side project 能读一个本地 markdown 目录并基于其回答问题；第 3 篇博客发布

### Week 16：Agent + tool calling + JD 反向分析

**主线**：Agent 原理、tool calling 协议、ReAct 模式
**副线**：Side project 加 1-2 个简单 tool（如 file_read、web_fetch）
**求职**：Boss 抓 20 个 Electron/Chromium 目标岗 JD，做统计分析
**门禁**：Side project 能通过 tool 完成一个多步任务；JD 分析报告完成

### Week 17：微调原理（LoRA/QLoRA）+ Side project 打包优化 + 短板补强

**主线**：LoRA/QLoRA 原理（不做实操，理解够用）+ 尚硅谷微调章节复习
**副线**：Side project 打包体积优化、native 模块处理、模型分离下载
**求职**：根据 Week 16 JD 分析结果，补 5 个高频出现但你不会的技能
**门禁**：能画 LoRA 训练流程图；Side project 打包体积 < 200MB；短板补强清单完成

### Week 18：AI 阶段验收 + 简历 v1 定稿 + 第 4 篇博客

**主线**：AI 部分闭卷小测（RAG 流程、Agent、LoRA）
**副线**：Side project v1 打磨、README 完善、演示视频重录
**求职**：简历 v1 定稿、面试项目讲解稿 5 分钟版
**博客**：第 4 篇《我用 6 个月做了一个 Electron AI 助手 - 技术复盘》
**门禁**：Side project v1 可分发；简历 v1 定稿；第 4 篇博客发布

---

## 阶段四：面试冲刺 + 决策（Week 19-24）

### Week 19：投递启动 + 面试八股整理

**主线**：Boss 上主动投递 5 家目标公司（预热单）
**副线**：整理 C++/Electron/Chromium/AI 面试题库（每类 10-30 题）
**Side project**：进入维护模式，只 bug 修复
**门禁**：至少 5 家投递、5 家读过 JD 后针对性改简历、题库初稿完成

### Week 20：第 1-3 轮面试 + 面试复盘

**主线**：投递 10 家新岗；面试 3-5 家（初面/一面）
**副线**：每次面试后立刻复盘（30 分钟内写完），存到 `plan/interview-log/`
**门禁**：面试次数 ≥3；面试复盘 ≥3 份

### Week 21：第 4-6 轮面试 + 系统设计题准备

**主线**：面试进入二面/技术深挖阶段，可能有系统设计题
**副线**：准备 3 个系统设计题模板（Electron 应用架构 / 简单 chatbot / 桌面应用性能优化）
**门禁**：面试次数累计 ≥6；系统设计模板完成

### Week 22：第 7-10 轮面试 + 短板专项

**主线**：进入高价值 offer 面试阶段，面试次数累计 10 次
**副线**：根据面试反馈，把最常挂的知识点专项复习
**门禁**：面试累计 ≥10；至少收到 2 个 offer 意向

### Week 23：Offer 谈判 + 背调 + 第 5 篇博客

**主线**：offer 谈判、比价、确认目标
**副线**：第 5 篇博客《半年跳槽复盘 - 22K 到 30K 的路径》（哪怕未拿 offer 也可写"求职期学习记录"版）
**门禁**：至少 1 个 offer 达到 28K 或明确决策"继续等"；第 5 篇博客发布

### Week 24：决策 + 收尾 + 半年总结

**主线**：接 offer 或继续等；如接则做离职准备
**副线**：写半年总结、更新 GitHub 项目、更新 LinkedIn / 掘金 profile
**门禁**：明确决策；半年总结文档；能力矩阵终版

---

</details>

---

## 每周开始时的 3 分钟仪式

1. 打开本周 `week-XX.md` 或纲要
2. 拆到每天：把周任务分到周一到周五，各 1.5 小时
3. 更新 `daily/STATE.md`：本周主题、Day 1 任务
4. 更新 `daily/current.md`：Day 1 具体动作
5. 开始学习

## 每周结束时的 30 分钟仪式

1. 写周日复盘 `daily/history/YYYY-MM-DD-weekly.md`
2. 更新累计小时数、累计博客数、Side project 进度
3. 预读下周纲要
4. 更新简历（每 2 周至少加一行）

## 缺席日处理

- 缺席 1 天：不追赶，只记录
- 连续缺席 3 天：周日复盘时分析原因（工作忙？状态差？计划不合适？）
- 连续缺席 5 天：启动"最小可完成版"——只保留每天 30 分钟核心任务
- 缺席一整周：不砍计划，下周照常，只是里程碑往后顺延 1 周
