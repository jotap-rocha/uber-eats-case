# ShadowTraffic - Gerador de Dados

Gerador de dados sinteticos para Postgres e MinIO.

---

## Configuracao

### 1. Obter Licenca

1. Acesse: https://shadowtraffic.io
2. Cadastre Free Trial
3. Copie as credenciais

### 2. Criar arquivo .env

```powershell
copy gen\.env.template gen\.env
notepad gen\.env
```

Preencha conforme as instruções no arquivo `.env.template`. As principais variáveis são:

```ini
# PostgreSQL
POSTGRES_HOST=postgres-ubereats
POSTGRES_PORT=5432
POSTGRES_DB=<seu_database>
POSTGRES_USERNAME=<seu_usuario>
POSTGRES_PASSWORD=<sua_senha>

# MinIO
AWS_REGION=us-east-1
AWS_S3_FORCE_PATH_STYLE=true
AWS_ACCESS_KEY_ID=<seu_usuario>
AWS_SECRET_ACCESS_KEY=<sua_senha>

# ShadowTraffic License (obtenha em https://shadowtraffic.io)
LICENSE_ID=<seu_license_id>
LICENSE_KEY=<sua_license_key>
LICENSE_EMAIL=<seu_email>
LICENSE_OWNER=<seu_nome>
```

---

## Geradores

| Gerador | Destino | Taxa | Limite |
|---------|---------|------|--------|
| `gen-drivers` | `drivers` (Postgres) | ~50/s | 80.000 |
| `gen-users` | `users` (Postgres) | ~50/s | 80.000 |
| `gen-minio` | `uber-eats` (MinIO) | ~500/s | Infinito |

---

## Como Usar

### Iniciar Geradores

```powershell
# Com infra rodando
.\scripts\start-generators.ps1
```

### Parar Geradores

```powershell
.\scripts\stop-generators.ps1
```

### Monitorar

```powershell
# Logs
docker-compose logs -f gen-drivers gen-users gen-minio

# Contagem Postgres (use suas credenciais do .env)
docker exec postgres-ubereats psql -U <seu_usuario> -d <seu_database> -c "SELECT COUNT(*) FROM drivers;"

# Arquivos MinIO
docker exec minio-ubereats mc ls local/uber-eats/ --recursive
```

---

## Ajustar Velocidade

Edite `gen/postgres/*.json.template`:

```json
{
  "localConfigs": {
    "maxEvents": 100000,    // Quantidade
    "throttleMs": 20        // Velocidade (menor = mais rapido)
  }
}
```

Depois:

```powershell
.\gen\setup-configs.ps1
.\scripts\stop-generators.ps1
.\scripts\start-generators.ps1
```

---

## Troubleshooting

### Licenca expirada

```powershell
# 1. Renove em https://shadowtraffic.io
# 2. Atualize gen/.env
# 3. Reinicie:
.\scripts\stop-generators.ps1
.\scripts\start-generators.ps1
```

### Connection refused

```powershell
# Inicie a infra primeiro
.\scripts\start-infra.ps1
.\scripts\start-generators.ps1
```

### Geradores param sozinhos

Isso é normal! Quando atingem `maxEvents`, finalizam automaticamente.

---

## Links

- ShadowTraffic: https://shadowtraffic.io
- Docs: https://docs.shadowtraffic.io
