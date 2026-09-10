# ==============================================================================
# Script: toggle-ingestion.ps1
# Descricao: Liga/desliga a camada de ingestao/CDC (Redpanda + Kafka Connect
#            com o connector Debezium Oracle + Airbyte) manualmente, separado
#            da geracao de dados (toggle-shadowtraffic.ps1). Uso tipico: voce
#            quer os bancos rodando e gerando dado, mas nao precisa que o CDC
#            esteja capturando nesse momento -- ou o oposto, quer validar/rodar
#            syncs sem o ShadowTraffic consumindo recursos.
#
# Categorias de uso deste projeto:
#   Geracao:  bancos (start-infra.ps1) + ShadowTraffic  -> toggle-shadowtraffic.ps1
#   Ingestao: bancos (start-infra.ps1) + Redpanda/Kafka Connect/Airbyte -> este script
#
# Uso:
#   .\scripts\toggle-ingestion.ps1 on       # religa Redpanda+Kafka Connect+Airbyte
#   .\scripts\toggle-ingestion.ps1 off      # desliga os tres
#   .\scripts\toggle-ingestion.ps1 status   # mostra estado de cada um
#
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("on", "off", "status")]
    [string]$Action
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot

. "$PSScriptRoot\lib\shadowtraffic-common.ps1"

function Test-AirbyteRunning {
    $c = docker ps -a --filter "name=airbyte-abctl-control-plane" --format "{{.Names}}"
    if (-not $c) { return $null }  # nao instalado
    return Test-ContainerRunning -Name "airbyte-abctl-control-plane"
}

function Show-Status {
    $redpandaState = if (Test-ContainerRunning -Name "redpanda") { "ATIVO" } else { "PARADO" }
    $connectState  = if (Test-ContainerRunning -Name "kafka-connect") { "ATIVO" } else { "PARADO" }
    $airbyteRunning = Test-AirbyteRunning
    $airbyteState = if ($null -eq $airbyteRunning) { "NAO INSTALADO" } elseif ($airbyteRunning) { "ATIVO" } else { "PARADO" }

    Write-Host "Redpanda:      $redpandaState"
    Write-Host "Kafka Connect: $connectState"
    Write-Host "Airbyte:       $airbyteState"

    if (Test-ContainerRunning -Name "kafka-connect") {
        try {
            $connectors = Invoke-RestMethod -Uri "http://localhost:8083/connectors" -Method Get -ErrorAction Stop
            if ($connectors -contains "oracle-ubereats-connector") {
                $s = Invoke-RestMethod -Uri "http://localhost:8083/connectors/oracle-ubereats-connector/status" -Method Get
                Write-Host "  connector oracle-ubereats-connector: $($s.connector.state)"
            } else {
                Write-Host "  connector oracle-ubereats-connector: NAO REGISTRADO"
            }
        } catch {
            Write-Host "  connector: Kafka Connect API ainda nao responde"
        }
    }
}

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

        # Ver mesmo comentario em toggle-shadowtraffic.ps1: "running" nao
        # garante que o Oracle ja aceita conexao, e o connector Debezium
        # precisa conectar nele durante o registro.
        Write-Host "[INFO] Aguardando bancos ficarem prontos (healthcheck)..." -ForegroundColor Cyan
        foreach ($c in @("postgres-ubereats", "oracle-ubereats", "minio-ubereats")) {
            if (-not (Wait-ContainerHealthy -Name $c)) {
                Write-Host "[ERRO] $c nao ficou pronto a tempo. Verifique: docker logs $c" -ForegroundColor Red
                exit 1
            }
        }

        Write-Host "[INFO] Subindo Redpanda + Kafka Connect..." -ForegroundColor Cyan
        docker-compose up -d redpanda kafka-connect | Out-Null

        Register-OracleConnectorIfNeeded

        Write-Host ""
        Write-Host "[INFO] Subindo Airbyte..." -ForegroundColor Cyan
        & "$PSScriptRoot\start-airbyte.ps1"

        Write-Host ""
        Write-Host "[OK] Ingestao LIGADA (Redpanda + Kafka Connect + Airbyte)."
        Write-Host "   Desligar: .\scripts\toggle-ingestion.ps1 off"
    }

    "off" {
        Write-Host "[INFO] Desligando Airbyte..." -ForegroundColor Cyan
        if (Test-AirbyteRunning) {
            & "$PSScriptRoot\stop-airbyte.ps1"
        } else {
            Write-Host "   -> ja estava parado ou nao instalado." -ForegroundColor Gray
        }

        Write-Host ""
        Write-Host "[INFO] Desligando Redpanda + Kafka Connect..." -ForegroundColor Cyan
        docker-compose stop redpanda kafka-connect | Out-Null

        Write-Host ""
        Write-Host "[OK] Ingestao DESLIGADA. Configuracao (connector, sources/destinations) preservada."
        Write-Host "   Religar: .\scripts\toggle-ingestion.ps1 on"
    }
}
