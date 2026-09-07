# Side Project：AI 桌面助手（本地 LLM + Electron）

## 目标

半年内产出一个**可演示、可打包分发、可写入简历**的 Electron AI 桌面助手，作为求职时的核心作品。

**产品定位**：类似 Chatbox / LM Studio / Cherry Studio 的简化版，但突出**你自己的技术决策**，不是简单套壳。

**为什么选这个项目**：
1. 完美命中"Electron + AI 集成"求职主叙事
2. 涉及 Electron 全部核心机制（主/渲染/IPC/原生模块/打包），学习和产出双赢
3. 集成本地 LLM 展示 AI 能力，不依赖云端 API
4. 8G 4060 完全够跑（llama.cpp 量化模型）
5. 6 个月完成 MVP 是现实的

## 技术栈

**必选（学习目标）：**
- Electron（主框架，最新稳定版）
- TypeScript（类型安全，面试加分）
- React（渲染层 UI，用最主流的）
- Node.js child_process 或 N-API（调用 llama.cpp）
- llama.cpp（本地 LLM 推理，命令行 or C++ 绑定）

**选做（时间允许）：**
- Zustand / Redux（状态管理）
- SQLite（本地对话存储）
- LangChain.js（Agent 层）
- Chroma / lancedb（本地向量库做 RAG）

**明确不做：**
- 云端 API 集成（如 OpenAI API）——不体现你的价值
- Web 版（浏览器可用版）——脱离桌面主叙事
- 移动端——超出范围
- 自己训练模型——超出能力范围

## 里程碑（12 个双周版本）

| 版本 | 周次 | 交付 | 演示价值 |
|---|---|---|---|
| v0.1 | 7-8 | Electron 骨架 + Chat UI 静态版 | 项目跑起来了 |
| v0.2 | 9-10 | 主/渲染进程通信打通 + 消息状态管理 | 能发消息（假回复） |
| v0.3 | 11-12 | llama.cpp CLI 调用 + 真实 LLM 回复 | **MVP：能真的对话** |
| v0.4 | 13-14 | 流式响应 + 打字机效果 + Markdown 渲染 | 体验接近成品 |
| v0.5 | 15 | 会话记忆 + 多会话切换 + SQLite 持久化 | 完整对话产品 |
| v0.6 | 16 | 本地知识库 RAG（选一个方向：代码知识库/个人文档/技术笔记）| RAG 展示 AI 能力 |
| v0.7 | 17 | Agent 能力：文件操作/网页抓取 tool（选 1-2 个）| Agent 展示 |
| v0.8 | 18 | 性能优化 + 打包分发 + README 完善 | **v1：可分发** |
| 收尾 | 19-24 | Bug 修复、简历项目描述、演示视频、面试讲解稿 | 求职材料 |

## 项目结构（建议）

```
ai-desktop-assistant/
├── src/
│   ├── main/              # Electron 主进程
│   │   ├── index.ts       # 入口
│   │   ├── llm/           # LLM 调用层（llama.cpp）
│   │   ├── ipc/           # IPC 处理
│   │   ├── storage/       # SQLite 持久化
│   │   └── rag/           # RAG 层
│   ├── renderer/          # Electron 渲染进程
│   │   ├── App.tsx
│   │   ├── components/
│   │   ├── store/         # 状态管理
│   │   └── styles/
│   └── shared/            # 主/渲染共享类型
├── native/                # 可选：C++ N-API 原生模块
├── models/                # 本地模型存放（gitignore）
├── docs/
│   ├── architecture.md    # 架构文档（面试用）
│   ├── decisions/         # ADR 决策记录
│   └── benchmarks/        # 性能测试报告
├── package.json
├── tsconfig.json
├── electron-builder.yml
└── README.md
```

## 简历亮点提炼（提前想好）

在开发过程中，主动设计以下"技术决策点"，最后写进简历：

1. **为什么用 llama.cpp 而不是 Ollama** → 决策记录：性能对比、集成方式对比、可控性对比
2. **为什么用 child_process 而不是 N-API** → 决策记录：开发效率 vs 性能 vs 稳定性
3. **IPC 通信如何设计** → 决策记录：Context Isolation 下的安全 IPC 模式
4. **流式响应如何实现** → 决策记录：主进程流式输出到渲染进程的方案
5. **RAG 如何选型** → 决策记录：向量库选择、embedding 模型选择、chunk 策略
6. **性能问题如何定位** → 决策记录：Chrome DevTools + Electron 性能分析
7. **打包体积如何优化** → 决策记录：native 模块处理、模型分离下载

**每个决策点写一份 ADR（Architecture Decision Record），放在 `docs/decisions/`**——面试时能拿出来讲的干货。

## 简历项目描述（草稿）

> **AI 桌面助手（Electron + 本地 LLM）** · 2026.09 - 2027.03 · 个人项目
>
> 独立设计并开发的 Electron 桌面 AI 助手，集成本地 llama.cpp 推理引擎，支持流式对话、多会话管理、本地知识库 RAG 和 Agent 工具调用。
>
> **技术栈**：Electron / TypeScript / React / Node.js / llama.cpp / SQLite / LangChain.js
>
> **核心工作**：
> - 主/渲染进程架构设计，实现 Context Isolation 下的安全 IPC 通信协议
> - 集成 llama.cpp 本地推理（[决策]：对比 Ollama/child_process/N-API 三种集成方案，选定 X 方案，理由 XXX）
> - 实现流式响应管道，主进程流式读取 → IPC 增量推送 → 渲染进程打字机渲染
> - 基于 Chroma 实现本地文档 RAG，chunk 策略采用 XXX，检索准确率提升 XXX
> - 使用 electron-builder 完成 Windows 打包和自动更新配置
>
> **可交付物**：GitHub 开源仓库（链接）、演示视频（链接）、7 份 ADR 决策记录、性能测试报告

## 反模式（不要做）

- ❌ 抄袭 Chatbox / Cherry Studio 源码——面试官一眼看穿
- ❌ 只做 UI 好看不管技术深度——你的目标是"技术决策可讲"
- ❌ 追求功能全——功能少但每个都能讲清楚，胜过功能多但都是抄的
- ❌ 用 Cursor 全代写不理解代码——AI 辅助可以，但每行代码你都要能解释
- ❌ 用 Claude Code 生成 ADR——ADR 是你的技术判断，AI 生成的看得出来

## 与学习进度的绑定

项目开发是**主要学习载体**，不是"学完再做"：

- 学 Electron IPC → 立即在项目里实现真实 IPC
- 学 Node child_process → 立即用来调 llama.cpp
- 学 React 状态管理 → 立即用在 Chat UI
- 学 RAG → 立即加到项目里

**"边学边造"是这个方案的核心逻辑**，因为你的 Chromium 历史经验难以整理成博客，只能靠 side project 制造可讲的技术决策。

## 关键约束

1. **代码质量优先于速度**：宁可慢，也要每行代码你能解释
2. **每个双周里程碑必须可演示**：卡壳时降级功能，不要跳里程碑
3. **文档同步写**：ADR、README、架构图与代码同步产出，最后一次性补是不可能的
4. **开源到 GitHub**：从第 1 周起就 push 到公开仓库，commit 历史本身是求职证据
5. **避免过度设计**：不引入不必要的抽象层、微服务、复杂状态机——面试官反感"个人项目过度工程"
