# ==============================================================================
# Script: stop-airbyte.ps1
# Descricao: Desliga o Airbyte (abctl) para liberar CPU/memoria quando nao esta
#            em uso -- ele NAO faz parte do docker-compose.yml deste projeto e
#            nao precisa ficar de pe o tempo todo.
# ==============================================================================

Write-Host "[INFO] Parando Airbyte (abctl)..." -ForegroundColor Cyan

docker stop airbyte-abctl-control-plane

Write-Host ""
Write-Host "[OK] Airbyte parado." -ForegroundColor Green
Write-Host "   -> Configuracao de sources/destinations/connections e preservada." -ForegroundColor Gray
Write-Host "   -> Para religar: .\scripts\start-airbyte.ps1" -ForegroundColor Gray
