# q-framework 训练轨（面试深挖链驱动）

> 建立：2026-09-22（W3D2 下午）
> 依据：宁鑫洋 09-22 三条指令 —— ①不替换主线，与 Electron **对照**；
> ②按「面试官怎么一步步深挖」设计训练；③排课依据不是「他写过什么」，
> 而是「面试官挖得到、而他现在答不上来的那一层」。
> 自评结果（09-22 本人原话）：**第一层基本能答（缺 GN vs CMake 一问），第二层往后全不清楚。**
> → 训练**从第二层起排**，第一层只补一问。

---

## 零、排课总原则（09-21/09-22 两次被本人驳回后定稿）

1. ❌ 不按「本人提交过的模块」排课（09-21 本人驳回：要的是**重点技术框架与设计框架**、体现**技术深度+广度**）
2. ❌ 不替换 Electron 主线，不新开独立时段（09-22 本人指令：「没必要替换，只需要把他和 Electron 对照起来」）
3. ✅ **挂在现有 17:00-17:50 Electron 时段里做对照**，主线内容照常，q-framework 作为同一问题的「另一种答案」出现
4. ✅ 本人写过的六块（默认设置 / DuiLib 主页面 / 常驻进程 / 自动升级 / 右键菜单 / 商单接入）
   **不单独排周**，作为「他已有的答案」在对照时随时调用
5. ✅ 技术含量高 = **面试官挖得到、且他现在答不上来的那一层**（09-22 定义）

---

## 一、项目规模的标准答法（教练 09-22 实查，本人须自行复核）

面试官问「这项目多大」，考的不是行数，是**能不能描述一个系统的规模与边界**。

实查数据（`find` + `wc -l`，排除 `out/`）：

| 目录 | 文件数 | 行数 | 性质 |
|---|---|---|---|
| `base/` | 2827 | **621,270** | ⚠️ **Chromium 搬来的，不是团队写的** |
| `tools/` | 536 | 122,659 | 工具链 |
| `ui/` | 153 | 66,648 | DuiLib 主 UI |
| `installer/` | 199 | 41,484 | 安装器 |
| `components/` | 140 | 29,784 | 业务组件 |
| `app/` | 72 | 22,398 | 应用层 |
| `webview/` | 52 | 9,926 | **CEF + WebView2 双后端** |
| `testing/` | 98 | 9,851 | |
| `QFA_SDK/` | 15 | 7,046 | |
| `service/` | 31 | 5,318 | 🟢 本人第一作者 |
| `net/` `ipc/` `utils/` `shell_extension/` | 各 2-5 | 1,000-2,200 | 🟢 shell_extension 本人独占 |

**标准答法**（约 60 字，自己用话说出来，不要背）：

> 桌面端 C++17 项目，团队自有代码约 20 万行，直接复用 Chromium 的 `base` 库（另 62 万行）。
> GN + Ninja 构建，1172 次提交，核心开发 3-4 人。产品是 Windows 上的压缩工具。

**为什么这样答**：给出了结构——哪些自己写、哪些站在巨人肩上、用什么构建。
「三个人做的」显得太小，「几十万行」又是虚数。

---

## 二、🆕 重大发现（09-22 教练实查，推翻此前判断）

**`webview/` 不是单一 CEF，是「同一套接口 + 两种浏览器内核」的双后端架构。**

```
webview/
├── webview.h          ← 纯虚基类 QFrameWork::WebView，Create() 工厂 + 15 个纯虚函数
├── cef/       38 文件  ← CEF（Chromium Embedded Framework）
├── webview2/   8 文件  ← 微软 WebView2（Edge 内核，进程外运行时）
└── common/     2 文件
```

编译期 `#if defined(ENABLE_CEF)` 切换后端。

### 为什么这个发现改变了排课价值

本人手里有一个**同一接口、两种浏览器内核实现**的真实工程，
而 Electron 是**第三种**做法。→ **三方对照，不是类比。**

### CEF 侧的目录结构与 Electron 惊人同构

```
webview/cef/
├── browser/   ← 对应 Electron 主进程（main）
│   ├── cef_browser_process_app.cc
│   ├── cef_browser_message_handler.cpp
│   ├── cef_browser_file_handler.cpp
│   └── cef_browser_registry_handler.cpp
├── render/    ← 对应 Electron 渲染进程（renderer）
│   ├── cef_render_process_app.cc
│   ├── cef_render_message_handler.cpp
│   ├── cef_render_appcmd_handler.cpp     ← JS→C++ 的入口
│   ├── cef_render_file_handler.cpp
│   └── cef_render_registry_handler.cpp
└── common/    ← 两端共用（client_app、file_system_handler、async_file_task）
```

`browser/` ↔ `render/` 的对称拆分，**就是 Electron 的 main/renderer 拆分**。
每一对 `*_handler` 都跨进程成对出现 —— 这正是 `ipcMain` / `ipcRenderer` 的模式。

### 现成的对照锚点

- `webview.h` 第 55-56 行注释原文：
  「宿主窗口 DPI 变化时调用（如 WM_DPICHANGED）。**WebView2 通常无需额外处理；CEF 需同步 renderer 的 device scale**。」
  → 一句话点出两种架构的进程模型差异，是面试可讲的具体细节。
- `webview.h` 第 63-68 行：六个函数被 `#if defined(ENABLE_CEF)` 包着暴露在抽象层外
  （`WebViewRunChildProcess` / `WebViewInit` / `WebViewMessageLoopWorkOnce` / `WebViewIsCefEnabled`）
  → **抽象层的破绽**。为什么这六个抽不进纯虚基类？这是第二层的压轴问。
- `ipc/` 模块：Windows IOCP 命名管道，带长度前缀的消息序列化、最大 16MB、
  自动分片重组、多客户端会话管理（出处 `ipc/README.md`）
  → 与 Electron 的 IPC 对照：一个手写传输层，一个框架内置。

---

## 三、面试深挖链（四层）—— 训练大纲的骨架

> 用法：这不是问题清单，是**排课依据**。本人自评「第几层开始答不上」，训练就从那层排。
> 09-22 自评结果：**第一层缺一问，第二层起全不清楚。**

### 第一层 · 确认你真在里面干过 —— ✅ 09-22 自评基本能答

- 这项目多大？几个人？你负责哪块？→ 见上「标准答法」
- 构建系统是什么？→ 本人能答：GN + Ninja
- ❌ **唯一缺口：为什么不用 CMake？** → 排为 W4D1 作业（提示：看 `.gn` 与 `BUILD.gn`，
  再想 `base/` 是从哪来的）

**本人自述职责**（09-22 原话）：设置默认、DuiLib 主页面、常驻进程、自动升级、右键菜单、商单接入。
本人自评「都是我认为的简单功能，没做深度开发」——
⚠️ 这六块**不是不值钱**，是**还没被问到值钱的那一面**。见第五节。

### 第二层 · 确认你懂架构，不只是改过几行 —— 🔴 训练起点

1. 一个 WebView 从创建到显示，经过哪几层？
2. `webview.h` 那个抽象基类为什么要存在？直接调 CEF 不行吗？
3. 两个后端（CEF / WebView2）能抽成同一个接口，说明什么？
4. **哪些地方抽不动、要开后门？**（第 63-68 行那组 `#if defined(ENABLE_CEF)`）

### 第三层 · 这一层刷人 —— 🔴 与 24 周主线 Chromium 进程模型天然合流

1. CEF 是多进程的。browser 进程和 renderer 进程之间怎么通信？
2. C++ 调 JS、JS 调 C++ 分别走什么路？（`HandleAppCmd` 那条链，
   `cef_render_appcmd_handler` → 跨进程 → `cef_browser_message_handler`）
3. 跨进程传参数，`std::string` 怎么过去的？谁拥有那块内存？
4. `ExcuteJavaScript` 带 callback，异步的。**那个 callback 在哪个线程被调用？**

### 第四层 · 加分项，答不上不致命

1. CEF 的沙箱和 Electron 的沙箱是同一套吗？
2. WebView2 是进程外的，Edge 更新了你的程序会不会崩？
3. 崩溃了怎么定位？（项目里 `crashpad/` 和 `breakpad/` 两套并存 —— 为什么两套？）

---

## 四、排期（正式落地，不再挂「下一步」）

**起始日：2026-09-28（周一）= W4D1。**
W3 剩余时间不动（React 补课 + MyVector 收尾优先）。

| 周次 | q-framework 内容 | 挂载方式 | 对应层 |
|---|---|---|---|
| **W4** | `webview/` 抽象层：双后端设计、接口边界、抽象的破绽 | 挂 17:00 段，每天 **15min** 对照 | 第二层 |
| **W5-W6** | CEF 多进程 + IPC 链路（browser/render 成对 handler、AppCmd 全链路、线程模型） | 挂 17:00 段，每天 **15-20min** | 第三层 |
| W7+ | 沙箱对照、crashpad/breakpad、构建系统深挖 | 待 W6 复盘后定 | 第四层 |

**硬约束（防教练自己缩水）**：
- 15min 是**保底不是上限**（本人 09-16 立的规矩）；有余力就往深推
- 不许用「今天不做」切知识点，只分「主线必补」与「扩展有余力再上」（本人 09-21 立规）
- 每天的 q-framework 对照项**必须写进当日记录**，不许无声消失

---

## 五、本人写过的六块 → 与 Electron 的对照点（随时调用，不单独排周）

本人自评「简单功能」。**反驳：它们不是简单，是还没被问到值钱的那一面。**

| 本人写过 | Electron 里的同一问题 | 值钱在哪（面试可讲的角度） |
|---|---|---|
| **常驻进程** | `app.on('window-all-closed')` 要不要 `quit()`；单实例锁 | 进程生命周期谁说了算；窗口全关 ≠ 进程该死 |
| **自动升级** | `autoUpdater` 模块 | 你是**手写**的，Electron 是框架内置 —— 差异本身就是考点：差分更新？签名校验？升级中进程在跑怎么办？ |
| **右键菜单**（`shell_extension/`，**本人 6/6 独占**） | Electron `Menu` / `Tray` | ⚠️ **完全不是一回事**：Shell 扩展是 COM 组件**被 explorer.exe 加载进它的进程**。你的代码跑在别人进程里——崩了会拖垮资源管理器。这个反差是强考点 |
| **自动升级 + 常驻进程** | — | 两者耦合：升级时常驻进程要不要退？谁来拉起新版本？ |
| **默认设置** | `electron-store` / 配置持久化 | 配置读写的线程安全、多进程同时写怎么办 |
| **DuiLib 主页面** | BrowserWindow + HTML/CSS | **同一个问题的两种答案**：原生控件树 vs DOM 树。为什么这个产品主 UI 不用网页？ |
| **商单接入** | — | 待本人补充技术细节后填 |

⚠️ **教练 09-21 在此处犯过错**：曾以「没写过就讲不清」反对本人吃透全项目，
被本人以「项目不大、三四人做、水平相当、只是模块不同」驳回，教练核 `git log` 后收回。
**唯一保留的硬规矩：「我写的」和「我吃透的」要能分开说。**

---

## 六、W4 每日对照项（正式排课，W5-W6 待 W4 复盘后细排）

> 每天 15min，挂在 17:00-17:50 段尾。Electron 主线内容不动。
> ⚠️ 本人 09-20 立的硬规矩：**不许假设他会题目里的任何附带知识**。
> 故每个非当日主角的概念标一行「它是什么」。

**名词表（先读这个，都是本人未标掌握的）**
- **CEF** = Chromium Embedded Framework，把 Chromium 打包成一个库供 C++ 程序嵌入网页
- **WebView2** = 微软方案，复用系统上**已装的 Edge 运行时**，不自带内核
- **DuiLib** = Windows 上的 DirectUI 库，用 C++ 画原生界面，不走 HTML
- **纯虚函数 / 抽象基类** = 本人已掌握（W2 特殊成员函数训练覆盖）

| 日 | 主角 | 动作（本人做，教练不代写） | 验收 |
|---|---|---|---|
| **W4D1 09-28** | 补第一层缺口 | 查 `.gn` / `BUILD.gn`，答「为什么不用 CMake」 | 能说出与 `base/` 来源的关系 |
| **W4D2 09-29** | 双后端全景 | 只读 `webview/webview.h` 70 行，画出接口全貌 | 说清 `Create()` 为什么是 static，`Delegate` 是干什么的 |
| **W4D3 09-30** | 抽象的理由 | 对比 `cef/cefwebview_impl.h` 与 `webview2/webview2_impl.h` 的类声明 | 答第二层问 2、3 |
| **W4D4 10-01** | **抽象的破绽** | `webview.h` 第 63-68 行那六个函数 | 答：为什么抽不进纯虚基类（**压轴**） |
| **W4D5 10-02** | 三方对照 | CEF / WebView2 / Electron 三者的进程模型各是什么 | 一张对照表，本人自画 |
| W4 周末 | 收口 | 把第二层四问闭卷自答 | 四问全答 = 第二层结账 |

**W4 门禁（q-framework 侧）**：第二层四问闭卷可答 + 一张三方对照表。

---

## 七、待查线索（跨周保留）

- ⚠️ **Cheng Zhao（Electron 创造者）在本仓库 202 次提交** ——
  若 `webview/` 抽象层与 Electron `BrowserWindow` 同源，则对照学习升级为**同源对照**。
  `ui/lynx_ui/lynx_window.h` 第 32-39 行注释自述「镜像 QFrameWork::WebView 接口」。
  **待查：Cheng Zhao 的 202 次提交集中在哪些目录**（教练 W4D1 前实查 `git log --author`）
- `crashpad/` 与 `breakpad/` 两套崩溃收集并存，为什么（第四层）
- `components/compress/` 本人仅 2 次提交但自述「主要负责照片压缩」——
  **本人 09-22 指示：简历口径不再讨论**。此条仅作为「排课需要知道手感分布」保留，不追问
