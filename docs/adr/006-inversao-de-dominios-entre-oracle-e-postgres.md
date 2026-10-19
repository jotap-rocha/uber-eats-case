# 006 — Inversão de domínios entre Oracle e Postgres (pedido e catálogo no Postgres)

**Status:** Aceita  
**Data:** 2026-10-18  
**Autores:** time

---

## Contexto

O Oracle Free tem teto de 12 GB (`ORA-12954`) e estava no limite. Isso levou ao invariante "o gerador
será congelado" para `orders`, `payments`, `drivers`, `products` e `restaurants`.

A medição direta dos bancos (consultas somente leitura, 2026-10-18) mostrou que esse invariante
descrevia o problema de forma imprecisa:

| Banco | Tabela | Espaço (tabela + índices) |
|---|---|---|
| Oracle | `ORDER_ITEMS` (~57,5 mi linhas) | ~11.741 MB |
| Oracle | `PAYMENTS` | 58 MB |
| Oracle | `ORDERS` | 17 MB |
| Oracle | `RECEIPTS`, `INVENTORY`, `PRODUCTS`, `RESTAURANTS` | ~14 MB somados |
| Oracle | **Total do schema** | **~11.830 MB** |
| Postgres | `drivers` (154.448 linhas) + `users` (32.755 linhas) | 69 MB (banco inteiro) |

Dois fatos pesaram na decisão:

- **Uma única tabela (`ORDER_ITEMS`) ocupa 99% do Oracle.** `drivers` já está no Postgres, não no Oracle,
  e `ORDERS` ocupa só 17 MB. Inverter apenas as tabelas pequenas não liberaria espaço.
- **Não existe FK física em nenhum dos dois bancos.** A integridade referencial é lógica e garantida
  pelo gerador (`lookup`, Onda 1). O gerador já referencia entidades entre bancos (por exemplo, `orders`
  busca `user_id` no Postgres e `restaurant_id` no Oracle). Mover tabelas entre bancos não perde
  nenhuma constraint física.

Havia também um requisito de modelagem: manter os domínios de negócio juntos na mesma fonte. `ORDER_ITEMS`
é filho de `ORDERS` e de `PRODUCTS`, então não pode ser movida sozinha sem separar a família.

## Decisão

1. **Domínio Pedido e catálogo vai para o Postgres:** `orders`, `order_items`, `payments`, `receipts`,
   `products`, `inventory` e `restaurants`.
2. **Domínio Pessoas vai para o Oracle:** `users` e `drivers`.
3. **MongoDB continua como satélite documental** (`perfil_restaurante`), ligado ao restaurante só por
   `restaurant_id` lógico.
4. **Ingestão:** Debezium + Kafka Connect captura os **dois** bancos relacionais (o Postgres via replicação
   lógica). Airbyte fica com **MongoDB e MinIO**.
5. **O Kappa continua lendo somente do barramento** (invariante preservado). O trilho batch consome o mesmo
   tópico por Kafka Connect Sink (captura única).
6. **O cancelamento de pedido é uma entidade nova** (evento com motivo, quem cancelou e momento), dentro do
   domínio Pedido, e não um valor de `status` de `orders`.
7. O contrato canônico de CDC na Bronze não muda. Só muda a origem do `cdc_sequence`: LSN para o domínio
   Pedido (Postgres) e SCN para o domínio Pessoas (Oracle).

## Alternativas consideradas

### Opção A — Mover só `ORDER_ITEMS` para o Postgres ❌ Rejeitada

Resolveria o teto, mas separaria o item do pedido e do produto, quebrando a coerência de domínio exigida.
Toda junção `order_items ⋈ orders ⋈ products` só existiria na Silver.

### Opção B — Inverter só as tabelas pequenas entre os bancos ❌ Rejeitada

Não libera espaço: o peso está em `ORDER_ITEMS`, que não é uma "tabela pequena".

### Opção C — Manter tudo e modelar o cancelamento no Postgres sobre o Oracle congelado ❌ Rejeitada

Mantém o teto como restrição permanente e o gerador congelado, e o cancelamento ficaria numa fonte diferente
do pedido.

### Opção D — Inversão por domínio, com Debezium nos relacionais ✅ Escolhida

Resolve a causa do teto, preserva a coerência de domínio, mantém o Kappa alimentado pelo barramento e reduz
uma ferramenta de captura (o Airbyte deixa de capturar bancos relacionais).

### Opção E — Kappa lendo da landing ❌ Rejeitada

Foi levantada como plano B e descartada: enfraqueceria a distinção entre Lakehouse e Kappa e substituiria
replay por retenção de storage. O Debezium já entrega direto ao barramento, então o plano B não é necessário.

## Consequências

### Positivas

- O teto de 12 GB deixa de ser restrição do projeto: o Oracle cai para cerca de 100 MB, e o gerador pode voltar
  a gerar.
- Cada domínio de negócio vive inteiro numa fonte só.
- Uma ferramenta de CDC para os dois bancos relacionais.

### Negativas / Tradeoffs

- O Postgres passa a guardar ~12 GB no VHDX da D: (HDD), mais o WAL de replicação lógica.
- Refaz o que existe da Fase 0: tabelas, carga, conectores e referências do gerador entre bancos.
- Troca a ferramenta de captura do Postgres (Airbyte → Debezium) e exige configurar `wal_level=logical`,
  slot e publicação.

### Riscos

- O volume de CDC de `orders` (9 `UPDATE`s por pedido) e `order_items` pode crescer o WAL e o slot de
  replicação. **A medir** antes de religar o gerador.
- O seed do MongoDB (`perfil_restaurante`) tem `RESTAURANT_COUNT = 500` fixo, e o Oracle reporta ~622
  restaurantes (por estatística, a confirmar). Há perfis a menos que restaurantes.

## Pendências (fora desta decisão)

- Procedimento de migração: **recomeçar do zero nos dois bancos relacionais** (decisão do usuário), com o
  gerador novo já incluindo o cancelamento. Os dados são sintéticos, então não há cópia dos 11,7 GB atuais.
  Cada operação destrutiva (`DROP`, `TRUNCATE`, remoção de volume) continua exigindo confirmação explícita
  no momento da execução; esta ADR não a concede.
- Modelagem do cancelamento (campos, quem cancela, estado final do pedido cancelado) e destino do estado
  `Completed`.
- Silver: SCD2 ou tabela de eventos para o histórico de transições do pedido.
- Seed do `menu`: passar a referenciar `product_id`.
- Atualizar o `CLAUDE.md`: o invariante do teto do Oracle e a seção de arquitetura por cloud, que cita o
  Airbyte para Postgres.
- Verificar se a Fase 1 (Azure), ainda não aplicada, precisa ajustar os conectores.

## Impacto em SI/LGPD

Nenhum. Todo dado do projeto é sintético (ShadowTraffic). A decisão não altera o tratamento de dados
pessoais. A migração envolve bancos tratados como produção, então qualquer operação destrutiva segue
exigindo confirmação explícita.

## Revisão

Esta ADR deve ser revisada se:

- O Debezium no Postgres não sustentar o volume de `orders`/`order_items` no disco disponível.
- O disco da D: não comportar os ~12 GB mais WAL.
- A Fase 1 (Azure), ao ser aplicada, mostrar que o desenho do trilho batch por Kafka Connect Sink exige outro
  arranjo de domínios.
