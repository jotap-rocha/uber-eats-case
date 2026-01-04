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

Preencha:

```ini
# PostgreSQL
POSTGRES_HOST=postgres-ubereats
POSTGRES_PORT=5432
POSTGRES_DB=ubereats_db
POSTGRES_USERNAME=usrUberEats
POSTGRES_PASSWORD=supersecret

# MinIO
AWS_REGION=us-east-1
AWS_S3_FORCE_PATH_STYLE=true
AWS_ACCESS_KEY_ID=usrUberEats
AWS_SECRET_ACCESS_KEY=supersecret

# ShadowTraffic License
LICENSE_ID=seu-id
LICENSE_KEY=sua-key
LICENSE_EMAIL=seu@email.com
LICENSE_OWNER=Seu Nome
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

# Contagem Postgres
docker exec postgres-ubereats psql -U usrUberEats -d ubereats_db -c "SELECT COUNT(*) FROM drivers;"

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
