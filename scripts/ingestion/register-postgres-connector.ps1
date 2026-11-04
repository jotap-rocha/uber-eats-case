# ==============================================================================
# Script: register-postgres-connector.ps1
# Descricao: Injeta a senha do usuario do CDC (dbz_ubereats) e o nome do banco
#            (shared/gen/.env) no template do conector Postgres e registra no
#            Kafka Connect via REST API.
# Uso: rodar na regeracao (F5 do modelo fisico), depois que postgres-ubereats
#      (com o usuario e a publicacao do CDC criados no init) e kafka-connect
#      estiverem saudaveis, e ANTES da carga dos dados (F4.0 #5).
# ==============================================================================

$scriptFolder = $PSScriptRoot
$envFile = "$scriptFolder\..\..\shared\gen\.env"

if (-not (Test-Path $envFile)) {
    Write-Host "[ERRO] shared/gen/.env nao encontrado." -ForegroundColor Red
    exit 1
}

$envVars = Get-Content $envFile | Where-Object { $_ -match '=' -and $_ -notmatch '^\s*#' } | ConvertFrom-StringData

foreach ($key in @("POSTGRES_DEBEZIUM_PASSWORD", "POSTGRES_DB")) {
    if (-not $envVars.$key) {
        Write-Host "[ERRO] $key ausente no shared/gen/.env." -ForegroundColor Red
        exit 1
    }
}

$template = "$scriptFolder\..\..\config\shared\debezium\postgres-connector.json.template"
$connectorJson = (Get-Content $template -Raw) `
    -replace "REPLACE_POSTGRES_DEBEZIUM_PASSWORD", $envVars.POSTGRES_DEBEZIUM_PASSWORD `
    -replace "REPLACE_POSTGRES_DB", $envVars.POSTGRES_DB

Write-Host "[INFO] Registrando connector Postgres no Kafka Connect (http://localhost:8083)..." -ForegroundColor Cyan

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
Write-Host "Verificar status: Invoke-RestMethod http://localhost:8083/connectors/postgres-ubereats-connector/status" -ForegroundColor Gray
