# ==============================================================================
# Script: start-all.ps1
# Descrição: Sobe TODA a fábrica de dados (Infra + Geradores)
# Autor: Uber Eats Data Pipeline Project
# ==============================================================================

Write-Host "🚀 Iniciando TODA a fábrica de dados (Infra + Setup + Geradores)..."
Write-Host ""

Write-Host "🚀 1/3: Injetando segredos do .env nos arquivos .json..."
.\gen\setup-configs.ps1

Write-Host ""
Write-Host "🚀 2/3: Iniciando infraestrutura (Postgres + MinIO)..."
Write-Host "   (Isso pode levar um minuto... O Postgres e o MinIO estão se auto-configurando.)"
docker-compose up -d postgres-ubereats minio-ubereats minio-setup

Write-Host ""
Write-Host "🚀 3/3: Iniciando geradores ShadowTraffic..."
docker-compose up -d gen-drivers gen-users gen-minio

Write-Host ""
Write-Host "✅ Fábrica de dados iniciada em background."
Write-Host ""
Write-Host "📊 Acessos Rápidos:"
Write-Host "   -> Postgres: localhost:5432 (DB: ubereats_db | User: usrUberEats)"
Write-Host "   -> MinIO Console: http://localhost:9001 (User: usrUberEats | Senha: supersecret)"
Write-Host "   -> Bucket: uber-eats (criado automaticamente)"
Write-Host ""
Write-Host "💡 Comandos úteis:"
Write-Host "   -> Ver logs: docker-compose logs -f"
Write-Host "   -> Ver status: docker-compose ps"
Write-Host "   -> Parar tudo: .\scripts\stop-all.ps1"
Write-Host "   -> Parar apenas geradores: .\scripts\stop-generators.ps1"

