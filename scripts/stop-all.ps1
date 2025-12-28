# ==============================================================================
# Script: stop-all.ps1
# Descrição: Para TODOS os serviços (Infra + Geradores)
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "🛑 Parando todos os contêineres..."

docker-compose down

Write-Host ""
Write-Host "✅ Ambiente parado."
Write-Host "   -> Seus dados (volumes) estão salvos."
Write-Host "   -> Para reiniciar: .\scripts\start-all.ps1"
Write-Host ""
Write-Host "💡 Comandos relacionados:"
Write-Host "   -> Iniciar apenas infra: .\scripts\start-infra.ps1"
Write-Host "   -> Iniciar apenas geradores: .\scripts\start-generators.ps1"
Write-Host "   -> Reset completo (DESTRUTIVO): .\scripts\reset-all.ps1"

