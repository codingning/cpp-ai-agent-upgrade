# Week 05（第 5 周，2026-10-05 ~ 2026-10-11）

## 🚫 本周重大调整：国庆停训 3 天 + 节后复训（09-23 定）

> **依据**：国办发明电〔2025〕7 号 —— 国庆 **10月1日（周四）~ 7日（周三）** 放假 7 天。
> **10-05（一）、10-06（二）、10-07（三）三天在假期内，停训。**
> 见 `docs/calendar-holidays.md`（教练 09-23 实查，多源一致）。

### 🔴 2026-10-09 23:00 追加重排：10-09 同样零产出，复习日整体落到 10-10

> **23:00 写记录 job 结账实查**：10-09 与 10-08 一样零产出，
> 四证据源互证 —— `cpp-practice` 最新 commit 仍 `8fc7041`(09-30)、`vite-project` 仍 `b82149c`(09-30)、
> `E:\code\q-framework` 10-07 后零改动、会话库 10-09 本人消息 **0 条**。
>
> **🔴 根因已挖到底（上方 09:3x 那版只查到「cron 没跑」，没查到为什么没跑）**：
> gateway 进程 `last_heartbeat_at = UTC 2026-09-30T17:52:43`（北京时间 **10-01 01:52**）后
> **`gateway.previous_unclean_exit`**（非正常退出），直到 **10-09 10:17** 才重启，
> **空窗 8 天 8 小时**；三条 cron 的 `last_run` 全停在 09-30；
> `cron/executions.db` 的 `executions` 表 **10-01 ~ 10-08 整段零条记录**；
> `cron/output/febcd5257994/` 最后一份产物是 `2026-09-30_09-31-38.md`，**10-08/10-09 无任何文件**。
>
> → **10-08、10-09 两天均为教练侧故障，不记本人欠账，不需要他解释。**
> ⚠️ 上方 09:3x 版写的「10-08 未训练**原因待本人说明**」**予此作废** ——
> 他根本没收到推送，不知道有课，把球踢给他问原因本身就是错的。
>
> **停训实际 12 天**（中秋 3 + 国庆 7 + 故障 2），`calendar-holidays.md` 4.2 照旧生效。

| 原定日 | 原定内容 | 最新去向 | 性质 |
|---|---|---|---|
| ~~10-08 四~~ → ~~10-09 五~~ | 间隔复习 + C++ 7 天复测 + Rule of 2 复测 + base 顶层扫描 + q-fw 第四格 | **→ 10-10（六，调休上班日，按 1.5h 不是 4h）** | 故障两天，**不记本人账** |
| 10-09 五 | `variant` / `std::visit` / `Result<T>`、结构化绑定、q-fw 第五格三方对照表 | **→ W6（10-12 起）** | 容量类，必顺延 |
| 10-10 六 | `if constexpr`、Electron `electron-store` 持久化 | **→ W6（10-12 起）** | 容量类，必顺延 |
| 10-11 日 | W4 + W5 两周复盘合并 | **不动** | 复盘档保留 |

**一条都没砍，全部有新日期。** 10-10 只做复习一件事，不排新内容 ——
停 12 天后直接上智能指针或 IPC，等于把 09-28~09-30 三天的投入作废。

---

### 🔴 2026-10-09 09:3x 追加重排（已被上方 23:00 版取代，保留备查）

> **教练 10-09 09:3x 三源核实 10-08 全天零痕迹**（不是只看文件 mtime，那是 09-24 犯过的错）：
> ① 四个仓 `find -newermt "2026-10-07 23:59"` 全部零命中
>    （计划仓 / `cpp-practice` / `vite-project` / `ai-desktop-assistant`）
> ② `daily/history/` 无 `2026-10-08.md`；`progress.jsonl` 最后一条仍是 09-30
> ③ `profiles/coach/state.db` 从 09-30 23:0x 到 10-09 10:17 之间**零 session**；
>    `cron/usage_audit.jsonl` 从 09-30 直接跳到 10-09 ——
>    **三条 cron 在 10-01 ~ 10-08 一次都没跑，10-08 本人没收到任何推送。**
>
> **结论：停训实际 9 天（10-01 ~ 10-08），比原估 7 天多两天。**
> `docs/calendar-holidays.md` 4.2「节后第一天上午整段用于间隔复习」**照旧生效，10-09 执行**。

| 原定日 | 原定内容 | 新去向 | 性质 |
|---|---|---|---|
| 10-08 四 | 间隔复习 + C++ 7 天复测 + Rule of 2 复测 + base 顶层扫描 + q-fw 第四格 | **→ 10-09（五）** | 整体右移 |
| 10-09 五 | `variant` / `std::visit` / `Result<T>`、结构化绑定、q-fw 第五格三方对照表 | **→ 10-10（六，调休上班日，按 1.5h 不是 4h）** | 容量类，必顺延 |
| 10-10 六 | `if constexpr`、Electron `electron-store` 持久化 | **→ W6（10-12 起）** | 容量类，必顺延 |
| 10-11 日 | W4 + W5 两周复盘合并 | **不动** | 复盘档保留 |

**顺延理由（不是切知识点，一条未砍，全部有新日期）**：
`variant` 是本人完全没学过的新知识点，按 09-28 铁律必须先讲定义再让他验证，
需要一个完整时段；塞进 10-09 这个「停 9 天后的复习日」会变成两层未知叠加，
与 09-23 撤 `useReducer`、09-28 把 `useState` 留到 09-29 同一判据。

**教练另认两条账（10-09）**：
- 本文件第 166 行写「`webview.h` 第 63-68 行那**六个** `#if defined(ENABLE_CEF)` 函数」
  —— **实查是 4 个**（`grep -n ENABLE_CEF webview/webview.h` 只命中第 63 行一处；
  块内为 `WebViewRunChildProcess` / `WebViewInit` / `WebViewMessageLoopWorkOnce` /
  `WebViewIsCefEnabled`，且**都是自由函数不是成员函数**）。「六个」系照记忆写，**作废**。
- 原顺延 10-08 的「侧读 Chatbox `preload.ts`」—— 实查 `F:\code` 下**无 Chatbox 源码**，
  需联网拉仓库。**改期 10-10 并降为扩展项**，不算本人欠账
  （同类翻车 09-17、09-19 各一次：布置前未实抓来源）。

### 本周实际可用 4 天（已被上方 10-09 重排取代，保留备查）

| 日期 | 星期 | 排法 |
|---|---|---|
| ~~10-05 ~ 10-07~~ | ~~一/二/三~~ | 🚫 **国庆停训** |
| **10-08** | **四** | 🔴 **节后第一天 · 上午段整段用于间隔复习，不排新内容** |
| **10-09** | **五** | 正常 1.5h |
| **10-10** | **六** | ⚠️ **法定调休上班日** → 按**工作日 1.5h** 排，**不是** 4h 深度档 |
| **10-11** | **日** | 2h 复盘（W4 + W5 两周复盘合并做） |

### 🔴 10-08（节后第一天）必须是间隔复习，不是往下冲

**理由**：停训 7 天（10-01~10-07）+ 此前中秋停 3 天，
`useState`、组件/props、`useEffect` 这些**只学过一次、只写过一遍**的东西会掉干净。
停 7 天后直接排 `variant` 这类新内容，等于把前面三天的投入丢掉。

**10-08 上午 40min 复习方式（硬性）**：
1. **闭卷自答**，不许翻笔记：
   - `const [messages, setMessages] = useState([])` 这一行里，`[...]` 是什么语法？
   - `setMessages([...messages, x])` 为什么不能写成 `messages.push(x)`？
   - `useEffect(() => {...}, [])` 第二个参数不写会怎样？
   - `npm run X` 时 npm 做了什么？
   - map/set 的 `insert` 失效哪些迭代器？`unordered_map` rehash 失效哪些？（09-23 答错过两条）
2. **重跑一次自己 09-28~09-30 写的代码**，确认还能跑、还看得懂
3. **不是重读笔记**——读笔记会产生「我还记得」的错觉，闭卷答不出来才是真相

**10-08 下午段**才开始接 W4 顺延来的新内容（`variant` / `Result<T>` / 侧读 preload）。

### 本周原定内容的去向

W4 顺延来的东西占掉 10-08~10-10 三天，**本周原定的智能指针 + Electron IPC 主题整体顺延一周至 W6**。
→ **24 周总路线顺延约 1.5 周**，已在 `plan/roadmap-24-weeks.md` 标注，不重算终点日期
（本人目标是能力达标不是打卡天数，终点按实际进度定）。

**q-framework 第三层**（本文件下方）：前置条件是 W4 门禁「第二层四问」过关，
而第二层因假期只跑了三格（09-28/29/30），**第四格「抽象的破绽」顺延 10-08、第五格顺延 10-09**。
→ 第三层实际从 **10-10** 起跑，本周只能跑 1-2 格，其余顺延 W6。

---

## 本周主题

**C++ 智能指针深度** + **Electron IPC 机制** + **记事本主/渲染进程通信**
+ 🆕 **q-framework 第三层：CEF 多进程与 IPC 链路**

---

## 🆕 本周 q-framework 对照轨（2026-09-22 排入，依据 `docs/q-framework-track.md`）

**本周主题与 q-framework 第三层天然合流** —— 原定主题就是 Electron IPC，
q-framework 的 CEF 侧恰好是同一问题的另一种实现。

挂载：每天 17:00 段末尾 **15-20min**，下方原有内容不动。

**第三层四问（刷人的一层）**：
1. CEF 是多进程的。browser 进程和 renderer 进程之间怎么通信？
2. C++ 调 JS、JS 调 C++ 分别走什么路？
   （`cef/render/cef_render_appcmd_handler.cpp` → 跨进程 → `cef/browser/cef_browser_message_handler.cpp`）
3. 跨进程传参数，`std::string` 怎么过去的？谁拥有那块内存？
4. `ExcuteJavaScript` 带 callback，异步的。**那个 callback 在哪个线程被调用？**

**额外锚点**：`ipc/` 模块是团队手写的 Windows IOCP 命名管道
（带长度前缀序列化、最大 16MB、自动分片重组、多客户端会话管理，出处 `ipc/README.md`）。
→ 与 Electron 内置 IPC 对照：一个手写传输层，一个框架给好。

**细排**：W4 周日复盘后按本人实际进度定，不提前写死。
前置条件：W4 门禁「第二层四问」必须先过。

## 本周目标

- 深入理解 unique_ptr / shared_ptr / weak_ptr 三者的机制和适用场景
- 掌握 Electron IPC 三种方式：ipcMain.handle/on、webContents.send、MessageChannel
- Side project：真正实现主进程处理消息，渲染进程通过 IPC 通信

## 每日任务

### 周一（1.5 小时）

**C++ 30 分钟**：
- unique_ptr 深入：为什么无运行时开销？（相比裸指针）
- 陷阱题：unique_ptr 数组版本 `unique_ptr<T[]>` 和 `unique_ptr<T>` 区别在析构

**Electron 45 分钟**：
- 阅读 [IPC 官方教程](https://www.electronjs.org/docs/latest/tutorial/ipc)
- 理解 4 种 IPC 模式：Renderer→Main（单向）、Renderer→Main（请求-响应）、Main→Renderer、Renderer↔Renderer

**记录 15 分钟**

### 周二（1.5 小时）

**C++ 30 分钟**：
- shared_ptr 深入：control block 的结构，引用计数在哪
- 循环引用问题：两个对象互持 shared_ptr 会怎样

**Electron 45 分钟**：
- 在 side project 里加第 1 种 IPC：`ipcRenderer.send` + `ipcMain.on`
- 场景：用户发送消息 → 主进程接收 → console.log

**记录 15 分钟**

### 周三（1.5 小时）

**C++ 30 分钟**：
- weak_ptr：解决循环引用的机制
- 手写场景：Observer 模式，Subject 弱引用 Observer

**Electron 45 分钟**：
- IPC 请求-响应模式：`ipcRenderer.invoke` + `ipcMain.handle`
- 改造 side project：发送消息返回一个假的 AI 回复（写死的字符串）

**记录 15 分钟**

### 周四（1.5 小时）

**C++ 30 分钟**：
- shared_ptr 线程安全：引用计数是原子的，但对象本身不是
- make_shared vs new shared_ptr：性能和内存布局差异

**Electron 45 分钟**：
- Main → Renderer 主动推送：`webContents.send`
- 场景：主进程 setInterval 每秒推送一个时间戳到渲染进程
- 用来准备未来的流式响应

**记录 15 分钟**

### 周五（1.5 小时）

**C++ 30 分钟**：
- enable_shared_from_this：类内部安全获取自身 shared_ptr
- 场景：一个 Session 类，回调时需要传自己 → 用 shared_from_this

**Electron 45 分钟**：
- IPC 类型安全：如何在 TypeScript 里给 IPC channel 加类型
- 参考模式：定义 IPC channel 的类型枚举 + 类型化 wrapper

**记录 15 分钟**

### 周六（4 小时深度）

**上午 2 小时：智能指针综合练习**
- 场景 1：写一个简单的 shared_ptr 实现（约 100 行）
  - 引用计数、控制块、拷贝、移动、析构、operator->/*
  - 单元测试：多个 shared_ptr 指向同一对象，最后一个销毁时对象析构
- 场景 2：Observer 模式（Subject weak_ptr 持有 Observer，Observer shared_ptr 持有）
  - 演示：Observer 销毁后 Subject 不会崩溃

**下午 2 小时：Electron IPC 类型安全化**
- 定义类型化 IPC 层：
  ```typescript
  // shared/ipc.ts
  export enum IpcChannel { CHAT_SEND = 'chat:send', CHAT_REPLY = 'chat:reply' }
  export interface ChatSendPayload { text: string; conversationId: string }
  ```
- 主进程和渲染进程都用这层类型
- Chat UI 完整走 IPC：输入 → 渲染进程 IPC 发送 → 主进程处理 → 返回假响应 → 渲染进程更新 UI

### 周日（2 小时复盘）

**1 小时：周日复盘 + 智能指针闭卷小测**
- 闭卷回答：unique_ptr / shared_ptr / weak_ptr 三个场景各选哪个
- 闭卷回答：shared_ptr 循环引用怎么破

**1 小时：Chromium 学习博客素材整理**
- 目标：第 6 周发布第 1 篇博客
- 主题预备：《我如何一周内理解 Electron IPC —— 从 Chromium 部门工程师视角》
- 素材来源：本周学习笔记 + 官方文档 + 你自己踩的坑
- 只列大纲和素材，不写正文

## 本周门禁

- [ ] 简版 shared_ptr 可运行，通过单元测试
- [ ] Observer 模式无循环引用问题
- [ ] Side project：真实 IPC 打通，Chat UI 消息经过主进程处理
- [ ] IPC channel 类型化（TypeScript）
- [ ] 5 天日记 + 1 份周日复盘 + 博客大纲

## 卡壳降级

- shared_ptr 写不出来：读一份现成实现（folly、boost 简版），能看懂即可
- IPC 类型化不熟：先用 any，第 6 周补类型

## 参考

- 《Effective Modern C++》Item 18-21（智能指针章节）
- Electron IPC 官方文档
- Chromium Mojo 文档（本周仅浏览，不深入）
