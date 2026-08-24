# Logs e auditoria seguros

> **Purpose**: Rastreabilidade sem vazar dados sensíveis.  
> **Confidence**: 0.94

## Não logar

- Senhas, hashes completos, OTP.
- **Tokens** de sessão, refresh tokens, API keys.
- **CPF/documento completo**, PAN de cartão, dados de saúde integral.
- **Connection strings** e secrets.
- Corpo de requisição com **payload sensível** (sanitizar ou omitir campos).

## Logar (auditoria)

- **Quem** (subject/user id ou identificador técnico autorizado).
- **Quando** (timestamp UTC).
- **De onde** (IP / device id quando política permitir e LGPD compatível).
- **Qual ação** (ex.: `CASE_STATUS_UPDATED`, `PIPELINE_RUN_PRD`).
- **Sucesso ou falha**.
- **ID de correlação** da requisição (`request_id`, trace id).

## Boas práticas

- Redação automática (*masking*) para campos conhecidos (`password`, `authorization`).
- Retenção e acesso aos logs alinhados à governança (quem pode ler logs de PRD).

## Erros ao usuário final

- Mensagem genérica na UI/API pública; detalhe técnico só em log seguro.

## Referências cruzadas

- [backend-seguro.md](backend-seguro.md), [frontend-seguro.md](frontend-seguro.md)
