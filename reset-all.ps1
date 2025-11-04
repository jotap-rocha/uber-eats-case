Write-Host "🔥🔥🔥 ATENÇÃO! FORMATANDO TODO O AMBIENTE... 🔥🔥🔥"

Write-Host "   -> 1/3: Forçando a parada de contêineres 'zumbis' (se existirem)..."
docker stop postgres-ubereats minio-ubereats minio-setup gen-drivers gen-users gen-minio | Out-Null
docker rm postgres-ubereats minio-ubereats minio-setup gen-drivers gen-users gen-minio | Out-Null

Write-Host "   -> 2/3: Parando contêineres E DESTRUINDO volumes (postgres_data, minio_data)..."
docker-compose down -v

Write-Host "   -> 3/3: Limpando arquivos .json gerados (que continham segredos)..."
Remove-Item -Path ".\gen\postgres\drivers.json" -ErrorAction SilentlyContinue
Remove-Item -Path ".\gen\postgres\users.json" -ErrorAction SilentlyContinue

Write-Host "✅ Ambiente 100% limpo e formatado."
Write-Host "   -> Na próxima vez que rodar 'start-all.ps1', as tabelas e o bucket serão recriados."