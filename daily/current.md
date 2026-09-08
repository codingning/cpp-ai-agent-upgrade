# 当日任务 · 2026-09-08（W1D2，周二）

## 本周节奏（真实日历）

| 日期 | 星期 | 编号 | 状态 |
|---|---|---|---|
| 09-07 | 周一 | W1D1 | ✅ 完成 |
| 09-08 | 周二 | **W1D2 ← 今天** | 上午 ✅ / 下午 ⏳ |
| 09-09 | 周三 | W1D3 | |
| 09-10 | 周四 | W1D4 | |
| 09-11 | 周五 | W1D5 | |
| 09-12 | 周六 | W1D6（深度日 4h） | |
| 09-13 | 周日 | W1D7（复盘日 2h） | |

## 上午 C++（已完成）

- ✅ 手写 FileHandle 类（RAII 实践）
- ✅ 边界测试三种路径都触发析构（正常/异常/提前 return）
- ✅ 亲眼验证栈展开机制（第 2 题眼见为实）
- ✅ 触发 double-free UB 并加 `= delete` 编译期堵漏
- ✅ 记录扫盲概念：UB / CRT / SIGSEGV / CVE / Sandbox Escape

## 下午 Electron（17:00-17:45，45min）

按 week-01.md 周二排期：**main.js 逐行读懂 + 改窗口**。

### ① main.js 逐行读懂（20min）

打开 `F:\code\ai-desktop-assistant\main.js`，每行加注释。目标能回答：

1. `app.whenReady()` 是什么？为什么不能直接调 `createWindow()`？
2. `BrowserWindow` 的 `webPreferences.preload` 指向什么？
3. `app.on('window-all-closed')` 里为什么判断 `process.platform !== 'darwin'`？
4. `app.on('activate')` 什么时候触发？

不懂的行先查 https://www.electronjs.org/zh/docs/latest/api/browser-window ，还不懂再问。

### ② 改窗口（15min）

改 `BrowserWindow` 构造参数，一次改一个观察效果：

- `width: 1200`
- `height: 800`
- `title: 'AI 桌面助手'`
- `autoHideMenuBar: true`

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
