# Regras de qualidade — Icatu Slides

> Regras operacionais para decks HTML **Icatu**. Complementa [design-system.md](design-system.md) e os PDFs em `templates/ppts/ICATU/`.

## Marca e fontes

1. Use **apenas** cores de [icatu-palette.md](icatu-palette.md) (derivadas do PDF).
2. **Roboto** com fallback **Arial** (orientação do template PDF).
3. **Logo** somente de `templates/ppts/ICATU/assets/` ou arquivo explicitamente aprovado — ver [sources-and-logo.md](sources-and-logo.md).
4. **Sem pesquisa na internet** para atualizar identidade: se faltar ativo, peça ao time de marca ou use o último PDF no repositório.

## Preenchimento de tela

1. Cada slide deve ocupar **~90% da altura** útil (`100dvh` menos barra institucional), evitando “vazio” no centro.
2. Use `justify-content: center` no eixo principal quando o conteúdo for único bloco; use `margin-top: auto` em barras inferiores para empurrar rodapé contextual.
3. `padding-top` máximo recomendado: `clamp(40px, 7vh, 88px)` em slides com faixa diagonal.

## Português (pt-BR)

1. Acentuação correta em títulos e corpo (ação, não, também, módulo, etc.).
2. Números grandes em contexto corporativo: separador de milhar conforme padrão interno Icatu (definir no `slide-spec` se houver norma).

## Contraste

1. Texto principal sobre **Azul #01**: preferir `#f0f3f7` ou `#D5DBE6`.
2. Texto sobre **Azul #03**: usar **Azul #01** ou **Cinza #01** para corpo; evitar branco puro em blocos muito pequenos se o contraste estiver no limite.

## Dados e gráficos

1. Máximo **3–4 séries** por gráfico para legibilidade.
2. Não usar gradientes arco-íris; no máximo combinações de tokens da paleta Icatu.

## Revisão final (checklist)

- [ ] Todas as cores batem com a tabela da paleta.
- [ ] Logo presente onde o template PDF sugere (capa / finalização).
- [ ] Nenhum token AIDE (`--gold` dourado Kurv, cyan `#00b4ff`) misturado ao deck Icatu.
- [ ] Geometria de fundo revisada lado a lado com `template_ppt_Icatu.pdf`.
