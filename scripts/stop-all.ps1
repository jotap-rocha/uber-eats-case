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
    
    # Pergunta se deseja desligar o Docker Desktop
    Write-Host "[DOCKER] Deseja desligar o Docker Desktop tambem? (S/N)" -ForegroundColor Yellow
    $resposta = Read-Host "Opcao"
    
    if ($resposta -eq "S" -or $resposta -eq "s") {
        Write-Host "[DOCKER] Desligando Docker Desktop..." -ForegroundColor Yellow
        
        # Tenta fechar graciosamente
        try {
            Stop-Process -Name "Docker Desktop" -ErrorAction SilentlyContinue
            Write-Host "[DOCKER] Docker Desktop desligado com sucesso!" -ForegroundColor Green
        } catch {
            Write-Host "[AVISO] Nao foi possivel desligar o Docker Desktop automaticamente." -ForegroundColor Yellow
            Write-Host "        Feche manualmente se desejar." -ForegroundColor Gray
        }
    } else {
        Write-Host "[DOCKER] Docker Desktop continua rodando." -ForegroundColor Gray
    }
} else {
    Write-Host "[ERRO] Falha ao parar containers." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Para reiniciar: .\scripts\start-all.ps1" -ForegroundColor Gray
