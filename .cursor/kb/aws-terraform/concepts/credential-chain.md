---
domain: aws-terraform
topic: credential-chain
---

# Cadeia de credenciais do provider `aws`

O provider usa o AWS SDK for Go v2. A **primeira** fonte que resolver vence:

| Ordem | Fonte | Uso no harness |
|---|---|---|
| 1 | Argumentos no bloco `provider` (`access_key`, `secret_key`) | **Proibido** |
| 2 | Env vars `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` / `AWS_SESSION_TOKEN` | Só com credenciais **temporárias** (ex.: exportadas por action OIDC) |
| 3 | Shared config/credentials (`~/.aws/config`) via `profile` / `AWS_PROFILE` | Dev local com SSO |
| — | Web identity (`assume_role_with_web_identity` no provider **ou** `AWS_ROLE_ARN` + `AWS_WEB_IDENTITY_TOKEN_FILE`) | CI OIDC, EKS IRSA (posição exata na cadeia: a validar) |
| 4 | Container credentials (ECS task role) | Runner em ECS |
| 5 | Instance metadata (IMDS — instance profile) | Runner em EC2 |

Depois de resolver a identidade base, `assume_role` (se presente) troca por uma role.

## Regra de ouro

> Credencial de **longa duração** (IAM user + access key) não entra no fluxo.
> Toda credencial deve ser **temporária** (STS): SSO, OIDC, instance profile, task role.

## Por que SSO no dev

- `aws sso login` gera token de sessão com expiração; nada fica em `~/.aws/credentials`.
- Permission set do IAM Identity Center = permissão mínima por conta.
- Perfil exemplo (`~/.aws/config`, fora do repo):

```ini
[profile <PROFILE>]
sso_session    = <SSO_SESSION>
sso_account_id = <AWS_ACCOUNT_ID>
sso_role_name  = <PERMISSION_SET>
region         = <REGION>

[sso-session <SSO_SESSION>]
sso_start_url  = https://<ORG>.awsapps.com/start
sso_region     = <REGION>
sso_registration_scopes = sso:account:access
```

## Por que OIDC no CI

- O provedor de CI emite um JWT por job; a AWS (via `aws_iam_openid_connect_provider`)
  troca por credenciais STS de 1h. Não há secret para vazar ou rotacionar.
- Trust policy amarra `sub` ao repo/branch — um fork não consegue assumir a role.

## Diagnóstico

```bash
aws sts get-caller-identity --profile <PROFILE>   # quem sou eu?
aws configure list --profile <PROFILE>            # de onde veio a credencial
TF_LOG=DEBUG terraform plan 2>&1 | grep -i credential   # nunca colar a saída inteira em issue
```

**Nunca** cole a saída de `env` ou `aws configure export-credentials` em logs, issues ou
chat — contém o session token.
