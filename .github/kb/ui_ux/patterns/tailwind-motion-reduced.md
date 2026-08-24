# Padrão — Tailwind e movimento reduzido

> **Purpose**: Snippets alinhados ao Tailwind 3.4+ do SisFraude.  
> **Confidence**: 0.94

## Variantes nativas

Tailwind expõe **`motion-safe:`** e **`motion-reduce:`** (baseados em `prefers-reduced-motion`).

### Exemplos

```html
<!-- Anima só quem não pediu redução -->
<div class="motion-safe:animate-slide-in motion-reduce:animate-none">

<!-- Transição pesada só em modo “safe” -->
<div class="transition-transform motion-safe:duration-300 motion-reduce:transition-none">

<!-- Entrada de toast: slide opcional -->
<div class="motion-safe:animate-in motion-safe:slide-in-from-top-2 motion-reduce:animate-none">
```

## `tailwindcss-animate`

Classes como `animate-in`, `fade-in` combinam com **`motion-reduce:animate-none`** no mesmo elemento.

## Global (último recurso)

Se animações de terceiros não aceitam variantes, um bloco global em CSS:

```css
@media (prefers-reduced-motion: reduce) {
  html:focus-within {
    scroll-behavior: auto;
  }
}
```

Evite `!important` em tudo — pode quebrar spinners necessários; prefira classe por componente.

## Checklist

- [ ] Novos componentes com `animate-*` também têm ramo `motion-reduce:`?
- [ ] Autoplay de carrossel / marquee desliga ou respeita redução?

## Referências

- [concepts/movimento-reduzido.md](../concepts/movimento-reduzido.md)
