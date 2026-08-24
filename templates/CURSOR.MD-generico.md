# <NOME_DO_PROJETO> — Contexto para Cursor (template genérico)

> **Como usar:** copie este arquivo para `.cursor/CURSOR.MD` (ou `CURSOR.md`, conforme o padrão do time). Substitua `<...>`, remova seções irrelevantes e atualize links relativos (`../docs/`, etc.).

> **Uma linha sobre o produto:** <descrição curta do que o repositório entrega>

---

## Roteamento de agentes (multi-agente)

Sempre consulte **`.cursor/commands/core/router.md`** (ou o arquivo de roteamento definido pelo time) para decidir qual agente deve liderar a resposta.

Após selecionar o agente primário:

1. Abra e siga o arquivo Markdown do agente escolhido em `.cursor/agents/`.
2. Use esse arquivo como instrução principal de comportamento, escopo e estilo de resposta.
3. Use agentes de apoio apenas quando houver ganho claro.
4. Consulte a knowledge base relevante em `.cursor/kb/` (e o índice, se existir).
5. **Agente “expert” do domínio deste repositório (opcional):** priorize  
   `.cursor/agents/<pasta>/<nome>-expert.md`  
   para assuntos estritamente específicos do produto `<NOME_DO_PROJETO>`.

---

# Cursor Project Context

Este repositório pode usar uma **arquitetura multi-agente** no Cursor.

| Recurso | Caminho típico |
|--------|----------------|
| Agentes | `.cursor/agents/` |
| Knowledge base | `.cursor/kb/` |
| Comandos (slash / automação) | `.cursor/commands/` |
| SDD / especificações (opcional) | `.cursor/sdd/` |
| Dev loop / tarefas longas (opcional) | `.cursor/dev/` |

---

## Agentes disponíveis (pastas)

> Ajuste a lista às pastas que existirem no seu clone. Exemplo de categorias comuns:

| Categoria | Pasta |
|-----------|--------|
| Workflow / SDD | `.cursor/agents/workflow` |
| Qualidade de código | `.cursor/agents/code-quality` |
| Engenharia de dados | `.cursor/agents/data-engineering` |
| AI / ML | `.cursor/agents/ai-ml` |
| Comunicação / planejamento | `.cursor/agents/communication` |
| Domínio do produto | `.cursor/agents/domain` |
| Exploração / KB | `.cursor/agents/exploration` |
| Dev loop | `.cursor/agents/dev` |
| **Específico do projeto** | `.cursor/agents/<seu-projeto>/` |

---

## Knowledge base

- Índice (quando existir): `.cursor/kb/_index.yaml`
- Domínios de exemplo — **substitua pelos seus:**

| Domínio | Propósito | Ponto de entrada sugerido |
|---------|-----------|---------------------------|
| `<dominio-a>` | `<ex.: autenticação, Spark, API interna>` | `.cursor/kb/<dominio-a>/index.md` |
| `<dominio-b>` | `<ex.: contratos, erros comuns>` | `.cursor/kb/<dominio-b>/index.md` |

### Estrutura sugerida por domínio

```text
.cursor/kb/{domínio}/
├── index.md            # Visão geral
├── quick-reference.md  # Cheat sheet (opcional)
├── concepts/           # Conceitos
├── patterns/           # Padrões e receitas
└── specs/              # YAML / contratos (opcional)
```

---

## Instruções operacionais

Ao responder perguntas sobre este repositório:

1. Identifique o **agente** mais adequado (via router + intenção do usuário).
2. Carregue conhecimento da **KB** quando o tópico for recorrente ou sensível a detalhes.
3. Use **comandos** em `.cursor/commands/` quando a tarefa for repetitiva ou precisar de um fluxo fixo.

**Idioma padrão:** português brasileiro, salvo pedido explícito em outro idioma.

---

## Contexto do projeto

| Campo | Conteúdo |
|-------|----------|
| **Problema de negócio** | <O que o sistema resolve para usuários ou para a empresa.> |
| **Solução** | <Arquitetura em alto nível: serviços, jobs, biblioteca, etc.> |
| **Ambientes** | <dev / hml / prd ou equivalente; nomes oficiais.> |
| **Requisitos / decisões** | Links: [`../notes/...`](../notes/) ou [`../docs/00-INDEX.md`](../docs/00-INDEX.md) |

---

## Visão geral da arquitetura

Substitua o diagrama abemplo por um que reflita **seu** sistema (C4, fluxo de dados, sequência, etc.).

```text
[FONTE/SISTEMA A]  ──▶  [PROCESSAMENTO / API]  ──▶  [DESTINO / CLIENTE]
                              │
                              └──▶ [OBSERVABILIDADE / FILAS / NOTIFICAÇÕES] (opcional)
```

| Camada / componente | Tecnologia | Propósito |
|--------------------|------------|-----------|
| `<nome>` | `<ex.: Node 20, Python 3.11, Spark>` | `<uma frase>` |
| `<nome>` | `<...>` | `<...>` |

---

## Estrutura do repositório (exemplo)

> Personalize árvore e comentários. Mantenha caminhos reais.

```text
<nome-do-repo>/
├── src/                    # ou apps/, packages/, lib/
├── tests/
├── docs/
│   └── 00-INDEX.md         # índice da documentação (recomendado)
├── scripts/                # build, deploy, utilitários (opcional)
├── .cursor/
│   ├── agents/
│   ├── kb/
│   ├── commands/
│   ├── sdd/                # opcional
│   └── dev/                # opcional
├── CONTEXT.md              # onboarding rápido (recomendado)
├── README.md
├── .cursorrules
└── <manifesto de deps: package.json, pyproject.toml, etc.>
```

---

## Execução e desenvolvimento local

### Comandos rápidos

```bash
# Instalar dependências
<comando>

# Testes
<comando>

# Build / lint (se houver)
<comando>
```

### Variáveis de ambiente

- Referência: `.env.example` (ou documentação em `docs/`).
- **Nunca** commitar segredos.

---

## Workflows de desenvolvimento (opcional)

### Spec-Driven Development (SDD)

Se o time usar comandos tipo `/define`, `/design`, `/build`:

| Comando | Fase | Propósito |
|---------|------|-----------|
| `/brainstorm` | 0 | Explorar ideias (opcional) |
| `/define` | 1 | Requisitos |
| `/design` | 2 | Arquitetura / especificação |
| `/build` | 3 | Implementação |
| `/ship` | 4 | Encerramento / arquivo |
| `/iterate` | — | Ajustar docs no meio do fluxo |

**Artefatos típicos:** `.cursor/sdd/features/`, `.cursor/sdd/archive/`

### Dev Loop (opcional)

```bash
# Exemplo genérico — alinhar ao comando real do projeto
/dev "<descreva a tarefa>"
```

---

## Guia de uso de agentes

### Referência com `@`

No chat ou Composer, use `@` apontando para o arquivo do agente, por exemplo:

```text
@.cursor/agents/<categoria>/<agente>.md

<contexto curto + resultado esperado>
```

### Tabela resumo (preencha)

| Categoria | Quando usar |
|-----------|-------------|
| Workflow | Features com rastreabilidade (SDD) |
| Code quality | Review, testes, refino de estilo |
| Data engineering | Pipelines, Spark, lakehouse (se aplicável) |
| Domínio | Regras de negócio do produto |
| Exploration | Onboarding em codebase grande, nova KB |

---

## Padrões de código

> Adapte à linguagem principal do repositório.

- **Estilo:** <PEP 8 / ESLint / fmt — o que o CI usa>
- **Testes:** `<pytest | jest | ...>`
- **Tipagem:** <obrigatória onde fizer sentido>
- **Princípios:** Clean Code, SOLID, mudanças pequenas e revisáveis
- **Observabilidade:** logging estruturado, métricas/traces se o projeto já adotar

---

## Comandos disponíveis (slash)

> Liste apenas os que existem em `.cursor/commands/`. Exemplo genérico:

| Comando | Propósito |
|---------|-----------|
| `/review` | Revisão de código |
| `/sync-context` | Atualizar este `CURSOR.MD` / contexto |
| `/readme-maker` | Gerar ou refinar README |
| `<...>` | `<...>` |

---

## Troubleshooting

### Problemas comuns (template de tabela)

| Sintoma | Causa provável | Onde investigar |
|---------|----------------|-----------------|
| `<erro ou mensagem>` | `<hipótese>` | `<doc ou caminho>` |
| Build quebrado | versão de runtime / cache | `docs/`, CI logs |

### Fluxo sugerido

1. Índice: `docs/00-INDEX.md` (ou README).
2. Logs locais / CI.
3. Issues internas / runbook (link).

---

## Monitoramento e logging (opcional)

- **Onde ficam logs:** `<caminho ou serviço>`
- **Retenção / rotação:** `<política>`
- **Alertas:** `<ferramenta>`

---

## Obtendo ajuda

| Tipo | Recurso |
|------|---------|
| Onboarding rápido | [`../CONTEXT.md`](../CONTEXT.md) |
| Índice de docs | [`../docs/00-INDEX.md`](../docs/00-INDEX.md) |
| Agentes e `@` | `HOW_TO_USE_AGENTS.md` (se existir) |
| Criar projeto com agentes | `MANUAL_AGENTES.md` (se existir) |

---

## Links externos

- Repositório / board: `<URL>`
- Documentação oficial das tecnologias principais: `<URLs>`

---

## Histórico de versões

| Data | Mudanças |
|------|----------|
| `<AAAA-MM-DD>` | Criação do `.cursor/CURSOR.MD` a partir do template genérico |

---

*Última atualização: <AAAA-MM-DD>*
