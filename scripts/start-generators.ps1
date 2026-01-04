# ==============================================================================
# Script: start-generators.ps1
# Descricao: Sobe APENAS os geradores ShadowTraffic (requer infra ativa)
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "[INFO] Verificando se a infraestrutura esta ativa..."

# Verifica se o Postgres esta rodando
$postgresRunning = docker ps --filter "name=postgres-ubereats" --filter "status=running" --format "{{.Names}}"
$minioRunning = docker ps --filter "name=minio-ubereats" --filter "status=running" --format "{{.Names}}"

if (-not $postgresRunning -or -not $minioRunning) {
    Write-Host "[ERRO] A infraestrutura nao esta rodando!"
    Write-Host "   Execute primeiro: .\scripts\start-infra.ps1"
    exit 1
}

Write-Host "[OK] Infraestrutura ativa detectada."
Write-Host ""
Write-Host "[1/2] Injetando segredos do .env nos arquivos .json..."
.\gen\setup-configs.ps1

Write-Host ""
Write-Host "[2/2] Iniciando geradores ShadowTraffic..."
Write-Host "   (Os geradores vao comecar a popular os dados agora.)"

# Sobe apenas os geradores
docker-compose up -d gen-drivers gen-users gen-minio

Write-Host ""
Write-Host "[OK] Geradores ShadowTraffic iniciados em background."
Write-Host ""
Write-Host "Geradores ativos:"
Write-Host "   -> gen-drivers: Populando tabela 'drivers' no Postgres"
Write-Host "   -> gen-users: Populando tabela 'users' no Postgres"
Write-Host "   -> gen-minio: Gerando eventos JSON no bucket 'uber-eats'"
Write-Host ""
Write-Host "Monitoramento:"
Write-Host "   -> Ver logs: docker-compose logs -f gen-drivers gen-users gen-minio"
Write-Host "   -> Parar geradores: .\scripts\stop-generators.ps1"


