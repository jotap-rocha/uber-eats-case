# Observabilidade para o usuário

> **Purpose**: Em sistemas técnicos, transparência reduz tickets e aumenta confiança.  
> **Confidence**: 0.93

## O que mostrar (quando aplicável)

| Dado | Por quê |
|------|---------|
| **Status** | Running, sucesso, falha, cancelado |
| **Início e fim** | Audit trail humano |
| **Duração** | Performance percebida + SLA |
| **Responsável** | Usuário ou serviço que disparou |
| **Logs** | Trecho relevante + link “ver completo” |
| **Erro** | Código + mensagem amigável + correl ID |
| **Quantidade processada** | Linhas, registros, arquivos |
| **Custo estimado** | Em jobs cloud/warehouse quando disponível |
| **Link para detalhes** | Job run, trace, ticket |

## UI

- Timeline vertical para pipelines.
- Badge de ambiente (`DEV`/`PRD`) sempre visível em ações sensíveis.

## Relação com erro

Camada “usuário” (mensagem curta) + camada “suporte” (payload técnico expansível).

## Referências cruzadas

- [tratamento-erro-amigavel.md](tratamento-erro-amigavel.md), [percepcao-de-performance.md](percepcao-de-performance.md)
