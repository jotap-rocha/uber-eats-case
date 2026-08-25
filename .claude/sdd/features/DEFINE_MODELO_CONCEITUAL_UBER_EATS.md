# DEFINE: Modelo Conceitual do Domínio Uber Eats

| Campo | Valor |
|-------|-------|
| **Feature** | MODELO_CONCEITUAL_UBER_EATS |
| **Fase do roadmap** | Fase 0 — Fundação (`docs/plan.md`) |
| **Input** | `.claude/sdd/features/BRAINSTORM_MODELO_CONCEITUAL_UBER_EATS.md` |
| **Status** | ✅ Complete (Built) |
| **Data** | 2026-08-24 |

---

## Problem Statement

O gerador de dados sintéticos do projeto (`gen/minio/uber-eats.json`, 20 streams simulando Postgres/MySQL/MongoDB/Kafka) não tem um modelo conceitual documentado. Isso deixa os relacionamentos entre entidades inconsistentes — 3 entidades usam chave dupla (natural vs. técnica) sem padrão único, e 2 relacionamentos estão fisicamente quebrados (geram valor aleatório em vez de referenciar o registro correto). Sem esse modelo, não é possível corrigir a integridade referencial do Shadow Traffic (critério de saída da Fase 0) nem reaproveitar uma definição única de domínio nas 9 combinações arquitetura×cloud do roadmap.

## Target Users

| Usuário | Papel | Dor |
|---------|-------|-----|
| Autor do projeto (portfólio pessoal) | Desenvolvedor/arquiteto de dados construindo as 9 combinações arquitetura×cloud | Sem modelo formal, cada arquitetura reinterpretaria o domínio de um jeito diferente, e a correção de integridade referencial não teria um contrato claro pra seguir |

## Goals

| Prioridade | Meta |
|------------|------|
| **MUST** | Documentar as 13 entidades do domínio com relacionamento, cardinalidade e chave-alvo canônica |
| **MUST** | Estabelecer o ID técnico sequencial (não CPF/CNPJ/license_number) como chave de junção canônica nas 3 entidades de chave dupla |
| **MUST** | Registrar os 2 bugs mecânicos de integridade referencial (`payment_key`, `product_id`) com correção definida |
| **SHOULD** | Registrar os 2 gaps estruturais (geolocalização da Entrega, ligação de Avaliação) como discovery obrigatório da próxima feature, sem propor solução de atributo/regra de negócio agora |
| **SHOULD** | Publicar o modelo final também em `docs/MODELO_CONCEITUAL_UBER_EATS.md`, visível no repositório/portfólio, além do registro em `.claude/sdd/` |
| **COULD** | Referenciar este modelo a partir do `README.md` raiz, na seção de arquitetura |

## Success Criteria

- [ ] Todas as 20 streams do gerador aparecem classificadas (entidade, subentidade/histórico, ou fora de escopo com motivo) — nenhuma stream fica sem categoria
- [ ] Nenhuma das 3 entidades de chave dupla (Usuário, Restaurante, Motorista) tem mais de uma chave de junção candidata no modelo final — cada uma tem exatamente uma chave-alvo
- [ ] Os 2 bugs mecânicos (`payment_key`, `product_id`) têm a correção exata (de → para) documentada, pronta pra implementação na próxima feature
- [ ] Os 2 gaps estruturais aparecem com problema declarado e entidades envolvidas, sem solução prematura de atributo/regra de negócio
- [ ] Documento final publicado em `docs/MODELO_CONCEITUAL_UBER_EATS.md`

## Acceptance Tests

| ID | Cenário | Given | When | Then |
|----|---------|-------|------|------|
| AT-001 | Cobertura completa das streams | As 20 streams do gerador `gen/minio/uber-eats.json` | O documento final é revisado | Toda stream aparece classificada como entidade, subentidade/histórico, ou fora de escopo com motivo — nenhuma fica sem categoria |
| AT-002 | Chave canônica sem ambiguidade | As 3 entidades de chave dupla (Usuário, Restaurante, Motorista) | O modelo de relacionamentos é revisado | Cada uma aparece com exatamente uma chave-alvo (ID técnico), sem menção a CPF/CNPJ/license_number como chave de junção |
| AT-003 | Bugs vs. gaps separados corretamente | Os 4 problemas de integridade encontrados no brainstorm | Categorizados no DESIGN | Os 2 bugs mecânicos (`payment_key`, `product_id`) têm correção "de → para" definida; os 2 gaps estruturais têm problema declarado, sem solução de atributo/regra de negócio |
| AT-004 | Publicação visível | O modelo aprovado | O BUILD é executado | Existe `docs/MODELO_CONCEITUAL_UBER_EATS.md` no repositório, com o conteúdo do modelo |

## Out of Scope

- Atributos e tipos de dado por entidade (fica só em entidade + relacionamento + cardinalidade — modelagem dimensional é da Fase 1/Warehouse)
- Correção efetiva do gerador Shadow Traffic (`gen/minio/uber-eats.json`) — vira a próxima feature
- Solução de atributo/regra de negócio para os 2 gaps estruturais (geolocalização da Entrega, ligação de Avaliação) — fica só o problema declarado
- Streams comportamentais/telemetria: `mysql/menu`, `mongodb/recommendations`, `kafka/search`, `kafka/gps`
- Diagrama visual (Mermaid/ER gráfico) — só tabela textual, por decisão do usuário no brainstorm
- Reconciliação entre as tabelas Postgres reais (`sql/*.sql`) e os streams `postgres/*` simulados no MinIO — questão técnica de arquitetura de dados, não de modelo conceitual

## Constraints

- Modelo deve ser único e reaproveitável, sem alteração, nas 3 arquiteturas (Warehouse, Lakehouse, Kappa) × 3 clouds (Azure, AWS, GCP) do roadmap em `docs/plan.md`
- Única fonte de verdade para o modelo: `gen/minio/uber-eats.json` — nenhuma amostra externa (confirmado pelo usuário no brainstorm)
- Formato de entrega: tabela textual em Markdown, sem diagrama

## Assumptions

| ID | Suposição | Impacto se errada | Validada? |
|----|-----------|---------------------|-----------|
| A-001 | `gen/minio/uber-eats.json` é a fonte de verdade completa do domínio e não muda antes da próxima feature | Modelo ficaria desatualizado assim que o gerador mudar | [x] Confirmado pelo usuário |
| A-002 | ID técnico sequencial é estável o suficiente pra servir de chave canônica nas 3 clouds | Chave canônica precisaria reavaliação se algum motor gerar IDs técnicos diferentes por cloud | [ ] Decisão de design, não fato verificável ainda |
| A-003 | As tabelas Postgres reais (`sql/*.sql`) e os streams `postgres/*` do MinIO representam o mesmo domínio, mesmo sem unificação física hoje | Pipeline de integração da próxima feature precisaria reconciliar 2 fontes Postgres distintas | [ ] Não validado — fora do escopo desta feature |

## Requisitos operacionais de pipeline (mandato)

**N/A justificado** — esta feature produz um modelo conceitual (documentação), não implementa ingestão/transformação de dados. Nenhum dos sinais de `PIPELINE_MANDATORY_PRACTICES.yaml.applies_when` (medalhão, DLT, autoloader, Spark streaming, Unity Catalog, PyODBC) se aplica aqui. A seção volta a valer na próxima feature (correção do Shadow Traffic), se ela envolver pipeline real.

## Clarity Score Breakdown

| Elemento | Score | Justificativa |
|----------|-------|----------------|
| Problem | 3/3 | Claro, específico, ligado ao critério de saída da Fase 0 |
| Users | 2/3 | Um único usuário/persona (projeto pessoal) — claro, mas sem múltiplos stakeholders para comparar |
| Goals | 3/3 | Priorizados MUST/SHOULD/COULD, mensuráveis |
| Success | 3/3 | Critérios testáveis, com acceptance tests concretos |
| Scope | 3/3 | Extensivamente delimitado no brainstorm (YAGNI aplicado a 7 streams) |
| **Total** | **14/15** | Acima do mínimo de 12 — segue para Design sem gaps bloqueantes |

## Open Questions

- Nenhuma pendente para o Design. A decisão de publicar também em `docs/` foi resolvida nesta fase (ver Goals/Success Criteria).

## Revision History

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | 2026-08-24 | Documento inicial, extraído de `BRAINSTORM_MODELO_CONCEITUAL_UBER_EATS.md` |
| 1.1 | 2026-08-24 | Status atualizado para Complete (Designed) após `/design` concluído |
| 1.2 | 2026-08-24 | Status atualizado para Complete (Built) após `/build` concluído |

---

## Status: ✅ Complete (Built)

**Próximo passo:** `/ship`
