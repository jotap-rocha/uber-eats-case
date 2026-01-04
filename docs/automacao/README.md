# Automacao - Documentacao Tecnica

Scripts PowerShell e Docker Compose para gerenciar a infraestrutura local (start/stop/reset).

---

## Estrutura de Arquivos

```
uber-eats-case/
├── docker-compose.yml       # Orquestracao de todos os containers
├── scripts/                 # Scripts PowerShell
│   ├── start-all.ps1       # Inicia tudo (infra + geradores)
│   ├── start-infra.ps1     # Inicia apenas Postgres + MinIO
│   ├── start-generators.ps1 # Inicia apenas ShadowTraffic
│   ├── stop-all.ps1        # Para tudo
│   ├── stop-infra.ps1      # Para apenas infra
│   ├── stop-generators.ps1  # Para apenas geradores
│   ├── reset-all.ps1       # Reset DESTRUTIVO
│   └── README.md           # Documentacao dos scripts
└── gen/
    └── setup-configs.ps1    # Injeta secrets nos JSONs
```

---

## Scripts PowerShell

### start-all.ps1

**Funcao**: Inicia toda a infraestrutura (Postgres + MinIO + ShadowTraffic)

**Uso**:
```powershell
.\scripts\start-all.ps1
```

**O que faz**:
1. Injeta secrets de `gen/.env` nos JSONs do ShadowTraffic
2. Sobe Postgres e MinIO via docker-compose
3. Aguarda health checks
4. Sobe os 3 geradores ShadowTraffic

**Quando usar**:
- Primeira execucao do projeto
- Quando precisa de dados sendo gerados
- Demos/apresentacoes

---

### start-infra.ps1

**Funcao**: Inicia apenas a infraestrutura (Postgres + MinIO)

**Uso**:
```powershell
.\scripts\start-infra.ps1
```

**O que faz**:
1. Sobe Postgres via docker-compose
2. Sobe MinIO via docker-compose
3. Executa `minio-setup` (cria bucket `uber-eats`)
4. Aguarda health checks

**Quando usar**:
- Desenvolvimento local (queries, exploracao)
- Quando ja tem dados suficientes
- Para economizar licenca ShadowTraffic
- Testes com dados estaticos

**Vantagens**:
- ✅ Menor consumo de CPU/RAM (~10% vs ~25%)
- ✅ Nao gasta licenca
- ✅ Mais rapido para iniciar (~30s vs ~2min)

---

### start-generators.ps1

**Funcao**: Inicia apenas os geradores ShadowTraffic

**Uso**:
```powershell
.\scripts\start-generators.ps1
```

**Pre-requisito**: Infra deve estar rodando (`start-infra.ps1`)

**O que faz**:
1. Verifica se Postgres e MinIO estao ativos
2. Injeta secrets de `gen/.env` nos JSONs
3. Sobe os 3 geradores via docker-compose

**Quando usar**:
- Quando precisa gerar mais dados
- Apos usar `start-infra.ps1`
- Para controlar geracao sob demanda

---

### stop-generators.ps1

**Funcao**: Para apenas os geradores ShadowTraffic

**Uso**:
```powershell
.\scripts\stop-generators.ps1
```

**O que faz**:
1. Para os 3 geradores (gen-drivers, gen-users, gen-minio)
2. Mantem Postgres e MinIO rodando

**Quando usar**:
- Dados suficientes para testes
- Economizar licenca ShadowTraffic
- Reduzir consumo de recursos

**Vantagens**:
- ✅ Economiza ~15% CPU e ~1.5 GB RAM
- ✅ Mantem infra disponivel para queries
- ✅ Nao perde dados

---

### stop-infra.ps1

**Funcao**: Para apenas a infraestrutura (Postgres + MinIO)

**Uso**:
```powershell
.\scripts\stop-infra.ps1
```

**O que faz**:
1. Para Postgres
2. Para MinIO
3. Mantem volumes (dados preservados)

**Quando usar**:
- Raramente usado (normalmente usa-se `stop-all.ps1`)
- Casos especificos onde quer parar infra mas nao geradores

**Observacao**: Geradores falharao se a infra parar!

---

### stop-all.ps1

**Funcao**: Para todos os containers (infra + geradores)

**Uso**:
```powershell
.\scripts\stop-all.ps1
```

**O que faz**:
1. Executa `docker-compose down`
2. Para todos os containers
3. Remove a rede Docker
4. **Preserva volumes** (dados mantidos)

**Quando usar**:
- Terminou o trabalho do dia
- Quer liberar recursos do Docker
- Precisa reiniciar o ambiente

**Dados preservados**:
- ✅ 111k+ registros no Postgres
- ✅ Eventos JSON no MinIO
- ✅ Configuracoes

---

### reset-all.ps1

**Funcao**: Reset completo e DESTRUTIVO (apaga TODOS os dados)

**Uso**:
```powershell
.\scripts\reset-all.ps1
```

**⚠️ ATENCAO**: Este comando e IRREVERSIVEL!

**O que faz**:
1. Para forcadamente todos os containers (mesmo "zumbis")
2. Remove todos os containers
3. **DELETA VOLUMES** (postgres_data, minio_data)
4. Remove JSONs gerados (`drivers.json`, `users.json`)
5. Remove a rede Docker

**Quando usar**:
- Quer comecar do zero
- Ambiente corrompido
- Testes exigem limpeza completa
- Algo deu muito errado

**O que voce perde**:
- ❌ Todos os 111k+ registros do Postgres
- ❌ Todos os eventos JSON do MinIO
- ❌ Todas as configuracoes geradas

**Apos o reset**:
```powershell
# Recriar o ambiente
.\scripts\start-all.ps1
```

---

## Docker Compose

### Arquivo docker-compose.yml

Orquestra 6 servicos:

```yaml
services:
  postgres-ubereats:    # Banco OLTP
  minio-ubereats:       # Data Lake S3
  minio-setup:          # Cria bucket (roda 1x)
  gen-drivers:          # Gerador (tabela drivers)
  gen-users:            # Gerador (tabela users)
  gen-minio:            # Gerador (eventos JSON)
```

### Comandos Docker Compose Uteis

```powershell
# Ver status de todos os containers
docker-compose ps

# Ver logs de um servico
docker-compose logs -f postgres-ubereats

# Ver logs de multiplos servicos
docker-compose logs -f gen-drivers gen-users

# Restart de um servico especifico
docker-compose restart postgres-ubereats

# Parar um servico especifico
docker-compose stop gen-minio

# Iniciar um servico especifico
docker-compose up -d gen-minio

# Ver uso de recursos
docker stats
```

---

## Dependencias entre Servicos

```
postgres-ubereats (base)
    ↓
gen-drivers (depende do Postgres healthy)
gen-users (depende do Postgres healthy)

minio-ubereats (base)
    ↓
minio-setup (depende do MinIO healthy)
    ↓
gen-minio (depende do minio-setup completed)
```

**Ordem de inicializacao**:
1. Postgres e MinIO sobem em paralelo
2. Aguardam ficarem "healthy" (~15-30s)
3. `minio-setup` cria o bucket
4. Geradores sobem em paralelo

---

## Health Checks

### Postgres

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U usrUberEats -d ubereats_db"]
  interval: 10s
  timeout: 5s
  retries: 5
```

**Verificar manualmente**:
```powershell
docker exec postgres-ubereats pg_isready -U usrUberEats
```

### MinIO

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
  interval: 30s
  timeout: 20s
  retries: 3
```

**Verificar manualmente**:
```powershell
curl http://localhost:9000/minio/health/live
```

---

## Volumes Docker

### postgres_data

Armazena:
- Tabelas `drivers` e `users`
- Indices
- WAL (Write-Ahead Log)

**Localizacao**: Volume gerenciado pelo Docker

**Tamanho estimado**: ~5 GB (com 111k registros)

### minio_data

Armazena:
- Bucket `uber-eats`
- Eventos JSON (20+ streams)
- Metadata do MinIO

**Localizacao**: Volume gerenciado pelo Docker

**Tamanho estimado**: ~10 GB (depende do tempo rodando)

### Inspecionar Volumes

```powershell
# Listar volumes
docker volume ls

# Inspecionar volume
docker volume inspect uber-eats-case_postgres_data
docker volume inspect uber-eats-case_minio_data

# Ver tamanho
docker system df -v
```

---

## Troubleshooting

### Script nao executa (erro de policy)

```powershell
# Permitir execucao de scripts PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Ou execute com bypass:
powershell -ExecutionPolicy Bypass -File .\scripts\start-all.ps1
```

### Erro: "Port already in use"

```powershell
# Descobrir o que esta usando a porta
netstat -ano | findstr "5432"
netstat -ano | findstr "9000"
netstat -ano | findstr "9001"

# Parar tudo e tentar novamente
.\scripts\stop-all.ps1
.\scripts\start-all.ps1
```

### Containers "zumbis" (nao param)

```powershell
# Use o reset forcado
.\scripts\reset-all.ps1

# Ou force manualmente:
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
```

### Docker Desktop travou

```powershell
# Reinicie o Docker Desktop via System Tray
# Ou force:
Restart-Service docker

# Em ultimo caso: reinicie a maquina
```

---

## Performance e Otimizacao

### Consumo de Recursos (Estimativa)

| Cenario | CPU | RAM | Disco |
|---------|-----|-----|-------|
| **Apenas infra** | ~10% | 1 GB | 5 GB |
| **Infra + geradores** | ~25% | 2.5 GB | 15 GB |
| **Tudo + Airbyte** | ~45% | 6.5 GB | 25 GB |

### Otimizacoes

**Para maquinas com menos recursos**:

1. **Nao rode tudo junto**:
   ```powershell
   # Apenas infra (mais leve)
   .\scripts\start-infra.ps1
   ```

2. **Gere dados em etapas**:
   ```powershell
   # 1. Gere Postgres
   .\scripts\start-generators.ps1
   # Aguarde...
   .\scripts\stop-generators.ps1
   
   # 2. Depois gere MinIO (se necessario)
   docker-compose up -d gen-minio
   ```

3. **Ajuste o Docker Desktop**:
   - Settings > Resources
   - Reduza CPU e RAM alocados (minimo: 4 GB RAM, 2 CPUs)

---

## Automacao Avancada

### Criar Alias PowerShell

Adicione ao seu `$PROFILE`:

```powershell
# Abra o profile
notepad $PROFILE

# Adicione:
function Start-UberEatsInfra { .\scripts\start-infra.ps1 }
function Start-UberEatsAll { .\scripts\start-all.ps1 }
function Stop-UberEats { .\scripts\stop-all.ps1 }

Set-Alias -Name uberon -Value Start-UberEatsAll
Set-Alias -Name uberoff -Value Stop-UberEats

# Agora use:
# uberon   -> Inicia tudo
# uberoff  -> Para tudo
```

### Agendar Inicio Automatico (Task Scheduler)

```powershell
# Crie uma tarefa agendada no Windows
# Action: powershell.exe
# Arguments: -ExecutionPolicy Bypass -File "D:\uber-eats-case\scripts\start-infra.ps1"
# Trigger: At startup ou horario especifico
```

---

## Links

- Docker Compose: https://docs.docker.com/compose/
- PowerShell: https://docs.microsoft.com/powershell/
- Docker Desktop: https://www.docker.com/products/docker-desktop/

