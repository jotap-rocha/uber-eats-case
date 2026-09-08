# ==============================================================================
# Script: shadowtraffic-report-loop.ps1
# Descricao: Loop de background que escreve um snapshot da geracao de dados
#            (contagem por tabela + crescimento desde o snapshot anterior) em
#            logs/shadowtraffic-report.log a cada hora, enquanto gen-unified
#            estiver ativo. Nao chamar diretamente -- iniciado e encerrado
#            automaticamente por toggle-shadowtraffic.ps1 (on/off).
#
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

param(
    [int]$IntervalSeconds = 3600
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$logDir   = "$repoRoot\logs"
$logFile  = "$logDir\shadowtraffic-report.log"

if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

. "$PSScriptRoot\lib\shadowtraffic-common.ps1"

function Write-Snapshot {
    param($Snapshot, $Previous, [datetime]$Now, $PreviousTime)

    $lines = @()
    $lines += "==== $($Now.ToString('yyyy-MM-dd HH:mm:ss')) ===="

    if ($Previous) {
        $elapsedMin = [Math]::Round(($Now - $PreviousTime).TotalMinutes, 1)
        $lines += "  (desde $($PreviousTime.ToString('yyyy-MM-dd HH:mm:ss')), ${elapsedMin} min)"
    } else {
        $lines += "  (primeiro snapshot - baseline)"
    }

    foreach ($key in $Snapshot.Keys) {
        $value = $Snapshot[$key]
        if ($Previous) {
            $delta = $value - $Previous[$key]
            $lines += ("  {0,-12} {1,10}   (+{2})" -f "${key}:", $value, $delta)
        } else {
            $lines += ("  {0,-12} {1,10}" -f "${key}:", $value)
        }
    }
    $lines += ""

    Add-Content -Path $logFile -Value ($lines -join "`n")
}

Add-Content -Path $logFile -Value "---- loop de report iniciado (PID $PID), intervalo ${IntervalSeconds}s ----"

$envVars      = Get-EnvVars -RepoRoot $repoRoot
$previous     = $null
$previousTime = $null

while ($true) {
    if (-not (Test-ContainerRunning -Name "gen-unified")) {
        Add-Content -Path $logFile -Value "---- gen-unified nao esta mais ativo, encerrando loop de report ----`n"
        break
    }

    $now      = Get-Date
    $snapshot = Get-GeneratorSnapshot -EnvVars $envVars
    Write-Snapshot -Snapshot $snapshot -Previous $previous -Now $now -PreviousTime $previousTime

    $previous     = $snapshot
    $previousTime = $now

    Start-Sleep -Seconds $IntervalSeconds
}
