# ==============================================================================
# Lib: shadowtraffic-common.ps1
# Descricao: Funcoes compartilhadas entre toggle-shadowtraffic.ps1 e
#            shadowtraffic-report-loop.ps1 (leitura de .env, contagem por
#            tabela via Postgres/Oracle). Dot-source, nao executa nada sozinho.
#
# Uso:
#   . "$PSScriptRoot\lib\shadowtraffic-common.ps1"
#   $envVars = Get-EnvVars -RepoRoot $repoRoot
#   $snap = Get-GeneratorSnapshot -EnvVars $envVars
# ==============================================================================

function Get-EnvVars {
    param([Parameter(Mandatory = $true)][string]$RepoRoot)

    $envFile = "$RepoRoot\gen\.env"
    if (-not (Test-Path $envFile)) {
        Write-Host "[ERRO] gen\.env nao encontrado. Copie gen\.env.template para gen\.env e preencha as credenciais." -ForegroundColor Red
        exit 1
    }
    return (Get-Content $envFile | Where-Object { $_ -match '=' -and $_ -notmatch '^\s*#' } | ConvertFrom-StringData)
}

function Test-ContainerRunning {
    param([Parameter(Mandatory = $true)][string]$Name)
    $running = docker ps --filter "name=$Name" --filter "status=running" --format "{{.Names}}"
    return [bool]$running
}

function Get-PgMax {
    param(
        [Parameter(Mandatory = $true)]$EnvVars,
        [Parameter(Mandatory = $true)][string]$Table,
        [Parameter(Mandatory = $true)][string]$Column
    )
    $sql = "SELECT COALESCE(MAX($Column),0) FROM $Table;"
    $out = docker exec postgres-ubereats psql -U $EnvVars.POSTGRES_USERNAME -d $EnvVars.POSTGRES_DB -t -A -c $sql
    return [int]($out.Trim())
}

function Get-OracleScalar {
    param(
        [Parameter(Mandatory = $true)]$EnvVars,
        [Parameter(Mandatory = $true)][string]$Sql
    )
    $conn = "$($EnvVars.ORACLE_APP_USERNAME)/$($EnvVars.ORACLE_APP_PASSWORD)@//localhost:1521/$($EnvVars.ORACLE_SERVICE)"
    $script = "SET PAGESIZE 0`nSET FEEDBACK OFF`nSET HEADING OFF`nSET VERIFY OFF`n$Sql`nexit;`n"
    $lines = $script | docker exec -i oracle-ubereats sqlplus -s $conn
    $value = ($lines | Where-Object { $_.Trim() -match '^\d+$' } | Select-Object -First 1)
    if (-not $value) {
        Write-Host "[ERRO] Nao consegui ler resultado do Oracle para: $Sql" -ForegroundColor Red
        Write-Host ($lines -join "`n")
        exit 1
    }
    return [int]($value.Trim())
}

# Retorna um hashtable com a contagem atual de cada tabela sensivel.
# Usado tanto pelo "status" quanto pelo loop de report.
function Get-GeneratorSnapshot {
    param([Parameter(Mandatory = $true)]$EnvVars)

    return [ordered]@{
        users       = Get-PgMax -EnvVars $EnvVars -Table "users" -Column "user_id"
        drivers     = Get-PgMax -EnvVars $EnvVars -Table "drivers" -Column "driver_id"
        orders      = Get-OracleScalar -EnvVars $EnvVars -Sql "SELECT NVL(MAX(order_id),0) FROM UBEREATS.ORDERS;"
        payments    = Get-OracleScalar -EnvVars $EnvVars -Sql "SELECT NVL(MAX(payment_id),0) FROM UBEREATS.PAYMENTS;"
        restaurants = Get-OracleScalar -EnvVars $EnvVars -Sql "SELECT NVL(COUNT(*),0) FROM UBEREATS.RESTAURANTS;"
    }
}
