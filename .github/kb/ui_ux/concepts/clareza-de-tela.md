# Clareza de tela

> **Purpose**: O usuário entende em segundos *onde está* e *o que pode fazer*.  
> **Confidence**: 0.92

## Princípios

1. **Um objetivo principal por tela** — Evite misturar “relatório gerencial” com “ferramenta operacional” sem abas ou rotas claras.
2. **Título e subtítulo honestos** — Nomeie o que a tela *faz*, não o nome interno do projeto.
3. **Linguagem do domínio** — Use vocabulário da seguradora/analista (ex.: “caso”, “indício”, “réguas”), não só siglas de TI.
4. **Densidade controlada** — Informação demais gera abandono; use agrupamento, `Accordion`, tooltips ou detalhe em segunda camada.

## Sinais de problema

- Usuário pergunta “isso aqui atualizou?” sem estado visível.
- Campos obrigatórios só aparecem no submit.
- Labels genéricos (“Campo 1”, “Valor”) em fluxos críticos.

## No SisFraude

- Breadcrumb + contexto de sessão (empresa/linha) reforçam *clareza situacional*.
- Modais (`CaseDetail`) devem repetir identificador do caso no cabeçalho.

## Referências cruzadas

- [hierarquia-visual.md](hierarquia-visual.md), [menos-e-mais.md](menos-e-mais.md)
