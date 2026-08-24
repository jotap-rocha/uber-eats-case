# Testes de jobs em `workspace/prd` e matriz de projetos

**Última actualização:** 2026-04-30  
**Âmbito:** `/DATALAKE/workspace/prd` no edge **314** (Airflow + execução de pipelines).

Este documento regista o **plano de validação em três fases** e uma **matriz** de pastas de projeto com **runtime principal** (inferido do código versionado, sem `.venv`) e **estado de migração**. O estado inicial é **neutro** até a equipa actualizar após cada fase.

---

## 1. Plano de testes (simulado → controlado)

### Fase A — Manual simulado (sem carga real)

Objetivo: validar **interpretador**, **venv**, **imports**, **argumentos** e **ligação mínima** (ex.: JDBC/API em modo dry-run ou volume de amostra fixo), **sem** escrever dados de negócio finais.

1. No **314** (ou nó com mesmos mounts que o Airflow), entrar no projeto `prd/<projeto>/`.
2. Activar o venv documentado pelo projeto (`source .venv/bin/activate` ou equivalente).
3. Para **Python**: executar o job com flags de “dry-run” / datas de teste / `LIMIT` conforme o projeto permitir; se não existir modo explícito, usar sink temporário ou variável de ambiente acordada pela equipa.
4. Para **Spark**: onde o arranque é via `.sh` com `spark-submit`, usar **master local** ou **YARN com nome de aplicação de teste**, **partições mínimas**, e destinos só em caminhos de teste (`abfss://.../sandbox/...` ou tabelas `_test`), **sem** sobrescrever produção.
5. Registar resultado na matriz (secção 3): manter **Não avaliado** até concluir, depois actualizar para **OK simulado manual** ou **Falha** com nota breve.

### Fase B — Via Airflow simulado (sem carga real)

Objetivo: validar **parse da DAG**, **permits do user `airflow`**, **paths**, **Connections/Variables**, e **task shell/python** com o mesmo critério “sem carga real” da Fase A.

1. DAG correspondente em `/DATALAKE/dags` **pausada**; usar **Trigger DAG** com conf ou **pool de teste** se existir.
2. Onde a DAG só define `BashOperator` com scripts já testados na Fase A, reutilizar os mesmos parâmetros “simulados”.
3. Confirmar logs da task no UI e no filesystem (`AIRFLOW_HOME/logs`).
4. Actualizar matriz: **OK simulado Airflow** ou **Falha** (+ nota).

### Fase C — Via Airflow com cargas controladas

Objetivo: execução **real** restrita a **tabelas/caminhos de teste** acordados (prefixo `_test`, schema sandbox, intervalo de datas curto).

1. Checklist escrito: conjunto de **tabelas/caminhos** permitidos, **janela temporal**, **rollback** ou job de limpeza.
2. DAG despausada apenas para o período do teste; monitorizar YARN (311) e custos/limites ADLS.
3. Após sucesso: marcar na matriz **OK carga controlada** e data; em caso de erro **Falha** com referência ao run id.

**Notas transversais**

- Manter **segredos** fora de Git; usar Connections/Variables ou OCI Vault conforme [`../data-stack/airflow/README.md`](../data-stack/airflow/README.md).
- Qualquer mudança de versão Airflow/Spark/Python relevante para o job deve ser reflectida em [`../inventory.md`](../inventory.md) ou documentos referenciados nas regras do repositório.

---

## 2. Legenda — coluna «Runtime (principal)»

| Valor | Critério (heurística aplicada em 2026-04-30) |
|--------|-----------------------------------------------|
| **Spark (PySpark)** | Presença de `spark-submit` em `.sh` versionados e/ou `SparkSession` / `pyspark` em `.py` do projeto **fora** de `.venv`/`venv`. |
| **Python** | Entrada típica via `python …` em wrappers `.sh` ou jobs só Python, sem indícios Spark no código próprio do projeto. |
| **A definir** | Pasta de projeto sem artefactos `.py`/`.sh` relevantes na árvore versionada (ex.: scripts vazios ou só placeholder). |

Esta coluna descreve o **modo principal** de execução esperado; um projeto «Python» pode na mesma invocar JDBC pesado ou bibliotecas que não são Spark.

---

## 3. Matriz de projetos em `/DATALAKE/workspace/prd`

**Estado de migração (inicial):** todos **Não avaliado**. Substituir por exemplos como `OK — simulado manual`, `OK — Airflow simulado`, `OK — carga controlada`, `Falha — <motivo curto>` quando aplicável.

| Pasta do projeto | Runtime (principal) | Estado migração | Notas |
|-------------------|---------------------|-----------------|-------|
| `apex_data_ingestion` | Python | Não avaliado | Wrappers `.sh` chamam jobs em `src/jobs`. |
| `automacao_rs` | Python | Não avaliado | |
| `b2bicc` | A definir | Não avaliado | `scripts/tst/` vazio no snapshot analisado; DAG pode referenciar paths ainda não populados. |
| `cloud_services_availability` | Python | Não avaliado | |
| `controlm` | Python | Não avaliado | |
| `cyberark-sessoes-auditoria` | Python | Não avaliado | |
| `data-api-problemas-dynatrace-prd` | Spark (PySpark) | Não avaliado | Orquestração típica via `spark-submit` (DAG em `/DATALAKE/dags`). |
| `data-devops` | Python | Não avaliado | |
| `data-diagnostics-cloud` | Python | Não avaliado | |
| `data-erp` | Python | Não avaliado | |
| `data-erp-caixa-entrada` | Python | Não avaliado | |
| `data-gestao_acesso` | Python | Não avaliado | |
| `data-metrics-dynatrace` | Python | Não avaliado | |
| `data-onu-project` | Spark (PySpark) | Não avaliado | `SparkSession` em jobs sob `src/`. |
| `data-oraclecap-dataflow-anl` | Spark (PySpark) | Não avaliado | Scripts `spark-submit` sob `scripts/`. |
| `data-oraclecap-dataflow-prd` | Spark (PySpark) | Não avaliado | Scripts `spark-submit` sob `scripts/`. |
| `data-source-oracle-target-sqlserver-template` | Spark (PySpark) | Não avaliado | Pipelines PySpark em `src/`. |
| `data-sql-capacity-evolution-prd` | Spark (PySpark) | **OK — YARN Job 08** (2026-06-03) | Job 08 on YARN + Airflow; destino `IHMTZBDBI` via **pyodbc** — [`patterns/pyodbc-destino-ihmtzbdbi.md`](patterns/pyodbc-destino-ihmtzbdbi.md). Replicar YARN + pyodbc nos jobs 01–07. |
| `data-trilha-auditoria-dataflow-dsv` | Spark (PySpark) | Não avaliado | `submit_spark_job_*.sh`. |
| `data-trilha-auditoria-gold-dsv` | Spark (PySpark) | Não avaliado | `SparkSession` em `src/jobs`. |
| `exadata_availability` | Python | Não avaliado | |
| `indicadores-previdencia` | Python | Não avaliado | |
| `indicadores-siscorp` | Python | Não avaliado | Vários sub-pastas/scripts; sem PySpark detectado em `src`. |
| `linhas_de_negocio_dynatrace` | Python | Não avaliado | Wrappers chamam `python` em `src/ingestions`. |
| `projeto-sia` | Python | Não avaliado | |
| `relatorio-xp` | Python | Não avaliado | Duplicado nominal de `relatorio_xp`; alinhar qual pasta é canónica. |
| `relatorio_xp` | Python | Não avaliado | Ver nota em `relatorio-xp`. |
| `sentinela` | Python | Não avaliado | |
| `status_premios_erp` | Python | Não avaliado | |
| `zabbix_services_availability` | Python | Não avaliado | |

**Excluído da tabela:** ficheiros na raiz de `prd` (`README.md`, `CHECKLIST-EDGE-314.md`) — não são pastas de projeto.

---

## 4. Manutenção deste documento

- Ao concluir testes por projeto, actualizar **Estado migração** e, se necessário, **Runtime** se a heurística estiver errada.
- Para novos projetos sob `prd/`, acrescentar uma linha à tabela com estado **Não avaliado**.
