# Licenciamento e variáveis de ambiente

> **Purpose**: Fonte de verdade sobre licença/`.env`, incluindo uma discrepância real encontrada entre a doc humana e o `.env.template`.
> **Confidence**: 0.85 (pricing não confirmado por doc estruturada — ver ressalva)
> **MCP Validated**: 2026-09-07 — fonte: WebSearch (shadowtraffic.io/pricing.html, docs.shadowtraffic.io/cheatsheet/) + `gen/.env.template` + `docs/shadowtraffic/README.md` deste repo

## Overview

ShadowTraffic exige licença mesmo em modo trial. `https://shadowtraffic.io/pricing.html` é renderizado via JavaScript — não foi possível extrair tiers/preços exatos por fetch estático nesta validação; um resultado de busca (não verificado formalmente) menciona trial gratuito de ~30 dias com reembolso. **Antes de qualquer decisão de orçamento, confirme diretamente no site** (a página pode exigir navegação interativa).

Existe também um modelo de "lease" (enterprise) via AWS KMS com variáveis como `LICENSE_EDITION`/`LICENSE_LEASE_KEY` — não é o modelo usado neste projeto.

## Discrepância real: README vs. `.env.template`

`docs/shadowtraffic/README.md` (deste repo) documenta estas variáveis de licença:

```ini
LICENSE_ID=<seu_license_id>
LICENSE_KEY=<sua_license_key>
LICENSE_EMAIL=<seu_email>
LICENSE_OWNER=<seu_nome>
```

O `gen/.env.template` **real** (arquivo que o `docker-compose.yml` de fato carrega via `env_file: ./gen/.env`) usa outro conjunto:

```ini
LICENSE_ID=
LICENSE_EMAIL=
LICENSE_ORGANIZATION=
LICENSE_EDITION=
LICENSE_EXPIRATION=
LICENSE_SIGNATURE=
```

**Não existem `LICENSE_KEY` nem `LICENSE_OWNER` no `.env.template` real.** `LICENSE_ORGANIZATION`, `LICENSE_EDITION`, `LICENSE_EXPIRATION` e `LICENSE_SIGNATURE` não aparecem no README.

### Regra para agentes

**`gen/.env.template` é a fonte de verdade**, não `docs/shadowtraffic/README.md`. O README ficou desatualizado (provavelmente escrito num momento anterior à emissão real da licença, quando só o modelo `ID/KEY/EMAIL/OWNER` de outra doc/exemplo genérico era conhecido). Um agente que gerar instruções de setup de licença deve citar as 6 variáveis do `.env.template`, não as 4 do README — e sinalizar ao usuário que o README merece correção (fora do escopo desta KB).

## Outras variáveis relevantes (`gen/.env.template`)

| Bloco | Variáveis |
|---|---|
| Postgres | `POSTGRES_HOST/PORT/DB/USERNAME/PASSWORD` |
| MinIO (S3) | `AWS_REGION`, `AWS_S3_FORCE_PATH_STYLE`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` |
| Oracle | `ORACLE_HOST/PORT/SERVICE/PASSWORD`, `ORACLE_APP_USERNAME/PASSWORD`, `ORACLE_DBZ_PASSWORD`, `RESTAURANT_COUNT` |
| MongoDB (satélite, fora do ShadowTraffic) | `MONGO_HOST`, `MONGO_PORT` |

## Related

- [conceitos-fundamentais](conceitos-fundamentais.md)
- `docs/shadowtraffic/README.md` (howto humano — setup passo a passo)
