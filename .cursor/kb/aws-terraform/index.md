---
domain: aws-terraform
description: Provider Terraform hashicorp/aws — autenticação (SSO/profile no dev, OIDC/IAM role no CI, nunca access key versionada), state remoto em S3 com lock nativo (use_lockfile), default_tags e guard-rails de custo (AWS Budgets, destroy no mesmo dia)
mcp_validated: "2026-10-16"
confidence: 0.85
---

# KB: AWS Terraform (provider `aws`)

Só o específico do provider `hashicorp/aws` e do backend `s3`. Terraform genérico
(módulos, workspaces, HCL) não entra aqui.

## Papel

`role: iac-provider` — autentica o Terraform na conta AWS, guarda o state remoto com lock
e aplica tags/guard-rails comuns a todos os recursos de dados (S3, Redshift, MSK, Flink).

## Capability map

| Pergunta | Onde achar |
|---|---|
| Versões (Terraform/provider) e blocos base? | [concepts/provider-and-versions.md](concepts/provider-and-versions.md) |
| Ordem da cadeia de credenciais? | [concepts/credential-chain.md](concepts/credential-chain.md) |
| Como autenticar dev (SSO) e CI (OIDC)? | [patterns/provider-auth.md](patterns/provider-auth.md) |
| Backend S3 com lock (`use_lockfile`)? | [patterns/remote-state.md](patterns/remote-state.md) |
| Budget + tags + teardown? | [patterns/cost-guardrails.md](patterns/cost-guardrails.md) |
| Cheatsheet? | [quick-reference.md](quick-reference.md) |

## Custo e free tier

- **Terraform/provider:** grátis. O custo vem dos recursos criados.
- **Free Tier AWS (modelo de 2025):** conta nova recebe **US$ 100 em créditos** no
  cadastro + até **US$ 100** extras ao explorar serviços (total até US$ 200). No **Free
  plan** a conta fecha após **6 meses** ou quando os créditos acabam; não há cobrança sem
  upgrade, mas o acesso fica limitado a serviços selecionados. O **Paid plan** libera
  tudo, pay-as-you-go, e consome créditos primeiro. Há também 30+ serviços "always free"
  com limites mensais. **A validar:** se MSK Serverless, Redshift Serverless e Managed
  Flink exigem Paid plan na sua conta.
- **State em S3:** centavos/mês (objetos pequenos + requests). Lock nativo dispensa
  tabela DynamoDB (que seria custo e recurso extra).
- **Guard-rail obrigatório:** `aws_budgets_budget` com alerta (ex.: 50%/80%/100% de
  US$ 20) criado **antes** de qualquer recurso de dados — ver `cost-guardrails.md`.
- **Regra:** criar → testar → `terraform destroy` **no mesmo dia**. Recursos com cobrança
  por hora (MSK Serverless cluster-hora, Flink KPU-hora) não "dormem" sozinhos.
- `default_tags { Projeto, Ambiente, Dono, TTL }` permite filtrar custo no Cost Explorer.

## SI

- **Nunca** access key estática (`AKIA...`) em `.tf`, `.tfvars`, `.env` versionado ou
  variável de pipeline. Dev → `aws sso login` + `profile`; CI → OIDC + `assume_role_with_web_identity`.
- Role do CI com permissão mínima por stack; trust policy restrita a repo/branch.
- State contém atributos sensíveis (senhas geradas, endpoints): bucket privado, Block
  Public Access, criptografia (SSE-S3/SSE-KMS), versionamento ligado.
- Placeholders: `<AWS_ACCOUNT_ID>`, `<REGION>`, `<STATE_BUCKET>`, `<ROLE_NAME>`.

## Por que este serviço

| Alternativa (AWS) | Por que não aqui |
|---|---|
| CloudFormation / CDK | Lock-in AWS; o harness usa Terraform nas 3 nuvens (paridade com `azure-terraform`) |
| Terraform com backend local | Sem lock nem compartilhamento; perde-se o state ao trocar de máquina |
| Backend S3 + DynamoDB | **Deprecated** — lock nativo do S3 (`use_lockfile`) substitui |
| HCP Terraform (Cloud) | Opção válida, mas adiciona conta/SaaS externo; S3 basta para o escopo |

## Learning path

1. `concepts/provider-and-versions.md`
2. `concepts/credential-chain.md`
3. `patterns/provider-auth.md` → `patterns/remote-state.md` → `patterns/cost-guardrails.md`

## Fontes validadas (2026-10-16)

- developer.hashicorp.com/terraform/language/backend/s3 (`use_lockfile`, DynamoDB deprecated)
- Context7 `/hashicorp/terraform-provider-aws` v6.33 (`assume_role_with_web_identity`, `default_tags`)
- aws.amazon.com/free (modelo de créditos / Free vs Paid plan)
