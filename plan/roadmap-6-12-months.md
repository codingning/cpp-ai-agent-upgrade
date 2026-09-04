# 半年路线图：Windows C++ AI 推理基础设施与高级工程能力

## 目标边界

半年目标不是保证职位头衔，而是达到一组可核验的能力证据：能在 Windows/MSVC 上独立设计、实现、测试、调试和解释一个中等规模 inference runtime workbench；能复现和局部改造 ONNX Runtime/llama.cpp，处理张量与内存、并发调度、性能、ABI、错误和可观测性；最后用一个本地 Agent 展示层证明 runtime 的可用性。

每天最低 1 小时，按 24 周滚动推进。没有学习的日子只记录缺席，不追赶；有空时再补最小未完成单元。

## 岗位证据校准规则

岗位调研只统计北京及目标城市中可核验的近期样本：优先“一周内招聘者活跃”，其次“一个月内仍有活跃信号”；必须确认页面仍显示“招聘中”。仅有搜索引擎摘要、无活跃时间、已关闭或疑似长期复用的职位，只作为背景材料，不作为能力需求的计数依据。每四周复核一次岗位关键词，避免路线被过时 JD 带偏。

## 24 周分段

| 周次 | 阶段 | 必须产出 | 进入下一阶段门禁 |
|---|---|---|---|
| 1–4 | C++ 对象模型与可复现工程 | RAII、拷贝/移动、STL、错误模型；CMake Presets、CTest、诊断器 | 核心项达到 L2–L3；MSVC Debug/Release 构建测试可复现 |
| 5–8 | 并发、内存与性能基础 | 队列、线程池、取消/关闭；tensor/arena、缓存与 matmul Benchmark | 无明显泄漏；线程可回收；正确性、吞吐和尾延迟有基线 |
| 9–12 | ORT 基线与 Windows 系统边界 | C++ runner、EP/内存/线程/profiling 对照；DLL/API/ABI、转储 | 固定模型端到端运行；性能口径、坏输入和崩溃路径可诊断 |
| 13–16 | llama.cpp 与 LLM 推理机制 | model/context、Tokenizer、attention、prefill/decode、KV Cache、量化与 `llama-bench` | 固定 commit 基线；最短调用链图；至少一个 instrumentation 或小修复 |
| 17–20 | 主项目二期：优化、可观测与部署 | SIMD/多线程/批处理对照、日志/指标/trace、Windows 打包与兼容 | 有 flame graph 或等价 profiler 证据、SLO、回归门禁和新机复现 |
| 21–24 | 展示层与求职总验收 | 本地 Agent 调用自研 runtime；工具权限、结构化输出、人工审批；与固定 llama.cpp/ONNX Runtime 版本对照 | 作品演示、架构图、3 份 ADR、证据账本和 20 分钟答辩通过 |

## 训练营项目对标

| 训练营项目 | 对标方式 | 半年内定位 |
|---|---|---|
| AI 数字人 | 阅读实时音视频、音视频管线、推理和调度架构；实现一个非实时的音频/文本管线切片 | 架构参照或后续扩展，不作为主项目 |
| 从零构建 PR Agent | 读取 diff、调用工具、结构化审查、证据引用、人工审批 | **展示层，证明 runtime 可被应用调用** |
| 视频会议 | 阅读 Qt/音视频/WebRTC/网络并发架构；完成单机媒体管线或信令模拟 | 架构参照，不在半年内做完整会议系统 |
| mini-llama.cpp | 张量、Tokenizer、Transformer 前向、KV Cache、采样和 Benchmark | **核心源码线，为 workbench 提供 LLM 运行时证据** |

## 主项目选择

主项目固定为“Windows C++ inference runtime workbench”，使用 Adapter 统一 ONNX Runtime 和 llama.cpp，加入有界调度、取消、内存/指标和故障注入。它比从零重写完整 Transformer 更能在半年内形成可信工程证据，同时保留 toy tensor/matmul/量化组件验证底层理解。Agent 是最后 4 周的薄展示层，不独立扩展成平台。

若第 12 周发现数学或硬件先修不足，不切换项目，而是缩小模型范围：保留 tensor、matmul、量化、Tokenizer、采样和调度证据，延后完整 Transformer 前向。

## 架构能力验收

第 24 周必须提交：

- 一张组件/数据流/并发边界架构图；
- 至少 3 份 ADR，记录关键取舍和未选方案；
- 接口、错误模型、取消/超时和关闭协议；
- 测试矩阵、故障注入、性能基线和已知限制；
- 一次 20 分钟口头设计说明，能够回答容量、尾延迟、恢复、权限和演进问题。

## 设计模式与岗位闭环

设计模式不单独背诵，必须在项目中留下“问题—约束—模式—替代方案—成本—测试”的记录。优先覆盖与 runtime 直接相关的 RAII、Strategy、Factory、Registry、Adapter、Pipeline、Thread Pool、Arena、对象池和插件边界；Agent 层再按需使用 Command、Middleware 和 State。避免为了覆盖名词引入 Observer、Event Bus 或复杂继承。

每四周完成一次近期岗位抽样复盘：标记岗位状态、活跃时间、技能关键词、对应项目证据和当前缺口。岗位调研的结果只能调整后续训练优先级，不能替代代码、测试和性能证据。

## 简历验收

只有绑定 commit、构建命令、测试结果、性能数据和个人贡献的条目才进入简历。课程、题库、AI 生成代码和只读源码不单独算项目经验。
