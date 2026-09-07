# 当日任务 · 2026-09-07（W1D1，周日）

方案 X 生效：**Week 01 = 09-07 周日 ~ 09-13 周六**，今天算 W1D1。

## 已完成（准备阶段）

- ✅ Task 1 环境准备：Node v22.20 / MSVC 14.44 / VSCode 扩展齐 / `F:\code\ai-desktop-assistant` + `F:\code\cpp-practice` 双仓库 init
- ✅ Task 2 周计划预读：无卡点
- ✅ VSCode tasks.json 配置并自测通过（`Ctrl+Shift+B` 编译当前 .cpp）
- ✅ 学习时段落定：10:30-11:10 + 17:00-17:50（工作日 1.5h）

## 今日学习任务（W1D1，1.5h）

### ① C++ 30min · RAII 概念

- 阅读 https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-resource （R.1-R.5）
- 英语差用 Chrome 右键翻译
- 闭卷回答三问：
  1. 什么是 RAII？
  2. 为什么析构在错误路径也执行？
  3. 裸指针何时只是观察用途？

### ② Electron 45min · Quick Start

- 工作目录：`F:\code\ai-desktop-assistant`
- 步骤：
  1. `npm init -y`
  2. `npm install --save-dev electron`（如卡：`npm config set registry https://registry.npmmirror.com`）
  3. 照官方 https://www.electronjs.org/docs/latest/tutorial/quick-start 建 `main.js` / `index.html` / `preload.js`
  4. `package.json` 里加 `"start": "electron ."`
  5. `npm start` 能弹出窗口即成功
- commit：`feat: Electron quick-start 骨架（W1D1）`

### ③ 记录 15min

- 新建 `daily/history/2026-09-07.md`，模板见下

## 记录模板

```markdown
# 2026-09-07（W1D1，周日）

## 完成
- C++：...
- Electron：...

## 掌握（能口述）
- RAII 三问答案：
  1. ...
  2. ...
  3. ...

## 未掌握/卡壳
- ...

## 证据
- git commit：<hash> feat: Electron quick-start 骨架（W1D1）
- 弹窗截图（可选）：docs/w1d1-electron-window.png

## 明日计划
- W1D2：FileHandle 类 + main.js 逐行读懂
```

## 门禁提醒

W1D1 不需要写 C++ 代码，Day 2 起才写。今天核心产出：
- 一份 `daily/history/2026-09-07.md`
- 一个能弹窗的 Electron 骨架 commit
- 三个 RAII 问题的口述答案（写在记录里）
