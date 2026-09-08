---
name: shadowtraffic-adicionar-generator-seguro
description: Checklist para criar ou editar um generator em gen/unified/uber-eats.json.template (ShadowTraffic) sem repetir 3 classes de bug já ocorridas neste projeto — nome de campo divergente da coluna SQL real (ORA-00904), múltiplas chamadas de lookup inconsistentes entre si, e startingFrom desatualizado travando o pipeline no próximo restart. Use quando o pedido for "adicionar tabela/generator no shadowtraffic", "novo campo com lookup", "gerar dado sintético para uma nova entidade", ou revisão de PR que mexe em gen/unified/uber-eats.json.template.
---

# ShadowTraffic — Adicionar/Editar Generator com Segurança

## Quando usar

- Criar um generator novo (nova tabela Oracle/Postgres, ou novo `keyPrefix` no bucket MinIO).
- Adicionar/renomear qualquer campo em `row`, `data` ou `where` de um generator existente.
- Adicionar um campo que faz `lookup` de outro generator.
- Revisar um PR que altera `gen/unified/uber-eats.json.template`.

## Checklist (nesta ordem)

### 1. Destino é SQL com tabela já existente (DDL fixo em `sql/*.sh`)?

Se sim: **cada chave em `row`/`where` precisa ser o nome exato da coluna real** — o ShadowTraffic usa a chave do JSON literalmente como nome de coluna no `INSERT`/`UPDATE`, sem alias. Confira 1:1 contra a DDL antes de commitar. Um nome "lógico" tipo `*_key` que não existe na tabela já quebrou este projeto 2x com `ORA-00904: invalid identifier` (Onda 3, Etapa 3). `sqlHint` só muda o **tipo**, nunca o nome — não serve para corrigir isso.

→ Detalhe: `.claude/kb/shadowtraffic/patterns/nome-de-campo-igual-a-coluna-real.md`

### 2. O novo campo precisa de 2+ valores do MESMO registro referenciado?

Se sim (ex.: `lat` e `lon` do mesmo restaurante): **nunca** use `lookup` duas vezes contra o mesmo alvo — cada chamada é uma amostra independente, sem garantia de vir do mesmo registro. Use um único `lookup` guardado em `vars`/`varsOnce`, depois `var`+`path` para cada campo (valor é garantidamente consistente entre múltiplas referências ao mesmo `var`).

→ Padrão pronto: `.claude/kb/shadowtraffic/patterns/evitar-lookup-circular-e-multiplo.md`

### 3. O `lookup` que você está adicionando cria um ciclo?

Confirme que o generator alvo do `lookup` **não** depende (direta ou indiretamente) do generator atual já existir. Se depender, o par não pode ser gerado — nenhum dos dois teria por onde começar (ver decisão de remover `orders.payment_key`/`orders.rating_key` no ADR de `INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC`).

### 4. O campo novo é `sequentialInteger` ou `fork.key`?

Se sim, ele entra na lista de campos sensíveis a restart com dado pré-existente. **`scripts/toggle-shadowtraffic.ps1` hoje só recalcula `startingFrom` para 5 campos fixos: `users.user_id`, `drivers` fork key, `orders` fork key, `payments` fork key, `restaurants.restaurant_id`.** Um generator novo com `sequentialInteger`/`fork.key` **não é coberto automaticamente** — se não for adicionado à função `Sync-StartingPoints` do script, o próximo religamento desse generator específico pode reproduzir o mesmo incidente de colisão de PK e travamento total (ver `.claude/kb/shadowtraffic/patterns/restart-seguro-startingFrom.md`). Ao adicionar um campo desse tipo, atualize o script junto — não deixe para descobrir no próximo restart.

### 5. Validar antes de subir

```powershell
.\gen\setup-configs.ps1
Get-Content .\gen\unified\uber-eats.json -Raw | ConvertFrom-Json | Out-Null   # falha se o JSON for inválido
```

### 6. Testar

- Ambiente novo (`docker-compose down -v` + `up`): seguro testar com `start-generators.ps1`.
- Ambiente com dado já existente: use `.\scripts\toggle-shadowtraffic.ps1 on` (ver skill `shadowtraffic-ajustar-geracao`), nunca restart cru.

## Referências

- `.claude/kb/shadowtraffic/patterns/nome-de-campo-igual-a-coluna-real.md`
- `.claude/kb/shadowtraffic/patterns/evitar-lookup-circular-e-multiplo.md`
- `.claude/kb/shadowtraffic/patterns/restart-seguro-startingFrom.md`
- `.claude/kb/shadowtraffic/concepts/lookup-semantica-e-limites.md`
- `.claude/kb/shadowtraffic/specs/generator-targets-uber-eats.yaml` — mapa dos generators atuais
