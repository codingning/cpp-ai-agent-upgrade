# Chromium/Electron + AI 集成 · 求职升级训练系统

一个为期 24 周的证据驱动训练系统，目标：**22K → 28-32K 跳槽**，方向 **Electron/Chromium 桌面客户端 + AI 应用集成**。

**当前版本**：2026-09-07 版战略（替代原 C++ AI 推理基础设施方向，理由见 `plan/STRATEGY-2026-09-07.md`）。

## 入口顺序

按以下顺序读，读完就知道下一步做什么：

1. **`plan/STRATEGY-2026-09-07.md`** — 为什么走这条路、目标是什么
2. **`plan/roadmap-24-weeks.md`** — 24 周总路线 + 每阶段门禁
3. **`plan/weekly/week-01.md`** — 当周详细日任务（我现在处于 Week 1）
4. **`daily/STATE.md`** — 当前训练状态（累计投入、当前阶段、下一步）
5. **`daily/current.md`** — 今日具体任务

## 24 周路线一览

| 阶段 | 周次 | 主题 | 核心交付 |
|---|---|---|---|
| 一 | 1-6 | 基础重建 | C++17 到 L2 + Electron 入门 + 第 1 篇博客 |
| 二 | 7-12 | Electron 深化 + Side project | AI 桌面助手 MVP + 第 2 篇博客 |
| 三 | 13-18 | AI 集成 + 简历工程 | Side project v1 + 简历 v1 + 第 3、4 篇博客 |
| 四 | 19-24 | 面试冲刺 | 拿 offer + 第 5 篇博客 |

## 时间投入

- 工作日：每天 1.5 小时（30 分钟 C++ + 45 分钟 Electron/AI 主线 + 15 分钟记录）
- 周末：周六 4 小时深度 + 周日 2 小时复盘
- 每周合计：13 小时

## 三条腿分配

| 腿 | 比例 | 每周时长 | 核心产出 |
|---|---|---|---|
| Electron/Chromium 主线 | 45% | 6h | 3-5 篇技术博客 + 1 个 side project |
| C++ 底座补强 | 25% | 3h | L2-L3 能力矩阵 + 面试可讲 |
| AI 应用能力 | 20% | 2.5h | LangChain/RAG/Agent + AI 集成实验 |
| 求职工程 | 10% | 1.5h | 简历、面试、市场调研 |

## Side project：AI 桌面助手

**核心求职作品**。Electron + 本地 llama.cpp + LangChain，从 Week 7 立项到 Week 18 v1 完成。设计详见 `plan/side-project-ai-desktop.md`。

## 记录命令

每日记录（已有脚本可复用）：
```bash
python scripts/training.py record --minutes 90 --completed "完成 Week1 Day1" --blocker "无" --self-score 2 --phase A
```

## 学习方法论（不变）

- 每单元遵循：诊断 → 主资料 → 源码切片 → 实现 → 验证 → 复述
- 关键代码必须自己重写、解释、测试
- 7/21 天后复测才算掌握，只有 L4 证据能进简历
- 无学习日必须写记录说明"今日未训练"，不虚构

## 目录

- `plan/STRATEGY-2026-09-07.md` — 战略说明
- `plan/roadmap-24-weeks.md` — 24 周路线
- `plan/weekly/` — 周计划（Week 1-6 详细日任务；Week 7-24 周纲要）
- `plan/side-project-ai-desktop.md` — Side project 设计
- `plan/job-hunt-track.md` — 求职工程轨（简历、面试、投递）
- `plan/baseline.md` — 能力基线
- `plan/learning-loop.md` — 学习方法论
- `plan/competency-matrix.md` — L0-L4 能力矩阵
- `plan/archive/` — 归档的旧路线（原 AI infra 方向）
- `daily/STATE.md` — 训练续接状态
- `daily/current.md` — 今日任务
- `daily/history/` — 每日/每周复盘记录
- `curriculum/` — 训练单元（保留原有材料）
- `scripts/` — 训练脚本
- `assessment/`、`evidence/`、`labs/`、`projects/` — 保留原有目录

## 边界

不上传公司代码、凭据、密钥。训练代码只有进 `labs/` 或 `projects/` 才提交为证据。开源依赖固定版本核对许可。自动化只记录事实，不把"完成"升级为"掌握"。
