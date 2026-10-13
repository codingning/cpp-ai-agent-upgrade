# `F:\code\vite_react\vite-project` 文件地图

> 建立日期：2026-10-13（W6D2）
> 起因：本人原话「这个项目是用命令行生成的，我只改过 `App.tsx`，其他文件碰都没碰过，
> 更不知道作用是什么」。教练认账：项目建了 15 天（09-29），从没给过一张文件级地图。
> 维护规矩：教练只写「它是什么 / 谁读它」，不写任何需要本人掌握才算数的结论。

---

## 0. 先记住一件事：这个工程里有两个世界

```
构建时世界（你现在这台机器上的文件）        运行时世界（Electron 真正加载的东西）
─────────────────────────────────         ──────────────────────────────────
index.html  ┐                              dist/index.html
src/main.tsx├─→ npm run build ─→ dist/ ─→ dist/assets/*.js   ← 窗口里装的是这个
src/App.tsx │                              dist/favicon.svg
src/*.css   ┘
                ↑ 只有被 main.tsx 依赖链拉到的文件才进得来
```

**`src/` 里改了东西，`dist/` 不会自己变。** 这就是 10-12 断点 4 的本质：
他改的是源码 `index.html`，窗口装的是 09-28 的 `dist/`，所以点什么都没反应。

**例外（运行时世界同时读构建时世界）**：`main.cjs` 和 `preload.js` 是 Electron 直接读的，
**不经 Vite 打包**。所以这两个文件改完不用 build，重开 Electron 就生效。
→ 这条是判断「改完要不要重新 build」的判据。

---

## 1. 谁启动谁（一次 `npm run start` 的完整链路）

```
npm run start = npm run build && electron .
   │
   ├─ ① npm run build = tsc -b && vite build
   │     ├─ tsc -b        读 tsconfig.json → 两个子配置，只做类型检查（noEmit，不产 js）
   │     └─ vite build    读 vite.config.ts + index.html，把 src/main.tsx 依赖树打进 dist/
   │
   └─ ② electron .        读 package.json 的 "main" 字段 → 主进程入口 = main.cjs
         └─ main.cjs  app.whenReady() → new BrowserWindow → loadFile(dist/index.html)
               │                        │
               │                        └─ 渲染进程：跑 dist/assets/*.js（就是被打包的 App.tsx）
               │                           这一步用不用 preload.js？看 webPreferences.preload
               └─ 主进程：三个 ipcMain.handle + 一个 ipcMain.on 在这里注册
```

---

## 2. 根目录文件逐个说

| 文件 | 是什么 | 谁读它 | 现状态 |
|---|---|---|---|
| `package.json` | 工程身份证。`"main": "main.cjs"` 决定 Electron 从哪启动；`scripts` 是 `npm run X` 的 X→命令表；`dependencies`/`devDependencies` 是依赖清单 | npm、Electron | 09-29 你加了一个 `"main"` 字段，其余是生成的 |
| `package-lock.json` | 依赖的**精确版本锁**（1438 行，记着每个包的 sha512）。有它，换台机器 `npm install` 装出一模一样的版本 | npm 自动读，**不要手改** | 未动 |
| `package copy.json` | **废文件**。文件名里带空格，是 `npm init`/手工复制留下的副本 | 没人读 | 建议删 |
| `index.html` | ① Vite 的**构建入口**（Vite 默认就找根目录这个文件，不需要配）② 你在第 5 行手写了个 `<button>` —— ⚠️ **写在 `<head>` 里，且不在任何 React 组件内** | Vite（构建时） | 有你的改动，未 commit |
| `vite.config.ts` | Vite 的配置。现在只有两项：`plugins:[react()]`（让 Vite 会转 JSX）、`base:'./'`（09-22 你自己加的，修 `loadFile` 下绝对路径白屏） | Vite | 你自己改过 |
| `tsconfig.json` | **空壳转发**。只有 `references` 指向下面两个，自己没有 `compilerOptions` | tsc | 未动 |
| `tsconfig.app.json` | `src/` 的 TS 规则。`include:["src"]`。关键项：`jsx:"react-jsx"`（JSX 怎么转）、`noEmit:true`（只查类型不产文件）、`noUnusedLocals`（声明不用的变量报错） | tsc | 未动 |
| `tsconfig.node.json` | `vite.config.ts` 自己的 TS 规则（`include:["vite.config.ts"]`）。为什么要单开一个：**构建工具跑在 Node 里，和目标浏览器环境不是一回事**，`lib:["ES2023"]` 没有 DOM | tsc | 未动 |
| `.npmrc` | npm 镜像源配置。`registry=npmmirror.com` + `electron_mirror` —— 有你这条才下得动 Electron 那 200MB | npm | 未动 |
| `.oxlintrc.json` | linter 规则。`npm run lint` 读它 | oxlint | 未动 |
| `.gitignore` | 哪些文件不进 git。⚠️ **`dist` 在里面** → dist 是产物不该进库；但这造成一个后果：**别人 clone 下来没有 dist，必须先 build 才能跑** | git | 未动 |
| `README.md` | Vite 模板原样自带的说明，从没改过 | 人 | 未动 |
| `main.cjs` | **Electron 主进程入口**。职责：建窗口、注册 IPC。注意 `.cjs` 后缀 —— 因为 `package.json` 里 `"type":"module"` 把所有 `.js` 变成了 ES 模块，主进程要用 CommonJS 就得显式写 `.cjs` | Electron | 你昨天改过（+4 处未 commit） |
| `preload.js` | **预加载脚本**。跑在渲染进程里、但持着 Node 能力，是主/渲染两个世界之间唯一的合法信道。`contextBridge.exposeInMainWorld('electronAPI', {...})` 在这里 | Electron | 你昨天新建 |
| `renderer.js` | **废文件**。你昨天写的按钮监听，`grep -rn "renderer.js"` 全工程零命中 —— 没人加载它，一行都没跑过 | 没人读 | 建议删 |
| `scripts/electron-smoke.cjs` | 冒烟测试。`npm run test:electron` 跑它：用 `spawnSync` 起 Electron，塞 `ELECTRON_SMOKE_TEST=1` 告诉 main.cjs 去检查 `#root` 有没有渲染出来，然后自动退出 | node | 09-23 建的 |

## 3. 目录

| 目录 | 是什么 |
|---|---|
| `src/` | 源码。**唯一进 Vite 构建的目录** |
| `src/main.tsx` | React 入口。`createRoot(document.getElementById('root')!).render(<StrictMode><App/></StrictMode>)` —— 这 10 行是「React 怎么接管页面」的全部答案 |
| `src/App.tsx` | 根组件。你唯一改过的文件 |
| `src/index.css` | 全局样式，被 `main.tsx` 第 3 行 `import './index.css'` 拉进来 |
| `src/App.css` | ⚠️ **死文件**：`grep -rn "App.css" src/` 零命中，没有任何文件 import 它 |
| `src/assets/` | 被 `import` 的资源（这类才进 `dist/assets/` 并带哈希） |
| `public/` | 原样复制到 `dist/` 根下，**不加哈希**（09-22 你自己实测出来的） |
| `dist/` | Vite 构建产物。`main.cjs` 第 18 行加载的就是这里 |
| `node_modules/` | 装好的 2000+ 个包。Electron 的 exe 在 `node_modules/electron/dist/electron.exe` |
| `.git` | 版本库。远端 `codingning/vite-electron-practice`，分支 main |

---

## 4. 三个待你亲手验的判断（今天不跑就明天早上跑）

1. **改 `App.tsx` 后必须 build 才生效，改 `main.cjs` 不用** ——
   验法：跑 `npm run start` 看到界面 → 改 `App.tsx` 里一行标题 → 直接 `npm run start:electron`（不 build）→ 看不看得见；
   再改 `main.cjs` 里一句 `console.log` → 直接 `npm run start:electron` → 看不看得见。**两次对照，结论抄进记录。**
2. **`src/main.tsx` 是不是唯一入口** ——
   验法：`index.html` 里那行 `<script type="module" src="/src/main.tsx">` 是 Vite 唯一认的入口；
   试着把它临时注掉（改完记得改回），build 后看 `dist/assets/` 里还有没有 js。
3. **`renderer.js` 和 `App.css` 到底死没死** ——
   验法：`grep -rn "renderer.js\|App.css" --include="*.tsx" --include="*.ts" --include="*.html" --include="*.css" .`
   （排除 node_modules）。零命中 = 死文件。**这是你自己下的判据，不是抄我的。**
