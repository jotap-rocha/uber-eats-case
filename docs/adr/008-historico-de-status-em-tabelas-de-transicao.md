# 008 — Histórico de status em tabelas de transição, não só em CDC

**Status:** Aceita  
**Data:** 2026-11-02  
**Autores:** time

---

## Contexto

A RN-18 exige que o **pedido** e o **atendimento** tenham histórico de transições de status. Na Onda 3 o histórico de
status do pedido e do pagamento havia sido **removido**, em favor de mutação de linha capturada por CDC (Debezium). O
conceitual (§5) já registrou que a RN-18 desfaz essa decisão e que isso poderia virar ADR no lógico; a L0 #8 do
[modelo lógico](../../shared/docs/modelagem/03-modelo-logico.md) adotou tabelas, e a L4 formaliza.

O problema do CDC como única fonte: ele captura o que o banco **gravou**. Se duas mudanças de status acontecem entre duas
leituras do log (ou o conector reinicia e reprocessa), a Silver só enxerga o estado final de cada captura, e o tempo em cada
status, que alimenta a Gold (espera, preparo, atraso), fica impreciso. O simulador (ADR 007) também muda status em
sequência rápida dentro de uma transação, o que agrava isso.

## Decisão

1. **Tabelas de transição.** `order_status_transitions` e `restaurant_order_status_transitions` guardam cada mudança
   (de, para, quem, motivo, instante), com chave (`id do pai`, `sequence_number`). A criação é a linha 1.
2. **Mesma transação.** Toda mudança faz `UPDATE ... WHERE status = <de>` e insere a transição com `sequence_number` =
   último + 1. A chave composta é a trava da RN-27 (vale o que foi registrado primeiro).
3. **O CDC continua capturando todas as tabelas**, inclusive as de transição, com o contrato canônico da Bronze
   (`cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`). A **Silver não deriva histórico de status do
   CDC**: lê as tabelas de transição como qualquer outra.
4. **Fora do escopo.** Incidente tem caminho linear sem reabertura e guarda o histórico em colunas de instante
   (`review_started_at`, `decided_at`), sem tabela de transições (L3, decisão 4).

## Alternativas consideradas

- **B. Só CDC, com SCD2 na Silver (`apply_changes`).** Descartada: perde estados intermediários entre capturas, não registra
  ator nem motivo (a causa do status não está na linha), e deixa a regra de negócio dependente do comportamento do conector.
- **C. As duas coisas.** Descartada: duas fontes de verdade para o mesmo fato, com risco de divergência e custo de
  reconciliação, sem ganho de precisão sobre A.

## Consequências

- **Positivas.** Tempo em cada status exato e auditável; ator e motivo registrados; a RN-27 vira restrição de banco.
- **Custo.** Duas tabelas a mais por escrita de status. O status do pedido é redundante com a derivação da RN-16
  (L0 #7): a verificação nos testes (T2 e T3 da L4) é o que impede a divergência.
- **Contrato da Bronze.** As tabelas de transição entram como fontes comuns. Decimais e timestamps sem fuso seguem as
  consequências da L0 (conversão de horário de Brasília declarada na Bronze).
- **Reversão.** Voltar ao CDC puro exigiria nova ADR que substitua esta e refaça o contrato da Bronze e a Silver.

## Impacto em SI/LGPD

Nenhum. As tabelas guardam status, ator e motivo; todo dado do projeto é sintético.
