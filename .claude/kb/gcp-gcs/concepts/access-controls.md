---
domain: gcp-gcs
topic: access-controls
---

# Controles de acesso

## Camadas

| Controle | O que faz | Padrão do canônico |
|---|---|---|
| **Uniform bucket-level access (UBLA)** | Desliga ACLs; acesso só por IAM (bucket/projeto) | **Ligado** em todo bucket |
| **Public access prevention (PAP)** | Impede conceder a `allUsers`/`allAuthenticatedUsers` | **`enforced`** no bucket e via org policy `storage.publicAccessPrevention` |
| IAM no bucket | Quem lê/escreve objetos | Papel mínimo, por SA |
| IAM Conditions | Restringe por prefixo/tempo | Só quando bucket por zona não basta |
| CMEK | Chave do cliente no Cloud KMS | Se exigido por compliance (custo KMS) |
| VPC Service Controls | Perímetro contra exfiltração | Produção com dado sensível |

UBLA ligado por 90 dias torna-se **irreversível**; HNS exige UBLA.

## Papéis predefinidos (objetos)

| Papel | Permissões-chave | Observação |
|---|---|---|
| `storage.objectViewer` | `objects.get`, `objects.list` | Leitor |
| `storage.objectCreator` | `objects.create` | Não lê nem sobrescreve/apaga — append-only |
| `storage.objectUser` | get/list/create/update/delete | Leitura + escrita + delete; sem gerir ACL/IAM |
| `storage.objectAdmin` | tudo em objetos, inclusive `setIamPolicy` de objeto | Mais do que pipeline precisa |
| `storage.admin` | bucket inteiro (+ IAM do bucket) | Só IaC/admin |

Sobrescrever objeto = delete + create → escritor que **reescreve** partição precisa de
`objectUser` (ou `objectCreator` + `objectViewer` não basta).

## Identidades

| Runtime | Identidade | Segredo? |
|---|---|---|
| VM, Dataflow worker, Composer, Cloud Run | Service account anexada (metadata server) | Não |
| GKE | **Workload Identity Federation for GKE** (KSA → principal IAM ou SA) | Não |
| CI externo / outra nuvem | **Workload Identity Federation** (OIDC/AWS/Azure → token) | Não |
| Dev | ADC do usuário (`gcloud auth application-default login`) | Não |
| Ferramenta só S3-compatível | HMAC key (interoperabilidade) | **Sim** — Secret Manager, rotação |
| Chave JSON de SA | — | Evitar; nunca no git |

Service agents de serviços Google (ex.: Managed Kafka Connect, BigQuery Data Transfer) são
SAs gerenciadas pelo Google — conceda papel **no bucket** a elas, nada além.

## Soft delete e versionamento

- **Soft delete** (default 7 dias) retém objetos apagados/sobrescritos e **cobra storage**
  por eles. Produção: manter; lab: `--soft-delete-duration=0`.
- **Object Versioning**: útil no bucket de state do Terraform; em zonas de dados, só com
  lifecycle `num_newer_versions`.

## Auditoria

- Admin Activity logs (IAM, criação de bucket) ficam ligados por padrão.
- Data Access logs (leitura de objeto) precisam ser habilitados — geram custo de Logging.
- Nunca logar conteúdo de objeto; nomes de objeto aparecem nos logs (mais um motivo para não
  ter PII no caminho).
