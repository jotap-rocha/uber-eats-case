# Feedback constante na tela

> **Purpose**: O sistema sempre “fala” com o usuário: ocupado, sucesso, vazio, erro.  
> **Confidence**: 0.93

## Estados mínimos por interação

| Momento | Feedback esperado |
|---------|-------------------|
| Clique em ação | Botão `disabled` ou `aria-busy`, spinner opcional |
| Requisição HTTP | Skeleton ou overlay coerente com criticidade |
| Sucesso | Toast curto ou atualização óbvia na lista |
| Erro | Mensagem humana + próximo passo (retry, suporte) |
| Operação só no cliente | Mesmo assim: micro-feedback (highlight, toast “lista atualizada”) |

## Consistência

- Mesmo tipo de ação → mesmo tipo de feedback (ex.: sempre Sonner para confirmações leves).
- Evite **silêncio absoluto** após submit — principal causa de “duplo clique” e registros duplicados.

## Projeto local

- Lab Databricks / filtros client-side: combinar **spinner no botão**, **anel na card**, **overlay leve** e **toast** quando não há novo round-trip ao servidor.

## Referências cruzadas

- [tratamento-erro-amigavel.md](tratamento-erro-amigavel.md), [patterns/loading-etapas-e-cache.md](../patterns/loading-etapas-e-cache.md)
