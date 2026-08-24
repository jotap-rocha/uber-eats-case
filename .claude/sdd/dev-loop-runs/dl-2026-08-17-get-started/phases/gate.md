# Phase: **gate** — **Gate L2 vs L3**

**Run:** `dl-2026-08-17-get-started`
**Manifest:** estado canônico em `../DEVLOOP_MANIFEST.yaml` (`phases.gate.status`).

## Sumário (enxuto)

- Status: `pass`
- Decisão: `continue_l2`
- Artefato principal: este arquivo (`phases/gate.md`)
- Última atualização: 2026-08-17T00:00:00Z (registrado nesta fase)

## Cenário avaliado

Organizar os arquivos `.md` introdutórios da raiz do repositório (~11 arquivos: `AGENTIC_UPGRADE_Guia.md`,
`COMO_TORNAR_PROJETO_AGENTIC.md`, `copilot-instructions.md`, `CRIAR_AMBIENTE_VIRTUAL.md`,
`DEV_LOOP_Guia_Comandos.md`, `HOW_TO_MAKE_NEW_AGENT.md`, `HOW_TO_USE_AGENTS.md`, `MANUAL_AGENTES.md`,
`SDD_Guia_Comandos.md`, `START_HERE.md`, mantendo `README.md` e `CLAUDE.md` na raiz) em uma pasta
`get_started/`, atualizando os links internos que os referenciam e reduzindo a poluição visual da raiz.

## Decisão: `continue_l2`

## Justificativa

Comparando com `l2_vs_l3_gate` do CONTRACTS:

- **Aponta para L2** (`single_component_features`, `utilities_parsers`): a tarefa é uma reorganização de
  arquivos estática (mover markdown + ajustar links), escopo único e bem definido, sem ambiguidade de
  produto, sem decisões de arquitetura de sistema, sem múltiplos componentes de código interagindo.
- **Não se enquadra em L3**: não é `multi_component_features` (não há integração entre sistemas/serviços),
  não é `production_systems` em sentido de runtime/infra, não exige `team_projects_full_audit` nem
  `full_audit_trail_required` — é uma tarefa de organização documental/estrutural, reversível via git,
  com verificação objetiva simples (links não quebrados, arquivos no lugar certo).
- Volume (~11 arquivos) e a necessidade de manter coerência entre `.cursor/`, `.claude/` e `.github/`
  (espelhos) adicionam superfície de trabalho, mas não complexidade de decisão de produto — é
  mecânico e auditável com requirements/design leves em markdown, exatamente o caso de uso do Dev Loop.

Decisão: **prosseguir em L2** (`continue_l2`).

## Riscos e considerações para a fase `requirements`

1. **Arquivos que devem permanecer na raiz** (não mover): `README.md` (entrypoint padrão do GitHub,
   agora único remote) e `CLAUDE.md` (lido automaticamente por Claude Code). Confirmar se
   `copilot-instructions.md` também tem leitura automática por convenção do GitHub Copilot antes de mover
   (pode precisar ficar em `.github/` em vez de `get_started/`, verificar convenção).
2. **Quais arquivos vão para `get_started/`**: listar explicitamente o conjunto final (a lista de ~9-10
   candidatos já levantada) e validar se algum outro arquivo da raiz também deveria entrar.
3. **Links quebrados após mover**: `README.md` referencia `START_HERE.md`, `CONTEXT.md` e outros; qualquer
   arquivo movido precisa ter suas referências atualizadas em `README.md`, `CONTEXT.md`,
   `docs/00-INDEX.md`, e nos próprios arquivos movidos (links cruzados entre eles).
4. **Padrão de espelho `.cursor` / `.claude` / `.github`**: se algum dos arquivos movidos for referenciado
   dentro de `.cursor/`, `.claude/` ou `.github/` (comandos, agentes, KBs), os três devem ser considerados
   e mantidos coerentes, conforme `CLAUDE.md` e `.claude/CLAUDE.md`.
5. **Redução de poluição visual**: além de mover para `get_started/`, avaliar se a raiz final ficará limpa
   (idealmente só `README.md`, `CLAUDE.md`, `get_started/`, pastas de código/config e arquivos de
   configuração de ferramentas que exigem raiz fixa).
6. **Verificação objetiva sugerida para o design/craft**: script ou checagem manual de links quebrados
   (ex.: grep por nomes dos arquivos movidos em todo o repo) após a reorganização.

## Bloqueios / pendências

| Item | Severidade | Resumo |
|------|------------|--------|
| — | — | Nenhum bloqueio para prosseguir em L2 |
