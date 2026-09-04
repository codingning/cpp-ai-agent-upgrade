# 今日任务（2026-09-04）

## 主题

生命周期与 RAII：Day 1——先建立问题、验证 Windows 工具链、阅读概念和 WIL 的一个窄源码切片。今天只写 smoke test，不实现资源包装器。

## 闭卷诊断（5 分钟）

不查资料，写下三个预测：

1. 栈对象在正常返回、提前返回和抛出异常时，析构函数分别是否执行？
2. `std::unique_ptr` 为什么不能复制，但可以移动？
3. RAII 管理的“资源”是否只指堆内存？列出三个非内存资源。

把答案写入今天的 history 草稿；不确定也要保留原答案。

## 核心任务（不超过 60 分钟）

今天只要求完成：三个闭卷预测、`python scripts/doctor.py` 环境检查、一个最小 C++ smoke test。若时间不足，完成前三项中的前两项也可以，记录真实阻塞即可。

## 环境基线（10 分钟）

在 Windows 的 Visual Studio Developer PowerShell 中运行：

```powershell
python scripts/doctor.py
```

若 Windows 只提供 Python Launcher，使用 `py -3 scripts/doctor.py`。

记录 MSVC、CMake、CTest、Git 和 WSL2 是否可用。工具缺失就是今天的真实阻塞，不跳过、不伪造后续结果。

## 主资料（10 分钟，可选）

只阅读与以下问题直接相关的章节：

- [C++ Core Guidelines 的资源管理与 RAII（R.1–R.5）](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-resource)；
- [Microsoft C++ 对象生命周期与资源管理](https://learn.microsoft.com/en-us/cpp/cpp/object-lifetime-and-resource-management-modern-cpp?view=msvc-170)。

阅读后用自己的话回答：所有权是什么、析构为什么是错误路径的一部分、裸指针什么时候只能表示观察关系。不要复制资料原文。

## 源码切片（20 分钟，可选）

使用 `references/source-manifest.yml` 中固定的 Microsoft WIL commit，只定位 `include/wil/resource.h` 中一个 handle wrapper 相关的定义：

- 记录文件、commit 和符号；
- 画出有效、无效、移动后、reset/release 后的所有权状态；
- 说明删除器在什么时候调用；
- 写下一个看不懂的细节，不继续无限展开。

## Smoke test（5 分钟，核心）

创建并编译 `labs/week01/toolchain_smoke.cpp`，只需证明当前 MSVC 编译命令和程序运行有效。不要在今天提前实现完整 RAII wrapper。

## 复述与记录（5 分钟，核心）

- 保存工具检查和 smoke test 的命令与结果；
- 用自己的话解释 RAII 为什么覆盖错误路径，以及 move 前后谁拥有资源；
- 对照闭卷预测，但不因为读懂概念就提升到 L2；
- 写下 Day 2 要验证的三个失败：泄漏、double-close、提前返回。

## 验收

- 完成三个“原始预测 → 资料/源码结论 → 尚待实验验证”对照；
- Windows 必需工具状态已记录；
- （可选）能定位并初步解释一个 WIL 源码切片；
- smoke test 使用 MSVC 编译并运行；
- （可选）能在两分钟内不看资料解释 RAII、所有权和移动；
- 未完成时只记录已完成阶段和阻塞，不补写掌握结论。

## 完成后

运行：

```bash
python scripts/training.py record --minutes 60 --completed "生命周期与 RAII Day 1" --blocker "无" --self-score 1 --phase A
python scripts/training.py next
```

下一单元是 `curriculum/units/week01-raii.md` 的 Day 2：先用假资源复现泄漏、double-close 和提前返回，不直接实现最终包装器。
