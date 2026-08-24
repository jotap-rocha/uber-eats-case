# Acessibilidade

> **Purpose**: Mesmo sistema interno ganha produtividade e inclusão com bases de a11y.  
> **Confidence**: 0.93

## Lista de verificação

| Tema | Ação |
|------|------|
| **Contraste** | Texto vs fundo conforme WCAG AA onde possível |
| **Tamanho de fonte** | Evitar corpo < 14px equivalente em telas densas sem zoom |
| **Teclado** | Tab order lógico; `Esc` fecha modal; foco retorna ao trigger |
| **Textos alternativos** | Imagens e ícones decorativos vs informativos (`aria-hidden`) |
| **Labels** | Todo input com `<Label>` associado ou `aria-label` |
| **Mensagens** | Erros anunciados (`role="alert"` ou live region quando crítico) |
| **Status sem só cor** | Vermelho/verde **+ texto + ícone** (“Confirmado”, “Reprovado”) |

## Exemplo pedido pelo domínio

**Ruim**: apenas bola verde/vermelha para status.  
**Bom**: badge “Confirmado” com variante semântica + ícone.

## Tabelas

- Cabeçalhos com `scope`; células com botões devem ter nome acessível.

## Não é opcional em fluxos críticos

Auth, aprovações financeiras, exclusão: teste com teclado e leitor de tela pontualmente.

## Movimento

Preferências do usuário para menos animação: [movimento-reduzido.md](movimento-reduzido.md).

## Referências cruzadas

- [tratamento-erro-amigavel.md](tratamento-erro-amigavel.md), [seguranca-experiencia.md](seguranca-experiencia.md)
