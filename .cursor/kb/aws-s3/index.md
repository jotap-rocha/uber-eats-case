---
domain: aws-s3
description: Amazon S3 como data lake — layout de zonas (raw/curated/...), bucket policy × IAM policy, acesso por IAM role (instance profile / role assumida), Block Public Access, Object Ownership e criptografia padrão (SSE-S3 desde 2023, SSE-KMS opcional)
mcp_validated: "2026-10-16"
confidence: 0.85
---

# KB: Amazon S3 (data lake)

Paridade com `azure-adls-gen2`: namespace/layout de zonas, permissão mínima, acesso por
identidade de serviço (lá Service Principal + "Storage Blob Data Contributor"; aqui IAM role).

## Papel

`role: object-storage` — data lake do projeto: zonas `landing/raw/curated/...`, destino
do Kafka Connect (MSK), origem do `COPY` (Redshift) e do reference data (Flink).

## Capability map

| Pergunta | Onde achar |
|---|---|
| Como organizar zonas, prefixos e partições? | [concepts/zone-layout.md](concepts/zone-layout.md) |
| Bucket policy × IAM policy, BPA, criptografia, ownership? | [concepts/access-model-and-defaults.md](concepts/access-model-and-defaults.md) |
| Acesso por identidade de serviço (role)? | [patterns/service-identity-access.md](patterns/service-identity-access.md) |
| Cheatsheet? | [quick-reference.md](quick-reference.md) |

## Custo e free tier

| Item (S3 Standard, us-east-1 — ordem de grandeza, **a validar** na página de pricing) | Valor |
|---|---|
| Armazenamento | ~US$ 0,023 / GB-mês |
| PUT/COPY/POST/LIST | ~US$ 0,005 / 1.000 requests |
| GET | ~US$ 0,0004 / 1.000 requests |
| Transferência S3 → internet | cobrada; S3 → serviço na mesma região: grátis |

- **Free tier:** S3 era "12 meses grátis" (5 GB) no modelo antigo; no modelo de **créditos
  de 2025** (US$ 100 + até US$ 100, Free plan de 6 meses) o S3 consome créditos —
  **a validar** se ainda há cota gratuita mensal para S3 na sua conta.
- **O que queima:** muitos arquivos pequenos (requests), versionamento sem lifecycle,
  NAT Gateway no caminho VPC → S3 (use **gateway endpoint S3**, grátis).
- **Limitar:** lifecycle de expiração em `landing/` e `tmp/`, `NoncurrentVersionExpiration`,
  compactação de arquivos pequenos.
- **Destruir:** bucket precisa estar vazio (`force_destroy = true` só em lab, nunca em
  bucket com dado de produção). Regra: criar → testar → destruir no mesmo dia;
  **AWS Budgets** ativo antes.

## SI

- Acesso **só por IAM role** (instance profile, task role, role de serviço do
  Redshift/MSK Connect/Flink, SSO no dev). Nada de access key de IAM user nem URL
  pré-assinada de longa duração em código.
- **Block Public Access** ligado (default em bucket novo desde abril/2023) e
  **Object Ownership = BucketOwnerEnforced** (ACLs desabilitadas).
- Criptografia: SSE-S3 é automático em todo objeto novo desde 05/01/2023; use **SSE-KMS**
  (CMK) se precisar de controle de chave/auditoria de uso.
- Bucket policy negando tráfego sem TLS (`aws:SecureTransport = false`).
- PII só em zona com acesso restrito; zonas curated com PII pseudonimizada.
- Placeholders: `<BUCKET>`, `<AWS_ACCOUNT_ID>`, `<REGION>`, `<ROLE_NAME>`.

## Por que este serviço

| Alternativa (AWS) | Por que não aqui |
|---|---|
| **S3 Tables** (buckets de tabela Iceberg) | Bom para Iceberg gerenciado; o harness precisa de arquivos brutos (raw) + COPY/Connect genéricos — avaliar depois para curated |
| S3 Express One Zone | Baixa latência, zona única, mais caro por GB; não é data lake durável |
| EFS / FSx | File system POSIX, caro para volume de lake |
| HDFS em EMR | Acoplado a cluster ligado; S3 é o padrão de lake na AWS |

## Learning path

1. `concepts/zone-layout.md`
2. `concepts/access-model-and-defaults.md`
3. `patterns/service-identity-access.md`

## Fontes validadas (2026-10-16)

- docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html (SSE-S3 desde 05/01/2023)
- Context7 `/hashicorp/terraform-provider-aws` v6.33 (recursos `aws_s3_bucket_*`)
- BPA/ownership default em bucket novo (abril/2023): conhecimento + doc S3 — reconfirmar se crítico
