# `src/app/` — apenas `main.py` (contrato estrito)

> **Propósito:** Delimitar o único módulo com lógica de arranque; todo o resto da aplicação fica em `core` e `integrations`.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-07

## Regra

Em **`src/app/`** existe **somente** o ficheiro **`main.py`** com responsabilidades **estritamente** as listadas abaixo. **Não** coloque aqui orquestração de negócio, queries, chamadas HTTP/SQL diretas nem classes de domínio.

**Entrada do pacote:** `python -m src.app` deve resolver para **`main.py`** (via `src/app/__main__.py` com **uma** linha que delega em `main()`, sem lógica extra, se o projeto usar esse padrão).

## Responsabilidades permitidas em `main.py` (somente estas)

| # | Responsabilidade | Detalhe |
|---|------------------|---------|
| 1 | **Configuração** | Ajustes finais de config já carregada (paths, merges mínimos); *fail fast* se inválida |
| 2 | **Raiz do projeto** | Resolver caminho raiz do repo **automaticamente** quando necessário (ex.: partir de `Path(__file__)`, util em `src/utils/`) |
| 3 | **Ambiente PRD vs não-PRD** | Inferir ambiente de execução: **PRD** apenas quando o critério do projeto for satisfeito (ex.: segmento `PRD` no caminho absoluto relevante); **qualquer outro caso** (TST, HML, DEV, etc.) tratar como **não-PRD** |
| 4 | **Dry-run** | Interpretar flag/opção **dry-run**: se ativo, não executar efeitos colaterais (integrações reais); apenas fluxo seguro acordado |
| 5 | **Start** | Invocar o **único ponto de orquestração** em **`src/core`** (classe/função pública definida no contrato do projeto — ex. `Pipeline.run()`) |
| 6 | **Finish** | Encerramento controlado: logs finais, código de saída, `flush` de recursos externos já abertos no arranque **se** responsabilidade do bootstrap |
| 7 | **Show** (opcional) | Modo **`--show`** (ou equivalente): imprimir resumo do que foi resolvido (config, raiz, ambiente inferido, dry-run) e **sair sem** chamar o núcleo — útil para diagnóstico |

**Proibido em `main.py`:** montar “molde mestre” de cargas, consultar BD, enviar Teams, loops por cargas, regras de threshold — isso é **`core`** + **`integrations`**.

## Forma recomendada

Classes/métodos com visibilidade explícita (`_privado` vs público); `main.py` expõe no máximo uma função **`main()`** e o guard `if __name__ == "__main__"` delegando em `raise SystemExit(main())`.

## Relacionado

- [core-orquestracao.md](core-orquestracao.md)
- [integrations-execucao.md](integrations-execucao.md)
- [estrutura-pastas-src-layout.md](estrutura-pastas-src-layout.md)
