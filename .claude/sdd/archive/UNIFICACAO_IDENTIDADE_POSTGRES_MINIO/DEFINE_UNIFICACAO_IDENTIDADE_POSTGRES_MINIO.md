# DEFINE: Unificação de Identidade Postgres×MinIO (Onda 2)

| Campo | Valor |
|-------|-------|
| **Feature** | UNIFICACAO_IDENTIDADE_POSTGRES_MINIO |
| **Fase do roadmap** | Fase 0 — Fundação (`docs/plan.md`) |
| **Input** | `.claude/sdd/features/BRAINSTORM_UNIFICACAO_IDENTIDADE_POSTGRES_MINIO.md` |
| **Status** | ✅ Shipped |
| **Data** | 2026-08-24 |

---

## Problem Statement

Usuário e Motorista existem hoje como **duas populações desconectadas**: o Postgres real (Airbyte CDC, chave UUID, sem CPF) e o MinIO simulado (usado por `kafka/orders` e outros streams, chave int sequencial). Isso impede join real entre pedido↔usuário e pedido↔motorista no Gold, e mantém duas tabelas Silver de motorista (`silver_drivers_profile`, `silver_drivers_performance`) sem nenhuma ligação entre si — apesar de a Onda 1 já ter corrigido tudo que era resolvível só dentro do MinIO. A investigação confirmou que o ShadowTraffic suporta lookup cruzado entre conexões Postgres e MinIO no mesmo processo, desbloqueando a correção definitiva.

## Target Users

| Usuário | Papel | Dor |
|---------|-------|-----|
| Autor do projeto (portfólio pessoal) | Desenvolvedor/arquiteto de dados fechando a Fase 0 do roadmap multi-cloud | Sem esta correção, o "arcabouço de dados" nunca fica de fato pronto para ser reaproveitado nas 9 combinações arquitetura×cloud — Usuário/Motorista permanecem inconsistentes |

## Goals

| Prioridade | Meta |
|------------|------|
| **MUST** | Consolidar `gen-drivers`, `gen-users`, `gen-minio` (3 containers) num único gerador/processo com `connections: postgres` + `minio` |
| **MUST** | Migrar PK de Usuário/Motorista de UUID para int sequencial em `sql/create_users_table.sql`, `create_drivers_table.sql` e nos templates do gerador Postgres |
| **MUST** | Redirecionar `kafka/orders.user_key`/`driver_key` e todo consumidor MinIO (`mongodb/support`, `kafka/shift`, `kafka/route`, etc.) para o Postgres real unificado |
| **MUST** | Aposentar `mssql/users`, `mongodb/users`, `postgres/drivers` (streams MinIO simulados) do gerador |
| **MUST** | Corrigir `kafka/route.end_lat/end_lon` para lookup no `lat`/`lon` real do Usuário |
| **MUST** | Reconciliar `silver_drivers_profile` e `silver_drivers_performance` numa única dimensão de motorista no Silver |
| **MUST** | Regenerar dados e validar com join real no Gold que todos os relacionamentos retornam resultado consistente, sem órfãos |
| **MUST** | Atualizar `docs/MODELO_CONCEITUAL_UBER_EATS.md` refletindo o estado final, sem pendências conhecidas |
| **SHOULD** | Preservar sem alteração tudo que a Onda 1 já corrigiu (bugs mecânicos, chave de Restaurante, Avaliação→Pedido, origem da Entrega) |

## Success Criteria

- [ ] Um único processo/container ShadowTraffic gera Usuário, Motorista e todos os streams MinIO — `gen-drivers`/`gen-users`/`gen-minio` deixam de existir como serviços separados
- [ ] `users.user_id` e `drivers.driver_id` no Postgres real são int sequencial, não mais UUID
- [ ] 100% dos registros de `kafka/orders`, `mongodb/support`, `kafka/shift`, `kafka/route` (e demais consumidores) referenciam o `user_id`/`driver_id` real via lookup — nenhum stream MinIO gera identidade própria de usuário/motorista
- [ ] `mssql/users`, `mongodb/users`, `postgres/drivers` não existem mais no gerador MinIO
- [ ] `kafka/route.end_lat/end_lon` corresponde ao `lat`/`lon` real de um Usuário existente
- [ ] Existe uma única tabela Silver de dimensão de motorista, sem duplicidade
- [ ] Query de join no Gold entre pedido↔usuário e pedido↔motorista retorna 0 registros órfãos
- [ ] `docs/MODELO_CONCEITUAL_UBER_EATS.md` não lista nenhuma pendência de Onda 2 — todas resolvidas

## Acceptance Tests

| ID | Cenário | Given | When | Then |
|----|---------|-------|------|------|
| AT-001 | Gerador unificado | `docker-compose.yml` atualizado | `docker-compose up` | Apenas 1 serviço gerador roda (não mais 3); logs confirmam geração de Postgres e MinIO no mesmo processo |
| AT-002 | PK sequencial | Schema migrado, dados regenerados | Inspecionar `users.user_id`/`drivers.driver_id` no Postgres | Valores são inteiros sequenciais, não UUID |
| AT-003 | Join pedido↔usuário sem órfãos | Dados regenerados | Join `silver_kafka_orders` ↔ `silver_postgres_users` por `id_usuario` | 0 órfãos |
| AT-004 | Join pedido↔motorista sem órfãos | Dados regenerados | Join `silver_kafka_orders` ↔ dimensão única de motorista por `id_motorista` | 0 órfãos |
| AT-005 | Streams aposentados | Gerador MinIO revisado | `grep` por `mssql/users`\|`mongodb/users`\|`postgres/drivers` em `gen/minio/uber-eats.json` | 0 ocorrências |
| AT-006 | Destino da Entrega coerente | Dados regenerados | Comparar `end_lat/lon` de `silver_kafka_route` com `lat/lon` de algum usuário real | Coordenadas correspondem a um usuário existente |
| AT-007 | Dimensão de motorista única | Silver revisado | Verificar tabelas Silver de motorista | Existe 1 tabela, não 2 |
| AT-008 | Documentação sem pendência | Build concluído | `docs/MODELO_CONCEITUAL_UBER_EATS.md` revisado | Nenhuma linha de "Onda 2 pendente" — tudo marcado resolvido |

## Out of Scope

- Tudo já resolvido na Onda 1 (bugs mecânicos, chave de Restaurante, Avaliação→Pedido, origem da Entrega) — não revisitar
- Amarrar a origem da Entrega ao restaurante *exato* do pedido (limitação de lookup em 2 níveis — possível Onda 3, não parte desta feature)
- Novas entidades, novos relatórios Gold, novas regras de negócio além do já documentado

## Constraints

- Migração de PK (UUID→sequencial) exige regenerar os dados já carregados no Postgres real — não é uma migração incremental preservando histórico
- Unificação exige alterar `docker-compose.yml` (consolidar 3 serviços em 1) — mudança de infraestrutura local, não só de código de aplicação
- Validação final deve usar o pipeline Databricks real (Silver → Gold), consistente com a Onda 1

## Assumptions

| ID | Suposição | Impacto se errada | Validada? |
|----|-----------|---------------------|-----------|
| A-001 | O ShadowTraffic aceita um único config com múltiplas `connections` (`postgres` + `minio`) e lookup cruzado, exatamente como a documentação oficial mostra | Se houver diferença de comportamento na versão de imagem Docker usada (`shadowtraffic/shadowtraffic:latest`), a unificação pode falhar e exigir abordagem alternativa | [x] Confirmado via documentação oficial com exemplo prático equivalente; [ ] não testado neste projeto especificamente |
| A-002 | Nenhum outro script Silver/Gold além dos já identificados referencia `silver_drivers_profile` ou os streams aposentados | Se houver referência não identificada, a correção fica incompleta | [ ] Confirmar via grep no Design |
| A-003 | Regenerar o Postgres real (truncar e recarregar `users`/`drivers`) não quebra nada fora deste projeto | Não há consumidor externo a este projeto — risco baixo, mas não formalmente verificado | [ ] Assumir como verdadeira, projeto é portfólio isolado |

## Requisitos operacionais de pipeline (mandato)

Esta feature altera schema real (Postgres) e scripts do pipeline medalhão (Silver de motorista) — o sinal `medalhão bronze silver gold` de `PIPELINE_MANDATORY_PRACTICES.yaml` se aplica novamente.

| Categoria | Status | Justificativa |
|-----------|--------|----------------|
| Contrato de dados (DC-M01-05) | **SHOULD** — DC-M04 aplica | Mudança de schema real (PK UUID→sequencial) é uma mudança de contrato deliberada — vale documentar no runbook (`docs/MODELO_CONCEITUAL_UBER_EATS.md` já cumpre esse papel para este projeto de portfólio) |
| Medalhão e UC (MED-M01-04) | **SHOULD** — MED-M02, MED-M04 aplicam | Projeção explícita deve ser preservada na reconciliação da dimensão de motorista; a troca de PK é uma mudança de idempotência que precisa ser deliberada (SCD Type 1 já em uso, sem mudança de estratégia) |
| Qualidade e quarentena (DQ-M01-05) | **N/A justificado** | Correção de origem, não introduz pipeline de quarentena novo |
| Schema drift (SD-M01-04) | **N/A justificado** | Mudança de schema é deliberada e controlada, não drift não previsto |
| Teams / alertas (TM-M01-06) | **N/A justificado** | Sem mudança de comportamento operacional de falha/alerta |
| Observabilidade (OBS-M01-03) | **N/A justificado** | Fora do escopo desta correção pontual |
| Segurança (GOV-M01-02) | **N/A justificado** | Nenhum secret novo; migração de PK não envolve grants UC |
| Testes (TEST-M01-02) | **SHOULD** — TEST-M02 aplica | Recomenda-se `/pipeline-review-init` ao final da Onda 2, fechando de vez a Fase 0 |
| PyODBC (PYODBC-M01-05) | **N/A** | Não se aplica |

## Clarity Score Breakdown

| Elemento | Score | Justificativa |
|----------|-------|----------------|
| Problem | 3/3 | Claro, com achado técnico documentado e fontes citadas |
| Users | 2/3 | Único usuário/persona (projeto pessoal) |
| Goals | 3/3 | Priorizados, mensuráveis, ligados a arquivos reais |
| Success | 3/3 | Testável via join real + inspeção de schema |
| Scope | 3/3 | Onda 1 vs Onda 2 vs possível Onda 3 (2-level lookup) delimitado |
| **Total** | **14/15** | Acima do mínimo de 12 — segue para Design sem gaps bloqueantes |

## Open Questions

Resolvida no Design: motorista ganha `vehicle_make`/`vehicle_model`/`vehicle_year`/`license_number`/`city` no Postgres real (usuário preferiu não perder atributos a aceitar a simplificação).

## Revision History

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | 2026-08-24 | Documento inicial, extraído de `BRAINSTORM_UNIFICACAO_IDENTIDADE_POSTGRES_MINIO.md` |
| 1.1 | 2026-08-24 | Status atualizado para Complete (Designed) após `/design` concluído |
| 1.2 | 2026-08-24 | Build concluído (código/config); validação de integração pendente de execução manual — ver BUILD_REPORT |
| 1.3 | 2026-09-01 | Shipped e arquivado — volume Postgres recriado, PK sequencial e campos novos de `drivers` confirmados por inspeção direta do schema (`\d users`, `\d drivers`). Geração de dados (ShadowTraffic) e joins reais no Gold (AT-002 a AT-007) ficaram bloqueados por licença expirada da imagem `shadowtraffic/shadowtraffic:latest` — decisão consciente do usuário de aceitar a validação de schema como critério suficiente para fechar, retomando a validação de dados após renovar a licença |

---

## Status: ✅ Shipped
