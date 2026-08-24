# Padrão — Confirmação de ações críticas

> **Purpose**: Dialog consistente para operações irreversíveis ou caras.  
> **Confidence**: 0.94

## Gatilhos típicos

- Excluir registro  
- Executar carga / backfill  
- Parar cluster ou job  
- Publicar dashboard  
- Sobrescrever tabela  
- Rodar pipeline em produção  

## Estrutura recomendada (shadcn AlertDialog)

```text
[Título específico com nome/ID]
[1–2 frases de consequência]
[Checkbox opcional: “Entendo que…” para casos extremos]
[Cancelar]  [Ação destrutiva]
```

## Texto do botão primário

- Use verbo **consequente**: “Excluir permanentemente”, “Publicar em PRD”, não só “OK”.
- Evite “Confirmar” genérico sem leitura do título.

## Estado da operação

Após aceitar:

- Botão entra em loading; dialog não fecha até erro ou sucesso conhecido.
- Em sucesso: toast + fechar; em erro: manter contexto + mensagem amigável.

## Acessibilidade

- Foco inicial no botão cancelar ou no neutro (equipe pode decidir padrão; documente).
- `aria-describedby` ligado ao texto de risco.

## Referências

- [concepts/seguranca-experiencia.md](../concepts/seguranca-experiencia.md)
- [concepts/tratamento-erro-amigavel.md](../concepts/tratamento-erro-amigavel.md)
