---
domain: gcp-gcs
topic: quick-reference
---

# Cloud Storage — Quick Reference

### Criar bucket seguro (lab)

```bash
gcloud storage buckets create gs://<BUCKET> \
  --project=<GCP_PROJECT_ID> --location=<REGION> \
  --default-storage-class=STANDARD \
  --uniform-bucket-level-access --public-access-prevention \
  --soft-delete-duration=0          # lab: não reter apagados
```

### Conceder acesso a uma SA (no bucket)

```bash
gcloud storage buckets add-iam-policy-binding gs://<BUCKET> \
  --member="serviceAccount:<SA_EMAIL>" --role="roles/storage.objectViewer"
```

### Papéis

| Papel | Pode | Uso típico |
|---|---|---|
| `roles/storage.objectViewer` | ler/listar objetos | BigQuery load, Dataflow lendo ref |
| `roles/storage.objectCreator` | criar objetos (não ler/apagar) | Produtor append-only |
| `roles/storage.objectUser` | ler/criar/sobrescrever/apagar objetos | Pipeline que reescreve partição; Kafka Connect sink |
| `roles/storage.objectAdmin` | tudo em objetos (inclui ACL/retenção de objeto) | SA do Terraform no bucket de state |
| `roles/storage.admin` | bucket + objetos + IAM | Só admin/IaC |

### Zonas (prefixos)

```
gs://<BUCKET>-raw/<fonte>/<entidade>/dt=YYYY-MM-DD/
gs://<BUCKET>-curated/<dominio>/<entidade>/dt=YYYY-MM-DD/
gs://<BUCKET>-ref/<entidade>/current.json
gs://<BUCKET>-tmp/dataflow/{staging,temp}/
```

### Lifecycle (raw: apagar após 30 dias)

```json
{"rule":[{"action":{"type":"Delete"},"condition":{"age":30}}]}
```

```bash
gcloud storage buckets update gs://<BUCKET>-raw --lifecycle-file=lifecycle.json
```

### Checagens SI

```bash
gcloud storage buckets describe gs://<BUCKET> \
  --format="value(uniform_bucket_level_access,public_access_prevention)"
gcloud storage buckets get-iam-policy gs://<BUCKET>   # sem allUsers/allAuthenticatedUsers
```

### Free tier

5 GB-mês Standard só em `us-central1`/`us-east1`/`us-west1`; 5k Classe A, 50k Classe B,
100 GB egress NA/mês.

### Teardown

```bash
gcloud storage rm -r gs://<BUCKET>
```
