# 📋 Referência de Jobs — Pipeline SQL

## Visão Geral dos Jobs

| Job | Nome | Descrição | Tabela Destino |
|-----|------|-----------|----------------|
| 00 | app_servidores_sql_apex | Carrega servidores do APEX | DataBaseSqlServerDatabaseSourceFromApex |
| 01 | app_obter_info_sql_server | Info básica SQL Server | DatabaseSQLServerInfo |
| 02 | app_obter_info_sql_server_disk_space_info | Espaço em disco | DatabaseServerDiskSpaceInfo |
| 03 | app_obter_info_sql_server_memory_and_cpu | Memória e CPU | DatabaseServerCpuMemoryInfo |
| 04 | app_obter_info_sql_server_database_size_rows_logs | Tamanho/linhas/logs | DataBaseSQLServerSizeRowsLogs |
| 05 | app_obter_windows_info | Info Windows | DatabaseWindowsInfo |
| 06 | app_obter_info_sql_server_database_advanced_info | Info avançada DB | DataBaseSqlServerAdvancedInfo |
| 07 | app_obter_info_sql_server_advanced | Info avançada servidor | DataBaseSqlServerDatabaseAdvancedInfo |
| 08 | app_database_tables_size | TOP 100 maiores tabelas | DatabaseSqlServerTablesSize |

---

## Job 00 - Servidores APEX

### Propósito
Consulta os servidores **ativos** de SQL Server cadastrados no Oracle APEX e salva um snapshot mensal na tabela de configuração do banco `DatabaseCapacity`.

### Arquivo
`src/jobs/00_app_servidores_sql_apex.py`

### Tabela Destino
`DataBaseSqlServerDatabaseSourceFromApex`

### Banco de Dados Destino
`DatabaseCapacity` (SQL Server)

### Fonte de Dados
Oracle APEX (tabela de configuração de servidores ativos)

### Coluna Chave: CollectionTime

A coluna `CollectionTime` é **mandatória** na tabela de destino e é a chave para identificar o mês corrente dos dados.

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `CollectionTime` | `datetime` | Timestamp da coleta (define o mês do snapshot) |

> ⚠️ **Importante**: Sem essa coluna, o mecanismo de snapshot mensal não funciona.

### Regra de Negócio: Snapshot Mensal

O Job 00 implementa uma estratégia de **snapshot mensal**:

1. **Objetivo**: Manter **uma foto válida para cada mês** dos servidores ativos
2. **Primeira execução do mês**: 
   - Verifica se existem dados do mês corrente (via `CollectionTime`)
   - Se não houver → vai ao APEX, busca dados e insere
3. **Execuções subsequentes no mesmo mês**:
   - Verifica se existem dados do mês corrente (via `CollectionTime`)
   - Se houver → executa DELETE dos dados do mês
   - Vai ao APEX, busca os dados atualizados
   - Insere o **novo snapshot**

```
┌─────────────────────────────────────────────────────────────┐
│  Mês        │ Execução 1   │ Execução 2   │ Resultado      │
│─────────────┼──────────────┼──────────────┼────────────────│
│  Janeiro    │ INSERT 100   │ DELETE+INSERT│ 1 snapshot/mês │
│  Fevereiro  │ INSERT 105   │ -            │ 1 snapshot/mês │
│  Março      │ INSERT 110   │ DELETE+INSERT│ 1 snapshot/mês │
└─────────────────────────────────────────────────────────────┘
```

> **💡 Benefício**: Histórico mensal consistente, sem duplicações e sempre com a versão mais recente do mês.

### Fluxo de Execução Detalhado

```
┌─────────────────────────────────────────────────────────────┐
│                      JOB 00 - INÍCIO                        │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  1. VERIFICAR dados do mês corrente                         │
│     SELECT * FROM DataBaseSqlServerDatabaseSourceFromApex   │
│     WHERE MONTH(CollectionTime) = MONTH(GETDATE())          │
│       AND YEAR(CollectionTime) = YEAR(GETDATE())            │
└─────────────────────────┬───────────────────────────────────┘
                          │
              ┌───────────┴───────────┐
              │ Existem dados?        │
              └───────────┬───────────┘
                    │           │
            ┌───────┘           └───────┐
            │ SIM                       │ NÃO
            ▼                           │
┌───────────────────────┐               │
│  2. DELETE dados do   │               │
│     mês corrente      │               │
└───────────┬───────────┘               │
            │                           │
            └───────────┬───────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│  3. CONSULTAR Oracle APEX                                   │
│     Buscar servidores ativos                                │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  4. INSERT novo snapshot                                    │
│     Salvar na tabela de destino com CollectionTime = NOW()  │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│  5. Jobs 01-07 consultam esta tabela                        │
│     para saber quais servidores processar                   │
└─────────────────────────────────────────────────────────────┘
```

### Execução
```bash
# Execução padrão
bash scripts/run_00_app_servidores_sql_apex__00.sh
```

### Observações
- ⚠️ **Executado ANTES dos demais jobs** (é pré-requisito para Jobs 01-07)
- Popula a tabela de configuração que os jobs 01-07 consultam para saber quais servidores processar
- Pode ser executado múltiplas vezes no mês sem risco de duplicação
- Mantém histórico mensal para análise evolutiva

---

## 🔄 Padrão de Execução dos Jobs 01-07

Os jobs 01 a 07 seguem um padrão comum de execução, mas com **duas abordagens** diferentes dependendo dos parâmetros passados.

### Abordagem 1: Execução por Esteira (sem `--instancia`)

Quando você executa um job passando **apenas a esteira**, o comportamento é:

**Exemplo**: Executar Job 01 para PRODUÇÃO
```bash
bash scripts/PRD/run_prd__01_app_obter_info_sql_server__01.sh --esteira "PRODUÇÃO"
```

**Fluxo de Execução:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    JOBS 01-07 - EXECUÇÃO POR ESTEIRA                        │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  1. VERIFICAR TABELA DE DESTINO DO JOB                                      │
│     Exemplo Job 01: DatabaseSQLServerInfo                                   │
│     Verifica se existem dados da esteira PRODUÇÃO para o mês corrente       │
│     usando a coluna CollectionTime                                          │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              │ Existem dados do mês corrente │
              │ para esta esteira?            │
              └───────────────┬───────────────┘
                        │           │
                ┌───────┘           └───────┐
                │ SIM                       │ NÃO
                ▼                           │
┌───────────────────────────────┐           │
│  2. DELETE de TODAS as linhas │           │
│     da esteira no mês corrente│           │
│     (baseado em CollectionTime│           │
│      e Esteira)               │           │
└───────────────┬───────────────┘           │
                │                           │
                └───────────────┬───────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  3. CONSULTAR TABELA DE CONFIGURAÇÃO (Job 00)                               │
│     Tabela: DataBaseSqlServerDatabaseSourceFromApex                         │
│     Busca todos os servidores da esteira PRODUÇÃO do mês corrente           │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  4. LOOP SERVIDOR POR SERVIDOR                                              │
│     Para cada servidor da esteira:                                          │
│     ┌─────────────────────────────────────────────────────────────────────┐ │
│     │  a) Conecta no SQL Server de origem                                 │ │
│     │  b) Executa a query específica do job                               │ │
│     │  c) Adiciona metadados (CollectionTime, Esteira, etc.)              │ │
│     │  d) Salva na tabela de destino do job                               │ │
│     └─────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│     SRV1 → SRV2 → SRV3 → ... → SRVn                                        │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  5. RESULTADO FINAL                                                         │
│     Tabela de destino com snapshot mensal completo da esteira               │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Resumo da Abordagem 1:**
| Etapa | Ação |
|-------|------|
| 1 | Verifica dados do mês corrente na tabela de destino do job |
| 2 | Se existir → DELETE de todas as linhas da esteira no mês |
| 3 | Consulta tabela do Job 00 para obter servidores da esteira |
| 4 | Loop servidor por servidor, coletando e salvando dados |
| 5 | Snapshot mensal completo da esteira |

> **💡 Importante**: Essa abordagem garante que a esteira tenha **uma foto completa e consistente por mês**, mesmo se executada múltiplas vezes.

---

### Abordagem 2: Execução por Esteira + Servidor (com `--esteira` e `--instancia`)

Quando você executa um job passando **esteira E servidor específico**, o comportamento é mais granular:

**Exemplo**: Executar Job 01 para servidor específico da PRODUÇÃO
```bash
bash scripts/PRD/run_prd__01_app_obter_info_sql_server__01.sh \
  --esteira "PRODUÇÃO" \
  --instancia "SERVIDOR\\MSSQLSERVER"
```

**Fluxo de Execução:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              JOBS 01-07 - EXECUÇÃO POR ESTEIRA + SERVIDOR                   │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  1. VERIFICAR TABELA DE DESTINO DO JOB                                      │
│     Exemplo Job 01: DatabaseSQLServerInfo                                   │
│     Verifica se existem dados do mês corrente filtrando por:                │
│     - CollectionTime (mês corrente)                                         │
│     - Esteira (PRODUÇÃO)                                                    │
│     - Servidor (SERVIDOR\MSSQLSERVER)                                       │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              │ Existem dados do mês corrente │
              │ para este servidor+esteira?   │
              └───────────────┬───────────────┘
                        │           │
                ┌───────┘           └───────┐
                │ SIM                       │ NÃO
                ▼                           │
┌───────────────────────────────┐           │
│  2. DELETE PONTUAL            │           │
│     Apenas do servidor+esteira│           │
│     no mês corrente           │           │
└───────────────┬───────────────┘           │
                │                           │
                └───────────────┬───────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  3. VERIFICAR SE SERVIDOR ESTÁ ATIVO                                        │
│     Consulta: DataBaseSqlServerDatabaseSourceFromApex (Job 00)              │
│     Filtro: servidor + esteira + status ATIVO                               │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              │ Servidor está ATIVO?          │
              └───────────────┬───────────────┘
                        │           │
                ┌───────┘           └───────┐
                │ SIM                       │ NÃO
                ▼                           ▼
┌───────────────────────────────┐  ┌───────────────────────────────┐
│  4. EXECUTAR JOB              │  │  SKIP - Servidor inativo      │
│     - Conecta no SQL Server   │  │  Log: "Servidor não ativo"    │
│     - Executa query do job    │  │                               │
│     - Lê dados                │  └───────────────────────────────┘
└───────────────┬───────────────┘
                │
                ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  5. SALVAR NA TABELA DE DESTINO                                             │
│     INSERT com CollectionTime = NOW()                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Resumo da Abordagem 2:**
| Etapa | Ação |
|-------|------|
| 1 | Verifica dados do mês corrente para servidor+esteira específicos |
| 2 | Se existir → DELETE **apenas** desse servidor+esteira no mês |
| 3 | Verifica se servidor+esteira está ATIVO na tabela do Job 00 |
| 4 | Se ativo → executa a query do job no servidor de origem |
| 5 | Salva os dados na tabela de destino |

> **💡 Uso típico**: Reprocessar um servidor específico que falhou, sem afetar os demais servidores da esteira.

> **⚠️ Importante**: 
> - O DELETE é **pontual** (só afeta o servidor especificado)
> - Valida se o servidor ainda está **ATIVO** antes de executar
> - Outros servidores da esteira **não são afetados**

---

### Abordagem 3: Execução apenas por Servidor (somente `--instancia`)

Quando você passa **apenas o servidor** (sem esteira), o comportamento é similar à Abordagem 2, mas sem o filtro de esteira:

```bash
bash scripts/PRD/run_prd__01_app_obter_info_sql_server__01.sh \
  --instancia "SERVIDOR\\MSSQLSERVER"
```

> ⚠️ **Nota**: Neste caso, o filtro de esteira não é aplicado, processando o servidor independente da esteira.

---

### Comparação das Abordagens

| Aspecto | Abordagem 1 (só esteira) | Abordagem 2 (esteira + servidor) | Abordagem 3 (só servidor) |
|---------|--------------------------|----------------------------------|---------------------------|
| **Parâmetros** | `--esteira` | `--esteira` + `--instancia` | `--instancia` |
| **Escopo DELETE** | Toda a esteira no mês | Apenas servidor+esteira | Apenas servidor |
| **Servidores processados** | Todos da esteira | Apenas o especificado | Apenas o especificado |
| **Validação de ATIVO** | Implícita (lista do Job 00) | Explícita (verifica antes) | Explícita (verifica antes) |
| **Uso típico** | Carga mensal completa | Reprocessamento pontual | Reprocessamento pontual |
| **Duração** | Longa | Curta | Curta |

---

## Job 01 - Informações SQL Server

### Propósito
Coleta informações básicas de cada instância SQL Server.

### Arquivo
`src/jobs/01_app_obter_info_sql_server.py`

### Tabela Destino
`DatabaseSQLServerInfo`

### Script SQL Necessário
`src/queries/11- create_vw_fn_sql_info.sql`
- Cria: `fn_SQL_Info()`, `vw_sql_info`, certificado, login

### Execução
```bash
# Esteira completa
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh

# Servidor específico
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh \
  --instancia "SERVIDOR\MSSQLSERVER"
```

---

## Job 02 - Espaço em Disco

### Propósito
Coleta informações de espaço em disco dos servidores.

### Arquivo
`src/jobs/02_app_obter_info_sql_server_disk_space_info.py`

### Tabela Destino
`DatabaseServerDiskSpaceInfo`

### Script SQL Necessário
`src/queries/08 - create_vw_fn_disk_space_info.sql`

### Execução
```bash
bash scripts/HMG/run_hmg__02_app_obter_info_sql_server_disk_space_info__02.sh
```

---

## Job 03 - Memória e CPU

### Propósito
Coleta informações de memória e CPU.

### Arquivo
`src/jobs/03_app_obter_info_sql_server_memory_and_cpu.py`

### Tabela Destino
`DatabaseServerCpuMemoryInfo`

### Script SQL Necessário
Nenhum (usa DMVs do sistema)

### Execução
```bash
bash scripts/HMG/run_hmg__03_app_obter_info_sql_server_memory_and_cpu__03.sh
```

---

## Job 04 - Tamanho, Linhas e Logs

### Propósito
Coleta tamanho dos bancos, contagem de linhas e informações de log.

### Arquivo
`src/jobs/04_app_obter_info_sql_server_database_size_rows_logs.py`

### Tabela Destino
`DataBaseSQLServerSizeRowsLogs`

### Script SQL Necessário
`src/queries/10 - create_vw_fn_size_rows_log.sql`

### Execução
```bash
bash scripts/HMG/run_hmg__04_app_obter_info_sql_server_database_size_rows_logs__04.sh
```

---

## Job 05 - Informações Windows

### Propósito
Coleta informações do sistema operacional Windows.

### Arquivo
`src/jobs/05_app_obter_windows_info.py`

### Tabela Destino
`DatabaseWindowsInfo`

### Script SQL Necessário
Nenhum (usa DMVs do sistema)

### Execução
```bash
bash scripts/HMG/run_hmg__05_app_obter_windows_info__05.sh
```

---

## Job 06 - Info Avançada de Database

### Propósito
Coleta informações avançadas dos databases.

### Arquivo
`src/jobs/06_app_obter_info_sql_server_database_advanced_info.py`

### Tabela Destino
`DataBaseSqlServerAdvancedInfo`

### Script SQL Necessário
Nenhum (usa DMVs do sistema)

### Execução
```bash
bash scripts/HMG/run_hmg__06_app_obter_info_sql_server_database_advanced_info__06.sh
```

---

## Job 07 - Info Avançada do Servidor

### Propósito
Coleta informações avançadas do servidor SQL.

### Arquivo
`src/jobs/07_app_obter_info_sql_server_advanced.py`

### Tabela Destino
`DataBaseSqlServerDatabaseAdvancedInfo`

### Script SQL Necessário
Nenhum (usa DMVs do sistema)

### Execução
```bash
bash scripts/HMG/run_hmg__07_app_obter_info_sql_server_advanced__07.sh
```

---

## Parâmetros Comuns

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `--esteira` | Filtrar por esteira | `--esteira "HOMOLOGAÇÃO"` |
| `--instancia` | Filtrar por instância (múltiplo) | `--instancia "SRV\MSSQLSERVER"` |
| `--overwrite-log` | Sobrescrever log em vez de append | `--overwrite-log` |
| `--port` | Porta customizada | `--port 1434` |

---

## Job 08 - TOP 100 Maiores Tabelas

### Propósito
Coleta as 100 maiores tabelas (por RowCount) de um banco de dados SQL Server específico.

### Arquivo
`src/jobs/08_app_database_tables_size.py`

### Tabela Destino
`DatabaseSqlServerTablesSize`

### Script SQL Necessário
Nenhum (usa DMVs do sistema: `sys.tables`, `sys.indexes`, `sys.partitions`, `sys.allocation_units`)

### Parâmetros OBRIGATÓRIOS

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `--instancia` | Nome da instância SQL Server | `"SERVIDOR\MSSQLSERVER"` |
| `--database` | Nome do banco de dados de origem | `"MEU_BANCO_ORIGEM"` |
| `--esteira` | Nome da esteira | `"PRODUÇÃO"` |

### Parâmetros Opcionais

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `--port` | Porta customizada (sobrescreve detecção automática) | `--port 1539` |

### Diferenças em Relação aos Jobs 01-07

| Aspecto | Jobs 01-07 | Job 08 |
|---------|------------|--------|
| **Lógica de DELETE** | Mês corrente (`CollectionTime >= primeiro dia do mês`) | Últimos 7 dias (`CollectionTime >= GETDATE()-7`) |
| **Frequência** | Mensal | Semanal |
| **Parâmetros obrigatórios** | `--esteira` (opcional `--instancia`) | `--instancia`, `--database`, `--esteira` (todos obrigatórios) |
| **Conexão JDBC** | Conecta no `msdb` | Conecta diretamente no banco especificado |
| **Fonte de servidores** | Tabela do Job 00 | Parâmetro direto |

### Fluxo de Execução

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    JOB 08 - database_tables_size                            │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  1. RECEBER PARÂMETROS OBRIGATÓRIOS                                         │
│     --instancia, --database, --esteira                                      │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  2. CONECTAR DIRETAMENTE NO BANCO ESPECIFICADO                              │
│     JDBC URL: jdbc:sqlserver://host:port;databaseName={database}            │
│     (NÃO conecta no msdb como os outros jobs)                               │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  3. EXECUTAR QUERY TOP 100 MAIORES TABELAS                                  │
│     SELECT TOP 100 ... FROM sys.tables ... ORDER BY RowCount DESC           │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  4. VERIFICAR/DELETAR DADOS DOS ÚLTIMOS 7 DIAS                              │
│     DELETE FROM DatabaseSqlServerTablesSize                                 │
│     WHERE Servidor = X AND DatabaseName = Y AND Esteira = Z                 │
│       AND CollectionTime >= GETDATE()-7                                     │
└─────────────────────────────┬───────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  5. INSERIR NOVOS DADOS                                                     │
│     INSERT INTO DatabaseSqlServerTablesSize                                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Execução
```bash
# Exemplo: banco de linha de negócio em PRODUÇÃO (servidor padrão — ajuste ao seu inventário)
bash scripts/PRD/run_prd__08_app_database_tables_size__08.sh \
  --instancia "EXEMPLO-SRV-LINE-01\MSSQLSERVER" \
  --database "LINHA_NEGOCIO_A" \
  --esteira "PRODUÇÃO"

# Com porta customizada
bash scripts/PRD/run_prd__08_app_database_tables_size__08.sh \
  --instancia "EXEMPLO-SRV-CORP-01\INSTANCIA_NOMEADA" \
  --database "MeuBanco" \
  --esteira "PRODUÇÃO" \
  --port 1539
```

### Servidores padrão por banco

Documente o mapeamento **real** em `CONTEXT.md` ou em planilha interna. Exemplo ilustrativo:

| Banco (exemplo) | Servidor PRD (exemplo) | Esteira |
|-------------------|-------------------------|---------|
| `LINHA_NEGOCIO_A` | `EXEMPLO-SRV-LINE-01\MSSQLSERVER` | PRODUÇÃO |
| `ERP_EXEMPLO` | `EXEMPLO-SRV-ERP-01\MSSQLSERVER` | PRODUÇÃO |

### Observações
- ⚠️ **Todos os 3 parâmetros são OBRIGATÓRIOS** (diferente dos jobs 01-07)
- A conexão é feita **diretamente no banco especificado** (não no msdb)
- O DELETE considera os **últimos 7 dias** (não o mês corrente)
- Frequência recomendada: **semanal**

---

## Ordem de Execução

```
Job 00 (uma vez) → Job 01 → Job 02 → Job 03 → Job 04 → Job 05 → Job 06 → Job 07

Job 08 (independente, semanal, por banco específico)
```

## Logs

```
logs/<job_name>/YYYY-MM-DD.txt
```

Exemplo:
```
logs/01_app_obter_info_sql_server_sql_server_capacity_evolution HOMOLOGAÇÃO/2026-01-14.txt
```

