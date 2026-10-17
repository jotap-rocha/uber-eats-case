---
domain: terraform
topic: layout-and-modules
---

# Layout de pastas e módulos

## Layout padrão do harness

```text
infra/
├── bootstrap/            # cria o armazenamento do state (state local) — roda 1x
├── modules/              # módulos reutilizáveis, sem provider/backend próprios
│   ├── warehouse/
│   ├── streaming/
│   └── object-storage/
└── envs/
    └── dev/              # root module: backend + provider + chamadas de módulo
        ├── backend.tf
        ├── providers.tf
        ├── main.tf
        ├── variables.tf
        ├── outputs.tf
        └── terraform.tfvars.example
```

- Módulos nomeados por **papel** (mesmos `role` da KB `cloud-resolution`), não por serviço:
  trocar de nuvem troca o conteúdo do módulo, não a arquitetura.
- `envs/<env>` é o único lugar com `backend` e `provider`. Módulo nunca declara backend.
- Projeto free tier normalmente tem só `envs/dev`. Não crie `prod` por simetria.

## Módulo bem-feito

| Regra | Por quê |
|---|---|
| `variables.tf` com `description` e `type` em toda variável | É a API do módulo |
| `outputs.tf` só com o que outro módulo consome | Evita acoplamento |
| `versions.tf` com `required_providers` e versão mínima | Reprodutibilidade |
| Sem valores de ambiente hardcoded (região, nomes) | Reuso entre envs |
| Tags/labels padrão (`project`, `env`, `owner`, `ttl`) | Achar e destruir o que custa |

## Versões

- Fixe a versão do Terraform (`required_version`) e dos providers (`~>` na minor).
- Commit do `.terraform.lock.hcl`: **sim** (garante o mesmo provider em toda máquina).
- Atualizar provider = PR próprio com `terraform init -upgrade` + `plan` sem mudança inesperada.

## Workspaces

Evite `terraform workspace` para separar ambientes — pastas `envs/<env>` com states
separados são mais explícitas e mais difíceis de errar.
