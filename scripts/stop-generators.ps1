# ==============================================================================
# Script: stop-generators.ps1
# Descrição: Para APENAS os geradores ShadowTraffic
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "🛑 Parando APENAS os geradores ShadowTraffic..."

# Para apenas os geradores
docker-compose stop gen-drivers gen-users gen-minio

Write-Host ""
Write-Host "✅ Geradores parados."
Write-Host "   -> A infraestrutura (Postgres + MinIO) permanece ativa."
Write-Host "   -> Para reiniciar geradores: .\scripts\start-generators.ps1"
Write-Host ""
Write-Host "💡 Motivos para parar geradores:"
Write-Host "   -> Economizar licença ShadowTraffic"
Write-Host "   -> Dados já suficientes para testes"
Write-Host "   -> Desenvolvimento local sem geração contínua"

