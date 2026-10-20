# 2026-10-20（周二）· W7D2 · 工作日 1.5h 口径

> 日期用 `date` 实算。周次硬公式：`(10-20 − 09-07).days = 43` → `43//7+1 = W7`、`43%7+1 = D2`。
> **昨天（W7D1）上午 108%、下午 0%** —— 下午整格零产出，`B5` 一问没答。今天先把那格补上，
> 补法写在第二节，**不是砍，是占周二 q-fw 的格**（q-fw 第三层① 的去向在同一节写明）。

---

## 〇、开局三样必交（10min，昨天欠的，先交再开新内容）

全部在 `F:\code\cpp-practice\week-07\day1_thread.cpp`，都是**你自己的话**，我一个字不填。

### ① Q1 —— 四个 case 各一行，写明「崩 / 不崩 + 死在哪」

```
Q1-JOIN            ____
Q1-DETACH_NOSLEEP  ____
Q1-DETACH_SLEEP    ____
Q1-NEITHER         ____
```

**要写清的是「死在哪一行或哪个位置」**，不是「线程没 join」这种通用结论。
数据你已经有了，在 `F:\code\cpp-practice\build\cases-day1_thread.log`（15:16 那份，10 次/例）：

| case | 非零次数 |
|---|---|
| `CASE_JOIN` | 0 / 10 |
| `CASE_DETACH_NOSLEEP` | **6 / 10** |
| `CASE_DETACH_SLEEP` | 0 / 10 |
| `CASE_NEITHER` | **10 / 10** |

**判据**：`DETACH_NOSLEEP` 崩 6 次不崩 4 次 —— 你要在那一行写出**为什么它是不确定的**，
而 `NEITHER` 是 10/10 确定崩。两个都是崩，机制不一样。

### ② Q3 —— 补两句机制，不是重写整段

你昨天答的是「改成 `endl` 后 `-----` 也输出了」——**这是现象，不是原因**。补这两句：

```
a) endl 比 "\n" 多做了什么？ ____
b) std::terminate 走的是哪条退出路径？那条路径对 stdout 缓冲区做了什么？____
```

**它是什么**（非主角概念，各一行，直接给你）：
- **`"\n"`**：只是一个换行字符，写进 `cout` 的**用户态缓冲区**就完事了，什么时候真写到控制台由缓冲区自己决定。
- **`std::endl`**：换行字符 + **强制 flush**（把用户态缓冲区里的内容立刻推给操作系统）。
- **`std::terminate()`** 默认调 `abort()`。`abort()` 是 CRT 的**异常终止**路径，它**不做**正常退出该做的事
  —— 不刷新 `stdout` 缓冲区、不跑静态对象析构。所以缓冲区里还没推出去的内容，**跟着进程一起被丢掉**。
  （对照：`return 0` 走的是正常退出路径，CRT 会把缓冲区刷干净。）

**这条要你自己用实验确认**，不要信我这段：把 `test3` 里那个 `cout` 后面分别用 `"\n"` 和 `endl`，
各跑 `cases.bat` 一次，看 `-----` 那一行在不在。**两条命令贴 log。**

### ③ 源码提交

`git status` 现在是 `M cases.bat` / `M week-07/day1_thread.cpp`。填完 ① ② 我给你补跑一遍
（跑你 main 里没覆盖的情况，这是 10-17 起的固定动作），过了就提交。

---

## 一、10:30-11:10 · 40min · C++

### 1.1 R1 四类挂点索引（10min · 昨天顺延项，不改去向）

昨天你答对了方向：「对象生命周期结束时插入析构调用」。但「生命周期结束」在代码里对应**四个具体位置**，
要能各自指出来才算掌握。**闭卷答下面四问，每问写一行 + 一个你自己想的例子：**

```
R1-a 局部变量：在哪个符号处析构？____
R1-b 临时量（例如 make() 的返回值）：死在哪个时刻？____
R1-c 堆对象（new 出来的）：谁触发析构？编译器管不管？____
R1-d 异常抛出时，栈已经在作用域里的对象怎么办？____
```

**它是什么**（你只需要知道这四个名字对应哪四行代码，机制要自己说）：
- 临时量：像 `f()` 返回一个对象、但你没有用变量接住它，那个对象就活到**它所在的那条语句的分号**。
- 异常栈展开（stack unwinding）：`throw` 之后，控制流沿调用栈往回退，**每一层退出的作用域里的对象都会被析构**，然后才进 `catch`。

⚠️ 这题**不许写「函数退出路径」**。昨天就栽在把它挂在函数出口上。

### 1.2 `std::thread` 传参：为什么要 `std::ref`（25min · 今天主角）

**先把知识点讲清（09-28 铁律，这段是给的，不用你猜）：**

`std::thread t(f, a, b)` 构造时，**参数不是直接传给 `f` 的，是先被拷贝/移动存进线程对象内部，
再由线程在启动时取出、以右值形式交给 `f`**。这是「**decay-copy**」：
数组退化成指针、函数退化成函数指针、`const` 被剥掉，**引用本身不保留**。

**后果**：`f` 的形参是 `int&`，你传一个 `int` 变量进去，编译期就过不去 —— 线程内部存的是一个 `int` 副本
（右值），右值绑不到 `int&`。`std::ref(x)` 就是造一个 `reference_wrapper`，
它能被拷贝、又能隐式转回 `int&`，这样「引用」才能穿过那一层拷贝活下来。

**这一段我实跑验证过（`F:\code\cpp-practice\build.bat`，MSVC x64，2026-10-19 23:xx）：**

| 写法 | 结果 |
|---|---|
| `void addOne(int& n);` + `std::thread t(addOne, std::ref(a)); t.join();` | `CL_EXIT=0`，`RUN_EXIT=0`，输出 `with ref    a=1` |
| 同上，去掉 `std::ref` 写 `std::thread t(addOne, a);` | `CL_EXIT` 非 0，**`error C2672: "std::invoke": 未找到匹配的重载函数`**，模板实参 `_Ty1=int`（不是 `int&`） |

第二行那个「`_Ty1=int`（不是 `int&`）」就是 decay 的直接证据 —— **编译器告诉了你它把引用丢了。**

**你要做的实验（`week-07\day2_thread_args.cpp`）**：
```
实验 A：形参 int& ，用 std::ref 传，join 后打印原变量 → 记下值
实验 B：形参 int& ，不用 std::ref → 记下编译错误号（要贴原文那一行，不要只写「报错了」）
实验 C：形参写成 by value（int），不用 std::ref → 能编译，但打印原变量看它变没变
实验 D：形参 by value 但用 std::ref 传 → 先写预测：编译过不过？跑出来原变量变不变？
```
**A/B/C 用 `cases.bat` 跑**（一条命令四 case 全出来）；**D 先写预测再跑**，
这是你已经会的东西（Q2 那个反事实判据就是这么来的），不是新知识点，所以由你自己猜。

⚠️ **实验 B 用 `cases.bat` 会看到 `CL_EXIT` 非 0 加 `[SKIP RUN]`，那是正常的** —— 它本来就是编译失败。

### 1.3 W6-8 · Chromium 四进程口述（5min · W6 门禁未验证项）

**这四个进程名你在部门每天都要碰，不是新知识点。** 闭卷口述（打字即可，各两三行）：

```
browser 进程：跑什么？谁创建它？它崩了会怎样？____
GPU 进程：跑什么？为什么要把 GPU 单独拎出去？____
renderer 进程：跑什么？为什么它和目标网站关在同一个沙箱里？____
utility 进程：跑什么？举一个 360 里你会见到的例子。____
```

**判据**：能说出「renderer 是唯一直接处理不可信输入的进程」这一条，其余三问不要求逐字精确。

---

## 二、17:00-17:50 · 50min · 补昨天下午那格

### 2.1 B5 补做（25min · 昨天整格零产出，占今天 q-fw 格）

> **为什么占 q-fw 的格**：`week-07-to-24-outline.md` 第 46 行写死「W7 周一下午，**首项，不许后移**」，
> 昨天还是后移了。这格的解锁条件是你的简历行「参与 `content/` 进程隔离决策链路排障」——
> 闭卷不过，那条简历行继续冻结。
> **q-fw 第三层①（CEF browser/renderer 进程职责）的去向：W7 周四下午**，不是砍。

**先读**（`E:\code\browser\src` 本机，你可以自己打开核；行号我 10-19 实查过）：

| 类 | 出处 | 一句话 |
|---|---|---|
| `SiteInstance` | `content/public/browser/site_instance.h` 第 36 行起 | 一组**能互相同步执行脚本、因此必须住同一个渲染进程**的文档和 worker。由「站点」+「浏览上下文组」共同决定 |
| `SiteInfo` | `content/browser/site_info.h` 第 27 行起 | `SiteInstance` 的**身份（principal）**。主要用「站点 URL」表示 = scheme + eTLD+1；有时更细（origin）有时更粗 |
| `RenderProcessHost` | `content/public/browser/render_process_host.h` 第 131 行起 | browser 进程这一侧代表「浏览器↔渲染器通信通道」的对象。一般一个渲染进程对应一个 |
| `RenderFrameHostManager` | `content/browser/renderer_host/render_frame_host_manager.h` 第 138 行起 | 管一个 `FrameTreeNode` 的那些 `RenderFrameHost`，维护 `current_frame_host()`；跨站导航时负责**换进程** |
| `ChildProcessSecurityPolicy` | `content/public/browser/child_process_security_policy.h` 第 25 行起 | 给子进程发权限和收权限的单例。例：一个进程能不能加载 `file://`，取决于 browser 有没有命令它加载过 |

**然后闭卷，只答这一问**（答完我再给下一问）：

```
B5：这五个类里，哪一个决定「这个页面要不要单独开一个新的渲染进程」？
    答完再补一句：你怎么知道是它而不是另外四个？
```

⚠️ **不许复述我上表的措辞。** 用你自己的话，最好提一句你改过的那个函数
（`ShouldLockProcessToSite` / `CanCommitOriginAndUrl`）落在哪个类里。

> **上表五个路径我 23:xx 用 `ls` 逐个核过都存在**（`content/public/browser/site_instance.h` /
> `content/browser/site_info.h` / `content/public/browser/render_process_host.h` /
> `content/browser/renderer_host/render_frame_host_manager.h` /
> `content/public/browser/child_process_security_policy.h`）。
> 另外 `content/browser/child_process_security_policy_impl.h` 是它的实现类 —— **判据在 impl 里，接口头里没有**，
> 你要找 `ShouldLockProcessToSite` 就去 impl 那个文件。

### 2.2 W6-7 · CEF / WebView2 两方对照表（25min）

**它是什么**（非主角概念，给全）：
- **CEF**（Chromium Embedded Framework）：把 Chromium 内核嵌进别的程序。q-framework 用它，走的是 Chromium 那套多进程。
- **WebView2**：微软的同类方案，内核同样是 Chromium（Edge 的），但**只有 Windows**，且它自己管进程生命周期，你不直接碰。
- 两者在你的 `E:\code\q-framework\webview\` 下一人一个目录：`cef/` 与 `webview2/`（我实查存在，
  各有一整套 `*_file_handler` / `*_registry_handler` / `*_impl.cc`）。

**要交的东西**：四行表格，落进 `docs/q-framework-track.md`，**每格必须有你的实查依据**（文件路径 + 你看到的那几行说的是什么）：

| 维度 | CEF | WebView2 |
|---|---|---|
| 进程模型（谁起进程、几个） | | |
| JS ↔ C++ 通道用什么机制 | | |
| 谁管 `webview` 对象的生命周期 | | |
| 崩了表现是什么 | | |

**判据**：**至少两格能指到具体文件的行**。指不到就是没查，不是没掌握 —— 那两格写「未查到」并说明你找了哪些地方。

---

## 三、今天的容量账（不是砍，是写明去向）

| 原排 | 去向 | 理由 |
|---|---|---|
| B5（周一 下午首项） | **今天 2.1 补做 25min** | 被写死「不许后移」还是后移了，必须当周补 |
| q-fw 第三层① CEF browser/renderer 进程职责 | **W7 周四下午** | 今天下午格被 2.1 占用；周四本来就是 q-fw 格 |
| W6-7 两方对照表 | 今天 2.2（25min） | 与 CEF/WebView2 同材料，同一格做完最省 |
| 浏览器线 ②（他的功能落在哪层） | W7 周三下午 | 不变，需 B5 先过 |
| 浏览器线 ③ omnibox 两处分层 | W7 周五下午 | 不变 |
| 浏览器线 ④ 360 自有代码与上游并存 | W8 周一下午 | 不变 |
| 欠账 11（`base/` 扫 5 个重复轮子） | W7 周六 4h 档 | 不变 |
| 欠账 13（W3-2 扩容计数纸面推导） | W7 周五上午 | 不变 |
| 欠账 14（W4-1 / W4-7 / W4-8） | W7 周三上午各 5min | 不变 |

---

## 四、今天的最低完成线

**上午**：Q1 四行 + Q3 两句（**先交这个**）→ R1 a-d 四问 → 实验 A/B/C/D（D 要先写预测）。
**下午**：B5 一问 + 两方对照表四行。
`std::thread` 实验 D 或对照表做不完，**必须在下面写一行去向**，不许口头说。

---

## 五、硬规矩（10-19 起对双方生效）

**说「我自己跑过了」必须贴 log，或跑 `cases.bat`。没留证据的「跑过了」等于没跑。**
昨天 14:44 你说手动跑过三种情况，我信了但看不到；同一天上午我自己也栽在同一形状上
（说「换了 `endl` 重跑」，实际字符串替换静默失败，换根本没生效）。
**变换类实验必须先证明变换生效再跑。**

---

## 六、上午格结账（教练 14:1x 当场落盘，不是口头）

**上午格实投 10:30-11:33（63min，157%）。交卷率 100%。**

| 项 | 结果 |
|---|---|
| 〇① Q1 四 case | ✅ 四行各写明崩/不崩 + 死在哪 |
| 〇② Q3 两句机制 | ✅ `endl` 自带 flush ＋ `terminate` 不栈展开不析构全局对象 |
| 1.1 R1 a-d | ✅ 结清。**b 答了三版才对**，正解：临时量寿命单位 = 完整表达式（full-expression） |
| 1.2 实验 A/B/C/D | ✅ 四 case 全跑（教练实跑核过，`build\cases-day2_thread_args.log` 11:33 + `build\cl_B.txt`）<br>A=11 改到 / B `CL_EXIT=2` `error C2672` `_Ty1=int` / C（by value+ref）编过但 a=1 / D a=1 |
| 1.2 追加一问（C 的机制） | ✅ 「`std::ref` 保留引用，但最终是否复制取决于形参类型」—— 方向对 |
| **1.3 Chromium 四进程口述** | 🔴 **没做**。上午时间被 day2 的编译排障吃掉 |

### 🔴 唯一顺延项：1.3 Chromium 四进程口述（W6-8 门禁）

**去向：W7 周三（10-21）上午第一项，5min。** 与原排的「欠账 14（W4-1/W4-7/W4-8）各 5min」同格。
**不撤**（容量类顺延，周三上午 40min 装得下 5+15min）。

### 本次沉淀两条判据（已入 `docs/cpp-concept-map.md` + `docs/debt-map.md`）

- **判据 C**：`#if defined` 分不开「必须编译失败」的 case —— `cl` 编译单位是整个翻译单元，
  函数体全参与编译，一个错误带死整个文件。**他自己判对了方向并解决（B 挪进 `#elif` 分支里）。**
- **判据 D**：`cases.bat` 第二个参数是运行次数，漏掉会把第一个宏吃掉当次数，
  且不报错。→ 交卷前看 log 第 3-4 行 `RUNS:` / `CASES:`。

> `daily/progress.jsonl` 今日那一行按惯例 23:00 结账时写（每天一行，现在写会和晚上重复）。

---

## 七、下午 17:00 不动

2.1 B5（25min）+ 2.2 CEF/WebView2 对照表（25min），原排不变。
**B5 已经是本月第四次被排了**（10-19 写死「不许后移」照样后移）。今天 17:00 第一条消息必须是 B5 的答案。
