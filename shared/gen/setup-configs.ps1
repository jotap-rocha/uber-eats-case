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

# 2. Configura o gerador unificado (cadastros no Oracle e no Postgres, F5.4 do modelo fisico)
$templateUnified = "$scriptFolder\unified\uber-eats.json.template"
$configFileUnified = "$scriptFolder\unified\uber-eats.json"

# Lista de cidades para os cadastros sortearem cidade e coordenada perto do centro. Mesma fonte do
# seed que grava cities nos dois bancos (shared/gen/reference/cities.csv), entao as listas batem.
$citiesJson = (Import-Csv "$scriptFolder\reference\cities.csv" -Encoding UTF8 | ForEach-Object {
    '{"city_id": ' + $_.city_id + ', "lat": ' + $_.center_latitude + ', "lon": ' + $_.center_longitude + '}'
}) -join ', '
$citiesJson = "[$citiesJson]"

Write-Host "   -> Gerando $configFileUnified..."
(Get-Content $templateUnified) `
    -replace "REPLACE_POSTGRES_HOST", $envVars.POSTGRES_HOST `
    -replace "REPLACE_POSTGRES_PORT", $envVars.POSTGRES_PORT `
    -replace "REPLACE_POSTGRES_DB", $envVars.POSTGRES_DB `
    -replace "REPLACE_POSTGRES_USER", $envVars.POSTGRES_USERNAME `
    -replace "REPLACE_POSTGRES_PASSWORD", $envVars.POSTGRES_PASSWORD `
    -replace "REPLACE_ORACLE_HOST", $envVars.ORACLE_HOST `
    -replace "REPLACE_ORACLE_PORT", $envVars.ORACLE_PORT `
    -replace "REPLACE_ORACLE_SERVICE", $envVars.ORACLE_SERVICE `
    -replace "REPLACE_ORACLE_USER", $envVars.ORACLE_APP_USERNAME `
    -replace "REPLACE_ORACLE_PASSWORD", $envVars.ORACLE_APP_PASSWORD `
    -replace "REPLACE_CITIES_JSON", $citiesJson |
    Set-Content $configFileUnified

Write-Host "✅ Arquivo .json unificado (cadastros Oracle + Postgres) gerado com sucesso!"

# 3. O seed do MongoDB saiu daqui: os perfis sao gravados pelo seed em Python do simulador
#    (F3, decisao 1, do modelo fisico); o init so cria a colecao (shared/mongo/init/).

