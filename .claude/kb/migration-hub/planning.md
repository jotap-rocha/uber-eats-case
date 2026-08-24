### Planejamento do Ecossistema Big Data

Sequência de fases para evoluir o ambiente Big Data (cluster Hadoop/Spark + ferramentas), com decisões registradas, checklist e validações.

### Decisões já tomadas (source of truth)
- **Storage do Data Lake**: **Azure Data Lake Storage (ADLS Gen2)**  
  - Root (TBD): `abfss://<container>@<storage-account>.dfs.core.windows.net/datalake/`
  - **HDFS não será usado para dados de negócio** (apenas runtime/logs; ex.: `hdfs:///spark/eventlogs`).
- **Spark**: **3.5.2** (on YARN)
- **Python Big Data**: **3.11.11** (padronizado em todos os nós + venv)
- **dbt** (alvo): **dbt-core 1.9.3 + dbt-spark 1.9.3**
- **Airflow** (alvo): **2.11.1**
- **PostgreSQL** (alvo para metadata DB do Airflow no 314): **15** (via `dnf module postgresql:15`)

### Fase 1 — Fundação (Infra + Hadoop Core)
- **SSH sem senha (311 → 312/313/314)**: ✅
- **Java 11**: ✅
- **Hadoop 3.3.6 (HDFS + YARN)**: ✅

**Validações**
- **HDFS UI**: `http://islnx311.drmtz.com.br:9870/`
- **YARN RM UI**: `http://islnx311.drmtz.com.br:8088/`
- **NodeManagers ativos**: `yarn node -list`

### Fase 2 — Processamento (Spark + Python + dbt)
- **Spark 3.5.2 (on YARN)**: ✅
- **Spark History Server**: ✅
- **Python 3.11.11 + venv Big Data**: ✅
- **dbt 1.9.3**: ✅ instalado e validado (`dbt debug` + `dbt run` OK no projeto exemplo)

**Validações**
- **Spark on YARN (SparkPi)**: `spark-submit --master yarn ...`
- **History Server UI**: `http://islnx311.drmtz.com.br:18080/`
- **Python padronizado**: `/DATALAKE/opt/python311/bin/python3 -V`

### Fase 3 — Orquestração (Airflow no nó 314)
- **Airflow 2.11.1**: ✅ instalado e rodando no 314 (systemd: `airflow-webserver`/`airflow-scheduler`)
- **PostgreSQL 15 (metadata DB)**: ✅ instalado no 314 e em uso pelo Airflow

**Decisão operacional (recursos atuais limitados)**
- Airflow roda como **serviço do SO** (fora do YARN), mas competirá por CPU/RAM com o **NodeManager** no 314.

**Validação**
- **Airflow Webserver UI**: `http://islnx314.drmtz.com.br:8080/`

### Tuning YARN (NodeManager) — pós-upgrade de hardware (2026-06)

Máquinas **312/313/314**: ~**16 GiB RAM**, **6 vCPUs** (`MemTotal` ≈ 15 952 332 kB).

| Nó | Política | `yarn.nodemanager.resource.memory-mb` | `yarn.nodemanager.resource.cpu-vcores` | Reserva implícita (~) |
|----|----------|---------------------------------------|----------------------------------------|------------------------|
| **312, 313** | **80%** da máquina para YARN | **12462** | **4** | ~3,1 GiB + 2 vCPUs (OS, DataNode, NM) |
| **314** | **Meio-termo** (Airflow + PostgreSQL + YARN) | **8192** | **3** | ~7,4 GiB + 3 vCPUs (Airflow, PG, OS, DataNode, NM) |

Cluster-wide em `yarn-site.xml`: `yarn.scheduler.maximum-allocation-mb=12462`, `yarn.scheduler.maximum-allocation-vcores=4` (permite container grande nos workers 312/313; no 314 o teto efectivo continua a ser 8192 MB / 3 vCores do NM local).

**Capacidade YARN agregada (3 NM):** ~**33 GiB** RAM, **11 vCores**.

**314 — racional SRE:** reserva ~**50% CPU** e ~**52% RAM** para YARN; o restante cobre scheduler (~1,5 GiB observado), webserver (~400 MiB), PostgreSQL metadata (~100–300 MiB) e margem para picos de DAG + page cache do SO. Se Airflow estiver ocioso e a carga Spark crescer, candidato a subir memória YARN no 314: **9216 MB** (monitorizar `MemAvailable` e latência do scheduler antes).

Reinício após alterar: `yarn-daemon.sh stop/start nodemanager` em cada worker (312/313/314).

### Validação em lote (Fases 1–3)

Para repetir as checagens acima de forma idempotente (inclui HDFS/YARN, UIs no 311, Python nos nós, `dbt debug`, Airflow/PostgreSQL no 314):

- **Script**: [`validate_cluster.sh`](/DATALAKE/workspace/jp/platform/scripts/infra/validate_cluster.sh)

Com **Hadoop parado**, espera-se falha nas etapas que dependem de HDFS/YARN; com **cluster no ar**, o objetivo é exit code `0`.

### Operação com o **nó 313** no cluster (estado atual)

O **313** (`islnx313` / `10.26.132.12`) está **no ar** como **DataNode + NodeManager**, com **FQDN e armazenamento do DataNode** alinhados ao host (sem partilhar identidade com outro nó). Capacidade YARN/HDFS considera **três workers** (312, 313, 314).

| Observação | Notas |
|------------|--------|
| **Capacidade YARN** | Três NodeManagers; continuar a subir carga de forma gradual (Airflow+YARN no **314**). |
| **Fonte da verdade** | `.clauderules` + `kb/` + este ficheiro; após mudanças no ambiente, atualizar `STATUS-AMBIENTE`, `inventory` e `acess_links` conforme protocolo. |
| **Acesso humano vs. serviço** | SO só **`hadoop`**. Daemons: **`airflow`**, etc. Identidade por pessoa nas **ferramentas**: `usr_airflow_*` (FAB), `usr_dbt_*` (targets), `usr_spark_*` (nome/tags em jobs) — ver `kb/naming_conventions.md`. |

**Ordem de leitura/execução (alinhada ao `README.md`):** `kb/architecture.md` → `kb/cluster_topology.md` → `kb/inventory.md` → `kb/infra/STATUS-AMBIENTE.md` → Hadoop/Spark/dbt/Airflow nos paths do README → `scripts/infra/validate_cluster.sh` (objetivo **exit 0** com os quatro nós e **3** DNs/NMs).

---

### Plano — “pronto para clonar jobs” (sem execuções produtivas ainda)

Objetivo: confirmar que a **plataforma** está operacional para **copiar** pipelines do cluster antigo e **testar** primeiro **só Python**, depois **Spark**, com **312/313/314** como workers.

#### Fase A — Pré-requisitos (311; utilizador `hadoop` onde aplicável)

1. **Java 11** e `JAVA_HOME` — [`infra/java/01-java-11-openjdk.md`](infra/java/01-java-11-openjdk.md) e [`infra/java/CONFIGURACAO-JAVA_HOME.md`](infra/java/CONFIGURACAO-JAVA_HOME.md).  
2. **`HADOOP_HOME` / `SPARK_HOME`** carregados (`/etc/profile.d/bigdata.sh`).  
3. **Disco** em `/DATALAKE` com espaço para staging de clones e logs.

#### Fase B — Núcleo Hadoop/YARN (três workers)

1. **HDFS:** `hdfs dfs -ls /`, `hdfs dfsadmin -report` (esperado **3** DataNodes live).  
2. **Safe mode:** `hdfs dfsadmin -safemode get` → `OFF` para escrita e History Server.  
3. **YARN:** `yarn node -list` → **3** nós `RUNNING` (312, 313, 314).  
4. **UIs:** NameNode / RM / History — [`acess_links.md`](acess_links.md) (incl. proxy `datadriven-*` se aplicável).  
5. **Arquivo Spark no HDFS:** `hdfs dfs -ls /spark/jars/spark-jars-3.5.2.zip` + `hdfs fsck` sem **MISSING** em paths críticos (evita falha de AM no YARN).

#### Fase C — Spark no YARN (smoke, quando for testar Spark)

1. `spark-submit` **SparkPi** (ex.: [`spark/CHECKLIST-BOAS-PRATICAS.md`](spark/CHECKLIST-BOAS-PRATICAS.md)).  
2. **ADLS:** quando houver credenciais, [`spark/ADLS-GEN2-SPARK.md`](spark/ADLS-GEN2-SPARK.md) + `scripts/data_stack/adls/test_abfss.sh` (jobs que leem/escrevem no lake).

#### Fase D — Python (prioridade na tua migração)

1. **Interpretador:** `/DATALAKE/opt/python311/bin/python3` e venv **`bigdata-py311`** em **311, 312, 313 e 314** — [`infra/python/README.md`](infra/python/README.md).  
2. **Clones:** repositório ou `DAGS_FOLDER` + `requirements.txt` alinhados ao **3.11**; dependências instaladas no venv ou imagem que vocês adotarem para tasks.  
3. **Onde rodar:** jobs **só Python** podem validar primeiro no **311** ou via **Airflow** no **314** (`BashOperator` / `PythonOperator` apontando ao venv), sem YARN até estares confortável.

#### Fase E — Airflow (314)

1. **UI + systemd:** `airflow-webserver` / `airflow-scheduler` ativos.  
2. **Connections/Variables** espelhadas do ambiente antigo (sem segredos no Git) — ver secção migração abaixo.  
3. **DAGs:** copiar com **pause** ou `is_paused_upon_creation`; **não** ativar agendamento produtivo até os testes.

#### Fase F — Validação em lote

1. [`validate_cluster.sh`](/DATALAKE/workspace/jp/platform/scripts/infra/validate_cluster.sh): objetivo **exit 0** nas partes HDFS/YARN/Spark/dbt/Airflow e **SSH/Python nos quatro nós** (inclui **313**).

#### Fase G — Critério “pode começar a clonar”

- Fases **A, B, D (311–314), E** verdes; **C** verde quando fores testar Spark.  
- Decisão explícita: **nenhuma execução agendada produtiva** até concluíres testes Python → Spark → piloto único.

---

### Migração de jobs (cluster antigo → novo)

Checklist para cada job antes de portar:

| Item | Notas |
|------|--------|
| Versão Spark / Scala / Python | Alinhar com 3.5.2 / 2.12 / 3.11.11 |
| Paths de dados | `abfss://` (ADLS) vs `hdfs://` — atualizar para o root documentado |
| JARs extras / `--packages` | Copiar para o cluster ou `spark.yarn.jars` / archive |
| Agendamento | Mapear cron/Airflow antigo → DAG no Airflow 314 |
| Segredos | Service Principal / connection strings fora do Git; usar Airflow Connections ou env no submit |
| Validação | Mesma contagem de linhas / checksum em amostra; comparar schema |

**Job piloto (recomendado):** escolher um pipeline de baixo risco, somente leitura ou com escrita em prefixo de teste no ADLS, executar `spark-submit` manualmente e só então automatizar com DAG.

**Critérios de aceite do piloto:** job conclui no YARN sem `FAILED`; saída no ADLS conferível; logs no History Server; tempo de execução dentro de uma faixa acordada.

### Fase 4 — Observabilidade (mínimo viável)
**Estado:** não iniciada — executar **após** piloto de jobs e estabilização da plataforma (ver também `kb/infra/STATUS-AMBIENTE.md`).

- 🔄 Definir e provisionar stack (escopo enxuto):
  - CPU/RAM por nó
  - Containers YARN ativos
  - Execuções Spark (apps/stages)
  - Falhas de containers
  - Métricas JVM (Spark/YARN)

