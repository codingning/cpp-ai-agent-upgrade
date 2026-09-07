# 24 周路线图（2026-09-07 版）

**目标**：2027-03 前完成 22K → 28-32K 跳槽，方向 Electron/Chromium 客户端 + AI 集成。

**时间预算**：每天 1.5 小时（工作日）+ 每周末 6 小时 = 每周 13 小时。缺席不追赶，连续 2 周未达 10 小时启动最小可完成版。

## 四阶段总览

| 阶段 | 周次 | 主题 | 核心交付 | 阶段门禁 |
|---|---|---|---|---|
| 一 | 1-6 | 基础重建 | C++ 底座 + Electron 入门 + Chromium 概念地图 | C++17 RAII/STL 达 L2；Electron hello-world 跑通；Chromium 架构能画图口述 |
| 二 | 7-12 | Electron 深化 + Side project 启动 | Electron 主/渲染/IPC/原生模块深度 + AI 桌面助手 v0 | Electron 4 大机制能改代码；Side project MVP 可演示 |
| 三 | 13-18 | AI 集成 + 简历工程 | LangChain/RAG/微调理解 + Side project v1 + 简历初稿 | Side project 集成 LLM 可用；简历 v1 可投；开始看 JD |
| 四 | 19-24 | 面试冲刺 + 决策 | 简历定稿 + 主动投递 + 面试 5-10 家 + 谈判 | 拿到 ≥1 个满意 offer 或明确决策继续/离开 |

## 每周固定节奏

**工作日（周一到周五，每天 1.5 小时）**：
- 30 分钟：C++ 底座（第 1-12 周）或 AI 章节（第 13-18 周轮换）
- 45 分钟：Electron/Chromium 主线学习或 side project 编码
- 15 分钟：写当日记录 + 更新 STATE.md

**周六（4 小时）**：
- 深度编码时段：side project 主开发时间
- 或深度阅读时段：Chromium/Electron 源码切片

**周日（2 小时）**：
- 1 小时：技术博客写作
- 1 小时：本周复盘 + 下周计划微调

**每周固定产出**：
- 5 天工作日记录（有学习或缺席都要记）
- 1 次周日复盘写在 `daily/history/YYYY-MM-DD-weekly.md`
- 至少一段可运行代码 commit
- 至少一个技术点闭卷复述

## 阶段一：基础重建（第 1-6 周）

### 主题分布

| 周 | 主线 | 副线 | 周末深度 |
|---|---|---|---|
| 1 | C++ RAII/生命周期 | Electron 概念 + 环境搭建 | Electron hello-world |
| 2 | C++ 拷贝/移动/Rule of 5 | Chromium 架构总览阅读 | 画 Chromium 进程模型图 |
| 3 | C++ STL 常用容器 | Electron 主进程 API | 写 Electron 简易记事本 |
| 4 | C++17 结构化绑定/optional/variant | Electron 渲染进程 + preload | 记事本加持久化 |
| 5 | C++ 智能指针深度 | Electron IPC 机制 | 记事本主/渲染进程通信 |
| 6 | C++ 阶段验收 | Electron 阶段验收 + Chromium 复习 | 写第一篇技术博客草稿 |

**阶段门禁（第 6 周末验收）**：
- [ ] C++ 能不看资料实现 RAII 资源包装器 + Rule of 5 + 单元测试
- [ ] Electron 能独立搭建项目、写主/渲染进程、用 IPC 通信
- [ ] Chromium 能画出 Browser/Renderer/GPU/Utility 进程模型图并口述通信路径
- [ ] 完成 1 篇技术博客草稿（1500 字以上）

## 阶段二：Electron 深化 + Side project（第 7-12 周）

### 主题分布

| 周 | 主线 | 副线 | 周末深度 |
|---|---|---|---|
| 7 | Electron 主进程深度 + Node 集成 | C++ 并发基础（线程/mutex） | Side project 立项：AI 桌面助手 |
| 8 | Electron 渲染进程 + Web API | C++ condition_variable | Side project：UI 骨架 |
| 9 | Electron IPC 深度 + Context Isolation | C++ 线程池设计 | Side project：Chat UI + IPC |
| 10 | Electron 原生模块（N-API）| C++17 移动语义实战 | Side project：接入 llama.cpp CLI |
| 11 | Electron 打包 + 自动更新 | Chromium V8 与 JS 引擎入门 | Side project：本地对话可跑通 |
| 12 | Electron 阶段验收 + 性能优化 | 第二篇博客写作 | Side project：MVP 演示 |

**阶段门禁（第 12 周末验收）**：
- [ ] Electron 4 大机制（主/渲染/IPC/原生）能改代码不是只会用
- [ ] Side project：AI 桌面助手 MVP 版，能启动、对话、显示响应
- [ ] C++11 并发达 L2（线程池能自己写）
- [ ] 累计发表 2 篇技术博客

## 阶段三：AI 集成 + 简历工程（第 13-18 周）

### 主题分布

| 周 | 主线 | 副线 | 周末深度 |
|---|---|---|---|
| 13 | 尚硅谷 Transformer 章节复习 | Side project：加流式响应 | 简历 v0 起草 |
| 14 | LangChain 核心 | Side project：加会话记忆 | 简历 v0 完成 + 找同行 review |
| 15 | RAG 原理 + 实践 | Side project：加本地知识库 RAG | 第三篇博客 |
| 16 | Agent 与 tool calling | Side project：加简单 Agent 能力 | Boss 抓 20 个 JD 分析 |
| 17 | 微调原理（LoRA/QLoRA） | Side project：优化 + 打包 | JD 反向补短板清单 |
| 18 | AI 阶段验收 + 项目答辩排练 | 第四篇博客 | 简历 v1 定稿 |

**阶段门禁（第 18 周末验收）**：
- [ ] 能画出 RAG 系统架构图并解释每个组件的取舍
- [ ] Side project v1：可打包、可分发、集成本地 LLM + RAG + 简单 Agent
- [ ] 简历 v1 通过至少 2 位同行 review
- [ ] 累计 4 篇技术博客发表到公开平台

## 阶段四：面试冲刺 + 决策（第 19-24 周）

### 主题分布

| 周 | 主线 | 副线 |
|---|---|---|
| 19 | 简历投递 + 面试八股整理 | Side project 维护 + 第五篇博客 |
| 20 | 第 1-3 轮面试 | 面试复盘 + 简历微调 |
| 21 | 第 4-6 轮面试 + 系统设计题准备 | 短板专项补强 |
| 22 | 第 7-10 轮面试 | 面试题库沉淀 |
| 23 | Offer 谈判 + 背调准备 | 离职准备（如决定跳） |
| 24 | 决策 + 收尾 + 半年总结 | 写半年总结博客 |

**阶段门禁（第 24 周末验收）**：
- [ ] 主动投递 ≥20 家，进入面试 ≥10 家
- [ ] 拿到 ≥1 个 ≥28K 的 offer，或明确"不满意继续等"的判断
- [ ] 累计 5 篇技术博客
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
