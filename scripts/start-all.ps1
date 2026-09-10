# ==============================================================================
# Script: start-all.ps1
# Descricao: Inicia literalmente tudo -- bancos + ingestao/CDC + geracao de
#            dados -- delegando para os scripts especificos de cada categoria
#            (start-infra.ps1, toggle-ingestion.ps1, toggle-shadowtraffic.ps1)
#            em vez de duplicar comandos docker-compose aqui.
#
# Uso tipico: primeira execucao do projeto, ou demo/apresentacao onde tudo
# precisa estar de pe. No dia a dia, prefira ligar so a categoria que voce
# precisa (ver scripts/README.md).
# ==============================================================================

Write-Host "[INICIO] Iniciando TODA a fabrica de dados (bancos + ingestao + geracao)..." -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/3] Bancos (Postgres + Oracle + MinIO + Mongo)..." -ForegroundColor Cyan
& "$PSScriptRoot\start-infra.ps1"
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host ""
Write-Host "[2/3] Ingestao/CDC (Redpanda + Kafka Connect + Airbyte)..." -ForegroundColor Cyan
& "$PSScriptRoot\toggle-ingestion.ps1" on
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host ""
Write-Host "[3/3] Geracao de dados (ShadowTraffic)..." -ForegroundColor Cyan
& "$PSScriptRoot\toggle-shadowtraffic.ps1" on
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host ""
Write-Host "[OK] Fabrica de dados completa iniciada." -ForegroundColor Green
Write-Host ""
Write-Host "Comandos uteis:" -ForegroundColor White
Write-Host "   -> Ver status geracao:  .\scripts\toggle-shadowtraffic.ps1 status" -ForegroundColor Gray
Write-Host "   -> Ver status ingestao: .\scripts\toggle-ingestion.ps1 status" -ForegroundColor Gray
Write-Host "   -> Ver logs: docker-compose logs -f" -ForegroundColor Gray
Write-Host "   -> Parar tudo: .\scripts\stop-all.ps1" -ForegroundColor Gray
