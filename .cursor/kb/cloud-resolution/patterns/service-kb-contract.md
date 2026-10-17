---
domain: cloud-resolution
topic: service-kb-contract
---

# Contrato de toda KB de serviço de nuvem

Use ao criar ou revisar uma KB `{provider}-{serviço}` (via `kb-architect`). Testes do
canônico verificam este contrato (`tests/install_harness/test_cloud_catalog.py`).

## Nome e registro

- Pasta: `.claude/kb/{provider}-{serviço}/` (kebab-case; `provider` ∈ `azure|aws|gcp`).
- `_index.yaml`: campos `provider:` e `role:` obrigatórios; `agents:` inclui
  `cloud-data-engineer` (ou `iac-engineer` para `role: iac-provider`).
- Espelho idêntico em `.cursor/kb/`.
- Entra na categoria `cloud_{provider}` do `stack_map.json` do `install-harness`.

## Estrutura

```
{provider}-{serviço}/
├── index.md            # frontmatter domain/description + capability map + learning path
├── quick-reference.md  # ≤ 100 linhas
├── concepts/           # ≤ 150 linhas cada
└── patterns/           # ≤ 200 linhas cada
```

## Seções obrigatórias no `index.md`

| Seção | Conteúdo |
|---|---|
| `## Papel` | `role` + o que o serviço resolve nesse papel |
| `## Custo e free tier` | o que é grátis, o que consome crédito, como pausar/limitar, regra de teardown |
| `## SI` | identidade de serviço, permissão mínima, placeholders |
| `## Por que este serviço` | alternativas no mesmo provider e por que não foram escolhidas |

A skill de controle de custo e o agente `cloud-data-engineer` leem a seção
**Custo e free tier** antes de criar qualquer recurso. KB sem ela = KB incompleta.

## Patterns esperados por papel

O nome do arquivo é o mesmo nas três nuvens — assim o agente sabe o que abrir sem
conhecer o serviço.

| role | Patterns obrigatórios |
|---|---|
| `iac-provider` | `patterns/provider-auth.md`, `patterns/remote-state.md` |
| `warehouse` | `patterns/bulk-load.md`, `patterns/merge-scd2.md` |
| `streaming` | `patterns/kafka-client-auth.md`, `patterns/kafka-connect-sink.md` |
| `object-storage` | `patterns/service-identity-access.md` |
| `stream-processing` | `patterns/reference-data.md` |

## Regras de conteúdo

- Validar contra documentação oficial (Context-7 ou docs do vendor); preencher
  `mcp_validated`/`confidence` só quando houver validação de fato.
- Nada de ID real de conta, assinatura, projeto ou tenant; nada de chave.
- Riscos não testados ficam marcados como **risco a validar**, nunca como fato.
