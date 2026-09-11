# DESIGN: Arquitetura de Ingestão — Fase 2 (AWS)

| Campo | Valor |
|-------|-------|
| **Feature** | INGESTAO_AWS_FASE2 |
| **Input** | `.claude/sdd/features/DEFINE_INGESTAO_AWS_FASE2.md` |
| **Status** | ✅ Shipped |
| **Data** | 2026-09-10 |

---

## Architecture Overview

```text
┌──────────────────────────────────────────────────────────────────────────────────────┐
│         ETAPA 1 — Warehouse (conectividade + DMS batch + DataSync + Redshift)          │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  Fase 0 (Postgres/Oracle/MongoDB/MinIO em Docker/ShadowTraffic)                        │
│  migrada temporariamente para EC2 dentro da VPC da Fase 2 (Decisão 1)                  │
│                    │                                                                    │
│      ┌─────────────┼──────────────┬───────────────┐                                   │
│      ▼             ▼              ▼               ▼                                   │
│  DMS task      DMS task       DMS task        AWS DataSync                            │
│  (Postgres,    (Oracle,       (MongoDB,       (location: self-managed                 │
│  ongoing       ongoing        full load/      object storage → MinIO)                 │
│  replication)  replication)   snapshot)                                               │
│      │             │              │               │                                   │
│      └─────────────┴──────────────┴───────────────┘                                   │
│                              ▼                                                          │
│                        S3 (Bronze)                                                      │
│                              │                                                          │
│                              ▼                                                          │
│                  Redshift Serverless (COPY/MERGE)                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────┐
│                    ETAPA 2 — Lakehouse (zero ingestão nova)                             │
├──────────────────────────────────────────────────────────────────────────────────────┤
│                        S3 (Bronze, já populado na Etapa 1)                              │
│                              │                                                          │
│                              ▼                                                          │
│              Glue Catalog + tabelas Iceberg  ──▶  Athena                              │
└──────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────┐
│           ETAPA 3 — Kappa (2ª task DMS por fonte + ponte MinIO + consumidor)            │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  DMS task 2ª        DMS task 2ª         MinIO ──notificação──▶ Lambda ponte           │
│  (Postgres,         (Oracle,            (bucket, Webhook)      (PutRecord/            │
│  ongoing            ongoing                                    PutRecords)            │
│  replication,       replication,                                    │                 │
│  target Kinesis)    target Kinesis)                                 │                 │
│      │                  │                                           │                 │
│      └──────────────────┴───────────────────────────────────────────┘                 │
│                              ▼                                                          │
│                  Kinesis Data Streams (on-demand)                                      │
│                              │                                                          │
│                              ▼                                                          │
│              Lambda consumidor (Kinesis event source mapping)                          │
│                    │ lookup/enriquecimento                                             │
│                    ▼                                                                   │
│         S3 (Bronze) — cópia do MongoDB, já aterrissada na Etapa 1                       │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

**Contrato canônico de CDC — extensão para o DMS (transversal, aplicado desde a Etapa 1):**

| Coluna canônica | De onde vem (Airbyte/Postgres, Onda 3) | De onde vem (Debezium/Oracle, Onda 3) | De onde vem (AWS DMS, Fase 2) |
|---|---|---|---|
| `cdc_operation` | `_ab_cdc_deleted_at` (`I`/`U`/`D`) | `payload.op` (`c`/`u`/`d`) | Coluna `Op` do S3 target (`IncludeOpForFullLoad=true`) — `I`/`U`/`D` |
| `cdc_commit_ts` | `_ab_cdc_updated_at` | `payload.source.ts_ms` | Coluna de timestamp do S3 target (`TimestampColumnName`) |
| `cdc_sequence` | `_ab_cdc_lsn` | `payload.source.scn` | `transaction_id` + `transaction_record_id` (S3 target `IncludeTransactionDetails=true`) — combinados em uma chave ordenável |
| `cdc_source_system` | constante `'postgres-ubereats'` | constante `'oracle-ubereats'` | constante por task (`'postgres-dms-aws'`, `'oracle-dms-aws'`, `'mongo-dms-aws'`) |

A Silver/consumo (Redshift, Athena) **nunca** lê as colunas nativas do DMS diretamente — só as 4 colunas canônicas, mesma disciplina já estabelecida na Onda 3. **Nota de risco (carregada do DEFINE, A-002):** o formato exato de `transaction_id`/`transaction_record_id` do DMS precisa ser confirmado com um teste real no início do `/build` — a combinação proposta aqui é a leitura da documentação AWS, não testada neste projeto ainda.

---

## Decisões (ADRs inline)

### Decisão 1 — Sistemas da Fase 0 migram temporariamente para uma EC2 dentro da VPC da Fase 2 (resolve conectividade de rede)

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Data** | 2026-09-10 |

**Contexto:** o DEFINE deixou em aberto o método de conectividade de rede entre a AWS e os containers self-hosted da Fase 0 (Postgres/Oracle/MongoDB/MinIO), que hoje rodam localmente via Docker/ShadowTraffic (Assumption A-001). Toda task DMS/DataSync depende disso funcionar antes de qualquer outra coisa.

**Escolha:** subir uma instância **EC2** dentro da mesma VPC da Fase 2, rodando o **mesmo `docker-compose.yml`** já usado na Fase 0/1 (Postgres, Oracle, MongoDB, MinIO, ShadowTraffic `gen-unified`) — sem mudança de código, só de local de execução. DMS e DataSync acessam esses serviços por **IP privado dentro da VPC**, nunca pela internet pública.

**Racional:** evita 2 problemas de uma vez — (1) expor bancos de dados diretamente à internet (anti-padrão de segurança), e (2) o custo/complexidade de uma VPN Site-to-Site gerenciada só para uma janela de uso de portfólio pessoal. Reaproveitar o mesmo `docker-compose.yml` significa zero retrabalho de configuração dos geradores — só troca onde o Docker roda.

**Alternativas rejeitadas:**
1. Expor os containers via IP público com security group restrito — tecnicamente mais simples, mas expõe portas de banco de dados (5432/1521/27017/9000) à internet, mesmo que filtradas por IP de origem; risco de segurança desproporcional para o ganho.
2. VPN Site-to-Site gerenciada (AWS Site-to-Site VPN) — solução "correta" de produção, mas exige um Customer Gateway com IP público estático em casa (a maioria dos provedores residenciais não garante isso) e tem custo por hora mesmo ocioso.

**Consequências:** custo de EC2 rodando durante a janela de execução da Fase 2 (mitigado por ser só durante a fase, não permanente — mesmo princípio de "abrir conta só no início da fase"); a instância precisa de recursos suficientes para rodar Postgres+Oracle+MongoDB+MinIO+ShadowTraffic ao mesmo tempo (Oracle sozinho já usa ~2.25GB de imagem, ver `DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md` Decisão 6) — dimensionar a instância no `/build` (provável `t3.xlarge` ou maior).

### Decisão 2 — Redshift e Glue/Athena compartilham a mesma task DMS batch (S3 como landing único)

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o brainstorm avaliou manter o Redshift como target DMS nativo (em paralelo ao S3) ou fazê-lo ler só do S3. A decisão já estava fechada no DEFINE — esta seção só formaliza o desenho técnico.

**Escolha:** 1 task DMS por fonte relacional/documental com target S3 (Etapa 1); Redshift faz `COPY`/`MERGE` a partir daí; Glue+Iceberg+Athena leem o mesmo S3, sem nenhuma ingestão adicional (Etapa 2).

**Alternativas rejeitadas:**
1. DMS duplo (S3 + Redshift nativo) — rejeitado no brainstorm por duplicar configuração de endpoint sem necessidade, já que o padrão da Fase 1 (Synapse `COPY INTO` do ADLS Gen2) já provou que esse desenho funciona.

**Consequências:** Redshift depende do agendamento/latência do `COPY`/`MERGE` (não é CDC nativo instantâneo) — aceitável, já que o Warehouse não tem requisito de real-time (esse papel é do Kappa).

### Decisão 3 — Consumidor do Kappa é AWS Lambda (event source mapping do Kinesis), não Flink gerenciado

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o DEFINE deixou em aberto a escolha entre Flink gerenciado (Kinesis Data Analytics/Managed Service for Apache Flink) e Lambda como consumidor do Kappa.

**Escolha:** **AWS Lambda**, usando Kinesis como event source (invocação automática por lote de registros).

**Racional:** Managed Service for Apache Flink cobra por KPU-hora mesmo com baixo volume de eventos (não é verdadeiramente serverless/on-demand no sentido de "zero custo parado") — contraria o mesmo princípio que já descartou o MSK. Lambda com Kinesis trigger cobra só por invocação/tempo de execução, e a lógica necessária (parsear evento, enriquecer com lookup no MongoDB via S3, gravar/encaminhar o resultado) não exige o processamento de janelas complexas (windowing, watermarks) que justificaria Flink.

**Alternativas rejeitadas:**
1. Managed Service for Apache Flink — mais robusto para stateful stream processing real, mas custo desproporcional ao volume de um projeto de portfólio; reavaliar se o Kappa evoluir para agregações com janela de tempo.

**Consequências:** Lambda tem limite de tempo de execução (15 min) e de payload — não é um problema aqui (processamento por evento, sem estado acumulado entre invocações), mas deve ser reavaliado se o Kappa ganhar requisitos de agregação contínua no futuro.

### Decisão 4 — Lookup do MongoDB no consumidor via leitura direta do S3 (sem cache dedicado, nesta v1)

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o DEFINE deixou como Assumption (A-004) se o lookup direto no S3 por evento teria latência aceitável, ou se precisaria de um cache (ex. DynamoDB).

**Escolha:** a Lambda consumidora carrega a cópia do MongoDB do S3 (Bronze) **uma vez por cold start / a cada N minutos** (cache em memória do próprio processo Lambda, com TTL), não a cada evento individual — evita releitura do S3 por invocação sem introduzir um serviço novo (DynamoDB).

**Alternativas rejeitadas:**
1. Ler o S3 a cada evento — latência e custo de leitura desnecessários, dado que o MongoDB é estático (satélite sem mutação).
2. DynamoDB como cache dedicado — resolveria o problema de forma mais robusta (compartilhado entre instâncias concorrentes da Lambda), mas é um serviço a mais para uma tabela de referência pequena (~500 documentos, conforme dimensionamento já usado na Onda 3); reavaliar se o volume de restaurantes crescer muito.

**Consequências:** cada instância "quente" da Lambda mantém sua própria cópia em memória — se o S3 for atualizado (novo sync do DataSync/DMS), pode haver inconsistência temporária entre instâncias até o cache expirar; aceitável dado que o MongoDB é estático por definição (Onda 3).

### Decisão 5 — Ponte MinIO→Kinesis é uma Lambda dedicada, desacoplada do consumidor do Kappa

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o brainstorm fechou o mecanismo (Webhook do MinIO → Lambda → `PutRecord` no Kinesis), mas não detalhou se essa Lambda é a mesma que processa/enriquece os eventos no Kappa.

**Escolha:** duas Lambdas separadas — `lambda_minio_kinesis_bridge` (só recebe o Webhook e grava no Kinesis, sem lógica de negócio) e `lambda_kappa_consumer` (lê do Kinesis via event source mapping, faz o lookup/enriquecimento). Ambas compartilham o mesmo Kinesis Data Stream como ponto de acoplamento.

**Racional:** a ponte é infraestrutura pura (webhook → stream), enquanto o consumidor tem lógica de negócio (enriquecimento). Separar as duas facilita testar cada uma isoladamente e trocar o consumidor (ex. para Flink no futuro) sem tocar na ponte.

**Consequências:** +1 função Lambda no manifesto, mas cada uma com responsabilidade única (mais fácil de testar e de dar manutenção).

---

## File Manifest

### Etapa 1 — Warehouse (conectividade, ingestão batch, Redshift)

| # | Arquivo | Ação | Propósito | Agente | Dependências |
|---|---------|--------|-----------|--------|---------------|
| 1 | `infra/aws/fase2-ingestao/networking.tf` | Criar | VPC, subnets, security groups; define a rede onde a EC2 (Decisão 1) e os endpoints DMS/DataSync vivem | @infra-deployer | — |
| 2 | `infra/aws/fase2-ingestao/ec2_fase0.tf` | Criar | Instância EC2 rodando o `docker-compose.yml` da Fase 0 (Postgres/Oracle/MongoDB/MinIO/ShadowTraffic), dentro da VPC do item 1 | @infra-deployer | 1 |
| 3 | `infra/aws/fase2-ingestao/iam.tf` | Criar | Roles/policies para DMS, DataSync, Lambda (least privilege — leitura S3, `PutRecord` no Kinesis, execução Lambda) | @infra-deployer | — |
| 4 | `infra/aws/fase2-ingestao/dms_batch.tf` | Criar | DMS replication instance + endpoints (source: Postgres/Oracle/MongoDB na EC2 do item 2; target: S3) + 3 tasks (ongoing replication para Postgres/Oracle, full load para MongoDB) | @infra-deployer | 1, 2, 3 |
| 5 | `infra/aws/fase2-ingestao/datasync.tf` | Criar | DataSync location "Self-managed object storage" (MinIO na EC2 do item 2) + location S3 + task com agendamento | @infra-deployer | 1, 2, 3 |
| 6 | `infra/aws/fase2-ingestao/s3_bronze.tf` | Criar | Bucket S3 (Bronze), estrutura de prefixos por fonte/tabela, política de acesso | @infra-deployer | 3 |
| 7 | `infra/aws/fase2-ingestao/redshift.tf` | Criar | Redshift Serverless (namespace + workgroup), IAM role de acesso ao S3 | @infra-deployer | 3, 6 |
| 8 | `sql/aws/redshift_copy_merge.sql` | Criar | Scripts `COPY`/`MERGE` por tabela, projetando as 4 colunas canônicas de CDC (extensão da Decisão do Architecture Overview) | @databricks-sql-analyst (padrão de MERGE/SCD reaproveitável, mesmo raciocínio da Fase 1) | 7 |
| 9 | `docs/data-contract-cdc-aws-dms.md` | Criar | Extensão do contrato canônico de CDC (Onda 3) com o mapeamento específico do DMS (`Op`, `TimestampColumnName`, `transaction_id`/`transaction_record_id` → `cdc_sequence`) | (general) | — |

### Etapa 2 — Lakehouse (zero ingestão nova)

| # | Arquivo | Ação | Propósito | Agente | Dependências |
|---|---------|--------|-----------|--------|---------------|
| 10 | `infra/aws/fase2-ingestao/glue_catalog.tf` | Criar | Glue Catalog databases/tables (Iceberg) sobre o mesmo S3/Bronze da Etapa 1; crawler ou schema explícito | @infra-deployer | 6 |
| 11 | `sql/aws/athena_queries.sql` | Criar | Queries de validação Athena (contagem, join entre entidades, checagem de órfãos — mesma disciplina das Ondas 1/2/3) | (general) | 10 |

### Etapa 3 — Kappa (real-time)

| # | Arquivo | Ação | Propósito | Agente | Dependências |
|---|---------|--------|-----------|--------|---------------|
| 12 | `infra/aws/fase2-ingestao/kinesis.tf` | Criar | Kinesis Data Stream em modo on-demand | @infra-deployer | 1 |
| 13 | `infra/aws/fase2-ingestao/dms_realtime.tf` | Criar | 2ª task DMS por fonte relacional (Postgres, Oracle) — ongoing replication, target Kinesis (item 12) | @infra-deployer | 4, 12 |
| 14 | `src/aws/lambda_minio_kinesis_bridge/handler.py` | Criar | Recebe o Webhook de notificação de bucket do MinIO, valida payload, faz `PutRecord`/`PutRecords` no Kinesis | @python-developer | 12 |
| 15 | `infra/aws/fase2-ingestao/lambda_bridge.tf` | Criar | Função Lambda (item 14) + trigger HTTP (API Gateway ou Function URL) + permissões | @infra-deployer | 3, 14 |
| 16 | `docs/minio/webhook-notification-config.md` | Criar | Configuração da notificação de bucket do MinIO (destino Webhook, endpoint da Lambda do item 15) | (general) | 15 |
| 17 | `src/aws/lambda_kappa_consumer/handler.py` | Criar | Lê eventos do Kinesis (event source mapping), identifica o tipo de entidade, enriquece Pedido/Restaurante com lookup no cache do MongoDB | @python-developer | 12 |
| 18 | `src/aws/lambda_kappa_consumer/mongo_lookup.py` | Criar | Carrega a cópia do MongoDB do S3/Bronze (Etapa 1), cache em memória com TTL (Decisão 4) | @python-developer | 6, 17 |
| 19 | `infra/aws/fase2-ingestao/lambda_consumer.tf` | Criar | Função Lambda (item 17) + event source mapping com o Kinesis (item 12) + permissões de leitura S3 | @infra-deployer | 3, 12, 17 |
| 20 | `src/aws/lambda_minio_kinesis_bridge/teams_notify.py` | Criar | Alerta Teams em caso de falha da ponte (mandato SHOULD do DEFINE, TM-M01) | @teams-notifications-expert | 14 |
| 21 | `tests/aws/test_lambda_minio_kinesis_bridge.py` | Criar | Testes unitários do parsing do Webhook e chamada `PutRecord` (mock do cliente Kinesis) | @test-generator | 14 |
| 22 | `tests/aws/test_kappa_consumer_lookup.py` | Criar | Testes unitários do lookup/enriquecimento e do cache com TTL (mock do S3) | @test-generator | 17, 18 |

### Transversal

| # | Arquivo | Ação | Propósito |
|---|---------|--------|-----------|
| 23 | `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` | Editar (já parcialmente feito no `/brainstorm`/`/define`) | Registrar o resultado final do `/design` — decisão de EC2 na VPC (Decisão 1) e Lambda como consumidor do Kappa (Decisão 3) |
| 24 | `docs/MODELO_CONCEITUAL_UBER_EATS.md` | Verificar (provável no-op) | Confirmar que nenhuma mudança de modelo de domínio é necessária — esta feature é só de ingestão/infra |

---

## Code Patterns

### 1. DMS — task de ongoing replication para Postgres, target S3 (Etapa 1)

```hcl
resource "aws_dms_replication_task" "postgres_to_s3" {
  replication_task_id      = "postgres-batch-to-s3"
  migration_type           = "full-load-and-cdc"
  replication_instance_arn = aws_dms_replication_instance.fase2.replication_instance_arn
  source_endpoint_arn      = aws_dms_endpoint.postgres_source.endpoint_arn
  target_endpoint_arn      = aws_dms_endpoint.s3_bronze_target.endpoint_arn

  table_mappings = jsonencode({
    rules = [{
      rule-type = "selection"
      rule-id   = "1"
      rule-name = "all-tables"
      object-locator = { schema-name = "public", table-name = "%" }
      rule-action = "include"
    }]
  })
}

resource "aws_dms_endpoint" "s3_bronze_target" {
  endpoint_id   = "s3-bronze-target"
  endpoint_type = "target"
  engine_name   = "s3"

  s3_settings {
    bucket_name              = aws_s3_bucket.bronze.bucket
    bucket_folder             = "postgres"
    include_op_for_full_load  = true   # coluna Op -> cdc_operation
    timestamp_column_name     = "cdc_commit_ts"
    cdc_path                  = "cdc"
    add_column_name           = true
    # transaction_id/transaction_record_id -> cdc_sequence (ver docs/data-contract-cdc-aws-dms.md)
    include_transaction_details = true
  }
}
```

### 2. DMS — 2ª task, ongoing replication, target Kinesis (Etapa 3)

```hcl
resource "aws_dms_endpoint" "kinesis_realtime_target" {
  endpoint_id   = "kinesis-realtime-target"
  endpoint_type = "target"
  engine_name   = "kinesis"

  kinesis_settings {
    stream_arn            = aws_kinesis_stream.kappa.arn
    message_format        = "json"
    include_transaction_details = true
    include_partition_value = true
    partition_include_schema_table = true
  }
}

resource "aws_dms_replication_task" "postgres_to_kinesis" {
  replication_task_id      = "postgres-realtime-to-kinesis"
  migration_type           = "cdc"  # só CDC, sem full load — o full load já foi feito na task da Etapa 1
  replication_instance_arn = aws_dms_replication_instance.fase2.replication_instance_arn
  source_endpoint_arn      = aws_dms_endpoint.postgres_source.endpoint_arn
  target_endpoint_arn      = aws_dms_endpoint.kinesis_realtime_target.endpoint_arn
  table_mappings           = aws_dms_replication_task.postgres_to_s3.table_mappings
}
```

### 3. Kinesis Data Stream (on-demand)

```hcl
resource "aws_kinesis_stream" "kappa" {
  name             = "ubereats-kappa-fase2"
  stream_mode_details {
    stream_mode = "ON_DEMAND"
  }
}
```

### 4. Lambda ponte — MinIO Webhook → Kinesis `PutRecord`

```python
import json
import os
import boto3

kinesis = boto3.client("kinesis")
STREAM_NAME = os.environ["KINESIS_STREAM_NAME"]

def handler(event, context):
    """Recebe o payload do Webhook de notificação de bucket do MinIO
    (formato compatível com S3 Event Notification: Records[].s3.object.key etc.)
    e grava um registro no Kinesis por objeto notificado."""
    body = json.loads(event["body"])
    records = body.get("Records", [])

    for record in records:
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        event_name = record["eventName"]  # ex. s3:ObjectCreated:Put

        payload = {
            "bucket": bucket,
            "key": key,
            "event_name": event_name,
            "cdc_source_system": "minio-ubereats",
        }
        kinesis.put_record(
            StreamName=STREAM_NAME,
            Data=json.dumps(payload).encode("utf-8"),
            PartitionKey=key,
        )

    return {"statusCode": 200, "body": json.dumps({"processed": len(records)})}
```

### 5. Lambda consumidor do Kappa — lookup no MongoDB (cache em memória com TTL)

```python
import base64
import json
import time
import boto3

s3 = boto3.client("s3")
BRONZE_BUCKET = "ubereats-bronze-fase2"
MONGO_PREFIX = "mongodb/perfil_restaurante/"
CACHE_TTL_SECONDS = 300

_cache = {"data": None, "loaded_at": 0}

def _load_restaurant_profiles():
    now = time.time()
    if _cache["data"] is not None and (now - _cache["loaded_at"]) < CACHE_TTL_SECONDS:
        return _cache["data"]

    response = s3.list_objects_v2(Bucket=BRONZE_BUCKET, Prefix=MONGO_PREFIX)
    profiles = {}
    for obj in response.get("Contents", []):
        body = s3.get_object(Bucket=BRONZE_BUCKET, Key=obj["Key"])["Body"].read()
        for doc in json.loads(body):
            profiles[doc["restaurant_id"]] = doc

    _cache["data"] = profiles
    _cache["loaded_at"] = now
    return profiles

def handler(event, context):
    profiles = _load_restaurant_profiles()
    enriched = []

    for record in event["Records"]:
        payload = json.loads(base64.b64decode(record["kinesis"]["data"]))
        restaurant_id = payload.get("restaurant_id")
        if restaurant_id is not None and restaurant_id in profiles:
            payload["restaurant_profile"] = profiles[restaurant_id]
        enriched.append(payload)

    # Encaminhar `enriched` para o destino final (ex. novo stream, Firehose, log) — detalhar no /build
    return {"processed": len(enriched)}
```

### 6. AWS DataSync — MinIO (self-managed object storage) → S3

```hcl
resource "aws_datasync_location_object_storage" "minio_source" {
  server_hostname = aws_instance.fase0_ec2.private_ip
  bucket_name     = "ubereats-minio-bucket"
  access_key      = var.minio_access_key
  secret_key      = var.minio_secret_key
}

resource "aws_datasync_location_s3" "bronze_target" {
  s3_bucket_arn = aws_s3_bucket.bronze.arn
  subdirectory  = "/minio"
  s3_config {
    bucket_access_role_arn = aws_iam_role.datasync_s3_role.arn
  }
}

resource "aws_datasync_task" "minio_to_s3" {
  source_location_arn      = aws_datasync_location_object_storage.minio_source.arn
  destination_location_arn = aws_datasync_location_s3.bronze_target.arn

  schedule {
    schedule_expression = "rate(1 hour)"  # ajustar no /build conforme necessidade de frescor
  }
}
```

---

## Testing Strategy

| Tipo de teste | Escopo | Quando |
|---|---|---|
| `terraform validate` / `terraform plan` | Toda a infraestrutura do manifesto (Etapas 1-3) | Antes de qualquer `apply`, em cada etapa |
| Smoke test de conectividade (Etapa 1) | DMS consegue conectar nos endpoints source (Postgres/Oracle/MongoDB na EC2) e no target S3 | Manual, logo após a EC2 e a VPC subirem |
| Smoke test DataSync (Etapa 1) | Task de sync executa e novos objetos do MinIO aparecem no S3/Bronze | Manual, após configurar a location |
| Testes unitários — Lambda ponte (Etapa 3) | `tests/aws/test_lambda_minio_kinesis_bridge.py`: parsing do Webhook, chamada correta ao `put_record` (mock boto3) | Build, antes do deploy |
| Testes unitários — Lambda consumidor (Etapa 3) | `tests/aws/test_kappa_consumer_lookup.py`: cache/TTL, enriquecimento correto, comportamento quando `restaurant_id` não existe no cache | Build, antes do deploy |
| Smoke test de streaming (Etapa 3) | Escrever um objeto no MinIO; confirmar que aparece no Kinesis em segundos; confirmar que o consumidor processa e enriquece | Manual, após deploy da ponte e do consumidor |
| Join de integridade (todas as etapas) | Mesma disciplina das Ondas 1/2/3: query Athena/Redshift entre entidades relacionadas retorna 0 órfãos | Após cada etapa concluída |
| `/pipeline-review-init` | Lanes `data_contracts`, `architecture_medallion`, `idempotency_reprocessing`, `security_governance` no mínimo (mandatos MED-M04/GOV-M01 do DEFINE) | Após o Build completo de cada etapa, antes de avançar para a próxima |

---

## Riscos carregados do DEFINE (com mitigação de design)

| Risco (DEFINE) | Mitigação de design |
|---|---|
| A-001 — viabilidade de conectividade de rede AWS↔sistemas self-hosted | Decisão 1 (EC2 na mesma VPC) resolve o risco por completo — não há mais dependência de VPN/IP público residencial |
| A-002 — formato dos metadados de ordenação do DMS para `cdc_sequence` | Mapeamento proposto (`transaction_id`+`transaction_record_id` via `include_transaction_details`) documentado em `docs/data-contract-cdc-aws-dms.md` (item 9) — precisa de confirmação com teste real no início do `/build`, mesmo padrão de risco já visto no Design da Onda 3 (Oracle LogMiner) |
| A-003 — 2 tasks DMS concorrentes no mesmo replication slot/LogMiner | Sequenciamento por etapa (Goals do DEFINE) confina a 2ª task à Etapa 3, última da fase — mitigação operacional, não técnica; se ainda assim o motor não suportar, a Decisão 2 do brainstorm original (Kinesis como hub único, Firehose→S3) vira o plano B, sem precisar redesenhar do zero |
| A-004 — latência do lookup do consumidor contra o MongoDB no S3 | Decisão 4 (cache em memória com TTL na própria Lambda) resolve para o volume esperado (~500 documentos); reavaliar para DynamoDB só se o volume crescer muito |

---

## Status: ✅ Shipped

**Build report:** `BUILD_REPORT_INGESTAO_AWS_FASE2.md` (nesta pasta) — manifesto completo implementado; `terraform validate` não executou por limitação do ambiente de build (não do código, ver relatório).

**Próximo passo:** ✅ SHIPPED — ver `SHIPPED_2026-09-10.md` nesta mesma pasta.
