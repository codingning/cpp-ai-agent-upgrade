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

## 七、30 天吃透计划（2026-09-22 起，每天 25min）

### 设计原则（四条，均来自本人已立的规矩）

1. **每天有可验证产出**，不许「今天读了一下」。产出=一张调用链图 / 一段能跑的实验 / 一个改动
2. **从你独占的模块起手**，最有把握处建立读码方法，再推向陌生模块
3. **能动手就不只读**（你可编译可改可提 CL）—— **读十遍不如改一行**
4. **每个非当日主角的概念标一行「它是什么」**，不假设你会附带知识

### 前置概念清单（教练欠你的，D1 前补齐）

| 概念 | 它是什么 | 何时讲 |
|---|---|---|
| COM | Windows 的二进制组件标准，让 DLL 能被任何语言按接口调用 | D1 |
| Shell 扩展 | 注册给资源管理器的 COM 组件，右键菜单/图标由它提供 | D1 |
| GN / Ninja | GN 生成构建描述，Ninja 执行编译 | D3 |
| DuiLib / DirectUI | 用 XML 描述界面、自绘控件的 UI 库，无 Windows 原生控件 | D6 |
| Windows 服务 | 开机自启、无界面、可高权限运行的后台进程 | D11 |
| 命名管道 | Windows 进程间通信机制，像文件一样读写 | D13 |

---

### 🟢 阶段一（D1-D5）· 从你 100% 独占的模块起手

**目标**：建立读码方法论，先在最有把握的地方把「读懂」的标准立起来。

| 日 | 任务 | 产出物 |
|---|---|---|
| D1 | 读 `shell_extension/omnizip_shell.cpp` 全文（仅 2 文件） | 调用链图：右键点击 → 系统加载 DLL → 谁被调用 → 菜单项怎么出来 |
| D2 | 答三问：注册表里注册了什么？为何要 32/64 两个 DLL？`regsvr32` 做了什么 | 闭卷三问，写进当日记录 |
| D3 | 读 `shell_extension/BUILD.gn` + 跑一次编译 | 说清这个 DLL 是怎么被构建出来的 |
| D4 | **动手**：改一句菜单文案，编译，实机验证生效 | 编译输出 + 截图 |
| D5 | 小结 | 一段 150 字的「Shell 扩展我做了什么」，直接可进简历 |

**验收**：不看代码讲清「用户右键一个 zip 文件，从点击到菜单弹出，中间发生了什么」。

---

### 🟢 阶段二（D6-D10）· 主 UI 与 DuiLib

**目标**：`app/appmain/` 你有 32 次提交，`application.cc` 是你改最多的文件（19 次）。
但你排第四，**这块要区分「我改过」和「我理解全局」**。

| 日 | 任务 | 产出物 |
|---|---|---|
| D6 | 读 `app/main.cc` → `app/appmain/dllmain.cc` → `application.cc` 的启动链 | 启动时序图：exe 起来到主窗口显示 |
| D7 | 读 `zip_main_window.cc`（你改 14 次）+ 对应 skin XML | 说清 XML 与 C++ 如何绑定 |
| D8 | DuiLib 的 MVC 三层约束（`CLAUDE.md` 第 69-79 行）逐条找出代码实例 | 每条约束配一处真实代码 |
| D9 | **对照 Electron**：DuiLib 的 XML+C++ vs Electron 的 HTML+JS | 对照表第一行 |
| D10 | 小结 + 你在主 UI 里真正做的事（翻你自己的 32 次 commit） | 简历口径定稿 |

**验收**：讲清「为什么 UI 线程禁止 IO」在这个项目里具体是怎么保证的。

---

### 🟢 阶段三（D11-D15）· 服务模块（你的第二个独占区）

**目标**：`service/` 你 9 次提交第一作者，**但你自述时完全没提**。这是被低估的硬技术点。

| 日 | 任务 | 产出物 |
|---|---|---|
| D11 | 读 `service/service_controller.cc`（你改 7 次） | 服务生命周期图：安装→启动→响应→停止→卸载 |
| D12 | 读 `installer/setup/service_installer.cc`（你改 7 次） | 服务是怎么被装进系统的 |
| D13 | 服务与主程序如何通信？找出机制 | 通信机制说明 |
| D14 | 答一问：**为什么需要一个服务？不用服务会死在哪？** | ⚠️ 这是你历史高频坑（因果倒置），必须答「不拆开会死在哪」 |
| D15 | 小结 | 简历第二个技术点定稿 |

**验收**：讲清「哪些操作必须由服务做，普通进程做不了」，并说出权限模型。

---

### 🟡 阶段四（D16-D22）· 你没写过、但技术含量高的部分

**这是你 09-21 主张的核心**：没写过也能吃透。**这一阶段的产出必须标「吃透，非我开发」。**

| 日 | 任务 | 产出物 |
|---|---|---|
| D16 | 读 `ipc/`（仅 5 文件） | IPC 机制说明 |
| D17 | **对照 Electron IPC**：`ipcMain/ipcRenderer` vs 本项目机制 | 对照表第二行 |
| D18 | 读 `webview/` 抽象层（52 文件，只读接口不读实现） | 接口清单 + 为何要抽象两种后端 |
| D19 | **对照 Electron `BrowserWindow`** | 对照表第三行 |
| D20 | 读 `ui/lynx_ui/lynx_window.h` 的 AppCmd 范式 | 说清 JS↔C++ 怎么通的 |
| D21 | **三方对照**：Lynx AppCmd / WebView / Electron IPC 是同一个模式吗 | 对照表第四行 |
| D22 | 压缩引擎集成方式（不读算法，只读怎么被集成） | 集成方式说明 |

**验收**：**这一阶段每份产出开头必须写「以下内容我未参与开发，为阅读理解」。**

---

### 🔵 阶段五（D23-D30）· 产出转化

| 日 | 任务 | 产出物 |
|---|---|---|
| D23-24 | 画整体架构图（draw.io，`docs/q-framework-arch.drawio`） | 架构图，标明哪些你写过 |
| D25-26 | 四选型对照表定稿（DuiLib / WebView / Lynx / Electron） | 面试可直接答的对照表 |
| D27 | 简历项目描述定稿 | 200 字以内 |
| D28 | **预演面试追问**：教练出 10 个刁钻问题，闭卷答 | 10 问答案 |
| D29 | 补漏 | — |
| D30 | 博客素材整理（可作为第 2 篇博客） | 大纲 |

---

## 八、与 Electron 学习线的挂钩（不额外占时间）

**原则：不是两条线，是一条线的两个样本。** W4 起每周 Electron 学到什么，当周就去 q-framework 找对应实现。

| Electron 学到 | q-framework 对照 | 挂钩周 |
|---|---|---|
| IPC（ipcMain/ipcRenderer） | `ipc/` + Lynx AppCmd | D16-17 ≈ W4 |
| BrowserWindow 窗口管理 | `app/appmain/zip_main_window.cc` | D18-19 ≈ W5 |
| 多进程模型 | EXE 壳 + DLL + service 进程 | D11-15 ≈ W5 |
| 打包分发 | `installer/` | 你已有实战 ✅ |
| 前端渲染 | Lynx vs Chromium | D20-21 ≈ W6 |

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
