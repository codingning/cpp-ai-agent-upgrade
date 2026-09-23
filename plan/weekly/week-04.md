# Week 04（第 4 周，2026-09-28 ~ 2026-10-04）

## 🚫 本周重大调整：国庆停训 4 天（09-23 本人提出 + 教练实查后确定）

> **本人 09-23 原话**：「马上国庆节了，国庆 7 天假期我是没有时间学习的，这个假期你得跳过」。
>
> **依据**：国办发明电〔2025〕7 号 —— **国庆 10月1日（周四）~ 7日（周三）放假调休 7 天**。
> 教练 09-23 实查（人民网 / 中国政府网 / 国新办多源一致），见 `docs/calendar-holidays.md`。
>
> **本周（09-28 ~ 10-04）实际只剩 3 个训练日：09-28（一）、09-29（二）、09-30（三）。**
> 10-01 ~ 10-04 全部停训，本周原有的周四/周五/周六 4h 深度/周日 2h 复盘**全废**。
>
> **长假期间不留作业、不设「有空看看」、不做任何变相排课**（本人说了没时间，就是没时间）。
> 教练 10-01 ~ 10-07 的每日 cron 推送应停或改静默。

### 本周三天怎么排（内容一条不切，全部标明来源）

| 日 | 上午 C++ 30min | 下午 Electron 45min | 末尾 15min |
|---|---|---|---|
| **09-28 一** | `string_view`（本周原排） | 🔴 **useState**（中秋顺延来的 W3D5）+ 组件/props 补齐 | q-framework 第一层缺口 |
| **09-29 二** | `optional`（本周原排）+ 🔴 STL 算法/Lambda/词频题（中秋顺延来的 W3D5） | preload.js + contextBridge（本周原排） | q-framework 双后端全景 |
| **09-30 三** | 🔴 **W3 周复盘 + 迭代器失效 5 场景小测**（中秋顺延） | 🔴 **useEffect 概念课**（中秋顺延来的 W3 周六下午） | q-framework 抽象的理由 |

> **09-30 是国庆前最后一个训练日**，收工前必须额外做两件事：
> 1. **写一份「假期后第一件事」清单**（10-08 复训时照着走，不靠回忆）
> 2. **把 09-28/29/30 三天写的 React 代码全部 commit + push**，
>    假期七天后回来时代码状态是确定的

### 本周原有内容的去向（一条未切）

- `variant` / `std::visit` / `Result<T>`（原周三 C++）→ **顺延 10-08（周四）**
- 结构化绑定（原周四 C++）→ **顺延 10-09（周五）**
- `if constexpr`（原周五 C++）→ **顺延 10-10（周六，调休上班日，按 1.5h 工作日排）**
- 侧读 Chatbox preload.ts（原周三 Electron）→ **顺延 10-08**
- 「新建对话 / 切换对话」UI（原周四 Electron）→ **顺延 10-09**
- Electron 持久化 electron-store（原周五 Electron）→ **顺延 10-10**
- 简易 JSON parser（原周六上午 2h）→ **顺延 10-17（周六，W6 深度档）**
- **简历 v0 保底版（原周六下午 2h）→ 顺延 10-17 下午**
  ⚠️ 这条是**抗风险项**（「如果第 5 周被裁，这份简历能立刻投」），顺延两周有实际风险。
  **本人若认为不能等，说一声，教练把它提到 09-30 或节后 10-08 优先做。**
  （本人 09-22 已明确：简历不用教练写，教练只负责训练计划）
- 周日复盘（原 10-04）→ **顺延 10-11（周日）**，与 W5 复盘合并

### q-framework 对照轨的影响

**起始日 09-28 维持不变**（09-22 定，不因假期推迟）。
但本周只能跑三天（原表的周一/周二/周三三格），**周四「抽象的破绽」= 压轴那格顺延 10-08**，
周五「三方对照表」顺延 10-09。下方原表**保留不动**，此处标明实际执行日。

---

## 本周主题

**C++17 现代特性** + **Electron 渲染进程与 Preload** + **简历"保底版"完成**
+ 🆕 **q-framework 对照轨启动（第二层：架构理解）**

---

## 🆕 本周变更（2026-09-22 定，本人指令）

**q-framework 对照轨从本周正式起跑。** 依据 `docs/q-framework-track.md`。

三条本人指令（09-22 原话）：
1. 「没必要替换啊，只需要把他和 Electron 对照起来就行了」→ **不替换主线，不新开时段**
2. 「假如你是一个面试官…你先提出问题，再根据问题给我设计训练方式」→ **按面试深挖链排课**
3. 「哪里技术含量高我哪有你判断的准」→ 改用客观判据：
   **技术含量高 = 面试官挖得到、而他现在答不上来的那一层**

本人自评结果：**第一层基本能答（缺「为什么不用 CMake」一问），第二层往后全不清楚。**
→ 本周从**第二层**起排。

**挂载方式**：每天 17:00-17:50 段**末尾 15min**，下方原有 Electron 45min 内容**一律不动**。
15min 是保底不是上限。

### 🆕 重大发现（09-22 教练实查，推翻此前「不是 Electron 所以只能类比」的判断）

`webview/` 是**同一套接口 + 两种浏览器内核**的双后端架构：

```
webview/webview.h    ← 纯虚基类 QFrameWork::WebView，15 个纯虚函数
webview/cef/         ← CEF（Chromium Embedded Framework），38 文件
   ├── browser/      ← 对应 Electron 主进程
   ├── render/       ← 对应 Electron 渲染进程
   └── common/       ← 两端共用
webview/webview2/    ← 微软 WebView2（Edge 内核），8 文件
```

`browser/` ↔ `render/` 的对称拆分**就是 Electron 的 main/renderer 拆分**，
每一对 `*_handler` 跨进程成对出现 = `ipcMain`/`ipcRenderer` 模式。
→ 本人手里有「同一接口两种内核」的真实工程，Electron 是第三种做法，
**三方对照，不是类比**。

### 本周 q-framework 每日 15min

| 日 | 主角 | 动作（本人做，教练不代写） | 验收 |
|---|---|---|---|
| 周一 09-28 | 补第一层缺口 | 查 `.gn` / `BUILD.gn`，答「为什么不用 CMake」 | 能说出与 `base/` 来源的关系 |
| 周二 09-29 | 双后端全景 | 只读 `webview/webview.h`（70 行），画出接口全貌 | 说清 `Create()` 为什么 static、`Delegate` 干什么 |
| 周三 09-30 | 抽象的理由 | 对比 `cef/cefwebview_impl.h` 与 `webview2/webview2_impl.h` | 答：抽象基类为什么要存在，直接调 CEF 不行吗 |
| 周四 10-01 | **抽象的破绽** | `webview.h` 第 63-68 行那六个 `#if defined(ENABLE_CEF)` 函数 | 答：为什么抽不进纯虚基类（**压轴**） |
| 周五 10-02 | 三方对照 | CEF / WebView2 / Electron 三者进程模型 | 一张对照表，本人自画 |

**名词表**（本人未标掌握的一律标注，09-20 硬规矩）：
- **CEF** = Chromium Embedded Framework，把 Chromium 打包成库供 C++ 程序嵌入网页
- **WebView2** = 微软方案，复用系统上**已装的 Edge 运行时**，不自带内核
- **DuiLib** = Windows 上的 DirectUI 库，用 C++ 画原生界面，不走 HTML

---

## 本周目标

- 掌握 C++17 关键特性：结构化绑定、optional、variant、string_view
- 理解 Electron Context Isolation 和 preload 机制
- 完成简历 v0（应急保底版）
- 记事本加持久化（本地存储对话记录）

## 每日任务

### 周一（1.5 小时）

**C++ 30 分钟**：
- `std::string_view`：为什么需要它，与 const string& 区别
- 陷阱：string_view 悬垂引用
- 写代码：一个函数接受 string_view 参数，测试传入字面量、std::string、char*

**Electron 45 分钟**：
- 阅读 [Context Isolation](https://www.electronjs.org/docs/latest/tutorial/context-isolation)
- 理解：为什么默认打开 contextIsolation？关闭有什么安全风险？

**记录 15 分钟**

### 周二（1.5 小时）

**C++ 30 分钟**：
- `std::optional`：表达"可能没有"的语义
- 写一个函数：查找 vector 中第一个大于 N 的数，返回 optional
- 对比：以前用什么方式表达"没找到"（-1、nullptr、bool 返回值+out 参数）

**Electron 45 分钟**：
- 阅读 [preload script](https://www.electronjs.org/docs/latest/tutorial/tutorial-preload)
- 在 side project 中添加 ~~preload.ts~~ **`preload.js`**
  （**09-23 改**：实查 `package.json` 无 TypeScript、项目全 `.js`。
  week-01 第 50 行排的 TS 从未落地，已在 `docs/frontend-prereq.md` 6.2 标 W1-W6 作废）
- 用 contextBridge.exposeInMainWorld 暴露一个测试 API

**记录 15 分钟**

### 周三（1.5 小时）

**C++ 30 分钟**：
- `std::variant`：类型安全的联合体
- `std::visit`：访问 variant 的当前值
- 写代码：一个 `Result<T>` 类型，用 variant<T, Error> 实现

**Electron 45 分钟**：
- 侧读 Chatbox 或类似项目的 preload.ts
- 理解：主进程 API 如何安全暴露给渲染进程
- 记录 3 个你觉得设计好的地方

**记录 15 分钟**

### 周四（1.5 小时）

> # 🚫 **2026-10-01（周四）= 国庆假期第一天，停训。以下内容顺延 10-08（周四）**

**C++ 30 分钟**：
- 结构化绑定：`auto [key, value] = ...`
- 场景：遍历 map、返回多值
- 写代码：一个函数返回多个值（用 tuple + 结构化绑定接收）

**Electron 45 分钟**：
- side project：实现"新建对话"和"切换对话"的 UI
- ~~状态管理：暂时用 useReducer，不引入 Redux~~
  **🔴 09-23 改为 `useState`**：`docs/frontend-prereq.md` 实测本人 React 零基础，
  `useState` 本身排在 W3D5（09-25）才第一次学。`useReducer` 比 useState 更抽象
  （要同时理解 reducer 函数 + action 对象 + dispatch 三个新概念），
  在他刚学会 useState 一周内排它是叠加两层未知。
  **useReducer 顺延至 W6，不作废**；本日用 `useState` 数组 + 一个 `currentId` 即可。

**记录 15 分钟**

### 周五（1.5 小时）

> # 🚫 **2026-10-02（周五）= 国庆假期，停训。以下内容顺延 10-10（周六，调休上班日）**
> ⚠️ 10-10 虽是周六但为**法定调休上班日**，按**工作日 1.5h** 排，不按周六 4h 深度档。

**C++ 30 分钟**：
- `if constexpr`：编译期条件分支
- 写代码：模板函数根据 T 是不是 pointer 走不同分支

**Electron 45 分钟**：
- Electron 持久化方案调研：electron-store vs SQLite vs 文件
- 选定用哪个（推荐 electron-store 简单快速）
- 实现对话记录持久化（存到本地磁盘）

**记录 15 分钟**

### 周六（4 小时深度）

> # 🚫 **2026-10-03（周六）= 国庆假期，停训。以下 4h 深度档顺延 10-17（周六，W6）**
> ⚠️ **注意下半段的简历 v0 是抗风险项**，顺延两周有实际风险，见本文件顶部说明。

**上午 2 小时：C++17 综合练习**
- 场景：写一个简易 JSON parser（只支持字符串、数字、bool、null、对象、数组）
- 用 variant 表达 JSON value
- 用 optional 表达 parse 结果
- 只需 200 行左右，能 parse `{"name": "test", "age": 20, "active": true}` 就行

**下午 2 小时：简历"保底版"起草**
- 打开一个新文档 `plan/resume/v0-emergency.md`
- 用 STAR 法则整理过去 2 年 Chromium 部门工作：
  - 3-5 条工作项，每条包含：背景、任务、行动、结果
  - 突出：涉及的技术模块、bug 修复案例、性能改进（如有）、协作规模
- 关键：**不吹嘘，但要把已做的价值讲够**
- 目标：如果第 5 周被裁，这份简历能立刻投

### 周日（2 小时复盘）

> # 🚫 **2026-10-04（周日）= 国庆假期，停训。以下顺延 10-11（周日），与 W5 复盘合并**

**1 小时：周日复盘 + C++17 小测**
- 闭卷 20 分钟：写一段代码用到 optional、variant、结构化绑定
- 记录本周投入

**1 小时：简历 v0 review**
- 自己重读简历，删掉所有含糊表述
- 找 1 位朋友/前同事帮 review（可以匿名请人看）

## 本周门禁

- [ ] 简易 JSON parser 能跑通 3 个测试样例
- [ ] `Result<T>` 类型能用（用 variant 实现的）
- [ ] Electron side project：Context Isolation 打开 + preload 暴露 API + 对话持久化
- [ ] 简历 v0 完成初稿（1500 字左右）
- [ ] 5 天日记 + 1 份周日复盘
- [ ] 🆕 **q-framework 第二层四问闭卷可答**（WebView 创建链路 / 抽象基类为何存在 /
      双后端能抽成同一接口说明什么 / 哪些地方抽不动要开后门）
- [ ] 🆕 **CEF / WebView2 / Electron 三方进程模型对照表**（本人自画）

## 卡壳降级

- JSON parser 卡住：只做数字 + 字符串两种类型的 parse
- 简历不知怎么写：先列 20 条"做过的事"，第 5 周再整理
- optional/variant 混乱：只精掌握 optional，variant 延后

## 参考

- 《C++17 The Complete Guide》相关章节
- Electron Security 官方文档
- 简历模板：https://cv.smart-ai.club/ 或 latexresu.me

## 里程碑

**第 4 周结束时你应该有**：
- 3 篇 C++17 小实验代码（optional、variant、结构化绑定）
- 1 个可编译运行的简易 JSON parser
- 1 个能对话（假）+ 持久化的 Electron 记事本
- 1 份可以立刻应急投递的简历（v0）
