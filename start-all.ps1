Write-Host "🚀 1/2: Injetando segredos do .env nos arquivos .json..."
./gen/setup-configs.ps1

Write-Host "🚀 2/2: Iniciando TODA a fábrica de dados (Infra + Setup + Geradores)..."
Write-Host "   (Isso pode levar um minuto... O Postgres e o MinIO estão se auto-configurando.)"

docker-compose up -d

Write-Host "✅ Fábrica de dados iniciada em background."
Write-Host "   Consulte logs: docker-compose logs -f"
Write-Host "   -> Postgres: localhost:5432 (Tabelas criadas automaticamente)"
Write-Host "   -> MinIO (S3): http://localhost:9001 (Bucket 'uber-eats' criado automaticamente)"