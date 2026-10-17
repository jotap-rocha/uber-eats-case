---
domain: gcp-gcs
topic: service-identity-access
---

# Pattern: acesso ao lake por identidade de serviço (sem segredo)

## Problema

Pipelines (Dataflow, BigQuery load, Kafka Connect, jobs em GKE/CI) precisam ler/escrever no
lake com o **menor privilégio** e sem chave versionada. Equivale ao "Storage Blob Data
Contributor via Service Principal" do ADLS Gen2 — trocando o segredo do SP por SA + ADC.

## Solução

1. Uma **SA por pipeline** (não a SA default do Compute).
2. Papel **no bucket** da zona, não no projeto.
3. Runtime roda **como** a SA (anexada, Workload Identity no GKE, WIF no CI).
4. Bucket com UBLA + PAP `enforced`.

## 1. Terraform

```hcl
resource "google_service_account" "pipeline" {
  account_id   = "pipeline-ingest"
  display_name = "Pipeline de ingestão (lab)"
}

locals {
  sa = "serviceAccount:${google_service_account.pipeline.email}"
}

# lê ref, escreve curated (reescreve partição), lê/escreve tmp
resource "google_storage_bucket_iam_member" "ref_read" {
  bucket = "<BUCKET>-ref"
  role   = "roles/storage.objectViewer"
  member = local.sa
}

resource "google_storage_bucket_iam_member" "curated_rw" {
  bucket = "<BUCKET>-curated"
  role   = "roles/storage.objectUser"
  member = local.sa
}

resource "google_storage_bucket_iam_member" "tmp_rw" {
  bucket = "<BUCKET>-tmp"
  role   = "roles/storage.objectUser"
  member = local.sa
}
```

`_iam_member` é **aditivo** (não remove outros bindings). `_iam_binding`/`_iam_policy` são
autoritativos — usar só se o Terraform for dono de todo o IAM do bucket.

## 2. Runtime por contexto

**Dataflow / VM / Cloud Run** — anexar a SA:

```bash
gcloud dataflow flex-template run <JOB> ... --service-account-email=<SA_EMAIL>
gcloud run jobs deploy <JOB> ... --service-account=<SA_EMAIL>
```

Quem lança precisa de `roles/iam.serviceAccountUser` **na SA**.

**GKE (Workload Identity Federation for GKE)** — KSA impersona a SA:

```bash
gcloud iam service-accounts add-iam-policy-binding <SA_EMAIL> \
  --role="roles/iam.workloadIdentityUser" \
  --member="serviceAccount:<GCP_PROJECT_ID>.svc.id.goog[<NAMESPACE>/<KSA>]"
kubectl annotate serviceaccount <KSA> -n <NAMESPACE> \
  iam.gke.io/gcp-service-account=<SA_EMAIL>
```

(Alternativa sem SA intermediária: conceder o papel do bucket direto ao principal
`principal://iam.googleapis.com/projects/<PROJECT_NUMBER>/locations/global/workloadIdentityPools/<GCP_PROJECT_ID>.svc.id.goog/subject/ns/<NAMESPACE>/sa/<KSA>`.)

**CI externo** — WIF (ver `gcp-terraform/patterns/provider-auth.md`); o job age como a SA.

**Dev** — `gcloud auth application-default login` + impersonation:

```bash
gcloud storage ls gs://<BUCKET>-curated --impersonate-service-account=<SA_EMAIL>
```

## 3. Código (sem credencial)

```python
from google.cloud import storage

client = storage.Client()            # ADC: SA anexada / WIF / login do dev
bucket = client.bucket("<BUCKET>-curated")
bucket.blob("vendas/pedidos/dt=2026-10-16/part-000.parquet").upload_from_filename("part-000.parquet")
```

Nome do bucket vem de config/env, nunca hardcoded com ID real.

## 4. Verificação

```bash
# o que a SA pode no bucket
gcloud storage buckets get-iam-policy gs://<BUCKET>-curated \
  --flatten="bindings[].members" --filter="bindings.members:<SA_EMAIL>" \
  --format="value(bindings.role)"
# negação esperada: SA de ingestão não lê o bucket raw de outro domínio
gcloud storage ls gs://<OUTRO_BUCKET> --impersonate-service-account=<SA_EMAIL>   # 403
```

Policy Troubleshooter / Policy Analyzer confirmam acesso efetivo.

## Anti-patterns

- `roles/storage.admin` ou `objectAdmin` no projeto para a SA do pipeline.
- Usar a SA default do Compute (`<PROJECT_NUMBER>-compute@...`) com papel Editor.
- Chave JSON em variável de ambiente do container "porque é mais fácil".
- HMAC key para cliente que já suporta ADC.
- `allAuthenticatedUsers` (= qualquer conta Google, não "minha empresa").
