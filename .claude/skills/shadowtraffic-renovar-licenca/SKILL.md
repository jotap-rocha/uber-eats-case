---
name: shadowtraffic-renovar-licenca
description: Procedimento para diagnosticar licença expirada/inválida do ShadowTraffic, renovar as credenciais reais em gen/.env (LICENSE_ID, LICENSE_EMAIL, LICENSE_ORGANIZATION, LICENSE_EDITION, LICENSE_EXPIRATION, LICENSE_SIGNATURE) e religar o gerador sem colidir PK. Use quando o pedido for "licença do shadowtraffic expirou", "renovar licença", "gerador parou de gerar dados por licença", ou erro de licença nos logs de gen-unified. NÃO confunda com as variáveis LICENSE_KEY/LICENSE_OWNER citadas no README antigo — não existem no .env real deste projeto.
---

# ShadowTraffic — Renovar Licença Expirada

## Quando usar

- `docker-compose logs -f gen-unified` mostra erro relacionado a licença (expirada, inválida, assinatura não confere).
- Renovação programada da licença antes de expirar.
- Setup de um ambiente novo e a licença free trial precisa ser reemitida.

## Passo 1 — Diagnosticar

```powershell
docker-compose logs -f gen-unified
```

Confirme que o erro é de licença (não confundir com "Connection refused", que é infra não subida — nesse caso ver `.\scripts\start-infra.ps1`).

## Passo 2 — Obter/renovar credenciais

1. Acesse https://shadowtraffic.io e renove ou gere uma nova licença (trial ou paga).
2. As **6 variáveis reais** esperadas por este projeto (`gen/.env.template`) são:
   ```ini
   LICENSE_ID=
   LICENSE_EMAIL=
   LICENSE_ORGANIZATION=
   LICENSE_EDITION=
   LICENSE_EXPIRATION=
   LICENSE_SIGNATURE=
   ```
   Não existem `LICENSE_KEY`/`LICENSE_OWNER` neste projeto — se a fonte de onde você copiou as credenciais só citar essas duas, procure o formato completo assinado (inclui `LICENSE_SIGNATURE`) na área de conta do ShadowTraffic.

## Passo 3 — Atualizar `.env` (não o `.template`)

Edite `gen\.env` (arquivo real, git-ignorado) com os 6 valores novos.

## Passo 4 — Religar com segurança

Se `gen-unified` já gerou dados nas tabelas antes de a licença expirar (caso comum — o gerador roda por um tempo até a licença vencer), **não** use `start-generators.ps1`/`stop-generators.ps1` crus: eles não recalculam `startingFrom` e já causaram travamento total do pipeline por colisão de PK neste projeto.

```powershell
.\scripts\toggle-shadowtraffic.ps1 off   # se ainda estiver "preso" rodando
.\scripts\toggle-shadowtraffic.ps1 on    # relê o .env, recalcula startingFrom, sobe o container
.\scripts\toggle-shadowtraffic.ps1 status
```

Só use `start-generators.ps1` direto se as tabelas estiverem vazias (ambiente recém-criado).

## Referências

- `.claude/kb/shadowtraffic/concepts/licenciamento-e-env.md` — variáveis reais vs. README desatualizado
- `.claude/kb/shadowtraffic/patterns/restart-seguro-startingFrom.md` — por que não religar cru
- `docs/shadowtraffic/README.md` — howto humano de setup inicial de licença
