# 综合项目合同

## P1：C++20 本地工具调用 Agent

基于本地 llama.cpp 服务，逐步加入工具注册、参数校验、权限白名单、超时、取消、重试、日志、失败重放和 Benchmark。工具先做文件搜索、代码检索、SQLite 查询和安全 Shell；Shell 只接受结构化参数，不拼接未经验证的命令字符串。

验收：单元测试覆盖正常、拒绝、超时、取消、恶意参数和关闭；所有任务可回收；日志含 request/tool/status/duration/error；离线可重放。

## P2：C++ MCP Server/Client

先阅读并固定 cxxmcp commit，仅作为协议学习入口；实现文件索引或 SQLite 工具。覆盖协议错误、并发请求、超时、恶意参数和权限。无许可证或质量证据的 examples 仅阅读，不作依赖。

## P3：Git diff 代码审查 Agent

本地离线读取 diff，调用静态分析，输出结构化问题、证据位置、规则置信度和人工审批状态；先不接 CI。

## P4：mini-llama.cpp

按张量、Tokenizer、矩阵计算、Transformer 前向、KV Cache、采样、量化、Benchmark 递进，并与固定版本 llama.cpp 对照。

## P5：Electron + C++ 工作台

Electron 负责 UI/壳，C++ 负责索引、搜索和工具执行；验证 IPC、权限隔离、崩溃恢复、资源回收和可观测性。
