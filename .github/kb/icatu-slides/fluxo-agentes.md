# Fluxo de agentes — slides Icatu (usabilidade)

> Ordem recomendada para **planear**, **gerar**, **rever** e **corrigir** decks HTML no padrão corporativo **Icatu**, usando apenas a KB `icatu-slides` e os PDFs em `templates/ppts/ICATU/`.

Os exemplos com `@` abaixo usam o prefixo **`.github/`** (referência principal do repositório). No **Claude Code** use `.claude/`; no **Copilot** use `.github/` nos mesmos caminhos relativos a agentes e KB.

## Diagrama do fluxo

```text
                    ┌─────────────────────┐
                    │ icatu-slide-planner │
                    │   (só slide-map)    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ icatu-slide-builder │
                    │   (HTML + CSS/JS)   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ icatu-slide-reviewer │
                    │    (read-only)      │
                    └──────────┬──────────┘
                               │
              ┌────────────────┴────────────────┐
              │ PASS (0 CRITICAL, 0 ERROR)      │ BLOCK / WARNINGs a corrigir
              ▼                                 ▼
         Apresentar /                       ┌─────────────────────┐
         merge opcional                     │ icatu-slide-fixer   │
                                            │ (só mecânico)       │
                                            └──────────┬──────────┘
                                                       │
                                                       ▼
                                            ┌─────────────────────┐
                                            │ icatu-slide-reviewer│
                                            │      (de novo)      │
                                            └─────────────────────┘
```

## Passo a passo (resumo)

| Etapa | Agente (Cursor) | O que faz |
|-------|-----------------|-----------|
| 1 | `@.github/agents/communication/icatu-slide-planner.md` | Produz **slide-map** em Markdown: tipos `slide--icatu-*`, chunks, layout, acentos — **sem HTML**. |
| 2 | `@.github/agents/communication/icatu-slide-builder.md` + `@.github/kb/icatu-slides/` | Gera o **ficheiro HTML** alinhado ao mapa e à KB. |
| 3 | `@.github/agents/communication/icatu-slide-reviewer.md` + ficheiro HTML | **Relatório** só leitura: paleta, marca, motor, pt-BR, checklist PDFs. |
| 4 (se preciso) | `@.github/agents/communication/icatu-slide-fixer.md` + relatório + HTML | **Edits mínimos** (hex, acentos, eventos, etc.). **Não** regerar o deck. |
| 5 | `icatu-slide-reviewer` **outra vez** no mesmo HTML | Confirmar PASS ou iterar até aceitável. |

**Claude Code:** trocar o prefixo `.github/` por `.claude/` nos `@`.  
**GitHub Copilot:** usar `.github/agents/` e `.github/kb/` quando for o fluxo nessa árvore.

## Quando saltar etapas

| Situação | Ajuste |
|----------|--------|
| Deck muito pequeno ou já existe `slide-spec` completo | Pode ir direto ao **builder**, desde que o mapa esteja claro no prompt. |
| Relatório do revisor sem ERROR/CRITICAL | **Fixer** opcional; pode fechar após revisão única. |
| Falta SlideEngine, barra `.icatu-bar` inteira ou slide novo | **Fixer** não substitui o **builder** — voltar ao `icatu-slide-builder` (ou humano). |

## Ficheiros de apoio

| Recurso | Caminho |
|---------|---------|
| KB Icatu (paleta, tipos, template) | `.github/kb/icatu-slides/` |
| PDFs e logo | `templates/ppts/ICATU/` |
| Roteamento geral de agentes | `.github/commands/core/router.md` |
| Índice de agentes na raiz | `HOW_TO_USE_AGENTS.md` (tabela `communication/`) |

## Boas práticas

1. Colar no mesmo fio: **slide-map** (ou caminho `*-slide-spec.md`) + **HTML** quando pedir ao fixer/reviewer contexto completo.
2. Depois do fixer, **sempre** voltar a correr o **reviewer** antes de apresentar a stakeholders.
3. Não usar **aide-slide-*** para corrigir marca Icatu; o fluxo paralelo AIDE está em `HOW_TO_USE_AGENTS.md` e KB `aide-slides`.
