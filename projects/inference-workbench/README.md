# Windows Inference Runtime Workbench

这是第 9 周后启用的主项目目录。当前只保留合同和结构说明，避免在 C++、构建、并发和性能底座未通过门禁前提前堆功能。

计划模块：

- `backends/`：ONNX Runtime、llama.cpp Adapter；
- `runtime/`：模型注册、有界调度、取消与关闭；
- `memory/`：buffer/tensor pool 与 I/O Binding 实验；
- `observability/`：metrics、trace 和 benchmark 口径；
- `faults/`：坏输入、超时、取消竞争和 backend 失败注入；
- `cli/`：最小演示入口；
- `tests/`：单元、集成、并发和回归测试。

第三方依赖不得直接从浮动分支拉取；使用 `references/source-manifest.yml` 的固定基线或经过审计的 release，并分别记录代码、模型和数据许可证。
