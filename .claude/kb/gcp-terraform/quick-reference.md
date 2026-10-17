---
domain: gcp-terraform
topic: quick-reference
---

# GCP Terraform — Quick Reference

### Login (dev)

```bash
gcloud auth login
gcloud auth application-default login            # ADC usado pelo provider e backend
gcloud config set project <GCP_PROJECT_ID>
export GOOGLE_IMPERSONATE_SERVICE_ACCOUNT=<SA_EMAIL>   # opcional, recomendado
```

### Provider mínimo

```hcl
terraform {
  required_providers {
    google      = { source = "hashicorp/google",      version = "~> 7.0" }
    google-beta = { source = "hashicorp/google-beta", version = "~> 7.0" }
  }
}
provider "google" {
  project = var.project_id
  region  = var.region
}
# provider "google-beta" idêntico (mesmo project/region/versão)
```

### Backend

```hcl
terraform {
  backend "gcs" {
    bucket = "<BUCKET>"          # pré-existente, versioning ON
    prefix = "terraform/state"
  }
}
```

### APIs

```hcl
resource "google_project_service" "svc" {
  for_each = toset(["bigquery.googleapis.com", "managedkafka.googleapis.com",
                    "dataflow.googleapis.com", "storage.googleapis.com"])
  service  = each.key
}
```

### Ciclo

| Passo | Comando |
|---|---|
| Init (backend) | `terraform init` |
| Checagem | `terraform fmt -check && terraform validate` |
| Plano | `terraform plan -out tfplan` |
| Aplicar | `terraform apply tfplan` |
| Destruir lab | `terraform destroy` |

### Auth por contexto

| Contexto | Mecanismo |
|---|---|
| Laptop | ADC (`application-default login`) + impersonation |
| GitHub Actions / Azure DevOps / GitLab | Workload Identity Federation (OIDC) |
| VM/Cloud Build no GCP | SA anexada (metadata server) |
| Chave JSON | **proibido** versionar; evitar mesmo fora do git |

### Papéis comuns da SA do Terraform

| Necessidade | Papel |
|---|---|
| State no bucket | `roles/storage.objectAdmin` (no bucket) |
| Habilitar APIs | `roles/serviceusage.serviceUsageAdmin` |
| Criar SAs/IAM | `roles/iam.serviceAccountAdmin`, `roles/resourcemanager.projectIamAdmin` |

### Custo

Terraform grátis; crédito trial US$ 300/90 dias. Budget com alerta. Criar → testar →
destruir no mesmo dia.
