# Secrets, strings de conexão e credenciais

> **Purpose**: Centralizar, auditar e rotacionar segredos — OWASP recomenda cofre dedicado.  
> **Confidence**: 0.94

## Nunca armazenar ou publicar secrets em

- Código-fonte ou templates commitados sem revisão.
- **GitHub / GitLab** (histórico permanente até limpeza especializada).
- Arquivos **`.env` versionados`** ou exemplos com valores reais.
- **Frontend** / bundle JavaScript.
- **Logs**, traces abertos, prints de tela, vídeos de demo.
- **Imagens Docker** em camadas imutáveis com segredos baked-in.
- **Documentação pública** ou wikis sem controle de acesso.

## Cofres (exemplos)

- **Azure Key Vault**
- **AWS Secrets Manager** / Parameter Store (com KMS)
- **HashiCorp Vault**
- **OCI Vault**
- **Databricks Secrets** (escopos workspace/cluster)

Benefícios: **centralização**, **auditoria de acesso**, **rotação**, integração com identidade da nuvem.

## Operação

- Injetar em runtime (env do runtime, sidecar, SDK do cofre) — não duplicar em múltiplos repositórios.
- **Secret scanning** no CI (GitHub Advanced Security, Gitleaks, etc.) e política de rotação se vazamento.

## Referências cruzadas

- [frontend-seguro.md](frontend-seguro.md), [patterns/cofres-secrets-nuvem.md](../patterns/cofres-secrets-nuvem.md)
