# 🆕 Guia para Criação de Novo Pipeline — Pipeline SQL

> **Este documento é o guia definitivo para quando alguém solicitar a criação de um novo pipeline de extração de dados neste domínio (SQL / PySpark do repositório).**

---

## ⚠️ IMPORTANTE - LEIA PRIMEIRO

O processo de criação de um novo pipeline tem **DUAS ETAPAS**:

1. **ETAPA 1**: Pedir ao usuário para descrever com detalhes o que ele tem em mente
2. **ETAPA 2**: Fazer as perguntas específicas e garantir que TODAS sejam respondidas

---

## 🎯 ETAPA 1: COLETA DA VISÃO INICIAL

**ANTES de fazer qualquer pergunta**, envie esta mensagem ao usuário:

```markdown
## 🎯 Criação de Novo Pipeline — Pipeline SQL

Antes de começarmos, preciso entender bem o que você tem em mente!

**Por favor, descreva com a maior riqueza de detalhes possível:**

1. **Qual é o objetivo deste novo pipeline?** 
   - O que você quer coletar/monitorar?
   - Por que essa informação é importante?

2. **De onde vêm os dados?**
   - Quais tabelas/views do SQL Server serão consultadas?
   - São DMVs do sistema ou objetos customizados?

3. **O que será feito com os dados coletados?**
   - Para que serão usados?
   - Quem vai consumir esses dados?

4. **Você já tem a query SQL pronta?**
   - Se sim, compartilhe ela
   - Se não, descreva as informações que precisa extrair

5. **Existe alguma particularidade ou requisito especial?**
   - Frequência de execução?
   - Volume esperado de dados?
   - Alguma restrição ou cuidado especial?

---

📝 **Quanto mais detalhes você fornecer agora, mais assertivo será o pipeline que vou criar!**

Após sua descrição, farei perguntas específicas para garantir que tenho todas as informações necessárias.
```

---

## ⏳ AGUARDAR RESPOSTA DO USUÁRIO

Após o usuário responder com a descrição detalhada, analise a resposta e então prossiga para a **ETAPA 2**.

---

## 📋 ETAPA 2: CHECKLIST DE PERGUNTAS OBRIGATÓRIAS

Após receber a descrição inicial do usuário, envie o checklist abaixo.

**IMPORTANTE**: Baseie-se na descrição que o usuário já forneceu para pré-preencher o que for possível, mas garanta que TODAS as perguntas sejam respondidas.

```markdown
## ✅ Obrigado pela descrição! Agora preciso confirmar alguns detalhes específicos.

Com base no que você descreveu, vou fazer algumas perguntas para garantir que o pipeline seja criado corretamente.

**⚠️ IMPORTANTE: Responda TODAS as perguntas abaixo. Informações faltantes podem comprometer o sucesso da criação do pipeline.**
```

Copie e envie estas perguntas:

```markdown
## 🎯 Para criar seu novo pipeline, preciso que você responda as seguintes perguntas:

### 1️⃣ INFORMAÇÕES BÁSICAS DO JOB

| # | Pergunta | Sua Resposta |
|---|----------|--------------|
| 1 | **Qual será o número do Job?** (ex: 08, 09, 10...) | |
| 2 | **Qual o nome curto do Job?** (sem espaços, ex: `database_index_info`) | |
| 3 | **Qual a descrição do que a query coleta?** (ex: "Informações de índices") | |

### 2️⃣ QUERY SQL

| # | Pergunta | Sua Resposta |
|---|----------|--------------|
| 4 | **Qual a query SQL completa que será executada?** | |
| 5 | **A query usa objetos customizados (views, functions)?** Se sim, forneça o script de criação | |

### 3️⃣ TABELA DE DESTINO

| # | Pergunta | Sua Resposta |
|---|----------|--------------|
| 6 | **Qual o nome da tabela de destino no banco DatabaseCapacity?** | |
| 7 | **A tabela já existe ou precisa ser criada?** | |
| 8 | **Se a tabela existe, forneça a estrutura (DDL) ou as colunas** | |

> ⚠️ **ATENÇÃO - COLUNAS DE METADADOS OBRIGATÓRIAS:**
> Se você criou a tabela manualmente, ela **DEVE conter** as seguintes colunas além das colunas específicas do job:
> ```sql
> CollectionTime        DATETIME,      -- Timestamp da coleta (obrigatória)
> DATA_CARGA_UTC        DATETIME,      -- Adicionada automaticamente pelo pipeline
> DATA_CARGA_FORMATADA  DATETIME,      -- Adicionada automaticamente pelo pipeline
> DESCRICAO_QUERY       VARCHAR(128)   -- Adicionada automaticamente pelo pipeline
> ```
> 
> **Estas colunas são adicionadas pelo `DataProcessor.add_metadata_columns()` e a inserção FALHARÁ se não existirem na tabela!**

### 4️⃣ CONFIGURAÇÕES (OPCIONAIS - têm defaults)

| # | Pergunta | Default | Sua Resposta |
|---|----------|---------|--------------|
| 9 | **Memória do Driver Spark** | 2g | |
| 10 | **Memória do Executor Spark** | 2g | |
| 11 | **Esteiras específicas ou todas?** | Todas | |

---

⚠️ **ATENÇÃO**: Responda TODAS as perguntas obrigatórias (1-8) para que eu possa criar o pipeline com sucesso!
```

---

## 🔍 ETAPA 3: VALIDAÇÃO DAS RESPOSTAS

Após receber as respostas, valide RIGOROSAMENTE:

### ❌ Respostas Incompletas - Enviar Aviso OBRIGATÓRIO:

**NÃO PROSSIGA** com a criação do pipeline se alguma pergunta obrigatória não foi respondida!

```markdown
## ⚠️ ATENÇÃO - Informações Faltantes!

Percebi que algumas perguntas **obrigatórias** não foram respondidas:

- [ ] Pergunta X não foi respondida
- [ ] Pergunta Y está incompleta
- [ ] Pergunta Z precisa de mais detalhes

---

### ❗ Por que isso é importante?

Sem **TODAS** as informações, o pipeline pode:
- Ter erros de execução
- Não salvar os dados corretamente
- Precisar de retrabalho depois

---

### 📝 Por favor, responda as perguntas faltantes:

[Liste aqui as perguntas que faltam ser respondidas]

---

**Assim que você responder TODAS as perguntas, prossigo com a criação do pipeline!** 🚀
```

### ✅ Todas as Respostas Recebidas - Prosseguir:

```markdown
## ✅ Perfeito! Tenho todas as informações necessárias!

Vou criar o pipeline com as seguintes especificações:
- **Job**: XX_app_nome_do_job
- **Tabela destino**: [NOME_DA_TABELA]
- **Descrição**: [DESCRIÇÃO]

Aguarde enquanto crio os arquivos...
```

### Query SQL - Validações:

- [ ] A query retorna a coluna `Servidor`? (obrigatório)
- [ ] A query retorna `@@SERVERNAME + '\' + @@SERVICENAME as Instancia`? (recomendado)
- [ ] A query retorna `GETDATE() as CollectionTime`? (obrigatório)
- [ ] A query usa apenas DMVs do sistema ou precisa de objetos customizados?

### Tabela de Destino - Validações:

- [ ] A tabela de destino tem a coluna `CollectionTime` (DATETIME)? (obrigatório)
- [ ] A tabela de destino tem a coluna `DATA_CARGA_UTC` (DATETIME)? (obrigatório)
- [ ] A tabela de destino tem a coluna `DATA_CARGA_FORMATADA` (DATETIME)? (obrigatório)
- [ ] A tabela de destino tem a coluna `DESCRICAO_QUERY` (VARCHAR(128))? (obrigatório)

> ⚠️ **IMPORTANTE**: O `DataProcessor.add_metadata_columns()` adiciona automaticamente essas 4 colunas ao DataFrame. Se a tabela de destino não tiver essas colunas, a inserção **FALHARÁ** com erro de schema!

---

## 📂 ARQUIVOS QUE SERÃO CRIADOS

Após ter todas as respostas, criar os seguintes arquivos:

### 1. Arquivo Python do Job
```
src/jobs/XX_app_nome_do_job.py
```

### 2. Função da Query (adicionar em)
```
src/queries/queries_functions.py
```

### 3. Scripts Shell (um para cada ambiente)
```
scripts/HMG/run_hmg__XX_app_nome_do_job__XX.sh
scripts/PRD/run_prd__XX_app_nome_do_job__XX.sh
scripts/DSV/run_dsv__XX_app_nome_do_job__XX.sh
scripts/ANL/run_anl__XX_app_nome_do_job__XX.sh
scripts/QRY/run_qry__XX_app_nome_do_job__XX.sh
scripts/SLA/run_sla__XX_app_nome_do_job__XX.sh
scripts/TST/run_tst__XX_app_nome_do_job__XX.sh
```

---

## 🏗️ ESTRUTURA PADRÃO DO JOB PYTHON

O Job deve seguir esta estrutura (baseado nos Jobs 01-07):

```python
"""
Pipeline PySpark: Múltiplos SQL Servers → SQL Server Consolidado

Descrição: [DESCRIÇÃO DO JOB]
Tabela destino: [NOME_DA_TABELA]

Autor: [AUTOR]
Data: [DATA]
"""

# =============================================================================
# IMPORTS
# =============================================================================
import os
import argparse
import traceback
import time
from datetime import datetime
from dataclasses import dataclass
from typing import Dict, Any, List, Optional
import logging
from logging import Logger, getLogger

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import lit

from src.management.spark_manager import SparkManager
from src.utils import key_oci
from src.utils.teams_guard import teams_guard_block, reset_notifier, configure_teams_defaults
from src.utils.teams_notifier import notify_plain_to_teams, get_webhook_url
from src.utils.processamento_de_dados import DataProcessor
from src.queries.queries_functions import get_database_XXXX, get_config_sources_query
from src.utils.connections_classes import SQLServerWriter

# =============================================================================
# CONSTANTES
# =============================================================================
AMBIENTE_DEFAULT = "PRD"
DAYS_TO_KEEP_LOGS = 10
DEFAULT_SQL_PORT = "1433"
DEFAULT_JDBC_PORT = 1433
DEFAULT_ESTEIRA_FILTER = ""
DEFAULT_INSTANCIA_FILTER = ""
JOB_NAME_DEFAULT = "XX_app_nome_do_job"
WIKI_URL = "https://dev.azure.com/<sua-organizacao>/..."

# ... resto do código seguindo o padrão dos Jobs 01-07 ...
```

---

## 📝 TEMPLATE DA FUNÇÃO DE QUERY

Adicionar em `src/queries/queries_functions.py`:

```python
def get_database_nome_do_job() -> str:
    """
    Query para coletar [DESCRIÇÃO].
    Tabela destino: [NOME_DA_TABELA]
    
    Colunas retornadas:
    - Servidor: Nome do servidor
    - Instancia: Servidor + Instância
    - [outras colunas...]
    - CollectionTime: Timestamp da coleta
    """
    return """
        SELECT 
            CAST(@@SERVERNAME AS varchar(128)) AS Servidor,
            @@SERVERNAME + '\\' + @@SERVICENAME AS Instancia,
            -- [COLUNAS DA QUERY]
            GETDATE() AS CollectionTime
        FROM [FONTE_DOS_DADOS]
    """
```

---

## 📝 TEMPLATE DO SCRIPT SHELL

```bash
#!/bin/bash
set -eo pipefail

# Detecta diretório raiz
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)/"

# Configuração do ambiente
AMBIENTE="[NOME_DO_AMBIENTE]"  # HOMOLOGAÇÃO, PRODUÇÃO, etc.

# --- Parâmetros do Job ---
PYTHON_FILE="XX_app_nome_do_job.py"
APP_NAME="XX_app_nome_do_job_${AMBIENTE}"
DRIVER_MEMORY="2g"
EXECUTOR_MEMORY="2g"
NUM_EXECUTORS="1"
EXECUTOR_CORES="1"
TOTAL_EXECUTOR_CORES=$((NUM_EXECUTORS * EXECUTOR_CORES))

# --- Caminhos ---
PROJECT_PATH="${PROJECT_ROOT}"
SPARK_HOME="${SPARK_HOME:-/caminho/para/spark}"
SPARK_MASTER="spark://<HOST_MASTER_SPARK>:7077"
SPARK_JARS_DIR="${SPARK_HOME}/jars"

# JARs necessários
JAR_LIST=(
  "${SPARK_JARS_DIR}/ojdbc8.jar"
  "${SPARK_JARS_DIR}/mssql-jdbc-12.6.3.jre8.jar"
  "${SPARK_JARS_DIR}/delta-core_2.12-2.0.1.jar"
  "${SPARK_JARS_DIR}/delta-storage-2.0.0.jar"
  "${SPARK_JARS_DIR}/delta-contribs_2.12-2.0.1.jar"
)

REQUIRED_JARS=$(IFS=','; echo "${JAR_LIST[*]}")
REQUIRED_DRIVER_CLASSPATH=$(IFS=':'; echo "${JAR_LIST[*]}")

# Validações...
# [código de validação igual aos outros scripts]

# Execução
spark-submit \
  --conf spark.pyspark.driver.python="${PYTHON_VENV}" \
  --conf spark.pyspark.python="${PYTHON_VENV}" \
  --conf spark.pyspark.driver.env.PYTHONPATH="${PROJECT_ROOT}" \
  --conf spark.executorEnv.PYTHONPATH="${PROJECT_ROOT}" \
  --master "${SPARK_MASTER}" \
  --name "${APP_NAME}" \
  --driver-memory "${DRIVER_MEMORY}" \
  --executor-memory "${EXECUTOR_MEMORY}" \
  --executor-cores "${EXECUTOR_CORES}" \
  --num-executors "${NUM_EXECUTORS}" \
  --total-executor-cores "${TOTAL_EXECUTOR_CORES}" \
  --jars "${REQUIRED_JARS}" \
  --driver-class-path "${REQUIRED_DRIVER_CLASSPATH}" \
  "${PROJECT_ROOT}src/jobs/${PYTHON_FILE}" \
  --esteira "${AMBIENTE}" \
  --project-root "${PROJECT_ROOT}" \
  "$@"
```

---

## ✅ CHECKLIST PÓS-CRIAÇÃO

Após criar todos os arquivos, validar:

### Arquivos criados:
- [ ] Job Python criado em `src/jobs/`
- [ ] Função da query adicionada em `src/queries/queries_functions.py`
- [ ] Scripts shell criados para todos os ambientes
- [ ] Permissão de execução nos scripts (`chmod +x`)

### Tabela de destino no SQL Server:
- [ ] ⚠️ **Tabela tem a coluna `CollectionTime` (DATETIME)?**
- [ ] ⚠️ **Tabela tem a coluna `DATA_CARGA_UTC` (DATETIME)?**
- [ ] ⚠️ **Tabela tem a coluna `DATA_CARGA_FORMATADA` (DATETIME)?**
- [ ] ⚠️ **Tabela tem a coluna `DESCRICAO_QUERY` (VARCHAR(128))?**

> 💡 **Dica**: Se o usuário criou a tabela manualmente, SEMPRE perguntar:
> *"A tabela de destino contém as colunas de metadados obrigatórias (DATA_CARGA_UTC, DATA_CARGA_FORMATADA, DESCRICAO_QUERY)?"*

### Documentação:
- [ ] `CONTEXT.md` - adicionar na tabela de jobs
- [ ] `.cursor/kb/sql-capacity/02-jobs-reference.md` - adicionar seção do novo job
- [ ] `docs/00-INDEX.md` - se necessário

---

## 🔄 FLUXO RESUMIDO (3 ETAPAS OBRIGATÓRIAS)

```
┌─────────────────────────────────────────────────────────────┐
│  USUÁRIO SOLICITA NOVO PIPELINE                             │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  ETAPA 1: COLETA DA VISÃO INICIAL                           │
│  ─────────────────────────────────                          │
│  "Descreva com a maior riqueza de detalhes possível         │
│   o que você tem em mente para este novo pipeline"          │
│                                                             │
│  → Objetivo, fonte de dados, uso, query, requisitos         │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  ETAPA 2: CHECKLIST DE PERGUNTAS ESPECÍFICAS                │
│  ───────────────────────────────────────────                │
│  Após receber a descrição, enviar as 11 perguntas:          │
│  - Perguntas 1-8: OBRIGATÓRIAS                              │
│  - Perguntas 9-11: Opcionais (têm defaults)                 │
│                                                             │
│  ⚠️ FORÇAR o usuário a responder TODAS as obrigatórias!    │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  ETAPA 3: VALIDAÇÃO DAS RESPOSTAS                           │
│  ────────────────────────────────                           │
│  Verificar:                                                 │
│  - Todas obrigatórias respondidas? ✅/❌                    │
│  - Query SQL válida? ✅/❌                                  │
│  - Tabela de destino definida? ✅/❌                        │
│                                                             │
│  ❌ Se incompleto → AVISAR e NÃO PROSSEGUIR                │
│  ✅ Se completo → Prosseguir para criação                  │
└─────────────────────────┬───────────────────────────────────┘
                          │
              ┌───────────┴───────────┐
              │ Todas respondidas?    │
              └───────────┬───────────┘
                    │           │
            ┌───────┘           └───────┐
            │ NÃO                       │ SIM
            ▼                           ▼
┌───────────────────────┐  ┌─────────────────────────────────┐
│  COBRAR as respostas  │  │  CRIAR ARQUIVOS                 │
│  faltantes!           │  │  - Job Python                   │
│                       │  │  - Função da query              │
│  NÃO criar nada até   │  │  - Scripts shell (7 ambientes)  │
│  ter TUDO respondido  │  │  - Atualizar documentação       │
└───────────────────────┘  └─────────────────────────────────┘
```

### 📌 REGRA DE OURO

```
┌─────────────────────────────────────────────────────────────┐
│  ❌ NUNCA criar pipeline com informações incompletas!       │
│                                                             │
│  ✅ SEMPRE cobrar TODAS as respostas obrigatórias antes    │
│     de iniciar a criação dos arquivos.                      │
│                                                             │
│  💡 Quanto mais detalhes na ETAPA 1, menos dúvidas na       │
│     ETAPA 2 e maior chance de sucesso!                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 📝 TEMPLATE CREATE TABLE (TABELA DE DESTINO)

Ao criar uma nova tabela de destino, use este template como base:

```sql
-- =============================================================================
-- Tabela: [NOME_DA_TABELA]
-- Job XX - [DESCRIÇÃO DO JOB]
-- =============================================================================

CREATE TABLE dbo.[NOME_DA_TABELA]
(
    Id                    BIGINT IDENTITY(1,1) PRIMARY KEY,
    
    -- =====================================================
    -- COLUNAS ESPECÍFICAS DO JOB (personalize conforme necessário)
    -- =====================================================
    Servidor              VARCHAR(32),
    Esteira               VARCHAR(32),
    Instancia             VARCHAR(128),
    -- [ADICIONE OUTRAS COLUNAS ESPECÍFICAS AQUI]
    
    -- =====================================================
    -- COLUNAS DE METADADOS - OBRIGATÓRIAS EM TODAS AS TABELAS!
    -- Essas colunas são adicionadas automaticamente pelo
    -- DataProcessor.add_metadata_columns()
    -- =====================================================
    CollectionTime        DATETIME,          -- Timestamp da coleta
    DATA_CARGA_UTC        DATETIME,          -- UTC timestamp
    DATA_CARGA_FORMATADA  DATETIME,          -- Timestamp formatado
    DESCRICAO_QUERY       VARCHAR(128)       -- Descrição da query executada
);

-- Índice para otimizar DELETE mensal/semanal
CREATE INDEX IX_[NOME_DA_TABELA]_Collection_Esteira
ON dbo.[NOME_DA_TABELA] (CollectionTime, Esteira);
```

### ⚠️ AVISO CRÍTICO

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ❌ SE A TABELA NÃO TIVER AS COLUNAS DE METADADOS, O JOB VAI FALHAR!       │
│                                                                             │
│  O DataProcessor.add_metadata_columns() adiciona AUTOMATICAMENTE:           │
│  • DATA_CARGA_UTC                                                           │
│  • DATA_CARGA_FORMATADA                                                     │
│  • CollectionTime (sobrescreve se já existir na query)                     │
│  • DESCRICAO_QUERY                                                          │
│                                                                             │
│  Essas colunas precisam EXISTIR na tabela de destino!                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📚 REFERÊNCIAS

- Jobs existentes para usar como base: `src/jobs/01_app_obter_info_sql_server.py`
- Scripts shell existentes: `scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh`
- Queries existentes: `src/queries/queries_functions.py`

---

*Documento criado em Janeiro 2026*
*Última atualização: Janeiro 2026*

