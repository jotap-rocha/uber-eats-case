# Microcopy e internacionalização (i18n)

> **Purpose**: Textos de interface consistentes, inclusivos e preparados para mais de um idioma.  
> **Confidence**: 0.92

## Tom de voz (SisFraude / corporativo BR)

- **Direto e respeitoso**: segunda pessoa opcional (“Atualize os filtros”) ou neutro (“Filtros atualizados”).
- **Evite culpa**: “Não foi possível…” em vez de “Você digitou errado” quando o erro for técnico.
- **Verbos no imperativo** em botões: Salvar, Buscar, Limpar, Recarregar — um verbo por botão.

## Consistência lexical

| Evitar | Preferir |
|--------|-----------|
| Sinônimos alternados (“registro”, “item”, “linha”) no mesmo fluxo | Um termo de domínio: **caso**, **registro** na grade |
| “OK” genérico em confirmação | Verbo + objeto: “Excluir caso” |

## Pluralização e quantidades

- Toast/listagens: **“1 registro”** vs **“N registros”** — nunca string fixa “registro(s)” se puder formatar.
- Em TypeScript, helper único `formatCount(n, singular, plural)` ou biblioteca (`Intl.PluralRules`) evita divergência entre telas.

## i18n futuro (pt-BR → en)

1. **Extrair strings** — Nada de frases longas inline sem chave (`cases.list.updated`).
2. **Interpolação segura** — `{{count}}` com plural rules; datas/números com `Intl.NumberFormat` / `Intl.DateTimeFormat`.
3. **Layout** — Textos em inglês costumam ser ~30% mais curtos ou mais longos; evite caixas que quebrem com uma língua só.

## Acessibilidade + cópia

`aria-label` e mensagens de erro devem usar as **mesmas chaves** que o texto visível quando possível — uma fonte da verdade.

## Referências cruzadas

- [consistencia-design-system.md](consistencia-design-system.md), [tratamento-erro-amigavel.md](tratamento-erro-amigavel.md), [specs/ui-checklist.yaml](../specs/ui-checklist.yaml)
