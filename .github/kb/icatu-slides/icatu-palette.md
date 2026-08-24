# Paleta Icatu — extraída do template PDF

> Valores abaixo foram obtidos por **extração de texto** da página *Orientações Gerais* de `templates/ppts/ICATU/template_ppt_Icatu.pdf`. CMYK/Pantone constam como no documento.

## Cores principais e secundárias

| Nome oficial (PDF) | RGB | HEX | CMYK (PDF) | Pantone (PDF) |
|----------------------|-----|-----|------------|---------------|
| **Azul #01** | R27 G49 B87 | `#1B3157` | C98 M35 Y39 K32 | 534 C |
| **Azul #02** | R106 G162 B185 | `#6AA2B9` | C60 M24 Y20 K0 | 549 C |
| **Azul #03** | R213 G219 B230 | `#D5DBE6` | C15 M9 Y4 K0 | 642 C |
| **Verde #01** | R95 G187 B72 | `#5FBB48` | C66 M0 Y99 K0 | 360 C |
| **Cinza #01** | R147 G149 B152 | `#939598` | C0 M0 Y0 K50 | Cool Grey 7 C |

## Mapeamento semântico sugerido (HTML/CSS)

Use estes aliases nos decks para manter código legível:

| Token CSS | Origem | Uso típico |
|-----------|--------|------------|
| `--icatu-azul-01` | Azul #01 | Fundo escuro principal, faixas largas |
| `--icatu-azul-02` | Azul #02 | Destaque, ícones, gráficos, bordas vivas |
| `--icatu-azul-03` | Azul #03 | Superfícies claras, cartões “ar” |
| `--icatu-verde-01` | Verde #01 | Destaque positivo, etapas “sucesso”, CTAs secundários |
| `--icatu-cinza-01` | Cinza #01 | Texto secundário, eixos, legendas |

## Regras

1. **Não** substituir por cores “parecidas” de outras marcas ou geradas por IA.
2. Para **gradientes** entre tokens oficiais, use apenas combinações de `#1B3157`, `#6AA2B9`, `#D5DBE6`, `#5FBB48` com opacidade controlada (`rgba(..., 0.08)` a `0.25` em sobreposições).
3. Texto sobre `--icatu-azul-01`: preferir `#D5DBE6` ou branco `#ffffff` com contraste WCAG verificado.

## Tipografia (do mesmo PDF)

- Família principal: **Roboto** — pesos citados: **Black**, **Medium**, **Regular**, **Light**.
- Fallback explícito no template: **Arial** se Roboto não instalar.

Implementação sem CDN externa: embute arquivos de fonte obtidos na Vitrine (`@font-face`) ou usa Roboto já instalada no SO.
