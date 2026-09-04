# GitHub 推送状态

本地提交：`a2411dc Add adaptive C++ AI agent upgrade plan`

当前无法自动推送：GitHub CLI 已登录账号 `codingning`，但 keyring 中 token 已失效；当前仓库也尚未配置 remote。

恢复后执行：

```powershell
gh auth refresh -h github.com
gh repo create cpp-ai-agent-upgrade --public --source . --remote origin --push
```

如果仓库已存在：

```powershell
git remote add origin https://github.com/<账号>/cpp-ai-agent-upgrade.git
git push -u origin master
```

推送前请确认仓库不包含 `work/` 中的私有代码、转储、凭据或公司资料。
