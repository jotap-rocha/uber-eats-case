# Nota — migração do path Bronze do MinIO (ação operacional, não código)

> Descoberta durante o `/build` desta feature: o item 27 do manifesto de `DESIGN_INGESTAO_AZURE_FASE1.md` previa editar `pipeline/silver/ingestion_kafka_*.sql` e `ingestion_mysql_menu.sql` trocando o path de leitura do Auto Loader de `s3a://` (MinIO) para `abfss://` (ADLS Gen2). Ao inspecionar esses arquivos, nenhum deles referencia um path físico diretamente — todos leem `STREAM(live.gps)`, `STREAM(live.route)` etc., uma referência interna ao grafo do próprio pipeline Lakeflow. A definição física da fonte Bronze dessas entidades (`live.gps`, `live.ratings`, `live.route`, `live.search`, `live.shift`, `live.menu`) **não está versionada neste repositório** — vive na configuração do pipeline Lakeflow no workspace Databricks (parâmetro/notebook de origem, fora de `pipeline/`).

## Ação necessária (fora do escopo de código desta feature)

Ao migrar o Free Edition para consumir do ADLS Gen2, atualizar manualmente (ou via `databricks.yml`/DAB, se essa configuração vier a ser versionada em uma iteração futura) o path de origem dessas 6 fontes Bronze no workspace, de `s3a://uber-eats/<prefixo>/` para `abfss://bronze@<storage-account>.dfs.core.windows.net/minio/<prefixo>/` — mesmos prefixos já sincronizados pela conexão Airbyte descrita em `docs/azure/airbyte-minio-adls-config.md`.

## Por que isso não bloqueia o Build

Os arquivos Silver (`pipeline/silver/ingestion_kafka_*.sql`, `ingestion_mysql_menu.sql`) continuam válidos sem nenhuma edição — eles não têm conhecimento do path físico, só do nome lógico da tabela Bronze upstream (`live.gps`, etc.). O trabalho de código desta feature (Postgres/Oracle/MongoDB Bronze, Synapse, Event Hub, Kafka Connect) está completo independente deste item; esta nota registra a pendência operacional para não ser esquecida no `/ship` ou na configuração real do workspace.
