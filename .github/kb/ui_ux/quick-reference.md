# UI/UX — Referência rápida

> **Confidence**: 0.92 (boas práticas consolidadas; sem MCP obrigatório)

Versão estruturada (YAML, por severidade): [specs/ui-checklist.yaml](specs/ui-checklist.yaml).

## Checklist antes de liberar uma tela

- [ ] O objetivo da tela está claro?
- [ ] A ação principal está evidente?
- [ ] Existe feedback de loading?
- [ ] Existe mensagem de erro amigável?
- [ ] Existe estado vazio?
- [ ] A tela é consistente com o restante do sistema?
- [ ] Funciona bem em diferentes resoluções?
- [ ] Os textos são claros?
- [ ] A tabela tem filtro, ordenação e paginação (quando aplicável)?
- [ ] Ações críticas têm confirmação?
- [ ] Logs e detalhes técnicos estão disponíveis quando necessário?
- [ ] O usuário sabe o que aconteceu após clicar?

## Mapa técnico (SisFraude / stack típico)

| Necessidade | Onde costuma morar |
|-------------|-------------------|
| Feedback toast | Sonner (`@/components/ui/sonner`) |
| Loading inline | Skeleton shadcn, `aria-busy`, spinners em botões |
| Confirmação | `AlertDialog` shadcn |
| Tabela | Data table + paginação client/server |
| Estado vazio | Ilustração leve + CTA + link para doc |
| Cache / “rápido” | React Query `staleTime`, placeholders |

## Regra de ouro

**Tela principal para decisão. Tela de detalhe para investigação.**

## Etapas exemplo (operação longa)

1. Conectando ao Databricks  
2. Iniciando cluster serverless  
3. Executando consulta  
4. Carregando resultado  

## Status sem só cor

Sempre combinar **cor + texto + ícone** (ex.: “Crítico”, “Confirmado”, não só verde/vermelho).
