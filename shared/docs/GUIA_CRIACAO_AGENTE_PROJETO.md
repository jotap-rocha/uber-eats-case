# 📘 Guia Completo: Criação de Agentes e Engenharia de Contexto para Projetos

> **Este guia ensina como estruturar qualquer projeto para que o Cursor (ou outros IDEs com AI) atuem como agentes especializados com contexto rico.**

---

## 🎯 Objetivo

Criar uma estrutura de arquivos que permita:
- ✅ Onboarding rápido do agente AI (entender o projeto em segundos)
- ✅ Contexto rico e organizado para consulta
- ✅ Troubleshooting eficiente
- ✅ Documentação navegável e acessível
- ✅ Agente especializado que conhece o projeto profundamente

---

## 📁 Estrutura de Arquivos Obrigatória

### Estrutura Mínima (Projetos Simples)

```
projeto/
├── .cursorrules              # ⚠️ OBRIGATÓRIO - Regras automáticas
├── CONTEXT.md                # ⚠️ OBRIGATÓRIO - Contexto rápido
└── docs/
    └── 00-INDEX.md           # ⚠️ OBRIGATÓRIO - Índice da documentação
```

### Estrutura Completa (Projetos Médios/Grandes)

```
projeto/
├── .cursorrules              # ⚠️ OBRIGATÓRIO
├── CONTEXT.md                # ⚠️ OBRIGATÓRIO
├── README.md                 # Documentação principal
├── docs/
│   ├── 00-INDEX.md           # ⚠️ OBRIGATÓRIO
│   ├── architecture.md       # Arquitetura do projeto
│   ├── getting-started.md    # Guia de início rápido
│   ├── troubleshooting.md   # Resolução de problemas
│   └── ...                   # Outros documentos
└── .cursor/
    ├── agents/
    │   └── <projeto>-expert.md   # ⭐ Agente especializado
    └── kb/
        └── <projeto>/            # ⭐ Knowledge Base
            ├── 00-index.md
            ├── 01-architecture.md
            ├── 02-reference.md
            ├── 03-troubleshooting.md
            └── ...
```

---

## 📄 1. `.cursorrules` (Raiz do Projeto)

### Propósito
Arquivo que o Cursor lê **automaticamente** ao abrir o projeto. Define as regras de comportamento do agente.

### Template

```markdown
# <Nome do Projeto> - Cursor Rules

## Contexto do Projeto
<1-2 frases descrevendo o que é o projeto>

## Regras de Inicialização
Ao iniciar qualquer chat neste projeto:
1. Leia o arquivo `CONTEXT.md` para obter o contexto rápido
2. Leia `docs/00-INDEX.md` para conhecer a documentação disponível
3. Use o agente `.cursor/agents/<projeto>-expert.md` como referência (se existir)

## Regras de Execução
- <Regra específica 1>
- <Regra específica 2>
- <Regra específica 3>

## Regras de Código
- Responda sempre em <idioma>
- Siga <padrões de código>
- Use <tecnologias/frameworks>
- Prefira <abordagem A> sobre <abordagem B>

## Knowledge Base
- Documentação do projeto: `docs/`
- KB específica: `.cursor/kb/<projeto>/` (se existir)
- KB externa: `.cursor/kb/<tecnologia>/` (se existir)
```

### Exemplo Real

```markdown
# SQL Server Capacity Evolution - Cursor Rules

## Contexto do Projeto
Este é o projeto **SQL Server Capacity Evolution** - um pipeline PySpark para coleta e consolidação de metadados de instâncias SQL Server.

## Regras de Inicialização
Ao iniciar qualquer chat neste projeto:
1. Leia o arquivo `CONTEXT.md` para obter o contexto rápido
2. Leia `docs/00-INDEX.md` para conhecer a documentação disponível
3. Use o agente `.cursor/agents/sql-capacity-expert.md` como referência

## Regras de Execução
- O parâmetro `--instancia` NÃO deve conter domínio (.DRMTZ.COM.BR)
- Formato correto: `SERVIDOR\MSSQLSERVER`
- Logs estão em: `logs/<job_name>/YYYY-MM-DD.txt`

## Regras de Código
- Responda sempre em português brasileiro
- Siga Clean Code e SOLID
- Use type hints em Python
- Prefira DataFrame API sobre RDD

## Knowledge Base
- Documentação do projeto: `docs/`
- KB específica: `.cursor/kb/sql-capacity/`
- KB Spark: `.cursor/kb/spark/`
```

---

## 📄 2. `CONTEXT.md` (Raiz do Projeto)

### Propósito
Onboarding rápido - permite que o agente entenda o projeto em **segundos**.

### Template

```markdown
# 🚀 <Nome do Projeto> - Contexto Rápido

> **Use este arquivo para entender rapidamente o projeto antes de começar qualquer tarefa.**

## O que é este projeto?

<1 parágrafo explicando o propósito do projeto>

## Estrutura Principal

| Componente | Descrição |
|------------|-----------|
| Componente 1 | Descrição 1 |
| Componente 2 | Descrição 2 |
| Componente 3 | Descrição 3 |

## Comandos Rápidos

\`\`\`bash
# Comando mais comum 1
comando1

# Comando mais comum 2
comando2
\`\`\`

## Ambientes/Configurações

| Ambiente | Descrição |
|----------|-----------|
| DEV | Desenvolvimento |
| PROD | Produção |

## Problemas Comuns

| Erro | Causa Provável | Solução |
|------|----------------|---------|
| Erro 1 | Causa 1 | Solução 1 |
| Erro 2 | Causa 2 | Solução 2 |

## Arquivos Importantes

| Arquivo | Descrição |
|---------|-----------|
| `docs/arquivo1.md` | Descrição 1 |
| `docs/arquivo2.md` | Descrição 2 |

## Próximos Passos Recomendados

1. Leia `docs/00-INDEX.md` para navegar pela documentação
2. Consulte `docs/getting-started.md` para começar
3. Use `docs/troubleshooting.md` para resolver problemas
```

### Exemplo Real

```markdown
# 🚀 SQL Server Capacity Evolution - Contexto Rápido

> **Use este arquivo para entender rapidamente o projeto antes de começar qualquer tarefa.**

## O que é este projeto?

Pipeline PySpark que coleta metadados de múltiplas instâncias SQL Server e consolida em um banco de dados centralizado.

## Estrutura de Jobs

| Job | Descrição | Tabela Destino |
|-----|-----------|----------------|
| 00 | Carrega servidores do Oracle APEX | DataBaseSqlServerDatabaseSourceFromApex |
| 01 | Informações básicas SQL Server | DatabaseSQLServerInfo |
| 02 | Espaço em disco | DatabaseServerDiskSpaceInfo |

## Comandos Rápidos

\`\`\`bash
# Executar job específico para HMG
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh

# Reexecutar servidor específico (SEM domínio)
bash scripts/HMG/run_hmg__01_app_obter_info_sql_server__01.sh \
  --instancia "SERVIDOR\MSSQLSERVER"
\`\`\`

## Problemas Comuns

| Erro | Causa Provável | Solução |
|------|----------------|---------|
| "Falha na leitura" | Objeto SQL ausente | Executar scripts `src/queries/08, 10, 11*.sql` |
| "Falha na leitura" | Firewall | Liberar conectividade de rede |
```

---

## 📄 3. `docs/00-INDEX.md` (Índice da Documentação)

### Propósito
Navegação organizada pela documentação - permite encontrar rapidamente o documento certo.

### Template

```markdown
# 📚 Índice da Documentação - <Nome do Projeto>

> **Use este índice para navegar rapidamente pela documentação do projeto.**

---

## 🚀 Início Rápido

| Arquivo | Descrição | Quando Usar |
|---------|-----------|-------------|
| [../CONTEXT.md](../CONTEXT.md) | Contexto rápido do projeto | Primeira leitura, onboarding |
| [getting-started.md](getting-started.md) | Guia de início rápido | Começar a usar o projeto |

---

## 📖 Guias Essenciais

| Arquivo | Descrição | Quando Usar |
|---------|-----------|-------------|
| [architecture.md](architecture.md) | Arquitetura do projeto | Entender estrutura |
| [troubleshooting.md](troubleshooting.md) | Resolução de problemas | Quando algo não funciona |
| [api-reference.md](api-reference.md) | Referência da API | Consultar APIs |

---

## ⚙️ Operações

| Arquivo | Descrição | Quando Usar |
|---------|-----------|-------------|
| [deployment.md](deployment.md) | Guia de deploy | Fazer deploy |
| [configuration.md](configuration.md) | Configurações | Configurar ambiente |

---

## 🗂️ Navegação por Tarefa

### "Preciso executar X"
1. Leia [arquivo1.md](arquivo1.md)
2. Consulte [arquivo2.md](arquivo2.md)

### "Algo não está funcionando"
1. Siga [troubleshooting.md](troubleshooting.md)
2. Verifique [logs.md](logs.md)

### "Preciso entender a arquitetura"
1. Comece com [architecture.md](architecture.md)
2. Depois leia [design-decisions.md](design-decisions.md)

---

## 📋 Referência Rápida

| Tópico | Arquivo |
|--------|---------|
| Comandos | [commands.md](commands.md) |
| Configuração | [config.md](config.md) |
| API | [api.md](api.md) |

---

*Última atualização: <Data>*
```

---

## 📄 4. `.cursor/agents/<projeto>-expert.md` (Agente Especializado)

### Propósito
Define a "persona" especialista do projeto - o agente sabe tudo sobre o projeto.

### Template

```markdown
---
name: <projeto>-expert
description: <Descrição do especialista>. Use proativamente para questões sobre <tópicos principais>.
tools: Read, Write, Edit, Bash, Grep, Glob, TodoWrite, WebSearch
---

Você é um especialista sênior no projeto **<Nome do Projeto>**, <descrição do projeto>.

## Expertise Principal

### 1. <Área de Conhecimento 1>
- <Conhecimento específico 1>
- <Conhecimento específico 2>
- <Conhecimento específico 3>

### 2. <Área de Conhecimento 2>
- <Conhecimento específico 1>
- <Conhecimento específico 2>

### 3. <Área de Conhecimento 3>
- <Conhecimento específico 1>
- <Conhecimento específico 2>

## Ações Imediatas ao Ser Invocado

1. **Verificar contexto**: Ler `CONTEXT.md` se necessário
2. **Buscar KB**: `grep -r "termo" .cursor/kb/<projeto>/`
3. **Analisar logs**: Se erro reportado, verificar `logs/`
4. **Propor solução**: Com comandos específicos e código

## Padrões de Execução

### Exemplo Correto

\`\`\`bash
# CORRETO - forma recomendada
comando correto
\`\`\`

### Exemplo Incorreto

\`\`\`bash
# ERRADO - forma não recomendada
comando incorreto
\`\`\`

## Troubleshooting

### Erro Comum 1

**Sintoma:** <descrição do erro>

**Causa:** <causa provável>

**Solução:**
1. Passo 1
2. Passo 2
3. Passo 3

### Erro Comum 2

**Sintoma:** <descrição do erro>

**Causa:** <causa provável>

**Solução:**
1. Passo 1
2. Passo 2

## Checklist de Troubleshooting

1. [ ] Verificar <item 1>
2. [ ] Verificar <item 2>
3. [ ] Verificar <item 3>
4. [ ] Aplicar solução
5. [ ] Verificar sucesso

## Knowledge Base

- Projeto: `.cursor/kb/<projeto>/`
- Docs: `docs/`

## Respostas em <Idioma>

Sempre responda em **<idioma>**, com:
- Comandos completos e testáveis
- Explicações claras e objetivas
- Referências aos arquivos de documentação relevantes

## Referências

- README.md - Documentação principal
- docs/<arquivo1>.md - <Descrição>
- docs/<arquivo2>.md - <Descrição>
```

---

## 📄 5. `.cursor/kb/<projeto>/` (Knowledge Base)

### Propósito
Base de conhecimento técnica detalhada para consulta rápida.

### Estrutura Recomendada

```
.cursor/kb/<projeto>/
├── 00-index.md              # Índice da KB
├── 01-architecture.md       # Arquitetura detalhada
├── 02-reference.md          # Referência técnica
├── 03-troubleshooting.md    # Troubleshooting detalhado
├── 04-execution-patterns.md # Padrões de execução
└── 05-<tema>.md             # Outros temas específicos
```

### Template para Arquivo de KB

```markdown
# <Título> - <Nome do Projeto>

## Visão Geral

<Descrição geral do tópico>

## Detalhes

### Subtópico 1

<Conteúdo detalhado>

### Subtópico 2

<Conteúdo detalhado>

## Exemplos

\`\`\`<linguagem>
# Exemplo prático
código de exemplo
\`\`\`

## Referências

- [Link 1](url)
- [Link 2](url)
```

---

## ✅ Checklist de Criação

### Fase 1: Estrutura Básica (Obrigatória)

- [ ] Criar `.cursorrules` na raiz
- [ ] Criar `CONTEXT.md` na raiz
- [ ] Criar `docs/00-INDEX.md`
- [ ] Testar se o Cursor lê os arquivos corretamente

### Fase 2: Agente Especializado (Recomendado)

- [ ] Criar `.cursor/agents/<projeto>-expert.md`
- [ ] Definir expertise principal
- [ ] Adicionar padrões de execução
- [ ] Adicionar troubleshooting comum
- [ ] Testar invocação do agente

### Fase 3: Knowledge Base (Projetos Complexos)

- [ ] Criar `.cursor/kb/<projeto>/00-index.md`
- [ ] Criar arquivos de KB específicos
- [ ] Organizar por temas
- [ ] Adicionar exemplos práticos

### Fase 4: Documentação Complementar

- [ ] Criar `docs/architecture.md`
- [ ] Criar `docs/getting-started.md`
- [ ] Criar `docs/troubleshooting.md`
- [ ] Atualizar `docs/00-INDEX.md` com links

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
docs/<arquivos específicos> (detalhes)
    ↓
.cursor/kb/<projeto>/ (conhecimento técnico profundo)
```

### 2. Onboarding Progressivo

- **Nível 1:** `.cursorrules` → Contexto básico
- **Nível 2:** `CONTEXT.md` → Entendimento rápido
- **Nível 3:** `docs/00-INDEX.md` → Navegação
- **Nível 4:** Documentos específicos → Detalhes
- **Nível 5:** KB → Conhecimento técnico profundo

### 3. Buscabilidade

- Use tabelas para organização
- Use índices navegáveis
- Use grep-friendly (termos chave claros)
- Use links entre documentos

### 4. Manutenibilidade

- Mantenha `CONTEXT.md` atualizado
- Atualize `docs/00-INDEX.md` ao adicionar docs
- Revise o agente expert periodicamente
- Mantenha KB sincronizada com código

---

## 📊 Matriz de Decisão: Quando Criar Cada Arquivo

| Tamanho do Projeto | .cursorrules | CONTEXT.md | 00-INDEX.md | Expert | KB |
|-------------------|--------------|------------|-------------|--------|-----|
| **Pequeno** (< 5 arquivos) | ✅ | ✅ | ✅ | ⚪ | ⚪ |
| **Médio** (5-20 arquivos) | ✅ | ✅ | ✅ | ✅ | ⚪ |
| **Grande** (> 20 arquivos) | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Complexo** (múltiplos módulos) | ✅ | ✅ | ✅ | ✅ | ✅ |

**Legenda:**
- ✅ Obrigatório
- ⚪ Opcional mas recomendado

---

## 🔄 Fluxo de Trabalho Recomendado

### Ao Criar Novo Projeto

1. **Criar estrutura básica**
   ```bash
   mkdir -p projeto/{docs,.cursor/{agents,kb/projeto}}
   ```

2. **Criar arquivos obrigatórios**
   - `.cursorrules`
   - `CONTEXT.md`
   - `docs/00-INDEX.md`

3. **Testar no Cursor**
   - Abrir projeto no Cursor
   - Verificar se lê `.cursorrules`
   - Pedir para ler `CONTEXT.md`
   - Verificar se entende o projeto

4. **Criar agente especializado** (se projeto médio/grande)
   - `.cursor/agents/<projeto>-expert.md`
   - Testar invocação do agente

5. **Criar KB** (se projeto complexo)
   - `.cursor/kb/<projeto>/`
   - Organizar por temas

### Ao Adicionar Nova Funcionalidade

1. Atualizar `CONTEXT.md` se necessário
2. Adicionar documentação em `docs/`
3. Atualizar `docs/00-INDEX.md`
4. Atualizar agente expert se necessário
5. Adicionar à KB se for conhecimento técnico profundo

---

## 💡 Dicas e Boas Práticas

### 1. Mantenha CONTEXT.md Conciso
- Máximo 150 linhas
- Foco em informações essenciais
- Links para detalhes em vez de explicar tudo

### 2. Use Tabelas para Organização
- Tabelas são fáceis de ler e navegar
- Permitem comparação rápida
- Funcionam bem em markdown

### 3. Seja Específico nos Exemplos
- Use comandos reais e testáveis
- Mostre formato correto vs incorreto
- Inclua contexto necessário

### 4. Mantenha Links Atualizados
- Verifique links periodicamente
- Use links relativos quando possível
- Teste links ao atualizar documentação

### 5. Revise o Agente Expert Regularmente
- Adicione novos padrões aprendidos
- Atualize troubleshooting com novos erros
- Mantenha exemplos atualizados

---

## 🎓 Exemplos de Uso

### Exemplo 1: Projeto Python Simples

```
projeto-python/
├── .cursorrules          # Regras: Python 3.9+, pytest, type hints
├── CONTEXT.md            # API REST simples, FastAPI
├── docs/
│   └── 00-INDEX.md       # Links para docs de API, testes, deploy
└── src/
    └── ...
```

### Exemplo 2: Projeto Data Pipeline Complexo

```
projeto-pipeline/
├── .cursorrules          # Regras: Spark, Airflow, SQL
├── CONTEXT.md            # Pipeline ETL, 8 jobs, múltiplos ambientes
├── docs/
│   ├── 00-INDEX.md
│   ├── architecture.md
│   ├── troubleshooting.md
│   └── ...
└── .cursor/
    ├── agents/
    │   └── pipeline-expert.md
    └── kb/
        └── pipeline/
            ├── 00-index.md
            ├── 01-jobs.md
            ├── 02-troubleshooting.md
            └── ...
```

---

## 📚 Referências e Recursos

- [Cursor Documentation](https://cursor.sh/docs)
- [Markdown Guide](https://www.markdownguide.org/)
- [Documentation Best Practices](https://www.writethedocs.org/guide/)

---

## ✅ Checklist Final

Antes de considerar o projeto "pronto" para uso com agente:

- [ ] `.cursorrules` criado e testado
- [ ] `CONTEXT.md` criado e atualizado
- [ ] `docs/00-INDEX.md` criado com links funcionando
- [ ] Agente expert criado (se aplicável)
- [ ] KB criada (se aplicável)
- [ ] Todos os links testados
- [ ] Exemplos funcionam
- [ ] Documentação revisada por outra pessoa (se possível)

---

**Última atualização:** Janeiro 2026  
**Versão:** 1.0

---

*Este guia foi criado baseado nas melhores práticas de engenharia de contexto para projetos com agentes AI. Use como referência para estruturar seus projetos futuros.*

