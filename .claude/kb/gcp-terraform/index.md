---
domain: gcp-terraform
description: Terraform no GCP — providers google/google-beta, auth (ADC no dev, Workload Identity Federation no CI, nunca chave JSON versionada), state remoto em GCS com lock nativo e habilitação de APIs via google_project_service
mcp_validated: "2026-10-16"
confidence: 0.85
---

# KB: GCP Terraform (provider `google`)

Só o **específico do provider GCP**. Terraform genérico (módulos, workspaces, fmt/validate)
fica fora desta KB. Paridade de papel com o `azurerm` do levantamento Azure.

## Papel

`role: iac-provider` — autentica a ferramenta de IaC no GCP, guarda o state remoto (bucket GCS
com lock nativo) e habilita as APIs/recursos base do projeto antes dos serviços de dados
(`gcp-bigquery`, `gcp-managed-kafka`, `gcp-gcs`, `gcp-dataflow`).

## Capability map

| Pergunta | Onde achar |
|---|---|
| `google` vs `google-beta`, versão, pinning? | [concepts/providers.md](concepts/providers.md) |
| ADC, impersonation, WIF — qual usar onde? | [concepts/auth-chain.md](concepts/auth-chain.md) |
| Por que o `apply` falha com "API not enabled"? | [concepts/project-apis.md](concepts/project-apis.md) |
| Bloco `provider` + login dev + CI com WIF | [patterns/provider-auth.md](patterns/provider-auth.md) |
| Backend GCS com lock e versioning | [patterns/remote-state.md](patterns/remote-state.md) |
| Cheatsheet | [quick-reference.md](quick-reference.md) |

## Learning path

1. `concepts/auth-chain.md` — sem auth correta nada funciona
2. `patterns/provider-auth.md` — `gcloud auth application-default login` + provider
3. `patterns/remote-state.md` — bucket de state **antes** do primeiro `apply` compartilhado
4. `concepts/project-apis.md` — `google_project_service` para cada serviço usado
5. `concepts/providers.md` — quando o recurso exige `google-beta`

## Custo e free tier

- **Terraform e o provider são grátis.** O custo vem dos recursos que o `apply` cria.
- **Conta nova:** crédito Free Trial de **US$ 300 por 90 dias** (sem cobrança durante o trial;
  ao fim do crédito/prazo a conta trial fecha e os recursos param — 30 dias de graça para
  upgrade). Valores verificados em 2026-10-16 em `cloud.google.com/free`.
- **Always Free relevante aqui:** bucket de state cabe folgado nos 5 GB-mês de Cloud Storage
  regional (só regiões US: `us-central1`, `us-east1`, `us-west1`).
- **O que queima crédito rápido** (criado via Terraform): Managed Kafka (cobrado por
  vCPU/RAM-hora, mesmo ocioso) e Dataflow streaming (24/7). Ver `## Custo` de cada KB.
- **Budgets e alertas:** crie um budget no billing account (`google_billing_budget` ou
  `gcloud billing budgets create`) com alertas em 50/90/100%. Budget **só alerta, não para**
  recursos — o teardown continua sendo manual.
- **Parar/limitar/destruir:** `terraform destroy` (ou `-target` no recurso caro). Labels
  `env = "lab"` e `ttl = "<data>"` em todo recurso para achar o que sobrou.
- **Regra:** criar → testar → destruir **no mesmo dia**. O bucket de state pode ficar
  (custo ~zero); clusters e jobs não.

## SI

- **Nunca** chave JSON de service account no repo, em `terraform.tfvars` ou em variável de CI.
  Dev: `gcloud auth application-default login` (+ impersonation). CI: **Workload Identity
  Federation** (token OIDC curto, sem chave).
- SA do Terraform com papéis mínimos por serviço; `roles/owner` só em lab descartável.
- State contém atributos sensíveis em texto claro → bucket privado, UBLA, versioning,
  acesso só para a SA do Terraform e admins.
- Placeholders: `<GCP_PROJECT_ID>`, `<REGION>`, `<BUCKET>`, `<SA_EMAIL>`,
  `<WIF_PROVIDER>`, `<PROJECT_NUMBER>`.

## Por que este serviço

| Alternativa (GCP) | Por que não como padrão |
|---|---|
| `gcloud` em scripts | Imperativo, sem plano/diff nem state; ok para bootstrap pontual |
| Infrastructure Manager (Terraform gerenciado do Google) | Válido; menos portável entre nuvens e entre CI — o canônico fica no Terraform CLI |
| Config Connector (KRM no GKE) | Exige cluster GKE só para IaC — custo e complexidade |
| Deployment Manager | Legado / em descontinuação — não usar em projeto novo |

Terraform mantém paridade com `azurerm`/`aws`: mesmo fluxo `init → validate → plan → apply`.
