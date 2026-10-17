---
domain: terraform
description: Terraform agnóstico de nuvem — state remoto, layout de módulos, variáveis/secrets, ciclo init→validate→plan→apply com acordo e teardown; o específico de cada nuvem fica na KB role iac-provider
mcp_validated: null
confidence: null
---

# KB: Terraform (núcleo agnóstico)

Núcleo **sem provider**. Tudo que depende da nuvem (autenticação, backend de state, recursos
base) mora na KB com `role: iac-provider` do provider resolvido no Passo 0
(ver KB `cloud-resolution`). Agente principal: `iac-engineer`.

## Capability map

| Pergunta | Onde achar |
|---|---|
| Por que state remoto e como travar? | [concepts/state.md](concepts/state.md) |
| Como organizar pastas, módulos e ambientes? | [concepts/layout-and-modules.md](concepts/layout-and-modules.md) |
| Onde ficam variáveis e secrets? | [concepts/variables-and-secrets.md](concepts/variables-and-secrets.md) |
| Ciclo plan/apply com acordo humano | [patterns/plan-apply-with-agreement.md](patterns/plan-apply-with-agreement.md) |
| Teardown para não queimar crédito | [patterns/teardown.md](patterns/teardown.md) |
| Cheatsheet de comandos | [quick-reference.md](quick-reference.md) |

## Learning path

1. Passo 0 (`cloud-resolution`) → abrir a KB `role: iac-provider` do provider
2. `concepts/state.md` + `remote-state.md` da KB do provider
3. `concepts/layout-and-modules.md` → `concepts/variables-and-secrets.md`
4. `patterns/plan-apply-with-agreement.md` → `patterns/teardown.md`

## Guardrails (valem para todo provider)

- `apply` e `destroy` **só com acordo explícito** do usuário, depois de mostrar o `plan`.
  O `agent-policies` do harness pode pedir confirmação ou bloquear o comando.
- Nunca versionar `*.tfstate`, `*.tfvars` com segredo, nem `.terraform/`.
- Sempre `terraform fmt -check` e `terraform validate` antes do `plan`.
- Conta free tier/crédito: todo recurso com custo por hora tem plano de teardown
  (`patterns/teardown.md`) antes de ser criado.

## Skills relacionadas

Skills de Terraform vêm do skills.sh (ex.: guia de estilo e testes de módulos da HashiCorp),
instaladas pela categoria `cloud_core` do `install-harness`.
