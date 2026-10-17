---
domain: aws-s3
topic: access-model-and-defaults
---

# Modelo de acesso e defaults de segurança do S3

## Avaliação de permissão (simplificada)

```
Deny explícito em qualquer policy? ──sim──> NEGA
        │não
SCP / permission boundary / session policy permitem? ──não──> NEGA
        │sim
Mesma conta: Allow na IAM policy OU na bucket policy? ──sim──> PERMITE
Cross-account: Allow na IAM policy (conta origem) E na bucket policy? ──sim──> PERMITE
        │senão
NEGA (default)
```

## IAM policy × bucket policy

| | IAM policy (identity-based) | Bucket policy (resource-based) |
|---|---|---|
| Anexada a | role / usuário / grupo | bucket |
| Pergunta que responde | "o que **esta identidade** pode fazer?" | "**quem** pode fazer o quê neste bucket?" |
| `Principal` | implícito (a identidade) | obrigatório |
| Cross-account | não sozinha | sim (junto com IAM do outro lado) |
| Uso no harness | **padrão** para jobs/serviços | guarda-chuva: Deny sem TLS, Deny fora do VPC endpoint, cross-account |
| Limite de tamanho | por role (managed policies) | 20 KB por bucket |

Regra prática: **conceda com IAM policy na role**; use a bucket policy para **negar**
(TLS, rede) e para cross-account.

### Bucket policy guarda-chuva

```json
{
  "Version": "2012-10-17",
  "Statement": [
    { "Sid": "NegaSemTLS", "Effect": "Deny", "Principal": "*", "Action": "s3:*",
      "Resource": ["arn:aws:s3:::<BUCKET>", "arn:aws:s3:::<BUCKET>/*"],
      "Condition": { "Bool": { "aws:SecureTransport": "false" } } }
  ]
}
```

Cuidado com Deny por `aws:SourceVpce`: bloqueia também console e Terraform fora da VPC —
inclua exceção para a role de deploy ou não use em lab.

## Defaults atuais

| Default | Desde | Implicação |
|---|---|---|
| **SSE-S3 em todo objeto novo** (AES-256), sem custo, não desativável | 05/01/2023 (validado) | criptografia em repouso garantida; SSE-KMS se precisar de CMK |
| **Block Public Access** ligado em bucket novo | abril/2023 (a validar data exata) | policy/ACL pública é rejeitada |
| **Object Ownership = BucketOwnerEnforced** (ACLs off) em bucket novo | abril/2023 (a validar data exata) | permissão só por policy |

Mesmo sendo default, declare tudo no Terraform — torna explícito e evita drift.

## Block Public Access (4 flags)

| Flag | Bloqueia |
|---|---|
| `block_public_acls` | novas ACLs públicas |
| `ignore_public_acls` | ACLs públicas existentes |
| `block_public_policy` | bucket policy pública |
| `restrict_public_buckets` | acesso público/cross-account via policy pública |

Ligue também no nível da **conta** (`aws_s3_account_public_access_block`) em conta de lab.

## Criptografia

| Opção | Chave | Custo | Quando |
|---|---|---|---|
| SSE-S3 | gerenciada pelo S3 | grátis | default de lab |
| SSE-KMS (AWS managed `aws/s3`) | KMS | requests KMS | auditoria de uso |
| SSE-KMS (CMK) | sua key | US$ por key/mês + requests | controle de quem decifra; exige `kms:*` nas roles |
| DSSE-KMS | dupla camada | maior | compliance específico |

Com SSE-KMS ligue `bucket_key_enabled = true` (reduz requests KMS).

## Identidades típicas no harness

| Consumidor | Identidade |
|---|---|
| Dev (laptop) | SSO permission set |
| Redshift COPY | role associada ao namespace |
| MSK Connect | service execution role |
| Managed Flink | service execution role da aplicação |
| EC2/EMR/Glue | instance profile / job role |
