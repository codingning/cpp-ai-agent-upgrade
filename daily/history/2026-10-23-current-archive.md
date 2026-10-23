# 2026-10-23（周五）· W7D5 · 工作日 1.5h 口径

> 日期用 `date` 实算：`2026-10-22 23:00 星期四` → 明天 10-23 周五。
> 周次硬公式：`(10-23 − 09-07).days = 46` → `46//7+1 = W7`、`46%7+1 = D5`。
>
> **昨天（W7D4）57min / 63%** —— 上午约 20min（估算）+ 下午 37min。
> 10-19 以来最低，**下午整格基本空转，本月第四次**（10-14 / 10-16 / 10-19 / 10-22）。
> 17:00-17:50 只有 17:08 一条消息，B1 的答案是我给的，**B2 一个字没发也没要。**
>
> 📁 昨天那份 441 行（题面 + 你的答卷 + 我的批改）已存到
> `daily/history/2026-10-22-current-archive.md`，要回看去那里。
> 昨天的学习记录在 `daily/history/2026-10-22.md` —— **里面第二节有四道空题，就是今天第一项。**

> 🔴 **答题规则**：答案写到本文件最末尾「答题区」那一节，**上面的题面不要改。**

---

## 〇、先把话说直（30 秒看完，不占训练时间）

昨天有两件事值得记住，**它们不矛盾**：

**好的那一面**：你两次顶回我的批改，两次都成立。
预测 1 那条我给的「合格写法」被我自己的 `/O2` 实验打死；包体积精度之争你也对。
连续第三天把我问翻 —— 这是你今年最硬的能力，别收。

**坏的那一面**：下午那一格，你 16:49 问我「为什么顺延了，今天完成不了了吗」——
问得很好，我当场撤回。但**整格 50 分钟你实际只发了一条消息，而且是质疑包体积那条。**
B2 我说了「答完 B1 再给」，你没要，我也没主动给。两个人都停了。

今天这一格**由我先把 B2 发在下面**，不等你要。

---

## 一、上午第一项（10:30 起，10min）· 欠账 34 · 四条闭卷自答

> 这四条昨天 21:30 我就发给你了，到 23:00 没回。**不许抄我的原话**，抄原文不计分、当场退回
> （10-17 立的规矩：判据类题复述我的措辞 = 误以为自己会，比标「忘」更危险）。

**A1**　ProfileImport 这个 service 现在是 `kNoSandbox`。假设明天有人给它**上了沙箱**，
下面这两处代码**会死在哪一步**？（一句话，指明是哪个动作被拦住）

```
ie_importer_win.cc:252   base::win::RegKey key(HKEY_CURRENT_USER, ...)
firefox_importer.cc:657  base::CopyFile(file, destination)   ← 从别人的 profile 目录拷 places.sqlite
```

> 「沙箱」在这里是什么：Windows 沙箱会剥掉进程对注册表、对任意路径文件的访问权。
> 你要答的是：**这两行各自需要的那个权限，沙箱里还有没有。**

**A2**　utility 的隔离理由，**不许写「可以按任务单独配置权限」**（那是机制不是理由）。
换成一句话：**它处理的输入为什么不必当敌意代码来执行？**
（对照：renderer 处理的网页要执行站点给的 JS，所以必须当敌意代码环境配。）

**A3**　你在 q-framework 里搜不到谁加的 `--type=renderer`。**原因是什么**（一句话），
以及**以后再遇到「这个开关是谁加的」，你的搜索范围该怎么扩**（一句话）。

**A4**　「修好 data race」是什么意思？为什么跑 1000 次全对也证明不了？
（我昨天 17:04 直讲过，**用你自己的话重写**。写成我的措辞 = 退回。）

---

## 二、上午主线（10:40-11:10，30min）· mutex + `lock_guard`

### 先讲知识点（顺序铁律：这个你没学过，我直接讲，不让你猜）

**`std::mutex`（互斥量）**：一把锁。`lock()` 占住它，别的线程走到 `lock()` 会**停在那里等**；
`unlock()` 放开，等的那个才能进。头文件 `<mutex>`。

```cpp
std::mutex g_mu;
g_mu.lock();
++g_counter;        // 这一段同一时刻只有一个线程在跑
g_mu.unlock();
```

**问题**：中间那段如果 `return` 了、抛异常了，`unlock()` 就不会执行 → **死锁**
（所有线程永远等一把永远不放的锁）。

**`std::lock_guard<std::mutex>`**：RAII 封装（**就是你 W1 第一天学的那套**：
构造时 `lock()`，析构时 `unlock()`，作用域一出去自动放）。

```cpp
{
    std::lock_guard<std::mutex> lk(g_mu);   // 构造 → 上锁
    ++g_counter;
}                                            // } 处析构 → 自动解锁
```

> `lock_guard` **没有** `lock()` / `unlock()` 成员，它的全部用法就是「活着 = 锁着」。
> 这是 W1 RAII 那条「资源生命周期绑定对象生命周期」在并发上的同一个应用。

### 今天写什么

在 `F:\code\cpp-practice\week-07\` 新建 `day5_mutex.cpp`，**三个 case 一个文件、宏分支**
（你 10-21 自己推出来的手法，比分文件好，继续用；`#else` 里放 `#error` 守卫）：

```cpp
// CASE_RAW      —— 裸 ++g_counter，什么都不加（昨天那版，作对照组）
// CASE_LOCK     —— g_mu.lock() / g_mu.unlock() 手动成对
// CASE_GUARD    —— std::lock_guard，作用域自动放
```

骨架（**只有结构，内容你自己填**）：

```cpp
#include <iostream>
#include <thread>
#include <mutex>

long long g_counter = 0;
std::mutex g_mu;        // 三个 case 共用这一把，RAW 那个 case 不碰它

void bump(int times) {
    // 按当前宏，决定循环体里加不加锁
}

int main() {
    const int N = 2000000;
    // 两个线程各 bump(N)，都 join，打印 expected / actual / lost
}
```

### 🔴 编译卡点（10-17 立的规矩，不许全写完再批）

- **第一卡点**：`CASE_RAW` + `CASE_LOCK` 两个 case 写完，**先编译一次跑通**，把输出贴给我，再往下写
- **第二卡点**：`CASE_GUARD` 写完再编译一次

一条命令把三个 case 一起传（别一个一个传，log 会被整份覆盖 —— 10-21 栽过）：

```
..\cases.bat day5_mutex.cpp 5 CASE_RAW CASE_LOCK CASE_GUARD
```

### 先写预测再编译（带条件，不要对冲 —— 昨天那条教训）

- 预测 1：`CASE_LOCK` 跑 5 次，`lost` 会是什么？**写成带条件的句子**
- 预测 2：`CASE_GUARD` 和 `CASE_LOCK` 的结果会不会不同？为什么
- 预测 3（这个最值钱）：**三个 case 的运行时间**会有差别吗？哪个最慢？差多少量级？

> 提示：第 3 问你无法从代码看出来，**要测**。`cases.bat` 不打时间，
> 你用 `std::chrono::steady_clock` 在 `main` 里自己掐表 —— 这个我没教过，
> 写法是：取两次 `steady_clock::now()` 相减，用
> `std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count()` 拿毫秒数，头文件 `<chrono>`。
> **这是 API 用法不是今天的练习本体，直接用。**

---

## 三、下午整格（17:00-17:50，50min）· q-fw 第三层 B2 · 欠账 12

> **B2 我现在就发，不等你问。** 材料我全部 `grep` 过，文件和行号都确认存在。

### 昨天 B1 的结论，先接上

同一个 exe 两种身份：browser 侧（Chromium 内核，`render_process_host_impl.cc:3535`）
写入 `--type=renderer`；子进程侧（q-fw，`client_app.cc:55`）读这个开关认出自己。
**一端写、一端读。**

今天看的是**认出身份之后，两边各自装上了什么**。

### 材料（实查确认存在）

`E:\code\q-framework\webview\cef\` 下：

| 文件 | 内容 |
|---|---|
| `cef_util.cc:21-34` | `CefRunChildProcess()` —— 子进程入口，第 31-32 行按身份 `new CefRenderProcessApp()` |
| `cef_util.cc:36-53` | `CefInit()` —— 第 42 行 `new CefBrowserProcessApp` |
| `browser/` 目录 | 5 对文件：`cef_browser_{file,registry,message}_handler` + `cef_browser_handler` + `cef_browser_process_app` |
| `render/` 目录 | 6 对文件：`cef_render_{file,registry,message,appcmd}_handler` + `cef_render_handler_base` + `cef_render_process_app` |

**两边成对出现**：`cef_render_file_handler.cpp`（791 行）/ `cef_browser_file_handler.cpp`（859 行）。

### B2（一问，答完我再给 B3）

网页里的 JS 调一个「写文件」的接口。实查这条链是这样走的：

```
render 侧  cef_render_file_handler.cpp:203  HandleWriteFile(...)
           :209  CefRefPtr<CefListValue> args = CefListValue::Create();   ← 只是把参数打包
                 （整个文件里 Create() 出现 20 多次，全是在组消息）

browser 侧 cef_browser_file_handler.cpp:18   OnProcessMessageReceived(...)
           :113  HandleWriteFileAsync(...)
           :124  CefPostTask(TID_FILE, ... DoWriteFile ...)
           :255  DoWriteFile(...)
           :257  webview_util::WriteFile(filePath, content);              ← 真正落盘在这里
```

**问题**：render 侧明明已经拿到了文件路径和内容，**为什么不直接在 render 进程里写文件，
非要打包成一条消息跨进程送到 browser 进程再写？**

**要求**（避免你答成粗量）：
- 不许答「CEF 的架构就是这样」「为了解耦」—— 这是粗量，等于没答
- 必须用**昨天 Q1/Q2 那套话**来答：render 进程的 integrity level 是什么、
  它处理的输入来自哪、所以它**有没有**写任意路径文件的权限
- 再补一句：如果真让 render 直接写，**一个被攻破的网页能干什么**

> 这一问和昨天的 Utility vs Renderer 是**同一个知识点的第二个实例**。
> 昨天你是在 Chromium 本体里看它，今天是在 q-framework 里看同一条原则落地。
> **答得出来，说明昨天那个不是背的。**

---

## 四、顺延与去向（当场落盘，不写「以后」）

| 时间 | 内容 | 状态 |
|---|---|---|
| 10-23 上午 | 欠账 34 四条闭卷自答（A1-A4） | ✅ **已清**（A4 第二问返工一次后过） |
| 10-23 上午 | `day5_mutex.cpp` 三 case + 三预测（两个编译卡点） | ✅ 代码过、预测 3 返工后结论正确；⚠️ 卡点流程没走，记流程欠账 |
| 10-23 下午 | q-fw 第三层 **B2**（已发在上面，不用等） | 今天，整格 |
| 10-23 随手 | 提交昨天的 `day4_data_race.cpp`（欠账 35，`?? ` 状态） | 今天 23:00 和 day5 一起 commit |
| **10-24 周六 4h** | **7 日复测（`review_7d` 10-23 到期，10-23 排不下，移到周六首项）** | → **10-24 首项** |
| 10-24 周六 4h | **D 档第 1 题** `f935d6b0`「升级包下载后触发崩溃」（根因线程模型，与本周 thread 主线合流） | → 10-24（不变） |
| 10-24 周六 4h | 欠账 11 `base/` 扫 5 个重复轮子 | → 10-24（不变） |
| 10-24 周六 4h | 欠账 13 W3-2 扩容计数纸面推导（原排 10-23，今天排不下） | → **10-24** |
| W8 | 欠账 26 B5-②③（🟡 半过） | → W8（不变） |
| 随手 | `day1_operatorbool.cpp` 补 `~Test()` | 🟡 小项，挂着 |

> **周六 4h 档现在排了四项**（复测 + D 档第 1 题 + `base/` 扫轮子 + 纸面推导）。
> 这是真会满，周五收工时我会按实际进度再砍一次顺序，**不砍内容**。

---

## 五、代码小修（1 分钟，顺手）

> ✅ **本项作废 —— 他已经改过了，是我布置晚了。**
> 实查 `day4_data_race.cpp:13` 已是 `for (int i = 0; i < times; i++)`，
> 文件 mtime `2026-10-22 16:44`，**昨天写的时候就是 `int`**。
> 我昨晚排这条时看的是早先那一版，布置了一个已经不存在的问题。下面的原因说明留着当知识点。

`day4_data_race.cpp` 的 `for (size_t i = 0; i < times; i++)` → 改 `int i`。
原因：`i` 是 `size_t`（无符号 64 位）、`times` 是 `int`（有符号 32 位），
**有符号与无符号比较**会把 `times` 提升成无符号 —— 今天 N 是正数没出事，
但传 `bump(-1)` 时 `-1` 会变成 18446744073709551615，循环近乎不结束。
cl 没报是因为默认 `/W1`，这条是 **C4018**，`/W3` 起才报（我核过你的 `build\cl_plain.txt`，确实无警告）。

---

## 六、答题区（答案写这里，上面的题面不要动）

### A1-A4（四条闭卷自答）

```
A1：第一行需要的是注册表权限，第二行需要的是文件权限。沙箱里这两个权限都没有。

A2：因为　utility的代码还是chrome自己写的，所以不必当敌意代码来执行。但他解析的文件是别人的，所以要小心。

A3（原因 / 搜索范围怎么扩）：因为这个参数是browser进程添加的，而q-Framework是只使用内核，没有内核代码的，这个搜索范围应该去内核代码里搜索

A4：就是用方法控制线程的执行顺序，让资源不能被同时访问。 比如使用mutex，或者使用 atomic把变量变成原子操作。
```

### 上午 · day5_mutex 三预测

```
预测 1（CASE_LOCK 的 lost，带条件）：是0

预测 2（GUARD 和 LOCK 会不同吗，为什么）：不会，因为他们都加了锁

预测 3（三个 case 的耗时，哪个最慢，差多少量级）：LOCK 最慢，和lock_guard差8倍左右 和CASE_RAW差12倍左右
```

> 预测 3 实测结果：**LOCK 和 GUARD 只差 1ms**（54 vs 55），不是 8 倍。
> 8 倍是第一版代码把 `lock_guard` 建在 `for` 外面造成的 —— 那不是 `lock_guard` 对照组，
> 是「加锁 1 次」对「加锁 400 万次」，两个线程被做成了串行。
> 教练同机实跑正确版（锁移进循环体）：GUARD 54/55/55ms、LOCK 52/52/53ms。
> **结论：`lock_guard` 没有运行时额外开销**，它编译出来就是 lock/unlock，RAII 只把 unlock 挂在析构上。
> 真正的差距在「有锁 vs 无锁」：5ms → 54ms，约 10 倍。

### 上午 · 第一卡点输出（RAW + LOCK）

> ⚠️ 流程记录（不扣分，记事实）：今天**没有分两次卡点编译**，三个 case 一把 `/D` 全跑。
> `build\cases-day5_mutex.log` 每跑一次就整份覆盖，所以第一版（GUARD 写错那版，10:49）的 log 已经没有了。
> 下次按 10-17 的规矩分两次跑，中间那份 log 才留得下来。

第一版（10:49，`lock_guard` 建在 `for` 外面 —— **实验不成立**，留作教训）：

```
CASE_RAW    ms :4    expected :4000000  actual :2000000  lost :2000000
CASE_LOCK   ms :51   expected :4000000  actual :4000000  lost :0
CASE_GUARD  ms :6    expected :4000000  actual :4000000  lost :0   ← 6ms 是假的，锁在循环外
```

### 上午 · 第二卡点输出（加上 GUARD）

返工版（11:06，`lock_guard` 移进循环体，其余不动）—— 摘自 `F:\code\cpp-practice\build\cases-day5_mutex.log`：

```
===== cases.bat  周五 2026/10/23 11:06:18.11 =====
SRC  : F:\code\cpp-practice\week-07\day5_mutex.cpp
RUNS : 5 per case
CASES: CASE_RAW CASE_LOCK CASE_GUARD

================ case: CASE_RAW   (cl /DCASE_RAW) ================
CL_EXIT=0
--- run 1 stdout ---
ms :5
expected :4000000
actual :2058953
lost :1941047
--- exit codes over 5 runs ---
exits: 0 0 0 0 0
nonzero: 0 / 5

================ case: CASE_LOCK   (cl /DCASE_LOCK) ================
CL_EXIT=0
--- run 1 stdout ---
ms :54
expected :4000000
actual :4000000
lost :0
--- exit codes over 5 runs ---
exits: 0 0 0 0 0
nonzero: 0 / 5

================ case: CASE_GUARD   (cl /DCASE_GUARD) ================
CL_EXIT=0
--- run 1 stdout ---
ms :55
expected :4000000
actual :4000000
lost :0
--- exit codes over 5 runs ---
exits: 0 0 0 0 0
nonzero: 0 / 5
```

本人补跑（返工后两次）：GUARD 54ms / 55ms。
教练同机独立实跑正确版三次：GUARD 54/55/55ms，LOCK 52/52/53ms。三组数据互相对齐。

`CASE_RAW` 多次运行的 `lost`（教练同机五次）：1977859 / 1935843 / 1998563 / 1886761 / 1559523
—— **没有两次相同**。这组数据就是 A4 第二问的证据：data race 的结果依赖线程实际交错，
交错由 OS 调度决定，所以「跑 N 次全对」排除的只是「每次运行必出错」，
排除不掉「未遇到的交错会出错」。

### A4 第二问（返工后，本人原话，已过）

```
可能的交错有无数种，全对排除了每次运行必出错，没排除掉未遇到的交错会出错情况
```

> 教练补名字：**测试只能证伪，不能证明正确**。
> data race 的正确判据不是「跑多少次都对」，而是：
> ① 用工具查内存访问序（ThreadSanitizer 做这件事）；
> ② 从代码上证明每次访问都在同一把锁里、或该数据是 atomic。
> 今天的 LOCK/GUARD 属于 ②。
> ⚠️ 待本人验证：ThreadSanitizer 据教练印象 MSVC 不支持（MSVC 只有 ASan），
> **这是推测，用到时查官方文档确认。**

### 下午 · B2

```
```
