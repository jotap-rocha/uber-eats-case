---
domain: gcp-terraform
topic: provider-auth
---

# Pattern: autenticação do provider (dev + CI) sem chave

## Problema

Terraform precisa de credencial GCP no laptop e no CI sem chave JSON de service account
versionada ou guardada como secret de longa duração.

## Solução

- **Dev:** ADC do usuário + impersonation da SA do Terraform.
- **CI:** Workload Identity Federation (OIDC do CI → token curto da SA).
- O código Terraform é **o mesmo** nos dois — só muda como o ADC é obtido.

## 1. SA do Terraform + permissão de impersonation (bootstrap, uma vez)

```bash
gcloud iam service-accounts create terraform --project=<GCP_PROJECT_ID>
# quem pode impersonar (seu usuário de dev):
gcloud iam service-accounts add-iam-policy-binding <SA_EMAIL> \
  --member="user:<DEV_EMAIL>" --role="roles/iam.serviceAccountTokenCreator"
# conceda à SA só os papéis dos recursos que ela gerencia (não owner fora de lab)
```

## 2. Provider

```hcl
variable "project_id" { type = string }
variable "region"     { type = string }
variable "tf_sa"      { type = string }   # <SA_EMAIL>, via tfvars não-secreto

provider "google" {
  project                     = var.project_id
  region                      = var.region
  impersonate_service_account = var.tf_sa
}

provider "google-beta" {
  project                     = var.project_id
  region                      = var.region
  impersonate_service_account = var.tf_sa
}
```

No CI com WIF a SA já é a identidade final; deixe `tf_sa = ""`/`null` lá ou mantenha a
impersonation se o CI usa uma SA "porteira" separada.

## 3. Dev

```bash
gcloud auth application-default login
terraform init && terraform plan
```

## 4. WIF para GitHub Actions (Terraform do bootstrap)

```hcl
resource "google_iam_workload_identity_pool" "ci" {
  workload_identity_pool_id = "ci-pool"
}

resource "google_iam_workload_identity_pool_provider" "github" {
  workload_identity_pool_id          = google_iam_workload_identity_pool.ci.workload_identity_pool_id
  workload_identity_pool_provider_id = "github"
  attribute_mapping = {
    "google.subject"       = "assertion.sub"
    "attribute.repository" = "assertion.repository"
  }
  attribute_condition = "assertion.repository == \"<ORG>/<REPO>\""
  oidc { issuer_uri = "https://token.actions.githubusercontent.com" }
}

resource "google_service_account_iam_member" "ci_wif" {
  service_account_id = "projects/<GCP_PROJECT_ID>/serviceAccounts/<SA_EMAIL>"
  role               = "roles/iam.workloadIdentityUser"
  member             = "principalSet://iam.googleapis.com/${google_iam_workload_identity_pool.ci.name}/attribute.repository/<ORG>/<REPO>"
}
```

Workflow (trecho):

```yaml
permissions: { id-token: write, contents: read }
steps:
  - uses: actions/checkout@v4
  - uses: google-github-actions/auth@v2
    with:
      workload_identity_provider: <WIF_PROVIDER>   # projects/<PROJECT_NUMBER>/locations/global/workloadIdentityPools/ci-pool/providers/github
      service_account: <SA_EMAIL>
  - uses: hashicorp/setup-terraform@v3
  - run: terraform init && terraform plan
```

A action gera o arquivo `external_account` e exporta `GOOGLE_APPLICATION_CREDENTIALS`;
o provider o consome como ADC. Azure DevOps/GitLab: mesmo pool, provider OIDC do emissor
correspondente (**a validar** por emissor: claims e `issuer_uri`).

## Verificação

- `gcloud auth application-default print-access-token` retorna token (dev).
- `TF_LOG=DEBUG terraform plan` mostra a SA impersonada.
- `git grep -n '"private_key"'` vazio no repo.

## Anti-patterns

- `credentials = file("sa.json")` no provider.
- Secret de CI com JSON de chave "temporário".
- WIF sem `attribute_condition` (qualquer repo do emissor troca token).
