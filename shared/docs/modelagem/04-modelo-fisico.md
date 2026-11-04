# Modelo físico

Quarta etapa do fluxo (regras → adversarial → conceitual → lógico → **físico** → regeração). Parte do
[modelo lógico](03-modelo-logico.md) (L0 a L4) e das ADRs [006](../../../docs/adr/006-inversao-de-dominios-entre-oracle-e-postgres.md),
[007](../../../docs/adr/007-estoque-por-movimentos-e-gerador-hibrido.md) e [008](../../../docs/adr/008-historico-de-status-em-tabelas-de-transicao.md).
Revisão por fases. O DDL daqui é **documento**: só é aplicado na regeração, com confirmação (o Oracle atual segue tratado
como produção).

| Fase | Conteúdo | Status |
|---|---|---|
| F0 | Decisões transversais adiadas pelo lógico | aprovada |
| F1 | DDL Postgres: pedido, operação, dinheiro, pós-entrega | pendente |
| F2 | DDL Oracle: `customers`, `drivers`, `cities` | pendente |
| F3 | MongoDB (`restaurant_profiles`) e MinIO (`kafka/gps`) | pendente |
| F4 | CDC: configuração do Debezium, tópicos, contrato `cdc_*` visto da fonte | pendente |
| F5 | Plano da regeração: ordem de carga, divisão gerador × simulador, testes T1 a T18 como consultas | pendente |

---

## F0. Decisões transversais

Pendências que o lógico deixou para o físico. F0.3, F0.5 e F0.7 dependem de quem cria a compra (F0.1); as outras são
independentes.

### F0.1 Quem cria a compra

**Problema.** Hoje (ADR 007 e L1b) o ShadowTraffic insere pedido, atendimentos, itens, entrega e a linha 1 das transições
em geradores separados, **sem transação comum**, e a L2 deixou em aberto se ele também cria checkout, tentativas,
pagamento, componentes e recibo. Três problemas saem daí:

1. **Guarda do simulador.** O simulador pode pegar um atendimento cujos itens ainda não chegaram e checar estoque errado
   (L1b, risco).
2. **Dinheiro.** `payment_components` exige alocar a taxa de serviço por item com "a última parcela absorve a diferença"
   (RN-33) e decompor o imposto do bruto (RN-09). O ShadowTraffic não tem estado entre geradores (ADR 007) nem laço sobre
   os itens de um pedido: a soma dos componentes bater com `total_amount` (T8) ficaria frágil.
3. **Código de rastreio.** O ShadowTraffic não calcula SHA-256; ou se usa um trigger no Postgres ou alguém atualiza a linha
   depois.

**Proposta (recomendada): o simulador cria a compra inteira, numa transação.** Checkout, tentativas, pedido, atendimentos,
itens, entrega, linha 1 das duas tabelas de transição, pagamento, componentes e recibo nascem juntos, em Python, com
`BEGIN ... COMMIT`. O ShadowTraffic fica com o que não tem estado: cadastros (Oracle `customers`, `drivers`, `cities`;
Postgres `cities`, `restaurants`, `products`, `stock_items`, `product_recipes`), o MongoDB (`restaurant_profiles`) e o
MinIO (`kafka/gps`).

| Consequência | Efeito |
|---|---|
| Guarda (F0.5) | **Some**: não existe atendimento sem itens visível a outra transação |
| Dinheiro (F0.7) | Resolvido em Python, em `Decimal`, com a regra da RN-33 testável em `pytest` |
| Código de rastreio (F0.3) | Calculado no simulador, antes do INSERT |
| Sequências (F0.8) | **Um único dono de INSERT por tabela**; sem colisão entre gerador e simulador |
| Leitura entre bancos | O simulador passa a ler `customers` no Oracle (cidade, endereço e coordenadas copiados na compra). Não é um tipo novo de leitura: ele já lê `drivers` para abrir turno (RN-42) |
| ADR 007 | A fronteira muda ("ShadowTraffic até em análise" vira "ShadowTraffic só cadastro e eventos"). Vira **ADR 009** |
| Ritmo de compras | Passa a ser parâmetro do simulador (pedidos por minuto por cidade), não `throttleMs` do template |

**Alternativas.**

- **B. ShadowTraffic cria pedido e itens; simulador cria o dinheiro depois.** Mantém a ADR 007, mas o pagamento nasce
  depois do pedido (ordem invertida no CDC), a guarda continua necessária e o `checkout_id` tem de ser combinado entre os
  dois (faixas de id).
- **C. ShadowTraffic cria tudo, inclusive o dinheiro.** Mantém a ADR 007 inteira, mas T8 e a RN-33 dependem de `math` em
  geradores sem estado, a guarda continua necessária e o código de rastreio exige trigger.

### F0.2 Decimal no Debezium

**Problema.** Por padrão (`decimal.handling.mode=precise`) o Debezium entrega `NUMERIC`/`NUMBER` como bytes codificados
(e `NUMERIC` sem escala como struct). O conector Oracle atual usa `double`, que fere a L0 #3 (dinheiro nunca em ponto
flutuante).

**Proposta (recomendada): `decimal.handling.mode=string`** nos dois conectores. A Bronze grava o texto e declara o tipo de
destino por coluna (`DECIMAL(12,2)`, `DECIMAL(12,3)`, `DECIMAL(9,6)`, `DECIMAL(5,4)`); a conversão é exata. Alternativas:
`precise` (exato, mas exige decodificar bytes com a escala do schema) e `double` (descartada pela L0 #3).

**Achado que vai para a F2.** No conector Oracle, `NUMBER(p,0)` só vira inteiro (`int64`) com p ≤ 18; `NUMBER(19)` e
`INTEGER` (que no Oracle é `NUMBER(38)`) caem no `decimal.handling.mode` e chegariam como texto. Proposta: chaves do
Oracle em **`NUMBER(18)`** (teto de 10^18 − 1, folgado) e inteiros pequenos em `NUMBER(9)` (o `city_id` do IBGE tem 7
dígitos). Isso corrige a tradução "`bigint` → `NUMBER(19)`" da L1a e do handoff.

### F0.3 Código de rastreio

Formato fixado na L1b (decisão 12): 12 caracteres base32 Crockford do SHA-256 de `order_id` com sal; o pagamento usa o
mesmo formato com outro sal. Não pode ser coluna gerada (o Postgres 15 não a publica na replicação lógica).

**Proposta (recomendada, se F0.1 = simulador): função Python no simulador**, chamada antes do INSERT de `orders` e
`payments`. Os dois sais ficam no `.env` (`TRACKING_SALT_ORDER`, `TRACKING_SALT_PAYMENT`), fora do git; o teste de
regeração recalcula o código e confere. Alternativa: **trigger `BEFORE INSERT`** com `pgcrypto` (vale para qualquer
escritor, mas põe regra de negócio no banco e o sal vira configuração do banco). Se F0.1 ficar com o ShadowTraffic, o
trigger passa a ser a única opção viável.

### F0.4 Timestamp sem fuso no Debezium

**Correção do que o lógico supôs.** O Debezium **não desloca** o valor: `TIMESTAMP` sem fuso (Postgres e Oracle) chega
como `MicroTimestamp`, micros desde a época **lidos como se a hora do relógio fosse UTC**. O deslocamento de 3 h só
aparece se o consumidor tratar esse número como instante e converter para `America/Sao_Paulo`.

**Proposta (recomendada): nenhum transform no conector; a Bronze declara.** Todo `*_at` de negócio é **hora de Brasília
sem fuso** e vira `TIMESTAMP_NTZ` na Bronze, convertido com fuso de sessão UTC (assim o número volta a ser a hora do
relógio, sem deslocar). Já `cdc_commit_ts` (vem de `source.ts_ms`) é **instante real em UTC** e vira `TIMESTAMP`. As duas
semânticas ficam escritas no contrato da Bronze (F4). Complementos na regeração: `TZ=America/Sao_Paulo` nos contêineres
Postgres e Oracle, e a sessão do simulador com `SET TIME ZONE 'America/Sao_Paulo'`, para `now()`/`SYSTIMESTAMP` gravarem
a hora de Brasília. Alternativa: transform que converte para texto ISO no conector (mais peça para manter, sem ganho).

### F0.5 Guarda do simulador

Se F0.1 = simulador, **não há guarda**: a compra é uma transação. Se ficar com o ShadowTraffic, a guarda proposta é: o
simulador só processa atendimento com ao menos um item, com entrega já criada e com `created_at` há pelo menos N
segundos (parâmetro `intake_min_age_s`, sugestão 10). Mesmo assim não garante que **todos** os itens chegaram.

### F0.6 Leitura das janelas de funcionamento

**Proposta (recomendada): o simulador lê `restaurant_profiles` direto do MongoDB**, só leitura, com cache recarregado a
cada N minutos (parâmetro `profile_cache_refresh_min`, sugestão 15). O MongoDB é a fonte das janelas (RN-41) e é o
ShadowTraffic que as gera: uma cópia de configuração divergiria. Alternativa: copiar as janelas para o arquivo de
parâmetros (estático; quebra se o gerador mudar os perfis).

### F0.7 Dinheiro da compra

Segue F0.1. Se o simulador criar a compra, ele calcula componentes, imposto embutido e taxas em `Decimal` (nunca
`float`); o modo de arredondamento e a regra da última parcela (RN-33) ficam para a F5. Se não, ver as alternativas B e C
de F0.1.

### F0.8 Sequências e `startingFrom`

**Proposta (recomendada): um único dono de INSERT por tabela.**

| Dono | Chave | Como |
|---|---|---|
| ShadowTraffic (cadastros) | `sequentialInteger` com `startingFrom` | A skill `shadowtraffic-ajustar-geracao` recalcula o `startingFrom` a cada religada, como hoje |
| Simulador (operação, dinheiro, pós-entrega) | `bigint GENERATED BY DEFAULT AS IDENTITY` no Postgres | O banco dá o próximo valor; nada a recalcular no restart |
| Entidade fraca (chave composta) | número da linha (`line_number`, `sequence_number`, `assignment_number`, ...) | Calculado pelo dono, dentro da transação do pai ou da mudança (a chave composta é a trava da RN-27) |

Coluna identidade é coluna comum para a replicação lógica: o Debezium a publica. Com regeração do zero, as identidades
começam em 1.

### F0.9 Arquivo de parâmetros

**Proposta (recomendada): `shared/gen/parameters.yaml`**, versionado, com os parâmetros da L4 mais os novos desta fase
(ritmo de compras, `profile_cache_refresh_min`). Lido pelo simulador e pelos testes (`pytest`). O ShadowTraffic não o lê
diretamente: se algum valor precisar ir ao template, o `shared/gen/setup-configs.ps1` o injeta na renderização, como já
faz com o `.env`. Segredos (os sais de F0.3) **não** vão nele.

### Decisões da revisão da F0 (2026-11-03)

| # | Tema | Decisão |
|---|---|---|
| 1 | Quem cria a compra | **Simulador, numa transação**: checkout, tentativas, pedido, atendimentos, itens, entrega, linha 1 das transições, pagamento, componentes e recibo. O ShadowTraffic fica com cadastros, MongoDB e `kafka/gps`. Muda a fronteira da ADR 007: registrada na [ADR 009](../../../docs/adr/009-simulador-cria-a-compra-numa-transacao.md) |
| 2 | Decimal no Debezium | **`decimal.handling.mode=string`** nos dois conectores; a Bronze declara `DECIMAL(p,s)` por coluna. No Oracle, chaves em **`NUMBER(18)`** e inteiros pequenos em **`NUMBER(9)`** (corrige o "`NUMBER(19)`" da L1a) |
| 3 | Timestamp sem fuso | **Sem transform no conector.** `*_at` de negócio é hora de Brasília e vira `TIMESTAMP_NTZ` na Bronze; `cdc_commit_ts` é instante UTC. `TZ=America/Sao_Paulo` nos contêineres e na sessão do simulador |
| 4 | Código de rastreio | **Função Python no simulador**, antes do INSERT de `orders` e `payments`; sais no `.env` (`TRACKING_SALT_ORDER`, `TRACKING_SALT_PAYMENT`) |
| 5 | Guarda do simulador | **Não é necessária**: a compra é uma transação (decorre da decisão 1) |
| 6 | Janelas de funcionamento | **Leitura direta do MongoDB**, só leitura, com cache (`profile_cache_refresh_min`, sugestão 15) |
| 7 | Dinheiro da compra | **Simulador**, em `Decimal`; arredondamento e última parcela (RN-33) na F5 |
| 8 | Sequências | **Um dono de INSERT por tabela**: `sequentialInteger` + `startingFrom` nos cadastros do ShadowTraffic; `bigint GENERATED BY DEFAULT AS IDENTITY` nas tabelas do simulador; número da linha das entidades fracas calculado na transação |
| 9 | Arquivo de parâmetros | **`shared/gen/parameters.yaml`**, versionado, lido pelo simulador e pelos testes; sem segredos |
