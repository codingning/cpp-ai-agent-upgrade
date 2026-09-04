# 第 1 周单元：Windows 资源生命周期与 RAII

## 周问题

一个 Windows `HANDLE` 在正常返回、创建失败、提前返回、异常、移动、重复关闭和进程退出路径中，分别由谁负责关闭？如何用测试证明它恰好关闭一次？

## 一手资料与源码

- [C++ Core Guidelines：资源管理、R.1–R.5、C.20](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-resource)；
- [Microsoft WIL](https://github.com/microsoft/wil)：使用 `references/source-manifest.yml` 固定 commit，只读 `include/wil/resource.h` 中一个 handle wrapper 的定义及相关测试；
- Microsoft Learn：[对象生命周期](https://learn.microsoft.com/en-us/cpp/cpp/object-lifetime-and-resource-management-modern-cpp?view=msvc-170)、[MSVC AddressSanitizer](https://learn.microsoft.com/en-us/cpp/sanitizers/asan?view=msvc-170)和[C++ Code Analysis](https://learn.microsoft.com/en-us/cpp/code-quality/quick-start-code-analysis-for-c-cpp?view=msvc-170)。

每次最多追 2–4 个文件或符号。读前写预测；读后记录所有权状态图、无效值表示、move 后状态、deleter 调用点和析构异常规则。

## 七个最低单元

第一周按“由易到难”的降级路径执行：先用假资源建立生命周期模型，再实现最小 move-only 资源句柄，最后才接触 WIL 和真实 Windows handle。WIL 是优秀实现对照，不是 Day 1 的理解门槛。

### Day 1：工具链与问题建立

**核心**：运行 `python scripts/doctor.py`；确认 VS 2022 Developer PowerShell 中能找到 MSVC、CMake、CTest、Git，写三个闭卷预测，并编译一个 smoke test。**可选**：阅读 Core Guidelines R.1；只定位 WIL 的一个窄切片，不要求理解 `resource.h` 的模板细节。今天不实现资源包装器。

### Day 2：错误基线

**核心**：用假资源和计数 deleter 复现泄漏、double-close、提前返回三种错误中的至少两种。**可选**：补齐第三种并保留修正前后的证据；不要用真实危险资源制造破坏。

### Day 3：最小 RAII

闭卷实现 move-only `unique_resource`：默认态、接管、移动构造、移动赋值、`reset/release/swap`。禁止复制，析构不抛异常。

### Day 4：源码对照

对照固定 commit 的 WIL 和 `std::unique_ptr` 自定义 deleter。记录自己的实现缺少什么、WIL 为什么需要 traits/policy，以及本项目暂时不复制哪些复杂度。

### Day 5：Windows 实战

封装 `CreateFileW` 返回的文件 handle，覆盖成功、创建失败、提前返回、移动和重复 reset。所有路径使用临时测试文件，不碰公司或个人资料。

### Day 6：工程门禁

加入 CMake Presets、CTest/GoogleTest、MSVC 高警告、AddressSanitizer 可用配置和 Code Analysis。记录不兼容组合，不把工具不可用写成测试通过。

### Day 7：闭卷复述与 Review

五分钟解释所有权、move、无效值、deleter 和错误路径；Review 一周 diff；修复至少一个真实问题；安排 7/21 天复测。

## 周门禁

- Windows/MSVC Debug 与 Release 构建可复现；
- 假资源和真实文件 handle 测试覆盖恰好释放一次；
- 创建失败、提前返回、异常、移动和重复 reset 均有证据；
- 能指出 WIL 固定 commit 中对应设计位置；
- 对象生命周期从 L1 提升为 L2 候选，7 天复测通过后确认。

## 难度控制与通用能力保留

如果某日出现连续 15 分钟无法推进、编译环境缺失或源码阅读超出当前基础，立即退回上一层：假资源 → 标准库自定义 deleter → 最小 wrapper → WIL 对照。推理运行时是应用场景，不替代通用高级 C++ 训练；对象模型、STL、并发、错误模型、构建、调试、网络、ABI 和设计取舍仍按能力矩阵独立验收。
