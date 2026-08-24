# 🏗️ Arquitetura — Pipeline SQL

## Visão Geral

Pipeline PySpark para coleta e consolidação de metadados de instâncias SQL Server.

## Fluxo de Dados

```
┌─────────────────────┐
│   Oracle APEX       │  ← Fonte de configuração de servidores
│   (Job 00)          │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   SQL Server        │  ← Tabela de configuração
│   (Config Table)    │     DataBaseSqlServerDatabaseSourceFromApex
└─────────┬───────────┘
          │
          ▼
┌─────────────────────────────────────────────┐
│   Jobs 01-07: Coleta de cada SQL Server     │
│   ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐  │
│   │ SRV1  │ │ SRV2  │ │ SRV3  │ │ ...   │  │
│   └───────┘ └───────┘ └───────┘ └───────┘  │
│                                             │
│   Processamento servidor-a-servidor         │
│   (isolamento de falhas)                    │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────┐
│   SQL Server        │  ← Banco de dados consolidado
│   (DatabaseCapacity)│     Tabelas de destino por job
└─────────────────────┘
```

## Componentes Principais

### 1. Jobs (src/jobs/)

| Job | Responsabilidade |
|-----|------------------|
| 00 | Carrega lista de servidores do Oracle APEX |
| 01 | Informações básicas do SQL Server |
| 02 | Espaço em disco |
| 03 | Memória e CPU |
| 04 | Tamanho, linhas e logs de bancos |
| 05 | Informações do Windows |
| 06 | Informações avançadas de database |
| 07 | Informações avançadas do servidor |

### 2. Utilitários (src/utils/)

| Módulo | Função |
|--------|--------|
| connections_classes.py | Conexões Oracle/SQL Server |
| teams_notifier.py | Notificações Teams |
| teams_guard.py | Controle de notificações duplicadas |
| key_oci.py | Gestão de secrets OCI |
| processamento_de_dados.py | Processamento de DataFrames |

### 3. Gerenciamento (src/management/)

| Módulo | Função |
|--------|--------|
| spark_manager.py | Sessão Spark |
| config.py | Configurações |
| project_path.py | Caminhos do projeto |

### 4. Scripts (scripts/)

```
scripts/
├── HMG/           # Homologação
├── DSV/           # Desenvolvimento
├── ANL/           # Análise
├── QRY/           # Qualidade
├── SLA/           # SLA
└── TST/           # Teste
```

## Cluster Spark

Substitua pelos endpoints do **seu** ambiente (documente em `CONTEXT.md`):

| Componente | Endereço (exemplo) |
|------------|---------------------|
| Master | `spark://<HOST_MASTER>:7077` |
| UI | `http://<HOST_MASTER>:8080/` |
| History | `http://<HOST_MASTER>:18080/` |

## Banco de Dados

### Destino (DatabaseCapacity)

| Tabela | Job |
|--------|-----|
| DataBaseSqlServerDatabaseSourceFromApex | 00 |
| DatabaseSQLServerInfo | 01 |
| DatabaseServerDiskSpaceInfo | 02 |
| DatabaseServerCpuMemoryInfo | 03 |
| DataBaseSQLServerSizeRowsLogs | 04 |
| DatabaseWindowsInfo | 05 |
| DataBaseSqlServerAdvancedInfo | 06 |
| DataBaseSqlServerDatabaseAdvancedInfo | 07 |

### Fonte (Oracle APEX)

Tabela de configuração de servidores que alimenta os jobs.

## Padrão de Processamento

### Jobs 01-07 (Coleta de Metadados)

#### Abordagem 1: Execução por Esteira (sem `--instancia`)
1. **Verificar Tabela de Destino**: Consulta a tabela de destino do job (ex: `DatabaseSQLServerInfo`)
2. **DELETE Condicional**: Se existirem dados da esteira no mês corrente (via `CollectionTime`) → DELETE de todas as linhas
3. **Consultar Tabela do Job 00**: Busca todos os servidores da esteira em `DataBaseSqlServerDatabaseSourceFromApex`
4. **Loop Servidor por Servidor**: Para cada servidor da esteira:
   - Conecta no SQL Server de origem
   - Executa query específica do job
   - Adiciona metadados (`CollectionTime`, `Esteira`, etc.)
   - Salva na tabela de destino
5. **Notificações**: Teams notificado em caso de erros

> **Resultado**: Snapshot mensal completo e consistente da esteira

#### Abordagem 2: Execução por Esteira + Servidor (com `--esteira` e `--instancia`)
1. **Verificar Tabela de Destino**: Busca dados do mês corrente filtrando por servidor+esteira
2. **DELETE Pontual**: Se existir → DELETE apenas do servidor+esteira no mês
3. **Validar Servidor Ativo**: Verifica na tabela do Job 00 se servidor+esteira está ATIVO
4. **Executar Job**: Se ativo → executa query no servidor de origem
5. **Salvar**: INSERT dos dados coletados

> **Uso**: Reprocessar servidor específico que falhou sem afetar os demais

#### Abordagem 3: Execução apenas por Servidor (somente `--instancia`)
- Similar à Abordagem 2, mas sem filtro de esteira
- Processa o servidor independente da esteira

### Job 00 (Snapshot de Servidores)
1. **Verificação**: Consulta tabela destino usando coluna `CollectionTime` para verificar se já existem dados do mês corrente
2. **DELETE Condicional**: Se houver dados do mês corrente → executa DELETE
3. **Consulta APEX**: Lê servidores ativos do Oracle APEX
4. **INSERT Snapshot**: Insere novos dados com `CollectionTime` = timestamp atual
5. **Resultado**: Tabela `DataBaseSqlServerDatabaseSourceFromApex` com **uma foto válida por mês**

> **Coluna Chave**: `CollectionTime` (datetime) - mandatória para identificar o mês do snapshot

## Isolamento de Falhas

- Cada servidor é processado independentemente
- Falha em um servidor não afeta os demais
- Log individual por servidor
- Resumo final com estatísticas de sucesso/falha

