# ==============================================================================
# Script: reset-all.ps1
# Descricao: RESET COMPLETO - Remove TODOS os dados (DESTRUTIVO!)
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "[AVISO] FORMATANDO TODO O AMBIENTE..."
Write-Host ""

Write-Host "   -> 1/3: Forcando a parada de conteineres 'zumbis' (se existirem)..."
docker stop postgres-ubereats minio-ubereats minio-setup gen-drivers gen-users gen-minio 2>$null | Out-Null
docker rm postgres-ubereats minio-ubereats minio-setup gen-drivers gen-users gen-minio 2>$null | Out-Null

Write-Host "   -> 2/3: Parando conteineres E DESTRUINDO volumes (postgres_data, minio_data)..."
docker-compose down -v

Write-Host "   -> 3/3: Limpando arquivos .json gerados (que continham segredos)..."
Remove-Item -Path ".\gen\postgres\drivers.json" -ErrorAction SilentlyContinue
Remove-Item -Path ".\gen\postgres\users.json" -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "[OK] Ambiente 100% limpo e formatado."
Write-Host ""
Write-Host "Proximos passos:"
Write-Host "   -> Para recriar o ambiente: .\scripts\start-all.ps1"
Write-Host "   -> Na proxima execucao, as tabelas e o bucket serao recriados do zero."
Write-Host ""
Write-Host "[AVISO] Todos os dados foram DELETADOS permanentemente!"


