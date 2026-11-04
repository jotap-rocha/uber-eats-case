# 007 — Estoque por ficha técnica e movimentos, com gerador híbrido

**Status:** Aceita; fronteira do gerador (decisão 3 e adendo) revista pela [ADR 009](009-simulador-cria-a-compra-numa-transacao.md)  
**Data:** 2026-11-02  
**Autores:** time

---

## Contexto

O modelo conceitual aprovado (PR #15) tinha o **Estoque 1:1 com o Produto**, alterado só por "eventos do restaurante" e
**não a cada venda** (RN-37 original). Durante o modelo lógico, o usuário trouxe dois requisitos que contradizem isso:

1. **Baixa na produção.** Quando o restaurante começa a preparar, o estoque é abatido. O que se estoca **varia por produto**:
   o produto pronto (refrigerante em lata), um pré-pronto (feijão cozido) ou os insumos de uma receita (frango, arroz, batata).
2. **Reposição no intervalo.** Restaurantes não repõem durante o serviço, e sim antes de abrir e entre os períodos de
   funcionamento (por exemplo, almoço e jantar).

Isso exige saber o **saldo corrente** por item para aceitar ou rejeitar um atendimento. Uma pesquisa na documentação oficial
do ShadowTraffic (2026-11-02, somente leitura) mostrou:

| Necessidade | ShadowTraffic |
|---|---|
| Reposição por horário do dia | **Nativo** (`intervals` com cron). A doc não diz o fuso do cron; Brasília é UTC-3 fixo, então se escreve em UTC. |
| N movimentos por atendimento (um por linha da ficha) | Contornável e frágil (cadeia de geradores com `fork` + `lookup` por `name`) |
| Baixa só quando o atendimento entra em "em preparo" | Contornável e arriscado (sem exclusão mútua entre geradores que atualizam o mesmo atendimento) |
| Saldo por item, lido por outro gerador | **Não suportado.** Estado não é compartilhado entre geradores e some a cada restart (o loop reinicia a cada ~2 h) |

Fontes: <https://docs.shadowtraffic.io/functions/lookup/>, <https://docs.shadowtraffic.io/functions/intervals/>,
<https://docs.shadowtraffic.io/functions/customFunction/>, <https://docs.shadowtraffic.io/fork/key/>.

## Decisão

1. **Regras.** A RN-37 é revisada e entram as RN-38 a RN-41 em
   [`01-regras-de-negocio.md`](../../shared/docs/modelagem/01-regras-de-negocio.md): ficha técnica para todo produto, baixa ao
   entrar em "em preparo", verificação no aceite com rejeição "sem estoque", saldo disponível descontando o comprometido,
   reposição só fora das janelas, 1 ou 2 janelas de funcionamento por dia.
2. **Modelo.** O Estoque vira **Item de Estoque** (do restaurante, com unidade) e entram **Ficha Técnica** (produto × item ×
   quantidade), **Movimento de Estoque** (baixa por atendimento ou reposição) e **Janela de Funcionamento** (do perfil).
   Produto pronto é só um caso: ficha com uma linha apontando para ele mesmo como item de estoque.
3. **Gerador híbrido.**
   - O **ShadowTraffic** continua com cadastros, catálogo, criação de checkout, pedido, itens e atendimentos até
     **"em análise"**, além de MinIO, MongoDB e eventos.
   - Um **simulador de restaurante** próprio (Python) assume o atendimento **a partir do aceite**: verifica saldo, aceita ou
     rejeita, grava as baixas em transação ao entrar em "em preparo", avança o ciclo e faz a reposição nas janelas, em
     `America/Sao_Paulo`. Idempotência por chave única (atendimento, item de estoque) na baixa.
   - **Fronteira:** depois de "em análise", só o simulador escreve no atendimento. O ShadowTraffic não emite mais `UPDATE`
     nele, para as duas peças não se sobrescreverem.

## Alternativas consideradas

- **A. Só ShadowTraffic.** Descartada: sem saldo real, a rejeição "sem estoque" viraria sorteio e o saldo poderia ficar
  negativo; baixa e status podem divergir; estado perdido a cada restart.
- **B. Gerador próprio inteiro.** Descartada por agora: resolve tudo e tira a dependência da licença, mas reimplementa o que o
  ShadowTraffic já entrega (≈30 lookups, MinIO, MongoDB, GPS). Fica como evolução se a licença virar obstáculo recorrente.
- **C. Estoque 1:1 com o produto, só com movimentos.** Descartada: não representa produtos feitos de insumos.

## Consequências

- O conceitual passa de 30 para **33 entidades**; o diagrama 2.1 muda.
- O lógico troca `inventory` por itens de estoque, ficha técnica e movimentos, e o perfil no MongoDB ganha janelas.
- Uma peça nova para operar: o simulador precisa de testes (`pytest`, `ruff`), de um jeito de ligar e desligar e de uma skill
  própria, ao lado das skills do ShadowTraffic.
- O Debezium captura as escritas do simulador como as de qualquer outra aplicação; o contrato da Bronze não muda.
- O estado do estoque fica no banco, então o restart do ShadowTraffic não o perde.

## Riscos

- Fronteira mal respeitada (ShadowTraffic ainda atualizando atendimento depois de "em análise") gera sobrescrita. Mitigação:
  retirar do template toda transição posterior a "em análise".
- Atraso do simulador acumula atendimentos em análise; a RN-28 (rejeição automática após 5 minutos) passa a depender dele.

## Adendo (2026-11-02, revisão da L1b do modelo lógico)

O simulador deixa de ser só "de restaurante" e passa a ser o **simulador de operação**. Além do atendimento a partir de
"em análise", ele assume:

- **Turno:** abre e fecha (INSERT e UPDATE em `shifts`).
- **Atribuição de motorista:** atribui quando o primeiro atendimento fica pronto (RN-06), libera e reatribui (RN-07, RN-31),
  sempre dentro de turno aberto (RN-36) e da cidade do pedido (RN-35).
- **Entrega:** todo UPDATE em `deliveries` (status, prazo prometido, finalização ou falha) e o status do pedido daí em diante.
- **Ações do cliente e da plataforma** que concorrem com o restaurante: cancelamento do cliente (inclusive em análise),
  rejeição automática por prazo e confirmação automática.

Motivo: a atribuição depende do "pronto", que já é do simulador, e do turno aberto. Com isso a fronteira fica simples: nas
tabelas de operação o ShadowTraffic **só faz INSERT** (pedido, atendimentos, itens, entrega e a primeira linha das
transições), e todo UPDATE é do simulador. Os arquivos `kafka/shift` e `kafka/route` do MinIO deixam de ser a fonte de
turno e entrega (decisão 13 da L1b).

## Gatilhos de revisão

- Licença do ShadowTraffic deixar de ser renovável ou ficar cara → reavaliar a alternativa B.
- Necessidade de ajuste, descarte ou perda de estoque → novos tipos de movimento (hoje fora da v1, RN-40).
