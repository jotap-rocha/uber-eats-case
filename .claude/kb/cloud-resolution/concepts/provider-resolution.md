---
domain: cloud-resolution
topic: provider-resolution
---

# Passo 0 — resolver o provider

## Ordem de precedência (pare na primeira que responder)

1. **Declaração explícita** — linha `cloud:` no `CLAUDE.md` do projeto:
   ```
   cloud: azure        # ou aws | gcp | multi
   ```
   É a fonte de verdade. `multi` = o projeto usa mais de uma nuvem → resolva por tarefa
   (pergunte qual nuvem a tarefa atual toca, se não estiver claro no pedido).
2. **Infraestrutura como código** — blocos `provider "<nome>"` em `*.tf` na raiz,
   `infra/`, `terraform/` ou `iac/` (tabela abaixo).
3. **Dependências** — prefixos de SDK em `pyproject.toml` / `requirements.txt` /
   `package.json` (tabela abaixo).
4. **Perguntar ao usuário** — se nada acima responder ou se houver conflito
   (ex.: `.tf` de um provider e dependências de outro).

## Tabela de sinais → provider

Esta tabela é o **único** lugar onde nome de provider vira sinal. Agentes e skills consultam
aqui; nunca a copiam. Mesma regra usada pelo `install-harness` (`detect_clouds`).

| Provider (`cloud:`) | Provider Terraform | Prefixos de dependência |
|---|---|---|
| `azure` | `azurerm`, `azuread` | `azure-` (Python), `@azure/` (npm) |
| `aws` | `aws` | `boto3`, `aws-`, `@aws-sdk/` |
| `gcp` | `google`, `google-beta` | `google-cloud-`, `@google-cloud/` |

Provider novo = linha nova aqui + KBs `{provider}-*` + categoria `cloud_{provider}` no
`stack_map.json`. Nenhum agente ou skill muda.

Nunca "chute" a nuvem por gosto ou por popularidade.

## Depois de resolver

- Registre a resposta no `CLAUDE.md` (`cloud: <valor>`) se ela veio dos passos 2–4 e o
  usuário confirmou — assim o próximo agente não refaz o Passo 0.
- O mesmo campo é lido pelo `install-harness` para decidir quais KBs de provider propagar.

## Anti-padrões

| Anti-padrão | Por quê |
|---|---|
| Agente com "se Azure faça X, se AWS faça Y" | Vira 3 agentes num só; quebra quando entra provider novo |
| Skill com pasta `references/<provider>.md` | Duplica o que a KB de serviço já tem |
| Inferir provider só pelo nome do repositório | Não é sinal confiável |
