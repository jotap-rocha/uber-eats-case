# Airbyte - Ingestao de Dados

Ferramenta para ingerir dados: PostgreSQL + MinIO → Databricks.

---

## Acesso

```
URL: http://localhost:8000
Credenciais: Nao requer login (OSS local)
```

---

## Instalacao

### 1. Instalar

```powershell
.\abctl-v0.30.3-windows-amd64\abctl.exe local install
```

Aguarde ~2-3 minutos.

### 2. Verificar

```powershell
.\abctl-v0.30.3-windows-amd64\abctl.exe local status
docker ps | findstr airbyte
```

### 3. Acessar

Abra: `http://localhost:8000`

---

## Configurar Sources

### PostgreSQL

1. Sources > + New source > Postgres
2. Preencha:
   - **Host**: `host.docker.internal`
   - **Port**: `5432`
   - **Database**: `ubereats_db`
   - **User**: `usrUberEats`
   - **Password**: `supersecret`
   - **SSL**: `disable`
3. Test connection > Set up

### MinIO/S3

1. Sources > + New source > S3
2. Preencha:
   - **Bucket**: `uber-eats`
   - **Access Key**: `usrUberEats`
   - **Secret Key**: `supersecret`
   - **Endpoint**: `http://host.docker.internal:9000`
   - **Format**: `JSONL`
3. Test connection > Set up

---

## Configurar Destination

### Databricks

1. Destinations > + New destination > Databricks Lakehouse
2. Preencha:
   - **Hostname**: `<workspace>.cloud.databricks.com`
   - **HTTP Path**: `/sql/1.0/warehouses/<id>`
   - **Token**: `<seu-pat-token>`
   - **Catalog**: `main`
   - **Schema**: `uber_eats`
3. Test connection > Set up

**Obter credenciais**:
- Hostname: Settings > Server hostname
- HTTP Path: SQL Warehouses > Connection details
- Token: Settings > Developer > Access tokens

---

## Criar Conexoes (Syncs)

### Postgres → Databricks

1. Connections > + New connection
2. Selecione: PostgreSQL → Databricks
3. Configure:
   - **Frequency**: `Every 1 hour`
   - **Namespace**: `main.uber_eats`
4. Selecione tabelas: `drivers`, `users`
5. **Sync mode**: `Incremental | Append`
6. Set up connection

### MinIO → Databricks

1. Connections > + New connection
2. Selecione: MinIO → Databricks
3. Configure:
   - **Frequency**: `Every 15 minutes`
   - **Namespace**: `main.uber_eats_raw`
4. Selecione streams desejados
5. **Sync mode**: `Full Refresh | Overwrite`
6. Set up connection

---

## Executar Syncs

### Manual

1. Acesse a conexao
2. Clique em "Sync now"
3. Aguarde e verifique logs

### Agendado

Syncs executam automaticamente conforme frequencia configurada.

---

## Parar/Remover

### Parar

```powershell
docker stop airbyte-abctl-control-plane
```

### Reiniciar

```powershell
docker start airbyte-abctl-control-plane
```

### Remover

```powershell
.\abctl-v0.30.3-windows-amd64\abctl.exe local uninstall
```

---

## Troubleshooting

### Nao inicia

```powershell
.\abctl-v0.30.3-windows-amd64\abctl.exe local uninstall
.\abctl-v0.30.3-windows-amd64\abctl.exe local install
```

### Connection timeout

Use o IP da maquina ao inves de `localhost`:

```powershell
ipconfig
# Use: 192.168.x.x:5432
```

### Porta 8000 em uso

```powershell
netstat -ano | findstr "8000"
```

---

## Links

- Airbyte: https://airbyte.com
- Docs: https://docs.airbyte.com
- abctl: https://docs.airbyte.com/using-airbyte/getting-started/oss-quickstart
