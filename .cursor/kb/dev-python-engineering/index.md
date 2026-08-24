# Python para dados — engenharia e performance

> **Propósito:** Boas práticas de desenvolvimento Python aplicadas a pipelines e workloads de dados, com foco em medição, performance e manutenção.
> **MCP Validated:** 2026-05-06

## Navegação rápida

### Conceitos (≤150 linhas cada)

| Ficheiro | Tema |
|----------|------|
| [concepts/profiling-baseline.md](concepts/profiling-baseline.md) | Medir antes de otimizar; baseline e ferramentas |
| [concepts/vectorized-operations.md](concepts/vectorized-operations.md) | NumPy/Pandas/Polars vetorizado vs loops |
| [concepts/typing-contracts.md](concepts/typing-contracts.md) | Type hints, Pandera, pydantic nas fronteiras |
| [concepts/memory-dtypes.md](concepts/memory-dtypes.md) | dtypes, chunks, generators, cópias vs views |
| [concepts/io-columnar.md](concepts/io-columnar.md) | Parquet, particionamento, leitura lazy |
| [concepts/parallelism-gil.md](concepts/parallelism-gil.md) | CPU vs I/O, GIL, processos/Dask/Ray/Spark |
| [concepts/reproducible-environment.md](concepts/reproducible-environment.md) | pyproject, pinning, containers |
| [concepts/testing-pipelines.md](concepts/testing-pipelines.md) | Testes unitários, propriedades, smoke de performance |
| [concepts/pipeline-architecture.md](concepts/pipeline-architecture.md) | Ingestão → transformação → entrega; observabilidade |
| [concepts/clean-code-modules.md](concepts/clean-code-modules.md) | Módulos legíveis; dataclasses; logging (ver agente python-developer) |

### Padrões (≤200 linhas cada)

| Ficheiro | Tema |
|----------|------|
| [patterns/profiling-workflow.md](patterns/profiling-workflow.md) | Rotina: baseline → perfil → hipótese → validação |
| [patterns/schema-boundary.md](patterns/schema-boundary.md) | Validar dados na entrada/saída de cada estágio |
| [patterns/staged-pipeline-observability.md](patterns/staged-pipeline-observability.md) | Estágios pequenos, métricas e idempotência |
| [patterns/parallelism-choice.md](patterns/parallelism-choice.md) | Escolher threads vs processos vs cluster |

### Especificações

| Ficheiro | Tema |
|----------|------|
| [specs/performance-checklist.yaml](specs/performance-checklist.yaml) | Checklist reproduzível para revisão |

---

## Referência rápida

- [quick-reference.md](quick-reference.md) — tabelas e decisões em uma página

---

## Percurso sugerido

| Nível | Onde começar |
|-------|----------------|
| **Base** | `profiling-baseline`, `vectorized-operations`, `io-columnar` |
| **Robustez** | `typing-contracts`, `testing-pipelines`, `schema-boundary` |
| **Produção** | `pipeline-architecture`, `staged-pipeline-observability`, `parallelism-gil` |

---

## Agentes e contexto

| Recurso | Uso |
|---------|-----|
| [python-developer.md](../../agents/code-quality/python-developer.md) | Padrões de código: dataclasses, generators, tipagem, testes |
| [design-pipelines-patterns](../design-pipelines-patterns/index.md) | **Onde** fica cada pasta no repo de dados |
| [big-data-orchestrator.md](../../agents/dev/big-data-orchestrator.md) | spark-submit on-prem + delegação Spark |
| [migration-hub](../migration-hub/index.md) | Stack DATALAKE / cluster quando o job corre em YARN/Spark |

---

## Relação com outras KB

- **Spark/PySpark:** execução distribuída e I/O em cluster — ver `.cursor/kb/spark/`.
- **Pydantic:** validação de config/modelos — ver domínio `pydantic` no `_index.yaml`.
