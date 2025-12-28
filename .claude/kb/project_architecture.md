Documento de Arquitetura: Pipeline Uber Eats (End-to-End)
1. Visão Geral
Este documento detalha o fluxo de dados do projeto Uber Eats, desde a geração sintética até a camada Gold no Databricks Lakehouse, utilizando princípios de Engenharia de Dados Moderna (ELT, Medallion Architecture, e Data Governance).

2. Fase de Geração (ShadowTraffic)
Motor: ShadowTraffic rodando em containers Docker.

Fluxo A (Relacional): Dados transacionais (drivers, users) são injetados diretamente no banco PostgreSQL.

Fluxo B (Eventos/NoSQL): Dados de eventos (pedidos, gps, pagamentos) são gerados como arquivos JSON e salvos no MinIO (S3-Compatible).

3. Camada de Ingestão & Landing (Raw Zone)
Ferramenta: Airbyte OSS (Self-hosted).

Estratégia para Postgres:

O Airbyte lê o Postgres (Source) e escreve no Databricks (Destination).

O dado "aterrisa" em uma Landing Zone (External Volume no MinIO) ou diretamente em tabelas Delta no schema raw do Unity Catalog.

Estratégia para MinIO:

Não há movimentação via Airbyte. O Databricks acessa os arquivos diretamente via External Location e External Volume.

O MinIO físico funciona como a Raw Zone lógica para eventos.

4. Camada de Processamento (Databricks Lakehouse)
Governança: Unity Catalog (Namespace de 3 níveis: main.uber_eats.tabela).

Framework de Transformação: Delta Live Tables (DLT).

Leitura de Arquivos: Uso obrigatório de Auto Loader (cloudFiles) para ingestão incremental e eficiente da Raw para a Bronze.

5. Arquitetura Medalhão (Pipeline DLT)
🥉 Camada Bronze (Raw Tables)
Objetivo: Cópia exata (fiel) da fonte (PostgreSQL e arquivos JSON do MinIO).

Formato: Delta Lake.

Processamento: append-only. Nenhuma limpeza é feita aqui.

🥈 Camada Silver (Cleansed & Conformed)
Objetivo: Dados limpos, tipados e enriquecidos.

Ações:

Aplicação de Expectations (DLT) para garantir qualidade (ex: order_id não nulo).

Flattening de JSONs complexos vindos do MinIO.

Joins entre dados de sensores (GPS) e dados cadastrais (Drivers).

🥇 Camada Gold (Curated Business Tables)
Objetivo: Tabelas agregadas prontas para Analytics e BI.

Exemplos: fct_pedidos, dim_motoristas, metricas_entrega_por_regiao.

Consumo: Power BI, SQL Warehouse e AI/BI Genie.

6. Convenções de Desenvolvimento para o Agente
Modularidade: Códigos PySpark devem ser encapsulados em classes ou funções reutilizáveis.

DLT Patterns: Usar decorators @dlt.table e separar a lógica de negócio da lógica de leitura.

Performance: Evitar UDFs (User Defined Functions) desnecessárias; priorizar funções nativas do Spark SQL.

Configuração: Referenciar sempre o databricks.yml para deploy via Asset Bundles.