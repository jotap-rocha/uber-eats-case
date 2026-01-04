# ==============================================================================
# Script: stop-generators.ps1
# Descricao: Para APENAS os geradores ShadowTraffic
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "[INFO] Parando APENAS os geradores ShadowTraffic..."

# Para apenas os geradores
docker-compose stop gen-drivers gen-users gen-minio

Write-Host ""
Write-Host "[OK] Geradores parados."
Write-Host "   -> A infraestrutura (Postgres + MinIO) permanece ativa."
Write-Host "   -> Para reiniciar geradores: .\scripts\start-generators.ps1"
Write-Host ""
Write-Host "Motivos para parar geradores:"
Write-Host "   -> Economizar licenca ShadowTraffic"
Write-Host "   -> Dados ja suficientes para testes"
Write-Host "   -> Desenvolvimento local sem geracao continua"


