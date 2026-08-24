# Layout e geometria — Icatu Slides

> Estrutura de páginas e **formas de fundo** coerentes com o template corporativo. Categorias conforme sumário de `template_ppt_Icatu.pdf`.

## Categorias de página (PDF)

1. **Orientações Gerais** — referência interna (não é slide de apresentação pública).
2. **Capas**
3. **Sub-capas** (com ou sem imagem — textos “SUB-CAPA COM IMAGEM” / “SEM IMAGEM” no PDF)
4. **Páginas Narrativas**
5. **Páginas com Tópicos**
6. **Páginas com Dados e Gráficos**
7. **Páginas com Frases em Destaque**
8. **Finalização da Apresentação**

Cada categoria no PowerPoint de referência combina **blocos geométricos** (faixas sólidas, retângulos largos, cantos cortados sugeridos pelo layout). Em HTML, reproduza **olhando o PDF página a página** — não invente novos padrões angulares se o template mostrar ângulo fixo.

## Padrões geométricos recomendados (HTML/CSS)

### 1. Faixa diagonal (marca)

Bloco principal em **Azul #01** com secção em **Verde #01** ou **Azul #02** (45° ou −35°, conforme o slide de referência no PDF).

```html
<div class="icatu-geo">
  <div class="icatu-geo__diag" aria-hidden="true"></div>
  <div class="icatu-geo__content">…</div>
</div>
```

```css
.icatu-geo { position: relative; overflow: hidden; min-height: 100%; }
.icatu-geo__diag {
  position: absolute; inset: -20% -10% auto -10%;
  height: 62%;
  background: linear-gradient(135deg, var(--icatu-azul-01) 55%, var(--icatu-verde-01) 55%);
  transform: skewY(-4deg);
  opacity: 0.95;
}
.icatu-geo__content { position: relative; z-index: 1; padding: clamp(32px, 6vh, 72px); }
```

Ajuste **ângulo** e **proporção** para coincidir com o slide modelo do PDF (inspeção visual).

### 2. Coluna clara (Azul #03)

Painel de leitura sobre fundo escuro: cartão com `background: var(--icatu-azul-03)` e texto **Azul #01** ou **Cinza #01** para hierarquia.

### 3. Grade de processo (ex.: trilha)

O PDF `ppt_trilha_de_auditoria_jan_2026.pdf` usa **fluxo em etapas numeradas**. Em HTML: `display: grid` ou `flex` com círculos numerados (`border-radius: 50%`, borda `2px solid var(--icatu-azul-02)`), conectores em **Azul #02** semi-transparente.

### 4. Sub-capa com imagem

Grid **1.1fr 1fr**: esquerda título + linha verde/azul de acento; direita `figure` com `object-fit: cover` e cantos alinhados ao modelo do PDF.

## Logo e geometria

Reserve **área fixa** no canto (ex.: superior esquerdo) para o logo — ver [sources-and-logo.md](sources-and-logo.md). Não sobrepor o logo às faixas diagonais: mantenha `z-index` do logo acima do pano de fundo, com padding consistente.

## Checklist de layout

- [ ] Tipo de página escolhido entre as categorias do PDF.
- [ ] Paleta apenas [icatu-palette.md](icatu-palette.md).
- [ ] Diagonal / blocos conferidos visualmente com `template_ppt_Icatu.pdf`.
