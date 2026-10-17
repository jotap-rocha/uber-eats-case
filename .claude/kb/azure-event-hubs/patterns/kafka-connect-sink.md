---
domain: azure-event-hubs
topic: kafka-connect-sink
---

# Pattern — kafka-connect-sink (Kafka Connect contra Event Hubs)

Event Hubs faz o papel do cluster Kafka do Connect: guarda os tópicos internos
(`config`, `offset`, `status`) e os tópicos de dados. O worker roda fora (VM, container,
AKS) — Event Hubs **não** hospeda Connect.

> **RISCO A VALIDAR — HDFS 2 Sink:** a combinação *Confluent HDFS 2 Sink Connector* +
> Event Hubs **nunca foi testada contra um Event Hub real** neste projeto. A doc oficial
> da Microsoft só demonstra `FileStreamSource/Sink`. Trate tudo da seção 4 como hipótese
> até um teste de fumaça passar (seção 5).

## 1. Pré-requisitos no Event Hubs

- Namespace **Standard** (Basic não tem Kafka).
- Orçamento de tópicos: limite de **10 event hubs** por namespace no Standard =
  3 internos do Connect + tópicos de dados (+ DLQ, se usar).
- Tópicos internos **devem ser compactados**. O worker cria via AdminClient com
  compaction; a Microsoft avisa que não corrige configuração errada de tópico interno.
  Opcional: criar no Terraform com `cleanup_policy = "Compact"`.
- Identidade: policy SAS **no namespace** com `Manage, Send, Listen` (o worker cria
  tópicos) **ou** Entra ID com `Azure Event Hubs Data Owner`.

## 2. `connect-distributed.properties` (worker)

```properties
bootstrap.servers=<NAMESPACE>.servicebus.windows.net:9093
group.id=connect-cluster-group

config.storage.topic=connect-cluster-configs
offset.storage.topic=connect-cluster-offsets
status.storage.topic=connect-cluster-status
# Replicação é do serviço (3x no storage): RF dos internos = 1
config.storage.replication.factor=1
offset.storage.replication.factor=1
status.storage.replication.factor=1

key.converter=org.apache.kafka.connect.storage.StringConverter
value.converter=org.apache.kafka.connect.json.JsonConverter
value.converter.schemas.enable=false
offset.flush.interval.ms=10000
rest.advertised.host.name=connect

# Segredo fora do arquivo (KIP-421: referências em config do worker)
config.providers=env
config.providers.env.class=org.apache.kafka.common.config.provider.EnvVarConfigProvider

security.protocol=SASL_SSL
sasl.mechanism=PLAIN
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="${env:EH_NS_CONNECTION_STRING}";
# Os clientes internos (producer/consumer dos connectors) precisam do MESMO bloco
producer.security.protocol=SASL_SSL
producer.sasl.mechanism=PLAIN
producer.sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="${env:EH_NS_CONNECTION_STRING}";
consumer.security.protocol=SASL_SSL
consumer.sasl.mechanism=PLAIN
consumer.sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="${env:EH_NS_CONNECTION_STRING}";

plugin.path=/opt/connect/plugins
```

- Esquecer os prefixos `producer.`/`consumer.` = worker sobe, connectors falham com
  timeout/SASL. Algumas versões também exigem `admin.` — **a validar** na versão usada.
- `EnvVarConfigProvider` existe a partir do Kafka 3.5; versão mais antiga → gerar o
  arquivo em runtime (template + env), fora do git.

Subir: `bin/connect-distributed.sh connect-distributed.properties` → aguardar
`Finished starting connectors and tasks`; REST em `:8083`.

## 3. Smoke test com FileStream (validado pela doc Microsoft)

```bash
curl -s -X POST -H "Content-Type: application/json" localhost:8083/connectors -d '{
  "name": "file-sink",
  "config": {"connector.class": "org.apache.kafka.connect.file.FileStreamSinkConnector",
             "tasks.max": "1", "topics": "pedidos", "file": "/tmp/pedidos.out"}}'
curl -s localhost:8083/connectors/file-sink/status
```

Isso prova worker ↔ Event Hubs. Só então avance para o HDFS.

## 4. HDFS 2 Sink — **risco a validar**

```json
{
  "name": "hdfs-sink-pedidos",
  "config": {
    "connector.class": "io.confluent.connect.hdfs.HdfsSinkConnector",
    "tasks.max": "2",
    "topics": "pedidos",
    "hdfs.url": "hdfs://<NAMENODE_HOST>:8020",
    "hadoop.conf.dir": "/etc/hadoop/conf",
    "topics.dir": "/data/bronze/topics",
    "logs.dir": "/data/bronze/connect-wal",
    "format.class": "io.confluent.connect.hdfs.parquet.ParquetFormat",
    "flush.size": "1000",
    "rotate.interval.ms": "600000",
    "errors.tolerance": "all",
    "errors.deadletterqueue.topic.name": "pedidos-dlq",
    "errors.deadletterqueue.topic.replication.factor": "1"
  }
}
```

Hipóteses que o teste precisa confirmar ou derrubar:

| # | Risco | Como validar |
|---|---|---|
| R1 | HDFS 2 connector usa cliente **Hadoop 2.x**; gravar direto no ADLS Gen2 (`abfss://`) depende do driver ABFS (Hadoop 3.x) → provavelmente **não** funciona sem HDFS real | tentar `hdfs.url=abfss://...` e registrar o erro; plano B abaixo |
| R2 | Compatibilidade da versão do connector com a versão do Kafka Connect / Java | `GET /connector-plugins` lista a classe; task `RUNNING` |
| R3 | Recuperação de offsets: o connector reconstrói offsets a partir dos arquivos no HDFS + WAL (`logs.dir`), não só do consumer group no Event Hubs | matar o worker no meio de um flush e conferir duplicata/perda |
| R4 | DLQ conta no limite de 10 tópicos e precisa de RF=1 | criar e ver mensagens ruins chegando |
| R5 | Rede: worker precisa alcançar `:9093` (Event Hubs) **e** NameNode/DataNodes (8020/9866) | teste de conectividade antes do deploy |
| R6 | Kerberos no HDFS + SASL no Event Hubs no mesmo worker (JAAS duplo) | só se o HDFS for kerberizado |
| R7 | Licença/distribuição do connector Confluent no ambiente alvo | checar licença antes de produção |

## 5. Critério de aceite do risco

1. FileStream sink OK (seção 3).
2. HDFS sink `RUNNING`, arquivos Parquet aparecem em `topics.dir` após `flush.size`.
3. Restart do worker sem duplicar nem perder (contagem Event Hubs × arquivos).
4. Registrar resultado em ADR. Se R1 falhar, decidir plano B.

## Plano B (se HDFS 2 + ADLS não fechar)

| Opção | Trade-off |
|---|---|
| **Event Hubs Capture** → ADLS Gen2 (Avro/Parquet) | gerenciado, sem worker; cobrado por hora no Standard; layout de path fixo |
| Stream Analytics → ADLS (KB `azure-stream-analytics`) | SQL, SU-hora |
| Spark Structured Streaming (Kafka source) → Delta/Parquet | flexível; precisa cluster |
| Connector HDFS 3 / sink nativo ADLS de terceiros | outra licença; também **a validar** |

## Limpeza

Tópicos internos persistem após derrubar o worker: apagar os event hubs
`connect-cluster-*` ou o namespace inteiro no teardown do dia.
