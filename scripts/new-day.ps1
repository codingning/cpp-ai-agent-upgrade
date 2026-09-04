$root = Split-Path -Parent $PSScriptRoot
$progress = Join-Path $root 'daily/progress.jsonl'
if (!(Test-Path $progress)) { Write-Output '暂无进度记录；先执行今日最低任务。'; exit 0 }
$last = Get-Content $progress | Select-Object -Last 1 | ConvertFrom-Json
$blocker = "$($last.blocker)".Trim()
if ($blocker -and $blocker -notin @('无', 'none', 'null', 'n/a', 'no')) {
  Write-Output "下一单元建议：保留当前阶段并拆小阻塞项：$blocker"
}
elseif ($last.phase -eq 'A' -and $last.self_score -ge 1) {
  Write-Output '下一单元建议：进入 B 日，先复现错误基线，再闭卷实现真实资源包装器。'
}
elseif ($last.self_score -lt 2) {
  Write-Output '下一单元建议：保留当前阶段，缩小任务并补一个预测—结果微实验。'
}
elseif ($last.phase -eq 'B') {
  Write-Output '下一单元建议：进入 C 日，做故障注入、性能对照和口头复述。'
}
else {
  Write-Output '下一单元建议：进入 B 日，闭卷实现真实资源包装器并补边界测试。'
}
