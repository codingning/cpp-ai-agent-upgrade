# 今日任务 · 2026-09-19（周六）· W2 周六 · ToDesk 远程日

> ToDesk 已于 09-18 本人实测确认可用。按 **90min 保守排**，不按原计划 4h。
>
> **09-18 教练排错更正**：原写「画出 Browser/Renderer/GPU/Utility 四类进程」，
> 但你 09-15 读的那篇多进程架构文档**只详细讲了 Browser 和 Renderer**，
> GPU/Utility 只在末节一句话带过（你的记录第 65 行已注明「其余两个排到周六配专门资料」）。
> 我没给资料就让你画四个，等于逼你编。**今天先给资料，读完再画。**

---

## 开场 5 分钟 · 清尾

- [x] ~~`F:\code\ai-desktop-assistant` push 失败排查~~ —— **09-18 23:00 教练已实测：没失败**。
      `git ls-remote origin master` 返回 `240b09a`，和本地 master 一致，两个 commit 早就在远端了。
      昨天那两次超时是连接收尾卡住，不是凭据问题。**这项取消，但留一个提问**：
      「命令超时」这个现象，既可能是没推上去，也可能是推上去了没收尾——
      你昨天直接判了「失败」。**想一下：要区分这两种情况，最少需要跑哪一条命令？**
      （这是你昨天第三次踩「实验没有分辨力」，前两次是 require 位置和菜单份数）
- [ ] 概念图两处收尾：
  - `= delete` 只写了「禁止重载被选中」（你自己挖的那半），漏了主用途「禁用拷贝构造做 NonCopyable」
  - `= default` 的说明仍是 09-17 答错的那句，改标 ❓

---

## 主任务（70min）· Chromium 进程模型

### 第一步：读 GPU / Utility 的专门资料（25min）

**资料**：https://chromium.googlesource.com/chromium/src/+/HEAD/docs/mojo_and_services.md

⚠️ **09-19 14:10 教练实抓页面更正**：这篇文档已被上游改写。
末尾现在叫「Content-Layer Services Overview」，**只剩 Interface Brokers 和
Navigation-Associated Interfaces 两小节，没有按进程类型逐个介绍的内容**，
「exists only nominally」那句话在当前版本里也**不存在**了。我给的读法是照旧版写的，作废。

**改读这两节**（都在同一篇里，实抓确认存在）：
- 「Example: Building a Simple Out-of-Process Service」——整节，尤其
  `Hooking Up the Service Implementation` 里那个注册位置的**文件路径**，
  和它旁边已有的 `RunFilePatcher` / `RunUnzipper`。看懂这个就回答得出 Utility 装什么。
- 「Specifying a sandbox」——一段话，注意 `kService` 那句的**例外条件**。

**09-19 14:30 二次更正**：这篇文档里**确实没有 GPU 进程内容，也没有 Utility vs Renderer 的对比**。
本人读完反馈属实，是教练选错资料，不是他没读到。三个问题里只有第 2 问这篇能答。
GPU 与 Utility/Renderer 区别另配资料（见下方「补充资料」）。

**补充资料**（教练 09-19 实抓确认可访问）：
- Network Service 跑哪儿：https://chromium.googlesource.com/chromium/src/+/HEAD/services/network/README.md
  看「Where does the network service run?」一节（两段，直接给答案）
- 沙箱原则：https://chromium.googlesource.com/chromium/src/+/HEAD/docs/design/sandbox.md
  只看「Design principles」五条 + 「Sandbox Windows architecture」开头那句
  「Sandbox operates at process-level granularity」——这句直接击穿他「因为要沙箱所以单开进程」的因果倒置

读的时候只带着三个问题：

1. **GPU 进程**：为什么显卡相关的活要单独开一个进程？（提示：驱动崩溃会怎样）
2. **Utility 进程**：文档里说它「exists only nominally」，是用来 bootstrap 别的服务的。
   那 Network Service 跑在哪儿？（文档里有）
3. Utility 和 Renderer 都是被 Browser 创建的沙箱进程，**它们的区别是什么**？

**动手前先猜**（元规则第六次，这次必须写）：
- 我猜 GPU 进程独立出来是因为 ___
- 我猜 Utility 进程装的是 ___

### 第二步：画图（45min）

画出四类进程 + 通信路径，存 `docs/chromium-process-model.drawio`。

**工具**：draw.io（VSCode 装 "Draw.io Integration" 插件）。这图有跨进程箭头，markmap 画不了。
`.drawio` 是 XML，能进 git，教练能读。

**图上必须有**：
1. 四个进程框：Browser / Renderer / GPU / Utility，各自一句话职责
2. 通信箭头：谁跟谁通、走什么机制（提示：Mojo IPC）
3. **沙箱标注**：哪些进程在沙箱里？（你 09-17 读过 sandbox.md，接得上）
4. **Electron 对应层**：main process 对应哪个？renderer 对应哪个？
   `ipcMain`/`ipcRenderer` 对应 Chromium 的什么？
   ⚠️ 你 09-15 答过 RenderProcessHost / RenderProcess 的对应关系，**那次答反了**，这次画对

---

## 09-19 13:50 补排（本人自查发现漏项，教练确认）

> 上面这份 90min 排法**漏了 week-02.md 周六原定的三个 🔴 补课项中的两个**。
> 原文 129-145 行：1. B2 Chat UI v0 / 2. B3 进程模型图 / 3. B4 博客大纲。
> 我只排了 B3（升级成四进程 drawio），B2 和 B4 被我漏掉——而这两项都在
> 「本周门禁」清单里（week-02.md 190、192 行），不是可选项。
> 这是教练第二次犯「把新排内容当成替代原计划」的错。以下按门禁补回，不删上面任何内容。

### 补 B2 · Chat UI v0（40min，欠 5 天）

- `F:\code\ai-desktop-assistant` 的 index.html 改成 Chat UI 静态骨架
- 纯 HTML/CSS，不要 React、不要接任何模型：消息列表区 + 输入框 + 发送按钮
- 只要静态能看，不要求能发消息
- commit

### 补 B4 · 博客大纲（30min 封顶，欠 6 天）

- 建 `blog-drafts/` 目录（当前不存在）
- 第 1 篇：标题 + 大纲，《我为什么写一个 Electron AI 助手 · 序章》
- **只写大纲不写正文**，正文留到第 6 周。到 30min 无论写到哪里都停

### 今天的实际顺序（13:50 起）

1. 开场清尾 5min（概念图两处 + push 那个分辨力问题）
2. 主任务 Chromium 进程模型 70min（读 25 + 画图 45）
3. B2 Chat UI 40min
4. B4 博客大纲 30min 封顶

合计约 2.5h。**保底是前两项**（做完就算今天没崩）；3、4 是门禁欠账，做掉本周门禁才干净。

---

## 09-19 收尾遗留（明天周复盘一起处理）

### B4 博客大纲三处未改（教练 16:07 指出，本人当日未改）

`blog-drafts/01-why-electron-ai-assistant.md` 已建，三节标题齐，但只是标题+单句，不是可写作的大纲：

1. 第一节标题「什么是 Electron」与内容（选它的理由）不符 → 改成「为什么是 Electron」
2. 三节都缺子条目，每节至少补 2-3 条正文要讲的具体事。第一节可挂：
   - 做 Chromium C++ 两年日常碰什么活（举一件具体的）
   - 为什么不继续深挖 C++ 而往 Electron 走
   - 两者关系（09-19 刚画完进程模型图，现在答得出）
3. 「在 future 中保持竞争力」的 future 改成中文「未来」
4. 第三节只有「因为焦虑」——焦虑是情绪不是理由，往下追一层：怕被替代，还是怕两年后简历还是这几行

### 进程模型图两处 ❓ 未填（教练故意留空，不代填）

`docs/chromium-process-model.drawio` cell 48/49：
RenderProcessHost / RenderProcess 各自对应 Electron 的什么。
教练已确认**不是** ipcMain/ipcRenderer（那两个对应的是 Mojo 消息管道，见图中黄框）。
提示：想清楚「一个 BrowserWindow 在主进程这边是什么对象」。

### 09-19 教练自身错误记录（共 4 次，供周复盘核对计划可靠性）

1. 14:10 给的 mojo_and_services.md 读法照旧版写，文档已被上游改写
2. 14:30 该文档根本不含 GPU 与 Utility/Renderer 对比，出题超出资料范围（本人读完指出）
3. 15:17 曾说「Renderer 不直接跟 GPU 说话」——错，官方 debugging_gpu_related_code.md 原文说 GL 调用直接发往 GPU 进程
4. 15:40 要求删 overflow-y:auto 做对照实验，但 week-01~06 从未训练过 CSS 布局（本人指出，B2 据此降级）

---

## 有余力才做（不占上面时间）

二选一：

**A. `= default` vs 什么都不写**（欠了两天）
查：`= default` 算不算「用户声明」？算了以后连带影响什么？用自己的话写一句。

**B. 自写 noexcept → vector 扩容对照实验**
教练 09-18 写过一个，**不许照抄**。自己设计：两个类只差一个 `noexcept`，
用 vector 触发扩容看走哪条路。写之前先在注释里写「我预测输出是 ___，如果不是说明我哪里想错了」。

---

## 明天（09-20 周日）· W2 周复盘 · 量已调小

> **09-18 更正**：今天做的 `docs/cpp-concept-map.md` + `docs/debt-map.md`
> 已经覆盖了周复盘的「知识梳理」和「欠账盘点」两块，**周日不用重做**。

周日只补这四块（约 1h，不是 2h）：

1. **本周投入统计** —— 核对 `daily/progress.jsonl` 五天数据是否真实（这是 09-18 原定项，没做）
2. **口头复述自评** —— 本周每个知识点标注「自己想明白的」还是「抄教练的」。
   ⚠️ 这一栏 09-18 完全没有，而它是最防自欺的一栏。W1 周复盘有这栏，照着做
3. **W2 门禁逐条验收** —— 对 `plan/weekly/week-02.md` 末尾逐条判定，过/不过，不许写「差不多」
   （已知 A1 ✅、B1 ✅，其余自己判）
4. **下周调整** —— 至少回答：W3 主题是 STL 容器，本周暴露的盲区怎么带进去？

存 `daily/history/2026-09-20-weekly.md`。

**另**：W1 周复盘（`2026-09-13-weekly.md`）里第 13-14 行「达成率/缺口原因」、
第 191 行「下周调整」整节还空着，顺手补完。
