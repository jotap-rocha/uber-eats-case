# ==============================================================================
# Script: register-oracle-connector.ps1
# Descricao: Injeta a senha do usuario Debezium (gen/.env) no template do
#            connector e registra no Kafka Connect via REST API.
# Uso: rodar depois que oracle-ubereats e kafka-connect estiverem saudaveis.
# ==============================================================================

$scriptFolder = $PSScriptRoot
$envFile = "$scriptFolder\..\gen\.env"

if (-not (Test-Path $envFile)) {
    Write-Host "[ERRO] gen/.env nao encontrado." -ForegroundColor Red
    exit 1
}

$envVars = Get-Content $envFile | Where-Object { $_ -match '=' -and $_ -notmatch '^\s*#' } | ConvertFrom-StringData

$template = "$scriptFolder\oracle-connector.json.template"
$connectorJson = (Get-Content $template -Raw) -replace "REPLACE_ORACLE_DBZ_PASSWORD", $envVars.ORACLE_DBZ_PASSWORD

Write-Host "[INFO] Registrando connector Oracle no Kafka Connect (http://localhost:8083)..." -ForegroundColor Cyan

try {
    $response = Invoke-RestMethod -Uri "http://localhost:8083/connectors" `
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
Write-Host "Verificar status: Invoke-RestMethod http://localhost:8083/connectors/oracle-ubereats-connector/status" -ForegroundColor Gray
