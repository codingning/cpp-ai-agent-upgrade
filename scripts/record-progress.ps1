param(
  [Parameter(Mandatory=$true)][int]$Minutes,
  [Parameter(Mandatory=$true)][string]$Completed,
  [string]$Blocker = "",
  [int]$SelfScore = -1
)
$root = Split-Path -Parent $PSScriptRoot
$entry = [ordered]@{ date=(Get-Date -Format 'yyyy-MM-dd'); minutes=$Minutes; completed=$Completed; blocker=$Blocker; self_score=$SelfScore }
($entry | ConvertTo-Json -Compress) | Add-Content -Encoding UTF8 (Join-Path $root 'daily/progress.jsonl')
Write-Output "已记录：$($entry.date)，$Minutes 分钟"
