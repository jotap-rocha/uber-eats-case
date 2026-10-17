---
domain: aws-terraform
topic: provider-auth
---

# Pattern: autenticação do provider `aws`

## Problema

O Terraform precisa de credenciais AWS no laptop e no CI **sem** access key estática
versionada ou guardada como secret de longa duração.

## Dev local — IAM Identity Center (SSO) + profile

```bash
aws configure sso                      # uma vez: cria [profile <PROFILE>] em ~/.aws/config
aws sso login --profile <PROFILE>      # a cada expiração da sessão
export AWS_PROFILE=<PROFILE>           # PowerShell: $env:AWS_PROFILE="<PROFILE>"
aws sts get-caller-identity            # confirma conta/role antes do plan
```

```hcl
variable "aws_profile" {
  type    = string
  default = null       # no CI fica null → cadeia padrão (OIDC/env)
}

provider "aws" {
  region  = var.region
  profile = var.aws_profile
}
```

Dica: prefira `AWS_PROFILE` no shell a `profile` fixo no HCL — o mesmo código roda no CI.

## CI — OIDC + IAM role (sem secret)

### 1. Provedor OIDC e role (Terraform de bootstrap, aplicado 1× por admin)

```hcl
resource "aws_iam_openid_connect_provider" "ci" {
  url            = "https://token.actions.githubusercontent.com"   # GitHub Actions
  client_id_list = ["sts.amazonaws.com"]
}

data "aws_iam_policy_document" "ci_trust" {
  statement {
    actions = ["sts:AssumeRoleWithWebIdentity"]
    principals {
      type        = "Federated"
      identifiers = [aws_iam_openid_connect_provider.ci.arn]
    }
    condition {
      test     = "StringEquals"
      variable = "token.actions.githubusercontent.com:aud"
      values   = ["sts.amazonaws.com"]
    }
    condition {
      test     = "StringLike"
      variable = "token.actions.githubusercontent.com:sub"
      values   = ["repo:<ORG>/<REPO>:ref:refs/heads/main"]
    }
  }
}

resource "aws_iam_role" "ci_deploy" {
  name                 = "<ROLE_NAME>"
  assume_role_policy   = data.aws_iam_policy_document.ci_trust.json
  max_session_duration = 3600
}
```

- Anexe à role **só** as policies da stack (S3/Redshift/MSK/Flink do projeto), nunca
  `AdministratorAccess` no CI.
- Para Azure DevOps o issuer/`sub` mudam — **a validar** os valores do seu tenant.

### 2. Job do pipeline (GitHub Actions)

```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::<AWS_ACCOUNT_ID>:role/<ROLE_NAME>
      aws-region: <REGION>
  - run: terraform init -backend-config=backend.hcl && terraform plan
```

A action exporta credenciais **temporárias** em env — o provider as lê (cadeia padrão).

### Alternativa: token em arquivo (sem action)

```hcl
provider "aws" {
  region = var.region
  assume_role_with_web_identity {
    role_arn                = "arn:aws:iam::<AWS_ACCOUNT_ID>:role/<ROLE_NAME>"
    session_name            = "terraform-ci"
    web_identity_token_file = "/tmp/oidc-token"
  }
}
```

## Cross-account (opcional)

```hcl
provider "aws" {
  region = var.region
  assume_role {
    role_arn     = "arn:aws:iam::<AWS_ACCOUNT_ID>:role/<DEPLOY_ROLE>"
    session_name = "terraform"
  }
}
```

## Checklist

- [ ] `grep -rE "AKIA|aws_secret_access_key" .` vazio (o githook de segredos também pega)
- [ ] `allowed_account_ids` no provider
- [ ] Trust policy com `sub` restrito a repo **e** branch
- [ ] Role do CI sem `*:*`; `iam:PassRole` só para as roles de serviço da stack

## Anti-padrões

| Errado | Certo |
|---|---|
| `access_key = "AKIA..."` | SSO profile / OIDC |
| IAM user `terraform-ci` com key em secret do pipeline | role OIDC (credencial de 1h) |
| `sub` com `repo:<ORG>/*` | repo + branch específicos |
