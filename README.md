# Pipeline de Dados Uber Eats — Portfolio

Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats). O projeto implementa as melhores praticas de Data Engineering Moderna: arquitetura local automatizada (Docker + PowerShell), ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze → Silver → Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie.

---

## Arquitetura (alto nível)

- Fontes: PostgreSQL (OLTP) e MinIO (Data Lake).
- Ingestão: Airbyte para extrair e carregar os dados.
- Processamento: Databricks Lakehouse como plataforma central.
- Transformação: Arquitetura Medalhão (Bronze → Silver → Gold).
- Governança: Unity Catalog (qualidade, linhagem e segurança).
- Consumo: Power BI e Databricks AI/BI Genie.

---

## Requisitos de Hardware

### Minimos Recomendados

- **CPU**: Intel Core i5 8ª geracao ou equivalente (4 cores)
- **RAM**: 16 GB (20 GB recomendado)
- **Armazenamento**: 50 GB livres (SSD preferencial)
- **Sistema Operacional**: Windows 10/11

---

## Pre-requisitos de Software

- Windows 10/11 com Docker Desktop instalado e em execucao
- PowerShell 5.1+ (padrao do Windows) ou PowerShell 7+ (`pwsh`)
- Acesso a internet para baixar imagens Docker
- Workspace Databricks com Unity Catalog (opcional, para proximas etapas)
- Licenca ShadowTraffic Free Trial (https://shadowtraffic.io)

---

## Como Começar

### Passo 1: Configurar Credenciais

Antes de provisionar o ambiente, você precisa configurar as credenciais em dois arquivos:

#### A) Credenciais do Docker Compose (raiz do projeto)

1. **Copie o template**:
```powershell
copy .env.template .env
```

2. **Edite o arquivo `.env`** e preencha suas credenciais:
```powershell
notepad .env
```

**Variáveis principais**:
```ini
# PostgreSQL
POSTGRES_USER=<seu_usuario>
POSTGRES_PASSWORD=<sua_senha>
POSTGRES_DB=ubereats_db

# MinIO
MINIO_ROOT_USER=<seu_usuario>
MINIO_ROOT_PASSWORD=<sua_senha>
```

#### B) Credenciais do ShadowTraffic (pasta `gen/`)

1. **Copie o template**:
```powershell
copy gen\.env.template gen\.env
```

2. **Edite o arquivo `gen/.env`** e preencha as variáveis:
```powershell
notepad gen\.env
```

**Variáveis principais**:

```ini
# PostgreSQL (defina seu usuário e senha)
POSTGRES_HOST=postgres-ubereats
POSTGRES_PORT=5432
POSTGRES_DB=ubereats_db
POSTGRES_USERNAME=<seu_usuario>
POSTGRES_PASSWORD=<sua_senha>

# MinIO (defina seu usuário e senha)
AWS_REGION=us-east-1
AWS_S3_FORCE_PATH_STYLE=true
AWS_ACCESS_KEY_ID=<seu_usuario>
AWS_SECRET_ACCESS_KEY=<sua_senha>

# ShadowTraffic (obtenha em https://shadowtraffic.io)
LICENSE_ID=<seu_license_id>
LICENSE_KEY=<sua_license_key>
LICENSE_EMAIL=<seu_email>
LICENSE_OWNER=<seu_nome>
```

3. **Gere os arquivos de configuração** (opcional, o `start-all.ps1` faz isso automaticamente):
```powershell
powershell -ExecutionPolicy Bypass -File .\gen\setup-configs.ps1
```

---

### Passo 2: Provisionar o Ambiente (Pasta `docs/`)

Após configurar as credenciais, consulte a **documentação completa** em `docs/` para provisionar cada componente:

📚 **[Acesse a documentação completa aqui: docs/README.md](docs/README.md)**

**Ordem recomendada**:
1. [docs/automacao/README.md](docs/automacao/README.md) - Scripts de automação e Docker Compose
2. [docs/postgres/README.md](docs/postgres/README.md) - PostgreSQL (banco OLTP)
3. [docs/minio/README.md](docs/minio/README.md) - MinIO (Data Lake)
4. [docs/shadowtraffic/README.md](docs/shadowtraffic/README.md) - ShadowTraffic (gerador de dados)
5. [docs/airbyte/README.md](docs/airbyte/README.md) - Airbyte (ingestão de dados)

**Inicio rápido**:
```powershell
# Inicia toda a infraestrutura + geradores de dados
.\scripts\start-all.ps1

# Verifica o status
docker-compose ps
```

---

## Estrutura do Projeto

```
.
├── gen/                    # ⚙️ Configurações e credenciais
│   ├── .env               # Suas credenciais (CONFIGURE PRIMEIRO!)
│   ├── .env.template      # Template de exemplo
│   ├── setup-configs.ps1  # Script de injeção de secrets
│   ├── postgres/          # Configs ShadowTraffic para Postgres
│   └── minio/             # Configs ShadowTraffic para MinIO
├── docs/                   # 📚 Documentação técnica completa
│   ├── README.md          # Índice da documentação
│   ├── automacao/         # Scripts PowerShell e Docker Compose
│   ├── postgres/          # PostgreSQL
│   ├── minio/             # MinIO
│   ├── shadowtraffic/     # ShadowTraffic
│   └── airbyte/           # Airbyte
├── scripts/                # 🤖 Scripts de automação
│   ├── start-all.ps1      # Inicia tudo
│   ├── start-infra.ps1    # Apenas infra
│   ├── start-generators.ps1 # Apenas geradores
│   ├── stop-all.ps1       # Para tudo
│   └── reset-all.ps1      # Reset destrutivo
├── sql/                    # 📊 Scripts SQL (DDL, CDC)
├── pipeline/               # 🔄 Scripts Databricks (Delta Live Tables)
│   └── README.md          # Pipelines Lakeflow (em desenvolvimento)
├── docker-compose.yml      # Orquestração Docker
└── README.md              # Este arquivo
```

---

## Dados Gerados

O ambiente atual possui:
- **111.348 registros** na tabela `drivers`
- **111.155 registros** na tabela `users`
- **20+ streams de eventos JSON** no bucket MinIO `uber-eats` (orders, gps, payments, etc.)

---

## Status do Projeto

### ✅ Concluído

- [x] Infraestrutura local (Docker + PostgreSQL + MinIO)
- [x] Geração de dados sintéticos (ShadowTraffic)
- [x] Scripts de automação (PowerShell)
- [x] Configuração de ingestão (Airbyte OSS)
- [x] Documentação técnica completa

### 🚧 Em Desenvolvimento

- [ ] Pipelines Databricks (Delta Live Tables)
  - Camada Bronze (Auto Loader + CDC)
  - Camada Silver (Limpeza e transformação)
  - Camada Gold (Agregações e métricas)
- [ ] Governança (Unity Catalog)
- [ ] Dashboards (Power BI / Databricks AI/BI Genie)

**Próxima etapa**: Os scripts de processamento de dados no Databricks serão desenvolvidos e armazenados na pasta `pipeline/`. Esses scripts serão anexados ao **Lakeflow (Delta Live Tables)** para implementar a Arquitetura Medalhão.

---

## Acessos Rápidos

### URLs
- MinIO Console: `http://localhost:9001`
- Airbyte Console: `http://localhost:8000`

### Postgres
- Host: `localhost`
- Port: `5432`
- Database/User/Password: Conforme seu `gen/.env`

### MinIO
- Console: `http://localhost:9001`
- API: `http://localhost:9000`
- User/Password: Conforme seu `gen/.env`
- Bucket: `uber-eats`

---

## Comandos Rápidos

```powershell
# Iniciar ambiente completo
.\scripts\start-all.ps1

# Apenas infraestrutura (sem geradores)
.\scripts\start-infra.ps1

# Verificar status
docker-compose ps

# Parar tudo (preserva dados)
.\scripts\stop-all.ps1

# Reset completo (APAGA DADOS!)
.\scripts\reset-all.ps1
```

---

## Troubleshooting

Para problemas específicos, consulte a documentação de cada componente em `docs/`:

- Scripts e automação: [docs/automacao/README.md](docs/automacao/README.md)
- PostgreSQL: [docs/postgres/README.md](docs/postgres/README.md)
- MinIO: [docs/minio/README.md](docs/minio/README.md)
- ShadowTraffic: [docs/shadowtraffic/README.md](docs/shadowtraffic/README.md)
- Airbyte: [docs/airbyte/README.md](docs/airbyte/README.md)

---

## Suporte e Contribuicoes

- **Documentacao Completa**: Veja a pasta `docs/` para detalhes tecnicos de cada componente
- **Issues**: Relate problemas via [GitHub Issues](https://github.com/jotap-rocha/uber-eats-case/issues)
- **Repositorio**: https://github.com/jotap-rocha/uber-eats-case

---

Pronto! Com isso voce tem uma fabrica de dados local completa para testes de pipelines, CDC e integracoes, com dados sinteticos realistas.
