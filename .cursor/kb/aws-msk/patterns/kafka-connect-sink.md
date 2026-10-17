---
domain: aws-msk
topic: kafka-connect-sink
---

# Pattern: Kafka Connect sink (MSK → S3; HDFS como risco)

## Problema

Descarregar tópicos do MSK Serverless no data lake (S3, zona `raw/`) de forma
gerenciada, com auth IAM nas duas pontas. Paridade com o setup Event Hubs + Kafka Connect
do Azure (lá o maior risco era o HDFS 2 Sink — aqui também).

## Opções

| Opção | Quando | Observação |
|---|---|---|
| **MSK Connect + S3 Sink** | default | gerenciado, US$ 0,11/MCU-h, Kafka Connect 2.7.1 ou **3.7.x** |
| Kafka Connect self-managed (EC2/ECS) | precisa de plugin/config que o MSK Connect não aceita | você opera workers e tópicos internos |
| MSK Data Delivery (tópico → S3) | **só MSK provisionado com Express brokers** | não serve para Serverless |
| HDFS 2/3 Sink | só se HDFS for requisito duro | **risco a validar** (abaixo) |

## 1. Plugin (S3 Sink)

- Baixe o zip do conector S3 Sink (ex.: Confluent `kafka-connect-s3`, licença Confluent
  Community; ou alternativa Apache 2.0 como o S3 sink da Lenses/Aiven) e suba no S3.
- Verifique a licença do conector antes de usar em produção.

```hcl
resource "aws_mskconnect_custom_plugin" "s3_sink" {
  name         = "<PROJETO>-s3-sink"
  content_type = "ZIP"
  location {
    s3 {
      bucket_arn = "arn:aws:s3:::<ARTIFACTS_BUCKET>"
      file_key   = "plugins/kafka-connect-s3.zip"
    }
  }
}
```

## 2. Service execution role (MSK Connect)

Trust: `kafkaconnect.amazonaws.com`. Permissões:

- Kafka: `Connect`, `DescribeCluster`; `ReadData`/`DescribeTopic` nos tópicos lidos;
  `AlterGroup`/`DescribeGroup` no grupo `connect-<CONNECTOR_NAME>`; criação/escrita nos
  tópicos internos que o MSK Connect usa (prefixo `__amazon_msk_connect_*` — **a validar**
  o nome exato na sua versão).
- S3: `s3:PutObject`, `s3:AbortMultipartUpload`, `s3:ListMultipartUploadParts` em
  `arn:aws:s3:::<BUCKET>/raw/kafka/*`; `s3:ListBucket`, `s3:GetBucketLocation` no bucket.
- Logs: CloudWatch Logs no log group do connector.

## 3. Connector

```hcl
resource "aws_mskconnect_connector" "s3_sink" {
  name                 = "<PROJETO>-s3-sink"
  kafkaconnect_version = "3.7.x"        # a validar o literal aceito pela API na sua região

  capacity {
    provisioned_capacity {
      mcu_count    = 1
      worker_count = 1                   # lab: 1 worker, 1 MCU ≈ US$ 0,11/h
    }
  }

  connector_configuration = {
    "connector.class"                = "io.confluent.connect.s3.S3SinkConnector"
    "tasks.max"                      = "1"
    "topics"                         = "vendas.pedidos.v1"
    "s3.region"                      = var.region
    "s3.bucket.name"                 = "<BUCKET>"
    "topics.dir"                     = "raw/kafka"
    "storage.class"                  = "io.confluent.connect.s3.storage.S3Storage"
    "format.class"                   = "io.confluent.connect.s3.format.json.JsonFormat"
    "flush.size"                     = "1000"
    "rotate.schedule.interval.ms"    = "600000"
    "partitioner.class"              = "io.confluent.connect.storage.partitioner.TimeBasedPartitioner"
    "path.format"                    = "'dt'=YYYY-MM-dd"
    "partition.duration.ms"          = "86400000"
    "locale"                         = "en-US"
    "timezone"                       = "UTC"
    "timestamp.extractor"            = "Record"
    "key.converter"                  = "org.apache.kafka.connect.storage.StringConverter"
    "value.converter"                = "org.apache.kafka.connect.json.JsonConverter"
    "value.converter.schemas.enable" = "false"
  }

  kafka_cluster {
    apache_kafka_cluster {
      bootstrap_servers = aws_msk_serverless_cluster.this.bootstrap_brokers_sasl_iam
      vpc {
        security_groups = [aws_security_group.connect.id]
        subnets         = var.private_subnet_ids
      }
    }
  }

  kafka_cluster_client_authentication { authentication_type = "IAM" }
  kafka_cluster_encryption_in_transit { encryption_type = "TLS" }

  plugin {
    custom_plugin {
      arn      = aws_mskconnect_custom_plugin.s3_sink.arn
      revision = aws_mskconnect_custom_plugin.s3_sink.latest_revision
    }
  }

  service_execution_role_arn = aws_iam_role.connect.arn
}
```

- Credencial S3: o conector usa a cadeia padrão do SDK → pega a **service execution
  role**. Nenhuma `aws.access.key.id` na config.
- Parquet/Avro exigem schema (Schema Registry/Glue SR ou JSON com schema) — JSON sem
  schema é o caminho mais curto para o lab.
- VPC precisa de rota para o S3 (gateway endpoint S3 recomendado; sem NAT = sem custo extra).

## 4. Kafka Connect self-managed com IAM

```properties
# connect-distributed.properties (trecho)
bootstrap.servers=<BOOTSTRAP>:9098
security.protocol=SASL_SSL
sasl.mechanism=AWS_MSK_IAM
sasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required;
sasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMClientCallbackHandler
# repetir os 4 com prefixo producer. / consumer. / admin.
config.storage.topic=connect-configs
offset.storage.topic=connect-offsets
status.storage.topic=connect-status
offset.storage.partitions=3     # tópicos internos são compactados: cabem no limite de 120
status.storage.partitions=1
```

**A validar:** fatores de replicação dos tópicos internos no Serverless (`*.replication.factor`;
teste `-1` = default do broker) e pré-criar os 3 tópicos com `cleanup.policy=compact`.

## 5. HDFS Sink — **risco a validar**

- O HDFS 2/3 Sink (Confluent) escreve em um NameNode (`hdfs.url`); na AWS isso significa
  um **cluster EMR** ligado (custo por instância-hora) ou HDFS self-managed.
- Riscos não testados: empacotamento do plugin (jars Hadoop) no MSK Connect, rede
  connector → NameNode, Kerberos, e apontar `hdfs.url` para `s3a://` (não suportado
  oficialmente).
- Recomendação: usar **S3 Sink** e ler com Spark/EMR via S3. Se HDFS for requisito,
  POC isolada com EMR mínimo, critério de aceite = arquivo visível em `hdfs dfs -ls`.

## Verificação

```bash
aws kafkaconnect list-connectors --query 'connectors[].{n:connectorName,s:connectorState}'
aws s3 ls s3://<BUCKET>/raw/kafka/vendas.pedidos.v1/ --recursive | head
```

## Teardown

Connector → custom plugin (opcional) → cluster. Connector parado ainda é recurso: destrua.
