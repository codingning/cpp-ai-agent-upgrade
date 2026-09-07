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

**C++ 30 分钟**：
- 学习 Rule of Zero：什么时候不需要写任何特殊成员函数
- 举 3 个例子：只用 STL 容器就 OK 的类

**Electron 45 分钟**：
- 深入 [BrowserWindow API](https://www.electronjs.org/docs/latest/api/browser-window)
- 修改 side project：让主进程能同时打开多个窗口，窗口间通过菜单切换

**记录 15 分钟**

### 周四（1.5 小时）

**C++ 30 分钟**：
- 学习 `= default` 和 `= delete`
- 什么时候用 `= default`？什么时候用 `= delete`？
- 写一个 `NonCopyable` mixin 类

**Electron 45 分钟**：
- 学习 Electron [Menu API](https://www.electronjs.org/docs/latest/api/menu)
- 在 side project 里加入应用菜单：File / Edit / View / Help
- File 菜单加入"新建对话"、"退出"选项（先只有 UI，无功能）

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
