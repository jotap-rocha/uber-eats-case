# DESIGN: Modelo Conceitual do Domínio Uber Eats

| Campo | Valor |
|-------|-------|
| **Feature** | MODELO_CONCEITUAL_UBER_EATS |
| **Input** | `.claude/sdd/features/DEFINE_MODELO_CONCEITUAL_UBER_EATS.md` |
| **Status** | ✅ Complete (Built) |
| **Data** | 2026-08-24 |

---

## Architecture Overview

Esta feature não produz código — produz um **artefato de documentação** consumido em duas frentes: o registro de processo (SDD) e a publicação visível no repositório (`docs/`). O conteúdo em si (13 entidades, relacionamentos, decisões de chave, bugs e gaps) já foi integralmente elaborado e validado no BRAINSTORM; o BUILD desta feature consiste em **consolidar e publicar** esse conteúdo já pronto, não em descobri-lo.

```text
┌───────────────────────────────────────────────────────────────────────┐
│                     FLUXO DE PUBLICAÇÃO DO MODELO                      │
├───────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  BRAINSTORM_*.md        DEFINE_*.md         DESIGN_*.md (este)         │
│  (conteúdo completo) →  (requisitos)   →   (spec de publicação)        │
│                                                     │                  │
│                                                     ▼                  │
│                                            [BUILD desta feature]       │
│                                                     │                  │
│                    ┌────────────────────────────────┼──────────────┐  │
│                    ▼                                 ▼              │  │
│      docs/MODELO_CONCEITUAL_UBER_EATS.md   docs/00-INDEX.md         │  │
│      (modelo completo, publicado)          (+1 linha de navegação)  │  │
│                    │                                                │  │
│                    ▼                                                │  │
│      Consumido pelas 9 combinações arquitetura×cloud                │  │
│      (Fases 1-3 do roadmap em docs/plan.md), sem alteração           │  │
│                                                                       │  │
└───────────────────────────────────────────────────────────────────────┘
```

**Integration Points:**
- `docs/00-INDEX.md` — índice de navegação da documentação do projeto
- `docs/plan.md` — roadmap que consome este modelo nas Fases 1-3
- Próxima feature (correção do Shadow Traffic) — consome os bugs/gaps documentados aqui como input de discovery

---

## Decisões de Arquitetura (ADRs inline)

### Decisão: Modelo-alvo prescritivo (não descritivo)

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-24 |

**Contexto:** O gerador (`gen/minio/uber-eats.json`) tem 3 entidades com chave dupla e 2 relacionamentos fisicamente quebrados. Era preciso decidir se o modelo documenta o estado atual como está, ou define qual é o estado correto.

**Escolha:** Modelo prescritivo — define a chave-alvo/relacionamento correto para cada entidade, documentando os desvios atuais como "a corrigir".

**Racional:** Vira o contrato que a próxima feature (correção do Shadow Traffic) implementa diretamente, sem reabrir a pergunta "qual chave é a certa".

**Alternativas Rejeitadas:**
1. Modelo descritivo (as-is) — mais rápido de produzir, mas não resolve a ambiguidade de chave, só adia a decisão para depois.

**Consequências:** O modelo carrega uma decisão de arquitetura, não é neutro — a próxima feature deve seguir o contrato definido aqui, não redescobrir a chave correta.

---

### Decisão: ID técnico sequencial como chave canônica de junção

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-24 |

**Contexto:** Usuário, Restaurante e Motorista são referenciados por 2 chaves diferentes dependendo do stream (natural: `cpf`/`cnpj`/`license_number`; técnica: `user_id`/`restaurant_id`/`driver_id`).

**Escolha:** O ID técnico sequencial vence como chave-alvo de junção em todo o domínio. CPF/CNPJ/license_number continuam existindo como atributos — não são eliminados dos dados, só deixam de ser usados como chave de relacionamento.

**Racional:** CPF é PII sensível — não deveria se propagar como FK por todo o domínio (alinhado à KB `app_security/concepts/secrets-gestao.md`). IDs técnicos são estáveis e não variam de formato entre fontes.

**Alternativas Rejeitadas:**
1. Chave natural como canônica — mantém o padrão que `kafka/orders` já usa hoje, mas propaga PII (cpf) como chave de junção por todo o domínio.

**Consequências:** Toda correção de integridade referencial na próxima feature deve trocar lookups de `cpf`/`cnpj`/`license_number` por `user_id`/`restaurant_id`/`driver_id`, mantendo os campos naturais como atributos regulares.

---

### Decisão: Escopo de 13 entidades, 7 streams fora do modelo core

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-24 |

**Contexto:** O gerador tem 20 streams; nem todos representam "objetos" de negócio com identidade própria — alguns são histórico de estado, artefato derivado, construção de apresentação ou evento comportamental.

**Escolha:** 13 entidades no modelo core (Usuário, Restaurante, Produto, Motorista, Pedido, Item de Pedido, Pagamento, Entrega, Avaliação, Recibo, Estoque, Turno, Incidente). `kafka/status` e `kafka/events` viram subentidade/histórico das entidades Pedido e Pagamento; `mysql/menu`, `mongodb/recommendations`, `kafka/search`, `kafka/gps` ficam fora do modelo core; `mongodb/users` é absorvida por Usuário.

**Racional:** Critério objetivo — "tem identidade própria e é referenciado como pai por outra coisa" — separa entidade de log/evento/derivado/comportamental de forma consistente, sem depender só da lista original de 8 entidades do `plan.md`.

**Alternativas Rejeitadas:**
1. Modelar todos os 20 streams como entidades — infla o modelo com logs/telemetria sem valor de modelagem conceitual, e obscurece as entidades que realmente importam.

**Consequências:** Motorista, Turno, Recibo, Estoque e Incidente entram no modelo mesmo não estando nos 8 nomes originais do `plan.md`, porque o critério objetivo prevaleceu sobre a lista inicial (validado com o usuário).

---

### Decisão: Publicação dupla — SDD + docs/

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-24 |

**Contexto:** O modelo será reaproveitado nas 9 combinações arquitetura×cloud ao longo de ~10-13 meses de trabalho. Só o registro em `.claude/sdd/` fica pouco visível no dia a dia do portfólio.

**Escolha:** Publicar também em `docs/MODELO_CONCEITUAL_UBER_EATS.md`, navegável a partir de `docs/00-INDEX.md`.

**Racional:** Fica acessível sem precisar reabrir o processo SDD toda vez que uma das 9 combinações precisar consultar o modelo.

**Alternativas Rejeitadas:**
1. Manter só em `.claude/sdd/features/` — mais simples, mas dificulta consulta recorrente durante meses de trabalho.

**Consequências:** Dois arquivos precisam ficar sincronizados se o modelo mudar via `/iterate` — o SDD é a fonte do processo, `docs/` é a publicação para consumo externo.

---

## File Manifest

| # | Arquivo | Ação | Propósito | Dependências | Agente | Racional |
|---|---------|------|-----------|----------------|--------|----------|
| 1 | `docs/MODELO_CONCEITUAL_UBER_EATS.md` | Create | Publicar o modelo completo: 13 entidades, relacionamentos/cardinalidade, decisão de chave canônica, bugs mecânicos, gaps estruturais | Nenhuma | `@code-documenter` | Especialista em documentação abrangente e pronta para uso — sem geração de código envolvida |
| 2 | `docs/00-INDEX.md` | Edit | Adicionar 1 linha na tabela "Guias do projeto" apontando para o novo documento | 1 | `@code-documenter` | Mesmo agente, mantém o índice de navegação consistente |
| 3 | `README.md` | Edit (opcional — prioridade COULD no DEFINE) | Referenciar o modelo na seção de arquitetura, se houver tempo | 1 | `@code-documenter` | Prioridade COULD — só se as tarefas MUST/SHOULD já estiverem completas |

---

## Content Pattern (estrutura pronta para copiar no BUILD)

O `docs/MODELO_CONCEITUAL_UBER_EATS.md` deve seguir esta estrutura, reaproveitando o conteúdo já validado no BRAINSTORM (sem redescobrir nada, só consolidar e formatar para publicação):

```markdown
# Modelo Conceitual do Domínio — Uber Eats

> Fonte: BRAINSTORM/DEFINE/DESIGN em `.claude/sdd/features/*_MODELO_CONCEITUAL_UBER_EATS.md`.
> Reaproveitado sem alteração nas 3 arquiteturas (Warehouse, Lakehouse, Kappa) × 3 clouds
> (Azure, AWS, GCP) do roadmap em `docs/plan.md`.

## Entidades (13)
{tabela: Entidade | Stream de origem | Por que é entidade}

## Relacionamentos e cardinalidade (modelo-alvo)
{tabela: Entidade | Relaciona-se com | Cardinalidade | Chave-alvo | Observação/gap}

## Decisão de chave canônica
{ID técnico sequencial vence; cpf/cnpj/license_number mantidos como atributos}

## Bugs mecânicos (correção definida)
{payment_key, product_id — de → para}

## Gaps estruturais (discovery da próxima feature)
{geolocalização da Entrega; ligação de Avaliação}

## Streams fora do modelo core
{tabela: Stream | Categoria | Motivo}
```

**Fonte de cada seção:** copiar diretamente das seções equivalentes em `BRAINSTORM_MODELO_CONCEITUAL_UBER_EATS.md` — este DESIGN não introduz conteúdo novo de modelagem, só a estrutura de publicação.

---

## Estratégia de Verificação

Como não há código, a "testagem" é verificação de completude e consistência do documento publicado — cada item mapeia direto a um Acceptance Test do DEFINE:

| ID | Verificação | Como checar | Cobre |
|----|--------------|--------------|-------|
| V-001 | Todas as 20 streams do gerador aparecem classificadas no documento | `grep` por cada um dos 20 `keyPrefix` de `gen/minio/uber-eats.json` em `docs/MODELO_CONCEITUAL_UBER_EATS.md` — todos devem aparecer pelo menos uma vez | AT-001 |
| V-002 | Nenhuma das 3 entidades de chave dupla aparece com mais de uma chave-alvo | Revisão manual da tabela de relacionamentos — cada linha de Usuário/Restaurante/Motorista deve citar só `user_id`/`restaurant_id`/`driver_id` como chave-alvo, nunca `cpf`/`cnpj`/`license_number` | AT-002 |
| V-003 | Os 2 bugs mecânicos têm correção "de → para" documentada | Seção "Bugs mecânicos" contém `payment_key` e `product_id`, cada um com origem errada e correção definida | AT-003 |
| V-004 | Os 2 gaps estruturais aparecem sem solução prematura | Seção "Gaps estruturais" contém as 2 entradas, sem propor atributo ou regra de negócio nova | AT-003 |
| V-005 | Documento existe e está indexado | `Test-Path docs/MODELO_CONCEITUAL_UBER_EATS.md` retorna verdadeiro; `docs/00-INDEX.md` contém link para ele | AT-004 |

---

## Atualização de Status (após Build)

Ao concluir o BUILD, atualizar:
- `DEFINE_MODELO_CONCEITUAL_UBER_EATS.md`: Status → `✅ Complete (Built)`; Next Step → `/ship`
- Este `DESIGN_MODELO_CONCEITUAL_UBER_EATS.md`: Status → `✅ Complete (Built)`; Next Step → `/ship`

---

## Status: ✅ Complete (Built)

**Próximo passo:** `/ship`
