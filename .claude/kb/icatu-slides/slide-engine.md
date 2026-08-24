# Motor de slides — Icatu Slides

> Mesmo padrão técnico do KB **AIDE Slides** ([slide-engine.md](../aide-slides/slide-engine.md)): `SlideEngine`, scroll-snap, teclado e toque. Abaixo, versão resumida com **chrome** ajustado à paleta Icatu.

## Classe `SlideEngine`

Copie o bloco JavaScript completo de [../aide-slides/slide-engine.md](../aide-slides/slide-engine.md#slideengine-class) — é idêntico em comportamento.

## Chrome de navegação — CSS (Icatu)

Substitua o gradiente da barra de progresso para usar **Azul #02** + **Verde #01**:

```css
.deck-progress {
  position: fixed; top: 0; left: 0; height: 3px;
  background: linear-gradient(90deg, var(--icatu-azul-02), var(--icatu-verde-01));
  z-index: 100; transition: width 0.3s ease; pointer-events: none;
}
.deck-dots {
  position: fixed; right: clamp(12px, 2vw, 24px); top: 50%; transform: translateY(-50%);
  display: flex; flex-direction: column; gap: 7px; z-index: 100; padding: 7px;
  background: rgba(27, 49, 87, 0.55); border-radius: 20px; backdrop-filter: blur(8px);
}
.deck-dot.active {
  opacity: 1; transform: scale(1.5);
  background: var(--icatu-azul-02);
  box-shadow: 0 0 8px rgba(106, 162, 185, 0.45);
}
```

## Container `.deck` e `.slide`

Use o mesmo bloco **Scroll-Snap** e **Reveal** de [../aide-slides/slide-engine.md](../aide-slides/slide-engine.md#scroll-snap-container).

## Prefixo de classes

Prefira `deck` / `slide` **iguais ao AIDE** para reaproveitar JS sem mudanças; diferencie apenas o **tema** via variáveis `:root` Icatu no `<style>` do deck.
