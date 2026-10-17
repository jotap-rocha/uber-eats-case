> **Este repositório é o projeto `uber-eats-case`, não o Agent Harness Canônico.**
> Não copie o guia do repositório canônico do harness. Refine com `/grill-me`, `/grill-with-docs` ou `harness-architect`.

# Pipeline de Dados Uber Eats - Portfolio — Contexto para Claude Code

Pipeline completo de engenharia de dados construido como portfolio profissional, simulando um ambiente de producao de um aplicativo de delivery (Uber Eats): ingestao com Airbyte, processamento no Databricks Lakehouse com Delta Live Tables, Arquitetura Medalhao (Bronze -> Silver -> Gold), governanca com Unity Catalog e consumo em Power BI / Databricks AI/BI Genie.. Repositório agentic com agentes, comandos e knowledge bases para desenvolvimento assistido por IA em Cursor, Claude Code e GitHub Copilot.

---

## Fontes de Verdade

| Recurso | Caminho | Uso |
|---------|---------|-----|
| Contexto rápido | `CONTEXT.md` | Onboarding mínimo e comandos principais |
| Índice de documentação | `shared/docs/00-INDEX.md` | Navegação dos guias do projeto |
| Contexto Claude Code completo | `.claude/CURSOR.md` | Agentes, KBs, comandos e roteamento no ecossistema `.claude/` |
| Roteador de agentes | `.claude/commands/core/router.md` | Escolha de agente e escopo por intenção |
| Arquitetura do roteador | `.claude/sdd/architecture/AGENT_ROUTER.yaml` | Fonte estruturada dos agentes e hints |
| Roadmap multi-cloud | `shared/docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` | Plano das fases (0 a 4), decisões e histórico de revisões |

---

## Stack

| Camada | Tecnologia |
|--------|------------|
| Fontes (Docker local) | Postgres, Oracle Free 23ai (`gvenzl/oracle-free`), MongoDB, MinIO |
| Geração de dados | ShadowTraffic (`gen-unified`, `shared/gen/unified/uber-eats.json.template`) |
| Ingestão / CDC | Airbyte OSS (Postgres, MongoDB, MinIO), Debezium + Kafka Connect (Oracle) |
| Lakehouse | Databricks (Lakeflow/DLT, Unity Catalog), Bronze -> Silver -> Gold em `shared/pipeline/` |
| Clouds (fases) | Azure (Fase 1), AWS (Fase 2), GCP (Fase 3), cada uma com Warehouse, Lakehouse e Kappa |
| IaC | Terraform (`{aws,azure,gcp}/infra/`); DAB só para jobs Databricks |
| Qualidade | `pytest` e `ruff` (testes por trilha em `{cloud}/tests/`) |
| Ambiente | Windows 11, Docker Desktop, scripts PowerShell em `scripts/` |

cloud: azure, aws, gcp

Estrutura: `aws/`, `azure/`, `gcp/` (trilhas de ingestão), `shared/` (pipeline, gen, docs comuns), `config/` (conexões por nuvem), `scripts/`. Detalhes em `CONTEXT.md`.

---

## Invariantes

Regras do projeto que não se quebram sem decisão explícita do usuário. Validadas em entrevista (`/grill-me`, 2026-10-17). Itens marcados **(revisável)** são decisões atuais: o agente pode propor mudança com justificativa, mas não muda sozinho.

### Ambientes (dsv / prd)

- **Dois ambientes.** `dsv` (desenvolvimento) e `prd` (produção). Hoje o par Databricks é `DEV` (`dbc-029603a1-3b9b`) e `PRD` (`dbc-30ffc0e9-e96a`), perfis em `~/.databrickscfg`. Ambos são workspaces AWS (`cloud.databricks.com`). O desenvolvimento Databricks usa o **Databricks Free Edition**, que não tem suporte a Terraform: nenhum workspace Databricks é criado por Terraform, e o lakehouse reaproveita o projeto anterior (novo lakehouse). Se algum dia houver workspace Azure Databricks, será decisão do usuário.
- **Código único, parametrizado por ambiente.** PRD replica o DSV com os nomes dos ativos de PRD; a diferença vive só em variáveis (variáveis do bundle, `.tfvars`), nunca em edição manual de nomes no código.
- **DSV:** escrita livre pelo agente. **PRD:** o agente nunca escreve direto (nada de CLI/SDK/SQL com `--profile PRD` que altere algo). Só promove por pipeline de deploy, com o mesmo código já validado no DSV e confirmação do usuário a cada deploy. Leitura no PRD (consulta, `bundle validate`) é livre.
- **PRD é criado por fase e sob decisão do usuário**, não em toda nuvem de antemão. Até o CI existir, o agente não aplica nada em PRD.
- **Mecanismo de deploy por camada:** Terraform para recursos e definições declarativas (Event Hubs, ADLS, Kinesis, S3, Pub/Sub, query do Stream Analytics, jobs Glue); scripts SQL versionados e numerados em `{cloud}/sql/`, idempotentes, aplicados pela CLI da nuvem (`sqlcmd`, `bq`, `psql`) para o que roda dentro do serviço (Synapse, Redshift, BigQuery); DABs só para Databricks.
- **Promoção por `main` única + GitHub Actions + Environments.** Merge na `main` faz deploy no dsv da nuvem afetada (`paths:`); o job de prd exige aprovação do usuário (required reviewer). Sem branches por ambiente. Esse CI é fase própria de trabalho e pode ser levado depois ao agent-harness. Agentes de apoio: `iac-engineer` (Terraform) e `cloud-data-engineer` (warehouse, streaming, storage, custo).

### Dados e fontes

- **Todo dado do projeto é sintético** (ShadowTraffic). Sem `[AVISO_LGPD]` nem `rules/pii.md`. Se dado de pessoa real for carregado em qualquer fonte ou no repo, o agente para e avisa; a decisão de LGPD volta ao usuário. Mesmo sendo sintético, não imprimir registros crus de `users`/`drivers` em logs, docs ou PRs (usar contagens, schemas e exemplos falsos).
- **Teto do Oracle Free (12 GB) é aceito e permanente.** `orders`, `payments`, `drivers`, `products` e `restaurants` não crescem mais; o gerador será congelado. Não rediagnosticar como bug nem propor purge ou migração, salvo pedido do usuário.
- **Todos os bancos do projeto (Oracle, Postgres, MongoDB, MinIO, na Fase 0) são tratados como produção:** nunca `DROP`, `TRUNCATE`, `docker compose down -v`, `docker volume rm` ou purge sem confirmação.
- **Contrato canônico de CDC na Bronze:** `cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`. A Silver nunca lê o formato nativo de cada ferramenta de ingestão.
- A Fase 0 (fontes locais) não migra para a nuvem. Cada cloud ingere dela via rede.

### ShadowTraffic

- Ao editar `uber-eats.json.template`, usar a skill `shadowtraffic-adicionar-generator-seguro`.
- Religar ou ajustar o gerador com `shadowtraffic-ajustar-geracao`. Não usar `start-generators.ps1` / `stop-generators.ps1` direto quando as tabelas já têm dados (não recalculam `startingFrom` e já travaram o pipeline).
- Licença expirada: `shadowtraffic-renovar-licenca`.

### Arquitetura por cloud

- O Kappa lê só do barramento (Event Hub, Kinesis, Pub/Sub) e nunca do storage batch.
- Azure: Synapse é **Dedicated SQL Pool** (Serverless não suporta `MERGE`).
- **(revisável)** Azure: uma captura CDC por fonte; o trilho batch vem de um Kafka Connect Sink sobre o mesmo tópico (ADLS Sink é o maior risco técnico da Fase 1).
- **(revisável)** Azure: o `kafka-connect-azure` (porta 8084) é separado do `kafka-connect` local. Não repontar o local para a nuvem.
- **(revisável)** Conta cloud só é aberta no início da fase correspondente (créditos têm validade curta).
- AWS e GCP não usam Databricks: têm stack própria (Fase 2 e 3). Terraform é a única ferramenta de provisionamento.

### Custo

- Antes de `terraform apply` que crie ou escale recurso pago, mostrar o `plan` e uma estimativa de custo por hora/dia dos recursos novos, e esperar o "ok". Sem estimativa, não aplica.
- Todo recurso de custo contínuo (Synapse Dedicated, Event Hubs, clusters) nasce no Terraform com *budget alert* da conta. Teto de referência: cerca de R$ 200 (a confirmar pelo usuário ao abrir cada conta). Antes de abrir a conta, o agente conduz um planejamento de pré-requisitos; a conta só é aberta com todos os itens prontos e com o acompanhamento do agente.
- Ao fim de uma sessão com recurso caro ligado, o agente lista o que está rodando e pergunta se pausa ou destrói. Nunca deixa passar em silêncio.
- `terraform destroy` e pause nunca são automáticos: sempre com confirmação.
- Priorizar serverless e on-demand.

### Segurança e versionamento

- Segredos reais ficam fora do git (`shared/gen/.env`, `.tfvars` com credenciais).
- Commit e push só com confirmação do usuário, seguindo `git-boas-praticas-versionamento`.

---

## Comandos de Verificação

Este projeto não possui hoje uma suite de testes de aplicação na raiz. Use os comandos abaixo como verificação padrão:

```bash
python3 scripts/tooling/validate-agent-router.py
python3 install_dev_loop/install_dev_loop.py --dry-run --target .
```

Não há CI configurada no repositório no momento (pode ser adicionada em `.github/workflows/` se necessário).

---

## Dev Loop

O Dev Loop fica em `.claude/dev/` e oferece um fluxo de desenvolvimento nível 2 baseado em PROMPTs versionáveis.

### Quick Start

```bash
# Criar um PROMPT guiado pelo agente prompt-crafter
/dev "descreva o que você quer construir"

# Executar o primeiro PROMPT específico deste repositório
/dev tasks/PROMPT_HELLO_WORLD.md

# Executar o bootstrap do Dev Loop novamente, se precisar revisar a instalação
/dev tasks/PROMPT_INIT_DEV_LOOP.md
```

### Estrutura

```text
.claude/dev/
├── _index.md              # Documentação principal do Dev Loop
├── readme.md              # Visão curta do AgentLoop
├── docs/                  # Documentação de apoio
├── tasks/                 # PROMPT_*.md executáveis
├── templates/             # Templates de PROMPT e PROGRESS
├── examples/              # Exemplos e notas de execuções
├── progress/              # Memória de execução gerada pelo executor
└── logs/                  # Logs finais gerados pelo executor
```

Leia `.claude/dev/_index.md` para detalhes de uso, recuperação de sessão e opções como `--resume`, `--dry-run` e `--mode`.

---

## Convenções de Trabalho

- Responder em português brasileiro, salvo pedido explícito em outro idioma.
- Manter mudanças pequenas, focadas e alinhadas ao padrão existente.
- Não commitar segredos, `.env` real nem inventário local de infraestrutura.
- Ao alterar agentes, comandos ou roteamento, validar com `python3 scripts/tooling/validate-agent-router.py`.
- Quando a mudança afetar fluxo de uso, atualizar documentação em `CONTEXT.md`, `shared/docs/00-INDEX.md` ou `.claude/dev/_index.md`, conforme o escopo.
