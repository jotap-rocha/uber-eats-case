---
name: shadowtraffic-ajustar-geracao
description: Ajusta a velocidade/volume de geração de dados do ShadowTraffic (throttleMs, maxEvents em gen/unified/uber-eats.json.template) e religa o gerador (gen-unified) de forma segura, sem colidir PK e sem travar o pipeline inteiro. Use quando o pedido for "gerar mais rápido/devagar", "aumentar/diminuir volume de dados", "religar o shadowtraffic", "reiniciar gen-unified", ou qualquer restart do gerador quando as tabelas (users/drivers/orders/payments/restaurants) já têm dados de uma execução anterior. NÃO use `scripts/start-generators.ps1`/`stop-generators.ps1` diretos nesse caso — eles não recalculam startingFrom e já causaram travamento total do pipeline em produção local.
---

# ShadowTraffic — Ajustar Geração e Religar com Segurança

## Quando usar

- Mudar `throttleMs` (velocidade) ou `maxEvents` (volume) de qualquer generator em `gen/unified/uber-eats.json.template`.
- Religar `gen-unified` depois de parado, **quando as tabelas já contêm dados** de uma execução anterior.
- Qualquer pedido de "gerar mais dados", "acelerar/desacelerar o gerador", "reiniciar o ShadowTraffic".

## Por que não usar `start-generators.ps1`/`stop-generators.ps1` sozinhos

Esses scripts fazem `docker-compose stop/up` puro em `gen-unified`, sem tocar em `startingFrom`. Os campos `sequentialInteger`/`fork.key` do template são valores **fixos versionados** — o ShadowTraffic não lê o estado real do banco. Religar com um `startingFrom` desatualizado bate em PK duplicada (`ORA-00001` / `duplicate key value violates unique constraint`) e — achado não-óbvio, já reproduzido 2x — **isso trava o processo inteiro** (17 streams, CPU 99%, zero linhas novas), não só o fork específico que colidiu. Detalhe completo: `.claude/kb/shadowtraffic/patterns/restart-seguro-startingFrom.md`.

Esses dois scripts continuam válidos **apenas** logo após um ambiente 100% novo (`docker-compose down -v` + `up`, tabelas vazias) — nesse caso não há estado prévio para colidir.

## Procedimento seguro

1. **Se `gen-unified` estiver rodando**, desligue antes de editar:
   ```powershell
   .\scripts\toggle-shadowtraffic.ps1 off
   ```
2. **Edite** `gen/unified/uber-eats.json.template` — ajuste `localConfigs.throttleMs`/`localConfigs.maxEvents` do(s) generator(s) alvo.
3. **Religue** com o script seguro (não use `start-generators.ps1` aqui):
   ```powershell
   .\scripts\toggle-shadowtraffic.ps1 on
   ```
   Esse comando já faz, nesta ordem: lê o `MAX(id)`/`COUNT(*)` real de cada tabela sensível (`users`, `drivers`, `orders`, `payments`, `restaurants`), roda `gen\setup-configs.ps1` para injetar os segredos do `.env`, recalcula `startingFrom` (e `maxEvents` de `restaurants`) diretamente no `uber-eats.json` **gerado** (nunca no template), e só então sobe o container. Não é necessário rodar `gen\setup-configs.ps1` manualmente antes — o `on` já cobre isso.
4. **Confirme o estado**:
   ```powershell
   .\scripts\toggle-shadowtraffic.ps1 status
   ```

## Se o generator alvo não é nenhum dos 5 campos sensíveis

`throttleMs`/`maxEvents` de generators sem `sequentialInteger`/`fork.key` fixo (ex.: os que gravam em MinIO) podem, em tese, ser ajustados e o container religado sem risco de colisão de PK — mas use `toggle-shadowtraffic.ps1` mesmo assim por padrão: é o único caminho testado e não tem custo extra.

## Referências

- `.claude/kb/shadowtraffic/patterns/restart-seguro-startingFrom.md` — incidente completo e causa raiz
- `.claude/kb/shadowtraffic/concepts/mutacao-real-fork-statemachine.md` — semântica de `fork`/`maxForks`
- `scripts/toggle-shadowtraffic.ps1` — implementação
