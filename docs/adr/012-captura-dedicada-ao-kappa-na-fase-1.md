# 012 — Captura dedicada ao Kappa na Fase 1 (Azure)

**Status:** Aceita  
**Data:** 2026-11-04  
**Autores:** time  
**Revisa:** a decisão 5 da [ADR 006](006-inversao-de-dominios-entre-oracle-e-postgres.md) ("o trilho batch consome o mesmo
tópico por Kafka Connect Sink, captura única") e o invariante revisável correspondente do `CLAUDE.md`

---

## Contexto

O desenho da Fase 1 previa uma única captura CDC por fonte, publicada no Event Hubs; o trilho batch (warehouse e
lakehouse) consumiria o mesmo tópico por um Kafka Connect Sink até o ADLS, e o Kappa leria do barramento.

Na revisão da F4 do [modelo físico](../../shared/docs/modelagem/04-modelo-fisico.md) apareceram dois limites do Event Hubs
Standard, o tier que cabe no orçamento da conta:

1. **10 event hubs por namespace.** Cada tópico Kafka vira um event hub. Com a regeração são 31 tópicos de dados (28 do
   Postgres e 3 do Oracle), mais heartbeat, histórico de schema e os 3 internos do Kafka Connect.
2. **Retenção máxima de 7 dias.** O histórico de schema do conector Oracle precisa de retenção infinita: ele é relido a
   cada restart, e o ambiente é religado a cada sessão (pausar ou destruir no fim da sessão é regra de custo).

Além disso, o Kappa resolve um problema de negócio específico e usa poucas tabelas, e o desenvolvimento das arquiteturas é
sequencial: o Kappa vem depois do warehouse e do lakehouse.

## Decisão

1. **Warehouse e lakehouse** recebem pelo **Debezium e pelo Airbyte locais**, que gravam no storage (ADLS). Não passam
   pelo Event Hubs.
2. **O Kappa tem um conector Debezium dedicado**, local, que publica no Event Hubs **só as tabelas do problema de
   negócio**, dentro do Standard (até 10 event hubs, contando os 3 internos do Connect e o heartbeat). O Kappa continua
   lendo só do barramento (invariante preservado).
3. **O conector do Kappa só é registrado quando a fase do Kappa começar.** Ele faz o snapshot inicial das suas tabelas e
   segue o log dali em diante. No Postgres usa slot próprio (`dbz_ubereats_kappa`) sobre a mesma publicação.
4. Se o Kappa capturar tabela do Oracle, o **histórico de schema fica em arquivo local** (`FileSchemaHistory`, no volume do
   contêiner do Connect), nunca num event hub.

## Alternativas consideradas

- **Captura única com roteamento por fonte** (`ByLogicalTableRouter`, um tópico `postgres` e um `oracle`). Cabe no
  Standard, mas obriga Bronze e Kappa a separar tabelas por `source.table` e mantém o histórico do Oracle preso à
  retenção do Event Hubs. Descartada.
- **Vários namespaces Standard ou o tier Premium.** Resolvem o teto, mas multiplicam o custo por hora contra o teto de
  referência da conta. Descartadas.

## Consequências

**Positivas**

- O Event Hubs fica pequeno e barato, só com o que o Kappa usa, e só existe na fase do Kappa.
- O trilho batch não depende da retenção de 7 dias do Event Hubs.

**Negativas**

- Duas capturas por fonte no Postgres (dois slots), cada uma retendo WAL enquanto estiver parada; o
  `max_slot_wal_keep_size=4GB` da F4 limita o risco.
- O caminho do Debezium local até o ADLS (sink a partir do Redpanda local) precisa ser desenhado no planejamento da Fase 1.
- Os templates em `config/azure/debezium/` e os documentos da Fase 1 seguem o desenho antigo até lá.

## Gatilhos de revisão

- O Kappa precisar de mais tabelas do que o Standard comporta.
- A conta da Fase 1 passar a comportar o Premium.

## Impacto em SI/LGPD

Nenhum. Todo dado do projeto é sintético. Nada é aplicado nos bancos atuais por esta ADR.
