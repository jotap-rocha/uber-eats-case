---
domain: aws-msk
topic: kafka-client-auth
---

# Pattern: autenticação de cliente Kafka no MSK (SASL/IAM)

## Problema

Produtores, consumidores e ferramentas Kafka precisam autenticar no MSK Serverless sem
senha nem access key. Paridade com `azure-event-hubs` (lá: SASL PLAIN + connection
string; aqui: **IAM**, nenhum segredo).

## Como funciona

1. O cliente obtém credenciais AWS **temporárias** do runtime (instance profile, ECS task
   role, role do MSK Connect/Flink, SSO no dev).
2. O plugin assina um token SigV4 e o envia no handshake SASL na porta **9098**.
3. O MSK autoriza cada operação (Connect, WriteData, ReadData…) contra a **IAM policy**
   da identidade. Não há ACL Kafka.

## 1. IAM policy mínima

Produtor de `vendas.*` + consumidor do grupo `etl-vendas`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    { "Effect": "Allow",
      "Action": ["kafka-cluster:Connect", "kafka-cluster:DescribeCluster"],
      "Resource": "arn:aws:kafka:<REGION>:<AWS_ACCOUNT_ID>:cluster/<CLUSTER_NAME>/<CLUSTER_UUID>" },
    { "Effect": "Allow",
      "Action": ["kafka-cluster:DescribeTopic", "kafka-cluster:WriteData", "kafka-cluster:ReadData"],
      "Resource": "arn:aws:kafka:<REGION>:<AWS_ACCOUNT_ID>:topic/<CLUSTER_NAME>/<CLUSTER_UUID>/vendas.*" },
    { "Effect": "Allow",
      "Action": ["kafka-cluster:AlterGroup", "kafka-cluster:DescribeGroup"],
      "Resource": "arn:aws:kafka:<REGION>:<AWS_ACCOUNT_ID>:group/<CLUSTER_NAME>/<CLUSTER_UUID>/etl-vendas" }
  ]
}
```

- Admin de tópicos (pipeline de infra) adiciona `CreateTopic`, `AlterTopic`,
  `DescribeTopicDynamicConfiguration`, `AlterTopicDynamicConfiguration`.
- Produtor idempotente (default no Kafka ≥ 3.0) pode exigir `kafka-cluster:WriteDataIdempotently`
  — **a validar** com o seu cliente.
- Em Terraform, monte os ARNs a partir de `aws_msk_serverless_cluster.this.arn`
  (substitua `:cluster/` por `:topic/` / `:group/`).

## 2. Java / CLI Kafka — mecanismo `AWS_MSK_IAM`

```properties
# client.properties
security.protocol=SASL_SSL
sasl.mechanism=AWS_MSK_IAM
sasl.jaas.config=software.amazon.msk.auth.iam.IAMLoginModule required;
sasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMClientCallbackHandler
```

- Coloque o jar `aws-msk-iam-auth` (release "all" com dependências) em `kafka/libs/`.
- Dev com SSO: `...IAMLoginModule required awsProfileName="<PROFILE>";`
- Assumir role específica: `awsRoleArn="arn:aws:iam::<AWS_ACCOUNT_ID>:role/<ROLE>"` no JAAS.
- Maven: `software.amazon.msk:aws-msk-iam-auth` (use a última versão estável).

### Variante `OAUTHBEARER` (Java, mesmo jar)

```properties
security.protocol=SASL_SSL
sasl.mechanism=OAUTHBEARER
sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
sasl.login.callback.handler.class=software.amazon.msk.auth.iam.IAMOAuthBearerLoginCallbackHandler
sasl.client.callback.handler.class=software.amazon.msk.auth.iam.IAMOAuthBearerLoginCallbackHandler
```

(nomes das classes conforme README do `aws-msk-iam-auth` — **a validar** na versão usada)

## 3. Python — `OAUTHBEARER` com signer oficial

```bash
pip install confluent-kafka aws-msk-iam-sasl-signer-python
```

```python
import os
from confluent_kafka import Producer
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider

REGION = os.environ["AWS_REGION"]

def oauth_cb(_config):
    token, expiry_ms = MSKAuthTokenProvider.generate_auth_token(REGION)
    return token, expiry_ms / 1000

producer = Producer({
    "bootstrap.servers": os.environ["MSK_BOOTSTRAP"],   # host:9098 — vem de env, não do código
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "OAUTHBEARER",
    "oauth_cb": oauth_cb,
})
producer.produce("vendas.pedidos.v1", key=b"123", value=b'{"pedido_id":123}')
producer.flush()
```

Signers oficiais também para JavaScript, Go e .NET (`aws-msk-iam-sasl-signer-*`).

## 4. Rede

- Cliente na mesma VPC (ou VPC cliente registrada no cluster, máx. 5).
- SG do cluster: ingress TCP **9098** a partir do SG do cliente.
- Teste de conectividade:

```bash
kafka-topics.sh --bootstrap-server "$MSK_BOOTSTRAP" --command-config client.properties --list
```

## Troubleshooting

| Erro | Causa provável |
|---|---|
| `ClassNotFoundException ...IAMLoginModule` | jar fora do classpath |
| `SaslAuthenticationException: Access denied` | policy sem `kafka-cluster:Connect` ou ARN com UUID errado |
| `TopicAuthorizationException` | falta `WriteData`/`ReadData`/`DescribeTopic` no ARN do tópico |
| `GroupAuthorizationException` | falta `AlterGroup`/`DescribeGroup` no ARN do grupo |
| Token expirado em app longa | use a lib oficial (renova sozinha); não gere token manual |
| Timeout | fora da VPC / SG sem 9098 / bootstrap de outro tipo de auth |

## Anti-padrões

| Errado | Certo |
|---|---|
| `AWS_ACCESS_KEY_ID` fixo no container | task role / instance profile |
| Policy `kafka-cluster:*` em `*` | ações e ARNs por app |
| Logar o token SASL ou o payload com PII | logar só tópico/partição/offset |
