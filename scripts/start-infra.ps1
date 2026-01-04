# ==============================================================================
# Script: start-infra.ps1
# Descricao: Sobe APENAS a infraestrutura (Postgres + MinIO + Setup)
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "[INICIO] Iniciando APENAS a infraestrutura (Postgres + MinIO)..."
Write-Host "   (Isso pode levar um minuto... aguardando health checks.)"

# Sobe apenas os servicos de infraestrutura
docker-compose up -d postgres-ubereats minio-ubereats minio-setup

Write-Host ""
Write-Host "[OK] Infraestrutura iniciada em background."
Write-Host ""
Write-Host "Status dos servicos:"
Write-Host "   -> Postgres: localhost:5432 (Tabelas criadas automaticamente)"
Write-Host "   -> MinIO API: http://localhost:9000"
Write-Host "   -> MinIO Console: http://localhost:9001 (credenciais conforme gen/.env)"
Write-Host "   -> Bucket 'uber-eats': Criado automaticamente"
Write-Host ""
Write-Host "Proximos passos:"
Write-Host "   -> Para popular dados: .\scripts\start-generators.ps1"
Write-Host "   -> Ver logs: docker-compose logs -f"


