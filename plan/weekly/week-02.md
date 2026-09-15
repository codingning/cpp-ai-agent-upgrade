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

### 周五（1.5 小时）

**C++ 30 分钟**：
- 学习"编译器默认生成的移动构造在什么条件下会自动生成"
- 陷阱题：如果我写了拷贝构造，编译器还会给我生成移动构造吗？
- 写代码验证

**Electron 45 分钟**：
- 学习 Electron [Tray API](https://www.electronjs.org/docs/latest/api/tray)
- 在 side project 里加入系统托盘图标
- 点击托盘图标：显示/隐藏主窗口

**记录 15 分钟**

### 周六（4 小时深度）

**上午 2 小时：C++ Rule of 5 综合项目**
- 场景：写一个简版 `Vector<T>` 类（模板），实现 Rule of 5
- 支持：push_back、operator[]、size、capacity、拷贝、移动
- 单元测试：
  - 构造/析构无泄漏（用 valgrind 或简单计数器）
  - 拷贝后修改不影响原对象
  - 移动后原对象为空状态

**下午 2 小时：Chromium 架构深入**
- 阅读 [Chromium Design Docs](https://www.chromium.org/developers/design-documents/) 索引
- 挑一个感兴趣的文档细读：推荐 [Startup](https://www.chromium.org/developers/design-documents/startup/) 或 [Threading and Tasks](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/threading_and_tasks.md)
- 手绘一张图：Chromium 启动流程（从进程创建到第一个页面显示）
- 存到 `docs/chromium-startup.jpg`

### 周日（2 小时复盘）

**1 小时：周日复盘**
- 本周投入 vs 计划
- Rule of 5 是否掌握（测试：闭卷 15 分钟内说清楚 5 个特殊成员函数）
- Chromium 架构图能否口述

**1 小时：Side project 整理**
- 清理本周所有 commit
- 更新 README：说明当前进度（虽然还不成熟，但要有）
- 补充架构图（当前项目结构 + 未来 6 个月规划）

## 本周门禁

- [ ] `Vector<T>` 简版可运行，Rule of 5 完整实现
- [ ] Chromium 架构图 + 5 分钟口述说明
- [ ] Electron side project 有：多窗口 + 菜单 + 托盘
- [ ] 5 天日记 + 1 份周日复盘

## 卡壳降级

- 模板不熟：`Vector<T>` 改成 `IntVector`（非模板版）
- Chromium 文档太长：只精读 Multi-Process Architecture 一篇
- Electron API 太多：只做 BrowserWindow 一个，Menu/Tray 延后

## 参考资料

- 《Effective Modern C++》Item 17（特殊成员函数生成规则）
- Chromium Design Docs 官网
- Electron 官方 API 文档
