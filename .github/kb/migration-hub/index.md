# Migration hub — índice único (KB)

Ponto de entrada quando trabalhas com **`.github/kb`** ou `@`. **Este directorio** (`.github/kb/migration-hub/`) concentra a documentação narrativa da migração e da stack; **código executável** (scripts de infra, dbt): **`/DATALAKE/workspace/jp/platform/`** (`scripts/`, `dbt/`).

> **Revisão documental:** 2026-06-03

## Onde está o quê

| Conteúdo | Caminho |
|----------|---------|
| **Índice (este ficheiro)** | [`index.md`](index.md) |
| **Domínio migração** | [`migration/index.md`](migration/index.md) |
| **Scripts + dbt** | `/DATALAKE/workspace/jp/platform/` — ver [`README.md`](/DATALAKE/workspace/jp/platform/README.md) |
| **Ponte curta** (lista de links) | [`../migration/index.md`](../migration/index.md) |
| **Manifest YAML** | [`_index.yaml`](_index.yaml) |
| **Agente KB Architect** | [`../../agents/exploration/kb-architect.md`](../../agents/exploration/kb-architect.md) |
| **Agente migração Spark** | [`../../agents/data-engineering/spark-cluster-migration-expert.md`](../../agents/data-engineering/spark-cluster-migration-expert.md) |

## Ordem de leitura sugerida (migração)

1. [`planning.md`](planning.md)
2. [`migration/index.md`](migration/index.md)
3. [`naming_conventions.md`](naming_conventions.md)
4. [`infra/STATUS-AMBIENTE.md`](infra/STATUS-AMBIENTE.md)
5. [`infra/ssh_configuration.md`](infra/ssh_configuration.md) (malha **311**/**314**, chaves, `rsync`)

Validação em lote (311, utilizador `hadoop`):

`/DATALAKE/workspace/jp/platform/scripts/infra/validate_cluster.sh`

Malha SSH (311 e 314 → todos os nós), chaves e `rsync`: [`infra/ssh_configuration.md`](infra/ssh_configuration.md).

## Outros domínios em `.github/kb/`

Exemplos: [`../airflow/`](../airflow/index.md) (práticas DAG TaskFlow 2.11), [`../migration/`](../migration/), [`../spark/`](../spark/), [`../lakeflow/`](../lakeflow/), [`../sql-capacity/`](../sql-capacity/), [`../pydantic/`](../pydantic/).

---

## Por onde começar

| Se você quer… | Abra |
|---------------|------|
| Roadmap, fases A–G, migração de jobs | [`planning.md`](planning.md) |
| Estado actual das máquinas | [`infra/STATUS-AMBIENTE.md`](infra/STATUS-AMBIENTE.md) |
| SSH entre nós (311/314), `rsync` | [`infra/ssh_configuration.md`](infra/ssh_configuration.md) |
| Migração legado → novo (domínio) | [`migration/index.md`](migration/index.md) |
| Piloto SQL Capacity Job 08 (YARN) | [`migration/patterns/sql-capacity-yarn-prd-piloto.md`](migration/patterns/sql-capacity-yarn-prd-piloto.md) |
| SSL Java 11 + SQL Server (SHA1withRSA) | [`migration/patterns/java11-sqlserver-ssl-dual-cause.md`](migration/patterns/java11-sqlserver-ssl-dual-cause.md) |
| **Destino IHMTZBDBI via pyodbc** | [`migration/patterns/pyodbc-destino-ihmtzbdbi.md`](migration/patterns/pyodbc-destino-ihmtzbdbi.md) |
| **Modelo híbrido PySpark + pyodbc** | [`migration/patterns/pyodbc-destino-hibrido-pyspark.md`](migration/patterns/pyodbc-destino-hibrido-pyspark.md) |
| **Oracle VIPs + firewall (DPY-6005)** | [`migration/patterns/oracle-python-oracledb-vips-firewall.md`](migration/patterns/oracle-python-oracledb-vips-firewall.md) |
| Arquitetura da stack | [`architecture.md`](architecture.md) |
| Equipe / logins | [`team.md`](team.md) |

## Domínios (`kb-architect`)

| Domínio | Conteúdo |
|---------|-----------|
| **infra/** | [`STATUS-AMBIENTE.md`](infra/STATUS-AMBIENTE.md), Python, Java, [**SSH / malha 311–314**](infra/ssh_configuration.md), observabilidade |
| **hadoop/** | Instalação / guia Hadoop |
| **spark/** | [**PADRAO spark-submit PRD**](spark/PADRAO-SPARK-SUBMIT-PROJETO-PRD.md), ADLS, checklists, `01-spark-3.5.2.md` |
| **data-stack/** | **airflow/** (314, EDGE-314), **dbt/**, **datalake/** |
| **labs/** | Laboratórios (ex. WordCount YARN) |
| **migration/** | Índice, *quick-reference*, conceitos, padrão de portação, **piloto SQL Capacity YARN** |

## Raiz do KB (ficheiros transversais)

- [`architecture.md`](architecture.md) · [`cluster_topology.md`](cluster_topology.md) · [`inventory.md`](inventory.md)
- [`naming_conventions.md`](naming_conventions.md) · [`acess_links.md`](acess_links.md)
- [`planning.md`](planning.md) · [`team.md`](team.md)

## Projeto dbt (código em `platform`)

- Modelos e `dbt_project.yml`: **`/DATALAKE/workspace/jp/platform/dbt/datalake_dbt/`**
- Documentação do adapter + ambiente: [`data-stack/dbt/README.md`](data-stack/dbt/README.md)

## Automatização

- Validação cluster: [`validate_cluster.sh`](/DATALAKE/workspace/jp/platform/scripts/infra/validate_cluster.sh)

## Agente (estruturação do KB)

Para criar ou auditar domínios no estilo **KB Architect**, use no Cursor o agente em  
[`kb-architect.md`](../../agents/exploration/kb-architect.md).

## Agente (migração Spark legado → YARN)

Para portação de jobs, adaptação de `spark-submit` e validação no cluster novo, use  
[`spark-cluster-migration-expert.md`](../../agents/data-engineering/spark-cluster-migration-expert.md).
