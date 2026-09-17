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
- **当前日期**：2026-09-17（周四）= **W2D4**
- **今日状态**：W2D4（09-17）**基本完成，本周最扎实的一天**，约 200min（按 mtime 三段：10:30-11:03 / 14:00-14:21 / 17:35-18:12，另 21:34 重编一次）——**大幅超出 1.5h 保底**。09-16 欠账**全清**：Rule of 0/3/5 闭卷重答通过、C++98/C++11 分组纠正、Test3 传染机制说清、A3 两条结论补上。✅ A1 `week-02/day4_exception_raii.cpp` + ✅ B1 `week-02/day4_uniqueptr_test.cpp`（commit `ff3a0d1`）——**W2 门禁两项达成**。✅ 本日原定内容也动了手：`day4_noncopyable.cpp`，教练实跑 0 error / 1 条 C4189 / 退出码 0，`is_copy_constructible_v<Widget>`=0、`is_move_constructible_v<Widget>`=1 证明 mixin 生效；另自己用 `#ifdef USE_DELETE` 做出「`= delete` 禁某个重载被选中」的对照并抄回 C2280（这是 current.md 的提示项，做到了但没写进答案）。✅ A4 第二、三步（sandbox.md 两节 + 三句话 + 三问），并**自行补读** Electron 官方 sandbox / context-isolation 两篇（自己发现的缺口，值得记）。✅ 记录文件本人自写（09-16 是教练补的）。**遗留**：Menu 只写了 `menu.js` 未在 `main.js` require，菜单实际未生效；`= default` vs 什么都不写答成了生成规则、没答到「用户声明」；两处空白（move 翻车原因 / 析构 protected 的为什么）；Q11 与 Q12 自相矛盾（沙箱与 nodeIntegration 画等号）；`day4_noncopyable.cpp`、`menu.js` 未 commit；「今日一句话复述」连续第二天空缺；**元规则「运行前先写预测」第四次未执行**（代码注释只有事后抄回的报错，无事前预测——但 Menu 那题写了猜测，说明是只在被问到时才做）
- **能力等级**：C++ **L2-**（不变）——今天闭卷首次基本答对 Rule of 0/3/5 与 C++98/11 分组，索引缺失已补上；但「答非所问」（`= default` 那题）说明复述仍不稳定，等 09-22 七天复测再定。Chromium/Electron **L1+**（不变）——Q11/Q12 自相矛盾说明沙箱模型还没搭稳。7 天复测日 **2026-09-22**：闭卷说清 5 个特殊成员函数 + 生成规则方向性，过则提 L2
- **W1 欠账（9 条）→ 已清 7 条**：A 概念 4 条全清（异常路径 RAII ✅09-17 / 裸指针观察语义 ✅09-15 / move-from 状态 ✅09-17 / preload+contextIsolation ✅09-17）；B 产出 4 条清 1（MyUniquePtr 单元测试 ✅09-17；Chat UI v0、进程模型图+`docs/`、博客大纲+`blog-drafts/` → 周六）；C 索引缺失 1 条 ✅09-17 闭卷重答通过
- **本周门禁**：见 `plan/weekly/week-02.md` 末尾"本周门禁"。已达成：A1 异常路径 RAII ✅、B1 MyUniquePtr 单元测试 ✅
- **W1 门禁验收结果（09-15 补做）**：1 MyUniquePtr ✅；2 GitHub ≥2 commit ✅；3 Electron 主/渲染口述 ✅（下午读完 Chromium 后重答通过）；4 记录齐全 ✅（09-12/09-13 已补建，周复盘已补写）
- **下一步**：W2D5（09-18 周五）= **🔵 本周收束日**，见 `daily/current.md`。上午 40min 闭卷默写「特殊成员函数」整张表（6 个函数签名 + Rule 0/3/5 关系 + 6×6 抑制表 + move 退化场景）——这是 09-22 七天复测的预演；下午 50min 收束：画 W1+W2 C++ 概念关系图存 `docs/cpp-concept-map-w2.jpg`（每个节点必须能追溯到自己写过的文件）+ 核对 progress.jsonl + 本周门禁自测。**开场先花 10min 清 09-17 的三处空白 + 把 `day4_noncopyable.cpp`/`menu.js` commit + 补写一句话复述**。另：**09-19 前必须实测 ToDesk 可用性**，决定周六排多少时长
- **累计投入**：约 18.6 小时（W1 实际：09-08 90min + 09-09 90min + 09-10 45min + 09-11 105min = 5.5h，09-07/09-12/09-13 为 0；W2：09-14 105min + 09-15 180min + 09-16 110min + 09-17 200min = 9.9h。注：09-09~09-11 时长为 09-15 补记时估算，09-16/09-17 为按 mtime 推算）
- **周末方案变更**：09-12/09-13 断档根因为公司代理更新后家庭电脑无法直连办公机。**改用 ToDesk 远程**，09-19（周五）前确认可用性；周六时长先按 90min 保守排，拿到真实数据后再定，不按原计划 4h 排
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
