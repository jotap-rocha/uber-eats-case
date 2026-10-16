---
# Regras de pipeline de dados — carrega ao tocar código de pipeline.
# Remova este arquivo se o projeto não for de pipeline de dados.
paths:
  - "src/pipeline/**"
  - "pipelines/**"
  - "dags/**"
  - "notebooks/**"
---

# Pipeline de Dados — Medallion + SOLID + Contratos

Regras para projetos de engenharia de dados. Gerado automaticamente pelo `/harness-architect`
quando o tipo de projeto for `pipeline`. Adapte conforme a stack real do projeto.

## Norma canônica (enforcement)

- Fonte normativa de **IDs de check** e **severidade** (blocker / warning / info):
  `data-engineering.yaml` na raiz do projeto (instalado pelo `/install-harness` na categoria
  `pipeline_dados`). Esta rule **não** redefine IDs — aponta para o YAML.
- Enforcement: CLI `python -m config.canonical_data_check` (`validate` / `baseline` /
  `compare` / `report` / `explain`).
- Marker no projeto-filho: `.harness/data-check/project_profile.yaml` — override de perfil
  (vence auto-detect no engine) e também dispara o `/validar` data-check.
- `/validar` (helper `data_check_validate_argv`): invoca data-check com **marker** **ou**
  auto-detect de pipeline cloud útil (**SDP** / **DLT**). **DAB isolado** não escolhe perfil
  `databricks-*` nem ativa o gate DE. Sem ambos → só ruff + mypy + pytest.
- Perfis cloud Loop 2: `databricks-sdp-medallion`, `databricks-dlt-legacy`,
  `databricks-multi` — checks do pacote **D** (`databricks-cloud`) conforme o perfil efetivo.

## Arquitetura Medallion — invariantes por camada

| Camada | Responsabilidade | NUNCA fazer | Colunas obrigatórias |
|---|---|---|---|
| **Raw** | Cópia exata da fonte, imutável | Transformar, deletar, sobrescrever | `_source_file`, `_ingest_ts` |
| **Bronze** | Preservar forma-fonte (JSON struct/array OK) + lineage | Regras de negócio, normalizar aninhados | `_ingested_at`, `_source`, `_source_system`, `_run_id`, `_batch_id` |
| **Silver** | Normalizado flat, contrato ODCS, qualidade | Agregações Gold, colunas multivaloradas | `_processed_at`, `_pipeline_version`, `_source_system` |
| **Gold** | Subset analítico de negócio (antes de Diamond) | Limpeza (Silver) | `_updated_at` |

**Raw é sagrado:** nunca modifique ou delete dados da camada Raw.

## Gates SDD e Dev Loop (processo)

Antes de implementar ou evoluir pipeline, o harness **pergunta** via:

- SDD: `harness-brainstorm` (passos **4a** runtime, **4a-bis** AI-DEV-KIT se Databricks, **4b** Medallion)
  + `harness-define` (passos **2a** runtime/kit, **2c** Medallion)
- Dev Loop: `prompt-crafter` (passo 3b)

Runtime Databricks + AI-DEV-KIT: `kb/databricks/patterns/ai-dev-kit-gate.md` (gate humano; hard-stop
se kit não instalado ou analista não conhece o conceito).

Checklist completo: `kb/pipeline/patterns/medallion-sdd-gates.md` (tabelas, colunas/amostra,
`_source_system`, JSON aninhado, contrato dual, Genie/NL).

Implementação Silver pós-gate: `kb/pipeline/patterns/silver-checklist-odcs.md`.

## SOLID para pipelines

- **S** — Cada classe de transform faz UMA coisa: `BronzeIngestor`, `SilverTransformer`, `GoldAggregator`.
- **O** — `BaseTransform` é extensível sem modificar: herdar e implementar `transform()`.
- **L** — Qualquer `BaseTransform` é substituível sem quebrar `Pipeline.run()`.
- **I** — `Readable` e `Writable` são interfaces separadas; não force implementar os dois.
- **D** — `Pipeline(reader, transform, writer)` depende de abstrações, não de Spark/Delta concreto.

## Data contracts

- **Bronze:** contrato de **ingestão** (schema-fonte; struct/array permitidos) — documenta o que chegou.
- **Silver:** contrato **ODCS** completo (flat, quality, SLA) — gate mecânico `DE-B003`.
- **Gold:** contrato de **consumo** opcional (colunas expostas, descrições para NL/Genie).
- Cada fonte Silver tem contrato em `data-contracts/` (YAML ou Pydantic).
- O contrato declara: schema, SLA de freshness, producer/consumer, regras de qualidade.
- **Violação de contrato = não passar silenciosamente.** Registre na quarantine e notifique o owner.

## Schema evolution

- **mergeSchema:** aceite apenas para adições não-breaking (novas colunas opcionais).
- **quarantine + notify:** para mudanças potencialmente breaking (tipo alterado, coluna removida).
- **fail:** para mudanças que violam o contrato declarado.
- Toda evolução aceita gera um ADR em `docs/adr/`.

## Quarantine

- Registros com schema inválido ou regras de qualidade violadas vão para
  `{catalog}.bronze.quarantine` (ou equivalente na stack local).
- Quarantine inclui: dados originais + `_quarantine_reason` + `_quarantine_ts`.
- Taxa de quarantine > [THRESHOLD]% dispara notificação automática ao owner.

## Configuração centralizada

- **NUNCA hardcode** catalog, schema, workspace URL, table names.
- Tudo via `PipelineConfig` carregado de `config/environments/{PIPELINE_ENV}.yaml`.
- Mudar de DEV para PRD = mudar `PIPELINE_ENV=prd`. Zero edição de código.

## Observabilidade obrigatória

- Log estruturado por step: `pipeline`, `layer`, `run_id`, `records_in`, `records_out`,
  `records_quarantined`, `duration_ms`. Sem PII em logs. (Ver `rules/seguranca.md`.)
- Notificação ao owner via webhook (Slack/Teams/email) para: schema mismatch, alta taxa de
  quarantine, SLA breach, falha de step.

## Linhagem

- Toda tabela gerada pelo pipeline contém as colunas de lineage obrigatórias (ver Medallion acima).
- Em Databricks: Unity Catalog rastreia lineage automaticamente — não desabilite.
- Em local/Airflow: adicione `_pipeline_version` e `_run_id` para rastrear manualmente.
