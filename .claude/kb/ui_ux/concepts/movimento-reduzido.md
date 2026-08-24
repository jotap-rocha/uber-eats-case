# Movimento reduzido (`prefers-reduced-motion`)

> **Purpose**: Respeitar usuários com sensibilidade a animação e políticas de SO/navegador.  
> **Confidence**: 0.93  
> **WCAG**: 2.3.3 Animation from Interactions (AAA orientação).

## Regra

Se `prefers-reduced-motion: reduce`:

- **Elimine** animações decorativas (entrada em cascata, bounce, parallax).
- **Mantenha** feedback funcional mínimo (fade curto ou troca instantânea de estado).
- **Nunca** use movimento como único indicador de alerta — já coberto em [acessibilidade.md](acessibilidade.md).

## O que ajustar na prática

| Superfície | Reduzido |
|------------|----------|
| Toasts | Entrada sem slide longo; ou aparecer já na posição final |
| Modais | Sem scale-in agressivo; opacidade discreta ou instantâneo |
| Skeleton pulse | Trocar por estático ou pulse muito sutil / contraste apenas |
| Spinner | Permitido (não é animação de grande amplitude); evitar rotação excessivamente rápida |

## Implementação

Ver [patterns/tailwind-motion-reduced.md](../patterns/tailwind-motion-reduced.md).

## Teste

- Chrome DevTools → Rendering → **Emulate CSS media feature prefers-reduced-motion**.
- macOS: Acessibilidade → Display → Reduzir movimento.

## Referências cruzadas

- [percepcao-de-performance.md](percepcao-de-performance.md), [feedback-constante.md](feedback-constante.md)
