# Fluxo simples

> **Purpose**: Menos passos, menos memorização, menos erro — sem sacrificar segurança onde precisa.  
> **Confidence**: 0.92

## Diretrizes

1. **Caminho feliz linear** — Coleções: lista → detalhe → ação. Evite “voltar três telas” para concluir.
2. **Defaults sensatos** — Pré-preencher com último contexto (empresa, período) quando seguro.
3. **Reversibilidade** — Desfazer/toasts com “desfazer” para ações não destrutivas; para destrutivas use confirmação (ver [seguranca-experiencia.md](seguranca-experiencia.md)).
4. **Agrupar decisões** — Não espalhar o mesmo formulário em modais encadeados sem progresso visível.

## Anti-padrões

- Wizard de 8 passos quando 2 bastariam.
- Exigir dados que o sistema já conhece (session/API).

## Dados e filtros

Fluxo “filtro → aplicar → resultado” deve ser **previsível**: ou auto-aplica com debounce *e* feedback, ou um botão explícito com estado ocupado — misturar os dois sem critério confunde.

## Referências cruzadas

- [feedback-constante.md](feedback-constante.md), [percepcao-de-performance.md](percepcao-de-performance.md)
