$root = Split-Path -Parent $PSScriptRoot
$progress = Join-Path $root 'daily/progress.jsonl'
if (!(Test-Path $progress)) { Write-Output '暂无进度记录；先执行今日最低任务。'; exit 0 }
$last = Get-Content $progress | Select-Object -Last 1 | ConvertFrom-Json
if ($last.blocker) { Write-Output "下一天建议：拆小并重做阻塞项：$($last.blocker)" }
elseif ($last.self_score -ge 4) { Write-Output '下一天建议：保留复盘，增加一个边界测试或性能对照。' }
else { Write-Output '下一天建议：重复同一主题，先独立重写核心代码并补测试。' }
