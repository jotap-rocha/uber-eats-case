# Banco de dados seguro

> **Purpose**: Conta de aplicação com menor privilégio e defesa em profundidade.  
> **Confidence**: 0.94

## Contas e papéis

- Usuário da aplicação **não** deve ser `sysadmin`, `db_owner` ou superuser.
- **Conta dedicada por aplicação** (ou por serviço), não compartilhada entre times inconexos.

## Permissões

- **Mínimo necessário** — só objetos e operações requeridas.
- Quando possível, separar **somente leitura** (`SELECT`) de **escrita** (`INSERT`/`UPDATE` controlado).
- Conta **admin** restrita a migrações e runbooks — não usada pelo app em runtime.

## Padrão ilustrativo

| Conta | Uso |
|-------|-----|
| `app_readonly_user` | Relatórios, dashboards read-only |
| `app_writer_user` | CRUD da aplicação com escopo limitado |
| `app_admin_user` | Tarefas administrativas pontuais (fora do hot path) |

## Objetos de banco

- **Views** e **stored procedures** para encapsular lógica e restringir superfície quando fizer sentido.
- **Auditar** DDL/DML sensível conforme política (triggers de auditoria, logs nativos).

## Dados sensíveis

- **Criptografia em repouso** (TDE/encryption at rest do provedor) e, quando necessário, **colunas** cifradas ou tokenização.
- **Acesso direto** ao banco pelo usuário final da empresa é anti-padrão — usar API com controles.

## Referências cruzadas

- [sql-injection-prevencao.md](sql-injection-prevencao.md), [secrets-gestao.md](secrets-gestao.md)
