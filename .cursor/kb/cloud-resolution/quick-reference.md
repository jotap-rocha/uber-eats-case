---
domain: cloud-resolution
topic: quick-reference
---

# Cloud Resolution — Quick Reference

## Passo 0 (copie para a cabeça, não para o agente)

```
1. provider = CLAUDE.md `cloud:`  → senão *.tf provider  → senão deps  → senão pergunte
2. role     = papel da tarefa (iac-provider | warehouse | streaming | object-storage | stream-processing)
3. kb       = _index.yaml where provider == P and role == R
              0 → "não há KB para P/R — rode kb-architect" (pare)
              1 → abrir index.md
             >1 → perguntar e registrar no CLAUDE.md
4. ler "Custo e free tier" da KB antes de criar recurso
```

## Campos no `_index.yaml`

```yaml
  aws-s3:
    provider: aws
    role: object-storage
    agents: [cloud-data-engineer]
```

## Patterns por papel (mesmo nome nas 3 nuvens)

| role | abrir |
|---|---|
| iac-provider | `provider-auth.md`, `remote-state.md` |
| warehouse | `bulk-load.md`, `merge-scd2.md` |
| streaming | `kafka-client-auth.md`, `kafka-connect-sink.md` |
| object-storage | `service-identity-access.md` |
| stream-processing | `reference-data.md` |

## Install

`install-harness` lê o mesmo `cloud:` / `*.tf` / deps (`detect_clouds`) e propaga
`cloud_core` + `cloud_{provider}`. Forçar: `--force-category cloud_aws`.
