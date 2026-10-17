---
domain: gcp-managed-kafka
topic: auth-and-network
---

# Autenticação e endpoint

## Endpoint

- Bootstrap: `bootstrap.<CLUSTER>.<REGION>.managedkafka.<GCP_PROJECT_ID>.cloud.goog:9092`
  (obter com `gcloud managed-kafka clusters describe ... --format="value(bootstrapAddress)"`).
- **Toda conexão é TLS** → `security.protocol=SASL_SSL`. Certificado é público/confiável;
  normalmente não precisa truststore custom.
- Paridade Azure: Event Hubs usa 9093 + `$ConnectionString`; aqui 9092 + identidade Google.

## Mecanismos

| Mecanismo | Credencial | Quando |
|---|---|---|
| **SASL/OAUTHBEARER** (recomendado) | ADC: SA anexada à VM/GKE/Dataflow ou login do dev; handler `com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler` | Padrão — sem segredo |
| SASL/PLAIN + access token | user = e-mail do principal; password = access token OAuth (curto) | Clientes sem o handler Java (ex.: libs não-JVM) |
| SASL/PLAIN + chave de SA | user = e-mail da SA; password = **JSON da chave em base64, uma linha** | Só teste. Chave = segredo de longa duração |
| mTLS | Certificados de cliente via CA Service (`tls_config`) | Cenários sem identidade Google — **a validar** |

## Autorização

- IAM: `roles/managedkafka.client` dá conexão/produção/consumo no cluster.
- Para granularidade por tópico/grupo, o serviço oferece **Kafka ACLs** gerenciadas —
  **a validar** escopo e precedência sobre IAM antes de depender.
- O quickstart oficial também concede ao SA do cliente `roles/iam.serviceAccountTokenCreator`
  e `roles/iam.serviceAccountOpenIdTokenCreator` (geração do token pelo handler).

## Handler OAUTHBEARER

- Distribuído pelo repositório `googleapis/managedkafka` (release zip com dependências para
  `$KAFKA_HOME/libs/`; o quickstart usa v1.0.5). Para apps Java, adicionar o artefato
  Maven do login handler — coordenadas **a validar** no README do repositório.
- Python (`confluent-kafka`): usar `oauth_cb` que gera token a partir de `google.auth`
  (exemplo no mesmo repositório) — **a validar** por versão de lib.

## Rede

- Cliente precisa rotear para as subnets do cluster (mesma VPC ou peering/VPN).
- DNS privado criado automaticamente na VPC configurada; de outra VPC, configurar DNS.
- Firewall: egress TCP 9092 para os IPs dos brokers.

## Erros comuns

| Sintoma | Causa provável |
|---|---|
| Timeout no bootstrap | Cliente fora da VPC/subnet do cluster, ou DNS |
| `SaslAuthenticationException` | Falta `managedkafka.client`, token expirado ou chave PLAIN com quebra de linha |
| `ClassNotFoundException GcpLoginCallbackHandler` | Jar do handler fora do classpath |
