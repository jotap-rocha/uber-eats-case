# Padrões de desenho — projetos de dados (pastas e pipelines)

> **Propósito:** Árvore **obrigatória** para repositórios Python de **dados** (ETL, pipelines, multi-fonte): `etl/`, `pipelines/`, `src/`, `sql/`, `tests/`, `config/`, `data/`, `logs/`, `docs/`.
> **MCP Validated:** 2026-05-15

## Navegação

### Conceitos (≤150 linhas)

| Ficheiro | Tema |
|----------|------|
| [concepts/obrigatoriedade-arvore.md](concepts/obrigatoriedade-arvore.md) | Lista do que tem de existir na raiz |
| [concepts/separacao-etl-vs-pipelines.md](concepts/separacao-etl-vs-pipelines.md) | `etl/` implementa; `pipelines/` orquestra |
| [concepts/config-sql-secrets.md](concepts/config-sql-secrets.md) | YAML + `sql/` + `.config` / Vault |
| [concepts/src-modulos-compartilhados.md](concepts/src-modulos-compartilhados.md) | `logger.py`, `key_oci.py`, contracts, validation |
| [concepts/testes-por-nivel.md](concepts/testes-por-nivel.md) | `unit` / `integrated` / `system` |

### Padrões

| Ficheiro | Tema |
|----------|------|
| [patterns/scaffold-projeto-dados.md](patterns/scaffold-projeto-dados.md) | Bootstrap, entrypoints, melhorias opcionais |
| [patterns/spark-submit-yarn-config.md](patterns/spark-submit-yarn-config.md) | `config/spark.conf` + spark-submit on YARN |

### Specs

| Ficheiro | Tema |
|----------|------|
| [specs/project-layout-mandatory.yaml](specs/project-layout-mandatory.yaml) | Árvore máquina-legível |

---

## Referência rápida

- [quick-reference.md](quick-reference.md)

---

## Relação com **dev-python-engineering**

Para **como** escrever código de pipelines (performance, testes, observabilidade, tipos), usar em conjunto [dev-python-engineering](../dev-python-engineering/index.md). Esta KB define **onde** fica cada responsabilidade.

---

## Contraste com **design-automation-project-patterns**

| Tipo de repo | KB de layout |
|--------------|----------------|
| **Automação** operacional (bootstrap único, `src/app/main.py`) | [design-automation-project-patterns](../design-automation-project-patterns/index.md) |
| **Dados** (ETL, várias fontes, SQL versionado) | **Esta KB** |

---

## Agentes relacionados

| Agente | Uso |
|--------|-----|
| [python-developer](../../agents/code-quality/python-developer.md) | Classificar repo como **dados** → esta árvore + **dev-python-engineering** |
| [big-data-orchestrator](../../agents/dev/big-data-orchestrator.md) | spark-submit on-prem, PADRAO em [migration-hub/spark/PADRAO-SPARK-SUBMIT-PROJETO-PRD.md](../migration-hub/spark/PADRAO-SPARK-SUBMIT-PROJETO-PRD.md) |
| [airflow-dag-builder](../../agents/data-engineering/airflow-dag-builder.md) | Orquestração Airflow dos jobs em `workspace/prd/` |
| [big-data-cluster-expert](../../agents/data-engineering/big-data-cluster-expert.md) | Ambiente cluster, permissões, paths DATALAKE |

---

## Contexto do repositório exemplo (síntese explorer)

O projeto **cloud_services_availability** segue `pipelines/` (só `pipeline_*.py`), `src/pipeline_runtime/`, `etl/`, `src/utils/` e DAG de exemplo em `dags/`.
