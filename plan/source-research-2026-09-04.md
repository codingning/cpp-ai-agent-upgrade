# Windows C++ AI 推理基础设施训练：一手资料与路线校准（2026-09-04）

## 结论

不应上来就盲写代码，但也不应先连续数周只看课程。更合适的最小闭环是：

> 岗位问题 → 概念导读 → 定向阅读优秀源码 → 复现基线 → 最小实现或修改 → 正确性与性能测试 → 口头解释与证据归档

每个主题都必须在一周内走完这个闭环。阅读的目的不是“看完”，而是带着问题找到资源所有权、调用链、线程边界、内存流向和可测假设；代码的目的不是刷数量，而是验证刚读到的机制。

当前路线的两个关键调整应是：

1. 把“PR Agent + 本地工具运行时”从半年主项目降为后期展示层；主项目改为 **Windows 本地推理运行时工作台**，直接覆盖模型加载、Execution Provider、内存复用、调度、取消、批处理、性能与可观测性。
2. 把 `safe_name()`、`first_duplicate()` 从 RAII 任务中移出。它们可以算字符串/STL 热身，但不是资源生命周期训练。第一周应围绕文件、进程或模拟资源句柄完成 move-only RAII 封装，并与 WIL 源码对照。

## 证据边界

- 本报告只把官方文档、上游源码仓库和雇主自有招聘页作为事实来源。
- 招聘页是 2026-09-04 的定向样本，不是完整市场统计；岗位可能随时关闭。可访问性受 Workday 动态渲染和地区限制影响时，不把搜索摘要当作长期事实。
- 路线中的时间配比和项目取舍是根据这些事实做出的建议，不冒充官方结论。

## 当前岗位信号

| 雇主岗位样本 | 一手要求 | 对训练路线的含义 |
|---|---|---|
| [NVIDIA 上海：Software Engineer, LLM Inference（JR2004439）](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Software-Engineer--LLM-Inference_JR2004439) | C/C++、软件设计、调试、性能分析、测试设计、PyTorch；开发跨平台推理软件并做性能优化 | 不能只做语言题和 API 调用；每个项目必须有 profiling、测试和跨平台构建证据 |
| [NVIDIA：Senior Software Engineer - Local AI（JR2021826）](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-Software-Engineer---Local-AI_JR2021826) | Windows/Linux PC，本地推理；ONNX Runtime、TensorRT、llama.cpp、vLLM；CUDA、DirectX、Vulkan；量化/剪枝/蒸馏与端到端优化 | Windows 本地推理是有效方向；作品应同时展示运行时、硬件接口和性能—精度取舍 |
| [NVIDIA：Senior System Software Engineer - Local AI（JR2021893）](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/Senior-System-Software-Engineer---Local-AI_JR2021893) | 调度、内存管理、KV cache、图执行、量化、硬件感知优化；性能/精度 sweep；开源贡献 | 训练不能停留在“跑通模型”；需要进入 runtime internals，并留下可复现实验或上游贡献 |
| [AMD 上海：AI Framework Eng.（78999）](https://careers.amd.com/careers-home/jobs/78999?lang=en-us) | Linux 下 C++，GPU kernel，HIP/CUDA/ASM，框架集成，调试、性能、测试，LLVM/ROCm | 只会 Windows API 会缩窄岗位面；Windows 主练，同时保留 WSL2/Linux、Clang/GCC 和 GPU 基础 |
| [Arm：Senior Software Engineer – ML Inference Runtime（2026-19003）](https://careers.arm.com/job/galway/senior-software-engineer-ml-inference-runtime/33099/100035000640) | C/C++/Python、CI/自动测试，以及 tokenization、attention、KV cache、batching、quantization、llama.cpp、profiling、图/编译器与 Vulkan | 推理原理、C++ 工程、性能工具和源码贡献必须并行推进，不能串成互不相干的课程 |

这些样本共同指向六类核心证据：

1. 现代 C++ 与可靠工程；
2. Transformer 推理机制；
3. 主流运行时源码阅读与局部改造；
4. latency、throughput、内存和精度的可复现测量；
5. CPU/GPU 与硬件感知优化；
6. CI、测试、文档和开源协作。

Agent、MCP、工具调用可以保留，但它们不应挤占上述主线。

## 每个训练单元应该怎样安排

### 默认 60 分钟单元

| 环节 | 建议时间 | 必须留下的产物 |
|---|---:|---|
| 定义问题 | 5 分钟 | 一个可回答的问题，例如“这个 handle 在异常路径由谁关闭？” |
| 概念导读 | 10–15 分钟 | 3–5 条自己的话总结；注明尚不理解处 |
| 源码阅读 | 15–20 分钟 | 只读 1–3 个入口；画出最短调用链/所有权图 |
| 实验或修改 | 20–25 分钟 | 最小可编译改动、失败复现或基准复现 |
| 验证与回收 | 5–10 分钟 | 测试命令、结果、一个错误认识和下一问题 |

复杂主题可以跨多天，但不允许连续一周只有“看了多少页”。建议周循环为：概念与小实验 → 源码入口 → 基线复现 → 局部修改 → 测试/Benchmark → diff review 与口述。

### 源码阅读的硬规则

- 固定 tag 或 commit，不直接以不断变化的 `main/master` 作为训练基线。
- 每次只追一条问题链，最多阅读 2–4 个关键文件；不把“逛完整仓库”算完成。
- 读前写预测，读后写实际调用链、线程边界、所有权和错误路径。
- 必须做一个可观察验证：断点、日志、单测、失败注入或 benchmark 至少一个。
- 只有绑定源码位置、构建命令、实验结果和个人解释的阅读，才进入证据账本。

## 应学习的知识与一手入口

### 1. 现代 C++ 与 Windows 资源安全

先掌握对象生命周期、所有权、Rule of Zero/Move、异常安全和并发 RAII；不要把零散语法题当成主线。

- [C++ Core Guidelines：资源管理与 RAII](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-resource)
- [C++ Core Guidelines R.1：用资源句柄和 RAII 自动管理资源](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rr-raii)
- [C++ Core Guidelines C.20：能避免自定义默认操作时使用 Rule of Zero](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rc-zero)
- [C++ Core Guidelines CP.20：用 RAII 管理锁](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rconc-raii)
- [Microsoft WIL](https://github.com/microsoft/wil) 及其 [`resource.h`](https://github.com/microsoft/wil/blob/master/include/wil/resource.h)：Windows `HANDLE`、`HWND` 等资源的 move-only RAII 封装，是第一周最合适的窄范围优秀源码。

第一周练习应先用“假资源 + 可计数 deleter”写可确定测试，再接 `CreateFileW`/`CloseHandle` 或子进程 handle；这样可以安全验证恰好释放一次、移动后源对象为空、提前返回和异常路径不泄漏。

### 2. 构建、测试、静态/动态检查与 Windows 调试

- [Visual Studio 的 CMake Presets](https://learn.microsoft.com/en-us/cpp/build/cmake-presets-vs?view=msvc-170)：用同一套 preset 驱动 MSVC Debug/Release，并保留 WSL2 的 GCC/Clang preset。
- [CMake `GoogleTest` 模块](https://cmake.org/cmake/help/latest/module/GoogleTest.html) 与 [GoogleTest Primer](https://google.github.io/googletest/primer.html)：测试从第一个实验开始存在，不等到第六周才补。
- [MSVC AddressSanitizer](https://learn.microsoft.com/en-us/cpp/sanitizers/asan?view=msvc-170) 及其[已知限制](https://learn.microsoft.com/en-us/cpp/sanitizers/asan-known-issues?view=msvc-170)：Windows 原生做内存错误验证，并把不支持组合写进 preset/README。
- [Visual Studio C/C++ Code Analysis](https://learn.microsoft.com/en-us/cpp/code-quality/quick-start-code-analysis-for-c-cpp?view=msvc-170)：启用 C++ Core Check/clang-tidy，而不是只依赖编译通过。
- [Windows 用户态 dump](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/user-mode-dump-files) 与 [WPR/WPA](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/windows-performance-recorder)：把崩溃取证、CPU、线程调度和 I/O 分析做成项目门禁。
- [WSL 安装文档](https://learn.microsoft.com/en-us/windows/wsl/install)：用于 Linux 构建、GCC/Clang 兼容和 Linux-only 工具链验证；它是 Windows 机器上的第二验证环境，不是主环境替代品。

### 3. 推理运行时核心

先用 ONNX Runtime 学“通用图运行时”，再用 llama.cpp 学“LLM 专用执行路径”。两者能互相校准。

#### ONNX Runtime 主线

- [Execution Provider 架构](https://onnxruntime.ai/docs/execution-providers/)：理解图如何按硬件能力分区，而不是只记 provider 名字。
- [Windows 上的 ONNX Runtime / Windows ML 选择](https://onnxruntime.ai/docs/get-started/with-windows.html)：Windows 11 24H2+ 的 Windows ML 能辅助选择硬件执行后端；仍应理解底层 ORT C/C++ API。
- [图优化](https://onnxruntime.ai/docs/performance/model-optimizations/graph-optimizations.html)、[线程管理](https://onnxruntime.ai/docs/performance/tune-performance/threading.html)、[内存优化](https://onnxruntime.ai/docs/performance/tune-performance/memory.html)、[I/O Binding](https://onnxruntime.ai/docs/performance/tune-performance/iobinding.html) 和 [Profiling](https://onnxruntime.ai/docs/performance/tune-performance/profiling-tools.html)：直接对应运行时项目的实验矩阵。
- [官方 C/C++ inference examples](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/c_cxx)：先复现官方最小样例，再做自己的封装和测量。
- 定向源码入口：[`onnxruntime_cxx_api.h`](https://github.com/microsoft/onnxruntime/blob/main/include/onnxruntime/core/session/onnxruntime_cxx_api.h)、[`inference_session.cc`](https://github.com/microsoft/onnxruntime/blob/main/onnxruntime/core/session/inference_session.cc) 和 [`graph_partitioner.cc`](https://github.com/microsoft/onnxruntime/blob/main/onnxruntime/core/framework/graph_partitioner.cc)。第一次只回答“Session 初始化、图分区、Run 分别发生在哪里”。

#### llama.cpp 主线

- [llama.cpp 官方仓库](https://github.com/ggml-org/llama.cpp) 与[构建文档](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)：Windows 上先建立 CPU 基线，再按机器硬件选择 CUDA、Vulkan、SYCL 或 OpenVINO；不要一次打开所有后端。
- [`llama.h`](https://github.com/ggml-org/llama.cpp/blob/master/include/llama.h) → [`llama-model.cpp`](https://github.com/ggml-org/llama.cpp/blob/master/src/llama-model.cpp) → [`llama-context.cpp`](https://github.com/ggml-org/llama.cpp/blob/master/src/llama-context.cpp)：先追公共 API、模型和上下文生命周期。
- [`llama-kv-cache.cpp`](https://github.com/ggml-org/llama.cpp/blob/master/src/llama-kv-cache.cpp) 与 [`llama-batch.cpp`](https://github.com/ggml-org/llama.cpp/blob/master/src/llama-batch.cpp)：再追 KV cache、batch 和 decode 路径。
- [`llama-bench`](https://github.com/ggml-org/llama.cpp/tree/master/examples/llama-bench) 和 [`test-backend-ops.cpp`](https://github.com/ggml-org/llama.cpp/blob/master/tests/test-backend-ops.cpp)：任何修改前先复现固定模型、固定参数、固定 commit 的基线。

必须补齐的推理概念是：tensor shape/stride/dtype、算子图与图分区、内存 arena/复用、线程池与 affinity、tokenization、attention、KV cache、prefill/decode、batching、量化、采样、TTFT、tokens/s、吞吐—延迟—内存—精度取舍。

### 4. Windows 加速路线的取舍

- [Windows AI 总览](https://learn.microsoft.com/en-us/windows/ai/) 把 Windows ML 作为自定义 ONNX 模型和硬件加速的当前入口。
- [DirectML 官方说明](https://github.com/microsoft/DirectML) 已明确进入 maintenance mode；它仍被支持，但不再计划新增功能，样例和 issue 也不再更新。因此 DirectML 适合做兼容性阅读和历史架构对照，不适合作为半年主项目唯一地基。
- [OpenVINO](https://github.com/openvinotoolkit/openvino) 可作为 Intel CPU/GPU/NPU 比较后端；先用官方 [`benchmark_app`](https://docs.openvino.ai/2026/get-started/learn-openvino/openvino-samples/benchmark-tool.html) 做相同模型/输入的基线，不急着阅读整个实现。

如果训练机有 NVIDIA GPU，再把 CUDA/TensorRT 加为加速专项；如果没有，就先把 CPU cache、SIMD、线程与内存测量做扎实，避免用硬件缺失阻塞主线。

## 建议的 24 周主线

| 周次 | 学习与源码 | 项目产出 | 门禁 |
|---|---|---|---|
| 1–4 | 生命周期、RAII、move、STL；读 Core Guidelines 和 WIL 窄切片 | move-only Windows handle、Buffer、基础算法实验 | MSVC/clang-cl 构建；单测、ASan/静态分析；能解释所有权与错误路径 |
| 5–8 | 线程、条件变量、`jthread/stop_token`、队列/背压；读标准库接口与小型线程池实现 | 有界任务运行时、取消/关闭/超时；CMake Presets、CTest、CI、dump | 无悬挂线程；关闭幂等；失败注入；Windows + WSL2 构建 |
| 9–12 | tensor、图、EP、内存、线程、profiling；读 ORT API 和 Session/partitioner 入口 | ONNX Runtime C++ runner + benchmark harness | CPU/可用 EP 对照；warm-up、固定输入、p50/p95/p99、RSS；结果可重放 |
| 13–16 | tokenizer、attention、prefill/decode、KV cache、量化；读 llama.cpp API/model/context/cache/batch | 固定 commit 的 llama.cpp 基线、调用链图、局部 instrumentation | `llama-bench` 复现；至少一个可解释的测量或小修复；正确性不退化 |
| 17–20 | 调度、动态/连续 batching、内存复用、硬件后端、可观测性 | **Windows 本地推理运行时工作台**：ORT + llama.cpp Adapter、有限队列、取消、指标 | TTFT/tokens/s/吞吐/内存；超载、取消、坏输入、后端失败；架构图与 ADR |
| 21–24 | 性能—精度 sweep、CPU/GPU 专项、开源协作 | 优化前后报告、发布包、上游 issue/PR 或可审阅 patch；可选 Agent 展示层 | Windows 原生 + WSL2；固定模型/commit/命令；20 分钟讲解；简历证据齐全 |

## 主项目应怎样改

推荐名称：`windows-inference-runtime-workbench`。

最小架构：

- `IInferenceBackend`：ORT 与 llama.cpp 的 Adapter，不把第三方类型泄漏到业务层；
- `ModelRegistry`：模型、版本、license、输入 shape/dtype 与 backend capability；
- `RequestScheduler`：有界队列、超时、取消、关闭、优先级和可选 batching；
- `Buffer/TensorPool`：预分配与复用；ORT 路径实验 I/O Binding；
- `Metrics/Trace`：冷/热启动、TTFT、tokens/s、p50/p95/p99、CPU/RSS/VRAM、队列等待；
- `FaultInjection`：坏模型、坏 shape、OOM 模拟、取消竞争、backend crash/timeout；
- CLI 或极简 UI：只负责演示，不抢占运行时开发时间。

`PR Agent` 可以在第 21–24 周作为一个 workload：调用上述运行时分析 diff，展示结构化工具调用、权限和人工审批。这样 Agent 是“运行时能力的消费者”，不是替代推理基础设施主线。

`mini-llama.cpp` 不建议一开始从零重写完整 Transformer。先做固定版本的基线复现、调用链、KV cache/量化/内存实验和一个局部改造；只有这些完成后，再写 toy tensor/attention 组件来验证理解。

## 第一周可直接替换为下面的安排

1. **Day 1：工具链与问题建立**。验证 VS 2022、MSVC、CMake/Ninja、preset、CTest；读 Core Guidelines R.1 和 WIL `resource.h` 的一个 handle wrapper；画所有权状态图。只写 smoke test。
2. **Day 2：错误基线**。用假资源构造泄漏、double-close、提前返回三种失败；用计数和测试证明失败，不直接对真实系统资源做危险实验。
3. **Day 3：最小 RAII**。实现 move-only `unique_resource`/`unique_handle`，覆盖默认态、接管、移动构造、移动赋值、`reset/release/swap`。
4. **Day 4：源码对照**。与 WIL 和 `std::unique_ptr` 自定义 deleter 对照，记录为什么不允许复制、无效值如何表示、析构为何不能抛异常。
5. **Day 5：Windows 实战**。封装文件或子进程 handle；验证正常、创建失败、超时/提前返回和多次关闭入口。
6. **Day 6：工程门禁**。接入 GoogleTest、CTest、MSVC ASan、静态分析和 Debug/Release preset；保存命令与结果。
7. **Day 7：解释与 Review**。闭卷讲 5 分钟；审查当周 diff；回答“所有权是谁的、何时转移、每条错误路径如何释放”。

`safe_name()` 和 `first_duplicate()` 可以留到 STL/算法日，并按复杂度与边界测试验收；不要再把它们写成 RAII 的主要证据。

## 开源复用与许可证判断

| 项目 | 许可证/维护信号 | 使用建议 |
|---|---|---|
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | [MIT](https://github.com/ggml-org/llama.cpp/blob/master/LICENSE)；提交和构建后端变化快 | 强烈推荐阅读和实验；必须固定 commit，记录 API/模型/参数，不复制未审计示例后直接宣称原创 |
| [ONNX Runtime](https://github.com/microsoft/onnxruntime) | [MIT](https://github.com/microsoft/onnxruntime/blob/main/LICENSE)；持续发布，多硬件 EP | 主运行时学习框架；优先用稳定 release/tag，第三方 EP 和模型另查许可证 |
| [OpenVINO](https://github.com/openvinotoolkit/openvino) | Apache-2.0；2026 年仍持续发布 | 适合 Intel 后端与 benchmark 对照；不要求半年内深入全部 plugin/compiler 源码 |
| [WIL](https://github.com/microsoft/wil) | MIT；官方说明采用 live-at-head，2026 年仍有 release | 适合第一周 RAII 源码；训练项目仍应固定版本以保证复现 |
| [DirectML](https://github.com/microsoft/DirectML) | MIT；官方明确 maintenance mode、样例不再更新 | 只作兼容/历史对照；新主线优先 Windows ML/ORT |
| [GoogleTest](https://github.com/google/googletest) | BSD-3-Clause，官方支持 CMake/Windows | 从第一周使用；固定 release/tag，不用手工拷贝未知版本源码 |

代码仓库许可证不覆盖模型权重、数据集或第三方 kernel。证据清单必须为每个模型单独记录来源、版本、license、hash、用途与再分发限制。

## 建议在仓库中补出的结构

```text
curriculum/units/<week>-<topic>.md   # 问题、概念、源码入口、实验、验收
references/source-manifest.yml       # repo/tag/commit/license/last_verified
projects/inference-workbench/        # 半年主项目合同
benchmarks/                           # 固定配置与机器可读结果
evidence/                             # 构建、测试、profile、讲解、截图索引
adr/                                  # 后端、调度、错误模型、可观测性取舍
```

每个 `unit` 至少包含：先修知识、一个问题、一手资料不超过 3 项、源码文件不超过 4 个、最小实验、失败用例、测试命令、性能指标、口头问题、完成门禁。这样“学习资料”和“动手写代码”不会成为二选一，而是同一个可验证训练单元的前后两段。
