# Webhooks do ambiente Icatu

> **Confiança:** 0.95 · Específico deste workspace

## Fonte de verdade das URLs

As URLs dos webhooks **não** ficam no repositório Git. O padrão do time:

| Onde | Uso |
|------|-----|
| **`.env`** (local, gitignored) | Desenvolvimento, notebooks locais, testes manuais |
| **`.env.example`** | Lista de **nomes** de variáveis, sem valores reais |
| **Databricks Secrets** (produção) | Jobs e notebooks em PRD/DSV sem `.env` no workspace |

## Chaves principais (`.env.example`)

| Variável | Papel |
|----------|--------|
| **`URL_WEBHOOK_SENTINEL`** | Webhook padrão para alertas **Sentinel** e monitorização operacional geral |
| `URL_WEBHOOK_TRILHA_AUDITORIA_DSV` | Canal Trilha de Auditoria — ambiente DSV |
| `URL_WEBHOOK_TRILHA_AUDITORIA_PRD` | Canal Trilha de Auditoria — ambiente PRD |
| `URL_TRILHA_DSV_NOVO` | Webhook alternativo Trilha (DSV) |

### Sentinel vs Trilha

- **Sentinel:** alertas transversais (volume, falha de job, regras operacionais).
- **Trilha de Auditoria:** mensagens com contexto de **motor de regras** / movimentações suspeitas (exemplo com colunas CPF, Sistema, Régua, SCORE).

Escolha a variável **antes** de codificar: não misturar PRD com DSV.

## Carregar a URL no código

### Local (com `python-dotenv`)

```python
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[2] / ".env")  # ajustar níveis

webhook = os.environ["URL_WEBHOOK_SENTINEL"].strip()
assert webhook.startswith("https://"), "URL_WEBHOOK_SENTINEL inválida ou ausente"
```

### Databricks (secret)

```python
webhook = dbutils.secrets.get(scope="varonis", key="url_webhook_sentinel")
```

Mapear o nome do secret com o time de plataforma; o **nome lógico** no código pode espelhar `URL_WEBHOOK_SENTINEL`.

## Segurança

- Tratar cada URL como **credencial** (rotação se vazar).
- Não logar a URL completa em `print` ou tabelas de auditoria públicas.
- Revisar conteúdo das mensagens: **CPF e dados sensíveis** podem exigir mascaramento ou canal restrito (LGPD / política interna).
