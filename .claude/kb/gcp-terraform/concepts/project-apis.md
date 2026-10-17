---
domain: gcp-terraform
topic: project-apis
---

# APIs do projeto (`google_project_service`)

No GCP cada serviço precisa ter a **API habilitada no projeto** antes de criar recursos.
Erro típico no `apply`: `Error 403: <X> API has not been used in project ... or it is disabled`.

## APIs por KB de serviço

| KB | API(s) |
|---|---|
| `gcp-gcs` | `storage.googleapis.com` |
| `gcp-bigquery` | `bigquery.googleapis.com` (+ `bigquerystorage.googleapis.com` para leitura rápida) |
| `gcp-managed-kafka` | `managedkafka.googleapis.com`, `compute.googleapis.com` (subnet/VPC) |
| `gcp-dataflow` | `dataflow.googleapis.com`, `compute.googleapis.com` |
| Base IaC | `serviceusage.googleapis.com`, `iam.googleapis.com`, `cloudresourcemanager.googleapis.com`, `iamcredentials.googleapis.com` (impersonation/WIF), `sts.googleapis.com` (WIF) |
| Budgets | `billingbudgets.googleapis.com` |

## Padrão

```hcl
locals {
  apis = ["storage.googleapis.com", "bigquery.googleapis.com",
          "managedkafka.googleapis.com", "dataflow.googleapis.com",
          "compute.googleapis.com", "iam.googleapis.com"]
}

resource "google_project_service" "apis" {
  for_each           = toset(local.apis)
  project            = var.project_id
  service            = each.key
  disable_on_destroy = false   # explícito; default na v7 já é não desabilitar
}
```

Recursos de serviço dependem da API:

```hcl
resource "google_bigquery_dataset" "raw" {
  dataset_id = "raw"
  location   = var.region
  depends_on = [google_project_service.apis]
}
```

## Cuidados

- `disable_on_destroy = true` desliga a API **para o projeto inteiro** no destroy —
  só faz sentido quando o Terraform também gerencia o `google_project`.
- Habilitar API não custa; o custo vem dos recursos.
- Propagação leva segundos a minutos; em erro intermitente logo após habilitar, rodar o
  `apply` de novo é aceitável.
- Service agents (ex.: `service-<PROJECT_NUMBER>@gcp-sa-managedkafka.iam.gserviceaccount.com`)
  só existem depois da API ligada; para forçar a criação use
  `google_project_service_identity` (provider `google-beta`).
