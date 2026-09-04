# 设计模式与招聘要求缺口审计（2026-09-05）

## 证据边界

- 已核实来源：训练营公开 Wiki、训练营项目表截图、本地题库目录和本项目已有路线。
- 招聘网站搜索：本轮公开搜索受到 CAPTCHA/SSL 限制，未取得可稳定引用的具体职位页面；以下“招聘常见要求”标为待验证的岗位类别假设，不伪装成某家公司当前要求。

## 设计模式：确实缺失，且不能只背 GoF

设计模式应放在真实项目中训练，而不是单独背名词：

1. 创建型：工厂、抽象工厂、Builder、Prototype、依赖注入；
2. 结构型：Adapter、Facade、Decorator、Composite、Bridge、Proxy、Type Erasure；
3. 行为型：Strategy、Command、State、Observer、Chain of Responsibility、Template Method；
4. 并发模式：Thread Pool、Producer–Consumer、Reactor、Proactor、Actor、Pipeline、Active Object；
5. Agent/基础设施模式：Tool Registry、Middleware、Retry/Bulkhead/Circuit Breaker、Event Bus、Plugin、Saga/Outbox（按需）；
6. 反模式与成本：过度抽象、继承层次膨胀、全局单例、隐式线程、无边界事件总线。

验收重点：能说明问题、约束、替代方案、运行时成本、测试方式和何时不用，而不是能背出定义。

## 已发现的其他缺口

| 缺口 | 重要性 | 补充方式 |
|---|---|---|
| API/ABI、ODR、DLL 和插件边界 | 高 | CMake 多目标、DLL 导出、版本兼容实验 |
| 内存分配、缓存、SIMD 和尾延迟 | 高 | Benchmark、分配器/缓存对照、profiling |
| 协程、无锁和内存回收 | 中高 | 先线程池/stop_token，再协程和 hazard/epoch 阅读 |
| 网络协议和分布式容错 | 高 | Protobuf/gRPC、超时、重试、熔断、幂等、背压 |
| 安全工程 | 高 | 路径规范化、Shell 注入、权限白名单、密钥/日志脱敏、供应链审计 |
| 可观测性与发布 | 高 | 结构化日志、指标、trace、崩溃转储、版本/回滚、CI |
| 架构表达与 ADR | 高 | 每个主项目提交组件图、数据流图、ADR 和容量/演进说明 |
| Linux/容器/云原生 | 视岗位而定 | 保留一条最小兼容线，不挤占 Windows/Chromium 主线 |
| 代码 Review、面试和简历 | 高 | 每周 diff review，每 4 周模拟面试，证据账本 |
| 项目管理和协作 | 中高 | Issue、里程碑、变更记录、故障复盘、发布说明 |

## 岗位方向映射

- Windows/Chromium 高级工程：C++ 对象模型、线程/Sequence、IPC、崩溃、性能、构建、API/ABI、安全。
- C++ AI 推理/基础设施：C++17/20、矩阵/张量、内存和缓存、SIMD/GPU 基础、量化、Benchmark、Python/C++ 边界。
- Agent/工具基础设施：协议、状态机、插件、权限、幂等、重试/熔断、审计和可观测性。
- 音视频/实时系统：编解码、WebRTC/网络、线程模型、缓冲/抖动、端到端延迟和资源回收。
- 架构师方向：需求拆解、边界和取舍、容量、可靠性、安全、成本、演进和跨团队表达。

## 结论

原计划不是缺少“更多名词”，而是缺少把设计模式、架构取舍、发布运维和招聘表达接到项目证据上的闭环。现在应采用：

> 基础语义 → 模式在项目中落地 → 故障/性能验证 → ADR/架构表达 → 面试复盘 → 简历证据

