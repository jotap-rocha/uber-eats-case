---
name: adversarial-judge
description: >-
  Chama um segundo modelo LLM via OpenRouter (diferente do que gerou o plano) para contestar
  um artefato do fluxo /novo-projeto — grill (01-grill.md) ou PRD (02-prd.md) — antes de seguir
  pra próxima fase. Acha suposição errada, lacuna, e alternativa não considerada; sempre
  consultivo, nunca bloqueia. Use quando harness-define ou harness-design perguntarem se o
  usuário quer rodar o judge, ou quando o usuário pedir diretamente "roda um segundo modelo
  nesse plano", "quero uma segunda opinião via openrouter", "contesta esse PRD".
---

# Adversarial Judge

Segunda opinião de um modelo diferente (via OpenRouter) sobre um plano já escrito. O objetivo
é reduzir o viés de auto-confirmação: o mesmo modelo que escreveu o plano tende a concordar
consigo mesmo quando revisa. **Sempre opcional, sempre consultivo** — o resultado é uma lista
de objeções pra você julgar, nunca um gate automático.

## Pré-requisitos

- `OPENROUTER_API_KEY` — crie em [openrouter.ai/keys](https://openrouter.ai/keys). Nunca
  hardcoded — via variável de ambiente ou `.env` na raiz do repo (já no `.gitignore`).
- `OPENROUTER_JUDGE_MODEL` — o modelo a usar (ex.: um modelo de raciocínio forte de outro
  fornecedor, diferente do que gerou o plano — o ponto é diversidade de viés). Escolha em
  [openrouter.ai/models](https://openrouter.ai/models). Sem default embutido — o script não
  chuta um modelo, porque um chute pode ficar inválido/desatualizado; a escolha é sua.

Se qualquer uma faltar, o script falha com uma mensagem explicando o que configurar.

## Processo

1. Confirme que o artefato a contestar existe (`01-grill.md` ou `02-prd.md`, path completo do
   projeto em `.claude/projetos/{slug}/`).
2. Rode:
   ```bash
   python3 .claude/skills/adversarial-judge/scripts/run_judge.py \
     --artifact <path-do-artefato> \
     --output <path-do-artefato-sem-extensao>b-judge.md
   ```
   Exemplos de nome de saída: `01-grill.md` → `01b-judge.md`; `02-prd.md` → `02b-judge.md`.
3. Mostre a crítica completa ao usuário no chat — não resuma, não filtre. É ele quem decide
   o que incorporar de volta no artefato original.
4. Não edite o artefato original automaticamente. Se o usuário pedir pra incorporar algum
   ponto da crítica, edite manualmente e registre a origem (`via adversarial-judge`) na seção
   alterada.

## Quando NÃO usar

- Sem `OPENROUTER_API_KEY` / `OPENROUTER_JUDGE_MODEL` configuradas — não insista; informe como
  configurar e siga o fluxo normalmente sem o judge.
- Artefato ainda incompleto (grill com pergunta em aberto, PRD sem seção) — contestar plano
  incompleto gera ruído; termine o artefato primeiro.
- Falha de rede/API — reporte o erro do script ao usuário e siga sem bloquear o fluxo; isso
  nunca é motivo pra travar `harness-define` ou `harness-design`.
