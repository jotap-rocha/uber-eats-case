# ==============================================================================
# Script: stop-infra.ps1
# Descricao: Para APENAS os bancos (Postgres + Oracle + MinIO + Mongo)
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "[INFO] Parando APENAS os bancos..."

docker-compose stop postgres-ubereats oracle-ubereats minio-ubereats mongo-ubereats

Write-Host ""
Write-Host "[OK] Bancos parados."
Write-Host "   -> Os volumes (dados) estao preservados."
Write-Host "   -> Para iniciar novamente: .\scripts\start-infra.ps1"
Write-Host ""
Write-Host "[AVISO] ShadowTraffic e ingestao/CDC (se estiverem rodando) vao falhar sem os bancos."
Write-Host "   -> Parar geracao: .\scripts\toggle-shadowtraffic.ps1 off"
Write-Host "   -> Parar ingestao: .\scripts\toggle-ingestion.ps1 off"
