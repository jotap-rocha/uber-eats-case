# Padrão — cofres de secrets por nuvem / plataforma

> **Purpose**: Onde guardar credenciais conforme o ambiente do projeto.  
> **Confidence**: 0.92

## Mapeamento rápido

| Plataforma | Serviço típico |
|------------|----------------|
| Microsoft Azure | Azure Key Vault (+ Managed Identity) |
| AWS | Secrets Manager ou SSM Parameter Store (SecureString) + KMS |
| Oracle Cloud | OCI Vault |
| HashiCorp stack | Vault (KV v2, policies) |
| Databricks | Databricks Secrets (`scope`/`key`) para tokens warehouse, PAT, etc. |

## Princípios comuns

1. **Identidade da carga** (pod, function, VM) autentica no cofre — não senha estática no app em PRD.
2. **Rotação** periódica e em incidente; automatizar onde o provedor permitir.
3. **Least privilege** nas políticas IAM/RBAC do cofre — só o serviço necessário lê cada secret.
4. **Auditoria** de `get`/`list` para detectar uso anômalo.

## SisFraude / Vite local

- Variáveis locais em `.env` **não commitadas**; em PRD/staging, inject via plataforma (ex.: Supabase dashboard + GitHub Actions secrets para CI **sem** eco no log).

## Referências

- [concepts/secrets-gestao.md](../concepts/secrets-gestao.md)
