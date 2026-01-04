# Airbyte - Documentacao Tecnica

Ferramenta de ingestao de dados: PostgreSQL + MinIO → Databricks (Delta Lake).

---

## Especificacoes Tecnicas

| Item | Valor |
|------|-------|
| **Versao** | 2.0.1 (Chart 2.0.19) |
| **Deployment** | Kubernetes (Kind cluster) |
| **Ferramenta** | `abctl` (Airbyte CLI) |
| **Console Port** | `8000` |
| **Container Principal** | `airbyte-abctl-control-plane` |

---

## Arquitetura

O Airbyte roda em um **cluster Kubernetes local** (Kind) com:
- **Ingress-nginx**: Roteamento HTTP
- **Airbyte Server**: API e orquestração
- **Airbyte Worker**: Executa os syncs
- **PostgreSQL interno**: Metadata do Airbyte
- **MinIO interno**: Logs e artefatos

---

## URLs de Acesso

### Console Web
```
URL: http://localhost:8000
Credenciais: Nao requer login (OSS local)
```

**Observacao**: A primeira vez que acessar, pode pedir para criar uma conta (apenas para UI, nao e obrigatorio).

---

## Instalacao e Setup

### 1. Instalar Airbyte

O projeto ja inclui o `abctl` em `abctl-v0.30.3-windows-amd64/`.

```powershell
# Verificar versao
.\abctl-v0.30.3-windows-amd64\abctl.exe version

# Instalar Airbyte (primeira vez)
.\abctl-v0.30.3-windows-amd64\abctl.exe local install

# Aguardar ~2-3 minutos ate ficar pronto
```

### 2. Verificar Status

```powershell
# Status do Airbyte
.\abctl-v0.30.3-windows-amd64\abctl.exe local status

# Verificar pods do Kubernetes
kubectl get pods -n airbyte-abctl

# Verificar containers
docker ps | findstr airbyte
```

### 3. Acessar Console

Abra no browser: `http://localhost:8000`

---

## Configurar Conexoes

### Source: PostgreSQL

1. No Airbyte, clique em **"Sources"** > **"+ New source"**
2. Selecione **"Postgres"**
3. Preencha:
   - **Name**: `PostgreSQL Local (Uber Eats)`
   - **Host**: `host.docker.internal` (ou IP da sua maquina)
   - **Port**: `5432`
   - **Database**: `ubereats_db`
   - **Username**: `usrUberEats`
   - **Password**: `supersecret`
   - **Replication Method**: `CDC (Change Data Capture)` ou `Standard (Full Refresh)`
   - **SSL Mode**: `disable`
4. Clique em **"Test connection"**
5. Se OK, clique em **"Set up source"**

**Observacao**: Use `host.docker.internal` para acessar localhost do host a partir do container Kubernetes.

---

### Source: MinIO/S3

1. No Airbyte, clique em **"Sources"** > **"+ New source"**
2. Selecione **"S3"**
3. Preencha:
   - **Name**: `MinIO Local (Uber Eats Events)`
   - **Bucket**: `uber-eats`
   - **AWS Access Key ID**: `usrUberEats`
   - **AWS Secret Access Key**: `supersecret`
   - **Endpoint**: `http://host.docker.internal:9000`
   - **Path Prefix**: (vazio ou especifique, ex: `kafka/orders/`)
   - **File Format**: `JSONL` (JSON Lines)
4. Clique em **"Test connection"**
5. Se OK, clique em **"Set up source"**

---

### Destination: Databricks

1. No Airbyte, clique em **"Destinations"** > **"+ New destination"**
2. Selecione **"Databricks Lakehouse"**
3. Preencha:
   - **Name**: `Databricks Lakehouse`
   - **Hostname**: `<seu-workspace>.cloud.databricks.com`
   - **HTTP Path**: `/sql/1.0/warehouses/<warehouse-id>`
   - **Personal Access Token**: `<seu-pat-token>`
   - **Catalog**: `main` (Unity Catalog)
   - **Schema**: `uber_eats`
   - **Purge Staging Data**: `true`
4. Clique em **"Test connection"**
5. Se OK, clique em **"Set up destination"**

**Como obter as credenciais do Databricks**:
- **Hostname**: No workspace, clique em seu nome > Settings > Server hostname
- **HTTP Path**: SQL Warehouses > seu warehouse > Connection details
- **PAT Token**: Settings > Developer > Access tokens > Generate new token

---

## Criar Conexoes (Syncs)

### Sync 1: PostgreSQL → Databricks (drivers)

1. Clique em **"Connections"** > **"+ New connection"**
2. Selecione:
   - **Source**: PostgreSQL Local
   - **Destination**: Databricks Lakehouse
3. Configure:
   - **Connection name**: `Postgres Drivers → Databricks`
   - **Replication frequency**: `Every 1 hour` (ou `Manual`)
   - **Destination namespace**: `main.uber_eats`
   - **Destination stream prefix**: (vazio)
4. Selecione a tabela `drivers`:
   - **Sync mode**: `Incremental | Append` (para CDC)
   - **Cursor field**: `updated_at` (ou outra coluna de timestamp)
   - **Primary key**: `driver_id`
5. Clique em **"Set up connection"**

### Sync 2: PostgreSQL → Databricks (users)

Repita o processo para a tabela `users`.

### Sync 3: MinIO → Databricks (events)

1. Clique em **"Connections"** > **"+ New connection"**
2. Selecione:
   - **Source**: MinIO Local
   - **Destination**: Databricks Lakehouse
3. Configure:
   - **Connection name**: `MinIO Events → Databricks`
   - **Replication frequency**: `Every 15 minutes`
   - **Destination namespace**: `main.uber_eats_raw`
4. Selecione os streams desejados (ex: `kafka/orders/`)
5. **Sync mode**: `Full Refresh | Overwrite` (para JSON)
6. Clique em **"Set up connection"**

---

## Executar Syncs

### Manual

1. Acesse a conexao criada
2. Clique em **"Sync now"**
3. Aguarde a execucao
4. Verifique os logs

### Agendado

Os syncs serao executados automaticamente conforme a frequencia configurada.

---

## Monitoramento

### Via Console Web

1. Acesse `http://localhost:8000`
2. Clique na conexao
3. Veja o historico de syncs, logs e metricas

### Via CLI (abctl)

```powershell
# Status geral
.\abctl-v0.30.3-windows-amd64\abctl.exe local status

# Logs do Airbyte
kubectl logs -n airbyte-abctl -l app=airbyte-server

# Logs de um sync especifico (via UI)
```

### Via Docker

```powershell
# Ver logs do control plane
docker logs airbyte-abctl-control-plane --tail 50

# Listar pods do Kubernetes
kubectl get pods -n airbyte-abctl

# Logs de um pod especifico
kubectl logs -n airbyte-abctl <pod-name>
```

---

## Troubleshooting

### Airbyte nao inicia

```powershell
# Reinstalar
.\abctl-v0.30.3-windows-amd64\abctl.exe local uninstall
.\abctl-v0.30.3-windows-amd64\abctl.exe local install
```

### Erro: "Connection timeout"

Se o Airbyte nao consegue conectar no Postgres/MinIO:

```powershell
# Use o IP da maquina ao inves de localhost
ipconfig

# No Airbyte, use: <seu-ip-local>:5432
# Ex: 192.168.1.100:5432
```

### Porta 8000 em uso

```powershell
# Descobrir o que esta usando
netstat -ano | findstr "8000"

# Ou reconfigure o Airbyte para outra porta (via abctl)
```

### Sync falha com erro "Out of memory"

O Airbyte pode consumir muita memoria. Solucao:

1. Aumente a memoria do Docker Desktop (Settings > Resources)
2. Ou faça syncs menores (filtre por data/tabela)

---

## Performance e Otimizacao

### CDC vs Full Refresh

**CDC (Change Data Capture)**:
- ✅ Mais eficiente (apenas mudancas)
- ✅ Menor impacto no banco
- ❌ Requer configuracao no Postgres (`wal_level=logical`)

**Full Refresh**:
- ✅ Mais simples
- ❌ Reprocessa tudo a cada sync
- ❌ Alto consumo de recursos

**Recomendacao**: Use CDC para tabelas grandes (drivers, users).

### Paralelismo

Configure o numero de workers:

```yaml
# Via Kubernetes (avancado)
# Edite o deployment do airbyte-worker
```

### Frequencia de Syncs

- **Tabelas pequenas** (<100k linhas): A cada 15 min
- **Tabelas grandes** (>100k linhas): A cada 1 hora
- **Eventos JSON**: A cada 5-15 min (dependendo do volume)

---

## Parar e Remover Airbyte

### Parar (sem remover)

```powershell
docker stop airbyte-abctl-control-plane
```

### Reiniciar

```powershell
docker start airbyte-abctl-control-plane

# Ou reinstale
.\abctl-v0.30.3-windows-amd64\abctl.exe local install
```

### Remover Completamente

```powershell
# Desinstalar Airbyte
.\abctl-v0.30.3-windows-amd64\abctl.exe local uninstall

# Remover cluster Kind
kind delete cluster --name airbyte-abctl
```

---

## Integracao com Databricks

Apos configurar os syncs, os dados chegarao no Databricks:

```
main.uber_eats.drivers       # Tabela Delta
main.uber_eats.users         # Tabela Delta
main.uber_eats_raw.orders    # Dados brutos (JSON)
```

No Databricks, use Delta Live Tables para processar:

```python
# Bronze Layer (Auto Loader)
@dlt.table(name="orders_bronze")
def orders_bronze():
    return (
        spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", "json")
            .load("s3://uber-eats/kafka/orders/")
    )
```

---

## Links

- Airbyte: https://airbyte.com
- Docs: https://docs.airbyte.com
- abctl: https://docs.airbyte.com/using-airbyte/getting-started/oss-quickstart
- Connectors: https://docs.airbyte.com/integrations/

