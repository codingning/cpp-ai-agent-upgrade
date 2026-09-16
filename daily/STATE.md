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
- **当前日期**：2026-09-16（周三）= **W2D3**
- **今日状态**：W2D3（09-16）**部分完成**，约 110min（上午约 10:15-11:25、下午约 13:50-14:30，按文件 mtime 与对话打卡推算）。上午 ✅ Rule of Zero 实验文件 `week-02/day3_rule_of_zero.cpp`（150 行，Trace 类 + rule1/rule2/rule3 + Test1~Test4），教练实跑验证：0 error、4 条 C4996、退出码 0；**Test1 vs Test2 对照成立**——只多写一行 `~rule2() = default`，`std::move` 即静默退化为拷贝。闭卷三问只答出第 1 问（措辞不准），第 2、3 问因 Rule of 0/3/5 无索引答不出；C++98/C++11 分组答错（把拷贝赋值与移动构造对调）。下午 ⚠️ A4 只完成第一步（实删 preload + DevTools Console 抄回六行真实报错 + 两轮对照，数据质量高），**sandbox.md 未读、三问未答**；`main.js`/`preload.js` 实验后已还原（`git diff HEAD` 为空），Electron 侧无代码产出。**收尾环节当日全部缺失**：三仓零 commit、记录文件未建、STATE/current 未更新，由教练 23:00 依实跑证据补写（闭卷自答空缺处未代写）。**同一方法论毛病第三次出现**：「我看的指标真能反映我想测的东西吗」没问——09-15 traits 输出、09-15 typeid、09-16 `npm start` 终端无报错，已跨语言（C++→JS），属方法问题非知识问题
- **能力等级**：C++ **L1 → L2-**（能设计对照实验、能用实跑数据推翻自己和教练的判断；但闭卷复述仍不稳定）；Chromium/Electron **L1 → L1+**。7 天复测日 **2026-09-22**：闭卷说清 5 个特殊成员函数 + 生成规则方向性，过则提 L2
- **W1 欠账（9 条，已重排进 W2）**：A 概念 4 条（异常路径 RAII / 裸指针观察语义 / move-from 状态 / preload+contextIsolation）→ 周三、周四；B 产出 4 条（MyUniquePtr 单元测试 / Chat UI v0 / 进程模型手绘图+`docs/` / 博客大纲+`blog-drafts/`）→ 周四、周六；C 索引缺失 1 条（Rule of 3/5 数不出来）→ 周五收束日
- **本周门禁**：见 `plan/weekly/week-02.md` 末尾"本周门禁"
- **W1 门禁验收结果（09-15 补做）**：1 MyUniquePtr ✅；2 GitHub ≥2 commit ✅；3 Electron 主/渲染口述 ✅（下午读完 Chromium 后重答通过）；4 记录齐全 ✅（09-12/09-13 已补建，周复盘已补写）
- **下一步**：W2D4（09-17 周四）上午开场 15min 清今天的尾（Rule of 0/3/5 用自己的话重答 + C++98/C++11 分组纠错 + A3 两条结论 + Test3「哪个成员删掉了拷贝构造」），剩余时间做 A1 异常路径 RAII + B1 MyUniquePtr `assert` 单元测试（门禁项）；下午优先补 A4 第二、三步（读 `sandbox.md` + 三问），Menu API 顺延周六
- **累计投入**：约 15.3 小时（W1 实际：09-08 90min + 09-09 90min + 09-10 45min + 09-11 105min = 5.5h，09-07/09-12/09-13 为 0；W2：09-14 105min + 09-15 180min + 09-16 110min = 6.6h。注：09-09~09-11 时长为 09-15 补记时估算，09-16 为按 mtime 推算）
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
