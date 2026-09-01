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

# Sobe o gerador unificado (Postgres real + MinIO no mesmo processo)
docker-compose up -d gen-unified

Write-Host ""
Write-Host "[OK] Gerador ShadowTraffic iniciado em background."
Write-Host ""
Write-Host "Gerador ativo:"
Write-Host "   -> gen-unified: Populando 'users'/'drivers' no Postgres e eventos JSON no bucket 'uber-eats' (mesmo processo, permite lookup cruzado)"
Write-Host ""
Write-Host "Monitoramento:"
Write-Host "   -> Ver logs: docker-compose logs -f gen-unified"
Write-Host "   -> Parar gerador: .\scripts\stop-generators.ps1"


