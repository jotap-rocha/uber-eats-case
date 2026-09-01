Write-Host "🚀 Iniciando injeção de segredos do .env..."

# $PSScriptRoot é a "mágica": é a pasta onde o script (setup-configs.ps1) está.
$scriptFolder = $PSScriptRoot

# 1. Carrega o .env (que está na MESMA pasta do script)
$envFile = "$scriptFolder\.env"
if (-not (Test-Path $envFile)) {
    Write-Host "❌ ERRO: Arquivo .env não encontrado em $envFile"
    exit 1
}
$envVars = Get-Content $envFile | Where-Object { $_ -match '=' -and $_ -notmatch '^\s*#' } | ConvertFrom-StringData

# 2. Configura o gerador unificado (Postgres real + MinIO no mesmo processo)
$templateUnified = "$scriptFolder\unified\uber-eats.json.template"
$configFileUnified = "$scriptFolder\unified\uber-eats.json"

Write-Host "   -> Gerando $configFileUnified..."
(Get-Content $templateUnified) `
    -replace "REPLACE_POSTGRES_HOST", $envVars.POSTGRES_HOST `
    -replace "REPLACE_POSTGRES_PORT", $envVars.POSTGRES_PORT `
    -replace "REPLACE_POSTGRES_DB", $envVars.POSTGRES_DB `
    -replace "REPLACE_POSTGRES_USER", $envVars.POSTGRES_USERNAME `
    -replace "REPLACE_POSTGRES_PASSWORD", $envVars.POSTGRES_PASSWORD |
    Set-Content $configFileUnified

Write-Host "✅ Arquivo .json unificado (Postgres + MinIO) gerado com sucesso!"
