---
domain: gcp-terraform
topic: providers
---

# Providers `google` e `google-beta`

## Dois providers, mesmo código-base

| Provider | Uso |
|---|---|
| `hashicorp/google` | APIs GA. Padrão para tudo. |
| `hashicorp/google-beta` | Campos/recursos em beta/preview (ex.: alguns campos de Managed Kafka, `google_project_service_identity`). |

- Declare **ambos** com a mesma versão e o mesmo `project`/`region`.
- No recurso beta: `provider = google-beta`. Data sources usados por ele também.
- Recurso beta pode mudar sem aviso de compatibilidade — preferir GA quando existir.

## Versão

- Linha atual: **7.x** (guia de upgrade v7 publicado). Fixe com `~> 7.0` e grave
  `.terraform.lock.hcl` no git.
- Mudança relevante na v7: `google_project_service.disable_on_destroy` **não** tem mais
  default `true` — destruir o recurso só o remove do state e deixa a API ligada.
- Upgrade de major: ler `guides/version_7_upgrade` no registry antes; rodar `plan` limpo.

## Atributos do provider que importam

| Atributo | Para quê |
|---|---|
| `project` | Projeto default (`<GCP_PROJECT_ID>`); recurso pode sobrescrever |
| `region` / `zone` | Defaults de localização |
| `impersonate_service_account` | Roda como a SA do Terraform a partir do ADC do usuário |
| `user_project_override` + `billing_project` | APIs que cobram quota no projeto do chamador |
| `default_labels` | Labels em todos os recursos que suportam (`env`, `ttl`, `owner`) |
| `credentials` | Caminho/conteúdo de chave JSON — **não usar** neste canônico |

## `default_labels` para teardown

```hcl
provider "google" {
  project = var.project_id
  region  = var.region
  default_labels = {
    env = "lab"
    ttl = "2026-10-16"
  }
}
```

Facilita achar recursos esquecidos (`gcloud asset search-all-resources --query="labels.env=lab"`).

## Anti-patterns

- Misturar versões diferentes de `google` e `google-beta`.
- Usar `google-beta` "por garantia" em tudo.
- Não versionar o lock file → CI baixa versão diferente do laptop.
