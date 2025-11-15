# Pipeline de Dados Uber Eats — Portfólio (End-to-End)

Este projeto é a primeira etapa de uma arquitetura de dados completa, construída como parte do desafio Semana Databricks 2.0. Automatizei um ambiente local (com Docker Compose + PowerShell) que simula fontes reais: PostgreSQL (OLTP) e MinIO (S3) alimentados em tempo real pelo ShadowTraffic. A arquitetura end-to-end prevista inclui ingestão com Airbyte, processamento no Databricks Lakehouse, transformações na Arquitetura Medalhão e governança com Unity Catalog, preparando consumo em Power BI e Databricks AI/BI Genie.

---

## Arquitetura (alto nível)
- Fontes: PostgreSQL (OLTP) e MinIO (Data Lake).
- Ingestão: Airbyte para extrair e carregar os dados.
- Processamento: Databricks Lakehouse como plataforma central.
- Transformação: Arquitetura Medalhão (Bronze → Silver → Gold).
- Governança: Unity Catalog (qualidade, linhagem e segurança).
- Consumo: Power BI e Databricks AI/BI Genie.

## Escopo deste repositório
- Implementa a Etapa 1: simulação local das fontes (PostgreSQL + MinIO) e orquestração dos geradores ShadowTraffic.
- Fornece scripts para start/stop/reset e criação automática de tabelas/bucket.
- As etapas de ingestão (Airbyte), processamento/transformação (Databricks) e consumo são parte da visão do projeto, mas não foram construídas ainda.

## Visão Geral (infra local desta etapa)
- PostgreSQL: dados de `drivers` e `users` (tabelas criadas automaticamente por `sql/*.sql`).
- MinIO: bucket `uber-eats` para eventos JSON (console em `http://localhost:9001`).
- ShadowTraffic: geradores sintéticos para popular Postgres e MinIO.
- Scripts PowerShell automatizam setup e orquestração (`start-all.ps1`, `stop-all.ps1`, `reset-all.ps1`).

## Pré-requisitos
- Para esta etapa (infra local):
	- Windows 10/11 com Docker Desktop instalado e em execução.
	- PowerShell 5.1+ (padrão do Windows) ou PowerShell 7+ (`pwsh`).
	- Acesso à internet para baixar imagens Docker.
- Para próximas etapas (opcional):
	- Workspace Databricks com Unity Catalog habilitado.
	- Airbyte (self-hosted via Docker) para ingestão a partir das fontes locais.

## Estrutura do Projeto
```
.
├─ docker-compose.yml
├─ start-all.ps1
├─ stop-all.ps1
├─ reset-all.ps1
├─ gen/
│  ├─ .env.template        # Modelo para credenciais e variáveis
│  ├─ setup-configs.ps1    # Injeta variáveis do .env nos JSONs de geradores
│  ├─ minio/
│  │  └─ uber-eats.json    # Config do gerador para MinIO
│  └─ postgres/
│     ├─ drivers.json.template
│     └─ users.json.template
└─ sql/
	 ├─ create_drivers_table.sql
	 ├─ create_users_table.sql
	 └─ cdc configure/
			└─ database-cdc-config.sql
```

## Configuração (apenas uma vez)
1) Crie o arquivo `.env` a partir do template:
```
copy gen\.env.template gen\.env
```
2) Edite `gen/.env` e preencha as variáveis conforme seu ambiente/licença do ShadowTraffic. Para um ambiente local padrão, use:
- Postgres
	- `POSTGRES_HOST=localhost`
	- `POSTGRES_PORT=5432`
	- `POSTGRES_DB=ubereats_db`
	- `POSTGRES_USERNAME=usrUberEats`
	- `POSTGRES_PASSWORD=supersecret`
- MinIO
	- `AWS_REGION=us-east-1`
	- `AWS_S3_FORCE_PATH_STYLE=true`
	- `AWS_ACCESS_KEY_ID=usrUberEats`
	- `AWS_SECRET_ACCESS_KEY=supersecret`
- Licença ShadowTraffic: preencha os campos `LICENSE_*` conforme sua licença.

3) (Opcional) Gerar os JSONs de configuração para os geradores de Postgres manualmente:
```
powershell -ExecutionPolicy Bypass -File .\gen\setup-configs.ps1
```
Observação: o `start-all.ps1` executa esse passo automaticamente antes de subir os containers.

## Como Executar
1) Certifique-se de que o Docker Desktop está em execução.
2) No terminal (cmd.exe), execute o script de inicialização:
```
powershell -ExecutionPolicy Bypass -File .\start-all.ps1
```
O script:
- Injeta segredos/variáveis de `gen/.env` nos templates de Postgres (`drivers.json` e `users.json`).
- Sobe toda a infraestrutura via `docker-compose up -d` (em background).

Dicas:
- O ambiente sobe em background (detached). Veja logs com: `docker-compose logs -f`
- Para acompanhar um serviço específico: `docker-compose logs -f postgres-ubereats`
- A primeira execução pode levar ~1-2 minutos (download de imagens e inicialização do Postgres/MinIO).

## Acessos Rápidos
- Postgres: `localhost:5432` | DB: `ubereats_db` | Usuário: `usrUberEats` | Senha: `supersecret`
- MinIO Console: `http://localhost:9001` | Usuário: `usrUberEats` | Senha: `supersecret`
- Bucket MinIO: `uber-eats` (criado automaticamente pelo serviço `minio-setup`).

As tabelas `drivers` e `users` são criadas automaticamente a partir de `sql/create_*_table.sql` quando o volume do Postgres é criado pela primeira vez.

## Parar e Resetar
- Parar e manter os dados (volumes preservados):
```
powershell -ExecutionPolicy Bypass -File .\stop-all.ps1
```
- Reset total (DESTRUTIVO: remove volumes/dados):
```
powershell -ExecutionPolicy Bypass -File .\reset-all.ps1
```

## Solução de Problemas
- `.env` ausente: o `setup-configs.ps1` falhará. Crie `gen/.env` a partir de `gen/.env.template` e preencha as variáveis.
- Portas em uso: verifique se as portas `5432`, `9000`, `9001` não estão ocupadas por outros serviços.
- Docker não iniciado: garanta que o Docker Desktop esteja rodando antes de executar os scripts.
- Execução de scripts bloqueada: use `-ExecutionPolicy Bypass` como mostrado nos comandos acima.
- Verificar logs específicos:
```
docker-compose logs postgres-ubereats
docker-compose logs minio-ubereats
docker-compose logs gen-drivers
docker-compose logs gen-users
docker-compose logs gen-minio
```

## O que está sendo executado (docker-compose)
- `postgres-ubereats`: Postgres 15 com `wal_level=logical`, expõe `5432`.
- `minio-ubereats`: MinIO com API `9000` e console `9001`.
- `minio-setup`: cria o bucket `uber-eats` automaticamente.
- `gen-drivers` e `gen-users`: geradores ShadowTraffic para Postgres (usam `gen/postgres/*.json`).
- `gen-minio`: gerador ShadowTraffic para MinIO (usa `gen/minio/uber-eats.json`).

## Licenças e Credenciais
- Nunca commite arquivos `.env` ou configs geradas (`.json`) com credenciais.
- Os templates `.json.template` usam placeholders e são seguros para versionamento.

---

Pronto! Com isso você tem uma fábrica de dados local para testes de pipelines, CDC e integrações, com dados sintéticos realistas.
