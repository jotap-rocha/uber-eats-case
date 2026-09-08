# ==============================================================================
# Script: toggle-shadowtraffic.ps1
# Descricao: Liga/desliga o gerador ShadowTraffic (gen-unified) manualmente,
#            SEM reiniciar a numeracao dos IDs (users/drivers/orders/payments/
#            restaurants). Cada "on" recalcula "startingFrom" a partir do
#            MAX(id) real nas tabelas antes de subir o container.
#
# Por que este script existe (nao usar apenas docker-compose stop/start):
#   O config gen/unified/uber-eats.json.template usa "startingFrom": N fixo
#   para os campos sequenciais (user_id, driver_id, order_id, payment_id,
#   restaurant_id). Se o container for religado do zero com o mesmo N fixo
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

$repoRoot  = Split-Path -Parent $PSScriptRoot
$envFile   = "$repoRoot\gen\.env"
$jsonPath  = "$repoRoot\gen\unified\uber-eats.json"
$RESTAURANT_TARGET = 500

# ------------------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------------------

function Get-EnvVars {
    if (-not (Test-Path $envFile)) {
        Write-Host "[ERRO] gen\.env nao encontrado. Copie gen\.env.template para gen\.env e preencha as credenciais." -ForegroundColor Red
        exit 1
    }
    return (Get-Content $envFile | Where-Object { $_ -match '=' -and $_ -notmatch '^\s*#' } | ConvertFrom-StringData)
}

function Test-ContainerRunning([string]$name) {
    $running = docker ps --filter "name=$name" --filter "status=running" --format "{{.Names}}"
    return [bool]$running
}

function Get-PgMax([string]$table, [string]$column) {
    $sql = "SELECT COALESCE(MAX($column),0) FROM $table;"
    $out = docker exec postgres-ubereats psql -U $envVars.POSTGRES_USERNAME -d $envVars.POSTGRES_DB -t -A -c $sql
    return [int]($out.Trim())
}

function Get-OracleScalar([string]$sql) {
    $conn = "$($envVars.ORACLE_APP_USERNAME)/$($envVars.ORACLE_APP_PASSWORD)@//localhost:1521/$($envVars.ORACLE_SERVICE)"
    $script = "SET PAGESIZE 0`nSET FEEDBACK OFF`nSET HEADING OFF`nSET VERIFY OFF`n$sql`nexit;`n"
    $lines = $script | docker exec -i oracle-ubereats sqlplus -s $conn
    $value = ($lines | Where-Object { $_.Trim() -match '^\d+$' } | Select-Object -First 1)
    if (-not $value) {
        Write-Host "[ERRO] Nao consegui ler resultado do Oracle para: $sql" -ForegroundColor Red
        Write-Host ($lines -join "`n")
        exit 1
    }
    return [int]($value.Trim())
}

function Show-Status {
    $running = Test-ContainerRunning "gen-unified"
    $state = if ($running) { "ATIVO" } else { "PARADO" }
    Write-Host "Gerador (gen-unified): $state"

    $u = Get-PgMax "users" "user_id"
    $d = Get-PgMax "drivers" "driver_id"
    $o = Get-OracleScalar "SELECT NVL(MAX(order_id),0) FROM UBEREATS.ORDERS;"
    $p = Get-OracleScalar "SELECT NVL(MAX(payment_id),0) FROM UBEREATS.PAYMENTS;"
    $r = Get-OracleScalar "SELECT NVL(COUNT(*),0) FROM UBEREATS.RESTAURANTS;"

    Write-Host "  users:       $u"
    Write-Host "  drivers:     $d"
    Write-Host "  orders:      $o"
    Write-Host "  payments:    $p"
    Write-Host "  restaurants: $r / $RESTAURANT_TARGET"
}

function Sync-StartingPoints {
    Write-Host "[1/3] Calculando pontos de retomada (MAX id atual em cada tabela)..."

    $maxUser    = Get-PgMax "users" "user_id"
    $maxDriver  = Get-PgMax "drivers" "driver_id"
    $maxOrder   = Get-OracleScalar "SELECT NVL(MAX(order_id),0) FROM UBEREATS.ORDERS;"
    $maxPayment = Get-OracleScalar "SELECT NVL(MAX(payment_id),0) FROM UBEREATS.PAYMENTS;"
    $restCount  = Get-OracleScalar "SELECT NVL(COUNT(*),0) FROM UBEREATS.RESTAURANTS;"
    $maxRest    = Get-OracleScalar "SELECT NVL(MAX(restaurant_id),0) FROM UBEREATS.RESTAURANTS;"

    Write-Host "   users=$maxUser drivers=$maxDriver orders=$maxOrder payments=$maxPayment restaurants=$restCount/$RESTAURANT_TARGET"

    Write-Host "[2/3] Injetando segredos do .env (gen\setup-configs.ps1)..."
    & "$repoRoot\gen\setup-configs.ps1" | Out-Null

    Write-Host "[3/3] Ajustando 'startingFrom' no uber-eats.json gerado (sem tocar no template)..."
    $config = Get-Content $jsonPath -Raw | ConvertFrom-Json -Depth 100

    $usersGen = $config.generators | Where-Object { $_.table -eq "users" }
    $usersGen.row.user_id.startingFrom = $maxUser + 1

    $driversGen = $config.generators | Where-Object { $_.table -eq "drivers" }
    $driversGen.fork.key.startingFrom = $maxDriver + 1

    $ordersGen = $config.generators | Where-Object { $_.table -eq "orders" }
    $ordersGen.fork.key.startingFrom = $maxOrder + 1

    $paymentsGen = $config.generators | Where-Object { $_.table -eq "payments" }
    $paymentsGen.fork.key.startingFrom = $maxPayment + 1

    $restGen = $config.generators | Where-Object { $_.table -eq "restaurants" }
    $restGen.row.restaurant_id.startingFrom = $maxRest + 1
    $restGen.localConfigs.maxEvents = [Math]::Max(1, $RESTAURANT_TARGET - $restCount)

    ($config | ConvertTo-Json -Depth 100) | Set-Content -Path $jsonPath -Encoding utf8
    Write-Host "[OK] uber-eats.json atualizado. Nenhum ID sera reaproveitado ao religar."
}

# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------

$envVars = Get-EnvVars

switch ($Action) {

    "status" {
        Show-Status
    }

    "on" {
        foreach ($c in @("postgres-ubereats", "oracle-ubereats", "minio-ubereats")) {
            if (-not (Test-ContainerRunning $c)) {
                Write-Host "[ERRO] $c nao esta rodando. Rode primeiro: .\scripts\start-infra.ps1" -ForegroundColor Red
                exit 1
            }
        }

        if (Test-ContainerRunning "gen-unified") {
            Write-Host "[OK] gen-unified ja esta ativo. Nada a fazer."
            Show-Status
            exit 0
        }

        Sync-StartingPoints

        Write-Host "[INFO] Subindo gen-unified..."
        docker-compose up -d gen-unified | Out-Null

        Write-Host "[OK] Gerador LIGADO, retomando de onde parou."
        Write-Host "   Ver logs:  docker-compose logs -f gen-unified"
        Write-Host "   Desligar:  .\scripts\toggle-shadowtraffic.ps1 off"
    }

    "off" {
        if (-not (Test-ContainerRunning "gen-unified")) {
            Write-Host "[OK] gen-unified ja esta parado."
            exit 0
        }
        docker-compose stop gen-unified | Out-Null
        Write-Host "[OK] Gerador DESLIGADO. Progresso salvo nas tabelas."
        Write-Host "   Religar: .\scripts\toggle-shadowtraffic.ps1 on"
    }
}
