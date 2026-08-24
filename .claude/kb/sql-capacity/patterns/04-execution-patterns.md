# ⚡ Padrões de Execução — Pipeline SQL

## Execução Básica

### Por Esteira Completa

```bash
# Homologação
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh

# Desenvolvimento
bash scripts/DSV/run_dsv__01_app_obter_info_sql_server__01.sh

# Análise
bash scripts/ANL/run_anl__01_app_obter_info_sql_server__01.sh
```

### Servidor Específico

```bash
# ⚠️ IMPORTANTE: sem FQDN corporativo no host (ex.: não use HOST.EXEMPLO.CORP\INST — siga a política do projeto)
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh \
  --instancia "SERVIDOR\MSSQLSERVER"
```

### Múltiplos Servidores

```bash
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh \
  --instancia "SERVIDOR1\MSSQLSERVER" \
  --instancia "SERVIDOR2\MSSQLSERVER" \
  --instancia "SERVIDOR3\MSSQLSERVER"
```

---

## Parâmetros de Execução

| Parâmetro | Descrição | Obrigatório |
|-----------|-----------|-------------|
| `--esteira` | Filtrar por esteira | Sim (via script) |
| `--instancia` | Filtrar por instância | Não |
| `--overwrite-log` | Sobrescrever log | Não |
| `--port` | Porta customizada | Não |

### Exemplos

```bash
# Com sobrescrita de log
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh \
  --instancia "SERVIDOR\MSSQLSERVER" \
  --overwrite-log

# Com porta customizada
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh \
  --instancia "SERVIDOR\MSSQLSERVER" \
  --port 1434
```

---

## Formato do Parâmetro --instancia

### ✅ Correto (SEM domínio)

```bash
--instancia "SERVIDOR\MSSQLSERVER"
--instancia "EXEMPLO-SRV-HMG-01\MSSQLSERVER"
--instancia "EXEMPLO-SRV-HMG-02\MSSQLSERVER"
```

### ❌ Incorreto (COM domínio)

```bash
--instancia "SERVIDOR.EXEMPLO.CORP\MSSQLSERVER"
--instancia "EXEMPLO-SRV-HMG-01.EXEMPLO.CORP\MSSQLSERVER"
```

---

## Execução Sequencial de Todos os Jobs

### Uma Esteira

```bash
cd "$REPO_ROOT"   # raiz do clone deste repositório

# Executar todos os jobs de HMG em sequência
for script in $(ls scripts/HMG/*.sh | sort); do
  echo "Executando: $script"
  bash "$script"
done
```

### Com Pausa Entre Jobs

```bash
cd "$REPO_ROOT"   # raiz do clone deste repositório

for script in $(ls scripts/HMG/*.sh | sort); do
  echo "Executando: $script"
  bash "$script"
  echo "Aguardando 30 segundos..."
  sleep 30
done
```

---

## Reexecução de Jobs com Falha

### Identificar Servidores com Falha

```bash
# Listar servidores que falharam
grep "❌" logs/<job_name>/$(date +%Y-%m-%d).txt | \
  grep -oP "[\w]+\.[\w.]+\\\\MSSQLSERVER" | \
  sort -u
```

### Script de Reexecução

```bash
#!/bin/bash
# reexecutar_falhas.sh

SERVIDORES=(
  "SERVIDOR1\MSSQLSERVER"
  "SERVIDOR2\MSSQLSERVER"
  "SERVIDOR3\MSSQLSERVER"
)

PARAMS=""
for srv in "${SERVIDORES[@]}"; do
  PARAMS="$PARAMS --instancia \"$srv\""
done

bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh $PARAMS
```

---

## Execução via Spark-Submit Direto

### Básico

```bash
cd "$REPO_ROOT"   # raiz do clone deste repositório

spark-submit \
  --jars "${SPARK_HOME}/jars/ojdbc8.jar,${SPARK_HOME}/jars/mssql-jdbc-12.6.3.jre8.jar" \
  --driver-class-path "${SPARK_HOME}/jars/ojdbc8.jar:${SPARK_HOME}/jars/mssql-jdbc-12.6.3.jre8.jar" \
  --conf spark.pyspark.driver.python=.venv/bin/python \
  --conf spark.pyspark.python=.venv/bin/python \
  --master "spark://<HOST_MASTER_SPARK>:7077" \
  --driver-memory 2g \
  --executor-memory 2g \
  --executor-cores 1 \
  --num-executors 1 \
  --total-executor-cores 1 \
  --name "01_app_obter_info_sql_server HOMOLOGAÇÃO" \
  src/jobs/01_app_obter_info_sql_server.py \
  --esteira "HOMOLOGAÇÃO"
```

### Com Instância Específica

```bash
spark-submit \
  [... parâmetros acima ...] \
  src/jobs/01_app_obter_info_sql_server.py \
  --esteira "HOMOLOGAÇÃO" \
  --instancia "SERVIDOR\MSSQLSERVER"
```

---

## Verificação de Execução

### Durante a Execução

```bash
# Acompanhar log em tempo real
tail -f logs/<job_name>/$(date +%Y-%m-%d).txt
```

### Após a Execução

```bash
# Ver resumo
grep "RESUMO" logs/<job_name>/$(date +%Y-%m-%d).txt

# Contar sucessos e falhas
echo "Sucessos: $(grep -c '✅' logs/<job_name>/$(date +%Y-%m-%d).txt)"
echo "Falhas: $(grep -c '❌' logs/<job_name>/$(date +%Y-%m-%d).txt)"

# Listar falhas
grep "❌" logs/<job_name>/$(date +%Y-%m-%d).txt
```

---

## Ambientes e Scripts

### Nomenclatura dos Scripts

```
run_{esteira}__{job_name}__{ordem}.sh
```

Exemplos:
- `run_hmg__01_app_obter_info_sql_server__01.sh`
- `run_dsv__02_app_obter_info_sql_server_disk_space_info__02.sh`
- `run_anl__03_app_obter_info_sql_server_memory_and_cpu__03.sh`

### Mapeamento Esteira → Código

| Esteira | Código | Pasta |
|---------|--------|-------|
| HOMOLOGAÇÃO | HMG | scripts/HMG/ |
| DESENVOLVIMENTO | DSV | scripts/DSV/ |
| ANÁLISE | ANL | scripts/ANL/ |
| QUALIDADE | QRY | scripts/QRY/ |
| SLA | SLA | scripts/SLA/ |
| TESTE | TST | scripts/TST/ |

---

## 🚀 Execução no Ambiente PRD - Servidor Específico

### ⚠️ REGRA OBRIGATÓRIA

**SEMPRE usar o parâmetro `--instancia`** ao executar scripts PRD para um servidor específico:

```bash
bash scripts/PRD/run_prd__XX_app_*.sh --instancia "SERVIDOR\INSTANCIA"
```

### Exemplos Corretos para PRD

```bash
cd "$REPO_ROOT"   # raiz do clone deste repositório

# Instância MSSQLSERVER (default)
bash scripts/PRD/run_prd__01_app_obter_info_sql_server__01.sh --instancia "EXEMPLO-SRV-PRD-01\MSSQLSERVER"

# Instância nomeada
bash scripts/PRD/run_prd__06_app_obter_info_sql_server_database_advanced_info__06.sh --instancia "EXEMPLO-SRV-PRD-02\INSTANCIA_NOMEADA"

# Outra instância nomeada
bash scripts/PRD/run_prd__01_app_obter_info_sql_server__01.sh --instancia "EXEMPLO-SRV-PRD-03\OUTRA_INST"
```

### Executar TODOS os Jobs para um Servidor PRD

```bash
cd "$REPO_ROOT"   # raiz do clone deste repositório

SERVIDOR="EXEMPLO-SRV-PRD-01\MSSQLSERVER"

# JOB 01 - SQL Server Info
bash scripts/PRD/run_prd__01_app_obter_info_sql_server__01.sh --instancia "$SERVIDOR"

# JOB 02 - Disk Space Info
bash scripts/PRD/run_prd__02_app_obter_info_sql_server_disk_space_info__02.sh --instancia "$SERVIDOR"

# JOB 03 - Memory and CPU
bash scripts/PRD/run_prd__03_app_obter_info_sql_server_memory_and_cpu__03.sh --instancia "$SERVIDOR"

# JOB 04 - Database Size Rows Logs
bash scripts/PRD/run_prd__04_app_obter_info_sql_server_database_size_rows_logs__04.sh --instancia "$SERVIDOR"

# JOB 05 - Windows Info
bash scripts/PRD/run_prd__05_app_obter_windows_info__05.sh --instancia "$SERVIDOR"

# JOB 06 - Database Advanced Info
bash scripts/PRD/run_prd__06_app_obter_info_sql_server_database_advanced_info__06.sh --instancia "$SERVIDOR"

# JOB 07 - Server Advanced Info
bash scripts/PRD/run_prd__07_app_obter_info_sql_server_advanced__07.sh --instancia "$SERVIDOR"
```

### ❌ ERROS COMUNS - NÃO FAZER

```bash
# ERRADO: Sem o parâmetro --instancia
bash scripts/PRD/run_prd__01_app_obter_info_sql_server__01.sh "SERVIDOR\MSSQLSERVER"

# ERRADO: Com domínio
bash scripts/PRD/run_prd__01_app_obter_info_sql_server__01.sh --instancia "SERVIDOR.EXEMPLO.CORP\MSSQLSERVER"

# ERRADO: Parâmetro errado
bash scripts/PRD/run_prd__01_app_obter_info_sql_server__01.sh -i "SERVIDOR\MSSQLSERVER"
```

---

## Boas Práticas

1. **Sempre verificar logs** após execução
2. **Usar --instancia sem domínio**
3. **Reexecutar apenas servidores com falha** (não a esteira inteira)
4. **Usar --overwrite-log** em reexecuções para manter log limpo
5. **Verificar resumo final** para garantir que todos os servidores foram processados
6. **SEMPRE usar `--instancia` ao especificar servidor** (não passar como argumento posicional)

