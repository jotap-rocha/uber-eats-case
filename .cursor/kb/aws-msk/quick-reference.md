---
domain: aws-msk
topic: quick-reference
---

# Amazon MSK — Quick Reference

### Serverless em números

| Item | Valor |
|---|---|
| Auth | **IAM obrigatório** (SASL/IAM), sem ACLs Kafka |
| Porta | **9098** (SASL_SSL + IAM, privado) |
| Partições (líderes) | 2400 não-compactadas · **120 compactadas** por cluster |
| Throughput | 200 MBps in / 400 MBps out por cluster; 5 / 10 MBps por partição |
| Mensagem | máx. 8 MiB |
| Conexões | 3000 clientes; 100 tentativas/s |
| Consumer groups | 500 |
| Clusters por conta | 10 |
| Custo fixo | US$ 0,75/cluster-hora + US$ 0,0015/partição-hora |

### Terraform

```hcl
resource "aws_msk_serverless_cluster" "this" {
  cluster_name = "<PROJETO>-msk"
  vpc_config {
    subnet_ids         = var.private_subnet_ids
    security_group_ids = [aws_security_group.msk.id]   # ingress 9098 só do SG dos clientes
  }
  client_authentication {
    sasl {
      iam { enabled = true }
    }
  }
}

output "bootstrap" { value = aws_msk_serverless_cluster.this.bootstrap_brokers_sasl_iam }
```

### `client.properties` (Java / CLI Kafka)

```properties
security.protocol=SASL_SSL
sasl.mechanism=AWS_MSK_IAM
sasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required;
sasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMClientCallbackHandler
```

Jar `aws-msk-iam-auth` no classpath (`libs/` do Kafka ou plugin).

### Tópico compactado

```bash
kafka-topics.sh --bootstrap-server <BOOTSTRAP>:9098 --command-config client.properties \
  --create --topic clientes.estado --partitions 3 \
  --config cleanup.policy=compact      # só na criação, não altera depois
```

### Configs editáveis no Serverless

`cleanup.policy` (só na criação) · `compression.type` · `max.message.bytes` (≤ 8 MiB) ·
`message.timestamp.difference.max.ms` · `message.timestamp.type` · `retention.bytes` ·
`retention.ms`. **Todo o resto é fixo** (inclusive `segment.bytes`, `min.compaction.lag.ms`).

### IAM — ações mais usadas

| Ação | Para |
|---|---|
| `kafka-cluster:Connect`, `DescribeCluster` | qualquer cliente |
| `kafka-cluster:CreateTopic`, `DescribeTopic`, `AlterTopic` | admin de tópicos |
| `kafka-cluster:WriteData` | produtor |
| `kafka-cluster:ReadData`, `AlterGroup`, `DescribeGroup` | consumidor |

### Teardown

```bash
terraform destroy -target=aws_mskconnect_connector.s3_sink   # connector primeiro
terraform destroy -target=aws_msk_serverless_cluster.this
```

### Armadilhas

| Sintoma | Causa |
|---|---|
| `SaslAuthenticationException` | jar ausente, policy sem `Connect`, região errada no token |
| Timeout no bootstrap | cliente fora da VPC / SG sem 9098 |
| `INVALID_REQUEST` ao criar tópico | config não permitida ou limite de partições compactadas (120) |
| Kafka Streams falha em tópico interno | `segment.bytes` não editável no Serverless |
