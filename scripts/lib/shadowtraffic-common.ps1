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
    $running = docker ps --filter "name=$Name" --filter "status=running" --format "{{.Names}}" 2>$null
    if ($LASTEXITCODE -ne 0) {
        # Docker CLI/daemon indisponivel (ex.: Docker Desktop reiniciando) -- nao
        # confundir com "container parado". "docker ps" as vezes escreve o erro
        # no stdout em vez de stderr, entao checar so [bool]$running nao basta.
        Write-Host "[AVISO] docker ps falhou (Docker Desktop instavel/reiniciando?) -- assumindo $Name PARADO." -ForegroundColor Yellow
        return $false
    }
    return [bool]($running -eq $Name)
}

# Espera um container ficar "healthy" (Docker healthcheck). Containers sem
# healthcheck definido no compose (mongo, redpanda, kafka-connect, gen-unified)
# retornam Health.Status vazio -- nesse caso "running" ja basta. Existe porque
# o Oracle fica "running" bem antes do listener registrar o FREEPDB1: scripts
# encadeados (ex. start-all.ps1 -> toggle-shadowtraffic.ps1) batiam em
# ORA-12514 ao consultar MAX(id) logo depois do "docker-compose up".
function Wait-ContainerHealthy {
    param(
        [Parameter(Mandatory = $true)][string]$Name,
        [int]$TimeoutSeconds = 120,
        [int]$IntervalSeconds = 3
    )

    if (-not (Test-ContainerRunning -Name $Name)) {
        return $false
    }

    $elapsed = 0
    $health = $null
    while ($elapsed -lt $TimeoutSeconds) {
        $health = docker inspect --format='{{.State.Health.Status}}' $Name 2>$null
        if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($health) -or $health -eq "<no value>") {
            return $true
        }
        if ($health -eq "healthy") {
            return $true
        }
        if ($health -eq "unhealthy") {
            Write-Host "[ERRO] $Name esta 'unhealthy'. Verifique: docker logs $Name" -ForegroundColor Red
            return $false
        }
        Start-Sleep -Seconds $IntervalSeconds
        $elapsed += $IntervalSeconds
    }

    Write-Host "[AVISO] $Name ainda nao ficou 'healthy' apos $TimeoutSeconds s (status atual: $health)." -ForegroundColor Yellow
    return $false
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
        [Parameter(Mandatory = $true)][string]$Sql,
        [int]$MaxRetries = 6,
        [int]$RetryDelaySeconds = 5
    )
    $conn = "$($EnvVars.ORACLE_APP_USERNAME)/$($EnvVars.ORACLE_APP_PASSWORD)@//localhost:1521/$($EnvVars.ORACLE_SERVICE)"
    $script = "SET PAGESIZE 0`nSET FEEDBACK OFF`nSET HEADING OFF`nSET VERIFY OFF`n$Sql`nexit;`n"

    # O container fica "healthy" as vezes antes do listener re-registrar o
    # servico FREEPDB1 para conexoes TCP externas (gap conhecido da imagem
    # gvenzl/oracle-free) -- ORA-12514 nesse instante e transitorio, nao erro
    # real. Por isso tenta de novo em vez de confiar so no healthcheck do Docker.
    for ($attempt = 1; $attempt -le $MaxRetries; $attempt++) {
        $lines = $script | docker exec -i oracle-ubereats sqlplus -s $conn
        $value = ($lines | Where-Object { $_.Trim() -match '^\d+$' } | Select-Object -First 1)
        if ($value) {
            return [int]($value.Trim())
        }

        $output = ($lines -join "`n")
        $isTransient = $output -match 'ORA-12514|ORA-12541|ORA-12528|ORA-01034|ORA-12537'
        if ($isTransient -and $attempt -lt $MaxRetries) {
            Write-Host "   [AVISO] Oracle ainda nao aceita conexoes (tentativa $attempt/$MaxRetries) -- aguardando ${RetryDelaySeconds}s..." -ForegroundColor Yellow
            Start-Sleep -Seconds $RetryDelaySeconds
            continue
        }

        Write-Host "[ERRO] Nao consegui ler resultado do Oracle para: $Sql" -ForegroundColor Red
        Write-Host $output
        exit 1
    }
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

# Garante o connector Debezium Oracle registrado no Kafka Connect. Kafka
# Connect so o restaura sozinho a partir do topico connect_configs se ja
# estava registrado antes (mesmo redpanda/volume) -- num ambiente 100% novo,
# ou apos "docker-compose down -v", precisa ser criado na primeira vez.
# Chamado por toggle-ingestion.ps1 e start-all.ps1 (nao por start-infra.ps1 --
# esse fica so nos bancos).
function Register-OracleConnectorIfNeeded {
    param([string]$RegisterScript = "$PSScriptRoot\..\..\debezium\register-oracle-connector.ps1")

    Write-Host "[CDC] Verificando connector Debezium Oracle..." -ForegroundColor Cyan
    $connectReady = $false
    # Kafka Connect recem-criado (JVM + scan de plugins) pode levar mais de
    # 60s para responder -- 20x3s ja gerou falso "nao respondeu a tempo" com
    # o connector na verdade ja registrado (ver toggle-ingestion.ps1 status).
    for ($i = 0; $i -lt 40; $i++) {
        try {
            Invoke-RestMethod -Uri "http://localhost:8083/connectors" -Method Get -ErrorAction Stop | Out-Null
            $connectReady = $true
            break
        } catch {
            Start-Sleep -Seconds 3
        }
    }

    if (-not $connectReady) {
        Write-Host "   [AVISO] Kafka Connect nao respondeu a tempo. Rode manualmente depois: $RegisterScript" -ForegroundColor Yellow
        return
    }

    $connectors = Invoke-RestMethod -Uri "http://localhost:8083/connectors" -Method Get
    if ($connectors -contains "oracle-ubereats-connector") {
        Write-Host "   [OK] Connector ja registrado (restaurado do estado anterior)." -ForegroundColor Green
    } else {
        Write-Host "   [INFO] Connector nao encontrado -- registrando pela primeira vez..." -ForegroundColor Gray
        & $RegisterScript
    }
}
