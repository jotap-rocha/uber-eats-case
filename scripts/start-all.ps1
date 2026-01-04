# ==============================================================================
# Script: start-all.ps1
# Descricao: Inicia TODA a infraestrutura (Postgres + MinIO + ShadowTraffic)
# ==============================================================================

Write-Host "[INICIO] Iniciando TODA a fabrica de dados (Infra + Setup + Geradores)..." -ForegroundColor Cyan
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

# --- Passo 1: Injecao de Secrets ---
Write-Host "[1/3] Injetando segredos do .env nos arquivos .json..." -ForegroundColor Cyan
& "$PSScriptRoot\..\gen\setup-configs.ps1"

if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERRO] Falha ao injetar segredos. Verifique o arquivo gen/.env" -ForegroundColor Red
    exit 1
}

Write-Host ""

# --- Passo 2: Sobe Infraestrutura ---
Write-Host "[2/3] Iniciando infraestrutura (Postgres + MinIO)..." -ForegroundColor Cyan
Write-Host "   (Isso pode levar um minuto... O Postgres e o MinIO estao se auto-configurando.)" -ForegroundColor Gray
docker-compose up -d postgres-ubereats minio-ubereats minio-setup

Write-Host ""

# --- Passo 3: Sobe Geradores ---
Write-Host "[3/3] Iniciando geradores ShadowTraffic..." -ForegroundColor Cyan
docker-compose up -d gen-drivers gen-users gen-minio

Write-Host ""
Write-Host "[OK] Fabrica de dados iniciada em background." -ForegroundColor Green
Write-Host ""
Write-Host "Acessos Rapidos:" -ForegroundColor White
Write-Host "   -> Postgres: localhost:5432 (credenciais conforme gen/.env)" -ForegroundColor White
Write-Host "   -> MinIO Console: http://localhost:9001 (credenciais conforme gen/.env)" -ForegroundColor White
Write-Host "   -> Bucket: uber-eats (criado automaticamente)" -ForegroundColor Gray
Write-Host ""
Write-Host "Comandos uteis:" -ForegroundColor White
Write-Host "   -> Ver logs: docker-compose logs -f" -ForegroundColor Gray
Write-Host "   -> Ver status: docker-compose ps" -ForegroundColor Gray
Write-Host "   -> Parar tudo: .\scripts\stop-all.ps1" -ForegroundColor Gray
Write-Host "   -> Parar apenas geradores: .\scripts\stop-generators.ps1" -ForegroundColor Gray
