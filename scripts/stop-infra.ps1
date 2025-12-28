# ==============================================================================
# Script: stop-infra.ps1
# Descrição: Para APENAS a infraestrutura (Postgres + MinIO)
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "🛑 Parando APENAS a infraestrutura..."

# Para apenas os serviços de infraestrutura
docker-compose stop postgres-ubereats minio-ubereats

Write-Host ""
Write-Host "✅ Infraestrutura parada."
Write-Host "   -> Os volumes (dados) estão preservados."
Write-Host "   -> Para iniciar novamente: .\scripts\start-infra.ps1"
Write-Host ""
Write-Host "⚠️  IMPORTANTE: Os geradores ShadowTraffic (se estiverem rodando) podem falhar."
Write-Host "   -> Para parar os geradores também: .\scripts\stop-generators.ps1"

