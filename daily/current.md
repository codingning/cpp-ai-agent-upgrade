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

只读末尾「**The Content Layer's Services**」那一节（不用读前面的 Mojo 教程）。
那节按进程类型逐个介绍：browser / renderer / **gpu** / **utility** / plugin。

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
