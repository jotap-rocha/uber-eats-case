# ==============================================================================
# Script: start-airbyte.ps1
# Descricao: Liga o Airbyte (abctl) sob demanda, quando for configurar/rodar syncs
# ==============================================================================

Write-Host "[INFO] Iniciando Airbyte (abctl)..." -ForegroundColor Cyan

$container = docker ps -a --filter "name=airbyte-abctl-control-plane" --format "{{.Names}}"

if (-not $container) {
    Write-Host "[ERRO] Container airbyte-abctl-control-plane nao encontrado." -ForegroundColor Red
    Write-Host "Instale primeiro: .\abctl-v0.30.3-windows-amd64\abctl.exe local install" -ForegroundColor Yellow
    exit 1
}

docker start airbyte-abctl-control-plane

Write-Host ""
Write-Host "[OK] Airbyte iniciado." -ForegroundColor Green
Write-Host "   -> UI: http://localhost:8000" -ForegroundColor White
Write-Host "   -> Pode levar 1-2 minutos ate a UI responder." -ForegroundColor Gray
Write-Host "   -> Para desligar: .\scripts\stop-airbyte.ps1" -ForegroundColor Gray
