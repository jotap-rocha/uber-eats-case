# Checklist — configurar um Genie Space com qualidade

> **Propósito**: Sequência reutilizável para equipes de dados antes de abrir o chat a usuários de negócio.
> **Confiança**: 0.90
> **MCP Validated**: null

## Quando usar

Novo domínio analítico, novo catálogo de negócio ou auditoria de um espaço existente com reclamações de qualidade ou risco de vazamento.

## Passos

1. **Dados**: Views ou tabelas curadas em UC; descrições de coluna preenchidas; volume de objetos ≤ 30 no espaço.
2. **Segurança**: `SELECT` mínimo por persona; confirmar que credenciais do warehouse embutido não ampliam escopo indevido.
3. **Compute**: SQL warehouse serverless ou Pro; CAN USE para quem publica; preferir serverless pela doc. de performance.
4. **Knowledge store**: joins críticos; sinônimos (ex.: “ticket” = `id_chamado`); medidas/filtros compartilhados; ficar abaixo do teto de 200 snippets.
5. **Instruções SQL**: 5–15 exemplos que refletem perguntas reais; títulos = linguagem do usuário; parametrizar onde houver ambiguidade temporal/filtro.
6. **Funções UC**: Para lógica que não deve ser visível no SQL gerado; garantir `EXECUTE` aos consumidores autorizados.
7. **Texto geral**: calendário fiscal, moeda, idioma, arredondamento; evitar contradições com exemplos SQL.
8. **Sugestões automáticas**: Revisar queries sugeridas; aceitar só as alinhadas ao domínio.
9. **Settings**: título, descrição (Markdown), perguntas comuns, tags; validar thumbnail se política corporativa permitir.
10. **Piloto**: conjunto de perguntas de teste; revisar respostas não Trusted; iterar ([best practices](https://docs.databricks.com/aws/en/genie/best-practices)).
11. **API** (se aplicável): limites de throughput da Genie API; monitoramento de uso.

## Anti-padrão

Publicar espaço “vazio” só com tabelas cruas e sem exemplos — aumenta SQL incorreto e frustração.

## Relacionados

- [../concepts/genie-knowledge-store-e-instrucoes.md](../concepts/genie-knowledge-store-e-instrucoes.md)
- [../concepts/genie-requisitos-permissoes-limites.md](../concepts/genie-requisitos-permissoes-limites.md)
