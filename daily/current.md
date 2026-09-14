# 当日任务 · 2026-09-14（W2D1，周一）

> Week 02 = 2026-09-14（周一）~ 2026-09-20（周日）
> 本周主题：C++ Rule of 3/5（手写 String → 周六 Vector<T>）+ Chromium 多进程架构 + Electron 主进程 API

## 欠账台账（必须先认账）

| 欠的东西 | 原定日期 | 状态 |
|---|---|---|
| Electron：Chatbox 主进程源码阅读 + 启动流程图 | W1D4（09-10） | 顺延 2 次，仍未做 |
| Electron：Chat UI v0 骨架 | W1D5（09-11） | 未做 |
| W1D6 周六深度日 4h | 09-12 | 无记录 |
| W1D7 周日复盘 + W1 门禁验收 | 09-13 | 无记录 |

证据：`ai-desktop-assistant` 最后一次 commit 是 09-09（`c1aed94`）；
`daily/history/` 没有 09-12、09-13 两份文件；09-11 记录第七节 Electron 整段空白。

**重排决定（不补齐全部欠账，只保主线）**：
- Electron 源码阅读 → 今天下午做，不再顺延。这是本周所有 Electron 任务的地基。
- Chat UI v0 → 挪到周六深度日下午。
- W1 门禁验收 + 周复盘 → 并入本周日（09-20），一次写两周，不占工作日时段。
- C++ 主线不动。今天必须开 String，否则周六的 `Vector<T>` 直接做不了。

---

## 上午 10:30-11:10 · C++（40min）

**主题：Rule of Three —— 深拷贝 vs 浅拷贝到底差在哪一行**

前一周你写的 `MyUniquePtr` 是「独占，禁止拷贝」。这周反过来：
`String` 是**可以拷贝的**，所以必须自己写对拷贝。

### 任务：`F:\code\cpp-practice\week-02\day1_string.cpp`

自己写完整实现，下面只给声明骨架和签名：

```cpp
class String {
public:
    String();                              // 空串
    String(const char* s);                 // 从 C 字符串构造
    ~String();

    String(const String& other);           // 拷贝构造
    String& operator=(const String& other);// 拷贝赋值

    const char* c_str() const;             // const 成员函数：承诺不改对象状态
    size_t size() const;

private:
    char*  data_;
    size_t size_;
};
```

自己查的（不要问我，查完写进记录）：
- `strlen` / `strcpy` 在哪个头文件，各自算不算结尾的 `'\0'`
- `new char[n]` 对应的释放语法是什么，跟 `delete` 差一个什么符号

### 三个必过的验收点

1. `String a("hello"); String b = a;` 之后改 `b`，`a` 不能跟着变
2. `a = a;`（自赋值）不崩
3. `String c; c = a;`（先默认构造再赋值）不泄漏、不 double-free

### 闭卷先答，再写代码（写进记录）

1. 如果不写拷贝构造，编译器生成的那个会把 `data_` 怎么处理？析构时会发生什么？
2. 深拷贝和浅拷贝的差别，具体体现在拷贝构造函数的哪一行？
3. 拷贝赋值比拷贝构造多做了两件事，是哪两件？（提示：赋值前对象已经存在）
4. 为什么 `c_str()` 后面要加 `const`？不加会怎样？

---

## 下午 17:00-17:50 · Electron（50min）

### 只做一件事：读 Chatbox 主进程源码（欠两次了）

源码：https://github.com/Bin-Huang/chatbox/tree/main/src/main

**只看 `index.ts`（或 `main.ts`）一个文件**，不点开任何别的文件。

产出画在记录文件里，文字版就行：

```
app 启动
  ↓
（按代码顺序列它监听了哪些 app 事件，每个事件里干了什么）
  ↓
窗口创建（传了哪些 webPreferences）
  ↓
...
```

然后对照你的 `ai-desktop-assistant/main.js` 回答：
- 它比你多做了哪 3 件事
- 哪一件是今天就能抄过来的

**今天不写 Electron 代码。** 50 分钟只够读懂一个文件 + 画图，
再塞 Chat UI 就是两个都做半截。

---

## 记录（15min）

写 `daily/history/2026-09-14.md`，必须包含：
- C++ 四问的闭卷答案（自己的话，不许抄我的）
- 三个验收点的实测输出（贴编译器和运行输出，不是"跑通了"三个字）
- Chatbox 启动流程图 + 三处差异
- **周末为什么断**：09-12、09-13 两天发生了什么，三行写清。
  不是让你写检讨，是判断这是偶发还是时段假设已经失效。

---

## 今日验收清单

- [ ] `day1_string.cpp` 三个验收点全过，commit
- [ ] C++ 四问闭卷答案写进记录
- [ ] Chatbox 启动流程图 + 3 处差异
- [ ] 周末断档原因三行
- [ ] `daily/history/2026-09-14.md` 写完并 commit
