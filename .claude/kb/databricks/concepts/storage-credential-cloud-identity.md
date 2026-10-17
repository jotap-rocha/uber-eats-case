---
domain: databricks
topic: storage-credential-cloud-identity
---

# Storage credential do Unity Catalog por identidade de nuvem

Para o Unity Catalog ler/gravar no **seu** object storage (tabela externa, volume, landing),
você cria uma **storage credential** (identidade de nuvem) e uma **external location**
(caminho + credential). Grants do UC controlam quem usa o quê. O tipo da identidade muda
por nuvem; o modelo é o mesmo.

```text
identidade de nuvem ──(permissão no storage)──► bucket/container
        │
storage credential (UC)  ──►  external location (URL + credential)  ──►  GRANT READ/WRITE FILES
```

## Por nuvem

| Nuvem | Identidade recomendada | Permissão no storage | Observação |
|---|---|---|---|
| Azure | **Access Connector for Azure Databricks** (managed identity) | RBAC `Storage Blob Data Contributor` na storage account (ADLS Gen2) | Service principal também é aceito, mas managed identity dispensa rotação de segredo e funciona com storage protegido por regras de rede |
| AWS | **IAM role** confiada pelo UC master role da Databricks, com `sts:ExternalId` | Policy IAM com `s3:GetObject`/`PutObject`/`ListBucket`/… no bucket | A role precisa ser **self-assuming** (confiar em si mesma); desde 2025 a Databricks bloqueia credenciais com role não self-assuming |
| GCP | **Service account gerada pela Databricks** ao criar a credential | IAM no bucket GCS (ex.: `roles/storage.objectAdmin` ou leitura) para essa service account | Você não cria chave; só concede papel à SA mostrada pelo UC — **a validar** detalhes de papel mínimo |

## Fluxo (igual nas três)

1. Criar a identidade na nuvem (Terraform via `iac-engineer`; detalhe de permissão na KB
   `role: object-storage` do provider, `patterns/service-identity-access.md`).
2. No workspace, com privilégio `CREATE STORAGE CREDENTIAL` no metastore:
   ```bash
   databricks storage-credentials create --json @cred.json   # tipo por nuvem
   ```
   Azure: `{"name": "<CRED>", "azure_managed_identity": {"access_connector_id": "<ACCESS_CONNECTOR_RESOURCE_ID>"}}`.
   AWS: credential com `aws_iam_role.role_arn` → copie o **external ID** gerado e atualize o
   trust policy da role (ARN do UC master role: copie da documentação oficial da Databricks).
3. Validar a credential (Catalog Explorer → *Validate configuration*).
4. External location + grants:
   ```sql
   CREATE EXTERNAL LOCATION landing_loc
     URL '<SCHEME>://<BUCKET_OU_CONTAINER>/landing'
     WITH (CREDENTIAL <CRED>);
   GRANT READ FILES, WRITE FILES ON EXTERNAL LOCATION landing_loc TO `<GRUPO>`;
   ```
5. Opcional: marcar a credential como read-only e vinculá-la só aos workspaces que precisam.

## Free Edition — **a validar**

A Databricks Free Edition é serverless e roda na conta da própria Databricks. **Não está
confirmado** na documentação consultada (2026-10-16) se ela permite criar storage
credential/external location apontando para storage da sua conta de nuvem. Antes de
planejar a arquitetura em cima disso, teste no workspace Free Edition; se não houver
suporte, use volumes gerenciados do UC e ingestão via upload/API.

## SI

- Placeholders para IDs: `<ACCESS_CONNECTOR_RESOURCE_ID>`, `<AWS_ACCOUNT_ID>`,
  `<GCP_PROJECT_ID>`, `<CRED>`. Nunca ID real versionado.
- Sem chave estática: managed identity / role assumida / SA gerenciada pela Databricks.
- Grants no UC por **grupo**, não por usuário; registre em código (ver
  `concepts/unity-catalog-fs-grants-lineage.md`).
