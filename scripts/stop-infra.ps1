# ==============================================================================
# Script: stop-infra.ps1
# Descricao: Para APENAS a infraestrutura (Postgres + MinIO)
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "[INFO] Parando APENAS a infraestrutura..."

# Para apenas os servicos de infraestrutura
docker-compose stop postgres-ubereats minio-ubereats

Write-Host ""
Write-Host "[OK] Infraestrutura parada."
Write-Host "   -> Os volumes (dados) estao preservados."
Write-Host "   -> Para iniciar novamente: .\scripts\start-infra.ps1"
Write-Host ""
Write-Host "[AVISO] Os geradores ShadowTraffic (se estiverem rodando) podem falhar."
Write-Host "   -> Para parar os geradores tambem: .\scripts\stop-generators.ps1"


