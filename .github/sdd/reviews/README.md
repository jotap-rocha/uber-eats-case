# Workflow MakeApp Review

Revisão **por lane** com estado em disco — **uma lane por conversa/comando** para controlar contexto e tokens.

## Localização

```text
.github/sdd/reviews/{RUN_ID}/
  REVIEW_MANIFEST.yaml   # estado enxuto (status por lane)
  REVIEW_LOG.md          # histórico curto por rodada
  REVIEW_SUMMARY.md      # consolidado de todas as lanes (gerado ao concluir a lane ui_ux)
  lanes/
    backend.md
    frontend.md
    security.md
    databricks.md
    performance.md
    ui_ux.md
```

## Comandos Cursor

Definição canônica: `.github/commands/workflow-makeapp-review/workflow-makeapp-review.md` (entrada) e `reviewer-*.md` (atalhos em `commands/review/reviewer-*.md` apontam para `workflow-makeapp-review/`).

| Comando | Função |
|---------|--------|
| `/workflow-makeapp-review` | Visão geral e ordem dos passos (roteador) |
| `/reviewer-init` | Cria `RUN_ID`, manifest e stubs de lanes |
| `/reviewer-lane` | Revisa **uma** lane; ao terminar indica o **próximo** `/reviewer-lane` ou, após `ui_ux`, gera `REVIEW_SUMMARY.md` e indica round/fixer/init |
| `/reviewer-round` | Revalida pendências e procura achados novos (incremental) |
| `/reviewer-fixer` | Correções guiadas pelo usuário + atualiza manifest/log |

## Nova rodada só para uma lane (ex.: `security`)

Quando o manifest já marca uma lane como **`pass`** mas queres **rever só essa dimensão** ou **procurar regressões**, tens duas abordagens:

### 1. `/reviewer-round <RUN_ID>` — passagem incremental (leve)

- Por defeito o agente **só reabre** lanes com estado `fail`, `pending` ou `in_progress`.
- Lanes em **`pass`** **não** entram sem gatilho (evita trabalho duplicado).
- Para **incluir uma lane já `pass`** (por exemplo `security`), na **mesma mensagem** do comando:
  - pede explicitamente: *incluir lane `security` para nova varredura*; **e/ou**
  - cola um **`git diff`** ou lista **arquivos alterados** desde a última revisão.

O round repete **checks rasos** do contrato + **greps** (secrets, SQL, `innerHTML`, etc.), **incrementa** `round` no manifest, **acrescenta** novos findings (novos IDs, sem renumerar os antigos) e regista no `REVIEW_LOG.md`.

### 2. `/reviewer-lane <RUN_ID> <lane_id>` — revisão completa da dimensão

- Ex.: `/reviewer-lane rev-2026-04-30-layout-databricks security`
- Volta a correr a lane **de ponta a ponta** (KB, checklist, amostragem no escopo da lane).
- Útil para **auditoria mais profunda** ou para alinhar `lanes/<lane>.md` ao código **após vários fixers**.

### Onde ver o que já foi feito

- Estado por lane: `REVIEW_MANIFEST.yaml`
- Detalhe e histórico de findings: `lanes/<lane>.md` e `REVIEW_LOG.md`
- **`REVIEW_SUMMARY.md`** só reflete o consolidado até à última conclusão da lane `ui_ux`; após mudanças grandes, volta a correr `/reviewer-lane … ui_ux` ou atualiza o sumário à mão.

## Contrato de lanes

Ver [`.github/sdd/architecture/WORKFLOW_MAKEAPP_REVIEW_CONTRACTS.yaml`](../architecture/WORKFLOW_MAKEAPP_REVIEW_CONTRACTS.yaml).

## Relação com SDD

O pipeline **Brainstorm → Define → Design → Build → Ship** continua em `.github/commands/workflow/`.  
Este fluxo é **ortogonal**: gates de qualidade/revisão por dimensão, sem substituir o SDD.
