# KB — Migração (cluster legado → novo)

> **Revisão documental:** 2026-06-03  
> **Fonte normativa detalhada:** [`../planning.md`](../planning.md)

## Objetivo

Documentar e orientar a **migração de pipelines** do cluster antigo para o ambiente atual (**311–314**: Hadoop/YARN, Spark, Airflow no **314**, dados de negócio no **ADLS Gen2**). Este domínio resume estado e links; o **detalhe operacional** permanece no `planning.md` e nos guias referenciados.

## Estado resumido

- **Fases 1–3** (fundação, Spark/Python/dbt, Airflow + Postgres no 314): concluídas conforme [`../planning.md`](../planning.md) e [`../infra/STATUS-AMBIENTE.md`](../infra/STATUS-AMBIENTE.md).
- **Foco atual:** plano **“pronto para clonar jobs”** (Fases **A–G**), **migração de jobs** job a job, **piloto** antes de carga produtiva; **Fase 4** (observabilidade) após estabilização.

## Ordem de leitura recomendada

1. [`../planning.md`](../planning.md) — fases, critério Fase G, checklist de migração por job.
2. [`quick-reference.md`](quick-reference.md) — paths e comandos rápidos.
3. [`concepts/legado-vs-novo.md`](concepts/legado-vs-novo.md) — diferenças conceituais.
4. [`patterns/portacao-de-job.md`](patterns/portacao-de-job.md) — checklist de portação.
5. [`patterns/sql-capacity-yarn-prd-piloto.md`](patterns/sql-capacity-yarn-prd-piloto.md) — **piloto validado** Job 08 (YARN + Airflow).
6. [`patterns/java11-sqlserver-ssl-dual-cause.md`](patterns/java11-sqlserver-ssl-dual-cause.md) — **SSL Java 11** — duas causas SHA1withRSA (certpath + jar).
7. [`patterns/pyodbc-destino-ihmtzbdbi.md`](patterns/pyodbc-destino-ihmtzbdbi.md) — **solução validada** — destino IHMTZBDBI via pyodbc (contorna mssql-jdbc + Java 11).
8. [`patterns/oracle-python-oracledb-vips-firewall.md`](patterns/oracle-python-oracledb-vips-firewall.md) — **Oracle VIPs + firewall** — `DPY-6005`, liberação SCAN + VIPs.
9. Operação no edge **314:** [`../data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md`](../data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md) — espelho: `/DATALAKE/workspace/prd/CHECKLIST-EDGE-314.md`.
10. Estado do ambiente: [`../infra/STATUS-AMBIENTE.md`](../infra/STATUS-AMBIENTE.md).
11. Equipe e logins (fonte de verdade): [`../team.md`](../team.md).
12. Validação em lote: [`validate_cluster.sh`](/DATALAKE/workspace/jp/platform/scripts/infra/validate_cluster.sh) (executar no **311** como `hadoop`, cluster no ar).

## Índice global

Ver também [`../index.md`](../index.md) — documentação única em **`migration-hub/`**.

## Ficheiros neste domínio

| Ficheiro | Uso |
|----------|-----|
| [`quick-reference.md`](quick-reference.md) | Cheat sheet |
| [`concepts/legado-vs-novo.md`](concepts/legado-vs-novo.md) | Conceitos |
| [`patterns/portacao-de-job.md`](patterns/portacao-de-job.md) | Padrão por job |
| [`patterns/sql-capacity-yarn-prd-piloto.md`](patterns/sql-capacity-yarn-prd-piloto.md) | Piloto YARN validado — SQL Capacity Job 08 |
| [`patterns/java11-sqlserver-ssl-dual-cause.md`](patterns/java11-sqlserver-ssl-dual-cause.md) | SSL Java 11 — SHA1withRSA (jdk.certpath + jdk.jar) |
| [`patterns/pyodbc-destino-ihmtzbdbi.md`](patterns/pyodbc-destino-ihmtzbdbi.md) | **Destino IHMTZBDBI** — pyodbc (solução validada Job 08) |
| [`patterns/pyodbc-destino-hibrido-pyspark.md`](patterns/pyodbc-destino-hibrido-pyspark.md) | **Modelo híbrido** — PySpark + pyodbc (distribuído vs driver) |
| [`patterns/oracle-python-oracledb-vips-firewall.md`](patterns/oracle-python-oracledb-vips-firewall.md) | **Oracle VIPs + firewall** — `DPY-6005`, liberação SCAN + VIPs |
| [`prd-jobs-test-and-matrix.md`](prd-jobs-test-and-matrix.md) | Plano de testes (simulado/controlado) e matriz `workspace/prd` |
