# 014 — Ingestão batch pelo Airbyte e Debezium só no Kappa

**Status:** Aceita  
**Data:** 2026-11-12  
**Autores:** time  
**Revisa:** a decisão 4 da [ADR 006](006-inversao-de-dominios-entre-oracle-e-postgres.md) ("Debezium + Kafka Connect
captura os dois bancos relacionais; Airbyte fica com MongoDB e MinIO") e a decisão 1 da
[ADR 012](012-captura-dedicada-ao-kappa-na-fase-1.md) ("warehouse e lakehouse recebem pelo Debezium e pelo Airbyte
locais")

---

## Contexto

A ADR 006 pôs o Debezium nos dois bancos relacionais para ter **uma captura única** no barramento, consumida pelo
trilho batch (por Kafka Connect Sink) e pelo Kappa. A ADR 012 desfez a captura única: os limites do Event Hubs Standard
(10 event hubs por namespace, 7 dias de retenção) tiraram o batch do barramento, e o Kappa ganhou um conector Debezium
dedicado. Sobrou o Debezium alimentando warehouse e lakehouse sem o motivo original, e com um problema aberto: como
levar os eventos até o ADLS (o "carteiro", um sink do Kafka Connect para o storage).

No grill do projeto `azure-warehouse` (2026-11-11 e 2026-11-12, decisões D7, D9 e D11 de
[01-grill.md](../../.claude/projetos/azure-warehouse/01-grill.md)) apareceram os fatos que fecham a questão:

1. **Postgres:** o Airbyte tem CDC próprio por replicação lógica (slot próprio), com os metadados `_ab_cdc_*` que o
   [modelo físico](../../shared/docs/modelagem/04-modelo-fisico.md) (F4.6) já mapeia para o contrato canônico.
2. **Oracle:** as três tabelas do domínio Pessoas (`CITIES`, `CUSTOMERS`, `DRIVERS`) são pequenas e têm `UPDATED_AT`
   mantido por trigger (F2.2). O Debezium só estava ali por ser o único CDC aberto para Oracle.
3. **Kappa:** precisa do evento no barramento em segundos. O Airbyte é lote (sync de minutos) e não atende.
4. **Portfólio:** cada nuvem tem um serviço nativo de replicação (DMS na AWS, Datastream na GCP), e usá-lo conta para o
   portfólio.

## Decisão

1. **Warehouse e Lakehouse, em qualquer nuvem, ingerem por ferramenta de replicação em lote, nunca pelo Debezium.**
   Na Azure, o **Airbyte** local, gravando JSONL na landing do ADLS:
   - Postgres: CDC (replicação lógica, slot próprio do Airbyte);
   - Oracle: **sem CDC**, incremental por cursor `UPDATED_AT`;
   - sem Debezium, Redpanda nem sink no trilho batch.
2. **O Debezium fica restrito ao Kappa** (conector dedicado da ADR 012, que não muda), a confirmar no processo de cada
   Kappa.
3. **Por nuvem (revisável):** Azure usa Airbyte; AWS usa DMS; GCP usa Datastream. Se DMS ou Datastream complicarem
   demais, o Airbyte volta como opção para simplificar.
4. **O MongoDB fica fora do Warehouse** (o perfil de restaurante não responde nenhuma pergunta do fechamento
   financeiro). No Lakehouse e no Kappa, a decisão é de cada projeto.
5. O contrato canônico de CDC (`cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`) não muda; ele
   nasce na primeira camada de cada arquitetura a partir dos metadados da ferramenta (no Warehouse da Azure, na `stg`).

## Alternativas consideradas

### Opção A — Manter o Debezium no trilho batch, com sink até o ADLS ❌ Rejeitada

Exige um sink do Kafka Connect para o storage, um barramento local (Redpanda) ligado nas janelas de carga e o histórico
de schema do Oracle. Mais peças, mais memória numa máquina que já ficou sem ela, e o motivo da captura única deixou de
existir com a ADR 012.

### Opção B — Airbyte no batch, Debezium só no Kappa ✅ Escolhida

Uma ferramenta por papel: o Airbyte faz lote até o storage (o que ele faz de melhor), o Debezium faz streaming até o
barramento. Tira o "carteiro" do desenho.

### Opção C — Extrator Python leve (dlt) no lugar do Airbyte ❌ Rejeitada por ora

Proposta pelo revisor adversarial (Gemini): roda com poucas centenas de MB e grava direto no ADLS. Fica como **plano B**
se a prova local do Airbyte cair por memória mesmo depois de liberar recursos (D21 do grill). O Airbyte é ferramenta
de mercado e já está no ambiente.

## Consequências

### Positivas

- Menos peças no trilho batch: sem Redpanda, sink ou histórico de schema para warehouse e lakehouse.
- O Kappa e o batch deixam de disputar o mesmo conector: cada um tem a sua captura.
- Cada nuvem mostra o seu serviço nativo de replicação.

### Negativas / Tradeoffs

- **Oracle sem CDC:** mudanças intermediárias entre duas syncs se perdem (só a última versão chega), a vigência da
  versão é o `UPDATED_AT`, não o commit, e o conector do Airbyte não captura exclusões. O SCD2 das dimensões vindas do
  Oracle tem **granularidade por sync**. O impacto no fechamento financeiro é nulo porque os valores ficam congelados
  no pedido (RN-32).
- O Airbyte entrega *at-least-once*: a deduplicação por chave e posição do log é responsabilidade de quem consome.
- Três ferramentas de ingestão diferentes entre as nuvens (Airbyte, DMS, Datastream): mais coisa para aprender e
  documentar.

### Riscos

- **Memória local:** o `abctl` caiu com exit 137 em 2026-11-12. Mitigação: prova local obrigatória antes da conta (D21);
  plano B dlt.
- **Slot de replicação esquecido** retém WAL no Postgres e pode encher o disco. Mitigação: o slot só existe enquanto há
  sync previsto (D22).
- **Conector Oracle do Airbyte com nível de suporte baixo** (segundo a documentação do Airbyte). Coberto pela mesma prova
  local.
- O projeto `regeracao-f5` planeja o Debezium do Postgres (tasks 17 e 18), alinhado à ADR 006. O impacto desta ADR
  nessas tasks e na [ADR 013](013-snapshot-inicial-aceito-na-regeracao.md) é decisão do usuário, fora deste projeto.

## Revisão

Esta ADR deve ser revisada se:

- a prova local do Airbyte falhar e o dlt entrar no lugar;
- um Lakehouse precisar de latência que o lote não atende;
- o histórico intermediário das dimensões do Oracle virar requisito de negócio (exigiria CDC verdadeiro ou auditoria por
  trigger na origem);
- DMS ou Datastream se mostrarem inviáveis no custo ou no esforço.
