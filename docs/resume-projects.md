# 简历项目段落（v1 · 精简版）

> **v1 日期**：2026-11-03 18:0x
> **v1 变更原因（他 11-03 17:5x 明令）**：
> 「简历上不用写的太详细，只需要把技术点列一下就行了，然后如果面试官让我介绍，
> 我就可以挑一些我比较熟悉的地方去讲述」
> → v0 的展开版（每条 3-4 行解释）作废，改为**技术点清单式**。
> 深度内容不进简历，进训练清单（`docs/interview-drill-list.md`）。

---

## 🔴 三条简历纪律（11-03 本人三次纠正后定稿）

1. **掌握度 ≥ 署名权**。只要能对着代码讲清「是什么 / 为什么这么做 / 换方案代价在哪」，
   都可以写进简历。不是只能写自己敲过的代码。
   （作废：11-03 教练两次错纪律——「只写做过的」「闭卷答不出不许写」）
2. **不编事实**。不能把别人的决策说成自己的、不虚构数字、不说没发生的事。
3. **选题唯一尺子**：能不能体现**对 Chromium 内核的深度 + 广度，以及对框架的理解**。
   「是不是我亲手敲的」不是尺子。

---

# 简历正文（可直接用）

## 360 安全浏览器 · Windows 客户端开发（2024-12 ~ 2026-01）

基于 Chromium 深度定制的浏览器产品，fork 上游独立分支按版本周期 merge。
参与客户端功能开发与维护，改动覆盖 Chromium 五个层级。

**负责方向**：错误页与异常兜底、扩展接入与权限、地址栏（omnibox）功能、
广告过滤、安装器与推广、云控实验开关落地。

**技术点**
- Chromium 代码分层：`chrome/` / `content/` / `components/` / `extensions/` / `net/` 的职责边界与选层依据
- 进程模型：Browser / Renderer / GPU / Utility 进程分工；站点隔离（Site Isolation）判据
- 跨进程通信：Mojo 接口定义与绑定机制
- 任务与线程模型：`base/task/`、`SequencedTaskRunner` / `SingleThreadTaskRunner` / ThreadPool
- 扩展系统：API schema 编译期生成 C++ 绑定、权限校验链路、扩展白名单
- omnibox 架构：`components/` 平台无关逻辑层与 Views 呈现层的分层设计
- WebUI：C++ 与网页侧通信机制；替换上游 `sad_tab` 兜底页接入自建 WebUI
- 智能指针：`scoped_refptr` 侵入式引用计数与 `shared_ptr` 的差异
- 构建系统：GN + Ninja、`gn args`、component build 对增量编译的影响
- 沙箱：Renderer 沙箱限制与受限进程的资源访问方式
- 崩溃定位：minidump 收集与分析
- 上游 merge 工程化：自有代码目录隔离降低冲突面、冲突定位与回归

---

## q-framework 通用小程序框架 · 框架与产品开发（2026-01 ~ 至今）

自研 Windows 桌面客户端框架，提供窗口、WebView 容器、进程管理、IPC、
自动升级、崩溃上报等基础能力，业务侧用网页技术写界面。团队 3-4 人。
基于该框架落地两款已上线产品：**全能解压缩**、**全格式音频转换器**。

**负责方向**：DuiLib 主界面、常驻进程、自动升级、Shell 扩展（独立完成）、
默认设置、右键菜单、第三方 SDK 接入（商单），以及两款产品的业务功能开发。

**技术点**
- WebView 双后端抽象：一个抽象基类统一 CEF 与 WebView2 两种内核，抽象边界与破绽
- CEF 多进程：browser / renderer 进程职责与启动顺序（框架嵌入 CEF，非维护 CEF 本身）
- C++ ↔ JS 双向调用：`HandleAppCmd` 跨进程命令分发全链路；`ExcuteJavaScript` 异步 callback 的线程归属
- 自研 IPC 传输层：Windows 命名管道 + IOCP、长度前缀协议、16MB 上限与分片重组、多客户端会话管理
- 与 Chromium Mojo 的对照：同一问题的两种工程方案及取舍
- 崩溃上报：crashpad 与 breakpad 双栈并存的历史原因与各自定位
- Chromium `base/` 复用：框架直接搬用 Chromium 基础库
- Shell 扩展：COM 组件被 `explorer.exe` 加载进其进程运行，稳定性约束
- 进程生命周期：常驻进程、单实例控制、升级时序（旧进程退出与新版本拉起）
- WebView2 进程外运行时的版本耦合风险
- 构建：GN + Ninja
- UI 双轨：DuiLib DirectUI 与 Lynx 跨平台 UI 的渐进迁移

---

## 个人优势（放简历顶部或面试开场）

同一套 Chromium 技术栈在两种形态下都落地过：**一个直接改内核，一个嵌入内核**。

| 同一个问题 | 360 浏览器 | q-framework |
|---|---|---|
| JS 调 C++ | 扩展 API（schema 编译期生成绑定） | `HandleAppCmd` 手写分发 |
| 多进程 | Chromium 原生四类进程 | CEF 包装的多进程 |
| 跨进程通信 | Mojo | 自研 IOCP 命名管道 |
| 任务调度 | `base/task/` | 同一套 `base/` |
| 崩溃收集 | Crashpad | crashpad + breakpad |
| UI | Views + WebUI | DuiLib + CEF/WebView2 + Lynx |
| 构建 | GN + Ninja | GN + Ninja |

---

# 🔴 下一步（教练的活，不占训练格）

按上面**每一个技术点**反推面试官会问什么，重建 `docs/interview-drill-list.md`。
规矩：题目必须能从简历这几行字里直接长出来，**不许用教练读源码得到的细节出题**
（11-03 他否掉的错误做法）。

技术点共 24 条（浏览器 12 + q-framework 12），每条反推 2-4 个追问 → 预计 50-80 题。
按「深度 + 广度」排优先级，不按日期轮转。

---

## 变更记录

- **2026-11-03 v0** 展开版初稿（每条 3-4 行解释）
- **2026-11-03 v1** 改精简技术点清单；三条纪律定稿；IOCP 和 crashpad 双栈
  按「掌握度 ≥ 署名权」纪律写回技术点；确认 Mojo 优先级高于 IOCP（目标岗是
  Chromium 内核方向，Mojo 必问）；确认 q-framework 是「嵌入 CEF」不是「CEF 本身」
