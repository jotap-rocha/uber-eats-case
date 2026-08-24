# `src/core/` — orquestração (arquiteto da aplicação)

> **Propósito:** Um lugar central que define **os passos** do job em ordem, sem executar IO bruto.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-07

## Regra

Em **`src/core/`** reside o **orquestrador**: classe(s) e métodos que **sequenciam** o fluxo de negócio chamando **portas** implementadas em **`integrations`** (injetadas ou construídas na composição em `main.py` / factory).

- **Pode:** decisões de fluxo, loops sobre cargas/tarefas, agregação de resultados, política “verificar tudo antes de finalizar”.
- **Não pode:** SQL literal acoplado, `pyodbc.connect`, HTTP direto a Teams — isso vive em **`integrations`**.

## Papel (“arquiteto”)

O orquestrador é quem **sabe o roteiro**, não **como** o driver fala com o servidor. Exemplo **Sentinela** (referência de domínio):

1. Montar o **molde mestre** das cargas (estruturas/config já tipadas).
2. Para cada carga: **verificar** estado (delegando leitura ao adaptador de BD).
3. **Disparar mensagem** quando política exigir (delegando a `integrations/messaging`).
4. **Certificar** que todas as cargas foram percorridas / registadas conforme regra.
5. **Finalizar** o fluxo de negócio (status interno); *logging global de processo* pode coordenar-se aqui ou em `app` conforme desenho.

Um único módulo principal (ex. `orchestrator.py` ou nome do projeto) costuma bastar; outros ficheiros em `core/` são **modelos**, **políticas** ou **serviços de domínio** sem IO.

## OOP

Preferir **classes** com métodos **`_privados`** para passos internos e métodos **públicos** (`run`, `execute`) como API chamada por `main.py`.

## Relacionado

- [app-main-contract.md](app-main-contract.md)
- [integrations-execucao.md](integrations-execucao.md)
- [filosofia-camadas.md](filosofia-camadas.md)
