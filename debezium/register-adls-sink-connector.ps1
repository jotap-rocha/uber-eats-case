# ==============================================================================
# Script: register-adls-sink-connector.ps1
# Descricao: Injeta o nome do Storage Account (gen/.env) no template do sink
#            connector ADLS e registra no cluster Kafka Connect dedicado da
#            Fase 1/Azure (porta 8084). Consome os mesmos topicos que o
#            Stream Analytics tambem le (DESIGN, Decisao 1 -- captura unica,
#            2 consumidores) -- nao abre nenhuma captura nova.
# Uso: rodar depois que kafka-connect-azure estiver saudavel e os connectors
#      source (Postgres via Airbyte, Oracle via register-oracle-connector-azure.ps1)
#      ja estiverem publicando no Event Hub.
# ==============================================================================

$scriptFolder = $PSScriptRoot
$envFile = "$scriptFolder\..\gen\.env"

if (-not (Test-Path $envFile)) {
    Write-Host "[ERRO] gen/.env nao encontrado." -ForegroundColor Red
    exit 1
}

$envVars = Get-Content $envFile | Where-Object { $_ -match '=' -and $_ -notmatch '^\s*#' } | ConvertFrom-StringData

$template = "$scriptFolder\adls-sink-connector.json.template"
$connectorJson = (Get-Content $template -Raw) -replace "REPLACE_STORAGE_ACCOUNT", $envVars.AZURE_STORAGE_ACCOUNT_NAME

Write-Host "[INFO] Registrando sink connector ADLS no Kafka Connect (http://localhost:8084)..." -ForegroundColor Cyan

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
Write-Host "Verificar status: Invoke-RestMethod http://localhost:8084/connectors/adls-bronze-sink-connector/status" -ForegroundColor Gray
