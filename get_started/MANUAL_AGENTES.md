# 📘 Manual de Leitura Obrigatória: Criação de Projetos com Agentes AI

> **Este é o documento de referência definitivo. Leia antes de criar qualquer novo projeto.**

---

## 🎯 Princípio Fundamental

**Todo projeto deve ser estruturado para que um agente AI possa entender e trabalhar nele desde o primeiro momento.**

### Cursor, Claude Code e GitHub Copilot (este repositório)

Este template pode ser usado com **Cursor**, **Claude Code** e **GitHub Copilot**; as pastas `agents/`, `kb/`, `commands/` e `sdd/` podem existir sob mais de uma raiz:

| Ferramenta | Onde ficam agentes e KB | Instruções de projeto |
|------------|-------------------------|------------------------|
| **Cursor** *(referência principal)* | `.cursor/agents/`, `.cursor/kb/` | `.cursor/CURSOR.MD`, `START_HERE.md`; roteamento: `.cursor/commands/core/router.md` |
| **Claude Code** | `.claude/agents/`, `.claude/kb/` | `CLAUDE.md` → `.claude/CLAUDE.md`; roteamento: `.claude/commands/core/router.md` |
| **VS Code + GitHub Copilot** | `.github/agents/`, `.github/kb/` | `.github/copilot-instructions.md`; roteamento: `.github/commands/core/router.md` |

**Política de pastas:** **`.cursor/`** é a referência principal no fluxo de desenvolvimento documentado aqui. **Não há scripts** que copiem conteúdo entre `.cursor/`, `.claude/` e `.github/`; se o time mantiver mais de uma árvore, **alinhe manualmente** quando necessário.

Mantenha **`CONTEXT.md`** e **`docs/00-INDEX.md`** como âncoras comuns. Para hosts/portas reais (pipelines, Spark on-prem), use o fluxo `docs/inventario-ambiente.md.example` → `docs/inventario-ambiente.md`.

---

## 📁 Estrutura Obrigatória (Mínima)

```
projeto/
├── .cursorrules              # ⚠️ OBRIGATÓRIO
├── CONTEXT.md                # ⚠️ OBRIGATÓRIO
└── docs/
    └── 00-INDEX.md           # ⚠️ OBRIGATÓRIO
```

---

## 📄 1. `.cursorrules` (Raiz)

**Propósito:** Regras que o Cursor lê automaticamente.

**Template Mínimo:**

```markdown
# <Nome do Projeto> - Cursor Rules

## Contexto do Projeto
<1-2 frases descrevendo o projeto>

## Regras de Inicialização
Ao iniciar qualquer chat neste projeto:
1. Leia o arquivo `CONTEXT.md` para obter o contexto rápido
2. Leia `docs/00-INDEX.md` para conhecer a documentação disponível
3. Use o agente `.cursor/agents/<projeto>-expert.md` como referência (se existir)

## Regras de Execução
- <Regra específica 1>
- <Regra específica 2>

## Regras de Código
- Responda sempre em <idioma>
- Siga <padrões>
- Use <tecnologias>

## Knowledge Base
- Documentação: `docs/`
- KB específica: `.cursor/kb/<projeto>/` (se existir)
```

---

## 📄 2. `CONTEXT.md` (Raiz)

**Propósito:** Onboarding rápido - agente entende o projeto em segundos.

**Template Mínimo:**

```markdown
# 🚀 <Nome do Projeto> - Contexto Rápido

## O que é este projeto?
<1 parágrafo explicando o propósito>

## Estrutura Principal
| Componente | Descrição |
|------------|-----------|
| Componente 1 | Descrição 1 |
| Componente 2 | Descrição 2 |

## Comandos Rápidos
\`\`\`bash
# Comando mais comum
comando1
\`\`\`

## Problemas Comuns
| Erro | Causa | Solução |
|------|-------|---------|
| Erro 1 | Causa 1 | Solução 1 |

## Arquivos Importantes
- `docs/arquivo1.md` - Descrição
- `docs/arquivo2.md` - Descrição
```

**Regra de Ouro:** Máximo 150 linhas. Se precisar de mais, coloque links para `docs/`.

---

## 📄 3. `docs/00-INDEX.md`

**Propósito:** Navegação organizada pela documentação.

**Template Mínimo:**

```markdown
# 📚 Índice da Documentação - <Nome do Projeto>

## 🚀 Início Rápido
| Arquivo | Descrição | Quando Usar |
|---------|-----------|-------------|
| [../CONTEXT.md](../CONTEXT.md) | Contexto rápido | Primeira leitura |

## 📖 Guias Essenciais
| Arquivo | Descrição | Quando Usar |
|---------|-----------|-------------|
| [arquivo1.md](arquivo1.md) | Descrição | Quando precisar de X |

## 🎯 Navegação por Tarefa
### "Preciso fazer X"
1. Leia [arquivo1.md](arquivo1.md)
```

---

## 📄 4. `.cursor/agents/<projeto>-expert.md` (Opcional mas Recomendado)

**Propósito:** Define o especialista do projeto.

**Quando Criar:** Projetos médios/grandes (> 5 arquivos principais).

**Template Mínimo:**

```markdown
---
name: <projeto>-expert
description: Especialista em <projeto>. Use para <tópicos>.
tools: Read, Write, Edit, Bash, Grep, Glob
---

Você é um especialista sênior no projeto **<Nome>**.

## Expertise Principal
- <Área 1>
- <Área 2>

## Ações Imediatas
1. Ler `CONTEXT.md` se necessário
2. Buscar KB: `grep -r "termo" .cursor/kb/<projeto>/`
3. Propor solução com comandos

## Padrões de Execução
### ✅ Correto
\`\`\`bash
comando correto
\`\`\`

### ❌ Incorreto
\`\`\`bash
comando incorreto
\`\`\`

## Troubleshooting
### Erro Comum
**Sintoma:** <erro>
**Solução:** <solução>
```

---

## 📄 5. `.cursor/kb/<projeto>/` (Opcional)

**Propósito:** Base de conhecimento técnica para consulta rápida.

**Quando Criar:** Projetos complexos (múltiplos módulos, muitas funcionalidades).

**Estrutura Recomendada:**

```
.cursor/kb/<projeto>/
├── 00-index.md              # Índice da KB
├── 01-architecture.md      # Arquitetura técnica
├── 02-reference.md         # Referência rápida
├── 03-troubleshooting.md   # Soluções diretas
└── 04-execution-patterns.md # Padrões de execução
```

**Diferença Conceitual:**
- `docs/` = Documentação narrativa (para humanos entenderem)
- `.cursor/kb/` = Base de conhecimento técnica (para agente executar)

---

## ✅ Checklist de Criação

### Fase 1: Estrutura Básica (Sempre Fazer)

- [ ] Criar `.cursorrules` na raiz
- [ ] Criar `CONTEXT.md` na raiz
- [ ] Criar `docs/00-INDEX.md`
- [ ] Testar: Abrir projeto no Cursor e pedir para ler `CONTEXT.md`

### Fase 2: Agente Especializado (Projetos Médios/Grandes)

- [ ] Criar `.cursor/agents/<projeto>-expert.md`
- [ ] Definir expertise principal
- [ ] Adicionar padrões de execução
- [ ] Adicionar troubleshooting comum

### Fase 3: Knowledge Base (Projetos Complexos)

- [ ] Criar `.cursor/kb/<projeto>/00-index.md`
- [ ] Criar arquivos de KB por tema
- [ ] Organizar para busca rápida (grep-friendly)

---

## 🎯 Princípios de Design

### 1. Hierarquia de Informação

```
.cursorrules (regras automáticas)
    ↓
CONTEXT.md (contexto rápido)
    ↓
docs/00-INDEX.md (navegação)
    ↓
docs/<arquivos> (detalhes)
    ↓
.cursor/kb/<projeto>/ (conhecimento técnico)
```

### 2. Onboarding Progressivo

- **Nível 1:** `.cursorrules` → Contexto básico
- **Nível 2:** `CONTEXT.md` → Entendimento rápido
- **Nível 3:** `docs/00-INDEX.md` → Navegação
- **Nível 4:** Documentos específicos → Detalhes
- **Nível 5:** KB → Conhecimento técnico profundo

### 3. Separação de Responsabilidades

| Responsabilidade | Onde Colocar |
|------------------|--------------|
| **Educar/Explicar** | `docs/` |
| **Executar/Consultar** | `.cursor/kb/` |
| **Onboarding Rápido** | `CONTEXT.md` |
| **Regras Automáticas** | `.cursorrules` |

---

## 📊 Matriz de Decisão

| Tamanho do Projeto | .cursorrules | CONTEXT.md | 00-INDEX.md | Expert | KB |
|-------------------|--------------|------------|-------------|--------|-----|
| **Pequeno** (< 5 arquivos) | ✅ | ✅ | ✅ | ⚪ | ⚪ |
| **Médio** (5-20 arquivos) | ✅ | ✅ | ✅ | ✅ | ⚪ |
| **Grande** (> 20 arquivos) | ✅ | ✅ | ✅ | ✅ | ✅ |

**Legenda:** ✅ Obrigatório | ⚪ Opcional mas recomendado

---

## 🔄 Fluxo de Trabalho Padrão

### Ao Criar Novo Projeto

1. **Criar estrutura básica**
   ```bash
   mkdir -p projeto/{docs,.cursor/{agents,kb/projeto}}
   ```

2. **Criar arquivos obrigatórios** (em ordem)
   - `.cursorrules`
   - `CONTEXT.md`
   - `docs/00-INDEX.md`

3. **Testar no Cursor**
   - Abrir projeto
   - Pedir: "Leia CONTEXT.md e me explique o projeto"
   - Verificar se entendeu

4. **Criar agente expert** (se projeto médio/grande)
   - `.cursor/agents/<projeto>-expert.md`
   - Testar invocação

5. **Criar KB** (se projeto complexo)
   - `.cursor/kb/<projeto>/`
   - Organizar por temas

---

## 💡 Regras de Ouro

### 1. CONTEXT.md deve ser conciso
- Máximo 150 linhas
- Foco em essencial
- Links para detalhes

### 2. Use tabelas para organização
- Fáceis de ler
- Permitem comparação rápida
- Funcionam bem em markdown

### 3. Seja específico nos exemplos
- Comandos reais e testáveis
- Mostre correto vs incorreto
- Inclua contexto necessário

### 4. Mantenha links atualizados
- Verifique links periodicamente
- Use links relativos
- Teste ao atualizar

### 5. Revise o agente expert regularmente
- Adicione novos padrões aprendidos
- Atualize troubleshooting
- Mantenha exemplos atualizados

---

## 🎓 Diferença Conceitual: docs/ vs .cursor/kb/

### `docs/` = Documentação (Documentation)
- **Conceito:** Memória explícita, conhecimento narrativo
- **Propósito:** Transferir conhecimento para humanos
- **Modelo:** Biblioteca/manual completo
- **Uso:** Leitura e compreensão
- **Formato:** Narrativo, explicativo, com contexto

### `.cursor/kb/` = Base de Conhecimento (Knowledge Base)
- **Conceito:** Memória de trabalho, conhecimento procedural
- **Propósito:** Habilitar execução pelo agente AI
- **Modelo:** Manual de referência rápida
- **Uso:** Consulta e execução
- **Formato:** Técnico, direto, comandos prontos

**Analogia:**
- `docs/` = Manual do usuário (entender)
- `.cursor/kb/` = Cheat sheet (executar)

---

## 📋 Template Rápido de Início

### Passo 1: Criar `.cursorrules`

```markdown
# <Projeto> - Cursor Rules

## Contexto do Projeto
<Descrição>

## Regras de Inicialização
1. Leia `CONTEXT.md`
2. Leia `docs/00-INDEX.md`

## Regras de Código
- Responda em <idioma>
- Siga <padrões>
```

### Passo 2: Criar `CONTEXT.md`

```markdown
# 🚀 <Projeto> - Contexto Rápido

## O que é este projeto?
<Parágrafo>

## Estrutura Principal
| Componente | Descrição |
|------------|-----------|

## Comandos Rápidos
\`\`\`bash
comando
\`\`\`
```

### Passo 3: Criar `docs/00-INDEX.md`

```markdown
# 📚 Índice - <Projeto>

## 🚀 Início Rápido
| Arquivo | Descrição |
|---------|-----------|
| [../CONTEXT.md](../CONTEXT.md) | Contexto rápido |
```

---

## ✅ Checklist Final

Antes de considerar o projeto "pronto":

- [ ] `.cursorrules` criado e testado
- [ ] `CONTEXT.md` criado (< 150 linhas)
- [ ] `docs/00-INDEX.md` criado com links funcionando
- [ ] Agente expert criado (se aplicável)
- [ ] KB criada (se aplicável)
- [ ] Todos os links testados
- [ ] Exemplos funcionam
- [ ] Cursor consegue entender o projeto

---

## 🚀 Próximos Passos

1. **Agora:** Use este manual para criar seu próximo projeto
2. **Depois:** Consulte `docs/GUIA_CRIACAO_AGENTE_PROJETO.md` para detalhes completos
3. **Sempre:** Mantenha `CONTEXT.md` atualizado conforme o projeto evolui

---

## 📚 Referências

- **Guia Completo:** `docs/GUIA_CRIACAO_AGENTE_PROJETO.md`
- **Exemplo Prático:** Este repositório (estrutura com agentes, KB e comandos Cursor)
- **Estrutura Atual:** Veja `.cursorrules`, `CONTEXT.md`, `docs/00-INDEX.md`

---

**Versão:** 1.0  
**Última atualização:** Janeiro 2026

---

> **Este é seu ponto de partida. Consulte sempre antes de criar novos projetos.**

