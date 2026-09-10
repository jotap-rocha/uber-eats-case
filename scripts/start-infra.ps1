# ==============================================================================
# Script: start-infra.ps1
# Descricao: Inicia APENAS os bancos (Postgres + Oracle + MinIO + Mongo).
#            Base comum para as duas categorias de uso: geracao de dados
#            (toggle-shadowtraffic.ps1) e ingestao/CDC (toggle-ingestion.ps1).
#            Nao inclui Redpanda/Kafka Connect nem Airbyte -- ver
#            toggle-ingestion.ps1 para isso.
# ==============================================================================

Write-Host "[INICIO] Iniciando APENAS os bancos (Postgres + Oracle + MinIO + Mongo)..." -ForegroundColor Cyan
Write-Host ""

# --- FUNCAO: Verificar e Iniciar Docker Desktop ---
function Start-DockerDesktop {
    Write-Host "[DOCKER] Verificando Docker Desktop..." -ForegroundColor Yellow

    # Tenta executar docker ps para verificar se esta rodando
    $dockerRunning = $false
    try {
        docker ps 2>&1 | Out-Null
        $dockerRunning = $?
    } catch {
        $dockerRunning = $false
    }

    if ($dockerRunning) {
        Write-Host "[DOCKER] Docker Desktop ja esta rodando!" -ForegroundColor Green
        return
    }

    Write-Host "[DOCKER] Docker Desktop nao esta rodando. Iniciando..." -ForegroundColor Yellow

    # Caminho padrao do Docker Desktop
    $dockerPath = "C:\Program Files\Docker\Docker\Docker Desktop.exe"

    if (-not (Test-Path $dockerPath)) {
        Write-Host "[ERRO] Docker Desktop nao encontrado em: $dockerPath" -ForegroundColor Red
        Write-Host "Por favor, inicie o Docker Desktop manualmente." -ForegroundColor Red
        exit 1
    }

    # Inicia o Docker Desktop
    Start-Process -FilePath $dockerPath

    # Aguarda o Docker ficar pronto (max 120 segundos)
    Write-Host "[DOCKER] Aguardando Docker Desktop inicializar..." -ForegroundColor Yellow
    $timeout = 120
    $elapsed = 0

    while ($elapsed -lt $timeout) {
        Start-Sleep -Seconds 3
        $elapsed += 3

        try {
            docker ps 2>&1 | Out-Null
            if ($?) {
                Write-Host "[DOCKER] Docker Desktop iniciado com sucesso! ($elapsed segundos)" -ForegroundColor Green
                Write-Host ""
                return
            }
        } catch {
            # Continua aguardando
        }

        Write-Host "   Aguardando... ($elapsed/$timeout segundos)" -ForegroundColor Gray
    }

    Write-Host "[ERRO] Docker Desktop nao iniciou no tempo esperado." -ForegroundColor Red
    Write-Host "Por favor, verifique o Docker Desktop manualmente." -ForegroundColor Red
    exit 1
}

# --- Inicia Docker Desktop ---
Start-DockerDesktop

# --- Copiar .env para raiz (docker-compose precisa) ---
Write-Host "[SETUP] Preparando variaveis de ambiente..." -ForegroundColor Cyan
if (Test-Path "gen\.env") {
    Copy-Item -Path "gen\.env" -Destination ".env" -Force
    Write-Host "   -> Arquivo .env copiado para raiz (temporario)" -ForegroundColor Gray
} else {
    Write-Host "[ERRO] Arquivo gen/.env nao encontrado!" -ForegroundColor Red
    Write-Host "Execute: copy gen\.env.template gen\.env" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# --- Sobe os bancos ---
Write-Host "[INFRA] Iniciando Postgres + Oracle + MinIO + Mongo..." -ForegroundColor Cyan
Write-Host "   (Isso pode levar um minuto ou dois... aguardando health checks.)" -ForegroundColor Gray

docker-compose up -d postgres-ubereats oracle-ubereats minio-ubereats minio-setup mongo-ubereats

Write-Host ""
Write-Host "[OK] Bancos iniciados em background." -ForegroundColor Green
Write-Host ""
Write-Host "Status dos servicos:" -ForegroundColor White
Write-Host "   -> Postgres: localhost:5432 (Tabelas criadas automaticamente)" -ForegroundColor White
Write-Host "   -> Oracle: localhost:1521/FREEPDB1" -ForegroundColor White
Write-Host "   -> MinIO API: http://localhost:9000" -ForegroundColor White
Write-Host "   -> MinIO Console: http://localhost:9001 (credenciais conforme gen/.env)" -ForegroundColor White
Write-Host "   -> Bucket 'uber-eats': Criado automaticamente" -ForegroundColor Gray
Write-Host "   -> Mongo: localhost:27017 (satelite Perfil de Restaurante, seed unico)" -ForegroundColor White
Write-Host ""
Write-Host "Proximos passos (escolha conforme o que voce vai fazer agora):" -ForegroundColor White
Write-Host "   -> Gerar dados:        .\scripts\toggle-shadowtraffic.ps1 on" -ForegroundColor Gray
Write-Host "   -> Rodar CDC/ingestao: .\scripts\toggle-ingestion.ps1 on" -ForegroundColor Gray
Write-Host "   -> Ver logs: docker-compose logs -f" -ForegroundColor Gray
