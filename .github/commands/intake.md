---
name: intake
description: |
  Triagem, execução multi-agente (até 3 em paralelo) e resposta consolidada.
  Classifica a pergunta, escolhe agentes, executa cada um e sintetiza achados numa resposta completa.
---

# `/intake` — Triagem, execução e síntese

**Arquivo canônico:** `.github/commands/intake.md` (este documento).

**Fonte única de dados:** [`.github/sdd/architecture/AGENT_ROUTER.yaml`](../sdd/architecture/AGENT_ROUTER.yaml) — hints, roster, contrato `intake_contract` e regras de síntese.

**Diferença de `/core/agent`:** este comando **não altera** nem substitui `/core/agent`. O `/intake` foca em **vários agentes quando necessário**, execução **paralela** (quando possível) e **resposta consolidada** na mesma conversa.

## Uso

```text
/intake
/intake <pergunta ou objetivo em texto livre>
```

- Só **`/intake`**: pedir **uma** frase com o objetivo.
- **`/intake` + texto**: executar o fluxo completo abaixo.

## Contrato (obrigatório)

Siga **`intake_contract`** no YAML (`mode: execute_and_synthesize`):

| Parâmetro | Valor |
|-----------|--------|
| `min_agents` | 1 |
| `max_agents_parallel` | 3 |
| `max_context_paths` | 3 |

Passos (`intake_contract.steps`):

1. **`read_user_intent`** — Ler pergunta (ou pedir uma frase).
2. **`classify_one_line`** — Uma linha de classificação temática.
3. **`select_agents`** — Escolher **1 a 3** `agents[].id` que realmente ajudem (não fixar em dois). Usar `intake_hints`, [router.md](core/router.md) e cruzamento de domínios. Se um agente basta, use 1; se a pergunta cruza Spark + Databricks + segurança, use até 3.
4. **`list_context_paths`** — Unir `context_paths` das hints aplicáveis (máx. 3 paths únicos).
5. **`execute_agents_parallel`** — Executar **cada** agente selecionado (ver § Execução).
6. **`synthesize_response`** — Consolidar achados com `intake_contract.synthesis.rules_pt` e responder ao usuário.
7. **`optional_follow_up`** — Só se faltar workflow estruturado (RUN_ID, PR, SDD); senão **omitir** a secção.

## Seleção de agentes (`select_agents`)

- Todo `id` deve existir em `agents[]` no YAML; mencionar como **`@{id}`** (`conventions.mention_format`).
- **Não** limitar a primário + secundário: liste todos os participantes (1–3).
- Priorizar hints com `signals_pt` compatíveis; em empate, preferir o mais especializado no subdomínio.
- Se `primary_workflow` for o melhor encaminhamento (revisão por lanes, Dev Loop, SDD), inclua na síntese a recomendação do **`slash`**, mas **ainda execute** os agentes escolhidos para responder à pergunta atual (salvo se o usuário só pediu “qual comando usar”).
- Fallback: `intake_fallback.primary_agent_id`.

## Execução (`execute_agents_parallel`)

Para **cada** `agent_id` selecionado, obter `agents[].file` no YAML e executar **como esse agente** (papel, escopo, KB do arquivo e dos `context_paths`).

### Preferência: Task em paralelo

Se a ferramenta **Task** estiver disponível (modo Agent no Cursor):

1. No **mesmo turno**, dispare **uma Task por agente** (até `max_agents_parallel`), com `run_in_background: true` quando fizer sentido aguardar em lote.
2. Use `subagent_type` alinhado ao domínio quando existir no projeto (ex.: `spark-expert`, `databricks-data-engineer`, `code-reviewer`); caso contrário `intake_contract.parallel_execution.task_subagent_default` (`generalPurpose`).
3. Prompt de cada Task (template):

```text
Você executa APENAS como o agente @{agent_id} deste repositório.
Leia e siga integralmente: {agents[].file}
Consulte se necessário: {context_paths list}
Pergunta do usuário: {texto}
Responda SOMENTE com achados estruturados (tópicos, evidências, riscos, recomendações).
Não sintetize outros agentes. Idioma: pt-BR.
```

4. Aguarde **todas** as Tasks antes da síntese.

### Fallback: sequencial na mesma conversa

Se Task **não** estiver disponível (`intake_contract.parallel_execution.fallback_sequential`):

1. Para cada agente, **na ordem** escolhida: abrir `agents[].file`, carregar KB/paths relevantes, produzir achados na subsecção `### @{id}`.
2. Não pular agentes selecionados.

## Síntese (`synthesize_response`)

Aplicar **`intake_contract.synthesis.rules_pt`**:

- Integrar achados de **todos** os agentes executados numa **resposta completa** à pergunta original.
- Resolver conflitos por evidência (KB, código, contratos); dar peso ao `domain/*-expert` quando aplicável.
- Não repetir integralmente cada subsecção — destilar o que importa para o usuário.

## Formato de resposta (obrigatório)

```markdown
## Classificação
<uma linha>

## Agentes envolvidos
- `@id1` — <papel nesta pergunta>
- `@id2` — …
_(até 3)_

## Contexto consultado
1. `path/um`
2. `path/dois`
_(3 opcional)_

## Achados por agente

### `@id1`
<achados deste agente>

### `@id2`
…

## Resposta consolidada
<resposta completa ao usuário — principal entregável>

## Próximo passo (opcional)
<uma linha só se restar workflow/PR/SDD; omitir secção se a pergunta já estiver respondida>
```

## Roteamento e validação

- Hints: `intake_hints` · Fallback: `intake_fallback` · Router detalhado: [core/router.md](core/router.md)
- Validação: `python3 scripts/validate-agent-router.py`

## Relação com outros comandos

| Comando | Uso |
|---------|-----|
| `/core/agent` | Um agente, roteamento simples — **não modificado** por este fluxo |
| **Upgrade agentic** | Projeto já agentic: triagem com `/intake` + CLI em [`AGENTIC_UPGRADE_Guia.md`](../../get_started/AGENTIC_UPGRADE_Guia.md) (`upgrade_agentic.py` audit → apply → validate) |
| `/workflow-makeapp-review` | Revisão por lanes após resposta exploratória |
| `/workflow-data-pipeline-review` | Revisão de pipeline por lanes |
| `/workflow-dev-loop` | Implementação L2 com PROMPT |
| `/brainstorm` … `/ship` | SDD L3 |

### Upgrade de projeto agentic (complemento ao `/intake`)

O `/intake` **não executa** o upgrade no disco. Para **atualizar** um projeto local com merge a partir deste template:

1. **Explorar** (opcional): `/intake O que falta no meu .github/ comparado ao template?`
2. **Auditar:** `python3 …/agentspec/upgrade_agentic.py --target <destino> --source <template> --dry-run`
3. **Aplicar:** mesmo comando com `--apply`
4. **Validar:** `python3 scripts/validate-agent-router.py` no destino
5. **Conflitos:** `/dev tasks/PROMPT_UPGRADE_AGENTIC.md`

Guia completo: [`AGENTIC_UPGRADE_Guia.md`](../../get_started/AGENTIC_UPGRADE_Guia.md) em `get_started/`.

## Limitações

- Até **3** agentes por rodada (`max_agents_parallel`) para controlar custo e contexto.
- Tasks paralelas dependem do modo Agent e da ferramenta Task no Cursor.
- Não executa código no repositório salvo se um agente assim o exigir no seu `.md`; o intake **orquestra** agentes, não substitui ferramentas deles.
