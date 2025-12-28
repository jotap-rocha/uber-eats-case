# ==============================================================================
# Script: reset-all.ps1
# Descrição: RESET COMPLETO - Remove TODOS os dados (DESTRUTIVO!)
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "🔥🔥🔥 ATENÇÃO! FORMATANDO TODO O AMBIENTE... 🔥🔥🔥"
Write-Host ""

Write-Host "   -> 1/3: Forçando a parada de contêineres 'zumbis' (se existirem)..."
docker stop postgres-ubereats minio-ubereats minio-setup gen-drivers gen-users gen-minio 2>$null | Out-Null
docker rm postgres-ubereats minio-ubereats minio-setup gen-drivers gen-users gen-minio 2>$null | Out-Null

Write-Host "   -> 2/3: Parando contêineres E DESTRUINDO volumes (postgres_data, minio_data)..."
docker-compose down -v

Write-Host "   -> 3/3: Limpando arquivos .json gerados (que continham segredos)..."
Remove-Item -Path ".\gen\postgres\drivers.json" -ErrorAction SilentlyContinue
Remove-Item -Path ".\gen\postgres\users.json" -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "✅ Ambiente 100% limpo e formatado."
Write-Host ""
Write-Host "💡 Próximos passos:"
Write-Host "   -> Para recriar o ambiente: .\scripts\start-all.ps1"
Write-Host "   -> Na próxima execução, as tabelas e o bucket serão recriados do zero."
Write-Host ""
Write-Host "⚠️  IMPORTANTE: Todos os dados foram DELETADOS permanentemente!"

