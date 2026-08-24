# Status do Ambiente por Máquina

**Data da Atualização**: 11/05/2026

## Resumo bem pequeno do passo
Visão rápida do que está instalado/configurado em cada nó do cluster (311/312/313/314).

## Notas operacionais — `/DATALAKE`, venvs e SSH

- **`/DATALAKE` por nó:** cada máquina monta o seu **volume local** (LV); **não** assumir NFS único. Mudanças em `/DATALAKE/opt/pyenv` ou em `/DATALAKE/opt/venvs/bigdata-py311` só se propagam com **`rsync`** (ou equivalente) entre hosts.
- **Replicação recomendada:** Python/pyenv e pacotes do venv `bigdata-py311` — [`infra/python/README.md`](python/README.md); script no projecto: [`sync_bigdata_venv_from_local.sh`](/DATALAKE/workspace/jp/platform/scripts/infra/python/sync_bigdata_venv_from_local.sh) (executar no **nó de referência**, tipicamente **314**).
- **Malha SSH:** com chaves `hadoop` distribuídas, **311** e **314** podem aceder a **todos** os nós do cluster (311–314); método e validação — [`infra/ssh_configuration.md`](ssh_configuration.md).
- **ODBC / SQL Server (`pyodbc`, ex.: **Sentinela**):** ✅ em **311–314** — **`unixODBC`** (`libodbc.so.2`) + **`msodbcsql17`** (repo Microsoft RHEL 9; driver **ODBC Driver 17 for SQL Server**, alinhado a `prd/sentinela/src/integrations/database/sql_server.py`). Comandos típicos: `sudo dnf install -y unixODBC`; `curl -fsSL https://packages.microsoft.com/config/rhel/9/prod.repo | sudo tee /etc/yum.repos.d/mssql-release.repo`; `sudo ACCEPT_EULA=Y dnf install -y msodbcsql17`. Verificações: `ldconfig -p | grep libodbc`, `odbcinst -q -d`. **312** sem AppStream: instalar **`unixODBC`** com `rpm -ivh` a partir de `unixODBC-2.3.9-4.el9.x86_64.rpm` copiado de um nó subscrito; **`msodbcsql17`** continua via repo Microsoft (HTTPS). O pacote pip **`pyodbc`** fica no venv do projeto.

## Subida de serviços e cluster (atual)

- **HDFS + YARN**: **NameNode**, **SecondaryNameNode** e **ResourceManager** no **311**; **três** **DataNodes** e **três** **NodeManagers** nos workers **312**, **313** e **314** (validar com `hdfs dfsadmin -report` e `yarn node -list`).
- **Capacidade YARN (2026-06, pós-upgrade ~16 GiB / 6 vCPU por worker):** 312/313 **12462 MB + 4 vCores** (~80% máquina); 314 **8192 MB + 3 vCores** (meio-termo Airflow+PostgreSQL+YARN) — total agregado **~33 GiB / 11 vCores**. Detalhe em [`planning.md`](../planning.md) § tuning YARN.
- **313** (`islnx313`): após correção de rede/config (`dfs.datanode.hostname`, `yarn.nodemanager.hostname` para FQDN do 313) e **reset do armazenamento do DataNode** (novo `datanodeUuid`), o nó voltou a registar-se corretamente no NameNode — **não** reutilizar identidade duplicada entre hosts.
- **Safe mode:** quando aplicável, `hdfs dfsadmin -safemode get` deve estar **OFF** para escrita e Spark History ler event logs.
- **Spark History Server** no **311** (`start-history-server.sh`, porta **18080**).
- **`/spark/jars/spark-jars-3.5.2.zip` no HDFS**: manter cópia íntegra para `spark-submit` on YARN; se `fsck` reportar **MISSING** nesse path, recriar o zip a partir de `/DATALAKE/opt/spark/jars` e voltar a enviar ao HDFS.
- **Event logs Spark** (`hdfs:///spark/eventlogs`): corridas novas voltam a aparecer no History Server. **17/04/2026:** removido do HDFS o ficheiro com bloco em falta `application_1767379387793_0006` (histórico dessa corrida irrecuperável); `hdfs fsck /spark/eventlogs` e `hdfs fsck /` passam a **HEALTHY**.

## Validação automatizada (Fases 1–3)

- **Script**: [`validate_cluster.sh`](/DATALAKE/workspace/jp/platform/scripts/infra/validate_cluster.sh) (executar no **311** como `hadoop`, com `HADOOP_HOME`/`SPARK_HOME` carregados).
- **SSH**: o script assume **BatchMode** para os quatro hosts; alinhar chaves conforme [`infra/ssh_configuration.md`](ssh_configuration.md) (**311** ou **314** como origem típica para operações em lote).
- **Objetivo**: **exit code 0** com cluster no ar — inclui **SSH/Python em todos os quatro nós** (311–314), **três** DataNodes live e **três** NodeManagers, UIs no 311 (`9870`/`8088`/`18080`), `dbt debug` onde aplicável, Airflow/PostgreSQL no **314**.
- **Airflow (314) + PostgreSQL**: checagens do script **OK** (Web UI `8080`, `systemd` ativo, `pg_isready`).
- **Utilizadores FAB**: ver [`naming_conventions.md`](../naming_conventions.md); provisionamento idempotente: [`provision_team_users.sh`](/DATALAKE/workspace/jp/platform/scripts/data_stack/airflow/provision_team_users.sh).

## Máquinas

### 311 (Master) — `islnx311.drmtz.com.br`
- **Função**: NameNode / ResourceManager / Spark History Server
- **Java 11**: ✅ (`/usr/lib/jvm/java-11-openjdk-11.0.25.0.9-7.el9.x86_64`)
- **Hadoop 3.3.6**: ✅ (`HADOOP_HOME=/DATALAKE/opt/hadoop`, runtime `/DATALAKE/var/hadoop`)
- **Python (Big Data) 3.11.11**: ✅ (pyenv em `/DATALAKE/opt/pyenv/versions/3.11.11`; symlink `/DATALAKE/opt/python311` → essa versão; venv `/DATALAKE/opt/venvs/bigdata-py311`). Prefixo antigo `/DATALAKE/opt/python-3.11.11` removido (duplicado).
- **SSH**:
  - **Origem**: ✅ malha para **311–314** (chaves em `/home/hadoop/.ssh/`): `start-*.sh`, `validate_cluster.sh`, `rsync` de `/DATALAKE/opt/...`.
  - **Destino**: ✅ aceita ligações com chave registada (ex.: **311**, **314**).

### 312 (Worker 1) — `islnx312.drmtz.com.br`
- **Função**: DataNode / NodeManager
- **Java 11**: ✅
- **Hadoop 3.3.6**: ✅
- **Python (Big Data) 3.11.11**: ✅ (pyenv em `/DATALAKE/opt/pyenv/versions/3.11.11`; symlink `/DATALAKE/opt/python311` → essa versão; venv `/DATALAKE/opt/venvs/bigdata-py311`). Prefixo antigo `/DATALAKE/opt/python-3.11.11` removido (duplicado).
- **SSH (Destino)**: ✅ (aceita do **311** e do **314**, com chaves)

### 313 (Worker 2) — `islnx313.drmtz.com.br`
- **Função**: DataNode / NodeManager
- **Java 11**: ✅
- **Hadoop 3.3.6**: ✅ (`HADOOP_HOME=/DATALAKE/opt/hadoop`, etc.)
- **Python (Big Data) 3.11.11**: ✅ (pyenv em `/DATALAKE/opt/pyenv/versions/3.11.11`; symlink `/DATALAKE/opt/python311` → essa versão; venv `/DATALAKE/opt/venvs/bigdata-py311`). Prefixo antigo `/DATALAKE/opt/python-3.11.11` removido (duplicado).
- **HDFS/YARN**: ✅ DataNode e NodeManager operacionais; configuração com FQDN **islnx313.drmtz.com.br** (não apontar para outro host).
- **SSH (Destino)**: ✅ (aceita do **311** e do **314**, com chaves)

### 314 (Worker 3) — `islnx314.drmtz.com.br`
- **Função**: DataNode / NodeManager
- **Java 11**: ✅
- **Hadoop 3.3.6**: ✅
- **Python (Big Data) 3.11.11**: ✅ (pyenv em `/DATALAKE/opt/pyenv/versions/3.11.11`; symlink `/DATALAKE/opt/python311` → essa versão; venv `/DATALAKE/opt/venvs/bigdata-py311`). Prefixo antigo `/DATALAKE/opt/python-3.11.11` removido (duplicado).
- **Airflow**: ✅ (2.11.1, `LocalExecutor`, venv `/DATALAKE/opt/venvs/airflow-py311`)
  - **DAGs (`dags_folder`):** **`/DATALAKE/dags`** — `AIRFLOW__CORE__DAGS_FOLDER` em `/etc/sysconfig/airflow`; directório criado no host com permissões para `hadoop`/`airflow` (ver [`../data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md`](../data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md)). O `airflow.cfg` em `AIRFLOW_HOME` pode manter outro valor por defeito, mas a variável de ambiente **prevalece**.
  - **Novas DAGs pausadas:** `AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=True` em `/etc/sysconfig/airflow` (política “só visualização / sem runs agendados” até acordo; reinício de webserver+scheduler após alterar).
  - **Webserver**: ✅ `airflow-webserver.service` (porta `8080/tcp`)
  - **Scheduler**: ✅ `airflow-scheduler.service`
  - **Utilizadores (FAB):** processos como **`airflow`** (confirmado em runtime); operação no SO só **`hadoop`**; na Web UI a conta segue `usr_airflow_<login_da_equipe>`, **Admin** — logins canónicos: [`../team.md`](../team.md). Senhas fora de Git, no **314** (ver [`../data-stack/airflow/README.md`](../data-stack/airflow/README.md)). Conta *bootstrap:* `admin`.
- **dbt (1.9.3):** ✅ no venv **`bigdata-py311`** (instalado como **`airflow`** — mesmo venv usado para transformações alinhadas ao Airflow no 314); ver [`../data-stack/dbt/README.md`](../data-stack/dbt/README.md).
- **Projecto `platform` (scripts + dbt):** réplica no mesmo path que no **311**: **`/DATALAKE/workspace/jp/platform`**. Documentação em **`.claude/kb/migration-hub/`**. Pacotes pesados em **`/DATALAKE/downloads`**. Sincronizar com o nó de referência via `rsync` quando mudar; **não** substituir `/DATALAKE/opt` nem `/DATALAKE/var` do 314 por cópia do 311 (ver [`README.md`](/DATALAKE/workspace/jp/platform/README.md)).
- **Código de produção (`prd`):** **`/DATALAKE/workspace/prd`** — **um venv por pasta de projeto** (`prd/<projeto>/venv`), não um venv único na raiz; ver [`/DATALAKE/workspace/prd/README.md`](../../../../workspace/prd/README.md); checklist em [`../data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md`](../data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md) (espelho: `CHECKLIST-EDGE-314.md` em `prd`).
- **PostgreSQL**: ✅ (15.x, para metadata DB do Airflow)
- **ODBC/SQL Server:** ✅ mesmo stack que **311–314** em todos os workers (ver **Notas operacionais**).
- **SSH**:
  - **Origem**: ✅ malha para **311–314** quando as chaves estão distribuídas (`rsync`, agentes Cursor, manutenção paralela ao **311**).
  - **Destino**: ✅ aceita ligações com chave registada (ex.: **311**, **314**).

## Fase 4 — Observabilidade

**Estado:** não iniciada. Após piloto de jobs e estabilização, seguir o bullet “Fase 4” em [`../planning.md`](../planning.md) (CPU/RAM, containers YARN, métricas Spark/YARN).
