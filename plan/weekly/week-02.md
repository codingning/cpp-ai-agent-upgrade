# Week 02（第 2 周，2026-09-14 ~ 2026-09-20）

## 本周主题

**C++ 拷贝/移动/Rule of 5** + **Chromium 架构总览** + **Electron 主进程 API**

## 本周目标

- 掌握 C++ Rule of 0/3/5，理解默认特殊成员函数生成规则
- 能画出 Chromium 多进程架构图并口头讲解 5 分钟
- 熟悉 Electron 主进程核心 API：app、BrowserWindow、Menu、Tray

## 每日任务

### 周一（1.5 小时）

**C++ 30 分钟**：
- 学习 Rule of Three：拷贝构造、拷贝赋值、析构
- 手写一个 `String` 类（内部 char* + size_t），实现 Rule of 3
- 深拷贝 vs 浅拷贝的区别在哪一行代码上体现

**Chromium 45 分钟**：
- 阅读 [Chromium Architecture Overview](https://www.chromium.org/developers/design-documents/multi-process-architecture/)
- 用中文一句话解释：Browser Process / Renderer Process / GPU Process / Utility Process 各自做什么

**记录 15 分钟**

### 周二（1.5 小时）

**C++ 30 分钟**：
- 在 `String` 类基础上加 Rule of Five：移动构造、移动赋值
- 编译测试：`String a = "hello"; String b = std::move(a);` 后 a 的状态

**Chromium 45 分钟**：
- 继续 Chromium 架构：进程间用什么通信？（Mojo/IPC）
- 阅读 [Mojo Overview](https://chromium.googlesource.com/chromium/src/+/HEAD/mojo/README.md) 前 3 段
- 记录一个疑问，不深入

**记录 15 分钟**

### 周三（1.5 小时）

**C++ 40 分钟**：
- 学习 Rule of Zero：什么时候不需要写任何特殊成员函数
- 举 3 个例子：只用 STL 容器就 OK 的类
- 🔴 **补 A3**：move-from 对象的状态（W1 周五计划项，未做）
  - 在 Rule of Zero 的例子上顺带验：`std::move` 之后，源对象还能不能用？值是什么？
  - 关键词「有效但未指定」，要用实跑输出证明，不许只写结论

**Electron 50 分钟**：
- 🔴 **补 A4 优先**：为什么删掉 `preload.js` 后网页里访问 `process` 会失败？（W1D2 计划项，未做）
  - 动手：真的删掉 preload，跑一次，把报错原文抄下来
  - 再答：`contextIsolation` 是什么？它和 09-15 读的 Chromium 渲染进程沙箱是什么关系？
  - 这题和周二下午那篇是同一块知识的两面，连着做
- 原计划 [BrowserWindow API](https://www.electronjs.org/docs/latest/api/browser-window) 多窗口 → **降级为只读文档**，改代码顺延到周六

**记录 15 分钟**

### 周四（1.5 小时）

**C++ 40 分钟**：
- 学习 `= default` 和 `= delete`（09-15 已实测过一部分，本日补齐规则）
- 写一个 `NonCopyable` mixin 类
- 🔴 **补 A1 + B1（本周最重要的补课）**：异常路径下的 RAII + 单元测试
  - W1 周一计划项「为什么析构在错误路径也执行」、周二「边界测试：抛异常」，均未做
  - W1 门禁第 1 条原文要求「MyUniquePtr 含 move 语义**和单元测试**」，测试未做
  - 三条路径各写一个用例：正常返回 / 提前 return / **抛异常**，证明资源都被释放
  - 用 `assert` 断言，不许只用 `cout` 肉眼看（这是把「观察」升级成「测试」）
  - 关键词：栈展开（stack unwinding）

**Electron 50 分钟**：
- 学习 [Menu API](https://www.electronjs.org/docs/latest/api/menu)
- 在 side project 里加应用菜单：File / Edit / View / Help（先只有 UI）
- 🔴 **顺手清 TODO**：`main.js` 里 `win.on('closed')` 中的 `app.quit()` 删掉（多窗口场景会炸）

**记录 15 分钟**

### 周五（1.5 小时）· 🔵 本周收束日

> **改动说明**：原计划周五 C++ 内容（「编译器默认生成的移动构造在什么条件下自动生成」+ 陷阱题）
> **已于 09-15 周二提前完成**（`day2_gen_rules.cpp`，10 用例实验矩阵）。空出的时段改作收束。
>
> 改动理由（W1 复盘结论）：用户反馈「知识在增加但不成体系、说不流畅」。诊断为
> **一周只有输入、没有一次收束**——W1 周复盘因周末断档从未做过。把收束从周末（依赖办公机、
> 已证实会整周归零）搬到周五，是本周最重要的结构性调整。

**C++ 40 分钟 · 🔴 补 C：重建「特殊成员函数」那张表（索引缺失）**

W1 复盘暴露：Rule of 3 / Rule of 5 分别是哪几个函数，**答不上来**。
但同期 MyString、MyUniquePtr、10 用例矩阵都做过了——不是没学，是散点没挂到一张表上。

闭卷 15 分钟，不看任何资料、不看自己的代码，在纸上默写：

1. 6 个特殊成员函数，全名写出来（含函数签名）
2. Rule of 0 / 3 / 5 各是什么，三个数字之间什么关系
3. 一张抑制关系表：写了 A 会影响 B 吗？（6×6，只填「影响/不影响」）
4. 哪几种情况 `std::move` 会静默退化成拷贝？各举一个最小例子

写完再对 `day2_gen_rules.cpp` 的实跑输出核对，标出错了几处。

**这是 09-22 七天复测的预演。** 现在错没关系，下周还错就说明学法有问题。

**收束 50 分钟**（替代原 Electron 档）：

1. **画一张图**：把 W1+W2 学过的 C++ 概念串成一张关系图
   - 起点建议：RAII → 资源所有权 → 为什么需要拷贝/移动 → Rule of 5 → 抑制规则 → 退化陷阱
   - 手绘拍照或用任意工具，存 `docs/cpp-concept-map-w2.jpg`
   - **要求**：图上每个节点必须能追溯到自己写过的一个文件/一次实验，不能有"只是听说过"的节点

2. **核对 `daily/progress.jsonl`**：本周五天数据是否齐、时长是否真实

3. **本周门禁自测**（见文末），逐条判定，不许模糊

**记录 15 分钟**

---

### 周六（按 ToDesk 实测时长排，**不预设 4 小时**）

> **改动说明**：09-12 已证实「周末 6h」这个前提在公司代理更新后不成立。
> 本周改用 ToDesk 远程办公机，**09-19（周五）前必须确认可用性**。
> 时长先按 **90 分钟保守排**，拿到真实数据后再定。连不上就整日跳过，不欠账、不追赶。

**最低必做（90 分钟以内，按此顺序，做到哪算哪）**：

1. 🔴 **补 B2：Chat UI v0**（W1 周五计划项，欠了 4 天）
   - `F:\code\ai-desktop-assistant` 的默认 index.html 改成 Chat UI 静态骨架
   - 纯 HTML/CSS，不要 React：消息列表区 + 输入框 + 发送按钮
   - commit

2. 🔴 **补 B3：进程模型手绘图**（W1 周六计划项）
   - 建 `docs/` 目录（当前不存在）
   - 画 Main Process ↔ Renderer Process 关系，存 `docs/electron-process-model.jpg`
   - **加一条 09-15 新学的**：把 `RenderProcessHost` / `RenderProcess` 标在对应侧

3. 🔴 **补 B4：博客大纲**（W1 周日计划项）
   - 建 `blog-drafts/` 目录（当前不存在）
   - 第 1 篇标题 + 大纲：「我为什么写一个 Electron AI 助手 - 序章」
   - 只写大纲不写正文，正文留到第 6 周
   - 30 分钟封顶，不要陷进去

**有余力再做（时长充裕时按序追加）**：

4. 原计划 `Vector<T>` 简版（模板 + Rule of 5 + 单元测试）
   - 卡壳降级：改成 `IntVector` 非模板版
5. 周三顺延的 BrowserWindow 多窗口改代码
6. GPU Process / Utility Process 补课（09-15 发现多进程架构那篇对这两者只有一句话带过）
   - 资料：https://chromium.googlesource.com/chromium/src/+/main/docs/process_model_and_site_isolation.md

---

### 周日（2 小时复盘）

> **改动说明**：核心收束已移到周五。周日若 ToDesk 可用则做，不可用则整体跳过，
> 只需在 `daily/history/` 补一份「未学习」记录。**不再把周复盘押在周日**。

**1 小时：W2 周复盘** `daily/history/2026-09-20-weekly.md`

按 W1 复盘（`2026-09-13-weekly.md`）的结构写，**并新增一个固定动作**：

- 🔴 **对照 `plan/weekly/week-02.md` 逐条核查本周实际产出**
  （09-15 用户自查出 9 条 W1 欠账，比教练初查多 3 条。这个动作从本周起固定化）

**1 小时：Side project 整理**

- 清理本周 commit、更新 README
- 补 `docs/` 里的架构图

---

## 本周门禁（周五收束日自测，周日确认）

**原门禁**（保留）：

- [ ] `Vector<T>` 或 `IntVector` 简版可运行，Rule of 5 完整实现 ← 降级为周六「有余力」，未完成不算门禁失败
- [ ] Chromium 架构图 + 5 分钟口述说明
- [ ] Electron side project 有：多窗口 + 菜单 + 托盘 ← 多窗口顺延周六，托盘视时长可延后
- [ ] 5 天日记 + 1 份周复盘

**新增门禁（W1 欠账，本周必须清）**：

- [ ] A1 异常路径下 RAII 能讲清（栈展开）+ assert 单元测试跑通 ← 周四
- [ ] A3 move-from 对象状态，有实跑输出 ← 周三
- [ ] A4 「Chromium 沙箱 → contextIsolation → preload」一条链讲通 ← 周三
- [ ] B2 Chat UI v0 ← 周六
- [ ] B3 `docs/electron-process-model.jpg` ← 周六
- [ ] B4 `blog-drafts/` + 第 1 篇大纲 ← 周六
- [ ] C 闭卷默写 6 个特殊成员函数 + 抑制关系表 ← 周五

**A2「裸指针何时只是观察」**：本周不排，并入 W3 智能指针周（所有权语义的正餐）。

---

## 本周新增固定动作

1. **每日记录加「今日一句话复述」栏**（09-15 起）——不看代码、不看笔记，用嘴说出来的话写一句
2. **周五收束日**（本周起）——闭卷默写 + 概念图 + 门禁自测
3. **周复盘必须对照当周 plan 文件逐条核查产出**（09-20 起）

## 卡壳降级

- 模板不熟：`Vector<T>` 改成 `IntVector`（非模板版）
- Chromium 文档太长：只精读 Multi-Process Architecture 一篇 ← 09-15 已完成
- Electron API 太多：只做 BrowserWindow 一个，Menu/Tray 延后
- **ToDesk 连不上**：周六周日整日跳过，补「未学习」记录，B2/B3/B4 顺延 W3，不追赶

## 参考资料

- 《Effective Modern C++》Item 17（特殊成员函数生成规则）
- Chromium Design Docs 官网
- Electron 官方 API 文档
- Chromium Sandbox：https://chromium.googlesource.com/chromium/src/+/HEAD/docs/design/sandbox.md
- Chromium Sandbox FAQ：https://chromium.googlesource.com/chromium/src/+/HEAD/docs/design/sandbox_faq.md
