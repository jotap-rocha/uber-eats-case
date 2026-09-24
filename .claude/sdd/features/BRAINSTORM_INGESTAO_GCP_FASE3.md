# BRAINSTORM: Arquitetura de Ingestão — Fase 3 (GCP)

| Campo | Valor |
|-------|-------|
| **Feature** | INGESTAO_GCP_FASE3 |
| **Fase do roadmap** | Fase 3 — GCP (`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`) |
| **Depende de** | Fase 0 (4 sistemas de origem: Postgres, Oracle, MongoDB, MinIO — `BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md`), Fase 1/Azure e Fase 2/AWS (padrão de referência: dois trilhos separados) |
| **Status** | ✅ Complete (Defined) |
| **Data** | 2026-09-11 |

---

## Ideia inicial

O roadmap já registrava a Fase 3 (GCP) como **🔶 sob avaliação**, com achados preliminares soltos (Datastream cobrindo Postgres+Oracle+MongoDB, mas sem Pub/Sub como destino nativo — pendência real não resolvida para o trilho Kappa). O usuário trouxe uma proposta concreta de desenho —

```
Oracle -> Datastream -> GCS
Postgres -> Datastream -> GCS
MinIO -> Algum data sync -> GCS
MongoDB -> Datastream -> GCS

Bigquery: Consome do GCS
Dataproc: Consome do GCS. Preciso definir qual ferramenta da Google ajuda a catalogar o lakehouse, tal qual o Unity Catalog e o AWS Glue fazem.
Pub/Sub: Consome do MinIO e do GCS. Dataflow processa o streaming
```

— e pediu ajuda para fechar a decisão, no mesmo formato usado no brainstorm da Fase 2/AWS. O brainstorm resolveu a pendência do Pub/Sub (que não é destino nativo do Datastream), identificou a ferramenta de catalogação equivalente ao Unity Catalog/Glue, resolveu a lacuna de conectividade de rede (equivalente à decisão da EC2 na AWS) e corrigiu o papel do BigQuery frente ao GCS/BigLake.

---

## Decisões de escopo

| # | Decisão | Resposta |
|---|---------|----------|
| 1 | Como a GCP alcança os 4 sistemas self-hosted da Fase 0 (Postgres, Oracle, MongoDB, MinIO) na rede, já que Datastream é *pull-based* e precisa iniciar a conexão? | **Túnel SSH reverso** (bastion GCE público + `autossh`/systemd na máquina local), não uma VM na nuvem replicando o `docker-compose.yml` (como a AWS fez com a EC2 na Fase 2). Decisão explícita do usuário: manter os containers rodando localmente, aceitando o custo operacional do túnel em troca de não duplicar a infraestrutura da Fase 0 |
| 2 | O Datastream não tem Pub/Sub como destino (só BigQuery, Cloud Storage e BigLake Iceberg) — como fechar o trilho real-time (Kappa) para Postgres/Oracle? | **Debezium Server → Pub/Sub direto** (sink nativo documentado), como uma 2ª captação de CDC independente do Datastream que alimenta o trilho batch. Única exceção deliberada à regra "só ferramenta nativa da cloud" nesta fase — mesmo princípio de "dois trilhos separados" já usado na Azure e na AWS |
| 3 | Qual ferramenta GCP cataloga/governa o lakehouse, papel que o Unity Catalog (Databricks) e o AWS Glue Catalog cobrem nas outras fases? | **Dataplex Universal Catalog** — cataloga e governa as tabelas Iceberg do BigLake sobre o GCS, fechando a simetria das 3 fases |
| 4 | O BigQuery deve consultar o Iceberg do BigLake em tempo de execução (sem cópia própria, contraste arquitetural genuíno) ou ter carga física própria, como Redshift/Synapse? | **Carga física sempre** (`LOAD`/`MERGE` a partir do GCS bruto para o storage nativo do BigQuery) — decisão do usuário, por performance, por ser decisão arquitetural própria, e por manter método igual/similar nas 3 nuvens para permitir comparação justa na Fase 4. Consulta ad-hoc direta ao dado bruto (via BigLake/Dataproc) fica reservada a engenheiro/analista, não ao consumo de cliente. Query federation/query-in-place foi cogitada e **descartada** |
| 5 | Como o MinIO (não é banco de dados — Datastream/DMS não o alcançam) chega à GCP? | **Storage Transfer Service**, fonte "S3-compatible" via agente local (outbound, sem precisar do túnel SSH), destino GCS/Bronze — equivalente direto ao AWS DataSync usado na Fase 2. Sem alternativa viável (não é uma decisão com trade-off, é a única ferramenta GCP com conector para object storage genérico self-hosted) |

---

## Achado técnico que desbloqueou/restringiu a feature

- **Assimetria de conectividade entre os dois trilhos.** O Datastream é *pull-based* (a GCP precisa iniciar a conexão até o banco) — por isso exige o túnel SSH reverso via bastion. Já o Debezium Server (trilho real-time) e a Cloud Function ponte do MinIO são *push-based* (o processo local/o MinIO conectam para fora, até a API pública do Pub/Sub ou da Cloud Function) — não precisam de nenhum túnel ou porta exposta. Essa assimetria não existia de forma tão marcada nas Fases 1/2 (Airbyte e AWS DMS também são pull-based nos dois trilhos) e é um achado específico desta fase, decorrente de se ter mantido a Fase 0 local em vez de migrá-la para uma VM na nuvem.
- **Datastream cobre as 3 fontes relacionais/documentais num único serviço** (Postgres, Oracle via LogMiner, MongoDB — GA desde set/2025, confirmado em `docs/adversarial/architectural-reply.md`), reforçando o contraste já usado no roadmap ("Datastream unifica, DMS/Debezium não" — ver v1.4).
- **Datastream não tem Pub/Sub como destino** — só BigQuery, Cloud Storage e BigLake Iceberg tables (pendência já registrada no roadmap v1.4, resolvida nesta decisão #2 com Debezium Server como via alternativa para o Kappa).
- **Datastream escreve BigLake Iceberg tables diretamente** — elimina o hop manual GCS→Dataproc que a v1.2/1.3 do roadmap assumia como necessário para materializar Iceberg. O BigQuery, porém, não lê essas tabelas Iceberg em tempo de consulta (Decisão #4) — faz `LOAD`/`MERGE` a partir dos mesmos arquivos brutos do GCS, para dentro do seu storage nativo.
- **Datastream não garante ordenação nativa** (só fornece metadados adicionais por evento) e **ignora delete em cascata e `TRUNCATE`** — riscos já sinalizados no roadmap v1.4, herdados sem solução de design nesta rodada (ficam para o `/define`, mesmo padrão de risco não resolvido em brainstorm que a AWS também carregou).

---

## Abordagens exploradas

### Abordagem A — Dois trilhos separados, fiel às Fases 1 e 2 ⭐ Escolhida

**O que faz:** replica o princípio já validado na Azure e na AWS — real-time (Kappa) e batch (Warehouse/Lakehouse) nunca compartilham o mesmo caminho de dados, mesmo que isso signifique capturar CDC da mesma fonte por duas ferramentas diferentes (Datastream para o batch, Debezium Server para o real-time).

**Por que escolhida:** mantém a Fase 3 comparável às Fases 1/2 no critério mais importante do projeto — cada arquitetura (Warehouse/Lakehouse/Kappa) continua sendo genuinamente o que promete ser. Resolve de forma limpa a lacuna real do Datastream (sem Pub/Sub nativo) sem descaracterizar o Kappa.

### Abordagem B — BigQuery consultando BigLake Iceberg em tempo de execução, sem carga física (rejeitada)

**O que faz:** BigQuery não teria storage próprio para as tabelas desta feature — consultaria os arquivos Iceberg do GCS via BigLake diretamente, mesma fonte física do Dataproc/Lakehouse.

**Por que rejeitada:** tecnicamente é um contraste arquitetural genuíno (mostra o BigQuery moderno dissolvendo a fronteira Warehouse/Lakehouse), mas o usuário priorizou performance, decisão arquitetural própria e — principalmente — **paridade de método entre as 3 nuvens** para a comparação da Fase 4. Redshift e Synapse fazem carga física; o BigQuery desta feature também vai fazer.

### Abordagem C — Abrir mão do Kappa "de verdade" nesta fase (rejeitada)

**O que faz:** usar só Datastream → GCS/BigQuery (batch) e um gatilho de notificação do GCS → Pub/Sub → Dataflow para simular tempo real, evitando introduzir o Debezium Server como ferramenta não-nativa.

**Por que rejeitada:** mesma decisão já tomada na Azure e na AWS — isso faria o Kappa herdar o intervalo de entrega do trilho batch antes de disparar o evento, virando "batch disfarçado". Fidelidade ao Kappa venceu a simplicidade, mesmo padrão de decisão das duas fases anteriores.

### Abordagem D — Migrar a Fase 0 para uma GCE VM na VPC, espelhando a EC2 da AWS (rejeitada)

**O que faz:** subir uma Compute Engine instance na VPC do projeto, rodando o mesmo `docker-compose.yml` da Fase 0, para que Datastream/Storage Transfer Service acessem por IP privado — sem precisar de túnel.

**Por que rejeitada:** o usuário preferiu manter os containers rodando localmente e resolver a conectividade só para o Datastream via túnel SSH reverso, evitando duplicar a infraestrutura da Fase 0 numa VM permanente. Trade-off aceito: mais uma peça operacional (bastion + `autossh`) em vez de uma VM maior sempre ligada.

---

## Desenho consolidado

```
REAL-TIME (Kappa)
Postgres ──Debezium Server (container novo, logical decoding)──────▶ Pub/Sub ──▶ Dataflow (consumidor)
Oracle   ──Debezium Server (mesmo processo/container, LogMiner)────▶ Pub/Sub ──▶ Dataflow (consumidor)
MinIO    ──notificação de bucket (Webhook)──▶ Cloud Function ponte─▶ Pub/Sub ──▶ Dataflow (consumidor)

BATCH (Warehouse + Lakehouse)
Postgres ──Datastream (CDC, via bastion GCE + túnel SSH reverso)───▶ GCS (Bronze) ──▶ BigLake Iceberg tables
Oracle   ──Datastream (CDC/LogMiner, via túnel)─────────────────────▶ GCS (Bronze) ──▶ BigLake Iceberg tables
MongoDB  ──Datastream (full load/snapshot, via túnel)───────────────▶ GCS (Bronze) ──▶ BigLake Iceberg tables
MinIO    ──Storage Transfer Service (agente local, outbound)───────▶ GCS (Bronze)
```

**Consumidores:**
- **BigQuery (Warehouse):** `LOAD`/`MERGE` a partir dos mesmos arquivos brutos do GCS/Bronze — carga física para o storage nativo do BigQuery, aplicando o contrato canônico de CDC (dedup/upsert por `cdc_sequence`). Mesmo padrão operacional de Redshift (AWS, `COPY`/`MERGE` do S3) e Synapse (Azure, `COPY INTO` do ADLS Gen2 + `MERGE`).
- **Dataplex Universal Catalog + BigLake Iceberg + Dataproc (Lakehouse):** Dataplex cataloga as tabelas Iceberg materializadas sobre o mesmo GCS/Bronze; Dataproc processa/consulta essas tabelas — sem ingestão adicional, mesmo princípio de landing único compartilhado já usado na AWS (S3 alimentando Redshift + Glue/Athena) e na Azure (ADLS Gen2 alimentando Synapse + Databricks).
- **Dataflow (Kappa):** lê eventos só do Pub/Sub (nunca do GCS, para não descaracterizar o Kappa); enriquece Pedido/Restaurante com lookup na cópia do MongoDB já pousada como tabela Iceberg (mesma landing do trilho batch) via side input com refresh periódico — mesmo princípio do cache com TTL da Lambda consumidora na AWS.

---

## Escopo desta feature

| Item | Ação |
|------|------|
| Bastion de conectividade | GCE VM pública mínima + túnel SSH reverso (`autossh`/systemd) partindo da máquina local — usado só pelo Datastream (pull-based) |
| Datastream — Postgres/Oracle/MongoDB | 3 connection profiles via "Forward SSH tunnel", destino GCS (Bronze); depois materializados como tabelas Iceberg do BigLake |
| Storage Transfer Service — MinIO | Fonte "S3-compatible" via agente local (outbound), destino GCS (Bronze), agendado |
| Debezium Server (novo componente) | Container novo no `docker-compose.yml` local, capturando CDC de Postgres e Oracle, sink direto no Pub/Sub |
| Cloud Function ponte — MinIO | Recebe notificação de bucket (Webhook) do MinIO, publica no Pub/Sub — mesmo papel da Lambda ponte da AWS |
| Dataflow (consumidor Kappa) | Lê do Pub/Sub, enriquece com lookup na cópia Iceberg do MongoDB |
| BigQuery (Warehouse) | `LOAD`/`MERGE` físico a partir do GCS/Bronze, contrato canônico de CDC aplicado no `MERGE` |
| Dataplex Universal Catalog | Cataloga/governa as tabelas Iceberg do BigLake sobre o GCS — papel equivalente ao Unity Catalog/Glue |
| Dataproc | Processamento/consulta das tabelas Iceberg (papel de Lakehouse) |
| Contrato canônico de CDC (extensão) | Mapear metadados de ordenação do Datastream e do Debezium Server para `cdc_sequence`; adicionar constante `cdc_source_system` por ferramenta (`'postgres-datastream-gcp'`, `'oracle-datastream-gcp'`, `'mongo-datastream-gcp'`, `'postgres-debezium-gcp'`, `'oracle-debezium-gcp'`) |
| Reaproveitamento da Fase 0 (resolve pendência do roadmap) | Fecha para a Fase 3 a mesma decisão já tomada na Fase 2/AWS (v1.6): os sistemas self-hosted da Fase 0 são reaproveitados como fonte via ingestão de rede, em vez de recriar motores nativos GCP equivalentes |
| Atualizar `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` | Fechar a pendência "🔶 sob avaliação" da Fase 3 com o desenho decidido nesta feature — mesmo procedimento já aplicado quando o brainstorm da Fase 2/AWS foi formalizado (v1.5) |

## Fora de escopo

| Item | Por que fica para depois |
|------|-----------------------------|
| BigQuery consultando BigLake Iceberg em tempo de execução (query-in-place) | Avaliado e descartado nesta rodada (Abordagem B) — decisão do usuário por paridade de método entre as 3 nuvens |
| Motor relacional nativo GCP substituindo Oracle/MinIO | Descartado — decisão desta feature já fecha que a Fase 3 reaproveita os sistemas self-hosted da Fase 0, mesmo caminho da Fase 2/AWS |
| Mapeamento exato dos metadados de ordenação do Datastream/Debezium Server para `cdc_sequence` | Pendência transversal já registrada no roadmap (v1.4) — fica para o `/define` desta feature |
| Tratamento do delete em cascata/`TRUNCATE` ignorados pelo Datastream | Risco identificado, sem mitigação de design ainda — fica para o `/define` |
| Dimensionamento do bastion (tipo de GCE VM) e dos workers do Dataflow | Detalhe de implementação — fica para o `/define`/`/design` |
| Migrar a Fase 0 para uma GCE VM (espelhando a EC2 da AWS) | Avaliado e descartado nesta rodada (Abordagem D) — usuário optou por manter containers locais + túnel SSH |

## YAGNI aplicado

- Não duplicar a implementação do BigQuery (carga física **e** consulta em tempo de execução) só para "mostrar as duas formas" — o usuário decidiu explicitamente por uma via só (carga física), mesmo padrão nas 3 nuvens; a Abordagem B fica documentada como descartada, não como escopo extra.
- Não migrar a Fase 0 para uma VM na nuvem só para replicar a AWS "por simetria" — o túnel SSH resolve a conectividade sem duplicar infraestrutura; simetria entre clouds não é objetivo em si quando o resultado técnico é equivalente.
- Não introduzir MSK/Kafka gerenciado nem qualquer broker adicional para o Pub/Sub — Debezium Server tem sink nativo documentado para Pub/Sub, sem intermediário.
- Não resolver o mapeamento fino de metadados de ordenação (Datastream/Debezium → `cdc_sequence`) nem o tratamento de cascade delete agora — são decisões de design, não de arquitetura de ingestão; documentadas como pendência explícita, não descartadas.

---

## Draft Requirements para `/define`

1. Provisionar um bastion (GCE VM pública mínima) na VPC da Fase 3, com túnel SSH reverso (`autossh`/systemd rodando na máquina local) mantendo Postgres/Oracle/MongoDB acessíveis ao Datastream via "Forward SSH tunnel connectivity profile".
2. Criar 3 connection profiles + streams do Datastream (Postgres CDC, Oracle CDC via LogMiner, MongoDB full load/snapshot), destino GCS (Bronze), materializados como tabelas Iceberg do BigLake.
3. Configurar o Storage Transfer Service com fonte "S3-compatible" apontando para o MinIO (via agente local), destino GCS (Bronze), com agendamento definido.
4. Adicionar o Debezium Server como novo serviço no `docker-compose.yml` local, capturando CDC de Postgres (logical decoding) e Oracle (LogMiner), com sink direto no Pub/Sub.
5. Implementar a Cloud Function ponte: recebe a notificação de bucket (Webhook) do MinIO, publica no Pub/Sub.
6. Configurar o job/pipeline `LOAD`/`MERGE` do BigQuery a partir do GCS/Bronze, aplicando o contrato canônico de CDC (`cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`) para dedup/upsert.
7. Configurar o Dataplex Universal Catalog sobre as tabelas Iceberg do BigLake (GCS/Bronze), e o Dataproc para processamento/consulta dessas tabelas.
8. Implementar o pipeline Dataflow consumidor do Kappa: lê do Pub/Sub, enriquece Pedido/Restaurante com lookup na cópia Iceberg do MongoDB (side input com refresh periódico).
9. Definir e documentar o mapeamento dos metadados de ordenação nativos do Datastream e do Debezium Server para o campo canônico `cdc_sequence`.
10. Definir a política de tratamento do delete em cascata/`TRUNCATE` ignorados pelo Datastream (mitigação ou risco aceito documentado).
11. Atualizar `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` (Fase 3), fechando a pendência "🔶 sob avaliação" com o desenho decidido nesta feature — mesmo formato da subseção "Fase 2 — Arquitetura de Ingestão".

## Open Questions

- Formato exato dos metadados de ordenação emitidos pelo Datastream e pelo Debezium Server (para completar o mapeamento pro `cdc_sequence` canônico) — detalhar no `/define`.
- Tipo/tamanho do GCE VM usado como bastion, e mecanismo de resiliência do túnel `autossh` (restart automático se cair) — detalhar no `/define`.
- Frequência do job `LOAD`/`MERGE` do BigQuery e do agendamento do Storage Transfer Service (MinIO) — impacta a "frescura" do dado no Warehouse; a definir no `/define`.
- Mecanismo exato do side input do Dataflow para o lookup no MongoDB (refresh periódico vs. reload por Notificação de mudança no GCS) — decisão de performance a tomar no `/define`.
- Estratégia de retomada/backfill do Debezium Server em caso de queda prolongada do túnel ou do próprio container — detalhar no `/define`.

---

## Status: ✅ Complete (Defined)

**Revisão:** Brainstorm conduzido nesta sessão via `/brainstorm`, resolvendo a pendência "🔶 sob avaliação" registrada em `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` (Fase 3 — GCP). Próximo passo: `/define .claude/sdd/features/BRAINSTORM_INGESTAO_GCP_FASE3.md`.
