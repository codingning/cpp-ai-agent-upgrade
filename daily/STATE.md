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

## 当前状态

- **战略版本**：2026-09-07 版（Electron/Chromium + AI 集成方向，替代原 C++ AI 推理基础设施方向）
- **当前阶段**：阶段一 · 基础重建 · 第 1 周
- **本周主题**：C++ RAII 与生命周期 + Electron 环境搭建与 hello-world
- **当前日期**：2026-09-07（周日）
- **今日状态**：战略调整完成、24 周新路线落盘、Week 1 详细计划已就位；未开始 Week 1 具体任务
- **本周门禁**：见 `plan/weekly/week-01.md` 末尾"本周门禁"
- **下一步**：从周一开始执行 `plan/weekly/week-01.md` 的每日任务；今日为周日，可用 2 小时做本周任务预读 + Side project GitHub 仓库准备（可选）
- **累计投入**：0 小时（新路线起点）
- **累计博客**：0 篇（目标 24 周 5 篇）
- **Side project**：未启动（Week 1 周三启动）
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
