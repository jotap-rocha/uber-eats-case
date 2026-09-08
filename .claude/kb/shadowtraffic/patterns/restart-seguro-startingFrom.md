# Restart seguro de `sequentialInteger`/`fork.key` — recalcular `startingFrom`

> **Purpose**: Prevenir o incidente vivido em produção local (sessão 2026-09-07) — religar `gen-unified` com `startingFrom` fixo travou o pipeline inteiro (17 streams, CPU 99%, zero linhas novas) por colisão de PK.
> **Confidence**: 1.0 — reproduzido 2x na mesma sessão, causa raiz confirmada nos logs (`ORA-00001`/`duplicate key value violates unique constraint`).

## When to Use

- Antes de qualquer `docker restart gen-unified` / `docker-compose stop` + `up -d gen-unified` **quando as tabelas já têm dados de uma execução anterior**.
- Ao editar `gen/unified/uber-eats.json.template` em qualquer campo `"_gen": "sequentialInteger"` ou `fork.key` (hoje: `users.user_id`, `drivers` fork key, `orders` fork key, `payments` fork key, `restaurants.restaurant_id`).
- Ao decidir entre `docker-compose stop`/`start` manual vs. usar `scripts/toggle-shadowtraffic.ps1`.

## O problema

Os campos `startingFrom` no template são **valores estáticos versionados**. O ShadowTraffic não lê o estado atual do banco para decidir onde continuar — ele sempre recomeça a contagem em `startingFrom` a cada novo processo. Se a tabela de destino já contém linhas com IDs iguais ou maiores, o primeiro `INSERT` desse ID bate em PK duplicada:

```text
ORA-00001: unique constraint (...) violated on table UBEREATS.ORDERS columns (ORDER_ID)
ORA-03301: (ORA-00001 details) row with column values (ORDER_ID:1) already exists

ERROR: duplicate key value violates unique constraint "users_pkey"
```

## Achado não-óbvio: uma única colisão pode travar o pipeline inteiro

A expectativa razoável seria "só aquele `fork` específico falha, os outros 299 continuam". **Não foi o que se observou**: com `startingFrom: 1` e as tabelas já tendo ~800 linhas, os ~300 forks concorrentes de `orders` colidiram todos de uma vez e o processo Java ficou preso a **99% de CPU sem gerar nenhuma linha nova por mais de 6 minutos** (confirmado via `docker top` + ausência total de novas linhas de log). Em uma segunda ocorrência, com apenas **um único ID** colidindo na fronteira exata (porque um restart anterior já tinha avançado 1 posição além do `startingFrom` calculado), o pipeline também parou por completo — não se limitou a um fork isolado.

Conclusão prática: **não existe colisão "segura" ou "pequena"** neste config. Qualquer `startingFrom` desatualizado é tratado como falha total até o próximo restart com valor correto.

## Implementation — checklist antes de religar

```text
1. Para CADA campo sequencial (users.user_id, drivers/orders/payments fork.key,
   restaurants.restaurant_id): rodar SELECT MAX(coluna) na tabela real
   (Postgres via `docker exec postgres-ubereats psql ...`,
   Oracle via `docker exec -i oracle-ubereats sqlplus -s ...`).
2. Definir startingFrom = MAX(coluna) + 1 para cada um.
3. Para `restaurants` (generator não-fork, maxEvents=500 fixo): recalcular
   também `localConfigs.maxEvents = max(1, 500 - COUNT(*) atual)`, senão o
   generator tenta recriar o total (500) a partir do novo startingFrom e
   ultrapassa a meta.
4. Regenerar gen/unified/uber-eats.json (gen/setup-configs.ps1) e só então
   `docker-compose up -d gen-unified` / `docker restart gen-unified`.
5. Nunca fazer dois restarts seguidos usando o MESMO valor calculado — o
   processo entre os dois restarts pode já ter avançado além dele (condição
   de corrida observada na prática: startingFrom calculado ficou 1 posição
   atrás do estado real porque o processo anterior ainda estava gravando
   quando o valor foi lido).
```

## Automação — não fazer isso manualmente

`scripts/toggle-shadowtraffic.ps1 on` automatiza os passos 1–4 (lê MAX real de cada tabela, edita apenas o `uber-eats.json` **gerado** — nunca o template versionado — e só depois sobe o container). Usar sempre esse script para ligar/desligar o gerador manualmente; não usar `docker-compose stop`/`start gen-unified` direto quando já existir dado gerado, exceto se `startingFrom` for recalculado à mão antes.

## See Also

- [mutacao-real-fork-statemachine](../concepts/mutacao-real-fork-statemachine.md) — semântica de `fork`/`maxForks`/`keepAlive`
- `scripts/toggle-shadowtraffic.ps1` — implementação do fix automatizado
