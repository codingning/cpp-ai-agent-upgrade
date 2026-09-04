# 12 周路线图（Windows / C++ AI 推理基础设施）

每周默认 5–7 个最低单元、每天最低 1 小时。每个主题按 `plan/learning-loop.md` 完成 A/B/C 日，不以阅读时长代替能力证据。前 12 周目标是补齐进入推理源码和性能工程所需的 C++ 底座，并交付 Windows inference workbench 的第一条 ONNX Runtime 基线。

| 周 | 学习与源码问题 | 实践输出 | 周门禁 |
|---|---|---|---|
| 1 | 对象生命周期、RAII、所有权；标准库智能指针如何销毁和移动 | 生命周期探针、真实资源包装器 | 正常/提前返回/异常/移动/重复关闭均有测试，达到 L2 |
| 2 | Rule of 0/5、值语义、错误模型；容器或 runtime 如何表达所有权 | `Buffer`、对齐内存块、错误返回实验 | ASan 或 MSVC 诊断无明显泄漏；能解释每个特殊成员 |
| 3 | CMake Presets、CTest、GoogleTest、警告与静态分析；优秀项目如何组织 target | 把前两周实验工程化 | MSVC Debug/Release 与 WSL2 GCC/Clang preset 构建测试可复现 |
| 4 | STL、模板、`span/string_view/optional/variant`、复杂度和失效规则 | tensor shape、stride 和安全 view | 边界、溢出、空值、失效规则测试通过，核心项 L3 |
| 5 | 线程、锁、条件变量、内存模型；线程池如何关闭 | 有界队列和线程池 | 正常、超时、取消、关闭、重复关闭和异常任务通过 |
| 6 | C++20 `jthread/stop_token`、并发测量、背压 | 可取消算子调度器 | 线程全部回收；有竞态/死锁故障记录和吞吐基线 |
| 7 | 内存布局、对齐、缓存、分配与 profiler；推理框架的 tensor 存储 | contiguous tensor + arena 初版 | 正确性测试、分配次数和缓存相关 Benchmark |
| 8 | 标量/SIMD matmul、数值误差、Benchmark 方法 | float32 matmul 与一个向量化对照 | 固定输入、误差阈值、warmup、吞吐和尾延迟可复现 |
| 9 | ONNX Runtime C++ API、Session 生命周期和 Execution Provider 分区 | 复现固定 release 的官方 C++ inference example | Windows CPU 基线可运行；模型、输入、命令、版本和许可证齐全 |
| 10 | ORT threading、memory pattern、I/O Binding、profiling | benchmark harness + 两项开关对照 | warmup、p50/p95/p99、RSS 和正确性口径可复现 |
| 11 | llama.cpp 公共 API、model/context 生命周期、batch/decode；先复现后修改 | 固定 commit 的 `llama-bench` CPU 基线和最短调用链图 | 固定模型/参数；TTFT、tokens/s、RSS；能解释 model/context 所有权 |
| 12 | Windows DLL/API/ABI、部署、dump 与第一版 backend Adapter | inference workbench v0：ORT backend + CLI，预留 llama.cpp 接口 | Windows 新机与 WSL2 可复现；错误路径、日志、性能报告和 1 份 ADR 齐全 |

## 每周固定产出

- 一份主资料的定向笔记，不做大段摘抄；
- 一个固定 commit 的源码切片，记录入口、所有权、错误路径和取舍；
- 可构建代码、边界测试与至少一次失败记录；
- 一项诊断或性能证据；
- 五分钟闭卷说明；
- 下一周完成 7 天复测。

## 面试兼容线

每周保留 1 道 C++ 基础题、1 道算法题和 1 个项目追问。每四周做一次 45–60 分钟模拟面试并更新能力矩阵。题库不能挤占主项目；只有 AC、复杂度、边界测试和闭卷复述齐全才算完成。
