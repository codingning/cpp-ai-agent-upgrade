# 当日任务 · 2026-09-09（W1D3，周三）

## 本周节奏（真实日历）

| 日期 | 星期 | 编号 | 状态 |
|---|---|---|---|
| 09-07 | 周一 | W1D1 | ✅ 完成 |
| 09-08 | 周二 | W1D2 | ✅ 完成 |
| 09-09 | 周三 | **W1D3 ← 今天** | |
| 09-10 | 周四 | W1D4 | |
| 09-11 | 周五 | W1D5 | |
| 09-12 | 周六 | W1D6（深度日 4h） | |
| 09-13 | 周日 | W1D7（复盘日 2h） | |

## C++（30–50min）

- 手写 `MyUniquePtr<T>`，支持 `->`、`*`、移动构造/移动赋值和 `reset`。
- 闭卷先写核心实现，再补空指针、移动后源对象、重复 reset、异常路径测试。
- 用编译实验确认显式析构对隐式移动操作的影响。

## Electron（45min）

建立 side project TypeScript 骨架，保留最小可运行窗口。

### ① TypeScript 骨架（30min）

在 `F:\code\ai-desktop-assistant` 增加最小 TypeScript 配置和入口，记录编译/启动命令。

1. `app.whenReady()` 是什么？为什么不能直接调 `createWindow()`？
2. `BrowserWindow` 的 `webPreferences.preload` 指向什么？
3. `app.on('window-all-closed')` 里为什么判断 `process.platform !== 'darwin'`？
4. `app.on('activate')` 什么时候触发？

不懂的行先查 https://www.electronjs.org/zh/docs/latest/api/browser-window ，还不懂再问。

### ② 记录（15min）

改 `BrowserWindow` 构造参数，一次改一个观察效果：

- 记录类型或打包问题，以及一个尚未理解的 Electron 边界。

图标（`icon`）今天跳过，W2 再处理。

### ③ 记录追加（10min）

在 `daily/history/2026-09-08.md` 追加 Electron 部分：
- 完成清单
- 4 个问题的自答
- 未掌握/卡壳

## 收工

- 提交：`cd C:\Users\...\cpp-ai-agent-upgrade && git add -A && git commit -m "docs(w1d2): 完成 W1D2 学习记录"`
- side project 若有 commit：`cd F:\code\ai-desktop-assistant && git add -A && git commit -m "feat(w1d2): main.js 逐行注释 + 窗口参数调整"`

## 明日预告（W1D3，周三 09-09）

- C++：手写 MyUniquePtr（30-50 行，支持 `->` `*` move reset）
- Electron：建立 side project TypeScript 骨架
