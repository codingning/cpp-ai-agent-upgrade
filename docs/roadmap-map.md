# 24周路线 22K→28-32K
## 目标
### 2027-03 前跳槽成功
- 方向：Electron/Chromium 客户端 + AI 集成
- 时间预算：工作日 1.5h × 5 + 周末 6h = 13h/周
- 熔断：连续 2 周 <10h → 启动最小可完成版（每天只保留 30min 主线）
## 阶段一 W1-6 基础重建 🔵当前
### 门禁（W6 验收）
- C++ 不看资料实现 RAII 包装器 + Rule of 5 + 单元测试
- Electron 能独立搭项目、写主/渲染进程、用 IPC 通信
- Chromium 能画进程模型图并口述通信路径
- 1 篇技术博客草稿（1500字+）
### W1 RAII/生命周期 ✅已过
- 主线：C++ RAII/生命周期
- 副线：Electron 概念 + 环境搭建
- 周末：Electron hello-world
### W2 拷贝/移动/Rule of 5 🔵进行中
- 主线：C++ 拷贝/移动/Rule of 5
- 副线：Chromium 架构总览阅读
- 周末：画 Chromium 进程模型图 ❌欠着
- 已达成：A1 异常路径 RAII、B1 MyUniquePtr 测试
### W3 STL 容器
- 主线：C++ STL 常用容器
- 副线：Electron 主进程 API
- 周末：写 Electron 简易记事本
### W4 C++17 特性
- 主线：结构化绑定/optional/variant
- 副线：Electron 渲染进程 + preload
- 周末：记事本加持久化
- ⚠️ 简历 v0 保底版
### W5 智能指针深度
- 主线：C++ 智能指针深度
- 副线：Electron IPC 机制
- 周末：记事本主/渲染通信
### W6 阶段验收
- C++ 阶段验收 + Electron 阶段验收 + Chromium 复习
- 周末：第一篇技术博客草稿
## 阶段二 W7-12 Electron深化+Side project
### 门禁（W12 验收）
- Electron 4 大机制能改代码（不是只会用）
- Side project MVP：能启动、对话、显示响应
- C++11 并发达 L2（线程池能自己写）
- 累计 2 篇博客
### W7 主进程深度
- 主线：Electron 主进程 + Node 集成
- 副线：C++ 并发基础（线程/mutex）
- 周末：Side project 立项
### W8 渲染进程
- 主线：Electron 渲染进程 + Web API
- 副线：C++ condition_variable
- 周末：Side project UI 骨架
### W9 IPC深度
- 主线：IPC 深度 + Context Isolation
- 副线：C++ 线程池设计
- 周末：Chat UI + IPC
### W10 原生模块
- 主线：Electron 原生模块（N-API）
- 副线：C++17 移动语义实战
- 周末：接入 llama.cpp CLI
### W11 打包更新
- 主线：Electron 打包 + 自动更新
- 副线：Chromium V8 与 JS 引擎入门
- 周末：本地对话可跑通
### W12 阶段验收
- Electron 阶段验收 + 性能优化
- 副线：第二篇博客
- 周末：MVP 演示
## 阶段三 W13-18 AI集成+简历工程
### 门禁（W18 验收）
- 能画 RAG 架构图并解释每个组件取舍
- Side project v1：可打包分发、集成本地 LLM + RAG + Agent
- 简历 v1 通过 ≥2 位同行 review
- 累计 4 篇博客
### W13 Transformer
- 主线：尚硅谷 Transformer 章节
- 副线：Side project 流式响应
- 周末：简历 v0 起草
### W14 LangChain
- 主线：LangChain 核心
- 副线：Side project 会话记忆
- 周末：简历 v0 + 同行 review
### W15 RAG
- 主线：RAG 原理 + 实践
- 副线：Side project 本地知识库
- 周末：第三篇博客
### W16 Agent
- 主线：Agent 与 tool calling
- 副线：Side project Agent 能力
- 周末：Boss 抓 20 个 JD 分析
### W17 微调原理
- 主线：LoRA/QLoRA
- 副线：Side project 优化 + 打包
- 周末：JD 反向补短板清单
### W18 阶段验收
- AI 阶段验收 + 项目答辩排练
- 副线：第四篇博客
- 周末：简历 v1 定稿
## 阶段四 W19-24 面试冲刺
### 门禁（W24 验收）
- 主动投递 ≥20 家，进入面试 ≥10 家
- 拿到 ≥1 个 ≥28K offer，或明确「不满意继续等」
- 累计 5 篇博客
- 半年总结 + 能力矩阵终版
### W19 投递起步
- 简历投递 + 面试八股整理
- 副线：第五篇博客
### W20 面试1-3轮
- 面试复盘 + 简历微调
### W21 面试4-6轮
- 系统设计题准备 + 短板专项
### W22 面试7-10轮
- 面试题库沉淀
### W23 Offer谈判
- 背调准备 + 离职准备
### W24 决策收尾
- 半年总结博客
## 每周固定节奏
### 工作日 1.5h
- 30min C++ 底座（W1-12）/ AI 章节（W13-18）
- 45min Electron/Chromium 主线 或 side project 编码
- 15min 写记录 + 更新 STATE.md
- ⚠️ 1.5h 是保底不是上限
### 周六 4h
- 深度编码（side project）或 深度阅读（源码切片）
- ⚠️ 依赖 ToDesk 远程，未实测
### 周日 2h
- 1h 技术博客写作
- 1h 本周复盘 + 下周微调
### 每周必产出
- 5 天工作日记录（缺席也要记）
- 1 次周日复盘
- ≥1 段可运行代码 commit
- ≥1 个技术点闭卷复述
## 里程碑时间轴
### 2026-10月中 W6 阶段一门禁
### 2026-11月底 W12 MVP 可演示
### 2027-01月中 W18 简历 v1 定稿
### 2027-02 W19 开始投递
### 2027-03 W24 决策点
