# 🤖 Como Criar Agentes do Zero - Guia Completo

## ✅ Caminho recomendado para criar **arquivos** de agente (`.md`)

### 1. ⭐ **`agent-architect`** (`.cursor/agents/exploration/agent-architect.md`)
- **Especialidade:** Projetar e gravar um novo agente Cursor (Markdown em `.cursor/agents/`), alinhar ao `agent.template.md`, registrar no **`router.md`** e na tabela de **`HOW_TO_USE_AGENTS.md`**, e espelhar em `.github/` / `.claude/` se a política do time exigir.
- **Quando usar:** Sempre que o objetivo for **criar, clonar ou refatorar um agente** (não confundir com `PROMPT.md` do Dev Loop).

### 2. 🎨 **`prompt-crafter`** (`.cursor/agents/dev/prompt-crafter.md`)
- **Especialidade:** Construir **`PROMPT.md`** executável para o Dev Loop (fases, critérios, `@` para agentes existentes).
- **Quando usar:** Quando você quer uma **tarefa** bem definida para executar com `/dev`, não um novo arquivo em `.cursor/agents/`.

### 3. 📚 **`kb-architect`** (`.cursor/agents/exploration/kb-architect.md`)
- **Especialidade:** Criar e organizar **Knowledge Bases** (`.cursor/kb/`).
- **Quando usar:** Documentação de domínio para agentes consultarem — complementar ao agente, não substitui o `agent-architect` para criar o `.md` do agente.

### 4. 📋 **`agent.template.md`** (`.cursor/agents/_template/agent.template.md`)
- **Recurso:** Template completo (placeholders, checklist, seções opcionais).
- **Quando usar:** Base técnica; o **`agent-architect`** orienta como preencher e simplificar.

---

## 📖 Documentação Completa Disponível

Você também tem **3 recursos principais** na raiz / docs:

### 1. **`MANUAL_AGENTES.md`** (Raiz do projeto)
- ⭐ **Leitura OBRIGATÓRIA** antes de criar projetos
- Ensina estrutura básica: `.cursorrules`, `CONTEXT.md`, `docs/00-INDEX.md`
- Checklist de criação

### 2. **`docs/GUIA_CRIACAO_AGENTE_PROJETO.md`**
- Guia completo de 680 linhas
- Templates detalhados
- Exemplos práticos
- Estrutura completa de arquivos

### 3. **`HOW_TO_USE_AGENTS.md`** (Raiz do projeto)
- Índice dos agentes em `.cursor/agents/` e exemplos de uso com `@`
- **Ao criar um agente novo:** inclua uma linha na tabela da categoria correspondente (ex.: `data-engineering/`) para a equipe achar o arquivo rápido

---

## 🎯 Como Criar um Agente Novo - Passo a Passo

### PASSO 1: Use o Template

```bash
# Copie o template para novo agente
cp .cursor/agents/_template/agent.template.md \
   .cursor/agents/{categoria}/meu-novo-agente.md
```

**Categorias disponíveis:**
- `workflow/` - Agentes de fluxo de trabalho (brainstorm, define, design, build, iterate, ship)
- `data-engineering/` - Spark, Lakeflow, Medallion  
  - *Exemplo genérico “stack + repositório”:* [`spark-expert-on-premises.md`](../.cursor/agents/data-engineering/spark-expert-on-premises.md) — Spark on-premises, vault, JDBC; parametriza hosts e pastas via `CONTEXT.md`. Use como modelo ao criar outro agente “stack + repositório” na mesma pasta.
- `code-quality/` - Revisão, limpeza, testes
- `ai-ml/` - LLM, GenAI, prompts
- `domain/` - Domínio específico do projeto
- `exploration/` - Exploração de código e KB
- `communication/` - Análise de reuniões, explicações
- `dev/` - Desenvolvimento geral

### PASSO 2: Edite o Frontmatter (Cabeçalho YAML)

```yaml
---
name: meu-agente-expert  # Nome único, lowercase com hífen
description: |
  Especialista em {domínio}. Use PROATIVAMENTE quando {trigger}.
  
  <example>
  Context: {Situação específica}
  user: "Como faço X?"
  assistant: "Vou usar o meu-agente-expert para resolver isso."
  </example>

tools: [Read, Write, Edit, Grep, Glob, Bash, TodoWrite]
color: blue  # blue, green, orange, purple, red, yellow
model: sonnet  # Opcional: opus, sonnet, haiku
---
```

### PASSO 3: Defina a Identidade

```markdown
# Nome do Agente

> **Identity:** {propósito principal do agente em uma frase}
> **Domain:** {área de conhecimento}
> **Default Threshold:** 0.90  # Nível de confiança padrão
```

### PASSO 4: Adicione Seções Obrigatórias

#### ✅ Seções Essenciais (Mínimo)

1. **Quick Reference** - Fluxo de decisão visual
2. **Validation System** - Agreement Matrix + Thresholds
3. **Capabilities** - O que o agente sabe fazer
4. **Process** - Como o agente trabalha
5. **Knowledge Sources** - Onde buscar informação
6. **Quality Checklist** - Verificações antes de finalizar

#### ⭐ Seções Recomendadas (Completo)

7. **Execution Template** - Template de decisão
8. **Context Loading** - Quando carregar qual contexto
9. **Error Recovery** - Como lidar com falhas
10. **Anti-Patterns** - O que NÃO fazer
11. **Examples** - Exemplos práticos
12. **Extension Points** - Como estender o agente

### PASSO 5: Registre no Router

Adicione em `.cursor/commands/core/router.md`:

```markdown
### {Categoria}

## Agente primário
- `.cursor/agents/{categoria}/meu-agente-expert.md`

## Usar quando
{Descrição de quando este agente deve ser usado}

## Entregáveis típicos
- {Entregável 1}
- {Entregável 2}
```

---

## 💡 Exemplo Prático: Criar "Database Migration Expert"

### 1. Copiar Template

```bash
cp .cursor/agents/_template/agent.template.md \
   .cursor/agents/domain/database-migration-expert.md
```

### 2. Editar Frontmatter

```yaml
---
name: database-migration-expert
description: |
  Especialista em migrações de banco de dados. Use quando criar/modificar 
  schemas, planejar migrations, ou resolver problemas de migração.
  
  <example>
  Context: Usuário precisa criar migration
  user: "Preciso adicionar coluna email na tabela users"
  assistant: "Vou usar o database-migration-expert para criar a migration."
  </example>

tools: [Read, Write, Edit, Grep, Glob, Bash, TodoWrite]
color: purple
---
```

### 3. Definir Capacidades

```markdown
## Capabilities

### Capability 1: Create Migrations
Criar arquivos de migration SQL com up/down scripts.

### Capability 2: Plan Migration Strategy
Planejar ordem de execução e dependências.

### Capability 3: Rollback Plans
Criar planos de rollback seguros.
```

### 4. Adicionar Padrões de Execução

```markdown
## Padrões de Execução

### ✅ Migration Segura

\`\`\`sql
-- UP
BEGIN TRANSACTION;
ALTER TABLE users ADD COLUMN email VARCHAR(255);
CREATE INDEX idx_users_email ON users(email);
COMMIT;

-- DOWN
BEGIN TRANSACTION;
DROP INDEX idx_users_email;
ALTER TABLE users DROP COLUMN email;
COMMIT;
\`\`\`

### ❌ Migration Perigosa (Evitar)

\`\`\`sql
-- Sem transaction - PERIGOSO!
ALTER TABLE users DROP COLUMN password;
\`\`\`
```

---

## 🔧 Dicas de Criação de Agentes

### 1. **Nome do Agente**
- Use lowercase com hífen: `spark-expert`, `meu-produto-expert`
- Seja específico: `migration-expert` é melhor que `database-expert`

### 2. **Description**
- **Primeira linha:** O que o agente faz
- **Segunda linha:** Quando usar PROATIVAMENTE
- **Examples:** Mínimo 2 exemplos de uso

### 3. **Tools**
Ferramentas comuns:
- `Read` - Ler arquivos
- `Write` - Criar arquivos
- `Edit` - Editar arquivos
- `Grep` - Buscar em arquivos
- `Glob` - Encontrar arquivos por padrão
- `Bash` - Executar comandos shell
- `TodoWrite` - Criar TODOs
- `WebSearch` - Buscar na web
- `Task` - Delegar tarefas a outros agentes

### 4. **Color**
Cores por categoria:
- `blue` - Workflow, exploration
- `green` - Data engineering
- `orange` - Code quality
- `purple` - Domain-specific
- `red` - Critical/security
- `yellow` - Communication

### 5. **Validation System**
Sempre inclua:
- **Agreement Matrix** - Como KB e MCP concordam
- **Confidence Modifiers** - O que aumenta/diminui confiança
- **Task Thresholds** - Níveis de confiança por tipo de tarefa

---

## 📋 Checklist de Criação de Agente

```text
ESTRUTURA BÁSICA
[ ] Frontmatter YAML completo (name, description, examples, tools, color)
[ ] Identity section (Identity, Domain, Threshold)
[ ] Quick Reference com fluxo visual

SISTEMA DE VALIDAÇÃO
[ ] Agreement Matrix
[ ] Confidence Modifiers
[ ] Task Thresholds
[ ] Execution Template

CAPACIDADES
[ ] Capabilities bem definidas (mínimo 2)
[ ] Process/Workflow claro
[ ] Knowledge Sources listadas

QUALIDADE
[ ] Padrões de execução (Correto vs Incorreto)
[ ] Troubleshooting comum
[ ] Anti-Patterns documentados
[ ] Quality Checklist

INTEGRAÇÃO
[ ] Registrado no router (.cursor/commands/core/router.md)
[ ] Testado com query de exemplo
[ ] Documentado no CURSOR.md (se aplicável)
```

---

## 🚀 Comandos Úteis

### Testar Agente

```bash
# Invocar agente no chat
@meu-agente-expert como fazer X?
```

### Listar Todos os Agentes

```bash
grep -r "^name:" .cursor/agents/ | sed 's/.*name: //'
```

### Validar Frontmatter YAML

```bash
# Verificar se YAML está válido
python -c "import yaml; yaml.safe_load(open('.cursor/agents/domain/meu-agente.md').read().split('---')[1])"
```

---

## 📚 Próximos Passos

1. **Começe Simples:** Use o template e preencha seções essenciais
2. **Teste Rapidamente:** Invoque o agente e veja se responde bem
3. **Itere:** Adicione mais capacidades conforme necessário
4. **Documente:** Adicione exemplos práticos do seu domínio
5. **Compartilhe:** Se funcionar bem, compartilhe o padrão com a equipe

---

## 🎓 Recursos de Aprendizado

| Recurso | Localização | Use Para |
|---------|-------------|----------|
| **Template Completo** | `.cursor/agents/_template/agent.template.md` | Base para novos agentes |
| **Manual de Agentes** | `MANUAL_AGENTES.md` | Criar estrutura de projeto |
| **Guia Completo** | `docs/GUIA_CRIACAO_AGENTE_PROJETO.md` | Detalhes de implementação |
| **Índice e uso** | `HOW_TO_USE_AGENTS.md` | Listar agentes, `@` e fluxos; atualizar ao adicionar `.md` novos |
| **Agentes Existentes** | `.cursor/agents/**/*.md` | Exemplos práticos (40+ agentes!) |
| **Router** | `.cursor/commands/core/router.md` | Como registrar agentes |

---

## 💬 Resumo Rápido

**Você perguntou:** "Tem um agente que sabe criar outros agentes?"

**Resposta:** ✅ **SIM! Três recursos:**

1. 🎨 **`prompt-crafter`** - Cria instruções interativas para agentes
2. 📚 **`kb-architect`** - Cria bases de conhecimento
3. 📋 **`agent.template.md`** - Template completo para criar agentes

**Para criar um agente novo:**

```bash
# 1. Copie o template
cp .cursor/agents/_template/agent.template.md \
   .cursor/agents/domain/meu-agente.md

# 2. Edite: name, description, capabilities
# 3. Registre no router
# 4. Teste: @meu-agente como fazer X?
```

---

## 🔗 Links Relacionados

- [MANUAL_AGENTES.md](MANUAL_AGENTES.md) - Manual de leitura obrigatória
- [HOW_TO_USE_AGENTS.md](HOW_TO_USE_AGENTS.md) - Índice de agentes e exemplos de invocação
- [docs/GUIA_CRIACAO_AGENTE_PROJETO.md](../docs/GUIA_CRIACAO_AGENTE_PROJETO.md) - Guia completo
- [.cursor/agents/data-engineering/spark-expert-on-premises.md](../.cursor/agents/data-engineering/spark-expert-on-premises.md) - Exemplo de agente *projeto + stack* (Spark on-prem, vault, JDBC)
- [.cursor/agents/_template/agent.template.md](../.cursor/agents/_template/agent.template.md) - Template base
- [.cursor/commands/core/router.md](../.cursor/commands/core/router.md) - Sistema de roteamento

---

**Versão:** 1.0  
**Criado:** Março 2026  
**Última atualização:** Março 2026

---

> **💡 Dica Final:** Comece criando um agente simples e específico. É melhor ter um agente que faz uma coisa muito bem do que um agente genérico que faz muitas coisas mal!

