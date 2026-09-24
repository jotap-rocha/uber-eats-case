# ==============================================================================
# Script: register-oracle-connector-azure.ps1
# Descricao: Injeta a senha do usuario Debezium e a connection string do
#            Event Hub (gen/.env) no template do connector Oracle da Fase 1/
#            Azure, e registra no cluster Kafka Connect DEDICADO desta fase
#            (porta 8084 -- ver debezium/connect-worker-eventhub.properties.template
#            e docker-compose.yml, servico kafka-connect-azure).
# Uso: rodar depois que oracle-ubereats e kafka-connect-azure estiverem saudaveis.
# ==============================================================================

$scriptFolder = $PSScriptRoot
$envFile = "$scriptFolder\..\gen\.env"

if (-not (Test-Path $envFile)) {
    Write-Host "[ERRO] gen/.env nao encontrado." -ForegroundColor Red
    exit 1
}

$envVars = Get-Content $envFile | Where-Object { $_ -match '=' -and $_ -notmatch '^\s*#' } | ConvertFrom-StringData

$template = "$scriptFolder\oracle-connector-azure.json.template"
$connectorJson = (Get-Content $template -Raw) `
    -replace "REPLACE_ORACLE_DBZ_PASSWORD", $envVars.ORACLE_DBZ_PASSWORD `
    -replace "REPLACE_EVENTHUB_NAMESPACE_CONNECTION_STRING", $envVars.AZURE_EVENTHUB_CONNECTION_STRING `
    -replace "REPLACE_EVENTHUB_NAMESPACE", $envVars.AZURE_EVENTHUB_NAMESPACE

Write-Host "[INFO] Registrando connector Oracle (Azure) no Kafka Connect (http://localhost:8084)..." -ForegroundColor Cyan

try {
    $response = Invoke-RestMethod -Uri "http://localhost:8084/connectors" `
        -Method Post `
        -ContentType "application/json" `
        -Body $connectorJson
    Write-Host "[OK] Connector registrado: $($response.name)" -ForegroundColor Green
} catch {
    Write-Host "[ERRO] Falha ao registrar connector: $($_.Exception.Message)" -ForegroundColor Red
    if ($_.ErrorDetails) { Write-Host $_.ErrorDetails.Message -ForegroundColor Yellow }
    exit 1
}

Write-Host ""
Write-Host "Verificar status: Invoke-RestMethod http://localhost:8084/connectors/oracle-ubereats-connector-azure/status" -ForegroundColor Gray
Write-Host "[AVISO] Este connector le o mesmo LogMiner do Oracle que o connector local (porta 8083) -- evitar rodar os dois ao mesmo tempo em producao real (ver BUILD_REPORT, risco de concorrencia LogMiner)." -ForegroundColor Yellow
