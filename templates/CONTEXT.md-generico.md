# 🚀 <NOME_DO_PROJETO> — Contexto rápido (template genérico)

> **Use este arquivo para entender rapidamente o projeto antes de começar qualquer tarefa.**  
> **Como usar:** copie para a raiz do repositório como `CONTEXT.md`, substitua `<...>` e remova seções que não se aplicam. **Recomendação:** mantenha enxuto (idealmente **≤ ~150 linhas**); detalhes vão para `docs/`.

---

## O que é este projeto?

<1–3 frases: propósito, para quem é, principal tecnologia ou tipo de sistema (API, lib, pipeline, app, etc.).>

---

## Estrutura principal

> Se não houver “jobs”, use linhas de **módulos**, **serviços** ou **pacotes**.

| Componente | Descrição | Observação (opcional) |
|------------|-----------|------------------------|
| `<nome>` | `<o que faz>` | `<ex.: destino, contrato, owner>` |
| `<nome>` | `<...>` | `<...>` |
| `<nome>` | `<...>` | `<...>` |

---

## Comandos rápidos

```bash
# Tarefa mais comum (ex.: subir ambiente local)
<comando>

# Testes
<comando>

# Build / lint (se existir)
<comando>

# Exemplo com parâmetro importante do projeto
<comando> <flags_ou_args_tipicos>
```

---

## Ambientes

| Código / nome | Uso | Notas |
|---------------|-----|--------|
| `<DEV ou local>` | Desenvolvimento | `<VPN, mock, seed>` |
| `<HML/staging>` | Homologação | `<...>` |
| `<PRD>` | Produção | `<...>` |

---

## Problemas comuns

| Sintoma | Causa provável | Onde agir |
|---------|----------------|-----------|
| `<mensagem ou comportamento>` | `<hipótese>` | `<arquivo, doc ou comando>` |
| Build / CI falha | versão de runtime, cache | `<doc ou pipeline>` |
| Testes flaky | ordem, tempo, dados | `<pasta de testes>` |

---

## Arquivos importantes

| Arquivo | Descrição |
|---------|-----------|
| `README.md` | Visão geral e setup |
| `docs/00-INDEX.md` | Índice da documentação (recomendado) |
| `.cursorrules` | Regras automáticas do Cursor |
| `MANUAL_AGENTES.md` | Manual de estrutura com agentes (se existir no repo) |
| `HOW_TO_USE_AGENTS.md` | Lista de agentes e exemplos com `@` (se existir) |
| `<docs/seu-guia.md>` | `<tema: API, deploy, dados, etc.>` |

### Agentes Cursor (referência rápida)

| Uso | Arquivo |
|-----|---------|
| Domínio / produto (regras do negócio neste repo) | `.cursor/agents/<pasta>/<projeto>-expert.md` |
| Stack técnico (linguagem, framework, plataforma) | `.cursor/agents/<categoria>/<especialista>.md` |
| Lista completa e exemplos com `@` | `HOW_TO_USE_AGENTS.md` |

---

## Pré-requisitos externos (opcional)

> Substitua por: contas, permissões IAM, objetos de banco, filas, buckets, certificados, etc.

### Credenciais / identidade

- **Tipo:** `<service account / usuário técnico / app registration>`
- **Permissões mínimas:** `<resumo>`

### Scripts ou provisionamento

| Artefato | Propósito | Local |
|----------|-----------|--------|
| `<script.sql ou terraform>` | `<...>` | `<caminho>` |

---

## Configurações especiais (opcional)

> Ex.: hosts com regra de rede diferente, portas não padrão, feature flags.

| Contexto | Detalhe |
|----------|---------|
| `<ex.: região, VPN, prefixo DNS>` | `<regra ou exceção>` |

---

## Fluxo de dados ou de requisições (opcional)

```text
<Origem> → <Processamento / API> → <Destino>
```

---

## Infraestrutura relevante (opcional)

> Evite colar segredos. Prefira links internos ou runbooks.

- **Runtime / cluster:** `<nome ou “N/A”>`
- **URLs de observabilidade (não sensíveis):** `<dashboard, tracing>`
- **Onde rodar comandos oficiais:** `<CI, bastion, notebook>`

---

## Verificar logs (opcional)

```bash
# Exemplo genérico — ajuste caminhos
tail -n 100 <caminho_do_log>

grep -i "error\|erro\|fail" <caminho_do_log>
```

---

## Próximos passos recomendados

1. Abrir `docs/00-INDEX.md` (se existir) e escolher o guia da tarefa.
2. Confirmar setup em `README.md` e variáveis em `.env.example`.
3. Para falhas: seguir o runbook em `<docs/troubleshooting.md>` ou equivalente.

---

*Template genérico — personalize e mantenha links relativos corretos após copiar.*
