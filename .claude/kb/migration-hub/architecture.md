# Arquitetura do Ecossistema Big Data

## 📐 Visão Geral da Arquitetura

Este documento descreve a arquitetura completa do ecossistema Big Data provisionado neste ambiente. A arquitetura segue padrões modernos de data lake e processamento distribuído, adequada para análises em larga escala.

## 🎯 Objetivo (o que este documento é)

Este arquivo é o **desenho canônico da stack** que roda (ou vai rodar) neste ambiente:
- Define **papéis** (runtime, armazenamento, compute, orquestração, ingestão, transformação, observabilidade).
- Define **relações** (quem depende de quem e por quais interfaces/portas).
- Separa **Instalado** vs **Planejado/TBD** para evitar decisões implícitas.

**Migração (cluster legado → este ambiente):** ver domínio dedicado [`kb/migration/index.md`](migration/index.md) (resumo, ordem de leitura e links ao [`kb/planning.md`](planning.md)).

**Escopo**:
- **Cluster Big Data (311/312/313/314)**: Hadoop (HDFS+YARN) + Spark on YARN.
- **Nó 314 (worker + orquestração)**: Airflow (`LocalExecutor`) + PostgreSQL (metadata) + **dbt** no venv `bigdata-py311` (runtime típico do utilizador `airflow` para transformações); **DAGs** em **`/DATALAKE/dags`**; **jobs por projeto** em **`/DATALAKE/workspace/prd/<projeto>/`** com **um venv por projeto**. Segredos de integração: **OCI Vault** (consumo via Connections/Variables/pipeline — ver [`kb/naming_conventions.md`](naming_conventions.md)).
- **Edge node (fora do cluster)**: ISMTZAIRBYTE (Airbyte em Docker).

---

## 🏗️ Stack Tecnológico Atual

### Camada de Runtime

#### 1. Java 11 OpenJDK (Base)
```
┌─────────────────────────────────────────────┐
│         Java 11 OpenJDK (LTS)               │
│   ┌─────────────────────────────────────┐   │
│   │  JVM (HotSpot) + G1GC               │   │
│   │  - Heap Memory Management           │   │
│   │  - Just-In-Time Compilation         │   │
│   │  - Garbage Collection               │   │
│   └─────────────────────────────────────┘   │
│                                             │
│   Bibliotecas Core:                        │
│   • java.lang, java.util                  │
│   • java.io, java.nio                     │
│   • java.concurrent                       │
└─────────────────────────────────────────────┘
          ▲
          │ Executa todas as aplicações
          │ do ecossistema Big Data
```

**Status**: ✅ Instalado e Configurado  
**Versão**: 11.0.25 (LTS)  
**JAVA_HOME**: ✅ Configurado (shell) e também em `/etc/profile.d/java11.sh`  
**Função**: Runtime base para todos os componentes do ecossistema  
**Documentação**: 
- [infra/java/01-java-11-openjdk.md](infra/java/01-java-11-openjdk.md) - Instalação e componentes
- [infra/java/CONFIGURACAO-JAVA_HOME.md](infra/java/CONFIGURACAO-JAVA_HOME.md) - Configuração JAVA_HOME

---

## 🎯 Arquitetura Planejada (Em Construção)

### Visão Completa do Ecossistema

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CAMADA DE APRESENTAÇÃO                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │   Jupyter    │  │   Zeppelin   │  │   BI Tools   │            │
│  │   Notebook   │  │   Notebook   │  │   (Tableau)  │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
└─────────────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌─────────────────────────────┴───────────────────────────────────────┐
│                 CAMADA DE PROCESSAMENTO                             │
│  ┌───────────────────────────────────────────────────────────┐     │
│  │              Apache Spark (✅ Instalado: on YARN)          │     │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │     │
│  │  │  Spark SQL   │  │ Spark Stream │  │  Spark MLlib │   │     │
│  │  └──────────────┘  └──────────────┘  └──────────────┘   │     │
│  └───────────────────────────────────────────────────────────┘     │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────┐     │
│  │              dbt (✅ Instalado; Spark adapter 1.9.3)       │     │
│  │              - Transformação ELT via Spark on YARN        │     │
│  └───────────────────────────────────────────────────────────┘     │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────┐     │
│  │              Apache Hive (opcional / não foco atual)       │     │
│  │              - Metastore/SQL só se o time decidir         │     │
│  └───────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌─────────────────────────────┴───────────────────────────────────────┐
│              CAMADA DE GERENCIAMENTO DE RECURSOS                    │
│  ┌───────────────────────────────────────────────────────────┐     │
│  │           YARN (Yet Another Resource Negotiator)          │     │
│  │                    (✅ Instalado)                          │     │
│  │  ┌────────────────┐           ┌────────────────┐         │     │
│  │  │ ResourceManager│           │  NodeManager   │         │     │
│  │  └────────────────┘           └────────────────┘         │     │
│  └───────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌─────────────────────────────┴───────────────────────────────────────┐
│                   CAMADA DE ARMAZENAMENTO                           │
│  ┌───────────────────────────────────────────────────────────┐     │
│  │        Azure Data Lake Storage (ADLS Gen2)                 │     │
│  │                  (✅ Decidido)                              │     │
│  │  - Data Lake (landing/bronze/silver/gold)                  │     │
│  └───────────────────────────────────────────────────────────┘     │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────┐     │
│  │        HDFS (Hadoop Distributed File System)               │     │
│  │                  (✅ Instalado)                             │     │
│  │  - Uso: runtime/serviços (ex.: spark eventlogs)            │     │
│  │  - NÃO usar para dados de negócio                           │     │
│  └───────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌─────────────────────────────┴───────────────────────────────────────┐
│                    CAMADA DE INGESTÃO                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │    Airbyte   │  │    Kafka     │  │    Sqoop     │            │
│  │ (✅ Edge Node)│  │ (Planejado) │  │ (Planejado) │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
└─────────────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌─────────────────────────────┴───────────────────────────────────────┐
│                      CAMADA DE RUNTIME                              │
│  ┌───────────────────────────────────────────────────────────┐     │
│  │              ✅ Java 11 OpenJDK (LTS)                      │     │
│  │              - JVM (HotSpot)                              │     │
│  │              - G1 Garbage Collector                       │     │
│  └───────────────────────────────────────────────────────────┘     │
│  ┌───────────────────────────────────────────────────────────┐     │
│  │              Python (Big Data) 3.11.11 (✅ Instalado)       │     │
│  │              - venv `bigdata-py311` (PySpark/dbt); Airflow │     │
│  │                no 314 com venv dedicado `airflow-py311`     │     │
│  └───────────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌─────────────────────────────┴───────────────────────────────────────┐
│                  SISTEMA OPERACIONAL                                │
│              Red Hat Enterprise Linux 9.7                           │
└─────────────────────────────────────────────────────────────────────┘
```

### Papéis e relações (resumo)
- **ADLS (Azure Data Lake Storage)**: storage de dados de negócio (Data Lake medalhão).
- **HDFS (Hadoop)**: storage distribuído para necessidades do runtime/serviços (ex.: `hdfs:///spark/eventlogs`).
- **YARN (Hadoop)**: agendador/isolamento de recursos (RM no 311, NMs nos 312/313/314).
- **Spark on YARN**: executa jobs distribuídos usando containers do YARN; logs históricos via History Server.
- **dbt (Instalado)**: transformação ELT via **dbt-spark** sobre **Spark on YARN** (Trino permanece possibilidade futura conforme recursos).
- **Apache Airflow (314)**: orquestração (LocalExecutor, PostgreSQL 15 como metadata DB).
- **Airbyte (Edge node)**: ingestão via Docker, fora do cluster Hadoop.

---

## 📊 Componentes Detalhados

### ✅ Componentes Instalados

| Componente | Versão | Status | Camada | Documentação |
|------------|--------|--------|--------|--------------|
| Java 11 OpenJDK | 11.0.25 LTS | ✅ Instalado + JAVA_HOME Configurado | Runtime | [infra/java/01-java-11-openjdk.md](infra/java/01-java-11-openjdk.md) + [infra/java/CONFIGURACAO-JAVA_HOME.md](infra/java/CONFIGURACAO-JAVA_HOME.md) |
| SSH Passwordless | N/A | ✅ Configurado (311 → 312/313/314) | Infraestrutura | [infra/ssh_configuration.md](infra/ssh_configuration.md) |
| Hadoop | 3.3.6 | ✅ Instalado (HDFS + YARN) | Armazenamento/YARN | [hadoop/02-hadoop-3.3.6.md](hadoop/02-hadoop-3.3.6.md) |
| Apache Spark | 3.5.2 | ✅ Instalado (on YARN) | Processamento | [spark/01-spark-3.5.2.md](spark/01-spark-3.5.2.md) |
| Spark History Server | 3.5.2 | ✅ Instalado (311:18080) | Observabilidade | [acess_links.md](acess_links.md) |
| Airbyte (Edge) | 0.30.3 | ✅ Instalado (ISMTZAIRBYTE) | Ingestão | [acess_links.md](acess_links.md) |
| Azure Data Lake Storage (ADLS Gen2) | N/A | ✅ Decisão de arquitetura (storage de dados); URI canônica em [data-stack/datalake/README.md](data-stack/datalake/README.md) (preencher conta/container) | Armazenamento | [data-stack/datalake/README.md](data-stack/datalake/README.md) |
| Python (Big Data / venv) | 3.11.11 | ✅ Instalado (311–314) | Runtime | [infra/python/README.md](infra/python/README.md) |
| dbt (Core + Spark adapter) | 1.9.3 | ✅ Instalado (`bigdata-py311`) | Transformação (ELT) | [data-stack/dbt/README.md](data-stack/dbt/README.md) |
| Apache Airflow | 2.11.1 | ✅ Instalado (314; LocalExecutor; PostgreSQL 15) | Orquestração | [data-stack/airflow/README.md](data-stack/airflow/README.md) |

### 🔄 Componentes Planejados / opcionais

| Componente | Versão Alvo | Status | Camada | Prioridade |
|------------|-------------|--------|--------|------------|
| Apache Hive | 3.1.x | 🔄 Opcional (não no foco atual) | Processamento | Média |
| Apache HBase | 2.5.x | 🔄 Pendente | Armazenamento | Baixa |
| Apache Kafka | 3.6.x | 🔄 Pendente | Ingestão | Média |
| Apache Zookeeper | 3.8.x | 🔄 Pendente | Coordenação | Alta |

---

## 🔄 Fluxo de Dados Típico

### Ingestão → Armazenamento → Processamento → Análise

```
┌──────────────┐
│ Dados Fonte  │
│ (DBs, APIs,  │
│  Logs, IoT)  │
└──────┬───────┘
       │
       ▼
┌──────────────────────────────────┐
│      INGESTÃO                    │
│  Kafka / Flume / Sqoop          │
│  - Streaming real-time          │
│  - Batch ETL                    │
└──────┬───────────────────────────┘
       │
       ▼
┌──────────────────────────────────┐
│      ARMAZENAMENTO               │
│  ADLS Gen2 (Azure)              │
│  - Storage do Data Lake         │
│  - Camadas medalhão             │
└──────┬───────────────────────────┘
       │
       ▼
┌──────────────────────────────────┐
│      PROCESSAMENTO               │
│  Spark / Hive                   │
│  - Transformações               │
│  - Agregações                   │
│  - Machine Learning             │
└──────┬───────────────────────────┘
       │
       ▼
┌──────────────────────────────────┐
│      ANÁLISE / CONSUMO           │
│  Jupyter / Zeppelin / BI        │
│  - Visualizações                │
│  - Relatórios                   │
│  - Dashboards                   │
└──────────────────────────────────┘
```

---

## 🔧 Padrões de Deploy

### Modo Atual: Cluster Multi-node (Hadoop + Spark on YARN)

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Master Node │     │ Worker Node1 │     │ Worker Node2 │
│              │     │              │     │              │
│ NameNode     │     │ DataNode     │     │ DataNode     │
│ ResManager   │     │ NodeManager  │     │ NodeManager  │
│ Spark on YARN│     │ Spark Execs  │     │ Spark Execs  │
└──────────────┘     └──────────────┘     └──────────────┘
        │                   │                     │
        └───────────────────┴─────────────────────┘
                     Network
```

**Nós atuais**:
- **311**: NameNode + ResourceManager + Spark History Server
- **312/313/314**: DataNode + NodeManager (Spark executa via YARN containers)

### Edge Node (fora do cluster Hadoop)
- **ISMTZAIRBYTE**: Airbyte (Docker) — ingestão para o cluster

---

## 🔐 Considerações de Segurança

### Autenticação e Autorização (Futuro)

- **Kerberos**: Autenticação forte para Hadoop
- **Apache Ranger**: Autorização centralizada
- **Apache Knox**: Gateway de segurança
- **SSL/TLS**: Criptografia em trânsito

### Isolamento de Recursos

- **YARN**: Gerenciamento de recursos e quotas
- **CGroups**: Isolamento de CPU/Memória no nível do SO
- **Network Segmentation**: VLANs para segregação

---

## 📈 Escalabilidade

### Dimensionamento Horizontal

```
Capacidade = Nº de Nodes × Recursos por Node

Armazenamento: N × (Discos × Capacidade)
Processamento: N × (CPUs × Memória)
```

### Capacidade Planejada (Exemplo)

| Recurso | Por Node (atual) | Total (4 nodes) |
|---------|-------------------|-----------------|
| CPU | 2 vCPU | 8 vCPU |
| RAM | ~7 GB | ~28 GB |
| Disco (/DATALAKE) | ~99 GB | ~396 GB (raw) |

> Nota: recursos atuais são limitados por decisão de provisionamento inicial; há expectativa de aumento de CPU/RAM conforme evolução do ambiente.

---

## 🔍 Monitoramento (Futuro)

### Stack de Observabilidade

```
┌────────────────────────────────────────┐
│          Camada de Visualização        │
│              Grafana                   │
└────────────┬───────────────────────────┘
             │
┌────────────▼───────────────────────────┐
│       Camada de Métricas               │
│    Prometheus / Ganglia                │
└────────────┬───────────────────────────┘
             │
┌────────────▼───────────────────────────┐
│        Camada de Logs                  │
│    ELK Stack (Elasticsearch,           │
│    Logstash, Kibana)                   │
└────────────┬───────────────────────────┘
             │
┌────────────▼───────────────────────────┐
│    Componentes Hadoop/Spark            │
│    (Java JMX Metrics)                  │
└────────────────────────────────────────┘
```

### Métricas Chave

- **HDFS**: Utilização, throughput, latência
- **YARN**: Containers ativos, memória alocada
- **Spark**: Jobs executando, estágios, shuffle
- **JVM**: Heap usage, GC pauses, thread count

---

## 🎯 Casos de Uso

### 1. Processamento Batch
- ETL de dados históricos
- Agregações complexas
- Machine Learning training

### 2. Streaming Real-time
- Análise de logs em tempo real
- Detecção de fraudes
- IoT data processing

### 3. Data Lake
- Armazenamento centralizado
- Schema-on-read
- Multi-format support (Parquet, ORC, JSON)

### 4. Analytics Interativo
- Queries SQL ad-hoc
- Notebooks interativos
- Exploratory data analysis

---

## 🛣️ Roadmap de Implementação

### Fase 1: Fundação ✅
- [x] Java 11 OpenJDK instalado

### Fase 2: Storage Layer ✅
- [x] Hadoop HDFS + YARN

### Fase 3: Processing Layer
- [x] Apache Spark (on YARN)
- [x] dbt (dbt-spark 1.9.3 on Spark)
- [ ] Apache Hive (opcional)

### Fase 4: Ingestão
- [x] Airbyte (Edge node ISMTZAIRBYTE)
- [ ] Apache Kafka (TBD)
- [ ] Sqoop (TBD)

### Fase 5: Analytics & Viz
- [ ] Jupyter Notebook
- [ ] Zeppelin

### Fase 6: Observability
- [ ] Prometheus + Grafana
- [ ] ELK Stack

---

## 📚 Referências Arquiteturais

- [Hadoop Architecture](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
- [Spark Architecture](https://spark.apache.org/docs/latest/cluster-overview.html)
- [Lambda Architecture](http://lambda-architecture.net/)
- [Kappa Architecture](https://milinda.pathirage.org/kappa-architecture.com/)

---

## 📝 Histórico de Versões

| Versão | Data | Descrição | Componentes Adicionados |
|--------|------|-----------|-------------------------|
| 1.4 | 14/04/2026 | dbt/Airflow refletidos no diagrama; Hive como opcional; SSH ✅ na tabela | Alinhamento KB pós-provisionamento Fases 1–3 |
| 1.3 | 07/01/2026 | Decisão de storage + Python Big Data provisionado | Data Lake em ADLS; Python 3.11.11 + venv; Kafka/Trino no radar |
| 1.2 | 06/01/2026 | Objetivo do documento + stack atualizada | Hadoop/Spark instalados, Airbyte (edge), History Server |
| 1.1 | 30/12/2025 | Configuração do JAVA_HOME | JAVA_HOME configurado em ~/.bashrc |
| 1.0 | 30/12/2025 | Versão inicial com Java 11 | Java 11 OpenJDK |

---

**Documento criado em**: 30/12/2025  
**Última atualização**: 14/04/2026  
**Versão**: 1.4  
**Autor**: Documentação Big Data Project

---

## 📌 Notas

Este documento será atualizado conforme novos componentes forem provisionados no ecossistema. Cada adição será documentada com:
- Diagramas atualizados
- Integração com componentes existentes
- Fluxos de dados
- Configurações de interoperabilidade

