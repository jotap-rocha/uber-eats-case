---
domain: gcp-managed-kafka
topic: kafka-client-auth
---

# Pattern: autenticação do cliente Kafka (SASL_SSL)

## Problema

Produtor/consumidor/Kafka CLI precisa conectar ao Managed Kafka sem credencial de longa
duração no repositório.

## Solução

`SASL_SSL` + **OAUTHBEARER** com o handler do Google, usando ADC (SA anexada ao runtime ou
login do dev). PLAIN só como fallback, com segredo vindo de env/Secret Manager.

## 1. Permissões

```bash
gcloud projects add-iam-policy-binding <GCP_PROJECT_ID> \
  --member="serviceAccount:<SA_EMAIL>" --role="roles/managedkafka.client"
```

O quickstart oficial (cliente em VM com SA) também concede à SA
`roles/iam.serviceAccountTokenCreator` e `roles/iam.serviceAccountOpenIdTokenCreator`.

Runtime: VM/GKE/Dataflow **na VPC/subnet** do cluster, rodando como `<SA_EMAIL>`.

## 2. OAUTHBEARER (recomendado)

Handler: release zip de `github.com/googleapis/managedkafka` descompactado em
`$KAFKA_HOME/libs/` (ou dependência Maven do login handler em apps Java — **a validar**
coordenadas).

`client.properties`:

```properties
bootstrap.servers=bootstrap.<CLUSTER>.<REGION>.managedkafka.<GCP_PROJECT_ID>.cloud.goog:9092
security.protocol=SASL_SSL
sasl.mechanism=OAUTHBEARER
sasl.login.callback.handler.class=com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler
sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
```

Teste:

```bash
export BOOTSTRAP=$(gcloud managed-kafka clusters describe <CLUSTER> \
  --location=<REGION> --format="value(bootstrapAddress)")
kafka-topics.sh --bootstrap-server "$BOOTSTRAP" --command-config client.properties --list
echo "k1:v1" | kafka-console-producer.sh --bootstrap-server "$BOOTSTRAP" \
  --producer.config client.properties --topic <TOPIC> \
  --property parse.key=true --property key.separator=:
kafka-console-consumer.sh --bootstrap-server "$BOOTSTRAP" \
  --consumer.config client.properties --topic <TOPIC> --from-beginning
```

Nenhum segredo no arquivo — pode ser versionado (com placeholders).

## 3. PLAIN com access token (cliente sem handler)

```properties
security.protocol=SASL_SSL
sasl.mechanism=PLAIN
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required \
  username="<SA_EMAIL>" password="${KAFKA_ACCESS_TOKEN}";
```

- `KAFKA_ACCESS_TOKEN` = `gcloud auth print-access-token` (ou `google.auth` no código);
  expira em ~1 h — o cliente precisa renovar/reconectar.
- `${...}` **não** é expandido pelo Kafka: gere o arquivo em runtime ou use um
  `ConfigProvider` (ex.: `EnvVarConfigProvider`/`FileConfigProvider`) — nunca commit do valor.

## 4. PLAIN com chave de SA (somente teste)

- password = conteúdo da chave JSON **em base64, numa linha** (`base64 -w0 key.json`).
- Chave fica em Secret Manager; o arquivo `.properties` final é gerado em runtime e
  está no `.gitignore`. Apague a chave da SA ao terminar o teste.

## 5. Python (`confluent-kafka`)

```python
import os
conf = {
    "bootstrap.servers": os.environ["KAFKA_BOOTSTRAP"],
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "OAUTHBEARER",
    "oauth_cb": gcp_token_cb,   # retorna (token, expiry_epoch) via google.auth — a validar
}
```

Implementação de `gcp_token_cb` seguindo o exemplo Python do repositório
`googleapis/managedkafka` — **a validar** por versão da lib.

## Verificação

- `kafka-topics.sh --list` retorna sem `SaslAuthenticationException`.
- `git grep -nE "password=\"[A-Za-z0-9+/=]{100,}"` vazio.

## Anti-patterns

- Chave JSON base64 dentro de `client.properties` versionado.
- `security.protocol=PLAINTEXT`/`SASL_PLAINTEXT` (o serviço exige TLS).
- Rodar cliente fora da VPC e "abrir" acesso público para contornar.
