# Status do Ambiente por Máquina

**Data da Atualização**: 11/05/2026

## Resumo bem pequeno do passo
Visão rápida do que está instalado/configurado em cada nó do cluster (311/312/313/314).

**Operações:** `/DATALAKE` é **LV local** por nó — replicar `pyenv` e venv `bigdata-py311` com **`rsync`** (ver [`infra/python/README.md`](python/README.md)). Malha **SSH** **311**/**314** → todos os nós: [`infra/ssh_configuration.md`](ssh_configuration.md).

## Máquinas

### 311 (Master) — `islnx311.drmtz.com.br`
- **Função**: NameNode / ResourceManager
- **Java 11**: ✅ (`/usr/lib/jvm/java-11-openjdk-11.0.25.0.9-7.el9.x86_64`)
- **Hadoop 3.3.6**: ✅ (`HADOOP_HOME=/DATALAKE/opt/hadoop`, runtime `/DATALAKE/var/hadoop`)
- **Python (Big Data) 3.11.11**: ✅ (pyenv `/DATALAKE/opt/pyenv/versions/3.11.11`; symlink `/DATALAKE/opt/python311`; venv `/DATALAKE/opt/venvs/bigdata-py311`)
- **SSH**:
  - **Origem**: ✅ malha **311–314** (`validate_cluster.sh`, `rsync` em `/DATALAKE/opt/...`).
  - **Destino**: ✅ aceita chaves registadas (ex.: **311**, **314**).

### 312 (Worker 1) — `islnx312.drmtz.com.br`
- **Função**: DataNode / NodeManager
- **Java 11**: ✅
- **Hadoop 3.3.6**: ✅
- **Python (Big Data) 3.11.11**: ✅ (pyenv `/DATALAKE/opt/pyenv/versions/3.11.11`; symlink `/DATALAKE/opt/python311`; venv `/DATALAKE/opt/venvs/bigdata-py311`)
- **SSH (Destino)**: ✅ (aceita do **311** e do **314**, com chaves)

### 313 (Worker 2) — `islnx313.drmtz.com.br`
- **Função**: DataNode / NodeManager
- **Java 11**: ✅
- **Hadoop 3.3.6**: ✅
- **Python (Big Data) 3.11.11**: ✅ (pyenv `/DATALAKE/opt/pyenv/versions/3.11.11`; symlink `/DATALAKE/opt/python311`; venv `/DATALAKE/opt/venvs/bigdata-py311`)
- **SSH (Destino)**: ✅ (aceita do **311** e do **314**, com chaves)

### 314 (Worker 3) — `islnx314.drmtz.com.br`
- **Função**: DataNode / NodeManager
- **Java 11**: ✅
- **Hadoop 3.3.6**: ✅
- **Python (Big Data) 3.11.11**: ✅ (pyenv `/DATALAKE/opt/pyenv/versions/3.11.11`; symlink `/DATALAKE/opt/python311`; venv `/DATALAKE/opt/venvs/bigdata-py311`)
- **Airflow**: ✅ (2.11.1, `LocalExecutor`, venv `/DATALAKE/opt/venvs/airflow-py311`)
  - **Webserver**: ✅ `airflow-webserver.service` (porta `8080/tcp`)
  - **Scheduler**: ✅ `airflow-scheduler.service`
- **PostgreSQL**: ✅ (15.x, para metadata DB do Airflow)
- **ODBC / SQL Server (`pyodbc`):** ✅ cluster **311–314** — ver **STATUS-AMBIENTE**, secção *Notas operacionais* (312: `unixODBC` por RPM offline).
- **SSH**:
  - **Origem**: ✅ malha **311–314** com chaves (`rsync`, operações em lote).
  - **Destino**: ✅ aceita chaves registadas (ex.: **311**, **314**).
