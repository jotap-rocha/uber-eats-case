---
domain: cloud-resolution
description: Contrato de roteamento multi-cloud — resolve provider (azure|aws|gcp) e papel (role) e aponta a KB de serviço certa no _index.yaml; agentes e skills de nuvem são agnósticos e se especializam só por aqui
mcp_validated: null
confidence: null
---

# KB: Cloud Resolution (roteamento multi-cloud)

KB **agnóstica**. Não ensina nenhum serviço; ensina **como achar** a KB de serviço que ensina.
Todo agente de nuvem executa o **Passo 0** daqui antes de qualquer outra coisa.

> Regra central: os agentes `cloud-data-engineer` e `iac-engineer` **nunca** citam nome de provider ou
> serviço (skills de terceiros do skills.sh podem trazer exemplos de várias nuvens).
> Toda especialização mora numa KB `{provider}-{serviço}` com `provider:` e `role:` no `_index.yaml`.

## Capability map

| Pergunta | Onde achar |
|---|---|
| Como descobrir o provider do projeto? | [concepts/provider-resolution.md](concepts/provider-resolution.md) |
| Quais papéis existem e o que cada um cobre? | [concepts/roles.md](concepts/roles.md) |
| Que seções toda KB de serviço precisa ter? | [patterns/service-kb-contract.md](patterns/service-kb-contract.md) |
| Cheatsheet do Passo 0 | [quick-reference.md](quick-reference.md) |

## Learning path

1. `concepts/provider-resolution.md` — Passo 0 (provider)
2. `concepts/roles.md` — papel → KB
3. `patterns/service-kb-contract.md` — ao criar KB nova de serviço (`kb-architect`)

## SI

- Identificadores de conta, assinatura, projeto ou tenant: **placeholders only** em artefato
  versionado (`<SUBSCRIPTION_ID>`, `<AWS_ACCOUNT_ID>`, `<GCP_PROJECT_ID>`).
- Credenciais só via login interativo da CLI, identidade gerenciada ou secret manager
  (ver KBs de cofre e skill `cloud-secrets`).
