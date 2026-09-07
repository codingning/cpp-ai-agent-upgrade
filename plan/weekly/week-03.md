# Week 03（第 3 周，2026-09-21 ~ 2026-09-27）

## 本周主题

**C++ STL 常用容器** + **Electron 主进程 API 深化** + **Chat UI 骨架搭建**

## 本周目标

- 掌握 vector/map/unordered_map/list 的常用操作和复杂度
- 理解迭代器失效规则（这个面试高频）
- Side project：用 Electron 搭建一个能收发消息的记事本原型（当作 chat UI 基础）

## 每日任务

### 周一（1.5 小时）

**C++ 30 分钟**：
- `std::vector`：动态数组，push_back 的均摊 O(1) 是怎么回事
- 迭代器失效场景：push_back 后原迭代器可能失效，为什么

**Electron 45 分钟**：
- side project 引入 React（如果还没有）
- 用 create-electron-app 或手动集成 React + TypeScript
- Chat UI 用 React 重写

**记录 15 分钟**

### 周二（1.5 小时）

**C++ 30 分钟**：
- `std::map`（红黑树）vs `std::unordered_map`（哈希表）
- 查询复杂度：O(log n) vs O(1) 平均
- 什么场景用 map，什么场景用 unordered_map

**Electron 45 分钟**：
- Chat UI 组件拆分：ChatWindow / MessageList / MessageItem / InputBox
- 用 React 函数组件 + hooks

**记录 15 分钟**

### 周三（1.5 小时）

**C++ 30 分钟**：
- 迭代器失效详细规则：
  - vector 的 push_back：可能失效
  - vector 的 insert：失效之后的
  - map/set 的 insert/erase：只失效被删的
  - unordered_map rehash 时：全失效

**Electron 45 分钟**：
- 消息状态管理：先用 useState，暂不用 Redux
- 发送消息按钮：点击后消息添加到列表（本地状态，无后端）

**记录 15 分钟**

### 周四（1.5 小时）

**C++ 30 分钟**：
- `std::list` 什么时候用（很少用，但要知道特性）
- `std::deque` 与 vector 的区别
- 一道题：反转链表（用 STL list 或手写单链表）

**Electron 45 分钟**：
- 消息 UI 优化：区分用户消息和 AI 消息（左右对齐、颜色）
- 加入时间戳显示

**记录 15 分钟**

### 周五（1.5 小时）

**C++ 30 分钟**：
- STL 算法：`std::sort`、`std::find`、`std::for_each`
- Lambda 表达式做谓词
- 一道题：统计文本单词频率（vector + unordered_map + sort）

**Electron 45 分钟**：
- 添加"清空对话"按钮
- 添加消息复制功能（点击消息复制到剪贴板）

**记录 15 分钟**

### 周六（4 小时深度）

**上午 2 小时：C++ STL 综合练习**
- 场景 1：读取一个文本文件，统计每个单词出现次数，输出 Top 10
- 场景 2：LRU 缓存实现（list + unordered_map，经典面试题）
- 每题必须编译通过，写单元测试

**下午 2 小时：Chat UI 打磨**
- 用心打磨 UI，让它看起来像"能演示的产品"
- 参考 Chatbox / Claude 的界面
- 让朋友看一眼，问"这看起来是不是像正经产品"
- 修 5-10 个小 bug（滚动、宽度、字体）

### 周日（2 小时复盘）

**1 小时：周日复盘 + 迭代器失效小测**
- 闭卷回答 5 个迭代器失效场景
- 记录本周实际投入

**1 小时：博客草稿开始**
- 开始写第 1 篇博客的正文（第 6 周发布）
- 主题："从 Chromium 部门工程师到 Electron AI 助手 - 学习日志 Week 1-3"
- 只写 500 字草稿就好

## 本周门禁

- [ ] LRU 缓存能独立实现（20 分钟内）
- [ ] 迭代器失效 5 个场景闭卷讲清楚
- [ ] Chat UI 用 React 实现，能收发本地消息，UI 看起来像产品
- [ ] 5 天日记 + 1 份周日复盘 + 博客草稿 500 字

## 卡壳降级

- React 不熟：用最简 HTML/CSS/JS 也行，React 延后
- LRU 卡住：先只写 vector + map 版本（不最优但能过测试）

## 参考

- 《STL 源码剖析》相关章节（可选）
- LeetCode 146 LRU Cache
- 尚硅谷 05_Numpy&Pandas 里的 Python 版对照理解
