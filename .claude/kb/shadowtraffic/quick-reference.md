# ShadowTraffic — Quick Reference

> Fast lookup. Fonte: docs.shadowtraffic.io/cheatsheet/ (2026-09-07) + config real deste repo.

## O que é

Ferramenta em container (`docker run shadowtraffic/shadowtraffic`) que gera dados sintéticos a partir de **um único arquivo JSON** (`generators` + `connections`), simulando tráfego de produção. Neste repo: `gen/unified/uber-eats.json.template` → `gen/unified/uber-eats.json` (gerado com segredos, ignorado no git).

## Connections usadas neste projeto

| Connection | Kind | Uso aqui |
|---|---|---|
| `postgres` | `postgres` | `users` (estático), `drivers` (mutação real, fork+stateMachine) |
| `oracle` | `oracle` | `restaurants`, `products`, `inventory`, `orders`, `payments`, `order_items`, `receipts` |
| `minio` | `s3` (S3-compatible) | Todo o resto — pastas `kafka/*`, `mysql/*`, `mongodb/*` dentro do bucket `uber-eats` (ver nota abaixo) |

**Nota:** `mysql/menu/`, `mysql/ratings/`, `mongodb/support/`, `mongodb/recommendations/`, `kafka/*` são **prefixos de pasta dentro do bucket MinIO** (`keyPrefix`), não conexões reais a MySQL/MongoDB/Kafka dentro do ShadowTraffic. A única conexão Mongo real do projeto (`mongo-ubereats`) é alimentada por um seed JS estático (`mongo/init/01_perfil_restaurante.js`), fora do ShadowTraffic.

## Funções `_gen` mais usadas aqui

| Categoria | Funções vistas no config | Doc |
|---|---|---|
| Seleção | `lookup`, `var`, `oneOf`, `weightedOneOf`, `stateMachine`, `previousEvent` | `/functions/{lookup,var,stateMachine}/` |
| Escalar | `uuid`, `sequentialInteger`, `sequentialString`, `string`, `boolean`, `uniformDistribution`, `normalDistribution` | `/functions/` |
| Data/hora | `formatDateTime`, `now` | `/date-time-functions/` |
| Geo | `geoWander` (usado em `kafka/gps/`) | `/geo-functions/` |
| Math | `math` (fórmulas com `names`) | `/math-functions/` |

## Fork — chaves usadas

| Chave | Efeito |
|---|---|
| `key` | Identidade de cada fork (ex.: `sequentialInteger` para `driver_id`/`order_id`/`payment_id`) |
| `maxForks` | Teto de forks simultâneos |
| `keepAlive: true` | Fork permanece "vivo" para sofrer updates futuros (usado em `orders`, `payments`) |
| `stagger` | Espaçamento mínimo (ms) entre criação de novos forks |

## `localConfigs` / geração

| Chave | Efeito |
|---|---|
| `maxEvents` | Nº exato de eventos/linhas a criar, depois o generator para sozinho |
| `throttleMs` | Atraso entre eventos (menor = mais rápido) |

## Licenciamento (ver `concepts/licenciamento-e-env.md` para a discrepância)

- Trial gratuito ~30 dias com reembolso, segundo busca em shadowtraffic.io (não 100% confirmado via doc oficial estruturada — validar em https://shadowtraffic.io/pricing.html antes de decisão de orçamento).
- Variáveis reais usadas neste repo (`gen/.env.template`): `LICENSE_ID`, `LICENSE_EMAIL`, `LICENSE_ORGANIZATION`, `LICENSE_EDITION`, `LICENSE_EXPIRATION`, `LICENSE_SIGNATURE`.

## Common Pitfalls

| Don't | Do |
|---|---|
| Usar `lookup` 2x na mesma geração mirando a mesma tabela esperando o mesmo registro | Um único `lookup` em `vars`/`varsOnce` + múltiplos `var`+`path` (ver `patterns/evitar-lookup-circular-e-multiplo.md`) |
| Nomear campo em `row` como `*_key` quando a tabela SQL já existe com DDL fixo | Usar o nome exato da coluna real (ver `patterns/nome-de-campo-igual-a-coluna-real.md`) |
| Confiar em `docs/shadowtraffic/README.md` para nomes de variável de licença | Confiar em `gen/.env.template` (fonte real) |
| Desenhar `lookup` circular (A depende de B que depende de A) | Reordenar/remover campo — ver ADR em `.claude/sdd/archive/INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC/` |
| Religar `gen-unified` (`docker restart`/`stop`+`up`) com dado já existente nas tabelas | Usar `scripts/toggle-shadowtraffic.ps1 on`/`off` — recalcula `startingFrom` a partir do MAX(id) real antes de subir (ver `patterns/restart-seguro-startingFrom.md`) |

## Related Documentation

| Topic | Path |
|---|---|
| Índice completo | `index.md` |
| Mapa de geradores atual | `specs/generator-targets-uber-eats.yaml` |
| Howto humano (start/stop, .env) | `docs/shadowtraffic/README.md` |
