# GitHub 推送状态

远端仓库：<https://github.com/codingning/cpp-ai-agent-upgrade>

不要在此文件硬编码“最新提交”；恢复环境时使用 `git status -sb`、`git log -1 --oneline` 和 `git remote -v` 获取当前事实。

如需在新环境重新绑定远端，可执行：

```powershell
gh auth login -h github.com
git remote -v
```

如果远端尚未配置：

```powershell
git remote add origin https://github.com/codingning/cpp-ai-agent-upgrade.git
git push -u origin master
```

推送前请确认仓库不包含 `work/` 中的私有代码、转储、凭据或公司资料。
