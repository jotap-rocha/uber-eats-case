---
domain: gcp-terraform
topic: remote-state
---

# Pattern: state remoto em GCS (lock nativo)

## Problema

State local se perde, diverge entre pessoas e não tem lock. O state ainda guarda atributos
sensíveis em claro.

## Solução

Backend `gcs`: um bucket dedicado, privado, com **Object Versioning**. O backend suporta
**state locking nativo** (arquivo `.tflock` no próprio bucket) — não precisa de tabela
externa (como o DynamoDB da AWS).

## 1. Bucket de state (bootstrap — fora do state que ele guarda)

```bash
gcloud storage buckets create gs://<BUCKET> \
  --project=<GCP_PROJECT_ID> --location=<REGION> \
  --uniform-bucket-level-access --public-access-prevention
gcloud storage buckets update gs://<BUCKET> --versioning
```

Ou num diretório `bootstrap/` com state local descartável:

```hcl
resource "google_storage_bucket" "tfstate" {
  name                        = "<BUCKET>"
  location                    = var.region
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
  force_destroy               = false
  versioning { enabled = true }
  lifecycle_rule {
    condition { num_newer_versions = 10 }
    action    { type = "Delete" }
  }
}
```

## 2. Backend

```hcl
terraform {
  backend "gcs" {
    bucket = "<BUCKET>"
    prefix = "envs/lab"        # um prefix por ambiente/stack
    # impersonate_service_account = "<SA_EMAIL>"  # opcional; ou env GOOGLE_IMPERSONATE_SERVICE_ACCOUNT
  }
}
```

Backend não aceita variáveis: valores fixos ou `terraform init -backend-config=backend.hcl`
(arquivo **sem segredo**).

## 3. Permissões

| Identidade | Papel no bucket de state |
|---|---|
| SA do Terraform (dev impersonado e CI) | `roles/storage.objectAdmin` |
| Demais | nenhum |

```hcl
resource "google_storage_bucket_iam_member" "tf_state" {
  bucket = google_storage_bucket.tfstate.name
  role   = "roles/storage.objectAdmin"
  member = "serviceAccount:<SA_EMAIL>"
}
```

## Operação

- Lock preso (job morto): `terraform force-unlock <LOCK_ID>` **só** com certeza de que não há
  outro apply rodando.
- Recuperar state: `gcloud storage ls -a gs://<BUCKET>/envs/lab/` e copiar a geração anterior.
- Migrar de local: adicionar o bloco e `terraform init -migrate-state`.

## Custo

Arquivos de state são KB — cabem nos 5 GB-mês do Always Free (regiões US). Pode ficar entre
sessões de lab; o resto segue a regra criar → testar → destruir no mesmo dia.

## Anti-patterns

- Mesmo bucket para state e dados do lake.
- Bucket de state criado pelo mesmo state que ele armazena.
- Leitura pública/`allUsers` (o state tem segredos em claro).
- Desligar versioning "para economizar".
