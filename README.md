# C++ AI Inference & Agent Upgrade

一个面向 Windows C++ AI 推理基础设施岗位、兼顾高级 C++ 工程能力的证据驱动训练系统。半年目标是形成可求职、可展示、可复现的工程证据，而不是完成一份课程清单。

## 使用方式

先依次阅读：

1. `plan/learning-loop.md`：每天如何学习、读源码、实现和复测；
2. `plan/competency-matrix.md`：能力等级和目标；
3. `daily/STATE.md`：当前阶段和证据状态；
4. `daily/current.md`：当天唯一最低任务。

每天完成一个约 1 小时的最小闭环。不是上来盲写代码，也不是连续看资料：先闭卷诊断，再读一份主资料和一个源码切片，然后实现、验证和复述。

跨平台记录命令：

```bash
python scripts/training.py record --minutes 60 --completed "完成生命周期微实验" --blocker "无" --self-score 2 --phase A
python scripts/training.py next
```

Windows PowerShell 也可继续使用：

```powershell
pwsh ./scripts/record-progress.ps1 -Minutes 60 -Completed "完成 RAII Day 1" -Blocker "无" -SelfScore 1 -Phase A
```

然后查看下一单元建议：

```powershell
pwsh ./scripts/new-day.ps1
```

训练系统自身的回归测试：

```bash
python -m unittest discover -s tests -v
```

规则：先诊断，再定向学习；首次实现闭卷完成；AI 可在首次尝试后 Review 和生成反例。关键代码必须自己重写、解释、测试，并在 7/21 天后复测。计划不是固定日历，而是“能力矩阵 + 12/24 周路线图 + 每日滚动任务 + 阶段门禁”。

## 目录

- `plan/baseline.md`：当前能力基线与证据状态
- `plan/system-review-2026-09-04.md`：训练系统评审与改进理由
- `plan/learning-loop.md`：诊断、学习、源码、实现、验证、复述与复测闭环
- `plan/competency-matrix.md`：L0–L4 能力矩阵
- `plan/roadmap-12-weeks.md`：12 周路线和阶段门禁
- `plan/roadmap-6-12-months.md`：长期路线（含 C++17/20、Agent Runtime、AI 基础设施、设计模式和近期岗位时效校准）
- `plan/project-selection.md`：训练营项目对标与半年主项目/展示层选择
- `plan/source-research-2026-09-04.md`：官方资料、源码和当前岗位样本校准
- `plan/gap-audit-design-patterns-and-jobs-2026-09-05.md`：设计模式与岗位要求缺口审计
- `assessment/`：闭卷测评记录与后续测评题
- `evidence/`：可进入简历的工程证据卡
- `daily/current.md`：当天任务和验收标准
- `daily/progress.jsonl`：每日真实进度（不写入密钥或私密资料）
- `labs/`：可提交的最小实验和测试；`work/` 只放不提交的临时/私有内容
- `projects/`：递进式综合项目合同
- `curriculum/`：按“问题—资料—源码—实验—验证—复测”编写的训练单元
- `references/`：固定源码版本、许可证和用途清单
- `benchmarks/`、`adr/`：性能证据和架构决策
- `scripts/`：本地滚动计划辅助脚本

## 边界

本项目不自动上传学习过程中的私有代码、公司代码、凭据、模型密钥、Cookie、转储或原始日志。训练代码只有放入 `labs/` 或 `projects/` 才能成为提交证据；`work/` 始终忽略。开源依赖必须固定版本、核对许可证并本地验证。自动化只记录事实，不自动把“完成”升级为“掌握”。
