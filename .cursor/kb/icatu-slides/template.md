# Template HTML — Icatu Slides

> Esqueleto inicial. Preencha placeholders `{{…}}`. CSS: agregue trechos de [design-system.md](design-system.md), [component-library.md](component-library.md) e [slide-engine.md](slide-engine.md).

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TRILHA}} — {{TITULO}}</title>
<style>
  /* :root — ver design-system.md */
  /* componentes — ver component-library.md */
  /* deck + slide — ver slide-engine.md */
</style>
</head>
<body>

<!-- Barra institucional: logo obrigatório quando asset existir -->
<header class="icatu-bar" role="banner">
  <div class="icatu-bar__brand">
    <img
      class="icatu-bar__logo"
      src="../../templates/ppts/ICATU/assets/logo-icatu-horizontal.svg"
      alt="Icatu"
      width="140"
      height="32"
    />
  </div>
  <div class="icatu-bar__title">{{TRILHA_OU_AREA}}</div>
  <div class="icatu-bar__meta">{{ANO_OU_VERSAO}}</div>
</header>

<div class="deck-progress" id="progress"></div>
<nav class="deck-dots" id="dots" aria-label="Navegação entre slides"></nav>
<div class="deck-counter" id="counter" aria-live="polite"></div>
<div class="deck-hints" id="hints">&larr; &rarr; ou scroll</div>

<div class="deck" id="deck">

<section class="slide slide--icatu-cap" id="s1">
  <div class="icatu-geo">
    <div class="icatu-geo__diag" aria-hidden="true"></div>
    <div class="icatu-geo__content">
      <p class="icatu-label reveal">{{SUBTITULO_OPCIONAL}}</p>
      <h1 class="icatu-display reveal">{{TITULO_PRINCIPAL}}</h1>
    </div>
  </div>
</section>

<!-- Demais slides: slide--icatu-subcap, narrativa, tópicos, dados, frase, fim -->

</div>

<script>
/* Colar classe SlideEngine de ../aide-slides/slide-engine.md */
</script>
</body>
</html>
```

## CSS mínimo da barra

```css
.icatu-bar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 200;
  display: flex; align-items: center; justify-content: space-between;
  gap: 1rem; padding: 10px clamp(16px, 3vw, 32px);
  background: rgba(27, 49, 87, 0.92);
  border-bottom: 1px solid rgba(106, 162, 185, 0.25);
  font-family: var(--font-body);
}
.icatu-bar__title { font-weight: 600; color: var(--icatu-azul-03); font-size: 0.95rem; }
.icatu-bar__meta { font-size: 0.78rem; color: var(--text-dim); }
.deck { padding-top: 52px; } /* compensa header fixo */
```

Se o arquivo de logo ainda **não** existir em `assets/`, comente o `<img>` e use texto “Icatu” em `font-weight: 800; color: var(--icatu-azul-03);` **temporariamente** (somente até o asset oficial ser adicionado).
