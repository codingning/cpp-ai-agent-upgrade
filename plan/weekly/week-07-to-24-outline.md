# Week 07-24 纲要（阶段二/三/四简要周计划）

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
