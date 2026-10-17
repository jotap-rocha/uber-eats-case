---
domain: gcp-terraform
topic: auth-chain
---

# Cadeia de autenticação do provider

O provider (e o backend `gcs`) resolve credencial nesta ordem, parando na primeira:

1. `access_token` / `credentials` no bloco (ou `GOOGLE_OAUTH_ACCESS_TOKEN`,
   `GOOGLE_CREDENTIALS`, `GOOGLE_APPLICATION_CREDENTIALS`).
2. **Application Default Credentials (ADC)**: arquivo do `gcloud auth application-default
   login`, arquivo de configuração WIF (external account) ou metadata server (VM/Cloud Build).
3. Se `impersonate_service_account` estiver setado, a credencial acima é trocada por um token
   curto da SA alvo (exige `roles/iam.serviceAccountTokenCreator` **na SA**).

## Matriz contexto → mecanismo

| Contexto | Mecanismo | Chave de longa duração? |
|---|---|---|
| Dev (laptop) | ADC do usuário + impersonation da SA do Terraform | Não |
| CI externo (GitHub/GitLab/Azure DevOps) | Workload Identity Federation (OIDC → STS → SA) | Não |
| Cloud Build / VM no GCP | SA anexada via metadata server | Não |
| Chave JSON de SA | Último recurso, fora do git, rotação curta | **Sim** — evitar |

## Workload Identity Federation (CI)

- **Pool** + **provider OIDC** no projeto apontando para o emissor do CI
  (ex.: `https://token.actions.githubusercontent.com`).
- `attribute_condition` restringe **qual repo/branch** pode trocar token
  (ex.: `assertion.repository == "<ORG>/<REPO>"`). Sem condição = qualquer repo do emissor.
- A SA do Terraform recebe `roles/iam.workloadIdentityUser` para o principalSet do repo.
- O job do CI gera um arquivo de credencial **external_account** (sem segredo) e exporta
  `GOOGLE_APPLICATION_CREDENTIALS` para ele; o provider o lê como ADC.

## Impersonation no dev

- Você loga como você; o Terraform age como `<SA_EMAIL>` → mesmo conjunto de permissões do CI,
  sem baixar chave.
- Erro típico: `iam.serviceAccounts.getAccessToken denied` → falta TokenCreator na SA.

## Regra SI

Nenhuma chave JSON em repo, tfvars, variável de CI ou imagem. Se uma vazar: desabilitar a chave,
rotacionar, tratar como incidente (ver `rules/seguranca.md`).
