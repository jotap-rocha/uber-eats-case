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
LICENSE_EMAIL=<seu_email>
LICENSE_ORGANIZATION=<sua_organizacao>
LICENSE_EDITION=<sua_edicao>
LICENSE_EXPIRATION=<data_expiracao>
LICENSE_SIGNATURE=<assinatura_da_licenca>
```

---

## Gerador

Um único processo unificado (`gen-unified`) gera tudo — necessário para o lookup cruzado entre a conexão Postgres real e a conexão MinIO no mesmo config (`gen/unified/uber-eats.json`).

| Destino | Taxa | Limite |
|---------|------|--------|
| `users` (Postgres) | ~50/s | 80.000 |
| `drivers` (Postgres) | ~50/s | 80.000 |
| `uber-eats` (MinIO) | ~500/s | Infinito |

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

> ⚠️ Para **religar** depois de parar (quando as tabelas já têm dados gerados), não use `start-generators.ps1` — use `.\scripts\toggle-shadowtraffic.ps1 on` (ver seção "Ajustar Velocidade" abaixo). `start-generators.ps1` só é seguro em ambiente 100% novo, sem dado prévio.

### Monitorar

```powershell
# Logs
docker-compose logs -f gen-unified

# Contagem Postgres (use suas credenciais do .env)
docker exec postgres-ubereats psql -U <seu_usuario> -d <seu_database> -c "SELECT COUNT(*) FROM drivers;"

# Arquivos MinIO
docker exec minio-ubereats mc ls local/uber-eats/ --recursive
```

> Report automático: `.\scripts\toggle-shadowtraffic.ps1 on` já sobe junto um loop de background que escreve um snapshot (contagem por tabela + crescimento desde o snapshot anterior) em `logs/shadowtraffic-report.log` a cada hora, enquanto `gen-unified` estiver ativo — útil para deixar rodando sem monitorar a tela. `.\scripts\toggle-shadowtraffic.ps1 off` encerra o loop junto com o gerador. `.\scripts\toggle-shadowtraffic.ps1 status` mostra se o loop está ativo e o caminho do log.

---

## Ajustar Velocidade

Edite `gen/unified/uber-eats.json.template`:

```json
{
  "localConfigs": {
    "maxEvents": 100000,    // Quantidade
    "throttleMs": 20        // Velocidade (menor = mais rapido)
  }
}
```

Depois, **se as tabelas já tem dados de uma execucao anterior**, religue com o script seguro (nao use `stop-generators.ps1`/`start-generators.ps1` aqui — eles nao recalculam `startingFrom` e ja causaram travamento total do pipeline por colisao de PK):

```powershell
.\scripts\toggle-shadowtraffic.ps1 off
# edite o .template aqui
.\scripts\toggle-shadowtraffic.ps1 on
```

`toggle-shadowtraffic.ps1 on` ja injeta os segredos do `.env` e recalcula `startingFrom` a partir do `MAX(id)` real de cada tabela antes de subir o container — nao e preciso rodar `gen\setup-configs.ps1` manualmente. Detalhe do incidente: `.claude/kb/shadowtraffic/patterns/restart-seguro-startingFrom.md`.

Só use `.\gen\setup-configs.ps1` + `stop-generators.ps1`/`start-generators.ps1` em ambiente **recem-criado** (`docker-compose down -v` + `up`, tabelas vazias).

---

## Troubleshooting

### Licenca expirada

```powershell
# 1. Renove em https://shadowtraffic.io
# 2. Atualize gen/.env (LICENSE_ID, LICENSE_EMAIL, LICENSE_ORGANIZATION,
#    LICENSE_EDITION, LICENSE_EXPIRATION, LICENSE_SIGNATURE)
# 3. Religue com seguranca (tabelas ja tem dados na maioria dos casos):
.\scripts\toggle-shadowtraffic.ps1 off
.\scripts\toggle-shadowtraffic.ps1 on
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
