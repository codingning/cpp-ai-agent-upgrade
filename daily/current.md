# 当日任务 · 2026-09-11（W1D5，周五）

## 本周节奏（真实日历）

| 日期 | 星期 | 编号 | 状态 |
|---|---|---|---|
| 09-07 | 周一 | W1D1 | ✅ 完成 |
| 09-08 | 周二 | W1D2 | ✅ 完成 |
| 09-09 | 周三 | W1D3 | ✅ 完成 |
| 09-10 | 周四 | W1D4 | ⚠️ C++ 完成，Electron 顺延到今天 |
| 09-11 | 周五 | **W1D5 ← 今天** | |
| 09-12 | 周六 | W1D6（深度日 4h） | |
| 09-13 | 周日 | W1D7（复盘日 2h） | |

> **今天是补课日**：下午要做两份 Electron（W1D4 欠的 + 今天的）。
> 如果时间不够，优先做 W1D4 欠的那份（读源码画流程），Chat UI 可以挪到周六深度日。

---

## 上午 10:30-11:10 · C++（40min）

**主题：为什么 unique_ptr 不能拷贝，只能移动**

前四天你已经把 `MyUniquePtr` 从零写到支持自定义 deleter 了。
今天不写新功能，改成**回答问题 + 做实验**，把原理钉死。

### 任务 1：闭卷回答（15min）

在今天的记录文件里写答案，不许翻代码：

1. 如果允许 `MyUniquePtr` 拷贝，会发生什么灾难？用 day2 那个 FileHandle 的例子说明。
2. `= delete` 和「不写拷贝构造」有什么区别？编译器分别会做什么？
3. 移动构造的形参为什么是 `MyUniquePtr&&` 而不是 `const MyUniquePtr&`？
   （提示：想想移动要干什么，const 会挡住哪一步）
4. `std::move(a)` 这个函数本身做了什么？它真的"移动"了什么吗？

### 任务 2：做实验验证（25min）

在 `F:\code\cpp-practice\week-01\day5_move_semantics.cpp` 里：

```cpp
// 实验 1：把拷贝构造从 = delete 改成正常实现，看 double-free
// 实验 2：观察 move-from 之后源对象的状态
void test_moved_from_state() {
    MyUniquePtr<Widget> a(new Widget(1));
    MyUniquePtr<Widget> b = std::move(a);
    // a 现在是什么状态？能调 a->hello() 吗？能再 reset 吗？析构会崩吗？
    // 把你的猜测先写进注释，再运行验证
}

// 实验 3：函数返回值
MyUniquePtr<Widget> make_widget() {
    MyUniquePtr<Widget> up(new Widget(2));
    return up;          // 这里没写 std::move，能编译过吗？为什么？
}
```

**验收**：三个实验都跑出结果，且每个结果你能解释为什么。

---

## 下午 17:00-17:50 · Electron（50min）

### 补 W1D4 欠的：读 Chatbox 主进程源码（30min）

源码地址：https://github.com/Bin-Huang/chatbox/tree/main/src/main

**只看 `index.ts` 或 `main.ts` 一个文件**，不要点开别的。

要产出一张**启动流程图**（画在记录文件里，文字版即可）：

```
app 启动
  ↓
（按顺序列出它监听了哪些 app 事件，每个事件里干了什么）
  ↓
窗口创建
  ↓
...
```

对照你自己的 `ai-desktop-assistant/main.js`，回答：
- 它比你多做了哪些事？（至少找出 3 处）
- 哪一处是你现在就能抄过来用的？

### 今天的：Chat UI v0 骨架（20min）

在 `F:\code\ai-desktop-assistant` 里把默认页面改成聊天界面骨架。

纯 HTML + CSS，**不要引入 React**。需要三块：
- 消息列表区域（上方，可滚动）
- 输入框（下方）
- 发送按钮

点发送后把输入框内容追加到消息列表即可，不需要真的调 AI。

**验收**：`npm start` 能看到聊天界面，输入文字点发送能显示在列表里。
commit message: `feat: Chat UI v0 骨架`

> 时间不够就只做源码阅读，Chat UI 挪到周六。**不要两个都做半截。**

---

## 记录（15min）

写 `daily/history/2026-09-11.md`，重点记：
- C++ 四个问题的答案（自己的话）
- 三个实验的预测 vs 实际结果，不一致的地方重点写
- Chatbox 启动流程图 + 三处差异

---

## 今日验收清单

- [ ] `day5_move_semantics.cpp` 提交，三个实验有输出
- [ ] C++ 四问答案写进记录
- [ ] Chatbox 启动流程图画出来
- [ ] （可选）Chat UI v0 提交
- [ ] `daily/history/2026-09-11.md` 写完
