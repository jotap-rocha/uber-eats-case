# Edge 314 — Airflow, `workspace/prd` e dbt no YARN

**Nó:** `islnx314.drmtz.com.br`  
**Objetivo:** checklist para operação (configuração) e validação (“pente fino”) após migração de DAGs/jobs do cluster antigo.  
**Referências:** [`acess_links.md`](../../acess_links.md) (URLs **F5** para humanos), [`dbt/README.md`](../dbt/README.md), [`infra/STATUS-AMBIENTE.md`](../../infra/STATUS-AMBIENTE.md).

**Réplica no 314:** o mesmo ficheiro deve existir em **`/DATALAKE/workspace/prd/CHECKLIST-EDGE-314.md`** (sincronizar a partir do repo ou `rsync` a partir do 311).

---

## 1. Onde colocar as DAGs em relação aos jobs (recomendação de arquitetura)

**Problema:** querer manter DAGs **próximas** ao código de jobs/transformações que depois vão para **produção**, sem duplicar lógica nem perder rastreabilidade.

**Decisão actual (314):**

| Caminho | Função |
|---------|--------|
| **`/DATALAKE/dags`** | Ficheiros `.py` das DAGs que o **Airflow** carrega (`AIRFLOW__CORE__DAGS_FOLDER`). Fica sob **`/DATALAKE`**, ao lado lógico de **`/DATALAKE/workspace`** (DSV/PRD), separado da documentação em **`.cursor/kb`**. |
| **`/DATALAKE/workspace/prd/<projeto>/`** | Código de **produção por projeto** — cada projeto com o **seu próprio venv** (ver §2). Jobs e libs partilhadas por repo de projeto. |
| **`/DATALAKE/workspace/jp/platform`** | **Scripts** e projecto **dbt** de referência — **não** é o destino das DAGs de produção. |

**Isto é boa prática?** Sim, desde que: (1) o conteúdo de `/DATALAKE/dags` seja **deployado de forma controlada** (Git/rsync/CI) e não editado “à mão” em produção sem rastreio; (2) cada DAG seja **fina** e importe lógica dos módulos em `prd/<projeto>/`; (3) permissões: o utilizador **`airflow`** lê `/DATALAKE/dags` e precisa de leitura/execução nos venvs/código que as tasks invocam. Alternativa equivalente seria `.../workspace/dags` — o importante é **separar** DAGs de docs de infra e **versionar** o mesmo conjunto DAG + jobs.

**Anti-padrões:** copiar `.py` de job “na mão” para outro directório; DAG com centenas de linhas de regra de negócio sem testes fora do Airflow.

---

## 2. `workspace/prd` — um venv por projeto (não um venv único na raiz)

**Convenção:** em **`/DATALAKE/workspace/prd`**, cada **pasta de projeto** (ex.: `meu_pipeline_pr`, `outro_domínio`) mantém **o seu próprio** ambiente virtual, por exemplo:

```text
/DATALAKE/workspace/prd/<nome_projeto>/venv/bin/python
```

(ou `.venv` — **fixar por projeto** e documentar no README do projeto).

**O que documentar/fixar:**

1. **Por projeto:** `venv` (ou `.venv`) **dentro** de `prd/<nome_projeto>/`, mais `requirements.txt` / `pyproject.toml` nessa árvore.
2. **Nas DAGs / tasks:** invocar explicitamente o interpretador do **projeto** relevante, por exemplo:  
   `/DATALAKE/workspace/prd/<nome_projeto>/venv/bin/python /caminho/script.py`
3. **Utilizador OS:** o scheduler é **`airflow`**. Cada `prd/<projeto>/` deve permitir **leitura e execução** ao `airflow` (grupo partilhado com `hadoop` ou ACL).
4. **Raiz `prd`:** o ficheiro [`/DATALAKE/workspace/prd/README.md`](../../../../../workspace/prd/README.md) descreve esta convenção; **não** há um único `venv` obrigatório na raiz de `prd`.

---

## 3. “Connections” e “Variables” no Airflow (ponto 4 explicado)

São duas formas de **configuração** guardada na **metadata DB** do Airflow (PostgreSQL no 314), **sem** hardcodar segredos no Git.

| Conceito | O que é | Exemplos |
|----------|---------|----------|
| **Connections** | Credenciais e **como ligar** a sistemas externos: URI JDBC, host/porta, login, *password* (armazenada cifrada com Fernet), extras JSON. | Spark/Hive Thrift, Postgres, HTTP API, bucket ADLS (via extra), etc. |
| **Variables** | Pares **chave = valor** para parâmetros de job: nome de base, prefixo de path, *flags*. | `datalake_bucket`, `env=prd`, `spark_master=yarn`. |

**Na DAG:** `Connection.get_connection_from_secrets("spark_default")` ou `Variable.get("minha_chave")` — evita `user=admin password=123` no código.

**Fernet:** já configurado no `/etc/sysconfig/airflow` — necessário para gravar passwords de Connections com segurança.

**Segredos canónicos:** ver §7 — armazenamento em **OCI Vault**; o Airflow continua a ser o sítio onde as tasks **consomem** credenciais em runtime (Connections/Variables), eventualmente sincronizadas a partir do vault.

---

## 4. dbt no 314 a falar com o YARN (Spark on cluster)

**Intenção:** **`dbt`** corre **no 314** (cliente), e o **Spark executa no YARN** (recursos nos workers 312/313/314).

**Checklist técnico:**

1. **Venv:** `dbt-core` + `dbt-spark` no venv adequado (hoje: `bigdata-py311` como `airflow` no 314, alinhado a [`inventory.md`](../../inventory.md)).
2. **`profiles.yml`:** método **`session`** (driver local cria `SparkSession`; submete ao YARN). Ver [`dbt/README.md`](../dbt/README.md).
3. **Env:** carregar [`dbt_spark_env.sh`](/DATALAKE/workspace/jp/platform/scripts/data_stack/dbt/dbt_spark_env.sh) antes do `dbt` — define `HADOOP_CONF_DIR`, `SPARK_HOME`, PySpark, etc.
4. **`HADOOP_CONF_DIR`:** configs do cluster visíveis no 314 (normalmente `/DATALAKE/opt/hadoop/etc/hadoop`), consistentes com o **311**.
5. **`YARN_CONF_DIR`:** recomenda-se definir **igual a** `HADOOP_CONF_DIR` (mesmos XMLs YARN/HDFS em instalações Hadoop típicas) — ver §6.
6. **Validação:** `dbt debug` (com `profiles.yml` no utilizador de execução) e um `dbt run` de modelo simples **no 314** com RM/YARN no ar. **“100% operacional”** = isto mais ligação Spark/YARN validada — ver [`dbt/README.md`](../dbt/README.md) (estado).

---

## 5. Configuração Airflow a validar no 314

- [ ] **`AIRFLOW__CORE__DAGS_FOLDER`** — apontar para **`/DATALAKE/dags`** (recomendado em `/etc/sysconfig/airflow` para ficar explícito; reiniciar serviços após alterar).
- [ ] **`AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=True`** — novas DAGs aparecem pausadas (sem agendamento até despausar); mesmo ficheiro `/etc/sysconfig/airflow`; reiniciar `airflow-webserver` e `airflow-scheduler` após alterar.
- [ ] **Permissões:** user `airflow` lê `/DATALAKE/dags` e tem **leitura/execução** em cada **`/DATALAKE/workspace/prd/<projeto>/`** usado pelas tasks.
- [ ] **`PYTHONPATH`:** ver §5b — em geral **não** é necessário no `sysconfig` se cada task usar o **venv do projeto** com caminhos explícitos; use `PYTHONPATH` só para pacotes instaláveis partilhados, com critério.
- [ ] **Reinício** após mudar env: `airflow-webserver` e `airflow-scheduler`.
- [ ] **Teste:** `airflow dags list` / trigger de DAG de *smoke*.

### 5b. pyenv vs `PYTHONPATH` (Python das tasks)

- **pyenv** (ou o Python “de sistema” em `/DATALAKE/opt/python311`) pode gerir **qual** intérprete 3.11.x usar para **criar** venvs em `prd/<projeto>/venv`. Isso é independente do processo do **daemon** Airflow (que usa o venv `airflow-py311`).
- **Não** é obrigatório definir `PYTHONPATH` global no Airflow se: cada `BashOperator`/`PythonOperator` chama **`.../prd/<projeto>/venv/bin/python`** e o código está instalado no venv (`pip install -e .`) ou referenciado por path dentro do projeto.
- **Quando faz sentido `PYTHONPATH`:** desenvolvimento rápido com módulos não empacotados, ou libs comuns **fora** do venv — preferir empacotar ou `pip install -e` para evitar surpresas entre scheduler e worker.

---

## 6. Integração cluster (cliente no 314)

- [ ] **`HADOOP_CONF_DIR`** — apontar para `/DATALAKE/opt/hadoop/etc/hadoop` (ou caminho real do cluster).
- [ ] **`YARN_CONF_DIR`** — **boa prática:** definir **explicitamente** igual a `HADOOP_CONF_DIR` (em `bigdata.sh`, no shell da task, ou no mesmo sítio onde já exportam Hadoop). Evita ambiguidade em clientes YARN e alinha com scripts como `dbt_spark_env.sh`. Em muitos ambientes o YARN “funciona” só com `HADOOP_CONF_DIR`, mas **fixar os dois** remove variabilidade entre ferramentas (Spark, Hive, dbt).
- [ ] **Teste:** `hdfs dfs -ls /`, `yarn node -list` como utilizador **`hadoop`** (e repetir o que for necessário no contexto da task).
- [ ] **Spark:** `spark-submit --master yarn` de teste no 314.

---

## 7. Segurança e operações

- [ ] **Segredos canónicos:** **Oracle Cloud Infrastructure (OCI) — Vault** para armazenar palavras-passe, chaves API e material sensível de integrações. **Não** versionar segredos em Git. Sincronização com runtime (Airflow Connections, variáveis de ambiente em deploy, etc.) conforme pipeline da equipa.
- [ ] **Airflow:** Connections e Variables na metadata DB para consumo pelas DAGs; valores podem ser alimentados a partir do vault (processo operacional/CI), não copiados manualmente para repositórios.
- [ ] **Legado / transição:** ficheiros sob `/DATALAKE/var/airflow/secrets/` apenas onde ainda não exista integração com OCI — documentado em [`naming_conventions.md`](../../naming_conventions.md).
- [ ] **UI pública:** links **F5** em [`acess_links.md`](../../acess_links.md) (`https://datadriven-airflow.icatuseguros.com.br/`).
- [ ] **Carga:** 314 = NM + Airflow + Postgres — monitorizar RAM/disco em picos de DAG + Spark local (driver).

---

## 8. Comandos úteis de validação (pente fino)

Executar no **314** como `hadoop` ou conforme indicado:

```bash
# Systemd
systemctl is-active airflow-webserver airflow-scheduler

# Airflow (carregar /etc/sysconfig/airflow antes)
sudo bash -c 'set -a; source /etc/sysconfig/airflow; set +a; sudo -u airflow -E bash -lc "source /DATALAKE/opt/venvs/airflow-py311/bin/activate && airflow version"'

# Cluster (cliente)
source /etc/profile.d/bigdata.sh
hdfs dfs -ls /
yarn node -list

# Exemplo: Python de um projeto em prd (ajustar <projeto>)
/DATALAKE/workspace/prd/<projeto>/venv/bin/python -V
```

### Reinício dos serviços (quando voltar a haver sintomas)

Se a **Web UI** ou o **scheduler** parecerem presos (503 intermitente, Gunicorn sem responder, DAGs que deixam de ser agendadas sem erro claro de DAG), **no `islnx314`** um **restart controlado** dos dois serviços **pode ajudar** após confirmar `systemctl is-active` ou logs (`journalctl -u airflow-webserver`, `journalctl -u airflow-scheduler`):

```bash
sudo systemctl restart airflow-scheduler.service airflow-webserver.service
# Aguardar ~10–15 s; o bind em :8080 só fica disponível depois do Gunicorn subir.
systemctl is-active airflow-webserver airflow-scheduler
curl -sS -o /dev/null -w '%{http_code}\n' --connect-timeout 15 http://127.0.0.1:8080/
```

**Limitação:** isto **não** corrige falhas de **rede** (VPN sem rota até `10.26.132.13`, firewall, **F5**/pool). Se **`curl https://datadriven-airflow.icatuseguros.com.br/`** no cliente ligar e **resetar**, ou **`http://10.26.132.13:8080`** der **timeout** a partir da VPN, o foco continua a ser **rede / BIG-IP** — ver [`../../acess_links.md`](../../acess_links.md) e ticket à equipa responsável.

---

## 9. Sincronização deste documento

- **Fonte no repo:** `kb/data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md`  
- **Cópia no edge:** `/DATALAKE/workspace/prd/CHECKLIST-EDGE-314.md`  
- **Cópia na raiz do repo (atalho):** `EDGE-314-OPERACAO-E-VALIDACAO.md`  
- Após editar no **311**, `rsync` para o **314** ou commit + pull no clone do 314.
