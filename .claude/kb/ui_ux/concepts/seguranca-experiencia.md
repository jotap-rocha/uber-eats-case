# Segurança na experiência

> **Purpose**: Ações perigososas exigem confirmação clara e irreversível por engano.  
> **Confidence**: 0.94

## Quando confirmar sempre

- Excluir registro  
- Executar carga pesada / backfill  
- Parar cluster ou job  
- Publicar dashboard  
- Sobrescrever tabela  
- Rodar pipeline em **produção**  

## Conteúdo do diálogo

1. **Título explícito**: “Excluir caso CASE-00042?”  
2. **Consequência**: “Esta ação não pode ser desfeita.”  
3. **Refinar alvo**: Mostrar IDs/nomes; exigir digitação para casos extremos.  
4. **CTAs distintos**: Primário destrutivo só se padrão do DS; preferir “Excluir permanentemente” em vermelho + “Cancelar” neutro.

## Padrões de implementação

- `AlertDialog` com foco preso até decisão.
- Desabilitar duplo submit.

## Anti-padrão

`window.confirm` genérico sem contexto — baixa confiança e má UX.

## Referências cruzadas

- [patterns/confirmacao-acoes-criticas.md](../patterns/confirmacao-acoes-criticas.md), [observabilidade-usuario.md](observabilidade-usuario.md)
