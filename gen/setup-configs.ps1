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

# 2. Configura o gerador de Drivers (usando o caminho completo)
$templateDriver = "$scriptFolder\postgres\drivers.json.template"
$configFileDriver = "$scriptFolder\postgres\drivers.json" 

Write-Host "   -> Gerando $configFileDriver..."
(Get-Content $templateDriver) `
    -replace "REPLACE_POSTGRES_HOST", $envVars.POSTGRES_HOST `
    -replace "REPLACE_POSTGRES_PORT", $envVars.POSTGRES_PORT `
    -replace "REPLACE_POSTGRES_DB", $envVars.POSTGRES_DB `
    -replace "REPLACE_POSTGRES_USER", $envVars.POSTGRES_USERNAME `
    -replace "REPLACE_POSTGRES_PASSWORD", $envVars.POSTGRES_PASSWORD |
    Set-Content $configFileDriver

# 3. Configura o gerador de Users (usando o caminho completo)
$templateUser = "$scriptFolder\postgres\users.json.template" 
$configFileUser = "$scriptFolder\postgres\users.json" 

Write-Host "   -> Gerando $configFileUser..."
(Get-Content $templateUser) `
    -replace "REPLACE_POSTGRES_HOST", $envVars.POSTGRES_HOST `
    -replace "REPLACE_POSTGRES_PORT", $envVars.POSTGRES_PORT `
    -replace "REPLACE_POSTGRES_DB", $envVars.POSTGRES_DB `
    -replace "REPLACE_POSTGRES_USER", $envVars.POSTGRES_USERNAME `
    -replace "REPLACE_POSTGRES_PASSWORD", $envVars.POSTGRES_PASSWORD |
    Set-Content $configFileUser

Write-Host "✅ Arquivos .json do Postgres gerados com sucesso!"