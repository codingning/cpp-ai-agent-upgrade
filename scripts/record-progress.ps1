param(
  [Parameter(Mandatory=$true)][int]$Minutes,
  [Parameter(Mandatory=$true)][string]$Completed,
  [string]$Blocker = "",
  [int]$SelfScore = -1,
  [string]$Phase = ""
)
$root = Split-Path -Parent $PSScriptRoot
$normalizedBlocker = $Blocker.Trim()
if ($normalizedBlocker -in @('', '无', 'none', 'null', 'n/a', 'no')) { $normalizedBlocker = '' }
$entry = [ordered]@{
  date=(Get-Date -Format 'yyyy-MM-dd')
  minutes=$Minutes
  completed=$Completed
  blocker=$normalizedBlocker
  self_score=$SelfScore
  phase=$Phase.ToUpperInvariant()
  review_7d=(Get-Date).AddDays(7).ToString('yyyy-MM-dd')
  review_21d=(Get-Date).AddDays(21).ToString('yyyy-MM-dd')
}
($entry | ConvertTo-Json -Compress) | Add-Content -Encoding UTF8 (Join-Path $root 'daily/progress.jsonl')
Write-Output "已记录：$($entry.date)，$Minutes 分钟；7 天复测：$($entry.review_7d)"
