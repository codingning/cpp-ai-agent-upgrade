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

**🟣 追加档 · MyVector 三刀合一（75 分钟，不替代上面任何一条）**：
> **09-21 变更**：原排「周一/二/四各 25min 三刀」，本人当日提出合并，教练核对 `debt-map.md` 后采纳。
> 撤销理由见 `daily/current.md` 顶部（教练两处判断错误：noexcept 实验已于 09-20 完成、
> Rule of 5 的间隔检索价值已在 09-20 day7 用掉）。**周二、周四追加档相应撤销。**

- `F:\code\cpp-practice\week-03\my_vector.h`
- 第 1 段：`template<class T> class MyVector`，成员 `T* data_ / size_t size_ / size_t cap_`，
  构造 + 析构 + `push_back`（cap_ 固定 4，满了 assert）
- 第 2 段：改真扩容（2 倍、搬数据、释放旧的），push 10 个打印 cap_ 序列
- 第 3 段：补 Rule of 5，加测试把五条路径全走一遍
- 每段写完先编译再往下走，不要三段一起编译

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

**🟣 追加档 · Vector<T> 第 2 刀** —— ~~原排 25 分钟~~ **09-21 撤销，已并入周一 75min 合并档**

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

**🟣 追加档 · Vector<T> 第 3 刀** —— ~~原排 25 分钟~~ **09-21 撤销，已并入周一 75min 合并档**

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
      （拖了两周，本周升为门禁项，不再放「有余力」。
      **09-21 变更：三刀合并为周一一次 75min 追加档做完，周二/周四追加档撤销。**
      仍然不占用当天原有 C++ 30min 与 Electron 45min 的任何时间）

## W2 遗留欠账（W3 内必须清，不占门禁但要销账）

> **09-21 核对 `docs/debt-map.md` 后重写本节**：原 6 条里 4 条在 09-20 已清，
> 此处一直没同步，导致教练 09-21 照着过期条目排计划出错。以 debt-map.md 为准。

- [x] ~~进程模型图 cell 48/49 重填~~ ✅ 09-20 已重填（debt-map 已清区）
- [x] ~~博客大纲四处修改~~ ✅ 09-20 已改
- [x] ~~`= default` vs 什么都不写~~ ✅ 09-20 day7 实验1（D1 走拷贝 / D2 走移动）
- [x] ~~析构函数 `protected` 的「为什么」~~ ✅ **教练误标**：09-17 history 第 55-57 行本人已答对
- [x] ~~Q11/Q12 沙箱矛盾~~ ✅ 09-20 本人自核 Electron 官方三篇文档后重答通过（A4 整链结账）
- [x] ~~noexcept → vector 扩容退化，本人写一次实验~~ ✅ 09-20 day7 实验4：
      D7 走拷贝 / D8 走移动，本人自有实验证据

**实际仍欠的（debt-map.md 现存未清项）**：

- [ ] **Utility vs Renderer 的区别** —— 连续两次落地。出处待教练实读
      `process_model_and_site_isolation.md` / `sandbox.md` 确认后再布置（09-19 教练在此翻过车）
- [ ] **W1 周复盘三处空白** —— `2026-09-13-weekly.md` 第 13-14 行、第 191 行，跨周未补
- [ ] **博客第 1 篇正文** —— 大纲已及格，正文未开始（计划第 6 周发布）

## 卡壳降级

- React 不熟：用最简 HTML/CSS/JS 也行，React 延后
- LRU 卡住：先只写 vector + map 版本（不最优但能过测试）

## 参考

- 《STL 源码剖析》相关章节（可选）
- LeetCode 146 LRU Cache
- 尚硅谷 05_Numpy&Pandas 里的 Python 版对照理解
