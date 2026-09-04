# 综合项目合同

## P0：推理底层实验集（约 40–60 小时）

用小而可测的自研组件验证理解：move-only Windows handle、Buffer/tensor shape/stride/view、arena、float32 matmul、一个简化量化编解码和有界线程池。它们是学习证据，不尝试组成完整 Transformer。

验收：正确性、越界、错误路径、资源回收和并发测试通过；matmul/arena 有标量或基线版本与优化版本对照；每个组件能说明它与成熟 runtime 的对应关系和缺失能力。

## P1：Windows C++ inference runtime workbench（主项目，约 120–180 小时）

目标是复用并理解成熟运行时，构建一个可测试、可测量、可解释的本地推理工作台。先接 ONNX Runtime，再接 llama.cpp；不从零重写完整模型执行。

最小架构：

1. **`IInferenceBackend`**：ORT 与 llama.cpp 的 Adapter，不把第三方类型泄漏到业务层；
2. **`ModelRegistry`**：记录模型版本、hash、license、shape/dtype 和 backend capability；
3. **`RequestScheduler`**：有界队列、超时、取消、关闭、优先级和可选 batching；
4. **`Buffer/TensorPool`**：预分配与复用，ORT 路径实验 I/O Binding；
5. **`Metrics/Trace`**：冷/热启动、队列等待、TTFT、tokens/s、p50/p95/p99、CPU/RSS/VRAM；
6. **`FaultInjection`**：坏模型、坏 shape、OOM 模拟、取消竞争和 backend timeout/crash；
7. **CLI**：只负责可复现演示，不把时间消耗在完整 UI。

里程碑：ORT 官方样例复现 → benchmark harness → llama.cpp 固定基线 → 双 backend Adapter → 调度/取消/指标 → 故障注入 → Windows 打包与 WSL2 回归。

验收：正确性、坏输入、异常/关闭、资源回收和并发测试通过；Benchmark 固定硬件、编译选项、模型、输入、warmup、迭代、误差与统计口径；Windows 原生和 WSL2 构建可复现；至少 3 份 ADR；每个里程碑有 commit、失败记录和五分钟说明。

非目标：完整训练框架、自研 CUDA kernel、支持任意 Hugging Face 模型、分布式推理、商业级吞吐或完整桌面 UI。

## P2：本地 Agent 展示层（约 40–60 小时）

Agent 通过稳定接口调用 P1 runtime，完成一个离线 Git diff 审查或本地知识问答演示。覆盖结构化输入输出、工具注册、参数校验、权限白名单、超时、取消、日志、失败重放和人工审批。

验收：不得绕过 P1 直接把云端/现成服务伪装成自研推理证据；正常、拒绝、超时、取消、恶意参数和关闭测试通过；日志含 request/tool/model/status/duration/error；离线可重放。

## P3：源码对照与上游协作

固定 commit 阅读并小改 llama.cpp、ONNX Runtime 或一个适配 Windows 的活跃实现。每次只选择一个主题：tensor/arena、matmul、量化、Tokenizer、KV Cache、线程池或 graph execution。必须记录构建命令、源码入口、调用路径、测试、Benchmark、许可证和本地修改。

源码对照不是第三个完整项目；它贯穿 P0/P1 并服务于设计验证。第 21–24 周争取形成一个可审阅的上游 issue、文档修正、测试改进或小型 patch，但不以合并结果作为完成条件。

## 简历证据账本

任何能力进入简历前，必须登记：能力名称、个人贡献、代码提交、构建命令、测试结果、性能/稳定性数据、已知限制和可复述的面试问题。只有课程观看、AI 生成代码或未验证的开源阅读不得直接写入。
