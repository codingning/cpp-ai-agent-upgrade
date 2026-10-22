# 360 安全浏览器训练轨（面试深挖链驱动 · 第二条主线）

> 建立：2026-10-15（W6D4）晚
> 依据：本人 10-15 原话 **「我的简历上写了 360 安全浏览器客户端需求 + q-framework 项目开发，
> 你作为面试官，会怎么一步一步深挖我简历里的项目和我的技术深度呢？应该按照这个逻辑去训练我啊」**
> → 质疑成立：教练 09-22 给 q-framework 建了深挖链，**浏览器这条线一条没排**，
> 而它是两个项目里**更值钱**的那个（Chromium 本体，不是嵌内核）。
>
> 排法照本人同日指令：**先按他自己做过的深挖，再对整个项目拓宽。**
> 本文件与 `docs/q-framework-track.md` 同规格（四层深挖链 + 实查锚点 + 每个非主角概念标「它是什么」）。

---

## 零、仓库与提交实查（2026-10-15 教练实跑，可核）

- **仓库**：`E:\code\browser`（gclient 检出），源码在 `E:\code\browser\src`
- **remote**：`ssh://<user>@brow.src.corp.qihoo.net:29418/360browser.git`
- **当前分支 HEAD**：`84dafdec8dcd2 [se16][closetab] intercept close tab and pop 3`
- 🔴 **提交数已更正（2026-10-15 19:0x 重查，教练前一个数字是错的）**：

  | 口径 | 数 |
  |---|---|
  | `git log --author=ningxinyang`（**仅当前 checkout 分支**） | 28 ← 教练 17:47 误当成全部工作量写进本文件 |
  | `git log --all --author=ningxinyang`（**全分支**） | **159** |
  | Codex 从 Gerrit 导出（跨仓库，含 360Game/360pic 等） | 469 条，其中 `360browser` **147** |

  **根因记教练账**：连 `git branch -a` 都没跑就下结论 ——
  「拿单一证据源当全部证据」**第 3 次**（09-24、10-15 Q3、10-15 本条）。
  下文一节「23 个功能提交」的分档是**当前分支子集**的分档，结论本身仍有效，
  但**不是他的全部工作量**，W7 排课前必须按 159 全分支重做一次分档。
- 时间跨度（当前分支口径）**2025-04-07 ~ 2025-11-10**
- ⚠️ **内网 Gerrit 页 `brow.src.corp.qihoo.net/q/owner:...` 教练访问不了**
  （web 工具拦私有网段，curl 返回 `HTTP=401`）。**本文件全部数据来自本机 git 仓库实查**，
  比 Gerrit 页更全（含未上 Gerrit 的本地提交）。

### 目录分布（按本人提交的文件路径统计，前 15）

| 次数 | 目录 | 层 |
|---|---|---|
| 22 | `chrome/app/theme/360skin/skin/frame` | 皮肤资源（非代码） |
| 11 | `chrome/browser/360` | 🟢 360 自有业务层 |
| 6 | `chrome/browser/ui/views/side_panel` | 🔵 上游 UI 层 |
| 5 | `components/download/public/common` | 🔴 **上游跨层组件** |
| 5 | `chrome/browser/extensions/api/account360` | 🟡 扩展 API 实现 |
| 4 | `components/omnibox/browser` | 🔴 **上游跨层组件** |
| 4 | `chrome/common/360` | 🟢 360 自有 |
| 4 | `chrome/browser/360/external_apis` | 🟢 360 自有（AppCmd） |
| 3 | `components/download/internal/common` | 🔴 **上游跨层组件** |
| 3 | `chrome/browser/ui/webui/360/seerrors` | 🟡 WebUI |
| 3 | `chrome/browser/ui/views/omnibox` | 🔵 上游 UI 层 |
| 2 | `extensions/common` | 🔴 **上游扩展框架层** |
| 1 | `net/base/url_util.cc` | 🔴 **上游网络层** |

### 🔴 关键发现：他的手跨过了四层，但他不知道这四层叫什么

**10-15 上午他亲口答「`chrome/` 和 `content/` 的分界，我答不上来」。**
但实查他改过的上游文件里有：

```
components/omnibox/browser/omnibox_edit_model.cc
components/download/internal/common/download_item_impl.cc
components/download/internal/common/download_file_impl.cc
components/download/public/common/download_destination_observer.h
extensions/common/permissions/permissions_data.cc
extensions/browser/extension_util.cc
net/base/url_util.cc
```

→ **`chrome/` / `components/` / `extensions/` / `net/` 四层都动过。**
这正是他的典型形态（memory 在案）：**知识已在脑子里，缺的是名字和索引。**
**所以浏览器线第二层不是「从零教」，是「给他已经干过的事装上名字」。**

---

## 零点五、🔴 S 档：`8beac32` —— 他改过 `content/` 层的进程隔离决策点

**教练 17:47 建本文件时完全漏掉这个提交**（因为只查了当前分支）。
19:0x 全分支重查 + 实读 diff 后确认：**这是全部提交里最值钱的一个，单独立 S 档。**

实查（`git show --stat 8beac32`，教练本机跑，可核）：
`8beac32766ee0  ningxinyang  2025-11-19  "fix bug"` —— **19 文件 242+/37-**，其中 `content/` 下 16 个文件：

```
content/browser/site_info.cc/.h
content/browser/site_instance_impl.cc/.h
content/browser/child_process_security_policy_impl.cc/.h        (+63/-… 本次最大改动)
content/browser/renderer_host/render_process_host_impl.cc/.h
content/browser/renderer_host/render_frame_host_impl.cc
content/browser/renderer_host/render_frame_host_manager.cc
content/browser/renderer_host/navigation_request.cc
content/browser/renderer_host/navigator.cc
content/browser/dom_storage/dom_storage_context_wrapper.cc
content/browser/file_system/file_system_manager_impl.cc
content/public/browser/child_process_security_policy.h
content/public/browser/content_browser_client.cc/.h
+ chrome/browser/chrome_content_browser_client.cc/.h
```

改法（diff 原文）：给两个决策函数加了一个 `parent_host` 参数，用 `#if defined(FOR_360SE)` 包着：

```cpp
// content/browser/site_info.h
bool ShouldLockProcessToSite(const IsolationContext& isolation_context
#if defined(FOR_360SE)
    , std::string parent_host = ""
#endif
) const;

// content/browser/child_process_security_policy_impl.h
CanCommitStatus CanCommitOriginAndUrl(..., const UrlInfo& url_info
#if defined(FOR_360SE)
    , std::string parent_host = ""
#endif
);
```

**为什么是 S 档**：`ShouldLockProcessToSite` 决定「这个 site 要不要把 renderer 进程锁死」，
`CanCommitOriginAndUrl` 决定「这个 renderer 能不能提交这个页面」——
**这两个函数就是 Chromium 进程模型与沙箱权限体系的决策点本身**，不是业务层、不是 UI 层。
他动的是 Site Isolation 的判据。**全场面试最硬的一张牌，而他自己不知道这是什么。**

⚠️ **但他上午亲口答「`chrome/` 和 `content/` 的分界，我答不上来」** ——
手已经改到 `content/browser/renderer_host/` 里，却说不出这一层是什么。
**所以浏览器线必须从「给已经干过的事装上名字」起步，不是从零教。**

**挂账（W7 浏览器线第一课，教练出题用）**：`SiteInstance` / `SiteInfo` /
`RenderProcessHost` / `RenderFrameHostManager` / `ChildProcessSecurityPolicy`
五个类各是什么、Site Isolation 怎么决定页面放哪个进程、`FOR_360SE` 这个宏为什么必须包着改动。

### 📌 简历行（2026-10-17 本人指令入册：「把这条记录下来，排进训练计划」）

| 项 | 内容 |
|---|---|
| **简历写法** | 参与 Chromium `content/` 层 Site Isolation 进程隔离决策链路的排障与定制 |
| **支撑提交** | `8beac32`（19 文件 242+/37-，其中 `content/` 16 文件）+ `8bc3df2`（后续 2 文件）+ 三条 Revert 同批 |
| **决策点** | `ShouldLockProcessToSite`（这个 site 要不要把 renderer 锁死）、`CanCommitOriginAndUrl`（这个 renderer 能不能提交这个页面） |
| **⚠️ 使用前提** | **只有 W7 第一课闭卷过关后才能写进简历**。现在的状态是「手干过、说不出名字」，直接写上去面试会当场穿帮（见上方 122 行记录）。判据：五个类各能用一句话说清 + Site Isolation 决策链能画出来 |
| **⛔ 不许写** | 「改过 365 个文件」——那是工时不是能力（10-17 B2 已定）。365 里大部分是 360 定制接线，换公司不值钱 |

**排期**：W7 浏览器线**第一节**（不是第四节，升到最前）。原排在「W7 浏览器第二层②③④」里没点名，现单列为首项，
因为这是全场唯一一张 S 档牌。W7 完整格 = ①五个类 + 决策链闭卷（S 档，40min）②他的功能落在哪层 ③omnibox 两处分层 ④360 自有代码与上游并存。


⚠️ 另：`a6d8f64`/`f5d15f8`/`4d81f7c` 三条 Revert 也碰同一批文件，
`8bc3df2d`（2 文件）是同一主题的后续小改 —— 这组提交要**合起来当一个话题讲**，不是五个话题。

---

## 零点六、🔴🔴 S 档的真实案情（2026-10-20 本人自述 + 教练全链路实查，当日重写）

> **本节取代零点五里所有「机制推断」段落。** 10-20 上午教练凭 `site_info.cc` 里
> `#ifdef ENABLE_IE_KERNEL` 那个分支讲了一整段 IE 内核机制，**那是别人的代码（fuyang 的改动），
> 与本人提交无关，全部作废**。同日下午教练又把 bug 判成 OOPIF 跨进程合成，**同样作废**。
> 两次同形态错误：**没查提交就讲机制**（「拿眼前文件状态当他的改动」第 3、4 次）。

### 一、真实 bug（本人 10-20 17:4x 原话，未经教练加工）

> 「我们有一个游戏平台，使用的 360 浏览器的 chrom 内核去渲染的页面，结果一个游戏页面在玩的过程中，
> 出现了一部分区域被另一个区域遮挡的情况，排查可能是渲染顺序导致的，但是调试发现其中一个进程
> 发现不了另外一个遮盖部分的控件，怀疑是两个不同进程导致的，所以做了这次修改。」

**定性：NPAPI 插件（Flash）窗口遮挡**，不是 OOPIF 合成，不是 Site Isolation 本身出问题。
`wyxz.wan.360.cn` 的游戏跑在 NPAPI 插件里；NPAPI 插件在 Windows 上是**独立原生窗口（HWND）**，
不参与 Blink 图层合成。Blink 必须自己算「哪些 HTML 元素盖在插件窗口上」再在插件窗口上
**抠洞（cutout）** —— 实现就在 `third_party/blink/renderer/core/exported/plugin_occlusion_support.cc`
的 `GetPluginOcclusions` / `AddToOcclusions`。

**真根因（fuyang `0787c66` 解掉的）**：`AddToOcclusions` 原来有一行
`if (!renderer->HasNonZeroEffectiveOpacity()) { skip; }`
—— 盖在插件上的 iframe / div 容器 **opacity 恰好为 0**，被当成「不可见」跳过，
于是没抠洞，插件画面把那块 content 盖住了。
**这是纯渲染层 bug，与进程模型无关。**

### 二、本人的改动：`8beac32`（2025-11-19，19 文件 242+/37-）

**只做一件事：新加一个 `parent_host` 参数，从最外层穿到最里层，用域名白名单关掉进程锁。**

```
RenderFrameHostImpl::CanCommitOriginAndUrl        ← 取 parent_host
  GetMainFrame()->GetLastCommittedURL().host()      （仅非主框架）
    → ChildProcessSecurityPolicyImpl::CanCommitOriginAndUrl(..., parent_host)
      → CanCommitURL / CanAccessOrigin / CanAccessMaybeOpaqueOrigin
        → SiteInfo::ShouldLockProcessToSite(..., parent_host)          site_info.cc:757
          → ChromeContentBrowserClient::ShouldLockProcessToSite(..., parent_host)
              判据：parent_host 或 effective_url.host() 以 "360.cn" 结尾 → return false

另一路：SiteInstanceImpl::IsNavigationSameSite
      → IsSuitableForUrlInfo(url_info, parent_host)
      → RenderProcessHostImpl::IsSuitableHost(..., parent_host)

硬编码白名单：SiteInstanceImpl::IsSameSite 里
      if (src_url.host() == "wan.360.cn" || 以 ".wan.360.cn" 结尾) return true;
```

**他当时为什么加这个参数（本人 10-20 原话）**：「最里层获取不到主 host」——事实正确。

### 三、真正的技术教训（这条比提交本身值钱）

**fuyang 要的信息 `for_outermost_main_frame` 就在 `IsNavigationSameSite` 的形参里，
而且那个函数里已有现成的两行（当时被 `#ifdef FOR_WINX86` 框着）。**

| | 本人 `8beac32` | fuyang `0787c66`（11-25） |
|---|---|---|
| 判断依据 | 新加 `parent_host`，穿 6 层 | 复用已有 `for_outermost_main_frame`，不加参数 |
| 范围 | 域名白名单硬编码 | 构建宏 `USE_360HACK` |
| 规模 | 19 文件 242 行 | **3 文件 8 行** |
| 结果 | 2 天后 Revert（`4d81f7c` 11-21） | 12-08 被 Revert（`6e40f03`，message 空，原因查不到） |

→ **判据（本人 10-20 自己答对第①问）**：**一个判断需要你穿 6 层参数，先怀疑判断的位置选错了，
而不是参数不够。** 往外层找一个天然持有该信息的切点。
本人 17:4x 答「我会先尝试放开这里的宏，调试」——**与 fuyang `0787c66` 的做法一字不差**，
说明直觉已有，缺的是「先去外层看一眼」这个动作。

**本人 ② 问答对**：域名白名单是硬编码，新域名就要改代码重新发版（他自己看出的，教练只给了提示）。
**本人 ③ 问答错**：猜「shangshihao 发现了更好的改法」。实际后续**没有更好的改法** ——
`88c5bf18`（fuyang 2026-01-15，message「test for renderer」）是把两处宏**注释掉**，
`ShouldLockProcessToSite` 恒返回 `true`，是调试提交不是修复。
**HEAD（`84dafdec`）上 `need_check_opacity` / `wyxz.wan.360.cn` / `360.cn` 全部不存在。**

### 四、🔴 时间线：这个问题到今天没有进主线的解法

```
2025-05-22  fuyang   插件抠洞 + x86 子框架合并          → Revert
2025-11-19  本人     parent_host 穿 6 层 + 360.cn 白名单 → Revert（两天后）
2025-11-25  fuyang   宏放宽 USE_360HACK（8 行）          → Revert（12-08，原因无记录）
2026-01-15  fuyang   把宏注释掉「test for renderer」      → 调试提交
2026-10-20  HEAD     need_check_opacity / wyxz / 360.cn 全部不存在
```

**所以简历/面试口径必须改**（本节推翻零点五的写法）：

- ❌ 不说「我修了一个 bug」
- ✅ 说「**定位了一类插件渲染与进程模型冲突的问题，提了方案，因侵入安全核心类被回滚；
  后续团队三轮尝试同样未进主线**」
- **③ 问那处答错暴露一个危险惯性**：他把「被否定」等同于「别人有更优解」。
  事实是他和领导都没解决，这是社区级难题（`crbug.com/950453` 一类）。
  这个惯性在面试里很致命——会让他把「难题未解」说成「我不够好」。

### 五、⭐ 这件事真正改写了简历行的分量

零点五里写的是「参与排障与定制」，现在有了**完整闭环 + 失败原因 + 同题对照**：
定位（现象 → 怀疑进程）→ 方案（`parent_host` 穿链路）→ 被回滚原因（侵入 CPSPI 安全核心类，
穿 6 层签名）→ 对照（fuyang 用已有形参 8 行搞定）→ 结局（三轮全被回滚，问题仍在）。

**面试官最想听的不是「修好了」，是「你知道自己的方案错在哪」。** 这一节就是他错在哪的完整答案。

### 六、🔴 本人 10-20 18:2x 追问三条 —— 面试第二层，必须补的三个洞

> 他的原话：「①你是怎么排查的，为什么说是跨进程了 ②怎么定位到哪里是判断 render 是否分进程启动的代码
> ③这个问题最后就没有解决吗」。**三问全部是面试官的第二层追问，问得对。**

#### ⚠️ 事实更正：`a6d8f64`（撤销 fuyang 插件改动）是本人自己提的 Revert

`git log -1 --format="%an %ae %ad" a6d8f64f0bfa6` → **`ningxinyang@360.cn`，2025-12-04**。
零点六第四节的时间线写成了「本人方案被回滚、fuyang 方案被回滚」，
**漏了一条：本人在 12-04 回滚了 fuyang 5 月那条插件改动。** 这不是单向被否定，是双向来回。

#### ③ 答案：没有解决，实查可核（HEAD = `84dafdec`）

| 查的东西 | HEAD 上的状态 |
|---|---|
| `AddToOcclusions` 的 `need_check_opacity` 参数 | **不存在**。`plugin_occlusion_support.cc:474` 仍是原始的 `if (!renderer->HasNonZeroEffectiveOpacity()) { ... return; }` |
| `wyxz.wan.360.cn` / `360.cn` 白名单 | **不存在** |
| `IsNavigationSameSite` 里 `if (!for_outermost_main_frame) return true;` | **不存在** |
| `git log --all -S "need_check_opacity"` | 只命中那几条 commit 与 Revert，**最终没留下** |
| 2026 年之后碰过这两个文件的提交 | 只有 `096d4c9d`（xiehui「AI解决冲突第一轮」4 月）与 `59333b3a`（Chromium 154 快照导入 9 月）—— **都是升级合并，不是修这个 bug** |

**→ 面试口径（直接用）**：「这个问题我们团队三轮方案都被回滚了，最后没有进主线的修复。
根因在插件窗口的遮挡计算，但修它要么动安全核心类、要么全局关掉子框架隔离，代价都比收益大。
后来 NPAPI 本身在退场，这个 case 就被搁置了。」

#### ①② 教练**不能**替答 —— 边界写死

commit message 只有「fix bug」四个字，Gerrit 内网页教练访问不了（`curl` 401）。
**「他当时怎么排查的」「怎么定位到那段代码的」git 里没有任何记录。**
→ ⛔ **教练不许编排查过程给他背**。今天已犯两次同类错误（教练账 3、4），不犯第三次。

#### ① 的唯一线索：那个文件里有前人留的调试开关

```cpp
// plugin_occlusion_support.cc:54-56
bool bEnableCutoutLog = false;
bool bEnableCutoutLogDetail = false;

// AddToOcclusions 内（474 行起）
if (bEnableCutoutLog) {
    printf("AddToOcclusions [%p %s rect %s] Opacity: 0, skipped\n",
        renderer, renderer->DebugName()..., AbsoluteVisualRect(renderer)...);
}
```

打开它，**每个被算进遮挡的元素、每个被 opacity 跳过的元素都会打出 `DebugName` + 矩形坐标**。
→ **挂账（明天上午交）**：问他当时实际用的手段 —— 这类 printf 日志 /
`chrome://process-internals` / DevTools Layers / attach 调试器看 HWND / 还是别的。
**答「记不清」也收**，那就改成用方法论补事实空白（面试可接受
「当时具体步骤记不清，但这类问题我现在的排查路径是……」，不接受编细节）。

#### ② 教练给的是「以后怎么定位」，不是「你当时怎么定位的」

| 手法 | 做法 | 对应本案 |
|---|---|---|
| **① 从行为反查判据** | `chrome://process-internals` 列出每个 `SiteInstance` / `ProcessLock` / 所属进程。页面行为变了但不知哪行代码管 → 先找那个页面能看到的量 | 能直接看出游戏页和 iframe 是否同进程 |
| **② 从宏反查定制点** 🔴 | 360 定制全被宏包着：`USE_360HACK` / `FOR_360SE` / `FOR_WINX86` / `ENABLE_IE_KERNEL`。`grep <宏> + <子系统关键词>` 直接命中前人改过的位置 | **当时 grep `USE_360HACK` + `site_instance` 就会看到 fuyang 留的那两行** —— 信息本来就在仓库里，缺的是「先 grep 宏」这个动作 |
| **③ 从 Revert 链反查雷区** | `git log --all --grep="<关键词>"` 看这主题改过几轮、回滚几次。回滚多 = 问题真难 + 你的改动也会被回滚 | 本案 `--grep="opt for plugins"` 直接看出 fuyang 五月起已来回三轮 |

**②这条是本案真正的方法论收获**，与第三节「一个判断要穿 6 层参数，先怀疑位置选错」同一根：
**都是「先往外/往前看一眼」，而不是从自己站的地方硬往里凿。**



---

## 一、他做过的 23 个功能提交 —— 按「面试可讲价值」分三档

> ⚠️ 这张表是**排课依据**，不是简历。
> 判据沿用 09-22 定的：**技术含量高 = 面试官挖得到、且他现在答不上来的那一层。**

### 🥇 A 档：有真技术内核，面试能讲 5 分钟以上（3 个）

| commit | 日期 | 标题 | 规模 | 为什么是 A 档 |
|---|---|---|---|---|
| `04fd0d1` | 2025-10-30 | 网页打不开需求 | **9 文件 156 行** | 见下方「A1」——单例 + `SequencedTaskRunner` + 改上游 `sad_tab` + WebUI |
| `64986ec` | 2025-09-11 | 添加新扩展 id 和关闭接口 | **10 文件 92 行** | 见下方「A2」——扩展 API schema + 三层上游（extensions / net / chrome） |
| `578c743` | 2025-10-11 | SE-AI 地址栏优化 | **20 文件 168 行** | 见下方「A3」——改 `components/omnibox` + command id + 系统菜单 |

### 🥈 B 档：有可讲点但需要重新包装（5 个）

| commit | 标题 | 可讲点在哪 |
|---|---|---|
| `0061dc1` | 图生图/图生视频按钮（10 文件 111 行） | 改 `render_view_context_menu.cc` = 上游右键菜单扩展机制 |
| `e479e43` | 弹窗摘除实验（11 文件 103 行） | 跨 5 个模块的云控开关 + `pref_names` 落地 |
| `b5d1c68` | AI 翻译扩展加按钮（24 文件 71 行） | 文件数多但 22 个是 PNG → **真代码只 2 文件，别当大活讲** |
| `86f9b69` | 论坛加获取系统信息接口（2 文件 84 行） | `appcmd_handler` = 网页调 C++ 的入口（与 q-fw 的 `HandleAppCmd` **同一模式**） |
| `22af5e5` | 屏保推广优化二期（3 文件 24 行） | `installer/tdsetup` 安装器层 |

### 🥉 C 档：一行改动 / 云控开关 / Revert（15 个）

`350c023`（1 行）、`996d068`（1 行）、`07ffca4`（1 行）、`0fa147e`（2 行）、`ee35e4e`（1 行）、
`a32f67b`（4 行）、`903b79a`（1 行）、`d94a945`（1 行）、`cf0ce8b`（3 行）、`4a722f9`（30 行 fixbug）、
`9c8f382`、`7cc86b4`、`51ee6e5`、`480651d`、`1ce3fe2`/`d5c30b8`/`47cbb71`（Revert）

⚠️ **这 15 个不是没价值，是不能单独拿出来讲。**
正确用法：**合起来讲「云控开关体系」**——360 浏览器的实验/灰度是怎么做的，
`se_profile.cc` 为什么被反复改，一个实验从开关到全量走什么流程。
**这是一个话题，不是 15 个话题。**

---

## 二、A 档三个提交的技术内核（教练实读源码，可核）

### A1 · `04fd0d1` 网页打不开需求 —— 他手里最值钱的一个提交

**改动范围（9 文件）**：

```
chrome/browser/360/query_data/query_data_service.cc    +3
chrome/browser/360/se_browser_mixin.cc                 +6
chrome/browser/360/se_core_tab_helper.cc              +63   ← 主要逻辑
chrome/browser/360/se_core_tab_helper.h                +3
chrome/browser/ui/sad_tab_helper.cc                   +12   🔴 上游
chrome/browser/ui/views/sad_tab_view.cc                +6    🔴 上游
chrome/browser/ui/webui/360/seerrors/se_errors_ui.cc  +59
chrome/browser/ui/webui/360/seerrors/se_host_service.cc +8
chrome/browser/ui/webui/360/seerrors/se_host_service.h  +2
```

**`se_host_service.h` 全文（教练实读）**：

```cpp
enum class HostType {
  Cant_Open_Host_Type = 0, Internal_Network_Host_Type = 1,
  Dns_Error_Type = 2, Unknow_NetError_Type = 3, Switch_Host_Type = 4,
};

class SeHostService {
 public:
  static SeHostService* GetInstance();            // ← 单例
  void init();
  HostType GetHostType(const std::string& host);
  bool IsSwitchHostType(const std::string& host);
 private:
  void readFile();
  scoped_refptr<base::SequencedTaskRunner> GetFileTaskRunner();
  scoped_refptr<base::SequencedTaskRunner> file_task_runner_;   // 🔴 线程模型
  std::set<std::string> switch_hosts_;
  std::set<std::string> not_open_hosts_;
};
```

**🔴 面试官一定会挖的四个点（他目前全答不上名字）**：

1. **`base::SequencedTaskRunner` 是什么** —— Chromium 任务调度的核心类型。
   **它是什么**：一个「保证任务按投递顺序、在同一个序列上串行执行」的执行器。
   不保证同一个物理线程，只保证**不并发**。
   → 他用它把 `readFile()` 挪出 UI 线程。**他做对了，但不知道这叫什么、为什么必须这样。**
   → 面试追问链：为什么不能在 UI 线程读文件 → 卡的是哪个线程 → `SequencedTaskRunner` 和
   `SingleThreadTaskRunner` 差在哪 → 既然串行，那 `switch_hosts_` 还需要加锁吗？
2. **`scoped_refptr<T>` 是什么** —— Chromium 的引用计数智能指针（比 `shared_ptr` 早，侵入式）。
   → **与他 10-13 刚学的 `shared_ptr` 正好对照**：计数放在对象里 vs 放在独立 control block 里。
3. **单例 + 多线程** —— `GetInstance()` 在哪个线程被第一次调用？`init()` 和 `readFile()` 的时序。
4. **改上游 `sad_tab`** —— `sad_tab` 是 Chromium 的「页面崩了/加载失败」兜底页。
   他把它接到自己的 WebUI。**面试追问**：为什么不直接改 `sad_tab_view` 而要走 WebUI？
   WebUI 的 C++↔网页通信走什么（`mojo`? `WebUIMessageHandler`?）

**讲法差距（这就是他现在缺的那一档）**：

| 讲法 | 面试官反应 |
|---|---|
| ❌「我做了个网页打不开的需求」 | 业务需求，不追问，判 22K |
| ✅「替换上游 sad_tab 兜底页接自建 WebUI，host 分类数据要读本地文件，用 `SequencedTaskRunner` 挪出 UI 线程避免卡界面，单例 + 两个 `std::set` 做查表」 | 坐直，开始挖线程模型 |

### A2 · `64986ec` 添加新扩展 id 和关闭接口 —— 跨了三层上游

**实读到的两处改动**：

```cpp
// extensions/common/constants.h
+EXTENSIONS_EXPORT extern const char k360NewAIAssistExtensionId[];

// net/base/url_util.cc   ← 安全扩展白名单
static const char* _Security_Extension_List[] = {
   ...
+  "hhbobgeihfohcodnkfaelnicaekdeonj", //new ai assist
};
```

**`chrome/common/extensions/api/account360.json`（实读）**：
Chromium 的 **extension API schema**，`namespace: account360`，定义 `UserInfo` 类型
（`name`/`qt`/`qid`/`nickname`/`headurl`）与 `getAccount` 等函数。

**🔴 这里面有个他完全没意识到的知识点**：

**它是什么 · extension API 的「编译期代码生成」**：这个 `.json` 不是配置文件，
是**编译期被 `json_schema_compiler` 读走、自动生成 C++ 绑定代码**的源头。
生成物把 JS 侧的 `chrome.account360.getAccount()` 和 C++ 侧的
`Account360GetAccountFunction::Run()` 接起来。
→ **他改过这个文件，所以他亲手走过「JS 调 C++」的全链路，但从没把它当成一条链看。**
→ **这与 q-framework 的 `HandleAppCmd` 是同一个问题的两种答案**（真对照，不是类比）：
一个靠编译期生成绑定 + extension 权限系统，一个靠手写 handler + 字符串命令分发。

**面试追问链**：扩展 id 为什么要硬编码进 `net/` 的白名单（不是放配置）→
权限检查发生在哪一层 → `permissions_data.cc` 管什么 → 一个扩展想调 `chrome.account360`
要满足几个条件。

### A3 · `578c743` SE-AI 地址栏优化 —— 20 文件，改到了 `components/omnibox`

**改动文件（节选关键）**：

```
components/omnibox/browser/omnibox_edit_model.cc/.h       🔴 上游 omnibox 核心
components/omnibox/browser/omnibox_controller.h           🔴 上游
chrome/browser/ui/views/omnibox/omnibox_view_views.cc/.h  🔵 上游 views 层
chrome/app/chrome_command_ids.h                           命令 id
chrome/browser/ui/browser_command_controller.cc           命令分发
chrome/browser/ui/views/frame/system_menu_model_builder.cc 系统菜单
chrome/browser/ui/views/tabs/tab_strip.cc/.h              标签条
chrome/common/360/pref_names_360.cc/.h                    偏好项
```

**🔴 可讲点**：

**它是什么 · omnibox 的 model/view 分层**：`components/omnibox/browser/` 是**平台无关的
逻辑层**（edit model、controller、autocomplete），`chrome/browser/ui/views/omnibox/` 是
**Views 框架的呈现层**。他同时改了两边 → **他亲手跨过了 Chromium 最经典的一条分层线。**

**面试追问链**：为什么 omnibox 的逻辑放在 `components/` 而不是 `chrome/` →
`components/` 这一层的存在意义是什么（答案方向：可被 Chrome / WebView / 其他 embedder 复用）
→ 这就自然走到他上午答不出的那一问（`chrome/` vs `content/` vs `components/` 的分界）。

---

## 三、🔴 四层深挖链（排课骨架，与 q-framework 轨同规格）

> 用法：他自评「第几层开始答不上」，训练从那层排。
> **10-15 自评实测结果（上午六问）：第一层能答，第二层开始大面积空白。**

### 第一层 · 确认你真在里面干过 —— ✅ 基本能答

- 项目多大、你负责哪块、几个人 → 能答
- 编译一次多久？→ **他答「全编 4-5 小时，改一行几秒」** ✅
  ⚠️ 这个答案本身是**加分项**，因为它暗示他知道增量编译和链接的区别。
  **但他只调过 release/debug，没碰过 `gn args`** → 第三层要补。
- 崩溃怎么定位？→ **他答「尝试复现；用户现场收集 minidump，看过 minidump」** ✅ 及格
- ❌ **第一层唯一缺口**：**怎么跟上游 Chromium 版本？** 他答「merge，先用 AI 解，测出的 bug 人工查看」
  → 🔴 **这句面试不能这么说**，见第五节「讲法修正」。

### 第二层 · 确认你懂代码在哪一层 —— 🔴 训练起点（他答不出名字，但手干过）

1. **`chrome/` / `content/` / `components/` / `extensions/` / `net/` 各是什么，分界在哪？**
   （他 10-15 明确答「答不上来」，但实查他五层里改过四层）
2. 你改的那个功能在哪一层？**为什么必须在那一层？**
3. `components/omnibox/browser/` 和 `chrome/browser/ui/views/omnibox/` 为什么分两处？（A3 的现成例子）
4. **360 自有代码是怎么和上游并存的？**（`chrome/browser/360/` 这种目录 vs 直接改上游文件，
   两种做法的代价差别 —— 直接关联第一层那个 merge 问题）

### 第三层 · 这一层刷人 —— 与 q-framework 第三层天然合流

1. **进程模型**：你改的代码跑在哪个进程？Browser / Renderer / GPU / Utility 怎么分工？
   （⚠️ **这一问他已有 L2 证据**：09-19 画过进程模型图、09-23 三层链两问独立答对 →
   **这一问不重排，直接用他已有的答案，只补「你的代码落在哪个进程」这一句**）
2. **跨进程通信**：Mojo 是什么？`.mojom` 文件怎么定义接口？
   → 他 10-15 答「走 extension，我只看过一些 `.mojom` 文件」→ **看过不等于掌握，这是主训练点**
3. **线程模型**：UI 线程 / IO 线程 / ThreadPool 怎么分？
   → **A1 里他自己用过 `SequencedTaskRunner`** → **从他自己的代码进去，不从文档进去**
4. **沙箱**：Renderer 在沙箱里，你的功能要读文件怎么办？
   （⚠️ 他 09-20/09-23 已答对沙箱三层链 → 这里只补「Chromium 侧的具体机制」）
5. **扩展 API 全链路**：`account360.json` → 编译期生成 → C++ 实现 → JS 调用，这条链走完
   → **A2 的现成例子**

### 第四层 · 加分项（新方向下**升为必答**，与 q-fw 第四层同批）

1. **GN / `gn args`**：component build 是什么？为什么改一行只要几秒？
   `is_debug` / `is_component_build` / `symbol_level` 各管什么？
2. **minidump 深一层**：怎么拿符号表？`!analyze -v` 看什么？栈回溯断了怎么办？
3. **上游 merge 的工程化**：patch 管理、冲突定位、回归测试
4. **性能**：怎么抓 trace（`chrome://tracing`）？卡顿定位到哪一层？

---

## 四、两条线的关系（不是两份工作，是一个话题的两面）

| 同一个问题 | 360 浏览器的答案 | q-framework 的答案 |
|---|---|---|
| JS 调 C++ | extension API（`.json` schema 编译期生成绑定）+ `appcmd_handler` | `HandleAppCmd`（手写 handler + 字符串命令分发） |
| 多进程 | Chromium 原生（Browser/Renderer/GPU/Utility） | CEF 包装的 Chromium 多进程 |
| 跨进程通信 | Mojo | CEF message router + 自写 `ipc/`（IOCP 命名管道） |
| 任务调度 | `base/task/`（他 A1 用过 `SequencedTaskRunner`） | 同一套 `base/`（Chromium 搬来的） |
| 崩溃收集 | Crashpad（上游） | `crashpad/` + `breakpad/` **两套并存** |
| UI | Views + WebUI + 皮肤 XML | DuiLib + CEF/WebView2 + Lynx |
| 构建 | GN + Ninja（上游全套） | GN + Ninja（搬来的） |

**🔴 这张表就是他简历的真正骨架**：
不是「我做过两个项目」，而是**「同一套 Chromium 技术栈，我在两种形态下都落地过」**
—— 一个是直接改内核，一个是嵌入内核。**这个讲法值 28-32K，「我做过两个项目」值 22K。**

**另一层价值**：`base/` 是同一套。他在 q-framework 里学 `base/`（大项 11 扫重复轮子），
学到的东西**在浏览器里直接能用**，反之亦然。**两条线共享地基，不是两份工作量。**

---

## 五、🔴 讲法修正（教练判定：会直接掉分的三句）

> 这一节不是知识，是面试表达。他 10-15 的六问答案里挑出来的。

| 他现在的说法 | 问题 | 怎么说 |
|---|---|---|
| 「merge，先用 AI 解，测出的 bug 人工查看」 | **会被判不懂版本管理**。AI 解冲突这件事本身没错（2026 年很常见），但这么说等于「我不知道冲突为什么产生、也不知道解对没解对」 | 先说**机制**：我们 fork 上游，按版本 merge，360 自有代码尽量放 `chrome/browser/360/` 这类独立目录降低冲突面，直接改上游文件的地方是冲突高发区；再说**工具**：冲突用 AI 辅助定位，但判断留给人，回归靠测试。**顺序是「机制 → 工具」，不是只报工具** |
| 「我做了个网页打不开的需求」 | 业务口径，面试官不追问 | 见 A1 表格最后两行 |
| 「我只看过一些 `.mojom` 文件」 | 诚实但等于弃权 | 真实情况是「我的功能走 extension API 这条路，没写过 `.mojom`，但 Mojo 的作用和定位我清楚」—— **先划清边界，再给出已知的部分**。⚠️ 要等第三层训练完才能这么说，**现在不能说** |

---

## 五点五、🔴 23:00 补查：`content/` 不是一个提交的事，是 7 个提交 22 个文件

（本节接第零点五节的 S 档，因在第五节之后补写，编号排在此处）

教练 19:0x 只看了 `8beac32` 一个提交。23:00 全分支按目录重查（`E:/code/browser/src`，可核）：

```bash
git log --all --author=ningxinyang --oneline -- content/            # → 7 个提交
git log --all --author=ningxinyang --name-only --pretty=format: \
  | grep '^content/' | sort -u | wc -l                              # → 22 个不同文件
```

22 个文件全名（上面 S 档那 16 个 **之外**还多出 6 个）：

```
content/browser/download/download_manager_impl.cc      ← 新增
content/browser/plugin_list.cc                         ← 新增
content/browser/plugin_process_host.h                  ← 新增
content/browser/plugin_service_impl.cc / .h            ← 新增
content/browser/render_process_host_impl.h             ← 新增（S 档只记了 .cc）
```

**对排课的意义**：原判断「`content/` 是孤例，只够讲一课」**不成立**。
`plugin_service_impl` 那组是**插件进程**（`PluginProcessHost`），
`download_manager_impl` 是**下载线程模型**，和 S 档的**进程隔离决策**是
`content/` 层三个不同子系统 —— **浏览器线第二层的教材量够撑整周，不用借官方文档的陌生例子。**

### 五层各自的「不同文件数」（23:00 实跑，10-16 开场课用这组数）

```bash
for d in chrome components extensions net content; do
  git log --all --author=ningxinyang --name-only --pretty=format: \
    | grep "^$d/" | sort -u | wc -l
done
```

| 层 | 他改过的不同文件数 | 主要落点 |
|---|---|---|
| `chrome/` | **365** | `chrome/app/theme` 100 ／ `chrome/browser/360` 72 ／ `chrome/browser/ui` 65 ／ `chrome/installer/tdsetup` 27 ／ `chrome/installer/mini_installer` 19 ／ `chrome/browser/360se` 13 |
| `components/` | **30** | `download/`（含 `360/p2sp_download_wrapper.cc`）／`omnibox/`／`crash/core/app/crashpad.cc`／`360se/update/`／`bookmarks/`／`content_settings/` |
| `content/` | **22** | 见上节 |
| `extensions/` | **13** | `common/constants.*`／`browser/extension_host.cc`／**`common/mojom/external_api.mojom`**（提交 `d70cc09c`「支持登录」） |
| `net/` | **1** | `net/base/url_util.cc` |

**两条可直接出题的反差**：
- **365 : 22 = 16 倍** —— 他的工作量主要在产品层，但**技术含量最高的在 `content/`**。
  「文件数的分布」和「技术含量的分布」不是一回事 → 出成 B2。
- **他已经改过 `.mojom`**（`extensions/common/mojom/external_api.mojom`），
  而此前判断是「他只看过 `.mojom`」—— **改过和看过不是一回事**，W10 Mojo 那课的起点要重估。

---

## 六、排期（10-16 起，与 q-framework 轨并行）

> 下午 17:00-17:50 整格 50min。**两条线不平分，按「哪条更缺」动态给**。
> 本周先走完 q-fw 第二层收口（10-15 已完成），**浏览器线 10-16 起开场**。
>
> 🔴 **10-15 23:00 冲突消解备案**：`plan/weekly/week-06.md` 第 44 行原给 10-16 下午排的是
> 「复测补漏 + q-fw 第三层开场」，与本表此行**撞格**。已定：**10-16 下午归浏览器线**，
> ~~**q-fw 第三层开场顺延 10-17 的 4h 深度档**~~。
> `week-06.md` 已同步改，原文划掉保留。
>
> 🔴 **10-16 23:00 二次更正（教练账）**：把 q-fw 第三层开场并进 10-17 的 4h **是又一次撞格** ——
> 10-16 晚重算容量，4h = 240min 已被五格装满（B1-B4 补做 / 简版 `shared_ptr` / `base/` 扫轮子 /
> q-fw 第四层 Q6-Q7 + 两方对照 / 复测补漏），**再加第三层开头就是排不下的**。
> **撤回该并入**：q-fw 第三层开场**回归 `docs/q-framework-track.md` 原位 W7 第三层①**（下表 W7 行已写明）。
> ⚠️ 另：**10-16 下午这一格本人整格零交卷**（16:40 说「现在就开始」，16:44 题面发出后至 23:00 零回话，
> 原因未说明）→ **10-16 那格原题原验收标准整体挂 10-17 第一节 45min 补做，不作废。**


| 日期 | 下午那格 | 对应层 | 备注 |
|---|---|---|---|
| **10-16 五** | ~~**浏览器线开场**~~ 🔴 **整格零交卷**：五层定义（3.1）与实查文件数（3.2）已全给，B1-B4 本人一问未答，**原因未说明** | 浏览器第二层① | 题面 16:44 发出，至 23:00 零回话。**原题挂 10-17 补做** |
| **10-17 六** | 4h 深度档 **=五格 240min（10-16 23:00 重算，恰好装满）**：①**B1-B4 补做 + W4-7 判据题 45min** ②简版 `shared_ptr` 85min ③`base/` 扫轮子 50min ④q-fw 第四层 Q6-Q7 + CEF/WebView2 两方对照 40min ⑤复测三处补 R1/R5/R6 + 证据设计重做 20min | 浏览器第二层①补 | **q-fw 第三层开场不在此格**（撤回并入，回归 W7） |
| **10-18 日** | 2h 复盘 + 重写 W4/W5/W6 门禁 + **把两条线写进 W7 计划**（现 `week-07-to-24-outline.md` 只有 q-fw 单线，教练账） | — | |
| **W7** | 浏览器第二层②③④（他的功能在哪层 / omnibox 两处分层 / 360 自有代码与上游并存）+ **浏览器 S 档第一课：`SiteInstance`/`SiteInfo`/`RenderProcessHost`/`RenderFrameHostManager`/`ChildProcessSecurityPolicy` 五类 + Site Isolation 决策链闭卷（10-17 升为首项，简历行解锁条件）** + **q-fw 第三层①（CEF 两进程各自职责 / 谁先起 / 谁创建谁 —— 10-16 从 10-17 撤回至此，回归原位）** | 第二层收口 | |
| **W8** | **A1 深挖：`SequencedTaskRunner` + 单例 + sad_tab 替换**（上午 C++ 正好在学 `mutex`，**天然合流**）+ q-fw 第三层② | 浏览器第三层③ | |
| **W9** | **A2 深挖：扩展 API 全链路**（`.json` → 生成 → C++ → JS）+ q-fw 第三层③（`ipc/`） | 浏览器第三层⑤ | 两条线同讲「JS 调 C++」，**对照表现成** |
| **W10** | **Mojo**（他只「看过 `.mojom`」，这是最大单点缺口）+ q-fw 第三层④ | 浏览器第三层② | |
| **W11** | **GN / `gn args` / component build**（为什么改一行几秒）+ q-fw 第四层①（crashpad/breakpad） | 两线第四层 | |
| **W12** | **minidump 深一层 + 上游 merge 工程化** + 两条线吃透笔记定稿 | 两线第四层 | |

**硬约束（防教练缩水，沿用 09-16/09-21 他立的规矩）**：
- 50min 是保底不是上限
- 不许用「今天不做 X」切知识点，只分「主线必补」与「扩展项」，扩展项须写进当日记录
- **每个非当日主角的概念必须标一行「它是什么」**（他 09-20 立的硬规矩）
- 浏览器侧出题**优先用他自己的 23 个提交当教材**，不用官方文档的陌生例子

---

## 七、待查线索（跨周保留）

- `chrome/browser/360/external_apis/appcmd_handler.cc` —— 他改过两次（`86f9b69`、`e479e43`）。
  **这个文件名和 q-framework 的 `HandleAppCmd` 高度同名** → 待查：是不是同一套设计思路，
  甚至同一个人写的（q-fw 里 `Cheng Zhao` 有 202 次提交这条线索也还挂着）
- `components/download/` 他改过 3 个提交（含两个 Revert）→ 下载模块的线程模型是现成的第三层教材
- `se_browser_mixin.cc` 的 "mixin" 命名 —— Chromium 里 mixin 是什么模式，待确认后再出题
- ⚠️ **教练未验证项**：本人自述「全编 4-5 小时」未实测（他的机器、他的实感，**采信不复验**）

---

## 八、🔴 事实更正（2026-10-22 · 本人实查推翻教练断言）

### 更正 1 · integrity level 表里「utility = Medium」是教练写错的

10-21 23:xx 我（教练）给的那张表写着「network / utility | Medium」，把 utility 整个进程类型
标成了 Medium。**本人 10-22 上午查源码推翻。实查结论（已逐字核对，可复现）：**

`src/docs/design/sandbox.md:283-285` 原文：
> "At M75 the browser, crash handler, and **network** utility processes run at Medium integrity,
> the GPU process at Low and most remaining services including isolated renderers at Untrusted."

- Medium 只点了 **network utility 这一个 service**，不是整个 utility 进程类型。
- **utility 是「进程类型」的名字，不是一个权限等级。** 同一个进程类型里承载不同 service，
  每个 service 各自声明自己的沙箱类型（mojom 里的 `[ServiceSandbox=...]` 注解）。
- `src/chrome/common/importer/profile_import.mojom:88` →
  `[ServiceSandbox=sandbox.mojom.Sandbox.kNoSandbox]`
  书签导入这个 service **根本没有沙箱**，比 Medium 还宽，也比 GPU（Low）宽得多。
- 文档里同句话的 "most remaining services ... at Untrusted" 说明：
  **多数 service 是 Untrusted**，Medium 是例外不是常态。

👉 讲法：面试里不能说「utility 进程是 Medium」。要说「utility 是进程类型，
沙箱按 service 粒度声明，network service 是 Medium，profile import 是 kNoSandbox，
多数 service 是 Untrusted」。

### 更正 2 · 「代码是我们写的所以安全」这个解释不成立（本人自己反掉的）

本人 10-22 原话（采纳）：「恶意数据也可能利用解析漏洞，把原本可信的程序变成攻击者控制的程序，
所以『代码是我们写的』不足以解释 Medium。」—— 正确。输入不可信就意味着解析器是攻击面，
与解析器由谁编写无关。**这条推理要保留进面试话术，它比记住等级表值钱。**

### 本人尚未答出的那一问（挂到 W8）

为什么这个 service 能配 kNoSandbox / 沙箱化会死在哪 —— 要落到具体系统调用上，不是落到「配置如此」。
实查到的证据（教练 10-22 实跑 grep，行号可核）：
- `chrome/utility/importer/ie_importer_win.cc:252, 554, 607, 618`
  → `base::win::RegKey` 直开 `HKEY_CURRENT_USER` / `HKEY_LOCAL_MACHINE`
- `chrome/utility/importer/firefox_importer.cc:648-657`
  → 从**别的浏览器的 profile 目录** `base::CopyFile` 出 `places.sqlite` 等文件
- 对照 `src/docs/design/sandbox.md:419-433`（App Container / Low Box token）：
  低权限 token 只剩 `SeChangeNotifyPrivilege` + `SeIncreaseWorkingSetPrivilege`，
  且不给 Capability 就**连网络都访问不了** → 读任意注册表键、读任意用户目录文件都做不到。
