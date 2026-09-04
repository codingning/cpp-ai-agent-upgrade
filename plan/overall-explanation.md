# 整体规划说明

## 目标

目标不是背完 C++ 题库，而是把已有 Windows/Chromium 工程经验转化为可迁移、可解释、可测试、能独立完成的现代 C++ 与 AI 推理基础设施能力。主项目是 Windows inference runtime workbench，Agent 是调用它的展示层。

## 三层推进

1. **基础层（第 1–4 周）**：生命周期、RAII、拷贝/移动、STL、算法、C++11 并发。每个主题都要有最小代码、测试和错误复盘。
2. **工程层（第 5–8 周）**：线程池、取消、关闭、CMake、GoogleTest、Sanitizer、Benchmark、Windows 进程/句柄/崩溃分析。
3. **现代 C++ 与推理基础设施层（第 7–12 周及以后）**：把 C++17/20 用到 tensor、内存规划、算子、量化、Tokenizer、KV Cache、调度和 Windows 部署；Agent/MCP 只在 runtime 可用后作为应用层。

## C++17 / C++20 专项路径

### C++17：先建立稳定的日常工程能力

- 语言：结构化绑定、`if constexpr`、折叠表达式、类模板参数推导；
- 库：`std::string_view`、`std::optional`、`std::variant`、`std::any`、`std::filesystem`；
- 工程：异常/错误返回边界、路径处理、类型分支和接口表达；
- 验收：每项至少一个最小程序、一个边界测试和一段口头解释；
- 约束：先掌握语义，再讨论编译器支持，不把“能编译”当作掌握。

### C++20：在 C++11/17 稳定后逐步引入

- 类型系统：`concepts`、`requires`；
- 范围：`ranges`、视图和惰性求值；
- 并发：`jthread`、`stop_token`、信号量/闩锁/屏障；
- 编译期：`consteval`、`constinit`；
- 其他：三路比较、协程机制、modules 的设计目标和当前工具链边界；
- 验收：至少完成 concepts、ranges、jthread 三个可运行实验，并将 `stop_token` 接入线程池关闭测试；
- 降级：时间不足时先完成 concepts + ranges + jthread，协程和 modules 延后；
- 升级：提前完成时增加协程任务调度器和不同 MSVC/Clang 配置的编译对照。

## 每日循环

闭卷诊断 → 阅读一份主资料 → 追一个源码切片 → 闭卷实现 → 测试/诊断/Benchmark → 复述 → 7/21 天复测。AI 在首次实现后参与 Review 和反例生成。时间不固定时只保证最低单元，不用固定日历强行追赶。

## 可写入简历的能力门槛

只有完成真实可复现证据后才写入简历：

- C++：能独立实现并测试 RAII、拷贝/移动、线程安全组件，并解释边界；
- 工程化：有可复现 CMake、单元测试、Sanitizer、Benchmark 和 CI 结果；
- Windows/Chromium：能给出源码入口、变量/调用链、修复提交和定向回归结果；
- AI Agent：有离线可运行的工具注册、参数校验、权限白名单、超时/取消/失败重放和日志证据；
- MCP/推理基础设施：固定 commit，完成源码阅读、局部修改、测试和性能对照。

简历表述采用“做了什么 + 如何验证 + 边界是什么”，不把课程观看或 AI 生成代码写成能力。

## 项目作品梯度

- P1：RAII、tensor/arena、线程池和算子实验，证明高级 C++ 底座；
- P2：Windows inference runtime workbench，证明运行时、性能、调试和架构能力；
- P3：固定 commit 的 llama.cpp/ONNX Runtime 源码对照，证明阅读和迁移能力；
- P4：本地 Agent 展示层，证明 runtime 接口、工具治理和结构化输出；
- P5：Windows 打包、性能报告和项目答辩，形成求职作品集。

每个项目都必须固定版本、核对许可证、保留测试和性能报告；无许可证或无法复现的仓库只作阅读参考。

## 设计模式训练原则

设计模式不单独作为背诵章节，而是嵌入项目：线程池使用生产者-消费者/Active Object；工具调用使用 Registry、Command、Middleware 和 State；失败恢复使用 Retry/Circuit Breaker；模块边界使用 Adapter/Facade/Type Erasure；事件通知只在明确需要时使用 Observer/Event Bus。每次必须记录不用某个模式的理由和成本。

## 高级工程补充能力

除语言和项目外，还要训练 API/ABI 与 DLL、内存分配和缓存、SIMD/性能分析、网络容错、安全边界、结构化日志/指标/trace、CI/发布/回滚、ADR 和跨团队技术表达。Linux/容器/云原生保留最小兼容线，是否加深由目标岗位证据决定。
