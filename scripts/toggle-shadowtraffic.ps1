# ==============================================================================
# Script: toggle-shadowtraffic.ps1
# Descricao: Liga/desliga o gerador ShadowTraffic (gen-unified) manualmente,
#            SEM reiniciar a numeracao dos IDs (users/drivers/orders/payments/
#            restaurants). Cada "on" recalcula "startingFrom" a partir do
#            MAX(id) real nas tabelas antes de subir o container. Tambem
#            liga/desliga junto um loop de report horario (ver
#            shadowtraffic-report-loop.ps1) em logs/shadowtraffic-report.log.
#
# Por que este script existe (nao usar apenas docker-compose stop/start):
#   O config gen/unified/uber-eats.json.template usa "startingFrom": N fixo
#   para os campos sequenciais (user_id, driver_id, order_id, payment_id,
#   restaurant_id). Se o container for religado do zero com o mesmo N fixo
#   e a tabela ja tiver linhas alem desse N, o INSERT bate em PK duplicada
#   (ORA-00001 / "duplicate key value violates unique constraint"). Isso NAO
#   afeta so aquele fork: ja foi observado o pipeline inteiro (17 streams)
#   travar em 99% de CPU sem gerar mais nenhuma linha ate ser reiniciado com
#   o valor certo. Ver .claude/kb/shadowtraffic/patterns/
#   restart-seguro-startingFrom.md para o incidente completo.
#
# Uso:
#   .\scripts\toggle-shadowtraffic.ps1 on       # religa, retomando de onde parou
#   .\scripts\toggle-shadowtraffic.ps1 off      # desliga (dados ficam salvos)
#   .\scripts\toggle-shadowtraffic.ps1 status   # mostra estado + contagem por tabela
#
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("on", "off", "status")]
    [string]$Action
)

$ErrorActionPreference = "Stop"

$repoRoot  = Split-Path -Parent $PSScriptRoot
$jsonPath  = "$repoRoot\gen\unified\uber-eats.json"
$RESTAURANT_TARGET = 500

$logDir      = "$repoRoot\logs"
$logFile     = "$logDir\shadowtraffic-report.log"
$reportPid   = "$logDir\report.pid"
$reportLoop  = "$PSScriptRoot\shadowtraffic-report-loop.ps1"

. "$PSScriptRoot\lib\shadowtraffic-common.ps1"

# ------------------------------------------------------------------------------
# Helpers proprios deste script
# ------------------------------------------------------------------------------

function Test-ReportLoopRunning {
    if (-not (Test-Path $reportPid)) { return $false }
    $procId = Get-Content $reportPid -Raw
    if (-not $procId) { return $false }
    return [bool](Get-Process -Id ([int]$procId.Trim()) -ErrorAction SilentlyContinue)
}

function Start-ReportLoop {
    if (-not (Test-Path $logDir)) {
        New-Item -ItemType Directory -Path $logDir -Force | Out-Null
    }
    if (Test-ReportLoopRunning) { return }

    $proc = Start-Process powershell -ArgumentList @("-NoProfile", "-WindowStyle", "Hidden", "-File", $reportLoop) -WindowStyle Hidden -PassThru
    Set-Content -Path $reportPid -Value $proc.Id
    Write-Host "[OK] Loop de report iniciado (PID $($proc.Id)) -> $logFile"
}

function Stop-ReportLoop {
    if (-not (Test-Path $reportPid)) { return }
    $procId = (Get-Content $reportPid -Raw).Trim()
    if ($procId) {
        Stop-Process -Id ([int]$procId) -Force -ErrorAction SilentlyContinue
    }
    Remove-Item $reportPid -Force -ErrorAction SilentlyContinue
    Write-Host "[OK] Loop de report encerrado."
}

function Show-Status {
    $running = Test-ContainerRunning -Name "gen-unified"
    $state = if ($running) { "ATIVO" } else { "PARADO" }
    Write-Host "Gerador (gen-unified): $state"

    $reportState = if (Test-ReportLoopRunning) { "ATIVO" } else { "PARADO" }
    Write-Host "Loop de report:        $reportState  (log: $logFile)"

    $snap = Get-GeneratorSnapshot -EnvVars $envVars
    Write-Host "  users:       $($snap.users)"
    Write-Host "  drivers:     $($snap.drivers)"
    Write-Host "  orders:      $($snap.orders)"
    Write-Host "  payments:    $($snap.payments)"
    Write-Host "  restaurants: $($snap.restaurants) / $RESTAURANT_TARGET"
}

function Sync-StartingPoints {
    Write-Host "[1/3] Calculando pontos de retomada (MAX id atual em cada tabela)..."

    $snap = Get-GeneratorSnapshot -EnvVars $envVars
    $maxUser    = $snap.users
    $maxDriver  = $snap.drivers
    $maxOrder   = $snap.orders
    $maxPayment = $snap.payments
    $restCount  = $snap.restaurants
    $maxRest    = Get-OracleScalar -EnvVars $envVars -Sql "SELECT NVL(MAX(restaurant_id),0) FROM UBEREATS.RESTAURANTS;"

    Write-Host "   users=$maxUser drivers=$maxDriver orders=$maxOrder payments=$maxPayment restaurants=$restCount/$RESTAURANT_TARGET"

    Write-Host "[2/3] Injetando segredos do .env (gen\setup-configs.ps1)..."
    & "$repoRoot\gen\setup-configs.ps1" | Out-Null

    Write-Host "[3/3] Ajustando 'startingFrom' no uber-eats.json gerado (sem tocar no template)..."
    $config = Get-Content $jsonPath -Raw | ConvertFrom-Json -Depth 100

    $usersGen = $config.generators | Where-Object { $_.table -eq "users" }
    $usersGen.row.user_id.startingFrom = $maxUser + 1

    $driversGen = $config.generators | Where-Object { $_.table -eq "drivers" }
    $driversGen.fork.key.startingFrom = $maxDriver + 1

    $ordersGen = $config.generators | Where-Object { $_.table -eq "orders" }
    $ordersGen.fork.key.startingFrom = $maxOrder + 1

    $paymentsGen = $config.generators | Where-Object { $_.table -eq "payments" }
    $paymentsGen.fork.key.startingFrom = $maxPayment + 1

    $restGen = $config.generators | Where-Object { $_.table -eq "restaurants" }
    $restGen.row.restaurant_id.startingFrom = $maxRest + 1
    $restGen.localConfigs.maxEvents = [Math]::Max(1, $RESTAURANT_TARGET - $restCount)

    ($config | ConvertTo-Json -Depth 100) | Set-Content -Path $jsonPath -Encoding utf8
    Write-Host "[OK] uber-eats.json atualizado. Nenhum ID sera reaproveitado ao religar."
}

# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------

$envVars = Get-EnvVars -RepoRoot $repoRoot

switch ($Action) {

    "status" {
        Show-Status
    }

    "on" {
        foreach ($c in @("postgres-ubereats", "oracle-ubereats", "minio-ubereats")) {
            if (-not (Test-ContainerRunning -Name $c)) {
                Write-Host "[ERRO] $c nao esta rodando. Rode primeiro: .\scripts\start-infra.ps1" -ForegroundColor Red
                exit 1
            }
        }

        if (Test-ContainerRunning -Name "gen-unified") {
            Write-Host "[OK] gen-unified ja esta ativo. Nada a fazer."
            Start-ReportLoop
            Show-Status
            exit 0
        }

        Sync-StartingPoints

        Write-Host "[INFO] Subindo gen-unified..."
        docker-compose up -d gen-unified | Out-Null

        Start-ReportLoop

        Write-Host "[OK] Gerador LIGADO, retomando de onde parou."
        Write-Host "   Ver logs gerador:  docker-compose logs -f gen-unified"
        Write-Host "   Ver report horario: $logFile"
        Write-Host "   Desligar:  .\scripts\toggle-shadowtraffic.ps1 off"
    }

    "off" {
        Stop-ReportLoop

        if (-not (Test-ContainerRunning -Name "gen-unified")) {
            Write-Host "[OK] gen-unified ja esta parado."
            exit 0
        }
        docker-compose stop gen-unified | Out-Null
        Write-Host "[OK] Gerador DESLIGADO. Progresso salvo nas tabelas."
        Write-Host "   Religar: .\scripts\toggle-shadowtraffic.ps1 on"
    }
}
