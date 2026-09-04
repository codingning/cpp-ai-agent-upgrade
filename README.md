# C++ AI Agent Upgrade

一个按真实进度滚动更新的 C++ 能力提升项目。

## 使用方式

每天至少完成 `daily/current.md` 的最低任务（约 1 小时）。完成后运行：

```powershell
pwsh ./scripts/record-progress.ps1 -Minutes 60 -Completed "完成 RAII 最小实验" -Blocker "无"
```

然后根据记录更新下一天任务：

```powershell
pwsh ./scripts/new-day.ps1
```

规则：先独立思考，再使用 AI；关键代码必须自己重写、解释、测试。计划不是固定日历，而是“12 周路线图 + 每日滚动任务 + 每周门禁”。

## 目录

- `plan/baseline.md`：当前能力基线与证据状态
- `plan/roadmap-12-weeks.md`：12 周路线和阶段门禁
- `plan/roadmap-6-12-months.md`：长期路线
- `assessment/`：闭卷测评记录与后续测评题
- `daily/current.md`：当天任务和验收标准
- `daily/progress.jsonl`：每日真实进度（不写入密钥或私密资料）
- `projects/`：递进式综合项目合同
- `scripts/`：本地滚动计划辅助脚本

## 边界

本项目不自动上传学习过程中的私有代码、公司代码、凭据、模型密钥、Cookie、转储或原始日志。开源依赖必须固定版本、核对许可证并本地验证。
