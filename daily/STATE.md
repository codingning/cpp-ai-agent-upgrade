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
- **当前阶段**：阶段一 · 基础重建 · Week 02
- **Week 02 起止**：2026-09-14（周一）~ 2026-09-20（周日）
- **本周主题**：C++ Rule of 3/5（String → Vector<T>）+ Chromium 多进程架构 + Electron 主进程 API
- **当前日期**：2026-09-14（周一）= **W2D1**
- **今日状态**：W1D1~W1D5 C++ 全部完成；**Electron 侧欠账三项**：Chatbox 主进程源码阅读（W1D4 起顺延 2 次）、Chat UI v0、W1D6/W1D7（09-12 周六深度日、09-13 周日复盘）无记录
- **欠账重排**：Electron 源码阅读 → 09-14 下午（不再顺延）；Chat UI v0 → 本周六下午；W1 门禁验收 + W1 周复盘 → 并入 09-20 周日（与 W2 复盘合并）
- **本周门禁**：见 `plan/weekly/week-02.md` 末尾"本周门禁"（W1 门禁未验收，一并留到 09-20）
- **下一步**：W2D1 上午手写 String（Rule of 3，深拷贝/自赋值/赋值三验收）；下午 Chatbox 主进程源码阅读 + 启动流程图
- **累计投入**：约 6.5 小时（W1D1~W1D5；W1D4 按 0.75h、W1D5 按 0.75h 计；09-12/09-13 无投入）
- **累计博客**：0 篇（目标 24 周 5 篇）
- **Side project**：已启动 `F:\code\ai-desktop-assistant`（GitHub: codingning/ai-desktop-assistant, private）。已完成 IPC 双向通信（openFile / getCurrentData / helloName）；TypeScript 化暂缓
- **简历状态**：无（Week 4 完成 v0 保底版）

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
