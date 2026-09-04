# 每日训练自动化

自动化每天北京时间 23:00 执行一次：读取 `daily/STATE.md`、`daily/current.md`、进度记录和最近历史；依据当天真实证据写入中文每日记录。若没有学习证据，写入“未学习”，并保留下一日最低任务。

自动化只允许提交和推送本仓库的计划、状态、每日记录和训练代码；不得上传公司代码、私有资料、密钥、Token、Cookie、转储或未授权数据。若 GitHub 登录失效、冲突、测试失败或推送失败，必须报告失败原因。

恢复新环境时，先执行：

```powershell
git pull --ff-only
Get-Content .\README.md
Get-Content .\daily\STATE.md
Get-Content .\daily\current.md
```
