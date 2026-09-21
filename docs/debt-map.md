# W1-W2 欠账清单
## 说明
### 本文件是教练批改产出，非宁鑫洋自己的知识索引
- 清掉一条就从这里删掉，搬进 cpp-concept-map.md
- 更新日：2026-09-20
## 🔴 方法论（最高优先级，比任何知识点都重要）
### 动手前先写「我认为 X 由 ___ 决定」
- 09-20 起替代原「运行前先写预测」（原版 6 次未执行）
- 改版理由（本人 09-20 提出）：不是不会设计实验，是知识不足以判断
  「这个实验能不能验证我的要求」。写不出这句 = 该查文档，不是该跑实验，不罚
- ✅ 09-20 首次执行：day7_debt_clear.cpp 第 2 行写了预测，且实验推翻预测后回头改了第 3 行
### 实验要有分辨力
- 09-18 连犯两次，09-19 再犯一次
- 判据：如果两种假设都能产生你看到的结果，这个实验就是白做
- ✅ 09-20 本人自行绕过一次：发现 static_assert 对「=default 是否抑制移动」无分辨力
  （两侧都为真，因 const& 能绑右值），改用带打印的实例化才分开
### 不许拖延可即时完成的小项（教练 09-20 被本人当面指出）
- 教练对一个 3 分钟的实验说「挂到 W3」，与 Vector<T> 拖两周同一个动作
- 规矩：能当场做完的不许排进下周
- ✅ 09-21 本人再次执行此规矩：提出 MyVector 三刀合并为一天做完，教练核对后采纳
### 排计划前必须核 debt-map / history，不许照过期文件和记忆说话（09-21 教练第 5 次犯）
- 09-21 教练依 `week-03.md` 第 138 行过期条目断言「noexcept→扩容退化实验尚未做」，
  实际 09-20 day7 实验4 已完成并写在本文件第 57 行；同时主张「Rule of 5 要隔一天写」，
  但 09-20 day7 已把整张表逐条实验过，间隔检索价值已用掉
- 两处均由本人当场指出。连带发现 `week-03.md`「W2 遗留欠账」6 条里 4 条早已清却一直挂着
- 规矩：**本文件是欠账唯一权威源**。计划文件与本文件冲突时以本文件为准，并当场改计划文件
## C++ 概念欠账
### 🎉 C++ 侧已全部清空（2026-09-20，零 ❓）
- 知识图 `cpp-concept-map.md` 上 5 个 ❓ 全部拿到自有实验证据，无待补项
## Electron / Chromium 欠账
### ~~A4 sandbox → contextIsolation → preload 三层链~~ ✅ 09-20 结账
- 本人自核 Electron 官方 `tutorial/sandbox` + `tutorial/context-isolation` + `tutorial/security` 后重答通过
- 三层递进（不开这层攻击者能多拿到什么）：
  1. 沙箱掉 → 拿到渲染进程那个 OS 进程的全部权限（沙箱内只能自由用 CPU 和内存，其余靠 IPC 委托）
  2. 沙箱在、contextIsolation 掉 → 拿不到 OS，但拿到 **preload 那一层的权限**；
     且两者共享同一个 window，攻击者可改 `Array.prototype.push` 等内置方法，**等高权限代码来调用他**
  3. 两层都在、contextBridge 写错 → 仍漏。官方反例 `exposeInMainWorld('myAPI',{send: ipcRenderer.send})`
     等于让任意网站发任意 IPC；正确做法是一个 IPC 消息包一个方法
- **Q11/Q12 矛盾解法**：两句都对，不矛盾。开关是独立的（nodeIntegration 不影响 contextIsolation），
  但防护是**串联**的——第一层塌了后两层拦不住从第一层进来的人。
  官方原话：关 Node 集成可防止 XSS 升级成 RCE；开着时页面脚本直接有 `require('child_process')`，
  攻击者根本不需要偷 preload 的 API
### Utility 和 Renderer 的区别
- 09-19 记录里空缺，09-20 块 2 题 7 仍空——连续两次落地
- ⚠️ 教练 09-19 曾在此翻车（给了一篇不含答案的 mojo_and_services.md）
- 已确认覆盖的一句（Electron tutorial/sandbox）：除主进程外多数进程都在沙箱内，
  包括 renderer，也包括 utility（audio/GPU/network service 属此类）
  —— 这句能说明 Utility 装什么，回答不了「区别是什么」
- 状态：❌ 出处待教练实读 process_model_and_site_isolation.md / sandbox.md 后确认
## 产出欠账
### 博客第 1 篇正文
- 大纲 09-19 建、09-20 改到及格；正文计划第 6 周发布
- 状态：⚠️ 大纲完成，正文未开始
### W1 周复盘三处空白
- 2026-09-13-weekly.md 第 13-14 行（达成率/缺口原因）、第 191 行（下周调整整节）
- 状态：❌ 仍空
## 已清（保留 7 天作为对照，之后删）
### ✅ 左值/右值值类别（09-20 day7_value_category.cpp：五条重载探针实测，有名字的右值引用是左值，预测命中）
### ✅ 析构 protected 的「为什么」（**本条系教练误标**：09-17 history 第 55-57 行本人已答对，
  09-18 debt-map 未核原始记录照抄为「未补」，09-20 本人指出后销账。教练第 4 次「不核来源照记忆排」）
### ✅ `= default` vs 什么都不写（09-20 day7 实验1：D1 走拷贝 / D2 走移动，证明 =default 算用户声明）
### ✅ 拷贝赋值是否随拷贝构造一起 delete（09-20 day7 实验2：D10 成员逼出真实调用链，未跟着死）
### ✅ move 退化三条的最小例子（09-20 day7 实验3：D5 const / D6 无移动构造）
### ✅ noexcept → vector 扩容退化（09-20 day7 实验4：D7 走拷贝 / D8 走移动，本人自有实验证据）
### ✅ 移动构造反向抑制拷贝（09-20 day7 test3 #ifdef 对照：exit 0 vs exit 2，两条 C2280 + 编译器 note）
### ✅ Chromium 进程模型图（09-19 drawio，09-20 cell48/49 重填）
### ✅ Chat UI v0（09-19 index.html）
### ✅ 博客大纲 + blog-drafts/（09-19 建，09-20 改到及格）
### ✅ W2 周复盘 + 口头复述自评栏（09-20 完成，九题自答）
### ✅ Rule of 0/3/5 索引缺失（09-17 闭卷重答通过）
### ✅ 异常路径 RAII（day4_exception_raii.cpp）
### ✅ MyUniquePtr 单元测试（day4_uniqueptr_test.cpp）
### ✅ move-from 状态 + SSO 原因
### ✅ preload + contextIsolation（基础层，A4 整链仍欠）
### ✅ 语境转换（09-18 讲解 + 自己画进图里）
### ✅ Menu 接线 + 菜单份数（09-18 实验验证）
