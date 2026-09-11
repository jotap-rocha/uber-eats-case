# BRAINSTORM: Arquitetura de Ingestão — Fase 2 (AWS)

| Campo | Valor |
|-------|-------|
| **Feature** | INGESTAO_AWS_FASE2 |
| **Fase do roadmap** | Fase 2 — AWS (`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`) |
| **Depende de** | Fase 0 (4 sistemas de origem: Postgres, Oracle, MongoDB, MinIO — `BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md`), Fase 1/Azure (padrão de referência: dois trilhos separados) |
| **Status** | ✅ Brainstorm concluído |
| **Data** | 2026-09-10 |

---

## Ideia inicial

O roadmap já registrava a Fase 2 (AWS) como **🔶 sob avaliação**, com achados preliminares soltos (DMS como ferramenta única cobrindo Postgres+Oracle+MongoDB, mas com uma pendência real não resolvida: Kinesis não fala protocolo Kafka, então a notificação nativa de bucket do MinIO não consegue publicar direto nele). O usuário trouxe uma proposta concreta de desenho —

```
MongoDB -> DMS -> S3
MinIO -> AWS Data Sync -> S3
Postgres -> DMS -> S3
Oracle -> DMS -> S3
Redshift: Consome do S3
Glue e Athena: Consomem do S3
Kinesis: Consome do MinIO direto e S3
```

— e pediu ajuda para fechar a decisão. O brainstorm resolveu a pendência do Kinesis/MinIO, decidiu o papel do S3 como landing do Warehouse/Lakehouse, e definiu o desenho do Kappa (trilho real-time) para as 4 fontes.

---

## Decisões de escopo

| # | Decisão | Resposta |
|---|---------|----------|
| 1 | Como o MinIO alimenta o Kinesis, já que Kinesis não fala Kafka e a notificação nativa de bucket do MinIO só publica em Kafka/AMQP/NATS/Webhook? | **Webhook nativo do MinIO + Lambda ponte → `PutRecord` no Kinesis.** MSK (Kafka gerenciado) foi cogitado e descartado — teria brokers sempre ligados, contrariando o princípio já fixado no roadmap de priorizar serverless/on-demand |
| 2 | Redshift recebe CDC direto do DMS (target nativo) ou só lê do S3? | **Só lê do S3** (`COPY`/`MERGE`), mesmo padrão já validado na Fase 1 (Synapse fazendo `COPY INTO` do ADLS Gen2). Um único pipeline de ingestão batch alimenta Warehouse e Lakehouse ao mesmo tempo, em vez de manter 2 configurações de target no DMS |
| 3 | O Kappa da AWS deve replicar a lógica de "dois trilhos separados" da Fase 1 (real-time nunca passa pelo batch), ou pode simplificar usando o S3 como fronteira única também para o Kinesis (evento S3 → Lambda → Kinesis)? | **Replicar a Fase 1.** O usuário preferiu manter fidelidade ("quero Kappa de verdade") a economizar a leitura duplicada do log de CDC. Postgres e Oracle têm **2 tasks DMS cada** (1 → Kinesis nativo, 1 → S3) |
| 4 | O MongoDB (satélite estático "Perfil de Restaurante", sem sink de escrita — decisão já fechada na Onda 3) entra no trilho real-time (Kinesis)? | **Não fisicamente, mas é consumido pelo Kappa.** Sem mutação, sem CDC — continua só com a task DMS de full load/snapshot para o S3 (decisão #4 original mantida: não ganha task nova nem entra no Kinesis). Mas o **consumidor do Kappa** (Flink/Lambda) faz **lookup/enriquecimento** direto na cópia do MongoDB já aterrissada no S3 pelo trilho batch — ex.: ao processar um evento de Pedido vindo do Kinesis, o consumidor busca menu/horário do restaurante nessa referência. Não precisa de uma 2ª cópia do dado nem de um caminho de ingestão dedicado; o S3/Bronze já atualizado pelo trilho batch basta como tabela de referência |
| 5 | O MinIO consegue ser lido pelo DMS (evitando precisar de uma 2ª ferramenta, o DataSync)? | **Não.** DMS é uma ferramenta de replicação de banco de dados (motores relacionais/NoSQL suportados) — não tem conector para object storage genérico. A opção "S3 como source" do DMS serve para migrar dados já formatados como tabela externa dentro de um bucket S3 nativo da AWS, não para copiar objetos de um endpoint S3-compatível externo (como o MinIO, self-hosted). **AWS DataSync** é a ferramenta correta: tem um tipo de location "Self-managed object storage" desenhado exatamente para isso |
| 6 | Existe restrição de orçamento/free-tier específica a registrar? | Conta AWS só será aberta quando a fase começar; sem limites financeiros por serviço mensurados hoje. Fica valendo o princípio já existente no roadmap (Seção 2: priorizar serverless/on-demand) — o próprio desenho já favorece isso ao preferir Kinesis on-demand + Lambda em vez de MSK |

---

## Abordagens exploradas

### Abordagem A — Dois trilhos separados, fiel à Fase 1 ⭐ Escolhida

**O que faz:** replica exatamente o princípio da Fase 1/Azure — real-time (Kappa) e batch (Warehouse/Lakehouse) nunca compartilham o mesmo caminho de dados, mesmo que isso signifique ler o log de CDC da mesma fonte duas vezes.

- Postgres/Oracle: 2 tasks DMS cada (1 → Kinesis nativo, ongoing replication; 1 → S3, ongoing replication)
- MongoDB: 1 task DMS (full load/snapshot → S3, sem CDC)
- MinIO: 2 caminhos independentes — notificação de bucket (Webhook) → Lambda → Kinesis (real-time); AWS DataSync → S3 (batch, agendado)

**Por que escolhida:** o usuário priorizou fidelidade ao padrão já estabelecido e um Kappa que seja "de verdade" (streaming orientado a evento, não micro-lote via S3) sobre a economia de infraestrutura. Mantém a Fase 2 comparável à Fase 1 no critério mais importante do projeto — cada arquitetura (Warehouse/Lakehouse/Kappa) precisa continuar sendo genuinamente o que promete ser, não uma Lambda architecture disfarçada.

### Abordagem B — Kinesis como hub único (rejeitada)

**O que faz:** uma única leitura de CDC por fonte relacional, com o DMS apontando para o Kinesis; o S3 (Bronze) seria alimentado a partir do próprio Kinesis via Firehose, em vez de receber uma segunda leitura direta do DMS.

**Por que rejeitada:** tecnicamente mais barata (1 leitura de log em vez de 2) e mais alinhada ao conceito puro de Kappa (stream como fonte de verdade, batch materializado a partir dele). Mas o usuário preferiu a Abordagem A para manter o Kappa da AWS no mesmo padrão de rigor já aplicado na Fase 1.

### Abordagem C — S3 como fronteira única, Kinesis alimentado por evento (rejeitada)

**O que faz:** DMS e DataSync escrevem só no S3; um evento `ObjectCreated` do S3 dispara uma Lambda que empurra o registro para o Kinesis, cobrindo tanto CDC relacional quanto MinIO com o mesmo mecanismo de ponte.

**Por que rejeitada:** mais simples e mais barata, mas o Kappa vira "near-real-time por micro-lote" (herda o intervalo de entrega do DMS ao S3 antes mesmo de disparar o evento) — o usuário explicitamente não quis abrir mão da fidelidade do Kappa por essa simplificação.

**Nota:** o mecanismo Webhook/evento → Lambda → Kinesis da Abordagem A (escolhida) para o MinIO é tecnicamente o mesmo padrão de "ponte" cogitado aqui — a diferença é que ele dispara direto na notificação de escrita do objeto (MinIO), não num evento posterior do S3 já after um hop de DMS.

---

## Desenho consolidado

```
REAL-TIME (Kappa)
Postgres ──DMS (ongoing replication/CDC, task dedicada)──▶ Kinesis Data Streams ──▶ Kappa (Flink/Lambda)
Oracle   ──DMS (ongoing replication/CDC, task dedicada)──▶ Kinesis Data Streams ──▶ Kappa (Flink/Lambda)
MinIO    ──notificação de bucket (Webhook)──▶ Lambda ponte──▶ Kinesis Data Streams ──▶ Kappa (Flink/Lambda)

BATCH (Warehouse + Lakehouse)
Postgres ──DMS (2ª task, ongoing replication/CDC)──▶ S3 (Bronze) ──▶ Redshift (COPY/MERGE) + Glue/Athena (Iceberg)
Oracle   ──DMS (2ª task, ongoing replication/CDC)──▶ S3 (Bronze) ──▶ Redshift (COPY/MERGE) + Glue/Athena (Iceberg)
MongoDB  ──DMS (task única, full load/snapshot)────▶ S3 (Bronze) ──▶ Redshift (COPY/MERGE) + Glue/Athena (Iceberg)
MinIO    ──AWS DataSync (sync agendado)────────────▶ S3 (Bronze) ──▶ Redshift (COPY/MERGE) + Glue/Athena (Iceberg)
```

**Consumidores:**
- **Redshift Serverless (Warehouse):** `COPY`/`MERGE` a partir do S3 — mesmo padrão da Fase 1 (Synapse `COPY INTO` do ADLS Gen2).
- **Glue + Iceberg + Athena (Lakehouse):** leem o mesmo S3 (Bronze), sem pipeline de ingestão próprio.
- **Kinesis + Flink/Lambda (Kappa):** eventos entram só via Kinesis, alimentado por CDC nativo (Postgres/Oracle) e pela ponte de evento do MinIO — nunca via S3, para não descaracterizar o Kappa como batch disfarçado. O **consumidor** (Flink ou Lambda), no entanto, pode fazer **lookup/enriquecimento** contra o MongoDB — lendo a cópia já aterrissada no S3/Bronze pelo trilho batch (AWS DMS, full load) — sem que isso signifique o MongoDB entrar pelo Kinesis. É enriquecimento no processamento do stream, não uma 2ª fonte de eventos.

---

## Escopo desta feature

| Item | Ação |
|------|------|
| DMS — Postgres | 2 tasks: 1 ongoing replication → Kinesis (real-time), 1 ongoing replication → S3 (batch) |
| DMS — Oracle | 2 tasks: 1 ongoing replication → Kinesis (real-time), 1 ongoing replication → S3 (batch) |
| DMS — MongoDB | 1 task: full load/snapshot → S3 (sem CDC, fonte estática) |
| AWS DataSync — MinIO | Location "Self-managed object storage" apontando para o MinIO; destino S3 (Bronze), sync agendado |
| Ponte real-time MinIO | Notificação de bucket nativa do MinIO (destino Webhook) → Lambda → `PutRecord`/`PutRecords` no Kinesis Data Streams |
| Redshift Serverless | `COPY`/`MERGE` a partir do S3 (Bronze) — sem target DMS nativo |
| Glue + Iceberg + Athena | Leitura direta do mesmo S3 (Bronze) |
| Kinesis Data Streams | Modo on-demand (serverless) — target único do trilho real-time, consumido pelo Kappa (Flink ou Lambda) |
| Lookup/enriquecimento MongoDB no Kappa | O consumidor do Kappa (Flink/Lambda) lê a cópia do MongoDB já aterrissada no S3/Bronze (via DMS full load) como tabela de referência, para enriquecer eventos de Pedido/Restaurante em processamento — sem MongoDB entrar pelo Kinesis |
| Contrato canônico de CDC | Reaproveitar o mesmo princípio já definido na Onda 3 (`cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`) — mapear os metadados de ordenação do DMS (não documentado ainda) para o `cdc_sequence` canônico |

## Fora de escopo

| Item | Por que fica para depois |
|------|-----------------------------|
| MSK (Kafka gerenciado) | Descartado — contraria o princípio de priorizar serverless/on-demand (brokers sempre ligados, custo mesmo ocioso) |
| CDC/mutação real para MongoDB | Fonte estática por decisão já fechada na Onda 3 — não é escopo desta feature reabrir isso |
| Detalhamento fino do mapeamento de metadados de ordenação DMS → `cdc_sequence` | Pendência transversal já registrada no roadmap (Seção 2) — fica para o `/define` desta feature |
| Escolha do motor relacional nativo AWS (equivalente a Oracle/MinIO fora da Fase 0) | Já registrado no roadmap como decisão do `/define` desta fase, não deste brainstorm de ingestão |
| Dimensionamento de shards do Kinesis, configuração de Flink vs. Lambda no consumo do Kappa | Detalhe de implementação, não de arquitetura de ingestão — fica para o `/define`/`/design` |

## YAGNI aplicado

- Não usar MSK só porque "é mais parecido com o Kafka da Fase 1" — o ganho de familiaridade não paga o custo de manter brokers ligados; Kinesis + Lambda entrega o mesmo papel arquitetural (stream real-time) de forma serverless.
- Não dar ao MongoDB um caminho de CDC/Kinesis "para simetria com as outras 3 fontes" — ele é estático por decisão de projeto já fechada, um pipeline de CDC ali seria decorativo.
- Não unificar DMS+DataSync numa ferramenta só "para simplificar o desenho" — MinIO não é um banco de dados, forçar o DMS nele não funciona tecnicamente (já verificado nesta sessão).
- Não adotar a Abordagem C (S3 como fronteira única para o Kinesis) só por ser mais barata — o usuário decidiu explicitamente que fidelidade ao Kappa "de verdade" vale mais que a economia de uma leitura de log nesta fase do projeto.

---

## Draft Requirements para `/define`

1. Criar 2 tasks DMS para Postgres: ongoing replication com target Kinesis Data Streams (real-time) e ongoing replication com target S3/Bronze (batch).
2. Criar 2 tasks DMS para Oracle: mesmo padrão do Postgres (Kinesis + S3).
3. Criar 1 task DMS para MongoDB: full load/snapshot com target S3/Bronze, sem CDC.
4. Configurar AWS DataSync com location "Self-managed object storage" apontando para o MinIO, destino S3/Bronze, com agendamento definido.
5. Configurar notificação de bucket nativa do MinIO (destino Webhook) disparando uma Lambda que faz `PutRecord`/`PutRecords` no Kinesis Data Streams.
6. Provisionar Kinesis Data Streams em modo on-demand (serverless) como único target do trilho real-time.
7. Definir o consumidor do Kappa (Flink gerenciado vs. Lambda) lendo os eventos exclusivamente do Kinesis, com lookup/enriquecimento contra a cópia do MongoDB no S3/Bronze (via DMS full load) para dados de referência (menu/horário do restaurante).
8. Configurar Redshift Serverless com `COPY`/`MERGE` a partir do S3/Bronze — sem endpoint DMS nativo apontando para o Redshift.
9. Configurar Glue Catalog + tabelas Iceberg sobre o mesmo S3/Bronze, consumidas via Athena.
10. Mapear os metadados de ordenação nativos do DMS (equivalente a LSN/SCN) para o campo canônico `cdc_sequence` já definido na Onda 3, garantindo que a Silver não dependa do formato específico do DMS.
11. Documentar a decisão nesta subseção do roadmap (`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`, Fase 2), substituindo o status "🔶 sob avaliação" por decisão fechada — mesmo formato da subseção "Fase 1 — Arquitetura de Ingestão".

## Open Questions

- Formato exato dos metadados de ordenação emitidos pelo DMS (para completar o mapeamento pro `cdc_sequence` canônico) — detalhar no `/define`.
- Payload exato do Webhook de notificação do MinIO e formato esperado pela Lambda ponte antes do `PutRecord` — detalhar no `/define`.
- Escolha entre Flink gerenciado (Kinesis Data Analytics) e Lambda como consumidor do Kappa — decisão de custo/complexidade a tomar no `/define`, não teve trade-off explorado neste brainstorm.
- Mecanismo exato do lookup do consumidor contra o MongoDB no S3 (leitura direta de Parquet/CSV a cada evento vs. carregar em cache/side-table refrescada periodicamente, ex. DynamoDB) — decisão de performance a tomar no `/define`.
- Frequência de sync do AWS DataSync (MinIO → S3) — impacta a "frescura" do dado batch para Redshift/Glue/Athena; a definir no `/define`.

---

## Status: ✅ Brainstorm concluído

**Revisão:** Brainstorm conduzido nesta sessão via `/brainstorm`, resolvendo a pendência "🔶 sob avaliação" registrada em `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` (Fase 2 — AWS). Próximo passo: `/define .claude/sdd/features/BRAINSTORM_INGESTAO_AWS_FASE2.md`.
