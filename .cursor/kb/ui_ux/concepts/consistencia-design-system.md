# Consistência — botões, cores, menus, tabelas, mensagens

> **Purpose**: O usuário aprende uma vez e reaproveita em todo o sistema.  
> **Confidence**: 0.93

## Dimensões de consistência

| Área | Contrato |
|------|-----------|
| **Botões** | Variantes: primário (1 por vista), secundário, `outline`, `destructive`; ícone + label quando espaço permite |
| **Cores semânticas** | Mesmo token para “sucesso/alerta/erro/info” em badges, banners e toasts |
| **Menus** | Mesmo padrão de navegação (sidebar vs top), mesmo comportamento de submenu |
| **Tabelas** | Cabeçalho fixo opcional, mesma densidade (`compact`/`comfortable`), mesmos padrões de paginação |
| **Mensagens** | Tom de voz único (formal mas direto); templates para toast vs banner vs modal |

## Design tokens

Centralize em Tailwind + tema shadcn: `primary`, `destructive`, `muted`, `border`. Evite hex espalhado em componentes.

## Ícones

Uma família (ex.: Lucide), tamanhos padronizados (`size-4` em botões pequenos).

## Anti-padrão

Mesma ação com rótulos diferentes (“Salvar” vs “Aplicar” vs “Confirmar”) sem motivo de domínio.

## Projeto local

- Reutilizar `RiskBadge`, `StatusBadge`, `glass-card`, componentes `@/components/ui/*`.

## Referências cruzadas

- [tabelas-dados.md](tabelas-dados.md), [patterns/alinhamento-projeto-sisfraude.md](../patterns/alinhamento-projeto-sisfraude.md)
