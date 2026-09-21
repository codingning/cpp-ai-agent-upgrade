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

## 二、本人真实职责（git log 实查，2026-09-21 完成核实）

**⚠️ 实查结果与 09-21 自述有三处出入 —— 你低估了两块，高估了两块。**

### 按模块的作者分布（`git log --format="%an" -- <模块>`）

| 模块 | 你的提交 | 排名 | 其他主要作者 | 判定 |
|---|---|---|---|---|
| `shell_extension/` | **6** | **1/1** | 无 | 🟢 **100% 独占** |
| `service/` | **9** | **1/4** | liyun 4, litao8 1, lanshichao 1 | 🟢 **第一作者** |
| `installer/` | 19 | 2/4+ | lanshichao 108, liyun 18, litao8 13 | 🟡 重要贡献者 |
| `app/appmain/`（主 UI） | 32 | **4/4+** | liyun 101, lanshichao 85, litao8 65 | 🟡 参与者（非主力） |
| `components/compress/` | **2** | 末位 | liyun 17, litao8 17, xuhuazhi 15 | 🔴 **与自述严重不符** |
| `ipc/` | 1 | 并列 | 各 1 次 | ⚪ 极少 |
| `ui/lynx_ui/` | 0 | — | lanshichao 5 | ⚪ 未参与（与自述一致） |
| `webview/` | 0 | — | lanshichao 22, shangshihao 5 | ❌ 未参与 |

### 你改动最多的文件 TOP10

```
19  app/appmain/application.cc
16  installer/setup/install.cc
14  app/appmain/zip_main_window.cc
11  app/appmain/application.h
 7  service/service_controller.cc
 7  installer/setup/service_installer.cc
 5  shell_extension/omnizip_shell.cpp
 5  installer/setup/application.{h,cc}
 5  app/appmain/zip_main_window.h
 5  app/appmain/uninstall_retain_dialog.cc
```

### 三处出入（明日第一句话确认）

1. **`shell_extension/` 你低估了** —— 6/6 提交全是你，无第二作者碰过。
   简历可写「**独立负责**」，不是「参与」。
2. **`service/` 你完全没提** —— 9 次提交第一作者，且 `service_controller.cc` 是核心文件。
   Windows 服务 + 提权 + 进程通信，是硬技术点，**漏报可惜**。
3. **`components/compress/` 只有 2 次提交，但你自述「主要负责照片压缩」** ——
   ❓ **照片压缩代码是否在别的路径？请指出具体位置，教练重新核。**
   若确实只有 2 次，简历上「照片压缩」必须降级表述。

### 修正后的简历口径（待第 3 点确认后定稿）

- **独立负责**：Shell 扩展（COM 组件，32/64 双版本）
- **主导**：后台服务模块（`service/`）
- **核心贡献**：安装器（`installer/`，第二作者）
- **参与**：主 UI（`app/appmain/`，DuiLib 框架）
- **吃透但未参与开发**：IPC 机制、WebView 抽象层、压缩引擎集成、Lynx UI

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

- [x] ~~**Cheng Zhao 的 202 次提交具体改了什么**~~ ✅ **09-21 查清，教练昨日高估，已降级**
      - 实查：`build/` 3141 文件、`third_party/` 714、`buildtools/` 76、`tools/` 69
        —— **全是构建系统，零业务代码**。时间跨度 2016-07 ~ 2024-12
      - 提交标题样本：`Remove dependency on abseil` / `Do not assume clang on Windows`
        / `Update build configurations to latest` —— 构建维护，非功能开发
      - **结论修正**：不是「同源对照」，是「**同一套 GN 构建工具链**」。
        本仓 `build/` 引自 Cheng Zhao 的 `build-gn` 项目（Electron 作者维护的独立 GN 脚手架）
      - **剩余价值（降级但非零）**：读 Electron 源码时其 GN 构建体系你已天天在用，
        这是真实起点优势，但不等于业务代码同源
- [x] ~~`git log --author=ningxinyang` 逐模块核实职责边界~~ ✅ 09-21 完成，见第二节
- [ ] `webview/` 抽象层与 Electron `BrowserWindow` / `WebContents` 的接口对照
- [ ] `ipc/` 与 Electron IPC 的机制对照（⚠️ `ipc/` 仅 5 个文件，规模小，注意别高估）
- [ ] Lynx 的 `external.AppCmd` 与 Electron `ipcRenderer.invoke` 的对照
      （`lynx_window.h` 第 32-39 行注释已写明：LynxWindow 镜像 `QFrameWork::WebView` 接口，
      让 C++ 调用方用同一套 AppCmd 范式驱动两种后端 —— **这就是 IPC**）
- [ ] 项目是否有沙箱 / 权限隔离设计
- [ ] ❓ 照片压缩的真实代码位置（`components/compress/` 只有 2 次提交，与自述不符）

---

## 六、代码规模实查（决定投入，2026-09-21）

```
2827  base/        ← Chromium 原版，不是你们写的，不算学习量
1215  crashpad/    ← 第三方崩溃收集，同上
 536  tools/
 199  installer/   ← 你第二作者
 153  ui/
 140  components/
  98  testing/
  72  app/         ← 主 UI
  52  webview/
  31  service/     ← 你第一作者
   5  ipc/
   2  shell_extension/  ← 你 100% 独占
```

**关键判断：真正要啃的业务代码约 400-500 个文件**（app + components + ui + webview +
installer + service + ipc + shell_extension），不是 4000+。
`base/` 和 `crashpad/` 只当工具库查阅，**不读源码**。

这个规模 30 天可以吃透。

---

## 七、30 天吃透计划 · 技术深度版（2026-09-22 起，每天 25min）

> **⚠️ 本节于 09-21 晚重排。** 原版按「本人提交过的模块」排课，被本人当场驳回：
> 「不要只排我提交的部分，要排**重点技术框架和设计框架**，以及能体现**技术深度+广度**的部分」。
> **驳回成立。** 按职责边界排课，天花板是本人当前水平；按技术难点排课，天花板才是项目水平。
> 职责边界（第二节）只用于**简历表述**，不再用于**排课顺序**。

### 排课主轴：这个项目里最难的六样东西

实查确认的技术硬货（非推测，出处见各行）：

| # | 技术点 | 为什么是硬货 | 出处 |
|---|---|---|---|
| 1 | **IOCP 异步 IPC** | Windows 最高性能 I/O 模型；带长度前缀协议、16MB 大消息分片重组、多客户端会话管理。**自带 benchmark + unittest** | `ipc/README.md`、`iocp_named_pipe_benchmark.cc` |
| 2 | **Chromium 线程模型落地** | ThreadPool + WeakPtr + SEQUENCE_CHECKER 三件套在真实产品里的完整用法。**这是 Electron/Chromium 岗的核心考点** | `CLAUDE.md` 第 75-79 行 |
| 3 | **Windows 安全模型 / 服务提权** | `GetActiveUserToken` + `TokenLinkedToken` + UAC 提权 + 跨会话启动进程。**与 Chromium 沙箱同类知识** | `service/session_util.h` 第 8-18 行 |
| 4 | **WebView 双后端抽象** | 同一套接口驱动 WebView2 与 CEF 两种引擎；JS↔C++ 双向通信。**CEF 就是 Chromium 内核** | `webview/`、`CEF_JS_COMMUNICATION_GUIDE.md` |
| 5 | **可回滚安装（WorkItem）** | Chromium installer 的经典设计，事务化操作 + 失败自动回滚 | `installer/util/`，`CLAUDE.md` 第 166 行 |
| 6 | **门面 + 插件化引擎群** | `CompressService` 统一 6 种异构引擎（bit7z/FFmpeg/PDF/ONNX/ImageMagick/Office），含动态 DLL 加载 | `CLAUDE.md` 第 110-114 行 |

**补充广度素材**：`components/` 下 12 个子模块（登录/支付/埋点/默认程序/留存/激励视频/开屏广告）
—— 这是**商业化桌面产品的完整形态**，比纯技术更能体现工程广度。

---

### 🔴 阶段一（D1-D6）· IOCP 异步 IPC —— 全项目技术密度最高处

**为什么从这里开始**：① 它是整个项目的通信骨架；② 自带 benchmark 和 unittest，
**能跑能测能改数字**，符合「读十遍不如改一行」；③ 直接对标 Electron IPC，
是你面试差异化的最强武器。规模仅 5 个文件，不会陷进去。

| 日 | 任务 | 产出物（必须是图/实验，不许「我读了X」） |
|---|---|---|
| D1 | 前置课（教练讲）：同步 I/O / 异步 I/O / IOCP 各是什么，为什么需要 IOCP。然后读 `ipc/README.md` + `detailed.md` | 一句话答：**不用 IOCP 会死在哪**（⚠️ 你的高频坑：因果倒置，必须答「不拆开会死在哪」） |
| D2 | **跑起来**：编译并运行 `ipc_unittests.exe` + `iocp_named_pipe_benchmark.cc` | 真实 benchmark 数字截图 |
| D3 | 读 `iocp_named_pipe.h` 全部接口 | 类图：Server / Client / Session 三者关系 |
| D4 | 读消息协议实现：长度前缀、16MB 大消息如何分片重组 | 数据包结构图 + 一条消息从发到收的完整路径 |
| D5 | **动手实验**：改消息大小上限或并发数，重跑 benchmark，看数字怎么变 | 前后数字对比（⚠️ 必须有分辨力：先问「如果我的假设反了，数字会不一样吗」） |
| D6 | **对照 Electron IPC**：`ipcMain/ipcRenderer` vs IOCP 命名管道 | 对照表第 1 行：传输层 / 序列化 / 异步模型 / 谁更快为什么 |

**验收**：不看代码讲清「一条 20MB 的消息从客户端发出到服务端收到，中间经过哪些步骤」。

---

### 🔴 阶段二（D7-D12）· Chromium 线程模型在真实产品里的落地

**为什么重要**：**这是 Electron/Chromium 岗位的核心考点**。你已经学过 Chromium 进程模型（图已画），
但**线程模型没碰过**。而这个项目把 ThreadPool / WeakPtr / SEQUENCE_CHECKER 用在了生产代码里。

| 日 | 任务 | 产出物 |
|---|---|---|
| D7 | 前置课：`base::ThreadPool` / `WeakPtr` / `SEQUENCE_CHECKER` / `scoped_refptr` 各是什么 | 四个概念各一句话 |
| D8 | 在真实代码里找出 MVC 三层约束（`CLAUDE.md` 69-79 行）的实例 | 每条约束配一处真实代码位置 |
| D9 | 追一条完整链路：用户点「压缩」→ 投递线程池 → 后台执行 → 回 UI | 时序图（跨线程边界要标出来） |
| D10 | **专题 WeakPtr**：找出所有 `WeakPtrFactory` 用法，答「不用它会怎样」 | ⚠️ 与你 C++ 侧刚学的 Rule of 5 / 悬空指针**直接挂钩** |
| D11 | **动手实验**：故意在 UI 线程做一次 IO 或违反 SEQUENCE_CHECKER，看会怎样 | 崩溃/DCHECK 输出 |
| D12 | **对照 Electron**：Electron 的主/渲染进程 vs 这里的 UI/线程池 | 对照表第 2 行：进程隔离 vs 线程隔离，各自代价 |

**验收**：讲清「为什么 UI 线程禁止 IO」——不是背规则，是说出不遵守会死在哪。

---

### 🔴 阶段三（D13-D17）· Windows 安全模型 / 服务提权

**为什么是硬货**：`session_util.h` 里的 `GetActiveUserToken` / `TokenLinkedToken` / UAC 提权，
**与 Chromium 沙箱是同一类知识**（都是 Windows 令牌与权限模型）。
你已经学过 Electron 沙箱三层链，这里是它的 Windows 底层版本。

| 日 | 任务 | 产出物 |
|---|---|---|
| D13 | 前置课：Windows Session / Access Token / Primary Token / UAC 各是什么 | 四个概念各一句话 |
| D14 | 读 `service/session_util.h/.cc` | 答：服务（Session 0）为什么**不能直接**在用户桌面弹窗 |
| D15 | 读 `TokenLinkedToken` 提权路径 + `service_controller.cc` | 提权流程图 |
| D16 | 答核心一问：**哪些操作必须服务做，普通进程做不了？不拆服务会死在哪** | ⚠️ 再次针对因果倒置坑 |
| D17 | **对照 Chromium 沙箱**：Chromium 渲染进程沙箱 vs 这里的服务权限模型 | 对照表第 3 行：**这是你 Electron 沙箱知识的 Windows 底层版** |

**验收**：讲清「Session 0 隔离」是什么，以及它逼出了什么设计。

---

### 🟡 阶段四（D18-D23）· WebView 双后端抽象（含 CEF = Chromium 内核）

**为什么重要**：**CEF 就是 Chromium 嵌入式框架**，与 Electron 同源。
这个项目用一套接口同时驱动 WebView2 和 CEF —— **这是教科书级的抽象设计案例**。

| 日 | 任务 | 产出物 |
|---|---|---|
| D18 | 前置课：CEF / WebView2 各是什么，与 Electron 什么关系 | 三者关系图 |
| D19 | 读 `webview/webview.h` 抽象接口（只读接口不读实现） | 接口清单 + 答「为什么要抽象两种后端，直接用一种不行吗」 |
| D20 | 读 `CEF_JS_COMMUNICATION_GUIDE.md` + `CEF_READFILE_CALL_CHAIN.md` | JS→C++ 调用链图（**这是现成的调用链文档，白捡的深度**） |
| D21 | 读 `ui/lynx_ui/lynx_window.h` 的 AppCmd 范式 | Lynx 的 JS↔C++ 通信路径 |
| D22 | **三方对照**：CEF / WebView2 / Lynx / Electron 的 JS↔原生通信 | 对照表第 4 行（**四选一的技术选型题，面试高频**） |
| D23 | 答：这四种 UI 方案各自什么场景选哪个 | 选型决策表 |

**验收**：**本阶段每份产出开头必须写「以下内容我未参与开发，为阅读理解」。**

---

### 🟡 阶段五（D24-D26）· 架构设计模式专题

**这一段专攻「设计框架」**，是本人明确要求的部分。

| 日 | 任务 | 产出物 |
|---|---|---|
| D24 | **门面模式**：`CompressService` 如何统一 6 种异构引擎（含 PDF 动态 DLL 加载） | 类图 + 答「加第 7 种引擎要改几处」 |
| D25 | **WorkItem 事务模式**：`installer/util/` 可回滚操作单元（来自 Chromium） | 答「安装到一半失败了怎么回滚」 |
| D26 | **EXE 壳 + DLL 分层**：为什么不做成单个 exe | 答「这么切换来了什么，代价是什么」 |

---

### 🔵 阶段六（D27-D30）· 广度 + 产出转化

| 日 | 任务 | 产出物 |
|---|---|---|
| D27 | 扫 `components/` 12 个子模块（登录/支付/埋点/默认程序/留存/广告） | 一张商业化桌面产品的模块全景图 |
| D28 | 画整体架构图 `docs/q-framework-arch.drawio` | 架构图，标明哪些你写过、哪些你吃透 |
| D29 | 简历项目描述定稿 + 四选型对照表定稿 | 200 字简历段 + 对照表 |
| D30 | **预演面试**：教练出 10 个刁钻问题，闭卷答 | 10 问答案 |

---

### 📌 前置概念清单（教练欠的，到哪天讲哪天）

**不假设你会任何附带知识**（09-20 本人立的硬规矩）：

| 概念 | 何时讲 | 概念 | 何时讲 |
|---|---|---|---|
| 同步/异步 I/O、IOCP | D1 | Windows Session / Session 0 隔离 | D13 |
| 命名管道 | D1 | Access Token / Primary Token | D13 |
| `base::ThreadPool` | D7 | UAC / TokenLinkedToken | D13 |
| `WeakPtr` / `WeakPtrFactory` | D7 | CEF | D18 |
| `SEQUENCE_CHECKER` | D7 | WebView2 | D18 |
| `scoped_refptr` | D7 | 门面模式 / 事务模式 | D24/D25 |
| COM（Shell 扩展用） | 见下 | GN / Ninja | 随用随讲 |

---

### ⚪ 降级说明：你写过但技术密度低的部分

**Shell 扩展 / 主 UI / 安装器 UI 不单独排课**，原因：

- Shell 扩展仅 2 个文件，技术点是 COM 注册与 32/64 双版本 —— **半天能讲完，不值 5 天**
- 主 UI（DuiLib）是**将被淘汰的技术**，对 Electron 岗位无加分，只在 D8-D9 作为线程模型的载体出现
- 安装器 UI 同理，但其 **WorkItem 事务模式**有价值，已提到 D25

这三块的**简历表述**仍按第二节的 git 实查口径写（Shell 扩展可写「独立负责」），
但**学习投入**按技术密度分配，不按提交次数分配。

**如需单独准备面试话术**：D30 预演时会覆盖，不必单独占用学习日。

---

## 八、与 Electron / Chromium 学习线的挂钩（不额外占时间）

**原则：不是两条线，是一条线的两个样本。** 每个对照点都是面试可直接答的差异化素材。

| Electron/Chromium 侧 | q-framework 对照 | 挂钩日 | 对照要答清的 |
|---|---|---|---|
| Electron IPC（ipcMain/ipcRenderer） | IOCP 命名管道 | D6 | 传输层/序列化/异步模型/谁更快为什么 |
| Chromium 线程模型（已学进程模型，**线程模型是缺口**） | ThreadPool + WeakPtr + SEQUENCE_CHECKER 生产用法 | D12 | 进程隔离 vs 线程隔离，各自代价 |
| **Electron 沙箱三层链**（09-20 已结账） | Windows Token / Session 0 / UAC 提权 | D17 | **这是你沙箱知识的 Windows 底层版** |
| Chromium 内核嵌入 | CEF（= Chromium 嵌入式框架）+ WebView2 | D20-22 | 四种 JS↔原生通信方案选型 |
| Electron 打包分发 | `installer/` WorkItem 事务回滚 | D25 | 失败回滚怎么做 |
| React/Lynx 前端渲染 | Lynx AppCmd vs Electron preload | D21-22 | 两种前端集成范式 |

**面试落点**：这六行对照，每一行都是「只会 Electron 的人答不了」的题。
这才是 22K → 28-32K 的实际理由 —— **不是「我会 Electron」，是「我能做桌面技术选型」**。

---

## 九、时间与风险

- **每天 25min**，占下午时段一半，**不挤压 C++ 主线**
- 30 天 ≈ 750min ≈ 12.5h，落在 W3 末 ~ W7
- ⚠️ **风险**：D16-22 读陌生模块最容易变成「看过了」。
  对策：每日产出必须是**图或实验**，不许是「我读了 X 文件」
- ⚠️ **教练自查**：本计划每个阶段的第一天，先确认前置概念是否讲过，
  不许假设本人会 COM / 服务 / 命名管道等附带知识

---

## 十、简历落法（W7-24 outline 待改）

原计划只有一个 side project。改为两个：

1. **q-framework / OmniZip**（生产项目）—— 标注真实职责，技术陈述按上面三层
2. **ai-desktop-assistant**（学习项目）—— 标注自研，体现 Electron + AI 集成
