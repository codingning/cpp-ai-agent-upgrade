# 今日任务 · 2026-09-19（周六）· W2 周六 · ToDesk 远程日

> ToDesk 已于 09-18 确认可用。按 **90min 保守排**，不按原计划 4h。
> 拿到真实数据后，下周六再定时长。

---

## 开场 5 分钟 · 清尾

- [ ] `F:\code\ai-desktop-assistant` push 失败排查：终端手动跑 `git push origin master`，
      看它到底要什么（疑似 remote 内嵌凭据失效）。两个 commit 还在本地没丢。
- [ ] 概念图三处收尾：
  - `= delete` 只写了「禁止重载被选中」（你自己挖的那半），漏了主用途「禁用拷贝构造做 NonCopyable」
  - `= default` 的说明仍是 09-17 答错的那句，改标 ❓
  - （icon 残留已清 ✅）

---

## 主任务（60min）· 🔴 Chromium 进程模型手绘图

**这是 W1 周六欠到现在的项，也是阶段一门禁项**（W6 验收：能画 Browser/Renderer/GPU/Utility
进程模型图并口述通信路径）。欠了一周，今天补。

要求：
1. 画出四类进程：Browser / Renderer / GPU / Utility，标明各自职责
2. 画出通信路径：谁跟谁通信、走什么机制
3. **把 Electron 对应上去**：main process 对应哪个？renderer process 对应哪个？
   `ipcMain`/`ipcRenderer` 对应 Chromium 的什么？
   （你 09-15 已经答过 RenderProcessHost/RenderProcess 的对应关系，那次答反了，这次画对）
4. 存 `docs/chromium-process-model.drawio` 或手绘拍照存 `docs/`

**工具**：这张图有跨进程箭头，不是树形，markmap 画不了。用 draw.io（VSCode 装插件，
存 `.drawio` 是 XML，能进 git，教练能读）。

---

## 补课（30min）· 二选一，自己挑

### A. `= default` vs 什么都不写（欠了两天）

去查：`= default` 算不算「用户声明」？算了以后连带影响什么？
查完写一句话，不要抄，用自己的话。

### B. noexcept → vector 扩容退化，自己写一个对照实验

教练 09-18 写过一个（`%LOCALAPPDATA%\Temp\w2chk\noexcept_test.cpp`），**不许照抄**。
自己设计：两个类，唯一差异是移动构造有没有 `noexcept`，用 vector 触发扩容看走哪条路。
**写之前先在注释里写「我预测输出是 ___」**——这是元规则第六次了。

---

## 元规则（第六次）

前五次都没做。今天如果选了 B，预测那行是硬性要求，不写不算完成。

判据升级：不只写「预测输出是什么」，还要写「**如果不是，说明我哪里想错了**」。

---

## 明天（09-20 周日）· W2 周复盘

连续第二周欠着的项。周日 2h：
- 1h 本周复盘写 `daily/history/2026-09-20-weekly.md`
- 1h 下周计划微调

**你 09-17 说过「感觉不成体系」——周复盘就是治这个的，一次没做过。**
