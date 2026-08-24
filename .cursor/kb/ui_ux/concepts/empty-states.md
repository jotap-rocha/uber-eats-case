# Empty states bem feitos

> **Purpose**: Lista vazia não é “tela em branco”; é oportunidade de orientar.  
> **Confidence**: 0.92

## Componentes de um empty state

1. **Ilustração ou ícone leve** — Sem poluir; opcional em apps densos.
2. **Título claro** — “Nenhum caso com esses filtros” vs “Nada aqui”.
3. **Explicação curta** — Por que está vazio (filtro restritivo vs sem dados legítimos).
4. **CTA** — “Limpar filtros”, “Importar”, “Criar primeiro caso”.
5. **Link secundário** — Documentação ou exemplo de query.

## Diferenciar causas

| Causa | Mensagem típica |
|-------|------------------|
| Sem dados no sistema | Boas-vindas + primeiro passo |
| Filtro sem match | Sugerir relaxar critério |
| Erro mascarado | Não usar empty — usar estado de erro |

## Acessibilidade

Empty state é conteúdo: use texto real, não só imagem.

## Referências cruzadas

- [tabelas-dados.md](tabelas-dados.md), [tratamento-erro-amigavel.md](tratamento-erro-amigavel.md)
