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

**🟣 追加档 · Vector<T> 第 1 刀（25 分钟，不替代上面任何一条）**：
- `F:\code\cpp-practice\week-03\my_vector.h`
- 只写：`template<class T> class MyVector`，成员 `T* data_ / size_t size_ / size_t cap_`，
  加一个构造 + 一个析构 + `push_back`（先不管扩容，cap_ 固定 4，满了直接 assert）
- 目标不是写完，是让这个文件今天存在并能编译

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

**🟣 追加档 · Vector<T> 第 2 刀（25 分钟）**：
- 把固定 cap_ 改成真扩容：满了申请 2 倍新空间、搬数据、释放旧的
- 自己跑一次：push_back 10 个元素，每次打印 cap_，看是不是 4→8→16
- **跑之前先在注释里写死你猜的序列**（元规则，这是第 7 次要求了）

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

**🟣 追加档 · Vector<T> 第 3 刀（25 分钟）**：
- 给 MyVector 补 Rule of 5：拷贝构造 / 拷贝赋值 / 移动构造 / 移动赋值 / 析构
- 这是 W2 学的整张表第一次落到自己的容器上，不是新知识，是索引挂钩

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
- [ ] 🟣 **`MyVector<T>` 可编译可运行，含 Rule of 5 + 扩容 + assert 测试**
      （拖了两周，本周升为门禁项，不再放「有余力」。周一/二/四各切 25 分钟追加档，
      三刀切完就是成品。**这三刀不占用当天原有 C++ 30min 与 Electron 45min 的任何时间**）

## W2 遗留欠账（W3 内必须清，不占门禁但要销账）

- [ ] 进程模型图 cell 48/49 重填（09-20 已重答，落图待办）
- [ ] 博客大纲四处修改 → 09-20 已改
- [ ] `= default` vs 什么都不写：区别点在「用户是否声明」，概念图上仍是错的
- [ ] 析构函数 `protected` 的「为什么」
- [ ] Q11/Q12 沙箱矛盾：自己读 Electron 官方 webPreferences 文档核实
- [ ] noexcept → vector 扩容退化，本人写一次实验（**并入本周 MyVector，天然合流**）

## 卡壳降级

- React 不熟：用最简 HTML/CSS/JS 也行，React 延后
- LRU 卡住：先只写 vector + map 版本（不最优但能过测试）

## 参考

- 《STL 源码剖析》相关章节（可选）
- LeetCode 146 LRU Cache
- 尚硅谷 05_Numpy&Pandas 里的 Python 版对照理解
