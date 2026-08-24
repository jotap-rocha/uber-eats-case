# Merge do fragmento Dev Loop no AGENT_ROUTER

Após `python install_dev_loop.py`, o instalador copia este pacote para `.{ecosystem}/sdd/architecture/`, incluindo:

- `AGENT_ROUTER_DEVLOOP_FRAGMENT.yaml`
- `AGENT_ROUTER_DEVLOOP_MERGE.md` (este arquivo)

Se o projeto **já tiver** `AGENT_ROUTER.yaml` (template agentic completo), faça o merge manual abaixo. Se **não** tiver roteador, pode renomear o fragmento ou criar um `AGENT_ROUTER.yaml` mínimo só com estes blocos.

## 1. `roster_groups`

Em `AGENT_ROUTER.yaml`, na chave `roster_groups:`, adicione (ou atualize) o grupo:

```yaml
  workflow_dev_loop:
    title_pt: Dev Loop — implementação L2 por fases
    title_en: Dev Loop L2 phased implementation
```

## 2. `agents`

Na lista `agents:`, acrescente os cinco agentes de `AGENT_ROUTER_DEVLOOP_FRAGMENT.yaml` (ou importe o bloco `agents` do fragmento).

**Importante:** ajuste o prefixo `.claude/` nos campos `file:` para o ecossistema instalado (`.claude/`, `.claude/`, `.github/`).

## 3. `intake_hints`

Na lista `intake_hints:`, acrescente a entrada com `primary_workflow.slash: /workflow-dev-loop` e os `context_paths` do fragmento.

## 4. Validação

```bash
python3 scripts/validate-agent-router.py
```

(Requer `AGENT_ROUTER.yaml` completo no projeto; este repositório template já inclui as entradas no roteador canônico.)

## Referências

- Comandos: `.{ecosystem}/commands/workflow-dev-loop/`
- Contrato: `.{ecosystem}/sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml`
- Guia humano: `DEV_LOOP_Guia_Comandos.md` (raiz do projeto, instalado pelo pacote)
