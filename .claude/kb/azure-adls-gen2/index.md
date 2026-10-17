---
domain: azure-adls-gen2
description: Azure Data Lake Storage Gen2 como object storage do lake — Storage Account com namespace hierárquico (HNS), RBAC Storage Blob Data Contributor + ACL POSIX, acesso por Service Principal/Managed Identity via abfss, layout de zonas bronze/silver/gold
mcp_validated: "2026-10-16"
confidence: 0.8
---

# KB: Azure Data Lake Storage Gen2

ADLS Gen2 = **Storage Account StorageV2 com `is_hns_enabled = true`**. Mesmo serviço do
Blob Storage, com diretórios reais (rename/delete atômico de pasta) e ACLs POSIX.

## Papel

`role: object-storage` — data lake do projeto: zonas bronze/silver/gold, destino de
Event Hubs Capture/Kafka Connect, origem do `COPY INTO` do warehouse e do reference data
do Stream Analytics. Acesso sempre por **identidade de serviço** (SP ou Managed
Identity), nunca por account key.

## Capability map

| Pergunta | Onde achar |
|---|---|
| O que o HNS muda; RBAC vs ACL; URIs `abfss://` | [concepts/hns-rbac-acl.md](concepts/hns-rbac-acl.md) |
| Layout de containers/zonas e convenção de path | [concepts/zone-layout.md](concepts/zone-layout.md) |
| SP/MI com permissão mínima + Spark/Terraform | [patterns/service-identity-access.md](patterns/service-identity-access.md) |
| Cheatsheet | [quick-reference.md](quick-reference.md) |

## Custo e free tier

- Conta nova: crédito de avaliação **US$ 200 / 30 dias**; serviços de 12 meses grátis
  incluem uma cota de storage — limites exatos por SKU **a validar** no portal (grade
  "free services" da assinatura).
- Fora do crédito, lake de lab custa **centavos**: storage Hot LRS por GB-mês +
  transações (operações de escrita/listagem). HNS não tem sobretaxa de capacidade, mas
  operações de metadados são cobradas — **a validar** na página de preço.
- O que encarece: **GRS/RA-GRS** (use **LRS** em lab), milhões de arquivos pequenos
  (transações), tier **Archive** com reidratação, versionamento/soft delete acumulando.
- Não existe "pausar" storage — custo é por dado guardado. Teardown: `terraform destroy`
  do RG (apaga dados — confirmar antes, ver `seguranca.md`).
- Regra: **criar → testar → destruir no mesmo dia**; dado que precisa sobreviver vai para
  outra conta/RG fora do destroy.

## SI

- Identidade: **Service Principal** (Spark/Databricks/Kafka Connect fora do Azure) ou
  **Managed Identity** (Synapse, Stream Analytics, Event Hubs Capture).
- Permissão mínima: `Storage Blob Data Contributor` **no container** (não na conta,
  não na assinatura); leitura pura → `Storage Blob Data Reader`. `Owner` de dados só
  para quem precisa setar ACL.
- `shared_access_key_enabled = false` e `allow_nested_items_to_be_public = false`;
  TLS 1.2 mínimo.
- Client secret de SP: Key Vault / secret do CI; nunca em `core-site.xml`/notebook
  versionado. Preferir federated credential/MI quando o runtime suportar.
- Zona bronze pode ter PII → acesso restrito; silver/gold com PII mascarada ou
  pseudonimizada.
- Placeholders: `<STORAGE_ACCOUNT>`, `<TENANT_ID>`, `<CLIENT_ID>`, `<SUBSCRIPTION_ID>`.

## Por que este serviço

| Alternativa | Por que não (aqui) |
|---|---|
| Blob Storage sem HNS | Sem diretório real (rename = copiar N blobs), sem ACL POSIX; Spark/Hadoop sofrem com commit |
| Microsoft Fabric OneLake | Acoplado a capacidade Fabric; fora do escopo |
| Azure Files / NetApp | Compartilhamento SMB/NFS, não lake analítico |
| Premium BlockBlobStorage com HNS | Latência menor, custo maior; desnecessário em lab |

## Learning path

1. `concepts/hns-rbac-acl.md`
2. `concepts/zone-layout.md`
3. `patterns/service-identity-access.md`

## Quick Reference

Ver [quick-reference.md](quick-reference.md).
