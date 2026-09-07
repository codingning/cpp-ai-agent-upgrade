# Week 01（第 1 周，2026-09-07 ~ 2026-09-13）

## 本周主题

**C++ RAII 与生命周期** + **Electron 环境搭建与 hello-world**

## 本周目标

- 掌握 RAII 概念，能独立写一个资源包装类
- 完成 Electron 官方 quick-start，理解主进程/渲染进程基本概念
- 提交第 1 个 Electron 骨架 commit 到 GitHub（新建 side project 仓库）

## 每日任务

### 周一（1.5 小时）

**C++ 30 分钟**：
- 阅读 [C++ Core Guidelines R.1-R.5](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-resource)
- 闭卷回答：什么是 RAII？为什么析构在错误路径也执行？裸指针何时只是观察？

**Electron 45 分钟**：
- 阅读 [Electron 官方 Quick Start](https://www.electronjs.org/docs/latest/tutorial/quick-start)
- 环境准备：Node.js LTS + npm，装好 electron 包（`npm install --save-dev electron`）
- 用 npx 生成一个空项目骨架，能 `npm start` 弹出窗口就行

**记录 15 分钟**：
- 写今日 daily/history/2026-09-08.md：完成、卡壳、明日计划

### 周二（1.5 小时）

**C++ 30 分钟**：
- 手写一个 `FileHandle` 类：构造打开文件、析构关闭
- 边界测试：正常返回、抛异常、提前 return——都能正确关闭

**Electron 45 分钟**：
- 深入 quick-start：`main.js` 每一行都要读懂
- 修改窗口标题、大小、图标，观察 `BrowserWindow` 参数作用
- 尝试：为什么删除 `preload.js` 后网页里访问 `process` 会失败？

**记录 15 分钟**

### 周三（1.5 小时）

**C++ 30 分钟**：
- 学习 `std::unique_ptr` 的实现原理（不要用它，先自己写一个简版 `MyUniquePtr`）
- 只需 30-50 行，支持 `->`、`*`、move、reset

**Electron 45 分钟**：
- 建立 side project GitHub 仓库：`ai-desktop-assistant`（私有或公开都行）
- 初始化 Electron + TypeScript 项目结构
- 参考：[Electron + TypeScript 模板](https://github.com/electron/electron-quick-start-typescript)
- 第 1 个 commit：项目骨架

**记录 15 分钟**

### 周四（1.5 小时）

**C++ 30 分钟**：
- 继续完善 `MyUniquePtr`：加入 deleter、支持 array 版本（简版）
- 编译测试：`g++ -std=c++17 -Wall -Wextra` 无警告

**Electron 45 分钟**：
- 侧读一份优秀 Electron 项目源码：[Chatbox 主进程入口](https://github.com/Bin-Huang/chatbox/tree/main/src/main)
- 只看 `main.ts` 或 `index.ts` 一个文件
- 画出：应用启动流程（app 事件监听顺序）

**记录 15 分钟**

### 周五（1.5 小时）

**C++ 30 分钟**：
- 学习为什么 unique_ptr 不能拷贝，能移动
- 手动实现 `MyUniquePtr` 的移动构造和移动赋值
- 边界测试：move-from 对象的状态

**Electron 45 分钟**：
- 在你的 side project 里，把默认 HTML 改成一个简单 Chat UI 静态骨架
- 用最简单的 HTML/CSS 就行，不需要 React
- 页面上有：消息列表区域、输入框、发送按钮
- 第 2 个 commit：Chat UI v0

**记录 15 分钟**

### 周六（4 小时深度）

**上午 2 小时：C++ RAII 综合练习**
- 场景：写一个 `Timer` 类，构造记录起始时间，析构打印耗时
- 场景：写一个 `MutexLock` 类，构造 lock，析构 unlock
- 每个类都要有单元测试（用 assert 或简单 gtest）
- 编译并跑通

**下午 2 小时：Electron 深入**
- 阅读 Electron 官方 [Process Model](https://www.electronjs.org/docs/latest/tutorial/process-model)
- 画一张手绘图：Main Process ↔ Renderer Process 关系
- 拍照存 `docs/electron-process-model.jpg`
- 修改 side project：主进程添加日志输出，渲染进程打开 devtools 观察

### 周日（2 小时复盘）

**1 小时：写周日复盘**（`daily/history/2026-09-13-weekly.md`）
- 本周实际投入总小时数
- 完成 vs 计划的差异
- 卡壳点 + 解决方案
- 下周微调

**1 小时：技术博客准备**（这周不写，只准备）
- 建立一个博客草稿目录 `blog-drafts/`
- 起草第 1 篇博客的标题和大纲："我为什么写一个 Electron AI 助手 - 序章"
- 只写大纲，不写正文，正文留到第 6 周

## 本周门禁（周日晚验收）

- [ ] `MyUniquePtr` 代码可运行，包含 move 语义和单元测试
- [ ] side project GitHub 仓库存在，至少 2 个 commit
- [ ] Electron 主进程/渲染进程能口述区别
- [ ] 5 天工作日记录 + 1 份周日复盘

## 卡壳时的降级方案

- 如果 Electron 环境搭不起来：先只做 C++ 部分，第 2 周补
- 如果 C++ 移动语义卡住：先只完成基础 `MyUniquePtr`（不加 move），第 2 周深入
- 如果周中缺席 2 天：周六周日不追赶原计划，只做最低必需（`MyUniquePtr` + Electron 骨架）

## 参考资料

- C++：《Effective Modern C++》Item 17-22（如果有书）
- Electron：官方文档 Tutorial 章节前 5 节
- 优秀开源项目参考：Chatbox、Cherry Studio、LM Studio

## 下周预告

Week 02：C++ 拷贝/移动/Rule of 5 深入 + Chromium 架构总览 + Electron 主进程 API
