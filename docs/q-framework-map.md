# q-framework 吃透计划（简历主项目）

> 建立：2026-09-21（W3D1 晚）
> 项目路径：`E:\code\q-framework`（本人可访问、可构建）
> 产品：Windows 桌面「全能压缩（OmniZip）」

---

## 一、项目事实（教练实查，非推测）

**技术栈**（出处 `CLAUDE.md` 第 7-13 行）：

- 纯 C++17，Chromium 代码风格
- 构建：**GN + Ninja**（Chromium 同款）
- 编译器：MSVC 2022，可选 Clang 18
- 架构：EXE 壳 + `appmain.dll`（主业务）+ 静态库组件群
- 平台：Windows Only（x86 / x64 双版本）

**不是 Electron**。主 UI 用 DuiLib DirectUI（C++ 原生控件），
网页技术只以嵌入组件形式存在（`webview/` → 登录、支付模块）。

**Lynx**（出处 `ui/lynx_ui/lynx_window.h` 第 1 行版权头 "The Lynx Authors"）：

- Lynx = 字节跳动开源的跨平台 UI 框架，C++ 渲染引擎
- **不是 React**，但上层写法是 ReactLynx —— 用 React 语法（JSX/组件/hooks）写 Lynx 界面
- 项目内已有产物：`components/ForceAssociation/Window/frontend/dist/def.lynx.bundle`
- 定位（`process/context/all-context.md` 第 96 行）："Secondary UI，alternative frontend renderer"

**提交统计**（`git log` 实查，1172 commits，2016-07 ~ 2026-09）：

| 作者 | 提交数 | 备注 |
|---|---|---|
| lanshichao | 359 | |
| **Cheng Zhao** | **202** | ⚠️ Electron 创造者。项目含 Electron/Chromium 同源代码，待查 |
| autobuild | 162 | 机器人 |
| liyun | 130 | |
| litao8 | 92 | |
| xuhuazhi | 72 | |
| **ningxinyang** | **56** | 本人 |
| shangshihao | 31 | |

**结论**：核心开发者三四人，模块划分清晰，水平相当。
本人「没写过的模块也能吃透」的判断成立 —— 这不是大型项目的分工壁垒。

---

## 二、本人真实职责（自述，待用 git log 逐模块核实）

| 模块 | 路径 | 参与度 |
|---|---|---|
| 主 UI | `app/appmain/`（DuiLib） | ✅ 主要负责 |
| 照片压缩 | `components/compress/idPhoto/` + `imagemagick/` | ✅ 主要负责 |
| Shell 扩展 | `shell_extension/` | ✅ 主要负责 |
| Lynx UI 交互 | `ui/lynx_ui/` | ⚠️ 写过一些，不多 |
| 其余模块 | IPC / net / webview / 各压缩引擎 / installer | ❌ 未参与 |

---

## 三、唯一硬规矩（09-21 确立）

> **讲什么都可以，但「我写的」和「我吃透的」要能分开说。**

面试标准答法示例：
「IOCP 命名管道那套 IPC 不是我写的，但我读透了，还自己重写过一版验证。」

这个回答同时展示诚实和能力，且无被戳穿风险。
反面：声称「全是我写的」→ 被追问选型细节答不上 → 真写过的部分也一起失信。

**不限制吃透范围。不限制简历写整个项目。只限制职责表述。**

---

## 四、三层目标

### 第一层 · 把真写过的三块讲到「为什么这么设计」

- **Shell 扩展**：COM 注册机制、为何 32/64 两个 DLL、`regsvr32` 做了什么、
  为何不在主干编译需独立分支（`CLAUDE.md` 第 137-150 行有完整流程，有故事可讲）
- **照片压缩**：ImageMagick 集成方式、AI 证件照的 ONNX + OpenCV 链路
- **主 UI**：DuiLib 的 MVC 三层约束（`CLAUDE.md` 第 69-79 行）、
  UI 线程禁 IO、`base::WeakPtr` 防悬空回调、`SEQUENCE_CHECKER` 线程归属标注

### 第二层 · 全局架构（不声称自己写，但能讲清）

- EXE 壳 + `appmain.dll` 为何这么切
- IPC 为何选 IOCP 命名管道（不选共享内存 / socket / 消息队列）
- 线程模型三条规则的因果
- `base/` 库的边界：哪些是 Chromium 原版，哪些是本项目改的

### 第三层 · 横向对照（真正的差异化优势）

这是 22K → 28-32K 的实际理由：**不是「我会 Electron」，是「我能做桌面技术选型」。**

| 维度 | Electron | q-framework | 对照要答清的问题 |
|---|---|---|---|
| 跨进程通信 | `ipcMain` / `ipcRenderer` | IOCP 命名管道 | 各自取舍？延迟/吞吐/复杂度 |
| UI 层方案 | 全网页 | DuiLib / WebView / Lynx 三选 | 四种方案什么场景选哪个 |
| 进程模型 | 主进程 + 渲染进程 | EXE 壳 + DLL + 独立进程 | 隔离级别差在哪 |
| 沙箱 | Chromium 渲染进程沙箱 | 待查 | 有没有沙箱？没有的话风险在哪 |
| 前端集成 | React + Vite | ReactLynx + lynx.bundle | 构建产物、加载方式差异 |
| 资源打包 | asar | `create_ui_skin` → zip | |

---

## 五、待查清单（教练负责，查完填回本文件）

- [ ] **Cheng Zhao 的 202 次提交具体改了什么** —— 若 `webview/` 接口与 Electron
      `BrowserWindow` 同源，则对照学习不是类比而是**同源对照**，价值大幅提升
- [ ] `git log --author=ningxinyang` 逐模块核实本人真实职责边界
- [ ] `webview/` 抽象层与 Electron `BrowserWindow` / `WebContents` 的接口对照
- [ ] `ipc/iocp_named_pipe.h` 与 Electron IPC 的机制对照
- [ ] Lynx 的 `external.AppCmd` 与 Electron `ipcRenderer.invoke` 的对照
      （`lynx_window.h` 第 32-39 行注释已写明：LynxWindow 镜像 `QFrameWork::WebView` 接口，
      让 C++ 调用方用同一套 AppCmd 范式驱动两种后端 —— **这就是 IPC**）
- [ ] 项目是否有沙箱 / 权限隔离设计

---

## 六、排期原则（W4 起，待定稿）

**不作为额外任务，作为对照主线**：每周 Electron 学到什么，就去 q-framework 里找对应实现。

例：
- 学 Electron IPC 那周 → 同步读 `ipc/iocp_named_pipe.h`，写一份对照笔记
- 学 Electron 多窗口那周 → 同步读 `app/appmain/main_window.h` 的 DuiLib 窗口管理
- 学 React 那周 → 同步读 `ui/lynx_ui/` 的 ReactLynx 用法

**产出物**：每个对照点一段笔记，最终汇成简历项目的技术陈述 + 博客素材。

---

## 七、简历落法（W7-24 outline 待改）

原计划只有一个 side project。改为两个：

1. **q-framework / OmniZip**（生产项目）—— 标注真实职责，技术陈述按上面三层
2. **ai-desktop-assistant**（学习项目）—— 标注自研，体现 Electron + AI 集成
