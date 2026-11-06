# ==============================================================================
# Script: toggle-shadowtraffic.ps1
# Descricao: Liga/desliga o gerador ShadowTraffic (gen-unified) manualmente,
#            SEM reiniciar a numeracao dos IDs (customers/drivers no Oracle,
#            restaurants no Postgres; F5.5 do modelo fisico). Cada "on"
#            recalcula "startingFrom" a partir do MAX(id) real nas tabelas e o
#            "maxEvents" que falta ate a meta antes de subir o container. Tambem
#            liga/desliga junto dois loops em background:
#              - loop de report horario (shadowtraffic-report-loop.ps1) em
#                logs/shadowtraffic-report.log;
#              - loop de restart automatico a cada 2h por padrao
#                (shadowtraffic-restart-loop.ps1), que dispara este mesmo
#                script (off -> on) para liberar tetos vitalicios de
#                maxEvents/fork.maxForks+keepAlive -- ver
#                .claude/kb/shadowtraffic/patterns/
#                restart-automatico-periodico.md.
#
# Por que este script existe (nao usar apenas docker-compose stop/start):
#   O config shared/gen/unified/uber-eats.json.template usa "startingFrom": N fixo
#   para os campos sequenciais (vars.id de customers, drivers e restaurants).
#   Se o container for religado do zero com o mesmo N fixo
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

. "$PSScriptRoot\..\lib\shadowtraffic-common.ps1"

$repoRoot  = Get-RepoRoot
$jsonPath  = "$repoRoot\shared\gen\unified\uber-eats.json"

$logDir      = "$repoRoot\logs"
$logFile     = "$logDir\shadowtraffic-report.log"
$reportPid   = "$logDir\report.pid"
$reportLoop  = "$PSScriptRoot\shadowtraffic-report-loop.ps1"

# Loop de restart automatico (a cada 2h por padrao) -- ver
# shadowtraffic-restart-loop.ps1 e .claude/kb/shadowtraffic/patterns/
# restart-automatico-periodico.md.
$restartPidFile    = "$logDir\restart-loop.pid"
$restartLogFile    = "$logDir\shadowtraffic-restart.log"
$restartLoopScript = "$PSScriptRoot\shadowtraffic-restart-loop.ps1"

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

function Test-RestartLoopRunning {
    if (-not (Test-Path $restartPidFile)) { return $false }
    $procId = (Get-Content $restartPidFile -Raw).Trim()
    if (-not $procId) { return $false }
    $proc = Get-Process -Id ([int]$procId) -ErrorAction SilentlyContinue
    if (-not $proc) { return $false }

    # Confirma que o PID vivo e de fato o loop de restart, nao outro processo
    # que por acaso reaproveitou o mesmo numero (Windows recicla PIDs) com um
    # restart-loop.pid desatualizado -- evita falso positivo em
    # Test-RestartLoopRunning / falso alvo em Stop-RestartLoop.
    $cmdLine = (Get-CimInstance Win32_Process -Filter "ProcessId=$procId" -ErrorAction SilentlyContinue).CommandLine
    return [bool]($cmdLine -and $cmdLine -match "shadowtraffic-restart-loop")
}

function Start-RestartLoop {
    if (-not (Test-Path $logDir)) {
        New-Item -ItemType Directory -Path $logDir -Force | Out-Null
    }
    if (Test-RestartLoopRunning) { return }

    # Lancado explicitamente via "pwsh" (PowerShell 7+), nunca via "powershell"
    # (Windows PowerShell 5.1, usado por Start-ReportLoop): o ciclo interno do
    # loop de restart chama toggle-shadowtraffic.ps1 -Action on, que roda
    # Sync-StartingPoints com ConvertFrom-Json -Depth 100 -- parametro que nao
    # existe no Windows PowerShell 5.1 e quebraria a primeira chamada do ciclo.
    $proc = Start-Process pwsh -ArgumentList @("-NoProfile", "-WindowStyle", "Hidden", "-File", $restartLoopScript) -WindowStyle Hidden -PassThru
    Set-Content -Path $restartPidFile -Value $proc.Id
    Write-Host "[OK] Loop de restart iniciado (PID $($proc.Id)) -> $restartLogFile"
}

function Stop-RestartLoop {
    if (-not (Test-Path $restartPidFile)) { return }
    $procId = (Get-Content $restartPidFile -Raw).Trim()
    if (-not $procId) { return }

    if ([int]$procId -eq $PID) {
        # Este "off" foi autodisparado pelo proprio ciclo do loop de restart
        # (chamado via '&' dentro de shadowtraffic-restart-loop.ps1 -- mesmo
        # processo/$PID do loop, nao um processo filho). Nao matar: o mesmo
        # processo vai seguir sozinho para o "on" logo em seguida e
        # restart-loop.pid deve permanecer intacto. Ver Notes de
        # PROMPT_SHADOWTRAFFIC_RESTART_LOOP.md para o detalhamento completo
        # desta decisao de arquitetura (validada por the-planner).
        Add-Content -Path $restartLogFile -Value "  [INFO] loop de restart sobrevive ao proprio ciclo (PID $PID)"
        return
    }

    # Chamada externa/manual (processo diferente) -- desligar de verdade, mas
    # so se o PID vivo ainda for realmente o loop de restart (mesma checagem
    # de Test-RestartLoopRunning). Sem isso, um restart-loop.pid desatualizado
    # com PID reaproveitado pelo Windows para outro processo qualquer faria
    # este Stop-Process matar o processo errado.
    $cmdLine = (Get-CimInstance Win32_Process -Filter "ProcessId=$procId" -ErrorAction SilentlyContinue).CommandLine
    if ($cmdLine -and $cmdLine -match "shadowtraffic-restart-loop") {
        Stop-Process -Id ([int]$procId) -Force -ErrorAction SilentlyContinue
    }
    Remove-Item $restartPidFile -Force -ErrorAction SilentlyContinue
    Write-Host "[OK] Loop de restart encerrado."
}

function Show-Status {
    $running = Test-ContainerRunning -Name "gen-unified"
    $state = if ($running) { "ATIVO" } else { "PARADO" }
    Write-Host "Gerador (gen-unified): $state"

    $reportState = if (Test-ReportLoopRunning) { "ATIVO" } else { "PARADO" }
    Write-Host "Loop de report:        $reportState  (log: $logFile)"

    $restartState = if (Test-RestartLoopRunning) { "ATIVO" } else { "PARADO" }
    Write-Host "Loop de restart:       $restartState  (log: $restartLogFile)"

    $snap = Get-GeneratorSnapshot -EnvVars $envVars
    Write-Host "  customers:   $($snap.customers_count) linhas (max id $($snap.customers))"
    Write-Host "  drivers:     $($snap.drivers_count) linhas (max id $($snap.drivers))"
    Write-Host "  restaurants: $($snap.restaurants_count) linhas (max id $($snap.restaurants))"
}

# Retorna $true se sobrou algum gerador a rodar. Cada cadastro (F5.5 do modelo fisico) usa
# vars.id = sequentialInteger; a meta e o maxEvents do template (alinhado ao parameters.yaml por
# shared/gen/tests/test_template.py). Gerador que ja bateu a meta sai do config gerado.
function Sync-StartingPoints {
    Write-Host "[1/3] Calculando pontos de retomada (MAX id e contagem em cada tabela)..."
    $snap = Get-GeneratorSnapshot -EnvVars $envVars
    Write-Host "   customers=$($snap.customers_count) drivers=$($snap.drivers_count) restaurants=$($snap.restaurants_count)"

    Write-Host "[2/3] Injetando segredos do .env (shared\gen\setup-configs.ps1)..."
    & "$repoRoot\shared\gen\setup-configs.ps1" | Out-Null

    Write-Host "[3/3] Ajustando 'startingFrom' e 'maxEvents' no uber-eats.json gerado (sem tocar no template)..."
    $config = Get-Content $jsonPath -Raw | ConvertFrom-Json -Depth 100
    $remaining = @()
    foreach ($gen in $config.generators) {
        $maxId = $snap[$gen.table]
        $count = $snap["$($gen.table)_count"]
        $left  = [int]$gen.localConfigs.maxEvents - [int]$count
        if ($left -le 0) {
            Write-Host "   $($gen.table): meta de $($gen.localConfigs.maxEvents) atingida, fica de fora"
            continue
        }
        $gen.vars.id.startingFrom = [int]$maxId + 1
        $gen.localConfigs.maxEvents = $left
        Write-Host "   $($gen.table): faltam $left a partir do id $([int]$maxId + 1)"
        $remaining += $gen
    }
    $config.generators = $remaining

    ($config | ConvertTo-Json -Depth 100) | Set-Content -Path $jsonPath -Encoding utf8
    if ($remaining.Count -eq 0) {
        Write-Host "[OK] Todas as metas de cadastro atingidas. Nada a gerar."
        return $false
    }
    Write-Host "[OK] uber-eats.json atualizado. Nenhum ID sera reaproveitado ao religar."
    return $true
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
        # MinIO fora do escopo (ADR 010); o ShadowTraffic so grava no Oracle e no Postgres.
        foreach ($c in @("postgres-ubereats", "oracle-ubereats")) {
            if (-not (Test-ContainerRunning -Name $c)) {
                Write-Host "[ERRO] $c nao esta rodando. Rode primeiro: .\scripts\start-infra.ps1" -ForegroundColor Red
                exit 1
            }
        }

        # Container "running" != pronto para conexao (Oracle em especial fica
        # rodando bem antes do listener registrar o FREEPDB1). Sem isso, rodar
        # logo apos start-infra.ps1 (ex.: via start-all.ps1) da ORA-12514 aqui
        # ou no Show-Status abaixo.
        Write-Host "[INFO] Aguardando bancos ficarem prontos (healthcheck)..." -ForegroundColor Cyan
        foreach ($c in @("postgres-ubereats", "oracle-ubereats")) {
            if (-not (Wait-ContainerHealthy -Name $c)) {
                Write-Host "[ERRO] $c nao ficou pronto a tempo. Verifique: docker logs $c" -ForegroundColor Red
                exit 1
            }
        }

        if (Test-ContainerRunning -Name "gen-unified") {
            Write-Host "[OK] gen-unified ja esta ativo. Nada a fazer."
            Start-ReportLoop
            Start-RestartLoop
            Show-Status
            exit 0
        }

        if (-not (Sync-StartingPoints)) {
            Show-Status
            exit 0
        }

        Write-Host "[INFO] Subindo gen-unified..."
        docker-compose up -d gen-unified | Out-Null

        Start-ReportLoop
        Start-RestartLoop

        Write-Host "[OK] Gerador LIGADO, retomando de onde parou."
        Write-Host "   Ver logs gerador:  docker-compose logs -f gen-unified"
        Write-Host "   Ver report horario: $logFile"
        Write-Host "   Desligar:  .\scripts\toggle-shadowtraffic.ps1 off"
    }

    "off" {
        Stop-ReportLoop
        Stop-RestartLoop

        if (-not (Test-ContainerRunning -Name "gen-unified")) {
            Write-Host "[OK] gen-unified ja esta parado."
            exit 0
        }
        docker-compose stop gen-unified | Out-Null
        Write-Host "[OK] Gerador DESLIGADO. Progresso salvo nas tabelas."
        Write-Host "   Religar: .\scripts\toggle-shadowtraffic.ps1 on"
    }
}
