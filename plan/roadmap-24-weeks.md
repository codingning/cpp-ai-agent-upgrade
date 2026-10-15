# 24 周路线图（2026-09-07 版 · 2026-10-15 方向变更）

> # 🔴 2026-10-15 方向变更（本人指令，详见 `plan/STRATEGY-2026-10-15.md`）
>
> **本人三答**：①Electron/`vite-project`「完全不碰了，因为我没有相关经验」；
> ②「投的岗位方向也得改成偏 Chromium 内核/C++ 基础设施」；
> ③「C++/Chromium 内核更贴现在工作、更值钱，前端会越来越不值钱」。
>
> **→ 新目标方向：Chromium 内核 / C++ 基础设施。薪资目标与时间窗不变（2027-03 前 28-32K）。**
>
> **→ 下午 50min 时段自 10-15 起换轨**：Electron 主线 → **q-framework 深挖 + Chromium 本体知识**。
> **→ 上午 40min C++ 不变，且从「底座」升为「主业本身」**（并发从副线升主线）。
> **→ `vite-project` / `ai-desktop-assistant` 双归档，前端技术栈整条移出。**
>
> ⚠️ 本文件下方阶段二/三/四的旧表格**保留备查但已失效**，以各节顶部的 10-15 改写版为准。

**目标**：~~2027-03 前完成 22K → 28-32K 跳槽，方向 Electron/Chromium 客户端 + AI 集成。~~
**🔴 10-15 改**：2027-03 前完成 22K → 28-32K 跳槽，方向 **Chromium 内核 / C++ 基础设施**。

**时间预算**：每天 1.5 小时（工作日）+ 每周末 6 小时 = 每周 13 小时。缺席不追赶，连续 2 周未达 10 小时启动最小可完成版。

> ## 🚫 节假日停训（2026-09-23 加，依据国办发明电〔2025〕7 号，教练实查）
>
> 明细见 **`docs/calendar-holidays.md`**（含 2026 年全年节假日表 + 逐日可训练标记）。
>
> **近期两个停训区间**：
> - **中秋 09-25（五）~ 09-27（日）**，停 3 天 —— 本人只提了国庆，**中秋是教练实查发现的**
> - **国庆 10-01（四）~ 10-07（三）**，停 7 天 —— 本人 09-23 明确提出「这个假期你得跳过」
> - ⚠️ **10-10（周六）是法定调休上班日**，按**工作日 1.5h** 排，不按周六 4h 深度档
>
> **处置原则（均源自本人先前立的规矩）**：
> 1. **停训 ≠ 砍内容**。十天停训期内原有的全部内容一条不切，逐条标明顺延到哪一天
>    （本人 09-20「3 分钟实验挂到 W3」、09-21「今天不做 X」两次批评过教练缩水）
> 2. **假期本身不留作业**。本人说没时间就是没时间，不设「有空看看」、不做变相排课
> 3. **假期前最后一天必须收口**（09-24、09-30）：只排当天能闭环的内容 +
>    写「假期后第一件事」清单 + 代码全部 commit push
> 4. **假期后第一天必须间隔复习**（10-08）：上午整段闭卷自答 + 重跑自己的代码，
>    **不排新内容、不靠重读笔记**
>
> **对总周期的影响**：W3-W6 累计少约 1.5 周有效训练时间，24 周路线**整体顺延约 1.5 周**。
> **不重算终点日期**——目标是能力达标（阶段门禁），不是打卡满 24 个日历周。
> 阶段一（基础重建）的门禁内容不变，达成日顺延。

## 四阶段总览

> 🔴 **10-15 改写版（以此为准）**

| 阶段 | 周次 | 主题 | 核心交付 | 阶段门禁 |
|---|---|---|---|---|
| 一 | 1-6 | 基础重建 | C++ 底座 + Chromium 概念地图（~~Electron 入门~~ 10-15 作废） | C++17 RAII/STL/智能指针达 L2；Chromium 架构能画图口述 |
| 二 | 7-12 | **C++ 并发 + q-framework 深挖（第三/四层）** | 线程池自己写 + q-fw CEF 多进程/IPC/崩溃体系吃透笔记 | C++ 并发达 L2；q-fw 面试深挖链四层全部可答 |
| 三 | 13-18 | **Chromium 本体 + 构建与调试工程** | Chromium 源码级理解（Mojo/任务调度/沙箱/内存分配器）+ 一个自写 C++ 工具 + 简历 v1 | 能讲清 Mojo 与任务调度；简历 v1 可投；AI 段处置待本人定（见下） |
| 四 | 19-24 | 面试冲刺 + 决策 | 简历定稿 + 主动投递 + 面试 5-10 家 + 谈判 | 拿到 ≥1 个满意 offer 或明确决策继续/离开 |

### 🔴 待本人定：阶段三原排的 AI 集成六周（W13-W18）怎么处理

选项 A 整条移出 ／ **B 压缩成 2 周放 W17-W18（教练倾向）** ／ C 原样保留六周。
**他回答前，W13-W18 在文件里标「待定」，不删不改。** 详见 `plan/STRATEGY-2026-10-15.md` 第五节。

<details>
<summary>～～旧版四阶段总览（09-07 版，已失效，保留备查）～～</summary>

| 阶段 | 周次 | 主题 | 核心交付 | 阶段门禁 |
|---|---|---|---|---|
| 一 | 1-6 | 基础重建 | C++ 底座 + Electron 入门 + Chromium 概念地图 | C++17 RAII/STL 达 L2；Electron hello-world 跑通；Chromium 架构能画图口述 |
| 二 | 7-12 | Electron 深化 + Side project 启动 | Electron 主/渲染/IPC/原生模块深度 + AI 桌面助手 v0 | Electron 4 大机制能改代码；Side project MVP 可演示 |
| 三 | 13-18 | AI 集成 + 简历工程 | LangChain/RAG/微调理解 + Side project v1 + 简历初稿 | Side project 集成 LLM 可用；简历 v1 可投；开始看 JD |
| 四 | 19-24 | 面试冲刺 + 决策 | 简历定稿 + 主动投递 + 面试 5-10 家 + 谈判 | 拿到 ≥1 个满意 offer 或明确决策继续/离开 |

</details>

## 每周固定节奏

> 🔴 **10-15 改**：下午那格的内容换轨，时长与时段不变。

**工作日（周一到周五，每天 1.5 小时）**：
- **上午 10:30-11:10（40min）：C++ 主线**（现代 C++ → 并发 → 内存模型。**不再叫「底座」，这是主业**）
- **下午 17:00-17:50（50min）：q-framework 深挖 + Chromium 本体知识**
  （~~Electron/Chromium 主线学习或 side project 编码~~ **10-15 作废**）
- 15 分钟：写当日记录 + 更新 STATE.md

**周六（4 小时）**：
- 深度编码时段：side project 主开发时间
- 或深度阅读时段：Chromium/Electron 源码切片

**周日（2 小时）**：
- ~~1 小时：技术博客写作~~ 🚫 **2026-09-29 移出训练计划**（本人决定：改公众号且不算进计划）
  → 这 1 小时改为 **side project 开发 / q-framework 吃透笔记**（二选一，本人当周自定）
- 1 小时：本周复盘 + 下周计划微调

**每周固定产出**：
- 5 天工作日记录（有学习或缺席都要记）
- 1 次周日复盘写在 `daily/history/YYYY-MM-DD-weekly.md`
- 至少一段可运行代码 commit
- 至少一个技术点闭卷复述

## 阶段一：基础重建（第 1-6 周）

### 主题分布

> 🔴 **10-15 注**：W1-W6 已执行完毕，下表是实际走过的路，不改。
> 其中「Electron / React / preload」相关内容**自 10-15 起不再延续**，
> 已学到的方法论（实验分辨力等）与技术栈无关，照常保留。

| 周 | 主线 | 副线 | 周末深度 |
|---|---|---|---|
| 1 | C++ RAII/生命周期 | Electron 概念 + 环境搭建 | Electron hello-world |
| 2 | C++ 拷贝/移动/Rule of 5 | Chromium 架构总览阅读 | 画 Chromium 进程模型图 |
| 3 | C++ STL 常用容器 | Electron 主进程 API | 写 Electron 简易记事本 |
| 4 | C++17 结构化绑定/optional/variant | Electron 渲染进程 + preload | 记事本加持久化 |
| 5 | C++ 智能指针深度 | Electron IPC 机制 | 记事本主/渲染进程通信 |
| 6 | C++ 阶段验收 | Electron 阶段验收 + Chromium 复习 | ~~写第一篇技术博客草稿~~ 🚫 **09-29 移出计划**（改公众号，本人自主，不排期） |

**阶段门禁（第 6 周末验收）**：
- [ ] C++ 能不看资料实现 RAII 资源包装器 + Rule of 5 + 单元测试
- [ ] ~~Electron 能独立搭建项目、写主/渲染进程、用 IPC 通信~~ 🚫 **2026-10-15 方向变更，本条作废**
      → 替代项：**q-framework 面试深挖链第二层四问可答 + 智能指针三件套（unique/shared/weak）闭卷可讲**
- [ ] Chromium 能画出 Browser/Renderer/GPU/Utility 进程模型图并口述通信路径
- [ ] ~~完成 1 篇技术博客草稿（1500 字以上）~~ 🚫 **2026-09-29 本人决定移出训练计划**（详见 `docs/debt-map.md`）

## 阶段二：~~Electron 深化 + Side project（第 7-12 周）~~ 🔴 10-15 改写：C++ 并发 + q-framework 深挖

### 主题分布（10-15 改写版，以此为准）

| 周 | 上午 C++ 主线 | 下午 q-fw / Chromium | 周末深度 |
|---|---|---|---|
| 7 | `std::thread` / join vs detach / 线程生命周期 | q-fw 第三层①：CEF browser 进程 vs renderer 进程的职责与启动顺序 | `base/` 顶层扫轮子收尾 + 一个多线程小程序 |
| 8 | `std::mutex` / `lock_guard` / `unique_lock` / 死锁四条件 | q-fw 第三层②：`HandleAppCmd` 全链路（JS → render → 跨进程 → browser） | 用锁改造一段 q-fw 里的无锁代码（09-29 挖出的真 bug） |
| 9 | `condition_variable` / 生产者消费者 / spurious wakeup | q-fw 第三层③：`ipc/` 手写 IOCP 命名管道（16MB 上限、分片重组、会话管理） | 自己写 `ThreadSafeQueue<T>` |
| 10 | 线程池设计（任务队列 + worker + 优雅退出） | q-fw 第三层④：`ExcuteJavaScript` 的 callback 在哪个线程被调用 | 线程池完整实现 + 压测 |
| 11 | 原子操作 / `std::atomic` / 内存序入门（relaxed/acquire-release/seq_cst） | **q-fw 第四层①：`crashpad/` 与 `breakpad/` 为什么两套并存** | 崩溃 dump 实际抓一个并分析 |
| 12 | 阶段二验收：并发闭卷 + 线程池重写计时 | **q-fw 第四层②：CEF 沙箱 vs Chromium 沙箱；WebView2 进程外运行时的升级风险** | q-fw 吃透笔记定稿（面试深挖链四层全部可答） |

**阶段二门禁（第 12 周末验收，10-15 改写）**：
- [ ] C++ 并发达 L2：线程池能闭卷自己写出来、能讲清死锁四条件与内存序三档的区别
- [ ] q-framework 面试深挖链**四层全部可答**（第一、二层已过；第三、四层本阶段完成）
- [ ] 一份 q-framework 吃透笔记（结构 = 四层深挖链），面试时能当讲稿用
- [ ] 至少抓过一个真实崩溃 dump 并定位到函数

<details>
<summary>～～旧版阶段二（09-07 版，Electron 方向，已作废）～～</summary>

| 周 | 主线 | 副线 | 周末深度 |
|---|---|---|---|
| 7 | Electron 主进程深度 + Node 集成 | C++ 并发基础（线程/mutex） | Side project 立项：AI 桌面助手 |
| 8 | Electron 渲染进程 + Web API | C++ condition_variable | Side project：UI 骨架 |
| 9 | Electron IPC 深度 + Context Isolation | C++ 线程池设计 | Side project：Chat UI + IPC |
| 10 | Electron 原生模块（N-API）| C++17 移动语义实战 | Side project：接入 llama.cpp CLI |
| 11 | Electron 打包 + 自动更新 | Chromium V8 与 JS 引擎入门 | Side project：本地对话可跑通 |
| 12 | Electron 阶段验收 + 性能优化 | ~~第二篇博客写作~~ 🚫 移出（09-29） | Side project：MVP 演示 |

旧门禁（全部作废）：Electron 4 大机制能改代码 / Side project MVP 可演示 / C++11 并发达 L2 / 累计 2 篇博客。
**其中「C++11 并发达 L2」是唯一存活项，已提升为新阶段二的头号门禁。**

</details>

## 阶段三：~~AI 集成 + 简历工程（第 13-18 周）~~ 🔴 10-15 改写：Chromium 本体 + 工程链

> ⚠️ **本阶段 AI 段处置待本人定**（A 移出 / B 压缩 2 周 / C 原样保留）。
> 下表按**选项 B** 预排（AI 占 W17-W18 两周），**他若选 A 或 C，这张表要重排。**

### 主题分布（10-15 预排版，待 AI 段决定后定稿）

| 周 | 上午 C++ / Chromium 主线 | 下午 | 周末深度 |
|---|---|---|---|
| 13 | **Chromium 多进程模型源码级**：进程启动、`RenderProcessHost`、site isolation | 读 Chromium 官方 `docs/` 对应章节 + 对照 q-fw CEF 实现 | 画一张「从点链接到新进程」的全链路图 |
| 14 | **Mojo IPC**：接口定义、消息管道、与手写 IPC 的区别 | 对照 q-fw 的 `ipc/` 手写管道，写出差异表 | 用 Mojo 跑一个最小示例（如环境允许） |
| 15 | **任务调度**：`base::TaskRunner` / `SequencedTaskRunner` / 线程池、`PostTask` | q-fw `base/` 里这套怎么被用的（实查调用点） | 把阶段二自写的线程池与 `base` 的对照 |
| 16 | **沙箱与内存分配器**：沙箱层级、PartitionAlloc / MiraclePtr | 对照 q-fw 的 CEF 沙箱配置 | **Boss 抓 20 个 Chromium 内核 / C++ 基础设施岗 JD 做统计** |
| 17 | 🔴 待定（AI 段 B 方案：LangChain/RAG 原理速通，只求能聊） | JD 反向补短板清单 | 简历 v1 起草 |
| 18 | 🔴 待定（AI 段 B 方案：Agent / tool calling 原理） | 阶段三验收闭卷 | 简历 v1 定稿 + 项目讲解稿 5 分钟版 |

**阶段三门禁（10-15 改写）**：
- [ ] 能画 Chromium 多进程 + Mojo + 任务调度三张图并口述取舍
- [ ] 一个自己写的 C++/Chromium 侧小工具（替代原 Electron side project 的「可展示产出」位）
- [ ] 简历 v1 通过至少 2 位同行 review，**岗位口径 = Chromium 内核 / C++ 基础设施**
- [ ] JD 分析报告（20 个岗）+ 短板补强清单

<details>
<summary>～～旧版阶段三（09-07 版，AI 集成 + Electron side project，已失效）～～</summary>

| 周 | 主线 | 副线 | 周末深度 |
|---|---|---|---|
| 13 | 尚硅谷 Transformer 章节复习 | Side project：加流式响应 | 简历 v0 起草 |
| 14 | LangChain 核心 | Side project：加会话记忆 | 简历 v0 完成 + 找同行 review |
| 15 | RAG 原理 + 实践 | Side project：加本地知识库 RAG | ~~第三篇博客~~ 🚫 移出（09-29） |
| 16 | Agent 与 tool calling | Side project：加简单 Agent 能力 | Boss 抓 20 个 JD 分析 |
| 17 | 微调原理（LoRA/QLoRA） | Side project：优化 + 打包 | JD 反向补短板清单 |
| 18 | AI 阶段验收 + 项目答辩排练 | ~~第四篇博客~~ 🚫 移出（09-29） | 简历 v1 定稿 |

旧门禁（RAG 架构图 / Side project v1 可分发 / 简历 v1 review / 4 篇博客）——
**「简历 v1 review」存活并保留，其余随方向作废。**

</details>

## 阶段四：面试冲刺 + 决策（第 19-24 周）

### 主题分布

| 周 | 主线 | 副线 |
|---|---|---|
| 19 | **简历投递（岗位口径：Chromium 内核 / C++ 基础设施）** + 面试八股整理 | q-fw 吃透笔记维护 ~~+ 第五篇博客~~ 🚫 移出（09-29） |
| 20 | 第 1-3 轮面试 | 面试复盘 + 简历微调 |
| 21 | 第 4-6 轮面试 + 系统设计题准备 | 短板专项补强 |
| 22 | 第 7-10 轮面试 | 面试题库沉淀 |
| 23 | Offer 谈判 + 背调准备 | 离职准备（如决定跳） |
| 24 | 决策 + 收尾 + 半年总结 | ~~写半年总结博客~~ 🚫 移出（09-29） |

**阶段门禁（第 24 周末验收）**：
- [ ] 主动投递 ≥20 家，进入面试 ≥10 家
- [ ] 拿到 ≥1 个 ≥28K 的 offer，或明确"不满意继续等"的判断
- [ ] ~~累计 5 篇技术博客~~ 🚫 **移出训练计划（09-29）**
- [ ] 半年总结文档 + 能力矩阵终版

## 时间投入统计规则

每周日晚在 `daily/history/YYYY-MM-DD-weekly.md` 里填：
- 本周实际投入总小时数（区分工作日/周末）
- 完成任务清单
- 未完成任务及原因
- 下周微调

**连续 2 周低于 10 小时**：启动"最小可完成版"——只保留每天 30 分钟核心任务（当阶段主线），其他全部延后到下阶段。

## 与旧计划的对应

- 旧 `roadmap-12-weeks.md` → 归档到 `plan/archive/`，本文件替代它
- 旧 `roadmap-6-12-months.md` → 归档，本文件替代
- 旧 `plan/project-selection.md` → 归档，被 `plan/side-project-ai-desktop.md` 替代
- 旧 `plan/interview-and-resume.md` → 归档，被 `plan/job-hunt-track.md` 替代
- `plan/baseline.md` / `plan/learning-loop.md` / `plan/competency-matrix.md` → 保留，方法论仍适用
