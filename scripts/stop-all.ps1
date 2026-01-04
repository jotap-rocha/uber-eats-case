# ==============================================================================
# Script: stop-all.ps1
# Descricao: Para TODOS os servicos (Infra + Geradores)
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "[INFO] Parando todos os conteineres..."

docker-compose down

Write-Host ""
Write-Host "[OK] Ambiente parado."
Write-Host "   -> Seus dados (volumes) estao salvos."
Write-Host "   -> Para reiniciar: .\scripts\start-all.ps1"
Write-Host ""
Write-Host "Comandos relacionados:"
Write-Host "   -> Iniciar apenas infra: .\scripts\start-infra.ps1"
Write-Host "   -> Iniciar apenas geradores: .\scripts\start-generators.ps1"
Write-Host "   -> Reset completo (DESTRUTIVO): .\scripts\reset-all.ps1"


