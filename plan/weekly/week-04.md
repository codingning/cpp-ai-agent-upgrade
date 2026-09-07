# Week 04（第 4 周，2026-09-28 ~ 2026-10-04）

## 本周主题

**C++17 现代特性** + **Electron 渲染进程与 Preload** + **简历"保底版"完成**

## 本周目标

- 掌握 C++17 关键特性：结构化绑定、optional、variant、string_view
- 理解 Electron Context Isolation 和 preload 机制
- 完成简历 v0（应急保底版）
- 记事本加持久化（本地存储对话记录）

## 每日任务

### 周一（1.5 小时）

**C++ 30 分钟**：
- `std::string_view`：为什么需要它，与 const string& 区别
- 陷阱：string_view 悬垂引用
- 写代码：一个函数接受 string_view 参数，测试传入字面量、std::string、char*

**Electron 45 分钟**：
- 阅读 [Context Isolation](https://www.electronjs.org/docs/latest/tutorial/context-isolation)
- 理解：为什么默认打开 contextIsolation？关闭有什么安全风险？

**记录 15 分钟**

### 周二（1.5 小时）

**C++ 30 分钟**：
- `std::optional`：表达"可能没有"的语义
- 写一个函数：查找 vector 中第一个大于 N 的数，返回 optional
- 对比：以前用什么方式表达"没找到"（-1、nullptr、bool 返回值+out 参数）

**Electron 45 分钟**：
- 阅读 [preload script](https://www.electronjs.org/docs/latest/tutorial/tutorial-preload)
- 在 side project 中添加 preload.ts
- 用 contextBridge.exposeInMainWorld 暴露一个测试 API

**记录 15 分钟**

### 周三（1.5 小时）

**C++ 30 分钟**：
- `std::variant`：类型安全的联合体
- `std::visit`：访问 variant 的当前值
- 写代码：一个 `Result<T>` 类型，用 variant<T, Error> 实现

**Electron 45 分钟**：
- 侧读 Chatbox 或类似项目的 preload.ts
- 理解：主进程 API 如何安全暴露给渲染进程
- 记录 3 个你觉得设计好的地方

**记录 15 分钟**

### 周四（1.5 小时）

**C++ 30 分钟**：
- 结构化绑定：`auto [key, value] = ...`
- 场景：遍历 map、返回多值
- 写代码：一个函数返回多个值（用 tuple + 结构化绑定接收）

**Electron 45 分钟**：
- side project：实现"新建对话"和"切换对话"的 UI
- 状态管理：暂时用 useReducer，不引入 Redux

**记录 15 分钟**

### 周五（1.5 小时）

**C++ 30 分钟**：
- `if constexpr`：编译期条件分支
- 写代码：模板函数根据 T 是不是 pointer 走不同分支

**Electron 45 分钟**：
- Electron 持久化方案调研：electron-store vs SQLite vs 文件
- 选定用哪个（推荐 electron-store 简单快速）
- 实现对话记录持久化（存到本地磁盘）

**记录 15 分钟**

### 周六（4 小时深度）

**上午 2 小时：C++17 综合练习**
- 场景：写一个简易 JSON parser（只支持字符串、数字、bool、null、对象、数组）
- 用 variant 表达 JSON value
- 用 optional 表达 parse 结果
- 只需 200 行左右，能 parse `{"name": "test", "age": 20, "active": true}` 就行

**下午 2 小时：简历"保底版"起草**
- 打开一个新文档 `plan/resume/v0-emergency.md`
- 用 STAR 法则整理过去 2 年 Chromium 部门工作：
  - 3-5 条工作项，每条包含：背景、任务、行动、结果
  - 突出：涉及的技术模块、bug 修复案例、性能改进（如有）、协作规模
- 关键：**不吹嘘，但要把已做的价值讲够**
- 目标：如果第 5 周被裁，这份简历能立刻投

### 周日（2 小时复盘）

**1 小时：周日复盘 + C++17 小测**
- 闭卷 20 分钟：写一段代码用到 optional、variant、结构化绑定
- 记录本周投入

**1 小时：简历 v0 review**
- 自己重读简历，删掉所有含糊表述
- 找 1 位朋友/前同事帮 review（可以匿名请人看）

## 本周门禁

- [ ] 简易 JSON parser 能跑通 3 个测试样例
- [ ] `Result<T>` 类型能用（用 variant 实现的）
- [ ] Electron side project：Context Isolation 打开 + preload 暴露 API + 对话持久化
- [ ] 简历 v0 完成初稿（1500 字左右）
- [ ] 5 天日记 + 1 份周日复盘

## 卡壳降级

- JSON parser 卡住：只做数字 + 字符串两种类型的 parse
- 简历不知怎么写：先列 20 条"做过的事"，第 5 周再整理
- optional/variant 混乱：只精掌握 optional，variant 延后

## 参考

- 《C++17 The Complete Guide》相关章节
- Electron Security 官方文档
- 简历模板：https://cv.smart-ai.club/ 或 latexresu.me

## 里程碑

**第 4 周结束时你应该有**：
- 3 篇 C++17 小实验代码（optional、variant、结构化绑定）
- 1 个可编译运行的简易 JSON parser
- 1 个能对话（假）+ 持久化的 Electron 记事本
- 1 份可以立刻应急投递的简历（v0）
