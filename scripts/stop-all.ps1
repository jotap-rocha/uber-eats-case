# ==============================================================================
# Script: stop-all.ps1
# Descricao: Para TODOS os containers (preserva volumes/dados)
# ==============================================================================

Write-Host "[STOP] Parando todos os containers..." -ForegroundColor Yellow

docker-compose down

if ($LASTEXITCODE -eq 0) {
    Write-Host "[OK] Todos os containers foram parados." -ForegroundColor Green
    Write-Host "     (Volumes preservados - dados NAO foram apagados)" -ForegroundColor Gray
    Write-Host ""
    Write-Host "[DOCKER] Docker Desktop continua rodando." -ForegroundColor Gray
    Write-Host "         Para desligar manualmente, feche o Docker Desktop." -ForegroundColor Gray
} else {
    Write-Host "[ERRO] Falha ao parar containers." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Para reiniciar: .\scripts\start-all.ps1" -ForegroundColor Gray
