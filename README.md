# Pipeline de Dados Uber Eats — Portfolio

Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats). O projeto implementa as melhores praticas de Data Engineering Moderna: arquitetura local automatizada (Docker + PowerShell), ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze → Silver → Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie.

---

## Primeiro clone?

Leia [`get_started/START_HERE.md`](get_started/START_HERE.md). Ele explica o fluxo agentic, a fonte canonica `.cursor/`, os espelhos `.github/` e `.claude/`, e o triangulo de contexto.

Veja também o índice completo em [`get_started/README.md`](get_started/README.md).

---

## Arquitetura (alto nível)

- Fontes: PostgreSQL (OLTP) e MinIO (Data Lake).
- Ingestão: Airbyte para extrair e carregar os dados.
- Processamento: Databricks Lakehouse como plataforma central.
- Transformação: Arquitetura Medalhão (Bronze → Silver → Gold).
- Governança: Unity Catalog (qualidade, linhagem e segurança).
- Consumo: Power BI e Databricks AI/BI Genie.

Modelo conceitual do domínio (entidades, relacionamentos e chave canônica): [`docs/MODELO_CONCEITUAL_UBER_EATS.md`](docs/MODELO_CONCEITUAL_UBER_EATS.md).

---

## Requisitos de Hardware

### Minimos Recomendados

- **CPU**: Intel Core i5 8ª geracao ou equivalente (4 cores)
- **RAM**: 16 GB (20 GB recomendado)
- **Armazenamento**: 50 GB livres (SSD preferencial)
- **Sistema Operacional**: Windows 10/11

---

## Pre-requisitos de Software

Instale e configure **antes** de rodar o projeto:

| Ferramenta | Para que serve |
|------------|----------------|
| **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** | Orquestra os containers do projeto. Deve estar **instalado e em execução** antes de qualquer script. |
| **Imagens Postgres + MinIO** | Não é preciso instalar Postgres ou MinIO no Windows. O `docker-compose.yml` baixa e sobe automaticamente `postgres:15` e `minio/minio` na primeira execução de `.\scripts\start-all.ps1`. |
| **[DBeaver](https://dbeaver.io/download/)** | Cliente gráfico para consultar o PostgreSQL local — equivalente ao SSMS no ecossistema SQL Server. Veja [docs/postgres/README.md](docs/postgres/README.md). |
| **PowerShell** 5.1+ ou 7+ (`pwsh`) | Executa os scripts de automação em `scripts/`. |
| **Licença ShadowTraffic** | [Free Trial](https://shadowtraffic.io) para gerar dados sintéticos. |
| **Workspace Databricks** | Opcional nesta fase; necessário para Lakeflow/DLT (camadas Bronze → Gold). |

Requisitos adicionais: Windows 10/11, acesso à internet (download de imagens Docker) e ~16 GB de RAM.

---

## Como Começar

### Passo 0: Instalar Docker Desktop e DBeaver

1. **Docker Desktop**: instale, abra o aplicativo e aguarde o ícone indicar que o engine está rodando.
2. **DBeaver**: instale para inspecionar tabelas `drivers` e `users` após subir o ambiente (host `localhost`, porta `5432`, credenciais do `shared/gen/.env`).
3. **Não instale** Postgres nem MinIO nativamente no SO — eles rodam **dentro do Docker** via `docker-compose`.

### Passo 1: Configurar Credenciais (Pasta `shared/gen/`)

Antes de provisionar o ambiente, você precisa configurar as credenciais e variáveis de ambiente:

1. **Copie o template de configuração**:
```powershell
copy shared\gen\.env.template shared\gen\.env
```

2. **Edite o arquivo `shared/gen/.env`** e preencha as variáveis:
```powershell
notepad shared\gen\.env
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
4. [shared/docs/shadowtraffic/README.md](shared/docs/shadowtraffic/README.md) - ShadowTraffic (gerador de dados)
5. [docs/airbyte/README.md](docs/airbyte/README.md) - Airbyte (ingestão de dados)

**Inicio rápido**:
```powershell
# Inicia toda a infraestrutura + geradores de dados
.\scripts\all\start-all.ps1

# Verifica o status
docker-compose ps
```

---

## Estrutura do Projeto

```
.
├── aws/                     # Trilha de ingestao AWS (Fase 2): src/, infra/, sql/, tests/
├── azure/                   # Trilha de ingestao Azure (Fase 1): src/, infra/, sql/, tests/, docs/
├── gcp/                     # Trilha de ingestao GCP (Fase 3): src/, infra/, sql/, tests/, docs/
├── shared/                  # ⚙️ Comum as 3 nuvens
│   ├── gen/                # Configurações e credenciais
│   │   ├── .env            # Suas credenciais (CONFIGURE PRIMEIRO!)
│   │   ├── .env.template   # Template de exemplo
│   │   └── setup-configs.ps1 # Script de injeção de secrets
│   ├── mongo/init/          # Seed do satélite "Perfil de Restaurante"
│   ├── sql/                 # 📊 Scripts SQL comuns (oracle/, postgres/, legacy/)
│   ├── pipeline/            # 🔄 Scripts Databricks (Lakeflow / DLT) — Bronze, Silver, Gold
│   │   └── README.md
│   └── docs/                # 📚 Documentação técnica comum
│       ├── README.md       # Índice da documentação
│       ├── automacao/      # Scripts PowerShell e Docker Compose
│       ├── postgres/       # PostgreSQL
│       ├── minio/          # MinIO
│       ├── shadowtraffic/  # ShadowTraffic
│       └── airbyte/        # Airbyte
├── config/                  # Dado de conexão/ambiente por nuvem (Debezium, hadoop-conf, deploy)
│   └── {aws,azure,gcp,shared}/
├── scripts/                 # 🤖 Scripts de automação, por assunto
│   ├── all/start-all.ps1   # Inicia tudo
│   ├── infra/start-infra.ps1 # Apenas infra
│   ├── shadowtraffic/start-generators.ps1 # Apenas geradores
│   ├── all/stop-all.ps1    # Para tudo
│   └── infra/reset-all.ps1 # Reset destrutivo
├── docker-compose.yml      # Orquestração Docker
└── README.md               # Este arquivo
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

- [x] Scripts SQL em `shared/pipeline/` (Bronze parcial, Silver, Gold inicial)
- [ ] Deploy e validação do pipeline Lakeflow no Databricks
- [ ] Governança completa (Unity Catalog em todos os ambientes)
- [ ] Dashboards (Power BI / Databricks AI/BI Genie)

**Próxima etapa**: Anexar os scripts de `shared/pipeline/` a um pipeline Lakeflow no workspace e validar Bronze → Silver → Gold. Veja [shared/pipeline/README.md](shared/pipeline/README.md) — inclui esclarecimento de que MySQL/Kafka/MongoDB estão **embarcados no MinIO**, não em containers extras.

---

## Acessos Rápidos

### URLs
- MinIO Console: `http://localhost:9001`
- Airbyte Console: `http://localhost:8000`

### Postgres
- Host: `localhost`
- Port: `5432`
- Database/User/Password: Conforme seu `shared/gen/.env`

### MinIO
- Console: `http://localhost:9001`
- API: `http://localhost:9000`
- User/Password: Conforme seu `shared/gen/.env`
- Bucket: `uber-eats`

---

## Comandos Rápidos

```powershell
# Iniciar ambiente completo
.\scripts\all\start-all.ps1

# Apenas infraestrutura (sem geradores)
.\scripts\infra\start-infra.ps1

# Verificar status
docker-compose ps

# Parar tudo (preserva dados)
.\scripts\all\stop-all.ps1

# Reset completo (APAGA DADOS!)
.\scripts\infra\reset-all.ps1
```

---

## Troubleshooting

Para problemas específicos, consulte a documentação de cada componente em `shared/docs/`:

- Scripts e automação: [shared/docs/automacao/README.md](shared/docs/automacao/README.md)
- PostgreSQL: [shared/docs/postgres/README.md](shared/docs/postgres/README.md)
- MinIO: [shared/docs/minio/README.md](shared/docs/minio/README.md)
- ShadowTraffic: [shared/docs/shadowtraffic/README.md](shared/docs/shadowtraffic/README.md)
- Airbyte: [shared/docs/airbyte/README.md](shared/docs/airbyte/README.md)

---

## Agentic / SDD

| Recurso | Uso |
|---------|-----|
| `CONTEXT.md` | Contexto rapido do projeto |
| `.cursorrules` | Regras de colaboracao e arquitetura |
| `.cursor/CURSOR.MD` | Contexto canonico do Cursor |
| `.cursor/agents/domain/uber-eats-case-expert.md` | Agente especialista do dominio (a criar a partir de `templates/agent-expert.md.j2`) |
| `.cursor/sdd/` | Contratos e artefatos SDD |
| `get_started/SDD_Guia_Comandos.md` | Guia dos comandos SDD |

Documentação completa do framework agentic: [`shared/docs/00-INDEX.md`](shared/docs/00-INDEX.md).

---

## Suporte e Contribuicoes

- **Documentacao Completa**: Veja a pasta `docs/` para detalhes tecnicos de cada componente
- **Issues**: Relate problemas via [GitHub Issues](https://github.com/jotap-rocha/uber-eats-case/issues)
- **Repositorio**: https://github.com/jotap-rocha/uber-eats-case

---

Pronto! Com isso voce tem uma fabrica de dados local completa para testes de pipelines, CDC e integracoes, com dados sinteticos realistas.
