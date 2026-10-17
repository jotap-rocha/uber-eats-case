---
domain: gcp-gcs
description: Cloud Storage como data lake GCP — layout de zonas, uniform bucket-level access, public access prevention, IAM mínimo (objectViewer/objectCreator/objectUser/objectAdmin), acesso por service account, Workload Identity (GKE) e WIF; free tier e soft delete
mcp_validated: "2026-10-16"
confidence: 0.8
---

# KB: Cloud Storage (object storage / lake GCP)

Paridade com `azure-adls-gen2` (namespace, Storage Blob Data Contributor, acesso por Service
Principal). No GCP: bucket + prefixos, papéis `roles/storage.object*` e **service account**
(com Workload Identity/WIF no lugar de segredo de SP).

## Papel

`role: object-storage` — lake em zonas (`raw` → `curated` → `ref`), origem de carga do
`gcp-bigquery`, destino do sink do `gcp-managed-kafka`, reference data e staging/temp do
`gcp-dataflow`.

## Capability map

| Pergunta | Onde achar |
|---|---|
| Como organizar zonas, buckets e prefixos? | [concepts/lake-layout.md](concepts/lake-layout.md) |
| UBLA, PAP, papéis IAM, HNS, soft delete? | [concepts/access-controls.md](concepts/access-controls.md) |
| SA de pipeline com permissão mínima (+ GKE/CI) | [patterns/service-identity-access.md](patterns/service-identity-access.md) |
| Cheatsheet | [quick-reference.md](quick-reference.md) |

## Learning path

1. `concepts/lake-layout.md`
2. `concepts/access-controls.md` — UBLA + PAP **sempre** ligados
3. `patterns/service-identity-access.md`

## Custo e free tier

- **Always Free:** 5 GB-mês de storage **Standard regional só em `us-central1`, `us-east1`,
  `us-west1`** (somados), 5.000 operações Classe A e 50.000 Classe B por mês, 100 GB de
  egress a partir da América do Norte. Fora dessas regiões, cobra desde o 1º byte.
- **Conta nova:** Free Trial de **US$ 300 / 90 dias** (verificado 2026-10-16).
- **O que queima crédito:** egress entre regiões/internet, muitas operações (milhões de
  arquivos pequenos = muitas Classe A), classes Nearline/Coldline/Archive com **mínimo de
  retenção** e taxa de leitura, versionamento sem lifecycle, **soft delete** (retém objetos
  apagados — default de 7 dias — e cobra por eles).
- **Limitar:** lifecycle (`Delete` por idade em `raw`/`tmp`), bucket na **mesma região** do
  BigQuery/Kafka/Dataflow, compactar arquivos pequenos.
- **Destruir:** `gcloud storage rm -r gs://<BUCKET>` ou `terraform destroy` com
  `force_destroy = true` (só em lab). Em lab, soft delete com retenção 0 para não pagar
  objetos apagados.
- **Budgets:** budget + alertas 50/90/100% (só alerta).
- **Regra:** criar → testar → destruir no mesmo dia (exceção: bucket de state do Terraform).

## SI

- **Uniform bucket-level access (UBLA) ligado** → só IAM, sem ACL por objeto.
- **Public access prevention = enforced** em todo bucket (de preferência via org policy).
- Pipeline acessa como **service account** (VM/Dataflow/Composer/Cloud Run) ou Workload
  Identity (GKE) / WIF (CI externo). **Sem chave JSON, sem HMAC key** versionada.
- Papel mínimo no **bucket**, não no projeto: leitor `objectViewer`, escritor append
  `objectCreator`, read/write/delete `objectUser`; `objectAdmin` só para quem gerencia ACL/
  retenção (ex.: SA do Terraform no bucket de state).
- PII no lake: bucket/prefixo próprio, CMEK se exigido, nunca PII em **nome de objeto/prefixo**
  (aparece em logs e listagens).
- Placeholders: `<GCP_PROJECT_ID>`, `<REGION>`, `<BUCKET>`, `<SA_EMAIL>`.

## Por que este serviço

| Alternativa (GCP) | Por que não como lake |
|---|---|
| Filestore (NFS) | File share caro por TB provisionado; não é API de lake |
| Persistent Disk | Bloco atado a VM; não compartilhável pelos serviços gerenciados |
| HDFS em Dataproc | Dados morrem com o cluster; custo de VM ligada |
| Storage do próprio BigQuery | Serve ao warehouse; o lake bruto fica no GCS para todos os motores |

GCS é o único object storage nativo do GCP — a escolha aqui é de **configuração** (UBLA, PAP,
região, classe, lifecycle, HNS opcional), não de serviço.
