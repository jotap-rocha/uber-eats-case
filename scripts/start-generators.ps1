# ==============================================================================
# Script: start-generators.ps1
# Descrição: Sobe APENAS os geradores ShadowTraffic (requer infra ativa)
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "🎲 Verificando se a infraestrutura está ativa..."

# Verifica se o Postgres está rodando
$postgresRunning = docker ps --filter "name=postgres-ubereats" --filter "status=running" --format "{{.Names}}"
$minioRunning = docker ps --filter "name=minio-ubereats" --filter "status=running" --format "{{.Names}}"

if (-not $postgresRunning -or -not $minioRunning) {
    Write-Host "❌ ERRO: A infraestrutura não está rodando!"
    Write-Host "   Execute primeiro: .\scripts\start-infra.ps1"
    exit 1
}

Write-Host "✅ Infraestrutura ativa detectada."
Write-Host ""
Write-Host "🚀 1/2: Injetando segredos do .env nos arquivos .json..."
.\gen\setup-configs.ps1

Write-Host ""
Write-Host "🚀 2/2: Iniciando geradores ShadowTraffic..."
Write-Host "   (Os geradores vão começar a popular os dados agora.)"

# Sobe apenas os geradores
docker-compose up -d gen-drivers gen-users gen-minio

Write-Host ""
Write-Host "✅ Geradores ShadowTraffic iniciados em background."
Write-Host ""
Write-Host "📊 Geradores ativos:"
Write-Host "   -> gen-drivers: Populando tabela 'drivers' no Postgres"
Write-Host "   -> gen-users: Populando tabela 'users' no Postgres"
Write-Host "   -> gen-minio: Gerando eventos JSON no bucket 'uber-eats'"
Write-Host ""
Write-Host "💡 Monitoramento:"
Write-Host "   -> Ver logs: docker-compose logs -f gen-drivers gen-users gen-minio"
Write-Host "   -> Parar geradores: .\scripts\stop-generators.ps1"

