# Tratamento de erro amigável

> **Purpose**: Erro é inevitável; pânico do usuário não.  
> **Confidence**: 0.93

## Estrutura da mensagem

1. **O que falhou** (linguagem humana: “Não foi possível carregar os casos”).
2. **Por que importa** (“Verifique sua conexão ou tente em alguns minutos”).
3. **O que fazer** — Botões: **Tentar novamente**, **Voltar**, **Abrir detalhes técnicos** (colapsado).

## Boas práticas

- **Não expor stack trace** na superfície principal; disponibilize “copiar ID do erro”.
- **Preservar contexto** — Não limpar formulário inteiro em erro de rede.
- **404 vs 403 vs 500** — Mensagens diferentes; 403: orientar contato com admin.

## Formulários

- Erros inline por campo + resumo no topo para telas longas.
- `aria-invalid` e `aria-describedby` ligados ao texto de erro.

## Observabilidade

Erro visual para o usuário + **log correlacionável** para suporte (request id, timestamp).

## Referências cruzadas

- [observabilidade-usuario.md](observabilidade-usuario.md), [acessibilidade.md](acessibilidade.md)
