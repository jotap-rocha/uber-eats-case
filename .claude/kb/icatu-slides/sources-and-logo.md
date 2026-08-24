# Fontes, PDFs e logomarca — Icatu Slides

> Tudo que for **identidade Icatu** deve vir de **materiais internos** ou deste repositório — **sem pesquisa na web** para cores, logo ou layout “oficial”.

## PDFs canônicos (repositório)

| Caminho | Conteúdo |
|---------|----------|
| `templates/ppts/ICATU/template_ppt_Icatu.pdf` | Orientações gerais: **Roboto**, cores **Azul #01–#03**, **Verde #01**, **Cinza #01**, Pantone, tipos de página (capas, sub-capas, narrativas, etc.). |
| `templates/ppts/ICATU/ppt_trilha_de_auditoria_jan_2026.pdf` | Exemplo de deck (trilha, fases, sumário) para **ritmo** e hierarquia de informação. |

Sempre que houver divergência entre esta KB e o PDF **atualizado no repositório**, **o PDF vence**.

## Logomarca

- O template PDF remete ao **Guia da Marca** e à **Vitrine de Marketing** no **Portal Corporativo** (fonte interna de arquivos oficiais).
- Para slides HTML versionados neste repo, use arquivos colocados em:

  `templates/ppts/ICATU/assets/`

  Exemplos de nomes sugeridos (ajuste ao que o time exportar):

  - `logo-icatu-horizontal.svg` ou `.png`
  - `logo-icatu-mono-claro.svg` (se existir versão para fundo escuro)

### Uso em HTML

```html
<!-- Caminho relativo ao HTML em presentation/... -->
<img
  class="icatu-logo"
  src="../../templates/ppts/ICATU/assets/logo-icatu-horizontal.svg"
  alt="Icatu"
  width="160"
  height="auto"
/>
```

**Regras:**

1. **Não** redesenhar o logo em SVG “genérico”.
2. Manter **área de respiro** conforme Guia da Marca (se o PDF/guia especificar; caso contrário, padding mínimo `clamp(12px, 2vw, 24px)` ao redor do logo).
3. Fundo **Azul #01** (`#1B3157`): preferir versão **clara** do logo se o guia definir; nunca inverter cores arbitrariamente.

## Checklist antes de publicar deck

- [ ] Cores conferidas com [icatu-palette.md](icatu-palette.md) / PDF.
- [ ] Fonte **Roboto** (ou **Arial** se Roboto indisponível), conforme PDF.
- [ ] Logo de `assets/` com aprovação de marca.
- [ ] Nenhuma cor “inventada” fora da paleta (exceções só com **aprovação explícita** do time de marca).
