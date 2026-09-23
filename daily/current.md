# 今日任务 · 2026-09-23（周三）· W3D3 · 1.5h 保底

> 昨天 205 分钟，全天第三次在实验上推翻我（grep 口径、createElement 无分辨力、base/CORS）。
> C++ **L2 已达成**。但 Electron 三层链**复测没过**，维持 L1+——
> **今天第一件事是把昨天丢掉的那条捡回来，不是往前冲新内容。**

---

## 元规则（第 9 次要求，09-20~09-22 连续三天做到，保持）

动手前先写一句：**「我认为 X 由 ___ 决定」**。
写不出来说明该查文档，不是该跑实验 —— 不罚，直接去查。
实验结果推翻预测时，**回头把结论行改掉**。

**昨天新增一条判据（你自己衍生出来的，写进今天）**：
实验分辨力不只问「两种假设会不会产生同样结果」，还要问
**「我这条命令/探针测的到底是什么量」**（grep -c 数行数 vs grep -o|wc -l 数次数）。

---

## 上午 10:30-11:10（40min）· C++

### A. 🔴 map vs unordered_map（15min，周二顺延项，不作废）

- `std::map` = 红黑树，`std::unordered_map` = 哈希表
- 查询复杂度 O(log n) vs 平均 O(1)
- **重点不是背复杂度**，是回答：什么场景下你会**故意选更慢的 map**？

### B. 🔴 迭代器失效规则（15min，本日原排）

闭卷先写你的猜测，再查文档核：

1. `vector::push_back` 什么时候让迭代器失效？为什么是「可能」不是「一定」？
2. `vector::insert` 失效哪些？
3. `map`/`set` 的 `insert`/`erase` 失效哪些？
4. `unordered_map` 触发 rehash 时失效哪些？

> **它是什么（非当日主角，先标一行）**：
> **rehash** = 哈希表元素变多、装载因子超阈值时重建更大的桶数组并把所有元素重新分桶。
> **迭代器失效** = 迭代器指向的内存位置不再对应原来那个元素（可能被搬走、可能被释放），
> 继续解引用是 UB。

**和你昨天做的 placement new 是同一条线**：vector 扩容时元素被搬到新内存，
旧迭代器还指着旧那块 —— 你昨天亲手写过那个搬运循环，这道题你应该能自己推出来。

---

## 下午 17:00-17:50（50min）

### A. 🔴 Electron 三层链重考（15min）· 复测未通过项

昨天第 1 问答错，第 2 问不完整。**闭卷，不许翻昨天记录。**

> **问 1**：沙箱掉了（contextIsolation、contextBridge 都还在），
> 攻击者拿到的**具体是哪个进程**的权限？他能不能直接让主进程替他干活？为什么？
>
> **问 2**：contextIsolation 掉了，除了「拿到 preload 的权限」，
> 还有一条**主动攻击**路径 —— 它靠的是两边共享了什么东西？

两问都答对才算这条结账。昨天你 09-20 是答对过的，今天是测「隔三天还在不在」。

### B. 🟡 构建时 vs 运行时的分界（15min）· 昨天 Q5 理由不成立

昨天 Q5 你结论对（「用了 React 就不用 Vite」是错的），但理由答成「React 只是一个库」。
今天用**这条线**重答：

> JSX 是在**哪个时刻**消失的？React 这个库在运行的时候，手里拿到的是 JSX 还是别的东西？
> 它有没有机会看到过 JSX？

答完再回答昨天答不出的 Q4：**`vite build` 的产物怎么进 Electron？**
（我昨天直接讲了，那一版标的是「教练所给，未验证」——今天要你自己说一遍。）

### C. 🔴 loadFile 白屏实跑（20min）· 昨天遗留未决，必须真跑

这是昨天挂着的**唯一未结账实验**，我明确说过「不能证明、这是推测」。

> 把昨天那个 `F:\code\vite_react\vite-project\dist` 用 Electron 的 `loadFile` 加载，
> 看**会不会白屏**、控制台报什么。两版都测（有 base / 无 base）。

> **它是什么**：`loadFile` 是 `BrowserWindow.webContents` 的方法，
> 参数给本地文件路径，Electron 内部用 `file://` 协议加载它。
> 昨天你实测双击打开时 `file://` + `type="module"` 被 CORS 拦死 ——
> 问题就是：**Electron 对自己的 `file://` 有没有开后门。**

**先写预测再跑**：我认为 Electron 里会 / 不会白屏，因为 ___。
跑完不管结果是什么，都是结账 —— 这条挂了一整天了。

---

## 不做（写明，不是切掉）

- **q-framework D1（IOCP 异步 IPC）**：09-21 排、09-22 顺延，**今天继续顺延**。
  理由不是没时间，是 09-22 已把 q-framework 正式排到 **W4D1（09-28）起**，
  有了完整四层深挖链，不再临时塞散活。**不作废，已在 `plan/weekly/week-04.md` 落地。**
- **Utility vs Renderer**：连续第四次落地。出处仍未实读确认，**我不布置**。
  这条归我 —— 我欠你一次文档实读（`process_model_and_site_isolation.md` / `sandbox.md`），
  本周内给出处，否则这条算我的账不算你的。
- **Chat UI 组件拆分（React）**：依赖前端前置断层，`docs/frontend-prereq.md` 的
  「你实际会」列还全空。**先填表再动手**，顺延不作废。
- **扩展项**（有余力才上，做了必须写进记录）：
  ①元素级计数 vs 类级打印为何后者无分辨力
  ②`push_back` 用 swap 改造
  ③手动 try/catch 回滚 vs RAII 守卫（昨天新挂）

---

## 🔴 欠我的一件事（09-22 排了没回，今天第一句话回我）

**✅ 09-23 14:4x 已完成。** 本人填完 28 项，教练当场写完结论区 6.1/6.2/6.3
并按本人指令「现在就改，不要晚上」改完 W3/W4 六处 + debt-map 新增整节。

**填表结果（这是今天最大的发现，比上午段的 C++ 重要）**：
原排课前提「他会 JS，缺的是 React」**被推翻**——JS 四项语法（箭头函数/解构/展开/async-await）
本人自评**全「不会」**。关键证据是本人自己点破的：
「Electron 主进程是我从教程里拷贝的，所以并不是全部了解」→ **用过 ≠ 会写。**

→ W3 剩余三天改为：**周四 npm 工具链 + 组件/props ｜ 周五 useState ｜ 周六 补齐 + useEffect**。
JS 语法不单独开课，寄生在 React 练习里（`const [a, setA] = useState()` 一行同时是
useState 用法 + 数组解构，互为记忆锚点）。

---

## ✅ 上午段已结账（09-23 10:30-11:1x + 14:1x-14:4x 补讲）

**迭代器失效四题**：Q1 ✅ 独立答对（扩容→全失效 / 不扩容→只 end 失效，自己从昨天
placement new 搬运循环推出来的）｜ Q2 ⚠️ 漏扩容分支（第 1 题答对的规则第 2 题只用了一半）
｜ Q3 ❌ 错（答「全部失效」，实为 map/set 节点式：insert 不失效任何、erase 只失效被删的）
｜ Q4 ⚠️ 结论对理由缺（rehash **废迭代器、不废指针和引用**）

**教练实跑探针**：`%LOCALAPPDATA%\Temp\iter_probe.cpp`（MSVC /std:c++17）
- map：`find(2)` 地址 `...80C40`，插 100 个 + `erase(4)` 后地址不变、值仍 20、`++it` 正常
- unordered_map：`bucket_count 8 → 512`（真 rehash），但 key=2 地址不变，旧地址仍读出 20
- vector：`cap 4 → 6`（MSVC 是 1.5 倍不是 2 倍），`v[2]` 地址 `...A898 → ...A9D8` 变了
- `reserve(10)` 不扩容那版：地址不变 ✅

**map vs unordered_map 五条判据**（本人问「不知道什么场景故意选更慢的 map」，教练讲）：
①有序（遍历有序 + `lower_bound`/`upper_bound` 动态范围查询）②迭代器稳定
③最坏复杂度有保证（哈希碰撞可被恶意构造 = **HashDoS**）④key 只要 `operator<`
⑤不需预估规模（unordered_map 要 reserve）

**key 要求实测**（`%LOCALAPPDATA%\Temp\key_probe.cpp`）：
- `std::map<K,V>` 要 K 有 `operator<`（默认 `std::less<K>`）
- `std::unordered_map<K,V>` 要**两样**：`std::hash<K>` 有特化 + `K` 支持 `operator==`
- **enum class 两边都能用**（C++14 起标准要求 enum 有 `std::hash` 特化，实测 hash 值 12478008331234465636）
- **自定义类只有 map 现成能用**：`unordered_map<自定义struct>` 实测 `xhash(118) error C2064`

**q-framework 实证坐标（教练实查，非举例）**：`std::map` 1473 处、`std::unordered_map` 638 处（排除 base/）
- `components/pref/pref_service.h:125` `std::map<std::string, std::vector<Observer*>>` ——
  本人**实读代码后答对**：`NotifyPrefChange`（494-499 行）循环体里只调 `o->OnPrefChanged(key)`，没改 map ✅
- `ui/dui/Control/UIMenu.cpp:1417` `std::map<CDuiString, bool>` —— CDuiString 是 DuiLib 自有类，
  `std::hash` 不认识它，**这才是「选 map 是成本考量不是性能考量」的真实证据**

**遗留给本人的一问（不限今天）**：`OnPrefChanged` 是虚函数，若某个 Observer 在
`OnPrefChanged` 里调了 `RemoveObserver`，会发生什么？（第 2 条「迭代器稳定」真正咬人的形态）

---

## 📌 教练今天出错 2 次（记录在案，不遮）

1. 要本人「自己把『有序』拆成遍历有序 vs 动态范围查询」——他根本不知道 `lower_bound`
   是什么，**这不该他想，该教练先给定义**。已撤回该要求。
2. 断言「enum class 进 unordered_map 其中一个编译不过」——**没跑就说，实测两边都过**。
   **同类老毛病：未验证的断言直接出口。**

本人对上午段的评价「今天的 C++ 没有什么知识，只回答了一些我已知的东西」——
**教练接受排课失误那一半**（迭代器失效是查文档即得的记忆型内容，不该占满 40min），
**驳回另一半**（Q3/Q4 实际答错，不难 ≠ 已知）。

---

## 收工前（15min 记录）

`daily/history/2026-09-23.md`，五栏照旧：完成 / 掌握（闭卷自答）/ 未掌握卡壳 / 证据 / 明日计划。

昨天那份记录质量很高（尤其第十节把我的错和实测输出并排放）。保持这个写法。
